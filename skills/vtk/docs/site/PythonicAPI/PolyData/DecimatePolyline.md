<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/DecimatePolyline/ -->

# DecimatePolyline

Repository source: [DecimatePolyline](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/DecimatePolyline.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestDecimatePolyline.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestDecimatePolyline.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/DecimatePolyline/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DecimatePolyline.py**

```python
#!/usr/bin/env python3

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData)
from vtkmodules.vtkFiltersCore import vtkDecimatePolylineFilter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    number_of_points = 100

    circle = vtkPolyData()
    points = vtkPoints()
    lines = vtkCellArray()
    line_indices = list()

    for i in range(0, number_of_points):
        angle = 2.0 * math.pi * float(i) / float(number_of_points)
        points.InsertPoint(i, math.cos(angle), math.sin(angle), 0.0)
        line_indices.append(i)

    line_indices.append(0)
    lines.InsertNextCell(number_of_points + 1, line_indices)

    circle.SetPoints(points)
    circle.SetLines(lines)

    c_mapper = vtkPolyDataMapper(input_data=circle)

    colors = vtkNamedColors()

    c_actor = vtkActor(mapper=c_mapper)
    c_actor.property.color = colors.GetColor3d('Banana')
    c_actor.property.line_width = 3

    decimate = vtkDecimatePolylineFilter(input_data=circle, target_reduction=0.95)
    decimate.Update()

    d_mapper = vtkPolyDataMapper()
    decimate >> d_mapper

    d_actor = vtkActor(mapper=d_mapper)
    d_actor.property.color = colors.GetColor3d('Tomato')
    d_actor.property.line_width = 3

    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren.AddActor(c_actor)
    ren.AddActor(d_actor)

    ren_win = vtkRenderWindow(size=(640, 480), window_name='DecimatePolyline')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    ren_win.Render()

    iren.Start()

if __name__ == '__main__':
    main()
```
