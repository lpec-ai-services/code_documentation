<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Line/ -->

# Line

Repository source: [Line](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Line.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestLine.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestLine.png?raw=true target=)

### Description

The line is a primary one-dimensional cell. It is defined by two points. The direction along the line is from the first point to the second point.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Line/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/Line/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Line/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Line.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkLineSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    # Create two points, P0 and P1
    p0 = [1.0, 0.0, 0.0]
    p1 = [0.0, 1.0, 0.0]

    lineSource = vtkLineSource()
    lineSource.SetPoint1(p0)
    lineSource.SetPoint2(p1)

    # Visualize
    colors = vtkNamedColors()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(lineSource.GetOutputPort())
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetLineWidth(4)
    actor.GetProperty().SetColor(colors.GetColor3d("Peacock"))

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName("Line")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.SetBackground(colors.GetColor3d("Silver"))
    renderer.AddActor(actor)

    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
