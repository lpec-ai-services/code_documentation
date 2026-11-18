<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/ParallelCoordinates/ -->

# ParallelCoordinates

Repository source: [ParallelCoordinates](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/ParallelCoordinates.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestParallelCoordinates.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestParallelCoordinates.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/ParallelCoordinates/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ParallelCoordinates.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import vtkChartParallelCoordinates
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    # Set up a 2D scene, add an XY chart to it.
    view = vtkContextView()
    view.GetRenderer().background = colors.GetColor3d('Gainsboro')
    view.GetRenderWindow().size = (800, 600)
    view.GetRenderWindow().window_name = 'ParallelCoordinates'

    chart = vtkChartParallelCoordinates()
    view.scene.AddItem(chart)

    # Create a table with some points in it...
    table = vtkTable()
    arr_x = vtkFloatArray(name='Field 1')
    table.AddColumn(arr_x)
    arr_c = vtkFloatArray(name='Field 2')
    table.AddColumn(arr_c)
    arr_s = vtkFloatArray(name='Field 3')
    table.AddColumn(arr_s)
    arr_s2 = vtkFloatArray(name='Field 4')
    table.AddColumn(arr_s2)

    # Test charting with a few more points...

    table.SetNumberOfRows(10)
    for i in range(0, 10):
        table.SetValue(i, 0, 0 * i)
        table.SetValue(i, 1, 1 * i)
        table.SetValue(i, 2, 2 * i)
        table.SetValue(i, 3, 3 * i)

    chart.GetPlot(0).SetInputData(table)

    for i in range(0, 4):
        chart.GetAxis(i).title_properties.font_size = 12
        chart.GetAxis(i).title_properties.color = colors.GetColor3d('Black')

    view.GetRenderWindow().multi_samples = 0

    view.GetRenderWindow().Render()
    view.GetInteractor().Initialize()
    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
