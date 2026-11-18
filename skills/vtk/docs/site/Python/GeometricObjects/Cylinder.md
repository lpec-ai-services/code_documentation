<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Cylinder/ -->

# Cylinder

Repository source: [Cylinder](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Cylinder.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestCylinder.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestCylinder.png?raw=true target=)

### Description

[vtkCylinderSource](https://www.vtk.org/doc/nightly/html/classvtkCylinderSource.html) object creates a polygonal cylinder centered at Center.

The axis of the cylinder is aligned along the global y-axis. The height and radius of the cylinder can be specified, as well as the number of sides.

It is also possible to control whether the cylinder is open-ended or capped. If you have the end points of the cylinder, you should use a [vtkLineSource](https://www.vtk.org/doc/nightly/html/classvtkLineSource.html) followed by a [vtkTubeFilter](https://www.vtk.org/doc/nightly/html/classvtkTubeFilter.html) instead of the [vtkCylinderSource](https://www.vtk.org/doc/nightly/html/classvtkCylinderSource.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Cylinder/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Cylinder/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Cylinder.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create a sphere
    cylinderSource = vtkCylinderSource()
    cylinderSource.SetCenter(0.0, 0.0, 0.0)
    cylinderSource.SetRadius(5.0)
    cylinderSource.SetHeight(7.0)
    cylinderSource.SetResolution(100)

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cylinderSource.GetOutputPort())
    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d('Cornsilk'))
    actor.SetMapper(mapper)

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Cylinder')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkGreen'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
