<!-- source: https://examples.vtk.org/site/PythonicAPI/Filtering/Delaunay2D/ -->

# Delaunay2D

Repository source: [Delaunay2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Filtering/Delaunay2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestDelaunay2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestDelaunay2D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/Delaunay2D/)), ([Python](../../Python/Filtering/Delaunay2D.md)), ([Java](https://examples.vtk.org/site/Java/Filtering/Delaunay2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Delaunay2D.py**

```python
#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import vtkDelaunay2D
from vtkmodules.vtkFiltersGeneral import vtkVertexGlyphFilter
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

    # Create a set of heights on a grid.
    # This is often called a "terrain map".
    points = vtkPoints()

    grid_size = 10
    for x in range(grid_size):
        for y in range(grid_size):
            points.InsertNextPoint(x, y, int((x + y) / (y + 1)))

    # Add the grid points to a polydata object.
    polydata = vtkPolyData()
    polydata.SetPoints(points)

    delaunay = vtkDelaunay2D(input_data=polydata)

    # Visualize
    mesh_mapper = vtkPolyDataMapper()
    delaunay >> mesh_mapper

    mesh_property = vtkProperty(color=colors.GetColor3d('LightGoldenrodYellow'),
                                edge_visibility=True, edge_color=colors.GetColor3d('CornflowerBlue'),
                                line_width=3, render_lines_as_tubes=True)

    mesh_actor = vtkActor(mapper=mesh_mapper, property=mesh_property)

    glyph_filter = vtkVertexGlyphFilter(input_data=polydata)

    point_mapper = vtkPolyDataMapper()
    glyph_filter >> point_mapper

    point_property = vtkProperty(color=colors.GetColor3d('DeepPink'),
                                 point_size=10, render_points_as_spheres=True)
    point_actor = vtkActor(mapper=point_mapper, property=point_property)

    renderer = vtkRenderer(background=colors.GetColor3d('PowderBlue'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='Delaunay2D')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(mesh_actor)
    renderer.AddActor(point_actor)

    render_window_interactor.Initialize()
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
