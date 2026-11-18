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

# Add new codes here: sync_<name>() { ... } — see README.md.

targets=("$@")
[ ${#targets[@]} -eq 0 ] && targets=(tripoli4 tripoli5 valjean)
for t in "${targets[@]}"; do
  echo "== $t =="
  "sync_$t"
done
