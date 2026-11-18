<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/ImageTracerWidgetNonPlanar/ -->

# ImageTracerWidgetNonPlanar

Repository source: [ImageTracerWidgetNonPlanar](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/ImageTracerWidgetNonPlanar.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImageTracerWidgetNonPlanar.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImageTracerWidgetNonPlanar.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/ImageTracerWidgetNonPlanar/)), ([Java](https://examples.vtk.org/site/Java/Widgets/ImageTracerWidgetNonPlanar/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageTracerWidgetNonPlanar.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import vtkImageTracerWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
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
    render_window = vtkRenderWindow(window_name='ImageTracerWidgetNonPlanar')
    render_window.AddRenderer(renderer)

    renderer.AddActor(actor)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    style = vtkInteractorStyleTrackballCamera()
    render_window_interactor.interactor_style = style

    tracer_widget = vtkImageTracerWidget()
    tracer_widget.interactor = render_window_interactor
    tracer_widget.SetViewProp(actor)

    render_window.Render()

    render_window_interactor.Initialize()
    render_window.Render()
    tracer_widget.On()

    # Begin the mouse interaction.
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
