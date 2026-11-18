<!-- source: devs/documentation.rst -->

# Building the documentation

`valjean` uses the [sphinx](https://www.sphinx-doc.org/en/master/) package for its own documentation. Before building the documentation, you will need to install `valjean`, as explained in `the installation section`.

The HTML documentation can be built with:

    $ cd doc && make html
    $ sphinx-build -a src build/html  # equivalently

The documentation will appear in `doc/build/html` and can be browsed starting with the `index.html` file.

`sphinx` is also able to build a LaTeX version of the documentation with:

    $ cd doc && make latex
    $ sphinx-build -a -b latex src build/latex  # equivalently

This will dump the LaTeX sources in `doc/build/latex`, where you can compile them to PDF with `make`.

The automatic documentation for the tests can be built by adding the `-t tests` option to `sphinx-build`:

    $ sphinx-build -a -t tests src build/html

The documentation also contains a few examples in IPython notebook format. Conversion of the notebooks to HTML requires `pandoc`, which needs to be separately installed. Conversion of the notebooks is enabled by default. To deactivate it, pass the `-t no_notebooks` option to `sphinx-build`:

    $ sphinx-build -a -t no_notebooks src build/html

The `-t tests` and `-t no_notebooks` can be used together.

The `sphinx` system is deeply customizable; most of the options are set in `doc/src/conf.py`, which is fairly well documented.

## Version numbering weirdness

By default, the version number in the `sphinx` documentation is extracted from the **installed** version of `valjean`, and **not** the version in the current directory. If you are building the package documentation locally, then it doesn't really matter, but if you are building the documentation because you want to distribute the code to your users, **remember to install the package first!** It is simple:

    $ cd /path/to/valjean  # the path containing pyproject.toml
    $ pip install -U .[dev]
    $ cd doc && make html

You will find the full recipe in `distributing-code`.

## Extensions

We use a few `sphinx` extensions:

`autodoc`  
Extracts the docstrings from the Python code and turns them into documentation.

`doctest`  
Runs the example code included in the docstrings, in the form of code execution at a Python prompt.

`intersphinx`  
Add hyperlinks to `sphinx` documentation outside the current project (for instance, in the Python standard library).

`graphviz`  
Include `dot` graphs inline, render them when the documentation is built.

`todo`  
Add TODO items, collect all of them in one place.

`coverage`  
Measure documentation coverage. To use it:

    $ cd doc
    $ make coverage

`viewcode`  
Add links to the source code.

`imgmath`  
Allows to write in math mode.

`plot_directive`  
Generate [matplotlib](https://matplotlib.org/) plots from code included in the docs.

## Checking references

To check internal references the `nitpicky` option can be used:

    $ sphinx-build -a -n src build/html

from the `doc` folder, `-n` to activate the `nitpicky` option and `-a` (optional) to reconstruct documentation for all files.

## Checking external links

The special `linkcheck` builder can be used to check any external links found in the documentation. Of course you must run the check from a machine with good network connectivity. The command is:

    $ sphinx-build -a -b linkcheck src build/linkcheck

## Building the documentation for the tests

The documentation for the unit tests is not built by default. If you want to build it, you should pass the `tests` tag to `sphinx-build`:

    $ cd doc
    $ sphinx-build -a -t tests src build/html

## `tox` integration

There is a specific `tox` test environment to build the documentation. Check the page about `using tox for continuous integration`.
