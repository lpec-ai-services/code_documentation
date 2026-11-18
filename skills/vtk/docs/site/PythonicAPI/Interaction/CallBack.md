<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/CallBack/ -->

# CallBack

Repository source: [CallBack](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/CallBack.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestCallBack.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestCallBack.png?raw=true target=)

### Description

#### Demonstrate how to set up a callback with client data

Getting the camera orientation after interacting with the image is used as an example.

We define a callback passing the active camera as client data and linking the callback to the **EndInteractionEvent** of the [vtkRenderWindowInteractor](https://www.vtk.org/doc/nightly/html/classvtkRenderWindowInteractor.html) class. This allows us to get the camera orientation after we manipulate the image. We can then copy/paste this data as needed into our camera to set up a nice initial orientation as shown in the example.

To help orient the cone, we use a [vtkOrientationMarkerWidget](https://www.vtk.org/doc/nightly/html/classvtkOrientationMarkerWidget.html) and a [vtkOutlineFilter](https://www.vtk.org/doc/nightly/html/classvtkOutlineFilter.html).

##### C++

There are two methodologies in C++.

1. Create a class that inherits from [vtkCallbackCommand](https://www.vtk.org/doc/nightly/html/classvtkCallbackCommand.html) reimplementing `Execute(` [vtkObject](https://www.vtk.org/doc/nightly/html/classvtkObject.html) `*caller, unsigned long evId, void*)` and setting pointers to a client and/or call data as needed. When the class is implemented, it becomes the callback function.
2. Create a function with this signature: `void f(` [vtkObject](https://www.vtk.org/doc/nightly/html/classvtkObject.html) `* caller, long unsigned int evId, void* clientData, void* callData)` and, where needed, create a [vtkCallbackCommand](https://www.vtk.org/doc/nightly/html/classvtkCallbackCommand.html) setting its callback to the function we have created.

The example demonstrates both approaches.

In the function **PrintCameraOrientation** note how we convert an array to a vector and get a comma-separated list.

##### Python

In Python the approach is even simpler.

We define a function to use as the callback with this signature: `def my_callback(obj, ev):`. Then, to pass client data to it, we simply do: `my_callback.my_client_data = my_client_data`. This relies on the fact that Python functions are in fact objects and we are simply adding new attributes such as `my_client_data` in this case.

An alternative method is to define a class passing the needed variables in the `__init__` function and then implement a `__call__` function that does the work.

Both approaches are demonstrated in the example.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/CallBack/)), ([Python](../../Python/Interaction/CallBack.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CallBack.py**

```python
#!/usr/bin/env python3

"""
Demonstrate the use of a callback.

We also add call data.
"""

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import vtkOrientationMarkerWidget
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Demonstrate two ways of using callbacks.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c', '--class_cb', action='store_false',
                        help='Use a class callback instead of a function  callback.')
    args = parser.parse_args()
    return args.class_cb

def main():
    #  Decide what approach to use.
    use_function_callback = get_program_parameters()

    colors = vtkNamedColors()

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('MistyRose'))
    ren_win = vtkRenderWindow(size=(640, 640), window_name='CallBack')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    # Use a cone as a source with the golden ratio (φ) for the height. Because we can!
    # If the short side is one then φ = 2 × sin(54°) or φ = 1/2 + √5 / 2
    source = vtkConeSource(center=(0, 0, 0), radius=1, height=1.6180339887498948482, resolution=128)

    # Pipeline
    mapper = vtkPolyDataMapper()
    source >> mapper
    # Color and surface properties.
    actor_property = vtkProperty(color=colors.GetColor3d('Peacock'),
                                 ambient=0.6, diffuse=0.2,
                                 specular=1.0, specular_power=20.0)
    actor = vtkActor(mapper=mapper, property=actor_property)

    # Get an outline of the data set for context.
    outline_property = vtkProperty(color=colors.GetColor3d('Black'), line_width=2)
    outline = vtkOutlineFilter()
    outline_mapper = vtkPolyDataMapper()
    source >> outline >> outline_mapper
    outline_actor = vtkActor(mapper=outline_mapper, property=outline_property)

    # Add the actors to the renderer.
    ren.AddActor(actor)
    ren.AddActor(outline_actor)

    # Set up a nice camera position.
    camera = vtkCamera(position=(4.6, -2.0, 3.8), focal_point=(0.0, 0.0, 0.0),
                       clipping_range=(3.2, 10.2), view_up=(0.3, 1.0, 0.13))
    ren.active_camera = camera

    ren_win.Render()

    rgb = tuple(colors.GetColor3d('Carrot'))
    widget = vtkOrientationMarkerWidget(orientation_marker=make_axes_actor(),
                                        interactor=iren, default_renderer=ren,
                                        outline_color=rgb, viewport=(0.0, 0.0, 0.2, 0.2),
                                        zoom=1.5, enabled=True,
                                        interactive=True)

    # Set up the callback.
    if use_function_callback:
        # We are going to output the camera position when the event
        #   is triggered, so we add the active camera as an attribute.
        get_orientation.cam = ren.active_camera
        # Register the callback with the object that is observing.
        iren.AddObserver('EndInteractionEvent', get_orientation)
    else:
        iren.AddObserver('EndInteractionEvent', OrientationObserver(ren.active_camera))
        # Or:
        # observer = OrientationObserver(ren.active_camera)
        # iren.AddObserver('EndInteractionEvent', observer)

    iren.Initialize()
    iren.Start()

def get_orientation(caller, ev):
    """
    Print out the orientation.

    We must do this before we register the callback in the calling function.
    Add the active camera as an attribute.
        get_orientation.cam = ren.active_camera

    :param caller: The caller.
    :param ev: The event.
    :return:
    """
    # Just do this to demonstrate who called callback and the event that triggered it.
    print(f'Caller: {caller.class_name}, Event Id: {ev}')
    # Verify that we have a camera in this case.
    print(f'Camera: {get_orientation.cam.class_name}')
    # Now print the camera orientation.
    camera_orientation(get_orientation.cam)

class OrientationObserver:
    def __init__(self, cam):
        self.cam = cam

    def __call__(self, caller, ev):
        # Just do this to demonstrate who called callback and the event that triggered it.
        print(f'Caller: {caller.class_name}, Event Id: {ev}')
        # Verify that we have a camera in this case.
        print(f'Camera: {self.cam.class_name}')
        # Now print the camera orientation.
        camera_orientation(self.cam)

def camera_orientation(cam):
    flt_fmt = '0.6g'
    # print(caller.class_name, "modified")
    # Print the interesting stuff.
    res = list()
    print(f'Camera orientation:')
    res.append(f'{"position":<14s} = ({fmt_floats(cam.position)})')
    res.append(f'{"focal_point":<14s} = ({fmt_floats(cam.focal_point)})')
    res.append(f'{"view_up":<14s} = ({fmt_floats(cam.view_up)})')
    res.append(f'{"distance":<14s} = {cam.distance:{flt_fmt}}')
    res.append(f'{"clipping_range":<14s} = ({fmt_floats(cam.clipping_range)})')
    indent = ' '
    lf_indent = f'\n{indent}'
    s = f'{indent}' + '|'.join(res) + '\n'
    print(s.replace('|', lf_indent))

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

def make_axes_actor():
    axes = vtkAxesActor(shaft_type=vtkAxesActor.CYLINDER_SHAFT, tip_type=vtkAxesActor.CONE_TIP,
                        x_axis_label_text='X', y_axis_label_text='Y', z_axis_label_text='Z',
                        total_length=(1.0, 1.0, 1.0))
    axes.cylinder_radius = 1.25 * axes.cylinder_radius
    axes.cone_radius = 1.25 * axes.cone_radius
    axes.sphere_radius = 1.5 * axes.sphere_radius

    colors = vtkNamedColors()
    axes.x_axis_caption_actor2d.caption_text_property.color = colors.GetColor3d('FireBrick')
    axes.y_axis_caption_actor2d.caption_text_property.color = colors.GetColor3d('DarkGreen')
    axes.z_axis_caption_actor2d.caption_text_property.color = colors.GetColor3d('DarkBlue')

    return axes

if __name__ == '__main__':
    main()
```
