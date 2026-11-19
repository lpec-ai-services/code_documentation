<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_LinearityTest.html -->

# 14.7. Checking algorithm “*LinearityTest*”

## 14.7.1. Description

This algorithm allows to check the linear quality of the operator, by
calculating a residue with known theoretical properties. Different residue
formula are available. The test is applicable to any operator, of evolution
$\mathcal{D}$ or observation $\mathcal{H}$.

In any cases, with $\mathbf{x}$ the current verification point, one take
$\mathbf{dx}_0=Normal(0,\mathbf{x})$ and
$\mathbf{dx}=\alpha*\mathbf{dx}_0$ with $\alpha_0`a user scale
parameter, at 1 by default. :math:`F$ is the calculation code (given here by
the user by using the observation operator command “*ObservationOperator*”).

### 14.7.1.1. “CenteredDL” residue

One observe the following residue, coming from the centered difference of the
$F$ values at nominal point and at perturbed points, normalized by the
value at the nominal point:

$$R(\alpha) = \frac{|| F(\mathbf{x}+\alpha*\mathbf{dx}) + F(\mathbf{x}-\alpha*\mathbf{dx}) - 2*F(\mathbf{x}) ||}{|| F(\mathbf{x}) ||}$$

If it stays constantly really small with respect to 1, the linearity hypothesis
of $F$ is verified.

If the residue is varying, or if it is of order 1 or more, and it is small only
at a certain order of increment, the linearity hypothesis of $F$ is not
verified.

If the residue is decreasing and the decrease change in $\alpha^2$ with
respect to $\alpha$, it signifies that the gradient is correctly
calculated until the stopping level of the quadratic decrease.

### 14.7.1.2. “Taylor” residue

One observe the residue coming from the Taylor development of the $F$
function, normalized by the value at the nominal point:

$$R(\alpha) = \frac{|| F(\mathbf{x}+\alpha*\mathbf{dx}) - F(\mathbf{x}) - \alpha * \nabla_xF(\mathbf{dx}) ||}{|| F(\mathbf{x}) ||}$$

If it stay constantly really small with respect to 1, the linearity hypothesis
of $F$ is verified.

If the residue is varying, or if it is of order 1 or more, and it is small only
at a certain order of increment, the linearity hypothesis of $F$ is not
verified.

If the residue is decreasing and the decrease change in $\alpha^2$ with
respect to $\alpha$, it signifies that the gradient is correctly
calculated until the stopping level of the quadratic decrease.

### 14.7.1.3. “NominalTaylor” residue

One observe the residue build from two approximations of order 1 of
$F(\mathbf{x})$, normalized by the value at the nominal point:

$$R(\alpha) = \max(|| F(\mathbf{x}+\alpha*\mathbf{dx}) - \alpha * F(\mathbf{dx}) || / || F(\mathbf{x}) ||,|| F(\mathbf{x}-\alpha*\mathbf{dx}) + \alpha * F(\mathbf{dx}) || / || F(\mathbf{x}) ||)$$

If the residue stays constant equal to 1 at less than 2 or 3 percents (that that
$|R-1|$ stays equal to 2 or 3 percents), the linearity hypothesis of
$F$ is verified.

If it is equal to 1 only on part of the variation domain of increment
$\alpha$, it is on this sub-domain that the linearity hypothesis of
$F$ is verified.

### 14.7.1.4. “NominalTaylorRMS” residue

One observe the residue build from two approximations of order 1 of
$F(\mathbf{x})$, normalized by the value at the nominal point, on which
one estimate the quadratic root mean square (RMS) with the value at the nominal
point:

$$R(\alpha) = \max(RMS( F(\mathbf{x}), F(\mathbf{x}+\alpha*\mathbf{dx}) - \alpha * F(\mathbf{dx}) ) / || F(\mathbf{x}) ||,RMS( F(\mathbf{x}), F(\mathbf{x}-\alpha*\mathbf{dx}) + \alpha * F(\mathbf{dx}) ) / || F(\mathbf{x}) ||)$$

If it stay constantly equal to 0 at less than 1 or 2 percents, the linearity
hypothesis of $F$ is verified.

If it is equal to 0 only on part of the variation domain of increment
$\alpha$, it is on this sub-domain that the linearity hypothesis of
$F$ is verified.

## 14.7.2. Some noteworthy properties of the implemented methods

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

## 14.7.3. Optional and required commands

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

AmplitudeOfInitialDirection
:   *Real value*. This key indicates the scaling of the initial perturbation
    build as a vector used for the directional derivative around the nominal
    checking point. The default is 1, that means no scaling. It’s useful to
    modify this value, and in particular to decrease it when the biggest
    perturbations are going out of the allowed domain for the function.

    Example:
    `{"AmplitudeOfInitialDirection":0.5}`

AmplitudeOfTangentPerturbation
:   *Real value*. This key indicates the relative numerical magnitude of the
    perturbation used to estimate the tangent value of the operator at the
    evaluation point, i.e. its directional derivative. The conservative default
    is 1.e-2 i.e. 1%, and it is strongly recommended to adapt it to the needs of
    real problems, by decreasing its value by several orders of magnitude.

    Example :
    `{"AmplitudeOfTangentPerturbation":1.e-2}`

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

ResiduFormula
:   *Predefined name*. This key indicates the residue formula that has to be
    used for the test. The default choice is “CenteredDL”, and the possible ones
    are “CenteredDL” (residue of the difference between the function at nominal
    point and the values with positive and negative increments, which has to stay
    very small), “Taylor” (residue of the Taylor development of the operator
    normalized by the nominal value, which has to stay very small),
    “NominalTaylor” (residue of the order 1 approximations of the operator,
    normalized to the nominal point, which has to stay close to 1), and
    “NominalTaylorRMS” (residue of the order 1 approximations of the operator,
    normalized by RMS to the nominal point, which has to stay close to 0).

    Example :
    `{"ResiduFormula":"CenteredDL"}`

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

## 14.7.4. Information and variables available at the end of the algorithm

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

## 14.7.5. See also

References to other sections:

- [Checking algorithm “FunctionTest”](ref_algorithm_FunctionTest.md#section-ref-algorithm-functiontest)
