# Use-cases in Python — Macros Relauncher — Macro “relauncherComposeMultitypeAndReadMultiType.py” … Macro “relauncherCodeFlowrateSequential_TemporaryVar.py”
<!-- source PDF pages 406-413 -->

<!-- page 399 (PDF 406) -->
```python
if runner.onMaster():
    # Create the launcher
    lanceur = Relauncher.TLauncher2(tds, runner)
    lanceur.solverLoop()
    # Stop the slave processes
    runner.stopSlave()
tds.Scan("thev1:thev2")
```

The code is pretty straightforward, the fact that input attributes are vectors and strings is explained in the input file
readmultitype_sampling.dat. One line is added to be sure that an example of input file is present (the file
_output_multitype_mt_Key_condensate_.dat) by calling:

```python
ROOT.gSystem.Exec("multitype -mtKey")
```

The rest is very common and a screenshot of the result displayed in console is provided in the following subsection.

#### 13.8.11.3 Console

```python
************************************
*
     Row
           *
                 thev1 *
                             thev2 *
************************************
*
         0 * 0.2819049 * 11.424490 *
*
         1 * -0.692320 * 15.966536 *
*
         2 * -12345678 * 12.629065 *
*
         3 * -0.819208 * 11.086281 *
*
         4 * -1.561012 * -12345678 *
*
         5 * 0.8843648 * 10.340774 *
*
         6 * -12345678 * 7.1500716 *
*
         7 * 1.6335793 * 14.537357 *
*
         8 * -12345678 * -12345678 *
*
         9 * -0.239765 * 9.3210062 *
************************************
```

###  13.8.12 Macro “relauncherComposeMultitypeAndReadMultiType.py”

####  13.8.12.1 Objective

The objective of this macro is to to combine two different assessor in a chain, so that output attributes of the first assessor
is the input attributes of the second one. This example combined the multitype code to produce vectors and strings
as outputs (as explained in Producing outputs) and use these vectors and strings as inputs, using the code described in
Reading inputs.

#### 13.8.12.2 Macro Uranie

```python
"""
Example of code composition with multitype code
"""
from URANIE import DataServer, Relauncher
import ROOT
```

<!-- page 400 (PDF 407) -->
```python
# inputs
tds = DataServer.TDataServer("foo", "TDS for flowrate")
tds.fileDataRead("multitype_sampling.dat")
# output attributes...
# ... for code 1
w1 = DataServer.TAttribute("w1", DataServer.TAttribute.kString)
w2 = DataServer.TAttribute("w2", DataServer.TAttribute.kString)
v1 = DataServer.TAttribute("v1", DataServer.TAttribute.kVector)
v2 = DataServer.TAttribute("v2", DataServer.TAttribute.kVector)
f1 = DataServer.TAttribute("f1")
# ... for code 2
thev1 = DataServer.TAttribute("thev1")
thev2 = DataServer.TAttribute("thev2")
# ==================================================================
# ========================== Code 1 ================================
# ==================================================================
# Create the input files
inputFile1 = Relauncher.TFlatScript("multitype_input.dat")
inputFile1.addInput(tds.getAttribute("seed"))
ROOT.gSystem.Exec("multitype -mtKey")
# Create the output files
outputFile1 = Relauncher.TKeyResult("_output_multitype_mt_Key_.dat")
outputFile1.addOutput(w1, "w1")
outputFile1.addOutput(v1, "v1")
outputFile1.addOutput(v2, "v2")
outputFile1.addOutput(f1, "f1")
outputFile1.addOutput(w2, "w2")
# Create the user's evaluation function
eval1 = Relauncher.TCodeEval("multitype -mtKey")
eval1.addInputFile(inputFile1)
eval1.addOutputFile(outputFile1)
# ==================================================================
# ========================== Code 2 ================================
# ==================================================================
# Create the output files
inputFile2 = Relauncher.TKeyScript("_output_multitype_mt_Key_condensate_.dat")
inputFile2.addInput(w1, "w1")
inputFile2.addInput(v1, "v1")
inputFile2.addInput(v2, "v2")
inputFile2.addInput(f1, "f1")
inputFile2.addInput(w2, "w2")
# Create the output files
```

<!-- page 401 (PDF 408) -->
```python
outputFile2 = Relauncher.TKeyResult("_output_multitype_readmt_Key_.dat")
outputFile2.addOutput(thev1, "thev1")
outputFile2.addOutput(thev2, "thev2")
# Create the user's evaluation function
eval2 = Relauncher.TCodeEval("multitype -ReadmtKey")
eval2.addInputFile(inputFile2)
eval2.addOutputFile(outputFile2)
# ==================================================================
# ======================= Composition ==============================
# ==================================================================
# Create the composition
compo = Relauncher.TComposeEval()
# Add the code one-by-one, in the right order
compo.addEval(eval1)
compo.addEval(eval2)
# Create the runner by providing the TComposeEval
runner = Relauncher.TSequentialRun(compo)
runner.startSlave()
                     # compulsory
if runner.onMaster():
                       # compulsory
    # Create the launcher
    lanceur = Relauncher.TLauncher2(tds, runner)
    lanceur.solverLoop()
                          # run the code
    # Stop the slave processes
    runner.stopSlave()
    # Get the results
    tds.exportData("pouet_py.dat")
tds.Scan("thev1:thev2")
```

The code looks very much as the one in two previous examples. First a sample of 10 seed values are read from an input
file. Then, output attributes are defined for the first code, as in Macro Uranie.

```python
w1 = DataServer.TAttribute("w1", DataServer.TAttribute.kString)
w2 = DataServer.TAttribute("w2", DataServer.TAttribute.kString)
v1 = DataServer.TAttribute("v1", DataServer.TAttribute.kVector)
v2 = DataServer.TAttribute("v2", DataServer.TAttribute.kVector)
f1 = DataServer.TAttribute("f1")
```

The output attributes are defined for the first code, as in in Macro Uranie.

```python
thev1 = DataServer.TAttribute("thev1")
thev2 = DataServer.TAttribute("thev2")
```

The assessor are then defined with input and output files and the composition is finally done: it is an assessor in in which
we store the other assessors that should be run, in the correct order, as follows:

<!-- page 402 (PDF 409) -->
```python
compo = Relauncher.TComposeEval()
# Add the code one-by-one, in the right order
compo.addEval(eval1)
compo.addEval(eval2)
```

The rest is very common and a screenshot of the result displayed in console is provided in the following subsection.

#### 13.8.12.3 Console

```python
************************************
*
     Row
           *
                 thev1 *
                             thev2 *
************************************
*
         0 * 0.2819049 * 11.424490 *
*
         1 * -0.692320 * 15.966536 *
*
         2 * -12345678 * 12.629065 *
*
         3 * -0.819208 * 11.086281 *
*
         4 * -1.561012 * -12345678 *
*
         5 * 0.8843648 * 10.340774 *
*
         6 * -12345678 * 7.1500716 *
*
         7 * 1.6335793 * 14.537357 *
*
         8 * -12345678 * -12345678 *
*
         9 * -0.239765 * 9.3210062 *
************************************
```

###  13.8.13 Macro “relauncherCodeFlowrateSequential_TemporaryVar.py”

####  13.8.13.1 Objective

The goal of this macro is to show how to hide one of the evaluator’s attribute and not to store it in the final dataserver.
This is considered when a composition is done for instance, in which many variables might be intermediate needed ones,
resulting from an assessor and used as input to one of the following, but of no interest to the user at the end. The flowrate
code is provided with Uranie and has been also used and discussed throughout these macros.

#### 13.8.13.2 Macro

```python
"""
Example of code launching in sequential mode with temporary variable
"""
from URANIE import DataServer, Relauncher, Sampler
def increase_d(local_x):
    """Dummy function that increase by one the input."""
    local_y = local_x + 1
    return [local_y, ]
# Create the TDataServer
tds = DataServer.TDataServer("foo", "test")
# Define the attribute that should be considered as constant
r = DataServer.TAttribute("r")
```

<!-- page 403 (PDF 410) -->
```python
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
inputFile.addInput(tds.getAttribute("tu"), "Tu")
inputFile.addInput(tds.getAttribute("tl"), "Tl")
inputFile.addInput(tds.getAttribute("hu"), "Hu")
inputFile.addInput(tds.getAttribute("hl"), "Hl")
inputFile.addInput(tds.getAttribute("l"), "L")
inputFile.addInput(tds.getAttribute("kw"), "Kw")
# Create the output attributes
yhat = DataServer.TAttribute("yhat")
d = DataServer.TAttribute("d")
# Create the output files
outputFile = Relauncher.TKeyResult("_output_flowrate_withKey_.dat")
outputFile.addOutput(yhat, "yhat")
outputFile.addOutput(d, "d")
# Create the user's evaluation function
eval1 = Relauncher.TCodeEval("flowrate -s -k")
eval1.addInputFile(inputFile)
eval1.addOutputFile(outputFile)
# Create a second evaluation function that uses d to change it slightly
incd = DataServer.TAttribute("incd")
eval2 = Relauncher.TPythonEval(increase_d)
eval2.addInput(d)
eval2.addOutput(incd)
# Create the composition
evalC = Relauncher.TComposeEval()
# Add the code one-by-one, in the right order
evalC.addEval(eval1)
```

<!-- page 404 (PDF 411) -->
```python
evalC.addEval(eval2)
# Create the sequential runner
run = Relauncher.TSequentialRun(evalC)
run.startSlave()
                  # Start the master (necessary even for a sequential)
if run.onMaster():
    lanceur = Relauncher.TLauncher2(tds, run)
    # State to the master: d is an output attribute and I'm interested in its value
    # but I don't want to keep it in the end. It might be useful for another evaluator
    lanceur.addTemporary(d)
    lanceur.addConstantValue(r, 108)
    # resolution
    lanceur.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
tds.scan("*", "", "colsize=6")
```

Here again, a comparison is drawn with the macro in which we set an attribute to a constant value (see Macro “relauncher-
CodeFlowrateSequential_ConstantVar.py”), so only the differences are pointed out. The very first one is contained in the
beginning lines: a new dummy function, so that we can have a composition of two assessors, this function only adding
one to the provided parameter.

```python
def increase_d(local_x):
    """Dummy function that increase by one the input."""
    local_y = local_x + 1
    return [local_y, ]
```

The rest is exactly as for Macro “relauncherCodeFlowrateSequential_ConstantVar.py”, up to the interface with the newy
create function:

```python
# Create a second evaluation function that uses d to change it slightly
incd = DataServer.TAttribute("incd")
eval2 = Relauncher.TPythonEval(increase_d)
eval2.addInput(d)
eval2.addOutput(incd)
# Create the composition
evalC = Relauncher.TComposeEval()
# Add the code one-by-one, in the right order
evalC.addEval(eval1)
evalC.addEval(eval2)
```

A new output attribute is created, called incd for increased d, and the dummy function is defined as taking d as input
and incd as output. Then the composition is done by chaining flowrate with the new dummy function. The rest is fairly
common, up to the TMaster-inheriting object specification: the addTemporary method is called to specify that d is
read from the output of flowrate and can be pass to the rest of the chain, but it will not be kept in the final dataserver. The
addConstantValue is also used just changing the final parameters to show that if nothing is specified, then the value of
r is not stored and this might be tricky for bookkeeping. The results is shown in the next section (from the scan method)
and can be compared to Console for consistency check.

<!-- page 405 (PDF 412) -->
```python
lanceur = Relauncher.TLauncher2(tds, run)
# State to the master: d is an output attribute and I'm interested in its value
# but I don't want to keep it in the end. It might be useful for another evaluator
lanceur.addTemporary(d)
lanceur.addConstantValue(r, 108)
```

<!-- page 406 (PDF 413) -->
#### 13.8.13.3 Console

```python
******************************************************************************************************
 *
    Row
 * foo__n *
   rw.rw *
   tu.tu *
   tl.tl *
   hu.hu *
   hl.hl *
 l.l *
   kw.kw * yhat.y * incd.i *
                                                                                                                                                                                                                                                                                ******************************************************************************************************
    *
    0 *
    0 * 0.1495 * 111790 * 73.820 * 990.90 * 779.83 * 1474.3 * 11220. * 112.01 * 3589.9 *
     *
     1 *
     1 * 0.1394 * 104140 * 95.150 * 1101.5 * 707.21 * 1422.7 * 11493. * 193.62 * 6598.5 *
       *
       2 *
       2 * 0.0557 * 95387. * 84.809 * 1056.2 * 752.94 * 1184.6 * 11967. * 29.880 * 331.58 *
        *
        3 *
        3 * 0.0836 * 74144. * 103.17 * 1051.6 * 819.27 * 1587.4 * 11031. * 35.400 * 2432.1 *
         *
         4 *
         4 * 0.0586 * 65396. * 72.161 * 1003.1 * 710.34 * 1327.5 * 10484. * 24.990 *
                                     5758 *
           *
           5 *
           5 * 0.1203 * 92149. * 65.263 * 1031.6 * 797.34 * 1265.5 * 11638. * 97.386 * 1085.8 *
            *
            6 *
            6 * 0.1319 * 67464. * 93.378 * 1039.4 * 722.54 * 1514.3 * 10996. * 125.33 * 2363.4 *
             *
             7 *
             7 * 0.1059 * 80448. * 112.87 * 1027.1 * 794.32 * 1555.4 *
                                                                   11846 * 62.403 * 1117.3 *
               *
               8 *
               8 * 0.0784 * 100260 * 105.79 * 1072.7 * 767.70 * 1304.1 * 10152. * 45.867 * 522.41 *
                *
                9 *
                9 * 0.0697 * 105158 * 82.544 * 1020.4 * 726.05 * 1640.3 * 10380. * 28.412 * 2803.5 *
                 *
                                   10 *
                                   10 * 0.1252 * 89522. * 100.65 * 1006.2 * 742.35 * 1123.9 * 10743. * 123.70 * 2677.1 *
                   *
                                     11 *
                                     11 * 0.1165 * 73139. * 69.083 * 1108.5 * 809.59 * 1199.0 * 10620. * 112.27 * 4992.3 *
                    *
                                        12 *
                                        12 * 0.0992 * 86004. * 112.12 * 1069.4 * 763.84 * 1345.2 * 9951.0 * 69.808 * 415.71 *
                     *
                                           13 *
                                           13 * 0.0718 * 113775 * 90.580 * 1079.1 * 782.95 * 1416.6 * 10076. * 34.135 * 1017.8 *
                       *
                                             14 *
                                             14 * 0.0902 * 83779. * 80.244 * 1090.6 * 734.33 * 1644.2 *
                                                                                                                 11443 * 63.236 * 2923.3 *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ******************************************************************************************************
```
