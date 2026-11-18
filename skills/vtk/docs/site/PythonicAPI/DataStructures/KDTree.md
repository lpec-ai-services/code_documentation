<!-- source: https://examples.vtk.org/site/PythonicAPI/DataStructures/KDTree/ -->

# KDTree

Repository source: [KDTree](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/DataStructures/KDTree.py)

### Description

This example demonstrates how to use [vtkKdTree](https://www.vtk.org/doc/nightly/html/classvtkKdTree.html) to build a tree from a [vtkPoints](https://www.vtk.org/doc/nightly/html/classvtkPoints.html) object. Note that since AddDataSet or SetDataSet were not called, you cannot use GetDataSet.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/DataStructures/KDTree/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**KDTree.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import (
    reference,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import vtkKdTree

def main():
    # Setup point coordinates.
    x = (1.0, 0.0, 0.0)
    y = (0.0, 1.0, 0.0)
    z = (0.0, 0.0, 1.0)

    points = vtkPoints()
    points.InsertNextPoint(x)
    points.InsertNextPoint(y)
    points.InsertNextPoint(z)

    # Create the tree
    kd_tree = vtkKdTree()
    kd_tree.BuildLocatorFromPoints(points)

    test_point = (2.0, 0.0, 0.0)

    # Find the closest point to TestPoint.
    # vtkKdTree.FindClosestPoint: must build the locator first
    closest_point_dist = reference(0.0)
    id = kd_tree.FindClosestPoint(test_point, closest_point_dist)
    print(f'Test Point:    ({fmt_floats(test_point)})')
    # Get the closest point in the KD Tree from the point data.
    print(f'The closest point is point {id}.')
    print(f'Closest point: ({fmt_floats(points.GetPoint(id))})\nDistance: {closest_point_dist}')

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
