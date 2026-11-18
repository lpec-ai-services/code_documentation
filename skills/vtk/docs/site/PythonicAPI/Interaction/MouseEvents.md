<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/MouseEvents/ -->

# MouseEvents

Repository source: [MouseEvents](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/MouseEvents.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestMouseEvents.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestMouseEvents.png?raw=true target=)

### Description

This example creates a new [vtkInteractorStyle](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyle.html) which can be used to implement custom reactions on user events. If you just want to disable single events you can also have a look at [MouseEventsObserver](MouseEventsObserver.md). This specific example just prints a simple message and then calls the original eventhandler of the [vtkInteractorStyleTrackballCamera](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyleTrackballCamera.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/MouseEvents/)), ([Python](../../Python/Interaction/MouseEvents.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MouseEvents.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

class MyInteractorStyle(vtkInteractorStyleTrackballCamera):

    def __init__(self, parent=None):
        super().__init__()

        self.AddObserver('MiddleButtonPressEvent', self.middle_button_press_event)
        self.AddObserver('MiddleButtonReleaseEvent', self.middle_button_release_event)

    def middle_button_press_event(self, obj, event):
        print('Middle Button pressed')
        self.OnMiddleButtonDown()
        return

    def middle_button_release_event(self, obj, event):
        print('Middle Button released')
        self.OnMiddleButtonUp()
        return

def main():
    colors = vtkNamedColors()

    source = vtkSphereSource(center=(0, 0, 0), radius=1)

    mapper = vtkPolyDataMapper()
    source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    renderer.AddActor(actor)

    renwin = vtkRenderWindow(window_name='MouseEvents')
    renwin.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.interactor_style = MyInteractorStyle()
    interactor.render_window = renwin

    interactor.Initialize()
    renwin.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
