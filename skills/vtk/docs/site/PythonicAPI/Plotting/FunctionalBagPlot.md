<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/FunctionalBagPlot/ -->

# FunctionalBagPlot

Repository source: [FunctionalBagPlot](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/FunctionalBagPlot.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestFunctionalBagPlot.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestFunctionalBagPlot.png?raw=true target=)

### Description

This example illustrates how to use the [vtkPlotFunctionalBag](https://www.vtk.org/doc/nightly/html/classvtkPlotFunctionalBag.html). This class, depending on the number of components in a column, will either draw a line plot (1 component) or, for two component columns, a filled polygonal band (the bag) going from the first to second component.

The example uses a qualitative color map selected from [vtkColorSeries](https://www.vtk.org/doc/nightly/html/classvtkColorSeries.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/FunctionalBagPlot/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FunctionalBagPlot.py**

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
    vtkChartXY, vtkChartLegend, vtkPlotFunctionalBag
)
from vtkmodules.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtkmodules.vtkCommonCore import (
    vtkDoubleArray,
    vtkLookupTable,
    vtkMath
)
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    # Create an input table.
    num_cols = 7
    num_vals = 100

    input_table = vtkTable()

    arr = list()
    for i in range(0, num_cols):
        a = vtkDoubleArray()
        a.name = f'Y{i:d}'
        a.SetNumberOfValues(num_vals)
        for j in range(0, num_vals):
            a.SetValue(j, (i + 1) * abs(math.sin((j * 2.0 * vtkMath.Pi()) / float(num_vals))) * j + i * 20)
        arr.append(a)
        input_table.AddColumn(arr[i])

    # Create an X-axis column.
    x_arr = vtkDoubleArray(name='X')
    x_arr.SetNumberOfValues(num_vals)
    for j in range(0, num_vals):
        x_arr.SetValue(j, j * 2.0)
    input_table.AddColumn(x_arr)

    # Create the bag columns
    q3_arr = vtkDoubleArray(name='Q3', number_of_components=2, number_of_tuples=num_vals)
    q2_arr = vtkDoubleArray(name='Q2', number_of_components=2, number_of_tuples=num_vals)

    for i in range(0, num_vals):
        v0 = arr[1].GetVariantValue(i).ToFloat()
        v1 = arr[5].GetVariantValue(i).ToFloat()
        q3_arr.SetTuple2(i, v0, v1)

        v0 = arr[2].GetVariantValue(i).ToFloat()
        v1 = arr[4].GetVariantValue(i).ToFloat()
        q2_arr.SetTuple2(i, v0, v1)
    input_table.AddColumn(q3_arr)
    input_table.AddColumn(q2_arr)

    # Set up a 2D scene and add an XY chart to it.
    view = vtkContextView()
    view.GetRenderWindow().size = (640, 480)
    view.GetRenderWindow().multi_samples = 0
    view.GetRenderWindow().window_name = 'FunctionalBagPlot'

    chart = vtkChartXY(show_legend=True)
    chart.GetLegend().horizontal_alignment = vtkChartLegend.LEFT
    chart.GetLegend().vertical_alignment = vtkChartLegend.TOP

    view.scene.AddItem(chart)

    # Create the functional bag plots
    color3d = colors.GetColor3d('Tomato')
    q3_plot = vtkPlotFunctionalBag()
    q3_plot.color_f = (color3d.red, color3d.green, color3d.blue, 1.0)
    q3_plot.SetInputData(input_table, 'X', 'Q3')
    chart.AddPlot(q3_plot)

    color3d = colors.GetColor3d('Banana')
    q2_plot = vtkPlotFunctionalBag()
    q2_plot.color_f = (color3d.red, color3d.green, color3d.blue, 1.0)
    q2_plot.SetInputData(input_table, 'X', 'Q2')
    chart.AddPlot(q2_plot)

    color_series = vtkColorSeries()
    color_series.SetColorScheme(vtkColorSeries.BREWER_QUALITATIVE_SET3)

    lookup = vtkLookupTable(number_of_colors=num_cols, range=(0, num_cols - 1))
    for j in range(0, num_cols):
        plot = vtkPlotFunctionalBag()
        color = color_series.GetColorRepeating(j)
        lookup.SetTableValue(j, color.red / 255.0, color.green / 255.0, color.blue / 255.0, 1.0)
        rgb = [0.0] * 3
        lookup.GetColor(j, rgb)
        plot.color_f = (rgb[0], rgb[1], rgb[2], 1.0)
        plot.SetInputData(input_table, 'X', input_table.GetColumn(j).name)
        plot.GetPen().width = 3.0
        chart.AddPlot(plot)

    view.GetRenderer().background = colors.GetColor3d('SlateGray')

    # Render the scene
    view.GetRenderWindow().Render()
    view.GetInteractor().Initialize()
    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
