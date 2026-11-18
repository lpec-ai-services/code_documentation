<!-- source: https://examples.vtk.org/site/Python/Plotting/SurfacePlot/ -->

# SurfacePlot

Repository source: [SurfacePlot](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Plotting/SurfacePlot.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Plotting/TestSurfacePlot.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Plotting/TestSurfacePlot.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/SurfacePlot/)), ([PythonicAPI](../../PythonicAPI/Plotting/SurfacePlot.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SurfacePlot.py**

```python
#!/usr/bin/env python

from math import sin, sqrt

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import (
    vtkChartXYZ,
    vtkPlotSurface
)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import (
    vtkRectf,
    vtkTable,
    vtkVector2i
)
from vtkmodules.vtkRenderingContext2D import vtkContextMouseEvent
from vtkmodules.vtkViewsContext2D import vtkContextView

def main():
    colors = vtkNamedColors()

    chart = vtkChartXYZ()
    chart.SetGeometry(vtkRectf(150.0, 40.0, 500, 520))

    plot = vtkPlotSurface()

    view = vtkContextView()
    view.GetRenderer().SetBackground(colors.GetColor3d("Silver"))
    view.GetRenderWindow().SetSize(800, 600)
    view.GetScene().AddItem(chart)

    # Create a surface
    table = vtkTable()
    numPoints = 70
    inc = 9.424778 / (numPoints - 1)
    for i in range(numPoints):
        arr = vtkFloatArray()
        table.AddColumn(arr)

    table.SetNumberOfRows(numPoints)
    for i in range(numPoints):
        x = i * inc
        for j in range(numPoints):
            y = j * inc
            table.SetValue(i, j, sin(sqrt(x * x + y * y)))

    # Set up the surface plot we wish to visualize and add it to the chart
    plot.SetXRange(0, 10.0)
    plot.SetYRange(0, 10.0)
    plot.SetInputData(table)
    plot.GetPen().SetColorF(colors.GetColor3d("Tomato"))
    chart.AddPlot(plot)

    view.GetRenderWindow().SetMultiSamples(0)
    view.GetInteractor().Initialize()
    view.GetRenderWindow().SetWindowName("SurfacePlot")
    view.GetRenderWindow().Render()

    # Rotate
    mouseEvent = vtkContextMouseEvent()
    mouseEvent.SetInteractor(view.GetInteractor())

    # This section doesn't work because vtkVector2f is needed.
    pos = vtkVector2i()
    lastPos = vtkVector2i()

    mouseEvent.SetButton(vtkContextMouseEvent.LEFT_BUTTON)
    lastPos.Set(100, 50)
    mouseEvent.SetLastScreenPos(lastPos)
    pos.Set(150, 100)
    mouseEvent.SetScreenPos(pos)

    sP = [float(x) for x in pos]
    lSP = [float(x) for x in lastPos]
    screenPos = [float(x) for x in mouseEvent.GetScreenPos()]
    lastScreenPos = [float(x) for x in mouseEvent.GetLastScreenPos()]

    chart.MouseMoveEvent(mouseEvent)

    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
