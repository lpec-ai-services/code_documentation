<!-- source: devs/testing.rst -->

# Testing

## Unit tests

`valjean` uses [pytest](https://docs.pytest.org/en/latest) as a unit-test framework; some of the unit tests rely on the [hypothesis](https://hypothesis.readthedocs.io/en/latest/) package for property-based testing. The tests are defined in the `tests` folder and are automatically discovered by [pytest](https://docs.pytest.org/en/latest).

You can run the unit-test suite with:

    $ pytest

This will run the tests and produce a summary report. Additionally, [pytest](https://docs.pytest.org/en/latest) will calculate code coverage; a text report will be printed to stdout, and a nice HTML report will be written to `tests/htmlcov`.

The default `pytest` options are defined in the `pytest.ini` file, and `coverage` options are defined in `.coveragerc`, using [pytest-doc](https://pytest-cov.readthedocs.io/en/latest/). Extra options to `pytest` can be passed on the command line:

    $ pytest tests/cosette/test_rlist.py  # run all tests in the named file
    $ pytest tests/cosette/test_rlist.py::test_insert  # run this test only
    $ pytest -k depgraph        # only run tests whose name matches "depgraph"
    $ pytest -v                 # increase verbosity level by number of v
    $ pytest --verbosity=N      # set verbosity test output
    $ pytest -x                 # stop on the first test failure
    $ pytest --ff               # run previously failed tests first

The `--verbosity` option sets all the `valjean` loggers to the verbosity level N. `N=0` is equivalent to `WARNING`, `N=1` to `INFO` (default) and `N>1` to `DEBUG`. The verbosity level can also be increased by invoking the `-v` option, possibly multiple times. It is useful when debugging a failing test.

## Property-based testing and the [hypothesis](https://hypothesis.readthedocs.io/en/latest/) package

In traditional unit testing, one verifies that the code gives the expected answer for a given, fixed set of input values. For instance, one may test a sort algorithm by verifying that it produces `[1,2,3,4]` when fed `[4,2,3,1]`. However, this does not check that the algorithm behaves sensibly on any of the following arguments:

- empty lists;
- long lists;
- lists that are already sorted;
- lists of objects other than integers...

You see the point. One could write additional, specific unit tests to address each of these limitations. However, it is impossible to make sure that we have not forgotten some important edge case; also, we will need to write essentially the same tests over and over, and nobody likes doing the same thing over and over. But wait a minute, isn't "doing the same thing over and over" the kind of thing that computers are actually good at?

Enter *property-based testing*. The idea of this approach is that the developer should only check the expected properties of the code to be tested. For instance, in the case of the sort algorithm, the developer could check the following invariants about the list returned by the algorithm:

- it is sorted;
- it contains the same elements as the input list.

The testing library will generate a number of random inputs, call the sorting algorithm on each of them and check that the properties specified by the developer hold. If a counterexample is found, it will be shown to the user.

In Python, the [hypothesis](https://hypothesis.readthedocs.io/en/latest/) library offers a flexible and [well-documented API](https://hypothesis.readthedocs.io/en/latest/) for property-based testing. Additionally, [hypothesis](https://hypothesis.readthedocs.io/en/latest/) is well integrated with `pytest`. `valjean` unit tests leverage [hypothesis](https://hypothesis.readthedocs.io/en/latest/) whenever possible.

If you want some examples within `valjean`, a good place to start is the `tests.cosette.test_rlist` test module, which tests the invariants of the `RList` class.

## Testing example docstrings with [pytest](https://docs.pytest.org/en/latest)

Sometimes the docstrings contain example code such as the following:

``` python
>>> print(1+2)
3
```

These examples are also automatically tested with [pytest](https://docs.pytest.org/en/latest).

## `tox` integration

There are specific `tox` test environments to run the unit tests. Check the page about `using tox for continuous integration`.
