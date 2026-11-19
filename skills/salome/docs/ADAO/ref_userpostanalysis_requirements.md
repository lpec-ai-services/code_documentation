<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_userpostanalysis_requirements.html -->

# 12.6. Requirements to describe a post-processing after an ADAO calculation

Results processing is usually needed after an ADAO calculation, to insert it in
a complete study. After execution of a calculation case, the main information
is the variable “*Analysis*” which contains a result of optimal estimation. In
addition, all calculation variables that have been requested in intermediate
storage are also available by means of the special algorithm variable
“*StoreSupplementaryCalculations*”.

The simplest processing is often represented by a few lines of Python, which
can easily be repeated or carried over between studies. But more complex
processing of results, in the full SALOME study environment, is often done by
explicit parts of additional post-processing, either in YACS nodes or by Python
commands in TUI, or other methods. It is therefore often interesting to
identify at least part of the calculations following the ADAO estimation, and
to associate them in the calculation case.

ADAO thus gives the ability to define a general post-processing for each
calculation case. This definition is done by indicating the commands to be
performed at the output of the ADAO calculation.

## 12.6.1. Save a dedicated post-processing

In the graphical interface EFICAS for ADAO, there are 3 convenient methods to
integrate a dedicated post-processing for an ADAO case. The method is chosen
using the “*FROM*” keyword of the main entry “*UserPostAnalysis*”, as shown in
the following figure:

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/eficas_userpostanalysis_nodetype.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/eficas_userpostanalysis_nodetype.png)
>
> ****Choose your input type for the recorded post-processing****

Post-processing can be provided as an explicit script (input of type
“*String*”), as a script contained in an external file (input of type
“*Script*”), or by using a template (input of type “*Template*”). Templates are
provided by default when using the graphical editor EFICAS for ADAO or the TUI
interface, and are detailed in the
[Inventory of simple templates of post-processing (”Template”)](#section-ref-userpostanalysis-templates) section that follows. These are
simple scripts that can be adapted by the user, either in the integrated case
editing step with EFICAS for ADAO, or in the schema editing step before
execution, to improve the performance of the ADAO calculation in the SALOME
execution supervisor.

In the ADAO TUI textual interface (see the [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui) section), the
same information can be given using the “*setUserPostAnalysis*” command. The
arguments of this command allow to define the treatment either as a template
(argument “*Template*”) referring to one of the scripts detailed in the part
[Inventory of simple templates of post-processing (”Template”)](#section-ref-userpostanalysis-templates), or as an explicit script
(argument “*String*”), or as a script contained in an external file (argument
“*Script*”)

## 12.6.2. General form of a script to define a dedicated post-processing

A set of post-processing commands is a special Python script, which is
automatically activated at the end of the estimation calculations in ADAO. Any
Python commands, which a user can add after a GUI calculation in ADAO, can be
part of this post-processing. Several command set templates are available by
default,essentially to give the simplest possible example of recording these
series.

To be usable in an automatic way, it is required that any call of the ADAO
calculation case, to recover a variable, is done only with the reserved name
“*ADD*”. As an example, here is a very simple script (very similar to the
“*ValuePrinter*” template), usable to display the value of the optimal
estimate:

```python
import numpy
xa = numpy.ravel(ADD.get('Analysis')[-1])
print('  === Analysis =',xa)
```

If the command “*ADD.get(…)*”, used to obtain a result variable, does not use
the reserved name “*ADD*” for the calculation case, then the call will lead to
a runtime error and will warn about the missing case name.

To illustrate, the declaration of a model, in TUI interface, is done by using
the command:

```python
ADD.setUserPostAnalysis(Template = "AnalysisPrinter")
```

Warning

If not using the default available templates, it is up to the user to make
carefully established function scripts or external programs that do not
crash before being registered as an “*observer*” function. The debugging
can otherwise be really difficult!

Hereinafter we give the identifier and the contents of all the available
simple templates.

## 12.6.3. Inventory of simple templates of post-processing (”*Template*”)

### 12.6.3.1. Modèle **AnalysisPrinter**

Print on standard output the optimal value.

```python
print('# Post-analysis')
import numpy
xa=ADD.get('Analysis')[-1]
print('Analysis',xa)
```

### 12.6.3.2. Modèle **AnalysisSaver**

Save the optimal value in a file available in the system temporary directory named ‘analysis.txt’.

```python
print('# Post-analysis')
import os.path, numpy, tempfile
tempdir=tempfile.gettempdir()
xa=ADD.get('Analysis')[-1]
f=os.path.join(tempdir,'analysis.txt')
print('Analysis saved in "%s"'%f)
numpy.savetxt(f,xa)
```

### 12.6.3.3. Modèle **AnalysisPrinterAndSaver**

Print on standard output and, in the same time save in a file available in the system temporary directory, the optimal value.

```python
print('# Post-analysis')
import os.path, numpy, tempfile
tempdir=tempfile.gettempdir()
xa=ADD.get('Analysis')[-1]
print('Analysis',xa)
f=os.path.join(tempdir,'analysis.txt')
print('Analysis saved in "%s"'%f)
numpy.savetxt(f,xa)
```

### 12.6.3.4. Modèle **AnalysisSeriePrinter**

Print on standard output the optimal value series.

```python
print('# Post-analysis')
import numpy
xa=ADD.get('Analysis')
print('Analysis',xa)
```

### 12.6.3.5. Modèle **AnalysisSerieSaver**

Save the optimal value series in a file available in the system temporary directory named ‘analysis.txt’.

```python
print('# Post-analysis')
import os.path, numpy, tempfile
tempdir=tempfile.gettempdir()
xa=ADD.get('Analysis')
f=os.path.join(tempdir,'analysis.txt')
print('Analysis saved in "%s"'%f)
numpy.savetxt(f,xa)
```

### 12.6.3.6. Modèle **AnalysisSeriePrinterAndSaver**

Print on standard output and, in the same time save in a file available in the system temporary directory, the optimal value series.

```python
print('# Post-analysis')
import os.path, numpy, tempfile
tempdir=tempfile.gettempdir()
xa=ADD.get('Analysis')
print('Analysis',xa)
f=os.path.join(tempdir,'analysis.txt')
print('Analysis saved in "%s"'%f)
numpy.savetxt(f,xa)
```
