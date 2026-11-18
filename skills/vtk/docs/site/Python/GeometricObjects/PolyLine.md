<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/PolyLine/ -->

# PolyLine

Repository source: [PolyLine](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/PolyLine.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPolyLine.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPolyLine.png?raw=true target=)

### Description

The polyline is a composite one-dimensional cell consisting of one or more connected lines. The polyline is defined by an ordered list of n+1 points, where n is the number of lines in the polyline. Each pair of points (i, i+1) defines a line.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/PolyLine/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/PolyLine/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PolyLine.py**

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
    vtkPolyData,
    vtkPolyLine
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

    # Create five points.
    origin = [0.0, 0.0, 0.0]
    p0 = [1.0, 0.0, 0.0]
    p1 = [0.0, 1.0, 0.0]
    p2 = [0.0, 1.0, 2.0]
    p3 = [1.0, 2.0, 3.0]

    # Create a vtkPoints object and store the points in it
    points = vtkPoints()
    points.InsertNextPoint(origin)
    points.InsertNextPoint(p0)
    points.InsertNextPoint(p1)
    points.InsertNextPoint(p2)
    points.InsertNextPoint(p3)

    polyLine = vtkPolyLine()
    polyLine.GetPointIds().SetNumberOfIds(5)
    for i in range(0, 5):
        polyLine.GetPointIds().SetId(i, i)

    # Create a cell array to store the lines in and add the lines to it
    cells = vtkCellArray()
    cells.InsertNextCell(polyLine)

    # Create a polydata to store everything in
    polyData = vtkPolyData()

    # Add the points to the dataset
    polyData.SetPoints(points)

    # Add the lines to the dataset
    polyData.SetLines(cells)

    # Setup actor and mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(polyData)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Tomato'))

    # Setup render window, renderer, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('PolyLine')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkOliveGreen'))

    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
