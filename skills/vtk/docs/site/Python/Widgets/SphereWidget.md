<!-- source: https://examples.vtk.org/site/Python/Widgets/SphereWidget/ -->

# SphereWidget

Repository source: [SphereWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Widgets/SphereWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Widgets/TestSphereWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Widgets/TestSphereWidget.png?raw=true target=)

### Description

This example shows how to use the SphereWidget.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/SphereWidget/)), ([PythonicAPI](../../PythonicAPI/Widgets/SphereWidget.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SphereWidget.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import vtkSphereWidget
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

# Call back function

def sphereCallback(obj, event):
    print('Center: {}, {}, {}'.format(*obj.GetCenter()))

def main():
    colors = vtkNamedColors()

    # colors.SetColor('bkg', [0.1, 0.2, 0.4, 1.0])

    # A renderer and render window
    renderer = vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('MidnightBlue'))

    renwin = vtkRenderWindow()
    renwin.AddRenderer(renderer)
    renwin.SetWindowName("SphereWidget")

    # An interactor
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renwin)

    # A Sphere widget
    sphereWidget = vtkSphereWidget()
    sphereWidget.SetInteractor(interactor)
    sphereWidget.SetRepresentationToSurface()
    sphereWidget.GetSphereProperty().SetColor(colors.GetColor3d("BurlyWood"))

    # Connect the event to a function
    sphereWidget.AddObserver("InteractionEvent", sphereCallback)

    # Start
    interactor.Initialize()
    renwin.Render()
    sphereWidget.On()
    interactor.Start()

if __name__ == '__main__':
    main()
```
