<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_algorithm_InterpolationByReducedModelTest.html -->

# 14.6. Checking algorithm “*InterpolationByReducedModelTest*”

## 14.6.1. Description

This algorithm provides a simple way of analyzing the quality of the empirical
interpolation obtained by a reduced basis for complete states, using
measurements at precise points.

The results displayed by default are simple statistics related to the
normalized errors between the interpolation with a reduced basis and the
complete states we seek to represent on the reduced basis. The test requires a
reduced basis and a set of optimal measurement positions, and uses
pseudo-measurements from each complete state (”*snapshot*”) included in the
given test set.

Please note: to be consistent, this test must use the same mathematical norm as
that used to construct the reduced basis. As the norm is chosen by the user
when defining the test, the norm used to construct the reduced basis must be
verified.

## 14.6.2. Some noteworthy properties of the implemented methods

To complete the description, we summarize here a few notable properties of the
algorithm methods or of their implementations. These properties may have an
influence on how it is used or on its computational performance. For further
information, please refer to the more comprehensive references given at the end
of this algorithm description.

- The methods proposed by this algorithm **do not require derivation of the
  objective function or of one of the operators**, thus avoiding this
  additional calculation time when derivatives are calculated numerically by
  multiple evaluations.

## 14.6.3. Optional and required commands

The general required commands, available in the editing user graphical or
textual interface, are the following:

EnsembleOfSnapshots
:   *List of vectors or matrix*. This key contains an ordered collection of
    physical state vectors $\mathbf{y}$, called “*snapshots*” in reduced
    basis terminology. At each step index, there is 1 state per column if this
    list is in matrix form, or 1 state per element if it’s actually a list.
    Caution: the numbering of the support or points, on which or to which a state
    value is given in each vector, is implicitly that of the natural order of
    numbering of the state vector, from 0 to the “size minus 1” of this vector.

    Example :
    `{"EnsembleOfSnapshots":[y1, y2, y3...]}`

MeasurementLocations
:   *Integer series*. This series contains the indices of the positions at which
    a measurement is required to support a reduced basis interpolation, according
    to the order of the variables of a state vector arbitrarily considered in
    one-dimensional form, and in the same order as the information contained in
    the vectors of the reduced basis.

    This is similar to the set of optimal positions or points resulting from a
    [Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask), or the set
    of positions required to run a
    [Task algorithm “InterpolationByReducedModelTask”](ref_algorithm_InterpolationByReducedModelTask.md#section-ref-algorithm-interpolationbyreducedmodeltask).

ReducedBasis
:   *List of matrix*. Each element is a matrix, containing in each column a
    vector of the reduced basis obtained by the optimal search, ordered by
    decreasing preference and in the same order as the ideal points found
    iteratively.

    When it is an input, it is identical to a single output of a
    [Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask).

    Example :
    `rb = ADD.get("ReducedBasis")[-1]`

The general optional commands, available in the editing user graphical or
textual interface, are indicated in [List of commands and keywords for an ADAO checking case](ref_checking_keywords.md#section-ref-checking-keywords).
Moreover, the parameters of the command “*AlgorithmParameters*” allow to choose
the specific options, described hereafter, of the algorithm. See
[Description of options of an algorithm by “AlgorithmParameters”](ref_options_AlgorithmParameters.md#section-ref-options-algorithm-parameters) for the good use of this
command.

The options are the following:

ErrorNorm
:   *Predefined name*. This key indicates the norm used for the residue that
    controls the optimal search. The default is the “L2” norm. The possible
    criteria are in the following list: [“L2”, “Linf”].

    Example :
    `{"ErrorNorm":"L2"}`

NumberOfPrintedDigits
:   *Integer value*. This key indicates the number of digits of precision for
    floating point printed output. The default is 5, with a minimum of 0.

    Example:
    `{"NumberOfPrintedDigits":5}`

ShowElementarySummary
:   *Boolean value*. This variable leads to the activation, or not, of the
    calculation and display of a summary at each elementary evaluation of the
    test. The default value is “True”, the choices are “True” or “False”.

    Example :
    `{"ShowElementarySummary":False}`

## 14.6.4. Information and variables available at the end of the algorithm

At the output, after executing the algorithm, there are information and
variables originating from the calculation. The description of
[Variables and information available at the output](ref_output_variables.md#section-ref-output-variables) show the way to obtain them by the method
named `get`, of the variable “*ADD*” of the post-processing in graphical
interface, or of the case in textual interface. The input variables, available
to the user at the output in order to facilitate the writing of post-processing
procedures, are described in an [Inventory of potentially available information at the output](ref_output_variables.md#subsection-r-o-v-inventaire).

**Permanent outputs (non conditional)**

The unconditional outputs of the algorithm are the following:

> *None*

**Set of on-demand outputs (conditional or not)**

The whole set of algorithm outputs (conditional or not), sorted by
alphabetical order, is the following:

> *None* (messages or statistics are nevertheless displayed)

## 14.6.5. See also

References to other sections:

- [Task algorithm “InterpolationByReducedModelTask”](ref_algorithm_InterpolationByReducedModelTask.md#section-ref-algorithm-interpolationbyreducedmodeltask)
- [Task algorithm “MeasurementsOptimalPositioningTask”](ref_algorithm_MeasurementsOptimalPositioningTask.md#section-ref-algorithm-measurementsoptimalpositioningtask)
- [Checking algorithm “ReducedModelingTest”](ref_algorithm_ReducedModelingTest.md#section-ref-algorithm-reducedmodelingtest)
