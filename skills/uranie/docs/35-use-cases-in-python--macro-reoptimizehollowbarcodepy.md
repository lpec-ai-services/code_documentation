# Use-cases in Python — Macros Reoptimizer — Macro “reoptimizeHollowBarCode.py” … Macro “reoptimizeHollowBarVizirSplitRuns.py”
<!-- source PDF pages 414-430 -->

<!-- page 407 (PDF 414) -->
## 13.9 Macros Reoptimizer

### 13.9.1 Macro “reoptimizeHollowBarCode.py”

#### 13.9.1.1 Objective

The objective of the macro is to optimize the section of the hollow bar defined in Sizing of a hollow bar example problem
using the NLopt solvers (reducing it to a single-criterion optimisation as already explained in Local solver. This can be
done with different solvers, the results being achieved within more or less time and following the requested constraints
with more or less accuracy (depending on the hypothesis embedded by the chosen solver).

#### 13.9.1.2 Macro Uranie

```python
"""
Example of hollow bar optimisation
"""
import numpy as np
from URANIE import DataServer, Relauncher, Reoptimizer
import ROOT
# variables
x = DataServer.TAttribute("x", 0.0, 1.0)
y = DataServer.TAttribute("y", 0.0, 1.0)
thick = DataServer.TAttribute("thick")
                                        # thickness
sect = DataServer.TAttribute("sect")
                                      # section of the pipe
dist = DataServer.TAttribute("dist")
                                      # distortion
# Creating the TCodeEval, dumping output of the dummy python in output file
python_exec = "python3"
if ROOT.gSystem.GetBuildArch() == "win64":
    python_exec = python_exec[:-1]
code = Relauncher.TCodeEval(python_exec + " bar.py > bartoto.dat")
# Pass the python script itself as input. inputs are modified in bar.py
inputfile = Relauncher.TKeyScript("bar.py")
inputfile.addInput(x, "x")
inputfile.addInput(y, "y")
code.addInputFile(inputfile)
# precise the name of the output file in which to read the three output
outputfile = Relauncher.TFlatResult("bartoto.dat")
outputfile.addOutput(thick)
outputfile.addOutput(sect)
outputfile.addOutput(dist)
code.addOutputFile(outputfile)
# Create a runner
runner = Relauncher.TSequentialRun(code)
runner.startSlave()
                     # Usual Relauncher construction
if runner.onMaster():
    # Create the TDS
```

<!-- page 408 (PDF 415) -->
```python
    tds = DataServer.TDataServer("vizirDemo", "Param de l'opt vizir")
    tds.addAttribute(x)
    tds.addAttribute(y)
    # Choose a solver
    solv = Reoptimizer.TNloptCobyla()
    # solv = Reoptimizer.TNloptBobyqa()
    # solv = Reoptimizer.TNloptPraxis()
    # solv = Reoptimizer.TNloptNelderMead()
    # solv = Reoptimizer.TNloptSubplexe()
    # Create the single-objective constrained optimizer
    opt = Reoptimizer.TNlopt(tds, runner, solv)
    # add the objective
    opt.addObjective(sect)
                            # minimizing the section
    # and the constrains
    constrDist = Reoptimizer.TLesserFit(14)
    opt.addConstraint(dist, constrDist)
                                         # distortion (dist < 14)
    positiv = Reoptimizer.TGreaterFit(0.4)
    opt.addConstraint(thick, positiv)
                                       # thickness (thick > 0.4)
    # Starting point and maximum evaluation
    point = np.array([0.9, 0.2])
    opt.setStartingPoint(len(point), point)
    opt.setMaximumEval(1000)
    opt.solverLoop()
                      # running the optimization
    # Stop the slave processes
    runner.stopSlave()
# solution
tds.getTuple().Scan("*", "", "colsize=9 col=:::5:4")
```

The variables are defined as follow:

```python
# variables
x = DataServer.TAttribute("x", 0.0, 1.0)
y = DataServer.TAttribute("y", 0.0, 1.0)
thick = DataServer.TAttribute("thick")
                                        # thickness
sect = DataServer.TAttribute("sect")
                                      # section of the pipe
dist = DataServer.TAttribute("dist")
                                      # distortion
```

where the first two are the input ones while the last ones are computed using the provided code (as explained in Sizing of
a hollow bar example problem). This code is configured through these lines:

```python
# Creating the TCodeEval, dumping output of the dummy python in output file
code = Relauncher.TCodeEval(python_exec + " bar.py > bartoto.dat")
# Pass the python script itself as input. inputs are modified in bar.py
```

<!-- page 409 (PDF 416) -->
```python
inputfile = Relauncher.TKeyScript("bar.py")
inputfile.addInput(x, "x")
inputfile.addInput(y, "y")
code.addInputFile(inputfile)
# precise the name of the output file in which to read the three output
outputfile = Relauncher.TFlatResult("bartoto.dat")
outputfile.addOutput(thick)
outputfile.addOutput(sect)
outputfile.addOutput(dist)
code.addOutputFile(outputfile)
# Create a runner
runner = Relauncher.TSequentialRun(code)
runner.startSlave()
                     # Usual Relauncher construction
```

The usual Relauncher construction is followed, using a TSequentialRun runner and the solver is chosen in these lines:

```python
# Choose a solver
solv = Reoptimizer.TNloptCobyla()
# solv = Reoptimizer.TNloptBobyqa()
# solv = Reoptimizer.TNloptPraxis()
# solv = Reoptimizer.TNloptNelderMead()
# solv = Reoptimizer.TNloptSubplexe()
```

Combining the runner, solver and dataserver, the master object is created and the objective and constraint are defined
(keeping in mind that only single-criterion problems are implemented when dealing with NLopt, so the distortion criteria
is downgraded to a constraint). This is done in

```python
# Create the single-objective constrained optimizer
opt = Reoptimizer.TNlopt(tds, runner, solv)
# add the objective
opt.addObjective(sect)
                        # minimizing the section
# and the constrains
constrDist = Reoptimizer.TLesserFit(14)
opt.addConstraint(dist, constrDist)
                                     # distortion (dist < 14)
positiv = Reoptimizer.TGreaterFit(0.4)
opt.addConstraint(thick, positiv)
                                   # thickness (thick > 0.4)
```

Finally the starting point is set along with the maximal number of evaluation just before starting the loop.

```python
# Starting point and maximum evaluation
point = np.array([0.9, 0.2])
opt.setStartingPoint(len(point), point)
opt.setMaximumEval(1000)
opt.solverLoop()
                  # running the optimization
```

<!-- page 410 (PDF 417) -->
#### 13.9.1.3 Console

This macro leads to the following result

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
|....:....|....:....|....:....|....:....
|***************************************************************************
*
     Row
           * vizirDemo *
                               x.x *
                                           y.y * thick * sect * dist.dist *
***************************************************************************
*
         0 *
                     0 * 0.5173156 * 0.1173173 * 0.399 * 0.25 * 13.999986 *
***************************************************************************
```

###  13.9.2 Macro “reoptimizeHollowBarCodeMultiStart.py”

####  13.9.2.1 Objective

The objective of the macro is to optimize the section of the hollow bar defined in Sizing of a hollow bar example problem
using the NLopt solvers (reducing it to a single-criterion optimisation as already explained in Local solver. It is largely
based on the previous macro, the main change being the fact that we allow different starting points.

#### 13.9.2.2 Macro Uranie

```python
"""
Example of hollow bar optimisation in multistart mode
"""
import numpy as np
from URANIE import DataServer, Relauncher, Reoptimizer
import ROOT
# variables
x = DataServer.TAttribute("x", 0.0, 1.0)
y = DataServer.TAttribute("y", 0.0, 1.0)
thick = DataServer.TAttribute("thick")
                                        # thickness
sect = DataServer.TAttribute("sect")
                                      # section of the pipe
dist = DataServer.TAttribute("dist")
                                      # distortion
# Creating the TCodeEval, dumping output of the dummy python in an output file
python_exec = "python3"
if ROOT.gSystem.GetBuildArch() == "win64":
    python_exec = python_exec[:-1]
code = Relauncher.TCodeEval(python_exec + " bar.py > bartoto.dat")
# Pass the python script itself as input. inputs are modified in bar.py
inputfile = Relauncher.TKeyScript("bar.py")
inputfile.addInput(x, "x")
inputfile.addInput(y, "y")
code.addInputFile(inputfile)
# precise the name of the output file in which to read the three output
outputfile = Relauncher.TFlatResult("bartoto.dat")
```

<!-- page 411 (PDF 418) -->
```python
outputfile.addOutput(thick)
outputfile.addOutput(sect)
outputfile.addOutput(dist)
code.addOutputFile(outputfile)
# Create a runner
runner = Relauncher.TSequentialRun(code)
runner.startSlave()
                     # Usual Relauncher construction
if runner.onMaster():
    # Create the TDS
    tds = DataServer.TDataServer("vizirDemo", "Param de l'opt vizir")
    tds.addAttribute(x)
    tds.addAttribute(y)
    # Choose a solver
    solv = Reoptimizer.TNloptCobyla()
    # solv = Reoptimizer.TNloptBobyqa()
    # solv = Reoptimizer.TNloptPraxis()
    # solv = Reoptimizer.TNloptNelderMead()
    # solv = Reoptimizer.TNloptSubplexe()
    # Create the single-objective constrained optimizer
    opt = Reoptimizer.TNlopt(tds, runner, solv)
    # add the objective
    opt.addObjective(sect)
                            # minimizing the section
    # and the constrains
    constrDist = Reoptimizer.TLesserFit(14)
    opt.addConstraint(dist, constrDist)
                                         # distortion (dist < 14)
    positiv = Reoptimizer.TGreaterFit(0.4)
    opt.addConstraint(thick, positiv)
                                       # thickness (thick > 0.4)
    # Starting point
    p1 = np.array([0.9, 0.2])
    p2 = np.array([0.7, 0.1])
    p3 = np.array([0.5, 0.4])
    opt.setStartingPoint(len(p1), p1)
    opt.setStartingPoint(len(p2), p2)
    opt.setStartingPoint(len(p3), p3)
    # Set maximum evaluation
    opt.setMaximumEval(1000)
    opt.solverLoop()
                      # running the optimization
    # Stop the slave processes
    runner.stopSlave()
# solution
```

<!-- page 412 (PDF 419) -->
```python
tds.getTuple().Scan("*", "", "colsize=9 col=:::5:4")
```

As stated previously, the purpose of this macro is to use different starting points for optimisation fully based on the macro
shown in Macro “reoptimizeHollowBarCode.py”. The only difference is highlighted here:

```python
# Starting point
p1 = np.array([0.9, 0.2])
p2 = np.array([0.7, 0.1])
p3 = np.array([0.5, 0.4])
opt.setStartingPoint(len(p1), p1)
opt.setStartingPoint(len(p2), p2)
opt.setStartingPoint(len(p3), p3)
```

The results of this is that optimisation is performed three times, using the three starting points provided. Here it is done
sequentially, but obviously, the main idea is that it is a convenient way to parallelise these optimisation. This could be
done for instance, simply by changing the runner line from

```python
runner = Relauncher.TSequentialRun(code)
```

to, for instance in our case with 3 starting points

```python
runner=Relauncher.TThreadedRun(code,4)
```

####  13.9.2.3 Console

This macro leads to the following result

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
|....:....|....:....|....:....|....:....|....:....0050
|....:....|....:....
|....:....|....:....|....:....0100
|..
..:....|....:....|....:...
***************************************************************************
*
     Row
           * vizirDemo *
                               x.x *
                                           y.y * thick * sect * dist.dist *
***************************************************************************
*
         0 *
                     0 * 0.5173155 * 0.1173213 * 0.399 * 0.25 * 14.000005 *
*
         1 *
                     1 * 0.5173156 * 0.1173173 * 0.399 * 0.25 * 13.999986 *
*
         2 *
                     2 * 0.5173155 * 0.1173155 *
                                                   0.4 * 0.25 *
                                                                       14 *
***************************************************************************
```

###  13.9.3 Macro “reoptimizeHollowBarCodevizir.py”

####  13.9.3.1 Objective

The objective of the macro is to optimize the section and distortion of the hollow bar defined in Sizing of a hollow bar
example problem using the evolutionary solvers. This can be done with different solvers, the one chosen here being the
TVizirGenetic one.

<!-- page 413 (PDF 420) -->
#### 13.9.3.2 Macro Uranie

```python
"""
Example of hollow bar optimisation with Vizir
"""
from URANIE import DataServer, Relauncher, Reoptimizer
import ROOT
# variables
x = DataServer.TAttribute("x", 0.0, 1.0)
y = DataServer.TAttribute("y", 0.0, 1.0)
thick = DataServer.TAttribute("thick")
                                        # thickness
sect = DataServer.TAttribute("sect")
                                      # section of the pipe
dist = DataServer.TAttribute("dist")
                                      # distortion
# Creating TCodeEval, dumping output in an output
python_exec = "python3"
if ROOT.gSystem.GetBuildArch() == "win64":
    python_exec = python_exec[:-1]
code = Relauncher.TCodeEval(python_exec + " bar.py > bartoto.dat")
# Pass the python script as a input. Inputs are modified in bar.py
inputfile = Relauncher.TKeyScript("bar.py")
inputfile.addInput(x, "x")
inputfile.addInput(y, "y")
code.addInputFile(inputfile)
# precise the output file in which to read the three outputs
outputfile = Relauncher.TFlatResult("bartoto.dat")
outputfile.addOutput(thick)
outputfile.addOutput(sect)
outputfile.addOutput(dist)
code.addOutputFile(outputfile)
# Create a runner
runner = Relauncher.TSequentialRun(code)
runner.startSlave()
                     # Usual Relauncher construction
if runner.onMaster():
    # Create the TDS
    tds = DataServer.TDataServer("vizirDemo", "Param de l'opt vizir")
    tds.addAttribute(x)
    tds.addAttribute(y)
    # create the vizir genetic solver
    solv = Reoptimizer.TVizirGenetic()
    # Size of the population and maximum number of evaluation
    solv.setSize(200, 15000)
    # Create the multi-objective constrained optimizer
    opt = Reoptimizer.TVizir2(tds, runner, solv)
```

<!-- page 414 (PDF 421) -->
```python
    # add the objective
    opt.addObjective(sect)
                            # minimizing the section
    opt.addObjective(dist)
                            # minimizing the distortion
    # and the constrains
    positiv = Reoptimizer.TGreaterFit(0.4)
    opt.addConstraint(thick, positiv)
                                       # on thickness (thick > 0.4)
    opt.solverLoop()
                      # running the optimization
    # Stop the slave processes
    runner.stopSlave()
fig1 = ROOT.TCanvas("fig1", "Pareto Zone", 5, 64, 1270, 667)
phi = 12
theta = 30
pad1 = ROOT.TPad("pad1", "", 0, 0.03, 1, 1)
pad2 = ROOT.TPad("pad2", "", 0, 0.03, 1, 1)
pad2.SetFillStyle(4000)
                         # will be transparent
pad1.Draw()
pad1.Divide(2, 1)
pad1.cd(1)
ROOT.gPad.SetPhi(phi)
ROOT.gPad.SetTheta(theta)
ROOT.gStyle.SetLabelSize(0.03)
ROOT.gStyle.SetLabelSize(0.03, "Y")
ROOT.gStyle.SetLabelSize(0.03, "Z")
tds.getTuple().Draw("sect:y:x")
# Get the TH3 to change Z axis color
htemp = ROOT.gPad.GetPrimitive("htemp")
htemp.SetTitle("")
htemp.GetZaxis().SetLabelColor(2)
htemp.GetZaxis().SetAxisColor(2)
htemp.GetZaxis().SetTitleColor(2)
fig1.cd()
pad2.Draw()
pad2.Divide(2, 1)
pad2.cd(1)
ROOT.gPad.SetFillStyle(4000)
ROOT.gPad.SetPhi(phi)
ROOT.gPad.SetTheta(theta)
tds.getTuple().SetMarkerColor(4)
tds.getTuple().Draw("dist:y:x")
htemp = ROOT.gPad.GetPrimitive("htemp")
htemp.SetTitle("")
htemp.GetZaxis().SetLabelColor(4)
htemp.GetZaxis().SetAxisColor(4)
htemp.GetZaxis().SetTitleColor(4)
```

<!-- page 415 (PDF 422) -->
```python
htemp.GetZaxis().SetTickSize(-1*htemp.GetZaxis().GetTickLength())
htemp.GetZaxis().SetLabelOffset(-15*htemp.GetZaxis().GetLabelOffset())
htemp.GetZaxis().LabelsOption("d")
htemp.GetZaxis().SetTitleOffset(-1.5*htemp.GetZaxis().GetTitleOffset())
htemp.GetZaxis().RotateTitle()
pad2.cd(2)
tds.getTuple().SetMarkerColor(2)
tds.draw("dist:sect")
```

The variables are defined as follow:

```python
# variables
x = DataServer.TAttribute("x", 0.0, 1.0)
y = DataServer.TAttribute("y", 0.0, 1.0)
thick = DataServer.TAttribute("thick")
                                        # thickness
sect = DataServer.TAttribute("sect")
                                      # section of the pipe
dist = DataServer.TAttribute("dist")
                                      # distortion
```

where the first two are the input ones while the last ones are computed using the provided code (as explained in Sizing of
a hollow bar example problem). This code is configured through these lines

```python
# Creating TCodeEval, dumping output in an output
code = Relauncher.TCodeEval(python_exec + " bar.py > bartoto.dat")
# Pass the python script as a input. Inputs are modified in bar.py
inputfile = Relauncher.TKeyScript("bar.py")
inputfile.addInput(x, "x")
inputfile.addInput(y, "y")
code.addInputFile(inputfile)
# precise the output file in which to read the three outputs
outputfile = Relauncher.TFlatResult("bartoto.dat")
outputfile.addOutput(thick)
outputfile.addOutput(sect)
outputfile.addOutput(dist)
code.addOutputFile(outputfile)
```

The usual Relauncher construction is followed, using a TSequentialRun runner and the solver is chosen in these lines

```python
# create the vizir genetic solver
solv = Reoptimizer.TVizirGenetic()
# Size of the population and maximum number of evaluation
solv.setSize(200, 15000)
```

Combining the runner, solver and dataserver, the master object is created and the objective and constraint are defined.
This is done in:

```python
# Create the multi-objective constrained optimizer
opt = Reoptimizer.TVizir2(tds, runner, solv)
# add the objective
opt.addObjective(sect)
                        # minimizing the section
```

<!-- page 416 (PDF 423) -->
```python
opt.addObjective(dist)
                        # minimizing the distortion
# and the constrains
positiv = Reoptimizer.TGreaterFit(0.4)
opt.addConstraint(thick, positiv)
                                   # on thickness (thick > 0.4)
```

Finally the optimisation is launched and the rest of code is providing the graphical result shown in next section.

#### 13.9.3.3 Graph

Figure 13.55: Graph of the macro “reoptimizeHollowBarCodeVizir.py”

### 13.9.4 Macro “reoptimizeHollowBarVizirMoead.py”

#### 13.9.4.1 Objective

The objective of the macro is to optimize the section and distortion of the hollow bar defined in Sizing of a hollow bar
example problem using the evolutionary solvers, with a reduce number of points to compose the Pareto set/front. This
example is comparing both the usual Vizir genetic algorithm and the MOEAD implementation that is meant to be a
many-objective criteria algorithm. A short discussion on the many-objective aspect can be found in [Bla17].

#### 13.9.4.2 Macro Uranie

```python
"""
Example of hollow bar optimisation with Moead approach
"""
from array import array
from URANIE import DataServer, Relauncher, Reoptimizer
import ROOT
```

<!-- page 417 (PDF 424) -->
```python
# variables
x = DataServer.TAttribute("x", 0.0, 1.0)
y = DataServer.TAttribute("y", 0.0, 1.0)
thick = DataServer.TAttribute("thick")
                                        # thickness
sect = DataServer.TAttribute("sect")
                                      # section of the pipe
dist = DataServer.TAttribute("dist")
                                      # distortion
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Creating the assessor using the analytical function
code = Relauncher.TCIntEval("barAllCost")
code.addInput(x)
code.addInput(y)
code.addOutput(thick)
code.addOutput(sect)
code.addOutput(dist)
# Create a runner
runner = Relauncher.TSequentialRun(code)
runner.startSlave()
                     # Usual Relauncher construction
NB = 20
nMax = 3000
total = 4*NB
if runner.onMaster():
    # ==================================================
    # ========= Classical Vizir implementation =========
    # ==================================================
    # Create the TDS
    tds_viz = DataServer.TDataServer("vizirDemo", "Vizir parameter dataser")
    tds_viz.addAttribute(x)
    tds_viz.addAttribute(y)
    # create the vizir genetic solver
    solv_viz = Reoptimizer.TVizirGenetic()
    # Size of the population, and a maximum number of evaluation
    solv_viz.setSize(NB, nMax)
    # Create the multi-objective constrained optimizer
    opt_viz = Reoptimizer.TVizir2(tds_viz, runner, solv_viz)
    # add the objective
    opt_viz.addObjective(sect)
                                # minimizing the section
    opt_viz.addObjective(dist)
                                # minimizing the distortion
    # and the constrains
    positiv = Reoptimizer.TGreaterFit(0.4)
    opt_viz.addConstraint(thick, positiv)
                                           # on thickness (thick > 0.4)
    opt_viz.solverLoop()
                          # running the optimization
    # ==================================================
```

<!-- page 418 (PDF 425) -->
```python
# ============== MOEAD implementation ==============
# ==================================================
# Create the TDS
tds_moead = DataServer.TDataServer("vizirDemo", "Vizir parameter dataser")
tds_moead.addAttribute(x)
tds_moead.addAttribute(y)
# create the vizir genetic solver
solv_moead = Reoptimizer.TVizirGenetic()
solv_moead.setMoeadDiversity(NB)
solv_moead.setStoppingCriteria(1)
solv_moead.setSize(0, nMax)
# Create the multi-objective constrained optimizer
opt_moead = Reoptimizer.TVizir2(tds_moead, runner, solv_moead)
# add the objective
opt_moead.addObjective(sect)
                              # minimizing the section
opt_moead.addObjective(dist)
                              # minimizing the distortion
opt_moead.addConstraint(thick, positiv)
                                          # on thickness (thick > 0.4)
opt_moead.solverLoop()
                        # running the optimization
# Stop the slave processes
runner.stopSlave()
# Start the graphical part
# Preparing canvas
fig1 = ROOT.TCanvas("fig1", "Pareto Zone", 5, 64, 1270, 667)
pad1 = ROOT.TPad("pad1", "", 0, 0.03, 1, 1)
pad1.Draw()
pad1.Divide(2, 1)
pad1.cd(1)
# extracting data to construct graphs
viz = array('d', [0. for i in range(total)])
# There is always one more point in moead
moe = array('d', [0. for i in range(total+4)])
tds_viz.getTuple().extractData(viz, total, "x:y:sect:dist", "", "column")
tds_moead.getTuple().extractData(moe, total+4,
                                 "x:y:sect:dist", "", "column")
set_viz = ROOT.TGraph(NB, array('d', [viz[i] for i in range(NB)]),
                      array('d', [viz[NB+i] for i in range(NB)]))
fr_viz = ROOT.TGraph(NB, array('d', [viz[2*NB+i] for i in range(NB)]),
                     array('d', [viz[3*NB+i] for i in range(NB)]))
set_viz.SetMarkerColor(4)
set_viz.SetMarkerStyle(20)
set_viz.SetMarkerSize(0.8)
fr_viz.SetMarkerColor(4)
```

<!-- page 419 (PDF 426) -->
```python
fr_viz.SetMarkerStyle(20)
fr_viz.SetMarkerSize(0.8)
set_moe = ROOT.TGraph(NB+1, array('d', [moe[i] for i in range(NB+1)]),
                      array('d', [moe[NB+1+i] for i in range(NB+1)]))
fr_moe = ROOT.TGraph(NB, array('d', [moe[2*(NB+1)+i] for i in range(NB+1)]),
                     array('d', [moe[3*(NB+1)+i] for i in range(NB+1)]))
set_moe.SetMarkerColor(2)
set_moe.SetMarkerStyle(20)
set_moe.SetMarkerSize(0.8)
fr_moe.SetMarkerColor(2)
fr_moe.SetMarkerStyle(20)
fr_moe.SetMarkerSize(0.8)
# Legend
ROOT.gStyle.SetLegendBorderSize(0)
leg = ROOT.TLegend(0.25, 0.75, 0.55, 0.89)
leg.AddEntry(set_viz, "Vizir algo", "p")
leg.AddEntry(set_moe, "MOEAD algo", "p")
# Pareto Set
set_mg = ROOT.TMultiGraph()
set_mg.Add(set_viz)
set_mg.Add(set_moe)
set_mg.Draw("aP")
set_mg.SetTitle("Pareto Set")
set_mg.GetXaxis().SetTitle("x")
set_mg.GetYaxis().SetTitle("y")
leg.Draw()
ROOT.gPad.Update()
# Pareto Front
pad1.cd(2)
fr_mg = ROOT.TMultiGraph()
fr_mg.Add(fr_viz)
fr_mg.Add(fr_moe)
fr_mg.Draw("aP")
fr_mg.SetTitle("Pareto front")
fr_mg.GetXaxis().SetTitle("Section")
fr_mg.GetYaxis().SetTitle("Distortion")
leg.Draw()
ROOT.gPad.Update()
```

The variables are defined as follow:

```python
x = DataServer.TAttribute("x", 0.0, 1.0)
y = DataServer.TAttribute("y", 0.0, 1.0)
thick = DataServer.TAttribute("thick")
                                        # thickness
sect = DataServer.TAttribute("sect")
                                      # section of the pipe
dist = DataServer.TAttribute("dist")
                                      # distortion
```

where the first two are the input ones while the last ones are computed using the provided code (as explained in Sizing of
a hollow bar example problem). This code is configured through these lines

<!-- page 420 (PDF 427) -->
```python
# Creating the assessor using the analytical function
code = Relauncher.TCIntEval("barAllCost")
code.addInput(x)
code.addInput(y)
code.addOutput(thick)
code.addOutput(sect)
code.addOutput(dist)
```

The usual Relauncher construction is followed, using a TSequentialRun runner. The first solver is defined in these lines

```python
# create the vizir genetic solver
solv_viz = Reoptimizer.TVizirGenetic()
# Size of the population, and a maximum number of evaluation
solv_viz.setSize(NB, nMax)
```

Combining the runner, solver and dataserver, the master object is created and the objective and constraint are defined.
This is done in:

```python
# Create the multi-objective constrained optimizer
opt_viz = Reoptimizer.TVizir2(tds_viz, runner, solv_viz)
# add the objective
opt_viz.addObjective(sect)
                            # minimizing the section
opt_viz.addObjective(dist)
                            # minimizing the distortion
# and the constrains
positiv = Reoptimizer.TGreaterFit(0.4)
opt_viz.addConstraint(thick, positiv)
                                       # on thickness (thick > 0.4)
```

In a second block a new dataserver is created along with a new genetic solver in these lines:

```python
# create the vizir genetic solver
solv_moead = Reoptimizer.TVizirGenetic()
solv_moead.setMoeadDiversity(NB)
solv_moead.setStoppingCriteria(1)
solv_moead.setSize(0, nMax)
```

The idea here is to use the Moead algorithm whose principle in few words is to split the space into a certain numbers of
direction intervals (set by the argument in the function setMoeadDiversity). This should provide a Pareto front with
a better homogeneity in the front member distribution (particularly visible here when the size of the requested ensemble
is small). The second method, setStoppingCriteria(1) states that the only stopping criteria available is the total
number of estimation, allowed in the setSize method. Finally, the last function to be called is the setSize one, with
a peculiar first argument here: the size of the pareto can be chosen but if 0 is put (as done here) the number of elements
will be the number of intervals defined previously plus one (the plus one comes from the fact that the elements are created
at the edge of every interval, so for 20 intervals, there are 21 edges in total).
The rest of the code is creating the plot shown below in which both Pareto set and front are compared.

<!-- page 421 (PDF 428) -->
#### 13.9.4.3 Graph

Figure 13.56: Graph of the macro “reoptimizeHollowBarVizirMoead.py”

### 13.9.5 Macro “reoptimizeHollowBarVizirSplitRuns.py”

#### 13.9.5.1 Objective

The objective of the macro is to be able to run an evolutionary algorithm (here we are using a genetic one) with a limited
number of code estimation and restart it from where it stopped if it has not converged the first time. This is of utmost
usefulness when running a resource-consumming code or (/and) when running on a cluster with a limited number of cpu
time. The classical hollow bar example defined in Sizing of a hollow bar example problem is used to obtain a nice Pareto
set/front.

#### 13.9.5.2 Macro Uranie

```python
"""
Example of hollow bar optimisation in split runs
"""
from URANIE import DataServer, Relauncher, Reoptimizer
import ROOT
TOLERANCE = 0.001
NBmaxEVAL = 1200
SIZE = 500
def launch_vizir(run_number, fig_one):
    """Factorised function to run the Vizir analaysis."""
    # variables
    xvar = DataServer.TAttribute("x", 0.0, 1.0)
    yvar = DataServer.TAttribute("y", 0.0, 1.0)
```

<!-- page 422 (PDF 429) -->
```python
thick = DataServer.TAttribute("thick")
sect = DataServer.TAttribute("sect")
defor = DataServer.TAttribute("defor")
code = Relauncher.TCIntEval("barAllCost")
code.addInput(xvar)
code.addInput(yvar)
code.addOutput(thick)
code.addOutput(sect)
code.addOutput(defor)
# Create a runner
runner = Relauncher.TSequentialRun(code)
runner.startSlave()
# Output to state whether convergence is reached
has_converged = False
if runner.onMaster():
    # Create the TDS
    tds = DataServer.TDataServer("vizirDemo", "Param de l'opt vizir")
    tds.addAttribute(xvar)
    tds.addAttribute(yvar)
    solv = Reoptimizer.TVizirGenetic()
    # Name of the file that will contain
    filename = "genetic.dump"
    # whether = Test if a genetic.dump exists. If not, it creates it
    # and returns false, so that the "else" part is done to start the
    # initialisation of the vizir algorithm.
    if solv.setResume(NBmaxEVAL, filename):
        print("Restarting Vizir")
    else:
        solv.setSize(SIZE, NBmaxEVAL)
    # Create the multi-objective constrained optimizer
    opt = Reoptimizer.TVizir2(tds, runner, solv)
    opt.setTolerance(TOLERANCE)
    # add the objective
    opt.addObjective(sect)
    opt.addObjective(defor)
    positiv = Reoptimizer.TGreaterFit(0.4)
    opt.addConstraint(thick, positiv)
    # resolution
    opt.solverLoop()
    has_converged = opt.isConverged()
    # Stop the slave processes
    runner.stopSlave()
    fig_one.cd(run_number+1)
    tds.getTuple().SetMarkerColor(2)
```

<!-- page 423 (PDF 430) -->
```python
        tds.draw("defor:sect")
        tit = "Run number "+str(run_number+1)
        if has_converged:
            tit += ": Converged !"
        ROOT.gPad.GetPrimitive("__tdshisto__0").SetTitle(tit)
    return has_converged
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Delete previous file if it exists
ROOT.gSystem.Unlink("genetic.dump")
finished = False
i = 0
fig1 = ROOT.TCanvas("fig1", "fig1", 1200, 800)
fig1.Divide(2, 2)
while not finished:
    finished = launch_vizir(i, fig1)
    i = i+1
```

The idea is to show how to run this kind of configuration: the function LaunchVizir is the usual script one can run to
get an optimisation with Vizir on the hollow bar problem. The aim is to create a Pareto set of 500 points (SIZE) but only
allowing 1200 estimation (NBmaxEVAL). With this configuration we are sure that a first round of estimation will not
converge, so we will have to restart the optimisation from the point we stopped. With this regard, the beginning of this
function is trivial and the main point to be discussed arises once the solver is created.

```python
solv = Reoptimizer.TVizirGenetic()
# Name of the file that will contain
filename = "genetic.dump"
# whether = Test if a genetic.dump exists. If not, it creates it
# and returns false, so that the "else" part is done to start the
# initialisation of the vizir algorithm.
if solv.setResume(NBmaxEVAL, filename):
    print("Restarting Vizir")
else:
    solv.setSize(SIZE, NBmaxEVAL)
```

Clearly here, the interesting part apart, from the definition of the name of the file in which the final state will be kept,
is the first test on the solver, before using the setSize method. A new methods called setResume is called, with two
arguments : the number of elements requested in the Pareto set and the name of the file in which to save the state or to
restart from. This method returns “true” if genetic.dump is found and “false” if not. In the first case, the code will
assume that this file is the result of a previous run and it will start the optimisation from the its content trying to get all
the population non-dominated (if it’s not yet the case). If, on the other hand, no file is found, then the code knows that
it would have to store the results of its process, in a file whose name is the second argument, and because the function
returns “false”, then we move to the “else” part, that starts the optimisation.
Apart from this, the rest of the function is doing the optimisation, and plotting the pareto front in a provided canvas. The
only new part here is the fact that the solver (its master in fact) is now able to tell whether it has converged or not through
the following method

```python
has_converged = opt.isConverged()
```

this argument being return as the results of the function.
