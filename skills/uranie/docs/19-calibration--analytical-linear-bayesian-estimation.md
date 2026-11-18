# The Calibration module — Analytical linear Bayesian estimation … CIRCE method
<!-- source PDF pages 178-196 -->

<!-- page 171 (PDF 178) -->
• TNlopt: the optimisation master used for any TNloptSolver instance. An example can be found in Macro
“calibrationMinimisationFlowrate1D.py”;
• TVizir2: the optimisation master used for any TVizirSolverShare instance. Even though the optimisation will
remain mono-criterion, this might be useful for certain complex problems, as discussed in Macro “calibrationMinimisation
Flowrate2DVizir.py”.
It is also possible to access the optimisation master by calling the getOptimMaster method. This method returns
a pointer to the newly created TOptimShare instance. This might be useful to set some properties (for instance the
tolerance).

```python
# Set the calibration object
cal = Calibration.TMinimisation(tdsPar,runner,1)
cal.setDistance("relativeLS",tdsRef,"rw:l","Qexp")
# Set Vizir optimisation properties
solv = Reoptimizer.TVizirGenetic()
solv.setSize(24,15000,100)
cal.setOptimProperties(solv)
optimMaster = cal.getOptimMaster()
optimMaster.setTolerance(1e-6)
# Set Nlopt optimisation properties
solv = Reoptimizer.TNloptSubplexe()
cal.setOptimProperties(solv)
optimMaster = cal.getOptimMaster()
optimMaster.setTolerance(1e-6)
```

###  11.3.3 Looking at the results

Finally, once the computation is complete (using the standard estimateParameters method), the calibrated values of
the parameters are directly stored in the parameter TDataServer.
It is also recommended to check the residuals (using the standard drawResiduals method, introduced in Drawing the
residuals), as they may provide useful information on the quality of the calibration.
No additional options or visualization methods are specific to the TMinimisation implementation; these functions
behave exactly as described in their respective sections.
Two examples are also provided in the use-case section (see Macro “calibrationMinimisationFlowrate1D.py” and Macro
“calibrationMinimisationFlowrate2DVizir.py”).

## 11.4 Analytical linear Bayesian estimation

This method is fairly simple from an algorithm point of view as it consists mainly of the analytical formulation of the
posterior distribution under assumptions: the problem can be considered linear and the prior distributions are normally
distributed (or non-informative/flat, as discussed in [Bla17]).
In practice, this technique is applied by following the procedure provided in Calibration classes, distance and likelihood
functions, observations and model with one important difference, however: the code or function passed through the
constructor of the TLinearBayesian object is not strictly necessary. The parameter estimate is analytical so the main
point of providing an assessor is to get both the a priori and a posteriori residuals distributions.
The usage of the TLinearBayesian class can be summarised in a few key steps:
1. Prepare the data and the model:

<!-- page 172 (PDF 179) -->
• Select the assessor type to be used and construct the TLinearBayesian object with the appropriate likelihood
function via setLikelihood method (see Constructing the TLinearBayesian object).
2. Set the algorithm properties:
• Provide the input covariance matrix, i.e., the reference observation covariance (in [Bla17], this corresponds
to Σ). This step is mandatory, as the covariance matrix is used to compute the posterior distribution, as
discussed in [Bla17];
• Specify the name of the regressors. This is also a key step as a regressor can be an input variable, but also
any function of one or several input variables. This is discussed in Defining the TLinearBayesian properties;
• A transformation function may be provided, although this is optional. This is discussed in Transformation of
the results.
3. Perform the estimate and analyse the results:
• Run the estimate process;
• Extract the results and visualise them with the standard plotting tools (see Looking at the results).

### 11.4.1 Constructing the TLinearBayesian object

The constructors available for creating an instance of the TLinearBayesian class are detailed in Common methods of
the calibration classes. As a reminder, the available prototypes are:

```python
# Constructor with a runner
TLinearBayesian(tds, runner, ns=1, option="")
# Constructor with a TCode
TLinearBayesian(tds, code, ns=1, option="")
# Constructor with a function using Launcher
TLinearBayesian(tds, fcn, varexpinput, varexpoutput, ns=1, option="")
```

Details about these constructors can be found in Construction with a TRun, Construction with a TCode, and Construction
for a function with the Launcher architecture respectively for the TRun, TCode, and TLauncherFunction-based constructor
. In all cases, the number of samples 𝑛𝑠is set to 1 by default, and modifying it has no effect on the results, since
it returns the analytical distributions. This class does not define any specific options.
The final step is to construct the TDistanceLikelihoodFunction, a mandatory step that must always immediately
follow the constructor. This can be done via the setLikelihood method (following the prototype presented in Recommended
distance and likelihood functions, construction method).
Exclamation-Triangle Warning
The Analytical Linear Bayesian Estimation method relies on the assumption that residuals are Gaussian (centered)
with a defined covariance matrix (see Defining the TLinearBayesian properties). As a result, the likelihood is not a
free choice but is determined by these assumptions.
It is important to note that the setLikelihood method is used only for residual calculation, to compare the prior
and posterior. Regardless of the initial choice of likelihood, the function is locally redefined so that the computation is
performed via the lin_gauss function using matrix multiplication (through the TMahalanobisDistance method).
Although not recommended, it is still possible to define a custom likelihood function:

```python
setLikelihood(likelihoodFunc, tdsRef, input, reference, weight="")
```

<!-- page 173 (PDF 180) -->
### 11.4.2 Defining the TLinearBayesian properties

Once the TLinearBayesian instance is created along with its TDistanceLikelihoodFunction, two methods must
be called before performing parameter estimate. These methods are mandatory, as they define the analytical formula used
to obtain the Gaussian parameter values of the a posteriori distribution (see [Bla17]).
The first method (although the order is not important) is setRegressorName, whose prototype is

```python
setRegressorName(regressorname)
```

The only argument is regressorname, a string containing the list of regressor names separated by “:”. The method then
performs two checks: it verifies that the number of regressors matches the number of parameters to be calibrated and
it checks that every regressor name provided matches one existing attribute in the reference TDataServer (tdsref).
If the observation TDataServer does not contain the regressors (when the input file is loaded) these attributes must
be constructed from scratch, either with TAttributeFormula or by using another dedicated assessor (as done in the
use-case shown in Macro “calibrationLinBayesFlowrate1D.py”).
The other method is setObservationCovarianceMatrix, whose prototype is

```python
setObservationCovarianceMatrix(mat)
```

The only argument here is a TMatrixD whose content is the covariance matrix of the reference observation data. Once
again, this method will check two things:
• the provided matrix must have the correct dimensions (both rows and columns must be equal to 𝑛);
• the provided matrix should be symmetrical;
Once these conditions are satisfied, estimate can proceed. One can find an example of how to use these methods in the
use-case dedicated subsection (see Macro “calibrationLinBayesFlowrate1D.py”).

### 11.4.3 Looking at the results

Finally, once the computation is complete there are three different kinds of results, with several ways to interpret and
transform them. This section describes some important and specific aspects of these results.

#### 11.4.3.1 Transformation of the results

The idea is that when you want to consider your model as linear, you may need to slightly transform it to ensure proper
linear behaviour and to express and compute the needed regressors. For this particular situation, the use-case described
in Macro “calibrationLinBayesFlowrate1D.py” will be used. In this case, the flowrate function should be linearised as
follows:
𝑓𝜃(𝑥) = (2𝜋𝑇𝑢)
(︃
ln( 𝑟
𝑟𝜔
)
[︃
1 +
2𝐿𝑇𝑢
ln( 𝑟
𝑟𝜔)𝑟2𝜔𝐾𝜔
+ 𝑇𝑢
𝑇𝑙
]︃)︃−1
𝜃= 𝐻× 𝜃
where the regressor can be expressed as 𝐻= (2𝜋𝑇𝑢)
(︁
ln( 𝑟
𝑟𝜔)
[︁
1 +
2𝐿𝑇𝑢
ln( 𝑟
𝑟𝜔)𝑟2𝜔𝐾𝜔+ 𝑇𝑢
𝑇𝑙
]︁)︁−1
. From this, it is clear that
we will be calibrating a newly defined parameter 𝜃= (𝐻𝑢−𝐻𝑙). Therefore, at some point, we will need to transform it
back into our parameter of interest.
This is the reason why the setParameterTransformationFunction method has been implemented: to transform
the estimated parameters given the linear regressor, the observation covariance matrix, and the prior distribution. Since
the transformations, if they exist (they are optional), are expected to be carried out using simple operations with constant
values, they should affect only the mean vector and not the covariance matrix of the posterior multivariate normal
distribution. The prototype of this function is as follows:

<!-- page 174 (PDF 181) -->
```python
setParameterTransformationFunction(fTransfoParam)
```

Its only argument is a pointer to the transformation function. This function, used to obtain the transformed parameter
values, takes two arguments: the input parameters, which are the raw values estimated from the analytical formula detailed
in [Bla17], and the output parameters, which correspond to the desired transformed values. Both arguments are double
arrays of length equal to the number of parameters.
The example provided in the use-case Macro “calibrationLinBayesFlowrate1D.py” is simple as there is only one parameter
to be estimated, which implies that both arguments are one-dimensional double arrays which should look like this:

```python
void transf(double *x, double *res)
{
    res[0] = 1050 - x[0];
                           // simply H_l = \theta - H_u
}
```

Exclamation-Triangle Warning
To achieve this in Python, the function must be placed in a C file (for example, myFunction.C), and this file must
be loaded to obtain a handle on the function. The following lines summarize these two steps in a fictional macro that
defines a cal instance of TLinearBayesian:

```python
# Define all the needed material: dataservers, models...
cal=Calibration.TLinearBayesian(...) # Create the instance and distance function
...
# Load the file in which transformation function
ROOT.gROOT.LoadMacro("myFunction.C")
# Provide this function to the TLinearBayesian instance
cal.setParameterTransformationFunction(ROOT.transf)
```

####  11.4.3.2 Accessing the results

Once the estimate is done (via the classic estimateParameters method), the results can be accessed by calling three
methods, detailed below. All three functions share the same prototype: they take no arguments and return a TMatrixD
instance containing the corresponding information. The functions are:
• getParameterValueMatrix: it returns a TMatrixD with one raw filled with the calibrated values of the parameters
calculated from the analytical formula (one-dimensional);
• getParameterCovarianceMatrix: it returns a TMatrixD filled with the covariance matrix of the estimated parameters
(symmetric and (𝑛𝑃𝑎𝑟, 𝑛𝑃𝑎𝑟)-dimensional);
• getTransfParameterValueMatrix: it returns a TMatrixD with one raw filled with the transformed values of the
parameters, in case setParameterTransformationFunction has been correctly applied (one-dimensional).

#### 11.4.3.3 Drawing the parameters

Parameters can be plotted using a newly defined drawParameters instance, which shares the same prototype as the
original method described in Drawing the parameters.

```python
drawParameters(sTitre, variable = "*", option = "")
```

It takes up to three arguments, two of which are optional:
1. sTitre: the title of the plot (an empty string is allowed);

<!-- page 175 (PDF 182) -->
2. variable (optional): a list of parameter names to be drawn, separated by colons “:”. The default “*” draws all
parameters;
3. option (optional): a list of options, separated by commas “,” to adjust the plotting behavior:
• “nonewcanvas”: draw on the current canvas (instead of creating a new one);
• “vertical”: if multiple parameters are plotted, display them stacked vertically (one per row). By default, plots
are arranged horizontally, side by side.
• “apriori/aposteriori”: draw only the a priori residuals or only the a posteriori residuals. If neither option is
specified, both are displayed;
• “transformed”: this option specifies that the transformed values should be used as the mean vector of the
multivariate normal posterior distribution.
The main difference compared to the standard drawParameters method in TCalibration is that the plotted object
are analytical functions.
In addition to the parameters, the residuals can be plotted using the standard drawResiduals method, which remains
unchanged (see Drawing the residuals).

### 11.4.4 Prediction of the variance

Once the estimate is completed, it is possible to compute the central value for a new set of input values (i.e., for a
new design-of-experiments) using the newly estimated parameter values. Although this applies to every method in the
calibration module, the Linear Bayesian procedure has the advantage of providing the covariance matrix of the parameters.
Under some assumptions on the input distribution, it is possible to obtain a variance for each new predicted value, reflecting
only the uncertainty due to the parameters. For more details on the estimate, see [Bla17]. This can be done by calling
the computePredictionVariance method:

```python
computePredictionVariance(tdsPred, outname)
```

This method takes two arguments, which are:
1. tdsPred: a TDataServer containing the new locations to be estimated, in which all regressors must be available
in order to be able to compute the covariance matrix;
2. outname: the name of the attribute to be created, which will be filled with the diagonal elements (the variances)
of the Σ𝑝𝑟𝑒𝑑
𝜃
matrix.
An example is also provided in the use-case section (see Macro “calibrationLinBayesFlowrate1D.py”).

## 11.5 Approximate Bayesian Computation techniques (ABC)

This section covers methods grouped under the acronym ABC, which stands for Approximate Bayesian Computation. The
core idea is to perform Bayesian inference without explicitly evaluating the model likelihood function. For this reason,
these methods are also refered to as likelihood-free algorithms [Wil13].
As a reminder, the principle of the Bayesian approach is summarized in the equation 𝜋𝑝𝑜𝑠𝑡(𝜃|y) = 𝐿(y|𝜃)𝜋𝑝𝑟𝑖𝑜𝑟(𝜃)
𝜋(y)
∝
𝐿(y|𝜃)𝜋𝑝𝑟𝑖𝑜𝑟(𝜃), where 𝐿(y|𝜃) is the conditional probability of the observations given the parameter values 𝜃, 𝜋𝑝𝑟𝑖𝑜𝑟(𝜃)
is the a priori probability density of 𝜃(the prior), and 𝜋(y) is the marginal likelihood of the observations, which is constant
. For more details see [Bla17].
From a technical perspective, the methods in this section inherit from the TABC class (which itself inherits from TCalibration
, in order to benefit from all standard features). Currently, the only implemented ABC method is the Rejection
algorithm, presented in [Bla17], whose implementation is provided through the TRejectionABC class described below.
The usage of the TRejectionABC class can be summarised in a few key steps:

<!-- page 176 (PDF 183) -->
1. Prepare the data and the model:
• The parameters to be calibrated must be instances of classes inheriting from TStochasticAttribute;
• Select the assessor type and construct the TRejectionABC object with the appropriate distance function (see
Constructing the TRejectionABC object).
2. Set the algorithm properties:
• Define optional behaviours;
• Specify the uncertainty hypotheses via the dedicated methods (see Defining the TRejectionABC properties).
3. Perform the estimate and analyse the results:
• Run the estimate process;
• Extract the results and visualise them with the standard plotting tools (see Looking at the results).

### 11.5.1 Constructing the TRejectionABC object

The constructors available for creating an instance of the TRejectionABC class are detailed in Common methods of the
calibration classes. As a reminder, the available prototypes are:

```python
# Constructor with a runner
TRejectionABC(tds, runner, ns=1, option="")
# Constructor with a TCode
TRejectionABC(tds, code, ns=1, option="")
# Constructor with a function using Launcher
TRejectionABC(tds, fcn, varexpinput, varexpoutput, ns=1, option="")
```

Details about these constructors can be found in Construction with a TRun, Construction with a TCode, and Construction
for a function with the Launcher architecture respectively for the TRun, TCode, and TLauncherFunction-based constructor
. In all cases, the number of samples 𝑛𝑠must be specified, as it represents the number of retained samples in
the final posterior distribution. In our implementation, the total number of computations is determined by the chosen
percentile value (see Defining the percentile).
This class provides one specific option, which can be used to modify the default value of the a posteriori distribution
returned by the algorithm. Two possible choices are available for obtaining the single-point estimate that best represents
the distribution:
• Mean of the distribution: this is the default option;
• Mode of the distribution: the user must specify “mode” in the option field of the TRejectionABC constructor.
The default solution is straightforward, whereas the second requires internal smoothing of the distribution in order to
obtain the best estimate of the mode.
The final step is to construct the TDistanceLikelihoodFunction, a mandatory step that must always immediately
follow the constructor. Although ABC methods are Bayesian, they are likelihood-free: instead of directly computing the
likelihood, they calculate the distance between the observed data and the simulated data for several prior samples, until the
best-fitting distribution is identified. Consequently, the TDistanceLikelihoodFunction object can be constructed
via the setDistance method (following the prototype presented in Recommended distance and likelihood functions,
construction method). Advanced users also have the option to define a custom distance by following the prototype:

```python
setDistance(distFunc, tdsRef, input, reference, weight="")
```

<!-- page 177 (PDF 184) -->
Exclamation-Triangle Warning
If the reference dataset is compared against a deterministic model (i.e. a model with no intrinsic stochasticity), it is
necessary to explicitly specify the uncertainty hypotheses. This is done via the method described in Introducing noise
for deterministic function.

### 11.5.2 Defining the TRejectionABC properties

Once the TRejectionABC instance is created along with its associated TDistanceLikelihoodFunction, a few additional
methods can be used to fine-tune the algorithm parameters. These methods are optional, since each property has
a predefined default value. The available options are described in the following sub-sections.

#### 11.5.2.1 Defining the percentile

The first method discussed here is straightforward: the principle of rejection is to keep the best-tested configurations.
This can be done either by applying a threshold value on the distance results (called 𝛿in [Bla17]) or by retaining a fixed
fraction of the tested configurations, defined through a percentile 𝜀𝐷𝑖𝑠𝑡. The TRejectionABC method implements the
latter approach. By default, the percentile is set to 𝜀𝐷𝑖𝑠𝑡= 0.01.
To modify this value, the user can call setPercentile, whose prototype is

```python
setPercentile(eps)
```

where the argument eps specifies the fraction of configurations to be kept.
An important consequence is that the total number of configurations evaluated is computed as follows:
𝑛Comp =
𝑛𝑆
𝜀𝐷𝑖𝑠𝑡
where 𝑛𝑆is the number of retained samples in the final posterior distribution, as defined in the constructor (see Constructing
the TRejectionABC object).

#### 11.5.2.2 Introducing noise for deterministic function

As previously explained, when comparing your reference dataset to a deterministic model (i.e., a model with no intrinsic
stochastic behaviour), the user can explicitly specify his own uncertainty assumptions. This can be done by calling
setGaussianNoise, whose prototype is

```python
setGaussianNoise(stdname)
```

The idea is to inject random noise (assumed Gaussian and centered) into the model predictions, using internal variables
from the reference dataset to define its standard deviation. The only argument is a list of variables, formatted as "stdvaria
1:stdvaria2", where each element corresponds to a variable within the reference TDataServer. These values
provide the standard deviation for each observation point (for example, to represent experimental uncertainty).
This solution allows to:
• define a common uncertainty (applied generally across all observations in the reference dataset) by simply adding
an attribute with a TAttributeFormula, where the formula is constant;
• use experimental uncertainties that are provided along with the reference values;
• store all hypotheses within the reference TDataServer object. For this reason, we strongly recommend saving
both the parameter and reference datasets at the end of a calibration procedure.

<!-- page 178 (PDF 185) -->
Exclamation-Triangle Warning
The number of variables in the stdname list must match the number of model outputs. Even in the special case
where calibration involves two outputs, with one having no associated uncertainty, a zero-valued attribute should still
be added for that output if the other requires an uncertainty model.

### 11.5.3 Looking at the results

Finally, once the computation is complete (using the standard estimateParameters method), the results can be examined
in two main ways (in addition to inspecting the final datasets):
• using the drawParameters method, introduced in Drawing the parameters;
• using the drawResiduals method, introduced in Drawing the residuals.
No additional options or visualization methods are specific to the TRejectionABC implementation; these functions
behave exactly as described in their respective sections.
An example is also provided in the use-case section (see Macro “calibrationRejectionABCFlowrate1D.py”).

## 11.6 Markov chain Monte Carlo approach

In a Bayesian framework, Markov Chain Monte Carlo (MCMC) methods are a powerful tool for calibration. They
are especially valuable when the statistical model cannot be solved analytically, such as when the prior distribution has a
complex structure or the model is nonlinear. Unlike many classical approaches, MCMC does not require the assumption
of Gaussian errors: it remains applicable even when the likelihood is non-Gaussian.
Rather than providing a single “best-fit” solution (as in minimisation techniques), MCMC generates a collection of parameter
samples that represent the full posterior distribution (similar to ABC methods). However, these methods also come
at the cost of potentially high computational demand, since long sampling chains may be required to achieve convergence
and reliable estimates. Users should therefore interpret results as distributions and ensure that convergence diagnostics
are checked before drawing conclusions (see [Bla17] for more details).
The usage of the TMCMC class can be summarised in a few key steps:
1. Prepare the data and the model:
• The parameters to be calibrated must be instances of classes inheriting from TStochasticAttribute;
• Select the assessor type and construct the TMCMC object with the appropriate likelihood function (see Constructing
the TMCMC object).
2. Set the algorithm properties:
• Define optional behaviours;
• Specify the uncertainty hypotheses via the dedicated methods (see Defining the TMCMC properties).
3. Perform the estimate:
• Run the estimate process;
• Eventually continue it if the convergence is not reached (see Running the estimate, exporting and loading
chains, and continuing the calculation).
4. Perform post-processing:
• Investigate the quality of the samples through diagnostics and plots (see Investigating the quality of the samples
through diagnostics and plots).
5. Analyse the results:

<!-- page 179 (PDF 186) -->
• Extract the results and visualise them with the standard plotting tools (see Looking at the results).

### 11.6.1 Constructing the TMCMC object

The constructors available for creating an instance of the TMCMC class are detailed in Common methods of the calibration
classes. As a reminder, the available prototypes are:

```python
# Constructor with a runner
TMCMC(tds, runner, ns=1, option="")
# Constructor with a TCode
TMCMC(tds, code, ns=1, option="")
# Constructor with a function using Launcher
TMCMC(tds, fcn, varexpinput, varexpoutput, ns=1, option="")
```

Details about these constructors can be found in Construction with a TRun, Construction with a TCode, and Construction
for a function with the Launcher architecture respectively for the TRun, TCode, and TLauncherFunction-based
constructor. In all cases, the number of iterations 𝑛𝑠must be specified.
This class provides one specific option, which can be used to modify the default value of the a posteriori distribution
returned by the algorithm. Two possible choices are available for obtaining the single-point estimate that best represents
the distribution:
• Mean of the distribution: this is the default option;
• Mode of the distribution: the user must specify “mode” in the option field of the TMCMC constructor.
The default solution is straightforward, whereas the second requires internal smoothing of the distribution in order to
obtain the best estimate of the mode.
In practice, the constructor—whichever one is chosen—initializes a folder named MCMC_N, where N is an integer ensuring
the folder name is available. This folder contains all the information related to the MCMC calculation (the chain values, the
algorithm used, the number of accepted samples, etc.), with each chain stored in a separate file named MCMC_N_chain_M
(for the M-th chain, starting from 0). By default, only one chain is initialized, so the MCMC_N folder contains a single file
MCMC_N_chain_0. This folder will be duplicated once the setMultistart method is called (see Initialising several
chains). The files are automatically loaded and saved during the computation.
The next step is to construct the TDistanceLikelihoodFunction, a mandatory step that must always immediately
follow the constructor. For now, the only available likelihood function is the Gaussian, as it is the most commonly used.
It can be accessed through the classic setLikelihood method using the function name "log-gauss", following the
standard prototype (presented in Recommended distance and likelihood functions, construction method). As previously
explained, in this case the weights provided to the constructor correspond to the standard deviations of each observation.
Advanced users also have the option to define a custom likelihood by following the prototype:

```python
setLikelihood(likelihoodFunc, tdsRef, input, reference, weight="")
```

###  11.6.2 Defining the TMCMC properties

Once the TMCMC instance is created along with its TDistanceLikelihoodFunction, a few methods are available to
tune the algorithms. All of these methods are optional, as default values are provided. However, they should be applied
in the following order:
1. Define the MCMC algorithm properties that are shared by all chains: MCMC algorithm, acceptation range, and
information display interval (these can be set in any order).
2. Specify the number of chains to initialize.
3. Prepare the starting points and the initial standard deviations of the proposal distribution (these can be set in any
order).

<!-- page 180 (PDF 187) -->
#### 11.6.2.1 Chosing the MCMC algorithm

Several MCMC algorithms are available, and the desired algorithm can be selected using the setAlgo method, which
has the following prototype:

```python
setAlgo(algoMCMC)
```

The method takes a single string argument that specifies the algorithm to use. Currently, the following options are supported
:
• Component-wise Metropolis–Hastings, specified with “MH_1D”. This method updates one parameter at a time,
which is useful when parameters have different influences on the model. By generating new candidates along one
direction at a time, it prevents less influential parameters from being overshadowed by the more influential ones.
This approach is generally slower than the classic Metropolis–Hastings;
• Classic Metropolis–Hastings, specified with “MH_multiD” (default algorithm). This method generates candidates
in all directions simultaneously, making it faster than the component-wise approach, but it may be less efficient when
parameter influences vary widely.
Exclamation-Triangle Warning
As explained, this method should be done immediately after creating the TMCMC object and assigning its likelihood.

#### 11.6.2.2 Tuning the acceptation rate

As also explained in [Bla17], there are theoretical discussions on the acceptation rate expected, depending on the dimension
of the parameter space for instance. As stated in some references (see [GRG+96, RGG+97]) when well initialised
, for a single-dimension problem, the acceptation rate could be around 44%, decreasing to about 23% as the
dimensionality increases. By default, the exploration parameters are set during the initialisation step (see Initialising the
process).
If one wants to change this, a possible approach is to use the setAcceptationRatioRange method whose prototype
is the following

```python
setAcceptationRatioRange(lower, higher)
```

This prototype takes two arguments: the lower (𝑟low) and higher (𝑟hig) bounds. The idea is simply that after a certain
number of estimate (called batch, whose value is set to 100) the algorithm looks at the acceptation rate achieved (actually
this is computed for every configuration and kept in the final TDataServer object). If the lower and higher bounds have
been set, at the end of a batch, three cases are possible (when the acceptation rate is called 𝑟acc):
• 𝑟acc ≤𝑟low: the acceptation rate is too low compared to the desired range, this means the algorithm is moving
too far from the last accepted configuration. As a consequence, the variation range is reduced by 10% to improve
convergence.
• 𝑟hig ≤𝑟acc: the acceptation rate is too high compared to the desired range, this means that the algorithm is not
exploring the parameter space adequately, focusing only on a well-performing region. As a consequence, the
variation range is increased by 10% to encourage exploration.
• 𝑟low ≤𝑟acc ≤𝑟hig: the acceptance rate is within the desired range, no adjustment is made.
When the setAcceptationRatioRange method has been called, this process will be called at the end of every batch.
Otherwise, the default behaviour is to leave the acceptation rate unchanged, as no boundaries have been set.
From the prototype and the behaviour discussed above, two rules must be followed when using this method: (𝑟low, 𝑟hig) ∈
[0, 1]2 and 𝑟low < 𝑟hig.

<!-- page 181 (PDF 188) -->
Finally, the evolution of the acceptance rate can be examined by plotting the relevant information, as discussed in Drawing
the acceptation ratio.

#### 11.6.2.3 Information on the process

The next method discussed here is fairly simple: a MCMC simulation may take a long time to complete, particularly when
running code, regardless of the chosen architecture. This method changes the number of iterations between two output
displays. The prototype is simply:

```python
setNbDump(nbDump)
```

The method takes a single integer argument that specifies the interval (modulo) at which the algorithm displays its progress.
With the default value of 1000, the output will look like this:

```python
1000 events done
2000 events done
3000 events done
...
```

####  11.6.2.4 Initialising several chains

As already explained in [Bla17], initialising multiple chains can help assess the convergence of MCMC algorithms more
reliably. Since these algorithms are inherently sequential (each state of the chain depending on the previous one), running
several chains in parallel also makes it possible to exploit modern computational power more effectively. At present, this
parallelization is not yet implemented—the chains are still computed sequentially—but it will be supported in a future
release.
If you wish to initialise multiple chains, this should be done using the following prototype:

```python
setMultistart(nb_multistart)
```

The method takes a single integer argument that specifies the number of chains to be initialised.
Exclamation-Triangle Warning
As explained, this method duplicates the file of the initial chain to prepare several chains, preserving the properties that
have already been defined. For this reason, it should be performed immediately after selecting the MCMC algorithm,
to ensure that all chains use the same algorithm. If the default algorithm is used, this step should be done after creating
the TMCMC object and assigning its likelihood.

#### 11.6.2.5 Initialising the process

As already explained in [Bla17], the MCMC algorithm starts at a given point and then moves to a new configuration.
This means that two things must be specified for each parameter: a starting value, and a variation range used to move
to the next location. Since all the input parameters are stochastic (in other words, instances of classes inheriting from
TStochasticAttribute), the default values are
• randomly drawn for the starting point;
• the theoretical standard deviation used as the variation range.
The default behaviour can easily be overridden by calling the setStartingPoints and the setProposalStd methods
with these prototypes:

<!-- page 182 (PDF 189) -->
```python
# Prototype setStartingPoints
setStartingPoints(ichain, values)
# Prototype setProposalStd
setProposalStd(ichain, standDev)
```

The first argument of both prototypes is the chain index, an integer between −1 and 𝑛𝐶−1, where 𝑛𝐶is the number of
chains (indexed from 0 to 𝑛𝐶−1). If −1 is chosen, all chains will be assigned the same starting point (not recommended,
since the purpose of using multiple chains is to initialise them at different locations to verify convergence toward the same
region) or the same standard deviation.
The second argument of both prototypes is a vector containing either the initial values of the starting points (one value
for each parameter to calibrate) or the standard deviations (one for each parameter), which will be assigned to the corresponding
chain. This means that the vectors must have a size 𝑝, corresponding to the number of parameters.
11.6.3 Running the estimate, exporting and loading chains, and continuing the calculation

The computation can be performed using the standard estimateParameters method, which automatically saves the
chains in their associated files. Although it is generally unnecessary (since saving is done automatically), it is still possible
to manually export the results of a chain or reload them later using export_chain_MCMC and read_chain_MCMC,
whose prototypes are the following:

```python
# Export one chain
export_chain_MCMC(fileName)
# Read one chain
read_chain_MCMC(fileName)
```

Both methods take a single string argument specifying the file name used for exporting or loading the chain results.
In most cases, these methods are not required. They become useful when a computation finishes without reaching convergence
and the user wishes to extend the run. This can be done with the continueCalculation method, which
executes additional iterations of the MCMC algorithm in order to try to achieve convergence. Its prototype is:

```python
continueCalculation(new_Ns)
```

This method takes a single integer argument that specifies the number of additional iterations to run. In this case, it may be
useful to reload one of the previously computed chains with read_chain_MCMC before calling continueCalculation.
Regardless of which chain is loaded, the calculation will continue for all initialized chains.

### 11.6.4 Investigating the quality of the samples through diagnostics and plots

Computing iterations does not guarantee that the chains have reached convergence and are properly sampling the posterior
distribution. Although there is no exact way to prove convergence, several techniques can help assess the quality of the
samples. Before plotting and analyzing the results, it is mandatory to check these diagnostics to determine whether the
results are reliable or if the algorithm should be run for additional iterations (see Running the estimate, exporting and
loading chains, and continuing the calculation). These techniques serve two main purposes:
Ensuring convergence of the chains: Convergence means that the chains have stabilized around the same region. This
must be checked by the user using the trace plot (see Drawing the trace). It is also recommended to check the stability of
the acceptance ratio, which should typically lie between 20% and 50%, using the acceptance ratio plot (see Drawing the
acceptation ratio). Finally, the user must define the burn-in (also called warm-up), i.e., the number of initial iterations
discarded before the chain stabilizes. This is done with the setBurnin method:

```python
setBurnin(burnin)
```

<!-- page 183 (PDF 190) -->
This method takes a single integer argument that specifies the number of iterations to remove (non-converged iterations).
When multiple chains are initialized (at least 4), it is also possible to compute the Gelman–Rubin statistic, which compares
intra- and inter-chain variances (see Checking for convergence with the Gelman–Rubin diagnostic). Values close to
1 indicate good convergence.
Ensuring approximate independence of posterior samples: Because Markov chains generate dependent samples,
there is a risk that successive samples are correlated and do not explore the posterior distribution effectively. To assess
this, the Effective Sample Size (ESS) can be computed with the diagESS method (see Thinning the chains with ESS),
which provides the equivalent number of independent samples. This method also suggests an appropriate lag value, i.e.,
the number of iterations to skip before selecting the next uncorrelated sample. The lag is set using the setLag method:

```python
setLag(lag)
```

The method takes a single integer argument that specifies the lag value.
Exclamation-Triangle Warning
Setting lag and burn-in values with the setLag and setBurnin methods will affect most drawing methods, and a
line will indicate which default cut and lag were applied to produce the plot. The only exception is the residuals plot,
since the a posteriori residuals are computed during estimateParameters, before any burn-in or lag is applied. To
re-estimate residuals with a specific lag or burn-in, use the estimateCustomResiduals method (see Estimate custom
residuals). To remove the current cut and lag, use the clearDefaultCut method, which requires no arguments
and clears both lag and burn-in:

```python
clearDefaultCut()
```

Another important point is that these methods may discard a significant number of samples. The burn-in length and lag
value should therefore be chosen carefully to balance two goals: keeping enough points to ensure a good representation
of the posterior distribution, while also guaranteeing convergence and independence of the samples.

#### 11.6.4.1 Drawing the trace

This method is used to visualise the trace of the chains, i.e., the evolution of parameter values across iterations. It should
be used to check the stability of the chains (stability of the mean and variance, see [Bla17]), and to detect potential
autocorrelation (when the chain moves too slowly within the target distribution).
Thus, trace plots provide a first indication of the appropriate burn-in (the number of iterations to discard before stability
is reached) and lag (the number of iterations to skip to reduce autocorrelation). The prototype is:

```python
drawTrace(sTitre, variable = "*", option = "")
```

This method takes up to three arguments, two of which are optional:
1. sTitre: the title of the plot (an empty string is allowed);
2. variable (optional): a list of parameter names to be drawn, separated by colons “:”. The default "*" draws all
parameters;
3. option (optional): a list of options, separated by commas “,”, to adjust the plotting behavior:
• “nonewcanvas”: draw on the current canvas (instead of creating a new one);
• “vertical”: if multiple parameters are plotted, display them stacked vertically (one per row). By default, plots
are arranged horizontally, side by side;
Returning to the example in Macro “calibrationMCMCFlowrate1D.py”, the trace plots (shown in Figure 13.66) reveal that
the very beginning of the chain is unstable, likely because initialization was far from the most probable value. Afterward,

<!-- page 184 (PDF 191) -->
the behavior stabilizes, oscillating around what appears to be the most probable region. Based on this, a small burn-in of
about 10 iterations could be chosen.
Looking at the acceptance ratio plot (see Figure 13.67), however, suggests that the burn-in should be slightly larger.
Therefore, we set a value of 50 for the burn-in using the setBurnin method (see Investigating the quality of the samples
through diagnostics and plots). When a trace plot is drawn after defining a burn-in with setBurnin, the burn-in region
is indicated by a black dotted line.

#### 11.6.4.2 Drawing the acceptation ratio

This method is used to visualise the evolution of the acceptation ratio across iterations. It should be used to check the
stability of the chains, since an unstable acceptation ratio indicates that the chains may not have converged. It also allows
the user to verify that the acceptation ratio stabilizes within the desired range (between 20% and 50%), which ensures
good exploration of the target density while retaining a sufficient number of samples.
Thus, acceptation ratio plots provide useful guidance for determining an appropriate burn-in (the number of iterations
to discard before stability is reached) and for selecting a suitable initial standard deviation of the proposal distribution to
achieve an acceptation ratio within the desired range. The prototype is:

```python
drawAcceptationRatio(sTitre, variable = "*", option = "")
```

This method takes up to three arguments, two of which are optional:
1. sTitre: the title of the plot (an empty string is allowed);
2. variable (optional): a list of parameter names to be drawn, separated by colons “:”. The default "*" draws all
parameters;
3. option (optional): a list of options, separated by commas “,”, to adjust the plotting behavior:
• “nonewcanvas”: draw on the current canvas (instead of creating a new one);
• “vertical”: if multiple parameters are plotted, display them stacked vertically (one per row). By default, plots
are arranged horizontally, side by side;
Returning to the example in Macro “calibrationMCMCFlowrate1D.py”, the acceptation ratio plots (shown in Figure 13.67)
reveal that the acceptation ratio is unstable during the first iterations, likely because the chains were initialised far from
the most probable value. Afterward, the acceptation ratio stabilizes, oscillating around what appears to be an asymptote.
Based on this, a burn-in of about 50 can be considered appropriate. When a acceptation ratio plot is drawn after defining
a burn-in with setBurnin, the burn-in region is indicated by a black dotted line.

#### 11.6.4.3 Checking for convergence with the Gelman–Rubin diagnostic

Once the trace and acceptance ratio plots have been analysed, and an initial burn-in value has been chosen, the Gelman
–Rubin diagnostic can be used to verify the convergence of the chains. This diagnostic compares the intra- and
inter-chain variances (see [Bla17] for more details).
The method diagGelmanRubin has the following prototype:

```python
diagGelmanRubin()
```

This method takes no arguments, as it is called directly from the TCalibration object. For example, in Macro “calibration
MCMCFlowrate1D.py”, the Gelman–Rubin diagnostic is computed with:

```python
GelmanRubin_values = cal.diagGelmanRubin()
GelmanRubin_values["hl"] # To extract the Gelman-Rubin statistic for parameter hl
```

The returned object GelmanRubin_values is an unordered map where each parameter name (e.g., hl) is associated
with its Gelman–Rubin statistic value. The results are also printed in the console (see Console), accompanied by a short
generic commentary interpreting the statistic.

<!-- page 185 (PDF 192) -->
In this example, the Gelman–Rubin diagnostic confirms good convergence of the chains (and thus the suitability of the
chosen burn-in value). In other cases, where the statistics indicate poorer convergence, it may be necessary to run additional
iterations (see Running the estimate, exporting and loading chains, and continuing the calculation) or to adjust the
burn-in value (see Investigating the quality of the samples through diagnostics and plots).

#### 11.6.4.4 Thinning the chains with ESS

Once convergence of the chains has been assessed using the trace plot (see Drawing the trace), the acceptance ratio
plot (see Drawing the acceptation ratio), and the Gelman–Rubin diagnostic (see Checking for convergence with the Gelman
–Rubin diagnostic), the next step is to evaluate the autocorrelation of the samples. If samples are highly correlated,
the posterior distribution may not be properly explored (e.g., chains could remain trapped in a mode).
A common way to assess this is to compute the Effective Sample Size (ESS), which estimates how many samples can
effectively be considered as independent among the available ones. ESS thus indirectly indicates the appropriate lag (the
number of iterations to skip to obtain approximately uncorrelated samples). More details are provided in [Bla17].
The method diagESS has the following prototype:

```python
diagESS()
```

This method takes no arguments, as it is called directly from the TCalibration object. For example, in Macro “calibration
MCMCFlowrate1D.py”, the ESS diagnostic is computed with:

```python
ESS_values = cal.diagESS()
ESS_values["hl"][0] # To extract the ESS statistic for parameter hl computed on the␣
```

˓→first chain
The returned object ESS_values is an unordered map where each parameter name (e.g., hl) is associated with a vector
of ESS values, one per chain. The results are also printed in the console (see Console).
In this example, the ESS diagnostic confirms that each parameter has several hundred (at least 200) effectively uncorrelated
samples. It is therefore recommended to set the lag to 1 using setLag method (see Investigating the quality of the samples
through diagnostics and plots), which indicates that the samples are sufficiently uncorrelated.
If the ESS is too small, it may be necessary to run additional iterations (see Running the estimate, exporting and loading
chains, and continuing the calculation) or to adjust the initial standard deviation of the proposal distribution, which may
be too small, causing the chain to move too slowly (see Initialising the process).

### 11.6.5 Looking at the results

Once the convergence of the chains has been assessed and thinning applied, the results can be analysed in more detail.
While trace plots are already informative results on their own, several additional methods are available. Among the
implemented tools, it is possible to display pairwise parameter traces (see Drawing the 2D trace), visualise the posterior
distributions (see Drawing the parameters), and examine the residual distribution (see Drawing the residuals). These
methods are described in the following sections:

#### 11.6.5.1 Drawing the 2D trace

This method is used to visualise the trajectory of the chains across iterations by examining two parameters at a time. It
can help verify that the chains uniformly explore the distribution and that they converge toward the same posterior. It also
highlights potential covariance between pairs of parameters in the posterior distribution.
Although this method can be used as a diagnostic tool, it is less effective for assessing chain stability or detecting autocorrelation
. For those purposes, standard trace plots remain preferable.
The prototype is:

<!-- page 186 (PDF 193) -->
```python
draw2DTrace(sTitre, variable, option = "")
```

This method takes up to three arguments, two of which are optional:
1. sTitre: the title of the plot (an empty string is allowed);
2. variable (optional): a list of exactly two parameter names to be drawn, separated by colons ":". For example,
"t0:t1" is a valid argument to plot the chains of t0 and t1 together on a 2D trace;
3. option (optional): a list of options, separated by commas “,”, to adjust the plotting behavior:
• “nonewcanvas”: draw on the current canvas (instead of creating a new one);
Returning to the example in Macro “calibrationMCMCLinReg.py”, the 2D trace plot (shown in Figure 13.72) clearly show
the four chains converging toward the posterior distribution located in the center of the plot. The distribution appears
to be uniformly covered by a sufficient number of samples, without any obvious trend suggesting covariance between the
two parameters.

#### 11.6.5.2 Drawing the parameters

The posterior distributions of the parameters can be visualised using the dedicated instance of drawParameters, whose
prototype is identical to that discussed in Drawing the parameters.

```python
void drawParameters(sTitre, variable = "*", option = "")
```

The only difference from the standard drawParameters method in TCalibration is that this version automatically
accounts for the burn-in period and the lag (see Investigating the quality of the samples through diagnostics and plots for
details). Specifically, the first samples of each chain are discarded according to the burn-in value, and the remaining
samples are thinned using the specified lag (i.e., one sample is retained out of every lag iterations).
An example of this function is shown in Figure 13.74.

#### 11.6.5.3 Drawing the residuals

The residuals can be visualised with the standard drawResiduals method of any TCalibration object. Its arguments
and options have already been detailed in Drawing the parameters, and its prototype is recalled here for convenience:

```python
drawResiduals(sTitre, variable = "*", select = "1>0", option = "")
```

Since no specific implementation has been added for MCMC calibration, the main point to clarify is how the a priori and
a posteriori configurations are defined:
• A priori configuration: obtained from the parameter initialisation. This can either be provided explicitly by the
user through the method described in Initialising the process, or, if not specified, generated from a random draw
according to the given a priori probability density.
• A posteriori configuration: by default, the mean of the posterior distribution is used (as discussed in the constructor
section of this class, see Constructing the TMCMC object). If the option “mode” is specified when constructing the
TMCMC object, then the posterior mode is estimated and used instead.
An example of this function is shown in Figure 13.73.
Two examples are also provided in the use-case section (see Macro “calibrationMCMCFlowrate1D.py” and Macro “calibration
MCMCLinReg.py”).

<!-- page 187 (PDF 194) -->
## 11.7 CIRCE method

The CIRCE method is a statistical approach proposed as an alternative to expert judgement, designed to determine the
uncertainty of parameters in a physical model. Such uncertainties are often difficult to assess because some parameters
may not be directly measurable. However, by relying on separate-effect tests (SET) experiments, that are sensitive to the
physical model, it becomes possible to infer estimates of these uncertainties.
As explained in Introduction, CIRCE is not a strict calibration method, its logic differs from the standard framework (see
[Bla17] for details). For this reason, it does not inherit from the TCalibration class (and therefore does not provide the
common calibration methods presented in Common methods of the calibration classes). Instead, it has its own dedicated
structure, implemented in Uranie through the TCirce class.
The usage of the TCirce class can be summarised in a few key steps:
1. Prepare the data and the model:
• Specify the experimental dataserver;
• Construct the TCirce object by specifying the experimental attribute, the code attribute, and the sensitivity
attributes (see Constructing the TCirce object).
2. Set the algorithm properties:
• Initialise the algorithm;
• Define optional behaviours (see Defining the TCirce properties).
3. Perform the estimate:
• Run the estimate process (see Running the estimate).
4. Perform post-processing:
• Extract the results for post-treatment (see Looking at the results).

### 11.7.1 Constructing the TCirce object

To create an instance of the TCirce class, the constructor is available with the following prototype:

```python
TCirce(tds, systar, syhat, ssensi, sexpuncert = "", option = "")
```

This method takes up to six arguments, two of which are optional:
1. tds: a TDataServer object containing:
• one attribute for the experimental data,
• one attribute for the code output,
• and the attributes corresponding to the derivatives of the code output with respect to each parameter (one
attribute per parameter).
2. systar: name of the experimental attribute;
3. syhat: name of the code output attribute;
4. ssensi: list of attribute names corresponding to the derivatives of the code output with respect to each parameter,
separated by commas “,”;
5. sexpuncert (optional): name of the experimental uncertainty attribute;
6. option (optional): currently, no options are implemented for this class.

<!-- page 188 (PDF 195) -->
### 11.7.2 Defining the TCirce properties

Once the TCirce object has been constructed, it is possible to configure several hyperparameters of the algorithm.
The first one is the tolerance parameter used as a stopping criterion. Its default value is 1.0e-5, but it can be modified
with the setTolerance method, whose prototype is the following:

```python
setTolerance(dtol)
```

This method accepts a single argument: a double precision value defining the new tolerance.
It is also possible to provide initial values for the algorithm:
• an initial vector of biases (default value is null vector), set with setBVectorInitial;
• an initial correlation matrix (default value is identity matrix), set with setCMatrixInitial.

```python
setBVectorInitial(vec)
setCMatrixInitial(mat)
```

Each method accepts a single argument, namely the initial TVectorD (for the biases) or the initial TMatrixD (for the
correlation matrix).
Finally, the user can define the number of iterations for running the algorithm with different initial correlation matrices
(default value is 1) using the setNCMatrix method, whose prototype is the following:

```python
setNCMatrix(n)
```

This method accepts a single integer argument that sets the number of iterations.
All these methods have corresponding getter functions, which allow retrieving the current values:
• getTolerance returns the tolerance (double),
• getBVectorInitial returns the initial bias vector (TVectorD),
• getCMatrixInitial returns the initial correlation matrix (TMatrixD),
• getNCMatrix returns the number of iterations (integer).

### 11.7.3 Running the estimate

Since the TCirce class does not inherit from the TCalibration class (as it is not strictly a calibration method), it
provides its own execution method. This method is named estimate (rather than estimateParameters) and must
be called directly from the TCirce object to compute the vector of biases and the correlation matrix. Its prototype is:

```python
estimate(option = "")
```

This method accepts a single optional argument, which can specify options for running the process. At present, no options
are implemented for this class, so the argument should not be used.

### 11.7.4 Looking at the results

Once the computation is complete, several methods are available to extract or display the results.
The bias vector and the correlation matrix can be retrieved with the getBVector and getCMatrix methods, respectively:

```python
getBVector()
getCMatrix()
```

<!-- page 189 (PDF 196) -->
These methods take no arguments, as they are directly applied to the TCirce object after the process has been run. They
return a TVectorD and a TMatrixD corresponding to the bias vector and the correlation matrix.
It is also possible to obtain the likelihood value for the optimal parameters with the getLikelihood method:

```python
getLikelihood()
```

This method also takes no arguments. It returns a double corresponding to the likelihood value of the optimal parameters.
The methods getMatrixVarianceMu and getMatrixVarianceSigma return, respectively, the variance matrices of
mu and sigma, as computed via the Fisher Matrix confidence interval:

```python
getMatrixVarianceMu()
getMatrixVarianceSigma()
```

Finally, all of this information can be displayed on the console using the printResults method:

```python
printResults(option = "")
```

This method accepts a single optional argument, which can specify options for running the process. At present, no options
are implemented for this class, so the argument should not be used.
An example is also provided in the use-case section (see Macro “calibrationCirce.py”).
