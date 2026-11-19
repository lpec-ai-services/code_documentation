<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_InputValuesTest.html -->

# 14.5. Checking algorithm “*InputValuesTest*”

## 14.5.1. Description

This algorithm verifies the content of the current input variables and the way
the data is interpreted or read during its acquisition, through the display of
size information and statistics on the inputs. It also allows to display the
whole content of the variables read in printed form for verification (*warning,
if a variable is large in size, this can be difficult*).

## 14.5.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

## 14.5.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

Background
:   *Vector*. The variable indicates the background or initial vector used,
    previously noted as $\mathbf{x}^b$. Its value is defined as a
    “*Vector*” or “*VectorSerie*” type object. Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

CheckingPoint
:   *Vector*. The variable indicates the vector used as the state around which to
    perform the required check, noted $\mathbf{x}$ and similar to the
    background $\mathbf{x}^b$. It is defined as a “*Vector*” or
    “*VectorSerie*” type object. Its availability in output is conditioned by the
    boolean “*Stored*” associated with input.

Observation
:   *List of vectors*. The variable indicates the observation vector used for
    data assimilation or optimization, and usually noted $\mathbf{y}^o$.
    Its value is defined as an object of type “*Vector*” if it is a single
    observation (temporal or not) or “*VectorSeries*” if it is a succession of
    observations. Its availability in output is conditioned by the boolean
    “*Stored*” associated in input.

*Tips for this algorithm:*

> Because *“ObservationOperator”*, in the graphical interface, is a required
> command for ALL checking algorithms, you have to provide a value for it,
> despite the fact that this command is not required for this test, and will
> not be used. The easiest way is to give “1” as a STRING,
> *“ObservationOperator”* having to be of type sparse *Matrix*.

The general optional commands, available in the editing user graphical or
textual interface, are indicated in [List of commands and keywords for an ADAO checking case](ref_checking_keywords.md#section-ref-checking-keywords).
Moreover, the parameters of the command “*AlgorithmParameters*” allow to choose
the specific options, described hereafter, of the algorithm. See
[Description of options of an algorithm by “AlgorithmParameters”](ref_options_AlgorithmParameters.md#section-ref-options-algorithm-parameters) for the good use of this
command.

The options are the following:

NumberOfPrintedDigits
:   *Integer value*. This key indicates the number of digits of precision for
    floating point printed output. The default is 5, with a minimum of 0.

    Example:
    `{"NumberOfPrintedDigits":5}`

PrintAllValuesFor
:   *List of predefined names*. This key indicates the list of vector names whose
    detailed values are to be printed, the default value being the empty list. If
    the named vector is not a supplied entry, the name is simply ignored. The
    possible names are in the following list: [
    “Background”,
    “CheckingPoint”,
    “Observation”,
    ].

    Example :
    `{"PrintAllValuesFor":["Background"]}`

ShowInformationOnlyFor
:   *List of predefined names*. This key indicates the list of vector names whose
    summarized information (size, min/max…) is to be printed, the default value
    being the set of vectors. If the named vector is not a provided entry, the
    name is simply ignored. This allows you to restrict summarized printing. The
    possible names are in the following list: [
    “Background”,
    “CheckingPoint”,
    “Observation”,
    ].

    Example :
    `{"ShowInformationOnlyFor":["Background"]}`

SetDebug
:   *Boolean value*. This variable leads to the activation, or not, of the debug
    mode during the function or operator evaluation. The default is “False”, the
    choices are “True” or “False”.

    Example:
    `{"SetDebug":False}`

## 14.5.4. See also

References to other sections:

- [Checking algorithm “ControledFunctionTest”](ref_algorithm_ControledFunctionTest.md#section-ref-algorithm-controledfunctiontest)
- [Checking algorithm “FunctionTest”](ref_algorithm_FunctionTest.md#section-ref-algorithm-functiontest)
- [Checking algorithm “ParallelFunctionTest”](ref_algorithm_ParallelFunctionTest.md#section-ref-algorithm-parallelfunctiontest)
