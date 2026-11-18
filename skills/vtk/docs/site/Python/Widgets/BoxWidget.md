<!-- source: https://examples.vtk.org/site/Python/Widgets/BoxWidget/ -->

# BoxWidget

Repository source: [BoxWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Widgets/BoxWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Widgets/TestBoxWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Widgets/TestBoxWidget.png?raw=true target=)

### Description

This example uses a [vtkBoxWidget](https://www.vtk.org/doc/nightly/html/classvtkBoxWidget.html) to manipulate an actor. The class includes geometry to draw a box around the object, which is bound to it via *SetProp3D*. The box is dimensioned using the `SetPlaceFactor` method, and positioned with the `PlaceWidget` method. After the initial setup, synchronizing the box with the object is done through a custom callback class, which is passed to the box widget through the `AddObserver` method.

For a widget that isn't tied to a specific [vtkProp3D](https://www.vtk.org/doc/nightly/html/classvtkProp3D.html) and has its geometric representation separate from the interaction logic, see the example [BoxWidget2](https://examples.vtk.org/site/Python/Widgets/BoxWidget2/) - to be written.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/BoxWidget/)), ([PythonicAPI](../../PythonicAPI/Widgets/BoxWidget.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BoxWidget.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkInteractionWidgets import vtkBoxWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

# Call back function to resize the cone

def boxCallback(obj, event):
    t = vtkTransform()
    obj.GetTransform(t)
    obj.GetProp3D().SetUserTransform(t)

def main():
    colors = vtkNamedColors()

    # Create a Cone
    cone = vtkConeSource()
    cone.SetResolution(20)
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('BurlyWood'))

    # A renderer and render window
    renderer = vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('Blue'))
    renderer.AddActor(coneActor)

    renwin = vtkRenderWindow()
    renwin.AddRenderer(renderer)
    renwin.SetWindowName('BoxWidget')

    # An interactor
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renwin)

    # A Box widget
    boxWidget = vtkBoxWidget()
    boxWidget.SetInteractor(interactor)
    boxWidget.SetProp3D(coneActor)
    boxWidget.SetPlaceFactor(1.25)  # Make the box 1.25x larger than the actor
    boxWidget.PlaceWidget()
    boxWidget.On()

    # Connect the event to a function
    boxWidget.AddObserver('InteractionEvent', boxCallback)

    # Start
    interactor.Initialize()
    renwin.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
