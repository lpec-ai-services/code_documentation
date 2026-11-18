<!-- source: https://examples.vtk.org/site/PythonicAPI/DataStructures/OBBTreeIntersectWithLine/ -->

# OBBTreeIntersectWithLine

Repository source: [OBBTreeIntersectWithLine](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/DataStructures/OBBTreeIntersectWithLine.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/DataStructures/OBBTreeIntersectWithLine/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OBBTreeIntersectWithLine.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkPoints
)
from vtkmodules.vtkFiltersFlowPaths import vtkModifiedBSPTree
from vtkmodules.vtkFiltersSources import (
    vtkSphereSource
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()
    sphere_source.Update()

    line_p0 = [0.0, 0.0, 0.0]
    line_p1 = [0.0, 0.0, 2.0]
    tol = 1.0e-8
    # Create the locator.
    # Note: Using vtkModifiedBSPTree instead of vtkOBBTree.
    # vtkOBBTree doesn't seem to generate intersections.
    tree = vtkModifiedBSPTree(data_set=sphere_source.output)
    tree.BuildLocator()
    # Intersect the locator with the line.
    intersect_points = vtkPoints()
    # intersect_cells = vtkIdList()
    tree.IntersectWithLine(line_p0, line_p1, intersect_points, None)

    print(f'Number of Points: {intersect_points.number_of_points}')

    # Display the list of intersections.
    intersection = [0.0, 0.0, 0.0]
    for i in range(0, intersect_points.number_of_points):
        intersect_points.GetPoint(i, intersection)
        print(f'\tPoint Intersection {i}: ({fmt_floats(intersection)})')

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
