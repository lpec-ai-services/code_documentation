<!-- source: https://examples.vtk.org/site/PythonicAPI/DataStructures/KDTreeAccessPoints/ -->

# KDTreeAccessPoints

Repository source: [KDTreeAccessPoints](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/DataStructures/KDTreeAccessPoints.py)

### Description

This example demonstrates how to build a KDTree, get its number of points, and get a point by ID.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/DataStructures/KDTreeAccessPoints/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**KDTreeAccessPoints.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkKdTree,
    vtkPolyData
)
from vtkmodules.vtkFiltersGeneral import vtkVertexGlyphFilter

def main():
    # Setup point coordinates.
    x = (1.0, 0.0, 0.0)
    y = (0.0, 1.0, 0.0)
    z = (0.0, 0.0, 1.0)

    points = vtkPoints()
    points.InsertNextPoint(x)
    points.InsertNextPoint(y)
    points.InsertNextPoint(z)

    polydata = vtkPolyData(points=points)

    # The tree needs cells, so add vertices to each point.
    vertex_filter = vtkVertexGlyphFilter(input_data=polydata)

    # Create the tree.
    kd_tree = vtkKdTree()
    kd_tree.AddDataSet(vertex_filter.update().output)
    kd_tree.BuildLocator()

    # Get the number of points in the tree like this:
    kd_tree.data_sets.InitTraversal()
    print(f'Number of points in tree: {kd_tree.data_sets.next_data_set.number_of_points},')

    # Or you can get the number of points in the tree like this:
    print(f'Number of points in tree: {kd_tree.GetDataSet(0).number_of_points}.')

    # Get the 0th point in the tree.
    p = [0.0, 0.0, 0.0]
    kd_tree.GetDataSet(0).GetPoint(0, p)
    print(f'p: ({fmt_floats(p)})')

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
