<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/ColoredSphere/ -->

# ColoredSphere

Repository source: [ColoredSphere](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/ColoredSphere.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestColoredSphere.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestColoredSphere.png?raw=true target=)

### Description

This demonstrates a simple visualization pipeline. A polygonal representation of a sphere is created with the source object ([vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html)). The sphere is passed through a filter ([vtkElevationFilter](https://www.vtk.org/doc/nightly/html/classvtkElevationFilter.html)) that computes the height of each point of the sphere above a plane. The plane is perpendicular to the z-axis, and passes through the point (0,0,-1). The data is finally mapped ([vtkDataSetMapper](https://www.vtk.org/doc/nightly/html/classvtkDataSetMapper.html)) through a lookup table. The mapping process converts height value into colors, and interfaces the sphere geometry to the rendering library. The mapper is assigned to an actor, and then the actor is displayed.

The execution of the pipeline occurs implicitly when we render the actor. Each actor asks its mapper to update itself. The mapper in turn asks its input to update itself. This process continues until a source object is encountered. Then the source will execute if modified since the last render.

Info

See [Figure 4-19](../../VTKBook/04Chapter4.md#Figure%204-19) in [Chapter 4](../../VTKBook/04Chapter4.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/ColoredSphere/)), ([Python](../../Python/Rendering/ColoredSphere.md)), ([Java](https://examples.vtk.org/site/Java/Rendering/ColoredSphere/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ColoredSphere.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkElevationFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphere = vtkSphereSource(phi_resolution=12, theta_resolution=12)

    color_it = vtkElevationFilter(low_point=(0, 0, -1), high_point=(0, 0, 1))

    mapper = vtkDataSetMapper()
    sphere >> color_it >> mapper

    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name='ColoredSphere')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    renderer.AddActor(actor)

    ren_win.Render()

    # Interact with the data.
    iren.Start()

if __name__ == '__main__':
    main()
```
