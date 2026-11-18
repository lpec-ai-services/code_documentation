<!-- source: modules/valjean/dyn_import.rst -->

# `dyn_import` — Utilities for dynamically importing Python modules

This module contains somme common utility functions for dynamically importing Python source files as modules.

### `valjean.dyn_import.split_module_path(file_name)`

Split a path to a Python module into a path and a module name.

param path  
A path to a Python file.

type path  
str or `path-like object`

returns  
a `(path, name)` tuple.

### `valjean.dyn_import.dyn_import(file_name)`

Load a Python module from the given file name.

Note that this function adds the path to `file_name` to `sys.path`, so that local imports in `file_name` work as expected.

param str file_name  
the name of the file containing the module.

returns  
the loaded module.
