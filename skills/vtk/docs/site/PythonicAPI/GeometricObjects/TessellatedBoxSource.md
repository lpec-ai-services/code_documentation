<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/TessellatedBoxSource/ -->

# TessellatedBoxSource

Repository source: [TessellatedBoxSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/TessellatedBoxSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestTessellatedBoxSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestTessellatedBoxSource.png?raw=true target=)

### Description

Generates a box(cube) using [vtkTessellatedBoxSource](https://www.vtk.org/doc/nightly/html/classvtkTessellatedBoxSource.html) with 6 sides. The faces of the box can be subdivided into multiple triangles or quads.

Seealso

[Cube](https://examples.vtk.org/site/PythonicAPI/GeometricObjects/Cube/) generates multiple quads or triangles per side.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/TessellatedBoxSource/)), ([Python](../../Python/GeometricObjects/TessellatedBoxSource.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TessellatedBoxSource.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonExecutionModel import vtkAlgorithm
from vtkmodules.vtkFiltersGeneral import vtkShrinkFilter
from vtkmodules.vtkFiltersSources import vtkTessellatedBoxSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    bounds = [-10.0, 10.0, 10.0, 20.0, -5.0, 5.0]

    box_source = vtkTessellatedBoxSource(level=3, quads=True, bounds=bounds,
                                         output_points_precision=vtkAlgorithm.SINGLE_PRECISION)

    shrink = vtkShrinkFilter(shrink_factor=0.8)

    # Create a mapper and actor.
    mapper = vtkDataSetMapper()
    box_source >> shrink >> mapper

    back = vtkProperty()
    back.color = colors.GetColor3d('Tomato')

    actor = vtkActor(mapper=mapper)
    actor.property.edge_visibility = True
    actor.property.color = colors.GetColor3d('Banana')
    actor.backface_property = back

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='TessellatedBoxSource')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(actor)

    renderer.ResetCamera()
    renderer.active_camera.Azimuth(30)
    renderer.active_camera.Elevation(30)
    renderer.ResetCameraClippingRange()

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
