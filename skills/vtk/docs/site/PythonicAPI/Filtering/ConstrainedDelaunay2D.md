<!-- source: https://examples.vtk.org/site/PythonicAPI/Filtering/ConstrainedDelaunay2D/ -->

# ConstrainedDelaunay2D

Repository source: [ConstrainedDelaunay2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Filtering/ConstrainedDelaunay2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestConstrainedDelaunay2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestConstrainedDelaunay2D.png?raw=true target=)

### Description

Perform a 2D Delaunay triangulation respecting a specified boundary. This examples constructs a 10x10 grid of points. It then defines a polygon that uses the points in the grid. We want to triangulate all of the points except the region inside the boundary of the polygon. We expect a rectangular hole of size 4x3 in the resulting triangulated plane.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/ConstrainedDelaunay2D/)), ([Python](../../Python/Filtering/ConstrainedDelaunay2D.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ConstrainedDelaunay2D.py**

```python
#!/usr/bin/python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints, vtkMinimalStandardRandomSequence
from vtkmodules.vtkCommonDataModel import vtkPolyData, vtkCellArray, vtkPolygon
from vtkmodules.vtkFiltersCore import vtkDelaunay2D
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Generate a 10 x 10 grid of points.
    points = vtkPoints()
    grid_size = 10
    seed = 0
    random_sequence = vtkMinimalStandardRandomSequence()
    random_sequence.Initialize(seed)
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            d1 = random_sequence.value / 2.0 - 0.25
            random_sequence.Next()
            d2 = random_sequence.value / 2.0 - 0.25
            random_sequence.Next()
            points.InsertNextPoint(x + d1, y + d2, 0)

    polydata = vtkPolyData(points=points)

    # Create a cell array to store the polygon in.
    cell_array = vtkCellArray()

    # Define a polygonal hole with a clockwise polygon.
    polygon = vtkPolygon()

    polygon.GetPointIds().InsertNextId(22)
    polygon.GetPointIds().InsertNextId(23)
    polygon.GetPointIds().InsertNextId(24)
    polygon.GetPointIds().InsertNextId(25)
    polygon.GetPointIds().InsertNextId(35)
    polygon.GetPointIds().InsertNextId(45)
    polygon.GetPointIds().InsertNextId(44)
    polygon.GetPointIds().InsertNextId(43)
    polygon.GetPointIds().InsertNextId(42)
    polygon.GetPointIds().InsertNextId(32)

    cell_array.InsertNextCell(polygon)

    # Create a polydata to store the boundary. The points must be the same as
    # the points we will triangulate.
    boundary = vtkPolyData(points=polydata.points, polys=cell_array)

    # Triangulate the grid points
    delaunay = vtkDelaunay2D(input_data=polydata, source_data=boundary)

    # Visualize
    mesh_mapper = vtkPolyDataMapper()
    delaunay >> mesh_mapper

    mesh_property = vtkProperty(color=colors.GetColor3d('LightGoldenrodYellow'),
                                edge_visibility=True, edge_color=colors.GetColor3d('CornflowerBlue'),
                                line_width=1, render_lines_as_tubes=False,
                                interpolation=Property.Interpolation.VTK_FLAT)

    mesh_actor = vtkActor(mapper=mesh_mapper, property=mesh_property)

    boundary_mapper = vtkPolyDataMapper(input_data=boundary)

    boundary_property = vtkProperty(color=colors.GetColor3d('Raspberry'),
                                    edge_visibility=True, edge_color=colors.GetColor3d('Red'),
                                    line_width=3, render_lines_as_tubes=False,
                                    representation=Property.Representation.VTK_WIREFRAME)

    boundary_actor = vtkActor(mapper=boundary_mapper, property=boundary_property)

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('PowderBlue'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='ConstrainedDelaunay2D')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(mesh_actor)
    renderer.AddActor(boundary_actor)

    renderer.ResetCamera()
    renderer.active_camera.Zoom(1.3)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

@dataclass(frozen=True)
class Property:
    @dataclass(frozen=True)
    class Interpolation:
        VTK_FLAT: int = 0
        VTK_GOURAUD: int = 1
        VTK_PHONG: int = 2
        VTK_PBR: int = 3

    @dataclass(frozen=True)
    class Representation:
        VTK_POINTS: int = 0
        VTK_WIREFRAME: int = 1
        VTK_SURFACE: int = 2

if __name__ == '__main__':
    main()
```
