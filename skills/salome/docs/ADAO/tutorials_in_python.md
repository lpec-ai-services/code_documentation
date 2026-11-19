<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/tutorials_in_python.html -->

# 6. **[DocU]** Tutorials on using the ADAO module in Python

This section presents some examples on using the ADAO module in Python. The
first one shows how to build a very simple data assimilation case defining
explicitly all the required input data through the textual user interface (TUI)
described in [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). The second one shows, on the same case, how to
define input data using external sources through scripts. We describe here
always Python scripts because they can be directly inserted in script
definitions of Python interface, but external files can use other languages.

These examples are intentionally described in the same way than for the
[[DocU] Tutorials on using the ADAO module in SALOME](tutorials_in_salome.md#section-tutorials-in-salome) because they are similar to the ones that
can be treated in the graphical user interface in SALOME. A scripted form of a
case built in the GUI can be obtained directly using the TUI export button
[![eficas_totui](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/eficas_totui.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/eficas_totui.png) integrated in the interface. The mathematical notations used
afterward are explained in the section [[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory).

Other simple examples, and their accompanying illustrations, are included at
the end of the reference documentation of some algorithms. It is the case, in a
non-limitative way, of [Calculation algorithm “3DVAR”](ref_algorithm_3DVAR.md#section-ref-algorithm-3dvar),
[Calculation algorithm “KalmanFilter”](ref_algorithm_KalmanFilter.md#section-ref-algorithm-kalmanfilter) and
[Calculation algorithm “ExtendedBlue”](ref_algorithm_ExtendedBlue.md#section-ref-algorithm-extendedblue).

## 6.1. Building an estimation case with explicit data definition

This very simple example is a demonstration one, and describes how to set a
BLUE estimation framework in order to get the *fully weighted least square
estimated state* of a system from an observation of the state and from an *a
priori* knowledge (or background) of this state. In other words, we look for
the weighted middle between the observation and the background vectors. All the
numerical values of this example are arbitrary.

### 6.1.1. Experimental setup

We choose to operate in a 3-dimensional observation space, that is, we deal
with 3 simple measures. The 3 dimensionality is chosen in order to restrict the
size of numerical object to be explicitly entered by the user, but the problem
is not dependent of the dimension and can be set in observation dimension of
10, 100, 1000… The observation $\mathbf{y}^o$ is of value 1 in each
direction, so:

```python
Yo = [1 1 1]
```

The background state $\mathbf{x}^b$, which represent some *a priori*
knowledge or a mathematical regularization, is chosen of value of 0 in each
case, which leads to:

```python
Xb = [0 0 0]
```

Data assimilation requires information on errors covariances $\mathbf{R}$
and $\mathbf{B}$, respectively for observation and background error
variables. We choose here to have uncorrelated errors (that is, diagonal
matrices) and to have the same variance of 1 for all variables (that is,
identity matrices). We set:

```python
B = R = Id = [1 0 0 ; 0 1 0 ; 0 0 1]
```

Last, we need an observation operator $\mathbf{H}$ to convert the
background value in the space of observation values. Here, because the space
dimensions are the same and because we state a linear selection operator, we
can choose the identity as the observation operator:

```python
H = Id = [1 0 0 ; 0 1 0 ; 0 0 1]
```

With such choices, the “Best Linear Unbiased Estimator” (BLUE) will be the
average vector between $\mathbf{y}^o$ and $\mathbf{x}^b$, named the
*analysis*, denoted by $\mathbf{x}^a$, and its value is:

```python
Xa = [0.5 0.5 0.5]
```

As an extension of this example, one can change the variances represented by
$\mathbf{B}$ or $\mathbf{R}$ independently, and the analysis
$\mathbf{x}^a$ will move to $\mathbf{y}^o$ or to
$\mathbf{x}^b$, in inverse proportion of the variances in
$\mathbf{B}$ and $\mathbf{R}$. As an other extension, it is also
equivalent to search for the analysis thought a “Blue” algorithm or a “3DVAR”
one.

### 6.1.2. Using the graphical interface (GUI) to build the ADAO case

We have to set the variables to build the ADAO case by using the experimental
set up described above. All the technical information given above will be
directly inserted in the ADAO case definition, by using as required a list, a
vector or a string for each variable. We refer to the reference documentation
[[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). It will build an ADAO case, that can be saved as a standard
Python file.

The header of the file has to state the usual settings:

```python
from adao import adaoBuilder
case = adaoBuilder.New()
case.set( 'AlgorithmParameters', Algorithm='Blue' )
```

The definition of the observations and of the error covariances are the
following:

```python
case.set( 'Observation',         Vector=[1, 1, 1] )
case.set( 'ObservationError',    Matrix="1 0 0 ; 0 1 0 ; 0 0 1" )
```

In the same way, the *a priori* information is defined with its error
covariances by:

```python
case.set( 'Background',          Vector=[0, 0, 0] )
case.set( 'BackgroundError',     Matrix="1 0 0 ; 0 1 0 ; 0 0 1" )
```

The observation operator, very simple and here linear, can be defined by:

```python
case.set( 'ObservationOperator', Matrix="1 0 0 ; 0 1 0 ; 0 0 1" )
```

To get an automatic printing of the optimal analyzed state, one can add an
“*observer*” command, or add after execution some commands to treat the data
assimilation results. In this very simple case, one can just add:

```python
case.set( 'Observer',            Variable="Analysis", Template="ValuePrinter" )
```

The execution is then extremely simple to state and consist in the command
line, eventually in the saving file:

```python
case.execute()
```

The result of the execution of these commands (either at Python prompt, through
the “*shell*” command of SALOME, in the Python prompt of the interface, or by
the script execution menu) is the following:

```python
Analysis [0.5 0.5 0.5]
```

as shown here:

```python
adao@python$ python
Python 3.6.5 (default, Feb 01 2019, 12:12:12)
[GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from adao import adaoBuilder
>>> case = adaoBuilder.New()
>>> case.set( 'AlgorithmParameters', Algorithm='Blue' )
>>> case.set( 'Observation',         Vector=[1, 1, 1] )
>>> case.set( 'ObservationError',    Matrix="1 0 0 ; 0 1 0 ; 0 0 1" )
>>> case.set( 'Background',          Vector=[0, 0, 0] )
>>> case.set( 'BackgroundError',     Matrix="1 0 0 ; 0 1 0 ; 0 0 1" )
>>> case.set( 'ObservationOperator', Matrix="1 0 0 ; 0 1 0 ; 0 0 1" )
>>> case.set( 'Observer',            Variable="Analysis", Template="ValuePrinter" )
>>> case.execute()
Analysis [0.5 0.5 0.5]
0
>>>
```

As a simple extension of this example, one can notice that the same problem
solved with a “3DVAR” algorithm gives the same result. This algorithm can be
chosen at the ADAO case building step by only changing the “*Algorithm*”
argument on the beginning. The remaining parts of the ADAO case in “3DVAR” is
exactly similar to the BLUE algorithmic case.

## 6.2. Building an estimation case with external data definition by scripts

It is useful to get parts or all of the ADAO case data from external
definition, using Python script files to provide access to the data. As an
example, we build here an ADAO case representing the same experimental setup as
in the above example [Building an estimation case with explicit data definition](#section-tutorials-in-python-explicit), but using
data from a single one external Python script file.

First, we write the following script file, using conventional names for the
required variables. Here, all the input variables are defined in the same
script, but the user can choose to split the file in several ones, or to mix
explicit data definition in the ADAO textual interface and implicit data
definition by external files. The present script file looks like:

```python
import numpy
#
# Definition of the Background as a vector
# ----------------------------------------
Background = [0, 0, 0]
#
# Definition of the Observation as a vector
# -----------------------------------------
Observation = "1 1 1"
#
# Definition of the Background Error covariance as a matrix
# ---------------------------------------------------------
BackgroundError = numpy.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
#
# Definition of the Observation Error covariance as a matrix
# ----------------------------------------------------------
ObservationError = numpy.matrix("1 0 0 ; 0 1 0 ; 0 0 1")
#
# Definition of the Observation Operator as a matrix
# --------------------------------------------------
ObservationOperator = numpy.identity(3)
```

The names of the Python variables above are mandatory, in order to define the
right ADAO case variables, but the Python script can be bigger and define
classes, functions, file or database access, etc. with other names. Moreover,
the above script shows different ways to define arrays and matrices, using
list, string (as in Numpy or Octave), Numpy array type or Numpy matrix type,
and Numpy special functions. All of these syntax are valid.

After saving this script in a file (named here “*script.py*” for the example)
somewhere in your path, we use the textual interface (TUI) to build the ADAO
case. The procedure to fill in the case is similar to the previous example
except that, instead of selecting the “*Vector*” or “*Matrix*” option to build
each variable, one choose the “*Script*” option setting simultaneously the
“*Vector*” or “*Matrix*” type of the variable. This leads to the following
commands (either at Python prompt, through the “*shell*” command of SALOME, in
the Python prompt of the interface, or by the script execution menu):

```python
adao@python$ python
Python 3.6.5 (default, Feb 01 2019, 12:12:12)
[GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from adao import adaoBuilder
>>> case = adaoBuilder.New()
>>> case.set( 'AlgorithmParameters', Algorithm='Blue' )
>>> case.set( 'Observation',         Vector=True, Script="script.py" )
>>> case.set( 'ObservationError',    Matrix=True, Script="script.py" )
>>> case.set( 'Background',          Vector=True, Script="script.py" )
>>> case.set( 'BackgroundError',     Matrix=True, Script="script.py" )
>>> case.set( 'ObservationOperator', Matrix=True, Script="script.py" )
>>> case.set( 'Observer',            Variable="Analysis", Template="ValuePrinter" )
>>> case.execute()
Analysis [0.5 0.5 0.5]
0
>>>
```

Other steps and results are exactly the same as in the [Building an estimation
case with explicit data definition](#building-an-estimation-case-with-explicit-data-definition) previous example.

In fact, this script methodology is the easiest way to retrieve data from
in-line or previous calculations, from static files, from database or from
stream, all of them inside or outside of SALOME. It allows also to modify
easily some input data, for example for debug purpose or for repetitive
execution process, and it is the most versatile method in order to parametrize
the input data. **But be careful, script methodology is not a “safe” procedure,
in the sense that erroneous data, or errors in calculations, can be directly
injected into the ADAO case execution. The user have to carefully verify the
content of his scripts.**
