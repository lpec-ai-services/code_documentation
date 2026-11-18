<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/SplineWidget/ -->

# SplineWidget

Repository source: [SplineWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/SplineWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestSplineWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestSplineWidget.png?raw=true target=)

### Description

This example shows how to use [vtkSplineWidget](https://www.vtk.org/doc/nightly/html/classvtkSplineWidget.html) with a callback being used to get the length of the spline widget.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/SplineWidget/)), ([Python](../../Python/Widgets/SplineWidget.md)), ([Java](https://examples.vtk.org/site/Java/Widgets/SplineWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SplineWidget.py**

```python
#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkCommand
)
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkSplineWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main(argv):
    colors = vtkNamedColors()
    colors.SetColor('ParaViewBkg', 82, 87, 110, 255)

    window_width = 1024
    window_height = 1024

    ren_win = vtkRenderWindow(size=(window_width, window_height), window_name='SplineWidget')
    ren_win.SetSize(window_width, window_height)
    # Important: The interactor must be set prior to enabling the widgets.
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    renderer = vtkRenderer(background=colors.GetColor3d('ParaViewBkg'))

    # Create a cylinder.
    cylinder = vtkCylinderSource(center=(0.0, 0.0, 0.0), radius=3.0, height=5.0, resolution=100)

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    cylinder >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('Cornsilk')
    # Add the actor to the scene
    renderer.AddActor(actor)

    ren_win.AddRenderer(renderer)

    # A spline widget
    spline_widget = vtkSplineWidget(interactor=iren)
    spline_widget.SetProp3D(actor)
    spline_widget.PlaceWidget(-2.5, 2.5, 3.5, 3.5, 0, 0, )
    spline_widget.On()

    spline_widget.AddObserver(vtkCommand.EndInteractionEvent, SplineCallback(spline_widget))

    cow = vtkCameraOrientationWidget(parent_renderer=renderer)
    cow.On()

    ren_win.Render()
    iren.Start()

class SplineCallback:
    def __init__(self, spline_widget):
        self.spline = spline_widget

    def __call__(self, caller, ev):
        spline_widget = caller
        length = spline_widget.summed_length
        print(f'Length: {length:6.2f}')

if __name__ == '__main__':
    import sys

    main(sys.argv)
```
