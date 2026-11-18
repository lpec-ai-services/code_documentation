<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/AngleWidget/ -->

# AngleWidget

Repository source: [AngleWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/AngleWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestAngleWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestAngleWidget.png?raw=true target=)

### Description

Click three points to create an angle. You can then drag the points around.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/AngleWidget/)), ([Java](https://examples.vtk.org/site/Java/Widgets/AngleWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AngleWidget.py**

```python
#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import (
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
    ren_win = vtkRenderWindow(window_name='AngleWidget')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    angle_widget = vtkAngleWidget(interactor=iren)
    angle_widget.CreateDefaultRepresentation()

    # Render
    ren_win.Render()
    iren.Initialize()
    ren_win.Render()
    angle_widget.On()
    iren.Start()

if __name__ == '__main__':
    main()
```
