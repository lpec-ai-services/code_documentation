<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_observations_requirements.html -->

# 12.1. Requirements for observation or experimental measurements description

The whole set of measurements of the physical system we are considering are
called “*observations*”, or even simply “*an observation*”. As already
mentioned in [[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory), this observation is noted in the most
generic way by:

$$\mathbf{y}^o$$

It can depend in general of the space and the time, and even of parametric
variables, and this in a more or less complex way. We usually particularize the
time dependence by considering that, at each instant, the quantity
$\mathbf{y}^o$ is a vector of $\mbox{I\hspace{-.15em}R}^d$ (with
the dimension $d$ of the space being able to possibly vary in time). In
other words, **an observation is a (temporal) series of (varied)
measurements**. One will thus speak in an equivalent way of an observation
(vector), of a series or a vector of observations, and of a set of
observations. In its greatest generality, the sequential aspect of the series
of observations is related jointly to space, and/or to time, and/or to a
parametric dependence.

We can classify the ways of representing the observation according to the uses
that we have afterwards and the links with the algorithmic methods. The
classification that we propose is the following, each category being detailed
below:

1. [Use of a single spatial observation](#use-of-a-single-spatial-observation)
2. [Use of a time series of spatial observations](#use-of-a-time-series-of-spatial-observations)
3. [Use of a single spatio-temporal observation](#use-of-a-single-spatio-temporal-observation)
4. [Use of a parameterized series of spatial observations](#use-of-a-parameterized-series-of-spatial-observations)

The numerical representations of the observations use all the possibilities
described in the [List of possible input types](ref_entry_types.md#section-ref-entry-types). We specialize their uses here
to indicate different possible ways of writing this information.

## 12.1.1. Use of a single spatial observation

This refers to the use of a vector series dependent only on space. This
observation is moreover used at once, i.e. being completely known at the
beginning of the algorithmic analysis. This can for example be a spatial field
of measurements, or several fields physically homogeneous or not.

- The mathematical representation is $\mathbf{y}^o\,\in\,\mbox{I\hspace{-.15em}R}^d$.
- The canonical numerical representation is **a vector**.
- The numerical representation in ADAO is done with the keyword “*Vector*”. All
  the information, declared in one of the following representations, is
  transformed into a single vector (note: lists and tuples are equivalent):

  > - “*numpy.array*” variable : `numpy.array([1, 2, 3])`
  > - “*list*” variable : `[1, 2, 3]`
  > - string variable : `'1 2 3'`
  > - string variable : `'1,2,3'`
  > - string variable : `'1;2;3'`
  > - string variable : `'[1,2,3]'`
  > - Python data file, with variable “*Observation*” in the namespace, indicated by the keyword “*Script*” with the condition `Vector=True`
  > - data text file (TXT, CSV, TSV, DAT), with variable pointer by name in column or row, indicated by the keyword “*DataFile*” with the condition `Vector=True`
  > - binary data file (NPY, NPZ), with variable pointer by name, indicated by the keyword “*DataFile*” with the condition `Vector=True`

Examples of statements in TUI interface:

```python
case.setObservation( Vector = [1, 2, 3] )
case.setObservation( Vector = numpy.array([1, 2, 3]) )
case.setObservation( Vector = '1 2 3' )
case.setObservation( Vector=True, Script = 'script.py' )
case.setObservation( Vector=True, DataFile = 'data.csv' )
case.setObservation( Vector=True, DataFile = 'data.npy' )
```

Use note: in a given study, only the last record (whether a single vector or a
series of vectors) can be used, as only one observation concept exists per ADAO
study.

## 12.1.2. Use of a time series of spatial observations

This refers to a vector ordered series of observations, dependent on space and
time. At a given instant, it is assumed that only the observations of the
current and previous instants are known. The successive observations in time
are indexed by $n$, their instant of existence or of reference. This can
for example be a spatial field of measurements, physically homogeneous or not,
of which we consider a history.

- The mathematical representation is $\forall\,n\in\{0...N\},\,\mathbf{y}^o_n\,\in\mbox{I\hspace{-.15em}R}^d$.
- The canonical numerical representation is **an ordered series of vectors**.
- The numerical representation in ADAO is done with the keyword
  “*VectorSeries*”. The current indexing of the information is used to
  represent the time index when declaring in one of the following
  representations, and the information is transformed into an ordered series of
  vectors (note: lists and tuples are equivalent):

  > - “*list*” of “*numpy.array*” : `[numpy.array([1,2,3]), numpy.array([1,2,3])]`
  > - “*numpy.array*” of “*list*” : `numpy.array([[1,2,3], [1,2,3]])`
  > - “*list*” of “*list*” : `[[1,2,3], [1,2,3]]`
  > - “*list*” of string variables : `['1 2 3', '1 2 3']`
  > - “*list*” of string variables : `['1;2;3', '1;2;3']`
  > - “*list*” of string variables : `['[1,2,3]', '[1,2,3]']`
  > - string of “*list*” : `'[[1,2,3], [1,2,3]]'`
  > - string of “*list*” : `'1 2 3 ; 1 2 3'`
  > - Python data file, with variable “*Observation*” in the namespace, indicated by the keyword “*Script*” with the condition `VectorSerie=True`
  > - data text file (TXT, CSV, TSV), with variable pointer by name in column or row, indicated by the keyword “*DataFile*” with the condition `VectorSerie=True`
  > - binary data file (NPY, NPZ), with variable pointer by name, indicated by the keyword “*DataFile*” with the condition `VectorSerie=True`

Examples of statements in TUI interface:

```python
case.setObservation( VectorSerie = [[1,2,3], [1,2,3]] )
case.setObservation( VectorSerie = [numpy.array([1,2,3]), numpy.array([1,2,3])] )
case.setObservation( VectorSerie =  ['1 2 3', '1 2 3'] )
case.setObservation( VectorSerie =  '[[1,2,3], [1,2,3]]' )
case.setObservation( VectorSerie =  '1 2 3 ; 1 2 3' )
case.setObservation( VectorSerie=True, Script = 'script.py' )
case.setObservation( VectorSerie=True, DataFile = 'data.csv' )
case.setObservation( VectorSerie=True, DataFile = 'data.npy' )
```

Use note: in a given study, only the last record (whether a single vector or a
series of vectors) can be used, as only one observation concept exists per ADAO
study.

## 12.1.3. Use of a single spatio-temporal observation

This single spatio-temporal observation is similar to the previous one in its
representation as a vector series, but it imposes that it must be used in a
single run, i.e. by being fully known at the beginning of the algorithmic
analysis. It can therefore be represented as an indexed series, in the same way
as for a [Use of a time series of spatial observations](#use-of-a-time-series-of-spatial-observations).

## 12.1.4. Use of a parameterized series of spatial observations

One represents now a collection of observations parameterized by an index or a
discrete parameter. This form is still similar to the previous one. It is
therefore representable as an indexed series, in the same way as for a [Use of
a time series of spatial observations](#use-of-a-time-series-of-spatial-observations).

## 12.1.5. General comments on the observations

Warning

When the assimilation explicitly establishes a **temporal iterative
process**, as in state data assimilation, **the first observation is not used
but must be present in the data description of an ADAO case**. By convention,
it is therefore considered to be available at the same time as the draft time
value, and does not lead to a correction at that time. The numbering of the
observations starts at 0 by convention, so it is only from number 1 that the
observation values are used in the temporal iterative algorithms.

Observations can be provided by single time steps or by successive windows for
iterative algorithms. In this case, a series of observations must be provided
for each algorithmic iteration relative to a time window. In practice, for each
window, we provide a series as in a [Use of a time series of spatial
observations](#use-of-a-time-series-of-spatial-observations).

The observation acquisition options are richer in the TUI textual interface, as
not all options are necessarily available in the GUI.

For data entry via files, please refer to the description of the possibilities
around the keyword “*DataFile*” in the [Pseudo-types of digital data description](ref_entry_types.md#section-ref-entry-types-info).
