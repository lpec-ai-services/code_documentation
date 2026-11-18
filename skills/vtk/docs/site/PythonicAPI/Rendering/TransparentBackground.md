<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/TransparentBackground/ -->

# TransparentBackground

Repository source: [TransparentBackground](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/TransparentBackground.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestTransparentBackground.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestTransparentBackground.png?raw=true target=)

### Description

Demonstrates the use of two renderers. Notice that the second (and subsequent) renderers will have a transparent background.

You can manipulate the object in the second layer/renderer whilst the objects in the first layer/renderer form the background.

- Pressing **0** on the keyboard will let you manipulate the objects in layer 0.
- Pressing **1** on the keyboard will let you manipulate the objects in layer 1.

Info

Also see the [LayeredActors.py](LayeredActors.md) example, where we have added an extra callback so that the non-active layer objects move in conjunction with the active layer objects.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/TransparentBackground/)), ([Python](../../Python/Rendering/TransparentBackground.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TransparentBackground.py**

```python
#!/usr/bin/env python3

"""
    1. Create a cube and cone source.
    2. Render it with the cube in layer 0 and the cone in layer 1 of the render window.
    3. Interact with it.
    4. Notice that the cube and the cone are both visible and the layer 1 background is transparent.
    5. Pressing '0' on the keyboard will let you manipulate the objects in layer 0.
    6. Pressing '1' on the keyboard will let you manipulate the objects in layer 1.
"""

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkCubeSource
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def generate_and_display_cube_and_sphere():
    colors = vtkNamedColors()

    # Render the cube.
    cube_source = vtkCubeSource(x_length=4.0, y_length=9.0, z_length=1.0, center=(0.0, 0.0, 0.0))
    cube_mapper = vtkPolyDataMapper()
    cube_source >> cube_mapper
    cube_actor = vtkActor(mapper=cube_mapper)
    cube_actor.property.diffuse_color = colors.GetColor3d('DarkGreen')

    # Render the cone.
    cone_source = vtkConeSource(center=(0.0, 0.0, 0.0), height=1.0, radius=0.25, direction=(0.0, 1.0, 0.0),
                                resolution=60, capping=True)
    cone_mapper = vtkPolyDataMapper()
    cone_source >> cone_mapper
    cone_actor = vtkActor(mapper=cone_mapper)
    cone_actor.property.diffuse_color = colors.GetColor3d('DarkTurquoise')
    # Make the cone slightly transparent for fun.
    cone_actor.property.opacity = 0.75

    # The renderers, render window and interactor.
    renderers = list()
    #  We have two layers.
    ren_win = vtkRenderWindow(size=(800, 800), window_name='TransparentBackground', number_of_layers=2)
    for layer in range(0, 2):
        if layer == 0:
            # Layer 0 - background not transparent.
            renderers.append(vtkRenderer(background=colors.GetColor3d('Silver'), layer=layer))
            renderers[0].AddActor(cube_actor)
        if layer == 1:
            # Layer 1 - the background is transparent
            #           so we only see the layer 0 background color.
            renderers.append(vtkRenderer(background=colors.GetColor3d('MidnightBlue'), layer=layer))
            renderers[1].AddActor(cone_actor)
        ren_win.AddRenderer(renderers[layer])

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we always import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    ren_win.Render()
    ren_win.SetWindowName('TransparentBackground')

    iren.AddObserver('KeyPressEvent', keypress_callback_function)

    iren.Start()

def keypress_callback_function(caller, ev):
    iren = caller
    renderers = iren.render_window.renderers
    if renderers.number_of_items != 2:
        print(f'We need at least two renderers, we have only {renderers.number_of_items}.')
        return
    renderers.InitTraversal()
    # Top item
    ren0 = renderers.next_item
    # Bottom item
    ren1 = renderers.next_item

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

def main():
    generate_and_display_cube_and_sphere()

if __name__ == '__main__':
    main()
```
