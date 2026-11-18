# Use-cases in Python — Macros Launcher — Macro “sensitivityMorrisFunctionFlowrateRunner.py” … Macro “sensitivityRegressionLeveLE.py”
<!-- source PDF pages 289-307 -->

<!-- page 282 (PDF 289) -->
```python
*
         6 *
                     l * flowrateM * -23.89328 * 23.893280 * 8.2781934 *
*
         7 *
                    kw * flowrateM * 7.5766167 * 7.5766167 * 2.7457665 *
************************************************************************
```

###  13.6.7 Macro “sensitivityMorrisFunctionFlowrateRunner.py”

####  13.6.7.1 Objective

The objective of this macro is to perform a Morris sensitivity analysis on a set of eight parameters used in the flowrate-
Model model described in Presentation of the problem, but this time using the Relauncher architecture.

#### 13.6.7.2 Macro Uranie

```python
"""
Example of Morris analysis on flowrate with a Relauncher approach
"""
from URANIE import DataServer, Relauncher, Sensitivity
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
rw = DataServer.TUniformDistribution("rw", 0.05, 0.15)
r = DataServer.TUniformDistribution("r", 100.0, 50000.0)
tu = DataServer.TUniformDistribution("tu", 63070.0, 115600.0)
tl = DataServer.TUniformDistribution("tl", 63.1, 116.0)
hu = DataServer.TUniformDistribution("hu", 990.0, 1110.0)
hl = DataServer.TUniformDistribution("hl", 700.0, 820.0)
lvar = DataServer.TUniformDistribution("l", 1120.0, 1680.0)
kw = DataServer.TUniformDistribution("kw", 9855.0, 12045.0)
# Create the evaluator
code = Relauncher.TCIntEval("flowrateModel")
# Create output attribute
yout = DataServer.TAttribute("flowrateModel")
# Provide input/output attributes to the assessor
code.addInput(rw)
code.addInput(r)
code.addInput(tu)
code.addInput(tl)
code.addInput(hu)
code.addInput(hl)
code.addInput(lvar)
code.addInput(kw)
code.addOutput(yout)
run = Relauncher.TSequentialRun(code)
                                       # Replace to distribute computation
run.startSlave()
if run.onMaster():
    # Create the dataserver
    tds = DataServer.TDataServer("sobol", "foo bar pouet chocolat")
    tds.addAttribute(rw)
```

<!-- page 283 (PDF 290) -->
```python
tds.addAttribute(r)
tds.addAttribute(tu)
tds.addAttribute(tl)
tds.addAttribute(hu)
tds.addAttribute(hl)
tds.addAttribute(lvar)
tds.addAttribute(kw)
# Create the Morris object
nreplique = 3
nlevel = 10
scmo = Sensitivity.TMorris(tds, run, nreplique, nlevel)
scmo.setDrawProgressBar(False)
scmo.generateSample()
tds.exportData("_morris_sampling_.dat")
scmo.computeIndexes()
tds.exportData("_morris_launching_.dat")
ntresu = scmo.getMorrisResults()
ntresu.Scan("*")
# Graph
canmoralltraj = ROOT.gROOT.FindObject("canmoralltraj")
can = ROOT.TCanvas("c1", "Graph sensitivityMorrisFunctionFlowrateRunner",
                   5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2)
pad.cd(1)
scmo.drawSample("", -1, "nonewcanv")
pad.cd(2)
scmo.drawIndexes("mustar", "", "nonewcanv")
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval:

```python
# Define the DataServer
rw = DataServer.TUniformDistribution("rw", 0.05, 0.15)
r = DataServer.TUniformDistribution("r", 100.0, 50000.0)
tu = DataServer.TUniformDistribution("tu", 63070.0, 115600.0)
tl = DataServer.TUniformDistribution("tl", 63.1, 116.0)
hu = DataServer.TUniformDistribution("hu", 990.0, 1110.0)
hl = DataServer.TUniformDistribution("hl", 700.0, 820.0)
lvar = DataServer.TUniformDistribution("l", 1120.0, 1680.0)
kw = DataServer.TUniformDistribution("kw", 9855.0, 12045.0)
```

The interface to the function is then defined, using the Relauncher interface, through a TCIntEval object and a sequential

<!-- page 284 (PDF 291) -->
runner. On the contrary to the C++ script, python cannot use methods such as setInputs or setOutputs and the inputs
and outputs have to be included ony-by-one.

```python
# Create the evaluator
code = Relauncher.TCIntEval("flowrateModel")
# Create output attribute
yout = DataServer.TAttribute("flowrateModel")
# Provide input/output attributes to the assessor
code.addInput(rw)
code.addInput(r)
code.addInput(tu)
code.addInput(tl)
code.addInput(hu)
code.addInput(hl)
code.addInput(lvar)
code.addInput(kw)
code.addOutput(yout)
run = Relauncher.TSequentialRun(code)
                                       # Replace to distribute computation
run.startSlave()
```

The dataserver object is defined only on the master to avoid useless replication if one wants to run the estimation of the
function in parallel (by changing the TSequentialRun by either a TThreadedRun or a TMpiRun). To instantiate the
TMorris object, one uses the TDataServer, a pointer to the chosen runner, the number of replicas (here nreplique=3),
the level parameter (here nlevel=10)

```python
scmo = Sensitivity.TMorris(tds, run, nreplique, nlevel)
```

Creation of the sampling:

```python
scmo.generateSample()
```

Data are exported in an ASCII file:

```python
tds.exportData("_morris_sampling_.dat")
```

Computation of sensitivity indexes:

```python
scmo.computeIndexes()
```

The rest of the code is providing command to get a final plot.

<!-- page 285 (PDF 292) -->
#### 13.6.7.3 Graph

Figure 13.23: Graph of the macro “sensitivityMorrisFunctionFlowrateRunner.py”

#### 13.6.7.4 Console

```python
************************************************************************
*
     Row
           *
                 Input *
                            Output *
                                         mu.mu * mustar.mu * sigma.sig *
************************************************************************
*
         0 *
                    rw * flowrateM * 127.47900 * 127.47900 * 34.521839 *
*
         1 *
                     r * flowrateM * -0.069601 * 0.0696013 * 0.0793689 *
*
         2 *
                    tu * flowrateM * 0.0004201 * 0.0004201 * 0.0004641 *
*
         3 *
                    tl * flowrateM * 0.4659763 * 0.4659763 * 0.3301256 *
*
         4 *
                    hu * flowrateM * 21.192361 * 21.192361 * 8.8498989 *
*
         5 *
                    hl * flowrateM * -32.74887 * 32.748874 * 30.146134 *
*
         6 *
                     l * flowrateM * -23.89328 * 23.893280 * 8.2781934 *
*
         7 *
                    kw * flowrateM * 7.5766167 * 7.5766167 * 2.7457665 *
************************************************************************
```

###  13.6.8 Macro “sensitivityRegressionFunctionFlowrate.py”

####  13.6.8.1 Objective

The objective of this macro is to perform a regression with “SRC” method on a database generated with a function using
sampling of parameters obeying uniform laws with 4000 patterns. flowrateModel is a function defined in Presentation
of the problem and “loaded” through the macro UserFunctions.C (the file can be found in ${URANIESYS}/share/
uranie/macros). Function flowrateModel uses the eight variables defined in Presentation of the problem and set in
the main macro.

<!-- page 286 (PDF 293) -->
#### 13.6.8.2 Macro Uranie

```python
"""
Example of regression approach on the flowrate function
"""
from URANIE import DataServer, Launcher, Sampler, Sensitivity
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
# Size of a sampling.
nS = 4000
sampling = Sampler.TSampling(tds, "lhs", nS)
sampling.generateSample()
tlf = Launcher.TLauncherFunction(tds, "flowrateModel")
tlf.setDrawProgressBar(False)
tlf.run()
treg = Sensitivity.TRegression(tds, "rw:r:tu:tl:hu:hl:l:kw",
                               "flowrateModel", "SRC")
treg.computeIndexes()
treg.getResultTuple().SetScanField(60)
treg.getResultTuple().Scan("Out:Inp:Method:Algo:Value:CILower:CIUpper",
                           "Order==\"First\"","colsize=5 col=6:8::9:8:8:8")
can = ROOT.TCanvas("c1", "Graph sensitivityRegressionFunctionFlowrate",
                   5, 64, 1270, 667)
treg.drawIndexes("Flowrate", "", "hist, first, nonewcanv")
```

Each attribute is related to a TAttribute obeying uniform laws on specific intervals:

```python
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

<!-- page 287 (PDF 294) -->
The sampling is generated on 4000 patterns with a LHS method:

```python
sampling = Sampler.TSampling(tds, "lhs", nS)
sampling.generateSample()
```

Function flowrateModel is set to perform calculation on the sampling:

```python
tlf = Launcher.TLauncherFunction(tds, "flowrateModel")
tlf.run()
```

The regression is performed over all variables:

```python
treg = Sensitivity.TRegression(tds, "rw:r:tu:tl:hu:hl:l:kw",
                               "flowrateModel", "SRC")
treg.computeIndexes()
```

Sensitivity indexes are then displayed through an histogram:

```python
can = ROOT.TCanvas("c1", "Graph sensitivityRegressionFunctionFlowrate",
                   5, 64, 1270, 667)
treg.drawIndexes("Flowrate", "", "hist, first, nonewcanv")
```

####  13.6.8.3 Graph

Figure 13.24: Graph of the macro “sensitivityRegressionFunctionFlowrate.py”

#### 13.6.8.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
```

<!-- page 288 (PDF 295) -->
```python
                      Date: Thu Feb 12, 2026
*************************************************************************************
*
     Row
           *
                Out *
                           Inp * Metho *
                                              Algo *
                                                        Value *
                                                                 CILower *
                                                                            CIUpper *
*************************************************************************************
*
         0 * flowra *
                            rw * SRC^2 * --first-- * 0.820265 *
                                                                      -1 *
                                                                                 -1 *
*
         2 * flowra *
                            rw * SRC^2 * --rho^2-- *
                                                      0.81668 * 0.805846 * 0.826888 *
*
         4 * flowra *
                             r * SRC^2 * --first-- * 5.97e-06 *
                                                                      -1 *
                                                                                 -1 *
*
         6 * flowra *
                             r * SRC^2 * --rho^2-- * 1.92e-06 * 2.65e-07 * 0.001339 *
*
         8 * flowra *
                            tu * SRC^2 * --first-- * 8.64e-06 *
                                                                      -1 *
                                                                                 -1 *
*
        10 * flowra *
                            tu * SRC^2 * --rho^2-- * 4.03e-06 * 3.14e-07 * 0.001306 *
*
        12 * flowra *
                            tl * SRC^2 * --first-- * 5.73e-05 *
                                                                      -1 *
                                                                                 -1 *
*
        14 * flowra *
                            tl * SRC^2 * --rho^2-- * 0.000209 * 7.34e-07 * 0.002085 *
*
        16 * flowra *
                            hu * SRC^2 * --first-- * 0.039645 *
                                                                      -1 *
                                                                                 -1 *
*
        18 * flowra *
                            hu * SRC^2 * --rho^2-- * 0.037119 * 0.026221 * 0.049000 *
*
        20 * flowra *
                            hl * SRC^2 * --first-- * 0.040597 *
                                                                      -1 *
                                                                                 -1 *
*
        22 * flowra *
                            hl * SRC^2 * --rho^2-- * 0.039708 * 0.028688 * 0.052470 *
*
        24 * flowra *
                             l * SRC^2 * --first-- * 0.040895 *
                                                                      -1 *
                                                                                 -1 *
*
        26 * flowra *
                             l * SRC^2 * --rho^2-- * 0.041241 * 0.029896 * 0.054454 *
*
        28 * flowra *
                            kw * SRC^2 * --first-- * 0.009174 *
                                                                      -1 *
                                                                                 -1 *
*
        30 * flowra *
                            kw * SRC^2 * --rho^2-- * 0.009090 * 0.004191 * 0.015767 *
*
        32 * flowra *
                       __sum__ * SRC^2 * --first-- *
                                                      0.95065 *
                                                                      -1 *
                                                                                 -1 *
*
        34 * flowra *
                        __R2__ * SRC^2 * --first-- * 0.947296 *
                                                                      -1 *
                                                                                 -1 *
*
        36 * flowra *
                       __R2A__ * SRC^2 * --first-- *
                                                      0.94719 *
                                                                      -1 *
                                                                                 -1 *
*************************************************************************************
==> 19 selected entries
```

###  13.6.9 Macro “sensitivitySobolFunctionFlowrate.py”

####  13.6.9.1 Objective

The objective of this macro is to perform Sobol sensitivity analysis on a set of eight parameters used in the flowrate-
Model model described in Presentation of the problem.

#### 13.6.9.2 Macro Uranie

```python
"""
Example of Sobol estimation for the flowrate function
"""
from URANIE import DataServer, Sensitivity
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
```

<!-- page 289 (PDF 296) -->
```python
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
ns = 100000
tsobol = Sensitivity.TSobol(tds, "flowrateModel", ns, "rw:r:tu:tl:hu:hl:l:kw",
                            "flowrateModel", "DummyPython")
tsobol.setDrawProgressBar(False)
tsobol.computeIndexes()
tsobol.getResultTuple().Scan("*", "Algo==\"--first--\" || Algo==\"--total--\"")
cc = ROOT.TCanvas("c1", "histgramme", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2, 1)
pad.cd(1)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, hist, all")
pad.cd(2)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, pie, first")
ROOT.gSystem.Rename("_sobol_launching_.dat", "ref_sobol_launching_.dat")
tds.exportData("_onlyMandN_sobol_launching_.dat",
               "rw:r:tu:tl:hu:hl:l:kw:flowrateModel",
               "sobol__n__iter__tdsflowreate < 100")
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval:

```python
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

To instantiate the TSobol, one uses the TDataServer, the name of the function and the number of samplings needed
to perform sensitivity analysis (here ns=600):

```python
tsobol = Sensitivity.TSobol(tds, "flowrateModel", ns, "rw:r:tu:tl:hu:hl:l:kw",
                            "flowrateModel", "DummyPython")
```

The last argument is the option field, which in most cases is empty. Here it is filled with “DummyPython” which helps
specify to python which constructor to choose. There are indeed several possible constructors these 5 five first arguments,
but C++ can make the difference between them as the literal members are either std::string, ROOT::TString,
Char_t* or even Option_t*. For python, these format are all PyString, so the sixth argument is compulsory to

<!-- page 290 (PDF 297) -->
disentangle the possibilities.
Computation of the sensitivity indexes:

```python
tsobol.computeIndexes()
```

Data are exported from the TDataServer to an ASCII file:

```python
tds.exportData("_onlyMandN_sobol_launching_.dat",
               "rw:r:tu:tl:hu:hl:l:kw:flowrateModel",
               "sobol__n__iter__tdsflowreate < 100")
```

####  13.6.9.3 Graph

Figure 13.25: Graph of the macro “sensitivitySobolFunctionFlowrate.py”

<!-- page 291 (PDF 298) -->
#### 13.6.9.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
            Copyright (C) 2013-2026 CEA/DES
                     Contact: support-uranie@cea.fr
                    Date: Thu Feb 12, 2026
                                                                                                                 <URANIE::WARNING>
                                                                                                                                        <URANIE::WARNING> *** URANIE WARNING ***
                                                                                                                                                               <URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[8531]
                                                                                                                                                                                     <URANIE::WARNING> TDataServer::getTuple Error : There is no tree!
                                                                                                                                                                                                            <URANIE::WARNING> *** END of URANIE WARNING ***
                                                                                                                                                                                                                                   <URANIE::WARNING>
                                                                                                                                                                                                             <URANIE::INFO>
                                                                                                                                                                                                                                <URANIE::INFO> *** URANIE INFORMATION ***
                                                                                                                                                                                                                                                   <URANIE::INFO> *** File[${SOURCEDIR}/meTIER/sampler/souRCE/TSamplerStochastic.cxx] Line[66]
                                                                                                                                                                                                                                                                     <URANIE::INFO> TSamplerStochastic::init: the TDS [tdsflowreate] contains data: we need to empty it !
                                                                                                                                                                                                                                                                                        <URANIE::INFO> *** END of URANIE INFORMATION ***
                                                                                                                                                                                                                                                                                                           <URANIE::INFO>
                                             ** Case of Output atty [flowrateModel]
                                                                                                                                                                                                                                                                                nSimPerIndex 10000
                                                ** Input att [rw] First [0.830033] Total Order[0.865762]
                                                   ** Input att [r] First [0] Total Order[0.000102212]
                                                     ** Input att [tu] First [0] Total Order[0.0001]
                                                        ** Input att [tl] First [0] Total Order[0.000110756]
                                                           ** Input att [hu] First [0.0417298] Total Order[0.0554922]
                                                             ** Input att [hl] First [0.0367345] Total Order[0.0526188]
                                                                ** Input att [l] First [0.0384214] Total Order[0.0535728]
                                                                   ** Input att [kw] First [0.00669831] Total Order[0.0132316]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ************************************************************************************************************
                                    *
                                                                                                            Row
                                    *
                                                                                                                                                                                                                                                            Out.Out *
                                                                                                                                                                                                                                                            Inp.Inp * Order.Ord * Method.Me * Algo.Algo * Value.Val * CILower.C * CIUpper.C *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ************************************************************************************************************
                                       *
                                       0 * flowrateM *
                                                                             rw *
                                                                                                                                                                                                 First *
                                                                                                                                                                                                 Sobol * --first-- * 0.8300331 * 0.8238356 * 0.8360321 *
                                        *
                                        4 * flowrateM *
                                                                                rw *
                                                                                                                                                                                                        Total *
                                                                                                                                                                                                        Sobol * --total-- * 0.8657619 * 0.8465652 * 0.8850599 *
                                         *
                                         8 * flowrateM *
                                         r *
                                                                                                                                                                                                               First *
                                                                                                                                                                                                               Sobol * --first-- *
                                         0 *
                                         0 * 0.0196004 *
                                           *
                                                                                     12 * flowrateM *
                                           r *
                                                                                                                                                                                                                     Total *
                                                                                                                                                                                                                     Sobol * --total-- * 0.0001022 * 9.828e-05 * 0.0001062 *
                                            *
                                                                                        16 * flowrateM *
                                                                                        tu *
                                                                                                                                                                                                                            First *
                                                                                                                                                                                                                            Sobol * --first-- *
                                            0 *
                                            0 * 0.0196004 *
                                             *
                                                                                           20 * flowrateM *
                                                                                           tu *
                                                                                                                                                                                                                                   Total *
                                                                                                                                                                                                                                   Sobol * --total-- * 0.0001000 * 9.615e-05 * 0.0001039 *
                                               *
                                                                                             24 * flowrateM *
                                                                                             tl *
                                                                                                                                                                                                                                         First *
                                                                                                                                                                                                                                         Sobol * --first-- *
                                               0 *
                                               0 * 0.0196004 *
```

<!-- page 292 (PDF 299) -->
```python
*
28 * flowrateM *
tl *
Total *
Sobol * --total-- * 0.0001107 * 0.0001064 * 0.0001151 *
 *
   32 * flowrateM *
   hu *
       First *
       Sobol * --first-- * 0.0417297 * 0.0221474 * 0.0612800 *
   *
     36 * flowrateM *
     hu *
             Total *
             Sobol * --total-- * 0.0554921 * 0.0534156 * 0.0576470 *
    *
        40 * flowrateM *
        hl *
                    First *
                    Sobol * --first-- * 0.0367345 * 0.0171464 * 0.0562944 *
     *
           44 * flowrateM *
           hl *
                           Total *
                           Sobol * --total-- * 0.0526187 * 0.0506469 * 0.0546652 *
       *
             48 * flowrateM *
       l *
                                 First *
                                 Sobol * --first-- * 0.0384214 * 0.0188352 * 0.0579782 *
        *
                52 * flowrateM *
        l *
                                        Total *
                                        Sobol * --total-- * 0.0535727 * 0.0515661 * 0.0556552 *
         *
                   56 * flowrateM *
                   kw *
                                               First *
                                               Sobol * --first-- * 0.0066983 *
         0 * 0.0262952 *
           *
                     60 * flowrateM *
                     kw *
                                                     Total *
                                                     Sobol * --total-- * 0.0132315 * 0.0127261 * 0.0137570 *
            *
                        64 * flowrateM *
                                                                                    __sum__ *
                                                            First *
                                                            Sobol * --first-- * 0.9536171 *
                        -1 *
                        -1 *
             *
                           65 * flowrateM *
                                                                                             __sum__ *
                                                                   Total *
                                                                   Sobol * --total-- * 1.0409902 *
                           -1 *
                           -1 *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ************************************************************************************************************
                                                ==> 18 selected entries
```

<!-- page 293 (PDF 300) -->
### 13.6.10 Macro “sensitivitySobolFunctionFlowrateRunner.py”

#### 13.6.10.1 Objective

The objective of this macro is to perform Sobol sensitivity analysis on a set of eight parameters used in the flowrate-
Model model described in Presentation of the problem, but this time using the Relauncher architecture.

#### 13.6.10.2 Macro Uranie

```python
"""
Example of Sobol estimation for the flowrate function with Relauncher approach
"""
from URANIE import DataServer, Relauncher, Sensitivity
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
rw = DataServer.TUniformDistribution("rw", 0.05, 0.15)
r = DataServer.TUniformDistribution("r", 100.0, 50000.0)
tu = DataServer.TUniformDistribution("tu", 63070.0, 115600.0)
tl = DataServer.TUniformDistribution("tl", 63.1, 116.0)
hu = DataServer.TUniformDistribution("hu", 990.0, 1110.0)
hl = DataServer.TUniformDistribution("hl", 700.0, 820.0)
lvar = DataServer.TUniformDistribution("l", 1120.0, 1680.0)
kw = DataServer.TUniformDistribution("kw", 9855.0, 12045.0)
# Create the evaluator
code = Relauncher.TCIntEval("flowrateModel")
# Create output attribute
yout = DataServer.TAttribute("flowrateModel")
# Provide input/output attributes to the assessor
code.addInput(rw)
code.addInput(r)
code.addInput(tu)
code.addInput(tl)
code.addInput(hu)
code.addInput(hl)
code.addInput(lvar)
code.addInput(kw)
code.addOutput(yout)
run = Relauncher.TSequentialRun(code)
                                       # Replace to distribute computation
run.startSlave()
if run.onMaster():
    # Create the dataserver
    tds = DataServer.TDataServer("sobol", "foo bar pouet chocolat")
    code.addAllInputs(tds)
    # Create the sobol object
    ns = 100000
    tsobol = Sensitivity.TSobol(tds, run, ns)
    tsobol.setDrawProgressBar(ROOT.kFALSE)
    tsobol.computeIndexes()
```

<!-- page 294 (PDF 301) -->
```python
cc = ROOT.TCanvas("c1", "histgramme", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2, 1)
pad.cd(1)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, hist, all")
pad.cd(2)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, pie, first")
tds.exportData("_sobol_launching_.dat")
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval:

```python
# Define the DataServer
rw = DataServer.TUniformDistribution("rw", 0.05, 0.15)
r = DataServer.TUniformDistribution("r", 100.0, 50000.0)
tu = DataServer.TUniformDistribution("tu", 63070.0, 115600.0)
tl = DataServer.TUniformDistribution("tl", 63.1, 116.0)
hu = DataServer.TUniformDistribution("hu", 990.0, 1110.0)
hl = DataServer.TUniformDistribution("hl", 700.0, 820.0)
lvar = DataServer.TUniformDistribution("l", 1120.0, 1680.0)
kw = DataServer.TUniformDistribution("kw", 9855.0, 12045.0)
```

The interface to the function is then defined, using the Relauncher interface, through a TCIntEval object and a sequential
runner:

```python
# Create the evaluator
code = Relauncher.TCIntEval("flowrateModel")
# Create output attribute
yout = DataServer.TAttribute("flowrateModel")
# Provide input/output attributes to the assessor
code.addInput(rw)
code.addInput(r)
code.addInput(tu)
code.addInput(tl)
code.addInput(hu)
code.addInput(hl)
code.addInput(lvar)
code.addInput(kw)
code.addOutput(yout)
run = Relauncher.TSequentialRun(code)
                                       # Replace to distribute computation
run.startSlave()
```

To instantiate the TSobol, one uses the TDataServer, a pointer to the runner and the number of samplings needed to
perform sensitivity analysis (here ns=600):

<!-- page 295 (PDF 302) -->
```python
tsobol = Sensitivity.TSobol(tds, run, ns)
```

Computation of the sensitivity indexes:

```python
tsobol.computeIndexes()
```

Data are exported from the TDataServer to an ASCII file:

```python
tds.exportData("_sobol_launching_.dat")
```

####  13.6.10.3 Graph

Figure 13.26: Graph of the macro “sensitivitySobolFunctionFlowrateRunner.py”

#### 13.6.10.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
 <URANIE::WARNING>
 <URANIE::WARNING> *** URANIE WARNING ***
 <URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[8531]
 <URANIE::WARNING> TDataServer::getTuple Error : There is no tree!
 <URANIE::WARNING> *** END of URANIE WARNING ***
 <URANIE::WARNING>
 <URANIE::INFO>
 <URANIE::INFO> *** URANIE INFORMATION ***
 <URANIE::INFO> *** File[${SOURCEDIR}/meTIER/sampler/souRCE/TSamplerStochastic.cxx]␣
```

<!-- page 296 (PDF 303) -->
˓→Line[66]

```python
<URANIE::INFO> TSamplerStochastic::init: the TDS [sobol] contains data: we need to␣
```

˓→empty it !

```python
<URANIE::INFO> *** END of URANIE INFORMATION ***
<URANIE::INFO>
** Case of Output atty [flowrateModel]
                                        nSimPerIndex 10000
** Input att [rw] First [0.830033] Total Order[0.865762]
** Input att [r] First [0] Total Order[0.000102212]
** Input att [tu] First [0] Total Order[0.0001]
** Input att [tl] First [0] Total Order[0.000110756]
** Input att [hu] First [0.0417298] Total Order[0.0554922]
** Input att [hl] First [0.0367345] Total Order[0.0526188]
** Input att [l] First [0.0384214] Total Order[0.0535728]
** Input att [kw] First [0.00669831] Total Order[0.0132316]
```

###  13.6.11 Macro “sensitivityRegressionLeveLE.py”

Exclamation-Triangle Warning
The levele command will be installed on your machine only if a Fortran compiler is found

#### 13.6.11.1 Objective

The objective of this macro is to perform a SRC and SRRC measurement on the temporal use-case levele. This use-case
is an example of code that takes a dozen of entries in order to compute the evolution of dose as a function of time. The
result of every computation consists in 3 vectors: the time (always the same value disregarding all entries), the dose called
“y” and a third useless information.

#### 13.6.11.2 Macro Uranie

```python
"""
Example of regression analysis on the levelE code
"""
import sys
from ctypes import c_double
                             # for ROOT version greater or equal to 6.20
import numpy as np
from URANIE import Launcher, Sampler, Sensitivity
from URANIE import DataServer as DS
import ROOT
# Create DataServer and add input attributes
tds = DS.TDataServer("tds", "levelE usecase")
tds.addAttribute(DS.TUniformDistribution("t", 100, 1000))
tds.addAttribute(DS.TLogUniformDistribution("kl", 0.001, .01))
tds.addAttribute(DS.TLogUniformDistribution("kc", 1.0e-6, 1.0e-5))
tds.addAttribute(DS.TLogUniformDistribution("v1", 1.0e-3, 1.0e-1))
tds.addAttribute(DS.TUniformDistribution("l1", 100., 500.))
tds.addAttribute(DS.TUniformDistribution("r1", 1., 5.))
tds.addAttribute(DS.TUniformDistribution("rc1", 3., 30.))
tds.addAttribute(DS.TLogUniformDistribution("v2", 1.0e-2, 1.0e-1))
```

<!-- page 297 (PDF 304) -->
```python
tds.addAttribute(DS.TUniformDistribution("l2", 50., 200.))
tds.addAttribute(DS.TUniformDistribution("r2", 1., 5.))
tds.addAttribute(DS.TUniformDistribution("rc2", 3., 30.))
tds.addAttribute(DS.TLogUniformDistribution("w", 1.0e5, 1.0e7))
# Tell the code where to find attribute value in input file
sIn = "levelE_input_with_values_rows.in"
tds.getAttribute("t").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("kl").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("kc").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("v1").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("l1").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("r1").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("rc1").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("v2").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("l2").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("r2").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("rc2").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
tds.getAttribute("w").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
# Create DOE
ns = 1024
samp = Sampler.TSampling(tds, "lhs", ns)
samp.generateSample()
# How to read ouput files
out = Launcher.TOutputFileRow("_output_levelE_withRow_.dat")
# Tell the output file that attribute IS a vector and is SECOND column
out.addAttribute(DS.TAttribute("y", DS.TAttribute.kVector), 2)
# Creation of Launcher.TCode
myc = Launcher.TCode(tds, " levele 2> /dev/null")
myc.addOutputFile(out)
# Run the code
tl = Launcher.TLauncher(tds, myc)
tl.run(args.runOpt) # args.runOpt = "" or "nointermed"
# Launch Regression
tsen = Sensitivity.TRegression(tds, "t:kl:kc:v1:l1:r1:rc1:v2:l2:r2:rc2:w",
                               "y", "SRCSRRC")
tsen.computeIndexes()
res = tsen.getResultTuple()
# Plotting mess
tps = np.array([20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,
                200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000,
                1e+06, 2e+06, 3e+06, 4e+06, 5e+06, 6e+06, 7e+06, 8e+06, 9e+06],
               dtype=float)
colors = [1, 2, 3, 4, 6, 7, 8, 15, 30, 38, 41, 46]
c2 = ROOT.TCanvas("c2", "c2", 5, 64, 1600, 500)
```

<!-- page 298 (PDF 305) -->
```python
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(3, 1)
pad.cd(1)
ROOT.gPad.SetLogx()
ROOT.gPad.SetGrid()
mg = ROOT.TMultiGraph()
res.Draw("Value", "Inp==\"__R2__\" && Order==\"Total\" && Method==\"SRRC^2\"",
         "goff")
data3 = res.GetV1()
gr3 = ROOT.TGraph(26, tps, data3)
gr3.SetMarkerColor(2)
gr3.SetLineColor(2)
gr3.SetMarkerStyle(23)
mg.Add(gr3)
res.Draw("Value", "Inp==\"__R2__\" && Order==\"Total\" && Method==\"SRC^2\"",
         "goff")
data4 = res.GetV1()
gr4 = ROOT.TGraph(26, tps, data4)
gr4.SetMarkerColor(4)
gr4.SetLineColor(4)
gr4.SetMarkerStyle(23)
mg.Add(gr4)
mg.Draw("APC")
mg.GetXaxis().SetTitle("Time")
mg.GetYaxis().SetTitle("#sum Sobol")
mg.GetYaxis().SetRangeUser(0.0, 1.0)
# Legend
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetFillStyle(0)
lg = ROOT.TLegend(0.25, 0.7, 0.45, 0.9)
lg.AddEntry(gr4, "R2 SRC", "lp")
lg.AddEntry(gr3, "R2 SRRC", "lp")
lg.Draw()
pad.cd(2)
ROOT.gPad.SetLogx()
ROOT.gPad.SetGrid()
mg2 = ROOT.TMultiGraph()
names = ["t", "kl", "kc", "v1", "l1", "r1", "rc1",
         "v2", "l2", "r2", "rc2", "w"]
src = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
leg = ROOT.TLegend(0.25, 0.3, 0.45, 0.89, "Cumulative contributions")
leg.SetTextSize(0.035)
for igr in range(12):
```

<!-- page 299 (PDF 306) -->
```python
    sel = "Inp==\""+names[igr]+"\""
    sel += "&& Order==\"Total\" && Method==\"SRC^2\" && Algo!=\"--rho^2--\""
    res.Draw("Value", sel, "goff")
    data = res.GetV1()
    src[igr] = ROOT.TGraph()
    src[igr].SetMarkerColor(colors[igr])
    src[igr].SetLineColor(colors[igr])
    src[igr].SetFillColor(colors[igr])
    src[igr].SetPoint(0, 0.99999999*tps[0], 0)
    for ip in range(26):
        x = c_double(0)
        y = c_double(0)
                         # For ROOT lower than 6.20, user ROOT.Double
        if igr != 0:
            src[igr-1].GetPoint(ip+1, x, y)
        src[igr].SetPoint(ip+1, tps[ip], y.value+data[ip])
    src[igr].SetPoint(27, tps[25]*1.000000001, 0)
    leg.AddEntry(src[igr], names[igr], "f")
for igr2 in range(11, -1, -1):
    mg2.Add(src[igr2])
mg2.Draw("AFL")
mg2.GetXaxis().SetTitle("Time")
mg2.GetYaxis().SetTitle("SRC^{2}")
mg2.GetYaxis().SetRangeUser(0.0, 0.3)
leg.Draw()
pad.cd(3)
ROOT.gPad.SetLogx()
ROOT.gPad.SetGrid()
mg3 = ROOT.TMultiGraph()
srrc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for igr in range(12):
    sel = "Inp==\""+names[igr]+"\""
    sel += "&& Order==\"Total\" && Method==\"SRRC^2\" && Algo!=\"--rho^2--\""
    res.Draw("Value", sel, "goff")
    data = res.GetV1()
    srrc[igr] = ROOT.TGraph()
    srrc[igr].SetMarkerColor(colors[igr])
    srrc[igr].SetLineColor(colors[igr])
    srrc[igr].SetFillColor(colors[igr])
    srrc[igr].SetPoint(0, 0.99999999*tps[0], 0)
    for ip in range(26):
        x = c_double(0)
        y = c_double(0)
                         # For ROOT lower than 6.20, user ROOT.Double
        if igr != 0:
            srrc[igr-1].GetPoint(ip+1, x, y)
```

<!-- page 300 (PDF 307) -->
```python
        srrc[igr].SetPoint(ip+1, tps[ip], y.value+data[ip])
    srrc[igr].SetPoint(27, tps[25]*1.000000001, 0)
    srrc[igr].SetTitle(names[igr])
for igr2 in range(11, -1, -1):
    mg3.Add(srrc[igr2])
# mg3.Draw("a fb l3d")
mg3.Draw("AFL")
mg3.GetXaxis().SetTitle("Time")
mg3.GetYaxis().SetTitle("SRRC^{2}")
mg3.GetYaxis().SetRangeUser(0.0, 1.0)
leg.Draw()
```

The levele external code is located in the bin directory of the Uranie installation.
When looking at the code and comparing it to an usual Regression estimation, the organisation is completely transparent.
The only noticeable (and compulsory) thing to do is to change the default type of the attribute read at the end of the job.
This is done in this line:

```python
out.addAttribute(DS.TAttribute("y", DS.TAttribute.kVector), 2)
```

where the output attribute is provided, changing its nature to a vector, thanks to the second argument of the TAttribute
constructor from the default (kReal) to the desired nature (kVector). Once this is done, this information is broadcast
internally to the code that knows how to deal with this type of attribute.
The rest of the code is the graphical part, leading to the figure below (it is provided to illustrate how to represent results).

#### 13.6.11.3 Graph

The results of the previous macro is shown in Figure 13.27, where the left panel represents the value of the 𝑅2 coefficients
both the SRC and SRRC coefficients estimation. The middle and right panel display the cumulative sum of the quadratic
value of the coefficient respectively for the SRC and SRRC case.
Figure 13.27: Graph of the macro “sensitivityRegressionLeveLE.py”
