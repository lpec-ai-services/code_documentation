<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/TriangleStrip/ -->

# TriangleStrip

Repository source: [TriangleStrip](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/TriangleStrip.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTriangleStrip.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTriangleStrip.png?raw=true target=)

### Description

The triangle strip is a composite two-dimensional cell consisting of one or more triangles. The points defining the triangle strip need not lie in a plane. The triangle strip is defined by an ordered list of n+2 points, where n is the number of triangles. The ordering of the points is such that each set of three points defines a triangle.

Info

See [this wikipedia article](http://en.wikipedia.org/wiki/Triangle_strip) for an explanation.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/TriangleStrip/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/TriangleStrip/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/TriangleStrip/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TriangleStrip.py**

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
    vtkTriangleStrip
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(0, 1, 0)
    points.InsertNextPoint(1, 0, 0)
    points.InsertNextPoint(1.5, 1, 0)

    triangleStrip = vtkTriangleStrip()
    triangleStrip.GetPointIds().SetNumberOfIds(4)
    triangleStrip.GetPointIds().SetId(0, 0)
    triangleStrip.GetPointIds().SetId(1, 1)
    triangleStrip.GetPointIds().SetId(2, 2)
    triangleStrip.GetPointIds().SetId(3, 3)

    cells = vtkCellArray()
    cells.InsertNextCell(triangleStrip)

    polydata = vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetStrips(cells)

    # Create an actor and mapper
    mapper = vtkDataSetMapper()
    mapper.SetInputData(polydata)
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('PeachPuff'))
    actor.GetProperty().SetRepresentationToWireframe()

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('TriangleStrip')
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
