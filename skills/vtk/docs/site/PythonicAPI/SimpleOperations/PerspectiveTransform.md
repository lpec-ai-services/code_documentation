<!-- source: https://examples.vtk.org/site/PythonicAPI/SimpleOperations/PerspectiveTransform/ -->

# PerspectiveTransform

Repository source: [PerspectiveTransform](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/SimpleOperations/PerspectiveTransform.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/SimpleOperations/PerspectiveTransform/)), ([Java](https://examples.vtk.org/site/Java/SimpleOperations/PerspectiveTransform/)), ([CSharp](https://examples.vtk.org/site/CSharp/SimpleOperations/PerspectiveTransform/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PerspectiveTransform.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonMath import vtkMatrix4x4
from vtkmodules.vtkCommonTransforms import vtkPerspectiveTransform, vtkTransform

def main():
    m = vtkMatrix4x4()
    m.SetElement(0, 0, 1)
    m.SetElement(0, 1, 2)
    m.SetElement(0, 2, 3)
    m.SetElement(0, 3, 4)
    m.SetElement(1, 0, 2)
    m.SetElement(1, 1, 2)
    m.SetElement(1, 2, 3)
    m.SetElement(1, 3, 4)
    m.SetElement(2, 0, 3)
    m.SetElement(2, 1, 2)
    m.SetElement(2, 2, 3)
    m.SetElement(2, 3, 4)
    m.SetElement(3, 0, 4)
    m.SetElement(3, 1, 2)
    m.SetElement(3, 2, 3)
    m.SetElement(3, 3, 4)

    perspective_transform = vtkPerspectiveTransform()
    perspective_transform.SetMatrix(m)

    transform = vtkTransform()
    transform.SetMatrix(m)

    p = [1.0, 3.0, 3.0]

    normal_projection = [0.0] * 3
    transform.TransformPoint(p, normal_projection)

    print(f'Standard projection: ({fmt_floats(normal_projection)})')

    perspective_projection = [0.0] * 3
    perspective_transform.TransformPoint(p, perspective_projection)
    print(f'Standard projection: ({fmt_floats(perspective_projection)})')

def fmt_floats(v, w=0, d=6, pt='g'):
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
