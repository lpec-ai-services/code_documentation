<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/LayeredActors/ -->

# LayeredActors

Repository source: [LayeredActors](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/LayeredActors.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestLayeredActors.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestLayeredActors.png?raw=true target=)

### Description

Demonstrates the use of two renderers in a render window. Notice that the second (and subsequent) renderers will have a transparent background.

The first layer (layer 0) contains the base object, a slab in this case. The second layer (layer 1) contains an object (axes in this case). This axes object will always be in front of the base layer object. When the program runs, the top-most layer will be the active layer, layer 1 in this case.

Two callbacks are provided, the first callback selects which layer is active:

- Pressing **0** on the keyboard will let you manipulate the objects in layer 0.
- Pressing **1** on the keyboard will let you manipulate the objects in layer 1.

The second callback allows you to orient objects in all layers using the object in the active layer.

Note

Objects in the top-most layer will always be in front of any objects in other layers.

Info

This is an extension of the [TransparentBackground.py](TransparentBackground.md) example, extended by adding an extra callback so that the non-active layer objects move in conjunction with the active layer objects.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/LayeredActors/)), ([Python](../../Python/Rendering/LayeredActors.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LayeredActors.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersSources import vtkCubeSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def generate_and_display_cube_and_axes():
    colors = vtkNamedColors()

    # Make the slab and axes actors.
    cube_source = vtkCubeSource(x_length=4.0, y_length=9.0, z_length=1.0, center=(0.0, 0.0, 0.0))

    cube_mapper = vtkPolyDataMapper()
    cube_source >> cube_mapper

    back_face_property = vtkProperty(color=colors.GetColor3d('Sienna'))
    actor_property = vtkProperty(diffuse_color=colors.GetColor3d('BurlyWood'),
                                 edge_color=colors.GetColor3d('PapayaWhip'),
                                 edge_visibility=True, line_width=2)

    cube_actor = vtkActor(mapper=cube_mapper)
    cube_actor.property = actor_property
    cube_actor.property.edge_visibility = True
    cube_actor.property.line_width = 2
    cube_actor.backface_property = back_face_property

    transform = vtkTransform()
    transform.Translate(0.0, 0.0, 0.0)

    # The axes can be positioned with a user transform.
    axes = vtkAxesActor(user_transform=transform)

    # The renderers, render window and interactor.
    ren_win = vtkRenderWindow(size=(800, 800), window_name='LayeredActors')

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    # Define the renderers and allocate them to layers.
    renderers = list()
    for layer in range(0, 2):
        if layer == 0:
            # Layer 0 - background not transparent.
            renderers.append(vtkRenderer(background=colors.GetColor3d('DarkSlateGray'), layer=layer))
            renderers[layer].AddActor(cube_actor)
        if layer == 1:
            # Layer 1 - the background is transparent
            #           so we only see the layer 0 background color.
            renderers.append(vtkRenderer(background=colors.GetColor3d('MidnightBlue'), layer=layer))
            renderers[layer].AddActor(axes)
        ren_win.AddRenderer(renderers[layer])
        renderers[layer].SetLayer(layer)

    # Set a common camera view for each layer.
    for renderer in renderers:
        camera = renderer.active_camera
        camera.Elevation(-30)
        camera.Azimuth(-30)
        renderer.ResetCamera()

    #  We have two layers.
    ren_win.SetNumberOfLayers(len(renderers))

    ren_win.Render()

    iren.AddObserver('KeyPressEvent', select_layer)
    iren.AddObserver('EndInteractionEvent', orient_layer)

    iren.Start()

def select_layer(caller, ev):
    """
    Select the layer to manipulate.
    :param caller:
    :param ev:
    :return:
    """
    iren = caller
    renderers = iren.render_window.renderers
    if renderers.number_of_items < 2:
        print(f'We need at least two renderers, we have only {renderers.number_of_items}.')
        return
    renderers.InitTraversal()
    # Top item.
    ren0 = renderers.GetNextItem()
    # Bottom item.
    ren1 = renderers.GetNextItem()

    key = iren.key_sym
    # Numeric key codes are also allowed, namely KP_0 and KP_1.
    if key in ['0', 'KP_0']:
        print('Pressed:', key)
        iren.render_window.interactor.interactor_style.default_renderer = ren0
        ren0.interactive = True
        ren1.interactive = False
    if key in ['1', 'KP_1']:
        print('Pressed:', key)
        iren.render_window.interactor.interactor_style.default_renderer = ren1
        ren0.interactive = False
        ren1.interactive = True

def orient_layer(caller, ev):
    """
    Orient layer 0 based on the camera orientation in layer 1 or vice versa.

    :param caller:
    :param ev:
    :return:
    """

    iren = caller
    renderers = iren.render_window.renderers
    if renderers.number_of_items < 2:
        print(f'We need at least two renderers, we have only {renderers.number_of_items}.')
        return
    renderers.InitTraversal()
    # Top item.
    ren0 = renderers.GetNextItem()
    # Bottom item.
    ren1 = renderers.GetNextItem()

    if ren1.GetInteractive():
        orient1 = get_orientation(ren1)
        set_orientation(ren0, orient1)
        ren0.ResetCamera()

    else:
        orient0 = get_orientation(ren0)
        set_orientation(ren1, orient0)
        ren1.ResetCamera()

def get_orientation(ren):
    """
    Get the camera orientation.
    :param ren: The renderer.
    :return: The orientation parameters.
    """
    camera = ren.active_camera
    return {
        'position': camera.position,
        'focal point': camera.focal_point,
        'view up': camera.view_up,
        'distance': camera.distance,
        'clipping range': camera.clipping_range,
        'orientation': camera.orientation,
    }

def set_orientation(ren, p):
    """
    Set the orientation of the camera.
    :param ren: The renderer.
    :param p: The orientation parameters.
    :return:
    """
    camera = ren.active_camera
    camera.position = p['position']
    camera.focal_point = p['focal point']
    camera.view_up = p['view up']
    camera.distance = p['distance']
    camera.clipping_range = p['clipping range']

def main():
    generate_and_display_cube_and_axes()

if __name__ == '__main__':
    main()
```
