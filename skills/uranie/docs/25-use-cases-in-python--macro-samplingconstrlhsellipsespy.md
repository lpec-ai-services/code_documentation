# Use-cases in Python — Macros Sampler — Macro “samplingConstrLHSEllipses.py” … Macro “samplingSingularCorrelationCase.py”
<!-- source PDF pages 265-270 -->

<!-- page 258 (PDF 265) -->
#### 13.4.12.3 Graph

Figure 13.15: Graph of the macro “samplingConstrLHSLinear.py”

### 13.4.13 Macro “samplingConstrLHSEllipses.py”

#### 13.4.13.1 Objective

This macro shows the usage of the TConstrLHS class when one wants to create a constrained LHS with non-linear
constraints. In order to illustate the concept, it is applied on three input variables drawn from uniform distribution with
well-thought boundaries (as the concept of the LHS is to have nicely distributed marginals). The constraints are excluding
the inner part of an ellipse for one of the input plane and the outter part of another ellipse for another input plane.

#### 13.4.13.2 Macro Uranie

```python
"""
Example of Constrained lhs with ellipses
"""
import numpy as np
from URANIE import DataServer, Sampler
import ROOT
def nicegrid(l_tds, l_can):
    """Generate the grid plot."""
```

<!-- page 259 (PDF 266) -->
```python
    l_ns = l_tds.getNPatterns()
    l_nx = l_tds.getNAttributes()
    l_tds.drawPairs()
    all_h = []
    ROOT.gStyle.SetOptStat(0)
    for iatt in range(l_nx):
        l_can.GetPad(iatt*(l_nx+1)+1).cd()
        att = l_tds.getAttribute(iatt)
        a_name = att.GetName()
        all_h.append(ROOT.TH1F(a_name+"_histo", a_name+";x_"+str(iatt),
                               l_ns, att.getLowerBound(), att.getUpperBound()))
        l_tds.Draw(a_name+">>"+a_name+"_histo", "", "goff")
        all_h[iatt].Draw()
    return all_h
# Canvas to produce the pair plot
Can = ROOT.TCanvas("Can", "Can", 10, 32, 1400, 1000)
apad = ROOT.TPad("apad", "apad", 0, 0.03, 1, 1)
apad.Draw()
apad.cd()
ns = 250
          # Size of the samples to be produced
nx = 3
# Create dataserver and define the attributes
tds = DataServer.TDataServer("tds", "pouet")
for i in range(nx):
    tds.addAttribute(DataServer.TUniformDistribution("x_"+str(i), 0, i+1))
    tds.getAttribute("x_"+str(i)).delShare()
ROOT.gROOT.LoadMacro("ConstrFunctions.C")
# Generate the constr lhs
constrlhs = Sampler.TConstrLHS(tds, ns)
inputs = np.array([1, 0, 1, 2], dtype='i')
constrlhs.addConstraint(ROOT.CircularRules, 2, len(inputs), inputs)
constrlhs.generateSample()
# Do the plot
ListOfDiag = nicegrid(tds, apad)
```

The very beginning of these macros is the nicegrid method which is here only to show the nice marginal distributions
and the scatter plots. One can clearly skip this part to focus on the rest in the main function.
The macro very much looks like any other design-of-experiments generating macro above: the dataserver is created
along with the canvas object and the problem is defined along with the input variables and the number of locations to be
produced. Once done, then the TConstrLHS instance is created with the four following lines:

<!-- page 260 (PDF 267) -->
```python
# Generate the constr lhs
constrlhs = Sampler.TConstrLHS(tds, ns)
inputs = np.array([1, 0, 1, 2], dtype='i')
constrlhs.addConstraint(ROOT.CircularRules, 2, len(inputs), inputs)
constrlhs.generateSample()
```

The constructor is pretty obvious, as it takes only the dataserver object and the number of locations. Once created the
main method to be called is the addConstraint function which has been largely discussed in TConstrLHS example. The
first argument of this method is the pointer to the C++ function which has been included in our macro through the line
used right before the sampler creation:

```python
ROOT.gROOT.LoadMacro("ConstrFunctions.C")
```

which contains the CircularRules function. The rest of the argument are the number of constraints, the size of the list
of parameters and its content. Finally the nicegrid method is called to produce the nice plot shown in Figure 13.16

#### 13.4.13.3 Graph

Figure 13.16: Graph of the macro “samplingConstrLHSEllipses.py”

<!-- page 261 (PDF 268) -->
### 13.4.14 Macro “samplingSingularCorrelationCase.py”

#### 13.4.14.1 Objective

This macro shows the usage of the SVD decomposition for the specific case where the target correlation matrix is singular.
The idea is to provide a tool that will allow the user to compare quickly both the TSampling and TBasicSampling
implementation, with a singular correlation matrix, or not. In order to do that, a toy random correlation matrix generator
is provided.
The resulting design-of-experiments is presented side-by-side with the residual of the obtained correlation matrix.

#### 13.4.14.2 Macro Uranie

```python
"""
Example of DoE generation when the correlation matrix is singular
"""
from math import sqrt
from URANIE import DataServer, Sampler
import ROOT
# What classes to be used (true==TSampling, false==TBasicSampling)
ImanConover = False
SamplingType = "srs"
# Remove svd to use Cholesky
SamplerOption = "svd"
# Generating randomly a singular correlation matrix
# dimension of the
                    problem in total.
n = 10
# Number of dimension self explained.
# SHOULD BE SMALLER (singular) OR EQUAL TO (full-rank) n.
p = 6
# number of location in the doe
m = 300
# =======================================================================
            Internal recipe to get this correlation matrix
# =======================================================================
A = ROOT.TMatrixD(n, p)
Rand = ROOT.TRandom3()
for i in range(n):
    for j in range(p):
        A[i][j] = Rand.Gaus(0., 1.)
Gamma = ROOT.TMatrixD(n, n)
Gamma.MultT(A, A)
Gamma *= 1./n
Sig = ROOT.TMatrixD(n, n)
for i in range(n):
    Sig[i][i] = 1./sqrt(Gamma[i][i])
Corr = ROOT.TMatrixD(Sig, ROOT.TMatrix.kMult, Gamma)
Corr *= Sig
```

<!-- page 262 (PDF 269) -->
```python
# =======================================================================
                     Corr is our correlation matrix.
# =======================================================================
# Creating the TDS
tds = DataServer.TDataServer("pouet", "pouet")
# Adding attributes
for i in range(n):
    tds.addAttribute(DataServer.TNormalDistribution("n"+str(i), 0., 1.))
# Create the sampler and generate the doe
if ImanConover:
    sam = Sampler.TSampling(tds, SamplingType, m)
    sam.setCorrelationMatrix(Corr)
    sam.generateSample(SamplerOption)
else:
    sam = Sampler.TBasicSampling(tds, SamplingType, m)
    sam.setCorrelationMatrix(Corr)
    sam.generateCorrSample(SamplerOption)
# Compute the empirical correlation matrix
ResultCorr = tds.computeCorrelationMatrix()
# Change it into a residual matrix
ResultCorr -= Corr
ROOT.gStyle.SetOptStat(1110)
# Plot the results
c = ROOT.TCanvas("c", "c", 1800, 900)
apad = ROOT.TPad("apad", "apad", 0, 0.03, 1, 1)
apad.Draw()
apad.cd()
apad.Divide(2, 1)
apad.cd(1)
# Residual distribution
h = ROOT.TH1F("h", ";#Delta_{#rho}", 100, -0.2, 0.2)
for i in range(n):
    for j in range(i, n):
        h.Fill(ResultCorr[i][j])
h.Draw()
# all variables
apad.cd(2)
tds.drawPairs()
```

This macro starts by a bunch of variables provided to offer many possible configuration, among which:
• use Iman and Conover method or the more simple one to get the correlation (see [Bla17] for a complete description
of their respective correlation handling);
• produce a stratified or fully random sample;
• use Cholesky or SVD decomposition to decompose the target correlation matrix;

<!-- page 263 (PDF 270) -->
• use a full-rank or singular correlation matrix. This is allowed thanks to the toy random correlation matrix generator:
one has to define the number of variable (n) and the number of dimension that should be self-explained (p). If the
latter is strickly lower than the former, then the correlation matrix generated will be singular, whereas it will be a
full-rank one if both quantities are equal.
This is the main part of this macro

```python
# What classes to be used (true==TSampling, false==TBasicSampling)
ImanConover = False
SamplingType = "srs"
# Remove svd to use Cholesky
SamplerOption = "svd"
# Generating randomly a singular correlation matrix
# dimension of the
                    problem in total.
n = 10
# Number of dimension self explained.
# SHOULD BE SMALLER (singular) OR EQUAL TO (full-rank) n.
p = 6
# number of location in the doe
m = 300
```

Once this is settled, the correlation matrix is created and the dataserver is created and n centered-reduced normal attributes
are added. The chosen design-of-experiments is generated with the chosen options:

```python
# Create the sampler and generate the doe
if ImanConover:
    sam = Sampler.TSampling(tds, SamplingType, m)
    sam.setCorrelationMatrix(Corr)
    sam.generateSample(SamplerOption)
else:
    sam = Sampler.TBasicSampling(tds, SamplingType, m)
    sam.setCorrelationMatrix(Corr)
    sam.generateCorrSample(SamplerOption)
```

Finally the obtained design-of-experiments is shown along with the residual of all the correlation coefficients (difference
between the target values and the obtained ones). This is shown in Figure 13.17 and can be used to compare the performance
of the samplers.
