<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/post_processings/curves.html -->

# Curves

A *curve* retrieves or computes a (small) set of meaningful values
from the current state of the physical system (or the state at the
beginning of the time step). The name *curve* refers to the fact
that those values are implicitly a function of the time and that curves
are often used to create temporal plots. See Section
[The Curves post-processing](#curve-post-processing) for an example of a post-processing based
on curves.

Note

From a computational point of view, a *curve* generally performs a
type of operation called a *reduction*.

The main interest of curves is to hide details regarding how those
values are computed.

For example, the `NodalValue` curve (Section
[The NodalValue curve](#nodal-value-curve)) allows to retrieve the value of a node field
on a set of nodes. It hides the tedious task of determining which MPI
process holds each node and gathering the values among all processes.

Just like post-processings, a curve may be created in various ways,
although we strongly recommend using the `addCurve` method of the
physical system class. Using the `addCurve` method registers the
created curve in the physical system, so that it will automatically
participate to the dependencies resolutions.

## The `Value` curve

The `Value` curve retrieves values associated with mesh sets.

### Parameters

- `value`: name of the value.
- `location`: regular expression allowing to select mesh sets on which
  the values are extracted.

### Example

PYTHON

```python
auto p = ps.addCurve('Value',
                     value = "ResultantOfReactionForce[FZ]",
                     location = "top")
```

C++

```c++
auto c = ps.addCurve(ctx, "Value",
                     Parameters{{"value", "ResultantOfReactionForce[FZ]"},
                                {"location", "top"}});
```

## The `NodalValue` curve

The `NodalValue` curve retrieves values at nodes.

### Parameters

- `field`: name of the field.
- `node`: regular expression allowing to select mesh sets from whose nodes
  the values of the field are extracted.
- `nodes`: arrays of regular expressions allowing to select mesh sets
  from whose nodes the values of the field are extracted.

### Example

PYTHON

```python
c = ps.addCurve('NodalValue',
                field = 'Temperature',
                nodes = ['p1', 'p2', 'p3'])
```

C++

```c++
auto c = ps.addCurve(ctx, "NodalValue",
                     Parameters{{"field", "Temperature"},
                                {"nodes", Vector<Parameters>{"p1", "p2", "p3"}}});
```

## The `Maximum`, `Minimum` and `MaximumIncrement` curves

The `Maximum`, `Minimum` and `MaximumIncrement` curves calculate respectively:

- the maximum,
- the minimum,
- the maximum increment between the beginning of the time step and the end of the time step,

of a field over a set of locations.

### Parameters

- `field`: name of the field.
- `fieldType`: type of the field post-processed (`nodeField` or `ipField`).
- `overAll` and `onEach` allow to select if the extremum
  over all the locations is computed (see below).

Parameters, such as `material`, defining where to compute the
extremum are listed in the online help. If several locations are
specified, the curves returns by default the extrema on all the
locations. This behaviour is changed by the `overAll`
or `onEach` parameters.

For post-processing fields at integration points, optional parameters
allowing to select the quadrature are available. See the online help for
details. If the quadrature is not defined explicitly, the curve expects
that the field is only defined for one quadrature. If this is not the
case, its initialization will fail.

### Example

PYTHON

```python
c = ps.addCurve('Maximum',
                field = 'Temperature',
                fieldType = 'nodeField',
                material = 'Fuel')
```

C++

```c++
auto c = ps.addCurve(ctx, "Maximum",
                     Parameters{{"field", "Temperature"},
                                {"fieldType", "nodeField"},
                                {"material", "Fuel"}});
```

## The `Integral` and `MeanValue` curves

The `Integral` and `MeanValue` curves compute respectively the
integral and the mean value of a field over a set of locations.

### Parameters

- `field`: name of the field.
- `fieldType`: type of the field post-processed (`ipField`).
- `overAll` and `onEach` allow to select if the integral
  or the mean value over all the locations is computed (see below).
- `configuration` allow to select the configuration on which the
  integral or the mean value is computed. See the online help for
  possible values.

Parameters, such as `material`, defining where to compute the
integral or the mean value are listed in the online help. If several
locations are specified, the curves returns by default the integral or
the mean value on all the locations. This behaviour is changed by the
`overAll` or `onEach` parameters.

For post-processing fields at integration points, optional parameters
allowing to select the quadrature are available. See the online help for
details. If the quadrature is not defined explicitly, the curve expects
that the field is only defined for one quadrature. If this is not the
case, its initialization will fail.

### Example

PYTHON

```python
c = ps.addCurve('Integral',
                field = 'HeatSource',
                fieldType = 'ipField',
                material = 'Fuel')
```

C++

```c++
auto c = ps.addCurve(ctx, "Integral",
                     Parameters{{"field", "HeatSource"},
                                {"fieldType", "ipField"},
                                {"material", "Fuel"}});
```

## The `AbsoluteDistance` and `L2Distance` curves

The `AbsoluteDistance` and `L2Distance` curves computes the
distance between two fields \(f_{1}\) and \(f_{2}\) using
respectively the \(L^{\infty}\) and \(L^{2}\) norms defined by:

\[\begin{split}\begin{aligned}
\lVert f_{1}-f_{2} \rVert_{L^{\infty}} &= \max_{e \in \Omega, i} \left|f_{1, i}-f_{2,i}\right| \\
\lVert f_{1}-f_{2} \rVert_{L^{2}} &= \sqrt{\int_{\Omega} \sum_{i} \left(f_{1, i}-f_{2,i}\right)^2\,\mathrm{d}V} \\
\end{aligned}\end{split}\]

where \(\Omega\) is the domain of interest, \(i\) refers to the
components of the fields, \(e\) refers to discretization points
considered (nodes for node fields, integration points for fields at
integration points).

### Parameters

- `firstField`: name of the first field.
- `secondField`: name of the second field.
- `fieldType`: type of the field post-processed
  (`ipField`, `nodeField`).
- `overAll` and `onEach` allow to select if the norm over
  all the locations is computed.
- `configuration` allow to select the configuration on which the
  \(L^{2}\) norm is calculated. See the online help for
  possible values.

Parameters, such as `material`, defining where to compute the
integral or the mean value are listed in the online help. If several
locations are specified, the curves returns by default the norms on all
the locations. This behaviour is changed by the `overAll` or
`onEach` parameters.

For post-processing fields at integration points, optional parameters
allowing to select the quadrature are available. See the online help for
details. If the quadrature is not defined explicitly, the curve expects
that the field is only defined for one quadrature. If this is not the
case, its initialization will fail.

### Example

PYTHON

```python
c = ps.addCurve({'L2Distance': {'firstField': 'Temperature',
                                'secondField': 'ReferenceSolution',
                                'fieldType': 'ipField',
                                'material': 'bar',
                                'quadratureOrder': 1}})
```

## The `Curves` post-processing

The `Curves` post-processing generates a txt file containing the time in
the first column and values extracted by some curves in the other
columns (See Section [Curves](#curves)).

### Parameters

The following parameters are accepted when defining a `Curves` post-processing :

- `file`: name of the output file.
- `precision`: number of significant digits in the output file.
- `fileFormat`: data file format, expected values are `txt`
  or `csv`.
- `executeInitialPostProcessing`: export values at the beginning
  of the first time step.
- `curves`: list of curves. This list must contains dictionaries. Each
  dictionary must have a single entry:

  - The key is the kind of the curve considered. See Section
    [Curves](#curves) for a list of available curves.
  - The value is a dictionary containing the parameters used to
    initialize the cure.

### Example

PYTHON

```python
ps.addPostProcessing('Curves',
                     file = 'curves/local-temperatures.txt',
                     curves = [{'NodalValue': {'field': 'Temperature',
                                               'nodes': ['p1', 'p2', 'p3']}}])
```

C++

```c++
ps.addPostProcessing(ctx, "Curves",
                     Parameters{{"file", "curves/local-temperatures.txt"},
                                {"curves", Vector<Parameters>{Parameters{{"NodalValue", Parameters{{"field", "Temperature"},
                                                                         {"nodes", Vector<Parameters>{"p1", "p2", "p3"}}}}}}});
```
