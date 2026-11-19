<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_ObservationSimulationComparisonTest.html -->

# 14.9. Checking algorithm “*ObservationSimulationComparisonTest*”

## 14.9.1. Description

This algorithm allows to analyze in a simple way the stability of the
difference between measures and an operator $F$ during its execution. The
operator is any operator, so it can be the observation operator
$\mathcal{H}$ as well as the evolution operator $\mathcal{D}$, as
long as it is provided in each case according to the
[Requirements for functions describing an operator](ref_operator_requirements.md#section-ref-operator-requirements). The operator $F$ is considered
as depending on a vector variable $\mathbf{x}$ and returning another
vector variable $\mathbf{y}$.

The algorithm verifies that the difference is stable, that the operator is
working correctly and that its call is compatible with its usage in ADAO
algorithms. In practice, it allows to call one or several times the operator,
activating or not the “debug” mode during execution. It is very similar in its
current behavior to a [Checking algorithm “FunctionTest”](ref_algorithm_FunctionTest.md#section-ref-algorithm-functiontest) but it tests
the stability of the measurement-calculation difference.

Statistics on $\mathbf{x}$ input and $\mathbf{y}$ output vectors,
and potentially on the classical data assimilation error function $J$,
are given for each execution of operator, and an another global statistic is
given at the end. The precision of printed outputs can be controlled to
facilitate automatic tests of operator. It may also be useful to check the
entries themselves beforehand with the intended test
[Checking algorithm “InputValuesTest”](ref_algorithm_InputValuesTest.md#section-ref-algorithm-inputvaluestest).

## 14.9.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

## 14.9.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

CheckingPoint
:   *Vector*. The variable indicates the vector used as the state around which to
    perform the required check, noted $\mathbf{x}$ and similar to the
    background $\mathbf{x}^b$. It is defined as a “*Vector*” or
    “*VectorSerie*” type object. Its availability in output is conditioned by the
    boolean “*Stored*” associated with input.

BackgroundError
:   *Matrix*. This indicates the background error covariance matrix, previously
    noted as $\mathbf{B}$. Its value is defined as a “*Matrix*” type
    object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
    type object, as described in detail in the section
    [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

Observation
:   *List of vectors*. The variable indicates the observation vector used for
    data assimilation or optimization, and usually noted $\mathbf{y}^o$.
    Its value is defined as an object of type “*Vector*” if it is a single
    observation (temporal or not) or “*VectorSeries*” if it is a succession of
    observations. Its availability in output is conditioned by the boolean
    “*Stored*” associated in input.

ObservationError
:   *Matrix*. The variable indicates the observation error covariance matrix,
    usually noted as $\mathbf{R}$. It is defined as a “*Matrix*” type
    object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
    type object, as described in detail in the section
    [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

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
    “CostFunctionJ”,
    “CostFunctionJb”,
    “CostFunctionJo”,
    “CurrentState”,
    “Innovation”,
    “InnovationAtCurrentState”,
    “OMB”,
    “SimulatedObservationAtCurrentState”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 14.9.4. Information and variables available at the end of the algorithm

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

CostFunctionJ
:   *List of values*. Each element is a value of the chosen error function
    $J$.

    Example:
    `J = ADD.get("CostFunctionJ")[:]`

CostFunctionJb
:   *List of values*. Each element is a value of the error function $J^b$,
    that is of the background difference part. If this part does not exist in the
    error function, its value is zero.

    Example:
    `Jb = ADD.get("CostFunctionJb")[:]`

CostFunctionJo
:   *List of values*. Each element is a value of the error function $J^o$,
    that is of the observation difference part.

    Example:
    `Jo = ADD.get("CostFunctionJo")[:]`

CurrentState
:   *List of vectors*. Each element is a usual state vector used during the
    iterative algorithm procedure.

    Example:
    `xs = ADD.get("CurrentState")[:]`

Innovation
:   *List of vectors*. Each element is an innovation vector, which is in static
    the difference between the optimal and the background, and in dynamic the
    evolution increment.

    Example:
    `d = ADD.get("Innovation")[-1]`

InnovationAtCurrentState
:   *List of vectors*. Each element is an innovation vector at current state
    before analysis.

    Example:
    `ds = ADD.get("InnovationAtCurrentState")[-1]`

OMB
:   *List of vectors*. Each element is a vector of difference between the
    observation and the background state in the observation space.

    Example:
    `omb = ADD.get("OMB")[-1]`

SimulatedObservationAtCurrentState
:   *List of vectors*. Each element is an observed vector simulated by the
    observation operator from the current state, that is, in the observation
    space.

    Example:
    `hxs = ADD.get("SimulatedObservationAtCurrentState")[-1]`

## 14.9.5. Python (TUI) use examples

Here is one or more very simple examples of the proposed algorithm and its
parameters, written in [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). Moreover, when it is possible, the
information given as input also allows to define an equivalent case in
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome).

This example analyzes the (repeated) running of a simulation operator
$\mathbf{F}$ explicitly given in matrix form (described for the test by
the observation command “*ObservationOperator*”), applied to a particular state
:math: mathbf{x} on which to test (described for the test by the
“*CheckingPoint*” command), compared to measurements $\mathbf{y}$
(described for the test by the “*Observation*” command) by the difference OMB =
y - F(x) (Observation minus evaluation at Background) and the standard data
assimilation cost function J.

The test is repeated a configurable number of times, and a final statistic
allows to quickly check the good behavior of the operator. The simplest
diagnostic consists in checking, at the very end of the display, the order of
magnitude of the variations of the values indicated as the average of the
differences between the repeated outputs and their average, under the part here
entitled “*Launching statistical summary calculation for 5 states*”. For a
satisfactory operator, the values of differences from the mean and the standard
deviations should be close to the numerical zero.

```python
# -*- coding: utf-8 -*-
#
from numpy import array, eye, ones
from adao import adaoBuilder
case = adaoBuilder.New()
case.set("CheckingPoint",       Vector = array([0., 1., 2.]) )
case.set("Observation",         Vector = ones(3) )
case.set("ObservationOperator", Matrix = 1/3 * eye(3) )
case.setAlgorithmParameters(
    Algorithm="ObservationSimulationComparisonTest",
    Parameters={
        "NumberOfRepetition" : 5,
        "NumberOfPrintedDigits" : 2,
        "ShowElementarySummary":False,
        "StoreSupplementaryCalculations": [
            "CostFunctionJ",
            ],
        },
    )
case.execute()
```

The execution result is the following:

```none

     OBSERVATIONSIMULATIONCOMPARISONTEST
     ===================================

     This test allows to analyze the (repetition of the) launch of some
     given simulation operator F, applied to one single vector argument x,
     and its comparison to observations or measures y through the innovation
     difference OMB = y - F(x) (Observation minus evaluation at Background)
     and (if required) the data assimilation standard cost function J.
     The output shows simple statistics related to its successful execution,
     or related to the similarities of repetition of its execution.

===> Information before launching:
     -----------------------------

     Characteristics of input vector X, internally converted:
       Type...............: <class 'numpy.ndarray'>
       Length of vector...: 3
       Minimum value......: 0.00e+00
       Maximum value......: 2.00e+00
       Mean of vector.....: 1.00e+00
       Standard error.....: 8.16e-01
       L2 norm of vector..: 2.24e+00

     Characteristics of input vector of observations Yobs, internally converted:
       Type...............: <class 'numpy.ndarray'>
       Length of vector...: 3
       Minimum value......: 1.00e+00
       Maximum value......: 1.00e+00
       Mean of vector.....: 1.00e+00
       Standard error.....: 0.00e+00
       L2 norm of vector..: 1.73e+00

     ---------------------------------------------------------------------------

===> Beginning of repeated evaluation, without activating debug

     ---------------------------------------------------------------------------

===> End of repeated evaluation, without deactivating debug

     ---------------------------------------------------------------------------

===> Launching statistical summary calculation for 5 states

     ---------------------------------------------------------------------------

===> Statistical analysis of the outputs obtained through sequential repeated evaluations

     (Remark: numbers that are (about) under 2e-16 represent 0 to machine precision)

     Number of evaluations...........................: 5

     Characteristics of the whole set of outputs Y:
       Size of each of the outputs...................: 3
       Minimum value of the whole set of outputs.....: 0.00e+00
       Maximum value of the whole set of outputs.....: 6.67e-01
       Mean of vector of the whole set of outputs....: 3.33e-01
       Standard error of the whole set of outputs....: 2.72e-01

     Characteristics of the vector Ym, mean of the outputs Y:
       Size of the mean of the outputs...............: 3
       Minimum value of the mean of the outputs......: 0.00e+00
       Maximum value of the mean of the outputs......: 6.67e-01
       Mean of the mean of the outputs...............: 3.33e-01
       Standard error of the mean of the outputs.....: 2.72e-01

     Characteristics of the mean of the differences between the outputs Y and their mean Ym:
       Size of the mean of the differences...........: 3
       Minimum value of the mean of the differences..: 0.00e+00
       Maximum value of the mean of the differences..: 0.00e+00
       Mean of the mean of the differences...........: 0.00e+00
       Standard error of the mean of the differences.: 0.00e+00

     ---------------------------------------------------------------------------

===> Statistical analysis of the OMB differences obtained through sequential repeated evaluations

     (Remark: numbers that are (about) under 2e-16 represent 0 to machine precision)

     Number of evaluations...........................: 5

     Characteristics of the whole set of OMB differences:
       Size of each of the outputs...................: 3
       Minimum value of the whole set of differences.: 3.33e-01
       Maximum value of the whole set of differences.: 1.00e+00
       Mean of vector of the whole set of differences: 6.67e-01
       Standard error of the whole set of differences: 2.72e-01

     Characteristics of the vector Dm, mean of the OMB differences:
       Size of the mean of the differences...........: 3
       Minimum value of the mean of the differences..: 3.33e-01
       Maximum value of the mean of the differences..: 1.00e+00
       Mean of the mean of the differences...........: 6.67e-01
       Standard error of the mean of the differences.: 2.72e-01

     Characteristics of the mean of the differences between the OMB differences and their mean Dm:
       Size of the mean of the differences...........: 3
       Minimum value of the mean of the differences..: 0.00e+00
       Maximum value of the mean of the differences..: 0.00e+00
       Mean of the mean of the differences...........: 0.00e+00
       Standard error of the mean of the differences.: 0.00e+00

     ---------------------------------------------------------------------------

===> Statistical analysis of the cost function J values obtained through sequential repeated evaluations

     Number of evaluations...........................: 5

     Characteristics of the whole set of data assimilation cost function J values:
       Minimum value of the whole set of J...........: 7.78e-01
       Maximum value of the whole set of J...........: 7.78e-01
       Mean of vector of the whole set of J..........: 7.78e-01
       Standard error of the whole set of J..........: 0.00e+00
       (Remark: variations of the cost function J only come from the observation part Jo of J)

     ---------------------------------------------------------------------------

     End of the "OBSERVATIONSIMULATIONCOMPARISONTEST" verification

     ---------------------------------------------------------------------------
```

## 14.9.6. See also

References to other sections:

- [Checking algorithm “FunctionTest”](ref_algorithm_FunctionTest.md#section-ref-algorithm-functiontest)
