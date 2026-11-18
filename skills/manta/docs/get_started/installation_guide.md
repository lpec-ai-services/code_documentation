<!-- source: https://manta-project.gitlab.io/manta/get_started/installation_guide.html -->

# Installation guide

A complete guide to manually build and install MANTA is given on this page.

For quick directives about installation and setup, please refer to the
`README` file on MANTA
[Gitlab repositiry](https://gitlab.com/manta-project/manta/-/blob/master/README.md).

Please refer to the [A Spack recipe for Manta](#a-spack-recie-for-manta) section for more details regarding the installation of MANTA via its Spack recipe.

## Requirements

- [Git](https://git-scm.com/)
- [CMake](https://cmake.org/) (>=3.22 <=3.28)
- [Python](https://www.python.org/) (>=3.10 <=3.13)
- [Spack](https://spack.io/) (1.1.0): MANTA uses the **spack** package
  manager to download and build almost all its 3rd parties in a robust and
  consistent
  way. See [spack documentation](https://spack.readthedocs.io/en/latest/getting_started.html)
  to start using it, and get spack's dependencies.
- **MPI** (tested and developed with
  [openMPI](https://www.open-mpi.org/) >=4 and [MPICH](https://mpich.org) =3.4.3):
  MANTA uses the MPI which has precedence in the PATH (the one returned by `which mpiexec`).
  Please ensure that the detected MPI package is the intended one to use.

MANTA also requires one of these recent C++ compilers:

- **g++** >= 11
- **clang++** >= 12

At this time, MANTA is not tested with other compilers.

If you want to build MANTA with GPU support, you will also need [Cuda](https://developer.nvidia.com/cuda-toolkit) (version 12.0 was tested,
but not above).

Note

If `CMake` or appropriate compilers are not available on the machine, `spack`
which is required by MANTA can be used to install them easily.

Note

Spack handles MANTA's direct dependencies (the 1st level dependencies), but
also the dependencies of these 1st level dependencies and so on. But some of
these dependencies may depend on low-level thirdparties which are not available in the
`spack`'s ecosystem. In such case they rely on "external installations" for these packages
not handled by `spack`. So in a few cases, MANTA's building and functioning
requires some externally installed packages.

MANTA's workflow involves different kind of tests which are executed in `Docker` or `Podman`
images based on several linux distributions. The system's packages which are installed in this
docker images to run MANTA can be checked in the `<distribution identifier>.setup.sh`
file [here](https://gitlab.com/manta-project/manta/-/tree/master/ci/buildandtest_image/distrib).

## MANTA's list of dependencies

The following list gives the MANTA's dependencies. These dependencies are given with the format of 'spack specs' ([see here for details](https://spack.readthedocs.io/en/latest/spec_syntax.html)). Their homepage from which you can find instructions to build them are also given. This list of dependencies is the one that you get when you build the full manta with the cmake options: -DGENERATE_SPEC_LIST.
To have the list for a specific set of options, you should launch the script :

```bash
ci/jobs_configuration/check/check_dependencies.py <manta_path> <output_path> [--extra-cmake-args <args>]
```

Where:
:   - `<manta_path>`: Path to your Manta configuration
    - `<output_path>`: Destination for the generated dependencies list
    - `--extra-cmake-args`: Additional CMake arguments (default: `-DFORCE_OPENBLAS=ON`)

- [medcoupling@9.13.0](mailto:medcoupling%409.13.0) (<https://docs.salome-platform.org/latest/dev/MEDCoupling/developer/index.html>)
- [gmsh@4.13.1~alglib~cgns~compression~fltk~gmp~med~metis~mmg~netgen~voropp+eigen](mailto:gmsh%404.13.1~alglib~cgns~compression~fltk~gmp~med~metis~mmg~netgen~voropp+eigen) (<https://gmsh.info>)
- [tinyxml2@8.0.0](mailto:tinyxml2%408.0.0) (<http://grinninglizard.com/tinyxml2/>)
- [vtk@9.2.6+xdmf](mailto:vtk%409.2.6+xdmf) (<http://www.vtk.org>)
- [tfel@5.1.0~abaqus~ansys~aster+castem~calculix~cyrano~europlexus~lsdyna~comsol~diana-fea~fortran~java~python~python_bindings](mailto:tfel%405.1.0~abaqus~ansys~aster+castem~calculix~cyrano~europlexus~lsdyna~comsol~diana-fea~fortran~java~python~python_bindings) (<https://thelfer.github.io/tfel/web/index.html>)
- [mgis@3.1.0~c~fortran~python](mailto:mgis%403.1.0~c~fortran~python) (<https://thelfer.github.io/mgis/web/index.html>)
- [eigen@3.4.0](mailto:eigen%403.4.0) (<https://libeigen.gitlab.io/>)
- [petsc@3.24.1+mumps+superlu-dist~hypre~hdf5~metis~int64](mailto:petsc%403.24.1+mumps+superlu-dist~hypre~hdf5~metis~int64) fflags="-fallow-argument-mismatch" (<https://petsc.org>)
- [slepc@3.24.1](mailto:slepc%403.24.1) (<https://slepc.upv.es>)
- [zoltan@3.901~fortran+parmetis](mailto:zoltan%403.901~fortran+parmetis) (<https://sandialabs.github.io/Zoltan/>)
- [mtl3d@1.1~qhull](mailto:mtl3d%401.1~qhull) (<https://gitlab.com/manta-project/mtl3d>)
- [geode@2026-10-11](mailto:geode%402026-10-11) (<https://gitlab.com/geode-geometry/geode>)
- [moab@5.5.1](mailto:moab%405.5.1) build_type=Release (<https://bitbucket.org/fathomteam/moab>)
- [tinyxml2@8.0.0](mailto:tinyxml2%408.0.0) (<http://grinninglizard.com/tinyxml2/>)
- [rapidjson@1.2.0-2024-08-16](mailto:rapidjson%401.2.0-2024-08-16) (<https://rapidjson.org>)
- [cpp-argparse@3.2](mailto:cpp-argparse%403.2) (<https://github.com/p-ranav/argparse/>)
- [tinyboost@1.83.0](mailto:tinyboost%401.83.0) (<https://gitlab.com/manta-project/tinyboost>)
- [googletest@1.17.0](mailto:googletest%401.17.0) (<https://github.com/google/googletest>)
- [cereal@1.3.2](mailto:cereal%401.3.2) (<https://uscilab.github.io/cereal/>)
- [py-nanobind@2.8.0](mailto:py-nanobind%402.8.0) (<https://nanobind.readthedocs.io>)

## Spack setup

- Clone spack

  ```shell
  git clone https://github.com/spack/spack.git
  ```
- Set up spack

  ```shell
  export SPACK_ROOT=$PWD/spack/
  source $SPACK_ROOT/share/spack/setup-env.sh
  ```
- Checkout the appropriate release tag, e.g.:

  ```shell
  cd $SPACK_ROOT
  git checkout v1.1.0
  ```

  Note

  Spack will tell you which version of Spack you need with your current version
  of MANTA when running `cmake`. If you have not checked out the correct
  release tag, you will get an error message similar to

  ```text
  CMake Error at thirdparties-spack/CMakeLists.txt:49 (message):

  This manta's version is configured to work with spack major release **0.21**.
  If the spack version detected is another one, please checkout appropriate version
  in your spack repository.
  ```

  Warning

  Do not checkout a release branch, e.g. `releases/v0.21`.
  Spack release branches correspond to the latest **point** (i.e. minor)
  release of the corresponding major release (see the spack
  [Developer Guide](https://spack.readthedocs.io/en/latest/developer_guide.html#release-branches)),
  so they may change over time.

## Build MANTA

- Create a directory for the MANTA project:

  ```shell
  mkdir manta-project
  cd manta-project
  ```
- Clone MANTA:

  SSH

  ```shell
  git clone git@gitlab.com:manta-project/manta.git
  export MANTA_SRC=$PWD/manta/
  ```

  HTTP

  ```shell
  git clone https://gitlab.com/manta-project/manta.git
  export MANTA_SRC=$PWD/manta/
  ```

  Warning

  These commands to clone the repository must be adapted if you want to get the MANTA source code from somewhere else than gitlab (e.g., from the github mirror).
- Choose compiler (CC/CXX must point to mpi wrappers)

  Note

  In order to build MANTA and its thirdparties, you need at least gcc-11
  (including gfortran-11) or clang-12

  gcc

  ```shell
  export CXX=g++ && export CC=gcc
  ```

  Warning

  **For gcc, the fortran and c/c++ compilers version must match.
  If you are not using the default compilers of the distribution,
  you may have to specify manually the fortran compiler.**
  For example, on a system where the default gcc version (and so gfortan)
  is 11, and you want to use gcc-12, you have to do

  ```shell
  export CXX=g++-12 && export CC=gcc-12 && export FC=gfortran-12
  ```

  clang

  ```shell
  export CXX=clang++ && export CC=clang
  ```

  Warning

  If the fortran compiler is not specified, the default fortran
  compiler of the system will be chosen. Clang actually uses and relies on
  the latest version of the gcc toolchain that it finds on the system
  (unless specified with `--gcc-toolchain` option). This version of gcc that
  is used by clang can be checked with `clang -v`. **It is required for a
  proper build of manta that the fortran compiler used is the same as the
  one related to the gcc toolchain used by clang**. For example, let's
  assume that you are on a system where gcc-11 and gcc-12 are installed, and
  that the default gcc version (and so gfortran) is 11. Then, the above
  command will not be ok because gfortran-11 will be selected, whereas clang
  will relies on gcc-12. In such a case you have to do:

  ```shell
  export CXX=clang++ && export CC=clang && export FC=gfortran-12
  ```
- Create a `build` directory separate from the `$MANTA_SRC` directory:

  ```shell
  mkdir build
  ```

  At this point, you should have the following structure:

  ```shell
  manta-project
  ├───build
  └───manta
  ```
- Configure the project with `cmake`

  ```shell
  cd build
  cmake $MANTA_SRC -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=../install
  ```

  Note

  - Several options are available in order to tweak the configuration of the
    project. See the dedicated paragraph at the end of this page
    for some details.
  - If you have issues with building Manta using an *AMD* architecture,
    try configuring the project with the option `-DFORCE_MKL=ON`.
  - For some various reasons, it may happen that a failure occurs when spack
    build a MANTA's thirdparty. When this happens, the screen output of
    cmake suggests to install the related 1st-level MANTA's thirdparty
    another way and to provide to cmake this installation path through the
    `<THIRDPARTY NAME>_INSTALL_PATH` variable (_e.g._ `cmake $MANTA_SRC
    -DPETSC_INSTALL_PATH=/opt/petsc ...`). When doing so, the version and
    compilation option of the externally installed thirdparty are likely to
    differs from the one of MANTA's spack installation which which it has
    been tested. So this should be done when failing to build with spack, and
    trying to match as possible the version and compilation options of the
    spack installation.
- Build the project with `make`:

  ```shell
  make install -j 8
  ```
- Optionnaly Run the test base (in the 'build' directory):

  ```shell
  ctest -j 8
  ```

## Fine selecting which part of MANTA you would like to build, test and use

The above procedure will build all the features of MANTA. But as MANTA has a
modular design, you may be interested in a particular application, or internal
functionality of MANTA. In such a case, you could build only the "modules" of
MANTA that you are interested in.

To this end, you could use either a configuration file, or command line
arguments (or the `ccmake` GUI, but in the end this is the same as with command
line arguments).

On the command line, enabling a module named `foo` is controlled by
adding `-DMANTA_MODULE_ENABLE_manta_foo=<value>` on the command line. The
`<value>` can be one of the following:

- `YES`: The module must be built.
- `NO`: The module must not be built. If a YES module has a NO module in
  its dependency tree, an error is raised.
- `WANT`: The module should be built. It will not be built, however, if
  it depends on a NO module.
- `DONT_WANT`: The module doesn't need to be built. It will be built if a
  `YES` or `WANT` module depends on it.
- `DEFAULT`: Look at other metadata to determine the status.

You can specify the default behavior on the command line by adding
`-DMANTA_MODULE_DEFAULT=<value>`.
The value must be either `WANT` or `DONT_WANT`.

Note

Thanks to the management of the dependencies between the modules, you
can only tag by `WANT` the actual set of modules you are interested in
(without bothering about their dependencies) and by `DONT_WANT` all the
others.

You can also use a configuration file in which you set the build query for each
module of MANTA. MANTA will look for these files, ending when it finds one, with
this priority:

1. manta-enable-module.json in the **build directory**
2. manta-enable-module.json in the **source directory**

Warning

Don't confuse the file `manta-enable-module.json` in the source
directory with the file `.manta-enable-module.json` which must not be
edited.

A convenient way to manage this file is to use the command:

```shell
cmake <path to the source directory> -DGENERATE_MODULE_FILE=<BUILD or SOURCE>
```

If `SOURCE` is used, then the file `manta-enable-module.json` is created in
the source directory whereas If `BUILD` is used, it is created in the build
directory.

In one of these files you can specify the default behavior, i.e., the meaning of
`DEFAULT` (this must be either `WANT` or `DONT_WANT`),
and the build query for each module.

When using a file to specify the modules to build, you can still pass
`-DMANTA_MODULE_ENABLE_manta_foo=<value>` or
`-DMANTA_MODULE_DEFAULT=<value>`.
The values passed on the command line have higher priority than what is in the
configuration files.

## The cmake preset way

Warning

**Disclaimer:** The build process described here is experimental. If it fails,
please use the "manual way" subsection shown above instead.

In lieu of the previous method, one can use **CMake presets**, which are predefined configurations to streamline the build process. They can be used by running the following command:

```shell
cmake --workflow --preset install/gcc
```

- Don't forget to **set up the Spack environment** (see instructions above).
- You need to have Doxygen, Sphinx, and all the packages listed in `doc/sphinx/requirements.txt` installed on your system. You can create a Python virtual environment using the following steps:

  ```shell
  python -m venv MantaVenv
  source MantaVenv/bin/activate
  pip install -r manta/doc/sphinx/requirements.txt
  ```
- To use the CMake workflow feature, you need at least **CMake 3.24**.
- Start the installation of Manta using the presets. Modify the following lines according to your configuration:

  ```shell
  cd manta
  export MANTA_SRC_FOR_DOC=/path/to/manta   # Needed during the Sphinx documentation build step
  cmake --workflow --preset install/gcc     # Make sure to select the appropriate compiler
  ```

If you want the build process to use the maximum number of CPUs available on your
machine, you can precede the command with the appropriate environment variable:

```shell
cd manta
CMAKE_BUILD_PARALLEL_LEVEL=$(nproc) cmake --workflow --preset install/gcc
```

Warning

If you have run the command above with another preset before, you
may need to add the `--fresh` option to the command, in order to prevent
any conflict.

Note

This process, by default, creates `build` and `install` directories in the
parent directory of the Manta repository. The default build type is
`RelWithDebInfo`. You can use different presets such as `install/clang` to use
a different compiler to build Manta.

Note

If you want to modify those presets, you should avoid modifying
`CMakePresets.json` directly. Instead, you should create a
`CMakeUserPresets.json` file at the root of the Manta repository. It will not
be tracked by git. You can read the existing `CMakePresets.json` or the
[CMake documentation](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html)
to populate your `CMakeUserPresets.json` according to your needs.

## Python bindings

The Python bindings are compiled automatically if the **manta** module is.
You can disable the compilation of the Python bindings using the
`-DENABLE_PYTHON_BINDINGS=OFF` flag.

By default, the `numpy` package is automatically added to the `spack`
dependencies. This can be disabled by using the `-DENABLE_NUMPY_FROM_SPACK=OFF`
flag.

## Available CMake options

Several compilation options can be defined when calling the
`cmake` command in a build directory. This page lists the available
options and their respective effect on the way the library is built.

To use one of these options, the syntax is :

```
-D <option name>
```

Note : the blank space between `-D` and the `<option name>` is
optional.

Some cmake options have default values which allow to omit their
definitions when calling the `cmake` command. Those default values are
defined in the `manta/CMakeLists.txt` source file.

There are two different situations :

- The option is a boolean option, which can be whether `ON` or
  `OFF`. For instance, with the `FORCE_MKL`
  option :

```shell
cmake ../manta <some options> -D FORCE_MKL=ON
```

- The option stores a `string` value. For instance, with the
  `MESH_BACKEND` option :

```shell
cmake ../manta <some options> -D MESH_BACKEND=MOAB
```

> **Note** : the string is written directly, without quotes.
>
> **Warning** : CMake is **case sensitive** with variables’ name.

### Options and their definition

| Flag name | Description | Default value |
| --- | --- | --- |
| `MESH_BACKEND` | Choose which mesh backend library to use. Must be either `MOAB` (default) or `PUMI`. | `MOAB` |
| `DENSE_ALGEBRA_BACKEND` | Choose which dense algebra backend library to use. Must be either `EIGEN` (default) or `ROTGEN`. | `EIGEN` |
| `EXTRA_MODULE_GROUPS` | Add external (outside MANTA's repository) groups of modules to the build of MANTA. Several absolute paths can be provided, separated by `:`. Each path provided must refer to a directory having the same structure as for example `src/components`. | `<EMPTY>` |
| `ENABLE_SPACK_EXTERNALS` | Let spack search for external packages (within MANTA's spack environment, does not alter user spack's configuration) | `ON` |
| `IGNORE_PRE_COMMIT` | Do not perform any automatic 'pre-commit' installation | `OFF` |
| `DEPRECATION_WARNINGS` | Let the compiler generate warnings in case of usage of deprecated functions or methods | `OFF` |
| `DOCSNIPPETS` | Enable compilation of code snippets for documentation with ctest | `OFF` |
| `MANTA_FIELD_ALIGNMENT` | Force alignment value for floating point data handled by the "fields data structures" in manta. If not set, the default value is set by the dense algebra backend. | `<UNDEFINED>` |
| `ENABLE_PORTABLE_BUILD` | By default MANTA is built with `-march=native`, making it not portable. This option removes this compiler option, making it portable (but restricts some optimizations). | `OFF` |
| `ENABLE_PETSC_64BIT_INDICES` | Enable usage of 64bit indices in PETSc to avoid integer overflow for large problems. | `OFF` |
| `ENABLE_FAST_MATH` | Enable `-ffast-math` compiler flag. | `OFF` |
| `ENABLE_EPX_SRC` | Enable compilation of some source code extracted from Europlexus (some Riemann solvers, steam-water tables). Require fortran compiler. | `ON` |
| `ADD_EXAMPLES_TO_TESTS` | Enable creation of compilation/run tests for examples (in ctest). Must have value in: `NoCompile` (no test generated), `Compile` (only compilation tests generated) or `CompileAndRun` (compilation and run tests generated). WARNING: if the flag is set to `CompileAndRun`, the additional flags `CASTEM_BIN` and `GMSH_BIN` must also be prescribed | `NoCompile` |
| `FORCE_MKL` | Force use of mkl whatever the achitecture is. By default: Intel -> MKL / AMD -> openblas (blas, lapack), netlib (scalapack) | `OFF` |
| `FORCE_OPENBLAS` | Force use of openblas for blas/lapack and netlib's scalapack whatever the achitecture is. By default: Intel -> MKL / AMD -> openblas (blas, lapack), netlib (scalapack) | `OFF` |
| `FORCE_AMDAOCL` | Force use of AMD-AOCL libs for blas/lapack/scalapack. By default: Intel -> MKL / AMD -> openblas (blas, lapack), netlib (scalapack) | `OFF` |
| `ENABLE_SANITIZER` | Enable various sanitizer options (undefined, address,...) excluding memory leaks | `OFF` |
| `ENABLE_MEMORY_LEAK_SANITIZER` | Enable sanitizer options for memory leaks | `OFF` |
| `SLEPC` | Enable slepc usage (and compilation) | `ON` |
| `SUPERLU` | Enable SuperLU usage (and compilation) | `ON` |
| `MUMPS` | Enable mumps usage (and compilation) | `ON` |
| `HPDDM` | Enable hpddm usage (and compilation) | `OFF` |
| `ML4PETSC` | Enable ML preconditioner for PETSc support | `OFF` |
| `X4PETSC` | Enable X server for PETSc (to plot matrices profile for example) | `OFF` |
| `VALGRIND` | Enable usage of valgrind request mechanism (see valgrind doc) | `OFF` |
| `CALIPER` | Enable usage of caliper profiling | `OFF` |
| `ENABLE_PYTHON_BINDINGS` | Enable pymanta. This option is only taken into account if the manta module is selected | `ON` |
| `SPACK_BYPASS` | Disable usage of spack for the handling of 3rd parties | `OFF` |
| `<THIRDPARTY NAME>_INSTALL_PATH` | Use an external installation (not with MANTA's spack installation way) for the thirdparty `<THIRDPARTY NAME>` | `<UNDEFINED>` |
| `ENABLE_WERROR_FLAG` | Treat all warning as error | `ON` |
| `ENABLE_WERROR_FLAG_FOR_DOC` | Treat all warning as error in the build of the sphinx doc | `OFF` |
| `FORCE_ARCH_SPACK` | Force architecture for spack handling of 3rd parties. Must be the string that is returned by spack arch -t on the target system | `OFF` |
| `GENERATE_SPEC_LIST` | Generate the list of spack depencies. The path of the file in which the list will be generated must be provided: `-DGENERATE_SPEC_LIST=<path of the file>`. | `<UNDEFINED>` |
| `ENABLE_PETSC_CUDA` | Enable the usage of Cuda for the PETSc solvers and preconditionners (typically HYPRE preconditionner) | `OFF` |
| `SPACK_NOBUILD` | For each 3rd party, get it from the spack set of already installed package without building a new one if the spec does not match. If several variants of the package are already installed, take an arbitrary one. | `OFF` |
| `CUDA_ARCH_VALUE` | CUDA architecture version to target (if ENABLE_PETSC_CUDA is ON). See <https://developer.nvidia.com/cuda-gpus> , where architecture version is the version number without the dot. Default is 80 (i.e. "8.0") | `80` |
| `ENABLE_PETSC_HYPRE` | Enable the usage of the Hypre PETSc preconditionner. This is OFF by default, and ON when ENABLE_PETSC_CUDA is set. | `OFF` |
| `DISABLE_CCACHE` | Disable the use of ccache for compilation. | `OFF` |

## Use MANTA within Python

By default, MANTA is built and installed with Python bindings.

The easiest way to work with MANTA in Python is to load the MANTA's environment:

```shell
source <install-path>/share/manta/env.sh
```

Then, the Python `manta` module can be imported as any Python module:

```python
import manta
```

Full usage of the `manta` module in Python
is described in the [front-end section](../manta_frontend_user_guide/user_guide.md#manta-frontend-user-guide).

## Compilation tips

- You can pass some options to the compiler by adding
  `-DCMAKE_CXX_FLAGS='-wonderful-option -other-crazy-option'` to the cmake
  command.
- When compiling with clang, the ``` std::string``s may be not visible in a
  debugger. To fix that, add ``-DCMAKE_CXX_FLAGS='-fno-limit-debug-info' ``` to the
  cmake command when compiling MANTA.
- To understand where it take so much time to compile, compile with clang and
  `-DCMAKE_CXX_FLAGS='-ftime-trace'`. This will generate `.json` files along
  with the `.o` files (you may have to scavenge a little in the cmake tree to
  find them...). This file are 'flame graphs' which can be viewed online with
  <https://www.speedscope.app/> for instance (chrome://tracing/ is really bad...)

## Build on a machine without internet access

MANTA's default installation procedure uses spack which requires an internet
access to download the source code of the packages to build.

Building MANTA on a machine with no internet access is then a bit trickier.
The strategy is to use a machine which has an internet connection to fetch all
necessary files, which are then copied on the distant machine. Finally the
compilation is done on the distant machine. A shell script `bridge.sh` located
in `<MANTA SRC DIR>/bridge` is provided to help with that.

Please follow the instructions below. Those instructions are divided into two parts. The first one must be executed on the machine which has internet and the second part must be executed AFTER the first part, on the machine which does not have access to internet.

### On a machine with internet access (typically your local machine)

- Check that you can connect to the remote without typing your password, by configuring remote and local ssh framework. This is not mandatory, but if this step is not done, it will be required to type your cluster user account's password several times during the execution of the script.
- Create a directory and get into it. In the remainder of this section, this directory is called `MANTA_BRIDGE`.
- Copy the files `bridge.sh` from the manta source directory into `MANTA_BRIDGE`.

  Say that you have a Manta repository on your machine at the path `MANTA_SRC`:

  ```shell
  cp $MANTA_SRC/bridge/bridge.sh $MANTA_BRIDGE
  ```
- Execute the script `bridge.sh` with appropriate options. You can execute `$MANTA_BRIDGE/bridge.sh --help` to get the list of options and their description.

  A difficulty here is that the set of MANTA's thirdparties may depend on the cpu brand of the machine and MANTA's compilation options. To handle that:

  > - If you plan to build on the remote machine with some non-default cmake options, you should use the `--extra-cmake-args` option of the `bridge.sh` script to provide this exact set of non-default options.
  > - If your local machine has a intel cpu, and the remote an AMD cpu, or the other way around: you should use the compilation options which define the blas/lapack/scalapack to use (`FORCE_OPENBLAS`, `FORCE_MKL`, `FORCE_AMDAOCL`, see above) either in the `--extra-cmake-args` option of the `bridge.sh`, or when building on the remote machine (see just after) to end up having a consistent choice between the local and remote machine.

  Here is an example where one plans to build MANTA on a cluster which can be connected to with `ssh irene` (a configuration is set in the `$HOME/.ssh/config` file for the name `irene`). In this case not all the modules of MANTA are built and one uses `openblas` to handle blas/lapack/scalapack.

  ```shell
  bridge.sh  --remote irene --remote-dest /ccc/scratch/cont002/den/jamondol/manta-pack --extra-cmake-args '-DMANTA_components_MODULE_DEFAULT=DONT_WANT -DMANTA_frontend_MODULE_DEFAULT=DONT_WANT -DMANTA_frontend_MODULE_DEFAULT=DONT_WANT -DMANTA_MODULE_ENABLE_manta-components-io_gmsh=WANT -DMANTA_MODULE_ENABLE_manta-io_vtk=WANT -DMANTA_MODULE_ENABLE_manta-components-modeling=WANT -DMANTA_MODULE_ENABLE_manta-components-executable_utilities=WANT -DFORCE_OPENBLAS=ON'
  ```

### On the remote machine (with no internet access)

Let's assume that the directory that has been set for the option `--remote-dest` of the `bridge.sh` script is `MANTA_PACK`, and you plan to build MANTA in a build directory `MANTA_BUILD` and install it into `MANTA_INSTALL`.

- Load the appropriate environment (usually with module) to have appropriate compilers, cmake and MPI.
- Load spack

  A first, not mandatory but advised, step is to define some environment variable to avoid unwanted interferences with an existing user spack's configuration:

  ```shell
  export SPACK_USER_CACHE_PATH=$MANTA_PACK/dotspack && export SPACK_USER_CONFIG_PATH=$MANTA_PACK/dotspack
  ```

  Then:

  ```shell
  source $MANTA_PACK/spack/share/spack/setup-env.sh
  ```
- Specify to MANTA's build process the compilers to use (strongly recommanded, even for `gcc`). Here for example with gcc:

  ```shell
  export CC=gcc && export CXX=g++ && export FC=gfortran
  ```
- Go to the build directory:

  ```shell
  cd $MANTA_BUILD
  ```
- Execute cmake with options matching the one entered for the `bridge.sh` script. The spack database will be constructed at this step so it may take a long time...

  Following the example above, one would execute:

  ```shell
  cmake $MANTA_PACK/manta -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=$MANTA_INSTALL -DMANTA_components_MODULE_DEFAULT=DONT_WANT -DMANTA_frontend_MODULE_DEFAULT=DONT_WANT -DMANTA_frontend_MODULE_DEFAULT=DONT_WANT -DMANTA_MODULE_ENABLE_manta-components-io_gmsh=WANT -DMANTA_MODULE_ENABLE_manta-io_vtk=WANT -DMANTA_MODULE_ENABLE_manta-components-modeling=WANT -DMANTA_MODULE_ENABLE_manta-components-executable_utilities=WANT -DFORCE_OPENBLAS=ON
  ```
- Build and install MANTA

  Here there is another trap: usually on a computation cluster one work
  interactively on the login node. By default, MANTA is built with the
  compiler option `-march=native`, so that it is optimized for the
  architecture of the machine on which it is built. But it will not work on
  another architecture. It may happen that the login node does not have the same
  architecture as the computation nodes on which MANTA will eventually run.
  If this is the case, the best, if possible, is to build MANTA on a computation
  node on the target partition. If this is not possible, one can use the cmake
  option `-DENABLE_PORTABLE_BUILD=ON` (see above for details) to make MANTA
  portable across architectures.

  ```
  make install
  ```
- Optional: test the build

  ```
  ctest --output-on-failure
  ```

## A Spack recipe for Manta

A procedure for installing MANTA using its Spack package is detailed below.

It will guide the user from creating a Spack clone to loading the MANTA executable into the environment.

1. Download Spack

> First, let's clone the Spack repository.
>
> ```shell
> export SPACK_PATH=<define_this_path_to_the_desired_directory>
> git clone https://github.com/spack/spack.git $SPACK_PATH
> ```

2. Setup your environment

> You just have to source $SPACK_PATH/share/spack/setup-env.sh
>
> ```shell
> source $SPACK_PATH/share/spack/setup-env.sh
> ```

3. Configure Spack

> - Find compilers:
>
>   ```
>   spack compiler find
>   ```
> - Add the manta repository:
>
>   <manta_path> is the absolute path to the manta repository (that you have to clone or get manually).
>
>   ```
>   spack repo add <manta_path>/spack/spack_repo/manta
>   ```
>
>   The previous command will make the recipes for Manta and its dependencies accessible.
>   These recipes have been taken from the thirdparties-spack folder and adapted to version v1.0.0 of Spack.
>
>   ```
>   spack/
>   └── spack_repo
>       └── manta
>           └── packages
>               ├── cpp_argparse
>               ├── manta
>               ├── medcoupling
>               ├── medfile
>               ├── mgis
>               ├── moab
>               ├── more_concepts
>               ├── mtl3d
>               ├── mumps
>               ├── pumi
>               ├── salome_configuration
>               ├── tfel
>               └── tinyxml2
>   ```
>
>   spack/spack_repo/manta is the local repository of Spack recipes.
>   It contains the file repo.yaml so you can add the local repository of receipe into Spack with the
>   command spack repo add.
>   The recipe of Manta is here: spack/spack_repo/manta/packages/manta/package.py.

4. Install Manta directly or inside an environment

> - Directly:
>
>   ```
>   spack install manta
>   ```
>
>   or
>
>   ```
>   spack install --test root manta
>   ```
>
>   if you want to run tests.
> - Inside an environment:
>
>   ```
>   spack env create <env_name>
>   spack -e <env_name> add manta
>   spack -e <env_name> concretize
>   ```
>
>   then
>
>   ```
>   spack -e <env_name> install
>   ```
>
>   or
>
>   ```
>   spack -e <env_name> install --test root
>   ```
>
>   if you want to run tests.

5. Get Manta in your environment

> - From direct installation:
>
>   ```
>   spack load manta
>   ```
> - From Spack environment:
>
>   **Remark:** It is recommended to use the spack.view: true option in the
>   $SPACK_PATH/var/spack/environment/<env_name>/spack.yaml to load all runtime dependencies.
>
>   ```
>   spack env activate <env_name>
>   ```
