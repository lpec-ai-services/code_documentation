<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_EnsembleBlue.html -->

# 13.6. Calculation algorithm “*EnsembleBlue*”

## 13.6.1. Description

This algorithm realizes a BLUE (Best Linear Unbiased Estimator, which is here an
Aitken estimator) type estimation of the state of a system by an ensemble
method. To work, one must give a set of backgrounds, their number determining
the size of the ensemble for the estimation.

It is theoretically reserved for observation operator cases which are linear,
but has to work also in “slightly” non-linear cases. One can verify the
linearity of the observation operator with the help of the
[Checking algorithm “LinearityTest”](ref_algorithm_LinearityTest.md#section-ref-algorithm-linearitytest).

## 13.6.2. Some noteworthy properties of the implemented methods

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

## 13.6.3. Optional and required commands

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
    “Analysis”,
    “CurrentOptimum”,
    “CurrentState”,
    “EnsembleOfSimulations”,
    “EnsembleOfStates”,
    “Innovation”,
    “SimulatedObservationAtBackground”,
    “SimulatedObservationAtCurrentState”,
    “SimulatedObservationAtOptimum”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 13.6.4. Information and variables available at the end of the algorithm

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

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

Analysis
:   *List of vectors*. Each element of this variable is an optimal state
    $\mathbf{x}^*$ in optimization, an interpolate or an analysis
    $\mathbf{x}^a$ in data assimilation.

    Example:
    `xa = ADD.get("Analysis")[-1]`

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

Innovation
:   *List of vectors*. Each element is an innovation vector, which is in static
    the difference between the optimal and the background, and in dynamic the
    evolution increment.

    Example:
    `d = ADD.get("Innovation")[-1]`

SimulatedObservationAtBackground
:   *List of vectors*. Each element is a vector of observation simulated by the
    observation operator from the background $\mathbf{x}^b$. It is the
    forecast from the background, and it is sometimes called “*Dry*”.

    Example:
    `hxb = ADD.get("SimulatedObservationAtBackground")[-1]`

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

## 13.6.5. See also

References to other sections:

- [Calculation algorithm “Blue”](ref_algorithm_Blue.md#section-ref-algorithm-blue)
- [Calculation algorithm “EnsembleKalmanFilter”](ref_algorithm_EnsembleKalmanFilter.md#section-ref-algorithm-ensemblekalmanfilter)
