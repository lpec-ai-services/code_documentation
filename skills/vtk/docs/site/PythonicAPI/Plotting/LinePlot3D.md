<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/LinePlot3D/ -->

# LinePlot3D

Repository source: [LinePlot3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/LinePlot3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestLinePlot3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestLinePlot3D.png?raw=true target=)

### Description

This example illustrates plotting 3D points using [vtkPlotLine3D](https://www.vtk.org/doc/nightly/html/classvtkPlotLine3D.html). It plots the solution to the [Lorenz Attractor](https://en.wikipedia.org/wiki/Lorenz_system).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/LinePlot3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LinePlot3D.py**

```python
# !/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
# import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import (
    vtkChartXYZ,
    vtkPlotLine3D
)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import (
    vtkRectf,
    vtkTable
)
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    # Create the data.
    var_x_solution = vtkTable()

    arr_x0 = vtkFloatArray(name='X')
    var_x_solution.AddColumn(arr_x0)

    arr_x1 = vtkFloatArray(name='Y')
    var_x_solution.AddColumn(arr_x1)

    arr_x2 = vtkFloatArray(name='Z')
    var_x_solution.AddColumn(arr_x2)

    number_of_time_points = 1000
    var_x_solution.SetNumberOfRows(number_of_time_points)

    var_x = [0.0, 1.0, 1.05]

    delta_t = 0.01
    for ii in range(0, number_of_time_points):
        var_x_solution.SetValue(ii, 0, var_x[0])
        var_x_solution.SetValue(ii, 1, var_x[1])
        var_x_solution.SetValue(ii, 2, var_x[2])
        var_x_derivative = lorenz(var_x)
        var_x[0] += var_x_derivative[0] * delta_t
        var_x[1] += var_x_derivative[1] * delta_t
        var_x[2] += var_x_derivative[2] * delta_t

    # Set up a 3D scene and add an XYZ chart to it.
    view = vtkContextView()
    view.render_window.size = (640, 480)
    view.render_window.window_name = 'PlotLine3D'

    chart = vtkChartXYZ(geometry=vtkRectf(5.0, 5.0, 635.0, 475.0))
    view.scene.AddItem(chart)

    # Add a line plot.
    plot = vtkPlotLine3D(input_data=var_x_solution)
    plot.pen.color_f = colors.GetColor3d('LightCoral')
    view.render_window.multi_samples = 0
    plot.pen.width = 2.0
    chart.AddPlot(plot)

    # Finally render the scene.
    view.renderer.background = colors.GetColor3d('DarkOliveGreen')
    view.render_window.Render()
    view.renderer.Render()
    view.interactor.Initialize()
    view.GetInteractor().Start()

def lorenz(var_x):
    """
    Plot the solution to the Lorenz attractor.
    [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system)
    """

    sigma = 10.0
    rho = 28.0
    beta = 2.66666666666

    var_x_derivative = list()

    var_x_derivative.append(sigma * (var_x[1] - var_x[0]))
    var_x_derivative.append(var_x[0] * (rho - var_x[2]) - var_x[1])
    var_x_derivative.append(var_x[0] * var_x[1] - beta * var_x[2])

    return var_x_derivative

if __name__ == '__main__':
    main()
```
