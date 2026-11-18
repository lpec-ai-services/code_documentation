# Use-cases in Python — Macros Modeler — Macro “modelerCornellLinearRegression.py” … Macro “modelerFlowratePolynChaosRegression.py”
<!-- source PDF pages 337-356 -->

<!-- page 330 (PDF 337) -->
## 13.7 Macros Modeler

### 13.7.1 Macro “modelerCornellLinearRegression.py”

#### 13.7.1.1 Objective

The objective of the macro is to build a multilinear regression between the predictors related to the normalisation of the
variables x1, x2, x3, x4, x5, x6, x7 and a target variable y from the database contained in the ASCII file cornell.dat:

```python
#NAME: cornell
#TITLE: Dataset Cornell 1990
#COLUMN_NAMES: x1 | x2 | x3 | x4 | x5 | x6 | x7 | y
#COLUMN_TITLES: x_{1} | x_{2} | x_{3} | x_{4} | x_{5} | x_{6} | x_{7} | y
0.00 0.23 0.00 0.00 0.00 0.74 0.03 98.7
0.00 0.10 0.00 0.00 0.12 0.74 0.04 97.8
0.00 0.00 0.00 0.10 0.12 0.74 0.04 96.6
0.00 0.49 0.00 0.00 0.12 0.37 0.02 92.0
0.00 0.00 0.00 0.62 0.12 0.18 0.08 86.6
0.00 0.62 0.00 0.00 0.00 0.37 0.01 91.2
0.17 0.27 0.10 0.38 0.00 0.00 0.08 81.9
0.17 0.19 0.10 0.38 0.02 0.06 0.08 83.1
0.17 0.21 0.10 0.38 0.00 0.06 0.08 82.4
0.17 0.15 0.10 0.38 0.02 0.10 0.08 83.2
0.21 0.36 0.12 0.25 0.00 0.00 0.06 81.4
0.00 0.00 0.00 0.55 0.00 0.37 0.08 88.1
```

####  13.7.1.2 Macro Uranie

```python
"""
Example of linear regression model
"""
from URANIE import DataServer, Modeler
import ROOT
tds = DataServer.TDataServer()
tds.fileDataRead("cornell.dat")
tds.normalize("*", "cr")
                          # "*" is equivalent to "x1:x2:x3:x4:x5:x6:y"
# Third field not filled implies DataServer.TDataServer.kCR
c = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2)
pad.cd(1)
tds.draw("y:x7")
tlin = Modeler.TLinearRegression(tds, "x1cr:x2cr:x3cr:x4cr:x5cr:x6cr",
                                 "ycr", "nointercept")
tlin.estimate()
pad.cd(2)
```

<!-- page 331 (PDF 338) -->
```python
tds.draw("ycr:ycrhat")
```

The ASCII data file cornell.dat is loaded in the TDataServer:

```python
tds = DataServer.TDataServer()
tds.fileDataRead("cornell.dat")
```

The variables are all normalised with a standardised method. The normalised attributes are created with the cr extension:

```python
tds.normalize("*", "cr")
                          # "*" is equivalent to "x1:x2:x3:x4:x5:x6:y"
```

The linear regression is initialised and characteristic values are computed for each normalised variable with the estimate
method. The regression is built with no intercept:

```python
tlin = Modeler.TLinearRegression(tds, "x1cr:x2cr:x3cr:x4cr:x5cr:x6cr",
                                 "ycr", "nointercept")
tlin.estimate()
```

####  13.7.1.3 Graph

Figure 13.37: Graph of the macro “modelerCornellLinearRegression.py”

### 13.7.2 Macro “modelerFlowrateLinearRegression.py”

#### 13.7.2.1 Objective

The objective of this macro is to build a linear regression between a predictor rw and a target variable yhat from the
database contained in the ASCII file flowrate_sampler_launcher_500.dat defining values for the eight variables
described in Presentation of the problem on 500 patterns.

<!-- page 332 (PDF 339) -->
#### 13.7.2.2 Macro Uranie

```python
"""
Example of linear regression on flowrate
"""
from URANIE import DataServer, Modeler
import ROOT
tds = DataServer.TDataServer()
tds.fileDataRead("flowrate_sampler_launcher_500.dat")
c = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2)
pad.cd(1)
tds.draw("yhat:rw")
# tds.getAttribute("yhat").setOutput()
tlin = Modeler.TLinearRegression(tds, "rw", "yhat", "DummyForPython")
tlin.estimate()
pad.cd(2)
tds.draw("yhathat:yhat")
tds.startViewer()
```

The TDataServer is loaded with the database contained in the file flowrate_sampler_launcher_500.dat with
the fileDataRead method:

```python
tds = DataServer.TDataServer()
tds.fileDataRead("flowrate_sampler_launcher_500.dat")
```

The linear regression is initialised and characteristic values are computed for rw with the estimate method:

```python
tlin = Modeler.TLinearRegression(tds, "rw", "yhat", "DummyForPython")
tlin.estimate()
```

The last argument is the option field, which in most cases is empty. Here it is filled with “DummyPython” which helps
specify to python which constructor to choose. There are indeed several possible constructors these 5 five first arguments,
but C++ can make the difference between them as the literal members are either std::string, ROOT::TString,
Char_t* or even Option_t*. For python, these format are all PyString, so the sixth argument is compulsory to
disentangle the possibilities.

<!-- page 333 (PDF 340) -->
#### 13.7.2.3 Graph

Figure 13.38: Graph of the macro “modelerFlowrateLinearRegression.py”

### 13.7.3 Macro “modelerFlowrateMultiLinearRegression.py”

#### 13.7.3.1 Objective

The objective of the macro is to build a multilinear regression between the predictors 𝑟𝜔, 𝑟, 𝑇𝑢, 𝑇𝑙, 𝐻𝑢, 𝐻𝑙, 𝐿, 𝐾𝜔and a
target variable yhat from the database contained in the ASCII file flowrate_sampler_launcher_500.dat defining
values for these eight variables described in Presentation of the problem on 500 patterns. Parameters of the regression are
then exported in a .py file _FileContainingFunction_.C:

```python
void MultiLinearFunction(double *param, double *res)
{
  //////////////////////////////
  //
  //
         *********************************************
  //
         ** Uranie v3.12/0 -
                              Date : Thu Jan 04, 2018
  //
         ** Export Modeler :␣
```

˓→Modeler[LinearRegression]Tds[tdsFlowrate]Predictor[rw:r:tu:tl:hu:hl:l:kw]Target[yhat]

```python
//
       ** Date : Tue Jan
                          9 12:08:27 2018
//
       *********************************************
//
//
       *********************************************
//
       ** TDataServer
//
       **
                 Name
                       : tdsFlowrate
//
       **
                 Title : Design of experiments for Flowrate
//
       **
              Patterns : 500
//
       **
            Attributes : 10
//
       *********************************************
```

<!-- page 334 (PDF 341) -->
```python
//
//
       INPUT
              : 8
//
               rw : Min[0.050069828419999997] Max[0.14991758599999999] Unit[]
//
               r : Min[147.90551809999999] Max[49906.309529999999] Unit[]
//
               tu : Min[63163.702980000002] Max[115568.17200000001] Unit[]
//
               tl : Min[63.169232649999998] Max[115.90147020000001] Unit[]
//
               hu : Min[990.00977509999996] Max[1109.786159] Unit[]
//
               hl : Min[700.14498509999999] Max[819.81105760000003] Unit[]
//
               l : Min[1120.3428429999999] Max[1679.3424649999999] Unit[]
//
               kw : Min[9857.3689890000005] Max[12044.00546] Unit[]
//
//
       OUTPUT : 1
//
               yhat : Min[13.09821] Max[208.25110000000001] Unit[]
//
//////////////////////////////
//
//
       QUALITY
                :
//
//
                R2
                    = 0.948985
//
                R2a = 0.948154
//
                Q2
                    = 0.946835
//
//////////////////////////////
// Intercept
double y = -156.03;
// Attribute : rw
y += param[0]*1422.21;
// Attribute : r
y += param[1]*-3.07412e-07;
// Attribute : tu
y += param[2]*2.15208e-06;
// Attribute : tl
y += param[3]*-0.00498512;
// Attribute : hu
y += param[4]*0.261104;
// Attribute : hl
y += param[5]*-0.254419;
// Attribute : l
y += param[6]*-0.0557145;
// Attribute : kw
y += param[7]*0.00813552;
// Return the value
```

<!-- page 335 (PDF 342) -->
```python
  res[0] = y;
}
```

This file contains a MultiLinearFunction function. Comparison is made with a database generated from random
variables obeying uniform laws and output variable calculated with this database and the MultiLinearFunction function
.

#### 13.7.3.2 Macro Uranie

```python
"""
Example of multi-linear regression on flowrate
"""
from URANIE import DataServer, Launcher, Modeler, Sampler
import ROOT
tds = DataServer.TDataServer()
tds.fileDataRead("flowrate_sampler_launcher_500.dat")
c = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
tlin = Modeler.TLinearRegression(tds, "rw:r:tu:tl:hu:hl:l:kw",
                                 "yhat", "DummyForPython")
tlin.estimate()
tlin.exportFunction("c++", "_FileContainingFunction_", "MultiLinearFunction")
# Define the DataServer
tds2 = DataServer.TDataServer("tdsFlowrate", "Design of experiments")
# Add the study attributes
tds2.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds2.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds2.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds2.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds2.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds2.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds2.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds2.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
nS = 1000
# Generate DOE
sampling = Sampler.TSampling(tds2, "lhs", nS)
sampling.generateSample()
ROOT.gROOT.LoadMacro("_FileContainingFunction_.C")
# Create a TLauncherFunction from a TDataServer and an analytical function
# Rename the outpout attribute "ymod"
tlf = Launcher.TLauncherFunction(tds2, "MultiLinearFunction", "", "ymod")
# Evaluate the function on all the design of experiments
tlf.run()
```

<!-- page 336 (PDF 343) -->
```python
tds2.getTuple().SetMarkerColor(ROOT.kBlue)
tds2.getTuple().SetMarkerStyle(8)
tds2.getTuple().SetMarkerSize(1.2)
tds.getTuple().SetMarkerColor(ROOT.kGreen)
tds.getTuple().SetMarkerStyle(8)
tds.getTuple().SetMarkerSize(1.2)
tds2.draw("ymod:rw")
tds.draw("yhat:rw", "", "same")
```

The TDataServer is loaded with the database contained in the file flowrate_sampler_launcher_500.dat with
the fileDataRead method:

```python
tds = DataServer.TDataServer()
tds.fileDataRead("flowrate_sampler_launcher_500.dat")
```

The linear regression is initialised and characteristic values are computed for each variable with the estimate method:

```python
tlin = Modeler.TLinearRegression(tds, "rw:r:tu:tl:hu:hl:l:kw",
                                 "yhat", "DummyForPython")
tlin.estimate()
```

The last argument is the option field, which in most cases is empty. Here it is filled with “DummyPython” which helps
specify to python which constructor to choose. There are indeed several possible constructors these 5 five first arguments,
but C++ can make the difference between them as the literal members are either std::string, ROOT::TString,
Char_t* or even Option_t*. For python, these format are all PyString, so the sixth argument is compulsory to
disentangle the possibilities.
The model is exported in an external file in C++ language _FileContainingFunction_.C where the function name
is MultiLinearFunction:

```python
tlin.exportFunction("c++", "_FileContainingFunction_", "MultiLinearFunction")
```

A second TDataServer is created. The previous variables then obey uniform laws and are linked as TAttribute in
this new TDataServer:

```python
tds2.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds2.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds2.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds2.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds2.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds2.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds2.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds2.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

A sampling is realised with a LHS method on 1000 patterns:

```python
sampling = Sampler.TSampling(tds2, "lhs", nS)
sampling.generateSample()
```

The previously exported macro _FileContainingFunction_.C is loaded so as to perform calculation over the
database in the second TDataServer with the function MultiLinearFunction. Results are stored in the ymod
variable:

<!-- page 337 (PDF 344) -->
```python
ROOT.gROOT.LoadMacro("_FileContainingFunction_.C")
tlf = Launcher.TLauncherFunction(tds2, "MultiLinearFunction", "", "ymod")
tlf.run()
```

####  13.7.3.3 Graph

Figure 13.39: Graph of the macro “modelerFlowrateMultiLinearRegression.py”

### 13.7.4 Macro “modelerFlowrateNeuralNetworks.py”

#### 13.7.4.1 Objective

The objective of this macro is to build a surrogate model (an Artificial Neural Network) from a database.
From a first database created from an ASCII file flowrate_sampler_launcher_500.dat (which defines values
for eight variables described in Presentation of the problem on 500 patterns), two ASCII files are created:
one with the 300st patterns (_flowrate_sampler_launcher_app_.dat), the other with the 200 last patterns
(_flowrate_sampler_launcher_val_.dat). The surrogate model is built with the database extracted from the
first of the two files, the second allowing to perform calculations with a function.

#### 13.7.4.2 Macro Uranie

```python
"""
Example of neural network usage on flowrate
"""
from URANIE import DataServer, Launcher, Modeler
import ROOT
# Create a DataServer.TDataServer
# Load a database in an ASCII file
tdsu = DataServer.TDataServer("tdsu", "tds u")
```

<!-- page 338 (PDF 345) -->
```python
tdsu.fileDataRead("flowrate_sampler_launcher_500.dat")
tdsu.exportData("_flowrate_sampler_launcher_app_.dat", "",
                "tdsFlowrate__n__iter__<=300")
tdsu.exportData("_flowrate_sampler_launcher_val_.dat", "",
                "tdsFlowrate__n__iter__>300")
tds = DataServer.TDataServer("tdsFlowrate", "tds for flowrate")
tds.fileDataRead("_flowrate_sampler_launcher_app_.dat")
c = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
# Buils a surrogate model (Artificial Neural Networks) from the DataBase
tann = Modeler.TANNModeler(tds, "rw:r:tu:tl:hu:hl:l:kw, 3,yhat")
tann.setFcnTol(1e-5)
# tann.setLog()
tann.train(3, 2, "test")
tann.exportFunction("pmmlc++", "uranie_ann_flowrate", "ANNflowrate")
ROOT.gROOT.LoadMacro("uranie_ann_flowrate.C")
tdsv = DataServer.TDataServer()
tdsv.fileDataRead("_flowrate_sampler_launcher_val_.dat")
print(tdsv.getNPatterns())
# evaluate the surrogate model on the database
tlf = Launcher.TLauncherFunction(tdsv, "ANNflowrate",
                                 "rw:r:tu:tl:hu:hl:l:kw", "yann")
tlf.run()
tdsv.startViewer()
tdsv.Draw("yann:yhat")
# tdsv.draw("yhat")
```

The main TDataServer loads the main ASCII data file flowrate_sampler_launcher_500.dat

```python
tdsu = DataServer.TDataServer("tdsu", "tds u")
tdsu.fileDataRead("flowrate_sampler_launcher_500.dat")
```

The database is split in two parts by exporting the 300st patterns in a file and the remaining 200 in another one:

```python
tdsu.exportData("_flowrate_sampler_launcher_app_.dat", "",
                "tdsFlowrate__n__iter__<=300")
tdsu.exportData("_flowrate_sampler_launcher_val_.dat", "",
                "tdsFlowrate__n__iter__>300")
```

A second TDataServer loads _flowrate_sampler_launcher_app_.dat and builds the surrogate model over all
the variables:

<!-- page 339 (PDF 346) -->
```python
tds = DataServer.TDataServer("tdsFlowrate", "tds for flowrate")
tds.fileDataRead("_flowrate_sampler_launcher_app_.dat")
tann = Modeler.TANNModeler(tds, "rw:r:tu:tl:hu:hl:l:kw, 3,yhat")
tann.setFcnTol(1e-5)
tann.train(3, 2, "test")
```

The model is exported in an external file in C++ language "uranie_ann_flowrate.C" where the function name is
ANNflowrate:

```python
tann.exportFunction("c++", "uranie_ann_flowrate","ANNflowrate")
```

The model is loaded from the macro "uranie_ann_flowrate.C" and applied on the second database with the function
ANNflowrate:

```python
ROOT.gROOT.LoadMacro("uranie_ann_flowrate.C")
tdsv = DataServer.TDataServer()
tdsv.fileDataRead("_flowrate_sampler_launcher_val_.dat")
tlf = Launcher.TLauncherFunction(tdsv, "ANNflowrate",
                                 "rw:r:tu:tl:hu:hl:l:kw", "yann")
tlf.run()
```

####  13.7.4.3 Graph

Figure 13.40: Graph of the macro “modelerFlowrateNeuralNetworks.py”

#### 13.7.4.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
```

<!-- page 340 (PDF 347) -->
```python
                     Date: Thu Feb 12, 2026
<URANIE::WARNING>
<URANIE::WARNING> *** URANIE WARNING ***
<URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[760]
<URANIE::WARNING> TDataServer::fileDataRead: Expected iterator tdsu__n__iter__ not␣
```

˓→found but tdsFlowrate__n__iter__ looks like an URANIE iterator => Will be used as␣
˓→so.

```python
 <URANIE::WARNING> *** END of URANIE WARNING ***
 <URANIE::WARNING>
 ** TANNModeler::train niter[3] ninit[2]
 ** init the ANN
 ** Input
           (1) Name[rw] Min[0.101018] Max[0.0295279]
 ** Input
           (2) Name[r] Min[25668.6] Max[14838.3]
 ** Input
           (3) Name[tu] Min[89914.4] Max[14909]
 ** Input
           (4) Name[tl] Min[89.0477] Max[15.0121]
 ** Input
           (5) Name[hu] Min[1048.92] Max[34.8615]
 ** Input
           (6) Name[hl] Min[763.058] Max[33.615]
 ** Input
           (7) Name[l] Min[1401.09] Max[163.611]
 ** Input
           (8) Name[kw] Min[10950.2] Max[635.503]
 ** Output
            (1) Name[yhat] Min[78.0931] Max[44.881]
 ** Tolerance
               (1e-05)
 ** sHidden
               (3) (3)
 ** Nb Weights (31)
 ** ActivationFunction[LOGISTIC]
 **
 ** iter[1/3] : *= : mse_min[0.00150425]
 ** iter[2/3] : ** : mse_min[0.0024702]
 ** iter[3/3] : *= : mse_min[0.00122167]
 ** solutions : 3
 ** isol[1] iter[0] learn[0.00126206] test[0.00150425] *
 ** isol[2] iter[1] learn[0.00152949] test[0.0024702]
 ** isol[3] iter[2] learn[0.00107926] test[0.00122167] *
 ** CPU training finished. Total elapsed time: 1.84 sec
*******************************
*** TModeler::exportFunction lang[pmmlc++] file[uranie_ann_flowrate]␣
```

˓→name[ANNflowrate] soption[]

```python
*******************************
*******************************
*** exportFunction lang[pmmlc++] file[uranie_ann_flowrate] name[ANNflowrate]
*******************************
PMML Constructor: uranie_ann_flowrate.pmml
*** End Of exportModelPMML
*******************************
*** End Of exportFunction
*******************************
```

<!-- page 341 (PDF 348) -->
### 13.7.5 Macro “modelerFlowrateNeuralNetworksLoadingPMML.py”

#### 13.7.5.1 Objective

The objective of this macro is to build a surrogate model (an Artificial Neural Network) from a PMML file.

#### 13.7.5.2 Macro Uranie

```python
"""
Example of neural network loaded from pmml for flowrate
"""
from URANIE import DataServer, Launcher, Modeler
import ROOT
# Create a DataServer.TDataServer
# Load a database in an ASCII file
tds = DataServer.TDataServer("tdsFlowrate", "tds for flowrate")
tds.fileDataRead("_flowrate_sampler_launcher_app_.dat")
c = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
# Build a surrogate model (Artificial Neural Networks) from the PMML file
tann = Modeler.TANNModeler(tds, "uranie_ann_flowrate.pmml", "ANNflowrate")
# export the surrogate model in a C file
tann.exportFunction("c++", "uranie_ann_flowrate_loaded", "ANNflowrate")
# load the surrogate model in the C file
ROOT.gROOT.LoadMacro("uranie_ann_flowrate_loaded.C")
tdsv = DataServer.TDataServer("tdsv", "tds for surrogate model")
tdsv.fileDataRead("_flowrate_sampler_launcher_val_.dat")
print(tdsv.getNPatterns())
# evaluate the surrogate model on the database
tlf = Launcher.TLauncherFunction(tdsv, "ANNflowrate",
                                 "rw:r:tu:tl:hu:hl:l:kw", "yann")
tlf.run()
tdsv.startViewer()
tdsv.Draw("yann:yhat")
# tdsv.draw("yhat")
```

A TDataServer loads _flowrate_sampler_launcher_app_.dat:

```python
tds = DataServer.TDataServer("tdsFlowrate", "tds for flowrate")
tds.fileDataRead("_flowrate_sampler_launcher_app_.dat")
```

The surrogate model is loaded from a PMML file:

```python
tann = Modeler.TANNModeler(tds, "uranie_ann_flowrate.pmml", "ANNflowrate")
```

The model is exported in an external file in C++ language "uranie_ann_flowrate_loaded.C" where the function
name is ANNflowrate:

<!-- page 342 (PDF 349) -->
```python
tann.exportFunction("c++", "uranie_ann_flowrate_loaded", "ANNflowrate")
```

The model is loaded from the macro "uranie_ann_flowrate_loaded.C" and applied on the database with the
function ANNflowrate:

```python
ROOT.gROOT.LoadMacro("uranie_ann_flowrate_loaded.C")
tdsv = DataServer.TDataServer("tdsv", "tds for surrogate model")
tdsv.fileDataRead("_flowrate_sampler_launcher_val_.dat")
tlf = Launcher.TLauncherFunction(tdsv, "ANNflowrate",
                                 "rw:r:tu:tl:hu:hl:l:kw", "yann")
tlf.run()
```

####  13.7.5.3 Graph

Figure 13.41: Graph of the macro “modelerFlowrateNeuralNetworksLoadingPMML.py”

#### 13.7.5.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
PMML Constructor: uranie_ann_flowrate.pmml
*******************************
*** TModeler::exportFunction lang[c++] file[uranie_ann_flowrate_loaded]␣
```

˓→name[ANNflowrate] soption[]

```python
*******************************
```

<!-- page 343 (PDF 350) -->
```python
*******************************
*** exportFunction lang[c++] file[uranie_ann_flowrate_loaded] name[ANNflowrate]
*** End Of exportFunction
*******************************
```

###  13.7.6 Macro “modelerClassificationNeuralNetworks.py”

####  13.7.6.1 Objective

The objective of this macro is to build a surrogate model (an Artificial Neural Network) from a database for a “Classification
” Problem. From a first database loaded from the ASCII file problem2Classes_001000.dat, which defines
three variables (𝑥, 𝑦) ∈[−1., 1]2 and 𝑟𝑐01 ∈{0, 1} on 1000 patterns,
two ASCII files are created, one with the 800st patterns (_problem2Classes_app_.dat), the other with the 200 last
patterns (_problem2Classes_val_.dat). The surrogate model is built with the database extracted from the first of
the two files, the second allowing to perform calculations with a function.

#### 13.7.6.2 Macro Uranie

```python
"""
Example of classification problem with neural network
"""
from URANIE import DataServer, Launcher, Modeler
import ROOT
nH1 = 15
nH2 = 10
nH3 = 5
```

<!-- page 344 (PDF 351) -->
```python
sX = "x:y"
sY = "rc01"
sYhat = sY+"_"+str(nH1)+"_"+str(nH2)+"_"+str(nH3)
# Load a database in an ASCII file
tdsu = DataServer.TDataServer("tdsu", "tds u")
tdsu.fileDataRead("problem2Classes_001000.dat")
# Split into 2 datasets for learning and testing
Niter = tdsu.getIteratorName()
tdsu.exportData("_problem2Classes_app_.dat", "", Niter+"<=800")
tdsu.exportData("_problem2Classes_val_.dat", "", Niter+">800")
tds = DataServer.TDataServer("tdsApp", "tds App for problem2Classes")
tds.fileDataRead("_problem2Classes_app_.dat")
tann = Modeler.TANNModeler(tds, sX+", %i, %i, %i,@" % (nH1, nH2, nH3)+sY)
# tann.setLog()
tann.setNormalization(Modeler.TANNModeler.kMinusOneOne)
tann.setFcnTol(1e-6)
tann.train(2, 2, "test", False)
tann.exportFunction("c++", "uranie_ann_problem2Classes", "ANNproblem2Classes")
ROOT.gROOT.LoadMacro("uranie_ann_problem2Classes.C")
tdsv = DataServer.TDataServer()
tdsv.fileDataRead("_problem2Classes_val_.dat")
# evaluate the surrogate model on the database
tlf = Launcher.TLauncherFunction(tdsv, "ANNproblem2Classes", sX, sYhat)
tlf.run()
c = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
# Buils a surrogate model (Artificial Neural Networks) from the DataBase
tds.getTuple().SetMarkerStyle(8)
tds.getTuple().SetMarkerSize(1.0)
tds.getTuple().SetMarkerColor(ROOT.kGreen)
tds.draw(sY+":"+sX)
tdsv.getTuple().SetMarkerStyle(8)
tdsv.getTuple().SetMarkerSize(0.75)
tdsv.getTuple().SetMarkerColor(ROOT.kRed)
tdsv.Draw(sYhat+":"+sX, "", "same")
```

The main TDataServer loads the main ASCII data file problem2Classes_001000.dat

```python
tdsu = DataServer.TDataServer("tdsu", "tds u")
tdsu.fileDataRead("problem2Classes_001000.dat")
```

The database is split with the internal iterator attribute in two parts by exporting the 800st patterns in a file and the
remaining 200 in another one

<!-- page 345 (PDF 352) -->
```python
tdsu.exportData("_problem2Classes_app_.dat", "", Niter+"<=800")
tdsu.exportData("_problem2Classes_val_.dat", "", Niter+">800")
```

A second TDataServer loads _problem2Classes_app_.dat and builds the surrogate model over all the variables
with 3 hidden layers, a Hyperbolic Tangent (TanH) activation function (normalization) in the 3 hidden layers and set
the function tolerance to 1e-.6. The “@” character behind the output name defines a classification problem.

```python
tds = DataServer.TDataServer("tdsApp", "tds App for problem2Classes")
tds.fileDataRead("_problem2Classes_app_.dat")
tann = Modeler.TANNModeler(tds, sX+", %i, %i, %i,@" % (nH1, nH2, nH3)+sY)
tann.setNormalization(Modeler.TANNModeler.kMinusOneOne)
tann.setFcnTol(1e-6)
tann.train(2, 2, "test", False)
```

The model is exported in an external file in C++ language "uranie_ann_problem2Classes.C" where the function
name is ANNproblem2Classes

```python
tann.exportFunction("c++", "uranie_ann_problem2Classes", "ANNproblem2Classes")
```

The model is loaded from the macro uranie_ann_problem2Classes.C and applied on the second database with the
function ANNproblem2Classes.

```python
ROOT.gROOT.LoadMacro("uranie_ann_problem2Classes.C")
tdsv = DataServer.TDataServer()
tdsv.fileDataRead("_problem2Classes_val_.dat")
tlf = Launcher.TLauncherFunction(tdsv, "ANNproblem2Classes", sX, sYhat)
tlf.run()
```

We draw on a 3D graph, the learning database (in green) and the estimations by the Artificial Neural Network with red
points.

```python
c = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
tds.getTuple().SetMarkerStyle(8)
tds.getTuple().SetMarkerSize(1.0)
tds.getTuple().SetMarkerColor(ROOT.kGreen)
tds.draw(sY+":"+sX)
tdsv.getTuple().SetMarkerStyle(8)
tdsv.getTuple().SetMarkerSize(0.75)
tdsv.getTuple().SetMarkerColor(ROOT.kRed)
tdsv.Draw(sYhat+":"+sX, "", "same")
```

<!-- page 346 (PDF 353) -->
#### 13.7.6.3 Graph

Figure 13.42: Graph of the macro “modelerClassificationNeuralNetworks.py”

#### 13.7.6.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
 <URANIE::WARNING>
 <URANIE::WARNING> *** URANIE WARNING ***
 <URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[760]
 <URANIE::WARNING> TDataServer::fileDataRead: Expected iterator tdsu__n__iter__ not␣
```

˓→found but _tds___n__iter__ looks like an URANIE iterator => Will be used as so.

```python
<URANIE::WARNING> *** END of URANIE WARNING ***
<URANIE::WARNING>
<URANIE::WARNING>
<URANIE::WARNING> *** URANIE WARNING ***
<URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[760]
<URANIE::WARNING> TDataServer::fileDataRead: Expected iterator tdsApp__n__iter__ not␣
```

˓→found but _tds___n__iter__ looks like an URANIE iterator => Will be used as so.

```python
<URANIE::WARNING> *** END of URANIE WARNING ***
<URANIE::WARNING>
** TANNModeler::train niter[2] ninit[2]
** init the ANN
** Input
          (1) Name[x] Min[-0.999842] Max[0.998315]
** Input
          (2) Name[y] Min[-0.999434] Max[0.998071]
** Output
           (1) Name[rc01] Min[0] Max[1]
** Tolerance
              (1e-06)
```

<!-- page 347 (PDF 354) -->
```python
 ** sHidden
               (15,10,5) (30)
 ** Nb Weights (266)
 ** ActivationFunction[TanH]
 **
 ** iter[1/2] : ** : mse_min[0.00813999]
 ** iter[2/2] : ** : mse_min[0.00636923]
 ** solutions : 2
 ** isol[1] iter[0] learn[0.00405863] test[0.00813999] *
 ** isol[2] iter[1] learn[0.00560685] test[0.00636923] *
 ** CPU training finished. Total elapsed time: 19 sec
*******************************
*** TModeler::exportFunction lang[c++] file[uranie_ann_problem2Classes]␣
```

˓→name[ANNproblem2Classes] soption[]

```python
*******************************
*******************************
*** exportFunction lang[c++] file[uranie_ann_problem2Classes] name[ANNproblem2Classes]
*** End Of exportFunction
*******************************
```

###  13.7.7 Macro “modelerFlowratePolynChaosRegression.py”

####  13.7.7.1 Objective

The objective of this macro is to build a polynomial chaos expansion in order to get a surrogate model along with a
global sensitivity interpretation for the flowrate function, whose purpose and behaviour have been already introduced
in Presentation of the problem. The method used here is the regression one, as discussed below.

#### 13.7.7.2 Macro Uranie

```python
"""
Example of Chaos polynomial expansion using regression estimation on flowrate
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
```

<!-- page 348 (PDF 355) -->
```python
# Define of TNisp object
nisp = Modeler.TNisp(tds)
nisp.generateSample("QmcSobol", 500)
                                      # State that there is a sample ...
# Compute the output variable
tlf = Launcher.TLauncherFunction(tds, "flowrateModel", "*", "ymod")
tlf.setDrawProgressBar(False)
tlf.run()
# build a chaos polynomial
pc = Modeler.TPolynomialChaos(tds, nisp)
# compute the pc coefficients using the "Regression" method
degree = 4
pc.setDegree(degree)
pc.computeChaosExpansion("Regression")
# Uncertainty and sensitivity analysis
print("Variable ymod ================")
print("Mean
                = "+str(pc.getMean("ymod")))
print("Variance = "+str(pc.getVariance("ymod")))
print("First Order Indices ================")
print("Indice First Order[1] = "+str(pc.getIndexFirstOrder(0, 0)))
print("Indice First Order[2] = "+str(pc.getIndexFirstOrder(1, 0)))
print("Indice First Order[3] = "+str(pc.getIndexFirstOrder(2, 0)))
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

The first part is just creating a TDataServer and providing the attributes needed to define the problem. From there, a
TNisp object is created, providing the dataserver that specifies the inputs. This class is used to generate the sample.

<!-- page 349 (PDF 356) -->
```python
# Define of TNisp object
nisp = Modeler.TNisp(tds)
nisp.generateSample("QmcSobol", 500)
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
# compute the pc coefficients using the "Regression" method
degree = 4
pc.setDegree(degree)
pc.computeChaosExpansion("Regression")
```

The rest of the code is showing how to access the resulting sensitivity indices either one-by-one, or ordered up to a chosen
threshold of the output variance.

#### 13.7.7.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
Variable ymod ================
Mean
         = 77.65102218686935
Variance = 2079.6809330496953
First Order Indices ================
Indice First Order[1] = 0.8287315275344169
Indice First Order[2] = 1.0554825358264659e-06
Indice First Order[3] = 9.868045331678087e-08
Indice First Order[4] = 4.776680831542115e-06
Indice First Order[5] = 0.04140149326660007
Indice First Order[6] = 0.04132153620304167
Indice First Order[7] = 0.03940096615922832
Indice First Order[8] = 0.00954643619284736
Total Order Indices ================
Indice Total Order[1] = 0.8667727763800165
Indice Total Order[2] = 9.274665082296543e-06
Indice Total Order[3] = 7.017680590520732e-06
Indice Total Order[4] = 1.7194373944638416e-05
Indice Total Order[5] = 0.05419157561201169
Indice Total Order[6] = 0.05405781720242182
Indice Total Order[7] = 0.05221211558384676
Indice Total Order[8] = 0.012780873435736001
```
