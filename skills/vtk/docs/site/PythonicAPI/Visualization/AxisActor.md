<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/AxisActor/ -->

# AxisActor

Repository source: [AxisActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/AxisActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestAxisActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestAxisActor.png?raw=true target=)

### Description

This example illustrates the use of [vtkAxisActor](https://www.vtk.org/doc/nightly/html/classvtkAxisActor.html). This is a fairly complicated object that allows extensive control over a single axis. The parameters may be tricky to set up. [vtkAxisActor](https://www.vtk.org/doc/nightly/html/classvtkAxisActor.html) is usually used inside other classes,e.g. vtkCubeAxisActor.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/AxisActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AxisActor.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkStringArray
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingAnnotation import vtkAxisActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    source = vtkSphereSource(phi_resolution=31, theta_resolution=31)

    def fmt_floats(v, w=0, d=6, pt='f'):
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

    bounds = source.update().output.bounds
    print(f'bounds: ({fmt_floats(bounds)})')
    center = source.output.center
    print(f'center: ({fmt_floats(center)})')

    # Create the axis actor.
    labels = vtkStringArray(number_of_tuples=1)
    labels.SetValue(0, 'x Axis')
    axis = vtkAxisActor(tick_location=vtkAxisActor.VTK_TICKS_BOTH, axis_type=vtkAxisActor.VTK_AXIS_TYPE_X,
                        title='A Sphere', title_scale=0.2, title_visibility=True,
                        major_tick_size=0.05, minor_tick_size=1.0, draw_gridlines=False,
                        labels=labels, label_scale=0.1, minor_ticks_visible=True,
                        calculate_title_offset=0, calculate_label_offset=0
                        )
    axis.SetPoint1(-1.1, 0.0, 0.0)
    axis.SetPoint2(1.1, 0.0, 0.0)
    axis.SetDeltaMajor(0, 0.1)
    axis.title_text_property.color = colors.GetColor3d('Banana')
    axis.label_text_property.color = colors.GetColor3d('Orange')

    mapper = vtkPolyDataMapper()
    source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.diffuse_color = colors.GetColor3d('Tomato')

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='AxisActor')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    axis.camera = renderer.active_camera

    renderer.AddActor(actor)
    renderer.AddActor(axis)

    renderer.ResetCamera()
    renderer.ResetCameraClippingRange()

    # Render the image.
    render_window.Render()

    interactor.Initialize()
    interactor.Start()

if __name__ == '__main__':
    main()
```
