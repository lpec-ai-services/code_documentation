# Use-cases in Python — Macros Launcher — Input/Output with vector and string: introduction to macros with multitype … Macro “sensitivityMorrisFunctionFlowrate.py”
<!-- source PDF pages 271-288 -->

<!-- page 264 (PDF 271) -->
#### 13.4.14.3 Graph

Figure 13.17: Graph of the macro “samplingSingularCorrelationCase.py”

## 13.5 Macros Launcher

### 13.5.1 Input/Output with vector and string: introduction to macros with multitype

#### 13.5.1.1 Producing outputs

#### 13.5.1.2 Reading inputs

### 13.5.2 Macro “launchCodeReadMultiTypeRow.py”

#### 13.5.2.1 Objective

## 13.6 Macros Sensitivity

### 13.6.1 Macro “sensitivityBrutForceMethodFlowrate.py”

#### 13.6.1.1 Objective

The objective of this macro is to perform a sensitivity analysis with brute force method on a set of eight parameters used
in the flowrate model described in Presentation of the problem. Sensitivity indexes are computed dividing conditional
variance by the standard deviation of the output variable.
Exclamation-Triangle Warning
This macro is purely illustrative. It is not meant to be used for proper results with a real code / function as it needs
a large number of computation to only get the first order index. Its main appeal is to be nicely illustrative: it shows
plainly the definition of the conditional expectation and also its variance used to defined the first order sobol indices.

<!-- page 265 (PDF 272) -->
#### 13.6.1.2 Macro Uranie

```python
"""
Example of Sobol estimation with a brut-force approach
"""
from URANIE import DataServer, Launcher, Sampler
import ROOT
def draw_bar_with_tuple(val, name, stitle):
    """Draw the results estimated with brut-force approach."""
    h_div = ROOT.TH1F("hDivdrawBarWithTuple", stitle, 3, 0, 3)
    h_div.SetCanExtend(ROOT.TH1.kXaxis)
                                         # .SetBit(ROOT.TH1.kCanRebin)
    h_div.SetStats(0)
    if h_div != 0:
        h_div.SetBarWidth(0.45)
        h_div.SetBarOffset(0.1)
        h_div.SetMarkerColor(2)
        h_div.SetMarkerSize(2)
        h_div.SetFillColor(49)
        h_div.SetTitle(stitle)
        for ite, value in enumerate(val):
            h_div.Fill(name[ite], value)
        h_div.LabelsDeflate()
        h_div.LabelsOption(">u")
        h_div.SetMinimum(0.0)
        h_div.SetMaximum(1.0)
        ROOT.gStyle.SetPaintTextFormat("5.2f")
        h_div.Draw("bar2, text45")
    return h_div
nCond = 50
nbins = 10
# Create a DataServer.TDataServer
tds = DataServer.TDataServer()
print(" ******************************************************")
print(" ** sensitivityBrutForceMethodFlowrate nbins[%i] nCond[%i]" %
      (nbins, nCond))
print(" **")
# Create a DataServer.TDataServer
tds = DataServer.TDataServer()
# Add the eight attributes of the study with uniform law
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

<!-- page 266 (PDF 273) -->
```python
nvar = tds.getNAttributes()
print(" ** nX["+str(nvar)+"]")
nS = nbins*nvar*nCond
print(" ** nS["+str(nS)+"]")
# sam = Sampler.TSampling(tds, "lhs", nS)
sam = Sampler.TQMC(tds, "halton", nS)
sam.generateSample()
# Load the function
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Create a TLauncherFunction from a TDataServer and an analytical function
# Rename the outpout attribute "ymod"
tlf = Launcher.TLauncherFunction(tds, "flowrateModel",
                                 "rw:r:tu:tl:hu:hl:l:kw", "ymod")
# Evaluate the function on all the design of experiments
tlf.setDrawProgressBar(False)
tlf.run()
Canvas = ROOT.TCanvas("c1", "Graph for the Macro modeler", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2, 2)
pad.cd(1)
tds.computeStatistic("ymod")
tds.draw("ymod")
dstdy = tds.getAttribute("ymod").getStd()
svary = dstdy * dstdy
print(" ** ymod: std["+str(round(dstdy, 4))+"] vary["+str(round(svary, 1))+"]")
tds.getAttribute("ymod").setOutput()
ROOT.gStyle.SetOptStat(1)
valSobolCrt = []
sName = []
c = ROOT.TCanvas()
c.Divide(2)
c.cd(1)
for ivar in range(nvar):
    print(" *****************************")
    print(" *** "+str(tds.getAttribute(ivar).GetName()))
    svar = tds.getAttribute(ivar).GetName()
    if ivar == 0:
```

<!-- page 267 (PDF 274) -->
```python
        pad.cd(2)
    else:
        c.cd(1)
    tds.drawProfile("ymod:"+svar, "", "nclass="+str(nbins))
    hprofs = ROOT.gPad.GetPrimitive("Profile ymod:%s (Bin = %i )" %
                                    (svar, nbins+2))
    ntd = ROOT.TNtupleD("dd", "sjsjs", "i:x:m")
    ntd.SetMarkerColor(ROOT.kBlue)
    ntd.SetMarkerStyle(8)
    nnbins = hprofs.GetNbinsX()
    for i in range(1, nnbins+1):
        ntd.Fill(i-1, hprofs.GetBinCenter(i), hprofs.GetBinContent(i))
    tds.draw("ymod:"+svar)
    ntd.Draw("m:x", "", "same")
    if ivar == 0:
        pad.cd(3)
    else:
        c.cd(2)
    ntd.Draw("m")
    htemp = ROOT.gPad.GetPrimitive("htemp")
    dvarcond = htemp.GetRMS()
    # Tempory ROOT.TTree for histogram
    valSobolCrt.append(dvarcond*dvarcond / svary)
    sName.append(svar)
    print(" *** S1[ %s] Cond. Var.[%4.6g] -- [%1.6g]" %
          (svar, dvarcond*dvarcond, valSobolCrt[-1]))
    c.Modified()
    c.Update()
    c.SaveAs("SAFlowRateVersus"+svar+".png")
pad.cd(4)
hDiv = draw_bar_with_tuple(valSobolCrt, sName,
                           "Sensitivity Indexes: ymod
                                                       [Brute-Force Method]")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval:

```python
tds = DataServer.TDataServer()
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
```

<!-- page 268 (PDF 275) -->
```python
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

A design-of-experiments is built with a “Halton” method (𝑛𝑆= 4000):

```python
sam = Sampler.TQMC(tds, "halton", nS)
sam.generateSample()
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros):

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

The flowrateModel model is applied on previous variables:

```python
tlf = Launcher.TLauncherFunction(tds, "flowrateModel",
                                 "rw:r:tu:tl:hu:hl:l:kw", "ymod")
tlf.run()
```

Characteristic values for the output attribute are computed:

```python
tds.computeStatistic("ymod")
```

Sensitivity indexes are computed in the for loop. Average value of output variable is computed on nbins+2=12 points for
each input variable:

```python
c.cd(1)
...
nnbins = hprofs.GetNbinsX()
for i in range(1,nnbins+1): ntd.Fill(i-1, hprofs.GetBinCenter(i), hprofs.
```

˓→GetBinContent(i))
The RMS value is obtained from the graphic of ymod versus the considered output variable and the sensitivity index is
computed dividing the conditional variance value by the standard deviation of the output variable ymod.

```python
    c.cd(2)
ntd.Draw("m")
htemp = ROOT.gPad.GetPrimitive("htemp")
dvarcond = htemp.GetRMS()
valSobolCrt.append(dvarcond*dvarcond / svary)
```

<!-- page 269 (PDF 276) -->
#### 13.6.1.3 Graph

Figure 13.18: Graph of the macro “sensitivityBrutForceMethodFlowrate.py”

#### 13.6.1.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
Info in <TCanvas::Print>: png file SAFlowRateVersusrw.png has been created
Info in <TCanvas::Print>: png file SAFlowRateVersusr.png has been created
Info in <TCanvas::Print>: png file SAFlowRateVersustu.png has been created
Info in <TCanvas::Print>: png file SAFlowRateVersustl.png has been created
Info in <TCanvas::Print>: png file SAFlowRateVersushu.png has been created
Info in <TCanvas::Print>: png file SAFlowRateVersushl.png has been created
Info in <TCanvas::Print>: png file SAFlowRateVersusl.png has been created
Info in <TCanvas::Print>: png file SAFlowRateVersuskw.png has been created
 ******************************************************
 ** sensitivityBrutForceMethodFlowrate nbins[10] nCond[50]
 **
 ** nX[8]
 ** nS[4000]
 ** ymod: std[45.6059] vary[2079.9]
 *****************************
 *** rw
 *** S1[ rw] Cond. Var.[1763.28] -- [0.847774]
 *****************************
 *** r
 *** S1[ r] Cond. Var.[0.0624988] -- [3.00489e-05]
```

<!-- page 270 (PDF 277) -->
```python
*****************************
*** tu
*** S1[ tu] Cond. Var.[0.0886501] -- [4.26223e-05]
*****************************
*** tl
*** S1[ tl] Cond. Var.[0.0909604] -- [4.37331e-05]
*****************************
*** hu
*** S1[ hu] Cond. Var.[88.368] -- [0.0424867]
*****************************
*** hl
*** S1[ hl] Cond. Var.[88.2039] -- [0.0424078]
*****************************
*** l
*** S1[ l] Cond. Var.[84.9543] -- [0.0408454]
*****************************
*** kw
*** S1[ kw] Cond. Var.[20.8848] -- [0.0100413]
```

###  13.6.2 Macro “sensitivityFiniteDifferencesFunctionFlowrate.py”

####  13.6.2.1 Objective

The objective of this macro is to compute the finite differences indexes on a function.

#### 13.6.2.2 Macro Uranie

```python
"""
Example of finite difference approach to the flowrate model
"""
from URANIE import DataServer, Sensitivity
import ROOT
# loading the flowrateModel function
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
                         and add the attributes (stochastic variables here)
tds = DataServer.TDataServer("tdsflowrate", "DataBase flowrate")
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
tds.getAttribute("rw").setDefaultValue(0.075)
tds.getAttribute("r").setDefaultValue(25000.0)
tds.getAttribute("tu").setDefaultValue(90000.0)
tds.getAttribute("tl").setDefaultValue(90.0)
tds.getAttribute("hu").setDefaultValue(1050.0)
```

<!-- page 271 (PDF 278) -->
```python
tds.getAttribute("hl").setDefaultValue(760.0)
tds.getAttribute("l").setDefaultValue(1400.0)
tds.getAttribute("kw").setDefaultValue(10500.0)
# Create a TFiniteDifferences object
tfindef = Sensitivity.TFiniteDifferences(tds, "flowrateModel",
                                         "rw:r:tu:tl:hu:hl:l:kw",
                                         "flowrateModel", "steps=1%")
tfindef.setDrawProgressBar(False)
tfindef.computeIndexes()
matRes = tfindef.getSensitivityMatrix()
matRes.Print()
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval:

```python
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

Each parameter gets a default value:

```python
tds.getAttribute("rw").setDefaultValue(0.075)
tds.getAttribute("r").setDefaultValue(25000.0)
tds.getAttribute("tu").setDefaultValue(90000.0)
tds.getAttribute("tl").setDefaultValue(90.0)
tds.getAttribute("hu").setDefaultValue(1050.0)
tds.getAttribute("hl").setDefaultValue(760.0)
tds.getAttribute("l").setDefaultValue(1400.0)
tds.getAttribute("kw").setDefaultValue(10500.0)
```

To instantiate the TFiniteDifferences object, one uses the TDataServer, the name of the function, the name of
the output of the function, the names of the input variables separated by “:” and the option to specify the sampling:

```python
tfindef = Sensitivity.TFiniteDifferences(tds, "flowrateModel",
                                         "rw:r:tu:tl:hu:hl:l:kw",
                                         "flowrateModel", "steps=1%")
```

Computation of sensitivity indexes:

```python
tfindef.computeIndexes()
```

<!-- page 272 (PDF 279) -->
#### 13.6.2.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
1x8 matrix is as follows
     |
                 |
                             |
                                         |
                                                     |
                                                                 |
----------------------------------------------------------------------
   0 |
                   -3.586e-07
                                1.265e-09
                                             0.001265
                                                           0.1321
     |
                 |
                             |
                                         |
----------------------------------------------------------------------
   0 |
          -0.1321
                     -0.02729
                                 0.003639
```

###  13.6.3 Macro “sensitivityDataBaseFlowrate.py”

####  13.6.3.1 Objective

The objective of this macro is to perform a SRC regression on data stored in a TDataServer. Data are loaded in the
TDataServer from an ASCII data file flowrateUniformDesign.dat:

```python
#NAME: flowrateborehole
#TITLE: Uniform design of flow rate borehole problem proposed by Ho and Xu(2000)
#COLUMN_NAMES: rw| r| tu| tl| hu| hl| l| kw | ystar
#COLUMN_TITLES: r_{#omega}| r | T_{u} | T_{l} | H_{u} | H_{l} | L | K_{#omega} | y^{*}
#COLUMN_UNITS: m | m | m^{2}/yr | m^{2}/yr | m | m | m | m/yr | m^{3}/yr
0.0500 33366.67
                 63070.0 116.00 1110.00 768.57 1200.0 11732.14
                                                                26.18
0.0500
         100.00
                 80580.0
                          80.73 1092.86 802.86 1600.0 10167.86
                                                                14.46
0.0567
         100.00
                 98090.0
                          80.73 1058.57 717.14 1680.0 11106.43
                                                                22.75
0.0567 33366.67
                 98090.0
                          98.37 1110.00 734.29 1280.0 10480.71
                                                                30.98
0.0633
         100.00 115600.0
                          80.73 1075.71 751.43 1600.0 11106.43
                                                                28.33
0.0633 16733.33
                 80580.0
                          80.73 1058.57 785.71 1680.0 12045.00
                                                                24.60
0.0700 33366.67
                 63070.0
                          98.37 1092.86 768.57 1200.0 11732.14
                                                                48.65
0.0700 16733.33 115600.0 116.00
                                 990.00 700.00 1360.0 10793.57
                                                                35.36
0.0767
         100.0
                115600.0
                          80.73 1075.71 751.43 1520.0 10793.57
                                                                42.44
0.0767 16733.33
                 80580.0
                          80.73 1075.71 802.86 1120.0
                                                       9855.00
                                                                44.16
0.0833 50000.00
                 98090.0
                          63.10 1041.43 717.14 1600.0 10793.57
                                                                47.49
0.0833 50000.00 115600.0
                          63.10 1007.14 768.57 1440.0 11419.29
                                                                41.04
0.0900 16733.33
                 63070.0 116.00 1075.71 751.43 1120.0 11419.29
                                                                83.77
0.0900 33366.67 115600.0 116.00 1007.14 717.14 1360.0 11106.43
                                                                60.05
0.0967 50000.00
                 80580.0
                          63.10 1024.29 820.00 1360.0
                                                       9855.00
                                                                43.15
0.0967 16733.33
                 80580.0
                          98.37 1058.57 700.00 1120.0 10480.71
                                                                97.98
0.1033 50000.00
                 80580.0
                          63.10 1024.29 700.00 1520.0 10480.71
                                                                74.44
0.1033 16733.33
                 80580.0
                          98.37 1058.57 820.00 1120.0 10167.86
                                                                72.23
0.1100 50000.00
                 98090.0
                          63.10 1024.29 717.14 1520.0 10793.57
                                                                82.18
0.1100
         100.00
                 63070.0
                          98.37 1041.43 802.86 1600.0 12045.00
                                                                68.06
```

<!-- page 273 (PDF 280) -->
```python
0.1167 33366.67
                 63070.0 116.00
                                 990.00 785.71 1280.0 12045.00
                                                                81.63
0.1167
         100.00
                 98090.0
                          98.37 1092.86 802.86 1680.0
                                                       9855.00
                                                                72.5
0.1233 16733.33 115600.0
                          80.73 1092.86 734.29 1200.0 11419.29 161.35
0.1233 16733.33
                 63070.0
                          63.10 1041.43 785.71 1680.0 12045.00
                                                                86.73
0.1300 33366.67
                 80580.0 116.00 1110.00 768.57 1280.0 11732.14 164.78
0.1300
         100.00
                 98090.0
                          98.37 1110.00 820.00 1280.0 10167.86 121.76
0.1367 50000.00
                 98090.0
                          63.10 1007.14 820.00 1440.0 10167.86
                                                                76.51
0.1367 33366.67
                 98090.0 116.00 1024.29 700.00 1200.0 10480.71 164.75
0.1433 50000.00
                 63070.0 116.00
                                 990.00 785.71 1440.0
                                                       9855.00
                                                                89.54
0.1433 50000.00 115600.0
                          63.10 1007.14 734.29 1440.0 11732.14 141.09
0.1500 33366.67
                 63070.0
                          98.37
                                 990.00 751.43 1360.0 11419.29 139.94
0.1500
         100.00 115600.0
                          80.73 1041.43 734.29 1520.0 11106.43 157.59
```

####  13.6.3.2 Macro Uranie

```python
"""
Example of sensitivity analysis through linear regression
"""
from URANIE import DataServer, Sensitivity
import ROOT
# Create a DataServer.TDataServer
tds = DataServer.TDataServer()
# Load a database in an ASCII file
tds.fileDataRead("flowrateUniformDesign.dat")
# Graph
Canvas = ROOT.TCanvas("c2", "Graph for the Macro", 5, 64, 1270, 667)
# Visualisation
tds.Draw("ystar:rw")
# Sensitivity analysis
treg = Sensitivity.TRegression(tds, "rw:r:tu:tl:hu:hl:l:kw", "ystar", "src")
treg.computeIndexes()
treg.drawIndexes("Flowrate", "", "hist, first")
# treg.getResultTuple().Scan()
# Graph
c = ROOT.gROOT.FindObject("__sensitivitycan__0")
can = ROOT.TCanvas("c1", "Graph for the Macro sensitivityDataBaseFlowrate",
                   5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2)
pad.cd(1)
Canvas.DrawClonePad()
pad.cd(2)
c.DrawClonePad()
```

The TDataServer is filled with the data file flowrateUniformDesign.dat through the fileDataRead method:

<!-- page 274 (PDF 281) -->
```python
tds.fileDataRead("flowrateUniformDesign.dat")
```

The regression is performed on all the variables with a SRC method and sensitivity indexes are computed:

```python
treg = Sensitivity.TRegression(tds, "rw:r:tu:tl:hu:hl:l:kw", "ystar", "src")
treg.computeIndexes()
```

####  13.6.3.3 Graph

Figure 13.19: Graph of the macro “sensitivityDataBaseFlowrate.py”

### 13.6.4 Macro “sensitivityFASTFunctionFlowrate.py”

#### 13.6.4.1 Objective

The objective of this macro is to perform a Fast sensitivity analysis on a set of eight parameters used in the flowrate-
Model model described in Presentation of the problem.

#### 13.6.4.2 Macro Uranie

```python
"""
Example of the flowrate function sensitivity analysis
"""
from URANIE import DataServer, Sensitivity
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
tds = DataServer.TDataServer("tdsflowreate", "DataBase flowreate")
```

<!-- page 275 (PDF 282) -->
```python
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
# \param Size of a sampling.
nS = 4000
# Graph
fast = Sensitivity.TFast(tds, "flowrateModel", nS)
fast.setDrawProgressBar(False)
fast.computeIndexes("graph")
fast.getResultTuple().Scan("Out:Inp:Order:Method:Value", "Algo==\"--first--\"")
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

To instantiate the TFast object, one uses the TDataServer, the name of the function and the number of samplings
needed to perform sensitivity analysis (here nS=500):

```python
fast = Sensitivity.TFast(tds, "flowrateModel", nS)
```

Computation of sensitivity indexes:

```python
fast.computeIndexes("graph")
```

<!-- page 276 (PDF 283) -->
#### 13.6.4.3 Graph

Figure 13.20: Graph of the macro “sensitivityFASTFunctionFlowrate.py”

#### 13.6.4.4 Console

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
 <URANIE::WARNING>
 <URANIE::WARNING> *** URANIE WARNING ***
 <URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[8531]
 <URANIE::WARNING> TDataServer::getTuple Error : There is no tree!
 <URANIE::WARNING> *** END of URANIE WARNING ***
 <URANIE::WARNING>
 <URANIE::INFO>
 <URANIE::INFO> *** URANIE INFORMATION ***
 <URANIE::INFO> *** File[${SOURCEDIR}/meTIER/sampler/souRCE/TSpaceFilling.cxx]␣
```

˓→Line[167]

```python
<URANIE::INFO> TSamplerStochastic::init: the TDS [tdsflowreate] contains data: we␣
```

˓→need to empty it !

```python
 <URANIE::INFO> *** END of URANIE INFORMATION ***
 <URANIE::INFO>
************************************************************************
*
     Row
           *
                   Out *
                               Inp *
                                         Order *
                                                    Method *
                                                                 Value *
************************************************************************
```

<!-- page 277 (PDF 284) -->
```python
*
         0 * flowrateM *
                                rw *
                                         First *
                                                      FAST * 0.8278187 *
*
         2 * flowrateM *
                                 r *
                                         First *
                                                      FAST * 8.924e-07 *
*
         4 * flowrateM *
                                tu *
                                         First *
                                                      FAST * 2.308e-06 *
*
         6 * flowrateM *
                                tl *
                                         First *
                                                      FAST * 3.204e-05 *
*
         8 * flowrateM *
                                hu *
                                         First *
                                                      FAST * 0.0414390 *
*
        10 * flowrateM *
                                hl *
                                         First *
                                                      FAST * 0.0414046 *
*
        12 * flowrateM *
                                 l *
                                         First *
                                                      FAST * 0.0392873 *
*
        14 * flowrateM *
                                kw *
                                         First *
                                                      FAST * 0.0094983 *
************************************************************************
==> 8 selected entries
```

###  13.6.5 Macro “sensitivityRBDFunctionFlowrate.py”

####  13.6.5.1 Objective

The objective of this macro is to perform a RBD sensitivity analysis on a set of eight parameters used in the flowrate-
Model model described in Presentation of the problem.

#### 13.6.5.2 Macro Uranie

```python
"""
Example of RDB analysis on the flowrate function
"""
from URANIE import DataServer, Sensitivity
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
# Size of a sampling.
nS = 4000
# Graph
trbd = Sensitivity.TRBD(tds, "flowrateModel", nS)
trbd.setDrawProgressBar(False)
trbd.computeIndexes("graph")
trbd.getResultTuple().Scan("Out:Inp:Order:Method:Value", "Algo==\"--first--\"")
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

<!-- page 278 (PDF 285) -->
Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval

```python
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

To instantiate the TRBD object, one uses the TDataServer, the name of the function and the number of samplings needed
to perform sensitivity analysis (here 𝑛𝑆=4000):

```python
trbd = Sensitivity.TRBD(tds, "flowrateModel", nS)
```

Computation of sensitivity indexes:

```python
trbd.computeIndexes("graph")
```

####  13.6.5.3 Graph

Figure 13.21: Graph of the macro “sensitivityRBDFunctionFlowrate.py”

#### 13.6.5.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
 <URANIE::WARNING>
 <URANIE::WARNING> *** URANIE WARNING ***
```

<!-- page 279 (PDF 286) -->
```python
<URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[8531]
<URANIE::WARNING> TDataServer::getTuple Error : There is no tree!
<URANIE::WARNING> *** END of URANIE WARNING ***
<URANIE::WARNING>
<URANIE::WARNING>
<URANIE::WARNING> *** URANIE WARNING ***
<URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[8531]
<URANIE::WARNING> TDataServer::getTuple Error : There is no tree!
<URANIE::WARNING> *** END of URANIE WARNING ***
<URANIE::WARNING>
<URANIE::INFO>
<URANIE::INFO> *** URANIE INFORMATION ***
<URANIE::INFO> *** File[${SOURCEDIR}/meTIER/sampler/souRCE/TSpaceFilling.cxx]␣
```

˓→Line[167]

```python
<URANIE::INFO> TSamplerStochastic::init: the TDS [tdsflowrate] contains data: we␣
```

˓→need to empty it !

```python
 <URANIE::INFO> *** END of URANIE INFORMATION ***
 <URANIE::INFO>
************************************************************************
*
     Row
           *
                   Out *
                               Inp *
                                         Order *
                                                    Method *
                                                                 Value *
************************************************************************
*
         0 * flowrateM *
                                rw *
                                         First *
                                                       RBD * 0.7558010 *
*
         2 * flowrateM *
                                 r *
                                         First *
                                                       RBD * 0.0026080 *
*
         4 * flowrateM *
                                tu *
                                         First *
                                                       RBD * 0.0035324 *
*
         6 * flowrateM *
                                tl *
                                         First *
                                                       RBD * 0.0032848 *
*
         8 * flowrateM *
                                hu *
                                         First *
                                                       RBD * 0.0408758 *
*
        10 * flowrateM *
                                hl *
                                         First *
                                                       RBD * 0.0469345 *
*
        12 * flowrateM *
                                 l *
                                         First *
                                                       RBD * 0.0347870 *
*
        14 * flowrateM *
                                kw *
                                         First *
                                                       RBD * 0.0165843 *
************************************************************************
==> 8 selected entries
```

###  13.6.6 Macro “sensitivityMorrisFunctionFlowrate.py”

####  13.6.6.1 Objective

The objective of this macro is to perform a Morris sensitivity analysis on a set of eight parameters used in the flowrate-
Model model described in Presentation of the problem.

#### 13.6.6.2 Macro Uranie

```python
"""
Example of Morris estimation on flowrate
"""
from URANIE import DataServer, Sensitivity
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
tds = DataServer.TDataServer("tdsflowreate", "DataBase flowreate")
```

<!-- page 280 (PDF 287) -->
```python
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("r", 100.0, 50000.0))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
nreplique = 3
nlevel = 10
scmo = Sensitivity.TMorris(tds, "flowrateModel", nreplique, nlevel)
scmo.setDrawProgressBar(False)
scmo.generateSample()
tds.exportData("_morris_sampling_.dat")
scmo.computeIndexes()
tds.exportData("_morris_launching_.dat")
ntresu = scmo.getMorrisResults()
ntresu.Scan("*")
# Graph
canmoralltraj = ROOT.gROOT.FindObject("canmoralltraj")
can = ROOT.TCanvas("c1", "Graph of sensitivityMorrisFunctionFlowrate",
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

To instantiate the TMorris, one uses the TDataServer, the name of the function, the number of replicas (here

<!-- page 281 (PDF 288) -->
nreplique=3), the level parameter (here nlevel=10)

```python
scmo = Sensitivity.TMorris(tds, "flowrateModel", nreplique, nlevel)
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

####  13.6.6.3 Graph

Figure 13.22: Graph of the macro “sensitivityMorrisFunctionFlowrate.py”

#### 13.6.6.4 Console

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
```
