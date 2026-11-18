<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/PieChartActor/ -->

# PieChartActor

Repository source: [PieChartActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/PieChartActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestPieChartActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestPieChartActor.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/PieChartActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PieChartActor.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import (
    vtkNamedColors,
    vtkColorSeries
)
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkDataObject
from vtkmodules.vtkRenderingAnnotation import vtkPieChartActor
from vtkmodules.vtkRenderingCore import (
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    movies = {
        'Comedy': 27,
        'Action': 18,
        'Romance': 14,
        'Drama': 14,
        'Horror': 11,
        'Foreign': 8,
        'Scifi': 8
    }
    keys = list(sorted(movies.keys()))

    num_tuples = len(movies)
    bitter = vtkFloatArray(number_of_tuples=num_tuples)

    i = 0
    for k in keys:
        bitter.SetTuple1(i, movies[k])
        i += 1

    dobj = vtkDataObject()
    dobj.field_data.AddArray(bitter)

    colors = vtkNamedColors()

    actor = vtkPieChartActor(input_data=dobj, title='Movie Watching')
    actor.GetPositionCoordinate().SetValue(0.05, 0.1, 0.0)
    actor.GetPosition2Coordinate().SetValue(0.95, 0.85, 0.0)
    actor.property.color = colors.GetColor3d('Black')
    actor.property.line_width = 2
    actor.legend_actor.number_of_entries = num_tuples

    color_series = vtkColorSeries()
    color_series.color_scheme = vtkColorSeries.BREWER_QUALITATIVE_PASTEL2
    i = 0
    for k in keys:
        rgb = color_series.GetColorRepeating(i)
        actor.SetPieceColor(i, rgb.GetRed() / 255.0, rgb.GetGreen() / 255.0, rgb.GetBlue() / 255.0)
        actor.SetPieceLabel(i, k)
        i += 1

    actor.legend_visibility = True
    # Set text colors (same as actor for backward compat with test).
    actor.title_text_property.color = colors.GetColor3d('Banana')
    actor.title_text_property.font_size = 40
    actor.label_text_property.color = colors.GetColor3d('Bisque')
    actor.label_text_property.font_size = 24

    # Create the RenderWindow, Renderer and both Actors.
    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(1024, 512), window_name='PieChartActor')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    ren.AddActor(actor)

    # Render the image.
    ren_win.Render()

    iren.Start()

if __name__ == '__main__':
    main()
```
