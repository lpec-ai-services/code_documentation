<!-- source: https://manta-project.gitlab.io/manta/get_started/containerized_usage.html -->

# Containerized usage

MANTA can be used through some Apptainer (<https://apptainer.org/>) images
which are available on MANTA's gitlab project.

In this page we may refer to the image as `manta.sif`, but it may have different names depending on the version downloaded, such as `manta-apptainer_master.sif`

## How to install Apptainer

Read instructions [here](https://apptainer.org/docs/admin/main/installation.html#installation) to install Apptainer.

If you can't be root on your machine, a simple way to install Apptainer is to use Spack.

First you have to install Spack itself:

```shell
SPACK_ROOT=<a directory>
cd ${SPACK_ROOT}
git clone https://github.com/spack/spack.git
# The following line enables spack in the current shell.
# This should be added to the .bashrc or alike to avoid being typed in every new shell.
source  ${SPACK_ROOT}/spack/share/spack/setup-env.sh
```

Then Apptainer can be installed with:

```shell
spack install apptainer
# The following line  enables apptainer in the current shell.$
# This should be added to the .bashrc or alike to avoid being typed in every new shell.
spack load apptainer
```

## How to download MANTA's image

The following commands should download the Apptainer image `manta-apptainer_master.sif` in the current directory. This image is built nightly from the "master" branch of MANTA.

```shell
apptainer registry login --username <username> docker://registry.gitlab.com            #Login to registry. Useless when repo will be public
apptainer pull oras://registry.gitlab.com/manta-project/manta/manta-apptainer:master   #Pull the image
```

## How to build and run a C++ case with the Apptainer image

Let's build and run a C++ case that has the same structure as the
*examples* that can be found [here](https://gitlab.com/manta-project/manta/-/tree/master/examples). That C++
case will consist of a directory which contains at least a C++ source code
file with a `main` function, and a `CMakeLists.txt` specifiying how to build
this C++ file with MANTA.

In the following example, we will build and run the "charpy" commented example which can be found at:

Test case location

The test case can be found at:

[<MANTA REPO>/examples/commented_examples/](https://gitlab.com/manta-project/manta/-/tree/master/examples/commented_examples/)

The directory that the example is located at will be designated by `${CHARPY_EXAMPLE_SRC}`.
The Apptainer image is located in `${APPTAINER_IMAGE_DIR}`.

First one executes CMake and then build with make. In the Apptainer image, MANTA is installed in `/opt/manta`.

```shell
apptainer exec ${APPTAINER_IMAGE_DIR}/manta.sif cmake ${CHARPY_EXAMPLE_SRC} -DMANTA_INSTALL_DIR=/opt/manta
apptainer exec ${APPTAINER_IMAGE_DIR}/manta.sif make -j 8
```

Note

These commands use everything from the image: the compilers, CMake, make,
MANTA, ... There could be nothing but Apptainer on the host machine.

In this case one needs to generate the mesh using gmsh. The CMake execution
for this test copied the input gmsh file `charpy.geo` in the current working
directory. gmsh being available in the image, one can do:

```shell
apptainer exec ${APPTAINER_IMAGE_DIR}/manta.sif gmsh -3 charpy.geo
```

Note

If available, one could prefer to use the gmsh of the host machine, doing:

```shell
gmsh -3 charpy.geo
```

At last, one runs the MPI executable `main` which has been compiled:

```shell
mpirun -np 8 apptainer exec --bind /mnt/sandbox/:/mnt/sandbox ../manta.sif ./main
```

Note

MPI usage with Apptainer

This is where the magic happens: with this last command, one uses the MPI of
the host machine to execute through Apptainer the MPI executable `main`
which has been built using MANTA and MPI from within the image. Here 8
instances of Apptainer have been launched, each of them executing a single
instance of `main`.

One could have executed:

```shell
apptainer exec --bind /mnt/sandbox/:/mnt/sandbox ../manta.sif mpirun -np 8 ./main
```

But here, there is single instance of Apptainer launched, in which 8
instances of `main` have been launched using the image's MPI. This will
work, but restricts the MPI usage to the host machine alone, whereas
launching several instances of Apptainer with host related MPI allow to
run calculation on several computation nodes, as Apptainer itself can be
seen as a MPI executable. With the slurm job scheduler, one could launch a MPI
job with `srun -n X apptainer ...`.

## How to launch a Python calculation with the Apptainer image

To run a calculation defined with the frontend python API in a python script located on the host machine (an example script can be found at `$MANTA_SRC/apptainer/python_tests/shocktube-sod-test.py`), one can do:

```shell
apptainer exec manta.sif python simulation.py
```

And using MPI (see the [above note](#apptainer-mpi-note-label) for important details) :

```shell
mpirun -n 4 apptainer exec manta.sif python simulation.py
```

Note

One can launch a MANTA-aware python shell in the container

Example:

```shell
apptainer shell manta.sif
Apptainer>
Apptainer> python
Python 3.11.7 (main, Jul 30 2024, 12:51:22) [Clang 13.0.1 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import manta
>>> manta.info()
The following subsections are available:

- Solvers
- Model bricks
- Coupling schemes
- Properties
- Loadings
- Constraints
- Factories
- Models
- Post-Processings
>>> exit()
Apptainer> exit
exit
```

## A few pitfalls

### Symlinks in the path to the current working directory

By default, when the `apptainer exec` (or `apptainer shell` which can be
used to launch a shell inside the image) command is called, Apptainer
automatically mounts some directories of the host machine in the filesystem of
the container (see this [page](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html) for
details). In particular, it mounts the user's home directory and the current
working directory. This is what allows working seamlessly on files of the host
machine with command and executables from the image.

But as written in the Apptainer's [documentation](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html), these
convenient automatic mounts only work if there is no symlink resolving to
different locations on the host vs inside the container.

For example if the current working directory is
`/home/dvader/sandbox/work/`, and `sandbox` is actually a link to
`/mnt/sandbox`, then it will not work as expected as `/mnt/sandbox` is not
relevant in the container. In such a case, one can mount manually `/mnt/sandbox`:

```shell
apptainer exec --bind /mnt/sandbox/:/mnt/sandbox ...
```

### MPI version compatibility

The MANTA Apptainer image is built with a given MPI version. The version used for each Apptainer image can be found in the MANTA's main README file, which is visible at [this page](https://gitlab.com/manta-project/manta). You must use a "compatible" version of OpenMPI on your host machine. We recommend the following for version compatibility:

- Use the same version as in the image whenever possible.
- Do not use a different major version than the one in the image.
- The OpenMPI version on the host must be older or equal to the version inside the image.
