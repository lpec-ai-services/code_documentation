<!-- source: https://examples.vtk.org/site/PythonicAPI/Filtering/Glyph2D/ -->

# Glyph2D

Repository source: [Glyph2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Filtering/Glyph2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestGlyph2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestGlyph2D.png?raw=true target=)

### Description

Copy a polydata to every point in the input set. We use a hexagon for the demo.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/Glyph2D/)), ([Python](../../Python/Filtering/Glyph2D.md)), ([Java](https://examples.vtk.org/site/Java/Filtering/Glyph2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Glyph2D.py**

```python
#!/usr/bin/env python3

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
    polygon_source = vtkRegularPolygonSource()  # default is 6 sides

    glyph_2d = vtkGlyph2D(input_data=polydata, source_connection=polygon_source.output_port)

    mapper = vtkPolyDataMapper()
    glyph_2d >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('Salmon')

    # Visualize
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='Glyph2D')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style

    renderer.AddActor(actor)

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
