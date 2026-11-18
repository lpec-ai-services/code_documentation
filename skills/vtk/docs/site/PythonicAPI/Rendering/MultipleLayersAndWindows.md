<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/MultipleLayersAndWindows/ -->

# MultipleLayersAndWindows

Repository source: [MultipleLayersAndWindows](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/MultipleLayersAndWindows.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestMultipleLayersAndWindows.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestMultipleLayersAndWindows.png?raw=true target=)

## Description

Demonstrates the use of four renderers in two layers. The left renderers camera is independent of the right renderers camera.

There are four objects in two windows and two layers.

| Layers | Left | Right |
| --- | --- | --- |
| 0 | cube | cone |
| 1 | sphere | cylinder |

When the program first runs, the top-most layer will be the active layer, (layer 1 in this case). Objects in layer 0 will be almost transparent.

- Pressing **0** on the keyboard will let you manipulate the objects in layer 0. Objects in layer 1 will be almost transparent.
- Pressing **1** on the keyboard will let you manipulate the objects in layer 1. Objects in layer 0 will be almost transparent.

Note:

- The layer 0 background is the only visible background; backgrounds in layer 1 and subsequent layers are transparent.
- It is easy to access the renderers and actors from the interactor by iterating through the renderer and actor collections.
- In renderer collections and actor collections it is important to remember that the references are stored in last in - first out order.

Info

Also see the [LayeredActors](LayeredActors.md) and [TransparentBackground](TransparentBackground.md) examples.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/MultipleLayersAndWindows/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MultipleLayersAndWindows.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkCubeSource,
    vtkCylinderSource,
    vtkSphereSource
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()
    colors.SetColor("CubeColor", 250, 128, 114, 255)
    colors.SetColor("BkgColor", 230, 230, 230, 255)

    # Create the rendering window, interactor and renderers.
    ren_win = vtkRenderWindow(size=(1200, 600), position=(0, 50), number_of_layers=2,
                              window_name='MultipleLayersAndWindows')
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style
    # The renderers in each render window.
    left_rends = list()
    right_rends = list()
    # Define the renderers setting viewport, layer and color.
    for i in range(0, 2):
        left_rends.append(vtkRenderer(viewport=(0, 0, 0.5, 1), layer=i, background=colors.GetColor3d('BkgColor')))
        ren_win.AddRenderer(left_rends[i])
        right_rends.append(vtkRenderer(viewport=(0.5, 0, 1, 1), layer=i, background=colors.GetColor3d('Linen')))
        ren_win.AddRenderer(right_rends[i])

    # Create an actor and give it conical geometry.
    cone_source = vtkConeSource(resolution=8)
    cone_mapper = vtkPolyDataMapper()
    cone_source >> cone_mapper
    cone_actor = vtkActor(mapper=cone_mapper)
    cone_actor.property.diffuse_color = colors.GetColor3d('CubeColor')

    # Create an actor and give it cylindrical geometry.
    cylinder_source = vtkCylinderSource(resolution=8, height=0.5, radius=0.25)
    cylinder_mapper = vtkPolyDataMapper()
    cylinder_source >> cylinder_mapper
    cylinder_actor = vtkActor(mapper=cylinder_mapper)
    cylinder_actor.property.diffuse_color = colors.GetColor3d('Peacock')

    # Create an actor and give it cubic geometry.
    cube_source = vtkCubeSource()
    cube_mapper = vtkPolyDataMapper()
    cube_source >> cube_mapper
    cube_actor = vtkActor(mapper=cube_mapper)
    cube_actor.property.diffuse_color = colors.GetColor3d('CubeColor')

    # Create an actor and give it spherical geometry.
    sphere_source = vtkSphereSource(radius=0.25)
    sphere_mapper = vtkPolyDataMapper()
    sphere_source >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.diffuse_color = colors.GetColor3d('Peacock')

    # Assign our actors to the renderers.
    left_rends[0].AddActor(cube_actor)  # Cube -> Left renderer, Layer 0
    left_rends[1].AddActor(sphere_actor)  # Sphere -> Left renderer, Layer 1
    right_rends[0].AddActor(cone_actor)  # Cone -> Right renderer, Layer 0
    right_rends[1].AddActor(cylinder_actor)  # Cylinder -> Right renderer, Layer 1

    # Make the layer 0 actors almost transparent.
    cube_actor.property.opacity = 0.1
    cone_actor.property.opacity = 0.1

    ren_win.Render()

    iren.AddObserver('KeyPressEvent', select_layer)

    # Set the active cameras.
    left_rends[1].active_camera = left_rends[0].active_camera
    right_rends[1].active_camera = right_rends[0].active_camera

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
    number_of_items = renderers.number_of_items
    if number_of_items < 4:
        print(f'We need at least four renderers, we have only {renderers.number_of_items}.')
        return
    rens = list()
    renderers.InitTraversal()
    # Top item is rens[0] and the bottom item is rens[numberOfItems-1].
    for i in range(0, number_of_items):
        rens.append(renderers.next_item)
    # Reverse so that the bottom item is rens[0] and the top item is rens[numberOfItems-1].
    rens.reverse()

    def set_actor_properties(idx, opacity):
        """
        Note: rens is the list of renderers defined in the caller.

        :param idx: Index of the specified renderer.
        :param opacity: Opacity of the first actor in the specified renderer.
        :return:
        """
        # actor = rens[idx].GetActors()
        actor = rens[idx].actors
        actor.InitTraversal()
        actor.next_actor.property.opacity = opacity

    key = iren.key_sym
    # Numeric key codes are also allowed, namely KP_0 and KP_1.
    if key in ['0', 'KP_0']:
        set_actor_properties(0, 0.1)
        set_actor_properties(1, 0.1)
        set_actor_properties(2, 1)
        set_actor_properties(3, 1)

        print('Selected layer 0.')
        rens[0].interactive = False  # Cylinder -> Right renderer, Layer 1
        rens[1].interactive = False  # Sphere -> Left renderer, Layer 1
        rens[2].interactive = True  # Cone -> Right renderer, Layer 0
        rens[3].interactive = True  # Cube -> Left renderer, Layer 0

    if key in ['1', 'KP_1']:
        set_actor_properties(0, 1)
        set_actor_properties(1, 1)
        set_actor_properties(2, 0.1)
        set_actor_properties(3, 0.1)

        print('Selected layer 1.')
        rens[0].interactive = True  # Cylinder -> Right renderer, Layer 1
        rens[1].interactive = True  # Sphere -> Left renderer, Layer 1
        rens[2].interactive = False  # Cone -> Right renderer, Layer 0
        rens[3].interactive = False  # Cube -> Left renderer, Layer 0

    iren.Render()

if __name__ == '__main__':
    main()
```
