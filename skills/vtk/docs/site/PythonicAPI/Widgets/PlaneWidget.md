<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/PlaneWidget/ -->

# PlaneWidget

Repository source: [PlaneWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/PlaneWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestPlaneWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestPlaneWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/PlaneWidget/)), ([Java](https://examples.vtk.org/site/Java/Widgets/PlaneWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PlaneWidget.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingUI
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import (
    vtkPlaneWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='PlaneWidget')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    plane_widget = vtkPlaneWidget()
    plane_widget.interactor = render_window_interactor

    plane_widget.On()

    render_window_interactor.Initialize()

    renderer.active_camera.Roll(30)
    renderer.active_camera.Pitch(45)
    renderer.ResetCameraClippingRange()

    renderer.ResetCamera()
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
