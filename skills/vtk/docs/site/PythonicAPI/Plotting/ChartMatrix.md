<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/ChartMatrix/ -->

# ChartMatrix

Repository source: [ChartMatrix](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/ChartMatrix.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestChartMatrix.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestChartMatrix.png?raw=true target=)

### Description

This example illustrates the use [vtkChartMatrix](https://www.vtk.org/doc/nightly/html/classvtkChartMatrix.html), a container that holds a matrix of charts. The example creates a 2 x 2 matrix of plots. The matrix elements are:

- (0,0): a [vtkPlotPoints](https://www.vtk.org/doc/nightly/html/classvtkPlotPoints.html)
- (0,1): a [vtkPlotPoints](https://www.vtk.org/doc/nightly/html/classvtkPlotPoints.html)
- (1,0): a [vtkPlotLine](https://www.vtk.org/doc/nightly/html/classvtkPlotLine.html)
- (1,1): a [vtkPlotBar](https://www.vtk.org/doc/nightly/html/classvtkPlotBar.html) and a [vtkPlotPoints](https://www.vtk.org/doc/nightly/html/classvtkPlotPoints.html)

The example also illustrates how to use [vtkNamedColors](https://www.vtk.org/doc/nightly/html/classvtkNamedColors.html) to set the colors for the plots.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/ChartMatrix/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ChartMatrix.py**

```python
#!/usr/bin/env python3

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import (
    vtkChart,
    vtkPlotPoints, vtkChartMatrix
)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import (
    vtkTable,
    vtkVector2i,
    vtkVector2f
)
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    # Set up a 2D scene, add an XY chart to it.
    view = vtkContextView()
    view.GetRenderWindow().size = (1280, 1024)
    view.GetRenderWindow().window_name = 'ChartMatrix'

    matrix = vtkChartMatrix()
    view.scene.AddItem(matrix)
    matrix.SetSize(vtkVector2i(2, 2))
    matrix.SetGutter(vtkVector2f(30.0, 30.0))

    # Create a table with some points in it...
    table = vtkTable()

    arr_x = vtkFloatArray(name='X Axis')
    table.AddColumn(arr_x)

    arr_c = vtkFloatArray(name='Cosine')
    table.AddColumn(arr_c)

    arr_s = vtkFloatArray(name='Sine')
    table.AddColumn(arr_s)

    arr_s2 = vtkFloatArray(name='Sine2')
    table.AddColumn(arr_s2)

    tangent = vtkFloatArray(name='Tangent')
    table.AddColumn(tangent)

    num_points = 42
    inc = 7.5 / (num_points - 1)
    table.SetNumberOfRows(num_points)
    for i in range(0, num_points):
        table.SetValue(i, 0, i * inc)
        table.SetValue(i, 1, math.cos(i * inc))
        table.SetValue(i, 2, math.sin(i * inc))
        table.SetValue(i, 3, math.sin(i * inc) + 0.5)
        table.SetValue(i, 4, math.tan(i * inc))

    # Add multiple line plots, setting the colors etc.

    #  Plot colors
    ll_color = colors.GetColor3ub('sea_green')
    ul_color = colors.GetColor3ub('rose_madder')
    ur_color = colors.GetColor3ub('burnt_sienna')
    ur_color1 = colors.GetColor3ub('rose_madder')
    lr_color = colors.GetColor3ub('dark_orange')
    lr_color1 = colors.GetColor3ub('royal_blue')

    # Lower left plot, a point chart.
    chart = matrix.GetChart(vtkVector2i(0, 0))
    plot = chart.AddPlot(vtkChart.POINTS)
    plot.SetInputData(table, 0, 1)
    plot.SetMarkerStyle(vtkPlotPoints.DIAMOND)
    plot.GetXAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.GetYAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.color = (ll_color.red, ll_color.green, ll_color.blue, 255)

    # Upper left plot, a point chart.
    chart = matrix.GetChart(vtkVector2i(0, 1))
    plot = chart.AddPlot(vtkChart.POINTS)
    plot.SetInputData(table, 0, 2)
    plot.GetXAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.GetYAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.color = (ul_color.red, ul_color.green, ul_color.blue, 255)

    # Upper right plot, a bar and point chart.
    chart = matrix.GetChart(vtkVector2i(1, 1))
    plot = chart.AddPlot(vtkChart.BAR)
    plot.SetInputData(table, 0, 4)
    plot.GetXAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.GetYAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.color = (ur_color.red, ur_color.green, ur_color.blue, 255)

    plot = chart.AddPlot(vtkChart.POINTS)
    plot.SetInputData(table, 0, 3)
    plot.SetMarkerStyle(vtkPlotPoints.CROSS)
    plot.GetXAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.GetYAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.color = (ur_color1.red, ur_color1.green, ur_color1.blue, 255)

    # Lower right plot, two line charts.
    chart = matrix.GetChart(vtkVector2i(1, 0))
    plot = chart.AddPlot(vtkChart.LINE)
    plot.SetInputData(table, 0, 1)
    plot.GetXAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.GetYAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.color = (lr_color.red, lr_color.green, lr_color.blue, 255)

    plot = chart.AddPlot(vtkChart.LINE)
    plot.SetInputData(table, 0, 2)
    plot.GetXAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.GetYAxis().grid_pen.color_f = colors.GetColor3d('warm_grey')
    plot.color = (lr_color1.red, lr_color1.green, lr_color1.blue, 255)

    # Finally render the scene.
    view.GetRenderer().background = colors.GetColor3d('navajo_white')
    view.GetRenderWindow().Render()
    view.GetInteractor().Initialize()
    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
