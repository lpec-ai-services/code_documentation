<!-- source: modules/javert/table_repr.rst -->

# `table_repr` – Transform test results into `TableTemplate`

Module containing all available methods to convert a test result in a table to be converted in rst.

### `valjean.javert.table_repr.repr_bins(dsref)`

Representation of bins in tables.

When bins are given by edges, representation is `min - max`, when they are given at center, representation is `center`.

Trivial dimensions are not represented, i.e. dimensions where there is only one bin.

If there are more than one non-trivial dimensions, some repetition is expected. For example with two non-trivial dimensions of two bins each one point will be defined by its coordinated in the two dimensions and we expect all the bins to possibily be shown in a table. We expected 4 bins and their associated values in that case.

Let's consider the following dataset: \>\>\> from valjean.eponine.dataset import Dataset \>\>\> import numpy as np \>\>\> from collections import OrderedDict

\>\>\> vals = np.arange(6).reshape(1, 2, 1, 3, 1) \>\>\> errs = np.array(\[0.1\]\*6).reshape(1, 2, 1, 3, 1) \>\>\> bins = OrderedDict(\[('bacon', np.array(\[0, 1\])), ... ('egg', np.array(\[0, 2, 4\])), ... ('sausage', np.array(\[10, 20\])), ... ('spam', np.array(\[-5, 0, 5\])), ... ('tomato', np.array(\[-2, 2\]))\]) \>\>\> ds = Dataset(vals, errs, bins=bins) \>\>\> names, rbins = repr_bins(ds) \>\>\> print(list(ds.bins.keys())) \['bacon', 'egg', 'sausage', 'spam', 'tomato'\] \>\>\> print(names) \['egg', 'spam'\] \>\>\> print(ds.shape) (1, 2, 1, 3, 1) \>\>\> print(\[rb.shape for rb in rbins\]) \[(1, 2, 1, 3, 1), (1, 2, 1, 3, 1)\]

`'bacon'` and `'sausage'` are trivial dimensions, so won't be represented in the table, but we expect 6 values corresponding to 2 bins in `'egg'` and 3 in `'spam'`. Each value corresponds to a line in the table so each columns should have the same size and the same shape, the shape of the given dataset without trivial dimensions. We then have 3 `'spam'` bins in each `'egg'` bins or 2 `'egg'` bins in each `'spam'` bins. Each couple appears only once.

\>\>\> for name, rbin in zip(names, rbins): ... print(name, ':', rbin.flatten()) egg : \['0 - 2' '0 - 2' '0 - 2' '2 - 4' '2 - 4' '2 - 4'\] spam : \['-5' '0' '5' '-5' '0' '5'\]

As expected from the bins, `'egg'` bins are given by edges (`min - max`) while `'spam'` bins are given by center (`center`).

param dsref  
dataset

type dsref  
Dataset

returns  
list of the non-trivial dimensions and a tuple of the bins

rtype  
(list(str), tuple(numpy.ndarray))

The tuple must have the same length as the list of dimensions and the bins inside must have the same shape as `dsref.value`.

### `valjean.javert.table_repr.repr_testresultequal(result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestEqual` test.

param TestResultEqual result  
a test result.

param Verbosity verbosity  
verbosity level

returns  
list of templates representing a `TestResultEqual`

### `valjean.javert.table_repr.repr_equal_summary(result)`

Function to generate a summary table for the equal test (only tells if the test was successful or not).

param TestResultEqual result  
a test result.

rtype  
list(TextTemplate)

### `valjean.javert.table_repr.repr_equal(result)`

Representation of equal test.

param TestResultEqual result  
a test result.

returns  
Representation of a `TestResultEqual` as a table.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_testresultapproxequal(result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestApproxEqual` test.

param TestResultApproxEqual result  
a test result.

param Verbosity verbosity  
verbosity level

returns  
list of templates representing a `TestResultApproxEqual`

### `valjean.javert.table_repr.repr_approx_equal_summary(result)`

Function to generate a summary table for the approx equal test (only tells if the test was successful or not).

param TestResultApproxEqual result  
a test result.

rtype  
list(TextTemplate)

### `valjean.javert.table_repr.repr_approx_equal(result)`

Representation of approx equal test.

param TestResultApproxEqual result  
a test result.

returns  
Representation of a `TestResultApproxEqual` as a table.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_testresultstudent(result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestStudent` test.

param TestResultStudent result  
a test result.

param Verbosity verbosity  
verbosity level

returns  
list of templates representing a `TestResultStudent`

### `valjean.javert.table_repr.repr_student(result)`

Representation of Student test result.

param TestResultStudent result  
a test result.

returns  
Representation of a `TestResultStudent` as a table.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_student_silent(_result)`

Function to generate a silent table for the Student test (only tells if the test was successful or not).

param TestResultStudent result  
a Student test result.

returns  
empty list

### `valjean.javert.table_repr.repr_student_summary(result)`

Function to generate a summary table for the Student test (only tells if the test was successful or not).

param TestResultStudent result  
a Student test result.

rtype  
list(TextTemplate)

### `valjean.javert.table_repr.repr_student_intermediate(result)`

Function to generate an intermediate table for the Student test: print all the failing results.

param TestResultStudent result  
a Student test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_testresultbonferroni(result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestBonferroni` test.

Only represents the Bonferroni result, not the input test result.

param TestResultBonferroni result  
a test result.

param Verbosity verbosity  
verbosity level

returns  
list of templates representing a `TestResultBonferroni`

### `valjean.javert.table_repr.repr_bonferroni(result)`

Reprensetation of Bonferroni test result.

Only represents the Bonferroni result, not the input test result.

param TestResultBonferroni result  
a test result.

returns  
Representation of a `TestResultBonferroni` as a table.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_bonferroni_summary(result)`

Represent the result of a `TestBonferroni` test for the SUMMARY level of verbosity.

param TestResultBonferroni result  
a test result.

returns  
Representation of a `TestResultBonferroni` as a table.

rtype  
list(TextTemplate)

### `valjean.javert.table_repr.repr_testresultholmbonferroni(result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestHolmBonferroni` test.

param TestResultHolmBonferroni result  
a test result.

param Verbosity verbosity  
verbosity level

returns  
list of templates representing a `TestResultHolmBonferroni`

### `valjean.javert.table_repr.repr_holm_bonferroni(result)`

Reprensetation of Holm-Bonferroni test result.

Only represents the Holm-Bonferroni result, not the input test result.

param TestResultHolmBonferroni result  
a test result.

returns  
Representation of a `TestResultHolmBonferroni` as a table.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_holm_bonferroni_summary(result)`

Represent the result of a `TestHolmBonferroni` test for the SUMMARY level of verbosity.

param TestResultHolmBonferroni result  
a test result.

returns  
Representation of a `TestResultHolmBonferroni` as a table.

rtype  
list(TextTemplate)

### `valjean.javert.table_repr.percent_fmt(num, den)`

Format a fraction as a percentage. Example:

\>\>\> percent_fmt(2, 4) '2/4 (50.0%)' \>\>\> percent_fmt(0, 3) '0/3 (0.0%)' \>\>\> percent_fmt(7, 7) '7/7 (100.0%)' \>\>\> percent_fmt(0, 0) '0/0 (???%)'

param int num  
the numerator.

param int den  
the denominator.

rtype  
str

### `valjean.javert.table_repr.repr_testresultstatstasks(result, verbosity=Verbosity.DEFAULT)`

Represent a `TestResultStatsTasks` as a table. The table breaks down the tasks by status.

param TestResultStatsTasks result  
the test result to represent.

param Verbosity verbosity  
verbosity level

returns  
list of templates representing the test result.

### `valjean.javert.table_repr.repr_testresultstatstests(result, verbosity=Verbosity.DEFAULT)`

Represent a `TestResultStatsTests` as a table. The table breaks down the tests by success status.

param TestResultStatsTests result  
the test result to represent.

param Verbosity verbosity  
verbosity level

returns  
the tables representing the test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_testresultstats(result, status_ok, label)`

Helper function for `repr_testresultstatstests` and `repr_testresultstatstasks`. It generates a table with the `status_ok` value in the first row. Non-null results in other rows are considered as failures, and are highlighted if the count is non-zero. Null results are omitted from the table.

param result  
the test result to represent.

type result  
TestResultStatsTasks or TestResultStatsTests

param status_ok  
the status value that must be considered as a success.

param str label  
the type of things that we are testing (`'tests'` or `'tasks'`)

returns  
the tables representing the test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_testresultstatstestsbylabels(result, verbosity=Verbosity.DEFAULT)`

Represent a `TestResultStatsTestsByLabels` as tables. Shape of the table may change according to the number of flags required.

param TestResultStatsTestsByLabels result  
the test result to represent.

param Verbosity verbosity  
verbosity level

returns  
the tables representing the test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_testresultstatsbylabels(result)`

Function to print detailed statistics on tests, per category and sample run.

param TestResultStatsTestsByLabels result  
the test result to represent.

returns  
the tables representing the test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_testresultstatsbylabels_summary(result)`

Function to print detailed statistics on tests, per category and sample run in summary case: only print failed cases.

param TestResultStatsTestsByLabels result  
the test result to represent.

returns  
the tables representing the test result.

rtype  
list(TableTemplate), list(TextTemplate)

### `valjean.javert.table_repr.repr_testresultmetadata(result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestMetadata` test.

param TestResultMetadata result  
a test result.

param Verbosity verbosity  
verbosity level

returns  
list of templates representing a `TestResultMetadata`

### `valjean.javert.table_repr.repr_metadata(result)`

Function to generate a table from the metadata test results.

param TestResultMetadata result  
a test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_metadata_full_details(result)`

Function to generate a table from the metadata test results.

param TestResultMetadata result  
a test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_metadata_intermediate(result)`

Function to generate a table from the metadata test results.

param TestResultMetadata result  
a test result.

rtype  
list(TableTemplate)

### `valjean.javert.table_repr.repr_metadata_summary(result)`

Function to generate a table from the metadata test results.

param TestResultMetadata result  
a test result.

rtype  
list(TextTemplate)

### `valjean.javert.table_repr.repr_metadata_silent(_result)`

Function to generate a table from the metadata test results.

param TestResultMetadata result  
a test result.

returns  
empty list

### `valjean.javert.table_repr.repr_testresultexternal(_result, _verbosity=Verbosity.DEFAULT)`

Represent external test as tables -\> no table done.

If tables are required they are already done. Their representation in the report is done by `.ExternalRepresenter`.

returns  
empty list

### `valjean.javert.table_repr.repr_testresultfailed(result, _verbosity=Verbosity.DEFAULT)`

Represent a failed result as rst text.

param TestResultFailed result  
a failed test result.

rtype  
list(TextTemplate)
