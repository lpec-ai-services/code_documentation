<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/WarpVector/ -->

# WarpVector

Repository source: [WarpVector](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/WarpVector.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestWarpVector.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestWarpVector.png?raw=true target=)

### Description

This script creates a [vtkLine](https://www.vtk.org/doc/nightly/html/classvtkLine.html) and deflects it using a [vtkWarpVector](https://www.vtk.org/doc/nightly/html/classvtkWarpVector.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/WarpVector/)), ([Python](../../Python/PolyData/WarpVector.md)), ([CSharp](https://examples.vtk.org/site/CSharp/PolyData/WarpVector/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**WarpVector.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkDoubleArray,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkLine,
    vtkPolyData
)
from vtkmodules.vtkFiltersGeneral import vtkWarpVector
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
    points.InsertNextPoint(0.0, 0.0, 0.0)
    points.InsertNextPoint(1.0, 0.0, 0.0)
    points.InsertNextPoint(2.0, 0.0, 0.0)
    points.InsertNextPoint(3.0, 0.0, 0.0)
    points.InsertNextPoint(4.0, 0.0, 0.0)

    lines = vtkCellArray()
    line = vtkLine()
    line.GetPointIds().SetId(0, 0)
    line.GetPointIds().SetId(1, 1)
    lines.InsertNextCell(line)
    line.GetPointIds().SetId(0, 1)
    line.GetPointIds().SetId(1, 2)
    lines.InsertNextCell(line)
    line.GetPointIds().SetId(0, 2)
    line.GetPointIds().SetId(1, 3)
    lines.InsertNextCell(line)
    line.GetPointIds().SetId(0, 3)
    line.GetPointIds().SetId(1, 4)
    lines.InsertNextCell(line)

    warp_data = vtkDoubleArray()
    warp_data.SetNumberOfComponents(3)
    warp_data.SetName('warpData')
    # We are warping in the y-direction.
    warp = [0.0, 0.0, 0.0]
    warp[1] = 0.0
    warp_data.InsertNextTuple(warp)
    warp[1] = 0.1
    warp_data.InsertNextTuple(warp)
    warp[1] = 0.3
    warp_data.InsertNextTuple(warp)
    warp[1] = 0.0
    warp_data.InsertNextTuple(warp)
    warp[1] = 0.1
    warp_data.InsertNextTuple(warp)

    polydata = vtkPolyData(points=points, lines=lines)
    polydata.point_data.AddArray(warp_data)
    polydata.point_data.SetActiveVectors(warp_data.name)

    # WarpVector will use the array marked as active vector in polydata
    # it has to be a 3 component array with the same number of tuples
    # as points in polydata.
    warp_vector = vtkWarpVector(input_data=polydata)

    mapper = vtkPolyDataMapper()
    warp_vector >> mapper

    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('cobalt_green'))
    renderer.AddActor(actor)
    ren_win = vtkRenderWindow(window_name='WarpVector')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
