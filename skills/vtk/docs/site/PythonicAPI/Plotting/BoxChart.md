<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/BoxChart/ -->

# BoxChart

Repository source: [BoxChart](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/BoxChart.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestBoxChart.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestBoxChart.png?raw=true target=)

### Description

This example demonstrates how to generate a [box plot](https://en.wikipedia.org/wiki/Box_plot).

The example uses data from [the Michelson Morley experiment](https://en.wikipedia.org/wiki/Michelson%E2%80%93Morley_experiment). Compare the wiki example output with the [Wikipedia results](https://upload.wikimedia.org/wikipedia/commons/f/fa/Michelsonmorley-boxplot.svg)

Warning

The ChartBox expects an input table with exactly 5 rows per column. The 5 rows are minimum, 1st quartile, median, 3rd quartile and maximum. [vtkComputeQuartiles](https://www.vtk.org/doc/nightly/html/classvtkComputeQuartiles.html) is used to create a valid input table from the original data.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/BoxChart/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BoxChart.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import (
    vtkChartBox
)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkIntArray,
    vtkLookupTable,
    vtkStringArray
)
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkFiltersStatistics import (
    vtkComputeQuartiles,
    vtkStatisticsAlgorithm
)
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    # Set up a 2D scene, add an XY chart to it.
    view = vtkContextView()
    view.GetRenderWindow().size = (400, 400)
    view.GetRenderWindow().multi_samples = 0

    chart = vtkChartBox()
    view.scene.AddItem(chart)

    # Creates a vtkPlotBox input table.
    num_param = 5
    input_box_plot_table = vtkTable()

    for i in range(0, num_param):
        run = f'Run {i:d}'
        arr_index = vtkIntArray(name=run)
        input_box_plot_table.AddColumn(arr_index)

    input_box_plot_table.SetNumberOfRows(20)
    values = [
        [850, 960, 880, 890, 890], [740, 940, 880, 810, 840],
        [900, 960, 880, 810, 780], [1070, 940, 860, 820, 810],
        [930, 880, 720, 800, 760], [850, 800, 720, 770, 810],
        [950, 850, 620, 760, 790], [980, 880, 860, 740, 810],
        [980, 900, 970, 750, 820], [880, 840, 950, 760, 850],
        [1000, 830, 880, 910, 870], [980, 790, 910, 920, 870],
        [930, 810, 850, 890, 810], [650, 880, 870, 860, 740],
        [760, 880, 840, 880, 810], [810, 830, 840, 720, 940],
        [1000, 800, 850, 840, 950], [1000, 790, 840, 850, 800],
        [960, 760, 840, 850, 810], [960, 800, 840, 780, 870]]

    for j in range(0, len(values)):

        for i in range(0, 5):
            input_box_plot_table.SetValue(j, i, values[j][i])

    quartiles = vtkComputeQuartiles()
    quartiles.SetInputData(vtkStatisticsAlgorithm.INPUT_DATA, input_box_plot_table)
    quartiles.Update()

    out_table = quartiles.GetOutput()
    lookup = vtkLookupTable(number_of_colors=num_param, range=(0, num_param - 1))
    lookup.Build()

    chart.GetPlot(0).SetInputData(out_table)
    chart.show_legend = True
    chart.column_visibility_all = True
    chart.title = 'Michelson-Morley experiment'
    chart.GetTitleProperties().SetFontSize(16)
    chart.GetYAxis().title = 'Speed of Light (km/s - 299000)'

    # Set the labels.
    labels = vtkStringArray()
    labels.SetNumberOfValues(num_param)
    for i in range(0, num_param):
        run = f'Run {i:d}'
        labels.SetValue(i, run)
    chart.GetPlot(0).SetLabels(labels)

    # Render the scene.
    view.GetRenderWindow().SetMultiSamples(0)
    view.GetRenderer().background = colors.GetColor3d('LightGrey')
    view.GetInteractor().Initialize()
    view.Render()
    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
