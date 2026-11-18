<!-- source: devs/tox.rst -->

# Using `tox` for continuous integration

Unit tests, linting and documentation checks are part of the continuous integration (CI) suite. We use [tox](https://tox.wiki/en/latest/) to orchestrate the tests and run the tests with different Python versions.

## Configuration

The `tox` configuration is included in the `pyproject.toml` file.

## Available test environments

In CI, the unit tests are run for several versions of Python (at the time of writing, all the supported versions are tested). For the most recent Python version (3.9 at the time of writing), the CI environment provides the optional [ROOT](https://root.cern.ch/) dependency, which makes it possible to run the tests for the `depletion` module. For this reason, we pass the `PYTHONPATH` environment variable into the test environment.

## Additional environments

There are three additional test environments, with specific purposes:

- `docs`: `builds the documentation`, with and without the `tests` tag, in `nitpicky mode`. It also runs `the linkcheck builder` to check for broken or redirecting external links.
- `linting`: `runs the linters`.
- `parsing`: runs all the unit tests, plus the specific (slow) parsing tests on the outputs of older TRIPOLI-4 versions.

## Using `tox` from the command line

You can use `tox` to run your tests, build the documentation or lint the code from the command line. First, install `tox` in your `virtual environment`:

    $ pip install tox

- To run the unit tests:

      $ tox -e py39 valjean tests  # for Python 3.9, for example

  You need to specify the Python version on the command line.

- Building the documentation:

      $ tox -e docs

- Linting:

      $ tox -e linting valjean tests
