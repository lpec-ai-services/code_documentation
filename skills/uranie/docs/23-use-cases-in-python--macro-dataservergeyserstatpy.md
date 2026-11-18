# Use-cases in Python — Macros DataServer — Macro “dataserverGeyserStat.py” … Macro “dataserverPCAExample.py”
<!-- source PDF pages 229-245 -->

<!-- page 222 (PDF 229) -->
```python
leg.AddEntry(Q200, "Usual quantile (200 pts)", "l")
leg.AddEntry(Q400, "Usual quantile (400 pts)", "l")
leg.AddEntry(QW95, "Wilks quantile CL=95% (59 pts)", "l")
leg.AddEntry(QW95400, "Wilks quantile CL=95% (400 pts)", "l")
leg.AddEntry(QW99, "Wilks quantile CL=99% (90 pts)", "l")
leg.SetBorderSize(0)
leg.Draw()
```

In this macro, a dummy dataserver is created with a single attribute named “x”. Four histograms are prepared to store
the resulting value. Then the same loop will be used to computed 10000 values of every quantile with different switchs
to use one method instead of the other, or to change the number of points in the sample and/or the confidence level. All
this is defined in the small part before the loop:

```python
# Defining the sample size
nb = np.array([200, 400, 59, 90])
proba = 0.95
              # Quantile value
CL = np.array([0.95, 0.99])
                             # Confidence level value for the two Wilks computation
```

Then the computation is performed, first for the usual method (first two iterations of iq), then for the Wilks estimation
(last two iterations of iq). Every computational result is stored in the corresponding histogram which is finally displayed
and shown in the following subsection.

#### 13.3.8.3 Graph

Figure 13.6: Graph of the macro "dataserverComputeQuantile.py"

### 13.3.9 Macro “dataserverGeyserStat.py”

#### 13.3.9.1 Objective

This part shows the complete code used to produce the console display in Computing the elementary statistic.

<!-- page 223 (PDF 230) -->
#### 13.3.9.2 Macro Uranie

```python
"""
Example of statistical usage
"""
from URANIE import DataServer
tdsGeyser = DataServer.TDataServer("geyser", "poet")
tdsGeyser.fileDataRead("geyser.dat")
tdsGeyser.computeStatistic("x1")
print("min(x1)= "+str(tdsGeyser.getAttribute("x1").getMinimum())+";
                                                                     max(x1)= "
      + str(tdsGeyser.getAttribute("x1").getMaximum())+";
                                                           mean(x1)= " +
      str(tdsGeyser.getAttribute("x1").getMean())+";
                                                      std(x1)= " +
      str(tdsGeyser.getAttribute("x1").getStd()))
```

####  13.3.9.3 Console

This macro should result in this output in console:

```python
min(x1)= 1.6;
               max(x1)= 5.1;
                              mean(x1)= 3.487783088235295;
                                                            std(x1)= 1.141371251105209
```

###  13.3.10 Macro “dataserverGeyserRank.py”

####  13.3.10.1 Objective

This part shows the complete code used to produce the console display in Computing the ranking.

#### 13.3.10.2 Macro Uranie

```python
"""
Example of rank usage for illustration purpose
"""
from URANIE import DataServer
tdsGeyser = DataServer.TDataServer("geyser", "poet")
tdsGeyser.fileDataRead("geyser.dat")
tdsGeyser.computeRank("x1")
tdsGeyser.computeStatistic("Rk_x1")
print("NPatterns="+str(tdsGeyser.getNPatterns())+";
                                                     min(Rk_x1)= " +
      str(tdsGeyser.getAttribute("Rk_x1").getMinimum())+";
                                                            max(Rk_x1)= " +
      str(tdsGeyser.getAttribute("Rk_x1").getMaximum()))
```

####  13.3.10.3 Console

This macro should result in this output in console:

```python
NPatterns=272;
                min(Rk_x1)= 1.0;
                                  max(Rk_x1)= 272.0
```

<!-- page 224 (PDF 231) -->
### 13.3.11 Macro “dataserverNormaliseVector.py”

#### 13.3.11.1 Objective

This part shows the complete code used to produce the console display in Normalising the variable.

#### 13.3.11.2 Macro Uranie

```python
"""
Example of vector normalisation
"""
from URANIE import DataServer
tdsop = DataServer.TDataServer("foo", "pouet")
tdsop.fileDataRead("tdstest.dat")
# Compute a global normalisation of v, CenterReduced
tdsop.normalize("v", "GCR", DataServer.TDataServer.kCR, True)
# Compute a normalisation of v, CenterReduced (not global but entry by entry)
tdsop.normalize("v", "CR", DataServer.TDataServer.kCR, False)
# Compute a global normalisation of v, Centered
tdsop.normalize("v", "GCent", DataServer.TDataServer.kCentered)
# Compute a normalisation of v, Centered
                                          (not global but entry by entry)
tdsop.normalize("v", "Cent", DataServer.TDataServer.kCentered, False)
# Compute a global normalisation of v, ZeroOne
tdsop.normalize("v", "GZO", DataServer.TDataServer.kZeroOne)
# Compute a normalisation of v, ZeroOne (not global but entry by entry)
tdsop.normalize("v", "ZO", DataServer.TDataServer.kZeroOne, False)
# Compute a global normalisation of v, MinusOneOne
tdsop.normalize("v", "GMOO", DataServer.TDataServer.kMinusOneOne, True)
# Compute a normalisation of v, MinusOneOne (not global but entry by entry)
tdsop.normalize("v", "MOO", DataServer.TDataServer.kMinusOneOne, False)
tdsop.scan("v:vGCR:vCR:vGCent:vCent:vGZO:vZO:vGMOO:vMOO", "",
           "colsize=4 col=2:5::::::::")
```

####  13.3.11.3 Console

This macro should result in this output in console:

```python
*************************************************************************************
*
     Row
           * Instance *
                         v *
                              vGCR *
                                      vCR * vGCe * vCen * vGZO *
                                                                  vZO * vGMO * vMOO *
*************************************************************************************
*
         0 *
                    0 *
                         1 * -1.46 *
                                       -1 *
                                              -4 *
                                                     -3 *
                                                             0 *
                                                                    0 *
                                                                          -1 *
                                                                                 -1 *
*
         0 *
                    1 *
                         2 * -1.09 *
                                       -1 *
                                              -3 *
                                                     -3 * 0.12 *
                                                                    0 * -0.7 *
                                                                                 -1 *
*
         0 *
                    2 *
                         3 * -0.73 *
                                       -1 *
                                              -2 *
                                                     -3 * 0.25 *
                                                                    0 * -0.5 *
                                                                                 -1 *
*
         1 *
                    0 *
                         4 * -0.36 *
                                        0 *
                                              -1 *
                                                      0 * 0.37 *
                                                                  0.5 * -0.2 *
                                                                                  0 *
*
         1 *
                    1 *
                         5 *
                                 0 *
                                        0 *
                                               0 *
                                                      0 *
                                                           0.5 *
                                                                  0.5 *
                                                                           0 *
                                                                                  0 *
*
         1 *
                    2 *
                         6 * 0.365 *
                                        0 *
                                               1 *
                                                      0 * 0.62 *
                                                                  0.5 * 0.25 *
                                                                                  0 *
*
         2 *
                    0 *
                         7 * 0.730 *
                                        1 *
                                               2 *
                                                      3 * 0.75 *
                                                                    1 *
                                                                         0.5 *
                                                                                  1 *
*
         2 *
                    1 *
                         8 * 1.095 *
                                        1 *
                                               3 *
                                                      3 * 0.87 *
                                                                    1 * 0.75 *
                                                                                  1 *
```

<!-- page 225 (PDF 232) -->
```python
*
         2 *
                    2 *
                         9 * 1.460 *
                                        1 *
                                               4 *
                                                      3 *
                                                             1 *
                                                                    1 *
                                                                           1 *
                                                                                  1 *
*************************************************************************************
```

###  13.3.12 Macro “dataserverComputeStatVector.py”

####  13.3.12.1 Objective

This part shows the complete code used to produce the console display in Specific case of vectors.

#### 13.3.12.2 Macro Uranie

```python
"""
Example of statistical estimation on vector attributes
"""
from URANIE import DataServer
tdsop = DataServer.TDataServer("foo", "poet")
tdsop.fileDataRead("tdstest.dat")
# Considering every element of a vector independent from the others
tdsop.computeStatistic("x")
px = tdsop.getAttribute("x")
print("min(x[0])= "+str(px.getMinimum(0))+";
                                              max(x[0])= "+str(px.getMaximum(0))
      + ";
            mean(x[0])= "+str(px.getMean(0))+";
                                                 std(x[0])= "+str(px.getStd(0)))
print("min(x[1])= "+str(px.getMinimum(1))+";
                                              max(x[1])= "+str(px.getMaximum(1))
      + ";
            mean(x[1])= "+str(px.getMean(1))+";
                                                 std(x[1])= "+str(px.getStd(1)))
print("min(x[2])= "+str(px.getMinimum(2))+";
                                              max(x[2])= "+str(px.getMaximum(2))
      + ";
            mean(x[2])= "+str(px.getMean(2))+";
                                                 std(x[2])= "+str(px.getStd(2)))
print("min(xtot)= "+str(px.getMinimum(3))+";
                                              max(xtot)= "+str(px.getMaximum(3))
      + ";
            mean(xtot)= "+str(px.getMean(3))+";
                                                 std(xtot)= "+str(px.getStd(3)))
# Statistic for a single realisation of a vector, not considering other events
tdsop.addAttribute("Min_x", "Min$(x)")
tdsop.addAttribute("Max_x", "Max$(x)")
tdsop.addAttribute("Mean_x", "Sum$(x)/Length$(x)")
tdsop.scan("x:Min_x:Max_x:Mean_x", "", "colsize=5 col=2:::6")
```

####  13.3.12.3 Console

This macro should result in this output in console, split in two parts, the first one being from Uranie’s method

```python
min(x[0])= 1.0;
                 max(x[0])= 7.0;
                                  mean(x[0])= 3.0;
                                                    std(x[0])= 3.4641016151377544
min(x[1])= 2.0;
                 max(x[1])= 8.0;
                                  mean(x[1])= 4.666666666666666;
                                                                  std(x[1])= 3.
```

˓→055050463303893

```python
min(x[2])= 3.0;
                 max(x[2])= 9.0;
                                  mean(x[2])= 6.666666666666666;
                                                                  std(x[2])= 3.
```

˓→2145502536643185

```python
min(xtot)= 1.0;
                 max(xtot)= 9.0;
                                  mean(xtot)= 4.777777777777778;
                                                                  std(xtot)= 3.
```

˓→2317865716108862
The second on the other hand results from ROOT’s methods (the second part of the code shown above):

<!-- page 226 (PDF 233) -->
```python
*****************************************************
*
     Row
           * Instance *
                         x * Min_x * Max_x * Mean_x *
*****************************************************
*
         0 *
                    0 *
                         1 *
                                 1 *
                                         3 *
                                                  2 *
*
         0 *
                    1 *
                         2 *
                                 1 *
                                         3 *
                                                  2 *
*
         0 *
                    2 *
                         3 *
                                 1 *
                                         3 *
                                                  2 *
*
         1 *
                    0 *
                         7 *
                                 7 *
                                         9 *
                                                  8 *
*
         1 *
                    1 *
                         8 *
                                 7 *
                                         9 *
                                                  8 *
*
         1 *
                    2 *
                         9 *
                                 7 *
                                         9 *
                                                  8 *
*
         2 *
                    0 *
                         1 *
                                 1 *
                                         8 * 4.3333 *
*
         2 *
                    1 *
                         4 *
                                 1 *
                                         8 * 4.3333 *
*
         2 *
                    2 *
                         8 *
                                 1 *
                                         8 * 4.3333 *
*****************************************************
```

###  13.3.13 Macro “dataserverComputeCorrelationMatrixVector.py”

####  13.3.13.1 Objective

This part shows the complete code used to produce the console display in Special case of vector.

#### 13.3.13.2 Macro Uranie

```python
"""
Example of correlation matrix computation for vector
"""
from URANIE import DataServer
tdsop = DataServer.TDataServer("foo", "poet")
tdsop.fileDataRead("tdstest.dat")
# Consider a and x attributes (every element of the vector)
globalOne = tdsop.computeCorrelationMatrix("x:a")
globalOne.Print()
# Consider a and x attributes (cherry-picking a single element of the vector)
focusedOne = tdsop.computeCorrelationMatrix("x[1]:a")
focusedOne.Print()
```

####  13.3.13.3 Console

This macro should result in this output in console.

```python
4x4 matrix is as follows
     |
                 |
                             |
                                         |
                                                     |
---------------------------------------------------------
   0 |
                       0.9449
                                   0.6286
                                                0.189
   1 |
           0.9449
                                   0.8486
                                                  0.5
   2 |
           0.6286
                       0.8486
                                               0.8825
   3 |
            0.189
                          0.5
                                   0.8825
```

<!-- page 227 (PDF 234) -->
```python
2x2 matrix is as follows
     |
                 |
                             |
-------------------------------
   0 |
                          0.5
   1 |
              0.5
```

###  13.3.14 Macro “dataserverComputeQuantileVec.py”

####  13.3.14.1 Objective

This part shows the complete code used to produce the console display in computeQuantile.

#### 13.3.14.2 Macro Uranie

```python
"""
Example of quantile estimation for many values at once
"""
from sys import stdout
from ctypes import c_int, c_double
import numpy as np
from URANIE import DataServer
import ROOT
tdsvec = DataServer.TDataServer("foo", "bar")
tdsvec.fileDataRead("aTDSWithVectors.dat")
probas = np.array([0.2, 0.6, 0.8], 'd')
quants = np.array(len(probas)*[0.0], 'd')
tdsvec.computeQuantile("rank", len(probas), probas, quants)
prank = tdsvec.getAttribute("rank")
nbquant = c_int(0)
prank.getQuantilesSize(nbquant)
                                 # (1)
print("nbquant = " + str(nbquant.value))
aproba = c_double(0.8)
aquant = c_double(0)
prank.getQuantile(aproba, aquant)
                                   # (2)
print("aproba = " + str(aproba.value) + ", aquant = " + str(aquant.value))
theproba = np.array(nbquant.value*[0.0], 'd')
thequant = np.array(nbquant.value*[0.0], 'd')
prank.getQuantiles(theproba, thequant)
                                        # (3)
for i_q in range(nbquant.value):
    print("(theproba, thequant)[" + str(i_q) + "] = (" + str(theproba[i_q]) +
          ", " + str(thequant[i_q]) + ")")
allquant = ROOT.vector('double')()
prank.getQuantileVector(aproba, allquant)
                                           # (4)
stdout.write("aproba = " + str(aproba.value) + ", allquant = ")
```

<!-- page 228 (PDF 235) -->
```python
for quant_i in allquant:
    stdout.write(str(quant_i) + " ")
print("")
```

####  13.3.14.3 Console

This macro should result in this output in console:

```python
nbquant = 3
aproba = 0.8, aquant = 6.4
(theproba, thequant)[0] = (0.2, 1.6)
(theproba, thequant)[1] = (0.6, 4.8)
(theproba, thequant)[2] = (0.8, 6.4)
aproba = 0.8, allquant = 6.4 7.4
```

###  13.3.15 Macro “dataserverDrawQQPlot.py”

####  13.3.15.1 Objective

This macro is an example of how to produce QQ-plot for a certain number of randomly-drawn samples, providing the
correct parameter values along with modified versions to illustrate the impact.

#### 13.3.15.2 Macro Uranie

```python
"""
Example of QQ plot
"""
from URANIE import DataServer, Sampler
import ROOT
# Create a TDS with 8 kind of distributions
p1 = 1.3
p2 = 4.5
p3 = 0.9
p4 = 4.4
          # Fixed values for parameters
tds0 = DataServer.TDataServer()
tds0.addAttribute(DataServer.TNormalDistribution("norm", p1, p2))
tds0.addAttribute(DataServer.TLogNormalDistribution("logn", p1, p2))
tds0.addAttribute(DataServer.TUniformDistribution("unif", p1, p2))
tds0.addAttribute(DataServer.TExponentialDistribution("expo", p1, p2))
tds0.addAttribute(DataServer.TGammaDistribution("gamm", p1, p2, p3))
tds0.addAttribute(DataServer.TBetaDistribution("beta", p1, p2, p3, p4))
tds0.addAttribute(DataServer.TWeibullDistribution("weib", p1, p2, p3))
tds0.addAttribute(DataServer.TGumbelMaxDistribution("gumb", p1, p2))
# Create the sample
fsamp = Sampler.TBasicSampling(tds0, "lhs", 200)
fsamp.generateSample()
# Define number of laws, their name and numbers of parameters
nLaws = 8
```

<!-- page 229 (PDF 236) -->
```python
# number of parameters to put in () for the corresponding law
laws = ["normal", "lognormal", "uniform", "gamma", "weibull",
        "beta", "exponential", "gumbelmax"]
npar = [2, 2, 2, 3, 3, 4, 2, 2]
# Create the canvas
c = ROOT.TCanvas("c1", "", 800, 1000)
# Create the 8 pads
apad = ROOT.TPad("apad", "apad", 0, 0.03, 1, 1)
apad.Draw()
apad.cd()
apad.Divide(2, 4)
# Number of points to compare theoretical and empirical values
nS = 1000
mod = 0.8
           # Factor used to artificially change the parameter values
Par = lambda i, n, p, mod: "," + str(p*mod) if n >= i else ""
opt = ""
          # option of the drawQQPlot method
for i in range(nLaws):
    # Clean sstr
    test = ""
    # Add nominal configuration
    test += laws[i] + "(" + str(p1) + "," + str(p2) + Par(3, npar[i], p3, 1) \
        + str(p2) + Par(4, npar[i], p4, 1) + ")"
    # Changing par1
    test += ":" + laws[i] + "(" + str(p1*mod) + "," + str(p2) \
        + Par(3, npar[i], p3, 1) + str(p2) + Par(4, npar[i], p4, 1) + ")"
    # Changing par2
    test += ":" + laws[i] + "(" + str(p1) + "," + str(p2*mod) \
        + Par(3, npar[i], p3, 1) + str(p2) + Par(4, npar[i], p4, 1) + ")"
    # Changing par3
    if npar[i] >= 3:
        test += ":" + laws[i] + "(" + str(p1) + "," + str(p2) \
            + Par(3, npar[i], p3, mod) + str(p2) + Par(4, npar[i], p4, 1) + ")"
    # Changing par4
    if npar[i] >= 4:
        test += ":" + laws[i] + "(" + str(p1) + "," + str(p2) \
            + Par(3, npar[i], p3, 1) + str(p2) + Par(4, npar[i], p4, mod) + ")"
    apad.cd(i+1)
    # Produce the plot
    tds0.drawQQPlot(laws[i][:4], test, nS, opt)
```

The very first step of this macro is to create a sample that will contain a design-of-experiments filled with 200 locations,
using various statistical laws. All the tested laws, are those available in the drawQQPlot method and they might depend
on 2 to 4 parameters, defined a but randomly at the beginning of this piece of code.

```python
# Create a TDS with 8 kind of distributions
p1 = 1.3
p2 = 4.5
```

<!-- page 230 (PDF 237) -->
```python
p3 = 0.9
p4 = 4.4
          # Fixed values for parameters
tds0 = DataServer.TDataServer()
tds0.addAttribute(DataServer.TNormalDistribution("norm", p1, p2))
tds0.addAttribute(DataServer.TLogNormalDistribution("logn", p1, p2))
tds0.addAttribute(DataServer.TUniformDistribution("unif", p1, p2))
tds0.addAttribute(DataServer.TExponentialDistribution("expo", p1, p2))
tds0.addAttribute(DataServer.TGammaDistribution("gamm", p1, p2, p3))
tds0.addAttribute(DataServer.TBetaDistribution("beta", p1, p2, p3, p4))
tds0.addAttribute(DataServer.TWeibullDistribution("weib", p1, p2, p3))
tds0.addAttribute(DataServer.TGumbelMaxDistribution("gumb", p1, p2))
```

Once done, the sample is generated using TBasicSampling object with an LHS algorithm. On top of this, despite the
plot preparation with canvas and pad generation, several variables are set to prepare the tests, as shown below

```python
# Define number of laws, their name and numbers of parameters
nLaws = 8
# number of parameters to put in () for the corresponding law
laws = ["normal", "lognormal", "uniform", "gamma", "weibull",
        "beta", "exponential", "gumbelmax"]
npar = [2, 2, 2, 3, 3, 4, 2, 2]
# Number of points to compare theoretical and empirical values
nS = 1000
mod = 0.8
           # Factor used to artificially change the parameter values
```

Finally, after the line of hypothesis to be tested is constructed (the first paragraph in the for loop) the drawQQPlot
method is called for every empirical law in the following line.

```python
tds0.drawQQPlot(laws[i][:4], test, nS, opt)
```

For the first case, when one wants to test the TNormalDistribution “norm” with the known parameters and a variation
of each, it resumes as if this line was run:

```python
tds0.drawQQPlot( "norm", "normal(1.3,4.5):normal(1.04,4.5):normal(1.3,3.6)", nS)
```

The first field is the attribute to be tested, while the second one provides the three hypothesis with which our attribute
under investigation will be compared. The third argument is the number of steps to be computed for quantiles.
The result of this macro is shown below.

<!-- page 231 (PDF 238) -->
#### 13.3.15.3 Graph

Figure 13.7: Graph of the macro "dataserverDrawQQPlot.py"

### 13.3.16 Macro “dataserverDrawPPPlot.py”

#### 13.3.16.1 Objective

This macro is an example of how to produce PP-plot for a certain number of randomly-drawn samples, providing the
correct parameter values along with modified versions to illustrate the impact.

#### 13.3.16.2 Macro Uranie

```python
"""
Example of PP plot
"""
```

<!-- page 232 (PDF 239) -->
```python
from URANIE import DataServer, Sampler
import ROOT
# Create a TDS with 8 kind of distributions
p1 = 1.3
p2 = 4.5
p3 = 0.9
p4 = 4.4
          # Fixed values for parameters
tds0 = DataServer.TDataServer()
tds0.addAttribute(DataServer.TNormalDistribution("norm", p1, p2))
tds0.addAttribute(DataServer.TLogNormalDistribution("logn", p1, p2))
tds0.addAttribute(DataServer.TUniformDistribution("unif", p1, p2))
tds0.addAttribute(DataServer.TExponentialDistribution("expo", p1, p2))
tds0.addAttribute(DataServer.TGammaDistribution("gamm", p1, p2, p3))
tds0.addAttribute(DataServer.TBetaDistribution("beta", p1, p2, p3, p4))
tds0.addAttribute(DataServer.TWeibullDistribution("weib", p1, p2, p3))
tds0.addAttribute(DataServer.TGumbelMaxDistribution("gumb", p1, p2))
# Create the sample
fsamp = Sampler.TBasicSampling(tds0, "lhs", 200)
fsamp.generateSample()
# Define number of laws, their name and numbers of parameters
nLaws = 8
# number of parameters to put in () for the corresponding law
laws = ["normal", "lognormal", "uniform", "gamma",
        "weibull", "beta", "exponential", "gumbelmax"]
npar = [2, 2, 2, 3, 3, 4, 2, 2]
# Create the canvas
c = ROOT.TCanvas("c1", "", 800, 1000)
# Create the 8 pads
apad = ROOT.TPad("apad", "apad", 0, 0.03, 1, 1)
apad.Draw()
apad.cd()
apad.Divide(2, 4)
# Number of points to compare theoretical and empirical values
nS = 1000
mod = 0.8
           # Factor used to artificially change the parameter values
Par = lambda i, n, p, mod: ","+str(p*mod) if n >= i else ""
opt = ""
          # option of the drawPPPlot method
for i in range(nLaws):
    # Clean sstr
    test = ""
    # Add nominal configuration
    test += laws[i] + "(" + str(p1) + "," + str(p2) + Par(3, npar[i], p3, 1) \
        + str(p2) + Par(4, npar[i], p4, 1) + ")"
    # Changing par1
```

<!-- page 233 (PDF 240) -->
```python
test += ":" + laws[i] + "(" + str(p1*mod) + "," + str(p2) \
    + Par(3, npar[i], p3, 1) + str(p2) + Par(4, npar[i], p4, 1) + ")"
# Changing par2
test += ":" + laws[i] + "(" + str(p1) + "," + str(p2*mod) \
    + Par(3, npar[i], p3, 1) + str(p2) + Par(4, npar[i], p4, 1) + ")"
# Changing par3
if npar[i] >= 3:
    test += ":" + laws[i] + "(" + str(p1) + "," + str(p2) \
        + Par(3, npar[i], p3, mod) + str(p2) + Par(4, npar[i], p4, 1) + ")"
# Changing par4
if npar[i] >= 4:
    test += ":" + laws[i] + "(" + str(p1) + "," + str(p2) \
        + Par(3, npar[i], p3, 1) + str(p2) + Par(4, npar[i], p4, mod) + ")"
apad.cd(i+1)
# Produce the plot
tds0.drawPPPlot(laws[i][:4], test, nS, opt)
```

The macro is based on the one discussed in Macro “dataserverDrawQQPlot.py”. The only difference is this line

```python
tds0.drawPPPlot(laws[i][:4], test, nS, opt)
```

The call of the drawing method above can be resume, for the first case, like this:

```python
tds0.drawPPPlot( "norm", "normal(1.3,4.5):normal(1.04,4.5):normal(1.3,3.6)", nS)
```

The first field is the attribute to be tested, while the second one provides the three hypothesis with which our attribute
under investigation will be compared. The third argument is the number of steps to be computed for probabilities.
The result of this macro is shown below.

<!-- page 234 (PDF 241) -->
#### 13.3.16.3 Graph

Figure 13.8: Graph of the macro "dataserverDrawPPPlot.py"

### 13.3.17 Macro “dataserverPCAExample.py”

#### 13.3.17.1 Objective

The goal of this macro is to show how to handle a PCA analysis. It is not much discussed here, as a large description of
both methods and concepts is done in Combining these aspects: performing PCA.

#### 13.3.17.2 Macro Uranie

```python
"""
Example of PCA usage (standalone case)
"""
```

<!-- page 235 (PDF 242) -->
```python
from URANIE import DataServer
import ROOT
# Read the database
tdsPCA = DataServer.TDataServer("tdsPCA", "my TDS")
tdsPCA.fileDataRead("Notes.dat")
# Create the PCA object precising the variables of interest
tpca = DataServer.TPCA(tdsPCA, "Maths:Physics:French:Latin:Music")
tpca.compute()
graphical = True
                  # do graphs
dumponscreen = True
                     # or dumping results
showcoordinate = False
                        # show the points coordinate while dumping results
if graphical:
    # Draw all point in PCA planes
    cPCA = ROOT.TCanvas("cpca", "PCA", 800, 800)
    apad1 = ROOT.TPad("apad1", "apad1", 0, 0.03, 1, 1)
    apad1.Draw()
    apad1.cd()
    apad1.Divide(2, 2)
    apad1.cd(1)
    tpca.drawPCA(1, 2, "Pupil")
    apad1.cd(3)
    tpca.drawPCA(1, 3, "Pupil")
    apad1.cd(4)
    tpca.drawPCA(2, 3, "Pupil")
    # Draw all variable weight in PC definition
    cLoading = ROOT.TCanvas("cLoading", "Loading Plot", 800, 800)
    apad2 = ROOT.TPad("apad2", "apad2", 0, 0.03, 1, 1)
    apad2.Draw()
    apad2.cd()
    apad2.Divide(2, 2)
    apad2.cd(1)
    tpca.drawLoading(1, 2)
    apad2.cd(3)
    tpca.drawLoading(1, 3)
    apad2.cd(4)
    tpca.drawLoading(2, 3)
    # Draw the eigen values in different normalisation
    c = ROOT.TCanvas("cEigenValues", "Eigen Values Plot", 1100, 500)
    apad3 = ROOT.TPad("apad3", "apad3", 0, 0.03, 1, 1)
    apad3.Draw()
    apad3.cd()
    apad3.Divide(3, 1)
    ntd = tpca.getResultNtupleD()
    apad3.cd(1)
    ntd.Draw("eigen:i", "", "lp")
```

<!-- page 236 (PDF 243) -->
```python
    apad3.cd(2)
    ntd.Draw("eigen_pct:i", "", "lp")
    ROOT.gPad.SetGrid()
    apad3.cd(3)
    ntd.Draw("sum_eigen_pct:i", "", "lp")
    ROOT.gPad.SetGrid()
if dumponscreen:
    nPCused = 5
                 # 3 to see only the meaningful ones
    PCname = ""
    Cosname = ""
    Contrname = ""
    Variable = "Pupil"
    for iatt in range(1, nPCused+1):
        ##list of PC: PC_1:PC_2:PC_3:PC_4:PC_5
        PCname += "PC_"+str(iatt)+":"
        ##list of quality coeff: cosca_1:cosca_2:cosca_3:cosca_4:cosca_5
        Cosname += "cosca_"+str(iatt)+":"
        ##list of contribution: contr_1:contr_2:contr_3:contr_4:contr_5
        Contrname += "contr_"+str(iatt)+":"
    PCname = PCname[:-1]
    Cosname = Cosname[:-1]
    Contrname = Contrname[:-1]
    print("\n====== EigenValues ======")
    tpca.getResultNtupleD().Scan("*")
    if showcoordinate:
        print("\n====== EigenVectors ======")
        tpca._matEigenVectors.Print()
        print("\n====== New Coordinates ======")
        tdsPCA.scan((Variable+":"+PCname))
    varRes = tpca.getVariableResultNtupleD()
    print("\n====== Looking at variables: Quality of representation ======")
    varRes.Scan(("Variable:"+Cosname))
    print("\n====== Looking at variables: Contribution to axis ======")
    varRes.Scan(("Variable:"+Contrname))
    print("\n====== Looking at events:
                                        Quality of representation ======")
    tdsPCA.scan((Variable+":"+Cosname))
    print("\n====== Looking at events: Contribution to axis ========")
    tdsPCA.scan((Variable+":"+Contrname))
```

This first part of this macro is described in Combining these aspects: performing PCA. We will focus here on the second
part, where all the numerical results are dumped on screen. These results are stored in the dataserver for the points and in
a dedicated ntuple for the variable that can be retrieved by calling the method getVariableResultNtupleD. In both
cases, the results can be split into two kinds:

<!-- page 237 (PDF 244) -->
• the quality of the representation: it is called “cosca_X” as it is a squared cosinus of the projection of the source
under study (point or subject) on the X-th PC.
• the contribution to axis: it is called “contr_X” as it is the contribution of the source under study (point or subject)
to the definition of the X-th PC.
We start by defining the list of variables that one might want to display

```python
nPCused = 5
             # 3 to see only the meaningful ones
PCname = ""
Cosname = ""
Contrname = ""
Variable = "Pupil"
for iatt in range(1, nPCused+1):
    ##list of PC: PC_1:PC_2:PC_3:PC_4:PC_5
    PCname += "PC_"+str(iatt)+":"
    ##list of quality coeff: cosca_1:cosca_2:cosca_3:cosca_4:cosca_5
    Cosname += "cosca_"+str(iatt)+":"
    ##list of contribution: contr_1:contr_2:contr_3:contr_4:contr_5
    Contrname += "contr_"+str(iatt)+":"
PCname = PCname[:-1]
Cosname = Cosname[:-1]
Contrname = Contrname[:-1]
```

From there, once the variable ntuple is retrieved, one can dump both the quality and contribution coefficients for the
variable, here the subjects (it leads to the second and third block in the output shown in Console).

```python
varRes = tpca.getVariableResultNtupleD()
print("\n====== Looking at variables: Quality of representation ======")
varRes.Scan(("Variable:"+Cosname))
print("\n====== Looking at variables: Contribution to axis ======")
varRes.Scan(("Variable:"+Contrname))
```

Finally, one can do the same for the data points, with the same Scan method (which lead to the fourth and fifth block in
the output shown in Console).

```python
print("\n====== Looking at events:
                                    Quality of representation ======")
tdsPCA.scan((Variable+":"+Cosname))
print("\n====== Looking at events: Contribution to axis ========")
tdsPCA.scan((Variable+":"+Contrname))
```

####  13.3.17.3 Console

```python
====== EigenValues ======
************************************************************
*
     Row
           *
                   i.i * eigen.eig * eigen_pct * sum_eigen *
************************************************************
*
         0 *
                     1 * 2.8618175 * 57.236350 * 57.236350 *
*
         1 *
                     2 * 1.1506811 * 23.013622 * 80.249973 *
*
         2 *
                     3 * 0.9831407 * 19.662814 * 99.912787 *
*
         3 *
                     4 * 0.0039371 * 0.0787424 * 99.991530 *
```

<!-- page 238 (PDF 245) -->
```python
*
         4 *
                     5 * 0.0004234 * 0.0084696 *
                                                       100 *
************************************************************
====== Looking at variables: Quality of representation ======
************************************************************************************
*
     Row
           *
              Variable *
                           cosca_1 *
                                       cosca_2 *
                                                   cosca_3 *
                                                               cosca_4 *
                                                                           cosca_5 *
************************************************************************************
*
         0 *
                 Maths *
                          0.649485 *
                                       0.32645 * 0.0235449 * 0.0003614 * 0.0001582 *
*
         1 *
               Physics *
                          0.804627 *
                                      0.185581 * 0.0086212 * 0.0010515 * 0.0001193 *
*
         2 *
                French *
                          0.574697 *
                                      0.373378 * 0.0509446 * 0.0008976 * 8.252e-05 *
*
         3 *
                 Latin *
                          0.828562 *
                                      0.157999 * 0.0117556 * 0.0016205 * 6.335e-05 *
*
         4 *
                 Music * 0.0044470 *
                                      0.107272 *
                                                  0.888274 * 5.976e-06 * 8.299e-08 *
************************************************************************************
====== Looking at variables: Contribution to axis ======
************************************************************************************
*
     Row
           *
              Variable *
                           contr_1 *
                                       contr_2 *
                                                   contr_3 *
                                                               contr_4 *
                                                                           contr_5 *
************************************************************************************
*
         0 *
                 Maths *
                          0.226948 *
                                      0.283702 * 0.0239486 * 0.0917987 *
                                                                          0.373602 *
*
         1 *
               Physics *
                          0.281159 *
                                       0.16128 * 0.0087691 *
                                                              0.267082 *
                                                                           0.28171 *
*
         2 *
                French *
                          0.200815 *
                                      0.324485 * 0.0518182 *
                                                              0.228004 *
                                                                          0.194878 *
*
         3 *
                 Latin *
                          0.289523 *
                                      0.137309 * 0.0119572 *
                                                              0.411598 *
                                                                          0.149613 *
*
         4 *
                 Music * 0.0015539 * 0.0932252 *
                                                  0.903507 * 0.0015180 * 0.0001959 *
************************************************************************************
====== Looking at events:
                           Quality of representation ======
************************************************************************************
*
     Row
           *
                 Pupil *
                           cosca_1 *
                                       cosca_2 *
                                                   cosca_3 *
                                                               cosca_4 *
                                                                           cosca_5 *
************************************************************************************
*
         0 *
                  Jean * 0.8854534 * 0.0522119 * 0.0619429 * 0.0002655 * 0.0001260 *
*
         1 *
                 Aline * 0.7920409 * 0.0542262 * 0.1530381 * 0.0006354 * 5.916e-05 *
*
         2 *
                 Annie * 0.4784294 * 0.4813342 * 0.0384099 * 0.0018007 * 2.560e-05 *
*
         3 *
               Monique * 0.8785990 * 0.0024790 * 0.1180158 * 0.0009035 * 2.557e-06 *
*
         4 *
                Didier * 0.8515216 * 0.1382946 * 0.0079754 * 0.0021718 * 3.640e-05 *
*
         5 *
                 Andre * 0.2465355 * 0.3961581 * 0.3567663 * 9.471e-05 * 0.0004451 *
*
         6 *
                Pierre * 0.0263090 * 0.7670958 * 0.2060832 * 0.0004625 * 4.925e-05 *
*
         7 *
              Brigitte * 0.1876629 * 0.5897686 * 0.2211409 * 0.0013390 * 8.836e-05 *
*
         8 *
               Evelyne * 0.0583185 * 0.3457931 * 0.5953786 * 0.0004600 * 4.957e-05 *
************************************************************************************
====== Looking at events: Contribution to axis ========
************************************************************************************
*
     Row
           *
                 Pupil *
                           contr_1 *
                                       contr_2 *
                                                   contr_3 *
                                                               contr_4 *
                                                                           contr_5 *
************************************************************************************
*
         0 *
                  Jean * 0.3012931 * 0.0441856 * 0.0613538 * 0.0656820 * 0.2897335 *
*
         1 *
                 Aline * 0.0618830 * 0.0105370 * 0.0348056 * 0.0360894 * 0.0312404 *
*
         2 *
                 Annie * 0.0401366 * 0.1004284 * 0.0093797 * 0.1098075 * 0.0145176 *
*
         3 *
               Monique * 0.3784615 * 0.0026558 * 0.1479781 * 0.2828995 * 0.0074454 *
*
         4 *
                Didier * 0.1484067 * 0.0599446 * 0.0040461 * 0.2751439 * 0.0428726 *
*
         5 *
                 Andre * 0.0348742 * 0.1393737 * 0.1469047 * 0.0097384 * 0.4255425 *
*
         6 *
                Pierre * 0.0041001 * 0.2973223 * 0.0934888 * 0.0524003 * 0.0518702 *
*
         7 *
              Brigitte * 0.0157710 * 0.1232678 * 0.0540974 * 0.0817989 * 0.0501849 *
```
