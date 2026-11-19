<!-- source: modules/javert/test_external.rst -->

# `test_external` – Class to import external test

External test used to represent user formatted results in the report.

This test has been designed in order to offer the possibility to define and run user-defined tests outside valjean and include their results in a report, along with the native valjean tests.

The user is responsible for defining and representing the test results. The representation must be done with templates (see `templates` module).

For example, the simplest case is a custom plot to represent a test. In that case, if the path to the image is known a `TextTemplate` can be created and given to the test:

\>\>\> txtemp = TextTemplate("And this represents Javertnn" ... ".. image:: ../../doc/src/images/javert.jpgnn") \>\>\> textr = TestExternal(txtemp, name='', success=True).evaluate() \>\>\> print(bool(textr)) True

### `class valjean.javert.test_external.TestResultExternal  — bases: TestResult`

Result from a external test.

### `class valjean.javert.test_external.TestExternal(*templates, name, description='', labels=None, success=True)  — bases: Test`

Class building a test that will return the boolean value specified at initialisation.

#### `TestExternal.evaluate(self)`

Evaluate the test (do nothing in this case except building the TestResult).

rtype  
TestResultExternal
