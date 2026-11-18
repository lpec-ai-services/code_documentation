<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/HoverWidget/ -->

# HoverWidget

Repository source: [HoverWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/HoverWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestHoverWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestHoverWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/HoverWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**HoverWidget.py**

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
from vtkmodules.vtkInteractionWidgets import vtkHoverWidget
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

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # A renderer and render window
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='HoverWidget')
    render_window.AddRenderer(renderer)

    renderer.AddActor(actor)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Create the widget
    hover_widget = vtkHoverWidget()
    hover_widget.interactor = render_window_interactor
    hover_widget.timer_duration = 1000

    # Create a callback to listen to the widget's two VTK events.
    hoverCallback = HoverCallback()
    hover_widget.AddObserver('TimerEvent', hoverCallback)
    hover_widget.AddObserver('EndInteractionEvent', hoverCallback)

    render_window.Render()

    render_window_interactor.Initialize()
    render_window.Render()
    hover_widget.On()

    render_window_interactor.Start()

class HoverCallback:

    def __call__(self, caller, ev):
        if ev == 'TimerEvent':
            print('TimerEvent -> The mouse stopped moving and the widget hovered.')
        if ev == 'EndInteractionEvent':
            print('EndInteractionEvent -> The mouse started to move.')

if __name__ == '__main__':
    main()
```
