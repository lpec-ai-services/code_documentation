<!-- source: modules/gavroche/diagnostics.rst -->

# `diagnostics` – Diagnostic tests

 Test and task statistics ------------------------

This module defines a few tests that report about the success/failure status of other tests/tasks.

Three different tests are available:

- statistics over all the tasks done, generated with `task_stats`
- statistics over all the tests performed with `test_stats`
- statistics over the tests performed based on labels given at test initialization with `test_stats_by_labels`

The two tests over the test results are performed using the `TestResult`, so the statistics only includes the tests that were actually run.

### `valjean.gavroche.diagnostics.stats.stats_worker(test_fn, name, description, tasks, **kwargs)`

Function creating the test for all the required tasks (summary tests of test tasks or summary tests on all tasks for example).

param test_fn  
function generating the test to apply to tasks

param str name  
the name of the stat task

param str description  
its description

param tasks  
the list of tasks to be tested.

type tasks  
list(Task)

returns  
an `EvalTestTask` that evaluates the diagnostic test.

rtype  
EvalTestTask

### `valjean.gavroche.diagnostics.stats.task_stats(*, name, description='', labels=None, tasks)`

Create a `TestStatsTasks` from a list of tasks.

The `TestStatsTasks` class must be instantiated with the list of task results, which are not available to the user when the tests are specified in the job file. Therefore, the creation of the `TestStatsTasks` must be delayed until the other tasks have finished and their results are available in the environment. For this purpose it is necessary to wrap the instantiation of `TestStatsTasks` in a `Use` wrapper, and evaluate the resulting test using a `EvalTestTask`.

This function hides this bit of complexity from the user. Assume you have a list of tasks that you would like to produce statistics about (we will use `DelayTask` objects for our example):

\>\>\> from valjean.cosette.task import DelayTask \>\>\> my_tasks = \[DelayTask(1), DelayTask(3), DelayTask(0.2)\]

Here is how you make a `TestStatsTasks`:

\>\>\> stats = task_stats(name='delays', tasks=my_tasks) \>\>\> from valjean.gavroche.eval_test_task import EvalTestTask \>\>\> isinstance(stats, EvalTestTask) True \>\>\> print(stats.depends_on) {Task('delays.stats')} \>\>\> create_stats = next(task for task in stats.depends_on)

Here `create_stats` is the task that actually creates the `TestStatsTasks`. It soft-depends on the tasks in `my_tasks`:

\>\>\> \[task in create_stats.soft_depends_on for task in my_tasks\] \[True, True, True\]

The reason why the dependency is soft is that we want to collect statistics about the task outcome in any case, even (especially!) if some of the tasks failed.

param str name  
the name of the task to create.

param str description  
its description.

param tasks  
the list of tasks to be tested.

type tasks  
list(Task)

returns  
an `EvalTestTask` that evaluates the diagnostic test.

rtype  
EvalTestTask

### `class valjean.gavroche.diagnostics.stats.NameFingerprint(name, fingerprint=None)`

A small helper class to store a name and an optional fingerprint for the referenced item.

### `class valjean.gavroche.diagnostics.stats.TestStatsTasks(*, name, description='', labels=None, task_results)  — bases: Test`

A test that evaluates statistics about the success/failure status of the given tasks.

#### `TestStatsTasks.evaluate(self)`

Evaluate this test and turn it into a `TestResultStatsTasks`.

#### `TestStatsTasks.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

### `class valjean.gavroche.diagnostics.stats.TestResultStatsTasks(*, test, classify)  — bases: TestResult`

The result of the evaluation of a `TestStatsTasks`. The test is considered successful if all the observed tasks have successfully completed (`TaskStatus.DONE`).

### `class valjean.gavroche.diagnostics.stats.TestOutcome  — bases: Enum`

An enumeration that represents the possible outcomes of a test:

`SUCCESS`  
represents tests that have been evaluated and have succeeded;

`FAILURE`  
represents tests that have been evaluated and have failed;

`MISSING`  
represents tasks that did not generate any `'result'` key;

`NOT_A_TEST`  
represents tasks that did not generate a `TestResult` object as a result;

### `valjean.gavroche.diagnostics.stats.test_stats(*, name, description='', labels=None, tasks)`

Create a `TestStatsTests` from a list of tests.

The `TestStatsTests` class must be instantiated with the list of test results, which are not available to the user when the tests are specified in the job file. Therefore, the creation of the `TestStatsTests` must be delayed until the test tasks have finished and their results are available in the environment. For this purpose it is necessary to wrap the instantiation of `TestStatsTests` in a `Use` wrapper, and evaluate the resulting test using a `EvalTestTask`.

This function hides this bit of complexity from the user. Assume you have a list of tasks that evaluate some tests and that you would like to produce statistics about the tests results. Let us construct a toy dataset first:

\>\>\> from collections import OrderedDict \>\>\> import numpy as np \>\>\> from valjean.eponine.dataset import Dataset \>\>\> x = np.linspace(-5., 5., num=100) \>\>\> y = x\**2 \>\>\> error = np.zeros_like(y) \>\>\> bins = OrderedDict(\[('x', x)\]) \>\>\> parabola = Dataset(y, error, bins=bins, name='parabola') \>\>\> parabola2 = Dataset(y*(1+1e-6), error, bins=bins, name='parabola2')

Now we write a function that generates dummy tests for the `parabola` dataset:

\>\>\> from valjean.gavroche.test import TestEqual, TestApproxEqual \>\>\> def test_generator(): ... result = \[TestEqual(parabola, parabola2, name='equal?').evaluate(), ... TestApproxEqual(parabola, parabola2, ... name='approx_equal?').evaluate()\] ... return {'test_generator': {'result': result}}, TaskStatus.DONE

We need to wrap this function in a PythonTask so that it can be executed as a part of the dependency graph:

\>\>\> from valjean.cosette.pythontask import PythonTask \>\>\> create_tests_task = PythonTask('test_generator', test_generator)

Here is how you make a `TestStatsTests` to collect statistics about the results of the generated tests:

\>\>\> stats = test_stats(name='equal', tasks=\[create_tests_task\])

\>\>\> from valjean.gavroche.eval_test_task import EvalTestTask \>\>\> isinstance(stats, EvalTestTask) True

Here `stats` evaluates the test that gathers the statistics, and it depends on a special task that generates the `TestStatsTests` instance:

\>\>\> print(stats.depends_on) {Task('equal.stats')} \>\>\> create_stats = next(task for task in stats.depends_on)

In turn, `create_stats` has a soft dependency on the task that generates our test, `create_tests_task`:

\>\>\> create_tests_task in create_stats.soft_depends_on True

The reason why the dependency is soft is that we want to collect statistics about the test outcome in any case, even (especially!) if some of the tests failed or threw exceptions.

Let's run the tests:

\>\>\> from valjean.config import Config \>\>\> config = Config() \>\>\> from valjean.cosette.env import Env \>\>\> env = Env() \>\>\> for task in \[create_tests_task, create_stats, stats\]: ... env_up, status = task.do(env=env, config=config) ... env.apply(env_up) \>\>\> print(f"Task status: {status.name}") Task status: DONE

The results are stored in a `list` under the key `'result'`:

\>\>\> print(len(env\[stats.name\]\['result'\])) 1 \>\>\> stats_res = env\[stats.name\]\['result'\]\[0\] \>\>\> print("SUCCESS:", stats_res.classify\[TestOutcome.SUCCESS\]) SUCCESS: \['approx_equal?'\] \>\>\> print("FAILURE:", stats_res.classify\[TestOutcome.FAILURE\]) FAILURE: \['equal?'\]

param str name  
the name of the task to create.

param str description  
its description.

param tasks  
the list of tasks that generate the tests to observe.

type tasks  
list(Task)

returns  
an `EvalTestTask` that evaluates the diagnostic test.

rtype  
EvalTestTask

### `class valjean.gavroche.diagnostics.stats.TestStatsTests(*, name, description='', labels=None, task_results)  — bases: Test`

A test that evaluates statistics about the success/failure of the given tests.

#### `TestStatsTests.evaluate(self)`

Evaluate this test and turn it into a `TestResultStatsTests`.

#### `TestStatsTests.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

### `class valjean.gavroche.diagnostics.stats.TestResultStatsTests  — bases: TestResultStatsTasks`

The result of the evaluation of a `TestStatsTests`. The test is considered successful if all the observed tests have been successfully evaluated and have succeeded.

### `valjean.gavroche.diagnostics.stats.test_stats_by_labels(*, name, description='', labels=None, tasks, by_labels)`

Create a `TestStatsTestsByLabels` from a list of tests.

See `test_stats` for the generalities about this function.

Compared to `test_stats` it takes one argument more: `'by_labels'` to classify then build statistics based on these labels. **The order of the labels matters**, as they are successively selected.

Let's define three menus:

\>\>\> menu1 = {'food': 'egg + spam', 'drink': 'beer'} \>\>\> menu2 = {'food': 'egg + bacon', 'drink': 'beer'} \>\>\> menu3 = {'food': 'lobster thermidor', 'drink': 'brandy'}

These three menus are ordered by pairs. Statistics on meals are kept in the restaurant, using `TestMetadata`. The goal of the tests is to know if both persons of a pair order the same menu and when they do it.

``` 
orders = [TestMetadata(
    {'Graham': menu1, 'Terry': menu1}, name='gt_wday_lunch',
    labels={'day': 'Wednesday', 'meal': 'lunch'}),
          TestMetadata(
    {'Michael': menu1, 'Eric': menu2}, name='me_wday_dinner',
    labels={'day': 'Wednesday', 'meal': 'dinner'}),
          TestMetadata(
    {'John': menu2, 'Terry': menu2}, name='jt_wday',
    labels={'day': 'Wednesday'}),
          TestMetadata(
    {'Terry': menu3, 'John': menu3}, name='Xmasday',
    labels={'day': "Christmas Eve"})]
```

The restaurant owner uses `test_stats_by_labels` to build statistics on his menus and the habits of his consumers.

For example, the menus filtered on `day` will give:

``` 
=============  ============  =============
      day       % success      % failure
=============  ============  =============
Christmas Eve      1/1            0/1
    Wednesday      2/3            1/3
=============  ============  =============
```

These results means, considering the tests requested, both consumers have the same meal on Christmas Eve. On Wednesday, one pair of customers out of three did not order the same menu.

The same kind of statistics can be done based on the meal:

``` 
==========  ============  =============
   meal       % success     % failure
==========  ============  =============
  dinner         0/1            1/1
   lunch         1/1            0/1
==========  ============  =============
```

In that case two tests were not taken into account as they did not have any `'meal'` label.

It is also possible to make selections on multiple labels. In that case the order matters: the classification is performed following the order of the labels requested. For example, `'meal'` then `'day'` :

``` 
==========  =========  ============  =============
   meal        day       % success     % failure
==========  =========  ============  =============
  dinner    Wednesday       0/1            1/1
   lunch    Wednesday       1/1            0/1
==========  =========  ============  =============
```

- Only two tests are filtered due to the meal selection
- Requesting `'day'` then `'meal'` would only inverse the two first columns in that case and emit a **warning**: a preselection on `'day'` is done and in Christmas Eve case the `'meal'` label is not provided, the selection cannot be done. In the Wednesday one, no problem `'meal'` appears at least in one case (two in our cases).

Finally if the request involves a label that does not exist in any test an exception will be raised, mentioning the failing label.

param str name  
the name of the task to create.

param str description  
its description.

param tasks  
the list of tasks that generate the tests to observe.

type tasks  
list(Task)

param tuple(str) by_labels  
labels from the tests on which the classification will be based

returns  
an `EvalTestTask` that evaluates the diagnostic test.

rtype  
EvalTestTask

### `class valjean.gavroche.diagnostics.stats.TestStatsTestsByLabelsException  — bases: Exception`

Exception raised during the diagnostic test on `TestResult` when a classification by labels is required.

### `class valjean.gavroche.diagnostics.stats.TestStatsTestsByLabels(*, name, description='', labels=None, task_results, by_labels)  — bases: Test`

A test that evaluates statistics about the success/failure of the given tests using their labels to classify them.

Usually more than one test is performed for each tested case. This test summarize tests done on a given category defined by the user in the usual tests (`TestStudent`, `TestMetadata`, etc.).

During the evaluation a list of dictionaries of labels is built for each test. These labels are given by the user at the initialization of the test. Each dictionary also contains the name of the test (name of the task) and its result (sucess or failure). From this list of dictionaries an `Index` is built.

The result of the evaluation is given a a list of dictionaries containing the strings corresponding to the chosen labels under the `'labels'` key and the number of results OK, KO and total.

#### `TestStatsTestsByLabels.evaluate(self)`

Evaluate this test and turn it into a `TestResultStatsTestsByLabels`.

#### `TestStatsTestsByLabels.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

### `class valjean.gavroche.diagnostics.stats.TestResultStatsTestsByLabels(*, test, classify, n_labels)  — bases: TestResultStatsTasks`

The result of the evaluation of a `TestStatsTestsByLabels`. The test is considered successful if all the observed tests have been successfully evaluated and have succeeded.

An oracle is available for each individual test (usually what is required here).

`self.classify` is here a list of dictionaries with the following keys: `['labels', 'OK', 'KO', 'total']`.

#### `TestResultStatsTestsByLabels.oracles(self)`

Test if each test is successful.

rtype  
list(bool)

#### `TestResultStatsTestsByLabels.nb_missing_labels(self)`

Return the number of tests where at least one of the labels required were missing.

rtype  
int

### `valjean.gavroche.diagnostics.stats.classification_counts(classify, status_first)`

Count the occurrences of different statuses in the `classify` dictionary.

param dict classify  
a dictionary associating *things* to statuses. The statuses must have the same type as `status_first`

param status_first  
the status that is considered as success. This must be an enum class

returns  
a pair of lists of equal length. The first element of the pair is the list of statuses appearing in `classify` (`status_first` is guaranteed to come first in this list); the second element is the number of times the corresponding status appears in `classify`. Test of metadata ----------------

This module define tests for metadata.

### `class valjean.gavroche.diagnostics.metadata.Missing`

Class for missing metadata.

### `class valjean.gavroche.diagnostics.metadata.TestResultMetadata(test, dict_res)  — bases: TestResult`

Results of metadata comparisons.

#### `TestResultMetadata.per_key(self)`

Test result sorted by key.

#### `TestResultMetadata.only_failed_comparisons(self)`

Return only the failed comparisons. Structure is the same as the `dict_res`.

### `class valjean.gavroche.diagnostics.metadata.TestMetadata(dict_md, name, description='', labels=None, exclude=('results', 'index', 'score_index', 'response_index', 'response_type'))  — bases: Test`

A test that compares metadata.

Document the parameters...

#### `TestMetadata.build_metadata_dict(self)`

Build the dictionary of metadata.

Contains all the metadata for all samples.

#### `TestMetadata.compare_metadata(self)`

Metadata are compared with respect to the first one.

#### `TestMetadata.evaluate(self)`

Evaluate this test and turn it into a `TestResultMetadata`.

#### `TestMetadata.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.
