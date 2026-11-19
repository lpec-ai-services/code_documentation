<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_EnsembleKalmanFilter.html -->

# 13.7. Calculation algorithm “*EnsembleKalmanFilter*”

## 13.7.1. Description

This algorithm realizes an estimation of the state of a dynamic system by a
Ensemble Kalman Filter (EnKF), avoiding to have to perform the tangent or
adjoint operators for the observation and evolution operators, as in the simple
or extended Kalman filters.

It applies to non-linear observation and incremental evolution (process)
operators with excellent robustness and performance qualities. It can be
interpreted as an order reduction of the classical Kalman filter, with a
remarkable assimilation quality of this filtering for large problems. It can be
compared to the [Calculation algorithm “UnscentedKalmanFilter”](ref_algorithm_UnscentedKalmanFilter.md#section-ref-algorithm-unscentedkalmanfilter), whose
qualities are similar for non-linear systems.

We notice that there is no analysis performed at the initial time step
(numbered 0 in the time indexing) because there is no forecast at this time
(the background is stored as a pseudo analysis at the initial time step). If
the observations are provided in series by the user, the first one is therefore
not used. For a good understanding of time management, please refer to the
[Timeline of steps for data assimilation operators in dynamics](theory.md#schema-d-ad-temporel) and the explanations in the section
[Going further in data assimilation for dynamics](theory.md#section-theory-dynamic).

In case of linear of “slightly” non-linear operators, one can easily use the
[Calculation algorithm “ExtendedKalmanFilter”](ref_algorithm_ExtendedKalmanFilter.md#section-ref-algorithm-extendedkalmanfilter) or even the
[Calculation algorithm “KalmanFilter”](ref_algorithm_KalmanFilter.md#section-ref-algorithm-kalmanfilter), which are often far less expensive
to evaluate on small systems. One can verify the linearity of the operators
with the help of the [Checking algorithm “LinearityTest”](ref_algorithm_LinearityTest.md#section-ref-algorithm-linearitytest).

There are many deterministic or stochastic variants of this algorithm, allowing
in particular to perform size reduction of algebraic problems at different
levels (by using reduced rank methods, dimension reduction, changes of
computational space, leading to schemes of type Ensemble Square Root Kalman
Filters (EnSRKF) or Reduced-Rank Square Root Filters (RRSQRT), to deterministic
transformations…). We do not go into the complex details of classifications
and algorithmic equivalences, which are available in the literature. The
following stable and robust formulations are proposed here:

- “EnKF” (Ensemble Kalman Filter, see [[Evensen94]](bibliography.md#evensen94)), original stochastic algorithm, allowing consistent treatment of non-linear evolution operator,
- “ETKF” (Ensemble-Transform Kalman Filter), deterministic EnKF algorithm, allowing treatment of non-linear evolution operator with a lot less members (one recommends to use a number of members on the order of 10 or even sometimes less),
- “ETKF-N” (Ensemble-Transform Kalman Filter of finite size N), ETKF algorithm of “finite size N”, that doesn’t need inflation that is often required with the other algorithms,
- “MLEF” (Maximum Likelihood Kalman Filter, see [[Zupanski05]](bibliography.md#zupanski05)), deterministic EnKF algorithm, allowing in addition the consistent treatment of non-linear observation operator,
- “IEnKF” (Iterative EnKF), deterministic EnKF algorithm, improving treament of operators non-linearities,
- “E3DVAR” (EnKF 3DVAR, or 3D-Var-Ben), algorithm coupling ensemble and variational assimilation, which uses in parallel a 3DVAR variational assimilation for a single best estimate and an EnKF ensemble algorithm to improve the estimation of *a posteriori* error covariances,
- “EnKS” (Ensemble Kalman Smoother), smoothing algorithm with a fixed time lag L.

Without being a universal recommendation, one recommend to use “EnKF”
formulation as a reference algorithm, **“ETKF-N” ou “IEnKF” formulation for
robust performance**, and the other algorithms (in this order) as means to
obtain a less costly data assimilation with (hopefully) the same quality.

## 13.7.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The optimization methods proposed by this algorithm perform a **local search
  for the minimum**, theoretically enabling a locally optimal state (as opposed
  to a “*globally optimal*” state) to be reached.

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

- The methods proposed by this algorithm **have internal parallelism**, and can
  therefore take advantage of computational distribution resources. The
  potential interaction, between the parallelism of the numerical derivation,
  and the parallelism that may be present in the observation or evolution
  operators embedding user codes, must therefore be carefully tuned.

- The methods proposed by this algorithm **achieve their convergence on one or
  more static criteria, fixed by some particular algorithmic properties**. In
  practice, there may be several convergence criteria active simultaneously.

  The more frequent algorithmic property is the one of direct calculations,
  which evaluate the converged solution without any controllable iteration.
  There is no convergence threshold to be adjusted in this case.

## 13.7.3. Optional and required commands

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
    “State”.

    Example:
    `{"EstimationOf":"Parameters"}`

HybridCostDecrementTolerance
:   *Real value*. This key indicates a limit value, leading to stop successfully
    the optimization process for the variational part in the coupling, when the
    cost function decreases less than this tolerance at the last step. The
    default is 1.e-7, and it is recommended to adapt it to the needs on real
    problems. One can refer to the section describing ways for
    [Convergence control for calculation cases and iterative algorithms](advanced.md#subsection-iterative-convergence-control) for more detailed
    recommendations.

    Example:
    `{"HybridCostDecrementTolerance":1.e-7}`

HybridCovarianceEquilibrium
:   *Real value*. This key indicates, in hybrid variational optimization, the
    equilibrium factor between the static *a priori* covariance and the ensemble
    covariance. This factor is between 0 and 1, and its default value is 0.5.

    Example :
    `{"HybridCovarianceEquilibrium":0.5}`

HybridMaximumNumberOfIterations
:   *Integer value*. This key indicates the maximum number of internal iterations
    allowed for hybrid optimization, for the variational part. The default is
    15000, which is very similar to no limit on iterations. It is then
    recommended to adapt this parameter to the needs on real problems. For some
    optimizers, the effective stopping step can be slightly different of the
    limit due to algorithm internal control requirements. One can refer to the
    section describing ways for [Convergence control for calculation cases and iterative algorithms](advanced.md#subsection-iterative-convergence-control)
    for more detailed recommendations.

    Example:
    `{"HybridMaximumNumberOfIterations":100}`

InflationFactor
:   *Real value*. This key specifies the inflation factor in the ensemble
    methods, to be applied on the covariance or the anomalies depending on the
    choice of the type of inflation. Its value must be positive if the inflation
    is additive, or greater than 1 if the inflation is multiplicative. The
    default value is 1, which leads to an absence of multiplicative inflation.
    The absence of additive inflation is obtained by entering a value of 0.

    Example :
    `{"InflationFactor":1.}`

InflationType
:   *Predefined name*. This key is used to set the inflation method in ensemble
    methods, for those that require such a technique. Inflation can be applied in
    various ways, according to the following options: multiplicative or additive
    by the specified inflation factor, applied on the background or on the
    analysis, applied on covariances or on anomalies. The *multiplicative
    inflation on anomalies*, that are obtained by subtracting the ensemble mean,
    is elaborated by multiplying these anomalies by the inflation factor, then by
    rebuilding the ensemble members by adding the previously evaluated mean. Only
    one type of inflation is applied at the same time, and the default value is
    “MultiplicativeOnAnalysisAnomalies”. The possible names are in the following
    list: [
    “MultiplicativeOnAnalysisAnomalies”,
    “MultiplicativeOnBackgroundAnomalies”,
    ].

    Example :
    `{"InflationType":"MultiplicativeOnAnalysisAnomalies"}`

NumberOfMembers
:   *Integer value*. This key indicates the number of members used to realize the
    ensemble method. The default is 100, and it is recommended to adapt it to the
    needs on real problems.

    Example:
    `{"NumberOfMembers":100}`

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

SmootherLagL
:   *Integer value*. This key indicates the number of smoothing time intervals in
    the past for the EnKS. This is a number of intervals, not a fixed duration.
    The default value is 0, which leads to no smoothing.

    Example :
    `{"SmootherLagL":0}`

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
    “ForecastCovariance”,
    “ForecastState”,
    “IndexOfOptimum”,
    “InnovationAtCurrentAnalysis”,
    “InnovationAtCurrentState”,
    “SimulatedObservationAtCurrentAnalysis”,
    “SimulatedObservationAtCurrentOptimum”,
    “SimulatedObservationAtCurrentState”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

Variant
:   *Predefined name*. This key allows to choose one of the possible variants
    for the main algorithm. The default variant is the original “EnKF”
    formulation, and the possible choices are
    “EnKF” (Ensemble Kalman Filter),
    “ETKF” (Ensemble-Transform Kalman Filter),
    “ETKF-N” (Ensemble-Transform Kalman Filter),
    “MLEF” (Maximum Likelihood Kalman Filter),
    “IEnKF” (Iterative_EnKF),
    “E3DVAR” (EnKF 3DVAR),
    “EnKS” (Ensemble Kalman Smoother).

    One recommends to try the “ETKF-N” or “IEnKF” variants for a robust
    performance, and to reduce the number of members to about 10 or less for all
    variants other than the original “EnKF” formulation.

    Example :
    `{"Variant":"EnKF"}`

## 13.7.4. Information and variables available at the end of the algorithm

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

ForecastCovariance
:   *Liste of matrices*. Each element is a forecast state error covariance
    matrix predicted by the model during the time iteration of the algorithm
    used.

    Example :
    `pf = ADD.get("ForecastCovariance")[-1]`

ForecastState
:   *List of vectors*. Each element is a state vector forecasted by the model
    during the iterative algorithm procedure.

    Example:
    `xf = ADD.get("ForecastState")[:]`

IndexOfOptimum
:   *List of integers*. Each element is the iteration index of the optimum
    obtained at the current step of the iterative algorithm procedure of the
    optimization algorithm. It is not necessarily the number of the last
    iteration.

    Example:
    `ioo = ADD.get("IndexOfOptimum")[-1]`

InnovationAtCurrentAnalysis
:   *List of vectors*. Each element is an innovation vector at current analysis.
    This quantity is identical to the innovation vector at analysed state in the
    case of a single-state assimilation.

    Example:
    `da = ADD.get("InnovationAtCurrentAnalysis")[-1]`

InnovationAtCurrentState
:   *List of vectors*. Each element is an innovation vector at current state
    before analysis.

    Example:
    `ds = ADD.get("InnovationAtCurrentState")[-1]`

SimulatedObservationAtCurrentAnalysis
:   *List of vectors*. Each element is an observed vector simulated by the
    observation operator from the current analysis, that is, in the observation
    space. This quantity is identical to the observed vector simulated at
    current state in the case of a single-state assimilation.

    Example:
    `hxs = ADD.get("SimulatedObservationAtCurrentAnalysis")[-1]`

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

## 13.7.5. See also

References to other sections:

- [Calculation algorithm “KalmanFilter”](ref_algorithm_KalmanFilter.md#section-ref-algorithm-kalmanfilter)
- [Calculation algorithm “ExtendedKalmanFilter”](ref_algorithm_ExtendedKalmanFilter.md#section-ref-algorithm-extendedkalmanfilter)
- [Calculation algorithm “UnscentedKalmanFilter”](ref_algorithm_UnscentedKalmanFilter.md#section-ref-algorithm-unscentedkalmanfilter)

Bibliographical references:

- [[Evensen94]](bibliography.md#evensen94)
- [[Burgers98]](bibliography.md#burgers98)
- [[Bishop01]](bibliography.md#bishop01)
- [[Evensen03]](bibliography.md#evensen03)
- [[Zupanski05]](bibliography.md#zupanski05)
- [[Hamill00]](bibliography.md#hamill00)
- [[WikipediaEnKF]](bibliography.md#wikipediaenkf)
