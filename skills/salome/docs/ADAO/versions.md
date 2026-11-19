<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/versions.html -->

# 16. Versions of ADAO and external compatibility

## 16.1. Switching from a version of ADAO to a newer one

The ADAO module and its “.comm” case files are identified by versions, with
“Major”, “Minor”, “Revision” and optionally “Installation” characteristics. A
particular version is numbered as “Major.Minor.Revision”, with strong link with
the numbering of the SALOME platform. The optional indication of a fourth
number indicates a difference in the installation method, not in the content of
the version.

Each version “Major.Minor.Revision” of the ADAO module can read ADAO case files
of the previous minor version “Major.Minor-1.*”. In general, it can also read
ADAO case files of all the previous minor versions for one major branch, but it
is not guaranteed for all the commands or keywords. In general also, an ADAO
case file for one version can not be read by a previous minor or major version
of the ADAO module.

### 16.1.1. Switching from 9.x to 9.y with y > x

There is no known incompatibility for the ADAO case files. The upgrade procedure
is to read the old ADAO case file with the new SALOME/ADAO module, and save it
with a new name.

However, there may be incompatibilities from user cases written directly in TUI
interface. It is advisable to review the syntax and arguments in the TUI
scripts at each version change. In particular, it is advisable to check that
the algorithm parameters are still adequate and active, knowing that it has
been explicitly chosen that there is no message when an optional parameter
becomes inactive or changes its name (for the example, we quote the parameter
“*MaximumNumberOfSteps*” as having changed its name to
“*MaximumNumberOfIterations*”, for homogeneity with the variables that can be
displayed) to avoid a lock.

### 16.1.2. Switching from 8.5 to 9.2

There is no known incompatibility for the ADAO case files. The upgrade procedure
is to read the old ADAO case file with the new SALOME/ADAO module, and save it
with a new name.

However, there may be incompatibilities from user script files that would not
have a syntax compatible with Python 3. The most immediate error is the use of
printing “*print*” with “*command*” syntax instead of functional syntax
“*print(…)*”. In this case, it is suggested to correct the syntax of user
files in environment 8 before switching to environment 9.

### 16.1.3. Switching from 8.x to 8.y with y > x

There is no known incompatibility for the ADAO case files. The upgrade procedure
is to read the old ADAO case file with the new SALOME/ADAO module, and save it
with a new name.

To make future developments easier, it is strongly recommended to ensure that
your user scripts files use a Python 2 and a Python 3 compatible syntax. In
particular, it is recommended to use the functional syntax for “*print*” and not
the “*command*” syntax, for example:

```python
# Python 2 & 3
x, unit = 1., "cm"
print( "x = %s %s"%(str(x),str(unit)) )
```

or:

```python
# Python 2 & 3
x, unit = 1., "cm"
print( "x = {0} {1}".format(str(x),str(unit)) )
```

rather than:

```python
# Python 2 only
x, unit = 1., "cm"
print "x =", x, unit
```

### 16.1.4. Switching from 7.8 to 8.1

There is no known incompatibility for the ADAO case files. The upgrade procedure
is to read the old ADAO case file with the new SALOME/ADAO module, and save it
with a new name.

### 16.1.5. Switching from 7.x to 7.y with y > x

There is no known incompatibility for the ADAO case files. The upgrade procedure
is to read the old ADAO case file with the new SALOME/ADAO module, and save it
with a new name.

### 16.1.6. Switching from 6.6 to 7.2

There is no known incompatibility for the ADAO case files. The upgrade procedure
is to read the old ADAO case file with the new SALOME/ADAO module, and save it
with a new name.

There is one incompatibility introduced for the post-processing or observer
script files. The old syntax to call a result object, such as the “*Analysis*”
one (in a script provided through the “*UserPostAnalysis*” keyword), was for
example:

```python
Analysis = ADD.get("Analysis").valueserie(-1)
Analysis = ADD.get("Analysis").valueserie()
```

The new syntax is entirely similar to the (classical) one of a list or tuple
object:

```python
Analysis = ADD.get("Analysis")[-1]
Analysis = ADD.get("Analysis")[:]
```

The post-processing scripts has to be modified.

### 16.1.7. Switching from 6.x to 6.y with y > x

There is no known incompatibility for the ADAO case file. The upgrade procedure
is to read the old ADAO case file with the new SALOME/ADAO module, and save it
with a new name.

There is one incompatibility introduced for the operator script files, in the
naming of operators used to for the observation operator. The new mandatory
names are “*DirectOperator*”, “*TangentOperator*” and “*AdjointOperator*”, as
described in the last subsection of the chapter [[DocR] Reference description of the ADAO commands and keywords](reference.md#section-reference). The
operator script files has to be modified.

## 16.2. Versions of ADAO compatibility with support tools

The module benefits greatly from the **Python environment** [[Python]](bibliography.md#python) and the
multiple features of this language, from the scientific calculation tools
included in **NumPy** [[NumPy20]](bibliography.md#numpy20), **SciPy** [[SciPy20]](bibliography.md#scipy20), **NLopt** [[Johnson08]](bibliography.md#johnson08)
or in the tools that can be reached with them, and from the numerous
capabilities of **SALOME** [[Salome]](bibliography.md#salome) when used in combination.

Each version of the ADAO module is validated within the framework of SALOME,
and is therefore compatible with the environment implicitly defined by the
corresponding 9.16.0 version of SALOME identical to that of ADAO for the
current document. The validation versions are indicated here for information
purposes only, knowing that, in case of doubt, the SALOME version sheet
[[Salome]](bibliography.md#salome) is the official validation version.

Table 16.1 Validation versions of the support tools for ADAO

| Tool | Version |
| --- | --- |
| ADAO | 9.16.0 |
| EFICAS | 9.16.0 |
| SALOME | 9.16.0 |
| Python | 3.9.2 |
| Numpy | 1.20.3 |
| Scipy | 1.6.0 |
| MatplotLib | 3.3.4 |
| Gnuplot | 1.8 |
| NLopt | 2.7.0 |

The compatibility of the module is furthermore checked against various versions
of Python and support modules like Numpy and Scipy. The range of versions
reached in the tests depends on their availability, and the tests are not
systematically performed on all intermediate versions. For all tested versions,
the ADAO module behaves identically (to the extent of modifications depending
on the support tools). It is strongly discouraged (or impossible) to use ADAO
with a version lower than the minimum version, and there is no explicit
limitation to the use of the ADAO module beyond the reached version (but this
remains without guarantee). If an unusual error is encountered for previously
running calculations, it is strongly recommended to revert to supporting tool
versions within the range described below.

Table 16.2 Support tool verification version intervals for ADAO

| Tool | Minimal version | Reached version |
| --- | --- | --- |
| Python | 3.6.5 | 3.14.4 |
| Numpy | 1.14.3 | 2.4.6 |
| Scipy | 0.19.1 | 1.17.1 |
| MatplotLib | 2.2.2 | 3.10.9 |
| GnuplotPy | 1.8 | 1.8 |
| NLopt | 2.4.2 | 2.11.0 |
| FMPy | 0.3.20 | 0.3.29 |
