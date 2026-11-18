# Use-cases in Python — Macros Calibration — Macro “calibrationMinimisationFlowrate1D.py” … Macro “calibrationRejectionABCFlowrate1D.py”
<!-- source PDF pages 442-459 -->

<!-- page 435 (PDF 442) -->
gorithm. Two parameters are given, first one configuring the initial search, and the second the following one using
previous results.
These solvers are passed to the TEGO class with a dedicated method. Currently, EGO runs in verbose modes.
The resulting TDataServer is filled with all evaluated solutions. In our case of a multi modal problem, keeping just the
best solution is not appropriate. A postprocessing is needed to get best solutions.

## 13.11 Macros Calibration

This section introduces a few examples of calibration in order to illustrate the different techniques introduced in The
Calibration module, along with some of the available options.

### 13.11.1 Macro “calibrationMinimisationFlowrate1D.py”

#### 13.11.1.1 Objective

The goal here is to calibrate the parameter 𝐻𝑙within the flowrate model, while varying only two inputs (𝑟𝜔and 𝐿). The
remaining variables are fixed to the following values: 𝑟= 25050, 𝑇𝑢= 89335, 𝑇𝑙= 89.55, 𝐻𝑢= 1050, 𝐾𝜔= 10950.
The context of this example has already been presented in Use-case for this chapter, including the model (implemented
here as a C++ function) and the initial lines defining the TDataServer objects. This macro demonstrates how to apply
a simple minimisation approach using a Relauncher-based architecture.

#### 13.11.1.2 Macro Uranie

```python
"""
Example of calibration using minimisation approach on flowrate 1D
"""
from URANIE import DataServer, Relauncher, Reoptimizer, Calibration
import ROOT
# Load the function flowrateCalib1D
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Input reference file
ExpData = "Ex2DoE_n100_sd1.75.dat"
# define the reference
tdsRef = DataServer.TDataServer("tdsRef", "doe_exp_Re_Pr")
tdsRef.fileDataRead(ExpData)
# define the parameters
tdsPar = DataServer.TDataServer("tdsPar", "tdsPar")
tdsPar.addAttribute(DataServer.TAttribute("hl", 700.0, 760.0))
tdsPar.getAttribute("hl").setDefaultValue(728.0)
# Create the output attribute
out = DataServer.TAttribute("out")
# Create interface to assessors
Model = Relauncher.TCIntEval("flowrateCalib1D")
Model.addInput(tdsPar.getAttribute("hl"))
Model.addInput(tdsRef.getAttribute("rw"))
Model.addInput(tdsRef.getAttribute("l"))
```

<!-- page 436 (PDF 443) -->
```python
Model.addOutput(out)
# Set the runner
runner = Relauncher.TSequentialRun(Model)
# Set the calibration object
cal = Calibration.TMinimisation(tdsPar, runner, 1)
cal.setDistance("LS", tdsRef, "rw:l", "Qexp")
solv = Reoptimizer.TNloptSubplexe()
cal.setOptimProperties(solv)
cal.estimateParameters()
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
```

Apart from the initial lines described in the section Use-case for this chapter, the key step is to define the starting point
of the minimisation. This can be achieved either by calling the setStartingPoint method of the TNlopt class, or by
assigning a default value to the parameter attributes. In this example, it is done as follows:

```python
tdsPar.getAttribute("hl").setDefaultValue(728.0)
```

The model is defined (from a TCIntEval instance with the three input variables discussed above, in the correct order)
along with the computation distribution method (sequential).

```python
# Create interface to assessors
Model = Relauncher.TCIntEval("flowrateCalib1D")
Model.addInput(tdsPar.getAttribute("hl"))
Model.addInput(tdsRef.getAttribute("rw"))
Model.addInput(tdsRef.getAttribute("l"))
Model.addOutput(out)
# Set the runner
runner = Relauncher.TSequentialRun(Model)
```

Once this setup is complete, the calibration object (TMinimisation) is created. As explained in Recommended distance
and likelihood functions, construction method, the first step is to define the distance function (here the least squares distance
) using setDistance. This method also specifies the TDataServer containing the reference data, the names of
the reference inputs, and the reference variable against which the model output is compared. Finally, the optimisation
algorithm is defined by creating an instance of TNloptSubplexe, and the parameters are then estimated.

```python
# Set the calibration object
cal = Calibration.TMinimisation(tdsPar, runner, 1)
cal.setDistance("LS", tdsRef, "rw:l", "Qexp")
solv = Reoptimizer.TNloptSubplexe()
cal.setOptimProperties(solv)
cal.estimateParameters()
```

The final part demonstrates how to display the results. Since this method produces a point estimate, only a single value
is obtained, which is always shown on the screen, as illustrated in Console. Another important aspect is to examine

<!-- page 437 (PDF 444) -->
the residuals, as discussed in [Bla17]. This is illustrated in Figure 13.59, which shows the residuals of the a posteriori
estimates, typically following a normal distribution.

```python
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
```

####  13.11.1.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
|....:....|....:....|....:....|....:
.************************************************
*
     Row
           * tdsPar__n *
                             hl.hl * agreement *
************************************************
*
         0 *
                     0 * 749.72363 * 18.149368 *
************************************************
```

<!-- page 438 (PDF 445) -->
#### 13.11.1.4 Graph

Figure 13.59: Residuals graph of the macro “calibrationMinimisationFlowrate1D.py”

### 13.11.2 Macro “calibrationMinimisationFlowrate2DVizir.py”

#### 13.11.2.1 Objective

The goal here is to calibrate the parameters 𝐻𝑢and 𝐻𝑙within the flowrateCalib2D model (a two-dimensional version
of the flowrate model), while varying only two inputs (𝑟𝜔and 𝐿). The remaining variables are fixed to the following
values: 𝑟= 25050, 𝑇𝑢= 89335, 𝑇𝑙= 89.55, 𝐾𝜔= 10950. The context of this example has already been presented
in Use-case for this chapter, including the model (implemented here as a C++ function) and the initial lines defining the
TDataServer objects.
In addition to what has been presented in Macro “calibrationMinimisationFlowrate1D.py”, this macro introduces two new
elements:
• the use of Vizir instead of a simpler TNloptSolver-inheriting instance;
• the discussion of problem identifiability, as introduced in [Bla17].

#### 13.11.2.2 Macro Uranie

```python
"""
Example of calibration through minimisation with Vizir in Flowrate 2D
"""
from URANIE import DataServer, Relauncher, Reoptimizer, Calibration
```

<!-- page 439 (PDF 446) -->
```python
import ROOT
# Load the function flowrateCalib2DVizir
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Input reference file
ExpData = "Ex2DoE_n100_sd1.75.dat"
# define the reference
tdsRef = DataServer.TDataServer("tdsRef", "doe_exp_Re_Pr")
tdsRef.fileDataRead(ExpData)
# define the parameters
tdsPar = DataServer.TDataServer("tdsPar", "tdsPar")
tdsPar.addAttribute(DataServer.TAttribute("hu", 1020.0, 1080.0))
tdsPar.addAttribute(DataServer.TAttribute("hl", 720.0, 780.0))
# Create the output attribute
out = DataServer.TAttribute("out")
# Create interface to assessors
Model = Relauncher.TCIntEval("flowrateCalib2D")
Model.addInput(tdsPar.getAttribute("hu"))
Model.addInput(tdsPar.getAttribute("hl"))
Model.addInput(tdsRef.getAttribute("rw"))
Model.addInput(tdsRef.getAttribute("l"))
Model.addOutput(out)
# Set the runner
runner = Relauncher.TSequentialRun(Model)
# Set the calibration object
cal = Calibration.TMinimisation(tdsPar, runner, 1)
cal.setDistance("relativeLS", tdsRef, "rw:l", "Qexp")
# Set optimisaiton properties
solv = Reoptimizer.TVizirGenetic()
solv.setSize(24, 15000, 100)
cal.setOptimProperties(solv)
# cal.getOptimMaster().setTolerance(1e-6)
cal.estimateParameters()
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
# Draw the box plot of parameters
canPar = ROOT.TCanvas("CanPar", "CanPar", 1200, 800)
tdsPar.getTuple().SetMarkerStyle(20)
tdsPar.getTuple().SetMarkerSize(0.8)
tdsPar.Draw("hu:hl")
```

<!-- page 440 (PDF 447) -->
```python
# Look at the correlation and statistic
tdsPar.computeStatistic("hu:hl")
corr = tdsPar.computeCorrelationMatrix("hu:hl")
corr.Print()
print("hl is %3.8g +- %3.8g " % (tdsPar.getAttribute("hl").getMean(),
                                 tdsPar.getAttribute("hl").getStd()))
print("hu is %3.8g +- %3.8g " % (tdsPar.getAttribute("hu").getMean(),
                                 tdsPar.getAttribute("hu").getStd()))
```

Much of this code has already been covered in the previous section Macro “calibrationMinimisationFlowrate1D.py” (up to
the sequential run). The main difference here is that the input parameter is now defined as a TAttribute with boundaries
specifying the space in which the algorithm will search.

```python
tdsPar.addAttribute(DataServer.TAttribute("hu", 1020.0, 1080.0))
tdsPar.addAttribute(DataServer.TAttribute("hl", 720.0, 780.0))
```

The model is defined (from a TCIntEval instance with the three input variables discussed above, in the correct order)
along with the computation distribution method (sequential).

```python
# Create interface to assessors
Model = Relauncher.TCIntEval("flowrateCalib2D")
Model.addInput(tdsPar.getAttribute("hu"))
Model.addInput(tdsPar.getAttribute("hl"))
Model.addInput(tdsRef.getAttribute("rw"))
Model.addInput(tdsRef.getAttribute("l"))
Model.addOutput(out)
# Set the runner
runner = Relauncher.TSequentialRun(Model)
```

Once this setup is complete, the calibration object (TMinimisation) is created. As explained in Recommended distance
and likelihood functions, construction method, the first step is to define the distance function (here the relative least squares
distance) using setDistance. This method also specifies the TDataServer containing the reference data, the names
of the reference inputs, and the reference variable against which the model output is compared. Finally, the optimisation
algorithm is defined by creating an instance of TVizirGenetic, and the parameters are then estimated.

```python
# Set the calibration object
cal = Calibration.TMinimisation(tdsPar, runner, 1)
cal.setDistance("relativeLS", tdsRef, "rw:l", "Qexp")
# Set optimisaiton properties
solv = Reoptimizer.TVizirGenetic()
solv.setSize(24, 15000, 100)
cal.setOptimProperties(solv)
# cal.getOptimMaster().setTolerance(1e-6)
cal.estimateParameters()
```

The final part demonstrates how to display the results. Since this method produces a point estimate, only a
single value is obtained, which is always shown on the screen, as illustrated in Console. Another important aspect is to
examine the residuals, as discussed in [Bla17]. This is illustrated in Figure 13.60, which shows the residuals of the a
posteriori estimates, typically following a normal distribution. Finally, the parameter graph (Figure 13.61) reveals a wide
variety of possible solutions. This highlights a problem of identifiability, since infinitely many parameter combinations

<!-- page 441 (PDF 448) -->
can lead to the same results, as further confirmed by the correlation matrix shown in Console.

```python
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
# Draw the box plot of parameters
canPar = ROOT.TCanvas("CanPar", "CanPar", 1200, 800)
tdsPar.getTuple().SetMarkerStyle(20)
tdsPar.getTuple().SetMarkerSize(0.8)
tdsPar.Draw("hu:hl")
# Look at the correlation and statistic
tdsPar.computeStatistic("hu:hl")
corr = tdsPar.computeCorrelationMatrix("hu:hl")
corr.Print()
print("hl is %3.8g +- %3.8g " % (tdsPar.getAttribute("hl").getMean(),
                                 tdsPar.getAttribute("hl").getStd()))
print("hu is %3.8g +- %3.8g " % (tdsPar.getAttribute("hu").getMean(),
                                 tdsPar.getAttribute("hu").getStd()))
```

####  13.11.2.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
first 100
Genetic
  Generation : 1, rang max 23
        Nb d'evaluation : 100, taille de la Z.P. :
  Generation : 2, rang max 23
        Nb d'evaluation : 465, taille de la Z.P. :
  Generation : 3, rang max 8
        Nb d'evaluation : 963, taille de la Z.P. :
  Generation : 4, rang max 0
        Nb d'evaluation : 1617, taille de la Z.P. :
Genetic
         converge 1617
************************************************************************************
*
     Row
           * tdsPar__n *
                             hu.hu *
                                         hl.hl * agreement * rgpareto. * generatio *
************************************************************************************
*
         0 *
                     0 * 1038.1302 * 738.13383 * 0.3639076 *
                                                                     0 *
                                                                                 3 *
*
         1 *
                     1 *
                              1080 *
                                           780 * 0.3639083 *
                                                                     0 *
                                                                                 3 *
*
         2 *
                     2 * 1040.7058 * 740.77116 * 0.3639018 *
                                                                     0 *
                                                                                 3 *
```

<!-- page 442 (PDF 449) -->
```python
*
         3 *
                     3 * 1079.9545 *
                                           780 * 0.3639024 *
                                                                     0 *
                                                                                 3 *
*
         4 *
                     4 * 1040.7058 * 740.77116 * 0.3639018 *
                                                                     0 *
                                                                                 1 *
*
         5 *
                     5 * 1038.6638 * 738.70819 * 0.3639025 *
                                                                     0 *
                                                                                 3 *
*
         6 *
                     6 * 1040.7058 * 740.77116 * 0.3639018 *
                                                                     0 *
                                                                                 3 *
*
         7 *
                     7 * 1036.9776 * 736.98122 * 0.3639076 *
                                                                     0 *
                                                                                 3 *
*
         8 *
                     8 * 1036.9776 * 736.98122 * 0.3639076 *
                                                                     0 *
                                                                                 3 *
*
         9 *
                     9 * 1038.6638 * 738.70819 * 0.3639025 *
                                                                     0 *
                                                                                 3 *
*
        10 *
                    10 * 1036.9776 * 736.98122 * 0.3639076 *
                                                                     0 *
                                                                                 2 *
*
        11 *
                    11 *
                              1080 *
                                           780 * 0.3639083 *
                                                                     0 *
                                                                                 3 *
*
        12 *
                    12 * 1036.9776 * 736.98122 * 0.3639076 *
                                                                     0 *
                                                                                 3 *
*
        13 *
                    13 * 1040.7058 * 740.77116 * 0.3639018 *
                                                                     0 *
                                                                                 2 *
*
        14 *
                    14 *
                              1080 *
                                           780 * 0.3639083 *
                                                                     0 *
                                                                                 3 *
*
        15 *
                    15 *
                              1080 *
                                           780 * 0.3639083 *
                                                                     0 *
                                                                                 3 *
*
        16 *
                    16 * 1038.6638 * 738.70819 * 0.3639025 *
                                                                     0 *
                                                                                 3 *
*
        17 *
                    17 * 1040.7058 * 740.77116 * 0.3639018 *
                                                                     0 *
                                                                                 3 *
*
        18 *
                    18 *
                              1080 *
                                           780 * 0.3639083 *
                                                                     0 *
                                                                                 3 *
*
        19 *
                    19 * 1036.9776 * 736.98122 * 0.3639076 *
                                                                     0 *
                                                                                 3 *
*
        20 *
                    20 * 1036.9042 * 736.96108 * 0.3639019 *
                                                                     0 *
                                                                                 3 *
*
        21 *
                    21 * 1038.6638 * 738.70819 * 0.3639025 *
                                                                     0 *
                                                                                 3 *
*
        22 *
                    22 *
                              1080 *
                                           780 * 0.3639083 *
                                                                     0 *
                                                                                 3 *
*
        23 *
                    23 *
                              1080 *
                                           780 * 0.3639083 *
                                                                     0 *
                                                                                 3 *
************************************************************************************
2x2 matrix is as follows
     |
                 |
                             |
-------------------------------
   0 |
   1 |
hl is 752.4454 +- 19.946252
hu is 1052.4192 +- 19.959796
```

<!-- page 443 (PDF 450) -->
#### 13.11.2.4 Graphs

Figure 13.60: Residuals graph of the macro “calibrationMinimisationFlowrate2DVizir.py”

<!-- page 444 (PDF 451) -->
Figure 13.61: Parameter graph of the macro “calibrationMinimisationFlowrate2DVizir.py”

### 13.11.3 Macro “calibrationLinBayesFlowrate1D.py”

#### 13.11.3.1 Objective

The goal here is to calibrate the parameter 𝐻𝑙within the flowrate model, while varying only two inputs (𝑟𝜔and 𝐿). The
remaining variables are fixed to the following values: 𝑟= 25050, 𝑇𝑢= 89335, 𝑇𝑙= 89.55, 𝐻𝑢= 1050, 𝐾𝜔= 10950.
The context of this example has already been presented in Use-case for this chapter, including the model (implemented
here as a C++ function) and the initial lines defining the TDataServer objects. This macro demonstrates how to apply
a linear Bayesian estimation technique using a Relauncher-based architecture.

#### 13.11.3.2 Macro Uranie

```python
"""
Example of linear bayesian calibration with simple 1D flowrate model
"""
from URANIE import DataServer, Relauncher, Calibration
import ROOT
# Load the function flowrateCalib1D
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Input reference file
ExpData = "Ex2DoE_n100_sd1.75.dat"
```

<!-- page 445 (PDF 452) -->
```python
# define the reference
tdsRef = DataServer.TDataServer("tdsRef", "doe_exp_Re_Pr")
tdsRef.fileDataRead(ExpData)
# define the parameters
tdsPar = DataServer.TDataServer("tdsPar", "tdsPar")
tdsPar.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 760.0))
# Create the output attribute
out = DataServer.TAttribute("out")
# Create interface to assessors
Reg = Relauncher.TCIntEval("flowrateModelnoH")
Reg.addInput(tdsRef.getAttribute("rw"))
Reg.addInput(tdsRef.getAttribute("l"))
Reg.addOutput(DataServer.TAttribute("H"))
runnoH = Relauncher.TSequentialRun(Reg)
runnoH.startSlave()
if runnoH.onMaster():
    launch = Relauncher.TLauncher2(tdsRef, runnoH)
    launch.solverLoop()
    runnoH.stopSlave()
# Create interface to assessors
Model = Relauncher.TCIntEval("flowrateCalib1D")
Model.addInput(tdsPar.getAttribute("hl"))
Model.addInput(tdsRef.getAttribute("rw"))
Model.addInput(tdsRef.getAttribute("l"))
Model.addOutput(out)
# Set the runner
runner = Relauncher.TSequentialRun(Model)
# Set the covariance matrix of the input reference
sd = tdsRef.getValue("sd_eps", 0)
mat = ROOT.TMatrixD(100, 100)
for ival in range(tdsRef.getNPatterns()):
    mat[ival][ival] = (sd*sd)
# Set the calibration object
cal = Calibration.TLinearBayesian(tdsPar, runner, 1, "")
cal.setLikelihood("gauss_lin", tdsRef, "rw:l", "Qexp")
cal.setObservationCovarianceMatrix(mat)
cal.setRegressorName("H")
cal.setParameterTransformationFunction(ROOT.transf)
cal.estimateParameters()
# Draw the parameters
canPar = ROOT.TCanvas("CanPar", "CanPar", 1200, 800)
padPar = ROOT.TPad("padPar", "padPar", 0, 0.03, 1, 1)
padPar.Draw()
padPar.cd()
```

<!-- page 446 (PDF 453) -->
```python
cal.drawParameters("Parameters", "*", "nonewcanvas,transformed")
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
```

Much of this code has already been covered in the previous section Macro “calibrationMinimisationFlowrate1D.py” (up
to the sequential run). The main difference here is that the input parameter is now defined as a TStochasticDistribution
, representing the a priori chosen distribution. In this example, it can be either a TNormalDistribution or a
TUniformDistribution (see [Bla17]), with the latter being selected here:

```python
tdsPar.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 760.0))
```

Another difference from the previous example is that the method must be slightly adapted to obtain values for the regressor.
As discussed in [Bla17], linear Bayesian estimation can be applied when the model is approximately linear. This requires
linearising the flowrate function, as demonstrated here:
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
Here, the regressor can be expressed as
𝐻= (2𝜋𝑇𝑢)
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
From this expression, it is clear that we will be calibrating a newly defined parameter 𝜃= (𝐻𝑢−𝐻𝑙), which must later
be converted back into the parameter of interest. To obtain the regressor estimation, we simply use another C++ function,
flowrateModelnoH, together with the standard Relauncher approach:

```python
# Create interface to assessors
Reg = Relauncher.TCIntEval("flowrateModelnoH")
Reg.addInput(tdsRef.getAttribute("rw"))
Reg.addInput(tdsRef.getAttribute("l"))
Reg.addOutput(DataServer.TAttribute("H"))
runnoH = Relauncher.TSequentialRun(Reg)
runnoH.startSlave()
if runnoH.onMaster():
    launch = Relauncher.TLauncher2(tdsRef, runnoH)
    launch.solverLoop()
    runnoH.stopSlave()
```

This method also requires the input covariance matrix. The provided dataset (Ex2DoE_n100_sd1.75.dat) contains an
estimate of the uncertainty affecting the reference measurements. Since this uncertainty is constant across all samples, the
input covariance matrix is diagonal, with each diagonal element equal to the square of the standard deviation, as illustrated
below:

```python
# Set the covariance matrix of the input reference
sd = tdsRef.getValue("sd_eps", 0)
mat = ROOT.TMatrixD(100, 100)
for ival in range(tdsRef.getNPatterns()):
    mat[ival][ival] = (sd*sd)
```

<!-- page 447 (PDF 454) -->
The model is defined (from a TCIntEval instance with the three input variables discussed above, in the correct order)
along with the computation distribution method (sequential).
The calibration object is then created using a Mahalanobis distance function, which is used here for illustrative purposes
(see Analytical linear Bayesian estimation for more details). The three key steps are:
• Providing the input covariance matrix via the setObservationCovarianceMatrix method;
• Specifying the regressors’ names using setRegressorName;
• Defining the parameter transformation function (optional) with setParameterTransformationFunction.
The final step is more involved: since we are calibrating 𝜃, we need to recover the corresponding parameter value at the
end. This is achieved by providing a C++ function that transforms the parameter estimated from the linearisation back
into the parameter of interest. For illustration, this is implemented in UserFunctions.C via the transf function,
shown below:

```python
void transf(double *x, double *res)
{
    res[0] = 1050 - x[0];
                           // simply H_l = \theta - H_u
}
```

The complete block of code discussed in this section is as follows:

```python
# Set the calibration object
cal = Calibration.TLinearBayesian(tdsPar, runner, 1, "")
cal.setLikelihood("gauss_lin", tdsRef, "rw:l", "Qexp")
cal.setObservationCovarianceMatrix(mat)
cal.setRegressorName("H")
cal.setParameterTransformationFunction(ROOT.transf)
cal.estimateParameters()
```

The final part demonstrates how to display the results. Since this method produces normal a posteriori distributions, they
are represented by a vector of means and a covariance structure, both easily accessible. The means are displayed on screen,
as illustrated in Console. Two additional pieces of a posteriori information are presented as plots: the residuals (Figure
13.62), which show the expected normal distribution behavior, as discussed in [Bla17] and the posterior distribution
(Figure 13.63).

```python
# Draw the parameters
canPar = ROOT.TCanvas("CanPar", "CanPar", 1200, 800)
padPar = ROOT.TPad("padPar", "padPar", 0, 0.03, 1, 1)
padPar.Draw()
padPar.cd()
cal.drawParameters("Parameters", "*", "nonewcanvas,transformed")
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
```

<!-- page 448 (PDF 455) -->
#### 13.11.3.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
***
     TLinearBayesian::computeParameters(); Transformed parameters estimated are
1x1 matrix is as follows
     |
                 |
------------------
   0 |
            749.7
```

####  13.11.3.4 Graphs

Figure 13.62: Residuals graph of the macro “calibrationLinBayesFlowrate1D.py”

<!-- page 449 (PDF 456) -->
Figure 13.63: Parameter graph of the macro “calibrationLinBayesFlowrate1D.py”

### 13.11.4 Macro “calibrationRejectionABCFlowrate1D.py”

#### 13.11.4.1 Objective

The goal here is to calibrate the parameter 𝐻𝑙within the flowrate model, while varying only two inputs (𝑟𝜔and 𝐿). The
remaining variables are fixed to the following values: 𝑟= 25050, 𝑇𝑢= 89335, 𝑇𝑙= 89.55, 𝐻𝑢= 1050, 𝐾𝜔= 10950.
The context of this example has already been presented in Use-case for this chapter, including the model (implemented
here as a C++ function) and the initial lines defining the TDataServer objects. This macro demonstrates how to apply
a rejection ABC method using a Relauncher-based architecture.

#### 13.11.4.2 Macro Uranie

```python
"""
Example of calibration using Rejection ABC approach on flowrate 1D
"""
from URANIE import DataServer, Calibration, Relauncher
import ROOT
# Load the function flowrateCalib1D
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Input reference file
ExpData = "Ex2DoE_n100_sd1.75.dat"
```

<!-- page 450 (PDF 457) -->
```python
# define the reference
tdsRef = DataServer.TDataServer("tdsRef", "doe_exp_Re_Pr")
tdsRef.fileDataRead(ExpData)
# define the parameters
tdsPar = DataServer.TDataServer("tdsPar", "tdsPar")
tdsPar.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 760.0))
# Create the output attribute
out = DataServer.TAttribute("out")
# Create interface to assessors
Model = Relauncher.TCIntEval("flowrateCalib1D")
Model.addInput(tdsPar.getAttribute("hl"))
Model.addInput(tdsRef.getAttribute("rw"))
Model.addInput(tdsRef.getAttribute("l"))
Model.addOutput(out)
# Set the runner
runner = Relauncher.TSequentialRun(Model)
# Set the calibration object
nABC = 100
eps = 0.05
cal = Calibration.TRejectionABC(tdsPar, runner, nABC, "")
cal.setDistance("LS", tdsRef, "rw:l", "Qexp")
cal.setGaussianNoise("sd_eps")
cal.setPercentile(eps)
cal.estimateParameters()
# Draw the parameters
canPar = ROOT.TCanvas("CanPar", "CanPar", 1200, 800)
padPar = ROOT.TPad("padPar", "padPar", 0, 0.03, 1, 1)
padPar.Draw()
padPar.cd()
cal.drawParameters("Parameters", "*", "nonewcanvas")
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
# Compute statistics
tdsPar.computeStatistic()
print("The mean of hl is %3.8g" % (tdsPar.getAttribute("hl").getMean()))
print("The std of hl is %3.8g" % (tdsPar.getAttribute("hl").getStd()))
```

Much of this code has already been covered in the previous section Macro “calibrationMinimisationFlowrate1D.py” (up
to the sequential run). The main difference here is that the input parameter is now defined as a TStochasticDistribution
, representing the a priori chosen distribution.

<!-- page 451 (PDF 458) -->
```python
tdsPar.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 760.0))
```

The model is defined (from a TCIntEval instance with the three input variables discussed above, in the correct order)
along with the computation distribution method (sequential).
The calibration object is then created by specifying both the number of elements in the final sample (nABC = 100)
and the percentile of events retained (eps

```python
=
```

0.05, meaning that 2000 locations will be tested). Since the code is
deterministic, uncertainty is introduced by adding random Gaussian noise. The standard deviation of this noise is defined
on an event-by-event basis using a variable from the observation dataserver. Finally, the distance function is specified,
and the estimation process is performed.

```python
# Set the calibration object
nABC = 100
eps = 0.05
cal = Calibration.TRejectionABC(tdsPar, runner, nABC, "")
cal.setDistance("LS", tdsRef, "rw:l", "Qexp")
cal.setGaussianNoise("sd_eps")
cal.setPercentile(eps)
cal.estimateParameters()
```

The final part demonstrates how to display the results. Since this method produces samples of the a posteriori distributions,
basic statistical information are directly displayed on screen, as shown in Console. Two additional pieces of a posteriori
information are presented as plots: the residuals (Figure 13.64), which show the expected normal distribution behavior,
as discussed in [Bla17] and the posterior distribution (Figure 13.65).

```python
# Draw the parameters
canPar = ROOT.TCanvas("CanPar", "CanPar", 1200, 800)
padPar = ROOT.TPad("padPar", "padPar", 0, 0.03, 1, 1)
padPar.Draw()
padPar.cd()
cal.drawParameters("Parameters", "*", "nonewcanvas")
# Draw the residuals
canRes = ROOT.TCanvas("CanRes", "CanRes", 1200, 800)
padRes = ROOT.TPad("padRes", "padRes", 0, 0.03, 1, 1)
padRes.Draw()
padRes.cd()
cal.drawResiduals("Residuals", "*", "", "nonewcanvas")
# Compute statistics
tdsPar.computeStatistic()
print("The mean of hl is %3.8g" % (tdsPar.getAttribute("hl").getMean()))
print("The std of hl is %3.8g" % (tdsPar.getAttribute("hl").getStd()))
```

####  13.11.4.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
 <URANIE::INFO>
 <URANIE::INFO> *** URANIE INFORMATION ***
```

<!-- page 452 (PDF 459) -->
```python
<URANIE::INFO> *** File[${SOURCEDIR}/meTIER/calibration/souRCE/
```

˓→TDistanceLikelihoodFunction.cxx] Line[601]

```python
<URANIE::INFO> TDistanceLikelihoodFunction::setGaussianRandomNoise: gaussian random␣
```

˓→noise(s) is added using information in [sd_eps] to modify the output variable(s)␣
˓→[out].

```python
<URANIE::INFO> *** END of URANIE INFORMATION ***
<URANIE::INFO>
<URANIE::INFO>
<URANIE::INFO> *** URANIE INFORMATION ***
<URANIE::INFO> *** File[${SOURCEDIR}/meTIER/calibration/souRCE/TRejectionABC.cxx]␣
```

˓→Line[118]

```python
<URANIE::INFO> TRejectionABC::computeParameters:: 2000 evaluations will be performed␣
```

˓→!

```python
 <URANIE::INFO> *** END of URANIE INFORMATION ***
 <URANIE::INFO>
A posteriori mean coordinates are : (749.926)
The mean of hl is 749.92609
The std of hl is 1.9704229
```

####  13.11.4.4 Graphs

Figure 13.64: Residuals graph of the macro “calibrationRejectionABCFlowrate1D.py”
