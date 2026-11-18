# The DataServer module — Visualisation dedicated to uncertainties … Combining these aspects: performing PCA
<!-- source PDF pages 92-106 -->

<!-- page 85 (PDF 92) -->
## 2.5 Visualisation dedicated to uncertainties

ROOT integrates many high level visualisation features, but some of them, devoted to statistics are missing. As they are
linked to data, it seemed relevant to develop them in this library. Many of the methods discussed throughout this section
are in any case, based on the original ROOT methods that produce plots from a TTree-object: the TTree::Draw method
(and subsequently the TTree::Scan when dumping on screen the content of the TDataServer).
INFO-CIRCLE Summary: TTree::Draw and TTree::Scan methods
• TTree::Draw(const char* varexp=””, const char* select=””, Option_t* option=”” )
Draw the expression varexp for specified entries.
Returns -1 in case of error or number of selected events in case of success.
The list of the options is located on the THistPainter class on the ROOT website.
• TTree::Scan( const char* varexp=””, const char* select=””, Option_t* option=”” )
Scan the expression varexp for specified entries.
Returns -1 in case of error or number of selected events in case of success.
These tree arguments are the same on the TDataServer::draw and TDataServer::scan methods.

### 2.5.1 Histogram

The histogram is present in ROOT but it needs to be encapsulated when the user wants to choose an automatic method
determining the number of bins. By default, the number of bins is given in the variable of the configuration file of ROOT
.rootrc of the directory $ROOTSYS/etc. This information can be overloaded by an user file .rootrc in its home
directory ($HOME), or in a local file where ROOT is executed. Several methods exist to determine the number of “bins”
according to the characteristics of the variable to be visualised.
Again we consider the TDataServer built from the geyser.dat file, to which we add the attribute xnorm, then the
histograms will be plotted using the different methods of this new attribute.

```python
c2 = ROOT.TCanvas()
apad = ROOT.TPad("apad","apad",0, 0.03, 1, 1)
tdsGeyser = DataServer.TDataServer("tdsgeyser", "Database of the geyser")
tdsGeyser.fileDataRead("geyser.dat")
tdsGeyser.addAttribute("xnorm", "sqrt(x1*x1+x2*x2)")
apad.Divide(2,2)
apad.cd(1)
tdsGeyser.draw("xnorm","","nclass=root")
apad.cd(2)
tdsGeyser.draw("xnorm","","nclass=sturges")
apad.cd(3)
tdsGeyser.draw("xnorm","","nclass=fd")
apad.cd(4)
tdsGeyser.draw("xnorm","","nclass=scott")
```

<!-- page 86 (PDF 93) -->
Figure 2.42: Different histograms of the same attribute xnorm depending on the method for computing bins. The values
are respectively 100(root), 8 from sturges, 7 from fd and scoot.

### 2.5.2 Box-and-whisker(“boxplot”)

```python
tdsGeyser.drawBoxPlot("x2")
```

Figure 2.43: Boxplot of attribute x2 of the TDataServer geyser

### 2.5.3 CDF, CCDF curves

We can plot the graphs of CDF and/or CCDF.

```python
tdsGeyser.drawCDF("x2")
```

<!-- page 87 (PDF 94) -->
```python
tdsGeyser.drawCDF("x2","","ccdf")
```

Figure 2.44: CDF graph of attribute x2 of the TDataServer geyser
Figure 2.45: Graphs CDF+CCDF of the attribute x2 of the TDataServer geyser

### 2.5.4 Graph 2D with contour levels

When a 2D scatterplot is plotted, we do not automatically see the number of points falling in the same cell. To get
an assessment of this information, the contour levels of the number of points have to be put in background and then it
becomes possible to plot the classical scatterplot.

```python
tdsGeyser = DataServer.TDataServer("tdsgeyser", "Geyser database")
tdsGeyser.fileDataRead("geyser.dat")
```

<!-- page 88 (PDF 95) -->
```python
tdsGeyser.drawScatterplot("x2:x1")
```

Figure 2.46: Scatterplot between attributes x1 and x2 of the TDataServer geyser.
This figure has to be compared to the classical scatterplot shown, for instance, in Figure 2.4.

### 2.5.5 Graph 2D “profile”

It consists in partitioning the “x” axis with a number of bins and in plotting, for each segment, the mean value in blue and
the standard deviation by a black line. The number of segments N is passed as an option with the formalism nclass=N.
We can also visualise the scatterplot just below the profile plot, by adding the option “same” (resulting in the red points
also shown in Figure 2.47).

```python
tdsGeyser = DataServer.TDataServer("tdsgeyser", "Geyser database")
tdsGeyser.fileDataRead("geyser.dat")
tdsGeyser.drawProfile("x2:x1","","same")
```

<!-- page 89 (PDF 96) -->
Figure 2.47: Scatterplot between attributes x1 and x2 of the TDataServer geyser.

### 2.5.6 Graph 2D “Tufte”

This 2D graph consists in plotting the scatterplot of the two attributes, and also plotting each of the two histograms of the
attributes in X and Y, respectively below or on the left of the scatterplot.

```python
tdsGeyser = DataServer.TDataServer("tdsgeyser", "Database of the geyser")
tdsGeyser.fileDataRead("geyser.dat")
tdsGeyser.drawTufte("x2:x1")
```

Figure 2.48: Graphs of “Tufte” type between the attributes x1 and x2 of the TDataServer geyser.

<!-- page 90 (PDF 97) -->
### 2.5.7 Graph 2D “pairs”

This 2D graph consists in creating a matrix of graphs, where for the (i,j) cells with i different from j, the graph contains
the scatterplot of the attribute j versus the attribute i, and for cell (i,i), the graph contains the histogram of the attribute i.

```python
tdsGeyser = DataServer.TDataServer("tdsgeyser", "Database of the geyser")
tdsGeyser.fileDataRead("flowrateUniformDesign.dat")
tdsGeyser.drawPairs()
```

Figure 2.49: Graphs of “Pairs” of the TDataServer geyser
INFO-CIRCLE Summary: 2D Graph
• drawScatterplot (const char* varexp, const char* selection=””, Option_t* option=””)
Draw 2D graph with the number of points of attributes located in varexp on the background.
• drawProfile (const char* varexp, const char* selection=””, Option_t* option=””)
Draw 2D graphic of the mean and standard deviation of each segment of “X” axis for the attributes contained
in varexp.
Lightbulb Tip
The possible values of options option are:
nclass=[0-9]*
Specifies the number of segments in “X” axis .
same
Displays the 2D scatterplot below “profile”.
• drawTufte (const char* varexp, const char* selection=””, Option_t* option=””)
Draw 2D graph of the attributes located in varexp.

<!-- page 91 (PDF 98) -->
Lightbulb Tip
The possible values of options option are:
optstat
Prints the window containing statistics in each histogram
scatter
Prints the scatterplot the same way as the command drawScatterplot.
• drawPairs (const char* varexp, const char* selection=””, Option_t* option=””)
Create the matrix of graph with the attributes located in varexp.
It should be noticed that these functions have the same signature as the draw method of a TTree of ROOT.
Exclamation-Triangle Warning
For all these methods, the character varexp must contain either two attributes or a single character “:”

### 2.5.8 Graph “CobWeb”

For multidimensional problem, the drawPairs method is limited to spot correlation because of the way the output looks.
For instance in a problem with 8 uniformly-distributed inputs and one output, one can get a graphic as the one shown in
Figure 2.50 (obtained with the code below). No special trend can be seen here.

```python
tdsCobweb = DataServer.TDataServer("tdscobweb", "Database of the cobweb")
tdsCobweb.fileDataRead("cobwebdata.dat") # read data file
tdsCobweb.drawPairs() # do the drawPairs graph
```

Figure 2.50: Graphs of “drawPairs” type between the 8 uniformly-distributed inputs and the output of a given problem.
The “CobWeb” multidimensional graph, on the other hand, consists in plotting every dimension on a vertical axis and
connecting all the points for a single event with a straight line. It is particularly useful to spot correlation in high-dimension
problems as it is simple to highlight a certain region (by changing the colour for instance) to see if the rest of the variable

<!-- page 92 (PDF 99) -->
are randomly distributed or not.

```python
# Draw the cobweb plot
tdsCobweb.drawCobWeb("x0:x1:x2:x3:x4:x5:x6:x7:out") # Draw the cobweb
# Get the parallel coordination part to perform modification
para = ROOT.gPad.GetListOfPrimitives().FindObject("__tdspara__0")
# Get the output axis
axis = para.GetVarList().FindObject("out")
# Create a range for 0.97 < out < 1.0 and display it in blue
Range
       = ROOT.TParallelCoordRange(axis, 0.97, 1.0)
axis.AddRange(Range)
para.AddSelection("blue")
Range.Draw()
```

This code for instance specifies a region-of-interest in the output, when the value are greater than 0.97. A correlation is
highlighted between these values and a region, for which the fourth input variable has high value while the sixth input
variable values lie between 0.2 and 0.4. The result of this code is shown in Figure 2.51.
Figure 2.51: Graphs of “CobWeb” type between the 8 uniformly-distributed inputs and the output of a given problem.

### 2.5.9 QQ plot

Exclamation-Triangle Warning
This function requires the “mathmore” feature to have be installed along with your ROOT version. If not found, this
function cannot be used and will return nothing but an equivalent to this message.
Once dealing with an unknown set of points, it is possible to compare it to known statistical law (among the following
already implemented list: normal, uniform, weibull, gumbelmax, exponential, beta, gamma and lognormal). For instance,
if one wants to compare “x2” variable from the geyser dataset to a normal law, one can have a look at the quantile
distribution from the sample and compare it to the expected behaviour by following the steps below.

<!-- page 93 (PDF 100) -->
```python
tdsQQ = DataServer.TDataServer("tdsQQ", "Database of the QQ")
tdsQQ.fileDataRead("geyser.dat") # read data file
tdsQQ.computeStatistic() # to estimate mu and sigma
tdsQQ.drawQQPlot("x2", "normal(%g,%g)" % (tdsQQ.getAttribute("x2").getMean(), tdsQQ.
```

˓→getAttribute("x2").getStd()), 400)
Figure 2.52: Plot resulting from the “drawQQPlot” method, comparing “x2” to a normal distribution.
It is obvious here, that the “x2” law, clearly doesn’t seem to follow a normal law (which was pretty obvious by looking at
Figure 2.48 for instance). An heavy use of this method is provided in Macro “dataserverDrawQQPlot.py”.

### 2.5.10 PP plot

Exclamation-Triangle Warning
This function requires the “mathmore” feature to have be installed along with your ROOT version. If not found, this
function cannot be used and will return nothing but an equivalent to this message.
Once dealing with an unknown set of points, it is possible to compare it to known statistical law (among the following
already implemented list: normal, uniform, weibull, gumbelmax, exponential, beta, gamma and lognormal). For instance,
if one wants to compare “x2” variable from the geyser dataset to a normal law, one can have a look at the probabiliity
distribution from the sample and compare it to the expected behaviour by following the steps below.

```python
tdsPP = DataServer.TDataServer("tdsPP", "Database of the PP")
tdsPP.fileDataRead("geyser.dat") # read data file
tdsPP.computeStatistic() # to estimate mu and sigma
tdsPP.drawPPPlot("x2", "normal(%g,%g)" %(tdsPP.getAttribute("x2").getMean(), tdsPP.
```

˓→getAttribute("x2").getStd()), 400)

<!-- page 94 (PDF 101) -->
Figure 2.53: Plot resulting from the “drawPPPlot” method, comparing “x2” to a normal distribution.
It is obvious here, that the “x2” law, clearly doesn’t seem to follow a normal law (which was pretty obvious by looking at
Figure 2.48 for instance). An heavy use of this method is provided in Macro “dataserverDrawPPPlot.py”.

## 2.6 Combining these aspects: performing PCA

This part is introducing an example of analysis that combines all the aspects discussed up to now: handling data, perform
a statistical treatment and visualise the results. This analysis is called PCA for Principal Component Analysis and is often
used to
• gather event in a sample that seem to have a common behaviour;
• reduce the dimension of the problem under study.
There is a very large number of articles, even books, discussing the theoretical aspects of principal component analysis
(for instance one can have a look at [Jol11]) a small theoretical introduction can in any case be found in [Bla17].

### 2.6.1 PCA usage within Uranie

Let’s use a relatively simple example to illustrate the principle and the way we can achieve a reduction of dimension while
keeping the inertia as large as possible. One can have a look at a sample of marks from different pupils, in various kinds
of subject, all gathered in the Notes.dat whose content is shown below.

```python
#TITLE: Marks of my pupils
#COLUMN_NAMES: Pupil | Maths | Physics | French | Latin | Music
#COLUMN_TYPES: S|D|D|D|D|D
Jean 6 6 5 5.5 8
Aline 8 8 8 8 9
Annie 6 7 11 9.5 11
Monique 14.5 14.5 15.5 15 8
Didier 14 14 12 12 10
Andre 11 10 5.5 7 13
Pierre 5.5 7 14 11.5 10
```

<!-- page 95 (PDF 102) -->
```python
Brigitte 13 12.5 8.5 9.5 12
Evelyne 9 9.5 12.5 12 18
```

One can have a look at some of these variables against one another to have a sense of what’s about to be done. In Figure
2.54, the maths marks of the pupils are displayed against latin on the left and physics on the right. Whereas no specific
trend is shown on the left part, an obvious correlation can be seen from the right figure meaning one can try extrapolate
the maths marks from the value of the physics one.
Figure 2.54: Representation of some variables of the Notes sample.

#### 2.6.1.1 Perform the PCA

The way to perform this analysis is rather simple through Uranie: simply provide the dataserver that contains data to an
TPCA object, only precising the name of the variables to be investigated. This is exactly what’s done below:

```python
# Read the database
tdsPCA = DataServer.TDataServer("tdsPCA", "my TDS")
tdsPCA.fileDataRead("Notes.dat")
# Create the PCA object precising the variables of interest
tpca = DataServer.TPCA(tdsPCA, "Maths:Physics:French:Latin:Music")
tpca.compute()
```

Once done, the process described in the [Bla17] is finished and then interpretation starts.

<!-- page 96 (PDF 103) -->
#### 2.6.1.2 Interpretation of PCA results

The first result that one should consider is the non-zero eigenvalues (so the variance of the corresponding principal components
). These values are stored in a specific ntuple, that can be retrieve by calling the method getResultNtupleD().
This ntuple contains three kind of information: the eigenvalues itself (“eigen”), these values as contributions in percent
of the sum of eigenvalues (“eigen_pct”) and the sum of these contributions (“sum_eigen_pct”). All these values can be
accessed through the usual Scan method (see Macro “dataserverPCAExample.py” to see the results).
The following lines are showing how to represent the eigenvalues as plots and the results are gathered in Figure 2.55.
From this figure, one can easily conclude that only the three first principal components are useful (as it reached an inertia
of a bit more than 99% of the original one). This is the solution chosen for the rest of the graphical representations below
and this is the first nice results from this step: it is possible to reduce the dimension of our problem from the 5 different
subjects to the three principal component that needs to be explicated.

```python
# Draw the eigen values in different normalisation
c = ROOT.TCanvas("cEigenValues", "Eigen Values Plot", 1100, 500)
apad3 = ROOT.TPad("apad3", "apad3", 0, 0.03, 1, 1)
apad3.Draw()
apad3.cd()
apad3.Divide(3, 1)
ntd = tpca.getResultNtupleD()
apad3.cd(1)
ntd.Draw("eigen:i", "", "lp")
apad3.cd(2)
ntd.Draw("eigen_pct:i", "", "lp")
ROOT.gPad.SetGrid()
apad3.cd(3)
ntd.Draw("sum_eigen_pct:i", "", "lp")
ROOT.gPad.SetGrid()
c.SaveAs("PCA_notes_musique_Eigen.png")
```

Figure 2.55: Representation of the eigenvalues (left) their overall contributions in percent (middle) and the sum of the
contributions (right) from the PCA analysis.
As stated previously, one can have a look at the variables in their usual representation (that can be seen in Figure 2.56)
that is called the correlation circle. This plot is obtained by calling the drawLoading method that takes two arguments:

<!-- page 97 (PDF 104) -->
the first one being the number of the PC used as x-axis while the second one is the number of the PC used as y-axis. The
code to get Figure 2.56 is shown below:

```python
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
```

Figure 2.56 represents the correlation between the original variable and the principal component under study. Two kinds
of principal component are resulting from PCA:
• the size one where all variables are on the same size of the principal component. In our case, the first PC in Figure
2.56 represents the variability of marks.
• the shape one where variables are balanced from positive to negative value of the principal component. In our case,
the second PC in Figure 2.56 represents the difference observed between scientific variables, such as maths and
physics, from literary ones, such as french and latin.
Finally to complete the picture, the third PC is a shape one that represents the fact that music seems to have a very specific
behaviour, different from all the other studies.

<!-- page 98 (PDF 105) -->
Figure 2.56: Representation of correlation between the original variables and the PC under study.
Finally, one can also have a look at the points distribution in the new PC space (that can be seen in Figure 2.57). This
plot is obtained by calling the method drawPCA that takes two compulsory arguments: the first one being the number of
the PC used as x-axis while the second one is the number of the PC used as y-axis. An extra argument can be provided
that is used to specify a branch in the database that contains the name of the points (the name of the pupils) which allows
to get a nice final plot. The code to get Figure 2.57 is shown below:

```python
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
```

Figure 2.57 shows where to find our pupils with respect to our new basis and the interpretation of the correlation plot of
the variable holds as well:

<!-- page 99 (PDF 106) -->
• looking at PC1, it seems to be defined by two extremes, Jean and Monique, the former being bad at every subjects
while the latter is good at (almost) all subjects.
• looking at PC2, it also seems to be defined by two extremes, Pierre and Andre, the former having way better marks
at literary subjects than at scientific ones while its the other way around for the latter.
• looking at PC3, it seems to oppose Evelyn to all the other pupils, and this correspond to fact that every pupils is
bad at music, but Evelyn.
Figure 2.57: Representation of the data points in the PC-defined plane.
All these interpretations remain graphical and give an easy way to summarise the impact of the PCA analysis. Disregarding
the sources considered (the variables or the points), one can have quantitative interpretation coefficients that detail more
the “feeling” described above:
• the quality of the representation: it shows how well the source (either the subject or the pupil in our case) is
represented by a given PC. Summing these values over the PC should lead to 1 for every sources.
• the contribution to axis: it shows how much the source (either the subject or the pupil in our case) contribute to the
definition of the given PC. Summing these values over the source (for the given PC) should lead to 1 for every PC.
Example of how to get these numbers can be found in the use-case macros, see Macro “dataserverPCAExample.py”.
