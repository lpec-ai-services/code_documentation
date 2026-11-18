<!-- source: https://examples.vtk.org/site/PythonicAPI/DataStructures/IncrementalOctreePointLocator/ -->

# IncrementalOctreePointLocator

Repository source: [IncrementalOctreePointLocator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/DataStructures/IncrementalOctreePointLocator.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/DataStructures/IncrementalOctreePointLocator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IncrementalOctreePointLocator.py**

```python
#!/usr/bin/env python3

import math

from vtkmodules.vtkCommonCore import (
    vtkMath,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkIncrementalOctreePointLocator,
    vtkPolyData
)

def main():
    # Set up the point coordinates.
    x = (1.0, 0.0, 0.0)
    y = (0.0, 1.0, 0.0)
    z = (0.0, 0.0, 1.0)

    points = vtkPoints()
    points.InsertNextPoint(x)
    points.InsertNextPoint(y)
    points.InsertNextPoint(z)

    polydata = vtkPolyData()
    polydata.SetPoints(points)

    # Create the tree
    octree = vtkIncrementalOctreePointLocator(data_set=polydata)
    octree.BuildLocator()

    test_point = (2.0, 0.0, 0.0)
    print(f'Test Point ({fmt_floats(test_point)})')

    closest_point(octree, test_point)

    # Insert another point.
    new_pt = (2.1, 0, 0)
    octree.InsertNextPoint(new_pt)
    print(f'Inserted a new point: ({fmt_floats(new_pt)})')

    closest_point(octree, test_point)

def closest_point(octree, test_point):
    # Find the closest points to test_point.
    pt_id = octree.FindClosestPoint(test_point)

    # Get the coordinates of the closest point.
    pt = [0] * 3
    octree.GetDataSet().GetPoint(pt_id, pt)
    print(f'The closest point is point {pt_id}: ({fmt_floats(pt)})')
    print(f'Distance: {math.sqrt(vtkMath.Distance2BetweenPoints(test_point, pt)):0.3f}')

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
