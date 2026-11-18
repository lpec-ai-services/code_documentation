<!-- source: https://examples.vtk.org/site/Python/Interaction/MouseEventsObserver/ -->

# MouseEventsObserver

Repository source: [MouseEventsObserver](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Interaction/MouseEventsObserver.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Interaction/TestMouseEventsObserver.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Interaction/TestMouseEventsObserver.png?raw=true target=)

### Description

This example directly changes the observers of the vtkInteractor, which is an easy way to disable events or to add some simple callback functions. For a more general framework using [vtkInteractorStyle](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyle.html) see [MouseEvents](MouseEvents.md). This specific example just disables the left mouse button of the [vtkInteractorStyleTrackballCamera](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyleTrackballCamera.html) and prints a simple message instead.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/MouseEventsObserver/)), ([PythonicAPI](../../PythonicAPI/Interaction/MouseEventsObserver.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MouseEventsObserver.py**

```python
#!/usr/bin/env python

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

    source = vtkSphereSource()
    source.SetCenter(0, 0, 0)
    source.SetRadius(1)
    source.Update()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    renderer = vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('SlateGray'))
    renderer.AddActor(actor)

    renwin = vtkRenderWindow()
    renwin.AddRenderer(renderer)
    renwin.SetWindowName('MouseEventsObserver')

    interactor = vtkRenderWindowInteractor()
    interactor.SetInteractorStyle(vtkInteractorStyleTrackballCamera())
    interactor.SetRenderWindow(renwin)

    def DummyFunc1(obj, ev):
        print('Before Event')

    def DummyFunc2(obj, ev):
        print('After Event')

    # Print interator gives you a list of registered observers of the current
    # interactor style
    # print(interactor)

    # adding priorities allow to control the order of observer execution
    # (highest value first! if equal the first added observer is called first)
    interactor.RemoveObservers('LeftButtonPressEvent')
    interactor.AddObserver('LeftButtonPressEvent', DummyFunc1, 1.0)
    interactor.AddObserver('LeftButtonPressEvent', DummyFunc2, -1.0)
    interactor.Initialize()
    renwin.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
