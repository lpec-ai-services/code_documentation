# Overview: Uranie in a nutshell
<!-- source PDF pages 13-28 -->

<!-- page 6 (PDF 13) -->
OVERVIEW: URANIE IN A NUTSHELL
Abstract
This chapter introduces the global organisation of the Uranie software at a very large scale (module one) and
its main dependence: ROOT. Each and every Uranie modules is also briefly described in a specific section, before being
furthermore discussed later on.

## 1.1 Introducing Uranie

Uranie (the version under discussion here being v4.11.0) is a software dedicated to perform studies on uncertainty propagation
, sensitivity analysis and surrogate model generation and calibration, based on ROOT (the corresponding version
being v6.36.06).
As a result, Uranie benefits from numerous features of ROOT, among which:
• an interactive C++ interpreter (Cling), built on the top of LLVM and Clang;
• a Python interface (PyROOT);
• an access to SQL databases;
• many advanced data visualisation features;
• and much more…
In the following sections, the ROOT platform will be briefly introduced as well as the python interface it brings once the
Uranie classes are declared and known. The organisation of the Uranie platform is then introduced, from a broad scale,
giving access to more refined discussion within this documentation.

### 1.1.1 Uranie modules organisation

The platform consists of a set of so-called technical libraries, or modules (represented as green boxes in Figure 1.1),
each performing a specific task.

<!-- page 7 (PDF 14) -->
Figure 1.1: Organisation of the Uranie-modules (green boxes) in terms of inter-dependencies. The blue boxes represent
the external dependencies (discussed later on).
In the rest of this section each and every modules discussed in this documentation will be briefly described (in terms of
role and main components) starting with the DataServer one, which is the spine of the Uranie project, as shown in Figure
1.1. A more precise description will then be done in the dedicated other chapters.

#### 1.1.1.1 DataServer module

The DataServer library (cf The DataServer module) is the core of the Uranie platform. It describes the central element
of Uranie: the TDataServer. This object contains all the necessary information about the variables of a problem (such
as the names, units, probability laws, data files, and so on…) and allows to perform the very basic statistical operations.

#### 1.1.1.2 Sampler module

The Sampler library (cf The Sampler module) allows to create design-of-experiments using TDataServer’s attributes
which are random variables. There are a large variety of design-of-experiments some of which are only meant to be
called by more complicated methods.

<!-- page 8 (PDF 15) -->
#### 1.1.1.3 Launcher module

The Launcher library (cf The Launcher module) applies an analytic function or an external simulation code on the content
of a TDataServer. The TDataServer content can either result from a design-of-experiments generated using one of
the TSampler object, or can be loaded into from an external source (ASCII file, SQL database, etc…).

#### 1.1.1.4 Modeler module

The Modeler library (cf The Modeler Module) allows the construction of a surrogate model that links the output 𝑌and
the input factors 𝑋𝑖(for 𝑖= 1, . . . , 𝑛𝑋) (polynomial models, neural networks, …).

#### 1.1.1.5 Sensitivity module

The Sensitivity library (cf The Sensitivity module) allows to perform sensitivity analysis of one of the output response 𝑌
with respect to the input factors 𝑋𝑖(for 𝑖= 1, . . . , 𝑛𝑋). The very basic concepts of sensitivity analysis are introduced
as well in the introduction of this chapter while they are discussed a bit more thoroughly in [Bla17].

#### 1.1.1.6 Optimizer and Reoptimizer modules

The Optimizer and Reoptimizer libraries (cf The Optimizer module and The Reoptimizer module) are dedicated to
optimisation and model calibration. Model calibration consists in setting up the “degrees of freedom” of a model so
that future simulations will optimally fit an experimental database. The optimisation is a complex procedure and several
techniques are available to perform single-criterion or multi criteria one, with and without constraint.

#### 1.1.1.7 Relauncher module

The Relauncher library (cf The Relauncher module) is more a technical module that is used throughout the Uranie
platform to provide a general architecture for all parametric studies, allowing secure multi-processors and multi-thread
usage in a simple way.

#### 1.1.1.8 Calibration module

The Calibration library (cf The Calibration module) is more a dedicated module that is used to get the best estimations
of some of the parameter of a specific model under consideration. This module provides different techniques relying on
their own hypothesis on the model but all of these methods need data to perform this calibration.

### 1.1.2 External dependencies

Before starting with the internal organisation of the platform, this section is discussing the dependencies of the Uranie
platform. They are sorted in two categories: the compulsory and optional ones. The latter ones are shown as blue boxes
in Figure 1.1 and both types are listed and briefly discussed below.

#### 1.1.2.1 Compulsory dependencies

ROOT:
An oriented-object package that offers many possibilities for data handling, analysis, display… [BR97] Sources,
binaries and documentation are available at http://root.cern.ch (version used is v6.36.06)
Cmake:
Free and open-source software for managing the build process of compiled software [MH07]. It is available at
http://www.cmake.org/ (version used is v3.28.3)
CPPUnit:
Unit testing framework for C++ programming [FL02]. It is available at http://sourceforge.net/projects/cppunit/
(version used is v1.15.1)

<!-- page 9 (PDF 16) -->
#### 1.1.2.2 Optional dependencies

OPT++:
Libraries that include non linear optimisation algorithms written in C++ [MOHW07]. It is available at https:
//software.sandia.gov/opt++/ (version used is v2.4). It is mainly used for neural networks.
FFTW:
Library that computes discrete Fourier transform (DFT) (one or more dimensions), of arbitrary input size [FJ05].
It is available at http://www.fftw.org/ (version used is v3.3.10). It is mainly used for two methods in the Sensitivity
library.
NLopt:
Library for nonlinear optimisation [Joh]. It is available at http://ab-initio.mit.edu/nlopt (version used is v2.7.1). It
is mainly used for kriging and mono-criterion optimisation.
Boost:
It is a set of libraries used here to implement the low level functionality for coroutines in replacement of PCL
(Portable Coroutine Library) since V4.8.0. It is available at https://www.boost.org (version used is v1.83)
MPI:
(Message Passing Interface) Standardised and portable message-passing system needed to run parallel computing
[GFB+04]. It is available at http://www.open-mpi.org/ (version used is v3.1)
CUDA:
(Compute Unified Device Architecture) Parallel computing platform and pro- gramming model invented by
NVIDIA to harness the power of the graphics processing unit (GPU) [Nvi11] (version used is v13.0). If requested,
it should be used with the boost library, with a version greater than v1.83.

## 1.2 ROOT Environment

Uranie can be seen as a set of extension libraries for ROOT. As such, its traditional use is through the ROOT tools,
in particular the root command which offers a C++ interpreter. This is presented in this section. In the next section,
PyRoot will be presented.

### 1.2.1 Environment variables

Assuming you are in a ROOT enabled system, your shell environment probably defines ROOTSYS, PATH and LD_LI-
BRARY_PATH variables (unless they are installed in standard location). In order to use Uranie, assuming it is not installed
in standard or ROOT location, the environment variable LD_LIBRARY_PATH needs to be completed and must contain
the sub directory lib of the Uranie installation.
To achieve this, one can set the environment variable URANIESYS to Uranie’s installation directory. Then, depending on
the shell family used, the variable LD_LIBRARY_PATH can be updated as follows:
INFO-CIRCLE C Shell Family (csh, tcsh, etc.)

```python
##------ Uranie ------
setenv URANIESYS MyUranieInstallDirectory
setenv LD_LIBRARY_PATH ${URANIESYS}/lib:$LD_LIBRARY_PATH
```

INFO-CIRCLE Bourne Shell Family (sh, bash, etc.)

<!-- page 10 (PDF 17) -->
```python
##------ Uranie ------
export URANIESYS=MyUranieInstallDirectory
export LD_LIBRARY_PATH=${URANIESYS}/lib:$LD_LIBRARY_PATH
```

Uranie may need some external libraries that must be reachable via the LD_LIBRARY_PATH. You can adapt the former
script to take it into account. Uranie installation procedure provides a configuration script that tries to create a safe
environment.

### 1.2.2 ROOT interpreter and runtime compiler

Uranie can be used through the C++ interpreter of ROOT, either using the command line, or in batch mode, the successive
commands being stored in a file called a ROOT macro.
To run the macro "MyMacro.C" from a shell prompt, use the command:

```python
root -l MyMacro.C
```

The -l option prevents from launching the ROOT login window. Other options that may be useful are:
• -q: quit ROOT interpreter when the script is run.
• -b: run in batch mode (without DISPLAY)
These options are typically used when your job needs to be distributed.
To execute a Macro from the ROOT prompt, use the command:

```python
.x MyMacro.C
```

ROOT interpreter offers some facilities for macro writing. In particular, it takes care of loading the needed libraries, and
does not need the #include directives.
WARNING WITH ROOT6: The new versions of ROOT (from ROOT 6.0) is now using Cling the interpreter that
does also a compilation on the fly thanks to LLVM and Clang. It is now much more compliant with the C++ syntax that
previous version, allowing only few simplifications (some namespace loaded and include lines brought).
Another way to run a macro in a compile way is to append one or two “+” at the end of the script.

```python
root -l MyMacro.C+
```

A “+” compiles the macro if the source changes, while “++” forces a recompilation. From ROOT 6, this method does
not go faster that the “interpreted” one. The only difference remaining now is to produce easily a library (.so) file.
This runtime compiler still deals with libraries auto-load, but needs the #include directives. ROOT looks for include
files in standard location and in the $ROOTSYS/include directory. If Uranie is installed elsewhere, you have to specify
where to find its include files.
One way to do so is to use the .rootrc file. Here is an example:
INFO-CIRCLE .rootrc

```python
ACLiC.IncludePaths: -DJIT -I$URANIESYS/include -I/another/include/path
```

<!-- page 11 (PDF 18) -->
It defines a list of C++ compiler options that are added at compile time: -I adds an include path; -D defines a CPP macro.
This CPP macro can be used to write a single source code for both interpreted or compiled runs, hiding or showing part
of source lines (#include declarations for example).
Another way is to use the rootlogon.C file. If this file is available in the active directory, it will be systematically loaded
by ROOT before the application is launched. A more thorough discussion on this file can be found in Uranie namespace.
INFO-CIRCLE rootlogon.C

```python
gInterpreter->AddIncludePath("$URANIESYS/include");
gInterpreter->AddIncludePath("/another/include/path");
```

This allows both the interpreter and the compiler to find the needed files.
One important advantage of runtime compilation is that error messages are more easily understandable.

### 1.2.3 Standard compilation

For C++ enthusiasts, it is possible to use ROOT (and subsequently Uranie) as a set of libraries, and to compile an
executable. In this case, you have to take care of linked libraries. In order to help the user, ROOT provides a macro
that give many of the needed flag to perform the compilation, both to give the path to the headers and the path to the
libraries.

```python
g++ -o OutputName TheFileName.C
                                 `root-config --cflags --libs`
```

For this example:
• OutputName: the name of the resulting executable
• TheFileName.C: the C++ file containing the code
• root-config --cflags --libs: this command provides all the necessary flags to compile most of the macros
using ROOT.
This is a logic we acknowledge and try to follow as well for Uranie: if one wants to compile an Uranie macro, one can
use two flags.
• URANIECPPFLAG: it defines all the include path needed and add on top the ones from ROOT;
• URANIELDFLAG: it defines the linking option and path to library and add on top the ones from ROOT;
With this, an example of standalone compilation for a given macro UranieMacro.C will be:

```python
g++ -o OutputExecutable UranieMacro.C
                                       `echo ${URANIECPPFLAG} ${URANIELDFLAG}`
```

###  1.2.4 Uranie namespace

As for the vast majority of ROOT’s classes, Uranie’s classes started with a capital T (for instance “TFoo.h”, if a class
would be called “Foo”). Most of them inherit from TNamed, a generic class of ROOT which offers method for name and
title bookkeeping. This is an important feature of the way ROOT-files are written (the name being the tag used to write
or read any object and to handle them in memory). These classes belong to a specific namespace, in order to prevent
any mixing between ROOT and Uranie (even though in practice, the name of the new classes implemented in Uranie is
checked not to exist in ROOT for obvious safety and clarity reasons). Uranie defines many namespaces dedicated to the
different module already introduced in Uranie modules organisation.
• URANIE::DataServer ; the namespace associated with the DataServer library
• URANIE::Launcher ; the namespace associated with the Launcher library

<!-- page 12 (PDF 19) -->
• URANIE::Sampler ; the namespace associated with the Sampler library
• URANIE::Optimizer ; the namespace associated with the Optimizer library
• URANIE::Modeler ; the namespace associated with the Modeler library
• URANIE::Sensitivity ; the namespace associated with the Sensitivity library
• URANIE::Relauncher ; the namespace associated with the Relauncher library
• URANIE::MpiRelauncher ; the namespace associated with the Relauncher library once used with MPI
• URANIE::Calibration ; the namespace associated with the Calibration library
• URANIE::MetaModelOptim ; the namespace associated with the MetaModelOptim library
• URANIE::Reoptimizer ; the namespace associated with the Reoptimizer library
• URANIE::UncertModeler ; the namespace associated with the UncertModeler library
• URANIE::Reliability ; the namespace associated with the Reliability library
You can use the full qualified name to access to Uranie classes or use the using namespace directives to use the short
name.
Another way to use the short name is to use again the rootlogon.C macro. If done so, all macros could access Uranie
classes via the short name implicitly. Here is an example of rootlogon.C file:

```python
using namespace URANIE::DataServer;
using namespace URANIE::Launcher;
using namespace URANIE::Sampler;
using namespace URANIE::Optimizer;
using namespace URANIE::Modeler;
using namespace URANIE::UncertModeler;
using namespace URANIE::Sensitivity;
using namespace URANIE::Relauncher;
using namespace URANIE::Reoptimizer;
using namespace URANIE::Calibration;
using namespace URANIE::Reliability;
// using namespace URANIE::XMLProblem;
// using namespace URANIE::MpiRelauncher;
void rootlogon()
{
    gStyle->SetPalette(1);
    gStyle->SetOptDate(21);
    //General graphical style
    // Default colors
    int white = 0;
    int color = 30;
    //Legend
    gStyle->SetLegendBorderSize(0);
    gStyle->SetFillStyle(0);
    // Pads
    gStyle->SetPadColor(white);
```

<!-- page 13 (PDF 20) -->
```python
    gStyle->SetTitleFillColor(white);
    gStyle->SetStatColor(white);
}
/* ==================== Hint ====================
   Might be practical to store this in a convenient place (for instance
   your home directory) and to create an alias to make sure that you use
   only one rootlogon file independently of where you are.
   example : alias root="root -l ${HOME}/rootlogon.C"
   Many style issue can be set once and for all here.
   Warnings :
    => The name of the main function (in between the void and the () part)
    has to be the same as the name of the file (without extension).
    => If you intend to change this file name and make it a hidden file (let's
    say
         ${HOME}/.toto.C, the name of the main function would have to start with
    an underscore, so here it would be "void _toto()".
*/
```

The most generic solution to simply don’t have to bother with namespaces while possibly tuning root graphical options to
ones taste is to centralise this file and make it our own. By putting it somewhere central (for instance as a hidden file in
your home folder, something like ~/.rootlogon.C) it is possible to make an alias that could have two purposes:
INFO-CIRCLE C Shell Family (csh, tcsh, etc.)

```python
alias root root -l ~/.rootlogon.C
```

INFO-CIRCLE Bourne Shell Family (sh, bash, etc.)

```python
alias root="root -l ~/.rootlogon.C"
```

With this kind of alias, one can have two interesting by-products: on the one hand, there will be no splash screen anymore
(resulting from the “-l” option) while on the other hand, all the Uranie namespaces will be loaded along with your own
graphical preferences, if you have any.

### 1.2.5 Important modifications going from ROOT v5 to ROOT v6

This part summarises the important modifications that are brought when changing ROOT versions. This affects some of
the Uranie macros and if you’ve used Uranie before version 4.X, this part can be useful to understand the modifications
that will mainly affect the constructor of some Uranie’s objects.
The main subject is the way to handle function. As an example, we will considerer the “very” simple function that with
two inputs returns the sum of these two values (c.f. the Addition function below).

<!-- page 14 (PDF 21) -->
```python
void Addition(double *x, double *y)
{
    y[0] = x[0] + x[1] ;
}
```

In C++, within the Uranie framework, there are three ways to use this function in a macro, that would be called
analysis.C:
1. Having the function in a separated file MyFunction.C and load it through ROOT by calling

```python
gROOT->LoadMacro("MyFunction.C");
```

2. Having the function in a separated file MyFunction.C and include this file in the header of analysis.C as

```python
#include "MyFunction.C"
```

3. Having the function in the same file (analysis.C) before the main function.
This is common practice both for the 5 and 6 versions of ROOT.
From this, the way to handle this function is a little bit different going from one ROOT major-version (i.e. 5.X) to another
one (i.e. 6.X).
ROOT 5.X:
Disregarding the chosen option to read the function (1, 2, or 3 discussed above) the interpreter (CInt for these
versions of ROOT) is associating to the pointer of the function Addition (which is a pointer of the form (void
*)(double *, double*) a name, which it uses as a tag by CInt. The name is in this case “Addition”. For the
3 configuration defined up there, one can use the name and/or the pointer to access the function.
ROOT 6.X:
On the other hand, for these versions of ROOT, the interpreter is, as stated previously, a runtime compiler, so it
behaves very much like expected from properly C++ compiled code. When calling the function thanks to its pointer
(the (void *)(double *, double*) object) no information on a name is accessible. Compared to ROOT 5,
there is no pointer to the function if it is loaded through LoadMacro (which is perfectly logic from a C++ point of
view). The second and third access method can, on the other hand, use both the pointer and the name.
This obliges us to change several constructor that had been (over ?) simplified: in ROOT 5 versions, the compulsory
information were often just a pointer to the TDataServer object and either the name of the function or a pointer to
it. From this, if nothing else was specified, all current inputs in the TDataServer were used as inputs (this behaviour
could be changed usually providing at third argument) and the output variables were named using the tag taken from CInt
(this behaviour could be changed as well usually providing a fourth argument). Having no tag anymore from CInt when
running ROOT 6, the (usually) optional third and fourth arguments become now compulsory.

### 1.2.6 References

The ROOT environment [BR97] has already been under development for a long time now, it’s documentation is very well
advanced and is organised with different level of precision. One can indeed find many useful information in:
• The ROOT user guide (https://root.cern.ch/root/htmldoc/guides/users-guide/ROOTUsersGuideA4.pdf): useful
and relatively complete gathering of information. It might be helpful to keep it locally as a reference.
• The ROOT Class index (https://root.cern.ch/root/html/ClassIndex.html): Very complete description of all the
classes and their methods. One can spent hour passing through these pages to discover what’s doable using the
various objects. It is even possible to mask/show inherited method for sake of simplicity.
There are also many examples and macros that show how to handle the objects provided:
• The Howto website: https://root.cern.ch/howtos

<!-- page 15 (PDF 22) -->
• All the macro contained in the tutorial folder, installed once ROOT has been installed (check in the $ROOTSYS/tutorials
folder).

## 1.3 The Python Interface

Accessing Uranie tools is also possible using the Python language.
The PyROOT tool allows to access to ROOT classes from a Python command line or script. Uranie can benefit from this
tool as well. All the use-case macros provided in the previous version of this user manual are now available in Python in
Use-cases in Python.

### 1.3.1 Python version: greater than 3.8

From Uranie version 4.9, only Python greater than 3.8 can be used due to the use of ROOT version v6.32 (Python 2 is
deprecated). Two words of caution about this:
• The macros provided in Use-cases in Python have indeed been tested with Python 3 (upper than 3.8).
• Note, historically, from Uranie version 4.5 to v4.8, both Python 2 and 3 were used at the same time if it is installed
again a ROOT version from v6.20.00 to v6.28.06. In order to get this compatibility, it means that the printing
format has to be homogenised and this implies that from Uranie version 4.2, these macros might not be working
anymore for Python version below or equal to 2.6.
INFO-CIRCLE Possible python configuration on a Linux OS
When typing the following command on many present Linux OS

```python
ls -l `which python`
                      && ls -l `which python3`
```

one can get these lines

```python
lrwxrwxrwx. 1 root root 9
                           8 fÃ©vr.
                                     2023 /usr/bin/python -> ./python3
lrwxrwxrwx. 1 root root 10
                            8 fÃ©vr.
                                      2023 /usr/bin/python3 -> python3.11
```

Today’s operating systems usually embed both versions of python and many of these still use the version 2 as a reference
(see the block above with both python versions). Given the fact that one can have as many different python versions as
possible, it should be possible to specify which one is of interest for the ongoing installation. The following lines should
be used to specify the python version to be used, providing that the “dev” packages are indeed installed for this version:

```python
cmake ${PATH_TO_ROOT_SOURCES} -DPYTHON_EXECUTABLE=${PATH_TO_PYTHON_BIN} -DPYTHON_
```

˓→INCLUDE_DIR=${PATH_TO_PYTHON_INC}

```python
-DPYTHON_LIBRARY=${PATH_TO_PYTHON_LIB} ...
```

These three specific python flags should be used both for ROOT and Uranie in a coherent way in order to install both
platforms with a chosen Python’s version. To get the recommended cmake line both for ROOT and Uranie see the
README provided with the Uranie-sources.

### 1.3.2 Environment variables

In order to access ROOT and Uranie from Python, we need to ensure that some environment variables are properly set:
• $PYTHONPATH must contain the $ROOTSYS/lib directory, where $ROOTSYS is ROOT’s installation directory.
• $LD_LIBRARY_PATH must contain the $ROOTSYS/lib directory.

<!-- page 16 (PDF 23) -->
### 1.3.3 Using PyROOT

When the environment variables for Uranie and PyROOT are properly set, we can access to the classes as follows:

```python
# Load the ROOT module
import ROOT
# Create a new data server object
tds = ROOT.URANIE.DataServer.TDataServer("myTDS", "DataServer for python example")
# Add an attribute to the data server
tds.addAttribute(ROOT.URANIE.DataServer.TNormalDistribution("x", 0.0, 1.0))
# Create a sampler object
sampler = ROOT.URANIE.Sampler.TSampling(tds, "lhs", 1000)
# Generate data
sampler.generateSample()
# Display the histogram of attribute x
tds.draw("x")
```

This code should produce a graphic as the one displayed in Histogram produced using PyROOT
Figure 1.2: Histogram produced using PyROOT
The instructions above can be executed either through the Python command line, or be written in a file (myscript.py in the
example below) and run using the command:

```python
python -i myscript.py
```

The -i option allows to stay in the Python environment at the end of the execution. This prevents the produced image to
be automatically closed.

<!-- page 17 (PDF 24) -->
### 1.3.4 The PyURANIE interface

In the previous example, we can see that the access to Uranie’s classes is somewhat tedious. In order to ease the process,
a set of specific modules have been created. We call it the PyURANIE interface.
It is then possible to re-write the previous example using these specific modules:

```python
# Load the URANIE module
from ROOT import URANIE
# Load the DataServer and Sampler modules
from URANIE import DataServer, Sampler
# Create a new data server object
tds = DataServer.TDataServer("myTDS","DataServer for the python example")
# Add an attribute to the data server
tds.addAttribute( DataServer.TNormalDistribution("x", 0.0, 1.0) )
# Create a sampler object
sampler = Sampler.TSampling(tds, "lhs", 1000)
# Generate data
sampler.generateSample()
# Display the histogram of attribute x
tds.draw("x")
```

The access to ROOT classes is provided through the ROOT module.
The PyURANIE interface also allows to use the command:

```python
from URANIE.DataServer import *
```

This command loads all the classes of the DataServer module in Python and makes them directly accessible. It is similar to
the C++ command using namespace URANIE::DataServer. However, in Python, using this command is not recommended.
It can create name conflicts and use a large amount of memory.
Finally the equivalent of the rootlogon.C has been written for python, and is called rootlogon.py. It is composed
of two parts, as for the one in C++, the second one being the exact equivalent. The first one, on the other hand, is a bit
different and this difference arises from the way the language are dealing with loading modules. By doing

```python
from rootlogon import DataServer
```

one can, for instance, directly creates a TDataServer by doing

```python
toto=DataServer.TDataServer()
```

The example of rootlogon file for python is the following:

```python
import ROOT
# Create shortcuts if uranie exists
urasys = ROOT.TString(ROOT.gSystem.Getenv("URANIESYS"))
if not urasys.EqualTo(""):
    from ROOT.URANIE import DataServer as DataServer
```

<!-- page 18 (PDF 25) -->
```python
    from ROOT.URANIE import Sampler as Sampler
    from ROOT.URANIE import Launcher as Launcher
    from ROOT.URANIE import Relauncher as Relauncher
    from ROOT.URANIE import Reoptimizer as Reoptimizer
    from ROOT.URANIE import Sensitivity as Sensitivity
    from ROOT.URANIE import Optimizer as Optimizer
    from ROOT.URANIE import Modeler as Modeler
    from ROOT.URANIE import Calibration as Calibration
    from ROOT.URANIE import UncertModeler as UncertModeler
    from ROOT.URANIE import Reliability as Reliability
    from ROOT.URANIE import XMLProblem as XMLProblem
    from ROOT.URANIE import MpiRelauncher as MpiRelauncher
    pass
# General graphical style
white = 0
# PlotStyle
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptDate(21)
# Legend
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetFillStyle(0)
# Pads
ROOT.gStyle.SetPadColor(white)
ROOT.gStyle.SetTitleFillColor(white)
ROOT.gStyle.SetStatColor(white)
   ====================
                         Hint ====================
     Might be practical to store this in a convenient place (for instance
     the ".python" folder in your home directory) or any other place where
     your $PYTHONPATH is pointing.
     example : export PYTHONPATH=$PYTHONPATH:${HOME}/.mypython/
     It should then be called as "from rootlogon import " + the list of module
     This would replace the shortcuts created and import done in the rest of
     the scripts
     Many style issue can be set once and for all here.
     toto=DataServer.TDataServer()
```

###  1.3.5 FAQ: a Python handbook to interact with Uranie

This section introduces some frequently asked methods to help handling data and objects (as many objects proposed are
either ROOT or C++-based). Some of these methods are used throughout the examples in the macros in Use-cases in
Python, but the aim here is to gather everything that might be of use for a python user that would like to put his hand on
Uranie. Most of this methods rely on ROOT version being greater than 6.20 but the modification are small if one uses

<!-- page 19 (PDF 26) -->
older versions (as long as it is greater than6).

#### 1.3.5.1 TDataServer <-> array conversion

This section describes how to convert a TDataServer into a numpy.array and vice-versa. A breakdown of the macro
show below can be found in Macro “howtoConvertTDataServerArray.py”

```python
"""
Example of TDataServer into numpy array converter
"""
import numpy as np
from URANIE import DataServer
# import data into a dataserver
tds = DataServer.TDataServer("tds", "pouet")
tds.fileDataRead("myData.dat")
print("Dumping tds")
tds.scan()
# Define the list of variable to be read
VarList = "x:y"
# Create an array by defining the shape and the type (this array is a matrix)
TdsData = np.empty(shape=(tds.getNPatterns(), len(VarList.split(":"))),
                   dtype=np.float64)
# Dump the data into the created array (the last field empty unless a select is done␣
```

˓→on the sample)

```python
tds.getTuple().extractData(TdsData, TdsData.size, VarList, tds.getCut().GetTitle())
# Check the content
print("Dumping the array")
print(TdsData)
# Create a new Dataserver and feed it
tds2 = DataServer.TDataServer("brandnew", "pouet")
# Add the attribute in the dataserver and create the tuple
for name in VarList.split(":"):
    index = VarList.split(":").index(name)
    VarData = np.ascontiguousarray(TdsData.transpose()[index])
    tds2.addAttributeUsingData(name, VarData, VarData.size)
print("Dumping new tds")
tds2.Scan("*")
```

The macro shown above, is an example of how to convert the content stored in a TDataServer and its result is discussed
in Macro “howtoConvertTDataServerArray.py”.

#### 1.3.5.2 TMatrixD <-> array conversion

This section describes how to convert a TMatrixD into a numpy.array and vice-versa. A breakdown of the macro show
below can be found in Macro “howtoConvertTMatrixDArray.py”

```python
"""
Example of TMatrix into numpy array conversion
```

<!-- page 20 (PDF 27) -->
```python
"""
import numpy as np
import ROOT
# define the number of rows and columns
nrow = 3
ncol = 5
# Initialise and fill a TMatrixD
InMat = ROOT.TMatrixD(nrow, ncol)
for i in range(nrow):
    for j in range(ncol):
        InMat[i][j] = ROOT.gRandom.Gaus(0, 1)
print("Original TMatrixD")
InMat.Print()
# Create the ndarray with the good shape
mat_version = np.frombuffer(InMat.GetMatrixArray(), dtype=np.float64,
                            count=nrow*ncol).reshape(nrow, ncol)
print("Numpy array transformation")
print(mat_version)
# Back to another TMatrixD
OutMat = ROOT.TMatrixD(nrow, ncol)
OutMat.SetMatrixArray(mat_version)
print("\nRecreated TMatrixD")
OutMat.Print()
```

The macro shown above, is an example of how to convert the content stored in a TMatrixD but also how to go from a
numpy.array back to TMatrixD if one needs to provide this to an Uranie’s method. Its result is discussed in Macro
“howtoConvertTMatrixDArray.py”.

#### 1.3.5.3 Use a C++ function interactively

This section describes how to use a C++ function within the python framework. The idea is that every of our surrogate
model discussed later-on on can be exported in C++ and so they can be used either throughout the Uranie classes (for
instance to evaluate a set of new points) or, for single evaluation, in either C++ or python. This macro will focus on the
latter part. This macro is also detailled Macro “howtoLoadFunction.py”.

```python
"""
Example of C++ function in python
"""
import numpy as np
import ROOT
# Loading a function
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Preparing inputs and outputs
inp = np.array([1.2, 0.8])
                            # input values
out = np.zeros(4)
                   # output values initialise with 4 zeros
```

<!-- page 21 (PDF 28) -->
```python
# Call the method, through the ROOT interface
ROOT.operation(inp, out)
# Print the result
print("Results are")
print(out)
```

The macro shown above, is an example of how to load a function and use it in a single-point estimation. Its result is
discussed in Macro “howtoLoadFunction.py”.

#### 1.3.5.4 Pass argument “by-reference”

This sections shows how to use function that would have been defined using the “by-reference” prototype, which is specific
to C++. This macro is also detailled Macro “howtoPassReference.py”.

```python
"""
Example of C++style reference usage
"""
from ctypes import c_double
                             # for ROOT version greater or equal to 6.20
from URANIE import DataServer
# create a dataserver and read data
tds = DataServer.TDataServer("pouet", "foo")
tds.fileDataRead("myData.dat")
# compute quantile (this method get the results 'by reference')
proba = 0.9
             # ROOT.Double(0.9) for ROOT version lower than 6.20
quant = c_double(0.0)
                       # ROOT.Double(0.0) for ROOT version lower than 6.20
# Compute the quantile and dump the value returned by reference
tds.computeQuantile("x", proba, quant)
print("Result is ")
print(quant.value)
```

The macro shown above, is an example of how to load a function and use it in a single-point estimation. Its result is
discussed in Macro “howtoPassReference.py”.

### 1.3.6 References

The PyROOT environment has a few specificities which it is preferable to be aware of (the rest being discussed already
in References). The following websites help to learn about them:
• Presentation on the PyROOT website: http://root.cern.ch/drupal/content/pyroot
• The PyROOT Manual: http://wlav.web.cern.ch/wlav/pyroot/index.html
• The ROOT users forum: http://root.cern.ch/phpBB3/index.php
Finally, reference [Gil09] introduces (in French) some of these problems and shows examples on how to use Uranie with
PyROOT.
