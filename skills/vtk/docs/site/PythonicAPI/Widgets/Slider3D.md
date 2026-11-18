<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/Slider3D/ -->

# Slider3D

Repository source: [Slider3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/Slider3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestSlider3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestSlider3D.png?raw=true target=)

### Description

This example demonstrates how to use a 3D slider widget. Here, the slider controls the resolution of the sphere. The slider is positioned in world coordinates - so if you rotate/translate/scale the scene, the slider will change orientation/position/size. Contrast this with [Slider2D](Slider2D.md) that remains at a fixed location in the window.

If the callback is connected to InteractionEvent, the scene will update whenever the mouse is moved on the slider. This is not ideal if the re-rendering takes significant time as it will make the interaction very choppy. If you want to move the slider and have the scene update when the mouse button is released, connect the callback to EndInteractionEvent instead.

Note

This original source code for this example is [here](https://gitlab.kitware.com/vtk/vtk/blob/395857190c8453508d283958383bc38c9c2999bf/Examples/Widgets/Cxx/Slider.cxx).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/Slider3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Slider3D.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Tuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkCommand
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (
    vtkSliderRepresentation3D,
    vtkSliderWidget
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

    # A sphere.
    phi_resolution = 4
    sphere_source = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=4.0,
                                    phi_resolution=phi_resolution,
                                    theta_resolution=phi_resolution * 2)

    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.SetInterpolationToFlat()
    actor.property.color = colors.GetColor3d('MistyRose')
    actor.property.edge_color = colors.GetColor3d('Tomato')
    actor.property.edge_visibility = True

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='Slider3D')
    render_window.AddRenderer(renderer)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    style = vtkInteractorStyleTrackballCamera()
    render_window_interactor.interactor_style = style

    # Add the actors to the scene.
    renderer.AddActor(actor)

    # Render an image (lights and cameras are created automatically).
    render_window.Render()

    sp = make_slider_properties()

    sp.Range.value = sphere_source.theta_resolution
    sp.Text.title = 'Sphere Resolution'

    widget = make_3d_slider_widget(sp, render_window_interactor)
    cb = SliderCallback(sphere_source)
    widget.AddObserver(vtkCommand.InteractionEvent, cb)

    renderer.Render()
    renderer.active_camera.Dolly(0.9)
    render_window_interactor.Initialize()
    render_window.Render()

    render_window_interactor.Start()

def make_slider_properties():
    sp = Slider3DProperties()
    sp.Range.minimum_value = 3
    sp.Range.maximum_value = 50
    sp.Position.point1 = (-4.0, 5.9, 0.0)
    sp.Position.point2 = (4, 5.9, 0)
    sp.Dimensions.slider_length = 0.075
    sp.Dimensions.slider_width = 0.05
    sp.Dimensions.end_cap_length = 0.05
    sp.Dimensions.title_height = 0.125
    sp.Dimensions.label_height = 0.055
    # Set color properties:
    # Change the color of the knob that slides.
    sp.Colors.slider_color = 'Green'
    # Change the color of the text indicating what the slider controls.
    sp.Colors.title_color = 'AliceBlue'
    # Change the color of the text displaying the value.
    sp.Colors.label_color = 'AliceBlue'
    # Change the color of the knob when the mouse is held on it.
    sp.Colors.selected_color = 'DeepPink'
    # Change the color of the bar.
    sp.Colors.bar_color = 'MistyRose'
    # Change the color of the ends of the bar.
    sp.Colors.bar_ends_color = 'Yellow'

    return sp

def make_3d_slider_widget(properties, interactor):
    """
    Make a 3D slider widget.

    :param properties: The 3D slider properties.
    :param interactor: The vtkInteractor.
    :return: The slider widget.
    """
    colors = vtkNamedColors()

    slider_rep = vtkSliderRepresentation3D(minimum_value=properties.Range.minimum_value,
                                           maximum_value=properties.Range.maximum_value,
                                           value=properties.Range.value,
                                           title_text=properties.Text.title,
                                           tube_width=properties.Dimensions.tube_width,
                                           slider_length=properties.Dimensions.slider_length,
                                           slider_width=properties.Dimensions.slider_width,
                                           end_cap_length=properties.Dimensions.end_cap_length,
                                           end_cap_width=properties.Dimensions.end_cap_width,
                                           title_height=properties.Dimensions.title_height,
                                           label_height=properties.Dimensions.label_height,
                                           )

    # Set the color properties.
    slider_rep.tube_property.color = colors.GetColor3d(properties.Colors.bar_color)
    slider_rep.cap_property.color = colors.GetColor3d(properties.Colors.bar_ends_color)
    slider_rep.slider_property.color = colors.GetColor3d(properties.Colors.slider_color)
    slider_rep.selected_property.color = colors.GetColor3d(properties.Colors.selected_color)

    # Set the position.
    slider_rep.point1_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point1_coordinate.value = properties.Position.point1
    slider_rep.point2_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point2_coordinate.value = properties.Position.point2

    widget = vtkSliderWidget(representation=slider_rep, interactor=interactor, enabled=True)
    widget.SetAnimationModeToAnimate()

    return widget

@dataclass(frozen=True)
class Coordinate:
    @dataclass(frozen=True)
    class CoordinateSystem:
        VTK_DISPLAY: int = 0
        VTK_NORMALIZED_DISPLAY: int = 1
        VTK_VIEWPORT: int = 2
        VTK_NORMALIZED_VIEWPORT: int = 3
        VTK_VIEW: int = 4
        VTK_POSE: int = 5
        VTK_WORLD: int = 6
        VTK_USERDEFINED: int = 7

@dataclass
class Slider3DProperties:
    @dataclass
    class Colors:
        title_color: str = 'White'
        label_color: str = 'White'
        slider_color: str = 'White'
        selected_color: str = 'HotPink'
        bar_color: str = 'White'
        bar_ends_color: str = 'White'

    @dataclass
    class Dimensions:
        tube_width: float = 0.008
        slider_length: float = 0.01
        slider_width: float = 0.02
        end_cap_length: float = 0.005
        end_cap_width: float = 0.05
        title_height: float = 0.03
        label_height: float = 0.025

    @dataclass
    class Position:
        coordinate_system: int = Coordinate.CoordinateSystem.VTK_WORLD
        point1: Tuple = (0.1, 0.1, 0.0)
        point2: Tuple = (0.9, 0.1, 0.0)

    @dataclass
    class Range:
        minimum_value: float = 0.0
        maximum_value: float = 1.0
        value: float = 0.0

    @dataclass
    class Text:
        title: str = ''

class SliderCallback:

    def __init__(self, sphere_source):
        """
        """
        self.sphere_source = sphere_source

    def __call__(self, caller, ev):
        slider_widget = caller
        value = int(slider_widget.representation.value)
        self.sphere_source.phi_resolution = value // 2
        self.sphere_source.theta_resolution = value

if __name__ == '__main__':
    main()
```
