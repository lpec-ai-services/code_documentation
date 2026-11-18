<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/StackedBar/ -->

# StackedBar

Repository source: [StackedBar](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/StackedBar.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestStackedBar.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestStackedBar.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/StackedBar/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**StackedBar.py**

```python
#!/usr/bin/env python3

from collections import defaultdict

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import (
    vtkAxis,
    vtkChart,
    vtkChartLegend,
    vtkChartXY
)
from vtkmodules.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtkmodules.vtkCommonCore import (
    VTK_TEXT_CENTERED,
    VTK_TEXT_RIGHT,
    vtkIntArray,
    vtkDoubleArray,
    vtkStringArray
)
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    months = get_months()
    db = get_data()

    # Set up a 2D scene, add an XY chart to it.
    view = vtkContextView()
    view.GetRenderWindow().size = (500, 350)
    chart = vtkChartXY()
    view.scene.AddItem(chart)

    # Create a table with some points in it...
    table = vtkTable()

    arr_month = build_array('Month', list(months.keys()))
    table.AddColumn(arr_month)

    arr_books_2008 = build_array('Books 2008', db['book'][2008])
    table.AddColumn(arr_books_2008)
    arr_new_popular_2008 = build_array('New / Popular 2008', db['new_popular'][2008])
    table.AddColumn(arr_new_popular_2008)
    arr_periodical_2008 = build_array('Periodical 2008', db['periodical'][2008])
    table.AddColumn(arr_periodical_2008)
    arr_audiobook_2008 = build_array('Audiobook 2008', db['audiobook'][2008])
    table.AddColumn(arr_audiobook_2008)
    arr_video_2008 = build_array('Video 2008', db['video'][2008])
    table.AddColumn(arr_video_2008)

    arr_books_2009 = build_array('Books 2009', db['book'][2009])
    table.AddColumn(arr_books_2009)
    arr_new_popular_2009 = build_array('New / Popular 2009', db['new_popular'][2009])
    table.AddColumn(arr_new_popular_2009)
    arr_periodical_2009 = build_array('Periodical 2009', db['periodical'][2009])
    table.AddColumn(arr_periodical_2009)
    arr_audiobook_2009 = build_array('Audiobook 2009', db['audiobook'][2009])
    table.AddColumn(arr_audiobook_2009)
    arr_video_2009 = build_array('Video 2009', db['video'][2009])
    table.AddColumn(arr_video_2009)

    # Create a color series to use with our stacks.
    color_series1 = vtkColorSeries(color_scheme=vtkColorSeries.WILD_FLOWER)

    # Add multiple line plots, setting the colors etc.
    bar = chart.AddPlot(vtkChart.BAR)
    bar.color_series = color_series1
    bar.SetInputData(table, 'Month', 'Books 2008')
    bar.SetInputArray(2, 'New / Popular 2008')
    bar.SetInputArray(3, 'Periodical 2008')
    bar.SetInputArray(4, 'Audiobook 2008')
    bar.SetInputArray(5, 'Video 2008')

    color_series2 = vtkColorSeries(color_scheme=vtkColorSeries.WILD_FLOWER)

    bar = chart.AddPlot(vtkChart.BAR)
    bar.color_series = color_series2
    bar.SetInputData(table, 'Month', 'Books 2009')
    bar.SetInputArray(2, 'New / Popular 2009')
    bar.SetInputArray(3, 'Periodical 2009')
    bar.SetInputArray(4, 'Audiobook 2009')
    bar.SetInputArray(5, 'Video 2009')

    chart.SetShowLegend(True)
    axis = chart.GetAxis(vtkAxis.BOTTOM)
    axis.behavior = 1
    axis.maximum = 13.0
    axis.title = 'Month'
    chart.GetAxis(vtkAxis.LEFT).title = ''
    chart.title = 'Circulation 2008, 2009'

    # Set up the legend to be off to the top right of the viewport.
    chart.legend.inline = False
    chart.legend.horizontal_alignment = vtkChartLegend.RIGHT
    chart.legend.vertical_alignment = vtkChartLegend.TOP

    # Set up some custom labels for months.
    dates = vtkDoubleArray()
    strings = vtkStringArray()
    for k, v in months.items():
        dates.InsertNextValue(k)
        strings.InsertNextValue(v)

    axis.SetCustomTickPositions(dates, strings)
    axis.label_properties.orientation = 90
    axis.label_properties.SetVerticalJustification(VTK_TEXT_CENTERED)
    axis.label_properties.SetJustification(VTK_TEXT_RIGHT)

    # Finally render the scene and compare the image to a reference image.
    view.GetRenderer().background = colors.GetColor3d('Cornsilk')
    view.GetRenderWindow().multi_samples = 0
    view.GetRenderWindow().Render()
    view.GetRenderWindow().size = (600, 400)
    view.GetRenderWindow().window_name = 'StackedBar'
    view.GetInteractor().Initialize()
    view.GetInteractor().Start()

def get_months():
    month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    return dict(zip(month_numbers, month_names))

def get_data():
    db = defaultdict(lambda: defaultdict(list))
    db['book'][2008] = [5675, 5902, 6388, 5990, 5575, 7393,
                        9878, 8082, 6417, 5946, 5526, 5166]
    db['new_popular'][2008] = [701, 687, 736, 696, 750, 814,
                               923, 860, 786, 735, 680, 741]
    db['periodical'][2008] = [184, 176, 166, 131, 171, 191,
                              231, 166, 197, 162, 152, 143]
    db['audiobook'][2008] = [903, 1038, 987, 1073, 1144, 1203,
                             1173, 1196, 1213, 1076, 926, 874]
    db['video'][2008] = [1524, 1565, 1627, 1445, 1179, 1816,
                         2293, 1811, 1588, 1561, 1542, 1563]

    db['book'][2009] = [6388, 5990, 5575, 9878, 8082, 5675,
                        7393, 5902, 5526, 5166, 5946, 6417]
    db['new_popular'][2009] = [696, 735, 786, 814, 736, 860,
                               750, 687, 923, 680, 741, 701]
    db['periodical'][2009] = [197, 166, 176, 231, 171, 152,
                              166, 131, 184, 191, 143, 162]
    db['audiobook'][2009] = [1213, 1076, 926, 987, 903, 1196,
                             1073, 1144, 1203, 1038, 874, 1173]
    db['video'][2009] = [2293, 1561, 1542, 1627, 1588, 1179,
                         1563, 1445, 1811, 1565, 1524, 1816]
    return db

def build_array(name, py_list):
    array = vtkIntArray(name=name)
    for i in range(0, len(py_list)):
        array.InsertNextValue(py_list[i])
    return array

if __name__ == '__main__':
    main()
```
