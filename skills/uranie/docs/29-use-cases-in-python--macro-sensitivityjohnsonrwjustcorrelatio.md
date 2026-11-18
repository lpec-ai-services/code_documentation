# Use-cases in Python — Macros Launcher — Macro “sensitivityJohnsonRWJustCorrelationFakeFlowrate.py” … Macro “sensitivitySobolRankFunctionFlowrate.py”
<!-- source PDF pages 327-336 -->

<!-- page 320 (PDF 327) -->
```python
  6 |
         -0.1943
                                 -0.4415
  7 |
          0.2848
                     -0.4415
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

˓→Line[66]

```python
<URANIE::INFO> TSamplerStochastic::init: the TDS [tdsflowrate] contains data: we␣
```

˓→need to empty it !

```python
 <URANIE::INFO> *** END of URANIE INFORMATION ***
 <URANIE::INFO>
************************************************************
*
     Row
           *
                   Out *
                               Inp *
                                        Method *
                                                     Value *
************************************************************
*
         0 * flowrateM *
                                rw * JohnsonRW * 0.5113911 *
*
         2 * flowrateM *
                                 r * JohnsonRW * 0.1409327 *
*
         4 * flowrateM *
                                tu * JohnsonRW * 0.0505176 *
*
         6 * flowrateM *
                                tl * JohnsonRW * 0.0482684 *
*
         8 * flowrateM *
                                hu * JohnsonRW * 0.0969452 *
*
        10 * flowrateM *
                                hl * JohnsonRW * 0.0306674 *
*
        12 * flowrateM *
                                 l * JohnsonRW * 0.0836757 *
*
        14 * flowrateM *
                                kw * JohnsonRW * 0.0376016 *
*
        16 * flowrateM *
                            __R2__ * JohnsonRW * 0.9500813 *
*
        18 * flowrateM *
                           __R2A__ * JohnsonRW * 0.9496787 *
************************************************************
==> 10 selected entries
```

###  13.6.18 Macro “sensitivityJohnsonRWJustCorrelationFakeFlowrate.py”

####  13.6.18.1 Objective

The objective of this macro is to perform a sensitivity analysis using the Johnson’s relative weight method on a set of
eight parameters which IS NOT the usual flowrateModel model. Indeed, compared to version detailled in Macro
“sensitivityJohnsonRWCorrelatedFunctionFlowrate.py”, the idea is here to correlate the input variables with a random
correlation matrix and to translate this into a full correlation matrix, meaning defining a “fake” output by computing their
covariance with every input as if this output was a perfect linear combination of these inputs.
An important particularity of this study is that no data are generated at all, it only uses the correlation matrix.

#### 13.6.18.2 Macro Uranie

```python
"""
Example of Johnson relative weight applied only to a correlation matrix
"""
from math import sqrt
from URANIE import DataServer, Sensitivity
```

<!-- page 321 (PDF 328) -->
```python
import ROOT
def gen_corr(_nx=8, correlated=True, seed=0):
    """Generate randomly a good, highly-correlated, correlation matrix for inputs
    define the proper covariance with the output to do as if this output if a
    perfect linear combination of the inputs."""
    # Define a randomly filled matrix
    a_mat = ROOT.TMatrixD(_nx, _nx)
    for i in range(_nx):
        for j in range(_nx):
            a_mat[i][j] = ROOT.gRandom.Gaus(0, 1)
    # Compute AA^T and normalise it to get "covariance matrix"
    gamma = ROOT.TMatrixD(a_mat, ROOT.TMatrixD.kMultTranspose, a_mat)
    gamma *= 1. / _nx
    # Inverse of the diagonal matrix to do as if this was 1/sqrt(variance)
    sig = ROOT.TMatrixD(_nx, _nx)
    for i in range(_nx):
        sig[i][i] = 1. / sqrt(gamma[i][i])
    # Compute the input correlation matrix
    in_corr_right = ROOT.TMatrixD(gamma, ROOT.TMatrixD.kMult, sig)
    in_corr = ROOT.TMatrixD(sig, ROOT.TMatrixD.kMult, in_corr_right)
    if not correlated:
        in_corr.UnitMatrix()
    var_y = in_corr.Sum()
    # Proper correlation, output included
    corr = ROOT.TMatrixD(_nx+1, _nx+1)
    corr.UnitMatrix()
    # putting already defined input
    corr.SetSub(0, 0, in_corr)
    # Adjust the covariance of the output wrt to all inputs
    for i in range(_nx):
        value = 0
        for j in range(_nx):
            value += in_corr[i][j]
        corr[_nx][i] = corr[i][_nx] = value / sqrt(var_y)
    return corr
# Define the DataServer
tds = DataServer.TDataServer("tdsflowrate", "DataBase flowrate")
tds.addAttribute("rw")
tds.addAttribute("r")
tds.addAttribute("tu")
tds.addAttribute("tl")
tds.addAttribute("hu")
tds.addAttribute("hl")
```

<!-- page 322 (PDF 329) -->
```python
tds.addAttribute("l")
tds.addAttribute("kw")
# outputs
tds.addAttribute("flowrateModel")
tds.getAttribute("flowrateModel").setOutput()
# Get the full correlation matrix
inCorr = gen_corr(8, True, args.seed)
# Johnson definition
tjrw = Sensitivity.TJohnsonRW(tds, "rw:r:tu:tl:hu:hl:l:kw", "flowrateModel")
# Putting the newly defined correlation that states our output
# as a perfect linear combination of inputs
tjrw.setCorrelationMatrix(inCorr)
tjrw.computeIndexes()
# Get the results on screen
tjrw.getResultTuple().Scan("Out:Inp:Method:Value", "Order==\"First\"")
# Get the results as plots
cc = ROOT.TCanvas("canhist", "histgramme")
tjrw.drawIndexes("Flowrate", "", "nonewcanv, hist, first")
cc.Print("appliUranieFakeFlowrateJohnsonRWCorrelationHistogram_py.png")
ccc = ROOT.TCanvas("canpie", "TPie")
tjrw.drawIndexes("Flowrate", "", "nonewcanv, pie")
ccc.Print("appliUranieFakeFlowrateJohnsonRWCorrelationPie_py.png")
```

The first function, called GenCorr, is not discussed, because it is really technical and not really interesting here. The only
thing to know is that it provides a proper correlation matrix: a positive-definite symmetrical matrix for the input and it
computes the covariance for a “fake” output that would be a perfect linear combination of all the inputs.
Because of this, the function flowrateModel is not loaded anymore and the definition of the attributes is not the same:
it is not necessary to use TStochasticAttribute because no data are generated here:

```python
# Define the DataServer
tds = DataServer.TDataServer("tdsflowrate", "DataBase flowrate")
tds.addAttribute("rw")
tds.addAttribute("r")
tds.addAttribute("tu")
tds.addAttribute("tl")
tds.addAttribute("hu")
tds.addAttribute("hl")
tds.addAttribute("l")
tds.addAttribute("kw")
# outputs
tds.addAttribute("flowrateModel")
tds.getAttribute("flowrateModel").setOutput()
```

Compared to the discussion in Macro Uranie, the only differences are the instantiation of the TJohnsonRW object and
the method code to provide the correlation matrix.

<!-- page 323 (PDF 330) -->
```python
# Get the full correlation matrix
inCorr = gen_corr(8, True, args.seed)
# Johnson definition
tjrw = Sensitivity.TJohnsonRW(tds, "rw:r:tu:tl:hu:hl:l:kw", "flowrateModel")
# Putting the newly defined correlation that states our output
# as a perfect linear combination of inputs
tjrw.setCorrelationMatrix(inCorr)
```

The method called to provide the correlation matrix is setCorrelationMatrix and it means that the user give a full
correlation matrix (input and output variables), on the contrary to the one used in Macro Uranie which is setInput-
CorrelationMatrix, which set only the input correlation matrix.
The computation of sensitivity indices can finally be done:

```python
tjrw.computeIndexes()
```

The rest is very common to all sensitivity macros discussed here: it will produce two plots (the first one being a histogram
show below) and the console is also shown below for completness.

#### 13.6.18.3 Graph

Figure 13.34: Graph of the macro “sensitivityJohnsonRWJustCorrelationFakeFlowrate.py”

#### 13.6.18.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
 <URANIE::WARNING>
 <URANIE::WARNING> *** URANIE WARNING ***
 <URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[2202]
```

<!-- page 324 (PDF 331) -->
```python
<URANIE::WARNING> TDataServer::getNPatterns[tdsflowrate] WARNING
<URANIE::WARNING>
                   The TTree is NULL
<URANIE::WARNING> *** END of URANIE WARNING ***
<URANIE::WARNING>
<URANIE::WARNING>
<URANIE::WARNING> *** URANIE WARNING ***
<URANIE::WARNING> *** File[${SOURCEDIR}/meTIER/sensitivity/souRCE/TSensitivity.cxx]␣
```

˓→Line[165]

```python
 <URANIE::WARNING> TSensitivity::constructor
                                               ERROR The TTree is empty []
 <URANIE::WARNING> *** END of URANIE WARNING ***
 <URANIE::WARNING>
 <URANIE::WARNING>
 <URANIE::WARNING> *** URANIE WARNING ***
 <URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[8531]
 <URANIE::WARNING> TDataServer::getTuple Error : There is no tree!
 <URANIE::WARNING> *** END of URANIE WARNING ***
 <URANIE::WARNING>
************************************************************
*
     Row
           *
                   Out *
                               Inp *
                                        Method *
                                                     Value *
************************************************************
*
         0 * flowrateM *
                                rw * JohnsonRW * 0.2844573 *
*
         2 * flowrateM *
                                 r * JohnsonRW * 0.1600467 *
*
         4 * flowrateM *
                                tu * JohnsonRW * 0.2004196 *
*
         6 * flowrateM *
                                tl * JohnsonRW * 0.0512434 *
*
         8 * flowrateM *
                                hu * JohnsonRW * 0.0446220 *
*
        10 * flowrateM *
                                hl * JohnsonRW * 0.1295644 *
*
        12 * flowrateM *
                                 l * JohnsonRW * 0.0333889 *
*
        14 * flowrateM *
                                kw * JohnsonRW * 0.0962574 *
*
        16 * flowrateM *
                            __R2__ * JohnsonRW *
                                                         1 *
************************************************************
==> 9 selected entries
```

###  13.6.19 Macro “sensitivityHSICFunctionFlowrate.py”

####  13.6.19.1 Objective

The objective of this macro is to perform a sensitivity analysis using the HSIC method on a set of eight parameters used
in the flowrateModel model described in Presentation of the problem.

#### 13.6.19.2 Macro Uranie

```python
"""
Example of HSIC method applied to flowrate
"""
from URANIE import DataServer, Sensitivity, Launcher, Sampler
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
tds = DataServer.TDataServer("tdsflowrate", "DataBase flowrate")
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
```

<!-- page 325 (PDF 332) -->
```python
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
# Generation of the sample (it can be a given sample).
nS = 500
sampling = Sampler.TSampling(tds, "lhs", nS)
sampling.generateSample()
tlf = Launcher.TLauncherFunction(tds, "flowrateModel")
tlf.setDrawProgressBar(False)
tlf.run()
# Create a THSIC object, compute indexes and print results
thsic = Sensitivity.THSIC(tds, "rw:r:tu:tl:hu:hl:l:kw","flowrateModel")
thsic.computeIndexes("quiet")
thsic.getResultTuple().SetScanField(60)
thsic.getResultTuple().Scan("Out:Inp:Method:Order:Value:CILower:CIUpper","",
```

˓→"colsize=5 col=6:8::9:8:8:8")

```python
# Print HSIC indexes
can = ROOT.TCanvas("c1", "Graph sensitivityHSICFunctionFlowrate", 5, 64, 1270, 667)
thsic.drawIndexes("Flowrate", "", "hist, first, nonewcanv")
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval

```python
# Define the DataServer
tds = DataServer.TDataServer("tdsflowrate", "DataBase flowrate")
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

HSIC does not need a specific DOE, it works with a given sample. We generate a sample with TSampling and we
evaluate it using TLauncherFunction

```python
nS = 500
sampling = Sampler.TSampling(tds, "lhs", nS)
sampling.generateSample()
```

<!-- page 326 (PDF 333) -->
```python
tlf = Launcher.TLauncherFunction(tds, "flowrateModel")
tlf.setDrawProgressBar(False)
tlf.run()
```

To instantiate the THSIC object, one uses the TDataServer, the name of the input and output variables:

```python
thsic = Sensitivity.THSIC(tds, "rw:r:tu:tl:hu:hl:l:kw","flowrateModel")
```

Computation of sensitivity indexes:

```python
thsic.computeIndexes("quiet")
```

It will produce one plots containing the HSIC indexes and the p-value to test the Independance between inputs and
outputs.The console is also shown below for completness.

#### 13.6.19.3 Graph

Figure 13.35: Graph of the macro “sensitivityHSICFunctionFlowrate.py”

#### 13.6.19.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
*************************************************************************************
*
     Row
           *
                Out *
                           Inp * Metho *
                                             Order *
                                                        Value *
                                                                 CILower *
                                                                            CIUpper *
*************************************************************************************
*
         0 * flowra *
                            rw *
                                  HSic *
                                            R2HSic * 0.804431 *
                                                                      -1 *
                                                                                 -1 *
```

<!-- page 327 (PDF 334) -->
```python
*
         1 * flowra *
                            rw *
                                  HSic *
                                              HSic * 0.072723 *
                                                                      -1 *
                                                                                 -1 *
*
         2 * flowra *
                            rw *
                                  HSic *
                                           pValues * 6.8e-106 *
                                                                      -1 *
                                                                                 -1 *
*
         3 * flowra *
                             r *
                                  HSic *
                                            R2HSic * 0.002238 *
                                                                      -1 *
                                                                                 -1 *
*
         4 * flowra *
                             r *
                                  HSic *
                                              HSic * 0.000202 *
                                                                      -1 *
                                                                                 -1 *
*
         5 * flowra *
                             r *
                                  HSic *
                                           pValues * 0.712174 *
                                                                      -1 *
                                                                                 -1 *
*
         6 * flowra *
                            tu *
                                  HSic *
                                            R2HSic * 0.002528 *
                                                                      -1 *
                                                                                 -1 *
*
         7 * flowra *
                            tu *
                                  HSic *
                                              HSic * 0.000228 *
                                                                      -1 *
                                                                                 -1 *
*
         8 * flowra *
                            tu *
                                  HSic *
                                           pValues * 0.662668 *
                                                                      -1 *
                                                                                 -1 *
*
         9 * flowra *
                            tl *
                                  HSic *
                                            R2HSic * 0.003806 *
                                                                      -1 *
                                                                                 -1 *
*
        10 * flowra *
                            tl *
                                  HSic *
                                              HSic * 0.000344 *
                                                                      -1 *
                                                                                 -1 *
*
        11 * flowra *
                            tl *
                                  HSic *
                                           pValues * 0.449068 *
                                                                      -1 *
                                                                                 -1 *
*
        12 * flowra *
                            hu *
                                  HSic *
                                            R2HSic * 0.025554 *
                                                                      -1 *
                                                                                 -1 *
*
        13 * flowra *
                            hu *
                                  HSic *
                                              HSic * 0.002309 *
                                                                      -1 *
                                                                                 -1 *
*
        14 * flowra *
                            hu *
                                  HSic *
                                           pValues * 3.13e-05 *
                                                                      -1 *
                                                                                 -1 *
*
        15 * flowra *
                            hl *
                                  HSic *
                                            R2HSic * 0.020243 *
                                                                      -1 *
                                                                                 -1 *
*
        16 * flowra *
                            hl *
                                  HSic *
                                              HSic * 0.001829 *
                                                                      -1 *
                                                                                 -1 *
*
        17 * flowra *
                            hl *
                                  HSic *
                                           pValues * 0.000445 *
                                                                      -1 *
                                                                                 -1 *
*
        18 * flowra *
                             l *
                                  HSic *
                                            R2HSic * 0.024934 *
                                                                      -1 *
                                                                                 -1 *
*
        19 * flowra *
                             l *
                                  HSic *
                                              HSic * 0.002253 *
                                                                      -1 *
                                                                                 -1 *
*
        20 * flowra *
                             l *
                                  HSic *
                                           pValues * 5.64e-05 *
                                                                      -1 *
                                                                                 -1 *
*
        21 * flowra *
                            kw *
                                  HSic *
                                            R2HSic * 0.010567 *
                                                                      -1 *
                                                                                 -1 *
*
        22 * flowra *
                            kw *
                                  HSic *
                                              HSic * 0.000955 *
                                                                      -1 *
                                                                                 -1 *
*
        23 * flowra *
                            kw *
                                  HSic *
                                           pValues * 0.032459 *
                                                                      -1 *
                                                                                 -1 *
*************************************************************************************
```

###  13.6.20 Macro “sensitivitySobolRankFunctionFlowrate.py”

####  13.6.20.1 Objective

The objective of this macro is to perform a sensitivity analysis using the SobolRank method on a set of eight parameters
used in the flowrateModel model described in Presentation of the problem.

#### 13.6.20.2 Macro Uranie

```python
"""
Example of HSIC method applied to flowrate
"""
from URANIE import DataServer, Sensitivity, Launcher, Sampler
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
tds = DataServer.TDataServer("tdsflowrate", "DataBase flowrate")
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

<!-- page 328 (PDF 335) -->
```python
# Generation of the sample (it can be a given sample).
nS = 500
sampling = Sampler.TSampling(tds, "lhs", nS)
sampling.generateSample()
tlf = Launcher.TLauncherFunction(tds, "flowrateModel")
tlf.setDrawProgressBar(False)
tlf.run()
# Create a TSobolRank object, compute indexes and print results
tsobolrank = Sensitivity.TSobolRank(tds, "rw:r:tu:tl:hu:hl:l:kw","flowrateModel")
tsobolrank.computeIndexes()
tsobolrank.getResultTuple().SetScanField(60)
tsobolrank.getResultTuple().Scan("Out:Inp:Method:Order:Value:CILower:CIUpper","",
```

˓→"colsize=5 col=6:8::9:8:8:8")

```python
# Print Sobol indexes
can = ROOT.TCanvas("c1", "Graph sensitivitySobolRankFunctionFlowrate", 5, 64, 1270,␣
```

˓→667)

```python
tsobolrank.drawIndexes("Flowrate", "", "hist, first, nonewcanv")
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval

```python
# Define the DataServer
tds = DataServer.TDataServer("tdsflowrate", "DataBase flowrate")
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

SobolRank does not need a specific DOE, it works with a given sample. We generate a sample with TSampling and we
evaluate it using TLauncherFunction

```python
nS = 500
sampling = Sampler.TSampling(tds, "lhs", nS)
sampling.generateSample()
tlf = Launcher.TLauncherFunction(tds, "flowrateModel")
tlf.setDrawProgressBar(False)
tlf.run()
```

To instantiate the TSobolRank object, one uses the TDataServer, the name of the input and output variables:

<!-- page 329 (PDF 336) -->
```python
tsobolrank = Sensitivity.TSobolRank(tds, "rw:r:tu:tl:hu:hl:l:kw","flowrateModel")
```

Computation of sensitivity indexes:

```python
tsobolrank.computeIndexes()
```

It will produce one plot containing the first Sobol indices. The console is also shown below for completness.

#### 13.6.20.3 Graph

Figure 13.36: Graph of the macro “sensitivitySobolRankFunctionFlowrate.py”

#### 13.6.20.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
*************************************************************************************
*
     Row
           *
                Out *
                           Inp * Metho *
                                             Order *
                                                        Value *
                                                                 CILower *
                                                                            CIUpper *
*************************************************************************************
*
         0 * flowra *
                            rw * Sobol *
                                             First * 0.816872 *
                                                                      -1 *
                                                                                 -1 *
*
         1 * flowra *
                             r * Sobol *
                                             First * -0.04759 *
                                                                      -1 *
                                                                                 -1 *
*
         2 * flowra *
                            tu * Sobol *
                                             First * -0.04164 *
                                                                      -1 *
                                                                                 -1 *
*
         3 * flowra *
                            tl * Sobol *
                                             First * -0.00414 *
                                                                      -1 *
                                                                                 -1 *
*
         4 * flowra *
                            hu * Sobol *
                                             First * 0.041272 *
                                                                      -1 *
                                                                                 -1 *
*
         5 * flowra *
                            hl * Sobol *
                                             First * 0.036748 *
                                                                      -1 *
                                                                                 -1 *
*
         6 * flowra *
                             l * Sobol *
                                             First * 0.062867 *
                                                                      -1 *
                                                                                 -1 *
*
         7 * flowra *
                            kw * Sobol *
                                             First * 0.021273 *
                                                                      -1 *
                                                                                 -1 *
*************************************************************************************
```
