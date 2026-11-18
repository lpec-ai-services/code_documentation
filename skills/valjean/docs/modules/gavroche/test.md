<!-- source: modules/gavroche/test.rst -->

# `test` – Domain-specific language for writing tests

Domain-specific language for writing numeric tests.

This module provides a few classes and functions to write numeric tests.

Let us import the relevant modules first:

> \>\>\> from collections import OrderedDict \>\>\> from valjean.eponine.dataset import Dataset \>\>\> import numpy as np

Now we create a toy data set:

> \>\>\> x = np.linspace(-5., 5., num=100) \>\>\> y = x\*\*2 \>\>\> error = np.zeros_like(y) \>\>\> bins = OrderedDict() \>\>\> bins\['x'\] = x \>\>\> parabola = Dataset(y, error, bins=bins)

We perturb the data by applying some small amount of noise:

> \>\>\> eps = 1e-8 \>\>\> noise = np.random.uniform(-eps, eps, parabola.shape) \>\>\> y2 = y + noise \>\>\> parabola2 = Dataset(y2, error, bins=bins)

Now we can test if the new dataset is equal to the original one:

> \>\>\> from valjean.gavroche.test import TestEqual \>\>\> test_equality = TestEqual(parabola, parabola2, name="parabola", ... description="equality test") \>\>\> test_equality_res = test_equality.evaluate() \>\>\> print(bool(test_equality_res)) False

However, they are approximately equal:

> \>\>\> from valjean.gavroche.test import TestApproxEqual \>\>\> test_approx = TestApproxEqual(parabola, parabola2, name="parabola", ... description="approx equal test") \>\>\> test_approx_res = test_approx.evaluate() \>\>\> print(bool(test_approx_res)) True

### `class valjean.gavroche.test.CheckBinsException  — bases: Exception`

An error is raised when check bins fails.

### `valjean.gavroche.test.same_arrays(arr1, arr2)`

Return `True` if `arr1` and `arr2` are equal.

param arr1  
the first array.

param arr2  
the second array.

### `valjean.gavroche.test.same_bins(bins1, bins2)`

Return `True` if all the coordinate arrays are compatible.

param bins1  
the first dictionary of coordinate arrays.

param bins2  
the second dictionary of coordinate arrays.

### `valjean.gavroche.test.same_bins_datasets(*datasets)`

Return `True` if all datasets have the same coordinates.

param datasets  
any number of datasets.

type datasets  
`Dataset`

### `valjean.gavroche.test.check_bins(*datasets)`

Check if the datasets have compatible coordinates, raise if not.

raises ValueError  
if the datasets do not have compatible coordinates.

### `class valjean.gavroche.test.Test(*, name, description='', labels=None)  — bases: ABC`

Generic class for comparing any kind of results.

Base class for tests.

#### `Test.evaluate(self)`

Evaluate the test on the given inputs.

Must return a subclass of `TestResult`.

#### `Test.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

### `class valjean.gavroche.test.TestDataset(dsref, *datasets, name, description='', labels=None)  — bases: Test`

Generic class for comparing datasets.

#### `TestDataset.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

#### `TestDataset.evaluate(self)`

Evaluate the test on the given datasets.

Must return a subclass of `TestResult`.

### `class valjean.gavroche.test.TestResult(test)  — bases: ABC`

Base class for test results.

This result should be filled by `Test` daughter classes.

### `class valjean.gavroche.test.TestResultFailed(test, msg)  — bases: TestResult`

Class for failed TestResults when an exception was raised during the evaluation.

### `class valjean.gavroche.test.TestResultEqual(test, equal)  — bases: TestResult`

Result from `TestEqual`.

### `class valjean.gavroche.test.TestEqual  — bases: TestDataset`

Test if the datasets values are equal. Errors are ignored.

#### `TestEqual.evaluate(self)`

Evaluation of `TestEqual`.

returns  
`TestResultEqual`

#### `TestEqual.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

### `class valjean.gavroche.test.TestResultApproxEqual(test, approx_equal)  — bases: TestResult`

Result from `TestApproxEqual`.

### `class valjean.gavroche.test.TestApproxEqual(dsref, *datasets, name, description='', labels=None, rtol=1e-05, atol=1e-08)  — bases: TestDataset`

Test if the datasets values are equal within the given tolerances. Errors are ignored.

#### `TestApproxEqual.evaluate(self)`

Evaluation of `TestApproxEqual`.

returns  
`TestResultApproxEqual`

#### `TestApproxEqual.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.
