<!-- source: https://examples.vtk.org/site/Python/Visualization/DisplayCoordinateAxes/ -->

# DisplayCoordinateAxes

Repository source: [DisplayCoordinateAxes](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/DisplayCoordinateAxes.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestDisplayCoordinateAxes.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestDisplayCoordinateAxes.png?raw=true target=)

### Description

This example shows how to display the coordinate axes in the render window.

Seealso

[Axes](../GeometricObjects/Axes.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/DisplayCoordinateAxes/)), ([Java](https://examples.vtk.org/site/Java/Visualization/DisplayCoordinateAxes/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DisplayCoordinateAxes.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionWidgets import vtkOrientationMarkerWidget
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
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
    sphereSource.SetRadius(1.0)
    sphereSource.Update()

    polydata = sphereSource.GetOutput()

    # Create a mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(polydata)

    # Create an actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    # A renderer and render window
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('DisplayCoordinateAxes')
    renderWindow.AddRenderer(renderer)

    # An interactor
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))

    axes = vtkAxesActor()

    widget = vtkOrientationMarkerWidget()
    rgba = [0] * 4
    colors.GetColor('Carrot', rgba)
    widget.SetOutlineColor(rgba[0], rgba[1], rgba[2])
    widget.SetOrientationMarker(axes)
    widget.SetInteractor(renderWindowInteractor)
    widget.SetViewport(0.0, 0.0, 0.4, 0.4)
    widget.SetEnabled(1)
    widget.InteractiveOn()

    renderer.GetActiveCamera().Azimuth(50)
    renderer.GetActiveCamera().Elevation(-30)

    renderer.ResetCamera()
    renderWindow.Render()

    # Begin mouse interaction
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
