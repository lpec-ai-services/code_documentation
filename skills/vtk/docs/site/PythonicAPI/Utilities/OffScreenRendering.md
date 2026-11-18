<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/OffScreenRendering/ -->

# OffScreenRendering

Repository source: [OffScreenRendering](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/OffScreenRendering.py)

### Description

This example renders a scene directly to a file without displaying a window. You must turn on VTK_OPENGL_HAS_OSMESA in the VTK advanced build configuration.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/OffScreenRendering/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OffScreenRendering.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOImage import vtkPNGWriter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkGraphicsFactory,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkWindowToImageFilter
)

def main():
    colors = vtkNamedColors()

    # Setup off-screen rendering.
    graphics_factory = vtkGraphicsFactory(off_screen_only_mode=True, use_mesa_classes=True)

    # Create a sphere
    sphere_source = vtkSphereSource()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('White')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(off_screen_rendering=True)
    render_window.AddRenderer(renderer)

    # Add the actor to the scene.
    renderer.AddActor(actor)

    render_window.Render()

    window_to_image_filter = vtkWindowToImageFilter(input=render_window)
    window_to_image_filter.update()

    writer = vtkPNGWriter()
    writer.SetFileName('screenshot.png')
    window_to_image_filter >> writer
    writer.Write()

if __name__ == '__main__':
    main()
```
