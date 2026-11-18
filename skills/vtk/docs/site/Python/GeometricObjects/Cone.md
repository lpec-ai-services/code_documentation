<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Cone/ -->

# Cone

Repository source: [Cone](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Cone.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestCone.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestCone.png?raw=true target=)

### Description

[vtkConeSource](https://www.vtk.org/doc/nightly/html/classvtkConeSource.html) object creates a cone centered at a specified point and pointing in a specified direction. (By default, the center is the origin and the direction is the x-axis.)

Depending upon the resolution of this object, different representations are created. If resolution=0 a line is created; if resolution=1, a single triangle is created; if resolution=2, two crossed triangles are created.

For resolution > 2, a 3D cone (with resolution number of sides) is created.

It also is possible to control whether the bottom of the cone is capped with a (resolution-sided) polygon, and to specify the height and radius of the cone.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Cone/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/Cone/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Cone/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Cone.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    coneSource = vtkConeSource()
    # coneSource.SetResolution(60)
    # coneSource.SetCenter(-2,0,0)

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(coneSource.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d('bisque'))

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Salmon'))

    renderWindow.SetSize(640, 480)
    renderWindow.SetWindowName('Cone')
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
