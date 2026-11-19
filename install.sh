#!/usr/bin/env bash
# Make every skill in this repo available to opencode globally by symlinking
# skills/<name> into ~/.config/opencode/skills/<name>.
#   ./install.sh            # install / refresh links
#   ./install.sh --remove   # remove the links created by this repo
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
DEST="${OPENCODE_SKILLS_DIR:-$HOME/.config/opencode/skills}"
mkdir -p "$DEST"

# links to skills that were renamed or removed in this repo (e.g. salome-gui → salome)
for link in "$DEST"/*; do
  [ -L "$link" ] || continue
  target="$(readlink "$link")"
  case "$target" in "$ROOT"/skills/*) [ -e "$target" ] || { rm "$link"; echo "removed stale $link"; } ;; esac
done

for dir in "$ROOT"/skills/*/; do
  name="$(basename "$dir")"
  link="$DEST/$name"
  if [ "${1:-}" = "--remove" ]; then
    [ -L "$link" ] && rm "$link" && echo "removed $link"
    continue
  fi
  if [ -e "$link" ] && [ ! -L "$link" ]; then
    echo "skip $name: $link exists and is not a symlink" >&2
    continue
  fi
  ln -sfn "${dir%/}" "$link"
  echo "linked $link -> ${dir%/}"
done
