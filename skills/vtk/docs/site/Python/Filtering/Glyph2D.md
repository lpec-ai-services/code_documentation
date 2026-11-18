<!-- source: https://examples.vtk.org/site/Python/Filtering/Glyph2D/ -->

# Glyph2D

Repository source: [Glyph2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Filtering/Glyph2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Filtering/TestGlyph2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Filtering/TestGlyph2D.png?raw=true target=)

### Description

Copy a polydata to every point in the input set. We use a hexagon for the demo.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/Glyph2D/)), ([PythonicAPI](../../PythonicAPI/Filtering/Glyph2D.md)), ([Java](https://examples.vtk.org/site/Java/Filtering/Glyph2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Glyph2D.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import vtkGlyph2D
from vtkmodules.vtkFiltersSources import vtkRegularPolygonSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
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
    points.InsertNextPoint(1, 1, 0)
    points.InsertNextPoint(2, 2, 0)

    polydata = vtkPolyData()
    polydata.SetPoints(points)

    # Create anything you want here, we will use a polygon for the demo.
    polygonSource = vtkRegularPolygonSource()  # default is 6 sides

    glyph2D = vtkGlyph2D()
    glyph2D.SetSourceConnection(polygonSource.GetOutputPort())
    glyph2D.SetInputData(polydata)
    glyph2D.Update()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph2D.GetOutputPort())
    mapper.Update()

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Salmon'))

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))

    style = vtkInteractorStyleImage()
    renderWindowInteractor.SetInteractorStyle(style)

    renderWindow.SetWindowName('Glyph2D');
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
