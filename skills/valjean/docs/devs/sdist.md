<!-- source: devs/sdist.rst -->

# Distributing the code

Two package management systems are currently supported: `pip` and `conda`.

All the packages, including the documentation package, are available in the `Fichiers` area of the valjean [Tuleap](https://codev-tuleap.intra.cea.fr/projects/valjean) page.

## Source distribution

### Creation

A source distribution can be created with the command:

    $ poetry build

This will produce a `valjean-{x.y.z}.tar.gz` source archive and a `valjean-{x.y.z}-py3-none-any.whl` in the `dist` folder. These files are suitable for the distribution of `valjean` to users and for installing it.

### Installation

The source distribution may be installed with:

    $ pip install /path/to/valjean-{x.y.z}.tar.gz

You can also install the wheel:

    $ pip install /path/to/valjean-{x.y.z}-py3-none-any.whl

Both commands should work.

Note

If the archives are built from an untagged commit, the archive name will contain the hash of the commit, like `valjean-{x.y}.dev{z}+g{hash}.tar.gz`.

## Conda package

### Creation

It is possible to create a conda package of `valjean` following these steps:

1.  Install `conda` with [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [anaconda](https://www.anaconda.com/download)

2.  Setup your conda workspace (`source MY/CONDA/PATH/bin/activate`)

3.  Create the `conda` package:

        $ cd /path/to/valjean
        $ conda build conda.recipe --python=PY_VERSION

The conda package should appear in the conda installation at the path: `MY/CONDA/PATH/conda-bld/linux-64/valjean-v{VERSION}-{NUMBER}_{HASH}_py{PY_VERSION}.tar.bz2` with:

- `VERSION`: last tag from valjean in the branch used to build the archive
- `NUMBER`: number of commits since this tag
- `HASH`: short hash of the commit used
- `PY_VERSION`: Python version.

The option `--python` is needed in the command to get the correct python version in the archive name (else it uses the default version of conda).

If the build corresponds to the tag and the hash seems useless, it is possible to modify or comment the string. Without the string the default name would be `valjean-v{VERSION}-py{PY_VERSION}_{NUMBER}.tar.bz2`.

### Installation

To install the conda package:

1.  Setup your favorite conda workspace

2.  Install the package:

        $ conda install -c file://PATH/TO/valjean-DETAILS.tar.bz2 --use-local valjean

with `DETAILS=v{VERSION}-{NUMBER}_{HASH}_py{PY_VERSION}`.

Offline installation can be done adding the `--offline` option.

## Documentation package

### Creation

Follow the documentation build steps in `building-documentation-dvpers`, then archive the `html` folder:

    $ cd doc/build
    $ tar czf valjean-doc-XXX.tar.gz --transform 's,^,valjean-doc-XXX/,' html

### Installation

To install the documentation:

    $ tar xzf valjean-doc-XXX.tar.gz
