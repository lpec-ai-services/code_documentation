<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_ExtendedBlue.html -->

# 13.8. Calculation algorithm “*ExtendedBlue*”

## 13.8.1. Description

This algorithm realizes an extended BLUE (Best Linear Unbiased Estimator) type
estimation of the state of a system.

This algorithm is a partially non-linear generalization of a
[Calculation algorithm “Blue”](ref_algorithm_Blue.md#section-ref-algorithm-blue). It is equivalent for a linear observation
operator. One can verify the linearity of the observation operator with the
help of a [Checking algorithm “LinearityTest”](ref_algorithm_LinearityTest.md#section-ref-algorithm-linearitytest).

In case of non-linearity, its results are close to a
[Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar), without being entirely equivalent.

This mono-objective optimization algorithm is naturally written for a single
estimate, without any dynamic or iterative notion (there is no need in this
case for an incremental evolution operator, nor for an evolution error
covariance). In ADAO, it can also be used on a succession of observations,
placing the estimate in a recursive framework partly similar to a
[Calculation algorithm “KalmanFilter”](ref_algorithm_KalmanFilter.md#section-ref-algorithm-kalmanfilter). A standard estimate is made at each
observation step on the state predicted by the incremental evolution model,
knowing that the state error covariance remains the background covariance
initially provided by the user. To be explicit, unlike Kalman-type filters, the
state error covariance is not updated.

## 13.8.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The optimization methods proposed by this algorithm perform a **local search
  for the minimum**, theoretically enabling a locally optimal state (as opposed
  to a “*globally optimal*” state) to be reached.

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

- The methods proposed by this algorithm **achieve their convergence on one or
  more static criteria, fixed by some particular algorithmic properties**. In
  practice, there may be several convergence criteria active simultaneously.

  The more frequent algorithmic property is the one of direct calculations,
  which evaluate the converged solution without any controllable iteration.
  There is no convergence threshold to be adjusted in this case.

## 13.8.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

Background
:   *Vector*. The variable indicates the background or initial vector used,
    previously noted as $\mathbf{x}^b$. Its value is defined as a
    “*Vector*” or “*VectorSerie*” type object. Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

BackgroundError
:   *Matrix*. This indicates the background error covariance matrix, previously
    noted as $\mathbf{B}$. Its value is defined as a “*Matrix*” type
    object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
    type object, as described in detail in the section
    [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

EvolutionError
:   *Matrix*. The variable indicates the evolution error covariance matrix,
    usually noted as $\mathbf{Q}$. It is defined as a “*Matrix*” type
    object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
    type object, as described in detail in the section
    [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

EvolutionModel
:   *Operator*. The variable indicates the evolution model operator, usually
    noted $M$, which describes an elementary step of evolution. Its value
    is defined as a “*Function*” type object or a “*Matrix*” type one. In the
    case of “*Function*” type, different functional forms can be used, as
    described in the section [Requirements for functions describing an operator](ref_operator_requirements.md#section-ref-operator-requirements). If there
    is some control $U$ included in the evolution model, the operator has
    to be applied to a pair $(X,U)$.

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
textual interface, are indicated in [List of commands and keywords for data assimilation or optimization case](ref_assimilation_keywords.md#section-ref-assimilation-keywords).
Moreover, the parameters of the command “*AlgorithmParameters*” allows to
choose the specific options, described hereafter, of the algorithm. See
[Description of options of an algorithm by “AlgorithmParameters”](ref_options_AlgorithmParameters.md#section-ref-options-algorithm-parameters) for the good use of this
command.

The options are the following:

EstimationOf
:   *Predefined name*. This key allows to choose the type of estimation to be
    performed. It can be either state-estimation, with a value of “State”, or
    parameter-estimation, with a value of “Parameters”. The default choice is
    “Parameters”.

    Example:
    `{"EstimationOf":"Parameters"}`

NumberOfSamplesForQuantiles
:   *Integer value*. This key indicates the number of simulation to be done in
    order to estimate the quantiles. This option is useful only if the
    supplementary calculation “SimulationQuantiles” has been chosen. The default
    is 100, which is often sufficient for correct estimation of common quantiles
    at 5%, 10%, 90% or 95%.

    Example:
    `{"NumberOfSamplesForQuantiles":100}`

Quantiles
:   *List of real values*. This list indicates the values of quantile, between 0
    and 1, to be estimated by simulation around the optimal state. The sampling
    uses a multivariate Gaussian random sampling, directed by the *a posteriori*
    covariance matrix. This option is useful only if the supplementary
    calculation “SimulationQuantiles” has been chosen. The default is a void
    list.

    Example:
    `{"Quantiles":[0.1,0.9]}`

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

SimulationForQuantiles
:   *Predefined name*. This key indicates the type of simulation, linear (with
    the tangent observation operator applied to perturbation increments around
    the optimal state) or non-linear (with standard observation operator applied
    to perturbed states), one want to do for each perturbation. It changes mainly
    the time of each elementary calculation, usually longer in non-linear than in
    linear. This option is useful only if the supplementary calculation
    “SimulationQuantiles” has been chosen. The default value is “Linear”, and the
    possible choices are “Linear” and “NonLinear”.

    Example:
    `{"SimulationForQuantiles":"Linear"}`

StateBoundsForQuantiles
:   *List of pairs of real values*. This key allows to define pairs of upper and
    lower bounds for every state variable used for quantile simulations. Bounds
    have to be given by a list of list of pairs of lower/upper bounds for each
    variable, with possibly `None` every time there is no bound.

    If these bounds are not defined for quantile simulation and if optimization
    bounds are defined, they are used for quantile simulation. If these bounds
    for quantile simulation are defined, they are used regardless of the
    optimization bounds defined. If this variable is set to `None`, then no
    bounds are used for the states used in the quantile simulation regardless of
    the optimization bounds defined.

    Example :
    `{"StateBoundsForQuantiles":[[2.,5.],[1.e-2,10.],[-30.,None],[None,None]]}`

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
    “Analysis”,
    “APosterioriCorrelations”,
    “APosterioriCovariance”,
    “APosterioriStandardDeviations”,
    “APosterioriVariances”,
    “BMA”,
    “CostFunctionJ”,
    “CostFunctionJAtCurrentOptimum”,
    “CostFunctionJb”,
    “CostFunctionJbAtCurrentOptimum”,
    “CostFunctionJo”,
    “CostFunctionJoAtCurrentOptimum”,
    “CurrentOptimum”,
    “CurrentState”,
    “CurrentStepNumber”,
    “EnsembleOfSimulations”,
    “EnsembleOfStates”,
    “ForecastState”,
    “Innovation”,
    “InnovationAtCurrentAnalysis”,
    “MahalanobisConsistency”,
    “OMA”,
    “OMB”,
    “SampledStateForQuantiles”,
    “SigmaBck2”,
    “SigmaObs2”,
    “SimulatedObservationAtBackground”,
    “SimulatedObservationAtCurrentOptimum”,
    “SimulatedObservationAtCurrentState”,
    “SimulatedObservationAtOptimum”,
    “SimulationQuantiles”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 13.8.4. Information and variables available at the end of the algorithm

At the output, after executing the algorithm, there are information and
variables originating from the calculation. The description of
[Variables and information available at the output](ref_output_variables.md#section-ref-output-variables) show the way to obtain them by the method
named `get`, of the variable “*ADD*” of the post-processing in graphical
interface, or of the case in textual interface. The input variables, available
to the user at the output in order to facilitate the writing of post-processing
procedures, are described in an [Inventory of potentially available information at the output](ref_output_variables.md#subsection-r-o-v-inventaire).

**Permanent outputs (non conditional)**

The unconditional outputs of the algorithm are the following:

Analysis
:   *List of vectors*. Each element of this variable is an optimal state
    $\mathbf{x}^*$ in optimization, an interpolate or an analysis
    $\mathbf{x}^a$ in data assimilation.

    Example:
    `xa = ADD.get("Analysis")[-1]`

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

Analysis
:   *List of vectors*. Each element of this variable is an optimal state
    $\mathbf{x}^*$ in optimization, an interpolate or an analysis
    $\mathbf{x}^a$ in data assimilation.

    Example:
    `xa = ADD.get("Analysis")[-1]`

APosterioriCorrelations
:   *List of matrices*. Each element is an *a posteriori* error correlations
    matrix of the optimal state, coming from the $\mathbf{A}$ covariance
    matrix. In order to get them, this *a posteriori* error covariances
    supplementary calculation has to be requested at the same time by the keyword
    “APosterioriCovariance”.

    Example:
    `apc = ADD.get("APosterioriCorrelations")[-1]`

APosterioriCovariance
:   *List of matrices*. Each element is an *a posteriori* error covariance
    matrix $\mathbf{A}$ of the optimal state.

    Example:
    `apc = ADD.get("APosterioriCovariance")[-1]`

APosterioriStandardDeviations
:   *List of matrices*. Each element is an *a posteriori* error standard errors
    diagonal matrix of the optimal state, coming from the $\mathbf{A}$
    covariance matrix. In order to get them, this *a posteriori* error
    covariances supplementary calculation has to be requested at the same time by
    the keyword “APosterioriCovariance”.

    Example:
    `aps = ADD.get("APosterioriStandardDeviations")[-1]`

APosterioriVariances
:   *List of matrices*. Each element is an *a posteriori* error variance errors
    diagonal matrix of the optimal state, coming from the $\mathbf{A}$
    covariance matrix. In order to get them, this *a posteriori* error
    covariances supplementary calculation has to be requested at the same time by
    the keyword “APosterioriCovariance”.

    Example:
    `apv = ADD.get("APosterioriVariances")[-1]`

BMA
:   *List of vectors*. Each element is a vector of difference between the
    background and the optimal state.

    Example:
    `bma = ADD.get("BMA")[-1]`

CostFunctionJ
:   *List of values*. Each element is a value of the chosen error function
    $J$.

    Example:
    `J = ADD.get("CostFunctionJ")[:]`

CostFunctionJAtCurrentOptimum
:   *List of values*. Each element is a value of the error function $J$.
    At each step, the value corresponds to the optimal state found from the
    beginning.

    Example:
    `JACO = ADD.get("CostFunctionJAtCurrentOptimum")[:]`

CostFunctionJb
:   *List of values*. Each element is a value of the error function $J^b$,
    that is of the background difference part. If this part does not exist in the
    error function, its value is zero.

    Example:
    `Jb = ADD.get("CostFunctionJb")[:]`

CostFunctionJbAtCurrentOptimum
:   *List of values*. Each element is a value of the error function $J^b$. At
    each step, the value corresponds to the optimal state found from the
    beginning. If this part does not exist in the error function, its value is
    zero.

    Example:
    `JbACO = ADD.get("CostFunctionJbAtCurrentOptimum")[:]`

CostFunctionJo
:   *List of values*. Each element is a value of the error function $J^o$,
    that is of the observation difference part.

    Example:
    `Jo = ADD.get("CostFunctionJo")[:]`

CostFunctionJoAtCurrentOptimum
:   *List of values*. Each element is a value of the error function $J^o$,
    that is of the observation difference part. At each step, the value
    corresponds to the optimal state found from the beginning.

    Example:
    `JoACO = ADD.get("CostFunctionJoAtCurrentOptimum")[:]`

CurrentOptimum
:   *List of vectors*. Each element is the optimal state obtained at the usual
    step of the iterative algorithm procedure of the optimization algorithm. It
    is not necessarily the last state.

    Example:
    `xo = ADD.get("CurrentOptimum")[:]`

CurrentState
:   *List of vectors*. Each element is a usual state vector used during the
    iterative algorithm procedure.

    Example:
    `xs = ADD.get("CurrentState")[:]`

CurrentStepNumber
:   *List of integers*. Each element is the index of the current step in the
    iterative process, driven by the series of observations, of the algorithm
    used. This corresponds to the observation step used. Note: it is not the
    index of the current iteration of the algorithm even if it coincides for
    non-iterative algorithms.

    Example:
    `csn = ADD.get("CurrentStepNumber")[-1]`

EnsembleOfSimulations
:   *List of vectors or matrix*. This key contains an ordered collection of
    physical state vectors or simulated state vectors $\mathbf{y}$ that may
    be observed. These are $H$ operator **outputs**, i.e. simulated
    observation states (called “*snapshots*” in reduced-base terminology). At
    each step index, there is 1 state per column if this list is in matrix form,
    or 1 state per element if it’s actually a list. Caution: the numbering of the
    support or points, on which or to which a state value is given in each
    vector, is implicitly that of the natural order of numbering of the state
    vector, from 0 to the “size minus 1” of this vector.

    Example :
    `{"EnsembleOfSimulations":[y1, y2, y3...]}`

EnsembleOfStates
:   *List of vectors or matrix*. Each element is an ordered collection of
    physical or parameter state vectors $\mathbf{x}$. These are $H$
    operator **entries**, i.e. current states before observation. At each step
    index, there is 1 state per column if this list is in matrix form, or 1 state
    per element if it’s actually a list. Caution: the numbering of the support or
    points, on which or to which a state value is given in each vector, is
    implicitly that of the natural order of numbering of the state vector, from 0
    to the “size minus 1” of this vector.

    Example :
    `{"EnsembleOfStates":[x1, x2, x3...]}`

ForecastState
:   *List of vectors*. Each element is a state vector forecasted by the model
    during the iterative algorithm procedure.

    Example:
    `xf = ADD.get("ForecastState")[:]`

Innovation
:   *List of vectors*. Each element is an innovation vector, which is in static
    the difference between the optimal and the background, and in dynamic the
    evolution increment.

    Example:
    `d = ADD.get("Innovation")[-1]`

InnovationAtCurrentAnalysis
:   *List of vectors*. Each element is an innovation vector at current analysis.
    This quantity is identical to the innovation vector at analysed state in the
    case of a single-state assimilation.

    Example:
    `da = ADD.get("InnovationAtCurrentAnalysis")[-1]`

MahalanobisConsistency
:   *List of values*. Each element is a value of the Mahalanobis quality
    indicator.

    Example:
    `mc = ADD.get("MahalanobisConsistency")[-1]`

OMA
:   *List of vectors*. Each element is a vector of difference between the
    observation and the optimal state in the observation space.

    Example:
    `oma = ADD.get("OMA")[-1]`

OMB
:   *List of vectors*. Each element is a vector of difference between the
    observation and the background state in the observation space.

    Example:
    `omb = ADD.get("OMB")[-1]`

SampledStateForQuantiles
:   *List of vector series*. Each element is a series of column state vectors,
    generated to estimate by simulation and/or observation the quantile values
    required by the user. There are as many states as the number of samples
    required for this quantile estimate.

    Example :
    `xq = ADD.get("SampledStateForQuantiles")[:]`

SigmaBck2
:   *List of values*. Each element is a value of the quality indicator
    $(\sigma^b)^2$ of the background part.

    Example:
    `sb2 = ADD.get("SigmaBck")[-1]`

SigmaObs2
:   *List of values*. Each element is a value of the quality indicator
    $(\sigma^o)^2$ of the observation part.

    Example:
    `so2 = ADD.get("SigmaObs")[-1]`

SimulatedObservationAtBackground
:   *List of vectors*. Each element is a vector of observation simulated by the
    observation operator from the background $\mathbf{x}^b$. It is the
    forecast from the background, and it is sometimes called “*Dry*”.

    Example:
    `hxb = ADD.get("SimulatedObservationAtBackground")[-1]`

SimulatedObservationAtCurrentOptimum
:   *List of vectors*. Each element is a vector of observation simulated from
    the optimal state obtained at the current step the optimization algorithm,
    that is, in the observation space.

    Example:
    `hxo = ADD.get("SimulatedObservationAtCurrentOptimum")[-1]`

SimulatedObservationAtCurrentState
:   *List of vectors*. Each element is an observed vector simulated by the
    observation operator from the current state, that is, in the observation
    space.

    Example:
    `hxs = ADD.get("SimulatedObservationAtCurrentState")[-1]`

SimulatedObservationAtOptimum
:   *List of vectors*. Each element is a vector of observation obtained by the
    observation operator from simulation on the analysis or optimal state
    $\mathbf{x}^a$. It is the observed forecast from the analysis or the
    optimal state, and it is sometimes called “*Forecast*”.

    Example:
    `hxa = ADD.get("SimulatedObservationAtOptimum")[-1]`

SimulationQuantiles
:   *List of vector series*. Each element is a series of observation column
    vectors, corresponding, for a particular quantile required by the user, to
    the observed state that achieves the requested quantile. Each observation
    column vector is rendered in the same order as the quantile values required
    by the user.

    Example:
    `sQuantiles = ADD.get("SimulationQuantiles")[:]`

## 13.8.5. Python (TUI) use examples

Here is one or more very simple examples of the proposed algorithm and its
parameters, written in [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). Moreover, when it is possible, the
information given as input also allows to define an equivalent case in
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome).

This example describes the interpolation between two physical states. These two
vector fields, of identical discretization, are the observation
$\mathbf{y}^o$ and the background state $\mathbf{x}^b$. The
confidence in errors on the two information are considered identical. The
$H$ model fully observe the available field, it is a matrix selection
operator.

The interpolated resulting field is simply the “middle” between the two fields,
with an increased confidence (that is, a smaller variance) on the errors.

```python
# -*- coding: utf-8 -*-
#
from numpy import array, ravel
from adao import adaoBuilder
case = adaoBuilder.New()
case.setBackground( Vector = array([0., 1., 2.]), Stored=True )
case.setBackgroundError( ScalarSparseMatrix = 1. )
case.setObservation( Vector = array([10., 11., 12.]), Stored=True )
case.setObservationError( ScalarSparseMatrix = 1. )
case.setObservationOperator( Matrix = array([[1., 0., 0.],
                                             [0., 1., 0.],
                                             [0., 0., 1.]]), )
case.setAlgorithmParameters(
    Algorithm="ExtendedBlue",
    Parameters={
        "StoreSupplementaryCalculations": [
            "APosterioriCovariance",
            ],
        },
    )
case.execute()
#
#-------------------------------------------------------------------------------
#
print("Interpolation between two vectors, of observation and background")
print("----------------------------------------------------------------")
print("")
print("Observation vector............:", ravel(case.get("Observation")))
print("A priori background vector....:", ravel(case.get("Background")))
print("")
print("Expected theoretical state....:", ravel([5., 6., 7.]))
print("")
print("Interpolation result..........:", ravel(case.get("Analysis")[-1]))
print("A posteriori covariance.......:\n", case.get("APosterioriCovariance")[-1])
```

The execution result is the following:

```none
Interpolation between two vectors, of observation and background
----------------------------------------------------------------

Observation vector............: [10. 11. 12.]
A priori background vector....: [0. 1. 2.]

Expected theoretical state....: [5. 6. 7.]

Interpolation result..........: [5. 6. 7.]
A posteriori covariance.......:
 [[0.5 0.  0. ]
 [0.  0.5 0. ]
 [0.  0.  0.5]]
```

## 13.8.6. See also

References to other sections:

- [Calculation algorithm “Blue”](ref_algorithm_Blue.md#section-ref-algorithm-blue)
- [Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar)
- [Checking algorithm “LinearityTest”](ref_algorithm_LinearityTest.md#section-ref-algorithm-linearitytest)
