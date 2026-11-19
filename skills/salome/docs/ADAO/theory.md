<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/theory.html -->

# 2. **[DocT]** A brief introduction to Data Assimilation and Optimization

**Data Assimilation** is a general well established framework for computing the
optimal estimate of the true state of a system, over time if necessary. It uses
values obtained by combining both observations and *a priori* models, including
information about their errors while simultaneously respecting constraints.
This takes into account the laws of behavior or motion of the system through
the equations of the model, and the way the measurements are physically related
to the variables of the system.

In other words, data assimilation merges measurement data of a system, that are
the observations, with *a priori* system physical and mathematical knowledge,
embedded in numerical models. The goal is to obtain the best possible estimate,
called “*analysis*”, of the system real state and of its stochastic properties.
Note that this real state (or “*true state*”) cannot usually be reached, but
can only be estimated. Moreover, despite the fact that the used information are
stochastic by nature, data assimilation provides deterministic techniques in
order to perform very efficiently the estimation.

Because data assimilation looks for the **best possible** estimate, its
underlying procedure always integrates optimization in order to find this
estimate: particular optimization methods are always embedded in data
assimilation algorithms. Optimization methods can be seen in ADAO as a way to
extend data assimilation applications. They will be introduced this way in the
section [Going further in the state estimation by optimization methods](#section-theory-optimization), but they are far more general and
can be used without data assimilation concepts.

Two main types of applications exist in data assimilation, which are covered by
the same formalism: **fields reconstruction** (see [Fields reconstruction or
measures interpolation](#fields-reconstruction-or-measures-interpolation)) and **parameters identification** (see [Parameters
identification, models adjustment, or calibration](#parameters-identification-models-adjustment-or-calibration)). These are also referred
to as **state estimation** and **parameters estimation** respectively, and one
can if necessary elaborate joint estimation of both (see [Joint state and
parameter estimation in dynamics](#joint-state-and-parameter-estimation-in-dynamics)). In ADAO, some algorithms can be used
either in state estimation or in parameter estimation. This is done simply by
changing the required option “*EstimationOf*” in the algorithm parameters.
Before introducing the [Simple description of the data assimilation methodological framework](#section-theory-da-framework) in a next section,
these two types of applications are briefly described. At the end, some
detailed information allow [Going further in the data assimilation framework](#section-theory-more-assimilation) and
[Going further in the state estimation by optimization methods](#section-theory-optimization), as well as [Going further in data assimilation for dynamics](#section-theory-dynamic)
and having [An overview of reduction methods and of reduced optimization](#section-theory-reduction).

## 2.1. Fields reconstruction or measures interpolation

**Fields reconstruction (or interpolation)** consists in finding, from a
restricted set of real measures, the physical field which is the most
*consistent* with these measures.

This *consistency* is to understand in terms of interpolation, that is to say
that the field we want to reconstruct, using data assimilation on measures, has
to fit at best the measures, while remaining constrained by the overall field
calculation. The calculation is thus an *a priori* estimation of the field that
we seek to identify. One also speaks of **state estimation** in this case.

If the system evolves over time, the reconstruction of the whole field has to
be established at each time step, taking into account the information over a
time window. The interpolation process is more complicated in this case because
it is temporal, and not only in terms of instantaneous field values.

A simple example of fields reconstruction comes from meteorology, in which one
look for value of variables such as temperature or pressure in all points of the
spatial domain. One have instantaneous measurements of these quantities at
certain points, but also a history set of these measures. Moreover, these
variables are constrained by evolution equations for the state of the
atmosphere, which indicates for example that the pressure at a point can not
take any value independently of the value at this same point in previous time.
One must therefore make the reconstruction of a field at any point in space, in
a “consistent” manner with the evolution equations and with the measures of the
previous time steps.

## 2.2. Parameters identification, models adjustment, or calibration

The **identification (or adjustment) of parameters** by data assimilation is a
form of state calibration which uses both the physical measurement and an *a
priori* parameters estimation (called the “*background*”) of the state that one
seeks to identify, as well as a characterization of their errors. From this
point of view, it uses all available information on the physical system, with
restrictive yet realistic assumptions about errors, to find the “*optimal
estimation*” from the true state. We note, in terms of optimization, that the
background realizes a “*regularization*”, in the mathematical meaning of
Tikhonov [[[Tikhonov77]](bibliography.md#tikhonov77) [[WikipediaTI]](bibliography.md#wikipediati), of the main problem of parameters
identification. One can also use the term “*inverse problem*” to refer to this
process.

In practice, the two observed gaps “*calculation-measures*” and
“*calculation-background*” are combined to build the calibration correction of
parameters or initial conditions. The addition of these two gaps requires a
relative weight, which is chosen to reflect the trust we give to each piece of
information. This confidence is depicted by the covariance of the errors on the
background and on the observations. Thus the stochastic aspect of information is
essential for building the calibration error function.

A simple example of parameters identification comes from any kind of physical
simulation process involving a parametrized model. For example, a static
mechanical simulation of a beam constrained by some forces is described by beam
parameters, such as a Young coefficient, or by the intensity of the force. The
parameters estimation problem consists in finding for example the right Young
coefficient value in order that the simulation of the beam corresponds to
measurements, including the knowledge of errors.

All quantities representing the description of physics in a model are likely to
be calibrated in a data assimilation process, whether they are model
parameters, initial conditions or boundary conditions. Their simultaneous
consideration is greatly facilitated by the data assimilation framework, which
makes it possible to objectively process a heterogeneous set of available
information.

## 2.3. Joint estimation of states and parameters

It is sometimes necessary, when considering the two previous types of
applications, to need to simultaneously estimate states (fields) and parameters
characterizing a physical phenomenon. This is known as **joint estimation of
states and parameters**.

Without going into the advanced methods to solve this problem, we can mention
the conceptually very simple approach of considering the vector of states to be
interpolated as *augmented* by the vector of parameters to be calibrated. It
can be noted that we are in *state estimation* or *reconstruction of fields*,
and that in the temporal case of parameters identification, the evolution of
the parameters to estimate is simply the identity. The assimilation or
optimization algorithms can then be applied to the augmented vector. Valid for
moderate nonlinearities in the simulation, this simple method extends the
optimization space, and thus leads to larger problems, but it is often possible
to reduce the representation to numerically computable cases. Without
exhaustiveness, the separated variables optimization, the reduced rank
filtering, or the specific treatment of covariance matrices, are common
techniques to avoid this dimension problem. In the temporal case, we will see
below indications for a [Joint state and parameter estimation in dynamics](#joint-state-and-parameter-estimation-in-dynamics).

To go further, we refer to the mathematical methods of optimization and
augmentation developed in many books or specialized articles, finding their
origin for example in [[Lions68]](bibliography.md#lions68), [[Jazwinski70]](bibliography.md#jazwinski70) or [[Dautray85]](bibliography.md#dautray85). In particular
in the case of more marked nonlinearities during the numerical simulation of
the states, it is advisable to treat in a more complete but also more complex
way the problem of joint estimation of states and parameters.

## 2.4. Simple description of the data assimilation methodological framework

We can write these features in a simple manner. By default, all variables are
vectors, as there are several parameters to readjust, or a discrete field to
reconstruct.

According to standard notations in data assimilation, we note
$\mathbf{x}^a$ the optimal parameters that is to be determined by
calibration, $\mathbf{y}^o$ the observations (or experimental
measurements) that we must compare to the simulation outputs,
$\mathbf{x}^b$ the background (*a priori* values, or regularization
values) of searched parameters, $\mathbf{x}^t$ the unknown ideals
parameters that would give exactly the observations (assuming that the errors
are zero and the model is exact) as output.

In the simplest case, which is static, the steps of simulation and of
observation can be combined into a single observation operator noted
$\mathcal{H}$ (linear or nonlinear). It transforms the input parameters
$\mathbf{x}$ to results $\mathbf{y}$, to be directly compared to
observations $\mathbf{y}^o$:

$$\mathbf{y} = \mathcal{H}(\mathbf{x})$$

Moreover, we use the linearized operator $\mathbf{H}$ to represent the
effect of the full operator $\mathcal{H}$ around a linearization point
(and we will usually omit thereafter to mention $\mathcal{H}$, even if it
is possible to keep it, to mention only $\mathbf{H}$). In reality, we
have already indicated that the stochastic nature of variables is essential,
coming from the fact that model, background and observations are all incorrect.
We therefore introduce errors of observations additively, in the form of a
random vector $\mathbf{\epsilon}^o$ such that:

$$\mathbf{y}^o = \mathbf{H} \mathbf{x}^t + \mathbf{\epsilon}^o$$

The errors represented here are not only those from observation, but also from
the simulation. We can always consider that these errors are of zero mean.
Noting $E[.]$ the classical mathematical expectation, we can then define a
matrix $\mathbf{R}$ of the observation error covariances by the
expression:

$$\mathbf{R} = E[\mathbf{\epsilon}^o.{\mathbf{\epsilon}^o}^T]$$

The background can be written formally as a function of the true value, by
introducing the errors vector $\mathbf{\epsilon}^b$ such that:

$$\mathbf{x}^b = \mathbf{x}^t + \mathbf{\epsilon}^b$$

The background errors $\mathbf{\epsilon}^b$ are also assumed of zero
mean, in the same manner as for observations. We define the $\mathbf{B}$
matrix of background error covariances by:

$$\mathbf{B} = E[\mathbf{\epsilon}^b.{\mathbf{\epsilon}^b}^T]$$

The optimal estimation of the true parameters $\mathbf{x}^t$, given the
background $\mathbf{x}^b$ and the observations $\mathbf{y}^o$, is
then called an “*analysis*”, noted as $\mathbf{x}^a$, and comes from the
minimisation of an error function, explicit in variational assimilation, or
from the filtering correction in assimilation by filtering.

In **variational assimilation**, in a static case, one classically attempts to
minimize the following function $J$:

$$J(\mathbf{x})=\frac{1}{2}(\mathbf{x}-\mathbf{x}^b)^T.\mathbf{B}^{-1}.(\mathbf{x}-\mathbf{x}^b)+\frac{1}{2}(\mathbf{y}^o-\mathbf{H}.\mathbf{x})^T.\mathbf{R}^{-1}.(\mathbf{y}^o-\mathbf{H}.\mathbf{x})$$

$J$ is classically designed as the “*3D-Var*” functional in data
assimilation (see for example [[Talagrand97]](bibliography.md#talagrand97)) or as the generalized Tikhonov
regularization functional in optimization (see for example [[WikipediaTI]](bibliography.md#wikipediati)).
Since $\mathbf{B}$ and $\mathbf{R}$ covariance matrices are
proportional to the variances of errors, their presence in both terms of the
function $J$ can effectively weight the gap terms by the confidence in
the background or observations errors. The parameters vector $\mathbf{x}$
realizing the minimum of this function therefore constitute the analysis
$\mathbf{x}^a$. It is at this level that we have to use the full panoply
of function minimization methods otherwise known in optimization (see also
section [Going further in the state estimation by optimization methods](#section-theory-optimization)). Depending on the size of the
parameters vector $\mathbf{x}$ to identify, and of the availability of
gradient or Hessian of $J$, it is appropriate to adapt the chosen
optimization method (gradient, Newton, quasi-Newton…).

In **assimilation by filtering**, in this simple case usually referred to as
“*BLUE*” (for “*Best Linear Unbiased Estimator*”), the $\mathbf{x}^a$
analysis is given as a correction of the background $\mathbf{x}^b$ by a
term proportional to the difference between observations $\mathbf{y}^o$
and calculations $\mathbf{H}\mathbf{x}^b$:

$$\mathbf{x}^a = \mathbf{x}^b + \mathbf{K}(\mathbf{y}^o - \mathbf{H}\mathbf{x}^b)$$

where $\mathbf{K}$ is the Kalman gain matrix, which is expressed using
covariance matrices in the following form:

$$\mathbf{K} = \mathbf{B}\mathbf{H}^T(\mathbf{H}\mathbf{B}\mathbf{H}^T+\mathbf{R})^{-1}$$

The advantage of filtering is to explicitly calculate the gain, to produce then
the *a posteriori* covariance analysis matrix.

In this simple static case, we can show, under an assumption of Gaussian error
distributions (very little restrictive in practice) and of $\mathcal{H}$
linearity, that the two *variational* and *filtering* approaches give the same
solution.

It is indicated here that these methods of “*3D-Var*” and “*BLUE*” may be
extended to dynamic or time-related problems, called respectively “*4D-Var*”
and “*Kalman Filter (KF)*” and their derivatives. They have to take into
account an evolution operator to establish an analysis at the right time steps
of the gap between observations and simulations, and to have, at every moment,
the propagation of the background through the evolution model. The next section
provides information on [Going further in data assimilation for dynamics](#section-theory-dynamic). In
the same way, these methods can be used in case of non linear observation or
evolution operators. Many other variants have been developed to improve the
numerical quality of the methods or to take into account computer requirements
such as calculation size and time.

## 2.5. A schematic view of Data Assimilation and Optimization approaches

To help the reader get an idea of the approaches that can be used with ADAO in
Data Assimilation and Optimization, we propose here a simplified scheme
describing an arbitrary classification of methods. It is partially and freely
inspired by [[Asch16]](bibliography.md#asch16) (Figure 1.5).

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/meth_ad_and_opt.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/meth_ad_and_opt.png)
>
> ****A simplified classification of methods that can be used with ADAO in Data Assimilation and Optimization (acronyms and internal descriptive links are listed below)****

It is deliberately simple to remain readable, the dashed lines showing some of
the simplifications or extensions. For example, it does not specifically
mention the methods with reductions (of which it is given hereafter
[An overview of reduction methods and of reduced optimization](#section-theory-reduction)), some of which were variations of the basic
methods shown here, nor does it mention the more detailed extensions. It also
omits the test methods available in ADAO and useful for the study.

Each method mentioned in this diagram is the subject of a specific descriptive
section in the chapter on [[DocR] Data assimilation or optimization calculation cases](reference.md#section-reference-assimilation). The acronyms
mentioned in the diagram have the meaning indicated in the associated internal
links:

- 3D-Var: [Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar),
- 4D-Var: [Calculation algorithm “4DVAR”](ref_algorithm_4DVAR.md#section-ref-algorithm-4dvar),
- Blue: [Calculation algorithm “Blue”](ref_algorithm_Blue.md#section-ref-algorithm-blue),
- DiffEvol : [Calculation algorithm “DifferentialEvolution”](ref_algorithm_DifferentialEvolution.md#section-ref-algorithm-differentialevolution),
- EKF: [Calculation algorithm “ExtendedKalmanFilter”](ref_algorithm_ExtendedKalmanFilter.md#section-ref-algorithm-extendedkalmanfilter),
- EnKF: [Calculation algorithm “EnsembleKalmanFilter”](ref_algorithm_EnsembleKalmanFilter.md#section-ref-algorithm-ensemblekalmanfilter),
- DFO: [Calculation algorithm “DerivativeFreeOptimization”](ref_algorithm_DerivativeFreeOptimization.md#section-ref-algorithm-derivativefreeoptimization),
- Incr-Var: Incremental version Variational optimization,
- KF: [Calculation algorithm “KalmanFilter”](ref_algorithm_KalmanFilter.md#section-ref-algorithm-kalmanfilter),
- LLS: [Calculation algorithm “LinearLeastSquares”](ref_algorithm_LinearLeastSquares.md#section-ref-algorithm-linearleastsquares),
- NLLS: [Calculation algorithm “NonLinearLeastSquares”](ref_algorithm_NonLinearLeastSquares.md#section-ref-algorithm-nonlinearleastsquares),
- QR: [Calculation algorithm “QuantileRegression”](ref_algorithm_QuantileRegression.md#section-ref-algorithm-quantileregression),
- Swarm: [Calculation algorithm “ParticleSwarmOptimization”](ref_algorithm_ParticleSwarmOptimization.md#section-ref-algorithm-particleswarmoptimization),
- Tabu: [Calculation algorithm “TabuSearch”](ref_algorithm_TabuSearch.md#section-ref-algorithm-tabusearch),
- UKF: [Calculation algorithm “UnscentedKalmanFilter”](ref_algorithm_UnscentedKalmanFilter.md#section-ref-algorithm-unscentedkalmanfilter).

## 2.6. An overview of reduction methods and of reduced optimization

Data assimilation and optimization approaches always imply a certain amount of
reiteration of a unitary numerical simulation representing the physics that is
to be treated. In order to handle this physics as well as possible, this
elementary numerical simulation is often of large size, even huge, and leads to
an extremely high computational cost when it is repeated. The complete physical
simulation is often called “*high fidelity simulation*” (or “*full scale
simulation*”).

To avoid this practical challenge, **different strategies to reduce the cost of
the optimization calculation exist, and some of them also allow to control the
numerical error implied by this reduction**. These strategies are seamlessly
integrated into some of the ADAO methods or are the purpose of special
algorithms.

To establish such an approach, one seeks to reduce at least one of the
ingredients that make up the data assimilation or optimization problem. One can
thus classify the reduction methods according to the ingredient on which they
operate, knowing that some methods deal with several of them. A rough
classification is provided here, which the reader can complete by reading
general mathematical books or articles, or those specialized in his physics.

Reduction of data assimilation or optimization algorithms:
:   the optimization algorithms themselves can generate significant
    computational costs to process numerical information. Various methods can
    be used to reduce their algorithmic cost, for example by working in the
    most suitable reduced space for optimization, or by using multi-level
    optimization techniques. ADAO has such techniques that are included in
    variants of classical algorithms, leading to exact or approximate but
    numerically more efficient resolutions. By default, the algorithmic options
    chosen in ADAO are always the most efficient when they do not impact the
    quality of the optimization.

Reduction of the representation of covariances:
:   in data assimilation algorithms, covariances are the most expensive
    quantities to handle or to store, often becoming the limiting quantities
    from the point of view of the computational cost. Many methods try to use a
    reduced representation of these matrices (leading sometimes but not
    necessarily to reduce the dimension of the optimization space).
    Classically, factorization, decomposition (spectral, Fourier, wavelets…)
    or ensemble estimation (EOF…) techniques, or combinations, are used to
    reduce the numerical load of these covariances in the computations. ADAO
    uses some of these techniques, in combination with sparse computation
    techniques, to make the handling of covariance matrices more efficient.

Reduction of the physical model:
:   the simplest way to reduce the cost of the unit calculation consists in
    reducing the simulation model itself, by representing it in a more economic
    way. Numerous methods allow this reduction of models by ensuring a more or
    less rigorous control of the approximation error generated by the
    reduction. The use of simplified models of the physics allows a reduction
    but without always producing an error control. On the contrary, all
    decomposition methods (Fourier, wavelets, SVD, POD, PCA, Kahrunen-Loeve,
    RBM, EIM, etc.) aim at a reduction of the representation space with an
    explicit error control. Although they are very frequently used, they must
    nevertheless be completed by a fine analysis of the interaction with the
    optimization algorithm in which the reduced computation is inserted, in
    order to avoid instabilities, discrepancies or inconsistencies that are
    notoriously harmful. ADAO fully supports the use of this type of reduction
    method, even if it is often necessary to establish this generic independent
    reduction prior to the optimization.

Reduction of the data assimilation or optimization space:
:   the size of the optimization space depends greatly on the type of problem
    treated (estimation of states or parameters) but also on the number of
    observations available to conduct the data assimilation. It is therefore
    sometimes possible to conduct the optimization in the smallest space by
    adapting the internal formulation of the optimization algorithms. When it
    is possible and judicious, ADAO integrates this kind of reduced formulation
    to improve the numerical performance without reducing the quality of the
    optimization.

Combining multiple reductions:
:   many advanced algorithms seek to combine multiple reduction techniques
    simultaneously. However, it is difficult to have both generic and robust
    methods, and to use several very efficient reduction techniques at the same
    time. ADAO integrates some of the most robust methods, but this aspect is
    still largely the subject of research and development.

One can end this quick overview of reduction methods highlighting that their
use is ubiquitous in real applications and in numerical tools, and that ADAO
allows to use proven methods without even knowing it.

## 2.7. Going further in the data assimilation framework

To get more information about the data assimilation techniques, the reader can
consult introductory documents like [[Talagrand97]](bibliography.md#talagrand97) or [[Argaud09]](bibliography.md#argaud09), on-line
training courses or lectures like [[Bouttier99]](bibliography.md#bouttier99) and [[Bocquet04]](bibliography.md#bocquet04) (along with
other materials coming from geosciences applications), or general documents
like [[Talagrand97]](bibliography.md#talagrand97), [[Tarantola87]](bibliography.md#tarantola87), [[Asch16]](bibliography.md#asch16), [[Kalnay03]](bibliography.md#kalnay03), [[Ide97]](bibliography.md#ide97),
[[Tikhonov77]](bibliography.md#tikhonov77) and [[WikipediaDA]](bibliography.md#wikipediada). In a more mathematical way, one can also
consult [[Lions68]](bibliography.md#lions68), [[Jazwinski70]](bibliography.md#jazwinski70).

Note that data assimilation is not restricted to meteorology or geo-sciences,
but is widely used in other scientific domains. There are several fields in
science and technology where the effective use of observed but incomplete data
is crucial.

Some aspects of data assimilation are also known by other names. Without being
exhaustive, we can mention the names of *calibration*, *adjustment*, *state
estimation*, *parameter estimation*, *parameter adjustment*, *inverse problems*
or *inversion*, *Bayesian estimation*, *field interpolation* or *optimal
interpolation*, *variational optimization*, *quadratic optimization*,
*mathematical regularization*, *meta-heuristics for optimization*, *model
reduction*, *data smoothing*, *data-driven* modeling, model and data learning
(*Machine Learning* and *Artificial Intelligence*), etc. These terms can be
used in bibliographic searches.

## 2.8. Going further in the state estimation by optimization methods

As seen before, in a static simulation case, the variational data assimilation
requires to minimize the goal function $J$:

$$J(\mathbf{x})=\frac{1}{2}(\mathbf{x}-\mathbf{x}^b)^T.\mathbf{B}^{-1}.(\mathbf{x}-\mathbf{x}^b)+\frac{1}{2}(\mathbf{y}^o-\mathbf{H}.\mathbf{x})^T.\mathbf{R}^{-1}.(\mathbf{y}^o-\mathbf{H}.\mathbf{x})$$

which is named the “*3D-Var*” objective function. It can be seen as a *least
squares minimization* extended form, obtained by adding a regularizing term
using $\mathbf{x}-\mathbf{x}^b$, and by weighting the differences using
$\mathbf{B}$ and $\mathbf{R}$ the two covariance matrices. The
minimization of the $J$ function leads to the *best* $\mathbf{x}$
state estimation. To get more information about these notions, one can consult
reference general documents like [[Tarantola87]](bibliography.md#tarantola87).

State estimation possibilities extension, by using more explicitly optimization
methods and their properties, can be imagined in two ways.

First, classical optimization methods often involves using various
gradient-based minimizing procedures. They are extremely efficient to look for
a single local minimum. But they require the goal function $J$ to be
sufficiently regular and differentiable, and are not able to capture global
properties of the minimization problem, for example: global minimum, set of
equivalent solutions due to over-parametrization, multiple local minima, etc.
**An approach to extend estimation possibilities is then to use a whole range of
optimizers, allowing global minimization, various robust search properties,
etc**. There is a lot of minimizing methods, such as stochastic ones,
evolutionary ones, heuristics and meta-heuristics for real-valued problems,
etc. They can treat partially irregular or noisy function $J$, can
characterize local minima, etc. The main drawbacks are a greater numerical cost
to find state estimates, and often a lack of guarantee of convergence in finite
time. Here, we only point the following topics, as the methods are available in
ADAO:

- *Derivative Free Optimization (or DFO)* (see [Calculation algorithm “DerivativeFreeOptimization”](ref_algorithm_DerivativeFreeOptimization.md#section-ref-algorithm-derivativefreeoptimization)),
- *Particle Swarm Optimization (or PSO)* (see [Calculation algorithm “ParticleSwarmOptimization”](ref_algorithm_ParticleSwarmOptimization.md#section-ref-algorithm-particleswarmoptimization)),
- *Differential Evolution (or DE)* (see [Calculation algorithm “DifferentialEvolution”](ref_algorithm_DifferentialEvolution.md#section-ref-algorithm-differentialevolution)),
- *Quantile Regression (or QR)* (see [Calculation algorithm “QuantileRegression”](ref_algorithm_QuantileRegression.md#section-ref-algorithm-quantileregression)).

Secondly, optimization methods try usually to minimize quadratic measures of
errors, as the natural properties of such goal functions are well suited for
classical gradient optimization. But other measures of errors can be more
adapted to real physical simulation problems. Then, **an another way to extend
estimation possibilities is to use other measures of errors to be reduced**.
For example, we can cite *absolute error value*, *maximum error value*, etc.
The most classical instances of error measurements are recalled or specified
below, indicating their identifiers in ADAO for the possible selection of a
quality criterion:

- the objective function for the augmented weighted least squares error measurement (which is the basic default functional in all data assimilation algorithms, often named “*3D-Var*” objective function, and which is known in the quality criteria for ADAO as “*AugmentedWeightedLeastSquares*”, “*AWLS*” or “*DA*”) is:

  > $$J(\mathbf{x})=\frac{1}{2}(\mathbf{x}-\mathbf{x}^b)^T.\mathbf{B}^{-1}.(\mathbf{x}-\mathbf{x}^b)+\frac{1}{2}(\mathbf{y}^o-\mathbf{H}.\mathbf{x})^T.\mathbf{R}^{-1}.(\mathbf{y}^o-\mathbf{H}.\mathbf{x})$$
- the objective function for the weighted least squares error measurement (which is the squared $L^2$ weighted norm of the innovation, with a $1/2$ coefficient to be homogeneous with the previous one, and which is known in the quality criteria for ADAO as “*WeightedLeastSquares*” or “*WLS*”) is:

  > $$J(\mathbf{x})=\frac{1}{2}(\mathbf{y}^o-\mathbf{H}.\mathbf{x})^T.\mathbf{R}^{-1}.(\mathbf{y}^o-\mathbf{H}.\mathbf{x})$$
- the objective function for the least squares error measurement (which is the squared $L^2$ norm of the innovation, with a $1/2$ coefficient to be homogeneous with the previous ones, and which is known in the quality criteria for ADAO as “*LeastSquares*”, “*LS*” or “*L2*”) is:

  > $$J(\mathbf{x})=\frac{1}{2}(\mathbf{y}^o-\mathbf{H}.\mathbf{x})^T.(\mathbf{y}^o-\mathbf{H}.\mathbf{x})=\frac{1}{2}||\mathbf{y}^o-\mathbf{H}.\mathbf{x}||_{L^2}^2$$
- the objective function for the absolute error value measurement (which is the $L^1$ norm of the innovation, and which is known in the quality criteria for ADAO as “*AbsoluteValue*” or “*L1*”) is:

  > $$J(\mathbf{x})=||\mathbf{y}^o-\mathbf{H}.\mathbf{x}||_{L^1}$$
- the objective function for the maximum error value measurement (which is the $L^{\infty}$ norm, and which is known in the quality criteria for ADAO as “*MaximumError*”, “*ME*” or “*Linf*”) is:

  > $$J(\mathbf{x})=||\mathbf{y}^o-\mathbf{H}.\mathbf{x}||_{L^{\infty}}$$

These error measures may be not differentiable for the last two, but some
optimization methods can still handle them: heuristics and meta-heuristics for
real-valued problem, etc. As previously, the main drawback remain a greater
numerical cost to find state estimates, and often a lack of guarantee of
convergence in finite time. Here again, we only point the following methods as
it is available in the ADAO module:

- *Derivative Free Optimization (or DFO)* (see [Calculation algorithm “DerivativeFreeOptimization”](ref_algorithm_DerivativeFreeOptimization.md#section-ref-algorithm-derivativefreeoptimization)),
- *Particle Swarm Optimization (or PSO)* (see [Calculation algorithm “ParticleSwarmOptimization”](ref_algorithm_ParticleSwarmOptimization.md#section-ref-algorithm-particleswarmoptimization)),
- *Differential Evolution (or DE)* (see [Calculation algorithm “DifferentialEvolution”](ref_algorithm_DifferentialEvolution.md#section-ref-algorithm-differentialevolution)).

The reader interested in the subject of optimization can look at [[WikipediaMO]](bibliography.md#wikipediamo)
as a general entry point.

## 2.9. Going further in data assimilation for dynamics

We can analyze a system in temporal evolution (dynamics) with the help of data
assimilation, in order to explicitly take into account the flow of time in the
estimation of states or parameters. We briefly introduce here the problematic,
and some theoretical or practical tools, to facilitate the user treatment of
such situations. It is nevertheless indicated that the variety of physical and
user problems is large, and that it is therefore recommended to adapt the
treatment to the constraints, whether they are physical, numerical or
computational.

### 2.9.1. General form of dynamic systems

Systems in temporal evolution can be studied or represented using dynamic
systems. In this case, it is easy to conceive the analysis of their behavior
with the help of data assimilation (it is even in this precise case that the
data assimilation approach was initially widely developed).

We formalize the numerical simulation framework in a simple way. A simple
dynamic system dynamic system on the state $\mathbf{x}$ can be described
in continuous time in the form:

$$\forall t \in \mathbb{R}^{+}, \frac{d\mathbf{x}}{dt} = \mathcal{D}(\mathbf{x},\mathbf{u},t)$$

where $\mathbf{x}$ is the unknown state vector, $\mathbf{u}$ is a
known external control vector, and $\mathcal{D}$ is the (possibly
non-linear) operator of the system dynamics. It is an Ordinary Differential
Equation (ODE), of the first order, on the state. In discrete time, this
dynamical system can be written in the following form:

$$\forall n \in \mathbb{N}, \mathbf{x}_{n+1} = M(\mathbf{x}_{n},\mathbf{u}_{n},t_n\rightarrow t_{n+1})$$

for an indexing $t_n$ of discrete times with $n\in\mathbf{N}$.
$M$ is the discrete evolution operator, symbolically obtained from
$\mathcal{D}$ by the discretization scheme. Usually, we omit the time
notation in the evolution operator $M$. Approximating the
$\mathcal{D}$ operator by $M$ introduces (or adds, if it already
exists) a $\epsilon$ model error.

We can then characterize two types of estimates in dynamics, which we describe
hereafter on the discrete time dynamical system: [State estimation in
dynamics](#state-estimation-in-dynamics) and [Parameter estimation in dynamics](#parameter-estimation-in-dynamics). Combined, the two types can
be used to make a [Joint state and parameter estimation in dynamics](#joint-state-and-parameter-estimation-in-dynamics). In ADAO,
many algorithms can be used either in state estimation or in parameter
estimation. This is done simply by changing the required option
“*EstimationOf*” in the algorithm parameters, which only changes the way the
$\mathbf{u}$ control is applied in cases where it is explicitly not
included in $M$.

### 2.9.2. State estimation in dynamics

The state estimation can be conducted by data assimilation on the discrete time
version of the dynamical system, written in the following form:

$$\mathbf{x}_{n+1} = M(\mathbf{x}_{n},\mathbf{u}_{n}) + \mathbf{\epsilon}_{n}$$

$$\mathbf{y}_{n} = H(\mathbf{x}_{n}) + \mathbf{\nu}_{n}$$

where $\mathbf{x}$ is the system state to be estimated,
$\mathbf{x}_{n}$ and $\mathbf{y}_{n}$ are respectively the
computed (unobserved) and measured (observed) state of the system, $M$
and $H$ are the incremental evolution and observation operators,
respectively, $\mathbf{\epsilon}_{n}$ and $\mathbf{\nu}_{n}$ are
the evolution and observation noise or error, respectively, and
$\mathbf{u}_{n}$ is a known external control. The two operators $M$
and $H$ are directly usable in data assimilation with ADAO.

### 2.9.3. Parameter estimation in dynamics

The parameter estimation can be written in a slightly differently way to be
solved by data assimilation. The parameters are denoted $\mathbf{a}$.
Still on the discrete time version of the dynamical system, we look for a
nonlinear $G$ mapping, parameterized by $\mathbf{a}$, between
inputs $\mathbf{x}_{n}$ and measurements $\mathbf{y}_{n}$ at each
step $t_n$, the error to be controlled as a function of parameters
$\mathbf{y}_{n}$ being
$\mathbf{y}_{n}-G(\mathbf{x}_{n},\mathbf{a})$. We can proceed by
optimization on this error, with regularization, or by filtering by writing the
problem represented in state estimation:

$$\mathbf{a}_{n+1} = \mathbf{a}_{n} + \mathbf{\epsilon}_{n}$$

$$\mathbf{y}_{n} = G(\mathbf{x}_{n},\mathbf{a}_{n}) + \mathbf{\nu}_{n}$$

where, this time, the choice of the evolution and observation error models
$\mathbf{\epsilon}_{n}$ and $\mathbf{\nu}_{n}$ condition the
performance of convergence and observation tracking (while the error
representations come from the behavior of the physics in the case of state
estimation). The estimation of the parameters $\mathbf{a}$ is done by
using pairs $(\mathbf{x}_{n},\mathbf{y}_{n})$ of corresponding inputs and
outputs. Moreover, the error functionals are based on the difference between
the input estimate and the output estimate.

In this case of parameter estimation, in order to apply data assimilation
methods, we therefore impose the hypothesis that the evolution operator is the
identity (*Note: it is therefore not used, but must be declared in ADAO, for
example as a unitary diagonal matrix*), and the observation operator is
$G$.

### 2.9.4. Joint state and parameter estimation in dynamics

A special case concerns the joint estimation of state and parameters used in a
dynamic system. One seeks to jointly estimate the state $\mathbf{x}$
(which depends on time) and the parameters $\mathbf{a}$ (which here does
not depend on time). There are several ways to deal with this problem, but the
most general one is to use as below a state vector augmented by the parameters,
and to extend the operators accordingly.

To do this, using the notations of the previous two subsections, we define the
auxiliary variable $\mathbf{w}$ such that:

$$\mathbf{w} = \left[
\begin{array}{c}
\mathbf{x} \\
\mathbf{a}
\end{array}
\right]
= \left[
\begin{array}{c}
\mathbf{w}_{|x} \\
\mathbf{w}_{|a}
\end{array}
\right]$$

and the operators of evolution $\tilde{M}$ and observation
$\tilde{H}$ associated to the augmented problem:

$$\tilde{M}(\mathbf{w},\mathbf{u}) = \left[
\begin{array}{c}
M(\mathbf{w}_{|x},\mathbf{u}) \\
\mathbf{w}_{|a}
\end{array}
\right]
= \left[
\begin{array}{c}
M(\mathbf{x},\mathbf{u}) \\
\mathbf{a}
\end{array}
\right]$$

$$\tilde{H}(\mathbf{w}) = \left[
\begin{array}{c}
H(\mathbf{w}_{|x}) \\
G(\mathbf{w}_{|x},\mathbf{w}_{|a})
\end{array}
\right]
= \left[
\begin{array}{c}
H(\mathbf{x}) \\
G(\mathbf{x},\mathbf{a})
\end{array}
\right]$$

With these notations, by extending the noise variables
$\mathbf{\epsilon}$ and $\mathbf{\nu}$ appropriately, the joint
state $\mathbf{x}$ and parameters $\mathbf{a}$ discrete-time
estimation problem, using the joint variable $\mathbf{w}$, is then
written:

$$\mathbf{w}_{n+1} = \tilde{M}(\mathbf{w}_{n},\mathbf{u}_{n}) + \mathbf{\epsilon}_{n}$$

$$\mathbf{y}_{n} = \tilde{H}(\mathbf{w}_{n}) + \mathbf{\nu}_{n}$$

where $\mathbf{w}_{n}=[\mathbf{x}_n~~\mathbf{a}_n]^T$. The incremental
evolution and observation operators are therefore respectively the augmented
operators $\tilde{M}$ and $\tilde{H}$, and are directly suitable
for study cases with ADAO.

### 2.9.5. Conceptual scheme for data assimilation in dynamics

To complete the description, we can represent the data assimilation process in
a dynamics specific way using a temporal scheme, which describes the action of
the evolution ($M$ or $\tilde{M}$) and observation ($H$ or
$\tilde{H}$) operators during the discrete simulation and the recursive
estimation of the state ($\mathbf{x}$). A possible representation is as
follows, particularly appropriate for iterative Kalman filtering algorithms:

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/schema_temporel_KF.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/schema_temporel_KF.png)
>
>
> Fig. 2.1 **Timeline of steps for data assimilation operators in dynamics**

with **P** the state error covariance and *t* the discrete iterative time. In
this scheme, the analysis **(x,P)** is obtained by means of the “*correction*”
by observing the “*prediction*” of the previous state. Another way of
understanding data assimilation in dynamics, by observing the states in the
measurement space, is to represent the same sequential assimilation process as
in the previous figure in the following form:

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/schema_temporel_sequentiel.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/schema_temporel_sequentiel.png)
>
>
> Fig. 2.2 **Sequential scheme of states and measures for data assimilation in dynamics**

The concepts described in this diagram can be directly and simply used in ADAO
to understand and elaborate study cases, and are included in the description
and the examples of some algorithms.
