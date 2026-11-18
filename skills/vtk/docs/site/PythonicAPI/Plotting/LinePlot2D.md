<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/LinePlot2D/ -->

# LinePlot2D

Repository source: [LinePlot2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/LinePlot2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestLinePlot2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestLinePlot2D.png?raw=true target=)

### Description

This example demonstrates how to plot XY data.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/LinePlot2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LinePlot2D.py**

```python
# !/usr/bin/env python3

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# # noinspection PyUnresolvedReferences
# import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import vtkChartXY
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    # Create the data.
    table = vtkTable()

    arr_x = vtkFloatArray(name='X Axis')
    table.AddColumn(arr_x)

    arr_c = vtkFloatArray(name='Cosine')
    table.AddColumn(arr_c)

    arr_s = vtkFloatArray(name='Sine')
    table.AddColumn(arr_s)

    number_of_time_points = 1000
    table.SetNumberOfRows(number_of_time_points)

    # Fill in the table with some example values.
    num_points = 69
    inc = 7.5 / (num_points - 1)
    table.SetNumberOfRows(num_points)
    for i in range(0, num_points):
        table.SetValue(i, 0, i * inc)
        table.SetValue(i, 1, math.cos(i * inc))
        table.SetValue(i, 2, math.sin(i * inc))

    # Set up the view
    view = vtkContextView()
    view.render_window.window_name = 'LinePlot'
    view.renderer.background = colors.GetColor3d('SlateGray')

    # Add multiple line plots, setting the colors etc.
    chart = vtkChartXY()
    view.scene.AddItem(chart)
    line = chart.AddPlot(vtkChartXY.LINE)
    line.SetInputData(table, 0, 1)
    line.color = tuple(colors.GetColor4ub('Lime'))
    line.width = 1
    line = chart.AddPlot(vtkChartXY.LINE)
    line.SetInputData(table, 0, 2)
    line.color = tuple(colors.GetColor4ub('Red'))
    line.width = 5

    # Start interactor
    view.render_window.Render()
    view.interactor.Initialize()
    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
