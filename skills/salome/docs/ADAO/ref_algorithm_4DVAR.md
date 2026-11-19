<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_4DVAR.html -->

# 13.2. Calculation algorithm “*4DVAR*”

## 13.2.1. Description

This algorithm realizes an estimation of the state of a dynamic system, by a
variational minimization method of the classical $J$ function in data
assimilation:

$$J(\mathbf{x})=(\mathbf{x}-\mathbf{x}^b)^T.\mathbf{B}^{-1}.(\mathbf{x}-\mathbf{x}^b)+\sum_{t\in T}(\mathbf{y^o}(t)-H(\mathbf{x},t))^T.\mathbf{R}^{-1}.(\mathbf{y^o}(t)-H(\mathbf{x},t))$$

which is usually designed as the “*4D-Var*” functional (see for example
[[Talagrand97]](bibliography.md#talagrand97)). The terms “*4D-Var*”, “*4D-VAR*” and “*4DVAR*” are equivalent.
This mono-objective optimization algorithm is naturally written for a single
estimate on a time window for the simulation. It is well suited in cases of
non-linear observation and evolution operators, its application domain is
similar to the one of Kalman filters, specially the
[Calculation algorithm “ExtendedKalmanFilter”](ref_algorithm_ExtendedKalmanFilter.md#section-ref-algorithm-extendedkalmanfilter) or the
[Calculation algorithm “UnscentedKalmanFilter”](ref_algorithm_UnscentedKalmanFilter.md#section-ref-algorithm-unscentedkalmanfilter).

## 13.2.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The optimization methods proposed by this algorithm perform a **non-local
  search for the minimum**, without however ensuring a global search. This is
  the case when optimization methods have the ability to avoid being trapped by
  the first local minimum found. These capabilities are sometimes heuristic.

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

## 13.2.3. Optional and required commands

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

ConstrainedBy
:   *Predefined name*. This key allows to choose the method to take into account
    the bounds constraints. The only one available is the “EstimateProjection”,
    which projects the current state estimate on the bounds constraints.

    Example:
    `{"ConstrainedBy":"EstimateProjection"}`

CostDecrementTolerance
:   *Real value*. This key indicates a limit value, leading to stop successfully
    the iterative optimization process when the cost function decreases less than
    this tolerance at the last step. The default is 1.e-7, and it is recommended
    to adapt it to the needs on real problems. One can refer to the section
    describing ways for [Convergence control for calculation cases and iterative algorithms](advanced.md#subsection-iterative-convergence-control) for more
    detailed recommendations.

    Example:
    `{"CostDecrementTolerance":1.e-7}`

EstimationOf
:   *Predefined name*. This key allows to choose the type of estimation to be
    performed. It can be either state-estimation, with a value of “State”, or
    parameter-estimation, with a value of “Parameters”. The default choice is
    “State”.

    Example:
    `{"EstimationOf":"Parameters"}`

GradientNormTolerance
:   *Real value*. This key indicates a limit value, leading to stop successfully
    the iterative optimization process when the norm of the gradient is under
    this limit. It is only used for non-constrained optimizers. The default is
    1.e-5 and it is not recommended to change it.

    Example:
    `{"GradientNormTolerance":1.e-5}`

InitializationPoint
:   *Vector*. The variable specifies one vector to be used as the initial state
    around which an iterative algorithm starts. By default, this initial state is
    not required and is equal to the background $\mathbf{x}^b$. Its value
    must allow to build a vector of the same size as the background. If provided,
    it replaces the background only for initialization.

    Example :
    `{"InitializationPoint":[1, 2, 3, 4, 5]}`

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

Minimizer
:   *Predefined name*. This key allows to choose the optimization minimizer. The
    default choice is “LBFGSB”, and the possible ones are
    “LBFGSB” (nonlinear constrained minimizer, see [[Byrd95]](bibliography.md#byrd95), [[Morales11]](bibliography.md#morales11), [[Zhu97]](bibliography.md#zhu97)),
    “TNC” (nonlinear constrained minimizer),
    “CG” (nonlinear unconstrained minimizer),
    “BFGS” (nonlinear unconstrained minimizer),
    It is highly recommended to keep the default value.

ProjectedGradientTolerance
:   *Real value*. This key indicates a limit value, leading to stop successfully
    the iterative optimization process when all the components of the projected
    gradient are under this limit. It is only used for constrained optimizers.
    The default is -1, that is the internal default of each minimizer (generally
    1.e-5), and it is not recommended to change it.

    Example:
    `{"ProjectedGradientTolerance":-1}`

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
    “CostFunctionJAtCurrentOptimum”,
    “CostFunctionJb”,
    “CostFunctionJbAtCurrentOptimum”,
    “CostFunctionJo”,
    “CostFunctionJoAtCurrentOptimum”,
    “CurrentIterationNumber”,
    “CurrentOptimum”,
    “CurrentState”,
    “EnsembleOfSimulations”,
    “EnsembleOfStates”,
    “IndexOfOptimum”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 13.2.4. Information and variables available at the end of the algorithm

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

## 13.2.5. See also

References to other sections:

- [Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar)
- [Calculation algorithm “KalmanFilter”](ref_algorithm_KalmanFilter.md#section-ref-algorithm-kalmanfilter)
- [Calculation algorithm “ExtendedKalmanFilter”](ref_algorithm_ExtendedKalmanFilter.md#section-ref-algorithm-extendedkalmanfilter)
- [Calculation algorithm “EnsembleKalmanFilter”](ref_algorithm_EnsembleKalmanFilter.md#section-ref-algorithm-ensemblekalmanfilter)

Bibliographical references:

- [[Byrd95]](bibliography.md#byrd95)
- [[Morales11]](bibliography.md#morales11)
- [[Talagrand97]](bibliography.md#talagrand97)
- [[Zhu97]](bibliography.md#zhu97)
