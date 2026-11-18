# Use-cases in Python — Macros DataServer — Macro “dataserverAttributes.py” … Macro “dataserverComputeQuantile.py”
<!-- source PDF pages 209-228 -->

<!-- page 202 (PDF 209) -->
```python
Result is
4.0
```

##  13.3 Macros DataServer

In a first step, to get accustomed with TDataServer, we propose different macros related to this subject. Since it
constitutes the preliminary and almost mandatory step of a proper use of Uranie, these macros are only for educational
purposes.

### 13.3.1 Macro “dataserverAttributes.py”

#### 13.3.1.1 Objective

The goal of this macro is only to master the objects TAttribute and TDataServer of Uranie. Three attributes will
be created and linked to a TDataServer object, then the log of this object will be printed to check internal data of this
TDataServer.

#### 13.3.1.2 Macro Uranie

```python
"""
Example of attribute management
"""
from URANIE import DataServer
# Define the attribute "x"
px = DataServer.TAttribute("x", -2.0, 4.0)
px.setTitle("#Delta P^{#sigma}")
px.setUnity("#frac{mm^{2}}{s}")
# Define the attribute "y"
py = DataServer.TAttribute("y", 0.0, 1.0)
# Define the DataServer of the study
tds = DataServer.TDataServer("tds", "my first TDS")
# Add the attributes in the DataServer.TDataServer
tds.addAttribute(px)
tds.addAttribute(py)
tds.addAttribute(DataServer.TAttribute("z", 0.25, 0.50))
tds.printLog()
```

The first attribute “x” is defined on [-2.0, 4.0]; its title is Δ𝑃𝜎and unity 𝑚𝑚2
𝑠

```python
px = DataServer.TAttribute("x", -2.0, 4.0)
px.setTitle("#Delta P^{#sigma}")
px.setUnity("#frac{mm^{2}}{s}")
```

The second attribute “y” is defined on [0.0,1.0]; it will be set with its name as title but without unity.

```python
py = DataServer.TAttribute("y", 0.0, 1.0)
```

Secondly, a TDataServer object is created and the two attributes x and y created before are linked to this one.

<!-- page 203 (PDF 210) -->
```python
tds = DataServer.TDataServer("tds", "my first TDS")
tds.addAttribute(px)
tds.addAttribute(py)
```

Finally, the last attribute z (defined on [0.25,0.50]) is directly added to the TDataServer (its title will be its name and
it will be set without unity) by creating it. An attribute could, indeed, be added to a TDataServer meanwhile creating
it, but then no other information than those available in the constructor would be set.

```python
tds.addAttribute(DataServer.TAttribute("z", 0.25, 0.50))
```

Then, the log of the TDataServer object is printed.

```python
tds.printLog()
```

Generally speaking, all Uranie objects have the printLog method which allows to print internal data of the object.

#### 13.3.1.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
TDataServer::printLog[]
Name[tds] Title[my first TDS]
Origin[Unknown]
 _sdatafile[]
 _sarchivefile[_dataserver_.root]
*******************************
** TDataSpecification::printLog
                                 ******
**
     Name[uheader__tds] Title[Header of my first TDS]
**
     relationName[Header of my first TDS]
**
     attributs[4]
**** With _listOfAttributes
 Attribute[0/4]
*******************************
** TAttribute::printLog
                         ******
**
      Name[tds__n__iter__]
**
     Title[tds__n__iter__]
**
     unity[]
**
      type[0]
**
     share[1]
**
     Origin[kIterator]
**
     Attribute[kInput]
**
     _snote[]
--------------------------------------------------------------------------------------
```

˓→------

```python
--------------------------------------------------------------------------------------
```

˓→------

```python
** - min[] max[]
** - mean[] std[]
**
     lowerBound[-1.42387e+64] upperBound[1.42387e+64]
** NOT _defaultValue[]
```

<!-- page 204 (PDF 211) -->
```python
** NOT _stepValue[]
 ** No Attribute to substitute level[0]
*******************************
 Attribute[1/4]
*******************************
** TAttribute::printLog
                         ******
**
      Name[x]
**
     Title[#Delta P^{#sigma}]
**
     unity[#frac{mm^{2}}{s}]
**
      type[0]
**
     share[2]
**
     Origin[kAttribute]
**
     Attribute[kInput]
**
     _snote[]
--------------------------------------------------------------------------------------
```

˓→------

```python
--------------------------------------------------------------------------------------
```

˓→------

```python
** - min[] max[]
** - mean[] std[]
**
     lowerBound[-2] upperBound[4]
** NOT _defaultValue[]
** NOT _stepValue[]
 ** No Attribute to substitute level[0]
*******************************
 Attribute[2/4]
*******************************
** TAttribute::printLog
                         ******
**
      Name[y]
**
     Title[y]
**
     unity[]
**
      type[0]
**
     share[2]
**
     Origin[kAttribute]
**
     Attribute[kInput]
**
     _snote[]
--------------------------------------------------------------------------------------
```

˓→------

```python
--------------------------------------------------------------------------------------
```

˓→------

```python
** - min[] max[]
** - mean[] std[]
**
     lowerBound[0] upperBound[1]
** NOT _defaultValue[]
** NOT _stepValue[]
 ** No Attribute to substitute level[0]
*******************************
 Attribute[3/4]
*******************************
** TAttribute::printLog
                         ******
**
      Name[z]
**
     Title[z]
```

<!-- page 205 (PDF 212) -->
```python
**
     unity[]
**
      type[0]
**
     share[2]
**
     Origin[kAttribute]
**
     Attribute[kInput]
**
     _snote[]
--------------------------------------------------------------------------------------
```

˓→------

```python
--------------------------------------------------------------------------------------
```

˓→------

```python
** - min[] max[]
** - mean[] std[]
**
     lowerBound[0.25] upperBound[0.5]
** NOT _defaultValue[]
** NOT _stepValue[]
 ** No Attribute to substitute level[0]
*******************************
** TDataSpecification::fin de printLog *******************************
fin de TDataServer::printLog[]
```

###  13.3.2 Macro “dataserverMerge.py”

####  13.3.2.1 Objective

The objective of this macro is to merge data contained in a TDataServer with data contained in another TDataServer.
Both TDataServer have to contain the same number of patterns. We choose here to merge two TDataServer, loaded
from two ASCII files, each of which contains 9 patterns.
The first ASCII file "tds1.dat" defines the four variables x, dy, z, theta:

```python
#COLUMN_NAMES: x| dy| z| theta
#COLUMN_TITLES: x_{n}| "#delta y"| ""| #theta
#COLUMN_UNITS: N| Sec| KM/Sec| M^{2}
1 1 11 11
1 2 12 21
1 3 13 31
2 1 21 12
2 2 22 22
2 3 23 32
3 1 31 13
3 2 32 23
3 3 33 33
```

and the second ASCII file "tds2.dat" defines the four other variables x2, y, u, ua:

```python
#COLUMN_NAMES: x2| y| u| ua
1 1 102 11
1 2 104 12
1 3 106 13
2 1 202 21
2 2 204 22
```

<!-- page 206 (PDF 213) -->
```python
2 3 206 23
3 1 302 31
3 2 304 32
3 3 306 33
```

The merging operation will be executed in the first TDataServer tds1; so it will contain all the attributes at the end.

#### 13.3.2.2 Macro Uranie

```python
"""
Example of data merging
"""
from URANIE import DataServer
tds1 = DataServer.TDataServer()
tds2 = DataServer.TDataServer()
tds1.fileDataRead("tds1.dat")
print("Dumping tds1")
tds1.Scan("*")
tds2.fileDataRead("tds2.dat")
print("Dumping tds2")
tds2.Scan("*")
tds1.merge(tds2)
print("Dumping merged tds1 and tds2")
tds1.Scan("*", "", "colsize=3 col=9::::::::")
```

Both TDataServers are filled with ASCII data files with the method filedataRead().

```python
tds1.fileDataRead("tds1.dat")
tds2.fileDataRead("tds2.dat")
```

Data of the second dataserver tds2 are then merged into the first one.

```python
tds1.merge(tds2)
```

Data are then dumped in the terminal:

```python
tds1.Scan("*")
```

####  13.3.2.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
Dumping tds1
************************************************************************
*
     Row
           * tds1__n__ *
                               x.x *
                                         dy.dy *
                                                       z.z * theta.the *
```

<!-- page 207 (PDF 214) -->
```python
************************************************************************
*
         0 *
                     1 *
                                 1 *
                                             1 *
                                                        11 *
                                                                    11 *
*
         1 *
                     2 *
                                 1 *
                                             2 *
                                                        12 *
                                                                    21 *
*
         2 *
                     3 *
                                 1 *
                                             3 *
                                                        13 *
                                                                    31 *
*
         3 *
                     4 *
                                 2 *
                                             1 *
                                                        21 *
                                                                    12 *
*
         4 *
                     5 *
                                 2 *
                                             2 *
                                                        22 *
                                                                    22 *
*
         5 *
                     6 *
                                 2 *
                                             3 *
                                                        23 *
                                                                    32 *
*
         6 *
                     7 *
                                 3 *
                                             1 *
                                                        31 *
                                                                    13 *
*
         7 *
                     8 *
                                 3 *
                                             2 *
                                                        32 *
                                                                    23 *
*
         8 *
                     9 *
                                 3 *
                                             3 *
                                                        33 *
                                                                    33 *
************************************************************************
Dumping tds2
************************************************************************
*
     Row
           * tds2__n__ *
                             x2.x2 *
                                           y.y *
                                                       u.u *
                                                                 ua.ua *
************************************************************************
*
         0 *
                     1 *
                                 1 *
                                             1 *
                                                       102 *
                                                                    11 *
*
         1 *
                     2 *
                                 1 *
                                             2 *
                                                       104 *
                                                                    12 *
*
         2 *
                     3 *
                                 1 *
                                             3 *
                                                       106 *
                                                                    13 *
*
         3 *
                     4 *
                                 2 *
                                             1 *
                                                       202 *
                                                                    21 *
*
         4 *
                     5 *
                                 2 *
                                             2 *
                                                       204 *
                                                                    22 *
*
         5 *
                     6 *
                                 2 *
                                             3 *
                                                       206 *
                                                                    23 *
*
         6 *
                     7 *
                                 3 *
                                             1 *
                                                       302 *
                                                                    31 *
*
         7 *
                     8 *
                                 3 *
                                             2 *
                                                       304 *
                                                                    32 *
*
         8 *
                     9 *
                                 3 *
                                             3 *
                                                       306 *
                                                                    33 *
************************************************************************
Dumping merged tds1 and tds2
************************************************************************
*
     Row
           * tds1__n__ * x.x * dy. * z.z * the * x2. * y.y * u.u * ua. *
************************************************************************
*
         0 *
                     1 *
                           1 *
                                 1 *
                                      11 *
                                            11 *
                                                   1 *
                                                         1 * 102 *
                                                                    11 *
*
         1 *
                     2 *
                           1 *
                                 2 *
                                      12 *
                                            21 *
                                                   1 *
                                                         2 * 104 *
                                                                    12 *
*
         2 *
                     3 *
                           1 *
                                 3 *
                                      13 *
                                            31 *
                                                   1 *
                                                         3 * 106 *
                                                                    13 *
*
         3 *
                     4 *
                           2 *
                                 1 *
                                      21 *
                                            12 *
                                                   2 *
                                                         1 * 202 *
                                                                    21 *
*
         4 *
                     5 *
                           2 *
                                 2 *
                                      22 *
                                            22 *
                                                   2 *
                                                         2 * 204 *
                                                                    22 *
*
         5 *
                     6 *
                           2 *
                                 3 *
                                      23 *
                                            32 *
                                                   2 *
                                                         3 * 206 *
                                                                    23 *
*
         6 *
                     7 *
                           3 *
                                 1 *
                                      31 *
                                            13 *
                                                   3 *
                                                         1 * 302 *
                                                                    31 *
*
         7 *
                     8 *
                           3 *
                                 2 *
                                      32 *
                                            23 *
                                                   3 *
                                                         2 * 304 *
                                                                    32 *
*
         8 *
                     9 *
                           3 *
                                 3 *
                                      33 *
                                            33 *
                                                   3 *
                                                         3 * 306 *
                                                                    33 *
************************************************************************
```

###  13.3.3 Macro “dataserverLoadASCIIFilePasture.py”

####  13.3.3.1 Objective

The objective of this macro is to load two TDataServer objects using two different ways: either with an ASCII file
"pasture.dat" or with a design-of-experiments. Then, we evaluate the analytic function ModelPasture on this two
TDataServer. The data file "pasture.dat" is written in the “Salome-table” format of Uranie:

```python
#COLUMN_NAMES: time| yield
9 8.93
14 10.8
```

<!-- page 208 (PDF 215) -->
```python
21 18.59
28 22.33
42 39.35
57 56.11
63 61.73
70 64.62
79 67.08
```

####  13.3.3.2 Macro Uranie

```python
"""
Example of data loading with pasture file
"""
from URANIE import DataServer, Sampler, Launcher
import ROOT
C = ROOT.TCanvas("mycanvas", "mycanvas", 1)
ROOT.gROOT.LoadMacro("UserFunctions.C")
tds = DataServer.TDataServer()
tds.fileDataRead("pasture.dat")
tds.getTuple().SetMarkerStyle(8)
tds.getTuple().SetMarkerSize(1.5)
tds.draw("yield:time")
tlf = Launcher.TLauncherFunction(tds, "ModelPasture", "time", "yhat")
tlf.run()
tds.getTuple().SetMarkerColor(ROOT.kBlue)
tds.getTuple().SetLineColor(ROOT.kBlue)
tds.draw("yhat:time", "", "lpsame")
tds2 = DataServer.TDataServer()
tds2.addAttribute(DataServer.TUniformDistribution("time2", 9, 80))
tsamp = Sampler.TSampling(tds2, "lhs", 1000)
tsamp.generateSample()
tds2.getTuple().SetMarkerColor(ROOT.kGreen)
tds2.getTuple().SetLineColor(ROOT.kGreen)
tlf = Launcher.TLauncherFunction(tds2, "ModelPasture", "", "yhat2")
tlf.run()
tds2.draw("yhat2:time2", "", "psame")
tds.draw("yhat:time", "", "lpsame")
ROOT.gPad.SaveAs("pasture.png")
```

The design ModelPasture is defined in a function

<!-- page 209 (PDF 216) -->
```python
void ModelPasture(Double_t *x, Double_t *y)
{
  Double_t theta1=69.95, theta2=61.68, theta3=-9.209, theta4=2.378;
  y[0] = theta1;
  y[0] -= theta2* TMath::Exp( -1.0 * TMath::Exp( theta3 + theta4 * TMath::Log(x[0])));
}
```

Which is C++ and is loaded thanks to the function ROOT.gROOT.LoadMacro("UserFunctions.C").
The first TDataServer is filled with the ASCII file "pasture.dat" through the fileDataRead method

```python
tds.fileDataRead("pasture.dat")
```

The design is evaluated with the function ModelPasture applied on the input attribute time, leading to the output attribute
named yhat.

```python
tlf = Launcher.TLauncherFunction(tds, "ModelPasture", "time", "yhat")
tlf.run()
```

A TAttribute, obeying an uniform law on [9;80] is added to the second TDataServer which is filled with a
design-of-experiments of 1000 patterns, using the LHS method.

```python
tsamp = Sampler.TSampling(tds2, "lhs", 1000)
tsamp.generateSample()
```

The design is now evaluated with this TDataServer on the attribute time2

```python
tlf = Launcher.TLauncherFunction(tds2, "ModelPasture", "", "yhat2")
tlf.run()
```

####  13.3.3.3 Graph

Figure 13.2: Graph of the macro "dataserverLoadASCIIFilePasture.py"

<!-- page 210 (PDF 217) -->
#### 13.3.3.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
Info in <TCanvas::Print>: png file pasture.png has been created
```

###  13.3.4 Macro “dataserverLoadASCIIFile.py”

####  13.3.4.1 Objective

Loading data in a TDataServer, using the “Salome-table” format of Uranie and applying basic visualisation methods
on attributes.
The data file is named "flowrateUniformDesign.dat" and data correspond to an Uniform design-of-experiments
of 32 patterns for a “code” with 8 inputs (𝑟𝜔, 𝑟, 𝑇𝑢, 𝑇𝑙, 𝐻𝑢, 𝐻𝑙, 𝐿, 𝐾𝜔) along with a response (“yhat”). The data file
"flowrateUniformDesign.dat" is in the “Salome-table” format of Uranie.

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
```

<!-- page 211 (PDF 218) -->
```python
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

####  13.3.4.2 Macro Uranie

```python
"""
Example of data loading file
"""
from URANIE import DataServer
import ROOT
# Create a DataServer.TDataServer
tds = DataServer.TDataServer()
# Load the data base in the DataServer
tds.fileDataRead("flowrateUniformDesign.dat")
# Graph
Canvas = ROOT.TCanvas("c1", "Graph for the Macro loadASCIIFile",
                      5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2, 2)
pad.cd(1)
tds.draw("ystar")
pad.cd(2)
tds.draw("ystar:rw")
pad.cd(3)
tds.drawTufte("ystar:rw")
pad.cd(4)
tds.drawProfile("ystar:rw")
tds.startViewer()
```

<!-- page 212 (PDF 219) -->
#### 13.3.4.3 Graph

Figure 13.3: Graph of the macro "dataserverLoadASCIIFile.py"

### 13.3.5 Macro “dataserverLoadASCIIFileYoungsModulus.py”

#### 13.3.5.1 Objective

The objective of this macro is to load the ASCII data file "youngsmodulus.dat" and to apply visualisations on the
attribute E with different options. The data file "youngsmodulus.dat" is in the “Salome-table” format of Uranie.

```python
#NAME: youngsmodulus
#TITLE: Young's Modulus E for the Golden Gate Bridge
#COLUMN_NAMES: E
#COLUMN_TITLES: Young's Modulues
#COLUMN_UNITS: ksi
```

<!-- page 213 (PDF 220) -->
```python
```

Data are then exported in header file "youngsmodulus.h" which can be imported in some C file:

```python
// File "youngsmodulus.h" generated by ROOT v5.34/32
// DateTime Tue Nov
                     3 10:40:13 2015
// DataServer : Name="youngsmodulus" Title="Young's Modulus E for the Golden Gate␣
```

˓→Bridge" Global Select=""

```python
#define youngsmodulus_nPattern 41
//
    Attribute Name="E"
Double_t E[youngsmodulus_nPattern] = {
 2.890000000e+04,
 2.920000000e+04,
 2.740000000e+04,
 2.870000000e+04,
 2.840000000e+04,
 2.990000000e+04,
 3.020000000e+04,
 2.950000000e+04,
 2.960000000e+04,
 2.840000000e+04,
 2.830000000e+04,
 2.930000000e+04,
 2.930000000e+04,
 2.810000000e+04,
```

<!-- page 214 (PDF 221) -->
```python
 3.020000000e+04,
 3.020000000e+04,
 3.030000000e+04,
 3.120000000e+04,
 2.880000000e+04,
 2.760000000e+04,
 2.960000000e+04,
 2.590000000e+04,
 3.200000000e+04,
 3.340000000e+04,
 3.060000000e+04,
 3.270000000e+04,
 3.130000000e+04,
 3.050000000e+04,
 3.130000000e+04,
 2.900000000e+04,
 2.940000000e+04,
 2.830000000e+04,
 3.050000000e+04,
 3.110000000e+04,
 2.930000000e+04,
 2.740000000e+04,
 2.930000000e+04,
 2.930000000e+04,
 3.130000000e+04,
 2.750000000e+04,
 2.940000000e+04,
};
// End of attribute E
// End of File youngsmodulus.h
```

####  13.3.5.2 Macro Uranie

```python
"""
Example of young modulus data loading
"""
from URANIE import DataServer
import ROOT
tds = DataServer.TDataServer()
tds.fileDataRead("youngsmodulus.dat")
# gEnv.SetValue("Hist.Binning.1D.x", 10)
# tds.getTuple().Draw("E>>Attribute E(6, 25000, 34000)", "", "text")
# tds.getTuple().Draw("E>>Attribute E(16, 25000, 34000)")
tds.computeStatistic("E")
tds.getAttribute("E").printLog()
tds.exportDataHeader("youngsmodulus.h")
```

<!-- page 215 (PDF 222) -->
```python
Canvas = ROOT.TCanvas("c1", "Graph for the Macro loadASCIIFile",
                      5, 64, 1270, 667)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(2, 2)
pad.cd(1)
tds.draw("E")
pad.cd(2)
tds.draw("E", "", "nclass=sturges")
pad.cd(3)
tds.draw("E", "", "nclass=scott")
pad.cd(4)
tds.draw("E", "", "nclass=fd")
```

The TDataServer is filled with the ASCII data file "youngsmodulus.dat" with the method fileDataRead:

```python
tds.fileDataRead("youngsmodulus.dat")
```

Variable E is then visualised with different options:

```python
tds.draw("E", "", "nclass=sturges")
tds.draw("E", "", "nclass=scott")
tds.draw("E", "", "nclass=fd")
```

Characteristic values are computed (maximum, minimum, mean and standard deviation) with:

```python
tds.computeStatistic("E")
```

Data are exported in a header file with

```python
tds.exportDataHeader("youngsmodulus.h")
```

<!-- page 216 (PDF 223) -->
#### 13.3.5.3 Graph

Figure 13.4: Graph of the macro "dataserverLoadASCIIFileYoungsModulus.py"

#### 13.3.5.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
*******************************
** TAttribute::printLog
                         ******
**
      Name[E]
**
     Title[ Young's Modulues]
**
     unity[ksi]
**
      type[0]
**
     share[1]
**
     Origin[kAttribute]
**
     Attribute[kInput]
**
     _snote[]
--------------------------------------------------------------------------------------
```

˓→------

```python
--------------------------------------------------------------------------------------
```

˓→------

```python
** - min[25900] max[33400]
** - mean[29575.6] std[1506.95]
**
     lowerBound[-1.42387e+64] upperBound[1.42387e+64]
** NOT _defaultValue[]
** NOT _stepValue[]
 ** No Attribute to substitute level[0]
```

<!-- page 217 (PDF 224) -->
```python
*******************************
```

###  13.3.6 Macro “dataserverLoadASCIIFileIonosphere.py”

####  13.3.6.1 Objective

The objective of this macro is to load the ASCII data file ionosphere.dat which defines 34 input variables and one output
variable y and applies visualisation on one of these variables. The data file ionosphere.dat is in the “Salome-table”
format of Uranie but is not shown for convenience.

#### 13.3.6.2 Macro Uranie

```python
"""
Example of data loading for Ionosphere dataset
"""
from URANIE import DataServer
import ROOT
tds = DataServer.TDataServer()
tds.fileDataRead("ionosphere.dat")
tds.getAttribute("x28").SetTitle("#Delta P_{e}^{F_{iso}}")
# Graph
Canvas = ROOT.TCanvas("c1", "Graph for the Macro loadASCIIFileIonosphere",
                      5, 64, 1270, 667)
tds.draw("x28")
```

The TDataServer is filled with ionosphere.dat with the fileDataRead method

```python
tds.fileDataRead("ionosphere.dat")
```

A new title is set for the variable x28

```python
tds.getAttribute("x28").SetTitle("#Delta P_{e}^{F_{iso}}")
```

This variable is then drawn with its new title

```python
tds.draw("x28")
```

<!-- page 218 (PDF 225) -->
#### 13.3.6.3 Graph

Figure 13.5: Graph of the macro "dataserverLoadASCIIFileIonosphere.py"

### 13.3.7 Macro “dataserverLoadASCIIFileCornell.py”

#### 13.3.7.1 Objective

The objective of this macro is to load the ASCII data file cornell.dat which defines seven input variables and one
output variable y on twelve patterns. The input file cornell.dat is in the “Salome-table” format of Uranie

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

<!-- page 219 (PDF 226) -->
#### 13.3.7.2 Macro Uranie

```python
"""
Example of data loading and stat analysis
"""
from URANIE import DataServer
tds = DataServer.TDataServer()
tds.fileDataRead("cornell.dat")
matCorr = tds.computeCorrelationMatrix("")
matCorr.Print()
```

The TDataServer is filled with cornell.dat with the fileDataRead method:

```python
tds.fileDataRead("cornell.dat")
```

Then the correlation matrix is computed on all attributes:

```python
matCorr = tds.computeCorrelationMatrix("")
```

####  13.3.7.3 Console

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
                       0.1042
                                   0.9999
                                               0.3707
                                                           -0.548
   1 |
           0.1042
                                   0.1008
                                              -0.5369
                                                          -0.2926
   2 |
           0.9999
                       0.1008
                                                0.374
                                                          -0.5482
   3 |
           0.3707
                      -0.5369
                                    0.374
                                                          -0.2113
   4 |
           -0.548
                      -0.2926
                                  -0.5482
                                              -0.2113
   5 |
          -0.8046
                      -0.1912
                                  -0.8052
                                              -0.6457
                                                           0.4629
   6 |
           0.6026
                        -0.59
                                   0.6071
                                               0.9159
                                                          -0.2744
   7 |
          -0.8373
                     -0.07082
                                   -0.838
                                              -0.7067
                                                           0.4938
     |
                 |
                             |
                                         |
----------------------------------------------------------------------
   0 |
          -0.8046
                       0.6026
                                  -0.8373
   1 |
          -0.1912
                        -0.59
                                 -0.07082
   2 |
          -0.8052
                       0.6071
                                   -0.838
   3 |
          -0.6457
                       0.9159
                                  -0.7067
   4 |
           0.4629
                      -0.2744
                                   0.4938
   5 |
                      -0.6564
                                   0.9851
   6 |
          -0.6564
                                  -0.7411
   7 |
           0.9851
                      -0.7411
```

<!-- page 220 (PDF 227) -->
### 13.3.8 Macro “dataserverComputeQuantile.py”

#### 13.3.8.1 Objective

The objective of this macro is to test the classical quantile estimation and compare it to the Wilks estimation for a dummy
gaussian distribution. Four different estimations of the 95% quantile value are done (along with one estimation of th 99%
quantile) for illustration purposes:
• using the usual method with a 200-points sample.
• using the usual method with a 400-points sample.
• using the Wilks method with a 95% confidence level (with 59-points sample).
• using the Wilks method with a 95% confidence level (with 400-points sample).
• using the Wilks method with a 99% confidence level (with 90-points sample).

#### 13.3.8.2 Macro Uranie

```python
"""
Example of quantile estimation (Wilks and not) for illustration purpose
"""
from ctypes import c_double
                             # For ROOT version greater or equal to 6.20
import numpy as np
from URANIE import DataServer
import ROOT
# Create a DataServer
tds = DataServer.TDataServer("foo", "pouet")
tds.addAttribute("x")
                       # With one attribute
# Create Histogram to store the quantile values
Q200 = ROOT.TH1F("quantile200", "", 60, 1, 4)
Q200.SetLineColor(1)
Q200.SetLineWidth(2)
Q400 = ROOT.TH1F("quantile400", "", 60, 1, 4)
Q400.SetLineColor(4)
Q400.SetLineWidth(2)
QW95 = ROOT.TH1F("quantileWilks95", "", 60, 1, 4)
QW95.SetLineColor(2)
QW95.SetLineWidth(2)
QW95400 = ROOT.TH1F("quantileWilks95400", "", 60, 1, 4)
QW95400.SetLineColor(8)
QW95400.SetLineWidth(2)
QW99 = ROOT.TH1F("quantileWilks99", "", 60, 1, 4)
QW99.SetLineColor(6)
QW99.SetLineWidth(2)
# Defining the sample size
nb = np.array([200, 400, 59, 90])
proba = 0.95
              # Quantile value
CL = np.array([0.95, 0.99])
                             # Confidence level value for the two Wilks computation
# Loop over the number of estimation
for iq in range(4):
```

<!-- page 221 (PDF 228) -->
```python
    # Produce 10000 drawing to get smooth distribution
    for itest in range(10000):
        tds.createTuple()
                           # Create the tuple to store value
        # Fill it with random drawing of centered gaussian
        for ival in range(nb[iq]):
            tds.getTuple().Fill(ival+1, ROOT.gRandom.Gaus(0, 1))
        # Estimate the quantile...
        quant = c_double(0)
                             # ROOT.Double for ROOT version lower than 6.20
        if iq < 2:
            # ... with usual methods...
            tds.computeQuantile("x", proba, quant)
            if iq == 0:
                Q200.Fill(quant.value)
                                        # ... on a 200-points sample
            else:
                Q400.Fill(quant.value)
                                        # ... on a 400-points sample
                tds.estimateQuantile("x", proba, quant, CL[iq-1])
                QW95400.Fill(quant.value)
                                           # compute the quantile at 95% CL
        else:
            # ... with the wilks optimised sample
            tds.estimateQuantile("x", proba, quant, CL[iq-2])
            if iq == 2:
                QW95.Fill(quant.value)
                                        # compute the quantile at 95% CL
            else:
                QW99.Fill(quant.value)
                                        # compute the quantile at 99% CL
        # Delete the tuple
        tds.deleteTuple()
# Produce the plot with requested style
ROOT.gStyle.SetOptStat(0)
can = ROOT.TCanvas("Can", "Can", 10, 10, 1000, 1000)
Q400.GetXaxis().SetTitle("Quant_{95%}(Gaus_{(0, 1)})")
Q400.GetXaxis().SetTitleOffset(1.2)
Q400.Draw()
Q200.Draw("same")
QW95.Draw("same")
QW95400.Draw("same")
QW99.Draw("same")
# Add the theoretical estimation
lin = ROOT.TLine()
lin.SetLineStyle(3)
lin.DrawLine(1.645, 0, 1.645, Q400.GetMaximum())
# Add a block of legend
leg = ROOT.TLegend(0.4, 0.6, 0.8, 0.85)
leg.AddEntry(lin, "Theoretical quantile", "l")
```
