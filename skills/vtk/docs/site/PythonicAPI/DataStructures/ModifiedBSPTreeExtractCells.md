<!-- source: https://examples.vtk.org/site/PythonicAPI/DataStructures/ModifiedBSPTreeExtractCells/ -->

# ModifiedBSPTreeExtractCells

Repository source: [ModifiedBSPTreeExtractCells](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/DataStructures/ModifiedBSPTreeExtractCells.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/DataStructures/TestModifiedBSPTreeExtractCells.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/DataStructures/TestModifiedBSPTreeExtractCells.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/DataStructures/ModifiedBSPTreeExtractCells/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ModifiedBSPTreeExtractCells.py**

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
    vtkIdList,
    vtkPoints
)
from vtkmodules.vtkFiltersCore import vtkExtractCells
from vtkmodules.vtkFiltersFlowPaths import vtkModifiedBSPTree
from vtkmodules.vtkFiltersSources import (
    vtkLineSource,
    vtkSphereSource
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource(phi_resolution=7, theta_resolution=15)
    sphere_source.update()

    line_p0 = [-0.6, -0.6, -0.6]
    line_p1 = [0.6, 0.6, 0.6]
    tol = 1.0e-8
    # Create the locator.
    tree = vtkModifiedBSPTree(data_set=sphere_source.output)
    # Intersect the locator with the line.
    intersect_points = vtkPoints()
    intersect_cells = vtkIdList()
    tree.IntersectWithLine(line_p0, line_p1, tol, intersect_points, intersect_cells)

    print(f'Number of Points: {intersect_points.number_of_points}')

    # Display the list of intersections.
    intersection = [0.0, 0.0, 0.0]
    for i in range(0, intersect_points.number_of_points):
        intersect_points.GetPoint(i, intersection)
        # intersection = intersect_points.point(i)
        print(f'\tPoint Intersection {i}: ({fmt_floats(intersection)})')

    print(f'Number of Cells: {intersect_cells.GetNumberOfIds()}')
    for i in range(0, intersect_cells.GetNumberOfIds()):
        cellId = intersect_cells.GetId(i)
        print(f'\tCellId {i}: {cellId}')

    # Render the line, sphere and intersected cells
    line_source = vtkLineSource(point1=line_p0, point2=line_p1)

    line_mapper = vtkPolyDataMapper()
    line_source >> line_mapper
    line_actor = vtkActor(mapper=line_mapper)

    sphere_mapper = vtkPolyDataMapper()
    sphere_source >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.SetRepresentationToWireframe()
    sphere_actor.property.color = colors.GetColor3d('Gold')

    cell_source = vtkExtractCells(cell_list=intersect_cells)

    cell_mapper = vtkDataSetMapper()
    sphere_source >> cell_source >> cell_mapper
    cell_actor = vtkActor(mapper=cell_mapper)
    cell_actor.property.color = colors.GetColor3d('Tomato')

    renderer = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'))
    render_window = vtkRenderWindow(window_name='ModifiedBSPTreeExtractCells')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(line_actor)
    renderer.AddActor(sphere_actor)
    renderer.AddActor(cell_actor)

    render_window.Render()
    render_window_interactor.Start()

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
