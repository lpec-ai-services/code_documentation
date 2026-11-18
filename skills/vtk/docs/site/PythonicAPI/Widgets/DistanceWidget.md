<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/DistanceWidget/ -->

# DistanceWidget

Repository source: [DistanceWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/DistanceWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestDistanceWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestDistanceWidget.png?raw=true target=)

### Description

- Contributed by Arnaud Gelas

Click two points to see the distance between them.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/DistanceWidget/)), ([Java](https://examples.vtk.org/site/Java/Widgets/DistanceWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DistanceWidget.py**

```python
#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import vtkDistanceWidget
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('Navy'))
    render_window = vtkRenderWindow(window_name='DistanceWidget')
    render_window.AddRenderer(renderer)
    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    distance_widget = vtkDistanceWidget(interactor=render_window_interactor)
    distance_widget.CreateDefaultRepresentation()
    distance_widget.representation.label_format = '%-#6.3g mm'

    # Render an image (lights and cameras are created automatically).
    render_window.Render()

    render_window_interactor.Initialize()
    render_window.Render()
    distance_widget.On()

    # Begin mouse interaction.
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
