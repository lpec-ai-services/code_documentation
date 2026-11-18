#!/usr/bin/env bash
# Download and convert the documentation of each code into skills/<code>/docs.
#   ./sync.sh                 # all codes
#   ./sync.sh tripoli4        # one code
#   T5_VERSION=dev ./sync.sh tripoli5   # other T5 version (latest-release, v0.3.0, dev…)
#   T4_FAST=1 ./sync.sh tripoli4        # plain-text extraction (faster, less structure)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="${PYTHON:-python3}"

sync_tripoli4() {
  local url="https://www.cea.fr/energies/tripoli-4/Documents/user_guide_T412_CEA_R_6599_final.pdf"
  "$PY" "$ROOT/tools/pdf2md.py" --url "$url" --out "$ROOT/skills/tripoli4/docs" \
    ${T4_FAST:+--fast}
}

sync_tripoli5() {
  local version="${T5_VERSION:-latest-release}"
  "$PY" "$ROOT/tools/sphinx2md.py" \
    --base "https://tripoli5.asnr.dev/documentation/${version}/" \
    --out "$ROOT/skills/tripoli5/docs"
}

# Add new codes here: sync_<name>() { ... } — see README.md.

targets=("$@")
[ ${#targets[@]} -eq 0 ] && targets=(tripoli4 tripoli5)
for t in "${targets[@]}"; do
  echo "== $t =="
  "sync_$t"
done
