<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/MouseEventsObserver/ -->

# MouseEventsObserver

Repository source: [MouseEventsObserver](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/MouseEventsObserver.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestMouseEventsObserver.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestMouseEventsObserver.png?raw=true target=)

### Description

This example directly changes the observers of the vtkInteractor, which is an easy way to disable events or to add some simple callback functions. For a more general framework using [vtkInteractorStyle](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyle.html) see [MouseEvents](MouseEvents.md). This specific example just disables the left mouse button of the [vtkInteractorStyleTrackballCamera](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyleTrackballCamera.html) and prints a simple message instead.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/MouseEventsObserver/)), ([Python](../../Python/Interaction/MouseEventsObserver.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MouseEventsObserver.py**

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

def main():
    colors = vtkNamedColors()

    source = vtkSphereSource(center=(0, 0, 0), radius=1)

    mapper = vtkPolyDataMapper()
    source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    renderer.AddActor(actor)

    renwin = vtkRenderWindow(window_name='MouseEventsObserver')
    renwin.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.interactor_style = vtkInteractorStyleTrackballCamera()
    interactor.render_window = renwin

    def dummy_func1(obj, ev):
        print('Before Event')

    def dummy_func2(obj, ev):
        print('After Event')

    # Printing the interator gives you a list of registered
    #  observers of the current interactor style.
    # print(interactor)

    # Adding priorities allow to control the order of observer execution
    # (highest value first! If equal, the first added observer is called first).
    interactor.RemoveObservers('LeftButtonPressEvent')
    interactor.AddObserver('LeftButtonPressEvent', dummy_func1, 1.0)
    interactor.AddObserver('LeftButtonPressEvent', dummy_func2, -1.0)
    interactor.Initialize()
    renwin.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
