<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_AdjointTest.html -->

# 14.1. Checking algorithm “*AdjointTest*”

## 14.1.1. Description

This algorithm allows to check the quality of the adjoint of an operator
$F$, by computing a residue whose theoretical properties are known. The
test is applicable to any operator, of evolution $\mathcal{D}$ or
observation $\mathcal{H}$..

For all formulas, with $\mathbf{x}$ the current verification point, we
take $\mathbf{dx}_0=Normal(0,\mathbf{x})$ and
$\mathbf{dx}=\alpha_0*\mathbf{dx}_0$ with $\alpha_0$ a scaling user
parameter, defaulting to 1. $F$ is the computational operator or code
(which is here defined by the observation operator command
“*ObservationOperator*”).

One can observe the following residue, which is the difference of two scalar
products:

$$R(\alpha) = | < TangentF_x(\mathbf{dx}) , \mathbf{y} > - < \mathbf{dx} , AdjointF_x(\mathbf{y}) > |$$

in which the optional quantity $\mathbf{y}$ must be in the image of
$F$. If it is not given, we take its default evaluation $\mathbf{y}
= F(\mathbf{x})$.

This residue must remain constantly equal to zero at the accuracy of the
calculation.

## 14.1.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The methods proposed by this algorithm **require the derivation of the
  objective function or of one of the operators**. It requires that at least
  one or both of the observation or evolution operators are differentiable, and
  this implies an additional calculation time in the case where the derivatives
  are calculated numerically by multiple evaluations.

- The methods proposed by this algorithm **have no internal parallelism, but
  use the numerical derivation of operator(s), which can be parallelized**. The
  potential interaction, between the parallelism of the numerical derivation,
  and the parallelism that may be present in the observation or evolution
  operators embedding user codes, must therefore be carefully tuned.

## 14.1.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

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

AmplitudeOfInitialDirection
:   *Real value*. This key indicates the scaling of the initial perturbation
    build as a vector used for the directional derivative around the nominal
    checking point. The default is 1, that means no scaling. It’s useful to
    modify this value, and in particular to decrease it when the biggest
    perturbations are going out of the allowed domain for the function.

    Example:
    `{"AmplitudeOfInitialDirection":0.5}`

EpsilonMinimumExponent
:   *Integer value*. This key indicates the minimal exponent value of the power
    of 10 coefficient to be used to decrease the increment multiplier. The
    default is -8, and it has to be negative between 0 and -20. For example, its
    default value leads to calculate the residue of the scalar product formula
    with a fixed increment multiplied from 1.e0 to 1.e-8.

    Example:
    `{"EpsilonMinimumExponent":-12}`

InitialDirection
:   *Vector*. This key indicates the vector direction used for the directional
    derivative around the nominal checking point. It has to be a vector of the
    same vector size than the checking point. If not specified, this direction
    defaults to a random perturbation around zero of the same vector size than
    the checking point.

    Example:
    `{"InitialDirection":[0.1,0.1,100.,3}` for a state space of dimension 4

NumberOfPrintedDigits
:   *Integer value*. This key indicates the number of digits of precision for
    floating point printed output. The default is 5, with a minimum of 0.

    Example:
    `{"NumberOfPrintedDigits":5}`

SetSeed
:   *Integer value*. This key allow to give an integer in order to fix the seed
    of the random generator used in the algorithm. By default, the seed is left
    uninitialized, and so use the default initialization from the computer, which
    then change at each study. To ensure the reproducibility of results involving
    random samples, it is strongly advised to initialize the seed. A simple
    convenient value is for example 123456789. It is recommended to put an integer
    with more than 6 or 7 digits to properly initialize the random generator.

    Example:
    `{"SetSeed":123456789}`

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
    “Residu”,
    “SimulatedObservationAtCurrentState”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 14.1.4. Information and variables available at the end of the algorithm

At the output, after executing the algorithm, there are information and
variables originating from the calculation. The description of
[Variables and information available at the output](ref_output_variables.md#section-ref-output-variables) show the way to obtain them by the method
named `get`, of the variable “*ADD*” of the post-processing in graphical
interface, or of the case in textual interface. The input variables, available
to the user at the output in order to facilitate the writing of post-processing
procedures, are described in an [Inventory of potentially available information at the output](ref_output_variables.md#subsection-r-o-v-inventaire).

**Permanent outputs (non conditional)**

The unconditional outputs of the algorithm are the following:

Residu
:   *List of values*. Each element is the value of the particular residue
    checked during the running of the algorithm, in the order of the tests.

    Example:
    `r = ADD.get("Residu")[:]`

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

CurrentState
:   *List of vectors*. Each element is a usual state vector used during the
    iterative algorithm procedure.

    Example:
    `xs = ADD.get("CurrentState")[:]`

Residu
:   *List of values*. Each element is the value of the particular residue
    checked during the running of the algorithm, in the order of the tests.

    Example:
    `r = ADD.get("Residu")[:]`

SimulatedObservationAtCurrentState
:   *List of vectors*. Each element is an observed vector simulated by the
    observation operator from the current state, that is, in the observation
    space.

    Example:
    `hxs = ADD.get("SimulatedObservationAtCurrentState")[-1]`

## 14.1.5. Python (TUI) use examples

Here is one or more very simple examples of the proposed algorithm and its
parameters, written in [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). Moreover, when it is possible, the
information given as input also allows to define an equivalent case in
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome).

This example describes the test of the quality of the adjoint of some operator,
whose direct formulation is given and whose adjoint formulation is here
approximated by default. The required information is minimal, namely here an
operator $F$ (described for the test by the observation command
“*ObservationOperator*”), and a state $\mathbf{x}^b$ to test it on
(described for the test by the command “*CheckingPoint*”). An observation
$\mathbf{y}^o$ can be given as here (described for the test by the
command “*Observation*”). The output has been set to determine the printout,
for example to make more easy automatic comparison.

The actual check is to observe whether the residue is consistently equal to
zero at the accuracy of the calculation.

```python
# -*- coding: utf-8 -*-
#
from numpy import array, eye
from adao import adaoBuilder
case = adaoBuilder.New()
case.setCheckingPoint( Vector = array([0., 1., 2.]), Stored=True )
case.setObservation( Vector = [10., 11., 12.] )
case.setObservationOperator( Matrix = eye(3), )
case.setAlgorithmParameters(
    Algorithm="AdjointTest",
    Parameters={
        "EpsilonMinimumExponent" :-12,
        "NumberOfPrintedDigits" : 3,
        "SetSeed" : 1234567,
        },
    )
case.execute()
```

The execution result is the following:

```none

     ADJOINTTEST
     ===========

     This test allows to analyze the quality of an adjoint operator associated
     to some given direct operator F, applied to one single vector argument x.
     If the adjoint operator is approximated and not given, the test measures
     the quality of the automatic approximation, around an input checking point X.

===> Information before launching:
     -----------------------------

     Characteristics of input vector X, internally converted:
       Type...............: <class 'numpy.ndarray'>
       Length of vector...: 3
       Minimum value......: 0.000e+00
       Maximum value......: 2.000e+00
       Mean of vector.....: 1.000e+00
       Standard error.....: 8.165e-01
       L2 norm of vector..: 2.236e+00

     ---------------------------------------------------------------------------

===> Numerical quality indicators:
     -----------------------------

     Using the "ScalarProduct" formula, one observes the residue R which is the
     difference of two scalar products:

         R(Alpha) = | < TangentF_X(dX) , Y > - < dX , AdjointF_X(Y) > |

     which must remain constantly equal to zero to the accuracy of the calculation.
     One takes dX0 = Normal(0,X) and dX = Alpha*dX0, where F is the calculation
     operator. If it is given, Y must be in the image of F. If it is not given,
     one takes Y = F(X).

     (Remark: numbers that are (about) under 2e-16 represent 0 to machine precision)

     -------------------------------------------------------------
       i   Alpha     ||X||       ||Y||       ||dX||     R(Alpha)
     -------------------------------------------------------------
        0  1e+00   2.236e+00   1.910e+01   3.536e+00   0.000e+00
        1  1e-01   2.236e+00   1.910e+01   3.536e-01   0.000e+00
        2  1e-02   2.236e+00   1.910e+01   3.536e-02   0.000e+00
        3  1e-03   2.236e+00   1.910e+01   3.536e-03   0.000e+00
        4  1e-04   2.236e+00   1.910e+01   3.536e-04   0.000e+00
        5  1e-05   2.236e+00   1.910e+01   3.536e-05   0.000e+00
        6  1e-06   2.236e+00   1.910e+01   3.536e-06   0.000e+00
        7  1e-07   2.236e+00   1.910e+01   3.536e-07   0.000e+00
        8  1e-08   2.236e+00   1.910e+01   3.536e-08   0.000e+00
        9  1e-09   2.236e+00   1.910e+01   3.536e-09   0.000e+00
       10  1e-10   2.236e+00   1.910e+01   3.536e-10   0.000e+00
       11  1e-11   2.236e+00   1.910e+01   3.536e-11   0.000e+00
       12  1e-12   2.236e+00   1.910e+01   3.536e-12   0.000e+00
     -------------------------------------------------------------

     End of the "ADJOINTTEST" verification by the "ScalarProduct" formula.

     ---------------------------------------------------------------------------
```

## 14.1.6. See also

References to other sections:

- [Checking algorithm “FunctionTest”](ref_algorithm_FunctionTest.md#section-ref-algorithm-functiontest)
- [Checking algorithm “LinearityTest”](ref_algorithm_LinearityTest.md#section-ref-algorithm-linearitytest)
- [Checking algorithm “TangentTest”](ref_algorithm_TangentTest.md#section-ref-algorithm-tangenttest)
- [Checking algorithm “GradientTest”](ref_algorithm_GradientTest.md#section-ref-algorithm-gradienttest)
- [Checking algorithm “LocalSensitivityTest”](ref_algorithm_LocalSensitivityTest.md#section-ref-algorithm-localsensitivitytest)
