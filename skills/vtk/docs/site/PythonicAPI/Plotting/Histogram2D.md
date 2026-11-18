<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/Histogram2D/ -->

# Histogram2D

Repository source: [Histogram2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/Histogram2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestHistogram2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestHistogram2D.png?raw=true target=)

### Description

This examples uses a vtkChartHistogram to draw a 2D histogram represented as an image.

The example shows how to set various properties.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/Histogram2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Histogram2D.py**

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
    vtkChartHistogram2D
)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_DOUBLE,
    vtkMath
)
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkRenderingCore import vtkColorTransferFunction
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    # Define colors.
    colors = vtkNamedColors()
    background_color = colors.GetColor3d('SlateGray')
    title_color = colors.GetColor3d('Orange')
    axis_title_color = colors.GetColor3d('Orange')
    axis_label_color = colors.GetColor3d('Beige')
    legend_background_color = colors.GetColor4ub('Tomato')

    # Set up a 2D scene, add an XY chart to it.
    size = 400
    view = vtkContextView()
    view.GetRenderWindow().size = (512, 512)
    view.GetRenderWindow().window_name = 'Histogram2D'

    view.GetRenderer().background = background_color

    # Define a chart
    chart = vtkChartHistogram2D(title='2D Histogram')
    chart.title_properties.font_size = 36
    chart.title_properties.color = title_color

    # Chart Axes.
    chart.GetAxis(0).title_properties.font_size = 24
    chart.GetAxis(0).title_properties.color = axis_title_color
    chart.GetAxis(0).label_properties.color = axis_label_color
    chart.GetAxis(0).label_properties.font_size = 18

    chart.GetAxis(1).title_properties.font_size = 24
    chart.GetAxis(1).title_properties.color = colors.GetColor3d('orange')
    chart.GetAxis(1).label_properties.color = colors.GetColor3d('beige')
    chart.GetAxis(1).label_properties.font_size = 18

    # Chart Legend.
    chart.GetLegend().draw_border = True
    chart.GetLegend().brush.color = legend_background_color

    # Add the chart to the view.
    view.scene.AddItem(chart)

    data = vtkImageData()
    data.extent = (0, size - 1, 0, size - 1, 0, 0)
    data.AllocateScalars(VTK_DOUBLE, 1)

    data.SetOrigin(100.0, -100.0, 0.0)
    data.SetSpacing(2.0, 1.0, 1.0)

    component = data.number_of_scalar_components - 1
    for i in range(0, size):
        for j in range(0, size):
            data.SetScalarComponentFromDouble(j, i, 0, component,
                                              math.sin(vtkMath.RadiansFromDegrees(float(2 * i))) *
                                              math.cos(vtkMath.RadiansFromDegrees(float(j))))
    chart.SetInputData(data)

    transfer_function = vtkColorTransferFunction()
    transfer_function.AddHSVSegment(0.0, 0.0, 1.0, 1.0, 0.3333, 0.3333, 1.0, 1.0)
    transfer_function.AddHSVSegment(0.3333, 0.3333, 1.0, 1.0, 0.6666, 0.6666, 1.0, 1.0)
    transfer_function.AddHSVSegment(0.6666, 0.6666, 1.0, 1.0, 1.0, 0.2, 1.0, 0.3)
    transfer_function.Build()
    chart.SetTransferFunction(transfer_function)

    view.GetRenderWindow().Render()
    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
