<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_output_variables.html -->

# 11.3. Variables and information available at the output

## 11.3.1. How to obtain the information available at the output

At the output, after executing data assimilation, optimization or checking
study, there are variables and information originating from the calculation. The
obtaining of this information is then carried out in a standardized way using
the post-processing step of calculation.

The step is easily identified by the user into its ADAO definition case (by the
keyword “*UserPostAnalysis*”) or in its YACS execution scheme (by nodes or
blocks located after the calculation block, and graphically connected to the
output port “*algoResults*” of the calculation block):

1. In the case where the user defines the post-processing in his ADAO case, it uses an external script file or commands in the field type “*String*” or “*Template*”. The script it provides has a fixed variable “*ADD*” in the namespace.
2. In the case where the user defines the post-processing in its YACS scheme by a Python node located after the block of calculation, it should add a input port of type “*pyobj*” named for example “*Study*”, graphically connected to the output port “*algoResults*” of the calculation block. The Python post-processing node must then start with `ADD = Study.getResults()`.

Templates are given hereafter as [Examples of Python scripts to obtain or treat the outputs](#subsection-r-o-v-template). In all cases,
the post-processing of the user has in the namespace a variable whose name is
“*ADD*”, and whose only available method is named `get`. The arguments of this
method are an output information name, as described in an
[Inventory of potentially available information at the output](#subsection-r-o-v-inventaire).

For example, to have the optimal state after a data assimilation or optimization
calculation, one use the following call:

```python
ADD.get("Analysis")
```

This call returns a list of values of the requested notion (or, in the case of
input variables that are by nature only a unique specimen, the value itself).
One can then request a particular item in the list by the standard list commands
(especially `[-1]` for the last, and `[:]` for all items).

## 11.3.2. Examples of Python scripts to obtain or treat the outputs

These examples present Python commands or scripts which allow to obtain or to
treat the output of an algorithm run. To help the user, they are directly
available in the user interface, when building the ADAO case in the embedded
case editor, in the “*Template*” type fields. In an equivalent way, these
commands can be integrated in an external user script (and inserted in the ADAO
case by a “*Script*” type input) or can exist as a string, including line feeds
(and inserted in the ADAO case by a “*String*” type input). Lot of variants can
be build from these simple examples, the main objective being to help the user
to elaborate the exact procedure he needs in output.

The first example (named “*AnalysisPrinter*” in the inputs of type “*Template*”
for “*UserPostAnalysis*” section) consists in printing, in the standard log
output, the value of the analysis or the optimal state, noted as
$\mathbf{x}^a$ in the section [[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory). It is realized by
the commands:

```python
import numpy
xa=numpy.ravel(ADD.get('Analysis')[-1])
print('Analysis:',xa)
```

The `numpy.ravel` function is here to be sure that the `xa` variable will
contain a real unidimensional vector, whatever the previous computing choices
are.

A second example (named “*AnalysisSaver*” in the inputs of type “*Template*”
for “*UserPostAnalysis*” section) consists in saving on file the value of the
analysis or the optimal state $\mathbf{x}^a$. It is realized by the
commands:

```python
import numpy
xa=numpy.ravel(ADD.get('Analysis')[-1])
f='/tmp/analysis.txt'
print('Analysis saved in "%s"'%f)
numpy.savetxt(f,xa)"
```

The chosen recording file is a text one named `/tmp/analysis.txt`.

It is easy to combine these two examples by building a third one (named
“*AnalysisPrinterAndSaver*” in the inputs of type “*Template*” for
“*UserPostAnalysis*” section). It consists in simultaneously printing in the
standard log output and in saving on file the value of $\mathbf{x}^a$. It
is realized by the commands:

```python
import numpy
xa=numpy.ravel(ADD.get('Analysis')[-1])
print('Analysis:',xa)
f='/tmp/analysis.txt'
print('Analysis saved in "%s"'%f)
numpy.savetxt(f,xa)
```

To facilitate these examples extension for user needs, we recall that all the
SALOME functions are available at the same level than these commands. The user
can for example request for graphical representation with the PARAVIS [[1]](#id3) or
other modules, for computing operations driven by YACS [[2]](#id4) or an another
module, etc.

Other usage examples are also given for [STEP 4: Supplement and modify the YACS scheme, and save it](gui_in_salome.md#section-u-step4) of the
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome) section, or in part [[DocU] Tutorials on using the ADAO module in SALOME](tutorials_in_salome.md#section-tutorials-in-salome).

## 11.3.3. Cross compliance of the information available at the output

The availability of information after the calculation is conditioned by the fact
that they have been calculated or requested.

Each algorithm does not necessarily provide the same information, and not
necessarily for example uses the same intermediate quantities. Thus, there is
information that are always present such as the optimal state resulting from the
calculation. The other information are only present for certain algorithms
and/or if they have been requested before the execution of the calculation.

It is recalled that the user can request additional information during the
preparation of its ADAO case, using the optional control “*AlgorithmParameters*” of
ADAO case. Reference will be made to the
[Description of options of an algorithm by “AlgorithmParameters”](ref_options_AlgorithmParameters.md#section-ref-options-algorithm-parameters) for the proper use of this
command, and to the description of each algorithm for the information available
by algorithm. One can also ask to keep some input information by changing the
boolean “* * Stored” associated with it in the edition of the ADAO case.

## 11.3.4. Inventory of potentially available information at the output

The main set of potentially available information at the output is listed here
regardless of algorithms, for inventory. One has to look directly to algorithm
details to get full inventory.

The optimal state is an information that is always naturally available after an
optimization or a data assimilation calculation. It is indicated by the
following keywords:

> Analysis
> :   *List of vectors*. Each element of this variable is an optimal state
>     $\mathbf{x}^*$ in optimization, an interpolate or an analysis
>     $\mathbf{x}^a$ in data assimilation.
>
>     Example:
>     `xa = ADD.get("Analysis")[-1]`

The following variables are input variables. They are made available to the
user at the output in order to facilitate the writing of post-processing
procedures, and are conditioned by a user request using a boolean “*Stored*”
at the input. All these returned input variables can be obtained with the
standard command “.get(…)”, which return the unique object given on input.

> Background
> :   *Vector*. The variable indicates the background or initial vector used,
>     previously noted as $\mathbf{x}^b$. Its value is defined as a
>     “*Vector*” or “*VectorSerie*” type object. Its availability in output is
>     conditioned by the boolean “*Stored*” associated with input.
>
> BackgroundError
> :   *Matrix*. This indicates the background error covariance matrix, previously
>     noted as $\mathbf{B}$. Its value is defined as a “*Matrix*” type
>     object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
>     type object, as described in detail in the section
>     [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
>     conditioned by the boolean “*Stored*” associated with input.
>
> EvolutionError
> :   *Matrix*. The variable indicates the evolution error covariance matrix,
>     usually noted as $\mathbf{Q}$. It is defined as a “*Matrix*” type
>     object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
>     type object, as described in detail in the section
>     [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
>     conditioned by the boolean “*Stored*” associated with input.
>
> Observation
> :   *List of vectors*. The variable indicates the observation vector used for
>     data assimilation or optimization, and usually noted $\mathbf{y}^o$.
>     Its value is defined as an object of type “*Vector*” if it is a single
>     observation (temporal or not) or “*VectorSeries*” if it is a succession of
>     observations. Its availability in output is conditioned by the boolean
>     “*Stored*” associated in input.
>
> ObservationError
> :   *Matrix*. The variable indicates the observation error covariance matrix,
>     usually noted as $\mathbf{R}$. It is defined as a “*Matrix*” type
>     object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
>     type object, as described in detail in the section
>     [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
>     conditioned by the boolean “*Stored*” associated with input.

All other information are conditioned by the algorithm and/or the user requests
of availability. The main ones are the following, without being exhaustive, in
alphabetical order:

> APosterioriCorrelations
> :   *List of matrices*. Each element is an *a posteriori* error correlations
>     matrix of the optimal state, coming from the $\mathbf{A}$ covariance
>     matrix. In order to get them, this *a posteriori* error covariances
>     supplementary calculation has to be requested at the same time by the keyword
>     “APosterioriCovariance”.
>
>     Example:
>     `apc = ADD.get("APosterioriCorrelations")[-1]`
>
> APosterioriCovariance
> :   *List of matrices*. Each element is an *a posteriori* error covariance
>     matrix $\mathbf{A}$ of the optimal state.
>
>     Example:
>     `apc = ADD.get("APosterioriCovariance")[-1]`
>
> APosterioriStandardDeviations
> :   *List of matrices*. Each element is an *a posteriori* error standard errors
>     diagonal matrix of the optimal state, coming from the $\mathbf{A}$
>     covariance matrix. In order to get them, this *a posteriori* error
>     covariances supplementary calculation has to be requested at the same time by
>     the keyword “APosterioriCovariance”.
>
>     Example:
>     `aps = ADD.get("APosterioriStandardDeviations")[-1]`
>
> APosterioriVariances
> :   *List of matrices*. Each element is an *a posteriori* error variance errors
>     diagonal matrix of the optimal state, coming from the $\mathbf{A}$
>     covariance matrix. In order to get them, this *a posteriori* error
>     covariances supplementary calculation has to be requested at the same time by
>     the keyword “APosterioriCovariance”.
>
>     Example:
>     `apv = ADD.get("APosterioriVariances")[-1]`
>
> BMA
> :   *List of vectors*. Each element is a vector of difference between the
>     background and the optimal state.
>
>     Example:
>     `bma = ADD.get("BMA")[-1]`
>
> CostFunctionJ
> :   *List of values*. Each element is a value of the chosen error function
>     $J$.
>
>     Example:
>     `J = ADD.get("CostFunctionJ")[:]`
>
> CostFunctionJAtCurrentOptimum
> :   *List of values*. Each element is a value of the error function $J$.
>     At each step, the value corresponds to the optimal state found from the
>     beginning.
>
>     Example:
>     `JACO = ADD.get("CostFunctionJAtCurrentOptimum")[:]`
>
> CostFunctionJb
> :   *List of values*. Each element is a value of the error function $J^b$,
>     that is of the background difference part. If this part does not exist in the
>     error function, its value is zero.
>
>     Example:
>     `Jb = ADD.get("CostFunctionJb")[:]`
>
> CostFunctionJbAtCurrentOptimum
> :   *List of values*. Each element is a value of the error function $J^b$. At
>     each step, the value corresponds to the optimal state found from the
>     beginning. If this part does not exist in the error function, its value is
>     zero.
>
>     Example:
>     `JbACO = ADD.get("CostFunctionJbAtCurrentOptimum")[:]`
>
> CostFunctionJo
> :   *List of values*. Each element is a value of the error function $J^o$,
>     that is of the observation difference part.
>
>     Example:
>     `Jo = ADD.get("CostFunctionJo")[:]`
>
> CostFunctionJoAtCurrentOptimum
> :   *List of values*. Each element is a value of the error function $J^o$,
>     that is of the observation difference part. At each step, the value
>     corresponds to the optimal state found from the beginning.
>
>     Example:
>     `JoACO = ADD.get("CostFunctionJoAtCurrentOptimum")[:]`
>
> CurrentOptimum
> :   *List of vectors*. Each element is the optimal state obtained at the usual
>     step of the iterative algorithm procedure of the optimization algorithm. It
>     is not necessarily the last state.
>
>     Example:
>     `xo = ADD.get("CurrentOptimum")[:]`
>
> CurrentState
> :   *List of vectors*. Each element is a usual state vector used during the
>     iterative algorithm procedure.
>
>     Example:
>     `xs = ADD.get("CurrentState")[:]`
>
> IndexOfOptimum
> :   *List of integers*. Each element is the iteration index of the optimum
>     obtained at the current step of the iterative algorithm procedure of the
>     optimization algorithm. It is not necessarily the number of the last
>     iteration.
>
>     Example:
>     `ioo = ADD.get("IndexOfOptimum")[-1]`
>
> Innovation
> :   *List of vectors*. Each element is an innovation vector, which is in static
>     the difference between the optimal and the background, and in dynamic the
>     evolution increment.
>
>     Example:
>     `d = ADD.get("Innovation")[-1]`
>
> InnovationAtCurrentState
> :   *List of vectors*. Each element is an innovation vector at current state
>     before analysis.
>
>     Example:
>     `ds = ADD.get("InnovationAtCurrentState")[-1]`
>
> OMA
> :   *List of vectors*. Each element is a vector of difference between the
>     observation and the optimal state in the observation space.
>
>     Example:
>     `oma = ADD.get("OMA")[-1]`
>
> OMB
> :   *List of vectors*. Each element is a vector of difference between the
>     observation and the background state in the observation space.
>
>     Example:
>     `omb = ADD.get("OMB")[-1]`
>
> Residu
> :   *List of values*. Each element is the value of the particular residue
>     checked during the running of the algorithm, in the order of the tests.
>
>     Example:
>     `r = ADD.get("Residu")[:]`
>
> SimulatedObservationAtBackground
> :   *List of vectors*. Each element is a vector of observation simulated by the
>     observation operator from the background $\mathbf{x}^b$. It is the
>     forecast from the background, and it is sometimes called “*Dry*”.
>
>     Example:
>     `hxb = ADD.get("SimulatedObservationAtBackground")[-1]`
>
> SimulatedObservationAtCurrentOptimum
> :   *List of vectors*. Each element is a vector of observation simulated from
>     the optimal state obtained at the current step the optimization algorithm,
>     that is, in the observation space.
>
>     Example:
>     `hxo = ADD.get("SimulatedObservationAtCurrentOptimum")[-1]`
>
> SimulatedObservationAtCurrentState
> :   *List of vectors*. Each element is an observed vector simulated by the
>     observation operator from the current state, that is, in the observation
>     space.
>
>     Example:
>     `hxs = ADD.get("SimulatedObservationAtCurrentState")[-1]`
>
> SimulatedObservationAtOptimum
> :   *List of vectors*. Each element is a vector of observation obtained by the
>     observation operator from simulation on the analysis or optimal state
>     $\mathbf{x}^a$. It is the observed forecast from the analysis or the
>     optimal state, and it is sometimes called “*Forecast*”.
>
>     Example:
>     `hxa = ADD.get("SimulatedObservationAtOptimum")[-1]`
>
> SimulationQuantiles
> :   *List of vector series*. Each element is a series of observation column
>     vectors, corresponding, for a particular quantile required by the user, to
>     the observed state that achieves the requested quantile. Each observation
>     column vector is rendered in the same order as the quantile values required
>     by the user.
>
>     Example:
>     `sQuantiles = ADD.get("SimulationQuantiles")[:]`

[[1](#id1)]

For more information on PARAVIS, see the *PARAVIS module* and its integrated help available from the main menu *Help* of the SALOME platform.

[[2](#id2)]

For more information on YACS, see the *YACS module* and its integrated help available from the main menu *Help* of the SALOME platform.
