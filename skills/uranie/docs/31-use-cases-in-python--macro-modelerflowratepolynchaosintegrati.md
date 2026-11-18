# Use-cases in Python — Macros Modeler — Macro “modelerFlowratePolynChaosIntegration.py” … Macro “modelerTestKriging.py”
<!-- source PDF pages 357-371 -->

<!-- page 350 (PDF 357) -->
### 13.7.8 Macro “modelerFlowratePolynChaosIntegration.py”

#### 13.7.8.1 Objective

The objective of this macro is to build a polynomial chaos expansion in order to get a surrogate model along with a
global sensitivity interpretation for the flowrate function, whose purpose and behaviour have been already introduced
in Presentation of the problem. The method used here is the regression one, as discussed below.

#### 13.7.8.2 Macro Uranie

```python
"""
Example of Chaos polynomial expansion on flowrate
"""
from URANIE import DataServer, Launcher, Modeler
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
tds = DataServer.TDataServer("tdsflowreate", "DataBase flowreate")
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
# Define of TNisp object
nisp = Modeler.TNisp(tds)
nisp.generateSample("Petras", 5)
                                  # State that there is a sample ...
# Compute the output variable
tlf = Launcher.TLauncherFunction(tds, "flowrateModel", "*", "ymod")
tlf.setDrawProgressBar(False)
tlf.run()
# build a chaos polynomial
pc = Modeler.TPolynomialChaos(tds, nisp)
# compute the pc coefficients using the "Integration" method
degree = 4
pc.setDegree(degree)
pc.computeChaosExpansion("Integration")
# Uncertainty and sensitivity analysis
print("Variable ymod ================")
print("Mean
                = "+str(pc.getMean("ymod")))
print("Variance = "+str(pc.getVariance("ymod")))
print("First Order Indices ================")
print("Indice First Order[1] = "+str(pc.getIndexFirstOrder(0, 0)))
print("Indice First Order[2] = "+str(pc.getIndexFirstOrder(1, 0)))
print("Indice First Order[3] = "+str(pc.getIndexFirstOrder(2, 0)))
```

<!-- page 351 (PDF 358) -->
```python
print("Indice First Order[4] = "+str(pc.getIndexFirstOrder(3, 0)))
print("Indice First Order[5] = "+str(pc.getIndexFirstOrder(4, 0)))
print("Indice First Order[6] = "+str(pc.getIndexFirstOrder(5, 0)))
print("Indice First Order[7] = "+str(pc.getIndexFirstOrder(6, 0)))
print("Indice First Order[8] = "+str(pc.getIndexFirstOrder(7, 0)))
print("Total Order Indices ================")
print("Indice Total Order[1] = "+str(pc.getIndexTotalOrder("rw", "ymod")))
print("Indice Total Order[2] = "+str(pc.getIndexTotalOrder("r", "ymod")))
print("Indice Total Order[3] = "+str(pc.getIndexTotalOrder("tu", "ymod")))
print("Indice Total Order[4] = "+str(pc.getIndexTotalOrder("tl", "ymod")))
print("Indice Total Order[5] = "+str(pc.getIndexTotalOrder("hu", "ymod")))
print("Indice Total Order[6] = "+str(pc.getIndexTotalOrder("hl", "ymod")))
print("Indice Total Order[7] = "+str(pc.getIndexTotalOrder("l", "ymod")))
print("Indice Total Order[8] = "+str(pc.getIndexTotalOrder("kw", "ymod")))
# Dump main factors up to a certain threshold
seuil = 0.99
print("Ordered functionnal ANOVA")
pc.getAnovaOrdered(seuil, 0)
print("Number of experiments = "+str(tds.getNPatterns()))
# save the pv in a program (C langage)
pc.exportFunction("NispFlowrate", "NispFlowrate")
```

The first part is just creating a TDataServer and providing the attributes needed to define the problem. From there,
a TNisp object is created, providing the dataserver that specifies the inputs. This class is used to generate the sample
(Petras being a design-of-experiments dedicated to integration problem).

```python
nisp = Modeler.TNisp(tds)
nisp.generateSample("Petras", 5)
                                  # State that there is a sample ...
```

The function is launched through a TLauncherFunction instance in order to get the output values that will be needed
to train the surrogate model.

```python
tlf = Launcher.TLauncherFunction(tds, "flowrateModel", "*", "ymod")
tlf.run()
```

Finally, a TPolynomialChaos instance is created and the computation of the coefficients is performed by requesting a
truncature on the resulting degree of the polynomial expansion (set to 4) and the use of a regression method.

```python
pc = Modeler.TPolynomialChaos(tds, nisp)
# compute the pc coefficients using the "Integration" method
degree = 4
pc.setDegree(degree)
pc.computeChaosExpansion("Integration")
```

The rest of the code is showing how to access the resulting sensitivity indices either one-by-one, or ordered up to a chosen
threshold of the output variance.

<!-- page 352 (PDF 359) -->
#### 13.7.8.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
Variable ymod ================
Mean
         = 77.65109941166783
Variance = 2078.9066967013787
First Order Indices ================
Indice First Order[1] = 0.8289221400657457
Indice First Order[2] = 1.0447660450188066e-06
Indice First Order[3] = 8.946920854938701e-12
Indice First Order[4] = 5.302986799455716e-06
Indice First Order[5] = 0.041385187477657376
Indice First Order[6] = 0.04138518747765731
Indice First Order[7] = 0.03934189598916908
Indice First Order[8] = 0.009521571788843197
Total Order Indices ================
Indice Total Order[1] = 0.8668339836271369
Indice Total Order[2] = 2.1617808194716235e-06
Indice Total Order[3] = 2.2829619916786966e-09
Indice Total Order[4] = 1.0738582524791707e-05
Indice Total Order[5] = 0.054109548638212865
Indice Total Order[6] = 0.05410954863821284
Indice Total Order[7] = 0.0520766679067344
Indice Total Order[8] = 0.012730598799757903
```

###  13.7.9 Macro “modelerbuildSimpleGP.py”

####  13.7.9.1 Objective

This macro is the one described in Example: construction of a simple Kriging model, that creates a simple gaussian process,
whose training (utf_4D_train.dat) and testing (utf_4D_test.dat) database can both be found in the document
folder of the Uranie installation (${URANIESYS}/share/uranie/docUMENTS).

#### 13.7.9.2 Macro Uranie

```python
"""
Example of Gaussian Process building
"""
from URANIE import DataServer, Modeler
# Load observations
tdsObs = DataServer.TDataServer("tdsObs", "observations")
tdsObs.fileDataRead("utf_4D_train.dat")
# Construct the GPBuilder
gpb = Modeler.TGPBuilder(tdsObs,
                                         # observations data
                         "x1:x2:x3:x4",
                                         # list of input variables
                         "y",
                                         # output variable
                         "matern3/2")
                                         # name of the correlation function
```

<!-- page 353 (PDF 360) -->
```python
# Search for the optimal hyper-parameters
gpb.findOptimalParameters("ML",
                                         # optimisation criterion
                          100,
                                         # screening design size
                          "neldermead",
                                         # optimisation algorithm
                          500)
                                         # max. number of optim iterations
# Construct the kriging model
krig = gpb.buildGP()
# Display model information
krig.printLog()
```

####  13.7.9.3 Console

This is the result of the last command:

```python
.*******************************
** TKriging::printLog[]
*******************************
 Input Variables:
                       x1:x2:x3:x4
 Output Variable:
                       y
 Deterministic trend:
 Correlation function: URANIE::Modeler::TMatern32CorrFunction
 Correlation length:
                       normalised
                                    (not normalised)
                       1.6181e+00 (1.6172e+00 )
                       1.4372e+00 (1.4370e+00 )
                       1.5026e+00 (1.5009e+00 )
                       6.7884e+00 (6.7944e+00 )
 Variance of the gaussian process:
                                        70.8755
 RMSE (by Leave One Out):
                                        0.499108
 Q2:
                                        0.849843
*******************************
```

###  13.7.10 Macro “modelerbuildGPInitPoint.py”

####  13.7.10.1 Objective

This macro is the one described in Choice of the initial point of the optimisation, that creates a gaussian process, whose
training (utf_4D_train.dat) and testing (utf_4D_test.dat) database can both be found in the document folder
of the Uranie installation (${URANIESYS}/share/uranie/docUMENTS), and whose starting point, in the parameter
space, is specified.

#### 13.7.10.2 Macro Uranie

```python
"""
Example of Gaussian Process building with initial point set
"""
import numpy as np
from URANIE import DataServer, Modeler
```

<!-- page 354 (PDF 361) -->
```python
# Load observations
tdsObs = DataServer.TDataServer("tdsObs", "observations")
tdsObs.fileDataRead("utf_4D_train.dat")
# Construct the GPBuilder
gpb = Modeler.TGPBuilder(tdsObs, "x1:x2:x3:x4", "y", "matern3/2")
# Set the correlation function parameters
params = np.array([1.0, 0.25, 0.01, 0.3])
gpb.getCorrFunction().setParameters(params)
# Find the optimal parameters
gpb.findOptimalParameters("ML",
                                         # optimisation criterion
                          0,
                                         # screening size MUST be equal to 0
                          "neldermead",
                                         # optimisation algorithm
                          500,
                                         # max. number of optim iterations
                          False)
                                         # Don't reset parameters of GP builder
# Create the kriging model
krig = gpb.buildGP()
# Display model information
krig.printLog()
```

####  13.7.10.3 Console

This is the result of the last command:

```python
*******************************
** TKriging::printLog[]
*******************************
 Input Variables:
                       x1:x2:x3:x4
 Output Variable:
                       y
 Deterministic trend:
 Correlation function: URANIE::Modeler::TMatern32CorrFunction
 Correlation length:
                       normalised
                                    (not normalised)
                       1.6182e+00 (1.6173e+00 )
                       1.4373e+00 (1.4371e+00 )
                       1.5027e+00 (1.5011e+00 )
                       6.7895e+00 (6.7955e+00 )
 Variance of the gaussian process:
                                        70.8914
 RMSE (by Leave One Out):
                                        0.49911
 Q2:
                                        0.849842
*******************************
```

###  13.7.11 Macro “modelerbuildGPWithAPriori.py”

####  13.7.11.1 Objective

This macro is the one described in Deterministic trend and bayesian prior, that creates a gaussian process with a specific
trend and an a priori knowledge on the mean and variance of the trend parameters.

<!-- page 355 (PDF 362) -->
#### 13.7.11.2 Macro Uranie

```python
"""
Example of Gaussian Process building with a priori knowledge
"""
import numpy as np
from URANIE import DataServer, Modeler
# Load observations
tdsObs = DataServer.TDataServer("tdsObs", "observations")
tdsObs.fileDataRead("utf_4D_train.dat")
# Construct the GPBuilder
gpb = Modeler.TGPBuilder(tdsObs,
                                         # observations data
                         "x1:x2:x3:x4",
                                         # list of input variables
                         "y",
                                         # output variable
                         "matern3/2",
                                         # name of the correlation function
                         "linear")
                                         # trend defined by a keyword
# Bayesian study
meanPrior = np.array([0.0, 0.0, -1.0, 0.0, -0.1])
covPrior = np.array([1e-4, 0.0, 0.0, 0.0, 0.0,
                     0.0, 1e-4, 0.0, 0.0, 0.0,
                     0.0, 0.0, 1e-4, 0.0, 0.0,
                     0.0, 0.0, 0.0, 1e-4, 0.0,
                     0.0, 0.0, 0.0, 0.0, 1e-4])
gpb.setPriorData(meanPrior, covPrior)
# Search for the optimal hyper-parameters
gpb.findOptimalParameters("ReML",
                                         # optimisation criterion
                          100,
                                         # screening design size
                          "neldermead",
                                         # optimisation algorithm
                          500)
                                         # max. number of optim iterations
# Construct the kriging model
krig = gpb.buildGP()
# Display model information
krig.printLog()
```

####  13.7.11.3 Console

This is the result of the last command:

```python
.*******************************
** TKriging::printLog[]
*******************************
 Input Variables:
                       x1:x2:x3:x4
 Output Variable:
                       y
 Deterministic trend:
                       linear
 Trend parameters (5): [3.06586494e-05; 1.64887174e-05; -9.99986787e-01; 1.51959859e-
```

˓→05; -9.99877606e-02 ]

```python
Correlation function: URANIE::Modeler::TMatern32CorrFunction
```

<!-- page 356 (PDF 363) -->
```python
 Correlation length:
                       normalised
                                    (not normalised)
                       2.1450e+00 (2.1438e+00 )
                       1.9092e+00 (1.9090e+00 )
                       2.0062e+00 (2.0040e+00 )
                       8.4315e+00 (8.4390e+00 )
 Variance of the gaussian process:
                                        155.533
 RMSE (by Leave One Out):
                                        0.495448
 Q2:
                                        0.852037
*******************************
```

###  13.7.12 Macro “modelerbuildSimpleGPEstim.py”

####  13.7.12.1 Objective

This macro is the one described in Prediction of a new data set, one-by-one approach, to create and use a simple gaussian
process, whose training (utf_4D_train.dat) and testing (utf_4D_test.dat) database can both be found in the document
folder of the Uranie installation (${URANIESYS}/share/uranie/docUMENTS). It uses the simple one-by-one
approch described in the [Bla17] for completness.

#### 13.7.12.2 Macro Uranie

```python
"""
Example of Gaussian Process building with estimation on another dataset
"""
from URANIE import DataServer, Modeler, Relauncher
# Load observations
tdsObs = DataServer.TDataServer("tdsObs", "observations")
tdsObs.fileDataRead("utf_4D_train.dat")
# Construct the GPBuilder
gpb = Modeler.TGPBuilder(tdsObs,
                                         # observations data
                         "x1:x2:x3:x4",
                                         # list of input variables
                         "y",
                                         # output variable
                         "matern3/2")
                                         # name of the correlation function
# Search for the optimal hyper-parameters
gpb.findOptimalParameters("ML",
                                         # optimisation criterion
                          100,
                                         # screening design size
                          "neldermead",
                                         # optimisation algorithm
                          500)
                                         # max. number of optim iterations
# Construct the kriging model
krig = gpb.buildGP()
# Display model information
krig.printLog()
# Load the data to estimate
tdsEstim = DataServer.TDataServer("tdsEstim", "estimations")
tdsEstim.fileDataRead("utf_4D_test.dat")
```

<!-- page 357 (PDF 364) -->
```python
# Construction of the launcher
lanceur = Relauncher.TLauncher2(tdsEstim,
                                                  # data to estimate
                                krig,
                                                  # model used
                                "x1:x2:x3:x4",
                                                  # list of the input variables
                                "yEstim:vEstim")
                                                  # name of model's outputs
# Launch the estimations
lanceur.solverLoop()
# Display some results
tdsEstim.draw("yEstim:y")
```

####  13.7.12.3 Graph

Figure 13.43: Graph of the macro “modelerbuildSimpleGPEstim.py”

### 13.7.13 Macro “modelerbuildSimpleGPEstimWithCov.py”

#### 13.7.13.1 Objective

This macro is the one described in Prediction of a new data set, global approach, to create and use a simple gaussian
process, whose training (utf_4D_train.dat) and testing (utf_4D_test.dat) database can both be found in the
document folder of the Uranie installation (${URANIESYS}/share/uranie/docUMENTS). It uses the global approach,
computing the input covariance matrix and translating it to the prediction covariance matrix.

#### 13.7.13.2 Macro Uranie

```python
"""
Example of Gaussian Process building with estimation using full data (covariance)
"""
from URANIE import DataServer, Modeler
```

<!-- page 358 (PDF 365) -->
```python
import ROOT
# Load observations
tdsObs = DataServer.TDataServer("tdsObs", "observations")
tdsObs.fileDataRead("utf_4D_train.dat")
# Construct the GPBuilder
gpb = Modeler.TGPBuilder(tdsObs,
                                         # observations data
                         "x1:x2:x3:x4",
                                         # list of input variables
                         "y",
                                         # output variable
                         "matern1/2")
                                         # name of the correlation function
# Search for the optimal hyper-parameters
gpb.findOptimalParameters("ML",
                                         # optimisation criterion
                          100,
                                         # screening design size
                          "neldermead",
                                         # optimisation algorithm
                          500)
                                         # max. number of optim iterations
# Construct the kriging model
krig = gpb.buildGP()
# Display model information
krig.printLog()
# Load the data to estimate
tdsEstim = DataServer.TDataServer("tdsEstim", "estimations")
tdsEstim.fileDataRead("utf_4D_test.dat")
# Reducing DB to 1000 first event (leading to cov matrix of a million value)
nS = 1000
tdsEstim.exportData("utf_4D_test_red.dat", "", "tdsEstim__n__iter__<="+str(nS))
# Reload reduced sample
tdsEstim.fileDataRead("utf_4D_test_red.dat", False, True)
krig.estimateWithCov(tdsEstim,
                                       # data to estimate
                     "x1:x2:x3:x4",
                                       # list of the input variables
                     "yEstim:vEstim",
                                       # name given to the model's outputs
                     "y",
                                       # name of the true reference
                     "DummyOption")
                                       # options
cTwo = None
# Produce residuals plots if true information provided
if tdsEstim.isAttribute("_Residuals_"):
    cTwo = ROOT.TCanvas("c2", "c2", 1200, 800)
    cTwo.Divide(2, 1)
    cTwo.cd(1)
    # Usual residual considering uncorrated input points
    tdsEstim.Draw("_Residuals_")
    cTwo.cd(2)
    # Corrected residuals, taking full prediction covariance matrix
    tdsEstim.Draw("_uncorrResiduals_")
```

<!-- page 359 (PDF 366) -->
```python
# Retrieve all the prediction covariance coefficient
tdsEstim.getTuple().SetEstimate(nS*nS)
                                        # allocate the correct size
# Get a pointer to all values
tdsEstim.getTuple().Draw("_CovarianceMatrix_", "", "goff")
cov = tdsEstim.getTuple().GetV1()
# Put these in a matrix nicely created
Cov = ROOT.TMatrixD(nS, nS)
Cov.Use(0, nS-1, 0, nS-1, cov)
# Print it if size is reasonnable
if nS < 10:
    Cov.Print()
```

####  13.7.13.3 Graph

Figure 13.44: Graph of the macro “modelerbuildSimpleGPEstimWithCov.py”

### 13.7.14 Macro “modelerTestKriging.py”

#### 13.7.14.1 Objective

The idea is to provide a simple example of a kriging usage, and an how to, to produce plots in one dimension to represent
the results. This example is the one taken from [Bla17] that uses a very simple set of six points as training database:

<!-- page 360 (PDF 367) -->
```python
#TITLE: utf-1D-train.dat
#COLUMN_NAMES: x1|y
6.731290e-01 3.431918e-01
7.427596e-01 9.356860e-01
4.518467e-01 -3.499771e-01
2.215734e-02 2.400531e+00
9.915253e-01 2.412209e+00
1.815769e-01 1.589435e+00
```

The aim will be to get a kriging model that describes this dataset and to check its consistency over a certain number of
points (here 100 points) which will be the testing database:

```python
#TITLE: utf-1D-test.dat
#COLUMN_NAMES: x1|y
5.469435e-02 2.331524e+00
3.803054e-01 -3.277316e-02
7.047152e-01 6.030177e-01
2.360045e-02 2.398694e+00
9.271965e-01 2.268814e+00
7.868263e-01 1.324318e+00
7.791920e-01 1.257942e+00
6.107965e-01 -8.514510e-02
1.362316e-01 1.926999e+00
5.709913e-01 -2.758435e-01
8.738804e-01 1.992941e+00
2.251602e-01 1.219826e+00
9.175259e-01 2.228545e+00
5.128368e-01 -4.096161e-01
7.692913e-01 1.170999e+00
7.394406e-01 9.062407e-01
5.364506e-01 -3.772856e-01
1.861864e-01 1.551961e+00
7.573444e-01 1.065237e+00
1.005755e-01 2.141109e+00
9.114685e-01 2.201001e+00
3.628465e-01 7.920271e-02
2.383583e-01 1.103353e+00
7.468092e-01 9.716492e-01
3.126209e-01 4.578112e-01
8.034716e-01 1.466248e+00
6.730402e-01 3.424931e-01
8.021345e-01 1.455015e+00
2.503736e-01 9.966807e-01
9.001793e-01 2.145059e+00
7.019990e-01 5.799112e-01
6.001746e-01 -1.432102e-01
4.925013e-01 -4.126441e-01
5.685795e-01 -2.849419e-01
1.238257e-01 2.007351e+00
2.825838e-01 7.124861e-01
4.025708e-01 -1.574002e-01
```

<!-- page 361 (PDF 368) -->
```python
8.562999e-01 1.875879e+00
3.214125e-01 3.865241e-01
2.021767e-01 1.418581e+00
6.338581e-01 5.717657e-02
3.042007e-01 5.276410e-01
4.860707e-01 -4.088007e-01
9.645326e-01 2.379243e+00
3.583711e-02 2.378513e+00
2.143110e-01 1.314473e+00
7.299624e-01 8.224203e-01
2.719263e-02 2.393622e+00
3.321495e-01 3.020224e-01
8.642671e-01 1.930341e+00
8.893604e-01 2.086039e+00
1.119469e-01 2.078562e+00
9.859741e-01 2.408725e+00
5.594688e-01 -3.166326e-01
1.904448e-01 1.516930e+00
4.232618e-01 -2.529865e-01
1.402221e-01 1.899932e+00
2.647519e-01 8.691058e-01
1.667035e-01 1.706823e+00
2.332246e-01 1.148786e+00
8.324190e-01 1.700059e+00
4.743443e-01 -3.958790e-01
3.435927e-01 2.154677e-01
9.846049e-01 2.407603e+00
9.705327e-01 2.390043e+00
6.631883e-01 2.662970e-01
6.153726e-01 -5.862472e-02
4.632361e-01 -3.766509e-01
6.474053e-01 1.502050e-01
7.161034e-02 2.273461e+00
4.514511e-01 -3.489255e-01
5.976782e-02 2.315661e+00
8.361934e-01 1.729000e+00
5.280981e-01 -3.922313e-01
9.394759e-01 2.313181e+00
2.710088e-01 8.138628e-01
8.161943e-01 1.571375e+00
5.047683e-01 -4.135789e-01
8.427635e-02 2.220534e+00
3.540224e-01 1.400987e-01
4.698548e-03 2.413597e+00
9.124315e-02 2.188105e+00
9.996285e-01 2.414210e+00
4.167139e-01 -2.249546e-01
5.892062e-01 -1.978247e-01
2.929336e-01 6.231119e-01
4.456454e-01 -3.325379e-01
1.148699e-02 2.410532e+00
3.892636e-01 -8.548741e-02
```

<!-- page 362 (PDF 369) -->
```python
7.188374e-01 7.248622e-01
3.697949e-01 3.323350e-02
6.864519e-01 4.502113e-01
1.586679e-01 1.767741e+00
6.603030e-01 2.445009e-01
6.277168e-01 1.721489e-02
4.305704e-01 -2.817686e-01
1.553435e-01 1.792379e+00
5.476842e-01 -3.512131e-01
8.475444e-01 1.813503e+00
9.527370e-01 2.352313e+00
```

In this example, two different correlation functions are tested and the obtained results are compared at the end.

#### 13.7.14.2 Macro Uranie

```python
"""
Example of simple GP usage and illustration of results
"""
from math import sqrt
import numpy as np
from URANIE import DataServer, Modeler, Relauncher
import ROOT
def print_solutions(tds_obs, tds_estim, title):
    """Simple function to produce the 1D plot with observation
    points, testing points along with the uncertainty band."""
    nb_obs = tds_obs.getNPatterns()
    nb_est = tds_estim.getNPatterns()
    rx_arr = np.zeros([nb_est])
    x_arr = np.zeros([nb_est])
    y_est = np.zeros([nb_est])
    y_rea = np.zeros([nb_est])
    std_var = np.zeros([nb_est])
    tds_estim.computeRank("x1")
    tds_estim.getTuple().copyBranchData(rx_arr, nb_est, "Rk_x1")
    tds_estim.getTuple().copyBranchData(x_arr, nb_est, "x1")
    tds_estim.getTuple().copyBranchData(y_est, nb_est, "yEstim")
    tds_estim.getTuple().copyBranchData(y_rea, nb_est, "y")
    tds_estim.getTuple().copyBranchData(std_var, nb_est, "vEstim")
    xarr = np.zeros([nb_est])
    yest = np.zeros([nb_est])
    yrea = np.zeros([nb_est])
    stdvar = np.zeros([nb_est])
    for i in range(nb_est):
        ind = int(rx_arr[i]) - 1
        xarr[ind] = x_arr[i]
        yest[ind] = y_est[i]
```

<!-- page 363 (PDF 370) -->
```python
        yrea[ind] = y_rea[i]
        stdvar[ind] = 2*sqrt(abs(std_var[i]))
    xobs = np.zeros([nb_obs])
    tds_obs.getTuple().copyBranchData(xobs, nb_obs, "x1")
    yobs = np.zeros([nb_obs])
    tds_obs.getTuple().copyBranchData(yobs, nb_obs, "y")
    gobs = ROOT.TGraph(nb_obs, xobs, yobs)
    gobs.SetMarkerColor(1)
    gobs.SetMarkerSize(1)
    gobs.SetMarkerStyle(8)
    zeros = np.zeros([nb_est])
                                # use doe plotting only
    gest = ROOT.TGraphErrors(nb_est, xarr, yest, zeros, stdvar)
    gest.SetLineColor(2)
    gest.SetLineWidth(1)
    gest.SetFillColor(2)
    gest.SetFillStyle(3002)
    grea = ROOT.TGraph(nb_est, xarr, yrea)
    grea.SetMarkerColor(4)
    grea.SetMarkerSize(1)
    grea.SetMarkerStyle(5)
    grea.SetTitle("Real Values")
    mgr = ROOT.TMultiGraph("toto", title)
    mgr.Add(gest, "l3")
    mgr.Add(gobs, "P")
    mgr.Add(grea, "P")
    mgr.Draw("A")
    mgr.GetXaxis().SetTitle("x_{1}")
    leg = ROOT.TLegend(0.4, 0.65, 0.65, 0.8)
    leg.AddEntry(gobs, "Observations", "p")
    leg.AddEntry(grea, "Real values", "p")
    leg.AddEntry(gest, "Estimated values", "lf")
    leg.Draw()
    return [mgr, leg]
# Create dataserver and read training database
tdsObs = DataServer.TDataServer("tdsObs", "observations")
tdsObs.fileDataRead("utf-1D-train.dat")
nbObs = 6
# Canvas, divided in 2
Can = ROOT.TCanvas("can", "can", 10, 32, 1600, 700)
apad = ROOT.TPad("apad", "apad", 0, 0.03, 1, 1)
apad.Draw()
apad.Divide(2, 1)
# Name of the plot and correlation functions used
outplot = "GaussAndMatern_1D_AllPoints.png"
Correl = ["Gauss", "Matern3/2"]
```

<!-- page 364 (PDF 371) -->
```python
# Pointer to needed objects, created in the loop
gpb = [0, 0]
kg = [0, 0]
tdsEstim = [0, 0]
lkrig = [0, 0]
mgs = [0, 0]
legs = [0, 0]
# Looping over the two correlation function chosen
for im in range(2):
    # Create the TGPBuiler object with chosen option to find optimal parameters
    gpb[im] = Modeler.TGPBuilder(tdsObs, "x1", "y", Correl[im], "")
    gpb[im].findOptimalParameters("LOO", 100, "Subplexe", 1000)
    # Get the kriging object
    kg[im] = gpb[im].buildGP()
    # open the dataserver and read the testing basis
    tdsEstim[im] = DataServer.TDataServer("tdsEstim_"+str(im),
                                          "base de test")
    tdsEstim[im].fileDataRead("utf-1D-test.dat")
    # Applied resulting kriging on test basis
    lkrig[im] = Relauncher.TLauncher2(tdsEstim[im], kg[im], "x1",
                                      "yEstim:vEstim")
    lkrig[im].solverLoop()
    # do the plot
    apad.cd(im+1)
    mgs[im], legs[im] = print_solutions(tdsObs, tdsEstim[im], Correl[im])
    lat = ROOT.TLatex()
    lat.SetNDC()
    lat.SetTextSize(0.025)
    lat.DrawLatex(0.4, 0.61, "RMSE (by Loo) "+str(kg[im].getLooRMSE()))
    lat.DrawLatex(0.4, 0.57, "Q2 "+str(kg[im].getLooQ2()))
```

The first function of this macro (called PrintSolutions) is a complex part that will not be detailed, used to represent
the results.
The macro itself starts by reading the training database and storing it in a dataserver. A TGPBuilder is created with the
chosen correlation function and the hyper-parameters are estimation by an optimisation procedure in:

```python
gpb[im] = Modeler.TGPBuilder(tdsObs, "x1", "y", Correl[im], "")
gpb[im].findOptimalParameters("LOO", 100, "Subplexe", 1000)
kg[im] = gpb[im].buildGP()
```

The last line shows how to build and retrieve the newly created kriging object.
Finally, this kriging model is tested against the training database, thanks to a TLauncher2 object, as following:
