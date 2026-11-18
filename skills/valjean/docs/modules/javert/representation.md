<!-- source: modules/javert/representation.rst -->

# `representation` – Transform test results into items

This module contains code that converts a test result into some kind of human-readable representation (table, plots, etc.).

Possible improvement: turn `Representer` into an `ABC`; loop over the classes in `eponine` that inherit from `` `TestResult `` and add `@abstractmethod` methods in `Representer`. This way, if a new `TestResult` is added to `eponine`, it will no longer be possible to instantiate any of the classes that derive from `Representer`, pointing to the fact that the code in this module needs to be extended to handle the new class. This is better than silently falling back to some default do-nothing implementation, which may lead to bugs.

This module uses the `Strategy` design pattern. The `Representation` class plays the role of `Context`, `Representer` plays the role of `Strategy` and the classes derived from `Representer` (such as `TableRepresenter`, `PlotRepresenter`, etc.) play the role of `ConcreteStrategy`. See E. Gamma et al., "Design Patterns" (1995), ISBN 0-201-63361-2, Addison-Weasley, USA.

Currently we have 3 main `Representer` classes:

- `Representer`: parent class of all others, containing the default `Representer.__call__` method, calling the class method named `'repr_' + class.name` of the test;
- `TableRepresenter`: inherited from `Representer`, designed as a parent class for user's own representations of tables. Its `TableRepresenter.__call__` method first looks for a method called `'repr_' + class.name`; if it does not exist call the default method from the catalogue of table representation accessible in `.table_repr`;
- `PlotRepresenter`: inherited from `Representer`, designed as a parent class for user's own representations of plots. Its `PlotRepresenter.__call__` method first looks for a method called `'repr_' + class.name`; if it does not exist call the default method from the catalogue of plot representation accessible in `.plot_repr`.

An example of use of the `Representer` objects can be seen in the `FullTableRepresenter`. In this table representation, for the Bonferroni test result, the input test result is first represented in a table, then the Bonferroni itself is represented in a second table.

Thus the use of the `Representer` is foreseen as:

- use the default methods provided in `TableRepresenter` and `PlotRepresenter`;
- if customisation is needed, you can easily call the additional method available in `.table_repr` and `.plot_repr`;
- you can also write your own representation method provided they follow the naming convention `'repr_' + class.name`;
- `valjean` calls the `Representer` classes through the `Representation` class.

### `class valjean.javert.representation.Representation(representer, verbosity=Verbosity.DEFAULT)`

Class for representing test results as templates calling the available representers (tables or plots).

This class corresponds to the `Context` role in the `Strategy` design pattern.

### `class valjean.javert.representation.Representer`

Base class for representing test results as templates (in the sense of the `templates` module).

This class corresponds to the `Strategy` role in the `Strategy` design pattern. Its subclasses play the role of `ConcreteStrategy`.

### `class valjean.javert.representation.ExternalRepresenter`

This class is the default representation class for external tests, i.e. tests defined by the users who already defined the test representation as templates.

### `class valjean.javert.representation.TableRepresenter  — bases: Representer`

This class is the default representation class for tables. It contains the overridden `Representer.__call__`.

Advice: users willing to customize the behaviour of TableRepresenter for specific test results should subclass TableRepresenter and define the relevant `repr_*` methods.

### `class valjean.javert.representation.FullTableRepresenter  — bases: TableRepresenter`

Class to define the specific methods for full representation of tables. This only involve few cases needing the `TableRepresenter.__call__` method like in Bonferroni and Holm-Bonferroni test results.

#### `FullTableRepresenter.repr_testresultbonferroni(self, result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestBonferroni` test in two tables:

1.  First test result (Student, equal, etc)
2.  Bonferroni test result

param result  
a test result.

type result  
TestResultBonferroni

returns  
Representation of a `TestResultBonferroni` as two tables (the first test result and the Bonferroni result).

rtype  
list(TableTemplate)

#### `FullTableRepresenter.repr_testresultholmbonferroni(self, result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestHolmBonferroni` test in two tables:

1.  First test result (Student, equal, etc)
2.  Holm-Bonferroni test result

param result  
a test result.

type result  
TestResultHolmBonferroni

returns  
Representation of a `TestResultHolmBonferroni` as two tables (the first test result and the Holm-Bonferroni result).

rtype  
list(TableTemplate)

### `class valjean.javert.representation.PlotRepresenter(post='default')  — bases: Representer`

This class is the default representation class for plots. It contains the overridden `Representer.__call__`.

Advice: users willing to customize the behaviour of `PlotRepresenter` for specific test results should subclass `PlotRepresenter` and define the relevant `repr_*` methods.

#### `PlotRepresenter.repr_testresultbonferroni(self, result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestBonferroni` test one a plot (only the input test for the moment) (Student, equal, etc)

param result  
a test result.

type result  
TestResultBonferroni

returns  
Representation of a `TestResultBonferroni` as a plot (the first test result).

rtype  
list(PlotTemplate)

#### `PlotRepresenter.repr_testresultholmbonferroni(self, result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestHolmBonferroni` test as a plot (Student, equal, etc)

param result  
a test result.

type result  
TestResultHolmBonferroni

returns  
Representation of a `TestResultHolmBonferroni` as a plot (the first test result).

rtype  
list(PlotTemplate)

### `class valjean.javert.representation.FullPlotRepresenter  — bases: PlotRepresenter`

Class to define the specific methods for full representation of plots. This only involve few cases needing the `PlotRepresenter.__call__` method like in Bonferroni and Holm-Bonferroni test results.

#### `FullPlotRepresenter.repr_testresultbonferroni(self, result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestBonferroni` test one a plot (only the input test for the moment) (Student, equal, etc)

param result  
a test result.

type result  
TestResultBonferroni

returns  
Representation of a `TestResultBonferroni` as a plot (the first test result).

rtype  
list(PlotTemplate)

#### `FullPlotRepresenter.repr_testresultholmbonferroni(self, result, verbosity=Verbosity.DEFAULT)`

Represent the result of a `TestHolmBonferroni` test as a plot (Student, equal, etc)

param result  
a test result.

type result  
TestResultHolmBonferroni

returns  
Representation of a `TestResultHolmBonferroni` as a plot (the first test result).

rtype  
list(PlotTemplate)

### `class valjean.javert.representation.EmptyRepresenter  — bases: Representer`

Class that does not generate any templates for any test result.

### `class valjean.javert.representation.FullRepresenter(post=plot_repr.post_treatment)  — bases: Representer`

This class generates the fullest possible representation for test results. If anything can be represented as an template, `FullRepresenter` will do it.
