#!/usr/bin/env python3
"""Harvest HAL (hal.science) metadata and open-access PDFs, incrementally.

Uses the public HAL search API (Solr, https://api.archives-ouvertes.fr/docs/search)
paging by document id, so it scales to the whole archive. Everything is
recorded in a SQLite catalogue, so runs can be interrupted and resumed, and
later runs only fetch what was added or modified since the previous one.

Subcommands
  count   how many records match (and how many have an open-access file); nothing saved
  run     harvest metadata, then download the PDFs that are missing or have a new version
  stats   what the catalogue contains
  export  write the catalogue as JSON Lines (one record per line, with the PDF path)

Examples
  # what would a full harvest represent?
  python3 tools/hal_harvest.py count --since 1900-01-01
  python3 tools/hal_harvest.py count --since 1900-01-01 --with-file

  # first run: everything modified since a date (here: all of HAL with a PDF)
  python3 tools/hal_harvest.py run --out ~/hal --since 1900-01-01 --with-file --mailto you@lab.fr

  # later: only what changed since the last complete run (the same command works too)
  python3 tools/hal_harvest.py run --out ~/hal --with-file --mailto you@lab.fr

  # in batches: each invocation does ~5000 records and the next one continues
  python3 tools/hal_harvest.py run --out ~/hal --since 1900-01-01 --with-file --max-docs 5000

  # narrower scopes (all filters combine)
  python3 tools/hal_harvest.py run --out ~/hal-cea --portal cea --since 2015-01-01 --with-file
  python3 tools/hal_harvest.py run --out ~/hal-nucl --domain phys.nucl --domain spi.nrj \\
      --type ART --type THESE --type REPORT --since 2000-01-01 --with-file
  python3 tools/hal_harvest.py run --out ~/hal --query 'title_t:"thermal hydraulics"' --since 2010-01-01

Layout of --out
  hal.sqlite              catalogue (records, runs)
  pdf/NNN/<halId>vV.pdf   open-access main files, sharded by docid % 1000

Notes
  * The date filter uses modifiedDate_tdate by default, so new versions and
    corrections are picked up on update runs. Use --date-field
    submittedDate_tdate for "new deposits only".
  * Each update run starts one day before the previous run's start time
    (--overlap-days) so nothing is lost at the boundary; duplicates are merged.
  * Only files flagged open access are downloaded (embargoed files are skipped
    and retried on later runs when their embargo ends and the record changes).
  * Be polite: keep --workers low and pass --mailto so HAL can contact you.
    Licences vary per document (field licence_s); check them before
    redistributing anything.

Requires: pip install requests
"""
import argparse
import datetime as dt
import json
import sqlite3
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API = "https://api.archives-ouvertes.fr/search/"
FIELDS = [
    "docid", "halId_s", "version_i", "uri_s", "doiId_s", "docType_s", "title_s",
    "subTitle_s", "authFullName_s", "structName_s", "producedDate_tdate",
    "publicationDate_tdate", "submittedDate_tdate", "modifiedDate_tdate",
    "language_s", "domainAllCode_s", "keyword_s", "abstract_s", "journalTitle_s",
    "conferenceTitle_s", "collCode_s", "licence_s", "openAccess_bool",
    "fileMain_s", "files_s",
]
SCHEMA = """
CREATE TABLE IF NOT EXISTS records (
  halid TEXT PRIMARY KEY, docid INTEGER, version INTEGER, doctype TEXT,
  title TEXT, year INTEGER, modified TEXT, file_url TEXT, licence TEXT,
  json TEXT, pdf_path TEXT, pdf_version INTEGER, pdf_status TEXT, pdf_bytes INTEGER,
  seen_run INTEGER);
CREATE INDEX IF NOT EXISTS records_pdf_status ON records(pdf_status);
CREATE TABLE IF NOT EXISTS runs (
  id INTEGER PRIMARY KEY, started TEXT, finished TEXT, since TEXT, until TEXT,
  scope TEXT, found INTEGER, new INTEGER, updated INTEGER,
  downloaded INTEGER, failed INTEGER, complete INTEGER DEFAULT 0);
"""


# ----------------------------------------------------------------- helpers

def now_utc():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso(d):
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_date(s):
    d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


class Throttle:
    """At most one request every `interval` seconds, across threads."""

    def __init__(self, interval):
        self.interval, self.lock, self.last = interval, threading.Lock(), 0.0

    def wait(self):
        with self.lock:
            delay = self.last + self.interval - time.monotonic()
            if delay > 0:
                time.sleep(delay)
            self.last = time.monotonic()


def make_session(mailto):
    s = requests.Session()
    ua = "code-documentation-hal-harvester/1.0 (+https://github.com/lpec-ai-services/code_documentation"
    s.headers["User-Agent"] = ua + (f"; mailto:{mailto})" if mailto else ")")
    retry = Retry(total=6, backoff_factor=2, status_forcelist=(429, 500, 502, 503, 504),
                  allowed_methods=("GET",), respect_retry_after_header=True)
    s.mount("https://", HTTPAdapter(max_retries=retry, pool_maxsize=16))
    s.mount("http://", HTTPAdapter(max_retries=retry, pool_maxsize=16))
    return s


def or_clause(field, values, quote=True):
    vals = " OR ".join(f'"{v}"' if quote else v for v in values)
    return f"{field}:({vals})"


def build_filters(a, since, until):
    fq = [f"{a.date_field}:[{iso(since)} TO {iso(until)}]"]
    if a.type:
        fq.append(or_clause("docType_s", a.type))
    if a.domain:
        fq.append(or_clause("domainAllCode_s", a.domain))
    if a.collection:
        fq.append(or_clause("collCode_s", a.collection))
    if a.lang:
        fq.append(or_clause("language_s", a.lang))
    if a.with_file:
        fq.append("openAccess_bool:true")
        fq.append("fileMain_s:*")
    fq.extend(a.fq)
    return fq


def endpoint(a):
    base = a.api if a.api.endswith("/") else a.api + "/"
    return base + (a.portal.strip("/") + "/" if a.portal else "")


def scope_text(a):
    parts = [f"portal={a.portal or 'all'}", f"q={a.query}", f"date={a.date_field}"]
    for name in ("type", "domain", "collection", "lang", "fq"):
        if getattr(a, name):
            parts.append(f"{name}={','.join(getattr(a, name))}")
    if a.with_file:
        parts.append("with_file")
    return "; ".join(parts)


def search(session, throttle, a, fq, rows, after=None):
    """One page of results sorted by docid, starting after docid `after`.

    Paging by docid range (keyset) instead of Solr cursors: it needs no
    server-side state, never skips or repeats a record, and lets a run
    resume from the last docid it saved.
    """
    params = [("q", a.query), ("fl", ",".join(FIELDS)), ("rows", rows),
              ("sort", "docid asc"), ("wt", "json")]
    params += [("fq", f) for f in fq]
    if after is not None:
        params.append(("fq", f"docid:{{{int(after)} TO *]"))
    throttle.wait()
    r = session.get(endpoint(a), params=params, timeout=120)
    r.raise_for_status()
    return r.json()


# ----------------------------------------------------------------- catalogue

def open_db(out):
    out.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(out / "hal.sqlite")
    db.executescript(SCHEMA)
    cols = {r[1] for r in db.execute("PRAGMA table_info(runs)")}
    for col in ("last_docid INTEGER", "processed INTEGER DEFAULT 0"):
        if col.split()[0] not in cols:  # catalogues made by earlier versions
            db.execute(f"ALTER TABLE runs ADD COLUMN {col}")
    db.commit()
    return db


def upsert(db, doc, run_id):
    """Insert or update a record. Returns 'new', 'updated' or 'same'."""
    halid, version = doc.get("halId_s"), int(doc.get("version_i") or 1)
    if not halid:
        return "same"
    year = (doc.get("producedDate_tdate") or "")[:4]
    title = (doc.get("title_s") or [""])[0]
    file_url = doc.get("fileMain_s") if doc.get("openAccess_bool", True) else None
    licence = doc.get("licence_s")
    row = db.execute("SELECT version, pdf_version, pdf_status FROM records WHERE halid=?",
                     (halid,)).fetchone()
    status = "pending" if file_url else "no_file"
    if row:
        old_version, pdf_version, old_status = row
        if file_url and version == old_version and old_status not in (None, "pending", "no_file"):
            status = old_status  # same version: keep ok / failed (retry with --retry-failed)
        db.execute("""UPDATE records SET docid=?, version=?, doctype=?, title=?, year=?,
                      modified=?, file_url=?, licence=?, json=?, pdf_status=?, seen_run=?
                      WHERE halid=?""",
                   (doc.get("docid"), version, doc.get("docType_s"), title,
                    int(year) if year.isdigit() else None, doc.get("modifiedDate_tdate"),
                    file_url, licence, json.dumps(doc, ensure_ascii=False), status,
                    run_id, halid))
        return "updated" if version != old_version or status != old_status else "same"
    db.execute("""INSERT INTO records (halid, docid, version, doctype, title, year, modified,
                  file_url, licence, json, pdf_status, seen_run)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
               (halid, doc.get("docid"), version, doc.get("docType_s"), title,
                int(year) if year.isdigit() else None, doc.get("modifiedDate_tdate"),
                file_url, licence, json.dumps(doc, ensure_ascii=False), status, run_id))
    return "new"


# ----------------------------------------------------------------- downloads

def pdf_target(out, halid, docid, version):
    return out / "pdf" / f"{int(docid or 0) % 1000:03d}" / f"{halid}v{version}.pdf"


def download(session, throttle, out, rec, max_mb):
    halid, docid, version, url = rec
    dest = pdf_target(out, halid, docid, version)
    if dest.exists() and dest.stat().st_size > 0:
        return halid, version, "ok", str(dest.relative_to(out)), dest.stat().st_size
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_suffix(".part")
    try:
        throttle.wait()
        with session.get(url, stream=True, timeout=(30, 300), allow_redirects=True) as r:
            if r.status_code != 200:
                return halid, version, f"http_{r.status_code}", None, None
            size, first = 0, True
            with open(part, "wb") as f:
                for chunk in r.iter_content(1 << 16):
                    if first:
                        if not chunk.lstrip()[:5].startswith(b"%PDF"):
                            raise ValueError("not_pdf")
                        first = False
                    size += len(chunk)
                    if max_mb and size > max_mb * 1e6:
                        raise ValueError("too_large")
                    f.write(chunk)
        part.replace(dest)
        return halid, version, "ok", str(dest.relative_to(out)), size
    except ValueError as e:
        part.unlink(missing_ok=True)
        return halid, version, str(e), None, None
    except requests.RequestException as e:
        part.unlink(missing_ok=True)
        return halid, version, f"error:{type(e).__name__}", None, None


def download_pending(db, session, throttle, a, out, limit=None, retry_failed=False):
    statuses = ("pending",) + (("error", "http_") if retry_failed else ())
    where = " OR ".join(["pdf_status=?"] + ["pdf_status LIKE ?"] * (len(statuses) - 1))
    args = [statuses[0]] + [s + "%" for s in statuses[1:]]
    sql = f"SELECT halid, docid, version, file_url FROM records WHERE ({where}) " \
          "AND file_url IS NOT NULL ORDER BY docid"
    if limit:
        sql += f" LIMIT {int(limit)}"
    todo = db.execute(sql, args).fetchall()
    ok = failed = 0
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        for i, (halid, version, status, path, size) in enumerate(
                pool.map(lambda r: download(session, throttle, out, r, a.max_mb), todo), 1):
            db.execute("UPDATE records SET pdf_status=?, pdf_path=?, pdf_version=?, pdf_bytes=? "
                       "WHERE halid=?", (status, path, version if status == "ok" else None,
                                         size, halid))
            ok += status == "ok"
            failed += status != "ok"
            if i % 100 == 0:
                db.commit()
                print(f"    downloads: {i}/{len(todo)} (ok {ok}, failed {failed})", flush=True)
    db.commit()
    return ok, failed


# ----------------------------------------------------------------- commands

def plan_run(db, a):
    """Resume the last run with this scope if it is incomplete, else start a new one.

    Returns (run_id or None, since, until, last_docid, processed).
    """
    scope = scope_text(a)
    last = db.execute("SELECT id, since, until, complete, last_docid, processed FROM runs "
                      "WHERE scope=? ORDER BY id DESC LIMIT 1", (scope,)).fetchone()
    if last and not last[3] and not a.restart:
        rid, since, until, _, last_docid, processed = last
        if not a.since or iso(parse_date(a.since)) == since:
            return rid, parse_date(since), parse_date(until), last_docid, processed or 0
    until = parse_date(a.until) if a.until else now_utc()
    done = db.execute("SELECT until, since FROM runs WHERE complete=1 AND scope=? "
                      "ORDER BY id DESC LIMIT 1", (scope,)).fetchone()
    if a.since and not a.restart and a.until is None and done:
        first = db.execute("SELECT MIN(since) FROM runs WHERE complete=1 AND scope=?",
                           (scope,)).fetchone()[0]
        if parse_date(first) <= parse_date(a.since):
            # this scope was already harvested from that date: just catch up
            print(f"Already harvested from {first[:10]} with this scope: fetching only what changed "
                  f"since the last complete run (use --restart to redo everything).")
            return None, parse_date(done[0]) - dt.timedelta(days=a.overlap_days), until, None, 0
    if a.since:
        return None, parse_date(a.since), until, None, 0
    if not done:
        sys.exit("No previous complete run with this scope: pass --since YYYY-MM-DD.")
    return None, parse_date(done[0]) - dt.timedelta(days=a.overlap_days), until, None, 0


def cmd_count(a):
    session, throttle = make_session(a.mailto), Throttle(a.interval)
    since = parse_date(a.since or "1900-01-01")
    until = parse_date(a.until) if a.until else now_utc()
    res = search(session, throttle, a, build_filters(a, since, until), rows=0)
    n = res["response"]["numFound"]
    print(f"{n:,} records match ({scope_text(a)}; {iso(since)} → {iso(until)})")
    if not a.with_file:
        a.with_file = True
        m = search(session, throttle, a, build_filters(a, since, until), rows=0)["response"]["numFound"]
        print(f"{m:,} of them have an open-access main file "
              f"(rough size at 2–5 MB per PDF: {m * 2 / 1e6:.1f}–{m * 5 / 1e6:.1f} TB)")


def cmd_run(a):
    out = Path(a.out).expanduser()
    db = open_db(out)
    session, throttle = make_session(a.mailto), Throttle(a.interval)
    run_id, since, until, last_docid, processed = plan_run(db, a)
    fq = build_filters(a, since, until)
    if run_id is None:
        run_id = db.execute("INSERT INTO runs (started, since, until, scope) VALUES (?,?,?,?)",
                            (iso(now_utc()), iso(since), iso(until), scope_text(a))).lastrowid
        db.commit()
        print(f"Run {run_id} (new): {scope_text(a)}")
    else:
        print(f"Run {run_id} (resumed after docid {last_docid}, {processed:,} records already done): "
              f"{scope_text(a)}")
    print(f"  {a.date_field} from {iso(since)} to {iso(until)}")

    counts, this_run = {"new": 0, "updated": 0, "same": 0}, 0
    downloaded = failed = 0
    complete = False
    while True:
        res = search(session, throttle, a, fq, rows=a.rows, after=last_docid)
        remaining = res["response"]["numFound"]
        docs = res["response"]["docs"]
        if not docs:
            complete = True
            break
        for doc in docs:
            counts[upsert(db, doc, run_id)] += 1
        last_docid = docs[-1]["docid"]
        processed += len(docs)
        this_run += len(docs)
        db.execute("UPDATE runs SET last_docid=?, processed=? WHERE id=?",
                   (last_docid, processed, run_id))
        db.commit()  # progress saved after every page: an interrupted run resumes here
        print(f"  metadata: {processed:,} done, {remaining - len(docs):,} to go "
              f"(this run: new {counts['new']:,}, updated {counts['updated']:,})", flush=True)
        if not a.no_pdf:
            ok, ko = download_pending(db, session, throttle, a, out)
            downloaded, failed = downloaded + ok, failed + ko
        if len(docs) >= remaining:
            complete = True
            break
        if a.max_docs and this_run >= a.max_docs:
            break

    if not a.no_pdf:  # leftovers from earlier interrupted runs, and optional retries
        ok, ko = download_pending(db, session, throttle, a, out, retry_failed=a.retry_failed)
        downloaded, failed = downloaded + ok, failed + ko
    db.execute("UPDATE runs SET finished=?, found=?, new=COALESCE(new,0)+?, updated=COALESCE(updated,0)+?, "
               "downloaded=COALESCE(downloaded,0)+?, failed=COALESCE(failed,0)+?, complete=? WHERE id=?",
               (iso(now_utc()), processed, counts["new"], counts["updated"], downloaded, failed,
                int(complete), run_id))
    db.commit()
    print(f"This run: {counts['new']:,} new, {counts['updated']:,} updated, "
          f"{downloaded:,} PDFs downloaded, {failed:,} failed. Total processed: {processed:,}.")
    print("Harvest complete for this scope." if complete else
          "Stopped before the end (--max-docs): run the same command again to continue.")


def cmd_stats(a):
    db = open_db(Path(a.out).expanduser())
    total = db.execute("SELECT COUNT(*) FROM records").fetchone()[0]
    print(f"{total:,} records")
    for status, n, b in db.execute("SELECT pdf_status, COUNT(*), SUM(pdf_bytes) FROM records "
                                   "GROUP BY pdf_status ORDER BY 2 DESC"):
        print(f"  pdf {status or '?':<14} {n:>10,}" + (f"  {b / 1e9:,.1f} GB" if b else ""))
    print("By type:")
    for t, n in db.execute("SELECT doctype, COUNT(*) FROM records GROUP BY 1 ORDER BY 2 DESC LIMIT 12"):
        print(f"  {t or '?':<10} {n:>10,}")
    print("Runs:")
    for r in db.execute("SELECT id, started, since, until, found, new, updated, downloaded, failed, "
                        "complete, scope FROM runs ORDER BY id DESC LIMIT 10"):
        print(f"  #{r[0]} {r[1]} since {r[2]} → {r[3]}: found {r[4]}, new {r[5]}, upd {r[6]}, "
              f"pdf ok {r[7]}, failed {r[8]}, {'complete' if r[9] else 'INCOMPLETE'} [{r[10]}]")


def cmd_export(a):
    out = Path(a.out).expanduser()
    db = open_db(out)
    dest = Path(a.file).expanduser() if a.file else out / "catalogue.jsonl"
    n = 0
    with open(dest, "w", encoding="utf-8") as f:
        for js, path, status in db.execute("SELECT json, pdf_path, pdf_status FROM records ORDER BY docid"):
            rec = json.loads(js)
            rec["_pdf_path"], rec["_pdf_status"] = path, status
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    print(f"{n:,} records → {dest}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def scope(p):
        p.add_argument("--since", help="start date (YYYY-MM-DD or ISO). Default for 'run': "
                                       "end of the previous complete run with the same scope")
        p.add_argument("--until", help="end date (default: now)")
        p.add_argument("--date-field", default="modifiedDate_tdate",
                       help="modifiedDate_tdate (default) or submittedDate_tdate, producedDate_tdate")
        p.add_argument("--portal", default="", help="HAL portal, e.g. cea (= cea.hal.science)")
        p.add_argument("--query", default="*:*", help="Solr query, e.g. 'text:neutronics'")
        p.add_argument("--type", action="append", default=[], help="docType_s: ART, COMM, THESE, "
                                                                   "REPORT, OUV, COUV, HDR, ...")
        p.add_argument("--domain", action="append", default=[],
                       help="domainAllCode_s, e.g. phys.nucl, spi.meca, spi.nrj, phys.cond")
        p.add_argument("--collection", action="append", default=[], help="collCode_s")
        p.add_argument("--lang", action="append", default=[], help="language_s, e.g. en, fr")
        p.add_argument("--with-file", action="store_true",
                       help="only records with an open-access main file")
        p.add_argument("--fq", action="append", default=[], help="extra raw Solr filter query")
        p.add_argument("--mailto", default="", help="contact e-mail sent in the User-Agent")
        p.add_argument("--interval", type=float, default=0.5,
                       help="minimum seconds between requests, all threads together")
        p.add_argument("--api", default=API, help=argparse.SUPPRESS)

    p = sub.add_parser("count", help="count matching records")
    scope(p)
    p.set_defaults(func=cmd_count)

    p = sub.add_parser("run", help="harvest metadata and PDFs")
    scope(p)
    p.add_argument("--out", required=True, help="output folder (catalogue + pdf/)")
    p.add_argument("--rows", type=int, default=500,
                   help="records per API request (page size, max 10000); the run continues "
                        "page after page until everything is harvested")
    p.add_argument("--workers", type=int, default=2, help="parallel downloads")
    p.add_argument("--max-mb", type=float, default=200, help="skip PDFs larger than this")
    p.add_argument("--no-pdf", action="store_true", help="metadata only")
    p.add_argument("--retry-failed", action="store_true", help="retry earlier failed downloads")
    p.add_argument("--overlap-days", type=float, default=1.0)
    p.add_argument("--max-docs", type=int, default=0,
                   help="stop this run after about N records; the same command continues later")
    p.add_argument("--restart", action="store_true",
                   help="start a new run even if the last one with this scope is unfinished")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("stats", help="catalogue summary")
    p.add_argument("--out", required=True)
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("export", help="catalogue as JSON Lines")
    p.add_argument("--out", required=True)
    p.add_argument("--file", help="destination (default: OUT/catalogue.jsonl)")
    p.set_defaults(func=cmd_export)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
