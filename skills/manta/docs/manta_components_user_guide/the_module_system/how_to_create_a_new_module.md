<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/the_module_system/how_to_create_a_new_module.html -->

# How to create a new "module"

For specifics related to private modules, see following section about [private modules](#id1).

## Create the files structure

The script `${REPOSITORY_ROOT}/refactor/create_module.py` automatically create the files for a new *module*.

The command `${REPOSITORY_ROOT}/refactor/create_module.py -g <group_name> -m
<module_name>` creates a template module structure. This script must be called
from the root of the MANTA repository::

```
groupname
└── foo
    ├── CMakeLists.txt
    ├── config.cmake
    ├── manta.module
    ├── manta
    │   └── groupname-foo
    │       ├── config.h
    │       └── decl
    ├── tests
    └── thirdparties.cmake
```

At least the file `manta.module` must be edited to add a valid description of
the new *module*. It is likely that the file `CMakeLists.txt` would have to be
edited also to handle specific compilation requirements of the new *module*.

If the new module requires a 3rd party to be handled by `spack`, the file
`thirdparties.cmake` must be used. This file will be executed if the module is
actually enabled. It aims at containing some
`manta_module_add_spack_spec("<a_spec>")` instructions.

`CMakeLists.txt`
:   Contains CMake instructions to build and test the module.

    It is created empty, and must be filled in.

`config.cmake`
:   Contains CMake instructions to be exported for downstream projects. Its content will be
    included in the file `<INSTALL_DIR>/share/manta/cmake/manta/<group_name>-<module_name>Config.cmake`
    (which is automatically included by `<INSTALL_DIR>/share/manta/cmake/manta/mantaConfig.cmake`).

    It is created empty, and may be filled in if required, or left empty.

`manta.module`
:   Defines the name of the created module, a description of what it is meant to
    be, and its dependencies to other modules. Here is an example:

    ```
    NAME
      manta::frontend-foo
    DESCRIPTION
      Provides the "foo" wonderful functionnality
    DEPENDS
      manta::components-system manta::frontend-bar
    TEST_DEPENDS
      manta-components::baz
    ```

    In this example, the created module `foo` in the group `frontend` has the
    name `manta::frontend-foo` in the CMake's machinery (it must be of the form
    `manta::<group_name>-<module_name>`).

    Warning

    The `-` character must not be used in either the `<group_name>` or the
    `<module_name>`.

    Warning

    At least one source file `.cpp` must be included in the private module repository. Otherwise, CMake will throw a warning saying that the module has no source files. This will lead later in the compilation to an error because CMake will not be able to detect the programming language.

    What is in the `DESCRIPTION` section will be used to automatically generate a
    page in the documentation describing the available modules.

    The created module `frontend-foo` requires the modules
    `manta::components-system` and `manta::frontend-bar` to construct the
    library `libmanta-frontend-foo.so`, and requires extra dependencies to run
    its associated tests: the module `manta::components-baz`.

    Its content is created as a draft, but must be edited.

`manta/frontend-foo/config.h`
:   Contains the preprocessing macro `MANTA_FRONTEND_FOO_VISIBILITY_EXPORT`.

    Its content is created automatically, and should *a priori* not be edited.

`tests/`
:   The tests of the module must be located in this directory.

`thirdparties.cmake`
:   Contains the spack specs for the external dependencies of the module. This
    file contains CMake instructions that will be executed only if the module is
    actually enabled. In the end it aims at containing some
    `manta_module_add_spack_spec("<a_spec>")` instructions.

## Writing the `CMakeLists.txt` file for a new module

Here is an example of a typical `CMakeLists.txt` for a module foo, with
explanations in comments:

```cmake
set(module_name "manta::frontend-foo")

# This is the first `manta_module_xxx` instruction to call.
manta_module_add_module(${module_name})

# This add some preprocessing definitions when building the module.
# Works exactly as CMake's `add_definitions`.
manta_module_definitions(${module_name} PUBLIC TFEL_ARCH64)

# In the following set of instructions, one makes the connection with the external library "bar".
# This assumes that a "spack spec" for "bar" is added in the `thirdparties.cmake` file.
# First one gets the installation directory of the "bar" external package. Here the second argument "bar" must be the name of the spack package.
manta_module_get_spack_thirdparty_install_dir(bar_install_dir "bar")
# In this example, the external 3rd party "bar" provides a CMake package. One load this package.
find_package(Bar REQUIRED CONFIG HINTS
             "${bar_install_dir}/share/bar/cmake/")
# Then one finally link with the imported target `bar::Bar` defined in the "bar"'s CMake package.
# `manta_module_link` works as CMake's `target_link_libraries`, and so, assuming that the "bar"'s CMake package is properly done, it automatically manage the include directories.
manta_module_link(${module_name} PUBLIC bar::Bar)

# This is a second example of connection with an external library that does not provide a CMake package.
# The CMAKE_INSTALL_LIBDIR, CMAKE_SHARED_LIBRARY_PREFIX and CMAKE_SHARED_LIBRARY_SUFFIX variables should be used for portability on several plateform, linux distros, ...
manta_module_get_spack_thirdparty_install_dir(bar_install_dir "baz")
manta_module_include(${module_name} SYSTEM PUBLIC ${baz_install_dir}/include)
manta_module_link(${module_name} PUBLIC ${baz_install_dir}/${CMAKE_INSTALL_LIBDIR}/${CMAKE_SHARED_LIBRARY_PREFIX}baz${CMAKE_SHARED_LIBRARY_SUFFIX})

# This has to be called to generate the tests for ctest.
# In this example, the tests of the current module require extra external dependencies that are not required to build the module library.
# The imported targets of such extra external dependencies for tests have to be added to the `manta_module_add_tests` function, as it is done here for `bar::TestingUtilities` and `bar::StrangeStuff`.
manta_module_add_tests(${module_name} bar::TestingUtilities bar::StrangeStuff)

# This has to be called to export the `barConfig.cmake` file in the installation directory of MANTA.
manta_module_export(${module_name})
```

Note

The MANTA's modules are automatically "connected" (meaning that the
`-IXXX` and the `-DYYY` are added to the compiler command line, the
libraries are passed to the linker, ...), for the build and tests of the
current module. One should not add them to `manta_module_link` or
`manta_module_add_tests`

## Update the file `.manta-enabled-modules.json`

Do forget to add the created module in the file `.manta-enabled-modules.json`
at the root of the source repository.

## Manage the initialization/finalization

If the created *module* requires doing something at the initialization of
MANTA (*i.e.* when calling `manta::init(argc, argv)`), it just had to have
in a `init.cpp` file:

```c++
#include "manta/components-system/init.h"

namespace manta {
static Int dummy0 =
    Init::registerInitCallBack("<module name>", [](int argc, char **argv) { /*<things to do at the init stage>*/ });

// if something has to be done at the finalize stage
static Int dummy1 = 
    Init::registerFinalizeCallBack("<module name>", []() { /*<things to do at the init stage>*/ });

}
```

Note

This piece of code can actually be in any compilation unit, but the
recommended practice is to have it in a file named `init.cpp`

## Handling command line arguments

To define new command line arguments related to the created module, you have to define them in a function `registerCLICallBack`. See the following snippet:

```c++
#include "manta/components-system/numeric_types.h"
#include "manta/components-system/command_line_arguments_parser.h"
#include "manta/components-system/init.h"

namespace manta {

struct Args { // ①
  int verbosityLevel;
  std::vector<std::string> inputFiles;
};

Args &getArgs()
{
  static Args args; // ②
  return args;
}

static Int dummy0 = Init::registerCLICallBack("<module name>", [](CommandLineArgumentsParser &parser) { // ③

  parser
      .add_argument("--verbose-level")    // ④ 
      .help("set the verbose level")
      .choices("0", "1", "2", "3")
      .store_into(getArgs().verbosityLevel);

  parser
      .add_argument("input-files")    //
      .help("list of input file\n")
      .nargs(CommandLineArgumentsParser::at_least_one)
      .action([](std::string value) { getArgs().inputFiles.push_back(value); }); // ⑤ 
});

static Int dummy1 = Init::registerInitCallBack("<module name>", [](int argc, char **argv) { // ⑥

  // Here one can do something with the values read from the command line using
  // the getArgs() function

  std::cout << "The input files read from the command line are:\n";
  for (const auto &inputFile : getArgs().inputFiles) {
    std::cout << "  - " << inputFile << std::endl;
  }
  std::cout << "The verbosity level read from the command line is: " << getArgs().verbosityLevel;
});

}    // namespace manta
```

① This convenient structure is defined to store the data read on the command line. It is defined and used only in the current `.cpp` file, so its name does not matter much.

② This is a common trick to define a static variable without the pain of
the [static initialization order fiasco](https://en.cppreference.com/w/cpp/language/siof). An instance of the
structure which store the data from the command line is then created a a
static variable inside a function and then get through this function.

③ ④ The parser used to manage command line argument in manta has
exactly the same interface as the one defined [here](https://github.com/p-ranav/argparse). Please refer to this
documentation for details about managing arguments.

⑤ WARNING: when an argument expects several values, the `action` is
applied sequentially for each value related to this argument, hence the
`push_back`.

⑥ The actual parsing of the command line is actually triggered
automatically by the `manta::init(Int argc, char **argv)` function. This
call is made before the execution of the callback functions registered
through the `registerInitCallBack` function. Then these callback
functions are the appropriate place to handle the data read from the
command line.

## Making an "executable" module

By default, a module builds into a shared library, a set of header files and
some cmake files to be used by downstream project. But the module system can
also be used to create executables.

The only difference is that you have to add `EXECUTABLE` to the function
`manta_module_add_module`, as in the following example:

```cmake
set(module_name "manta::tools-medsplitter")

manta_module_add_module(${module_name} EXECUTABLE)

manta_module_add_tests(${module_name})

manta_module_export(${module_name})
```

The executable created will have a name constructed from the "terminal" name of
the module prefix with `manta-`, here it will be `manta-medsplitter`. The
installation of the executable is triggered by the command
`manta_module_export`.

A unique `main` function MUST appear in one of the source files of the module.

Warning

As the name of the end executable does not contain the name of the "group",
one should not have several "executable modules" with the same name, even in
different "groups"

Note

The `config.h` file generated by the script
`generate_module_page_for_rst_doc.py` (see below) is useless for an "executable module",
and should be removed.

## Update the documentation

To update [this page](available_modules.md#available-modules) which describe the available
*modules*, you have to use the script
`${REPOSITORY_ROOT}/refactor/generate_module_page_for_rst_do.py` and redirect
its output to the file `available_modules.rst`::

```
${REPOSITORY_ROOT}/refactor/generate_module_page_for_rst_doc.py ${REPOSITORY_ROOT}/src > ${REPOSITORY_ROOT}/doc/sphinx/source/manta_components_user_guide/the_module_system/available_modules.rst
```

## Private modules

Private modules, i.e. non open-source modules with files stored in external
private repositories, are created similarly. All private modules are stored in
MANTA source repository in directories `components_private` (for component
modules) and `frontend_private` (for frontend modules). At its creation, the
module directory holds the same data structure as other modules with empty
source and tests directories. The external files will then be imported when
building MANTA and activating the private module.

In order to create a template module structure for a private repository, run :

```bash
${REPOSITORY_ROOT}/refactor/create_module.py -g <group_name> -m <module_name> -p --git <url_of_external_repository> --tag <version_tag>
```

The created files will be located in
`${REPOSITORY_ROOT}/src/<group_name>_private/<module_name>`. This script must
be called from the root of the MANTA repository::

```
<group_name>_private
└── foo
    ├── CMakeLists.txt
    ├── config.cmake
    ├── manta.module
    ├── manta => empty
    └── thirdparties.cmake
```

Warning

Avoid creating private modules manually. Source files copied in wrong locations could be involuntarily added and tracked by the MANTA repository.
The `create_module.py` script define the proper file structure for that.

Instructions to edit the files are the same as for regular modules ([Create the file structure](#module-files-creation))

In the `CMakeLists.txt`, a CMake function manta_module_import_private is added to the
regular file. It is needed to import external files and include them in the
MANTA module structure. It takes four arguments, auto-filled when using create_modules.py.

```cmake
manta_module_import_private(<module_name> <layer_name> <module_url> <module_tag>)
```

With following arguments :

- <module_name> : name of the external module
- <layer_name> : name of the manta layer where it should be installed : components_private, frontend_private, etc...
- <module_url> : url of the repository
- <module_tag> : git branch or tag to checkout

The import function is only run once you try to build MANTA and only then it
is checked if the URL is valid and the system you're on has proper access
rights. It is recommended to set the module_tag as a stable version of the
external repository rather than the master branch.

Note

Once the module is created, the user can override the default url to fetch the private module from and its version (git tag) with CMake variables `MODULE_<module_name>_URL` and `MODULE_<module_name>_VERSION`, using the command line or ccmake.

Note

The external repository is cloned in the build directory and its location is `${CMAKE_BUILD_DIR}/_deps/{module_name}-src/`. If you make edits to private module files, run git commands from this location.

The private module is required to have the following structure::

```
├── manta
|   └── <group_name>-<module_name>
|                       ├── decl
|                       └── config.h
├── tests
└── doc
```

Contrary to open modules, the `config.h` file for private modules is not automatically added, it has to be added manually in the module itself. It has the following form :

```c++
#pragma once

#include "manta/components-system/config.h"

#if defined _WIN32 || defined _WIN64 || defined __CYGWIN__
#if defined manta_{group_name}_private-{module_name}_EXPORTS
#define MANTA_<GROUP_NAME>_PRIVATE-<MODULE_NAME>_VISIBILITY_EXPORT MANTA_VISIBILITY_EXPORT
#else
#ifndef MANTA_STATIC_BUILD
#define MANTA_<GROUP_NAME>_PRIVATE-<MODULE_NAME>_VISIBILITY_EXPORT MANTA_VISIBILITY_IMPORT
#else
#define MANTA_<GROUP_NAME>_PRIVATE-<MODULE_NAME>}_VISIBILITY_EXPORT
#endif
#endif
#else
#define MANTA_<GROUP_NAME>_PRIVATE-<MODULE_NAME>_VISIBILITY_EXPORT MANTA_VISIBILITY_EXPORT
#endif
```

The Sphinx documentation of the private module must be located in the `doc/` directory. In practice, including private `.rst` files in the main Sphinx documentation is done as follows:

```rst
.. only:: include_private_foo

   .. toctree::
      :maxdepth: 1

      /private/foo/doc/foo.rst
```

As long as a private module is loaded via `manta_module_import_private` when `-DMANTA_MODULE_ENABLE_manta-components_private-foo=YES|WANT` is used in CMake, the corresponding private module documentation will be included.
