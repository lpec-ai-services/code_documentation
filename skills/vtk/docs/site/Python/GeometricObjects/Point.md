<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Point/ -->

# Point

Repository source: [Point](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Point.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPoint.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPoint.png?raw=true target=)

### Description

[vtkPoints](https://www.vtk.org/doc/nightly/html/classvtkPoints.html) object represents 3D points. The data model for [vtkPoints](https://www.vtk.org/doc/nightly/html/classvtkPoints.html) is an array of vx-vy-vz triplets accessible by ( point or cell) id.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Point/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Point/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Point.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create the geometry of a point (the coordinate)
    points = vtkPoints()
    p = [1.0, 2.0, 3.0]

    # Create the topology of the point (a vertex)
    vertices = vtkCellArray()
    # We need an an array of point id's for InsertNextCell.
    pid = [0]
    pid[0] = points.InsertNextPoint(p)
    vertices.InsertNextCell(1, pid)

    # Create a polydata object
    point = vtkPolyData()

    # Set the points and vertices we created as the geometry and topology of the polydata
    point.SetPoints(points)
    point.SetVerts(vertices)

    # Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(point)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Tomato'))
    actor.GetProperty().SetPointSize(20)

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Point')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkGreen'))

    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
