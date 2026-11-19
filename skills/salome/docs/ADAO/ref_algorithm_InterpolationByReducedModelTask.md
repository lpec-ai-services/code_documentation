<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_InterpolationByReducedModelTask.html -->

# 15.2. Task algorithm “*InterpolationByReducedModelTask*”

Warning

In this particular version, this algorithm or some of its variants are
experimental, and therefore remain subject to change in future versions.

This algorithm is reserved for use in the textual user interface (TUI), and
therefore not in graphical user interface (GUI).

## 15.2.1. Description

This algorithm enables highly efficient interpolation of physical measurements
using a reduced representation of the model for that physics. The output, for
each set of measurements supplied at the required positions, is a complete
field $\mathbf{y}$ by interpolation. Put another way, it’s a physical
field reconstruction using measurements and a reduced numerical model.

To interpolate these measurements, a method of Empirical Interpolation Method
(EIM [[Barrault04]](bibliography.md#barrault04)) type is used, which uses a reduced model of type Reduced
Order Model (ROM) issued from EIM or DEIM decomposition, with or without
measurement positioning constraints.

To use this algorithm, you need the optimally positioned measurements and the
associated reduced basis for model representation. This can be achieved as
described below, by means of a preliminary analysis using a MOP, which provides
positions and base. Once the base has been constructed and the positions
determined, it is possible to perform as many interpolations as there are sets
of measurements at the required positions, without having to repeat the prior
analysis.

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/irm_determination.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/irm_determination.png)
>
> ****General scheme for using the algorithm****

## 15.2.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

## 15.2.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

Observation
:   *List of vectors*. The variable indicates the observation vector used for
    data assimilation or optimization, and usually noted $\mathbf{y}^o$.
    Its value is defined as an object of type “*Vector*” if it is a single
    observation (temporal or not) or “*VectorSeries*” if it is a succession of
    observations. Its availability in output is conditioned by the boolean
    “*Stored*” associated in input.

The general optional commands, available in the editing user graphical or
textual interface, are indicated in [List of commands and keywords for a dedicated task or study oriented case](ref_task_keywords.md#section-ref-task-keywords). Moreover,
the parameters of the command “*AlgorithmParameters*” allow to choose the
specific options, described hereafter, of the algorithm. See
[Description of options of an algorithm by “AlgorithmParameters”](ref_options_AlgorithmParameters.md#section-ref-options-algorithm-parameters) for the good use of this
command.

The options are the following:

ObservationsAlreadyRestrictedOnOptimalLocations
:   *Boolean value*. The variable defines whether measurements are supplied only
    at the ideal positions or optimum points at which a measurement is required
    (“True”, default value), or whether they are supplied on a medium identical
    to the complete field and must therefore be restricted to the required
    positions (“False”).

    Example :
    `{"ObservationsAlreadyRestrictedOnOptimalLocations":False}`

OptimalLocations
:   *Integer series*. This series contains the indices of ideal positions or
    optimal points where a measurement is required, in the order of the variables
    of a state vector considered arbitrarily in one-dimensional form, and in the
    same order as the vectors of the reduced basis found iteratively.

    It is identical to a single output (one single series) of the ideal positions
    or optimum points (which is a list of integer series) of a
    [Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask).

ReducedBasis
:   *List of matrix*. Each element is a matrix, containing in each column a
    vector of the reduced basis obtained by the optimal search, ordered by
    decreasing preference and in the same order as the ideal points found
    iteratively.

    When it is an input, it is identical to a single output of a
    [Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask).

    Example :
    `rb = ADD.get("ReducedBasis")[-1]`

StoreSupplementaryCalculations
:   *List of names*. This list indicates the names of the supplementary
    variables, that can be available during or at the end of the algorithm, if
    they are initially required by the user. Their availability involves,
    potentially, costly calculations or memory consumptions. The default is then
    a void list, none of these variables being calculated and stored by default
    (excepted the unconditional variables). The possible names are in the
    following list (the detailed description of each named variable is given in
    the following part of this specific algorithmic documentation, in the
    sub-section “*Information and variables available at the end of the
    algorithm*”): [
    “Analysis”,
    “ReducedCoordinates”,
    ].

    Example :
    `{"StoreSupplementaryCalculations":["CurrentState", "Residu"]}`

## 15.2.4. Information and variables available at the end of the algorithm

At the output, after executing the algorithm, there are information and
variables originating from the calculation. The description of
[Variables and information available at the output](ref_output_variables.md#section-ref-output-variables) show the way to obtain them by the method
named `get`, of the variable “*ADD*” of the post-processing in graphical
interface, or of the case in textual interface. The input variables, available
to the user at the output in order to facilitate the writing of post-processing
procedures, are described in an [Inventory of potentially available information at the output](ref_output_variables.md#subsection-r-o-v-inventaire).

**Permanent outputs (non conditional)**

The unconditional outputs of the algorithm are the following:

Analysis
:   *List of vectors*. Each element of this variable is an optimal state
    $\mathbf{x}^*$ in optimization, an interpolate or an analysis
    $\mathbf{x}^a$ in data assimilation.

    Example:
    `xa = ADD.get("Analysis")[-1]`

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

Analysis
:   *List of vectors*. Each element of this variable is an optimal state
    $\mathbf{x}^*$ in optimization, an interpolate or an analysis
    $\mathbf{x}^a$ in data assimilation.

    Example:
    `xa = ADD.get("Analysis")[-1]`

ReducedCoordinates
:   *List of vectors*. Each element of this variable contains the coordinates of
    a complete physical state $\mathbf{y}$ in the reduced basis.

    Example:
    `rc = ADD.get("ReducedCoordinates")[-1]`

## 15.2.5. Python (TUI) use examples

Here is one or more very simple examples of the proposed algorithm and its
parameters, written in [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). Moreover, when it is possible, the
information given as input also allows to define an equivalent case in
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome).

### 15.2.5.1. First example

This example describes the implementation of a **reconstruction by
interpolation**, following the building of a reduced representation by an
*optimal measurement positioning* search.

To illustrate, we use the same very simple artificial fields (generated in such
a way as to exist in a vector space of dimension 2) that for the [study
examples with
“MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask-examples).
The preliminary positioning ADAO search yields 2 optimal positions for the
measurements, which are then used to establish a physical field interpolation
based on measurements at the optimum locations.

```python
# -*- coding: utf-8 -*-
#
from numpy import array, arange, ravel, set_printoptions
set_printoptions(precision=3)
#
dimension = 7
#
print("Defining a set of artificial physical fields")
print("--------------------------------------------")
Ensemble = array( [i+arange(dimension) for i in range(7)] ).T
print("- Dimension of physical field space....................: %i"%dimension)
print("- Number of physical field vectors.....................: %i"%Ensemble.shape[1])
print()
#
print("Search for optimal measurement positions")
print("-------------------------------------------")
from adao import adaoBuilder
case = adaoBuilder.New()
case.setAlgorithmParameters(
    Algorithm = "MeasurementsOptimalPositioningTask",
    Parameters = {
        "EnsembleOfSnapshots":Ensemble,
        "MaximumNumberOfLocations":3,
        "ErrorNorm":"L2",
        "StoreSupplementaryCalculations":[
            "ReducedBasis",
            "Residus",
        ],
    }
)
case.execute()
print("- ADAO calculation performed")
print()
#
print("Display of optimal positioning of measures")
print("------------------------------------------")
op = case.get("OptimalPoints")[-1]
print("- Number of optimal measurement positions..............: %i"%op.size)
print("- Optimal measurement positions, numbered by default...: %s"%op)
print()
#
print("Reconstruction by interpolation of known measured states")
print("--------------------------------------------------------")
rb = case.get("ReducedBasis")[-1]
measures_at_op = Ensemble[op,1]
#
interpolation = adaoBuilder.New()
interpolation.setAlgorithmParameters(
    Algorithm = "InterpolationByReducedModelTask",
    Parameters = {
        "ReducedBasis":rb,
        "OptimalLocations":op,
        }
    )
interpolation.setObservation( Vector = measures_at_op )
interpolation.execute()
field = interpolation.get("Analysis")[-1]
print("- Reference state 1 used for the learning..............:",ravel(Ensemble[:,1]))
print("- Optimal measurement positions, numbered by default...: %s"%op)
print("- Measures extracted from state 1 for reconstruction...:",measures_at_op)
print("- State 1 reconstructed with the precision of 1%.......:",field)

if max(abs(ravel(Ensemble[:,1])-field)) < 1.e-2:
    print("  ===> There is no difference between the two states, as expected")
else:
    raise ValueError("Difference recorded in reference state 1")
print()
#
print("Reconstruction by interpolation of unknown measured states")
print("----------------------------------------------------------")
measures_at_op = array([4, 3])
interpolation.setObservation( Vector = measures_at_op )
interpolation.execute()
field = interpolation.get("Analysis")[-1]
print("  Illustration of an interpolation on unknown real measurements")
print("- Optimal measurement positions, numbered by default...: %s"%op)
print("- Measures not present in the known states.............:",measures_at_op)
print("- State reconstructed with the precision of 1%.........:",field)
print("  ===> At measure positions %s, the reconstructed field is equal to measures"%op)
print()
```

The execution result is the following:

```none
Defining a set of artificial physical fields
--------------------------------------------
- Dimension of physical field space....................: 7
- Number of physical field vectors.....................: 7

Search for optimal measurement positions
-------------------------------------------
- ADAO calculation performed

Display of optimal positioning of measures
------------------------------------------
- Number of optimal measurement positions..............: 2
- Optimal measurement positions, numbered by default...: [6 0]

Reconstruction by interpolation of known measured states
--------------------------------------------------------
- Reference state 1 used for the learning..............: [1 2 3 4 5 6 7]
- Optimal measurement positions, numbered by default...: [6 0]
- Measures extracted from state 1 for reconstruction...: [7 1]
- State 1 reconstructed with the precision of 1%.......: [1. 2. 3. 4. 5. 6. 7.]
  ===> There is no difference between the two states, as expected

Reconstruction by interpolation of unknown measured states
----------------------------------------------------------
  Illustration of an interpolation on unknown real measurements
- Optimal measurement positions, numbered by default...: [6 0]
- Measures not present in the known states.............: [4 3]
- State reconstructed with the precision of 1%.........: [3.    3.167 3.333 3.5   3.667 3.833 4.   ]
  ===> At measure positions [6 0], the reconstructed field is equal to measures
```

## 15.2.6. See also

References to other sections:

- [Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask)

Bibliographical references:

- [[Barrault04]](bibliography.md#barrault04)
- [[Quarteroni16]](bibliography.md#quarteroni16)
