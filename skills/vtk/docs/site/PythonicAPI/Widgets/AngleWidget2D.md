<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/AngleWidget2D/ -->

# AngleWidget2D

Repository source: [AngleWidget2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/AngleWidget2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestAngleWidget2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestAngleWidget2D.png?raw=true target=)

### Description

The arc is still visible?

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/AngleWidget2D/)), ([Java](https://examples.vtk.org/site/Java/Widgets/AngleWidget2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AngleWidget2D.py**

```python
#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import (
    vtkAngleRepresentation2D,
    vtkAngleWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    ren_win = vtkRenderWindow(window_name='AngleWidget2D')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    pos1 = [50.0, 200.0, 0.0]
    pos2 = [200.0, 20.0, 0.0]
    center = [100.0, 100.0, 0.0]

    rep = vtkAngleRepresentation2D()

    angle_widget = vtkAngleWidget(representation=rep, interactor=iren)
    angle_widget.CreateDefaultRepresentation()

    ren_win.Render()

    angle_widget.On()

    rep.point1_display_position = pos1
    rep.point2_display_position = pos2
    rep.center_display_position = center
    rep.ray1_visibility = True
    rep.ray2_visibility = True
    rep.arc_visibility = True

    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
