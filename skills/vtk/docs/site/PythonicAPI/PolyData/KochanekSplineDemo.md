<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/KochanekSplineDemo/ -->

# KochanekSplineDemo

Repository source: [KochanekSplineDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/KochanekSplineDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestKochanekSplineDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestKochanekSplineDemo.png?raw=true target=)

### Description

The example provides vtkSliderWidgets to change tension, continuity and bias of the [vtkKochanekSpline](https://www.vtk.org/doc/nightly/html/classvtkKochanekSpline.html).

1. tension - Changes the length of the tangent vector
2. continuity - Changes the sharpness in change between tangents
3. bias - Primarily changes the direction of the tangent vector

Seealso

This [wikipedia article](https://en.wikipedia.org/wiki/Kochanek%E2%80%93Bartels_spline) describes the controls in detail.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/KochanekSplineDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**KochanekSplineDemo.py**

```python
#!/usr/bin/env python3

import math
from dataclasses import dataclass
from typing import Tuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonComputationalGeometry import (
    vtkKochanekSpline,
    vtkParametricSpline
)
from vtkmodules.vtkCommonCore import (
    vtkCommand,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersSources import vtkSphereSource, vtkParametricFunctionSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (
    vtkSliderRepresentation2D,
    vtkSliderWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkGlyph3DMapper
)

def main():
    colors = vtkNamedColors()

    number_of_points = 7
    points = vtkPoints(number_of_points=number_of_points)
    radius = 1.0
    delta = 2.0 * math.pi / float(number_of_points)
    for n in range(0, number_of_points):
        theta = delta * n
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        z = n * (math.pi / number_of_points)
        points.SetPoint(n, x, y, z)

    x_spline = vtkKochanekSpline()
    y_spline = vtkKochanekSpline()
    z_spline = vtkKochanekSpline()

    spline = vtkParametricSpline(x_spline=x_spline, y_spline=y_spline, z_spline=z_spline, points=points)

    resolution = 50 * number_of_points
    function_source = vtkParametricFunctionSource(parametric_function=spline,
                                                  u_resolution=resolution, v_resolution=resolution,
                                                  w_resolution=resolution)
    function_source.Update()

    # Set up the actor and mapper.
    mapper = vtkPolyDataMapper()
    function_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('DarkSlateGrey')
    actor.property.line_width = 3.0

    # Glyph the points.
    sphere = vtkSphereSource(phi_resolution=21, theta_resolution=21, radius=0.1)

    # Create a polydata to store everything in.
    poly_data = vtkPolyData(points=points)

    point_mapper = vtkGlyph3DMapper(input_data=poly_data, source_connection=sphere.output_port)

    point_actor = vtkActor(mapper=point_mapper)
    point_actor.property.color = colors.GetColor3d('Gold')
    point_actor.property.opacity = 0.75

    # Set up the renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='KochanekSpline')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    style = vtkInteractorStyleTrackballCamera()
    render_window_interactor.interactor_style = style

    renderer.AddActor(actor)
    renderer.AddActor(point_actor)

    render_window.Render()

    sp1 = make_slider_2d_properties()
    sp1.Text.title = 'Tension'
    sp1.Position.point1 = (0.05, 0.1)
    sp1.Position.point2 = (0.45, 0.1)

    tension_widget = make_2d_slider_widget(sp1, render_window_interactor)
    tension_cb = SliderCallbackTension(spline, function_source)
    tension_widget.AddObserver(vtkCommand.InteractionEvent, tension_cb)

    sp2 = make_slider_2d_properties()
    sp2.Position.point1 = (0.55, 0.1)
    sp2.Position.point2 = (0.95, 0.1)
    sp2.Text.title = 'Continuity'

    continuity_widget = make_2d_slider_widget(sp2, render_window_interactor)
    continuity_cb = SliderCallbackContinuity(spline, function_source)
    continuity_widget.AddObserver(vtkCommand.InteractionEvent, continuity_cb)

    sp3 = make_slider_2d_properties()
    sp3.Text.title = 'Bias'
    sp3.Position.point1 = (0.85, 0.2)
    sp3.Position.point2 = (0.85, 0.8)

    bias_widget = make_2d_slider_widget(sp3, render_window_interactor)
    bias_cb = SliderCallbackBias(spline, function_source)
    bias_widget.AddObserver(vtkCommand.InteractionEvent, bias_cb)

    render_window.Render()
    render_window_interactor.Start()

def make_slider_2d_properties():
    """
    This applies more specific values to the default Slider2DProperties.

    :return: The slider 2D properties.
    """
    sp = Slider2DProperties()

    sp.Colors.title_color = 'PeachPuff'
    sp.Colors.label_color = 'AliceBlue'
    sp.Colors.slider_color = 'Green'
    sp.Colors.bar_color = 'MistyRose'
    sp.Colors.bar_ends_color = 'Yellow'
    sp.Colors.selected_color = 'DeepPink'

    sp.Dimensions.slider_length = 0.05
    sp.Dimensions.slider_width = 0.025
    sp.Dimensions.end_cap_length = 0.02
    sp.Dimensions.title_height = 0.045
    sp.Dimensions.label_height = 0.035

    sp.Position.point1 = (0.3, 0.1)
    sp.Position.point2 = (0.7, 0.1)

    sp.Range.minimum_value = -1
    sp.Range.maximum_value = 1
    sp.Range.value = 0

    return sp

def make_2d_slider_widget(properties, interactor):
    """
    Make a 2D slider widget.

    :param properties: The 2D slider properties.
    :param interactor: The vtkInteractor.
    :return: The slider widget.
    """
    colors = vtkNamedColors()

    slider_rep = vtkSliderRepresentation2D(minimum_value=properties.Range.minimum_value,
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
    slider_rep.title_property.color = colors.GetColor3d(properties.Colors.title_color)
    slider_rep.label_property.color = colors.GetColor3d(properties.Colors.label_color)
    slider_rep.tube_property.color = colors.GetColor3d(properties.Colors.bar_color)
    slider_rep.cap_property.color = colors.GetColor3d(properties.Colors.bar_ends_color)
    slider_rep.slider_property.color = colors.GetColor3d(properties.Colors.slider_color)
    slider_rep.selected_property.color = colors.GetColor3d(properties.Colors.selected_color)

    # Set the position.
    slider_rep.point1_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point1_coordinate.value = properties.Position.point1
    slider_rep.point2_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point2_coordinate.value = properties.Position.point2

    title_font_family = properties.Text.title_font_family
    match title_font_family:
        case 'Courier':
            slider_rep.title_property.SetFontFamilyToCourier()
        case 'Times':
            slider_rep.title_property.SetFontFamilyToTimes()
        case _:
            slider_rep.title_property.SetFontFamilyToArial()
    slider_rep.title_property.bold = properties.Text.title_bold
    slider_rep.title_property.italic = properties.Text.title_italic
    slider_rep.title_property.shadow = properties.Text.title_shadow
    label_font_family = properties.Text.label_font_family
    match label_font_family:
        case 'Courier':
            slider_rep.label_property.SetFontFamilyToCourier()
        case 'Times':
            slider_rep.label_property.SetFontFamilyToTimes()
        case _:
            slider_rep.label_property.SetFontFamilyToArial()
    slider_rep.label_property.bold = properties.Text.label_bold
    slider_rep.label_property.italic = properties.Text.label_italic
    slider_rep.label_property.shadow = properties.Text.label_shadow

    widget = vtkSliderWidget(interactor=interactor)
    widget.SetRepresentation(slider_rep)
    widget.enabled = True
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
class Slider2DProperties:
    @dataclass
    class Colors:
        # The color of the text indicating what the slider controls.
        title_color: str = 'White'
        # The color of the text displaying the value.
        label_color: str = 'White'
        # The color of the knob that slides.
        slider_color: str = 'White'
        # The color of the knob when the mouse is held on it.
        selected_color: str = 'HotPink'
        # The color of the bar.
        bar_color: str = 'White'
        # The color of the ends of the bar.
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
        coordinate_system: int = Coordinate.CoordinateSystem.VTK_NORMALIZED_VIEWPORT
        point1: Tuple = (0.1, 0.1)
        point2: Tuple = (0.9, 0.1)

    @dataclass
    class Range:
        minimum_value: float = 0.0
        maximum_value: float = 1.0
        value: float = 0.0

    @dataclass
    class Text:
        # Font families are: Ariel, Courier and Times
        title: str = ''
        title_font_family = 'Arial'
        title_bold: bool = True
        title_italic: bool = False
        title_shadow: bool = True
        label_font_family = 'Arial'
        label_bold: bool = True
        label_italic: bool = False
        label_shadow: bool = True

class SliderCallbackTension:

    def __init__(self, parametric_spline, parametric_source):
        """
        """
        self.parametric_spline = parametric_spline
        self.parametric_source = parametric_source

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.parametric_spline.x_spline.SetDefaultTension = value
        self.parametric_spline.y_spline.default_tension = value
        self.parametric_spline.z_spline.default_tension = value
        self.parametric_source.Modified()

class SliderCallbackContinuity:

    def __init__(self, parametric_spline, parametric_source):
        """
        """
        self.parametric_spline = parametric_spline
        self.parametric_source = parametric_source

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.parametric_spline.x_spline.default_continuity = value
        self.parametric_spline.y_spline.default_continuity = value
        self.parametric_spline.z_spline.default_continuity = value
        self.parametric_source.Modified()

class SliderCallbackBias:

    def __init__(self, parametric_spline, parametric_source):
        """
        """
        self.parametric_spline = parametric_spline
        self.parametric_source = parametric_source

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.parametric_spline.x_spline.default_bias = value
        self.parametric_spline.y_spline.default_bias = value
        self.parametric_spline.z_spline.default_bias = value
        self.parametric_source.Modified()

if __name__ == '__main__':
    main()
```
