<!-- source: https://examples.vtk.org/site/PythonicAPI/Snippets/Slider3D/ -->

# Slider3D

### Description

Implement a 3D slider widget.

A vtkSliderRepresentation3D has a large number of properties. Most of these properties are defined in the dataclass: `Slider3DProperties`. It is best to create a function `def make_slider_properties():` that will be used to set up the slider with your preferred values for the parameters. If there are multiple sliders in your application then it is easy to modify the slider properties returned from this function as needed.

This is the approach adopted in [Slider3D](../Widgets/Slider3D.md).

To use the snippet, click the *Copy to clipboard* at the upper right of the code blocks.

### Implementation

```python
# from dataclasses import dataclass
# from typing import Tuple

# from vtkmodules.vtkInteractionWidgets import (
#     vtkSliderRepresentation3D,
#     vtkSliderWidget
# )

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

    def __init__(self, source):
        """
        """
        self.source = source

    def __call__(self, caller, ev):
        slider_widget = caller
        # Get the value and do something with it.
        value = slider_widget.representation.value
        self.source.something = value
```

### Usage

For an example showing the usage of this snippet and changing most of the default parameters, please see: [Slider3D](../Widgets/Slider3D.md).
