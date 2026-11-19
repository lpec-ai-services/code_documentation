<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_entry_types.html -->

# 11.1. List of possible input types

Each variable to be entered for the use of ADAO can be represented by means of
particular “pseudo-types”, which help to logically fill it in and validate it
computationally. These pseudo-types explicitly represent mathematical forms
([Pseudo-types of mathematical representation of data](#section-ref-entry-types-math)) or simple computer forms
([Pseudo-types of digital data description](#section-ref-entry-types-info)), which are detailed here.
[Notations and common conventions](notations.md#section-notations) are also used, together with
[Information on the names required for file entries](#section-ref-entry-types-names).

The explicit [Checking algorithm “InputValuesTest”](ref_algorithm_InputValuesTest.md#section-ref-algorithm-inputvaluestest) test is designed so
that the user can specifically check some entries, with the same analysis and
criteria as during the usual setup of a study.

## 11.1.1. Pseudo-types of mathematical representation of data

The inputs are described according to the simplest possible logic, in
mathematical representation, for algorithms or calculation tools.

**Vector**
:   *List of real values*. This indicates a variable that has to be filled as a
    vector. It is a simple ordered collection of real numbers. The vectors can
    be described in row or column version without making any difference. The
    details of the [Requirements for observation or experimental measurements description](ref_observations_requirements.md#section-ref-observations-requirements) help to
    illustrate different possible ways of writing this entry.

**VectorSerie**
:   *List of list of real values*. This indicates a variable that has to be
    filled in as a list of vectors. It is an ordered collection of vectors. The
    details of the [Requirements for observation or experimental measurements description](ref_observations_requirements.md#section-ref-observations-requirements) help to
    illustrate different possible ways of writing this entry.

**Matrix**
:   *Matrix*. This indicates a variable that has to be filled by a matrix. The
    matrices are special entries described by the
    [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements).

**Function**
:   *Function*. This indicates a variable that must be given as a function in
    the Python sense.. The functions are special entries described by the
    [Requirements for functions describing an operator](ref_operator_requirements.md#section-ref-operator-requirements).

**Dict**
:   *Dictionary*. This indicates a variable that has to be filled by a Python
    dictionary `{"key":"value...}`.

The variables to which these pseudo-types apply can themselves be given using
the following computer descriptions.

## 11.1.2. Pseudo-types of digital data description

Three pseudo-types, purely computer-based, are used to specify the way in which
input variables are provided.

**Script**
:   *File name*. This indicates a script given as an external file. It can be
    described by a full absolute path name or only by the file name without
    path. If the file is given only by a file name without path, and if a study
    directory is also indicated, the file is searched in the given study
    directory.

**String**
:   *String*. This indicates a string giving a literal representation of a
    matrix, a vector or a vector series, such as “1 2 ; 3 4” or “[[1,2],[3,4]]”
    for a square 2x2 matrix.

**DataFile**, **ColNames**, **ColMajor**
:   This indicates data given in an external file. It can be described by a
    full absolute path name or only by the file name without path. If the file
    is given only by a file name without path, and if a study directory is also
    indicated, the file is searched in the given study directory. The content
    of the file can be:

    - in text format (simple text in a file with a “.txt” or “.dat” extension,
      text with comma delimiter in a file with a “.csv” extension, text with
      tabulation delimiter in a file with a “.tsv” extension), named here TXT,
      CSV, TSV or DAT.
    - in binary format (single-variable in a Numpy file with a “.npy”
      extension, multi-variables in a NumpyZ file with a “.npz” extension),
      named here NPY or NPZ.

    By default, the values of a variable has to be ordered in rows to be
    acquired record line by record line (“ColMajor=False”), but they can also
    be ordered in lines to be acquired record row by record row
    (“ColMajor=True”).

    Without information or with a void list for the variable names, all the
    values of all the variables are used, but one can also select only the ones
    of the variables that are indicated in the name list “ColNames”. The
    variable names are always as header of columns.

    Example of CSV file for “*Observation*” variable in “*DataFile*”

    ```python
    # CSV file with delimiter ";" or ","
    # ==================================
    # Comment line beginning with #
    # The next line is dedicated to variable naming
    Alpha1;Observation;Alpha2
    0.1234;5.6789;9.0123
    1.2345;2.3456;3.
    2.3456;3.4567;4.56
    3.;4.;5.
    4;5;6
    5.123;6.789;7.8
    ```

    Example of TXT file for “*Observation*” variable in “*DataFile*”

    ```python
    # TXT file with space delimiter
    # =============================
    # Comment line beginning with #
    # The next line is dedicated to variable naming
    Alpha1 Observation Alpha2
    0.1234 5.6789 9.0123
    1.2345 2.3456 3.
    2.3456 3.4567 4.56
    3.     4.     5.
    4      5      6
    5.123  6.789  7.8
    ```

Warning

It is recommended, before using them as an input of this type, to carefully
check text or binary files. Various checks are carried out on loading, but
the variety of potential errors is great. In practice, by respecting the
requirements for naming variables and for comments, text files from
classical programs or spreadsheets are (most of the time) compatible.

## 11.1.3. Information on the names required for file entries

When a command or keyword can be entered using a script file identified by the
pseudo-type “*Script*”, this script must contain a variable or method that has
the same name than the variable to be completed. In other words, when importing
such a script into a Python command or Python node, it must create a variable
of the correct name in the current namespace of the node. For example, a Python
script making available the draft variable, named “*Background*”, must have the
following form:

```python
...
...
Background =...
...
...
```

Its import thus makes it possible to create the variable “*Background*” in the
current namespace. The dots”…” symbolize any code around this particular line
beginning.

Similarly, when a particular vector can be filled in using a data file
designated by the pseudo-type “*DataFile*”, the information in the file
“*DataFile*” must be named after the vector to be loaded.
