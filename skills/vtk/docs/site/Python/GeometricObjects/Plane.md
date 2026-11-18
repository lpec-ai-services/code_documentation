<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Plane/ -->

# Plane

Repository source: [Plane](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Plane.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPlane.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPlane.png?raw=true target=)

### Description

[vtkPlaneSource](https://www.vtk.org/doc/nightly/html/classvtkPlaneSource.html) object creates an m x n array of quadrilaterals arranged as a regular tiling in a plane.

The plane is defined by specifying an origin point, and then two other points that, together with the origin, define two axes for the plane. These axes do not have to be orthogonal - so you can create a parallelogram. (The axes must not be parallel.) The resolution of the plane (i.e., number of subdivisions) is controlled by the ivars XResolution and YResolution.

By default, the plane is centered at the origin and perpendicular to the z-axis, with width and height of length 1 and resolutions set to 1.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Plane/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Plane/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Plane.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkPlaneSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor('BkgColor', [26, 51, 77, 255])

    # Create a plane
    planeSource = vtkPlaneSource()
    planeSource.SetCenter(1.0, 0.0, 0.0)
    planeSource.SetNormal(1.0, 0.0, 1.0)
    planeSource.Update()

    plane = planeSource.GetOutput()

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(plane)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Banana'))

    # Create a renderer, render window and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Plane')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('BkgColor'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
