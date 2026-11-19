<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_EnsembleOfSimulationGenerationTask.html -->

# 15.1. Task algorithm “*EnsembleOfSimulationGenerationTask*”

This algorithm is reserved for use in the textual user interface (TUI), and
therefore not in graphical user interface (GUI).

## 15.1.1. Description

This algorithm allows to generate a set of physical results, of simulation or
observation type, using the $H$ operator for a design of experiment of
the $\mathbf{x}$ parametric state space. The result of this algorithm is
a homogeneous collection of simulated vectors $\mathbf{y}$ (available
using the storable variable “*EnsembleOfSimulations*”) corresponding directly
to the chosen homogeneous collection of state vectors $\mathbf{x}$
(available using the storable variable “*EnsembleOfStates*”).

The sampling of the states $\mathbf{x}$ can be given explicitly or under
form of hypercubes, explicit or sampled according to classic distributions, or
using Latin hypercube sampling (LHS) or Sobol sequences. The computations are
optimized according to the computer resources available and the options
requested by the user. You can refer to the
[Requirements for describing a state sampling](ref_sampling_requirements.md#section-ref-sampling-requirements) for an illustration of sampling.
Beware of the size of the hypercube (and then to the number of computations)
that can be reached, it can grow quickly to be quite large. When a state is not
observable, a *“NaN”* value is returned.

To be visible by the user while reducing the risk of storage difficulties, the
results of sampling or simulations has to be **explicitly** asked for using the
required variable.

The results obtained with this algorithm can be used to feed an
[Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask). In a
complementary way, and if the goal is to evaluate the calculation-measurement
error, an [Checking algorithm “SamplingTest”](ref_algorithm_SamplingTest.md#section-ref-algorithm-samplingtest) uses the same sampling
commands to establish a set of error functional values $J$ from
observations $\mathbf{y}^o$.

## 15.1.2. Some noteworthy properties of the implemented methods

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

## 15.1.3. Optional and required commands

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
textual interface, are indicated in [List of commands and keywords for a dedicated task or study oriented case](ref_task_keywords.md#section-ref-task-keywords). Moreover,
the parameters of the command “*AlgorithmParameters*” allow to choose the
specific options, described hereafter, of the algorithm. See
[Description of options of an algorithm by “AlgorithmParameters”](ref_options_AlgorithmParameters.md#section-ref-options-algorithm-parameters) for the good use of this
command.

The options are the following:

SampleAsExplicitHyperCube
:   *List of list of real values*. This key describes the calculations points as
    an hyper-cube, from a given list of explicit sampling of each variable as a
    list. That is then a list of lists, each of them being potentially of
    different size. By nature, the points are included in the domain defined by
    the bounds of the explicit lists for each variable.

    Example : `{"SampleAsExplicitHyperCube":[[0.,0.25,0.5,0.75,1.], [-2,2,1]]}` for a state space of dimension 2.

SampleAsIndependentRandomVariables
:   *List of triplets [Name, Parameters, Number]*. This key describes the
    calculations points as an hyper-cube, for which the points on each axis come
    from a independent random sampling of the axis variable, under the
    specification of the distribution, its parameters and the number of points in
    the sample, as a list *[Name, Parameters, Number]* for each axis. Unlike
    sampling described by the keyword “*SampleAsIndependentRandomVectors*”,
    points are explicitly distributed over a regular hypercube. The possible
    distribution names are ‘normal’ of parameters (mean,std), ‘lognormal’ of
    parameters (mean,sigma), ‘uniform’ of parameters (low,high), or ‘weibull’ of
    parameter (shape). That is then a list of the same size than the one of the
    state. By nature, the points are included in the unbounded or bounded domain,
    depending on the characteristics of the distributions chosen for each
    variable.

    Example :
    `{"SampleAsIndependentRandomVariables":[['normal',[0.,1.],3], ['uniform',[-2,2],4]]}` for a state space of dimension 2.

SampleAsIndependentRandomVectors
:   *List of pairs [Name, Parameters], plus [Dimension, Number]*. This key
    describes the calculation points in the form of particular distributions
    defined for each dimension, resulting in random vectors whose individual
    components follow the required distribution. Unlike the sampling described by
    the keyword “*SampleAsIndependentRandomVariables*”, the points are not
    distributed over a regular hypercube. The distribution on each axis variable
    is specified by its name and parameters, in the form of a list *[Name,
    Parameters]* for each axis. This list of pairs, whose number is identical to
    the size of the state space, is completed by a pair of integers *[Dimension,
    Number]* containing the dimension of the state space and the desired number
    of sampling points. Possible distribution names are ‘normal’ with parameters
    (mean,std), ‘lognormal’ with parameters (mean,sigma), ‘uniform’ with
    parameters (low,high), ‘loguniform’ with parameters (low,high), or ‘weibull’
    with parameters (shape). By their very nature, points are included in the
    unbounded or bounded domain, depending on the characteristics of the
    distributions chosen for each variable. Distributions can be different for
    each axis.

    Example :
    `{"SampleAsIndependentRandomVectors":[['normal',[0.,1.]], ['uniform',[-2,2]]]}` for a state space of dimension 2.

SampleAsMinMaxHaltonSequence
:   *List of real valued pairs [Min, Max], plus [Dimension, Number]*. This key
    describes the bounded domain in which the calculations points will be placed,
    from a *[Min, Max]* pair for each state component. The lower bounds are
    included. This list of pairs, identical in number to the size of the state
    space, is augmented by a pair of integers *[Dimension, Number]* containing
    the dimension of the state space and the desired number of sample points.
    Sampling is then automatically constructed using the Halton sequence method.
    By nature, the points are included in the domain defined by the explicit
    bounds.

    *Remark: it is required to have Scipy version 1.7.0 or higher to use this
    sampling option.*

    Example :
    `{"SampleAsMinMaxHaltonSequence":[[0.,1.],[-1,3]]+[[2,11]]}` for a state space of dimension 2 and 11 sampling points (there will be 16 points in practice).

SampleAsMinMaxLatinHyperCube
:   *List of real valued pairs [Min, Max], plus [Dimension, Number]*. This key
    describes the bounded domain in which the calculations points will be placed,
    from a *[Min, Max]* pair for each state component. The lower bounds are
    included. This list of pairs, identical in number to the size of the state
    space, is augmented by a pair of integers *[Dimension, Number]* containing
    the dimension of the state space and the desired number of sample points.
    Sampling is then automatically constructed using the Latin hypercube method
    (LHS). By nature, the points are included in the domain defined by the
    explicit bounds.

    Example :
    `{"SampleAsMinMaxLatinHyperCube":[[0.,1.],[-1,3]]+[[2,11]]}` for a state space of dimension 2 and for 11 sampling points.

SampleAsMinMaxSobolSequence
:   *List of real valued pairs [Min, Max], plus [Dimension, Number]*. This key
    describes the bounded domain in which the calculations points will be placed,
    from a *[Min, Max]* pair for each state component. The lower bounds are
    included. This list of pairs, identical in number to the size of the state
    space, is augmented by a pair of integers *[Dimension, Number]* containing
    the dimension of the state space and the minimum desired number of sample
    points (by construction, the number of points generated in the Sobol sequence
    will be the power of 2 immediately above this minimum number). Sampling is
    then automatically constructed using the Sobol sequence method. By nature,
    the points are included in the domain defined by the explicit bounds.

    *Remark: it is required to have Scipy version 1.7.0 or higher to use this
    sampling option.*

    Example :
    `{"SampleAsMinMaxSobolSequence":[[0.,1.],[-1,3]]+[[2,11]]}` for a state space of dimension 2 and 11 sampling points (there will be 16 points in practice).

SampleAsMinMaxStepHyperCube
:   *List of triplets of real values [Min, Max, Step]*. This key describes the
    calculations points as an hyper-cube, from a given list of implicit sampling
    of each variable by a triplet *[Min, Max, Step]*. That is then a list of the
    same size than the one of the state. The bounds are included. By nature, the
    points are included in the domain defined by the explicit bounds.

    Example :
    `{"SampleAsMinMaxStepHyperCube":[[0.,1.,0.25],[-1,3,1]]}` for a state space of dimension 2.

SampleAsnUplet
:   *List of states*. This key describes the calculations points as a list of
    n-uplets, each n-uplet being a state. By nature, points are included in the
    bounded domain defined as the convex envelope of explicitly designated
    points.

    Example :
    `{"SampleAsnUplet":[[0,1,2,3],[4,3,2,1],[-2,3,-4,5]]}` for 3 points in a state space of dimension 4.

SetDebug
:   *Boolean value*. This variable leads to the activation, or not, of the debug
    mode during the function or operator evaluation. The default is “False”, the
    choices are “True” or “False”.

    Example:
    `{"SetDebug":False}`

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
    “EnsembleOfSimulations”,
    “EnsembleOfStates”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 15.1.4. Information and variables available at the end of the algorithm

At the output, after executing the algorithm, there are information and
variables originating from the calculation. The description of
[Variables and information available at the output](ref_output_variables.md#section-ref-output-variables) show the way to obtain them by the method
named `get`, of the variable “*ADD*” of the post-processing in graphical
interface, or of the case in textual interface. The input variables, available
to the user at the output in order to facilitate the writing of post-processing
procedures, are described in an [Inventory of potentially available information at the output](ref_output_variables.md#subsection-r-o-v-inventaire).

**Permanent outputs (non conditional)**

The unconditional outputs of the algorithm are the following:

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

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

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

## 15.1.5. See also

References to other sections:

- [Checking algorithm “FunctionTest”](ref_algorithm_FunctionTest.md#section-ref-algorithm-functiontest)
- [Checking algorithm “ParallelFunctionTest”](ref_algorithm_ParallelFunctionTest.md#section-ref-algorithm-parallelfunctiontest)
- [Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask)
