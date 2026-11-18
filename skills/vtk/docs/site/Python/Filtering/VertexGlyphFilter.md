<!-- source: https://examples.vtk.org/site/Python/Filtering/VertexGlyphFilter/ -->

# VertexGlyphFilter

Repository source: [VertexGlyphFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Filtering/VertexGlyphFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Filtering/TestVertexGlyphFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Filtering/TestVertexGlyphFilter.png?raw=true target=)

### Description

This example creates a set of points and adds a vertex at each point using [vtkVertexGlyphFilter](https://www.vtk.org/doc/nightly/html/classvtkVertexGlyphFilter.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/VertexGlyphFilter/)), ([Java](https://examples.vtk.org/site/Java/Filtering/VertexGlyphFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**VertexGlyphFilter.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersGeneral import vtkVertexGlyphFilter
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
    points.InsertNextPoint(1, 1, 1)
    points.InsertNextPoint(2, 2, 2)

    polydata = vtkPolyData()
    polydata.SetPoints(points)

    vertexGlyphFilter = vtkVertexGlyphFilter()
    vertexGlyphFilter.AddInputData(polydata)
    vertexGlyphFilter.Update()

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(vertexGlyphFilter.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetPointSize(10)
    actor.GetProperty().SetColor(colors.GetColor3d('Yellow'))

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Green'))

    # Render and interact
    renderWindow.SetWindowName('VertexGlyphFilter')
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
