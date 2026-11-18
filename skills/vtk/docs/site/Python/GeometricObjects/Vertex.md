<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Vertex/ -->

# Vertex

Repository source: [Vertex](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Vertex.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestVertex.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestVertex.png?raw=true target=)

### Description

The vertex is a primary zero-dimensional cell. It is defined by a single point.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Vertex/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/Vertex/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Vertex/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Vertex.py**

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
    vtkVertex
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

    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)

    vertex = vtkVertex()
    vertex.GetPointIds().SetId(0, 0)

    vertices = vtkCellArray()
    vertices.InsertNextCell(vertex)

    polydata = vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetVerts(vertices)

    # Setup actor and mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(polydata)
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetPointSize(30)
    actor.GetProperty().SetColor(colors.GetColor3d('PeachPuff'))

    # Setup render window, renderer, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Vertex')
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
