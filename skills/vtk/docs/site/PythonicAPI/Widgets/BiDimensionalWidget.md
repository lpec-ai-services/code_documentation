<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/BiDimensionalWidget/ -->

# BiDimensionalWidget

Repository source: [BiDimensionalWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/BiDimensionalWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestBiDimensionalWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestBiDimensionalWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/BiDimensionalWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BiDimensionalWidget.py**

```python
#!/usr/bin/env python3

import copy

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionWidgets import vtkBiDimensionalWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()
    sphere_source.Update()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('DarkOliveGreen')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SteelBlue'))
    render_window = vtkRenderWindow(window_name='BiDimensionalWidget')
    render_window.AddRenderer(renderer)

    renderer.AddActor(actor)
    renderer.background = colors.GetColor3d('SteelBlue')

    # An interactor
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    bi_dimensional_widget = vtkBiDimensionalWidget()
    bi_dimensional_widget.interactor = render_window_interactor
    bi_dimensional_widget.CreateDefaultRepresentation()

    bi_dimensional_widget.AddObserver('EndInteractionEvent', bi_dimensional_widget_cb)

    # Render an image (lights and cameras are created automatically).
    render_window.Render()

    render_window_interactor.Initialize()
    render_window.Render()
    bi_dimensional_widget.On()

    # Begin mouse interaction.
    render_window_interactor.Start()

def bi_dimensional_widget_cb(caller, event):
    """
    Callback to display the four points and lengths, just so we know it's working.
    """
    representation = caller.representation

    pts = list()
    p1 = [0.0] * 3
    representation.GetPoint1DisplayPosition(p1)
    pts.append(p1)
    p2 = [0.0] * 3
    representation.GetPoint2DisplayPosition(p2)
    pts.append(p2)
    p3 = [0.0] * 3
    representation.GetPoint3DisplayPosition(p3)
    pts.append(p3)
    p4 = [0.0] * 3
    representation.GetPoint4DisplayPosition(p4)
    pts.append(p4)

    pts_disp = copy.deepcopy(pts)
    pts.clear()

    representation.GetPoint1WorldPosition(p1)
    pts.append(p1)
    representation.GetPoint2WorldPosition(p2)
    pts.append(p2)
    representation.GetPoint3WorldPosition(p3)
    pts.append(p3)
    representation.GetPoint4WorldPosition(p4)
    pts.append(p4)

    pts_world = copy.deepcopy(pts)
    pts.clear()

    res = list()
    for i in range(0, 4):
        res.append(f'{i}: ({fmt_floats(pts_disp[i])})')
    print('Display position:', ' '.join(res))
    res.clear()
    for i in range(0, 4):
        res.append(f'{i}: ({fmt_floats(pts_world[i], 6, 3, "f")})')
    print('World position  :', ' '.join(res))

    l1 = representation.length1
    l2 = representation.length2
    print(f'Length1: {l1:6.3f}, Length2: {l2:6.3f}')

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
