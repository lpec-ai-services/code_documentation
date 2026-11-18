<!-- source: https://examples.vtk.org/site/PythonicAPI/SimpleOperations/DistancePointToLine/ -->

# DistancePointToLine

Repository source: [DistancePointToLine](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/SimpleOperations/DistancePointToLine.py)

### Description

This example computes the distance from a point to a line.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/SimpleOperations/DistancePointToLine/)), ([CSharp](https://examples.vtk.org/site/CSharp/SimpleOperations/DistancePointToLine/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DistancePointToLine.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonCore import reference
from vtkmodules.vtkCommonDataModel import vtkLine

def main():
    lineP0 = (0.0, 0.0, 0.0)
    lineP1 = (2.0, 0.0, 0.0)

    p0 = (1.0, 0, 0)
    p1 = (1.0, 2.0, 0)

    print('p0 = ', p0)
    print('p1 = ', p1)

    dist0 = vtkLine.DistanceToLine(p0, lineP0, lineP1)
    print(f'Dist0: {dist0}')

    dist1 = vtkLine.DistanceToLine(p1, lineP0, lineP1)
    print(f'Dist1: {dist1}')

    t = reference(0.0)
    closest = [0.0] * 3
    dist0 = vtkLine.DistanceToLine(p0, lineP0, lineP1, t, closest)
    print(f'Dist0: {dist0}, closest point: ({fmt_floats(closest, 4, 1)}), t: {t}')

    dist1 = vtkLine.DistanceToLine(p1, lineP0, lineP1, t, closest)
    print(f'Dist1: {dist1}, closest point: ({fmt_floats(closest, 4, 1)}), t: {t}')

def fmt_floats(v, w=0, d=6, pt='f'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
