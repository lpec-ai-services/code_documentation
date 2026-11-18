<!-- source: devs/setup.rst -->

# Installation and setup

`valjean` uses `pyproject.toml` file for packaging and dependency management as recommended in `517`, `518` and `621`.

If you plan to develop `valjean` and you have checked out the source repository, you need to install it in development mode:

    $ python3 -m venv ~/venv-valjean-dev
    $ source ~/venv-valjean-dev/bin/activate
    $ pip install -U pip
    (venv-valjean-dev) $ cd /path/to/valjean-X.Y.Z
    (venv-valjean-dev) $ pip install -e .[dev]

This will install `valjean` and all of its dependencies in your current virtual environment. The development dependencies (e.g. `sphinx`, `pytest`, etc.) will also be installed; if you want to skip them, omit the `[dev]` string from the `pip install` command:

    $ pip install -e .

This procedure should install just a link to your source folder `/path/to/valjean-X.Y.Z`, instead of copying the source files to the installation directory. This way, you will not need to reinstall the package every time you modify the sources.

You can also install `valjean` with [poetry](https://python-poetry.org/), version \> 1.3 and `python > 3.7`:

    $ python3 -m venv ~/venv-valjean-dev
    $ source ~/venv-valjean-dev/bin/activate
    $ pip install -U pip
    $ pip install poetry
    (venv-valjean-dev) $ cd /path/to/valjean-X.Y.Z
    (venv-valjean-dev) $ poetry install -E dev

## Dependency management

Developers should think about updating the package constraints in `pyproject.toml` when needed using [poetry](https://python-poetry.org/) or directly.

See the [poetry](https://python-poetry.org/) documentation for more information about adding or upgrading dependencies.
