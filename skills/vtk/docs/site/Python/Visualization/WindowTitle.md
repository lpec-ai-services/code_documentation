<!-- source: https://examples.vtk.org/site/Python/Visualization/WindowTitle/ -->

# WindowTitle

Repository source: [WindowTitle](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/WindowTitle.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestWindowTitle.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestWindowTitle.png?raw=true target=)

### Description

This example demonstrates how to change the title of a render window.

- Contributed by Bryan P. Conrad

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/WindowTitle/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**WindowTitle.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphereSource = vtkSphereSource()
    sphereSource.SetCenter(0.0, 0.0, 0.0)
    sphereSource.SetRadius(5)

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    # Setup a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    # renderWindow.SetWindowName('Test')

    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))

    # Render and interact
    renderWindow.Render()
    # *** SetWindowName after renderWindow.Render() is called ***
    renderWindow.SetWindowName('WindowTitle')
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
