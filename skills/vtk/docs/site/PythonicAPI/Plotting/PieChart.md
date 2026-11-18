<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/PieChart/ -->

# PieChart

Repository source: [PieChart](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/PieChart.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestPieChart.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestPieChart.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/PieChart/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PieChart.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import vtkChartPie
from vtkmodules.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtkmodules.vtkCommonCore import (
    vtkIntArray,
    vtkStringArray
)
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    # Set up a 2D scene, add an XY chart to it.
    view = vtkContextView()
    view.GetRenderer().background = colors.GetColor3d('SlateGray')
    view.GetRenderWindow().size = (600, 350)
    view.GetRenderWindow().window_name = 'PieChart'

    chart = vtkChartPie()
    view.GetScene().AddItem(chart)

    # Create a table with some points in it...
    table = vtkTable()

    arr_data = vtkIntArray()
    label_array = vtkStringArray()

    db = get_data()
    arr_data.SetName('2008 Circulation')
    for k, v in db.items():
        arr_data.InsertNextValue(v)
        label_array.InsertNextValue(k)

    table.AddColumn(arr_data)

    # Create a color series to use with our stacks.
    color_series = vtkColorSeries()
    color_series.SetColorScheme(vtkColorSeries.WARM)

    # Add multiple pie plots, setting the colors etc.
    pie = chart.AddPlot(0)
    pie.color_series = color_series
    pie.input_data = table
    pie.SetInputArray(0, '2008 Circulation')
    pie.labels = label_array

    chart.show_legend = True

    chart.title = 'Circulation 2008'

    # Finally render the scene.
    view.GetRenderWindow().multi_samples = 0
    view.GetRenderWindow().Render()
    view.GetInteractor().Initialize()
    view.GetInteractor().Start()

def get_data():
    data = [77938, 9109, 2070, 12806, 19514]
    labels = ['Books', 'New and Popular', 'Periodical', 'Audiobook', 'Video']
    return dict(zip(labels, data))

if __name__ == '__main__':
    main()
```
