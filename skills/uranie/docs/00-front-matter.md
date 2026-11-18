# Front matter
<!-- source PDF pages 1-12 -->

<!-- page 1 (PDF 1) -->
The Uranie team, CEA DES, support-uranie@cea.fr
Feb 13, 2026

<!-- page i (PDF 2) -->
CONTENTS:
Overview: Uranie in a nutshell
1.1
Introducing Uranie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1.1
Uranie modules organisation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1.2
External dependencies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2
ROOT Environment
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.1
Environment variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.2
ROOT interpreter and runtime compiler
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.3
Standard compilation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.4
Uranie namespace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.5
Important modifications going from ROOT v5 to ROOT v6 . . . . . . . . . . . . . . . . . .
1.2.6
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3
The Python Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.1
Python version: greater than 3.8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.2
Environment variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.3
Using PyROOT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.4
The PyURANIE interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.5
FAQ: a Python handbook to interact with Uranie . . . . . . . . . . . . . . . . . . . . . . . .
1.3.6
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
The DataServer module
2.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2
The TAttribute class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1
Nature of the attribute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.2
List of variable information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.3
Examples of use of the class TAttribute . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.4
Adding TAttribute when data are already available
. . . . . . . . . . . . . . . . . . . . .
2.2.5
Introducing the TStochasticAttribute classes . . . . . . . . . . . . . . . . . . . . . . .
2.3
Data handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.1
Main format of input/output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.2
Import data from an ASCII file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.3
Import data from a TNtuple/TDSNtuple/TTree . . . . . . . . . . . . . . . . . . . . . . .
2.3.4
Adding attributes to a TDataServer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.5
Merging two DataServer
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.6
Pattern selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3.7
Export to an ASCII file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4
Statistical treatments and operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.1
Normalising the variable
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.2
Computing the ranking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.3
Computing the elementary statistic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4.4
The quantile computation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- page ii (PDF 3) -->
2.4.5
Correlation matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5
Visualisation dedicated to uncertainties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.1
Histogram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.2
Box-and-whisker(“boxplot”) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.3
CDF, CCDF curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.4
Graph 2D with contour levels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.5
Graph 2D “profile”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.6
Graph 2D “Tufte” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.7
Graph 2D “pairs” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.8
Graph “CobWeb” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.9
QQ plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5.10
PP plot
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6
Combining these aspects: performing PCA
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6.1
PCA usage within Uranie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
The Sampler module
3.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.2
The Stochastic methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.2.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.2.2
The main sampler classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
3.2.3
Simple example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.2.4
TConstrLHS example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.3
Description of a correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
3.3.1
Imposing the correlation coefficients
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
3.3.2
The copula classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
3.4
QMC method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.5
The random fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
3.6
OAT Design
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.6.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.6.2
OAT design in Uranie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.6.3
TOATDesign . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
3.7
The Vectorial Quantification method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
The Launcher module
4.1
Introduction.md . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
4.1.1
Overview of a simple case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
4.2
External Code
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
4.2.1
Code input and output files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
4.3
Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
4.3.1
Multi-step remote launching to clusters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
The Modeler Module
5.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
5.2
The TLinearRegression Class
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
5.3
Chaos polynomial expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
5.3.1
Nisp in a nutshell
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
5.4
The kriging method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
5.4.1
Construction of a kriging model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
5.4.2
Usage of a Kriging model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
The Sensitivity module
6.1
The Sobol method
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
6.1.1
Computation of Sobol’s sensitivity indices
. . . . . . . . . . . . . . . . . . . . . . . . . . . 126
The Optimizer module

<!-- page iii (PDF 4) -->
7.1
Function optimisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
7.1.1
Rosenbrock function
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
The Relauncher module
8.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
8.2
Relauncher abstraction levels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
8.3

```python
TEval
```

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
8.3.1

```python
TPythonEVal
```

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
8.3.2
TCIntEval and TCJitEval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
8.3.3
TCodeEval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
8.3.4
Evaluation functions composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
8.4
TRun . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
8.4.1

```python
TSequentialRun
```

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
8.4.2
TThreadedRun . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
8.4.3

```python
TMpiRun
```

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
8.5
TMaster . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
8.5.1
Dealing with attributes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
8.5.2
TLauncher2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
The Reoptimizer module
9.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
9.1.1
local optimizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
9.1.2
global optimizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
9.1.3
Number of objectives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
9.2
Problem definition
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
9.2.1
Objectives and Constraints
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
9.2.2
Sizing of a hollow bar example problem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
9.3
Local solver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
9.3.1
TNlopt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
9.3.2
Solvers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
9.4
Global solver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
9.4.1
A step-by-step description of Vizir . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
9.4.2
TVizir2 and TVizirIsland . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
9.4.3
Solvers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
10 The Metamodel Optimization module
10.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
10.2
Efficient Global Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
10.2.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
10.2.2
Problem definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
11 The Calibration module
11.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
11.1.1
Distances and likelihoods used to compare observations and model predictions
. . . . . . . . 154
11.2
Calibration classes, distance and likelihood functions, observations and model . . . . . . . . . . . . . . 155
11.2.1
General introduction to data and model definition . . . . . . . . . . . . . . . . . . . . . . . . 156
11.2.2
Defining data, distance and likelihood functions . . . . . . . . . . . . . . . . . . . . . . . . . 157
11.2.3
Common methods of the calibration classes . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
11.2.4
Use-case for this chapter
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
11.3
Minimisation techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
11.3.1
Constructing the TMinimisation object
. . . . . . . . . . . . . . . . . . . . . . . . . . . 170
11.3.2
Defining the TMinimisation properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
11.3.3
Looking at the results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
11.4
Analytical linear Bayesian estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
11.4.1
Constructing the TLinearBayesian object . . . . . . . . . . . . . . . . . . . . . . . . . . 172

<!-- page iv (PDF 5) -->
11.4.2
Defining the TLinearBayesian properties . . . . . . . . . . . . . . . . . . . . . . . . . . 173
11.4.3
Looking at the results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
11.4.4
Prediction of the variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
11.5
Approximate Bayesian Computation techniques (ABC) . . . . . . . . . . . . . . . . . . . . . . . . . 175
11.5.1
Constructing the TRejectionABC object
. . . . . . . . . . . . . . . . . . . . . . . . . . . 176
11.5.2
Defining the TRejectionABC properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
11.5.3
Looking at the results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
11.6
Markov chain Monte Carlo approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
11.6.1
Constructing the TMCMC object
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
11.6.2
Defining the TMCMC properties
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
11.6.3
Running the estimate, exporting and loading chains, and continuing the calculation
. . . . . . 182
11.6.4
Investigating the quality of the samples through diagnostics and plots . . . . . . . . . . . . . . 182
11.6.5
Looking at the results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
11.7
CIRCE method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
11.7.1
Constructing the TCirce object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
11.7.2
Defining the TCirce properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
11.7.3
Running the estimate
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
11.7.4
Looking at the results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
12 The Uncertainty modeler module
12.1
Tests based on the Empirical Distribution Function (“EDF tests”) . . . . . . . . . . . . . . . . . . . . . 190
13 Use-cases in Python
13.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
13.2
Macros Python HowTo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
13.2.1
Macro “howtoConvertTDataServerArray.py” . . . . . . . . . . . . . . . . . . . . . . . . 195
13.2.2
Macro “howtoConvertTMatrixDArray.py” . . . . . . . . . . . . . . . . . . . . . . . . . . 198
13.2.3
Macro “howtoLoadFunction.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
13.2.4
Macro “howtoPassReference.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
13.3
Macros DataServer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
13.3.1
Macro “dataserverAttributes.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
13.3.2
Macro “dataserverMerge.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
13.3.3
Macro “dataserverLoadASCIIFilePasture.py” . . . . . . . . . . . . . . . . . . . . . . . . 207
13.3.4
Macro “dataserverLoadASCIIFile.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210
13.3.5
Macro “dataserverLoadASCIIFileYoungsModulus.py” . . . . . . . . . . . . . . . . . . . 212
13.3.6
Macro “dataserverLoadASCIIFileIonosphere.py” . . . . . . . . . . . . . . . . . . . . . . 217
13.3.7
Macro “dataserverLoadASCIIFileCornell.py” . . . . . . . . . . . . . . . . . . . . . . . . 218
13.3.8
Macro “dataserverComputeQuantile.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
13.3.9
Macro “dataserverGeyserStat.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
13.3.10 Macro “dataserverGeyserRank.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
13.3.11 Macro “dataserverNormaliseVector.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . 224
13.3.12 Macro “dataserverComputeStatVector.py” . . . . . . . . . . . . . . . . . . . . . . . . . . 225
13.3.13 Macro “dataserverComputeCorrelationMatrixVector.py”
. . . . . . . . . . . . . . . . . 226
13.3.14 Macro “dataserverComputeQuantileVec.py” . . . . . . . . . . . . . . . . . . . . . . . . . 227
13.3.15 Macro “dataserverDrawQQPlot.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
13.3.16 Macro “dataserverDrawPPPlot.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
13.3.17 Macro “dataserverPCAExample.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
13.4
Macros Sampler
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
13.4.1
Macro “samplingFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
13.4.2
Macro “samplingLHS.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
13.4.3
Macro “samplingLHSCorrelation.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
13.4.4
Macro “samplingQMC.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
13.4.5
Macro “samplingBasicSampling.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
13.4.6
Macro “samplingOATRegular.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247

<!-- page v (PDF 6) -->
13.4.7
Macro “samplingOATRandom.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
13.4.8
Macro “samplingOATMulti.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
13.4.9
Macro “samplingOATRange.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
13.4.10 Macro “samplingSpaceFilling.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
13.4.11 Macro “samplingMaxiMinLHSFromLHSGrid.py” . . . . . . . . . . . . . . . . . . . . . 253
13.4.12 Macro “samplingConstrLHSLinear.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . 255
13.4.13 Macro “samplingConstrLHSEllipses.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
13.4.14 Macro “samplingSingularCorrelationCase.py” . . . . . . . . . . . . . . . . . . . . . . . . 261
13.5
Macros Launcher
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
13.5.1
Input/Output with vector and string: introduction to macros with multitype
. . . . . . . . . . 264
13.5.2
Macro “launchCodeReadMultiTypeRow.py”
. . . . . . . . . . . . . . . . . . . . . . . . 264
13.6
Macros Sensitivity
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
13.6.1
Macro “sensitivityBrutForceMethodFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . 264
13.6.2
Macro “sensitivityFiniteDifferencesFunctionFlowrate.py”
. . . . . . . . . . . . . . . . . 270
13.6.3
Macro “sensitivityDataBaseFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
13.6.4
Macro “sensitivityFASTFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . . 274
13.6.5
Macro “sensitivityRBDFunctionFlowrate.py”
. . . . . . . . . . . . . . . . . . . . . . . . 277
13.6.6
Macro “sensitivityMorrisFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . 279
13.6.7
Macro “sensitivityMorrisFunctionFlowrateRunner.py” . . . . . . . . . . . . . . . . . . . 282
13.6.8
Macro “sensitivityRegressionFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . 285
13.6.9
Macro “sensitivitySobolFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . . 288
13.6.10 Macro “sensitivitySobolFunctionFlowrateRunner.py” . . . . . . . . . . . . . . . . . . . . 293
13.6.11 Macro “sensitivityRegressionLeveLE.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
13.6.12 Macro “sensitivitySobolLeveLE.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
13.6.13 Macro “sensitivitySobolRe-estimation.py” . . . . . . . . . . . . . . . . . . . . . . . . . . 305
13.6.14 Macro “sensitivitySobolWithData.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 307
13.6.15 Macro “sensitivitySobolLoadFile.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
13.6.16 Macro “sensitivityJohnsonRWFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . 314
13.6.17 Macro “sensitivityJohnsonRWCorrelatedFunctionFlowrate.py” . . . . . . . . . . . . . . 316
13.6.18 Macro “sensitivityJohnsonRWJustCorrelationFakeFlowrate.py” . . . . . . . . . . . . . . 320
13.6.19 Macro “sensitivityHSICFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . . 324
13.6.20 Macro “sensitivitySobolRankFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . 327
13.7
Macros Modeler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
13.7.1
Macro “modelerCornellLinearRegression.py” . . . . . . . . . . . . . . . . . . . . . . . . 330
13.7.2
Macro “modelerFlowrateLinearRegression.py”
. . . . . . . . . . . . . . . . . . . . . . . 331
13.7.3
Macro “modelerFlowrateMultiLinearRegression.py” . . . . . . . . . . . . . . . . . . . . 333
13.7.4
Macro “modelerFlowrateNeuralNetworks.py” . . . . . . . . . . . . . . . . . . . . . . . . 337
13.7.5
Macro “modelerFlowrateNeuralNetworksLoadingPMML.py” . . . . . . . . . . . . . . . 341
13.7.6
Macro “modelerClassificationNeuralNetworks.py”
. . . . . . . . . . . . . . . . . . . . . 343
13.7.7
Macro “modelerFlowratePolynChaosRegression.py”
. . . . . . . . . . . . . . . . . . . . 347
13.7.8
Macro “modelerFlowratePolynChaosIntegration.py” . . . . . . . . . . . . . . . . . . . . 350
13.7.9
Macro “modelerbuildSimpleGP.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352
13.7.10 Macro “modelerbuildGPInitPoint.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
13.7.11 Macro “modelerbuildGPWithAPriori.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . 354
13.7.12 Macro “modelerbuildSimpleGPEstim.py” . . . . . . . . . . . . . . . . . . . . . . . . . . 356
13.7.13 Macro “modelerbuildSimpleGPEstimWithCov.py” . . . . . . . . . . . . . . . . . . . . . 357
13.7.14 Macro “modelerTestKriging.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 359
13.8
Macros Relauncher . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
13.8.1
Macro “relauncherFunctionFlowrateCInt.py” . . . . . . . . . . . . . . . . . . . . . . . . 365
13.8.2
Macro “relauncherFunctionFlowratePython.py” . . . . . . . . . . . . . . . . . . . . . . . 368
13.8.3
Macro “relauncherCodeFlowrateSequential.py” . . . . . . . . . . . . . . . . . . . . . . . 370
13.8.4
Macro “relauncherCodeFlowrateSequential_ConstantVar.py” . . . . . . . . . . . . . . . 373
13.8.5
Macro “relauncherCodeFlowrateThreaded.py”
. . . . . . . . . . . . . . . . . . . . . . . 377
13.8.6
Macro “relauncherCodeFlowrateMPI.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . 379

<!-- page vi (PDF 7) -->
13.8.7
Macro “relauncherCodeFlowrateSequentialFailure.py” . . . . . . . . . . . . . . . . . . . 381
13.8.8
Macro “relauncherCodeMultiTypeKey.py” . . . . . . . . . . . . . . . . . . . . . . . . . . 387
13.8.9
Macro “relauncherCodeMultiTypeKeyEmptyVectors.py” . . . . . . . . . . . . . . . . . . 389
13.8.10 Macro “relauncherCodeMultiTypeKeyEmptyVectorsAsFailure.py” . . . . . . . . . . . . 392
13.8.11 Macro “relauncherCodeReadMultiType.py” . . . . . . . . . . . . . . . . . . . . . . . . . 396
13.8.12 Macro “relauncherComposeMultitypeAndReadMultiType.py” . . . . . . . . . . . . . . . 399
13.8.13 Macro “relauncherCodeFlowrateSequential_TemporaryVar.py” . . . . . . . . . . . . . . 402
13.9
Macros Reoptimizer
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
13.9.1
Macro “reoptimizeHollowBarCode.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
13.9.2
Macro “reoptimizeHollowBarCodeMultiStart.py” . . . . . . . . . . . . . . . . . . . . . . 410
13.9.3
Macro “reoptimizeHollowBarCodevizir.py”
. . . . . . . . . . . . . . . . . . . . . . . . . 412
13.9.4
Macro “reoptimizeHollowBarVizirMoead.py” . . . . . . . . . . . . . . . . . . . . . . . . 416
13.9.5
Macro “reoptimizeHollowBarVizirSplitRuns.py” . . . . . . . . . . . . . . . . . . . . . . 421
13.9.6
Macro “reoptimizeZoneBiSubMpi.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . 424
13.9.7
Macro “reoptimizeZoneBiFunMpi.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
13.10 Macros MetaModelOptim
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433
13.10.1 Macro “metamodoptEgoHimmel.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433
13.11 Macros Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
13.11.1 Macro “calibrationMinimisationFlowrate1D.py”
. . . . . . . . . . . . . . . . . . . . . . 435
13.11.2 Macro “calibrationMinimisationFlowrate2DVizir.py” . . . . . . . . . . . . . . . . . . . . 438
13.11.3 Macro “calibrationLinBayesFlowrate1D.py” . . . . . . . . . . . . . . . . . . . . . . . . . 444
13.11.4 Macro “calibrationRejectionABCFlowrate1D.py” . . . . . . . . . . . . . . . . . . . . . . 449
13.11.5 Macro “calibrationMCMCFlowrate1D.py” . . . . . . . . . . . . . . . . . . . . . . . . . . 453
13.11.6 Macro “calibrationMCMCLinReg.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . 462
13.11.7 Macro “calibrationCirce.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 473
13.12 Macros UncertModeler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479
13.12.1 Macro “uncertModelerTestsYoungsModulus.py”
. . . . . . . . . . . . . . . . . . . . . . 479
Bibliography

<!-- page 1 (PDF 8) -->
LIST OF FIGURES
1.1
Organisation of the Uranie-modules (green boxes) in terms of inter-dependencies. The blue boxes represent
the external dependencies (discussed later on). . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2
Histogram produced using PyROOT
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1
Diagram of the class TDataServer
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2
Attributes of TAttribute class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3
Graph of the variable sdp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4
Scatterplot x2 versus x1 for the geyser data with modification of fields title and unit
. . . . . . .
2.5
Example of PDF, CDF and inverse CDF for Uniform distributions.
. . . . . . . . . . . . . . . . . . .
2.6
Example of PDF, CDF and inverse CDF for LogUniform distributions. . . . . . . . . . . . . . . . . .
2.7
Example of PDF, CDF and inverse CDF for Triangular distributions.
. . . . . . . . . . . . . . . . . .
2.8
Example of PDF, CDF and inverse CDF for LogTriangular distributions. . . . . . . . . . . . . . . . .
2.9
Example of PDF, CDF and inverse CDF for Normal distributions. . . . . . . . . . . . . . . . . . . . .
2.10 Example of PDF, CDF and inverse CDF for a Normal truncated distribution. . . . . . . . . . . . . . .
2.11 Example of PDF, CDF and inverse CDF for LogNormal distributions. . . . . . . . . . . . . . . . . . .
2.12 Example of PDF, CDF and inverse CDF for a LogNormal truncated distribution. . . . . . . . . . . . .
2.13 Example of PDF, CDF and inverse CDF for Trapezium distributions. . . . . . . . . . . . . . . . . . .
2.14 Example of PDF, CDF and inverse CDF for UniformByParts distributions. . . . . . . . . . . . . . . .
2.15 Example of PDF, CDF and inverse CDF for Exponential distributions.
. . . . . . . . . . . . . . . . .
2.16 Example of PDF, CDF and inverse CDF for a Exponential truncated distribution. . . . . . . . . . . . .
2.17 Example of PDF, CDF and inverse CDF for Cauchy distributions. . . . . . . . . . . . . . . . . . . . .
2.18 Example of PDF, CDF and inverse CDF for a Cauchy truncated distribution. . . . . . . . . . . . . . .
2.19 Example of PDF, CDF and inverse CDF for GumbelMax distributions. . . . . . . . . . . . . . . . . .
2.20 Example of PDF, CDF and inverse CDF for a GumbelMax truncated distribution.
. . . . . . . . . . .
2.21 Example of PDF, CDF and inverse CDF for Weibull distributions. . . . . . . . . . . . . . . . . . . . .
2.22 Example of PDF, CDF and inverse CDF for a Weibull truncated distribution. . . . . . . . . . . . . . .
2.23 Example of PDF, CDF and inverse CDF for Beta distributions.
. . . . . . . . . . . . . . . . . . . . .
2.24 Example of PDF, CDF and inverse CDF for GenPareto distributions. . . . . . . . . . . . . . . . . . .
2.25 Example of PDF, CDF and inverse CDF for a GenPareto truncated distribution.
. . . . . . . . . . . .
2.26 Example of PDF, CDF and inverse CDF for Gamma distributions. . . . . . . . . . . . . . . . . . . . .
2.27 Example of PDF, CDF and inverse CDF for a Gamma truncated distribution. . . . . . . . . . . . . . .
2.28 Example of PDF, CDF and inverse CDF for InvGamma distributions. . . . . . . . . . . . . . . . . . .
2.29 Example of PDF, CDF and inverse CDF for a InvGamma truncated distribution. . . . . . . . . . . . .
2.30 Example of PDF, CDF and inverse CDF for Student distributions. . . . . . . . . . . . . . . . . . . . .
2.31 Example of PDF, CDF and inverse CDF for a Student truncated distribution. . . . . . . . . . . . . . .
2.32 Example of PDF, CDF and inverse CDF for GeneralizedNormal distributions.
. . . . . . . . . . . . .
2.33 Example of PDF, CDF and inverse CDF for a generalized normal truncated distribution. . . . . . . . .
2.34 Example of PDF, CDF and inverse CDF for a composed distribution made out of three normal distributions
with respective weights. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- page 2 (PDF 9) -->
2.35 Example of PDF, CDF and inverse CDF for a truncated composed distribution made out of three normal
distributions with respective weights. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.36 Import data from an ASCII file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.37 Content of the ntuple tree contained in “hsimple.root” file. . . . . . . . . . . . . . . . . . . . . . . . .
2.38 Data importation from a TNtuple . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.39 Scatterplot of added attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.40 Graph with a selection definition
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.41 Graph with a definition of Cut . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.42 Different histograms of the same attribute xnorm depending on the method for computing bins. The
values are respectively 100(root), 8 from sturges, 7 from fd and scoot. . . . . . . . . . . . . . . . . . .
2.43 Boxplot of attribute x2 of the TDataServer geyser . . . . . . . . . . . . . . . . . . . . . . . . . .
2.44 CDF graph of attribute x2 of the TDataServer geyser
. . . . . . . . . . . . . . . . . . . . . . . .
2.45 Graphs CDF+CCDF of the attribute x2 of the TDataServer geyser
. . . . . . . . . . . . . . . . .
2.46 Scatterplot between attributes x1 and x2 of the TDataServer geyser. . . . . . . . . . . . . . . . . .
2.47 Scatterplot between attributes x1 and x2 of the TDataServer geyser. . . . . . . . . . . . . . . . . .
2.48 Graphs of “Tufte” type between the attributes x1 and x2 of the TDataServer geyser.
. . . . . . . .
2.49 Graphs of “Pairs” of the TDataServer geyser . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.50 Graphs of “drawPairs” type between the 8 uniformly-distributed inputs and the output of a given problem. 91
2.51 Graphs of “CobWeb” type between the 8 uniformly-distributed inputs and the output of a given problem.
2.52 Plot resulting from the “drawQQPlot” method, comparing “x2” to a normal distribution.
. . . . . . . .
2.53 Plot resulting from the “drawPPPlot” method, comparing “x2” to a normal distribution. . . . . . . . . .
2.54 Representation of some variables of the Notes sample. . . . . . . . . . . . . . . . . . . . . . . . . . .
2.55 Representation of the eigenvalues (left) their overall contributions in percent (middle) and the sum of the
contributions (right) from the PCA analysis.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.56 Representation of correlation between the original variables and the PC under study.
. . . . . . . . . .
2.57 Representation of the data points in the PC-defined plane. . . . . . . . . . . . . . . . . . . . . . . . .
3.1
Schematic view of the input/output relation through a code . . . . . . . . . . . . . . . . . . . . . . . . 100
3.2
Comparison of the two sampling methods SRS (left) and LHS (right) with samples of size 8. . . . . . . 102
3.3
Comparison of deterministic design-of-experiments obtained using either SRS (left) or LHS (right) algorithm
, when having two independent random variables (uniform and normal one) . . . . . . . . . . . 102
3.4
Tufte plot of the design-of-experiments created using a normal and uniform distribution, with a LHS
method with three correlation coefficient: 0, 0.45 and 0.9 . . . . . . . . . . . . . . . . . . . . . . . . . 107
3.5
Tufte plot of the rank of the design-of-experiments created using a normal and uniform distribution, with
a LHS method with three correlation coefficient: 0, 0.45 and 0.9 . . . . . . . . . . . . . . . . . . . . . 107
3.6
Example of sampling done with half million points and two uniform attributes (from 0 to 1), using AMH
copula and varying the parameter value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
3.7
Example of sampling done with half million points and two uniform attributes (from 0 to 1), using Clayton
copula and varying the parameter value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
3.8
Example of sampling done with half million points and two uniform attributes (from 0 to 1), using Frank
copula and varying the parameter value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
3.9
Example of sampling done with half million points and two uniform attributes (from 0 to 1), using Plackett
copula and varying the parameter value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
3.10 Comparison of both quasi Monte-Carlo sequences with both LHS and SRS sampling when dealing with
two uniform attributes.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.11 Comparison of design-of-experiments made with Petras algorithm, using different level values, when
dealing with two uniform attributes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
3.12 Gaussian Random Field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
3.13 Gaussian variograms. Several configurations (in terms of scale factor and variance parameters) are shown
as well. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.14 Sine cardinal variograms. Several configurations (in terms of scale factor and variance parameters) are
shown as well. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.15 Random values for OAT design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

<!-- page 3 (PDF 10) -->
3.16 Example of a dataset reduction (the geyser one) using the NeuralGas algorithm, to go from 272 points
(left) to 50 one (right) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
8.1
Schematic description of the needed steps to define a relauncher procedure
. . . . . . . . . . . . . . . 130
8.2
Hierarchy of classes and structures for the evaluation part of the Relauncher module. . . . . . . . . . . 131
8.3
Hierarchy of classes and structures for the runner part of the Relauncher module. . . . . . . . . . . . 136
9.1
Hollow Bar
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
9.2
Schematic description of the requested steps of an optimisation procedure once this one is performed
with Vizir . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
11.1 Hierarchy of classes and structures out of Doxygen for the Calibration module . . . . . . . . . . . . . 154
12.1 Results of the macro defined previously to produce variety of test of already implemented distributions . 191
13.1 Distribution of the pylint score for the following use-case macros
. . . . . . . . . . . . . . . . . . . . 195
13.2 Graph of the macro "dataserverLoadASCIIFilePasture.py" . . . . . . . . . . . . . . . . . . . 209
13.3 Graph of the macro "dataserverLoadASCIIFile.py" . . . . . . . . . . . . . . . . . . . . . . . . 212
13.4 Graph of the macro "dataserverLoadASCIIFileYoungsModulus.py" . . . . . . . . . . . . . . 216
13.5 Graph of the macro "dataserverLoadASCIIFileIonosphere.py"
. . . . . . . . . . . . . . . . 218
13.6 Graph of the macro "dataserverComputeQuantile.py" . . . . . . . . . . . . . . . . . . . . . . 222
13.7 Graph of the macro "dataserverDrawQQPlot.py" . . . . . . . . . . . . . . . . . . . . . . . . . . 231
13.8 Graph of the macro "dataserverDrawPPPlot.py" . . . . . . . . . . . . . . . . . . . . . . . . . . 234
13.9 Graph of the macro “samplingFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
13.10Graph of the macro “samplingLHS.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
13.11Graph de la macro “samplingLHSCorrelation.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
13.12Graph of the macro “samplingQMC.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
13.13Graph of the macro “samplingSpaceFilling.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
13.14Graph of the macro “samplingMaxiMinLHSFromLHSGrid.py” . . . . . . . . . . . . . . . . . . . 255
13.15Graph of the macro “samplingConstrLHSLinear.py” . . . . . . . . . . . . . . . . . . . . . . . . . 258
13.16Graph of the macro “samplingConstrLHSEllipses.py” . . . . . . . . . . . . . . . . . . . . . . . . . 260
13.17Graph of the macro “samplingSingularCorrelationCase.py”
. . . . . . . . . . . . . . . . . . . . . 264
13.18Graph of the macro “sensitivityBrutForceMethodFlowrate.py” . . . . . . . . . . . . . . . . . . . . 269
13.19Graph of the macro “sensitivityDataBaseFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . . . . 274
13.20Graph of the macro “sensitivityFASTFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . 276
13.21Graph of the macro “sensitivityRBDFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . 278
13.22Graph of the macro “sensitivityMorrisFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . 281
13.23Graph of the macro “sensitivityMorrisFunctionFlowrateRunner.py” . . . . . . . . . . . . . . . . . 285
13.24Graph of the macro “sensitivityRegressionFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . 287
13.25Graph of the macro “sensitivitySobolFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . 290
13.26Graph of the macro “sensitivitySobolFunctionFlowrateRunner.py” . . . . . . . . . . . . . . . . . . 295
13.27Graph of the macro “sensitivityRegressionLeveLE.py” . . . . . . . . . . . . . . . . . . . . . . . . . 300
13.28Graph of the macro “sensitivitySobolLeveLE.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305
13.29Graph of the macro “sensitivitySobolRe-estimation.py” . . . . . . . . . . . . . . . . . . . . . . . . 307
13.30Graph of the macro “sensitivitySobolWithData.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . 309
13.31Graph of the macro “sensitivitySobolLoadFile.py” . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
13.32Graph of the macro “sensitivityJohnsonRWFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . 315
13.33Graph of the macro “sensitivityJohnsonRWCorrelatedFunctionFlowrate.py” . . . . . . . . . . . . 319
13.34Graph of the macro “sensitivityJohnsonRWJustCorrelationFakeFlowrate.py”
. . . . . . . . . . . 323
13.35Graph of the macro “sensitivityHSICFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . . . . 326
13.36Graph of the macro “sensitivitySobolRankFunctionFlowrate.py” . . . . . . . . . . . . . . . . . . . 329
13.37Graph of the macro “modelerCornellLinearRegression.py” . . . . . . . . . . . . . . . . . . . . . . 331
13.38Graph of the macro “modelerFlowrateLinearRegression.py” . . . . . . . . . . . . . . . . . . . . . 333
13.39Graph of the macro “modelerFlowrateMultiLinearRegression.py” . . . . . . . . . . . . . . . . . . 337
13.40Graph of the macro “modelerFlowrateNeuralNetworks.py” . . . . . . . . . . . . . . . . . . . . . . 339

<!-- page 4 (PDF 11) -->
13.41Graph of the macro “modelerFlowrateNeuralNetworksLoadingPMML.py” . . . . . . . . . . . . . 342
13.42Graph of the macro “modelerClassificationNeuralNetworks.py”
. . . . . . . . . . . . . . . . . . . 346
13.43Graph of the macro “modelerbuildSimpleGPEstim.py” . . . . . . . . . . . . . . . . . . . . . . . . 357
13.44Graph of the macro “modelerbuildSimpleGPEstimWithCov.py” . . . . . . . . . . . . . . . . . . . 359
13.45Graph of the macro “modelerTestKriging.py”
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
13.46Representation of the output as a function of the first input with a colZ option . . . . . . . . . . . . . . 367
13.47Representation of the output as a function of the first input with a colZ option . . . . . . . . . . . . . . 370
13.48Representation of the output as a function of the first input with a colZ option . . . . . . . . . . . . . . 372
13.49Representation of the output as a function of the first input with a colZ option . . . . . . . . . . . . . . 378
13.50Representation of the output as a function of the first input with a colZ option . . . . . . . . . . . . . . 381
13.51Representation of the output data point when the code is asked to fail on purpose. . . . . . . . . . . . . 384
13.52Graph of the macro “relauncherCodeMultiTypeKey.py” . . . . . . . . . . . . . . . . . . . . . . . . 389
13.53Graph of the macro “relauncherCodeMultiTypeKeyEmptyVectors.py”
. . . . . . . . . . . . . . . 392
13.54Graph of the macro “relauncherCodeMultiTypeKeyEmptyVectorsAsFailure.py” . . . . . . . . . . 395
13.55Graph of the macro “reoptimizeHollowBarCodeVizir.py” . . . . . . . . . . . . . . . . . . . . . . . 416
13.56Graph of the macro “reoptimizeHollowBarVizirMoead.py” . . . . . . . . . . . . . . . . . . . . . . 421
13.57Graph of the macro “reoptimizeHollowBarVizirSplitRuns.py” . . . . . . . . . . . . . . . . . . . . 424
13.58The core and its assemblies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
13.59Residuals graph of the macro “calibrationMinimisationFlowrate1D.py”
. . . . . . . . . . . . . . . 438
13.60Residuals graph of the macro “calibrationMinimisationFlowrate2DVizir.py”
. . . . . . . . . . . . 443
13.61Parameter graph of the macro “calibrationMinimisationFlowrate2DVizir.py” . . . . . . . . . . . . 444
13.62Residuals graph of the macro “calibrationLinBayesFlowrate1D.py” . . . . . . . . . . . . . . . . . . 448
13.63Parameter graph of the macro “calibrationLinBayesFlowrate1D.py”
. . . . . . . . . . . . . . . . . 449
13.64Residuals graph of the macro “calibrationRejectionABCFlowrate1D.py” . . . . . . . . . . . . . . . 452
13.65Parameter graph of the macro “calibrationRejectionABCFlowrate1D.py”
. . . . . . . . . . . . . . 453
13.66Trace graph of the macro “calibrationMCMCFlowrate1D.py” . . . . . . . . . . . . . . . . . . . . . 459
13.67Acceptation ratio graph of the macro “calibrationMCMCFlowrate1D.py” . . . . . . . . . . . . . . . 460
13.68Residuals graph of the macro “calibrationMCMCFlowrate1D.py” . . . . . . . . . . . . . . . . . . . 461
13.69Parameter graph of the macro “calibrationMCMCFlowrate1D.py” . . . . . . . . . . . . . . . . . . 462
13.70Trace graph of the macro “calibrationMCMCLinReg.py” . . . . . . . . . . . . . . . . . . . . . . . 469
13.71Acceptation ratio graph of the macro “calibrationMCMCLinReg.py” . . . . . . . . . . . . . . . . . 470
13.722D Trace graph of the macro “calibrationMCMCLinReg.py” . . . . . . . . . . . . . . . . . . . . . 471
13.73Residuals graph of the macro “calibrationMCMCLinReg.py” . . . . . . . . . . . . . . . . . . . . . 472
13.74Parameter graph of the macro “calibrationMCMCLinReg.py” . . . . . . . . . . . . . . . . . . . . . 473
13.75Graph of the macro “uncertModelerTestsYoungsModulus.py” . . . . . . . . . . . . . . . . . . . . 480

<!-- page 5 (PDF 12) -->
LIST OF TABLES
2.1
List of Uranie classes representing the probability laws . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2
List of keywords of header in ASCII files.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3
List of keywords of header in ASCII files.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Abstract
This documentation presents the features of the Uranie platform (based on Uranie v4.11.0), that is developed
at CEA/DES. This platform is designed for uncertainty propagation, sensitivity analysis and computational code
qualification, in a single software environment. It is largely based on the ROOT software (http://root.cern.ch/), an
oriented-object framework that is designed and maintained by CERN, primarily used by the particle physicist to analyse
the very large amount of data recorded at the LHC (Large Hadron Collider).
Commit
61cebb3
