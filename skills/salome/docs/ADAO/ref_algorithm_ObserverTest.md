<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_ObserverTest.html -->

# 14.10. Checking algorithm “*ObserverTest*”

## 14.10.1. Description

This algorithm allows to verify an external function, given by the user, used as
an *observer*. This external function can be applied to each of the variables
that can be potentially observed. It is activated only on those who are
explicitly associated with the *observer* in its declaration.

## 14.10.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

## 14.10.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

Observers
:   *List of functions linked to variables*. This command allows to set internal
    observers, that are functions linked with a particular variable, which will
    be executed each time this variable is modified. It is a convenient way to
    monitor variables of interest during the data assimilation or optimization
    process, by printing or plotting it, etc. Common templates are provided to
    help the user to start or to quickly make his case.

The general optional commands, available in the editing user interface, are
indicated in [List of commands and keywords for data assimilation or optimization case](ref_assimilation_keywords.md#section-ref-assimilation-keywords).

*Tips for this algorithm:*

> Because *“CheckingPoint”* and *“ObservationOperator”*, in the graphical
> interface, are required commands for ALL checking algorithms, you have to
> provide a value for them, despite the fact that these commands are not
> required for this test, and will not be used. The easiest way is to give
> “1” as a STRING for both, *“ObservationOperator”* having to be of type
> sparse *Matrix*.
