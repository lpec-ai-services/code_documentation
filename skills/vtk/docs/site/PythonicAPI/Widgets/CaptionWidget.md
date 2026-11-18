<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/CaptionWidget/ -->

# CaptionWidget

Repository source: [CaptionWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/CaptionWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestCaptionWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestCaptionWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/CaptionWidget/)), ([Java](https://examples.vtk.org/site/Java/Widgets/CaptionWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CaptionWidget.py**

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
from vtkmodules.vtkInteractionWidgets import (
    vtkCaptionRepresentation,
    vtkCaptionWidget
)
from vtkmodules.vtkRenderingAnnotation import vtkCaptionActor2D
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Sphere
    sphere_source = vtkSphereSource()

    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('DarkOliveGreen')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('Blue'))
    render_window = vtkRenderWindow(window_name='CaptionWidget')
    render_window.AddRenderer(renderer)

    # An interactor
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Create the widget and its representation.
    caption_actor = vtkCaptionActor2D(caption='TestCaption')
    caption_actor.text_actor.text_property.font_size = 100

    caption_representation = vtkCaptionRepresentation()
    caption_representation.SetCaptionActor2D(caption_actor)

    pos = (0.5, 0, 0)
    caption_representation.SetAnchorPosition(pos)

    caption_widget = vtkCaptionWidget(interactor=render_window_interactor, representation=caption_representation)

    # Add the actors to the scene.
    renderer.AddActor(actor)

    render_window.Render()

    # Rotate the camera to bring the point the caption is pointing to into view.
    renderer.GetActiveCamera().Azimuth(90)

    caption_widget.On()

    # Begin the mouse interaction.
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
