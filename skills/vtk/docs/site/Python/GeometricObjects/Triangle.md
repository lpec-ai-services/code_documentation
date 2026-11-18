<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Triangle/ -->

# Triangle

Repository source: [Triangle](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Triangle.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTriangle.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTriangle.png?raw=true target=)

### Description

The triangle is a primary two-dimensional cell. The triangle is defined by a counterclockwise ordered list of three points. The order of the points specifies the direction of the surface normal using the right-hand rule.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Triangle/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/Triangle/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Triangle/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Triangle.py**

```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkTriangle
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

    # Create a triangle
    points = vtkPoints()
    points.InsertNextPoint(1.0, 0.0, 0.0)
    points.InsertNextPoint(0.0, 0.0, 0.0)
    points.InsertNextPoint(0.0, 1.0, 0.0)

    triangle = vtkTriangle()
    triangle.GetPointIds().SetId(0, 0)
    triangle.GetPointIds().SetId(1, 1)
    triangle.GetPointIds().SetId(2, 2)

    triangles = vtkCellArray()
    triangles.InsertNextCell(triangle)

    # Create a polydata object
    trianglePolyData = vtkPolyData()

    # Add the geometry and topology to the polydata
    trianglePolyData.SetPoints(points)
    trianglePolyData.SetPolys(triangles)

    # Create mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(trianglePolyData)
    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d('PeachPuff'))
    actor.SetMapper(mapper)

    # Create a renderer, render window, and an interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Triangle')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkGreen'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
