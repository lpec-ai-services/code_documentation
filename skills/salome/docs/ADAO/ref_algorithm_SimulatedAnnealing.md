<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_SimulatedAnnealing.html -->

# 13.15. Calculation algorithm “*SimulatedAnnealing*”

## 13.15.1. Description

This algorithm estimates the state of a system by gradient-free minimization of
a cost function $J$, using the simulated annealing search meta-heuristic.
It is based on reducing the $J$ error as far as possible, while allowing
a temporary rise in this error to avoid getting stuck in a local minimum. The
rise in error is driven by a statistical law of temperature, hence the analogy
with metal annealing, which gives the method its name. The method does not
require any particular information on the functional, nor does it need
derivatives (except in its hybrid “DualAnnealing” version).

It falls in the same category than the
[Calculation algorithm “DerivativeFreeOptimization”](ref_algorithm_DerivativeFreeOptimization.md#section-ref-algorithm-derivativefreeoptimization),
[Calculation algorithm “DifferentialEvolution”](ref_algorithm_DifferentialEvolution.md#section-ref-algorithm-differentialevolution),
[Calculation algorithm “ParticleSwarmOptimization”](ref_algorithm_ParticleSwarmOptimization.md#section-ref-algorithm-particleswarmoptimization),
[Calculation algorithm “TabuSearch”](ref_algorithm_TabuSearch.md#section-ref-algorithm-tabusearch).

It is a single-objective optimization method, allowing the search for the
global minimum of any cost function $J$ of type $L^1$, $L^2$
or $L^{\infty}$, with or without weights, as described in the section for
[Going further in the state estimation by optimization methods](theory.md#section-theory-optimization). As it is a meta-heuristic, except in
special cases, reaching a global or local optimal result is not guaranteed
(except in its hybrid “DualAnnealing” version). The default error functional is
that of weighted augmented least squares, classically used in data
assimilation.

There exists various variants of this algorithm. The following stable and
robust formulations are proposed here:

- “GeneralizedSimulatedAnnealing” (Generalized Simulated Annealing or GSA, see
  [[Tsallis96]](bibliography.md#tsallis96)), a classical algorithm combining classical and fast simulated
  annealing approaches. It is powerful, robust and represents a reference for
  simulated annealing methods.
- “DualAnnealing” (see [[Xiang97]](bibliography.md#xiang97)), an algorithm combining the previous GSA
  with a local search strategy, applied to states acceptable from the point of
  view of simulated annealing, which improves the speed and accuracy of the
  GSA. This improvement requires the tangent and adjoint operators.

The following are a few practical suggestions for the effective use of these
algorithms:

- The recommended variant of this algorithm is “DualAnnealing”, as it is both
  robust and converges very well, especially in high dimensions for such an
  algorithm. However, as it requires the tangent and adjoint operators, it is
  not always wise to use this acceleration feature.
- In cases where the error function or the observation operator are not
  derivable, the “GeneralizedSimulatedAnnealing” algorithm is suitable and
  achieves the same simulated annealing optimization as the accelerated
  variant.
- The easiest way to check convergence is to leave the parameters at their
  default values and let the simulated annealing stabilize. However, since
  stochastic convergence can take a long time, it is also possible to restrict
  calculations by limiting the number of simulation function evaluations. This
  does not limit theoretical convergence, but it does significantly reduce the
  number of calculations.

These suggestions are to be used as experimental indications, not as
requirements, because they are to be appreciated or adapted according to the
physics of each problem that is treated.

## 13.15.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The optimization methods proposed by this algorithm perform a **global search
  for the minimum**, theoretically achieving a globally optimal state over the
  search domain. However, this global optimality is achieved “*at
  convergence*”, which means in long or infinite time during an iterative
  optimization “*with real values*” (as opposed to “*with integer values*”).

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

- The methods proposed by this algorithm **have no internal parallelism or
  numerical derivation of operator(s)**, and therefore cannot take advantage of
  computer resources for distributing calculations. The methods are sequential,
  and any use of parallelism resources is therefore reserved for observation or
  evolution operators, i.e. user codes.

- The methods proposed by this algorithm **achieve their convergence on one or
  more residue or number criteria**. In practice, there may be several
  convergence criteria active simultaneously.

  The residue can be a conventional measure based on a gap (e.g.
  “*calculation-measurement gap*”), or be a significant value for the algorithm
  (e.g. “*nullity of gradient*”).

  The number is frequently a significant value for the algorithm, such as a
  number of iterations or a number of evaluations, but it can also be, for
  example, a number of generations for an evolutionary algorithm.

  Convergence thresholds need to be carefully adjusted, to reduce the gobal
  calculation cost, or to ensure that convergence is adapted to the physical
  case encountered.

## 13.15.3. Optional and required commands

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

Bounds
:   *List of pairs of real values*. This key allows to define pairs of upper and
    lower bounds for every state variable being optimized. Bounds have to be
    given by a list of list of pairs of lower/upper bounds for each variable,
    with a value of `None` each time there is no bound. The bounds can always
    be specified, but they are taken into account only by the constrained
    optimizers. If the list is empty, there are no bounds.

    Example:
    `{"Bounds":[[2.,5.],[1.e-2,10.],[-30.,None],[None,None]]}`

EstimationOf
:   *Predefined name*. This key allows to choose the type of estimation to be
    performed. It can be either state-estimation, with a value of “State”, or
    parameter-estimation, with a value of “Parameters”. The default choice is
    “Parameters”.

    Example:
    `{"EstimationOf":"Parameters"}`

MaximumNumberOfIterations
:   *Integer value*. This key indicates the maximum number of internal iterations
    allowed for iterative optimization. The default is 15000, which is very
    similar to no limit on iterations. It is then recommended to adapt this
    parameter to the needs on real problems. For some optimizers, the effective
    stopping step can be slightly different of the limit due to algorithm
    internal control requirements. One can refer to the section describing ways
    for [Convergence control for calculation cases and iterative algorithms](advanced.md#subsection-iterative-convergence-control) for more detailed
    recommendations.

    Example:
    `{"MaximumNumberOfIterations":100}`

MaximumNumberOfFunctionEvaluations
:   *Integer value*. This key indicates the maximum number of evaluation of the
    cost function to be optimized. The default is 15000, which is an arbitrary
    limit. It is then recommended to adapt this parameter to the needs on real
    problems. For some optimizers, the effective number of function evaluations
    can be slightly different of the limit due to algorithm internal control
    requirements.

    Example:
    `{"MaximumNumberOfFunctionEvaluations":50}`

Minimizer
:   *Predefined name*. This key allows to choose the optimization minimizer. The
    default choice is “LBFGSB”, and the possible ones are
    “LBFGSB” (nonlinear constrained minimizer, see [[Byrd95]](bibliography.md#byrd95), [[Morales11]](bibliography.md#morales11), [[Zhu97]](bibliography.md#zhu97)),
    “TNC” (nonlinear constrained minimizer),
    “CG” (nonlinear unconstrained minimizer),
    “BFGS” (nonlinear unconstrained minimizer),
    It is highly recommended to keep the default value.

QualityCriterion
:   *Predefined name*. This key indicates the quality criterion, minimized to
    find the optimal state estimate. The default is the usual data assimilation
    criterion named “DA”, the augmented weighted least squares. The possible
    criterion has to be in the following list, where the equivalent names are
    indicated by the sign “<=>”:
    [“AugmentedWeightedLeastSquares” <=> “AWLS” <=> “DA”,
    “WeightedLeastSquares” <=> “WLS”,
    “LeastSquares” <=> “LS” <=> “L2”,
    “AbsoluteValue” <=> “L1”,
    “MaximumError” <=> “ME” <=> “Linf”].
    See the section for [Going further in the state estimation by optimization methods](theory.md#section-theory-optimization) to have a detailed
    definition of these quality criteria.

    Example:
    `{"QualityCriterion":"DA"}`

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
    “BMA”,
    “CostFunctionJ”,
    “CostFunctionJb”,
    “CostFunctionJo”,
    “CostFunctionJAtCurrentOptimum”,
    “CostFunctionJbAtCurrentOptimum”,
    “CostFunctionJoAtCurrentOptimum”,
    “CurrentIterationNumber”,
    “CurrentOptimum”,
    “CurrentState”,
    “EnsembleOfSimulations”,
    “EnsembleOfStates”,
    “IndexOfOptimum”,
    “Innovation”,
    “InnovationAtCurrentState”,
    “OMA”,
    “OMB”,
    “SimulatedObservationAtBackground”,
    “SimulatedObservationAtCurrentOptimum”,
    “SimulatedObservationAtCurrentState”,
    “SimulatedObservationAtOptimum”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

Variant
:   *Predefined name*. This key allows to choose one of the possible variants
    for the main algorithm. The default variant is the original “DualAnnealing”,
    and the possible choices are
    “GeneralizedSimulatedAnnealing” (Generalized Simulated Annealing ou GSA),
    “DualAnnealing” (Dual Annealing).

    It is recommended to try the “DualAnnealing” variant with a very small number
    of iterations and a limited number of simulation function evaluations.

    Example :
    `{"Variant":"DualAnnealing"}`

## 13.15.4. Information and variables available at the end of the algorithm

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

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

Analysis
:   *List of vectors*. Each element of this variable is an optimal state
    $\mathbf{x}^*$ in optimization, an interpolate or an analysis
    $\mathbf{x}^a$ in data assimilation.

    Example:
    `xa = ADD.get("Analysis")[-1]`

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

CostFunctionJAtCurrentOptimum
:   *List of values*. Each element is a value of the error function $J$.
    At each step, the value corresponds to the optimal state found from the
    beginning.

    Example:
    `JACO = ADD.get("CostFunctionJAtCurrentOptimum")[:]`

CostFunctionJbAtCurrentOptimum
:   *List of values*. Each element is a value of the error function $J^b$. At
    each step, the value corresponds to the optimal state found from the
    beginning. If this part does not exist in the error function, its value is
    zero.

    Example:
    `JbACO = ADD.get("CostFunctionJbAtCurrentOptimum")[:]`

CostFunctionJoAtCurrentOptimum
:   *List of values*. Each element is a value of the error function $J^o$,
    that is of the observation difference part. At each step, the value
    corresponds to the optimal state found from the beginning.

    Example:
    `JoACO = ADD.get("CostFunctionJoAtCurrentOptimum")[:]`

CurrentIterationNumber
:   *List of integers*. Each element is the iteration index at the current step
    during the iterative algorithm procedure. There is one iteration index value
    per assimilation step corresponding to an observed state.

    Example:
    `cin = ADD.get("CurrentIterationNumber")[-1]`

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

IndexOfOptimum
:   *List of integers*. Each element is the iteration index of the optimum
    obtained at the current step of the iterative algorithm procedure of the
    optimization algorithm. It is not necessarily the number of the last
    iteration.

    Example:
    `ioo = ADD.get("IndexOfOptimum")[-1]`

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

## 13.15.5. See also

References to other sections:

- [Calculation algorithm “DerivativeFreeOptimization”](ref_algorithm_DerivativeFreeOptimization.md#section-ref-algorithm-derivativefreeoptimization)
- [Calculation algorithm “DifferentialEvolution”](ref_algorithm_DifferentialEvolution.md#section-ref-algorithm-differentialevolution)
- [Calculation algorithm “ParticleSwarmOptimization”](ref_algorithm_ParticleSwarmOptimization.md#section-ref-algorithm-particleswarmoptimization)
- [Calculation algorithm “TabuSearch”](ref_algorithm_TabuSearch.md#section-ref-algorithm-tabusearch)

Bibliographical references:

- [[Kirkpatrick83]](bibliography.md#kirkpatrick83)
- [[Tsallis96]](bibliography.md#tsallis96)
- [[WikipediaSA]](bibliography.md#wikipediasa)
- [[Xiang97]](bibliography.md#xiang97)
