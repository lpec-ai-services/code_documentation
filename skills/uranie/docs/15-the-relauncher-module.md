# The Relauncher module
<!-- source PDF pages 135-147 -->

<!-- page 128 (PDF 135) -->
THE RELAUNCHER MODULE

## 8.1 Introduction

The aim of the Relauncher module is to provide a general architecture for all parametric study and is, because of this
generality aspect, heavily used throughout the Uranie platform. However, it is generally used for more advanced techniques
than the usual recommended first steps and it allows more flexible distribution approaches.
Studies allowed thanks to this module (no concrete study will indeed be described in this chapter, as the module is more a
support for many other classes in other modules) aim at evaluate a model for different input parameter’s values and check
the evolution of its outputs. These studies can be split into two kinds:
• the opened-loop ones: all input parameters are known at the start (Monte-Carlo simulation for instance).
• the closed-loop ones: results of the evaluation will impact the next input parameter’s value (optimisation for instance
).
One can find examples of how to run analysis with the relauncher implementation in Macros Relauncher.
Item evaluations can be time consuming, and many kinds of such studies are able to distribute them on computer resources.
This architecture provides different ways to use these resources. However, if evaluation is fast, evaluation distribution is
counterproductive.
Because of the very specific organisation of this module, the class hierarchy is not shown here but split into pieces which
will be introduced in the next section. Every component is discussed in more details in the following sections and a
schematic description of the needed steps to define a relauncher procedure is shown in Figure 8.1.

## 8.2 Relauncher abstraction levels

In order to obtain a modular system, three abstraction levels are distinguished:
• The top level (TMaster) deals with the problem, and defines items to be evaluated. It plays a role of supervisor
and this level is usually called master.
• The intermediate level (TRun) defines where evaluations are computed using available computer resources. This
level is usually called runner.
• The bottom level (TEval) uses functions provided by the user to evaluate item characteristics and this level is
usually called assessor.
Ideally, the combination of any classes of this three levels are possible. In real world, some combinations are useless
(do not distribute a sequential algorithm) or impossible (many algorithm cannot converge if an non-calculable evaluation
occurs).
As you can see from the defined layers, the architecture is designed to realise many evaluations in parallel. It deals both
with a parallel evaluation and with a parallel studies (island optimisation for example). A feasibility test have been done
with a parallel evaluation, but it needs extra works from the user.

<!-- page 129 (PDF 136) -->
Now let’s start with a first hello world program. It treats the classical Rosenbrock optimisation problem (already introduced
in Rosenbrock function). The script below starts with namespace directive, continues with the user supplied evaluation
function, and ends with the study procedure. This procedure follows a bottom-up definition: used variables, evaluation
function declaration, used resources, and study. Variables are used to define the evaluation prototype and the study (item
definition variables, etc), and link these definitions together. In this example, some declarations may seem redundant, but
they show their relevance in a more complicated example.

```python
#!/usr/bin/env python3
import ROOT
### user evaluation function
def rosenbrock(x, y) :
    d1 = (1-x)
    d2 = (y-x*x)
    return [d1*d1 + d2*d2,]
### study section
# problem variables
itemvar = [
    ROOT.URANIE.DataServer.TAttribute("x", -3.0, 3.0),
    ROOT.URANIE.DataServer.TAttribute("y", -4., 6.),
]
ros = ROOT.URANIE.DataServer.TAttribute("rose")
# user evaluation function
eval = ROOT.URANIE.Relauncher.TPythonEval(rosenbrock)
for a in itemvar :
    eval.addInput(a)
eval.addOutput(ros)
# resources
run = ROOT.URANIE.Relauncher.TSequentialRun(eval)
#run = ROOT.URANIE.MpiRelauncher.TMpiRun(eval)
run.startSlave()
if run.onMaster() :
    # data server
    tds = ROOT.URANIE.DataServer.TDataServer("rosopt", "Rosenbrock Optimisation")
    for a in itemvar :
        tds.addAttribute(a)
    # optimisation
    algo = ROOT.URANIE.Reoptimizer.TVizirGenetic()
    study = ROOT.URANIE.Reoptimizer.TVizir2(tds, run, algo)
    study.addObjective(ros)
    study.solverLoop()
    # save results
    tds.exportData("pyrosenbrock.dat")
    run.stopSlave()
```

<!-- page 130 (PDF 137) -->
This example will not be detailed, it is showed for its structure that you may find again on other studies. however, it must
be self explanatory.
An important aspect needs to be pointed out. It concerns the resource handling. This script deals with both the study side
and the evaluation side which may be treated by different resources. Both sides need to know variables and evaluation
function, while study objects are only useful on study side. Here is the frame of the code that deals with it.

```python
   both side definitions
...
run.startSlave()
                  # slave is evaluation side
if run.onMaster() :
    # master is study side
    # study definitions
    ...
    run.stopSlave()
    pass
```

A translation of this code may be: once one starts the study, evaluation-needed objects are defined and evaluation-resources
could start their loop waiting for items. The study-resource are allocated from the onMaster method and many things
are done from there: distributing the evaluations and collecting the results. Once the study is finished (or at least, no more
evaluation is needed), evaluation-resources can be stopped: they stop their loop, exit and jump the study instruction bloc
which is no concern to them.
Finally the use of Relauncher module can be sketched in a four-steps process starting as usual, by defining the problem
/model to be tested, defining the rule to be applied on the various inputs (meaning configuring the assessors also
knowing the way one wants to run these calculations), choosing the corresponding runner and launch the computation
through the TLauncher2 instantiation (or any other TMaster inheriting class, such as the ones defined in the Reoptimizer
module for optimisation problem, see The Reoptimizer module). The colored arrows in Figure 8.1 show the allowed
associations of assessors and runners (to respect, for instance, the thread-safe properties of the assessors).
Figure 8.1: Schematic description of the needed steps to define a relauncher procedure

<!-- page 131 (PDF 138) -->
The next three sections will successively pass through the different level of abstraction, starting from the bottom level to
the top one.

## 8.3 TEval

The TEval abstract class defines the interface of user evaluation model. It provides an user class basis to define a model,
and allows composition class to combine models together.
A standard evaluation is a function from 𝑛input parameters to 𝑚output parameters. 𝑛and 𝑚are known and fixed during
the run, but they can now be string, vectors, or double. These evaluations may not return a value. Generally, it is due to
an inconsistent input set. TMaster may support (or not) this lack.
A glimpse of all the assessor classes available can be found in Figure 8.2 that displays the hierarchy of class starting from
the inheritance of TEval.
Figure 8.2: Hierarchy of classes and structures for the evaluation part of the Relauncher module.
All the assessors will need to have attributes attached to them, both inputs and outputs. Input attributes might have a
peculiar status, by being constant disregarding the provided stochastic law. On the other hand, output attributes might
be considered temporary if, for instance, their value is of no interest for the final analysis but might be used by another
assessor in composition. All this is discussed later on, in TMaster as these specification will be done directly on the master
object.

### 8.3.1 TPythonEVal

#### 8.3.1.1 function convention

The Python function, that can be used with Uranie, receives item values directly in the function parameters and return an
output list (even if they are only one value). The rosenbrock example is given below.

```python
def rosenbrock(x, y) :
    d1 = (1-x)
    d2 = (y-x*x)
    return [d1*d1 + d2*d2,]
```

TThreadedRun should now be supported and TMpiRun works but exits badly: the C++ destructor is not called, resulting
in an incorrect MPI exit (MPI_Finalize is not call). Put the stopSlave method call as last instruction to avoid that
evaluation processes stop before master process.
The TPythonEval is also able to deal with vectors and strings as inputs and outputs. If the way to deal with string is
transparent, vector are just simple plain list of real.

<!-- page 132 (PDF 139) -->
#### 8.3.1.2 parameter declaration

The class definition gives information neither about the input or output number nor about parameter order. These information
have to be added to link with TDataServer and TMaster definitions. We use the addInput and addOutput
method with TAttribute objects as argument to do so. Inputs and outputs have to be added in correct order. Here is
an example of how to precise inputs and outputs, from the script in Relauncher abstraction levels:

```python
# problem variables
x = DataServer.TAttribute("x", -3.0, 3.0)
y = DataServer.TAttribute("y", -4., 6.)
ros = DataServer.TAttribute("rose")
# user evaluation function
eval = Relauncher.TPythonEval(rosenbrock)
eval.addInput(x)
                  # Adding attribute in the correct order
eval.addInput(y)
eval.addOutput(ros)
```

###  8.3.2 TCIntEval and TCJitEval

These classes are generaly used when you use the cling root interpreter with Uranie. So they are not detailed here. Their
documentation can be find in the C++ version of this documentation, but their uses are very similar to a TPythonEval
class.
Using C function in python can be done with the ROOT cling interpreter and the TCIntEval. Suppose you have a C
rosenbrock function defined in the UserFunctions.C file as follow.

```python
void rosenbrock(double *in, double *out)
{
    double x, y, d1, d2;
    x = in[0]; y = in[1];
    d1 = (1-x);
    d2 = (y-x*x);
    out[0] = d1*d1 + d2*d2;
}
```

To use this function in Uranie, you need to load the script, and define the TCIntEVal (a TCJitEval does not work in
python interpreter)

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
fun = Relauncher.TCIntEval("rosenbrock")
```

It is also possible to simply use a C++ function in python, through the ROOT cling interpreter out of the Relauncher
paradigm (for single-purpose estimation for instance). This discussion is already covered in Use a C++ function interactively
.

### 8.3.3 TCodeEval

This class takes up the TCode class features and make it thread safe.
Evaluation is done by an external executable, which reads one (or more) configuration file, where it finds its inputs, and
writes the single result file, where to find the output variables. TCodeEval must create or adapt configuration files to
introduce item values, run the executable, and analyse the result file to get its outputs. It needs to know file formats, and
where to find values.

<!-- page 133 (PDF 140) -->
#### 8.3.3.1 Local environment

In order to be used in parallel (MPI or thread), we have to take care of file access conflicts: many processes which modify
the same file. To avoid such a thing, Uranie creates for each resource a personal directory named URA with then a set
of numbers and letters that is more robust than the older version with just increasing numbers. Everything is done in it:
input files are created there, executable is run from it and the output file are supposed to be found here as well. By default,
these directories are created in the current folder. You can specify another root directory, using the setWorkingDir
method. There are two other methods that can be called to change this:
• setOldTmpDir(): This will create folder named URANIE0, then URANIE1 and so on, up to the number of process
chosen (for sequential job, only URANIE0 will be created).
• keepAllFolders(): This method is meant for debugging. It creates a specific working directory for EVERY
computations (warning it might overflow your home directory).
Input files are often created from template files. These files, if they are not defined with a full path, are search in the
current directory. You can specify another one using the setReference method.
The class constructor takes a string (const char*) as argument which is the command line used to launch the executable.
%D jocker can be used, and will be replaced by the local directory.

#### 8.3.3.2 Various file format

With the introduction of the vectors and strings from version 3.10.0, more complex interaction with files were introduced:
how to differ two iterations of a single vector and how to differentiate a double from a string. This depends highly on the
nature of the input/output file under consideration, whether it is just a text file used as database (in this case it depends
mostly on the way you’ve written the code that generate/parse it) or whether it corresponds to a more strict kind of file, for
instance a piece of code (c++/python/zsh). In the latter case, strings and vectors are not written in the same way. To take
this into account, a rule has been defined (commonly to both input and output files, both in the Launcher and Relauncher
module). There is a method for any kind of file to define properties of vector and string objects:
• setVectorProperties(string

```python
beg,
     string
             delim,
                    string
```

end): the first element is the string
beginning of the vector (usually “[” for python, “(” for zsh/sh, nothing…), the second one is the delimiter between
iterators (usually “,” for c++/python, blank for zsh/sh…) and the last one is the end of the string (usually the opposite
character of the beginning one).
• setStringProperties(string

```python
beg,
     string
```

end): the first and second elements are respectively the
beginning and ending character used for string (oftenly """).
Depending on the kind of chosen file, there is a default configuration chosen. This default is precised in the following two
sections.
Exclamation-Triangle Warning
The chosen output format has to be consistent with the output parameters investigated, particularly when some are
vectors which can be empty for some specific configurations. In this peculiar but still possible case, the abscence of
results is indeed a result of its own and should not be taken as a failure (from an incomplete output file for instance,
this specific aspect being further discussed later-on in Dealing with attributes).
Most of the time this would be independent of Uranie as it would be specific to the code under investigation, and as
such, it might be tricky to handle. Two use-case macro have been written to show this, so please take a look at empty
vectors considered as results in Macro “relauncherCodeMultiTypeKeyEmptyVectors.py” or considered as an error in
Macro “relauncherCodeMultiTypeKeyEmptyVectorsAsFailure.py” only because of the way the output Key-format output
file is written. In a nutshell, in the former case caution has been taken to properly delimit and condensate the
results so that even when the vector is empty there are sign of this, while on the other hand a simple dump is done
for every instance of the vector meaning that with no content, no dumping is done leading to Uranie stating that there
might be missing information in this output file (once again this is discussed in Dealing with attributes).

<!-- page 134 (PDF 141) -->
#### 8.3.3.3 Input file

Input file formats supported by TCodeEval objects, include:
• TFlatScript, Input file is created from scratch. Values are given in order separated by a blank separator. The
default behaviour with respect to strings and vectors for this file, is to look like the DataServer format (from the
Launcher module): strings have no specific beginning/ending characters, as for the vectors whose delimiter is chosen
to be a comma.
• TLineScript, Input file is created from scratch. Each TAttribute values are written on a specific line. Changing
attribute means changing line. It is the equivalent of the Column format (from the Launcher module).
• TKeyScript, Input file is created from an original file. Each TAttribute is associated to a keyword. Values are
substituted using a “keyword = value” pattern.
• TFlagScript, Input file is created from a template file. Each TAttribute is associated to a keyword. Each
keyword is substituted directly by the current value.
TXmlScript is not provided in this version
The addInput method is used to declare parameters for all these file types. For TFlatScript and TLineScript,
it takes a single argument: a pointer to a TAttribute object, while in the two other cases, the same first argument is
completed by a const char * for the key. The declaration order is only significant when no key is specified (so for the
TFlatScript and TLineScript files).

```python
# Input File Flat format case
finp1 = Relauncher.TFlatScript("input_rosenbrock_with_values_rows.dat")
finp1.addInput(x)
                   # Adding attributes in the correct order, one-by-one
finp1.addInput(y)
# Or Input File Key format case
kinp1 = Relauncher.TKeyScript("input_rosenbrock_with_keys.dat")
kinp1.addInput(x, "x")
                        # Adding attributes in the correct order, one-by-one
kinp1.addInput(y, "y")
```

Once done, the input files are provided to the TCodeEval object, using the addInputFile method, as shown below:

```python
# Add to the TCodeEval
code = Relauncher.TCodeEval("rosenbrock -r")
                                              # put "rosenbrock -k" instead for key
code.addInputFile(finp1)
                          # put kinp1 instead for key
```

####  8.3.3.4 Output file

Output file formats supported by TCodeEval include:
• TFlatResult, Output file is made up of an header characterised by # as first line character, and a line of floats
separated by spaces. By default, it is constructed as the DataServer one (from Launcher module). One can consider
using a flat output file written over several lines (so constructed as a TOutputFileRow) but one needs to be very
careful about the fact that all attributes might not have the same number of entries (when dealing with vectors for
instance). This is discussed in the third item of Creation of input files without model files and in Objective. To do
this a specific method has to be called isMultiLine(string separ) which says to the class that the results are
written over many lines, and every field is separated by the string separ.
• TKeyResult, Value can be found on line composed with the key, a separator, the value and eventually a ; character.
A separator is composed with space, tab, = and : characters.
• TLineResult. All the values of a given TAttribute are written on a specific line. Changing attribute means
changing line. It is the equivalent of the Column format (from the Launcher module).

<!-- page 135 (PDF 142) -->
TXmlResult is not provided in this version
In a similar way of TInputFile, one should use the addOutput to declare parameters, the argument being the pointer
to the attribute under consideration for all these formats, pairing with the corresponding key when dealing with a TKeyResult
object. This step can be gathered in a single operation, as for the input file, using the setOutputs method. Here
is an example for the ongoing use-case.

```python
# Input File Flat format case
fout = Relauncher.TFlatResult("_output_rosenbrock_with_values_rows.dat")
fout.addOutput(ros)
# Or Input File Key format case
kout = Relauncher.TKeyResult("_output_rosenbrock_with_keys.dat")
kout.addOutput(ros, "ros")
```

Finally, use the addOutputFile method of TCodeEval to declare it:

```python
# Add output file to the TCodeEval
code.addOutputFile(fout)
                          # put kout instead for key
```

###  8.3.4 Evaluation functions composition

Composition offer the possibility to build an overall new kind of TEval from the succession of many others. It defines an
ordered sequence of evaluation functions. One important thing to notice is that composition does not deal with distribution
even if it is possible. It just applies sequentially all assessors and become really helpfull as the output of an assessor at the
i-Th rank can be used as input for the next assessor, the (i+1)-Th one. This is one by creating a TComposeEval object
as discussed briefly below.

#### 8.3.4.1 TComposeEval

This composer can be seen as an overall new assessor that is, usually provided to the runner (or to a master directly).
The constructor have no argument. The only important method is the addEval one that allows users to add evaluation
functions, keeping in mind that they should be called in the correct order, regarding what they expect (the only argument
of the function being a pointer to the assessor to be stacked to create the chain). Examples of composition can be found
in Macro “relauncherComposeMultitypeAndReadMultiType.py”.

## 8.4 TRun

The TRun sub-classes deals with the use of computer resources. Three modes are available:
• TSequentialRun: evaluations are computed sequentially on a single computer core.
• TThreadedRun: evaluations are computed using the computer multi-core resources. It uses the pthread library
with the shared memory paradigm. Using this runner prevents from using some assessor, as one should take care
of memory conflict.
• TMpiRun: evaluations are computed using a network of computers (usually multi-core) It uses the message passing
interface (MPI) library with a distributed memory paradigm.
If you run on a single node, you can use MPI or threads. MPI parallelisation is more expensive, but more generic (no
thread safe problem).

<!-- page 136 (PDF 143) -->
Exclamation-Triangle Warning
Disregarding the chosen solution to distribute the computation as long as it is parallelised (meaning whether one is
choosing thread or MPI) the number of allocated ressources (in the constructor or specify to the mpirun command)
should always be strickly greater than 1. CPU number 1 will always be the “master” that is dealing with the distribution
to its “slaves” and the gathering of all results.
The runner class hierarchy is smaller than the assessor one, as can be seen in Figure 8.3. It starts with the TRun class,
which is a pure virtual one in which few methods are given along with an integer to describe the number of CPUs.
Figure 8.3: Hierarchy of classes and structures for the runner part of the Relauncher module.

### 8.4.1 TSequentialRun

In this case, there is no distribution. If evaluations are fast, it remains the simplest way to run the evaluations. Here is the
interpretation of the inherited methods:
• startSlave: exits immediately,
• onMaster: tests is true
• and stopSlave: cleans TEval.
TSequentialRun constructor only has one argument, a pointer to a TEval object.

```python
# Creating the sequential runner
srun = Relauncher.TSequentialRun(code)
```

###  8.4.2 TThreadedRun

In this case, the program starts using a single resource (the main thread), then it launches evaluation on dedicated threads
(children), uses them and stops them before ending.
Threads use a shared memory paradigm: all threads have access to the same address space. All objects that are used are
defined by the main thread. Evaluation threads only use (or duplicate) them. It’s only the main thread that follows the
macro instructions, while its children only do the evaluation loop. Here is the interpretation of the inherited methods:
• startSlave starts some threads dedicated to evaluation (it is a unblocking operation), and then exits. These
threads loops for evaluations.
• As we are on the master thread, onMaster is true.

<!-- page 137 (PDF 144) -->
• stopSlave puts fake items for evaluation. When the thread gets it, it stops their evaluation loop and exits. Main
thread waits for all threads to be stopped.
TThreadedRun constructor has two arguments, a pointer to a TEval object and an integer. The second argument is the
number of threads that the user wants to use.

```python
# Creating the threaded runner
trun = Relauncher.TThreadedRun(code,4)
```

One important thing to take care is that the user evaluation function need to be thread safe. For example, with the old
ROOT5 interpreter, the rosenbrock macro (see Relauncher abstraction levels) cannot be distributed with thread. This is
because the user function is interpreted and the Root interpreter is not thread safe. You have to turn it in a compiled
format to make it works with threads.
Thread safe problems come usually with variable affectation. If two (or more) threads modify the same memory address
at the same time, the code expected behaviour is usually disturbed. It can be a global or static variable, an embedded
object working variable, a file descriptor, etc. Thread unsafe bug is difficult to squash. It may be necessary to clone objects
to avoid such problems.
Exclamation-Triangle Warning
One might want to use TDataServer objects in code of TCJitEval instances that would be distributed with a
TThreadedRun object. In this case, it is mandatory to call the method EnableThreadSafety() to remove all
dataserver and tree from the internal ROOT register which would induce race-condition. This can be done as below:

```python
import ROOT
ROOT.EnableThreadSafety()
```

###  8.4.3 TMpiRun

In this case, many processes are started on different nodes. MPI uses the distributed memory paradigm: each process
have is own address space. All processes run the same macro and define their own objects. If you create a big object in
the evaluation/master code section, all processes allocate it (this is why, generally, the main dataserver object is created
in the onMaster part to prevent from creating as many dataserver as there are slaves).
• the constructor calls MPI_Init for the initial process synchronisation. This step is automatical, as long as one is
running through the on-the-fly C++ compilator thanks to the root command or in python.
• startSlave either exits immediately for the master process (id=0) or starts evaluation loop for other ones.
• depending if we are on the master process or not, onMaster is true or false.
• stopSlave puts fake items for evaluation and then exits. Evaluation processes get it, stop their loop, exit from
startslave, and usually jump the master bloc instructions. Unlike threads, the master process is not waiting for
evaluation processes.
• the destructor calls MPI_Finalize for the final process synchronisation. In the specific case of python, where
ROOT and python (though the garbage collector approach) are arguing to destroy objects, a specific line (ROOT.
SetOwnership(run, True)) has to be added, as discussed in Macro.
TMpiRun constructor has one argument, a pointer to a TEval object.

```python
# Creating the threaded runner
mrun = Relauncher.TMpiRun(code)
```

To run a macro in a MPI context, you have to use the mpirun command. Here is a simple way to run our example:

<!-- page 138 (PDF 145) -->
```python
mpirun -n 8 python RosenbrockMacro.py
```

Here, we launch root on 8 cores (-n 8). The mpirun command has other options not mentioned here.
In general, one runs a MPI job on a cluster with a batch scheduler. The previous command is put in a shell script with
batch scheduler parameters. The ROOT macro does not use viewer, but saves results in a file. They will be analysed in a
post interactive session using all the ROOT facilities.
Exclamation-Triangle Warning
The TMpiRun implementation requires also at least 2 cores (one being the master and the other one the core on which
assessors are run). If only one core is provided, the loop will run infinitely.

#### 8.4.3.1 TBiMpiRun and TSubMpiRun

In some case, users want to use multi level of parallelism. Two examples are given in the use cases section : first one is an
optimization where each evaluation realizes an experiment design and launchs many evaluations and returns a overview
of values (max, min, mean) ; second one uses an MPI function (TPythonEval) for evaluation.
For a two level MPI, two classes are provided : TBiMpiRun and TSubMpiRun. TBiMpirun is the high level class and
splits MPI resources in different parts : one ressource for the TMaster and n resources for each TEval. TSubMpiRun
gives acces to the n ressources reserved for evaluation. For example with 16 resources, 1 resource is reserved for the
master and the rest can be splited in 3 parts of 5 resources each for evaluation. TBiMpiRun got an extra parameter, an
int defining the number of each evaluation resource. This number must be compatible with available resources (with 16
resources, it could be only 3 or 5).

## 8.5 TMaster

The object inheriting from the TMaster class has a supervisor role: it defines items to be evaluated, and treats these
evaluations. Usually, it is created with a TDataServer, and a TRun (TEval implicitly) that is used for evaluations. The
TMaster retrieves information both:
• from TDataServer, it extracts the declaration of the input variables.
• from TEval, it extracts extra parameters that will be computed for each item.
We could distinguish two cases depending of the TDataServer data:
• if it contains a header and data, the TMaster will complete items data by adding information (columns). This
happens most of the time when considering the pure launching aspect, meaning when using the TLauncher2
object, briefly defined below.
• if it contains only a header, it will be used as items definition parameters. The TMaster will fill it with its own items
(lines and columns). This case happens both for pure the launching aspect, given that a design-of-experiments will
be constructed at some point, but also for optimisation issues.
Disregarding the case, TMaster interface defines an abstract method, solverLoop, that runs the evaluation loop and
completes or fills the TDataServer data. This method is the one to properly start the analysis.

### 8.5.1 Dealing with attributes

Disregarding the kind of master considered (the TLauncher2, discussed briefly below or those introduced in the optimisation
part, in Problem definition for instance), there are common methods that are discussed below in order to simplify
or precise some important behaviour of your current analysis.

<!-- page 139 (PDF 146) -->
In simple problem, the TDataServer object and the ones deriving from TEval have input parameters that fit together. In
this case, you can use the addAllInputs method from the TEval class to define the TDataServer needed header (the
only argument being a pointer to the considered dataserver object). For more complex one, there might be a mismatch.
In other problem, one can distinguish between three kinds of situation:
• The TEval-based object is using few input parameters, one (or more) of which is requested to be set a constant
value for all the upcoming estimation. To do this properly, the parameter under consideration should be added to the
assessor but not to the dataserver. The method addConstantValue from the chosen TMaster inheriting object
is called with argument the pointer to the attribute and its value as second parameter. A third optionnal parameter
(set by default at false) specifies whether this value should be stored in the dataserver tuple at the end. This option
has been recently added as it might be better for bookkeeping to know what the underlying hypothesis was when the
computations were performed. An example of how to use this is provided in Macros Relauncher. This method has
also been implemented to be able to cope with vectors and strings but this implies to handle complicated concept
that are used internally, so we strongly recommand to contact us if you have no other choice.
• The TEval-based object (or more oftently the composition of evaluators) is using many internal parameters (attribute
that are created from one assessor and used by any other later on in the chain). If these parameters are
uninteresting for the final purpose of the analysis, they can be removed, simply by calling the addTemporary
method from the chosen TMaster inheriting object. The only argument is a pointer to the attribute under consideration
. Once more, an example of how to use this is provided in Macros Relauncher.
• Finally, in some pure launching problem (Sobol for instance), some TDataServer-objects have extra parameters
unused by the TEval. In this case, it means that the initial TDataServer is not empty and that the TMaster-object
is able to keep this parameters values, and completes the data by adding columns.

### 8.5.2 TLauncher2

TLauncher2 is a new version of TLauncher and TLauncherFunction using the relauncher classes. It’s a basic
implementation, and it has no extra method. The constructor takes the TMaster usual arguments: a TDataServer and
a TEval.

#### 8.5.2.1 Dealing with failure

From time to time, there might be problem when running a code. The source of these problems might differ from one
instance to another. In the Relauncher module one can consider different case:
• the command is returning a failure code. A convention for a command is to return 0 if all went well which means
that what should be done has been done while any other returned value can be considered as a way to inform that
a problem has been met. From the Uranie point of view, there is no way to know what kind of error is meant as it
is command dependent.
• the system function is returning other values. The command provided by the user is passed to the system C++
function and on top of the non-zero returning value (discussed above), there are few specific cases. Among these,
one can find the case where the command is not known (the user made a mistake in the TCodeEval definition) or
the command is suffering from an internal problem preventing from even reaching the exit (a segmentation fault for
instance). With most Linux platforms, the former returned code is 127 while the latter is 139. This interpretation
is just given for illustration purpose but unfornutatly no generalisation can be done.
• no output file is created. In this case, nothing can be done, all output variables will be missing and this might arise
even if the code is not returning any specific failing code (see the discussion above).
• One or more output variables are missing in the output file. This is special, as it can arise if the command has
stopped during the writting process, but this also can be coming from an empty vector whose output formatting has
not properly being taken care of. This is discussed in Various file format and illustrated in a use-case macro Macro
“relauncherCodeMultiTypeKeyEmptyVectorsAsFailure.py” because of the way the output Key-format output file is
written

<!-- page 140 (PDF 147) -->
All these problems will be considered as a failure from the command. As such, the input configuration will be discarded
and not stored in the final dataserver object. The following paragraph discussed the way to get back all failed configurations
.
Unlike in Dealing with attributes where all the methods are inherited from the TMaster class, the method setSaveEr-

```python
ror(TDataServer
```

*tdserror) has been implemented in order to help handling the command failures discussed
previously. Its only argument is a pointer to a dataserver object in which all failing configurations will be stored. Example
of its usage is shown in two use-case macros with the classical flowrate case in Various file format and illustrated
in a use-case macro Macro “relauncherCodeFlowrateSequentialFailure.py” and when an empty vector is interpreted as a
missing information because of the wrong output file formatting, see Macro “relauncherCodeMultiTypeKeyEmptyVectors
AsFailure.py”.
