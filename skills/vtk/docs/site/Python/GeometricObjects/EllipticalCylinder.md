<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/EllipticalCylinder/ -->

# EllipticalCylinder

Repository source: [EllipticalCylinder](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/EllipticalCylinder.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestEllipticalCylinder.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestEllipticalCylinder.png?raw=true target=)

### Description

The example creates an elliptical cross-section and stores it in a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). Then, the [vtkLinearExtrusionFilter](https://www.vtk.org/doc/nightly/html/classvtkLinearExtrusionFilter.html) creates an elliptical cylinder by extruding the [vtkPolyLine](https://www.vtk.org/doc/nightly/html/classvtkPolyLine.html) along a vector. The example sets the backface property of the [vtkActor](https://www.vtk.org/doc/nightly/html/classvtkActor.html) to show the front and back face of the cylinder.

Seealso

[EllipticalCylinderDemo](EllipticalCylinderDemo.md) to see the [vtkPolyLine](https://www.vtk.org/doc/nightly/html/classvtkPolyLine.html) and the vector represented as an oriented

arrow.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/EllipticalCylinder/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/EllipticalCylinder/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**EllipticalCylinder.py**

```python
#!/usr/bin/env python3

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkMath,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkPolyLine
)
from vtkmodules.vtkFiltersModeling import vtkLinearExtrusionFilter
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    angle = 0
    r1 = 50
    r2 = 30
    centerX = 10.0
    centerY = 5.0

    points = vtkPoints()
    idx = 0
    while angle <= 2.0 * vtkMath.Pi() + (vtkMath.Pi() / 60.0):
        points.InsertNextPoint(r1 * math.cos(angle) + centerX,
                               r2 * math.sin(angle) + centerY,
                               0.0)
        angle = angle + (vtkMath.Pi() / 60.0)
        idx += 1

    line = vtkPolyLine()
    line.GetPointIds().SetNumberOfIds(idx)
    for i in range(0, idx):
        line.GetPointIds().SetId(i, i)

    lines = vtkCellArray()
    lines.InsertNextCell(line)

    polyData = vtkPolyData()
    polyData.SetPoints(points)
    polyData.SetLines(lines)

    extrude = vtkLinearExtrusionFilter()
    extrude.SetInputData(polyData)
    extrude.SetExtrusionTypeToNormalExtrusion()
    extrude.SetVector(0, 0, 100.0)
    extrude.Update()

    lineMapper = vtkPolyDataMapper()
    lineMapper.SetInputData(polyData)

    lineActor = vtkActor()
    lineActor.SetMapper(lineMapper)
    lineActor.GetProperty().SetColor(colors.GetColor3d("Peacock"))

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(extrude.GetOutputPort())

    back = vtkProperty()
    back.SetColor(colors.GetColor3d("Tomato"))

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d("Banana"))
    actor.SetBackfaceProperty(back)

    ren = vtkRenderer()
    ren.SetBackground(colors.GetColor3d("SlateGray"))
    ren.AddActor(actor)
    ren.AddActor(lineActor)

    renWin = vtkRenderWindow()
    renWin.SetWindowName("EllipticalCylinder")
    renWin.AddRenderer(ren)
    renWin.SetSize(600, 600)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    style = vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)

    camera = vtkCamera()
    camera.SetPosition(0, 1, 0)
    camera.SetFocalPoint(0, 0, 0)
    camera.SetViewUp(0, 0, 1)
    camera.Azimuth(30)
    camera.Elevation(30)

    ren.SetActiveCamera(camera)
    ren.ResetCamera()
    ren.ResetCameraClippingRange()

    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
