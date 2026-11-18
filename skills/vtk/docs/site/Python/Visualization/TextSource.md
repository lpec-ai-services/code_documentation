<!-- source: https://examples.vtk.org/site/Python/Visualization/TextSource/ -->

# TextSource

Repository source: [TextSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/TextSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestTextSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestTextSource.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/TextSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TextSource.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkTextSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    textSource = vtkTextSource()
    textSource.SetText("Hello")
    textSource.SetForegroundColor(colors.GetColor3d('DarkSlateGray'))
    textSource.SetBackgroundColor(colors.GetColor3d('NavajoWhite'))
    # Turn off if you don't want the background drawn with the text.
    textSource.BackingOn()
    textSource.Update()

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(textSource.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('TextSource')

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Bisque'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
