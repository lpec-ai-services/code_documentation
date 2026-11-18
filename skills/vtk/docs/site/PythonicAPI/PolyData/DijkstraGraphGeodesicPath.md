<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/DijkstraGraphGeodesicPath/ -->

# DijkstraGraphGeodesicPath

Repository source: [DijkstraGraphGeodesicPath](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/DijkstraGraphGeodesicPath.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestDijkstraGraphGeodesicPath.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestDijkstraGraphGeodesicPath.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/DijkstraGraphGeodesicPath/)), ([CSharp](https://examples.vtk.org/site/CSharp/PolyData/DijkstraGraphGeodesicPath/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DijkstraGraphGeodesicPath.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersModeling import vtkDijkstraGraphGeodesicPath
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Create a sphere.
    sphere_source = vtkSphereSource()

    dijkstra = vtkDijkstraGraphGeodesicPath(start_vertex=0, end_vertex=7)

    # Create a mapper and actor.
    path_mapper = vtkPolyDataMapper()
    sphere_source >> dijkstra >> path_mapper

    path_actor = vtkActor(mapper=path_mapper)
    path_actor.property.color = colors.GetColor3d('HotPink')
    path_actor.property.line_width = 4

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    render_window = vtkRenderWindow(window_name='DijkstraGraphGeodesicPath')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(actor)
    renderer.AddActor(path_actor)

    camera = renderer.active_camera
    camera.position = (2.9, -1.6, 0.3)
    camera.focal_point = (0, 0, 0)
    camera.view_up = (0, 0, 1)
    camera.distance = 3
    camera.Zoom(1.5)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
