<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/post_processings/line_curves.html -->

# `LineCurves`

## Direct usage

a `LineCurves` is an object allowing to retrieve the values of some
nodal fields along a line at the beginning of the time step or at the
end of the time step. This object optionally allows to retrieve the
curvilinear abscissa and the coordinates of the nodes of the considered
line.

This object can only be created in Python by calling the
`addLineCurves` method of a physical system. The physical system
handles the resolution of the dependencies of the created
`LineCurves`.

### Example of usage

PYTHON

```python
T_bottom = ps.addLineCurves(line = 'bottom', nodalValues = ['Temperature'])
```

After the initialization of the physical system, the following methods
are available:

- `getCurvilinearAbscissa`, which returns a list containing the
  curvilinear abscissa along the considered line.
- `getCoordinates`, which returns a list containing the
  coordinates of the nodes along the considered line.
- `getValues`, which returns a list containing the values of the
  selected nodal fields along the line at the beginning of the time step
  or at the end of the time step, depending on the argument given.

### Parameters

- `line`: name of the line (string). This string is not
  interpreted as a regular expression.
- `nodalValue`: nodal value to be processed (string).
- `nodalValues`: list of nodal values to be processed (array of strings).
- `exportCurvilinearAbscissa`: boolean stating if the curvilinear
  abscissa shall be exported in the output file.
- `exportCoordinates`: boolean stating if the coordinates shall
  be exported in the output file.

## The `LineCurves` post-processing

The `LineCurves` post-processing exports values of selected nodal
quantities to a `txt` file at each time step.

### Example of usage

PYTHON

```python
ps->addPostProcessing(ctx, 'LineCurves',
                      file = 'temperature-profile.txt',
                      line = 'bottom',
                      nodalValue = 'Temperature')
```

C++

```c++
ps.addPostProcessing(ctx, "LineCurves",
                     Parameters{{"file", "temperature-profile.txt"},    //
                                {"line", "bottom"},                     //
                                {"nodalValue", "Temperature"}}));
```

### Parameters

- `file`: name of the output file.
- `precision`: number of significant digits in the output file.
- `line`: name of the line (string). This string is not
  interpreted as a regular expression.
- `nodalValue`: nodal value to be processed (string).
- `nodalValues`: list of nodal values to be processed (array of strings).
- `exportCurvilinearAbscissa`: boolean stating if the curvilinear
  abscissa shall be exported in the output file.
- `exportCoordinates`: boolean stating if the coordinates shall
  be exported in the output file.

### Format of the output file

The output file contains a description header and blocks of values per
time step.

Each block is built as follows. If the curvilinear abscissa is exported,
the first line of the block contains this value for each node of the
line. If the coordinates are exported, the following line contains the
first coordinate of each node, then the next line the second coordinate
in 2D, etc. The next lines contains the components of the exported
values.

#### Example

```
# values along the line 'bottom'
# first line: values of the curvilinear abscissa
# 2th line: values of 'Temperature'

#Time 0
0 0.0208333 0.0416667 0.0625 0.0833333 0.104167 0.125 0.145833 0.166667 0.1875 0.208333 0.229167 0.25 0.270833 0.291667 0.3125 0.333333 0.354167 0.375 0.395833 0.416667 0.4375 0.458333 0.479167 0.5 0.520833 0.541667 0.5625 0.583333 0.604167 0.625 0.645833 0.666667 0.6875 0.708333 0.729167 0.75 0.770833 0.791667 0.8125 0.833333 0.854167 0.875 0.895833 0.916667 0.9375 0.958333 0.979167 1
673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15 673.15

#Time 1
0 0.0208333 0.0416667 0.0625 0.0833333 0.104167 0.125 0.145833 0.166667 0.1875 0.208333 0.229167 0.25 0.270833 0.291667 0.3125 0.333333 0.354167 0.375 0.395833 0.416667 0.4375 0.458333 0.479167 0.5 0.520833 0.541667 0.5625 0.583333 0.604167 0.625 0.645833 0.666667 0.6875 0.708333 0.729167 0.75 0.770833 0.791667 0.8125 0.833333 0.854167 0.875 0.895833 0.916667 0.9375 0.958333 0.979167 1
188.159 192.365 196.593 200.841 205.108 209.394 213.697 218.018 222.354 226.705 231.071 235.45 239.841 244.244 248.657 253.08 257.511 261.951 266.397 270.848 275.305 279.765 284.229 288.694 293.16 297.626 302.091 306.555 311.015 315.472 319.923 324.369 328.809 333.24 337.663 342.076 346.479 350.87 355.249 359.615 363.966 368.302 372.623 376.926 381.212 385.479 389.727 393.955 398.161
```

#### The `manta-extractLineCurve` utility

The `manta-extractLineCurve` utility can be used to extract data
from a file generated by the `LineCurve` post-processing at various
time as follows:

```sh
$ manta-extract_line_curve_values temperature-profile.txt 1
```

The output of `manta-extractLineCurve` also transposes the values
extracted, which eases plotting the data. A typical output is thus:

```
#values at time 1
0 -0.5 -0.5 188.159
0.0208333 -0.479167 -0.5 192.365
0.0416667 -0.458333 -0.5 196.593
0.0625 -0.4375 -0.5 200.841
0.0833333 -0.416667 -0.5 205.108
0.104167 -0.395833 -0.5 209.394
0.125 -0.375 -0.5 213.697
....
```

Section [The manta-extract_line_curve_values utility](../miscellaneous/tools.md#manta-extra-line-curve-values) provides an in-depth
description of `manta-extract_line_curve_values`.
