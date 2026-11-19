<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_ParticleSwarmOptimization.html -->

# 13.13. Calculation algorithm “*ParticleSwarmOptimization*”

## 13.13.1. Description

This algorithm estimates the state of a system, by minimizing a cost function
$J$, using an evolutionary particle swarm method. It is a meta-heuristic
that does not require any particular information about the functional, and does
not require derivatives (except in its hybrid “VLS” version).

It falls in the same category than the
[Calculation algorithm “DerivativeFreeOptimization”](ref_algorithm_DerivativeFreeOptimization.md#section-ref-algorithm-derivativefreeoptimization),
[Calculation algorithm “DifferentialEvolution”](ref_algorithm_DifferentialEvolution.md#section-ref-algorithm-differentialevolution),
[Calculation algorithm “SimulatedAnnealing”](ref_algorithm_SimulatedAnnealing.md#section-ref-algorithm-simulatedannealing),
[Calculation algorithm “TabuSearch”](ref_algorithm_TabuSearch.md#section-ref-algorithm-tabusearch).

This is a mono-objective optimization method, allowing for global minimum
search of a general error function $J$ of type $L^1$, $L^2$
or $L^{\infty}$, with or without weights, as described in the section for
[Going further in the state estimation by optimization methods](theory.md#section-theory-optimization). As it is an optimization meta-heuristic,
reaching a global or local optimal result is nevertheless not guaranteed
(except in its hybrid “VLS” version). The default error function is the
augmented weighted least squares function, classically used in data
assimilation.

It is based on the evolution of a population (called a “swarm”) of states (each
state is called a “particle” or an “insect”). There exists various variants of
this algorithm. The following stable and robust formulations are proposed here:

- “CanonicalPSO” (Canonical Particle Swarm Optimization, see
  [[ZambranoBigiarini13]](bibliography.md#zambranobigiarini13)), classical algorithm called “canonical” of particle
  swarm, robust and defining a reference for particle swarm algorithms,
- “OGCR” (Simple Particle Swarm Optimization), simplified algorithm of
  particle swarm with no bounds on insects or velocities, not recommended
  because less robust, but sometimes a lot more efficient,
- “SPSO-2011” (Standard Particle Swarm Optimization 2011, voir
  [[ZambranoBigiarini13]](bibliography.md#zambranobigiarini13)), 2011 reference algorithm of particle swarm, robust,
  efficient and defined as a reference for particle swarm algorithms. This
  algorithm is sometimes called “$\omega$-PSO” or “Inertia PSO” because
  it incorporates a so-called inertia contribution, or also called “AIS” (for
  “Asynchronous Iteration Strategy”) or “APSO” (for “Advanced Particle Swarm
  Optimization”) because it incorporates evolutionary updating of the best
  elements, leading to intrinsically improved convergence of the algorithm.
- “SPSO-2011-SIS” (Standard Particle Swarm Optimisation 2011 with Synchronous
  Iteration Strategy), very similar to the 2011 reference algorithm, and with
  a synchronous particle update, called “SIS”,
- “SPSO-2011-PSIS” (Standard Particle Swarm Optimisation 2011 with Parallel
  Synchronous Iteration Strategy), similar to the “SPSO-2011-SIS” algorithm
  with synchronous updating and parallelization, known as “PSIS”, of the
  particles.

Each of the above methods can have the local aspect of its search accelerated
by a “VLS” (Variational Local Search) method concerning the best insects in the
swarm. The global aspect of the search remains preserved by the particle swarm
method, but great care must be taken experimentally to avoid premature
stagnation of the best particles in the swarm. Simply suffix the name of the
algorithm variant with “-VLS” to activate the acceleration, e.g.
“CanonicalPSO-VLS”.

The following are a few practical suggestions for the effective use of these
algorithms:

- The recommended variant of this algorithm is the “SPSO-2011” even if the
  “CanonicalPSO” algorithm remains by default the more robust one. If the state
  evaluation can be carried out in parallel, the “SPSO-2011-PSIS” algorithm can
  be used, even if its convergence is sometimes a little less efficient.
- The number of particles or insects usually recommended varies between 40 and
  100 depending on the algorithm, more or less independently of the dimension
  of the state space. Usually, the best performances are obtained for
  populations of 70 to 500 particles. Even if the default value for this
  elementary parameter comes from extended knowledge on these algorithms, it is
  recommended to adapt it to the difficulty of the given problems.
- The recommended number of generations for population evolution is often
  around 50, but it can easily vary between 25 and 500.
- The maximum number of evaluations of the simulation function should usually
  be limited to between a few thousand and a few tens of thousands of times the
  dimension of the state space.
- The error functional usually decreases by levels (thus with a zero
  progression of the value of the functional at each generation when we stay in
  the level), making it *not recommended* to stop on the criterion of decrease
  of the cost function. It is normally wiser to adapt the number of iterations
  or generations to accelerate the convergence of the algorithms.
- If the problem is constrained, it is necessary to define the bounds of the
  variables (by the variable “*Bounds*”). If the problem is totally
  unconstrained, it is essential to define increment bounds (by the variable
  “*BoxBounds*”) to delimit the optimal search in a useful way. Similarly, if
  the problem is partially constrained, it is recommended (but not required) to
  define increment bounds. In case these increment bounds are not defined, the
  variable bounds will be used as increment bounds.
- The use of hybrid “VLS”-type acceleration variants will require the
  availability of the operator gradient (either given explicitly or requested
  by finite differences at definition), but normally speeds up the local
  search. It is therefore a good idea to reduce the number of generations
  (which can sometimes be reduced to as few as 5 or 10), while specifying a
  reasonable number of insects (of the order of 1 to 5, for example) to be the
  subject of this local search. However, the parameters of the hybrid search
  have to be finely tuned for each case, in the form of a compromise, in order
  to have both the global and local capacity of this optimization. Indeed, too
  fast local convergence or too limited global exploration can reduce the
  algorithm’s ability to explore the solution space.

These suggestions are to be used as experimental indications, not as
requirements, because they are to be appreciated or adapted according to the
physics of each problem that is treated.

The count of the number of evaluations of the function to be simulated during
this algorithm is deterministic, namely the “*number of iterations or
generations*” multiplied by the “*number of individuals in the population*”.
With the default values of 40 to 100 individuals on 50 generations, it takes
between 40x50=2000 and 100*50=5000 evaluations, which is significantly more
than in variational optimization. It is for this reason that this algorithm is
usually interesting when the dimension of the state space is large, or when the
non-linearity of the simulation make the evaluation of the gradient of the
functional by numerical approximation complicated or invalid. But it is also
necessary that the calculation of the function to be simulated is not too
costly to avoid a prohibitive optimization time length.

To reduce the number of generations, we can use the ASAPSO adaptive method
[[Wang09]](bibliography.md#wang09) to modify the localization of the optimal swarm search. This consists
in linearly reducing the algorithm’s global search behavior, thus favoring
swarm localization. When the problem is favorable, it’s possible to reduce the
number of generations by a factor of 2 to 5, while still achieving virtually
the same quality for the best particle. Two keywords are available to control
the use of this adaptive method.

As with other algorithms, it is possible to compute a quantity called the *a
posteriori* covariance of the particle swarm. However, the meaning of the
indicator calculated here differs in nature from a covariance established in
filtering or variational analysis, for example. The indicator is calculated, in
the standard way, as the dispersion of all the particles. But its value is to
be compared exclusively with the evaluation of the same quantity for the
initial swarm, and used in a relative sense of variation between the beginning
and the end of the algorithm’s optimal search. This is because the initial
dispersion of the particles is controlled by the initialization parameters of
the swarm, whose aim is to cover the search space, and the final dispersion of
the particles reflects the localization performance of the optimal search.
Unlike the covariance of the background errors, which is classically involved
in calculating the objective to be optimized and is related to the variance of
the optimal state, the covariance calculated *a posteriori* reflects only the
dispersion of the particles. For the correct use of this algorithm, when the *a
posteriori* covariance calculation is requested, it is performed for the
initial swarm and for the final swarm.

## 13.13.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The optimization methods proposed by this algorithm perform a **non-local
  search for the minimum**, without however ensuring a global search. This is
  the case when optimization methods have the ability to avoid being trapped by
  the first local minimum found. These capabilities are sometimes heuristic.

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
  more number criteria**. In practice, there may be simultaneously several
  convergence criteria.

  The number is frequently a significant value for the algorithm, such as a
  number of iterations or a number of evaluations, but it can also be, for
  example, a number of generations for an evolutionary algorithm.

  Convergence thresholds need to be carefully adjusted, to reduce the gobal
  calculation cost, or to ensure that convergence is adapted to the physical
  case encountered.

## 13.13.3. Optional and required commands

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

BoxBounds
:   *List of pairs of real values*. This key allows to define pairs of upper and
    lower bounds for *increments* on every state variable being optimized (and
    not on state variables themselves, whose bounds can be indicated by the
    “*Bounds*” variable). Increment bounds have to be given by a list of list of
    pairs of lower/upper bounds for each increment on variable, with a value of
    `None` each time there is no bound. This key is only required if there are
    no variable bounds, and there are no default values.

    Example :
    `{"BoxBounds":[[-0.5,0.5], [0.01,2.], [0.,None], [None,None]]}`

CognitiveAcceleration
:   *Real value*. This key indicates the recall rate at the best previously known
    value of the current insect’s history. It is a floating point positive value.
    The default value is about $1/2+ln(2)=1.19315$, and it is recommended
    to adapt it, rather by reducing it, to the physical case that is being
    treated.

    In the standard (non-adaptive) case, this rate is constant and is equal to
    the indicated value. In the ASAPSO adaptive case [[Wang09]](bibliography.md#wang09), the value of this
    key indicates the initial recall rate, which then decreases linearly with the
    number of generations and the associated “*CognitiveAccelerationControl*”
    factor.

    Example :
    `{"CognitiveAcceleration":1.19315}`

CognitiveAccelerationControl
:   *Real value*. This key indicates the factor of change in the recall rate
    towards the best previously known value of the current insect’s history. It
    is a positive real value whose default is 0, that is, by default, there is no
    change in the recall rate.

    In the ASAPSO adaptive case [[Wang09]](bibliography.md#wang09), the value of this key indicates the
    **linear decrease** factor of the recall rate with the number of generations
    (with respect to the requested total number of generations), given that the
    initial value of the rate is indicated by the associated
    “*CognitiveAcceleration*” factor. There is no recommended value, but you
    could, for example, use the initial value $1.19315$ of the associated
    factor if you want to cancel any recall towards the best known value of the
    history at the end of the iterations.

    Example :
    `{"CognitiveAccelerationControl":0.}`

DistributionByComponents
:   *List of predefined names*. This keyword only needs to be defined when the
    particle swarm initialization keyword “*SwarmInitialization*” for the
    “*ParticleSwarmOptimization*” algorithm is set to
    “*DistributionByComponents*”. In this case, for each state component, the
    chosen distribution must be indicated in the form of a predefined name.
    Possible names are “uniform”, “loguniform”, “logarithmic”, “[‘normal’,σ]”,
    “[‘lognormal’,σ]” and “[‘logarithmicnormal’,σ]”. All “*normal*” distributions
    must be accompanied by an indication of the standard deviation σ, given that
    they are centered in the definition domain (so the mean is imposed and does
    not need to be specified). The values “uniform”, “loguniform”, “normal”,
    “lognormal” only affect position initialization by applying the indicated
    distribution, while the values “logarithmic” and “logarithmicnormal” affect
    both position and motion initialization. There must be the same number of
    values indicated as the size of an individual state. Distributions conform to
    the limits specified for the “*ParticleSwarmOptimization*” algorithm.
    Distributions can be different for each axis. When an identical distribution
    is chosen for all components, this is equivalent to choosing the global value
    of the previous “*SwarmInitialization*” keyword instead, if it exists.

    Example :
    `{"DistributionByComponents" : ['uniform', 'loguniform', 'logarithmic', ['normal', 1]]}` for a state space of dimension 4.

GlobalCostReductionTolerance
:   *Real value*. This key indicates the limit reduction factor, leading to the
    iterative optimization process being stopped when the cost function decreases
    by at least this tolerance over the entire optimal search. The default value
    is 1.e-16 (equivalent to no effect), and it is recommended to adapt it to the
    needs of real problems.

    Example:
    `{"GlobalCostReductionTolerance":1.e-16}`

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

HybridNumberOfLocalHunters
:   *Integer value*. This key indicates the number of insects on which the local
    search will be conducted. Insects are chosen as the best from the current
    iteration of the global search. With a default value of 1, the local search
    is performed on the best insect only. It is then recommended to adapt this
    parameter to the needs on real problems.

    Example :
    `{"HybridNumberOfLocalHunters":1}`

HybridNumberOfWarmupIterations
:   *Integer value*. This key indicates the number of initial iterations of the
    global search performed **before** establishing a local search on the best
    insects. By default, with a value of 0, the local search is performed from
    the first iterative step of the global search.

    Example :
    `{"HybridNumberOfWarmupIterations":0}`

InertiaWeight
:   *Real value*. This key indicates the part of the insect velocity which is
    imposed by the swarm, named “inertia weight”. It is a positive floating point
    value. It is a floating point value between 0 and 1. The default value is
    about $1/(2*ln(2))$ and it is recommended to adapt it to the physical
    case that is being treated.

    Example :
    `{"InertiaWeight":0.72135}`

InitializationPoint
:   *Vector*. The variable specifies one vector to be used as the initial state
    around which an iterative algorithm starts. By default, this initial state is
    not required and is equal to the background $\mathbf{x}^b$. Its value
    must allow to build a vector of the same size as the background. If provided,
    it replaces the background only for initialization.

    Example :
    `{"InitializationPoint":[1, 2, 3, 4, 5]}`

MaximumNumberOfFunctionEvaluations
:   *Integer value*. This key indicates the maximum number of evaluation of the
    cost function to be optimized. The default is 15000, which is an arbitrary
    limit. It is then recommended to adapt this parameter to the needs on real
    problems. For some optimizers, the effective number of function evaluations
    can be slightly different of the limit due to algorithm internal control
    requirements.

    Example:
    `{"MaximumNumberOfFunctionEvaluations":50}`

MaximumNumberOfIterations
:   *Integer value*. This key indicates the maximum number of internal iterations
    allowed for iterative optimization. The default is 50, which is an arbitrary
    limit. It is then recommended to adapt this parameter to the needs on real
    problems.

    Example:
    `{"MaximumNumberOfIterations":50}`

NumberOfInsects
:   *Integer value*. This key indicates the number of insects or particles in the
    swarm. The default is 100, which is a usual default for this algorithm.

    Example :
    `{"NumberOfInsects":100}`

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

SocialAcceleration
:   *Real value*. This key indicates the recall rate towards the best insect in
    the current insect’s neighborhood, which by default is the complete swarm. It
    is a floating point positive value. The default value is about
    $1/2+ln(2)=1.19315$ and it is recommended to adapt it, rather by
    reducing it, to the physical case that is being treated.

    In the standard (non-adaptive) case, this rate is constant and is equal to
    the indicated value. In the ASAPSO adaptive case [[Wang09]](bibliography.md#wang09), the value of this
    key indicates the initial recall rate, which then increases linearly with the
    number of generations and the associated “*SocialAccelerationControl*”
    factor.

    Example :
    `{"SocialAcceleration":1.19315}`

SocialAccelerationControl
:   *Real value*. This key indicates the factor of change in the recall rate
    towards the best insect in the current insect’s neighborhood, which by
    default is the complete swarm. It is a positive real value whose default is
    0, that is, by default, there is no change in the recall rate.

    In the ASAPSO adaptive case [[Wang09]](bibliography.md#wang09), the value of this key indicates the
    **linear growth** factor of the recall rate with the number of generations (
    with respect to the requested total number of generations), given that the
    initial value of the rate is indicated by the associated
    “*SocialAcceleration*” factor. There is no recommended value, but you can use
    the initial value $1.19315$ of the associated factor, for example, if
    you want to double the recall towards the best known value of the
    neighborhood at the end of the iterations.

    Example :
    `{"SocialAccelerationControl":0.}`

StoreInitialState
:   *Boolean value*. This variable defines whether the algorithm’s initial state
    is stored (with True) or not (with False, by default) as the first state in
    the iterative sequence of found states. This makes algorithmic iterative
    storage identical to temporal iterative storage (similar, for example, to
    Kalman filters).

    Example :
    `{"StoreInitialState":False}`

SwarmInitialization
:   *Predefined name*. The name defines the particle swarm initialization mode
    for the “*ParticleSwarmOptimization*” algorithm. The particle series is
    initialized by specifying the distribution per component, which can be
    identical for all components (this is the case for all values except
    “DistributionByComponents”), or component-specific with
    “DistributionByComponents”. In the latter case, it is also necessary to
    specify the “DistributionByComponents” keyword content. The default value is
    “UniformByComponents”.

    The possible name is therefore in the following list:
    [“UniformByComponents”,
    “LogUniformByComponents”,
    “LogarithmicByComponents”,
    “DistributionByComponents”].

    Example :
    `{"SwarmInitialization":"UniformByComponents"}`

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
    “CostFunctionJb”,
    “CostFunctionJo”,
    “CurrentIterationNumber”,
    “CurrentState”,
    “EnsembleOfStates”,
    “EnsembleOfSimulations”,
    “Innovation”,
    “InternalCostFunctionJ”,
    “InternalCostFunctionJb”,
    “InternalCostFunctionJo”,
    “OMA”,
    “OMB”,
    “SimulatedObservationAtBackground”,
    “SimulatedObservationAtCurrentState”,
    “SimulatedObservationAtOptimum”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

SwarmTopology
:   *Predefined name*. This key indicates how the particles (or insects)
    communicate information to each other during the evolution of the particle
    swarm. The most classical method consists in exchanging information between
    all particles (called “gbest” or “FullyConnectedNeighborhood”). But it is
    often more efficient to exchange information on a reduced neighborhood, as in
    the classical method “lbest” (or “RingNeighborhoodWithRadius1”) exchanging
    information with the two neighboring particles in numbering order (the
    previous one and the next one), or the method “RingNeighborhoodWithRadius2”
    exchanging with the 4 neighbors (the two previous ones and the two following
    ones). A variant of reduced neighborhood consists in exchanging with 3
    neighbors (method “AdaptativeRandomWith3Neighbors”) or 5 neighbors (method
    “AdaptativeRandomWith5Neighbors”) chosen randomly (the particle can be drawn
    several times). The default value is “FullyConnectedNeighborhood”, and it is
    advisable to change it carefully depending on the properties of the simulated
    physical system. The possible communication topology is to be chosen from the
    following list, in which the equivalent names are indicated by a “<=>” sign:
    [“FullyConnectedNeighborhood” <=> “FullyConnectedNeighbourhood” <=> “gbest”,
    “RingNeighborhoodWithRadius1” <=> “RingNeighbourhoodWithRadius1” <=> “lbest”,
    “RingNeighborhoodWithRadius2” <=> “RingNeighbourhoodWithRadius2”,
    “AdaptativeRandomWith3Neighbors” <=> “AdaptativeRandomWith3Neighbours” <=> “abest”,
    “AdaptativeRandomWith5Neighbors” <=> “AdaptativeRandomWith5Neighbours”].

    Example :
    `{"SwarmTopology":"FullyConnectedNeighborhood"}`

Variant
:   *Predefined name*. This key allows to choose one of the possible variants for
    the main algorithm. The default variant is the original “CanonicalPSO”, and
    the possible choices are
    “CanonicalPSO” (Canonical Particle Swarm Optimization),
    “OGCR” (Simple Particle Swarm Optimization),
    “SPSO-2011” (Standard Standard Particle Swarm Optimization 2011)
    identical to
    “SPSO-2011-AIS” (Standard Standard Particle Swarm Optimisation 2011 with Asynchronous Iteration Strategy),
    “SPSO-2011-SIS” (Standard Particle Swarm Optimisation 2011 with Synchronous Iteration Strategy),
    “SPSO-2011-PSIS” (Standard Particle Swarm Optimisation 2011 with Parallel Synchronous Iteration Strategy).
    The local accelerated “VLS” (Variational Local Search) versions are obtained
    by adding the suffix “-VLS” to each method:
    “CanonicalPSO-VLS”,
    “OGCR-VLS”,
    “SPSO-2011-AIS-VLS”,
    “SPSO-2011-SIS-VLS”,
    “SPSO-2011-PSIS-VLS”.

    It is recommended to try the “CanonicalPSO” variant with about 100 particles
    for robust performance, and to reduce the number of particles to about 40
    for all variants other than the original “CanonicalPSO” formulation.

    Example :
    `{"Variant":"CanonicalPSO"}`

VelocityClampingFactor
:   *Real value*. This key indicates the rate of group velocity attenuation in
    the update for each insect, useful to avoid swarm explosion, i.e.
    uncontrolled growth of insect velocity. It is a floating point value between
    0+ and 1. The default value is 0.3.

    Example :
    `{"VelocityClampingFactor":0.3}`

## 13.13.4. Information and variables available at the end of the algorithm

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

CurrentIterationNumber
:   *List of integers*. Each element is the iteration index at the current step
    during the iterative algorithm procedure. There is one iteration index value
    per assimilation step corresponding to an observed state.

    Example:
    `cin = ADD.get("CurrentIterationNumber")[-1]`

CurrentState
:   *List of vectors*. Each element is a usual state vector used during the
    iterative algorithm procedure.

    Example:
    `xs = ADD.get("CurrentState")[:]`

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

Innovation
:   *List of vectors*. Each element is an innovation vector, which is in static
    the difference between the optimal and the background, and in dynamic the
    evolution increment.

    Example:
    `d = ADD.get("Innovation")[-1]`

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

## 13.13.5. Python (TUI) use examples

Here is one or more very simple examples of the proposed algorithm and its
parameters, written in [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). Moreover, when it is possible, the
information given as input also allows to define an equivalent case in
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome).

This example describes the calibration of parameters $\mathbf{x}$ of a
quadratic observation model $H$. This model is here represented as a
function named `QuadFunction`. This function get as input the coefficients
vector $\mathbf{x}$, and return as output the evaluation vector
$\mathbf{y}$ of the quadratic model at the predefined internal control
points. The calibration is done using an initial coefficient set (background
state specified by `Xb` in the code), and with the information
$\mathbf{y}^o$ (specified by `Yobs` in the code) of 5 measures obtained
in these same internal control points. We set twin experiments (see
[To test a data assimilation chain: the twin experiments](methodology.md#section-methodology-twin)) and the measurements are supposed to be
perfect. We choose to emphasize the observations versus the background by
setting a great variance for the background error, here of $10^{6}$.

The adjustment is carried out by displaying intermediate results during
iterative optimization.

```python
# -*- coding: utf-8 -*-
#
from numpy import array, ravel
def QuadFunction( coefficients ):
    """
    Quadratic simulation in x points: y = a x^2 + b x + c
    """
    a, b, c = list(ravel(coefficients))
    x_points = (-5, 0, 1, 3, 10)
    y_points = []
    for x in x_points:
        y_points.append( a*x*x + b*x + c )
    return array(y_points)
#
Xb   = array([1., 1., 1.])
Yobs = array([57, 2, 3, 17, 192])
#
NumberOfInsects = 40
#
print("Resolution of the calibration problem")
print("-------------------------------------")
print("")
from adao import adaoBuilder
case = adaoBuilder.New()
case.setBackground( Vector = Xb, Stored=True )
case.setBackgroundError( ScalarSparseMatrix = 1.e6 )
case.setObservation( Vector = Yobs, Stored=True )
case.setObservationError( ScalarSparseMatrix = 1. )
case.setObservationOperator( OneFunction = QuadFunction )
case.setAlgorithmParameters(
    Algorithm="ParticleSwarmOptimization",
    Parameters={
        "NumberOfInsects":NumberOfInsects,
        "MaximumNumberOfIterations": 20,
        "StoreSupplementaryCalculations": [
            "CurrentState",
            ],
        "Bounds":[[0,5],[-2,2],[0,5]],
        "SetSeed":123456789,
        },
    )
case.setObserver(
    Info="  Intermediate state at the current iteration:",
    Template="ValuePrinter",
    Variable="CurrentState",
    )
case.execute()
print("")
#
#-------------------------------------------------------------------------------
#
print("Calibration of %i coefficients in a 1D quadratic function on %i measures"%(
    len(case.get("Background")),
    len(case.get("Observation")),
    ))
print("----------------------------------------------------------------------")
print("")
print("Observation vector.................:", ravel(case.get("Observation")))
print("A priori background state..........:", ravel(case.get("Background")))
print("")
print("Expected theoretical coefficients..:", ravel((2,-1,2)))
print("")
print("Number of iterations...............:", len(case.get("CurrentState")))
print("Number of simulations..............:", NumberOfInsects*len(case.get("CurrentState")))
print("Calibration resulting coefficients.:", ravel(case.get("Analysis")[-1]))
#
Xa = case.get("Analysis")[-1]
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10, 4)
#
plt.figure()
plt.plot((-5,0,1,3,10),QuadFunction(Xb),"b--",label="Simulation at background")
plt.plot((-5,0,1,3,10),Yobs,            "kX", label="Observation",markersize=10)
plt.plot((-5,0,1,3,10),QuadFunction(Xa),"r-", label="Simulation at optimum")
plt.legend()
plt.title("Coefficients calibration", fontweight="bold")
plt.xlabel("Arbitrary coordinate")
plt.ylabel("Observations")
plt.savefig("simple_ParticleSwarmOptimization1.png")
```

The execution result is the following:

```none
Resolution of the calibration problem
-------------------------------------

  Intermediate state at the current iteration: [ 1.76770856 -1.2054263   1.22625259]
  Intermediate state at the current iteration: [ 2.04776518 -1.17449716  3.14493347]
  Intermediate state at the current iteration: [ 2.04776518 -1.17449716  3.14493347]
  Intermediate state at the current iteration: [ 2.01933291 -1.          3.15162067]
  Intermediate state at the current iteration: [ 1.96384202 -0.74855119  3.40642058]
  Intermediate state at the current iteration: [ 1.96384202 -0.74855119  3.40642058]
  Intermediate state at the current iteration: [ 1.96384202 -0.74855119  3.40642058]
  Intermediate state at the current iteration: [ 1.96384202 -0.74855119  3.40642058]
  Intermediate state at the current iteration: [ 1.95417745 -0.73191939  3.14451887]
  Intermediate state at the current iteration: [ 1.96217646 -0.7883895   2.91127919]
  Intermediate state at the current iteration: [ 1.97610485 -1.00254825  2.89582746]
  Intermediate state at the current iteration: [ 2.0007262  -1.06443275  2.69825603]
  Intermediate state at the current iteration: [ 1.9934285  -1.02432071  2.39823319]
  Intermediate state at the current iteration: [ 1.9934285  -1.02432071  2.39823319]
  Intermediate state at the current iteration: [ 1.9942533  -0.99256953  2.30174702]
  Intermediate state at the current iteration: [ 1.9942533  -0.99256953  2.30174702]
  Intermediate state at the current iteration: [ 1.99742923 -0.99796085  2.1278678 ]
  Intermediate state at the current iteration: [ 1.99742923 -0.99796085  2.1278678 ]
  Intermediate state at the current iteration: [ 1.99742923 -0.99796085  2.1278678 ]
  Intermediate state at the current iteration: [ 1.99742923 -0.99796085  2.1278678 ]
  Intermediate state at the current iteration: [ 2.00166149 -1.0012696   2.02137857]

Calibration of 3 coefficients in a 1D quadratic function on 5 measures
----------------------------------------------------------------------

Observation vector.................: [ 57.   2.   3.  17. 192.]
A priori background state..........: [1. 1. 1.]

Expected theoretical coefficients..: [ 2 -1  2]

Number of iterations...............: 21
Number of simulations..............: 840
Calibration resulting coefficients.: [ 2.00166149 -1.0012696   2.02137857]
```

The figures illustrating the result of its execution are as follows:

[![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/simple_ParticleSwarmOptimization1.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/simple_ParticleSwarmOptimization1.png)

## 13.13.6. See also

References to other sections:

- [Calculation algorithm “DerivativeFreeOptimization”](ref_algorithm_DerivativeFreeOptimization.md#section-ref-algorithm-derivativefreeoptimization)
- [Calculation algorithm “DifferentialEvolution”](ref_algorithm_DifferentialEvolution.md#section-ref-algorithm-differentialevolution)
- [Calculation algorithm “SimulatedAnnealing”](ref_algorithm_SimulatedAnnealing.md#section-ref-algorithm-simulatedannealing)
- [Calculation algorithm “TabuSearch”](ref_algorithm_TabuSearch.md#section-ref-algorithm-tabusearch)

Bibliographical references:

- [[Wang09]](bibliography.md#wang09)
- [[WikipediaPSO]](bibliography.md#wikipediapso)
- [[ZambranoBigiarini13]](bibliography.md#zambranobigiarini13)
