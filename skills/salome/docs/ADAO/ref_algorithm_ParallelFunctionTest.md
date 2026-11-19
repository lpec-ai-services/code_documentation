<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_ParallelFunctionTest.html -->

# 14.11. Checking algorithm “*ParallelFunctionTest*”

## 14.11.1. Description

This algorithm allows to analyze in a simple way the stability of an operator
$F$ during its execution in parallel. The operator is any operator, so it
can be the observation operator $\mathcal{H}$ as well as the evolution
operator $\mathcal{D}$, as long as it is provided in each case according
to the [Requirements for functions describing an operator](ref_operator_requirements.md#section-ref-operator-requirements). The operator $F$ is
considered as depending on a vector variable $\mathbf{x}$ and returning
another vector variable $\mathbf{y}$.

The algorithm verifies that the operator is working correctly and that its call
is compatible with its usage in ADAO algorithms. In practice, it allows to call
one or several times the operator, activating or not the “debug” mode during
execution.

Statistics on $\mathbf{x}$ input and $\mathbf{y}$ output vectors
are given for each execution of operator, and an another global statistic is
given at the end. The precision of printed outputs can be controlled to
facilitate automatic tests of operator. It may also be useful to check the
entries themselves beforehand with the intended test
[Checking algorithm “InputValuesTest”](ref_algorithm_InputValuesTest.md#section-ref-algorithm-inputvaluestest).

## 14.11.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

- The methods proposed by this algorithm **have internal parallelism**, and can
  therefore take advantage of computational distribution resources. The
  potential interaction, between the parallelism of the numerical derivation,
  and the parallelism that may be present in the observation or evolution
  operators embedding user codes, must therefore be carefully tuned.

## 14.11.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

CheckingPoint
:   *Vector*. The variable indicates the vector used as the state around which to
    perform the required check, noted $\mathbf{x}$ and similar to the
    background $\mathbf{x}^b$. It is defined as a “*Vector*” or
    “*VectorSerie*” type object. Its availability in output is conditioned by the
    boolean “*Stored*” associated with input.

ObservationOperator
:   *Operator*. The variable indicates the observation operator, usually noted as
    $H$, which transforms the input parameters $\mathbf{x}$ to
    results $\mathbf{y}$ to be compared to observations
    $\mathbf{y}^o$. Its value is defined as a “*Function*” type object or a
    “*Matrix*” type one. In the case of “*Function*” type, different functional
    forms can be used, as described in the section
    [Requirements for functions describing an operator](ref_operator_requirements.md#section-ref-operator-requirements). If there is some control $U$
    included in the observation, the operator has to be applied to a pair
    $(X,U)$.

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

NumberOfRepetition
:   *Integer value*. This key indicates the number of time to repeat the function
    evaluation. The default is 1.

    Example:
    `{"NumberOfRepetition":3}`

SetDebug
:   *Boolean value*. This variable leads to the activation, or not, of the debug
    mode during the function or operator evaluation. The default is “False”, the
    choices are “True” or “False”.

    Example:
    `{"SetDebug":False}`

ShowElementarySummary
:   *Boolean value*. This variable leads to the activation, or not, of the
    calculation and display of a summary at each elementary evaluation of the
    test. The default value is “True”, the choices are “True” or “False”.

    Example :
    `{"ShowElementarySummary":False}`

StoreSupplementaryCalculations
:   *List of names*. This list indicates the names of the supplementary
    variables, that can be available during or at the end of the algorithm, if
    they are initially required by the user. Their availability involves,
    potentially, costly calculations or memory consumptions. The default is then
    a void list, none of these variables being calculated and stored by default
    (excepted the unconditional variables). The possible names are in the
    following list (the detailed description of each named variable is given in
    the following part of this specific algorithmic documentation, in the
    sub-section “*Information and variables available at the end of the
    algorithm*”): [
    “CurrentState”,
    “SimulatedObservationAtCurrentState”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 14.11.4. Information and variables available at the end of the algorithm

At the output, after executing the algorithm, there are information and
variables originating from the calculation. The description of
[Variables and information available at the output](ref_output_variables.md#section-ref-output-variables) show the way to obtain them by the method
named `get`, of the variable “*ADD*” of the post-processing in graphical
interface, or of the case in textual interface. The input variables, available
to the user at the output in order to facilitate the writing of post-processing
procedures, are described in an [Inventory of potentially available information at the output](ref_output_variables.md#subsection-r-o-v-inventaire).

**Permanent outputs (non conditional)**

The unconditional outputs of the algorithm are the following:

> *None*

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

CurrentState
:   *List of vectors*. Each element is a usual state vector used during the
    iterative algorithm procedure.

    Example:
    `xs = ADD.get("CurrentState")[:]`

SimulatedObservationAtCurrentState
:   *List of vectors*. Each element is an observed vector simulated by the
    observation operator from the current state, that is, in the observation
    space.

    Example:
    `hxs = ADD.get("SimulatedObservationAtCurrentState")[-1]`

## 14.11.5. Python (TUI) use examples

Here is one or more very simple examples of the proposed algorithm and its
parameters, written in [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). Moreover, when it is possible, the
information given as input also allows to define an equivalent case in
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome).

This example describes the test of the correct operation of a given operator,
and that its call proceeds in a way compatible with its common use in parallel
in the ADAO algorithms. The required information are minimal, namely here an
operator $F$ (described for the test by the observation command
“*ObservationOperator*”), and a state $\mathbf{x}^b$ to test it on
(described for the test by the command “*CheckingPoint*”).

The test is repeated a configurable number of times, and a final statistic
makes it possible to quickly verify the operator’s good behavior. The simplest
diagnostic consists in checking, at the very end of the display, the order of
magnitude of the values indicated as the mean of the differences between the
repeated outputs and their mean, under the part entitled “*Characteristics of
the mean of the differences between the outputs Y and their mean Ym*”. For a
satisfactory operator, these values should be close to the numerical zero.

Note

It can be useful to make sure that the evaluation of the operator is really
done in parallel, and for example that there is no forced use of a
parallelism acceleration, which would avoid a real parallel test. For this
purpose, it is recommended to systematically use the boolean special
parameter “*EnableParallelEvaluations*”, exclusively reserved for this
purpose, of the operator declaration command. The use of this parameter is
illustrated in this example.

```python
# -*- coding: utf-8 -*-
#
import numpy
from adao import adaoBuilder
#
def SomeOperator( x ):
    return numpy.dot(numpy.eye(x.size), numpy.ravel(x))
#
case = adaoBuilder.New()
case.setAlgorithmParameters(
    Algorithm="ParallelFunctionTest",
    Parameters={
        "NumberOfRepetition" : 50,
        "NumberOfPrintedDigits" : 2,
        "ShowElementarySummary":False,
        },
    )
case.setCheckingPoint( Vector = range(30) )
case.setObservationOperator(
    OneFunction = SomeOperator,
    Parameters  = {
        "EnableParallelEvaluations":True,
        "NumberOfProcesses":5,
        },
    )
case.execute()
```

The execution result is the following:

```none

     PARALLELFUNCTIONTEST
     ====================

     This test allows to analyze the (repetition of the) launch of some
     given simulation operator F, applied to one single vector argument x,
     in a parallel way.
     The output shows simple statistics related to its successful execution,
     or related to the similarities of repetition of its execution.

===> Information before launching:
     -----------------------------

     Characteristics of input vector X, internally converted:
       Type...............: <class 'numpy.ndarray'>
       Length of vector...: 30
       Minimum value......: 0.00e+00
       Maximum value......: 2.90e+01
       Mean of vector.....: 1.45e+01
       Standard error.....: 8.66e+00
       L2 norm of vector..: 9.25e+01

     ---------------------------------------------------------------------------

===> Beginning of repeated evaluation, without activating debug

     ---------------------------------------------------------------------------

     Appending the input vector to the agument set to be evaluated in parallel

     ---------------------------------------------------------------------------

===> Launching operator parallel evaluation for 50 states

===> End of operator parallel evaluation for 50 states

     ---------------------------------------------------------------------------

===> End of repeated evaluation, without deactivating debug

     ---------------------------------------------------------------------------

===> Launching statistical summary calculation for 50 states

     ---------------------------------------------------------------------------

===> Statistical analysis of the outputs obtained through parallel repeated evaluations

     (Remark: numbers that are (about) under 2e-16 represent 0 to machine precision)

     Number of evaluations...........................: 50

     Characteristics of the whole set of outputs Y:
       Size of each of the outputs...................: 30
       Minimum value of the whole set of outputs.....: 0.00e+00
       Maximum value of the whole set of outputs.....: 2.90e+01
       Mean of vector of the whole set of outputs....: 1.45e+01
       Standard error of the whole set of outputs....: 8.66e+00

     Characteristics of the vector Ym, mean of the outputs Y:
       Size of the mean of the outputs...............: 30
       Minimum value of the mean of the outputs......: 0.00e+00
       Maximum value of the mean of the outputs......: 2.90e+01
       Mean of the mean of the outputs...............: 1.45e+01
       Standard error of the mean of the outputs.....: 8.66e+00

     Characteristics of the mean of the differences between the outputs Y and their mean Ym:
       Size of the mean of the differences...........: 30
       Minimum value of the mean of the differences..: 0.00e+00
       Maximum value of the mean of the differences..: 0.00e+00
       Mean of the mean of the differences...........: 0.00e+00
       Standard error of the mean of the differences.: 0.00e+00

     ---------------------------------------------------------------------------

     End of the "PARALLELFUNCTIONTEST" verification

     ---------------------------------------------------------------------------
```

## 14.11.6. See also

References to other sections:

- [Checking algorithm “InputValuesTest”](ref_algorithm_InputValuesTest.md#section-ref-algorithm-inputvaluestest)
- [Checking algorithm “LinearityTest”](ref_algorithm_LinearityTest.md#section-ref-algorithm-linearitytest)
- [Checking algorithm “FunctionTest”](ref_algorithm_FunctionTest.md#section-ref-algorithm-functiontest)
- [Checking algorithm “ControledFunctionTest”](ref_algorithm_ControledFunctionTest.md#section-ref-algorithm-controledfunctiontest)
- [Task algorithm “EnsembleOfSimulationGenerationTask”](ref_algorithm_EnsembleOfSimulationGenerationTask.md#section-ref-algorithm-ensembleofsimulationgenerationtask)
