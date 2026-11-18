<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/CenterOfMass/ -->

# CenterOfMass

Repository source: [CenterOfMass](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/CenterOfMass.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/CenterOfMass/)), ([Java](https://examples.vtk.org/site/Java/PolyData/CenterOfMass/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CenterOfMass.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import vtkCenterOfMass

def main():
    # Create a point set of a square.
    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(1, 0, 0)
    points.InsertNextPoint(0, 1, 0)
    points.InsertNextPoint(1, 1, 0)

    polydata = vtkPolyData(points=points)

    # Compute the center of mass.
    centerOfMassFilter = vtkCenterOfMass(input_data=polydata, use_scalars_as_weights=False)
    centerOfMassFilter.update()

    center = centerOfMassFilter.center
    print(f'Center of mass is ({fmt_floats(center, 0, 6, 'g')})')

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
