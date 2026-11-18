<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/ImagePlaneWidget/ -->

# ImagePlaneWidget

Repository source: [ImagePlaneWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/ImagePlaneWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImagePlaneWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImagePlaneWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/ImagePlaneWidget/)), ([Java](https://examples.vtk.org/site/Java/Widgets/ImagePlaneWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImagePlaneWidget.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import vtkImagePlaneWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='ImagePlaneWidget')
    render_window.AddRenderer(renderer)

    renderer.AddActor(actor)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # style = vtkInteractorStyleTrackballActor()
    style = vtkInteractorStyleTrackballCamera()

    render_window_interactor.interactor_style = style

    plane_widget = vtkImagePlaneWidget()
    plane_widget.interactor = render_window_interactor
    plane_widget.TextureVisibilityOff()

    origin = (0, 1, 0)
    plane_widget.origin = origin
    plane_widget.UpdatePlacement()

    # Render
    render_window.Render()

    renderer.active_camera.Azimuth(-45)
    renderer.active_camera.Zoom(0.85)

    render_window_interactor.Initialize()
    render_window.Render()
    plane_widget.On()

    # Begin mouse interaction.
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
