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
  # Knowledge sources are local PDFs (no stable download URL). Only the
  # sources/ text is regenerated; SKILL.md, physics.md, methods.md and
  # equations.md are written by hand.
  local pdf="${NEUTRONICS_METHODES_PDF:?set NEUTRONICS_METHODES_PDF=/path/to/La_neutronique_-_Les_methodes_de_la_neutronique.pdf}"
  "$PY" "$ROOT/tools/pdf2md.py" --pdf "$pdf" \
    --out "$ROOT/skills/neutronics/sources/cea-methodes-neutronique" \
    --chapter-sizes 16,18 --section-sizes 11.5 --subsection-sizes 9.5,9.0 \
    --footer-y 770 --page-offset 42
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
  # the SALOME GUI user guide, from the GitHub mirrors of SALOME (sources only).
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
  "$PY" "$ROOT/tools/sphinx_src2md.py" --src "$tmp/gui/doc/salome/gui/input" --pkg-root "$tmp/gui" \
    --out "$ROOT/skills/salome-gui/docs" --source-url "$url/gui/tree/$ref/doc/salome/gui" --version "$vg"
  "$PY" "$ROOT/tools/dox2md.py" --src "$tmp/gui/doc/salome/tui/input" --ext .doc \
    --out "$ROOT/skills/salome-gui/docs/architecture" --source-url "$url/gui/tree/$ref/doc/salome/tui"
  rm -rf "$tmp"
}

# Add new codes here: sync_<name>() { ... } — see README.md.

targets=("$@")
[ ${#targets[@]} -eq 0 ] && targets=(tripoli4 tripoli5 valjean tfel_mfront salome)
for t in "${targets[@]}"; do
  echo "== $t =="
  "sync_$t"
done
