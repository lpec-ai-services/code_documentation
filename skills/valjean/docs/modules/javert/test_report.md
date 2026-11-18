<!-- source: modules/javert/test_report.rst -->

# `test_report` – Classes modelling a test report

This module contains a simple class that models a test report. A report consists of a number of sections, and each section contains: \* a title; \* some optional introductory text; \* optionally, other test reports and some test results.

This module also contains a task that creates a report from a list of test-evaluation tasks.

### `class valjean.javert.test_report.TestReport(*, title, text='', content=None)`

This class models a test report. It is essentially a rose tree (i.e. a tree with an arbitrary number of children at each node) with nodes annotated with a title and some introductory text. `TestResult` objects play the role of tree leaves.

### `class valjean.javert.test_report.TestReportTask(name, *, make_report, eval_tasks, kwargs=None)  — bases: PythonTask`

Task class that creates a `TestReport` from a function that classifies test results into report sections.
