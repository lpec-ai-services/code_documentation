<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Circle/ -->

# Circle

Repository source: [Circle](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Circle.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestCircle.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestCircle.png?raw=true target=)

### Description

A circle is simply the limiting case of a regular polygon. We use [vtkRegularPolygonSource](https://www.vtk.org/doc/nightly/html/classvtkRegularPolygonSource.html) with a large number of Sides to approximate a circle.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Circle/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/Circle/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Circle.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkRegularPolygonSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create a circle
    polygonSource = vtkRegularPolygonSource()
    # Comment this line to generate a disk instead of a circle.
    polygonSource.GeneratePolygonOff()
    polygonSource.SetNumberOfSides(50)
    polygonSource.SetRadius(5.0)
    polygonSource.SetCenter(0.0, 0.0, 0.0)

    #  Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(polygonSource.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Cornsilk'))

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName("Circle")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkGreen'))

    renderWindow.SetWindowName('Circle')
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
