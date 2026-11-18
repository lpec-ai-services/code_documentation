# Use-cases in Python — Macros Relauncher — Macro “relauncherFunctionFlowrateCInt.py” … Macro “relauncherCodeFlowrateMPI.py”
<!-- source PDF pages 372-387 -->

<!-- page 365 (PDF 372) -->
```python
lkrig[im] = Relauncher.TLauncher2(tdsEstim[im], kg[im], "x1",
                                  "yEstim:vEstim")
lkrig[im].solverLoop()
```

####  13.7.14.3 Graph

Figure 13.45: Graph of the macro “modelerTestKriging.py”

## 13.8 Macros Relauncher

The idea of this section is to show the basic usage of many of the classes defined in The Relauncher module, applied
either on the flowrate functions or the flowrate code, whose purpose and behaviour have been already introduced in
Presentation of the problem. All the following examples will load a tiny set of points which is gathered in the file called
flowrateUniformDesign.dat (already introduced in Objective).

### 13.8.1 Macro “relauncherFunctionFlowrateCInt.py”

#### 13.8.1.1 Objective

The goal of this macro is to show how to handle (in the most simple way) a C++-written function, compliant with the
ROOT (CINT) format. This function has been presented, at least its equation (see Equation 4.1) and would be interfaced
through the TCIntEval class in the Relauncher module (which means that we’ll use the function database from ROOT’s
catalog, see Important modifications going from ROOT v5 to ROOT v6 for more explanations). As this class is usually
considered not thread-safe, it can only be used with a TSequentialRun runner.

#### 13.8.1.2 Macro

```python
"""
Example of function launching in sequential mode
"""
from URANIE import DataServer, Relauncher
import ROOT
```

<!-- page 366 (PDF 373) -->
```python
# Create the DataServer.TDataServer
tds = DataServer.TDataServer("foo", "test")
tds.fileDataRead("flowrateUniformDesign.dat")
# Get the attributes
rw = tds.getAttribute("rw")
r = tds.getAttribute("r")
tu = tds.getAttribute("tu")
tl = tds.getAttribute("tl")
hu = tds.getAttribute("hu")
hl = tds.getAttribute("hl")
lvar = tds.getAttribute("l")
kw = tds.getAttribute("kw")
# Create the output attribute
yhat = DataServer.TAttribute("yhat")
# Constructing the code
ROOT.gROOT.LoadMacro("UserFunctions.C")
mycode = Relauncher.TCIntEval("flowrateModel")
mycode.addInput(rw)
mycode.addInput(r)
mycode.addInput(tu)
mycode.addInput(tl)
mycode.addInput(hu)
mycode.addInput(hl)
mycode.addInput(lvar)
mycode.addInput(kw) # Adding the input attributes
mycode.addOutput(yhat)
                        # Adding the output attributes
# Create the sequential runner
run = Relauncher.TSequentialRun(mycode)
run.startSlave()
                  # Start the master (necessary even for a sequential)
if run.onMaster():
    lanceur = Relauncher.TLauncher2(tds, run)
    # resolution
    lanceur.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
# Draw the result
can = ROOT.TCanvas("pouet", "foo", 1)
tds.Draw("yhat:rw", "", "colZ")
```

The first part of the macro is the definition of the flowrateModel function, already discussed throughout this documentation
. The dataserver object is then created and filled using the database file and pointers to the corresponding input
attributes are created, along with the new attribute for the output provided by the function. The following part is then
specific to the Relauncher organisation: a TCIntEval object is created with the function as only argument. Both the
input and output attributes are provided (here in a contracted way for input, but it could have been done one-by-one, as
for output).

<!-- page 367 (PDF 374) -->
```python
# Constructing the code
mycode = Relauncher.TCIntEval("flowrateModel")
mycode.addInput(rw)
mycode.addInput(r)
mycode.addInput(tu)
mycode.addInput(tl)
mycode.addInput(hu)
mycode.addInput(hl)
mycode.addInput(lvar)
mycode.addInput(kw) # Adding the input attributes
mycode.addOutput(yhat)
                        # Adding the output attributes
```

The methods setInputs and setOutputs are not allowed in python, so attributes has to be added one-by-one.
The following part is the heart of the relauncher strategy: the assessor is provided to the chosen runner, which should
always start the slaves (even in the case of a sequential one like here). On the main CPU, the master is created as well
(with the dataserver and the runner) and the resolution is requested.

```python
# Create the sequential runner
run = Relauncher.TSequentialRun(mycode)
run.startSlave()
                  # Start the master (necessary even for a sequential)
if run.onMaster():
    lanceur = Relauncher.TLauncher2(tds, run)
    # resolution
    lanceur.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
```

Once this is done, the slaves are stopped and the results is displayed for cross-check in the following subsection.

#### 13.8.1.3 Graph

Figure 13.46: Representation of the output as a function of the first input with a colZ option

<!-- page 368 (PDF 375) -->
### 13.8.2 Macro “relauncherFunctionFlowratePython.py”

#### 13.8.2.1 Objective

The goal of this macro is to show how to handle the Python-written function in a full python-script. This function has
been presented, at least its equation (see Equation 4.1) and would be interface through the TPythonEval class in the
Relauncher module.

#### 13.8.2.2 Macro

```python
"""
Example of python function launching
"""
import math
from URANIE import DataServer, Relauncher
import ROOT
def flowrate_model(drw, drvar, dtu, dtl, dhu, dhl, dlvar, dkw):
    """Simple flowrate model python function."""
    dnum = 2.0 * math.pi * dtu * (dhu - dhl)
    dlnronrw = math.log(drvar / drw)
    dden = dlnronrw * (1.0 + (2.0 * dlvar * dtu) / (dlnronrw * drw * drw * dkw)
                       + dtu / dtl)
    return [dnum / dden, ]
# Create the TDataServer
tds = DataServer.TDataServer("foo", "test")
tds.fileDataRead("flowrateUniformDesign.dat")
# Get the attributes
rw = tds.getAttribute("rw")
r = tds.getAttribute("r")
tu = tds.getAttribute("tu")
tl = tds.getAttribute("tl")
hu = tds.getAttribute("hu")
hl = tds.getAttribute("hl")
lvar = tds.getAttribute("l")
kw = tds.getAttribute("kw")
# Create the output attribute
yhat = DataServer.TAttribute("yhat")
# Constructing the code
mycode = Relauncher.TPythonEval(flowrate_model)
# Adding the input file
mycode.addInput(rw)
mycode.addInput(r)
mycode.addInput(tu)
mycode.addInput(tl)
mycode.addInput(hu)
mycode.addInput(hl)
mycode.addInput(lvar)
```

<!-- page 369 (PDF 376) -->
```python
mycode.addInput(kw)
# Adding the output file
mycode.addOutput(yhat)
# Create the sequential runner
run = Relauncher.TSequentialRun(mycode)
run.startSlave()
                  # Start the master (necessary even for a sequential)
if run.onMaster():
    launch = Relauncher.TLauncher2(tds, run)
    # resolution
    launch.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
# Draw the result
can = ROOT.TCanvas("pouet", "foo", 1)
tds.Draw("yhat:rw", "", "colZ")
```

Obviously the code is now different from the other macros already introduced, but unless some python-specificity, the
discussion has been largely done in Macro.
The first interesting part is the definition of the function flowrateModel. It is a classical python-function, for which
every input is either a double, a list (for vectors) or a string. Disregarding the inner part, where the computation is done,
the other interesting part is the return line: it should always be a list of all the objects that should be returned.

```python
def flowrate_model(drw, drvar, dtu, dtl, dhu, dhl, dlvar, dkw):
    """Simple flowrate model python function."""
    dnum = 2.0 * math.pi * dtu * (dhu - dhl)
    dlnronrw = math.log(drvar / drw)
    dden = dlnronrw * (1.0 + (2.0 * dlvar * dtu) / (dlnronrw * drw * drw * dkw)
                       + dtu / dtl)
    return [dnum / dden, ]
```

Apart from this, the only other difference is the assessor construction which is an instance of the TPythonEval class as
shown here:

```python
# Constructing the code
mycode = Relauncher.TPythonEval(flowrate_model)
```

The macro is also leading to the creation of the following plot.

<!-- page 370 (PDF 377) -->
#### 13.8.2.3 Graph

Figure 13.47: Representation of the output as a function of the first input with a colZ option

### 13.8.3 Macro “relauncherCodeFlowrateSequential.py”

#### 13.8.3.1 Objective

The goal of this macro is to show how to handle a code with a sequential runner. The flowrate code is provided with
Uranie and has been also used and discussed throughout these macros.

#### 13.8.3.2 Macro

```python
"""
Example of code launching in sequential mode
"""
from URANIE import DataServer, Relauncher
import ROOT
# Create the DataServer.TDataServer
tds = DataServer.TDataServer("foo", "test")
tds.fileDataRead("flowrateUniformDesign.dat")
# Get the attributes
rw = tds.getAttribute("rw")
r = tds.getAttribute("r")
tu = tds.getAttribute("tu")
tl = tds.getAttribute("tl")
hu = tds.getAttribute("hu")
hl = tds.getAttribute("hl")
lvar = tds.getAttribute("l")
kw = tds.getAttribute("kw")
# Create the output attribute
```

<!-- page 371 (PDF 378) -->
```python
yhat = DataServer.TAttribute("yhat")
d = DataServer.TAttribute("d")
# Set the reference input file and the key for each input attributes
fin = Relauncher.TFlatScript("flowrate_input_with_values_rows.in")
fin.addInput(rw)
fin.addInput(r)
fin.addInput(tu)
fin.addInput(tl)
fin.addInput(hu)
fin.addInput(hl)
fin.addInput(lvar)
fin.addInput(kw)
# The output file of the code
fout = Relauncher.TFlatResult("_output_flowrate_withRow_.dat")
fout.addOutput(yhat)
fout.addOutput(d)
                   # Passing the attributes to the output file
# Constructing the code
mycode = Relauncher.TCodeEval("flowrate -s -r")
mycode.setOldTmpDir()
mycode.addInputFile(fin)
                          # Adding the input file
mycode.addOutputFile(fout)
                            # Adding the output file
# Create the sequential runner
run = Relauncher.TSequentialRun(mycode)
run.startSlave()
                  # Start the master (necessary even for a sequential)
if run.onMaster():
    lanceur = Relauncher.TLauncher2(tds, run)
    # resolution
    lanceur.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
# Draw the result
can = ROOT.TCanvas("pouet", "foo", 1)
tds.Draw("yhat:rw", "", "colZ")
```

Here again, a comparison is drawn with the first Relauncher macro (see Macro) and only the differences are pointed
out. The first obvious one, in the very first steps in defining the dataserver and the attributes, is that there are two output
attributes. The second one (called ‘d’) will not be used here. The second (and only other difference) with respect to the
CINT function code, is the assessor creation shown below:

```python
# Set the reference input file and the key for each input attributes
fin = Relauncher.TFlatScript("flowrate_input_with_values_rows.in")
fin.addInput(rw)
fin.addInput(r)
fin.addInput(tu)
fin.addInput(tl)
fin.addInput(hu)
```

<!-- page 372 (PDF 379) -->
```python
fin.addInput(hl)
fin.addInput(lvar)
fin.addInput(kw)
# The output file of the code
fout = Relauncher.TFlatResult("_output_flowrate_withRow_.dat")
fout.addOutput(yhat)
fout.addOutput(d)
                   # Passing the attributes to the output file
# Constructing the code
mycode = Relauncher.TCodeEval("flowrate -s -r")
mycode.setOldTmpDir()
mycode.addInputFile(fin)
                          # Adding the input file
mycode.addOutputFile(fout)
                            # Adding the output file
```

The first three lines create the input file instance. It is here a TFlatScript object which can basically be compared to
a DataServer (or Salome-table) format of the Launcher module for its organisation (particularly with vectors and strings)
but without the compulsory header: the order in which you introduce the attribute is then of uttermost importance. The
second block of lines is creating the output file object from the TFlatResult class (the same remark applies to this
object).
Finally the assessor itself is created as an instance of the TCodeEval class. The only argument is the command to be run,
and it needs at least one input and output file. Apart from that, the runner is created and the rest is crystal clear, leading
to the following plot.

#### 13.8.3.3 Graph

Figure 13.48: Representation of the output as a function of the first input with a colZ option

<!-- page 373 (PDF 380) -->
### 13.8.4 Macro “relauncherCodeFlowrateSequential_ConstantVar.py”

#### 13.8.4.1 Objective

The goal of this macro is to show how to set one of the evaluator’s input attribute to a constant value, with a sequential
runner. The flowrate code is provided with Uranie and has been also used and discussed throughout these macros.

#### 13.8.4.2 Macro

```python
"""
Example of code launching in sequential mode with constant variable
"""
from URANIE import DataServer, Relauncher, Sampler
# Create the TDataServer
tds = DataServer.TDataServer("foo", "test")
# Define the attribute that should be considered as constant
r = DataServer.TAttribute("r")
# Add the study attributes (min, max and nominal values)
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
# The reference input file
sIn = "flowrate_input_with_keys.in"
nS = 15
# Generate the Design of Experiments
sampling = Sampler.TSampling(tds, "lhs", nS)
sampling.generateSample()
# Create the input files
inputFile = Relauncher.TKeyScript(sIn)
inputFile.addInput(tds.getAttribute("rw"), "Rw")
inputFile.addInput(r, "R")
                            # Add the constant attribute as an input
inputFile.addInput(tds.getAttribute("tu"), "Tu")
inputFile.addInput(tds.getAttribute("tl"), "Tl")
inputFile.addInput(tds.getAttribute("hu"), "Hu")
inputFile.addInput(tds.getAttribute("hl"), "Hl")
inputFile.addInput(tds.getAttribute("l"), "L")
inputFile.addInput(tds.getAttribute("kw"), "Kw")
# Create the output attribute
yhat = DataServer.TAttribute("yhat")
d = DataServer.TAttribute("d")
# Create the output files
outputFile = Relauncher.TKeyResult("_output_flowrate_withKey_.dat")
```

<!-- page 374 (PDF 381) -->
```python
outputFile.addOutput(yhat, "yhat")
outputFile.addOutput(d, "d")
# Create the user's evaluation function
myeval = Relauncher.TCodeEval("flowrate -s -k")
myeval.addInputFile(inputFile)
myeval.addOutputFile(outputFile)
# Create the sequential runner
run = Relauncher.TSequentialRun(myeval)
run.startSlave()
                  # Start the master (necessary even for a sequential)
if run.onMaster():
    lanceur = Relauncher.TLauncher2(tds, run)
    # State to the master : r is constant with value 108
    # By default the value is not kept in the tds.
    # The third argument says : yes, keep it for bookkeeping
    lanceur.addConstantValue(r, 108, True)
    # resolution
    lanceur.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
tds.scan("*","","colsize=6")
```

Here again, a comparison is drawn with the first Relauncher macro (see Macro) and only the differences are pointed
out. The first obvious one, in the very first steps in defining the dataserver and the attributes, is that instead of reading
a database-file, we are generating a design-of-experiments with one big specificity: all the input attributes are properly
defined, but r.

```python
# Define the attribute that should be considered as constant
r = DataServer.TAttribute("r")
# Add the study attributes (min, max and nominal values)
tds.addAttribute(DataServer.TUniformDistribution("rw", 0.05, 0.15))
tds.addAttribute(DataServer.TUniformDistribution("tu", 63070.0, 115600.0))
tds.addAttribute(DataServer.TUniformDistribution("tl", 63.1, 116.0))
tds.addAttribute(DataServer.TUniformDistribution("hu", 990.0, 1110.0))
tds.addAttribute(DataServer.TUniformDistribution("hl", 700.0, 820.0))
tds.addAttribute(DataServer.TUniformDistribution("l", 1120.0, 1680.0))
tds.addAttribute(DataServer.TUniformDistribution("kw", 9855.0, 12045.0))
```

A simple design-of-experiments is generated and all the input attributes are provided to the input file of the assessor,
event the constant one r.

```python
# Create the input files
inputFile = Relauncher.TKeyScript(sIn)
inputFile.addInput(tds.getAttribute("rw"), "Rw")
inputFile.addInput(r, "R")
                            # Add the constant attribute as an input
inputFile.addInput(tds.getAttribute("tu"), "Tu")
inputFile.addInput(tds.getAttribute("tl"), "Tl")
inputFile.addInput(tds.getAttribute("hu"), "Hu")
```

<!-- page 375 (PDF 382) -->
```python
inputFile.addInput(tds.getAttribute("hl"), "Hl")
inputFile.addInput(tds.getAttribute("l"), "L")
inputFile.addInput(tds.getAttribute("kw"), "Kw")
```

The rest is fairly common, up to the TMaster-inheriting object specification: the addConstantValue method is called
to specify that r is about to be constant for all ongoing estimation, and it provides it value. The last argument states that
the value under consideration should be stored in the ntuple of the dataserver object, as shown in the next section (from
the scan method).

```python
lanceur = Relauncher.TLauncher2(tds, run)
# State to the master : r is constant with value 108
# By default the value is not kept in the tds.
# The third argument says : yes, keep it for bookkeeping
lanceur.addConstantValue(r, 108, True)
```

<!-- page 376 (PDF 383) -->
#### 13.8.4.3 Console

```python
***************************************************************************************************************
 *
    Row
 * foo__n *
       rw.rw *
       tu.tu *
       tl.tl *
       hu.hu *
       hl.hl *
    l.l *
       kw.kw * yhat.y *
    d.d *
    r.r *
                                                                                                                                                                                                                                                                                                        ***************************************************************************************************************
    *
    0 *
    0 * 0.1495 * 111790 * 73.820 * 990.90 * 779.83 * 1474.3 * 11220. * 112.01 * 3588.9 *
            108 *
     *
     1 *
     1 * 0.1394 * 104140 * 95.150 * 1101.5 * 707.21 * 1422.7 * 11493. * 193.62 * 6597.5 *
                108 *
       *
       2 *
       2 * 0.0557 * 95387. * 84.809 * 1056.2 * 752.94 * 1184.6 * 11967. * 29.880 * 330.58 *
                    108 *
        *
        3 *
        3 * 0.0836 * 74144. * 103.17 * 1051.6 * 819.27 * 1587.4 * 11031. * 35.400 * 2431.1 *
                        108 *
         *
         4 *
         4 * 0.0586 * 65396. * 72.161 * 1003.1 * 710.34 * 1327.5 * 10484. * 24.990 *
                                     5757 *
                            108 *
           *
           5 *
           5 * 0.1203 * 92149. * 65.263 * 1031.6 * 797.34 * 1265.5 * 11638. * 97.386 * 1084.8 *
                                108 *
            *
            6 *
            6 * 0.1319 * 67464. * 93.378 * 1039.4 * 722.54 * 1514.3 * 10996. * 125.33 * 2362.4 *
                                    108 *
             *
             7 *
             7 * 0.1059 * 80448. * 112.87 * 1027.1 * 794.32 * 1555.4 *
                                                                   11846 * 62.403 * 1116.3 *
                                        108 *
               *
               8 *
               8 * 0.0784 * 100260 * 105.79 * 1072.7 * 767.70 * 1304.1 * 10152. * 45.867 * 521.41 *
                                            108 *
                *
                9 *
                9 * 0.0697 * 105158 * 82.544 * 1020.4 * 726.05 * 1640.3 * 10380. * 28.412 * 2802.5 *
                                                108 *
                 *
                                   10 *
                                   10 * 0.1252 * 89522. * 100.65 * 1006.2 * 742.35 * 1123.9 * 10743. * 123.70 * 2676.1 *
                                                    108 *
                   *
                                     11 *
                                     11 * 0.1165 * 73139. * 69.083 * 1108.5 * 809.59 * 1199.0 * 10620. * 112.27 * 4991.3 *
                                                        108 *
                    *
                                        12 *
                                        12 * 0.0992 * 86004. * 112.12 * 1069.4 * 763.84 * 1345.2 * 9951.0 * 69.808 * 414.71 *
                                                            108 *
                     *
                                           13 *
                                           13 * 0.0718 * 113775 * 90.580 * 1079.1 * 782.95 * 1416.6 * 10076. * 34.135 * 1016.8 *
                                                                108 *
                       *
                                             14 *
                                             14 * 0.0902 * 83779. * 80.244 * 1090.6 * 734.33 * 1644.2 *
                                                                                                                 11443 * 63.236 * 2922.3 *
                                                                    108 *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ***************************************************************************************************************
```

<!-- page 377 (PDF 384) -->
### 13.8.5 Macro “relauncherCodeFlowrateThreaded.py”

#### 13.8.5.1 Objective

The goal of this macro is to show how to handle a code run on several threads. In order to this, the usual sequential runner
will be removed and another runner will be called to do the job. The flowrate code is provided with Uranie and has
been also used and discussed throughout these macros.

#### 13.8.5.2 Macro

```python
"""
Example of code launching in threaded mode
"""
from URANIE import DataServer, Relauncher
import ROOT
# Create input attributes
rw = DataServer.TAttribute("rw")
r = DataServer.TAttribute("r")
tu = DataServer.TAttribute("tu")
tl = DataServer.TAttribute("tl")
hu = DataServer.TAttribute("hu")
hl = DataServer.TAttribute("hl")
lvar = DataServer.TAttribute("l")
kw = DataServer.TAttribute("kw")
# Create the output attribute
yhat = DataServer.TAttribute("yhat")
d = DataServer.TAttribute("d")
# Set the reference input file and the key for each input attributes
fin = Relauncher.TFlatScript("flowrate_input_with_values_rows.in")
fin.addInput(rw)
fin.addInput(r)
fin.addInput(tu)
fin.addInput(tl)
fin.addInput(hu)
fin.addInput(hl)
fin.addInput(lvar)
fin.addInput(kw)
# The output file of the code
fout = Relauncher.TFlatResult("_output_flowrate_withRow_.dat")
fout.addOutput(yhat)
fout.addOutput(d)
                   # Passing the attributes to the output file
# Constructing the code
mycode = Relauncher.TCodeEval("flowrate -s -r")
mycode.setOldTmpDir()
mycode.addInputFile(fin)
                          # Adding the input file
mycode.addOutputFile(fout)
                            # Adding the output file
# Fix the number of threads
nthread = 3
# Create the Threaded runner
```

<!-- page 378 (PDF 385) -->
```python
run = Relauncher.TThreadedRun(mycode, nthread)
run.startSlave()
                  # Start the master
if run.onMaster():
    # Define the DataServer
    tds = DataServer.TDataServer("tdsflowrate", "Design of Experiments")
    mycode.addAllInputs(tds)
    tds.fileDataRead("flowrateUniformDesign.dat", False, True)
    lanceur = Relauncher.TLauncher2(tds, run)
    # resolution
    lanceur.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
    # Draw the result
    can = ROOT.TCanvas("pouet", "foo", 1)
    tds.Draw("yhat:rw", "", "colZ")
```

The only difference when comparing this macro to the previous one (see Macro) is the runner creation:

```python
# Fix the number of threads
nthread = 3
# Create the Threaded runner
run = Relauncher.TThreadedRun(mycode, nthread)
```

The TSequentialRun object becomes a TThreadedRun object whose construction request on top of the assessor, the
number of threads to be used. Apart from that, the master is created and the rest is crystal clear, leading to the following
plot.

#### 13.8.5.3 Graph

Figure 13.49: Representation of the output as a function of the first input with a colZ option

<!-- page 379 (PDF 386) -->
### 13.8.6 Macro “relauncherCodeFlowrateMPI.py”

#### 13.8.6.1 Objective

The goal of this macro is to show how to handle a code run on several threads with another memory paradigm: when the
TThreadedRun instance is relying on shared memory (leading to possible thread-safe problem, as discussed in TThreaded
Run), the MPI implementation is based on the separation of the memory. The communication is made through messages
. In order to this, the usual sequential runner will be removed and another runner will be called to do the job. The
flowrate code is provided with Uranie and has been also used and discussed throughout these macros.

#### 13.8.6.2 Macro

```python
"""
Example of MPi usage for code launching
"""
from URANIE import DataServer, Relauncher, MpiRelauncher
import ROOT
# Create input attributes
rw = DataServer.TAttribute("rw")
r = DataServer.TAttribute("r")
tu = DataServer.TAttribute("tu")
tl = DataServer.TAttribute("tl")
hu = DataServer.TAttribute("hu")
hl = DataServer.TAttribute("hl")
lvar = DataServer.TAttribute("l")
kw = DataServer.TAttribute("kw")
# Create the output attribute
yhat = DataServer.TAttribute("yhat")
d = DataServer.TAttribute("d")
# Set the reference input file and the key for each input attributes
fin = Relauncher.TFlatScript("flowrate_input_with_values_rows.in")
fin.addInput(rw)
fin.addInput(r)
fin.addInput(tu)
fin.addInput(tl)
fin.addInput(hu)
fin.addInput(hl)
fin.addInput(lvar)
fin.addInput(kw)
# The output file of the code
fout = Relauncher.TFlatResult("_output_flowrate_withRow_.dat")
fout.addOutput(yhat)
fout.addOutput(d)
                   # Passing the attributes to the output file
# Instanciation de mon code
mycode = Relauncher.TCodeEval("flowrate -s -r")
# mycode.setOldTmpDir()
mycode.addInputFile(fin)
mycode.addOutputFile(fout)
```

<!-- page 380 (PDF 387) -->
```python
# Create the MPI runner
run = MpiRelauncher.TMpiRun(mycode)
run.startSlave()
if run.onMaster():
    # Define the DataServer
    tds = DataServer.TDataServer("tdsflowrate",
                                 "Design of Experiments for Flowrate")
    mycode.addAllInputs(tds)
    tds.fileDataRead("flowrateUniformDesign.dat", False, True)
    lanceur = Relauncher.TLauncher2(tds, run)
    # resolution
    lanceur.solverLoop()
    tds.exportData("_output_testFlowrateMPI_py_.dat")
    ROOT.SetOwnership(run, True)
    run.stopSlave()
```

Here the first difference when comparing this macro to the previous one (see Macro) is the runner creation:

```python
# Create the MPI runner
run = MpiRelauncher.TMpiRun(mycode)
```

The TThreadedRun object becomes a TMpiRun object whose construction only requests a pointer to the assessor.
Another line is different as it is specific to the language: because of the way ROOT and python deal with object destruction
(though the garbage collector approach for the latter), there is problem in the way one of the main key method for MPI
treatment MPI_Finalize is called. To prevent this from happening in python the following line should be added as soon
as the runner object is created:

```python
ROOT.SetOwnership(run, True)
```

It allows ROOT to destroy the object injected, calling the finalize method in order for every slave to be properly released.
Apart from that, the code is very similar, the only difference being the way to call this macro. It should not be run with
the usual command:

```python
python relauncherCodeFlowrateMPI.py
```

Instead, the command line should start with the mpirun command as such:

```python
mpirun -np N python relauncherCodeFlowrateMPI.py
```

where the N part should be replaced by the number of requested threads. Once run, this macro also leads to the following
plots.
Beware never to use the -i argument with the python command line as the macro would never end.
