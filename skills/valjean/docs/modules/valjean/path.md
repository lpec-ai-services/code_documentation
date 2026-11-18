<!-- source: modules/valjean/path.rst -->

# `path` — Utilities for accessing the filesystem

Utility functions to access the filesystem.

### `valjean.path.ensure(*paths, is_dir=False)`

Make sure that the given path exists.

param paths  
One or more paths. Multiple arguments will be concatenated into a single path.

type paths  
str or pathlib.Path

param bool is_dir  
If `True`, the path will be constructed as a directory.

### `valjean.path.sanitize_filename(name)`

Check that the `name` string can be used as a filename.

raises ValueError  
if the string contains characters that are forbidden in a filename.

returns  
`name` unchanged
