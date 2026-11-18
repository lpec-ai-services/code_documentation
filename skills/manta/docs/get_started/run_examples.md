<!-- source: https://manta-project.gitlab.io/manta/get_started/run_examples.html -->

# Learn with examples

## PyManta Examples

The general structure of a test-file
and some commented examples are available within the
[User guide of the MANTA and PyManta frontends](../manta_frontend_user_guide/user_guide.md#manta-frontend-user-guide).

Verification tests are documented in [Verification tests of the MANTA and PyManta frontends](../verification_tests/manta_frontend_verification_tests/verification_tests.md#manta-frontend-verification-tests).

## Manta components examples

This section is focused on examples written in the low-level API of MANTA.
These examples can be run within the build directory.

Moreover, the test base of the MANTA components (in examples/,
src/components/.../tests and verification_tests/)
can be browsed for inspiration about a particular subject.
Some of these tests are documented in [Verification tests of MANTA components](../verification_tests/manta_components_verification_tests/manta_components_verification_tests.md#manta-components-verification-tests).

For both these sections there are examples and tests. Examples can be found in
manta/examples, while tests can be found in the tests repository within each components,
or within the frontend.

### Looking for an example

If you are looking for specific features about numerical simulations and how to
treat them with MANTA, you can have a look into the tests and examples.

The **search_tool.py** Python application helps you to find examples and tests
related to a series of keywords. To get started, just run

```
./search_tool.py --help
```

For more information on using this tool, see the
[search tool section](../demos/search_tool.md#search-tool).

### Build and run examples using the test pipeline (easier)

The examples can be built and run using the test pipeline. First, some specific
options must be passed to `cmake` when configuring the project to generate the
tests that build and run those examples. Then, examples can be easily launched
using `ctest`.

#### Cmake options

The following options must be passed to cmake in order to generate tests related to examples:

```shell
cmake <..standard cmd (see above)..> -D ADD_EXAMPLES_TO_TESTS=<mode> [-D GMSH_BIN=<gmsh> -D CASTEM_BIN=<castem>]
```

where:

- `<mode>` is either:

  - `NoCompile` -> default, no test generated
  - `Compile` -> only generate compilation tests
  - `CompileAndRun` -> generate both compilation and run tests
- `<gmsh>` is a path to a `gmsh` executable on your system
- `<castem>` is a path to a `castem` executable on your system

Note

`-D GMSH_BIN=<gmsh> -D CASTEM_BIN=<castem>` arguments are only mandatory
when meshes have to be generated. Thus, they are not required if
`ADD_EXAMPLES_TO_TESTS` is set to `NoCompile` or
`Compile`, as no run test is generated, and no mesh needs to be generated.

Here are two examples:

```shell
cmake <path to manta> -DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=<install path> -D ADD_EXAMPLES_TO_TESTS=Compile
```

```shell
cmake <path to manta> -DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=<install path> -D ADD_EXAMPLES_TO_TESTS=CompileAndRun -D GMSH_BIN=gmsh -D CASTEM_BIN=castem21
```

#### Build and run the examples

Once the project has been configured with `cmake`, using the specific options
described above, and **once the project has been built** using `make` (see
dedicated section), the tests related to examples are launched using `ctest`
**from the build directory**.

To launch compilation tests, use:

```shell
ctest -R examples.*BUILD
```

To launch run tests, use:

```shell
ctest -R examples.*RUN
```

Warning

`BUILD` tests are only available if you've set the option
`ADD_EXAMPLES_TO_TESTS` to `Compile` or to
`CompileAndRun`, and RUN tests are only available if you've set the
option to `CompileAndRun`.

Note

Any `RUN` test automatically triggers a `SETUP` test where any
required mesh is generated.

### Build and run examples as stand alone computations (more involved)

Examples can also be built and run outside the test pipeline, as standalone
programs. This procedure is more involved than using the pipeline (see above).

- Create a directory for the example you plan to build and run

  ```shell
  mkdir example
  cd example
  ```
- Choose the same compiler that was used for building MANTA:

  ```shell
  export CXX=clang++ && export CC=clang
  ```
- Build the example:

  ```shell
  cmake $MANTA_SRC/example/... -DMANTA_INSTALL_DIR=<*absolute path* to MANTA installation directory>
  make -j 8
  ```

  Warning

  The path to MANTA installation directory must be an **absolute path**
- Execute the example

  - Generate the mesh (here, for a .geo mesh script, using gmsh) with either:

    ```shell
    gmsh <myFile.geo> -
    ```

    to use the parameters hard coded in the .geo file, or:

    ```shell
    gmsh -format msh2 -<meshDimension> -o <myMesh.msh> <myFile.geo>
    ```

    to override them. If the parameters have not been hard coded in the .geo
    file, use the second syntax.

    Warning

    The -format msh2 option is mandatory because MANTA's current msh
    reader only supports this format.
  - run the executable

    ```shell
    mpirun -np <number_of_processors> <path_to_executable> -some_petsc_options
    ```

### Weekly run of examples

Examples are built and run every Sunday. Since the regular CI process does
not require all of them to pass (only the build is checked),
some of them might fail.

The output can be obtained here :
[Examples run output](https://manta-project.gitlab.io/manta/test_output/test_output.html)

### Tips

- You can pass some options to the compiler by adding
  `-DCMAKE_CXX_FLAGS='-wonderful-option -other-crazy-option'` to the cmake
  command.
- When compiling with clang, the `std::string` may be not visible in a
  debugger. To fix that, add `-DCMAKE_CXX_FLAGS='-fno-limit-debug-info'`
  to the cmake command when compiling MANTA.
- To understand where it take so much time to compile, compile with clang and
  `-DCMAKE_CXX_FLAGS='-ftime-trace'`. This will generate `.json`
  files along with the `.o` files (you may have to scavenge a
  little in the cmake tree to find them...). This file are 'flame graphs'
  wich can be viewed online with [speedscope](https://www.speedscope.app/)
  for instance (`chrome://tracing/` is really bad...)
