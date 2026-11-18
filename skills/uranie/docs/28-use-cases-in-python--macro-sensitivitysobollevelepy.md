# Use-cases in Python — Macros Launcher — Macro “sensitivitySobolLeveLE.py” … Macro “sensitivityJohnsonRWCorrelatedFunctionFlowrate.py”
<!-- source PDF pages 308-326 -->

<!-- page 301 (PDF 308) -->
### 13.6.12 Macro “sensitivitySobolLeveLE.py”

Exclamation-Triangle Warning
The levele command will be installed on your machine only if a Fortran compiler is found

#### 13.6.12.1 Objective

The objective of this macro is to perform a full Sobol analysis on the temporal use-case levele. This use-case is an
example of code that takes a dozen of entries in order to compute the evolution of dose as a function of time. The result
of every computation consists in 3 vectors: the time (always the same value disregarding all entries), the dose called “y”
and a third useless information.

#### 13.6.12.2 Macro Uranie

```python
"""
Example of Sobol estimation on the levelE code
"""
import sys
import numpy as np
from URANIE import Launcher, Sensitivity
from URANIE import DataServer as DS
import ROOT
# Define the DataServer
tds = DS.TDataServer("tdsLevelE", "levele")
tds.addAttribute(DS.TUniformDistribution("t", 100, 1000))
tds.addAttribute(DS.TLogUniformDistribution("kl", 0.001, 0.01))
tds.addAttribute(DS.TLogUniformDistribution("kc", 0.000001, 0.00001))
tds.addAttribute(DS.TLogUniformDistribution("v1", 0.001, 0.1))
tds.addAttribute(DS.TUniformDistribution("l1", 100, 500))
tds.addAttribute(DS.TUniformDistribution("r1", 1, 5))
tds.addAttribute(DS.TUniformDistribution("rc1", 3, 30))
tds.addAttribute(DS.TLogUniformDistribution("v2", 0.01, 0.1))
tds.addAttribute(DS.TUniformDistribution("l2", 50, 200))
tds.addAttribute(DS.TUniformDistribution("r2", 1, 5))
tds.addAttribute(DS.TUniformDistribution("rc2", 3, 30))
tds.addAttribute(DS.TLogUniformDistribution("w", 100000, 10000000))
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
```

<!-- page 302 (PDF 309) -->
```python
tds.getAttribute("w").setFileKey(sIn, "", "%e", DS.TAttributeFileKey.kNewRow)
# How to read ouput files
out = Launcher.TOutputFileRow("_output_levelE_withRow_.dat")
# Tell the output file that attribute IS a vector and is SECOND column
out.addAttribute(DS.TAttribute("y", DS.TAttribute.kVector), 2)
# Creation of Launcher.TCode
myc = Launcher.TCode(tds, "levele 2> /dev/null")
myc.addOutputFile(out)
# Run Sobol analysis
tsobol = Sensitivity.TSobol(tds, myc, 10000)
tsobol.computeIndexes(args.computeIdxOpt) # args.computeIdxOpt = "" or "nointermed"
ntresu = tsobol.getResultTuple()
# Plotting mess
colors = [1, 2, 3, 4, 6, 7, 8, 15, 30, 38, 41, 46]
tps = np.array([20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,
                200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000,
                1e+06, 2e+06, 3e+06, 4e+06, 5e+06, 6e+06, 7e+06, 8e+06, 9e+06],
               dtype=float)
c2 = ROOT.TCanvas("c2", "c2", 5, 64, 1200, 900)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(1, 2)
pad.cd(1)
ROOT.gPad.SetLogx()
ROOT.gPad.SetGrid()
# LegendandMArker
ROOT.gStyle.SetMarkerStyle(3)
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetFillStyle(0)
mg2 = ROOT.TMultiGraph()
names = ["t", "kl", "kc", "v1", "l1", "r1", "rc1",
         "v2", "l2", "r2", "rc2", "w"]
fdeg = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
leg = [0., 0., 0., 0., 0., 0.]
Zeros = np.zeros([26])
for igr in range(12):
    sel = "Inp==\""+names[igr]+"\""
    sel += " && Order==\"First\" &&
                                     Algo==\"martinez11\""
    ntresu.Draw("CILower:CIUpper:Value", sel, "goff")
    data = ntresu.GetV3()
    themin = ntresu.GetV1()
    themax = ntresu.GetV2()
```

<!-- page 303 (PDF 310) -->
```python
    for i in range(26):
        themin[i] = data[i] - themin[i]
        themax[i] = - data[i] + themax[i]
    if (igr % 2) == 0:
        leg[int(igr/2)] = ROOT.TLegend(0.1+0.15*(igr/2), 0.91,
                                       0.25+0.15*(igr/2), 0.98)
        leg[int(igr/2)].SetTextSize(0.045)
    fdeg[igr] = ROOT.TGraphAsymmErrors(26, tps, data,
                                       Zeros, Zeros, themin, themax)
    fdeg[igr].SetMarkerColor(colors[igr])
    fdeg[igr].SetLineColor(colors[igr])
    fdeg[igr].SetFillColor(colors[igr])
    leg[int(igr/2)].AddEntry(fdeg[igr], names[igr], "pl")
for igr2 in range(11, -1, -1):
    mg2.Add(fdeg[igr2])
mg2.Draw("APC")
mg2.GetXaxis().SetTitle("Time")
mg2.GetYaxis().SetTitle("S_{1}[martinez11]")
for igr3 in range(6):
    leg[igr3].Draw()
mg = ROOT.TMultiGraph()
tdeg = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
pad.cd(2)
ROOT.gPad.SetLogx()
ROOT.gPad.SetGrid()
for igr in range(12):
    sel = "Inp==\""+names[igr]+"\""
    sel += " && Order==\"Total\" &&
                                     Algo==\"martinez11\""
    ntresu.Draw("CILower:CIUpper:Value", sel, "goff")
    data = ntresu.GetV3()
    themin = ntresu.GetV1()
    themax = ntresu.GetV2()
    for i in range(26):
        themin[i] = data[i] - themin[i]
        themax[i] = - data[i] + themax[i]
    for ip in range(26):
        if ip == 0:
            tdeg[igr] = ROOT.TGraphAsymmErrors()
            tdeg[igr].SetMarkerColor(colors[igr])
            tdeg[igr].SetLineColor(colors[igr])
            tdeg[igr].SetFillColor(colors[igr])
        tdeg[igr].SetPoint(ip, tps[ip], data[ip])
        tdeg[igr].SetPointError(ip, 0, 0, themin[ip], themax[ip])
```

<!-- page 304 (PDF 311) -->
```python
for igr2 in range(11, -1, -1):
    mg.Add(tdeg[igr2])
mg.Draw("APC")
mg.GetXaxis().SetTitle("Time")
mg.GetYaxis().SetTitle("S_{T}[martinez11]")
for igr3 in range(6):
    leg[igr3].Draw()
```

The levele external code is located in the bin directory of the Uranie installation.
When looking at the code and comparing it to an usual Sobol estimation, the organisation is completely transparent. The
only noticeable (and compulsory) thing to do is to change the default type of the attribute read at the end of the job. This
is done in this line:

```python
out.addAttribute(DS.TAttribute("y", DS.TAttribute.kVector), 2)
```

where the output attribute is provided, changing its nature to a vector, thanks to the second argument of the TAttribute
constructor from the default (kReal) to the desired nature (kVector). Once this is done, this information is broadcast
internally to the code that knows how to deal with this type of attribute.
The rest of the code is the graphical part, leading to the figure below (it is provided to illustrate how to represent results).

#### 13.6.12.3 Graph

The results of the previous macro is shown in Figure 13.28, where the evolution of the sobol coefficient is shown for all
inputs with the uncertainty band, for the first order coefficient and the total one, respectively on the top and bottom panel.

<!-- page 305 (PDF 312) -->
Figure 13.28: Graph of the macro “sensitivitySobolLeveLE.py”

### 13.6.13 Macro “sensitivitySobolRe-estimation.py”

#### 13.6.13.1 Objective

The objective of this macro is to perform a full Sobol analysis using the existing file created when the Sobol class is
allowed to perform the design-of-experiments and the estimations by itself (see the first item in the tip box in Computation
of Sobol’s sensitivity indices for more details). This would mean that the only computation done would be to estimate the
coefficients (no external code / function called).
Exclamation-Triangle Warning
The

```python
ref_sobol_launching_.dat
```

file
used
as
input
is
not
provided
in
the
usual
sub-directory
“/share/uranie/macros” of the installation folder of Uranie ($URANIESYS) but can be generated by the user
by running the macro discussed in Macro “sensitivitySobolFunctionFlowrate.py”.

#### 13.6.13.2 Macro Uranie

```python
"""
Example of sobol re-estimation
"""
```

<!-- page 306 (PDF 313) -->
```python
from URANIE import DataServer, Sensitivity
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
tds = DataServer.TDataServer("tdsflowreate", "DataBase flowreate")
tds.fileDataRead("ref_sobol_launching_.dat")
tsobol = Sensitivity.TSobol(tds, "rw:r:tu:tl:hu:hl:l:kw", "flowrateModel")
tsobol.setDrawProgressBar(False)
tsobol.computeIndexes()
cc = ROOT.TCanvas("c1", "histgramme", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2, 1)
pad.cd(1)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, hist, all")
pad.cd(2)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, pie, first")
```

There are no external code or function to be run here. The input file ref_sobol_launching_.dat has to be generated
by the use of sensitivtySobolFunctionFlowrate.py. Once done it is loaded into the dataserver and the TSobol
object is constructed from the simplest constructor with only the pointer to the dataserver, the input and output list:

```python
tsobol = Sensitivity.TSobol(tds, "rw:r:tu:tl:hu:hl:l:kw", "flowrateModel")
```

Once done, the computeIndexes() method is called and few lines are shown to display the results in the classical plot
form, leading to the figure below (it is provided to illustrate how to represent results). The numerical results are shown in
the console below and are identical to the ones shown in Console from where the full sample is coming from.

#### 13.6.13.3 Graph

The results of the previous macro is shown in Figure 13.29, where the evolution of the sobol coefficient is shown for all
inputs with the uncertainty band, for the first order coefficient and the total one, respectively on the top and bottom panel.

<!-- page 307 (PDF 314) -->
Figure 13.29: Graph of the macro “sensitivitySobolRe-estimation.py”

#### 13.6.13.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
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

###  13.6.14 Macro “sensitivitySobolWithData.py”

####  13.6.14.1 Objective

The objective of this macro is to perform a Sobol analysis using the some already made computations in order to be able
to save ressources. The idea (discussed in the second item in the tip box in Computation of Sobol’s sensitivity indices is
indeed to use the provided points as the 2 × 𝑛𝑆first estimations corresponding to both the 𝑀and 𝑁matrices content.
The class will still have to create all the cross configurations (the 𝑁𝑖matrices) and launch their corresponding estimations.
In order to do that there are few things to keep in mind:
• The input file (here _onlyMandN_sobol_launching_.dat) should contains input and output variables only,
the user being in charge of having a decent design-of-experiments for the sobol estimation.

<!-- page 308 (PDF 315) -->
Exclamation-Triangle Warning
The _onlyMandN_sobol_launching_.dat file used as input is not provided in the usual sub-directory
“/share/uranie/macros” of the installation folder of Uranie ($URANIESYS) but can be generated by the user by running
the macro discussed in Macro “sensitivitySobolFunctionFlowrate.py”.

#### 13.6.14.2 Macro Uranie

```python
"""
Example of sobol estimation using provided data
"""
from URANIE import DataServer, Sensitivity
import ROOT
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Define the DataServer
tds = DataServer.TDataServer("tdsflowreate", "DataBase flowrate")
tds.fileDataRead("_onlyMandN_sobol_launching_.dat")
ns = 10000
tsobol = Sensitivity.TSobol(tds, "flowrateModel", ns, "rw:r:tu:tl:hu:hl:l:kw",
                            "flowrateModel", "WithData")
tsobol.setDrawProgressBar(False)
tsobol.computeIndexes()
cc = ROOT.TCanvas("c1", "histgramme", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2, 1)
pad.cd(1)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, hist, all")
pad.cd(2)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, pie, first")
```

As
for
Macro
“sensitivitySobolFunctionFlowrate.py”,
the

```python
UserFunctions.C
```

file
is
loaded
and
the
input

file

```python
_onlyMandN_sobol_launching_.dat
```

(which
should
have
been
generated
by
the
use
of
sensitivtySobolFunctionFlowrate.py), is loaded into the dataserver.
The TSobol object is constructed
from the usual function constructor with a noticing difference: the option field is filled with WithData to specify that data
are already there and the code has to use these data and split them into both the 𝑀and 𝑁matrices.

```python
tsobol = Sensitivity.TSobol(tds, "flowrateModel", ns, "rw:r:tu:tl:hu:hl:l:kw",
                            "flowrateModel", "WithData")
```

Once done, the computeIndexes() method is called and few lines are shown to display the results in the classical plot
form, leading to the figure below (it is provided to illustrate how to represent results). The numerical results are shown in
the console below and are identical to the ones shown in Console from where the original set of points is coming from.

<!-- page 309 (PDF 316) -->
#### 13.6.14.3 Graph

The results of the previous macro is shown in Figure 13.30, where the evolution of the sobol coefficient is shown for all
inputs with the uncertainty band, for the first order coefficient and the total one, respectively on the top and bottom panel.
Figure 13.30: Graph of the macro “sensitivitySobolWithData.py”

#### 13.6.14.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
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

###  13.6.15 Macro “sensitivitySobolLoadFile.py”

####  13.6.15.1 Objective

The objective of this macro is to perform a full Sobol analysis using the existing file created when the Sobol class is allowed
to perform the design-of-experiments and the estimations by itself when this one is not considered accurate enough (from
the statistical point of view). The idea is to use anyway all the computations already done and generate some more to
increase the statistical precision. In order to do that there are few things to keep in mind:

<!-- page 310 (PDF 317) -->
• The problem should obviously be exactly the same: same input and output (name, statistical laws, parameter values
…).
• The input file (here ref_sobol_launching_.dat) should contains the internal variable in order to figure
out from what matrices every configuration is taken out of (generally an iterator whose name should look like
sobol__n__iter__ plus the dataserver name).
• If the pseudo-random generator seed is set to a given value, be sure that you are not be using the same seed than
the once used to generate the input file, which would lead to twice the same events.
One can find another discussion for this objective in the third item in the tip box in Computation of Sobol’s sensitivity
indices.
Exclamation-Triangle Warning
The

```python
ref_sobol_launching_.dat
```

file
used
as
input
is
not
provided
in
the
usual
sub-directory
“/share/uranie/macros” of the installation folder of Uranie ($URANIESYS) but can be generated by the user
by running the macro discussed in Macro “sensitivitySobolFunctionFlowrate.py”.

#### 13.6.15.2 Macro Uranie

```python
"""
Example of sobol estimation once a file is loaded
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
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
ns = 100000
tsobol = Sensitivity.TSobol(tds, "flowrateModel", ns,
                            "rw:r:tu:tl:hu:hl:l:kw",
                            "flowrateModel", "DummyPython")
tsobol.loadOtherSobolFile("ref_sobol_launching_.dat")
tsobol.setDrawProgressBar(False)
tsobol.computeIndexes()
myfilter = "Algo==\"--first--\" || Algo==\"--total--\""
tsobol.getResultTuple().Scan("*", myfilter)
cc = ROOT.TCanvas("c1", "histgramme", 5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
```

<!-- page 311 (PDF 318) -->
```python
pad.Draw()
pad.Divide(2, 1)
pad.cd(1)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, hist, all")
pad.cd(2)
tsobol.drawIndexes("Flowrate", "", "nonewcanv, pie, first")
```

As for Macro “sensitivitySobolFunctionFlowrate.py”, the UserFunctions.C file is loaded and all the input stochastic
distribution are chosen wisely. The number of new estimations is set (to 10000, doubling the statistic as this is also the
number used in Macro “sensitivitySobolFunctionFlowrate.py” which provided the input file that would be used to complete
this estimation).
All the code lines are exactly those taken out of Macro Uranie but the one that is used to load a previous estimation which
is shown below:

```python
tsobol.loadOtherSobolFile("ref_sobol_launching_.dat")
```

Once done, the computeIndexes() method is called and few lines are shown to display the results in the classical plot
form, leading to the figure below (it is provided to illustrate how to represent results). The numerical results are shown
in the console below and the improvement in terms of statistical precision can be seen by comparing the 95 percent
confidence intervals going from Console to Console.

#### 13.6.15.3 Graph

The results of the previous macro is shown in Figure 13.31, where the evolution of the sobol coefficient is shown for all
inputs with the uncertainty band, for the first order coefficient and the total one, respectively on the top and bottom panel.
Figure 13.31: Graph of the macro “sensitivitySobolLoadFile.py”

<!-- page 312 (PDF 319) -->
#### 13.6.15.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
            Copyright (C) 2013-2026 CEA/DES
                     Contact: support-uranie@cea.fr
                    Date: Thu Feb 12, 2026
                                                                                                                 <URANIE::WARNING>
                                                                                                                                        <URANIE::WARNING> *** URANIE WARNING ***
                                                                                                                                                               <URANIE::WARNING> *** File[${SOURCEDIR}/dataSERVER/souRCE/TDataServer.cxx] Line[760]
                                                                                                                                                                                     <URANIE::WARNING> TDataServer::fileDataRead: Expected iterator tdsflowreate_1__n__iter__ not found but tdsflowreate__n_
```

˓→_iter__ looks like an URANIE iterator => Will be used as so.

```python
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
                                                                                                                                                                                           <URANIE::INFO> *** File[${SOURCEDIR}/meTIER/sampler/souRCE/TSamplerStochastic.cxx] Line[66]
                                                                                                                                                                                                             <URANIE::INFO> TSamplerStochastic::init: the TDS [tdsflowreate] contains data: we need to empty it !
                                                                                                                                                                                                                                <URANIE::INFO> *** END of URANIE INFORMATION ***
                                                                                                                                                                                                                                                   <URANIE::INFO>
                                     ** Case of Output atty [flowrateModel]
                                                                                                                                                                                                                                nSimPerIndex 20000
                                        ** Input att [rw] First [0.823516] Total Order[0.873849]
                                           ** Input att [r] First [0] Total Order[5.22438e-05]
                                             ** Input att [tu] First [0] Total Order[5e-05]
                                                ** Input att [tl] First [0] Total Order[6.08391e-05]
                                                   ** Input att [hu] First [0.0319889] Total Order[0.0547724]
                                                     ** Input att [hl] First [0.0304453] Total Order[0.0540884]
                                                        ** Input att [l] First [0.0315935] Total Order[0.0527791]
                                                           ** Input att [kw] First [0] Total Order[0.0129065]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ************************************************************************************************************
                                *
                                                                                                Row
                                *
                                                                                                                                                                                                                                Out.Out *
                                                                                                                                                                                                                                Inp.Inp * Order.Ord * Method.Me * Algo.Algo * Value.Val * CILower.C * CIUpper.C *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ************************************************************************************************************
```

<!-- page 313 (PDF 320) -->
```python
*
0 * flowrateM *
rw *
First *
Sobol * --first-- * 0.8235162 * 0.8190045 * 0.8279262 *
 *
 4 * flowrateM *
   rw *
       Total *
       Sobol * --total-- * 0.8738492 * 0.8602341 * 0.8875120 *
   *
   8 * flowrateM *
   r *
             First *
             Sobol * --first-- *
   0 *
   0 * 0.0138594 *
    *
        12 * flowrateM *
    r *
                    Total *
                    Sobol * --total-- * 5.224e-05 * 5.081e-05 * 5.371e-05 *
     *
           16 * flowrateM *
           tu *
                           First *
                           Sobol * --first-- *
     0 *
     0 * 0.0138594 *
       *
             20 * flowrateM *
             tu *
                                 Total *
                                 Sobol * --total-- * 5.000e-05 * 4.863e-05 * 5.140e-05 *
        *
                24 * flowrateM *
                tl *
                                        First *
                                        Sobol * --first-- *
        0 *
        0 * 0.0138594 *
         *
                   28 * flowrateM *
                   tl *
                                               Total *
                                               Sobol * --total-- * 6.083e-05 * 5.917e-05 * 6.254e-05 *
           *
                     32 * flowrateM *
                     hu *
                                                     First *
                                                     Sobol * --first-- * 0.0319888 * 0.0181374 * 0.0458280 *
            *
                        36 * flowrateM *
                        hu *
                                                            Total *
                                                            Sobol * --total-- * 0.0547723 * 0.0533147 * 0.0562686 *
             *
                           40 * flowrateM *
                           hl *
                                                                   First *
                                                                   Sobol * --first-- * 0.0304453 * 0.0165929 * 0.0442861 *
               *
                             44 * flowrateM *
                             hl *
                                                                         Total *
                                                                         Sobol * --total-- * 0.0540884 * 0.0526485 * 0.0555665 *
                *
                                48 * flowrateM *
                l *
                                                                                First *
                                                                                Sobol * --first-- * 0.0315935 * 0.0177418 * 0.0454330 *
                 *
                                   52 * flowrateM *
                 l *
                                                                                       Total *
                                                                                       Sobol * --total-- * 0.0527791 * 0.0513732 * 0.0542224 *
                   *
                                     56 * flowrateM *
                                     kw *
                                                                                             First *
                                                                                             Sobol * --first-- *
                   0 *
                   0 * 0.0138594 *
                    *
                                        60 * flowrateM *
                                        kw *
                                                                                                    Total *
                                                                                                    Sobol * --total-- * 0.0129065 * 0.0125558 * 0.0132669 *
                     *
                                           64 * flowrateM *
                                                                                                                                                     __sum__ *
                                                                                                           First *
                                                                                                           Sobol * --first-- * 0.9175440 *
                                           -1 *
                                           -1 *
                       *
                                             65 * flowrateM *
                                                                                                                                                               __sum__ *
                                                                                                                 Total *
                                                                                                                 Sobol * --total-- * 1.0485587 *
                                             -1 *
                                             -1 *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ************************************************************************************************************
                                                                            ==> 18 selected entries
```

<!-- page 314 (PDF 321) -->
### 13.6.16 Macro “sensitivityJohnsonRWFunctionFlowrate.py”

#### 13.6.16.1 Objective

The objective of this macro is to perform a sensitivity analysis using the Johnson’s relative weight method on a set of eight
parameters used in the flowrateModel model described in Presentation of the problem.

#### 13.6.16.2 Macro Uranie

```python
"""
Example of Johnson relative weight method applied to flowrate
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
# param Size of a sampling.
nS = 1000
FuncName = "flowrateModel"
tjrw = Sensitivity.TJohnsonRW(tds, FuncName, nS,
                              "rw:r:tu:tl:hu:hl:l:kw", FuncName)
tjrw.computeIndexes()
# Get the results on screen
tjrw.getResultTuple().Scan("Out:Inp:Method:Value", "Order==\"First\"")
# Get the results as plots
cc = ROOT.TCanvas("canhist", "histgramme")
tjrw.drawIndexes("Flowrate", "", "nonewcanv,hist,first")
cc.Print("appliUranieFlowrateJohnsonRW1000Histogram_py.png")
ccc = ROOT.TCanvas("canpie", "TPie")
tjrw.drawIndexes("Flowrate", "", "nonewcanv,pie")
ccc.Print("appliUranieFlowrateJohnsonRW1000Pie_py.png")
```

The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Each parameter is related to the TDataServer as a TAttribute and obeys an uniform law on specific interval

<!-- page 315 (PDF 322) -->
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

To instantiate the TJohnsonRW object, one uses the TDataServer, the name of the function, the number of samplings
needed to perform sensitivity analysis (here 𝑛𝑆=4000) and the input and output variables:

```python
tjrw = Sensitivity.TJohnsonRW(tds, FuncName, nS,
                              "rw:r:tu:tl:hu:hl:l:kw", FuncName)
```

Computation of sensitivity indexes:

```python
tjrw.computeIndexes()
```

The rest is very common to all sensitivity macros discussed here: it will produce two plots (the first one being a histogram
show below) and the console is also shown below for completness.

#### 13.6.16.3 Graph

Figure 13.32: Graph of the macro “sensitivityJohnsonRWFunctionFlowrate.py”

#### 13.6.16.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
```

<!-- page 316 (PDF 323) -->
```python
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
                                rw * JohnsonRW * 0.8636266 *
*
         2 * flowrateM *
                                 r * JohnsonRW * 4.598e-05 *
*
         4 * flowrateM *
                                tu * JohnsonRW * 8.775e-06 *
*
         6 * flowrateM *
                                tl * JohnsonRW * 9.689e-05 *
*
         8 * flowrateM *
                                hu * JohnsonRW * 0.0439173 *
*
        10 * flowrateM *
                                hl * JohnsonRW * 0.0435594 *
*
        12 * flowrateM *
                                 l * JohnsonRW * 0.0378304 *
*
        14 * flowrateM *
                                kw * JohnsonRW * 0.0109144 *
*
        16 * flowrateM *
                            __R2__ * JohnsonRW * 0.9447092 *
*
        18 * flowrateM *
                           __R2A__ * JohnsonRW * 0.9442633 *
************************************************************
==> 10 selected entries
```

###  13.6.17 Macro “sensitivityJohnsonRWCorrelatedFunctionFlowrate.py”

####  13.6.17.1 Objective

The objective of this macro is to perform a sensitivity analysis using the Johnson’s relative weight method on a set of
eight parameters used in the flowrateModel model described in Presentation of the problem. Compared to version
detailled in Macro “sensitivityJohnsonRWFunctionFlowrate.py”, the idea is here to correlate the input variables with a
random correlation matrix.

#### 13.6.17.2 Macro Uranie

```python
"""
Example of Johson relative weight method applied to flowrate
"""
from math import sqrt
from URANIE import DataServer, Sensitivity
import ROOT
def gen_corr(_nx=8, correlated=True, seed=0):
    """Generate randomly a good, highly-correlated, input correlation matrix."""
    # Define a randomly filled matrix
```

<!-- page 317 (PDF 324) -->
```python
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
    return in_corr
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
# \param Size of a sampling.
nS = 1000
FuncName = "flowrateModel"
# Get a correlation matrix for the inputs
inCorr = gen_corr(8, True, args.seed)
inCorr.Print()
tjrw = Sensitivity.TJohnsonRW(tds, FuncName, nS,
                              "rw:r:tu:tl:hu:hl:l:kw", FuncName)
# Set the correlation
tjrw.setInputCorrelationMatrix(inCorr)
tjrw.computeIndexes()
# Get the results on screen
tjrw.getResultTuple().Scan("Out:Inp:Method:Value", "Order==\"First\"")
```

<!-- page 318 (PDF 325) -->
```python
# Get the results as plots
cc = ROOT.TCanvas("canhist", "histgramme")
tjrw.drawIndexes("Flowrate", "", "nonewcanv, hist, first")
cc.Print("appliUranieFlowrateJohnsonRWCorrelated1000Histogram_py.png")
ccc = ROOT.TCanvas("canpie", "TPie")
tjrw.drawIndexes("Flowrate", "", "nonewcanv, pie")
ccc.Print("appliUranieFlowrateJohnsonRWCorrelated1000Pie_py.png")
```

The first function, called GenCorr, is not discussed, because it is really technical and not really interesting here. The only
thing to know is that it provides a proper correlation matrix: a positive-definite symmetrical matrix.
The function flowrateModel is loaded from the macro UserFunctions.C (the file can be found in ${URANIESYS}/
share/uranie/macros)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Compared to the discussion in Macro Uranie, the instantiation of the attributes and the TJohnsonRW object is the same.
The only difference is done when injecting the correlation matrix, which is done in these lines:

```python
# Get a correlation matrix for the inputs
inCorr = gen_corr(8, True, args.seed)
tjrw = Sensitivity.TJohnsonRW(tds, FuncName, nS,
                              "rw:r:tu:tl:hu:hl:l:kw", FuncName)
# Set the correlation
tjrw.setInputCorrelationMatrix(inCorr)
```

The computation of sensitivity indices can finally be done:

```python
tjrw.computeIndexes()
```

The rest is very common to all sensitivity macros discussed here: it will produce two plots (the first one being a histogram
show below) and the console is also shown below for completness.

<!-- page 319 (PDF 326) -->
#### 13.6.17.3 Graph

Figure 13.33: Graph of the macro “sensitivityJohnsonRWCorrelatedFunctionFlowrate.py”

#### 13.6.17.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
8x8 matrix is as follows
     |
                 |
                             |
                                         |
                                                     |
                                                                 |
----------------------------------------------------------------------
   0 |
                       0.4488
                                   0.2894
                                             -0.05727
                                                           0.3627
   1 |
           0.4488
                                  0.02022
                                              -0.2547
                                                           0.3764
   2 |
           0.2894
                      0.02022
                                               0.4982
                                                          -0.2078
   3 |
         -0.05727
                      -0.2547
                                   0.4982
                                                          -0.9199
   4 |
           0.3627
                       0.3764
                                  -0.2078
                                              -0.9199
   5 |
           0.2569
                      -0.1996
                                   -0.288
                                               0.1004
                                                          -0.1362
   6 |
          -0.2167
                      -0.4425
                                 0.004268
                                               0.1412
                                                           -0.111
   7 |
          -0.2948
                       0.1982
                                -0.001661
                                               0.1943
                                                          -0.3131
     |
                 |
                             |
                                         |
----------------------------------------------------------------------
   0 |
           0.2569
                      -0.2167
                                  -0.2948
   1 |
          -0.1996
                      -0.4425
                                   0.1982
   2 |
           -0.288
                     0.004268
                                -0.001661
   3 |
           0.1004
                       0.1412
                                   0.1943
   4 |
          -0.1362
                       -0.111
                                  -0.3131
   5 |
                      -0.1943
                                   0.2848
```
