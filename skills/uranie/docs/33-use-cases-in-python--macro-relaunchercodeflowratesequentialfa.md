# Use-cases in Python — Macros Relauncher — Macro “relauncherCodeFlowrateSequentialFailure.py” … Macro “relauncherCodeReadMultiType.py”
<!-- source PDF pages 388-405 -->

<!-- page 381 (PDF 388) -->
#### 13.8.6.3 Graph

Figure 13.50: Representation of the output as a function of the first input with a colZ option

### 13.8.7 Macro “relauncherCodeFlowrateSequentialFailure.py”

#### 13.8.7.1 Objective

The goal of this macro is to show how to handle when a code is returning an error status. Up to version v4.5.0, the input
configuration was simply discarded while from any version now, there are discarded but they can be retrieved and store in
a dedicated TDataServer object. The code used here is the usual flowrate model which has been modified to return
a non zero exit status without producing an output file.

#### 13.8.7.2 Macro

```python
"""
Example of code launching in sequential mode with failure
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
```

<!-- page 382 (PDF 389) -->
```python
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
                      # Passing the attributes to the output file
fout.addOutput(d)
                   # Passing the attributes to the output file
# Constructing the code
mycode = Relauncher.TCodeEval("flowrate -s -rf")
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
    # Store the wrong calculation
    error = DataServer.TDataServer("WrongComputations", "pouet")
    lanceur.setSaveError(error)
    # resolution
    lanceur.solverLoop()
    run.stopSlave()
                     # Stop the slaves (necessary even for a sequential)
    # dump all wrong configurations
    error.getTuple().SetScanField(-1)
    error.scan("*")
# Draw the result
can = ROOT.TCanvas("pouet", "foo", 1)
tds.Draw("hu:hl")
```

Here there are very few differences with the one already introduced in Macro. The first one is obviously the command
line which is called using "-rf" argument, the f being introduced for failure.

<!-- page 383 (PDF 390) -->
```python
mycode = Relauncher.TCodeEval("flowrate -s -rf")
```

The second difference is the creation of the failure dataserver object in which all wrong configurations will be stored.
Once created, it is simply passed to the launcher object through the dedicated method setSaveError:

```python
# Store the wrong calculation
error = DataServer.TDataServer("WrongComputations", "pouet")
lanceur.setSaveError(error)
```

Once done the code is run and two things are looked at: the fact that in a peculiar area of the input space there are no
data anymore (by construction, as shown in Figure 13.51) and the fact that all configurations are now stored in a dedicated
TDataServer object which one can dump on screen with the command line below to obtain the second part of the
console output seen in Console

```python
# dump all wrong configurations
error.getTuple().SetScanField(-1)
error.scan("*")
```

The first part of the console output shown in Console is a perfect illustration of the way the relauncher module is discussion
failure: the first part is stating that a non-zero return value has been detected

```python
Command cd ${RUNNINGDIR}/URA_IkSFzC ; flowrate -s -rf has returned non-zero exit code␣
```

˓→(255).

```python
If any different from 127 (usually for unknown command) and 139 (usually for␣
```

˓→SIGSEV), the exit code meaning is "command" dependent.
The second part is letting the user know that no output file has been found (a second reason to consider this configuration
as a failure).

```python
Cannot open :: ${RUNNINGDIR}/URA_IkSFzC/_output_flowrate_withRow_.dat
```

This pattern is repeated every time a configuration is wrong.

<!-- page 384 (PDF 391) -->
#### 13.8.7.3 Graph

Figure 13.51: Representation of the output data point when the code is asked to fail on purpose.

<!-- page 385 (PDF 392) -->
#### 13.8.7.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
            Copyright (C) 2013-2026 CEA/DES
                     Contact: support-uranie@cea.fr
                    Date: Thu Feb 12, 2026
                                               Command cd ${RUNNINGDIR}/URA_IkSFzC ; flowrate -s -rf has returned non-zero exit code (255).
                If any different from 127 (usually for unknown command) and 139 (usually for SIGSEV), the exit code meaning is
```

˓→"command" dependent.

```python
Cannot open :: ${RUNNINGDIR}/URA_IkSFzC/_output_flowrate_withRow_.dat
         Command cd ${RUNNINGDIR}/URA_IkSFzC ; flowrate -s -rf has returned non-zero exit code (255).
     If any different from 127 (usually for unknown command) and 139 (usually for SIGSEV), the exit code meaning is
```

˓→"command" dependent.

```python
Cannot open :: ${RUNNINGDIR}/URA_IkSFzC/_output_flowrate_withRow_.dat
         Command cd ${RUNNINGDIR}/URA_IkSFzC ; flowrate -s -rf has returned non-zero exit code (255).
     If any different from 127 (usually for unknown command) and 139 (usually for SIGSEV), the exit code meaning is
```

˓→"command" dependent.

```python
Cannot open :: ${RUNNINGDIR}/URA_IkSFzC/_output_flowrate_withRow_.dat
         Command cd ${RUNNINGDIR}/URA_IkSFzC ; flowrate -s -rf has returned non-zero exit code (255).
     If any different from 127 (usually for unknown command) and 139 (usually for SIGSEV), the exit code meaning is
```

˓→"command" dependent.

```python
Cannot open :: ${RUNNINGDIR}/URA_IkSFzC/_output_flowrate_withRow_.dat
         Command cd ${RUNNINGDIR}/URA_IkSFzC ; flowrate -s -rf has returned non-zero exit code (255).
     If any different from 127 (usually for unknown command) and 139 (usually for SIGSEV), the exit code meaning is
```

˓→"command" dependent.

```python
Cannot open :: ${RUNNINGDIR}/URA_IkSFzC/_output_flowrate_withRow_.dat
                                                                                                                                                                                ************************************************************************************************************************************
   *
        Row
   * WrongComp *
             rw.rw *
        r.r *
             tu.tu *
             tl.tl *
             hu.hu *
             hl.hl *
        l.l *
             kw.kw␣
```

˓→* ystar.yst *

```python
************************************************************************************************************************************
 *
 0 *
 4 *
        0.0633 *
    100 *
        115600 *
       80.73 *
         1075.71 *
        751.43 *
     1600 *
           11106.43␣
```

˓→*

```python
28.33 *
 *
 1 *
 5 *
        0.0633 *
           16733.33 *
       80580 *
       80.73 *
         1058.57 *
        785.71 *
     1680 *
       12045␣
```

˓→*

```python
24.6 *
 *
 2 *
 8 *
        0.0767 *
    100 *
        115600 *
       80.73 *
         1075.71 *
        751.43 *
     1520 *
           10793.57␣
```

˓→*

```python
42.44 *
 *
 3 *
   12 *
     0.09 *
           16733.33 *
       63070 *
    116 *
         1075.71 *
        751.43 *
     1120 *
           11419.29␣
```

<!-- page 386 (PDF 393) -->
˓→*

```python
83.77 *
 *
 4 *
   23 *
        0.1233 *
           16733.33 *
       63070 *
     63.1 *
         1041.43 *
        785.71 *
     1680 *
       12045␣
```

˓→*

```python
86.73 *
                                                                                                                                                                                ************************************************************************************************************************************
```

<!-- page 387 (PDF 394) -->
### 13.8.8 Macro “relauncherCodeMultiTypeKey.py”

#### 13.8.8.1 Objective

The objective of this macro is to test the case where vectors and strings are produced as outputs, using the code described
in Producing outputs, with a Key format, obtained by doing:

```python
multitype -mtKey
```

The resulting output file, named _output_multitype_mt_Key_.dat looks like:

```python
w1 = nine
v1 = -0.512095
v1 = 0.039669
v1 = -1.3834
v1 = 1.37667
v1 = 0.220672
v1 = 0.633267
v1 = 1.37027
v1 = -0.765636
v2 = 14.1981
v2 = 14.0855
v2 = 10.7848
v2 = 9.45476
v2 = 9.17308
v2 = 6.60804
v2 = 10.0711
v2 = 14.1761
v2 = 10.318
v2 = 12.5095
v2 = 15.6614
v2 = 10.3452
v2 = 9.41101
v2 = 7.47887
f1 = 32.2723
w2 = eight
```

####  13.8.8.2 Macro Uranie

```python
"""
Example of multitype code launching
"""
from URANIE import DataServer, Relauncher, Sampler
import ROOT
# Create the DataServer.TDataServer and create the seed attribute
tds = DataServer.TDataServer("foo", "multitype usecase")
tds.addAttribute(DataServer.TUniformDistribution("seed", 0, 100000))
# Create DOE
tsam = Sampler.TSampling(tds, "lhs", 100)
tsam.generateSample()
# Create output attribute pointers
```

<!-- page 388 (PDF 395) -->
```python
w1 = DataServer.TAttribute("w1", DataServer.TAttribute.kString)
w2 = DataServer.TAttribute("w2", DataServer.TAttribute.kString)
v1 = DataServer.TAttribute("v1", DataServer.TAttribute.kVector)
v2 = DataServer.TAttribute("v2", DataServer.TAttribute.kVector)
f1 = DataServer.TAttribute("f1")
# Create the input files
inputFile = Relauncher.TFlatScript("multitype_input.dat")
inputFile.addInput(tds.getAttribute("seed"))
# Create the output files
outputFile = Relauncher.TKeyResult("_output_multitype_mt_Key_.dat")
outputFile.addOutput(w1, "w1")
outputFile.addOutput(v1, "v1")
outputFile.addOutput(v2, "v2")
outputFile.addOutput(f1, "f1")
outputFile.addOutput(w2, "w2")
# Create the user's evaluation function
myeval = Relauncher.TCodeEval("multitype -mtKey")
myeval.addInputFile(inputFile)
                                # Add the input file
myeval.addOutputFile(outputFile)
                                  # Add the output file
# Create the runner
runner = Relauncher.TSequentialRun(myeval)
# Start the slaves
runner.startSlave()
if runner.onMaster():
    # Create the launcher
    lanceur = Relauncher.TLauncher2(tds, runner)
    lanceur.solverLoop()
    # Stop the slave processes
    runner.stopSlave()
# Produce control plot
Can = ROOT.TCanvas("Can", "Can", 10, 10, 1000, 800)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.cd()
tds.drawPairs("w1:v1:v2:f1:w2")
```

The beginning of the code is pretty common to many other macros: creating a dataserver and input attributes (here the
only one is the seed, needed for the random generator to produce vectors and strings). A sampling object is created as
well to produce a 100-points design-of-experiments and the output attributes are created, as such:

```python
# Create output attribute pointers
w1 = DataServer.TAttribute("w1", DataServer.TAttribute.kString)
w2 = DataServer.TAttribute("w2", DataServer.TAttribute.kString)
v1 = DataServer.TAttribute("v1", DataServer.TAttribute.kVector)
```

<!-- page 389 (PDF 396) -->
```python
v2 = DataServer.TAttribute("v2", DataServer.TAttribute.kVector)
f1 = DataServer.TAttribute("f1")
```

This is where the specificity of the vector and string is precised. It will be passed on to the rest of the code automatically.
The rest is common to many relauncher job (for instance Macro “relauncherCodeFlowrateSequential.py”) with the only
difference being that the output file is a key type one. It results in the following plots.

#### 13.8.8.3 Graph

Figure 13.52: Graph of the macro “relauncherCodeMultiTypeKey.py”

### 13.8.9 Macro “relauncherCodeMultiTypeKeyEmptyVectors.py”

#### 13.8.9.1 Objective

The objective of this macro is to test the case where vectors and strings are produced as outputs, using the code described
in Producing outputs, with a Key format, obtained by doing:

```python
multitype -mtKey -empty
```

Unlike what’s done to in Macro “relauncherCodeMultiTypeKey.py”, the “-empty” allows the code to generate empty vectors
and not only vectors whose size would be between 1 and 15 elements. The resulting output file used is a key-format one
in a condensate form, named _output_multitype_mt_Key_condensate_.dat looks like:

<!-- page 390 (PDF 397) -->
```python
w1 = nine
v1 = [ -0.512095,0.039669,-1.3834,1.37667,0.220672,0.633267,1.37027,-0.765636 ]
v2 = [ 14.1981,14.0855,10.7848,9.45476,9.17308,6.60804,10.0711,14.1761,10.318,12.5095,
```

˓→15.6614,10.3452,9.41101,7.47887 ]

```python
f1 = 32.2723
w2 = eight
```

####  13.8.9.2 Macro Uranie

```python
"""
Example of code launching for which empty vectors are possible
"""
from URANIE import DataServer, Relauncher, Sampler
import ROOT
# Create the DataServer.TDataServer and create the seed attribute
tds = DataServer.TDataServer("foo", "multitype usecase")
tds.addAttribute(DataServer.TUniformDistribution("seed", 0, 100000))
# Create DOE
tsam = Sampler.TSampling(tds, "lhs", 100)
tsam.generateSample()
# Create output attribute pointers
w1 = DataServer.TAttribute("w1", DataServer.TAttribute.kString)
w2 = DataServer.TAttribute("w2", DataServer.TAttribute.kString)
v1 = DataServer.TAttribute("v1", DataServer.TAttribute.kVector)
v2 = DataServer.TAttribute("v2", DataServer.TAttribute.kVector)
f1 = DataServer.TAttribute("f1")
# Create the input files
inputFile = Relauncher.TFlatScript("multitype_input.dat")
inputFile.addInput(tds.getAttribute("seed"))
# Create the output files
outputFile = Relauncher.TKeyResult("_output_multitype_mt_Key_condensate_.dat")
outputFile.addOutput(w1, "w1")
outputFile.addOutput(v1, "v1")
outputFile.addOutput(v2, "v2")
outputFile.addOutput(f1, "f1")
outputFile.addOutput(w2, "w2")
outputFile.setVectorProperties("[", ", ", "]")
# Create the user's evaluation function
myeval = Relauncher.TCodeEval("multitype -mtKey -empty")
myeval.addInputFile(inputFile)
                                # Add the input file
myeval.addOutputFile(outputFile)
                                  # Add the output file
# Create the runner
runner = Relauncher.TSequentialRun(myeval)
# Start the slaves
runner.startSlave()
```

<!-- page 391 (PDF 398) -->
```python
if runner.onMaster():
    # Create the launcher
    lanceur = Relauncher.TLauncher2(tds, runner)
    lanceur.solverLoop()
    # Stop the slave processes
    runner.stopSlave()
# Produce control plot
Can = ROOT.TCanvas("Can", "Can", 10, 10, 1000, 800)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(1, 2)
pad.cd(1)
tds.getTuple().SetLineColor(2)
tds.getTuple().SetLineWidth(2)
tds.Draw("size__v1")
pad.cd(2)
tds.Draw("size__v2")
```

The beginning of the code is pretty common to the macro already discussed in Macro Uranie. Apart from the command
difference discussed in the objective above through the “-empty” argument, the main difference with previous macro
is the way the output file is declared. Despite from changing the name, the vector properties are set by calling the
setVectorProperties method to emphasize how to read the information.

```python
# Create the output files
outputFile = Relauncher.TKeyResult("_output_multitype_mt_Key_condensate_.dat")
outputFile.addOutput(w1, "w1")
outputFile.addOutput(v1, "v1")
outputFile.addOutput(v2, "v2")
outputFile.addOutput(f1, "f1")
outputFile.addOutput(w2, "w2")
outputFile.setVectorProperties("[", ", ", "]")
```

Apart from this, the code is smooth and the final results one can be interested in the size of the vectors produced when
empty vectors are allowed. This is produced though the following lines, and the resulting plots are shown in Figure 13.53.

```python
# Produce control plot
Can = ROOT.TCanvas("Can", "Can", 10, 10, 1000, 800)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(1, 2)
pad.cd(1)
tds.getTuple().SetLineColor(2)
tds.getTuple().SetLineWidth(2)
tds.Draw("size__v1")
pad.cd(2)
tds.Draw("size__v2")
```

If the output file was not properly formatted, then one can have issues with this specific case (empty vectors). The
consequences are shown in Macro “relauncherCodeMultiTypeKeyEmptyVectorsAsFailure.py”.

<!-- page 392 (PDF 399) -->
#### 13.8.9.3 Graph

Figure 13.53: Graph of the macro “relauncherCodeMultiTypeKeyEmptyVectors.py”

### 13.8.10 Macro “relauncherCodeMultiTypeKeyEmptyVectorsAsFailure.py”

#### 13.8.10.1 Objective

The objective of this macro is to test the case where vectors and strings are produced as outputs, using the code described
in Producing outputs, with a Key format, obtained by doing:

```python
multitype -mtKey -empty
```

Unlike what’s done to in Macro “relauncherCodeMultiTypeKey.py”, the “-empty” allows the code to generate empty vectors
and not only vectors whose size would be between 1 and 15 elements. The resulting output file used is a key-format
in a very row form, meaning that evey new element of the vectors are written as a new key-line. This file, named
_output_multitype_mt_Key_.dat could looks like this:

```python
w1 = nine
v1 = -0.512095
v1 = 0.039669
v1 = -1.3834
v1 = 1.37667
v1 = 0.220672
```

<!-- page 393 (PDF 400) -->
```python
v1 = 0.633267
v1 = 1.37027
v1 = -0.765636
v2 = 14.1981
v2 = 14.0855
v2 = 10.7848
v2 = 9.45476
v2 = 9.17308
v2 = 6.60804
v2 = 10.0711
v2 = 14.1761
v2 = 10.318
v2 = 12.5095
v2 = 15.6614
v2 = 10.3452
v2 = 9.41101
v2 = 7.47887
f1 = 32.2723
w2 = eight
```

####  13.8.10.2 Macro Uranie

```python
"""
Example of code launching with empy vectors as failure
"""
from URANIE import DataServer, Relauncher, Sampler
import ROOT
# Create the DataServer.TDataServer and create the seed attribute
tds = DataServer.TDataServer("foo", "multitype usecase")
tds.addAttribute(DataServer.TUniformDistribution("seed", 0, 100000))
# Create DOE
tsam = Sampler.TSampling(tds, "lhs", 100)
tsam.generateSample()
# Create output attribute pointers
w1 = DataServer.TAttribute("w1", DataServer.TAttribute.kString)
w2 = DataServer.TAttribute("w2", DataServer.TAttribute.kString)
v1 = DataServer.TAttribute("v1", DataServer.TAttribute.kVector)
v2 = DataServer.TAttribute("v2", DataServer.TAttribute.kVector)
f1 = DataServer.TAttribute("f1")
# Create the input files
inputFile = Relauncher.TFlatScript("multitype_input.dat")
inputFile.addInput(tds.getAttribute("seed"))
# Create the output files
outputFile = Relauncher.TKeyResult("_output_multitype_mt_Key_.dat")
outputFile.addOutput(w1, "w1")
outputFile.addOutput(v1, "v1")
```

<!-- page 394 (PDF 401) -->
```python
outputFile.addOutput(v2, "v2")
outputFile.addOutput(f1, "f1")
outputFile.addOutput(w2, "w2")
# Create the user's evaluation function
myeval = Relauncher.TCodeEval("multitype -mtKey -empty")
myeval.addInputFile(inputFile)
                                # Add the input file
myeval.addOutputFile(outputFile)
                                  # Add the output file
# Create the runner
runner = Relauncher.TSequentialRun(myeval)
# Start the slaves
runner.startSlave()
if runner.onMaster():
    # Create the launcher
    lanceur = Relauncher.TLauncher2(tds, runner)
    # Store the wrong calculation
    error = DataServer.TDataServer("WrongComputations", "pouet")
    lanceur.setSaveError(error)
    lanceur.solverLoop()
    # dump all wrong configurations
    error.getTuple().SetScanField(-1)
    error.scan("*")
    # Stop the slave processes
    runner.stopSlave()
# Produce control plot
Can = ROOT.TCanvas("Can", "Can", 10, 10, 1000, 800)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.cd()
tds.drawPairs("w1:v1:v2:f1:w2")
```

The beginning of the code is pretty common to the macro already discussed in Macro Uranie. Apart from the command
difference discussed in the objective above through the “-empty” argument, the main difference with previous macro is
the failure dataserver declaration and the output console that would be discussed later-on. The former is done through
the following lines:

```python
# Store the wrong calculation
error = DataServer.TDataServer("WrongComputations", "pouet")
lanceur.setSaveError(error)
```

Once the code is run, the configuration leading to empty vectors are gathered in the failure dataserver and dumped on
screen through the following lines:

```python
# dump all wrong configurations
```

<!-- page 395 (PDF 402) -->
```python
error.getTuple().SetScanField(-1)
error.scan("*")
```

The final part is the way to represent the results: as for the use-case macro discussed in Macro “relauncherCodeMulti-
TypeKey.py”, all data are plotted in a pair plot and this is summarised in Figure 13.54. From this picture one should really
pay attention to the number of entries to spot that some configuration are missing. Luckily when looking at the console
in Console. This time (unlike the failure in Macro “relauncherCodeFlowrateSequentialFailure.py”) the code is returning a
zero output status (because the code actually worked fine) but as from time to time one the two vectors is empty, no entry
is written in the output whose format is too simple (as it consist only in dumping vector elements by elements) this is why
the only message is the fact that, from time to time, one vector information is missing.

#### 13.8.10.3 Graph

Figure 13.54: Graph of the macro “relauncherCodeMultiTypeKeyEmptyVectorsAsFailure.py”

#### 13.8.10.4 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
```

<!-- page 396 (PDF 403) -->
```python
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v2 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v2 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v2 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v2 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v2 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v1 Not found
TKeyResult(_output_multitype_mt_Key_.dat): v2 Not found
************************************
*
     Row
           * WrongComp * seed.seed *
************************************
*
         0 *
                     9 *
                          93759.29 *
*
         1 *
                    33 * 74051.957 *
*
         2 *
                    35 * 71909.957 *
*
         3 *
                    50 * 4183.9188 *
*
         4 *
                    54 * 41806.234 *
*
         5 *
                    57 * 28298.703 *
*
         6 *
                    66 * 64903.722 *
*
         7 *
                    69 * 47690.947 *
*
         8 *
                    73 * 89415.222 *
*
         9 *
                    79 * 30656.411 *
*
        10 *
                    84 * 31627.094 *
*
        11 *
                    86 * 63698.481 *
*
        12 *
                    89 * 13461.926 *
*
        13 *
                    99 * 52994.014 *
************************************
```

###  13.8.11 Macro “relauncherCodeReadMultiType.py”

####  13.8.11.1 Objective

The objective of this macro is to test the case where vectors and strings are used as inputs, using the code described in
Reading inputs, with a Key format, obtained by doing:

```python
multitype -ReadmtKey
```

The input values will be read from a database which is produced with the multitype -mt code, as no sampling is
available yet to produce vectors and strings. The database file is readmultitype_sampling.dat which looks like
this:

```python
#NAME: foo
#TITLE: TDS for flowrate
#DATE: Mon Oct
                3 23:50:34 2016
#COLUMN_NAMES: v1| w1| v2| w2| f1| foo__n__iter__
#COLUMN_TYPES: V|S|V|S|D|D
```

<!-- page 397 (PDF 404) -->
```python
-6.901933299378e-02,-1.292435959913e-01,4.558876683004e-01,5.638486368789e-01,-4.
```

˓→767582766745e-02,7.102109543136e-03,2.819049677902e-01,-2.019788081790e+00,-2.
˓→604401028584e+00,-1.617682380292e+00,2.894560949798e-02,-3.493905850261e-01 six 1.
˓→142449011404e+01,7.318948216271e+00,1.502260859231e+01,6.041193793062e+00,6.
˓→729445145907e+00,1.128096968597e+01 zero 3.425632316777e+01 0.000000000000e+00

```python
-6.923200061823e-01,-4.798721931875e-01,-1.329893204384e+00,1.292933726829e+00 zero 1.
```

˓→249911290435e+01,6.309239169117e+00,1.596653626442e+01,5.500878012739e+00,1.
˓→322535550082e+01,7.070984389647e+00,1.708574150702e+00,1.265915339220e+01 two 4.
˓→295175025115e+01 1.000000000000e+00

```python
5.773813268848e-01,-3.512405673973e-01,-6.870089014992e-01,1.273074555211e-01 nine 1.
```

˓→242682578759e+01,1.109680842701e+01,1.670410641828e+01,7.296321908492e+00,8.
˓→732800753443e+00,1.262906549132e+01,8.882310687564e+00,1.104280818003e+01 five 5.
˓→591437936893e+01 2.000000000000e+00

```python
5.518508915499e-01,2.438158138873e-01,1.111784497742e+00,-1.517566514667e+00,7.
```

˓→146879916125e-01,2.328439269321e+00,-1.251913839951e+00,8.876684186954e-01,-1.
˓→383023165632e+00,-8.192089693621e-01,-1.079524713568e-01,6.595650273375e-01,-2.
˓→275345802432e-03,1.304354557600e+00 nine 1.021975159505e+01,4.995433740783e+00,1.
˓→108628156181e+01,1.041110604995e+01,1.111365770153e+01,6.365695806343e+00,6.
˓→374053973239e+00,6.854423942510e+00,7.144262333164e+00 two 4.093776591421e+01 3.
˓→000000000000e+00

```python
2.403942476958e-01,6.868091212609e-01,-1.561012830108e+00,1.937806684989e+00,-1.
```

˓→465851888061e+00,5.367279844359e-02,-1.263005327899e+00,-1.132259472701e+00 two 7.
˓→382048319627e+00,5.874867917970e+00,1.158191378461e+01,1.073321314846e+01 six 6.
˓→980549752305e+01 4.000000000000e+00

```python
2.220485143391e+00,-5.787212569267e-01,8.843648237689e-01,2.020662891124e+00,1.
```

˓→066403357312e+00,-5.817432767992e-01,3.063023900800e-01,-7.393588637933e-01 two 2.
˓→049656723853e+00,9.679003878866e+00,7.338089623518e+00,1.235630702472e+01,1.
˓→509238505697e+01,1.034077492413e+01,1.116077550501e+01,7.179221834787e+00,1.
˓→582041236432e+01,9.204085091129e+00,4.707490792498e+00,1.618155764288e+01 five 3.
˓→507773555061e+01 5.000000000000e+00

```python
8.908373817765e-01,-2.446355046704e-01,-1.900125532005e+00 seven 1.351254851860e+01,9.
```

˓→297087139459e+00,1.130966904782e+01,1.219245848701e+01,1.012996566249e+01,7.
˓→150071600452e+00,1.097549218518e+01,1.443074761657e+01 five 4.464560504112e+01 6.
˓→000000000000e+00

```python
-2.514644600888e+00,1.633579305804e+00 one 1.229098312451e+01,1.013486836958e+01,1.
```

˓→243386772880e+01,1.071783135260e+01,1.453735777922e+01,7.995593455015e+00,9.
˓→753966962919e+00,5.924583770352e+00,6.187713988125e+00,1.061975242996e+01,6.
˓→650425922126e+00 four 4.553396475968e+01 7.000000000000e+00

```python
-1.347811599520e+00,-1.259450135534e+00,1.812553405758e+00 five 7.717018655412e+00,1.
```

˓→053283796180e+01,7.404059210327e+00 eight 6.695868880279e+01 8.000000000000e+00

```python
-1.258360863204e-01,-9.000566818602e-01,7.039146852797e-01,1.015917277706e+00,-2.
```

˓→397650482929e-01 four 4.346717386417e+00,1.033024889324e+01,7.183787459050e+00,8.
˓→742095837835e+00,1.277095440277e+01,8.685683828779e+00,9.321006265935e+00,6.
˓→353438157123e+00,8.552570119034e+00 six 4.381313066586e+01 9.000000000000e+00
For every pattern, an input file is created with the Key condensate format, as the other key format is not practical (and
usable). This input file looks like this:

```python
w1 = nine
v1 = [ -0.512095,0.039669,-1.3834,1.37667,0.220672,0.633267,1.37027,-0.765636 ]
v2 = [ 14.1981,14.0855,10.7848,9.45476,9.17308,6.60804,10.0711,14.1761,10.318,12.5095,
```

<!-- page 398 (PDF 405) -->
˓→15.6614,10.3452,9.41101,7.47887 ]

```python
f1 = 32.2723
w2 = eight
```

The resulting output file, named _output_multitype_readmt_Key_.dat looks like:

```python
thev1 = -0.2397650482929
thev2 = 9.321006265935
```

####  13.8.11.2 Macro Uranie

```python
"""
Example of multitype code launching in sequential mode
"""
from URANIE import DataServer, Relauncher
import ROOT
# inputs
tds = DataServer.TDataServer("foo", "TDS for flowrate")
tds.fileDataRead("readmultitype_sampling.dat")
# Input attribute
w1 = tds.getAttribute("w1")
w2 = tds.getAttribute("w2")
v1 = tds.getAttribute("v1")
v2 = tds.getAttribute("v2")
f1 = tds.getAttribute("f1")
# output attribute
thev1 = DataServer.TAttribute("thev1")
thev2 = DataServer.TAttribute("thev2")
ROOT.gSystem.Exec("multitype -mtKey")
# Create the output files
inputFile = Relauncher.TKeyScript("_output_multitype_mt_Key_condensate_.dat")
inputFile.addInput(w1, "w1")
inputFile.addInput(v1, "v1")
inputFile.addInput(v2, "v2")
inputFile.addInput(f1, "f1")
inputFile.addInput(w2, "w2")
# Create the output files
outputFile = Relauncher.TKeyResult("_output_multitype_readmt_Key_.dat")
outputFile.addOutput(thev1, "thev1")
outputFile.addOutput(thev2, "thev2")
# Create the user's evaluation function
myeval = Relauncher.TCodeEval("multitype -ReadmtKey")
myeval.addInputFile(inputFile)
myeval.addOutputFile(outputFile)
runner = Relauncher.TSequentialRun(myeval)
runner.startSlave()
```
