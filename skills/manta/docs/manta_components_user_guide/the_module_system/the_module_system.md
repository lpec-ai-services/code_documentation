<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/the_module_system/the_module_system.html -->

# The "module" system

MANTA source code is structured into *modules*. A *module* is a
portion of the source code which provides a given functionality and some related
tests. It may be enabled or not. Enabling a *module* makes its
functionality and tests available to the user, but triggers its compilation and
the compilation/requirement of its external thirdparties. A *module* may
depend on other *modules*. In this case, enabling the *module*
automatically enable the *modules* which it depends on, and recursively.

The *modules* are stored into "groups". The full name of a module is `manta::<group_name>-<module_name>`.

Warning

The `-` character is used as a separator between the name of the *group*
and the name of the *module* in this group. This `-` character should not
be used in the terminal name of the module. Use `_` as a separator between words
in the terminal name of a *module*.

The root directory of a given module to use in `#include` directives
follows the same convention, except that a `/` is to be used instead of `::`.
For example, the header `baz.h` located in the directory `qux/` from the module
`manta::foo_group-bar_module` must be included as `#include "manta/foo_group-bar_module/qux/baz.h"`.

Contents

- [Available modules](available_modules.md)
- [Enabling/disabling modules](enabling_disabling_modules.md)
- [How to create a new "module"](how_to_create_a_new_module.md)
