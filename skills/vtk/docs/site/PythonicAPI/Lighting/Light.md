<!-- source: https://examples.vtk.org/site/PythonicAPI/Lighting/Light/ -->

# Light

Repository source: [Light](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Lighting/Light.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Lighting/TestLight.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Lighting/TestLight.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Lighting/Light/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Light.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingUI
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkPlaneSource,
    vtkSphereSource
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkLight,
    vtkLightActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    renderer = vtkRenderer(background=colors.GetColor3d('Black'), background2=colors.GetColor3d('SkyBlue'),
                           gradient_background=True, automatic_light_creation=True)

    # Create a light.
    light_position = (0, 0, 1)
    light_focal_point = (0, 0, 0)

    light = vtkLight(light_type=Light.LightType.VTK_LIGHT_TYPE_SCENE_LIGHT,
                     position=light_position, positional=True,
                     focal_point=light_focal_point, cone_angle=10,
                     diffuse_color=colors.GetColor3d('Red'),
                     ambient_color=colors.GetColor3d('Lime'),
                     specular_color=colors.GetColor3d('Blue')
                     )
    original_lights = renderer.lights
    print(f'Originally there {lights_txt(original_lights)}')

    # Display where the light is.
    light_actor = vtkLightActor(light=light)
    renderer.AddViewProp(light_actor)

    # Display where the light is focused.
    light_focal_point_sphere = vtkSphereSource(center=light_focal_point, radius=0.1)
    light_focal_point_mapper = vtkPolyDataMapper()
    light_focal_point_sphere >> light_focal_point_mapper
    light_focal_point_actor = vtkActor(mapper=light_focal_point_mapper)
    light_focal_point_actor.property.color = colors.GetColor3d('Yellow')
    renderer.AddViewProp(light_focal_point_actor)

    # Create a plane for the light to shine on.
    plane_source = vtkPlaneSource(resolution=(100, 100))
    plane_mapper = vtkPolyDataMapper(input_data=plane_source.update().output)
    plane_actor = vtkActor(mapper=plane_mapper)
    renderer.AddActor(plane_actor)

    ren_win = vtkRenderWindow(window_name='Light')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    ren_win.Render()
    print(f'Now there {lights_txt(original_lights)}')
    renderer.AddLight(light)  # We must do this after ren_win.Render()
    print(f'Now there {lights_txt(original_lights)}')

    camera = renderer.active_camera
    camera.position = (-2.17199, -2.50774, 2.18)
    camera.focal_point = (-0.144661, -0.146372, 0.180482)
    camera.view_up = (0.0157883, 0.638203, 0.769706)
    camera.SetDistance(3.69921)
    camera.SetClippingRange(1.76133, 6.14753)

    iren.Start()

def lights_txt(light_collection):
    number_of_lights = light_collection.number_of_items
    match number_of_lights:
        case 0:
            return f'are no lights.'
        case 1:
            return f'is one light.'
        case _:
            return f'are {number_of_lights} lights.'

@dataclass(frozen=True)
class Light:
    @dataclass(frozen=True)
    class LightType:
        VTK_LIGHT_TYPE_HEADLIGHT: int = 1
        VTK_LIGHT_TYPE_CAMERA_LIGHT: int = 2
        VTK_LIGHT_TYPE_SCENE_LIGHT: int = 3

if __name__ == '__main__':
    main()
```
