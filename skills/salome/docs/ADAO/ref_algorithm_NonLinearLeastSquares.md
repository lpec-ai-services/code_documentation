<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_NonLinearLeastSquares.html -->

# 13.12. Calculation algorithm “*NonLinearLeastSquares*”

## 13.12.1. Description

This algorithm realizes a state estimation by variational minimization of the
classical $J$ function of weighted “Least Squares”:

$$J(\mathbf{x})=(\mathbf{y}^o-\mathbf{H}.\mathbf{x})^T.\mathbf{R}^{-1}.(\mathbf{y}^o-\mathbf{H}.\mathbf{x})$$

It is similar to a [Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar), without its background
part. The background, required in the interface, is only used as an initial
point for the variational minimization.

This mono-objective optimization algorithm is naturally written for a single
estimate, without any dynamic or iterative notion (there is no need in this
case for an incremental evolution operator, nor for an evolution error
covariance). In ADAO, it can also be used on a succession of observations,
placing the estimate in a recursive framework partly similar to a Kalman
Filter. A standard estimate is made at each observation step on the state
predicted by the incremental evolution model.

In all cases, it is recommended to prefer a [Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar)
for its stability as for its behavior during optimization.

## 13.12.2. Some noteworthy properties of the implemented methods

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

## 13.12.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

Background
:   *Vector*. The variable indicates the background or initial vector used,
    previously noted as $\mathbf{x}^b$. Its value is defined as a
    “*Vector*” or “*VectorSerie*” type object. Its availability in output is
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
    “Parameters”.

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
    “CurrentStepNumber”,
    “EnsembleOfSimulations”,
    “EnsembleOfStates”,
    “ForecastState”,
    “IndexOfOptimum”,
    “Innovation”,
    “InnovationAtCurrentAnalysis”,
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

*Tips for this algorithm:*

> As the *“BackgroundError”* command is required for ALL the calculation
> algorithms in the graphical interface ADAO EFICAS, you have to provide a
> value, even if this command is not required for this algorithm, and will
> not be used. The simplest way is to give “1” as a STRING.

## 13.12.4. Information and variables available at the end of the algorithm

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

## 13.12.5. Python (TUI) use examples

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
perfect.

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
print("Resolution of the calibration problem")
print("-------------------------------------")
print("")
from adao import adaoBuilder
case = adaoBuilder.New()
case.setBackground( Vector = Xb, Stored=True )
case.setObservation( Vector = Yobs, Stored=True )
case.setObservationError( ScalarSparseMatrix = 1. )
case.setObservationOperator( OneFunction = QuadFunction )
case.setAlgorithmParameters(
    Algorithm="NonLinearLeastSquares",
    Parameters={
        "MaximumNumberOfIterations": 100,
        "StoreSupplementaryCalculations": [
            "CurrentState",
            ],
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
print("Number of simulations..............:", len(case.get("CurrentState"))*4)
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
plt.savefig("simple_NonLinearLeastSquares.png")
```

The execution result is the following:

```none
Resolution of the calibration problem
-------------------------------------

  Intermediate state at the current iteration: [1. 1. 1.]
  Intermediate state at the current iteration: [1.99739508 1.07086406 1.01346638]
  Intermediate state at the current iteration: [1.83891966 1.04815981 1.01208385]
  Intermediate state at the current iteration: [1.8390702  1.03667176 1.01284797]
  Intermediate state at the current iteration: [1.83967236 0.99071957 1.01590445]
  Intermediate state at the current iteration: [1.84208099 0.8069108  1.02813037]
  Intermediate state at the current iteration: [ 1.93711599 -0.56383147  1.12097995]
  Intermediate state at the current iteration: [ 1.99838848 -1.00480576  1.1563713 ]
  Intermediate state at the current iteration: [ 2.0135905  -1.04815936  1.16155285]
  Intermediate state at the current iteration: [ 2.01385679 -1.03874812  1.16129658]
  Intermediate state at the current iteration: [ 2.01377856 -1.03700048  1.16157611]
  Intermediate state at the current iteration: [ 2.01338903 -1.02943739  1.16528951]
  Intermediate state at the current iteration: [ 2.01265633 -1.01708474  1.17793974]
  Intermediate state at the current iteration: [ 2.01124871 -0.99745512  1.21485092]
  Intermediate state at the current iteration: [ 2.00863696 -0.96943287  1.30917045]
  Intermediate state at the current iteration: [ 2.00453385 -0.94011718  1.51021885]
  Intermediate state at the current iteration: [ 2.00013539 -0.93313894  1.80539445]
  Intermediate state at the current iteration: [ 1.95437219 -0.76890307  2.04566901]
  Intermediate state at the current iteration: [ 1.99797363 -0.92538077  1.81674454]
  Intermediate state at the current iteration: [ 1.99760514 -0.9592967   2.01402117]
  Intermediate state at the current iteration: [ 1.99917565 -0.99152673  2.03171823]
  Intermediate state at the current iteration: [ 1.99990376 -0.99963125  2.00671607]
  Intermediate state at the current iteration: [ 1.99999841 -1.00005288  2.00039727]
  Intermediate state at the current iteration: [ 2.00000014 -1.00000309  2.00000249]
  Intermediate state at the current iteration: [ 2.         -0.99999995  2.00000015]

Calibration of 3 coefficients in a 1D quadratic function on 5 measures
----------------------------------------------------------------------

Observation vector.................: [ 57.   2.   3.  17. 192.]
A priori background state..........: [1. 1. 1.]

Expected theoretical coefficients..: [ 2 -1  2]

Number of iterations...............: 25
Number of simulations..............: 100
Calibration resulting coefficients.: [ 2.         -0.99999995  2.00000015]
```

The figures illustrating the result of its execution are as follows:

[![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/simple_NonLinearLeastSquares.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/simple_NonLinearLeastSquares.png)

## 13.12.6. See also

References to other sections:

- [Calculation algorithm “LinearLeastSquares”](ref_algorithm_LinearLeastSquares.md#section-ref-algorithm-linearleastsquares)
- [Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar)
- [Checking algorithm “LinearityTest”](ref_algorithm_LinearityTest.md#section-ref-algorithm-linearitytest)

Bibliographical references:

- [[Byrd95]](bibliography.md#byrd95)
- [[Morales11]](bibliography.md#morales11)
- [[Zhu97]](bibliography.md#zhu97)
