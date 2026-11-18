<!-- source: getting_started/install.rst -->

# Installing `valjean`

## Requirements

`valjean` requires Python \>= 3.6. The package dependencies are handled by the build system.

## Getting the code

`valjean` is available on [GitHub](https://github.com/valjean-framework/valjean). It can be downloaded using:

    $ git clone https://github.com/valjean-framework/valjean.git

## Quick start

For those in a rush:

    $ python3 -m venv ~/venv-valjean
    $ source ~/venv-valjean/bin/activate
    (venv-valjean) $ pip install --upgrade pip
    (venv-valjean) $ pip install /path/to/valjean

Note

`/path/to/valjean` is the location of the package sources.

## Using virtual environments

The `valjean` package can be installed like a normal Python package, using the [pip](https://pip.pypa.io/en/stable) package manager.

The recommended way to install `valjean` is to use a *virtual environment*. At the time of writing, the preferred solution to create virtual environments is the `venv` module from the standard Python distribution:

    $ python3 -m venv ~/venv-valjean
    $ source ~/venv-valjean/bin/activate
    (valjean) $ pip install /path/to/valjean-x.y.z

Note

Ancient versions of `pip` (`<19.0`) will not be able to install `valjean`, because `valjean` uses a `pyproject.toml` file to describe the build, as specified in the `517` and `518` formats. If you are using an old version of `pip`, you should upgrade it (after activating the virtual environment) with:

    (venv-valjean) $ pip install --upgrade pip

## Prerequisites

`valjean` depends on a number of Python packages. You don't have to do anything special to install most of these packages, since `pip` should take care of everything. The one exception for the moment is [h5py](https://docs.h5py.org/en/stable/), which will not work unless the HDF5 library is installed on your machine.

## Using conda

It is also possible to use `valjean` from a `conda` environment. The first step is to install [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [anaconda](https://www.anaconda.com/download). The former is a light installation of python and only required packages will be installed. The latter is a full installation and can be used offline. Once the installation is done, you should run:

    $ source PATH/TO/CONDA/bin/activate

unless you have set up your shell to do that automatically for you.

The recommended way to install `valjean` with `conda` is to create a `conda` environment for the package and all of its dependencies:

    (base) $ conda create -n MY_ENV python=PY_VERSION
    (base) $ conda activate MY_ENV
    (MY_ENV) $ conda install -c file://PATH/TO/valjean-DETAILS.tar.bz2 --use-local valjean

`DETAILS` stands for `v{VERSION}-{NUMBER_HASH}_{pyPY_VERSION}` with:

- `VERSION`: last tag from valjean in the branch used to build the archive
- `NUMBER`: number of commits since this tag
- `HASH`: short hash of the commit used
- `PY_VERSION`: python version used to build the archive, the version used for the installation should be the same.

This procedure should allow to use `valjean` from the python interpreter, from a [jupyter](https://docs.jupyter.org/en/latest/) notebook or directly with the `valjean` command.

Note: only the `valjean` package is installed at that step, the others (`numpy`, `pyparsing`, ...) will be installed when running `valjean`. If you want to use `valjean` directly in python you'll probably need to install the required packages using `conda install PACKAGE`.

An offline installation is possible adding the `--offline` option in the installation command line. As a consequence updates of packages won't be possible, i.e. they will come from the available ones in the local installation of `conda`. The Python version of the package should probably be the default one of `conda`.

The conda package is not editable. If you prefer to use an editable version of `valjean` associated with conda it would probably be easier to use conda to get the python version, then install the package via `pip` or `poetry`. Virtual environnment have to be treated carefully in that case. To get an editable version offline fully working it might be necessary to install all (direct and indirect) dependencies.

## Checking package integrity

The `md5sum` of the archives (`pip` or `conda` installation) are given in Tuleap. To check them, just type `md5sum MY_ARCHIVE` and compare the obtained hash with the one stored on Tuleap.
