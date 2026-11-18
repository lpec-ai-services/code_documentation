<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/LineWidget2/ -->

# LineWidget2

Repository source: [LineWidget2](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/LineWidget2.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestLineWidget2.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestLineWidget2.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/LineWidget2/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LineWidget2.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingUI
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionWidgets import (
    vtkLineRepresentation,
    vtkLineWidget2
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # A renderer, render window and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    render_window = vtkRenderWindow(window_name='LineWidget2')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    # The line widget.
    line_widget = vtkLineWidget2(interactor=render_window_interactor)
    line_widget.CreateDefaultRepresentation()

    # You could do this if you want to set properties at this point:
    line_representation = vtkLineRepresentation()
    line_representation.line_property.SetColor(colors.GetColor3d('Yellow'))
    line_representation.end_point_property.SetColor(colors.GetColor3d('Magenta'))
    line_representation.end_point2_property.SetColor(colors.GetColor3d('Magenta'))
    line_widget.SetRepresentation(line_representation)

    line_callback = LineCallback()
    line_widget.AddObserver('InteractionEvent', line_callback)

    # Render
    render_window.Render()
    render_window_interactor.Initialize()
    render_window.Render()
    line_widget.On()

    # Begin the mouse interaction.
    render_window_interactor.Start()

class LineCallback:

    def __call__(self, caller, ev):
        # This is a vtkLineWidget2 line representation.
        rep = caller.representation
        polydata = vtkPolyData()
        rep.GetPolyData(polydata)
        pt = [0] * 3
        # Get the actual box coordinates of the line.
        for i in range(0, 2):
            polydata.GetPoint(i, pt)
            print(f'Point {i}: {fmt_floats(pt)}')
        print(f'Distance: {rep.distance:0.6g}')

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
