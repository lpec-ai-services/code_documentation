#!/usr/bin/env bash
# Download and convert the documentation of each code into skills/<code>/docs.
#   ./sync.sh                 # all codes
#   ./sync.sh tripoli4        # one code
#   T5_VERSION=dev ./sync.sh tripoli5   # other T5 version (latest-release, v0.3.0, dev…)
#   T4_MARKDOWN=1 ./sync.sh tripoli4    # pymupdf4llm output instead of cleaned text
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="${PYTHON:-python3}"

sync_tripoli4() {
  local url="https://www.cea.fr/energies/tripoli-4/Documents/user_guide_T412_CEA_R_6599_final.pdf"
  "$PY" "$ROOT/tools/pdf2md.py" --url "$url" --out "$ROOT/skills/tripoli4/docs" --front-matter-pages 20 --table-pages 552-562 \
    ${T4_MARKDOWN:+--markdown}
}

sync_tripoli5() {
  local version="${T5_VERSION:-latest-release}"
  "$PY" "$ROOT/tools/sphinx2md.py" \
    --base "https://tripoli5.asnr.dev/documentation/${version}/" \
    --out "$ROOT/skills/tripoli5/docs"
}

sync_valjean() {
  # Static conversion: reads the .rst/.ipynb sources and the docstrings with
  # ast. Nothing from the valjean repo is imported or executed.
  local tmp; tmp="$(mktemp -d)"
  git clone -q --depth 1 https://github.com/valjean-framework/valjean.git "$tmp/valjean"
  local version; version="$(sed -n 's/^version *= *"\(.*\)"/\1/p' "$tmp/valjean/pyproject.toml" | head -1)"
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/valjean/doc/src" --pkg-root "$tmp/valjean" \
    --out "$ROOT/skills/valjean/docs" --exclude tests.rst \
    --source-url https://github.com/valjean-framework/valjean --version "$version"
  rm -rf "$tmp"
}

sync_neutronics() {
  # Knowledge sources are local PDFs (no stable download URL); each is optional.
  # Only sources/ is regenerated; SKILL.md, physics.md, methods.md, technology.md and
  # equations.md are written by hand.
  local out="$ROOT/skills/neutronics/sources" any=""
  if [ -n "${NEUTRONICS_METHODES_PDF:-}" ]; then any=1
    "$PY" "$ROOT/tools/pdf2md.py" --pdf "$NEUTRONICS_METHODES_PDF" --out "$out/cea-methodes-neutronique" \
      --chapter-sizes 16,18 --section-sizes 11.5 --subsection-sizes 9.5,9.0 --footer-y 770 --page-offset 42
  fi
  if [ -n "${NEUTRONICS_STACEY_PDF:-}" ]; then any=1   # Stacey, Nuclear Reactor Physics, 3rd ed. (Wiley-VCH 2018)
    "$PY" "$ROOT/tools/pdf2md.py" --pdf "$NEUTRONICS_STACEY_PDF" --out "$out/stacey-reactor-physics-3e" \
      --chapter-sizes 13 --section-sizes 12.5 --subsection-sizes 10 --header-y 62 --printed-pages \
      --glyph-map "$ROOT/tools/glyphmaps/wiley-stix.json" --max-pages 20
  fi
  if [ -n "${NEUTRONICS_MARGUET_PDF:-}" ]; then any=1  # Marguet, La technologie des REP (EDF 2019)
    "$PY" "$ROOT/tools/pdf2md.py" --pdf "$NEUTRONICS_MARGUET_PDF" --out "$out/marguet-technologie-rep-2019" \
      --chapter-sizes 20.7 --section-sizes 14.3 --subsection-sizes 12 --header-y 55 --printed-pages --max-pages 20
  fi
  [ -n "$any" ] || { echo "set NEUTRONICS_METHODES_PDF, NEUTRONICS_STACEY_PDF and/or NEUTRONICS_MARGUET_PDF" >&2; return 1; }
}

sync_thermal_hydraulics() {
  # Local sources: the publisher's per-chapter PDFs and the IAEA report.
  # SKILL.md, physics.md, methods.md and equations.md are written by hand.
  local book="${TH_BOOK_DIR:?set TH_BOOK_DIR=/path/to/unzipped/thermal_hydraulics_of_water_cooled_nuclear_reactors}"
  local iaea="${TH_IAEA_TRS498_PDF:?set TH_IAEA_TRS498_PDF=/path/to/p15861-DOC-010-498_web.pdf}"
  local out="$ROOT/skills/thermal-hydraulics/sources"
  "$PY" "$ROOT/tools/pdfbook2md.py" --dir "$book" --out "$out/th-water-cooled-reactors-2017" \
    --extra Preface --extra Subject-Index \
    --title "Thermal Hydraulics of Water-Cooled Nuclear Reactors (F. D'Auria ed., Woodhead/Elsevier, 2017)" \
    -- --glyph-map "$ROOT/tools/glyphmaps/elsevier-advp.json" --max-pages 20
  "$PY" "$ROOT/tools/pdf2md.py" --pdf "$iaea" --out "$out/iaea-trs-498-fast-reactors" \
    --chapter-sizes 12.5 --subsection-sizes 10.5 --footer-y 610 --front-matter-pages 8 \
    --heading-regex '2:^\d+\.\d+\.\s+[A-Z][A-Z0-9 ,;:()\-–/&’]+$'
}

sync_tfel_mfront() {
  # Docs are Markdown in the TFEL repo (docs/web); gallery .mfront/.mtest in docs/gallery.
  # TFEL_REF selects a branch or tag (default: master).
  local ref="${TFEL_REF:-master}" tmp; tmp="$(mktemp -d)"
  git clone -q --depth 1 --branch "$ref" --filter=blob:none --sparse \
    https://github.com/thelfer/tfel.git "$tmp/tfel"
  git -C "$tmp/tfel" sparse-checkout set --no-cone '/docs/web/' '/docs/gallery/' '/CMakeLists.txt'
  local v; v="$(sed -n 's/^tfel_project(\([0-9]*\) \([0-9]*\) "\([0-9]*\)").*/\1.\2.\3/p' "$tmp/tfel/CMakeLists.txt")"
  local c; c="$(git -C "$tmp/tfel" log -1 --format='%h, %cs')"
  "$PY" "$ROOT/tools/mdtree2md.py" --src "$tmp/tfel/docs/web" --out "$ROOT/skills/tfel-mfront/docs" \
    --examples "$tmp/tfel/docs/gallery" --examples-glob '*.mfront' --examples-glob '*.mtest' \
    --source-url https://github.com/thelfer/tfel/tree/$ref/docs/web --version "$v ($ref $c)"
  rm -rf "$tmp"
  echo "Update the version line in skills/tfel-mfront/SKILL.md if it changed: $v"
}

sync_manta() {
  # The site is not reachable from everywhere: from a local mirror
  #   wget -m -np -k https://manta-project.gitlab.io/manta/   (Doxygen part can be removed)
  # set MANTA_MIRROR to the folder containing get_started/, theory_manual/, …
  # Without MANTA_MIRROR, fetch the site directly (needs searchindex.js online).
  local base="https://manta-project.gitlab.io/manta/"
  if [ -n "${MANTA_MIRROR:-}" ]; then
    "$PY" "$ROOT/tools/sphinx2md.py" --base "$base" --local "$MANTA_MIRROR" --out "$ROOT/skills/manta/docs"
  else
    "$PY" "$ROOT/tools/sphinx2md.py" --base "$base" --out "$ROOT/skills/manta/docs"
  fi
}

sync_salome() {
  # MEDCoupling (developer guide in Doxygen pages + user guide + tutorial) and
  # the GUI architecture notes, from the GitHub mirrors of SALOME (sources only).
  # The user documentation of every module comes from sync_salome_docs.
  local ref="${SALOME_REF:-master}" tmp; tmp="$(mktemp -d)"
  git clone -q --depth 1 --branch "$ref" --filter=blob:none --sparse \
    https://github.com/SalomePlatform/medcoupling.git "$tmp/mc"
  git -C "$tmp/mc" sparse-checkout set --no-cone '/doc/' \
    '/src/**/MEDCouplingExamplesTest.cxx' '/src/**/MEDCouplingExamplesTest.py' \
    '/src/**/MEDLoaderExamplesTest.py' '/src/**/UsersGuideExamplesTest*.py' \
    '/src/**/TestMEDCouplingIterativeStatistics.py'
  git clone -q --depth 1 --branch "$ref" --filter=blob:none --sparse \
    https://github.com/SalomePlatform/gui.git "$tmp/gui"
  git -C "$tmp/gui" sparse-checkout set --no-cone '/doc/'
  local v; v="$ref ($(git -C "$tmp/mc" log -1 --format='%h, %cs'))"
  local vg; vg="$ref ($(git -C "$tmp/gui" log -1 --format='%h, %cs'))"
  local mc="$ROOT/skills/salome-medcoupling/docs" url=https://github.com/SalomePlatform
  "$PY" "$ROOT/tools/dox2md.py" --src "$tmp/mc/doc/developer/doxygen/doxfiles" --out "$mc/developer" \
    --snippets "$tmp/mc/src" --source-url "$url/medcoupling/tree/$ref/doc/developer" --version "$v"
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/mc/doc/user/input" --pkg-root "$tmp/mc" \
    --out "$mc/user" --source-url "$url/medcoupling/tree/$ref/doc/user" --version "$v"
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/mc/doc/tutorial" --pkg-root "$tmp/mc" \
    --out "$mc/tutorial" --exclude '*_fr.rst' --source-url "$url/medcoupling/tree/$ref/doc/tutorial" --version "$v"
  # GUI architecture notes (developer Doxygen pages; not in the binary docs)
  "$PY" "$ROOT/tools/dox2md.py" --src "$tmp/gui/doc/salome/tui/input" --ext .doc \
    --out "$ROOT/skills/salome/docs/architecture" --source-url "$url/gui/tree/$ref/doc/salome/tui"
  rm -rf "$tmp"
}

sync_salome_docs() {
  # The SALOME user documentation of every module (GUI, SHAPER, GEOM, SMESH and
  # its meshing plug-ins, YACS, HexaBlock, EFICAS, JobManager, HOMARD, ADAO,
  # FIELDS, PARAVIS, samples, developer notes), from the HTML documentation
  # shipped with a SALOME binary install or a wget mirror of
  # docs.salome-platform.org/latest. Point SALOME_DOC_DIR at the folder holding
  # gui/, dev/ and main/ (…/BINARIES-*/DOCUMENTATION/share/doc/salome).
  # SALOME_VERSION is recorded in the INDEX (default: read from the path).
  local d="${SALOME_DOC_DIR:?set SALOME_DOC_DIR to the folder holding gui/ dev/ main/}"
  local v="${SALOME_VERSION:-$(grep -o 'SALOME-[0-9][0-9.]*[0-9]' <<<"$d" | head -1)}"
  local out="$ROOT/skills/salome/docs" site=https://docs.salome-platform.org/latest
  local m
  for m in GUI SHAPER GEOM SMESH YACS HEXABLOCK EFICAS JOBMANAGER NETGENPLUGIN BLSURFPLUGIN \
           GHS3DPLUGIN HexoticPLUGIN HYBRIDPLUGIN GMSHPLUGIN HELLO PYHELLO HOMARD/en ADAO/en; do
    [ -d "$d/gui/$m" ] || { echo "  missing gui/$m"; continue; }
    "$PY" "$ROOT/tools/sphinx2md.py" --base "$site/gui/$m/" --local "$d/gui/$m" \
      --out "$out/${m%/en}" --code-lang python >/dev/null
  done
  for m in FIELDS PARAVIS cmake/html git/html; do
    [ -d "$d/dev/$m" ] || { echo "  missing dev/$m"; continue; }
    "$PY" "$ROOT/tools/sphinx2md.py" --base "$site/dev/$m/" --local "$d/dev/$m" \
      --out "$out/dev/${m%/html}" --exclude 'api/*' --exclude 'fr/*' --code-lang python >/dev/null
  done
  "$PY" "$ROOT/tools/sphinx2md.py" --base "$site/main/" --local "$d/main" --out "$out/main" >/dev/null
  "$PY" "$ROOT/tools/salome_index.py" --docs "$out" --version "$v"
}

sync_scivianna() {
  # Docs, tutorials, AGENTS.md and examples from the GitHub repo (no code is run;
  # the API is read statically from the sources). SCIVIANNA_REF: branch or tag.
  local ref="${SCIVIANNA_REF:-}" tmp; tmp="$(mktemp -d)"
  git clone -q --depth 1 ${ref:+--branch "$ref"} https://github.com/cea-code-coupling/scivianna.git "$tmp/s"
  ref="$(git -C "$tmp/s" rev-parse --abbrev-ref HEAD)"
  local v; v="$(cat "$tmp/s/src/scivianna/VERSION" 2>/dev/null) ($ref $(git -C "$tmp/s" log -1 --format='%h, %cs'))"
  local out="$ROOT/skills/scivianna" url=https://github.com/cea-code-coupling/scivianna
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/s/docs/source" --pkg-root "$tmp/s/src" \
    --out "$out/docs" --exclude 'tutorials/*' --source-url "$url" --version "$v"
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/s/tutorials" --pkg-root "$tmp/s/src" \
    --out "$out/docs/tutorials" --source-url "$url/tree/$ref/tutorials" --version "$v"
  cp "$tmp/s/AGENTS.md" "$tmp/s/readme.md" "$out/docs/"
  cp "$tmp/s/src/scivianna/agent/instructions.md" "$out/docs/agent_instructions.md"
  rm -rf "$out/examples" && mkdir -p "$out/examples"
  (cd "$tmp/s/src/scivianna_example" && find . \( -name '*.md' -o -name '*.py' \) -exec cp --parents {} "$out/examples/" \;)
  rm -rf "$tmp"
  echo "Update the version line in skills/scivianna/SKILL.md if it changed: $v"
}

sync_vtk() {
  # 1. VTK user documentation (Documentation/docs in the VTK repo)
  # 2. examples.vtk.org Python examples, Pythonic API examples and the VTK Textbook,
  #    from the published site (gh-pages branch of the GitHub mirror; ~450 MB of
  #    HTML is fetched, images skipped). Conversion takes several minutes.
  local tmp; tmp="$(mktemp -d)"
  git clone -q --depth 1 --filter=blob:none --sparse https://github.com/Kitware/VTK.git "$tmp/vtk"
  git -C "$tmp/vtk" sparse-checkout set --no-cone '/Documentation/docs/'
  local v; v="master ($(git -C "$tmp/vtk" log -1 --format='%h, %cs'))"
  "$PY" "$ROOT/tools/mdtree2md.py" --src "$tmp/vtk/Documentation/docs" --out "$ROOT/skills/vtk/docs/user" \
    --source-url https://github.com/Kitware/VTK/tree/master/Documentation/docs --version "$v"
  git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/Kitware/vtk-examples.git "$tmp/ex"
  git -C "$tmp/ex" sparse-checkout init --no-cone
  printf '%s\n' '/site/Python/' '/site/PythonicAPI/' '/site/PythonHowTo/' '/site/PythonicAPIComments/' \
    '/site/VTKBook/' '!/site/**/*.png' '!/site/**/*.jpg' '!/site/**/*.gif' '!/site/**/*.vtp' '!/site/**/*.vtk' \
    > "$tmp/ex/.git/info/sparse-checkout"
  git -C "$tmp/ex" checkout -q
  local ve; ve="vtk-examples gh-pages ($(git -C "$tmp/ex" log -1 --format='%h, %cs'))"
  "$PY" "$ROOT/tools/sphinx2md.py" --base https://examples.vtk.org/site/ --local "$tmp/ex/site" \
    --out "$ROOT/skills/vtk/docs/site" --dir-urls --code-lang python
  "$PY" - "$ROOT/skills/vtk/docs/site/_meta.json" "$ve" <<'PYEOF'
import json, sys
m = json.load(open(sys.argv[1])); m["version"] = sys.argv[2]
json.dump(m, open(sys.argv[1], "w"), indent=2)
PYEOF
  rm -rf "$tmp"
}

sync_uranie() {
  # From the local PDF of the Uranie UserManual Python (no stable download URL).
  # SKILL.md is written by hand.
  local pdf="${URANIE_MANUAL_PDF:?set URANIE_MANUAL_PDF=/path/to/userManual_Py.pdf}"
  "$PY" "$ROOT/tools/pdf2md.py" --pdf "$pdf" --out "$ROOT/skills/uranie/docs" \
    --code-fonts Mono --code-lang python --footer-y 730 --max-pages 20 \
    --drop-regex '^\((continued from previous page|continues on next page)\)$|^CHAPTER$|^(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|THIRTEEN|FOURTEEN|FIFTEEN)$'
}

sync_icoco() {
  # The norm's documentation is its header comments (converted without Doxygen).
  local tmp; tmp="$(mktemp -d)"
  git clone -q --depth 1 https://github.com/cea-trust-platform/icoco-coupling.git "$tmp/i"
  local out="$ROOT/skills/icoco/docs"
  "$PY" "$ROOT/tools/cppdoc2md.py" --src "$tmp/i/include" --out "$out/api" --glob '*.hxx' \
    --source-url https://github.com/cea-trust-platform/icoco-coupling \
    --version "2.0 ($(git -C "$tmp/i" rev-parse --abbrev-ref HEAD) $(git -C "$tmp/i" log -1 --format='%h, %cs'))"
  cp "$tmp/i/README.md" "$out/README.md"
  mkdir -p "$out/swig" && cp "$tmp/i/swig/"*.i "$out/swig/"
  # Python implementation (pip package icoco)
  git clone -q --depth 1 https://github.com/cea-trust-platform/icoco-coupling-python.git "$tmp/p"
  local vp; vp="$(cat "$tmp/p/src/icoco/VERSION") ($(git -C "$tmp/p" rev-parse --abbrev-ref HEAD) $(git -C "$tmp/p" log -1 --format='%h, %cs'))"
  rm -rf "$out/python"
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/p/docs/sphinx" --pkg-root "$tmp/p/src" --out "$out/python" \
    --source-url https://github.com/cea-trust-platform/icoco-coupling-python --version "$vp"
  cp "$tmp/p/README.md" "$out/python/README.md"
  mkdir -p "$out/python/tests" && cp "$tmp/p/tests/"*.py "$tmp/p/tests/README.md" "$out/python/tests/"
  rm -rf "$tmp"
}

sync_c3po() {
  # Docs + API for every module (read statically) + the tests as examples. C3PO_REF: branch/tag.
  local ref="${C3PO_REF:-}" tmp; tmp="$(mktemp -d)"
  git clone -q --depth 1 ${ref:+--branch "$ref"} https://github.com/cea-code-coupling/c3po.git "$tmp/c"
  ref="$(git -C "$tmp/c" rev-parse --abbrev-ref HEAD)"
  local v; v="$(cat "$tmp/c/sources/c3po/VERSION") ($ref $(git -C "$tmp/c" log -1 --format='%h, %cs'))"
  local out="$ROOT/skills/c3po"
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/c/doc/source" --pkg-root "$tmp/c/sources" \
    --out "$out/docs" --api-package c3po --source-url https://github.com/cea-code-coupling/c3po --version "$v"
  rm -rf "$out/examples" && mkdir -p "$out/examples"
  (cd "$tmp/c/tests" && find . \( -name '*.py' -o -name 'README.md' \) -exec cp --parents {} "$out/examples/" \;)
  rm -rf "$tmp"
  echo "Update the version line in skills/c3po/SKILL.md if it changed: $v"
}

# Add new codes here: sync_<name>() { ... } — see README.md.

targets=("$@")
[ ${#targets[@]} -eq 0 ] && targets=(tripoli4 tripoli5 valjean tfel_mfront salome scivianna vtk icoco c3po)
for t in "${targets[@]}"; do
  echo "== $t =="
  "sync_$t"
done
