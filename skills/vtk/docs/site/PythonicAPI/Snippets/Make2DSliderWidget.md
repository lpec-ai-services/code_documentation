<!-- source: https://examples.vtk.org/site/PythonicAPI/Snippets/Make2DSliderWidget/ -->

# Make2DSliderWidget

### Description

Implement a 2D slider widget.

A **vtkSliderRepresentation2D** has a large number of properties. So it is convenient to generate a struct containing the initial properties then use a function **make_slider_2d_properties()** set up slider(s) with your preferred values for the parameters. If there are multiple sliders in your application, then it is easy to modify the slider properties returned from this function as needed.

This is the approach adopted in [Slider2D](../Widgets/Slider2D.md) and [KochanekSplineDemo](../PolyData/KochanekSplineDemo.md).

This snippet provides you with:

- A dataclass of initial parameters: **Slider2DProperties**.
- A function to provide user defined values for the properties: **make_slider_2d_properties**.
- A function that generates the slider widget: **make_2d_slider_widget**.
- A class **SliderCallback** that uses data provided and the renderer to change the image. You will need to edit this as appropriate.

To use the snippet, click the *Copy to clipboard* at the upper right of the code blocks.

### Implementation

```python
# from dataclasses import dataclass
# from decimal import Decimal, ROUND_HALF_UP
# from typing import Tuple

# from vtkmodules.vtkInteractionWidgets import (
#     vtkSliderRepresentation2D,
#     vtkSliderWidget
# )

def make_slider_2d_properties():
    """
    This applies more specific values to the default Slider2DProperties.

    :return: The slider 2D properties.
    """
    sp = Slider2DProperties()

    sp.Colors.bar_color = 'MistyRose'
    sp.Colors.bar_ends_color = 'Yellow'
    sp.Colors.label_color = 'AliceBlue'
    sp.Colors.selected_color = 'DeepPink'
    sp.Colors.slider_color = 'Green'
    sp.Colors.title_color = 'AliceBlue'

    sp.Dimensions.end_cap_length = 0.02
    sp.Dimensions.label_height = 0.035
    sp.Dimensions.slider_length = 0.05
    sp.Dimensions.slider_width = 0.025
    sp.Dimensions.title_height = 0.045

    sp.Position.point1 = (0.3, 0.1)
    sp.Position.point2 = (0.7, 0.1)

    sp.Range.minimum_value = 0.0
    sp.Range.maximum_value = 20.0
    sp.Range.value = 3.0

    return sp

def make_2d_slider_widget(properties, interactor):
    """
    Make a 2D slider widget.

    :param properties: The 2D slider properties.
    :param interactor: The vtkInteractor.
    :return: The slider widget.
    """

    colors = vtkNamedColors()

    slider_rep = vtkSliderRepresentation2D(end_cap_length=properties.Dimensions.end_cap_length,
                                           end_cap_width=properties.Dimensions.end_cap_width,
                                           label_height=properties.Dimensions.label_height,
                                           slider_length=properties.Dimensions.slider_length,
                                           slider_width=properties.Dimensions.slider_width,
                                           title_height=properties.Dimensions.title_height,
                                           tube_width=properties.Dimensions.tube_width,
                                           minimum_value=properties.Range.minimum_value,
                                           maximum_value=properties.Range.maximum_value,
                                           value=properties.Range.value,
                                           title_text=properties.Text.title,
                                           )

    slider_rep.tube_property.color = colors.GetColor3d(properties.Colors.bar_color)
    slider_rep.cap_property.color = colors.GetColor3d(properties.Colors.bar_ends_color)
    slider_rep.label_property.color = colors.GetColor3d(properties.Colors.label_color)
    slider_rep.selected_property.color = colors.GetColor3d(properties.Colors.selected_color)
    slider_rep.slider_property.color = colors.GetColor3d(properties.Colors.slider_color)
    slider_rep.title_property.color = colors.GetColor3d(properties.Colors.title_color)

    slider_rep.point1_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point1_coordinate.value = properties.Position.point1
    slider_rep.point2_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point2_coordinate.value = properties.Position.point2

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
        # The color of the bar.
        bar_color: str = 'White'
        # The color of the ends of the bar.
        bar_ends_color: str = 'White'
        # The color of the text displaying the value.
        label_color: str = 'White'
        # The color of the knob when the mouse is held on it.
        selected_color: str = 'HotPink'
        # The color of the knob that slides.
        slider_color: str = 'White'
        # The color of the text indicating what the slider controls.
        title_color: str = 'White'

    @dataclass
    class Dimensions:
        end_cap_length: float = 0.005
        end_cap_width: float = 0.05
        label_height: float = 0.025
        slider_length: float = 0.01
        slider_width: float = 0.02
        title_height: float = 0.03
        tube_width: float = 0.008

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
        label_font_family = 'Arial'
        label_bold: bool = True
        label_italic: bool = False
        label_shadow: bool = True
        title: str = ''
        title_font_family = 'Arial'
        title_bold: bool = True
        title_italic: bool = False
        title_shadow: bool = True

class SliderCallback:

    def __init__(self, tree, pd):
        """
        """
        self.tree = tree
        self.pd = pd

    def __call__(self, caller, ev):
        slider_widget = caller
        # Get the value and do something with it.
        value = slider_widget.representation.value
        # Use C++ rounding where 0.5 or -0.5 is rounded away from zero to 1 or -1.
        level = int(Decimal(str(value)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        self.tree.GenerateRepresentation(level, self.pd)
        slider_widget.slider_representation.value = level
```

### Usage

Here we:

- Use **make_slider_2d_properties()** to generate the base slider properties.
- Then modify some of the properties (usually ranges positioning and the title).
- Create the slider widget **make_2d_slider_widget(sp, iren)**.
- Create the callback and set any needed parameters.
- Add the observer to the slider widget.

Of course if you have multiple sliders, you would:

- Implement the slider 2D properties for each slider, setting ranges, positioning and title as appropriate.
- Implement a widget for each slider widget.
- Create a callback for each widget.

Use the code in a similar fashion to this:

```python
    sp = make_slider_2d_properties()
    sp.Range.minimum_value = 0
    sp.Range.maximum_value = bsp_tree.max_level
    # Use C++ rounding where 0.5 or -0.5 is rounded away from zero to 1 or -1.
    sp.Range.value = int(Decimal(str(bsp_tree.max_level / 2)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

    sp.Text.title = 'Level'

    widget = make_2d_slider_widget(sp, iren)
    cb = SliderCallback(bsp_tree, polydata)
    widget.AddObserver(vtkCommand.InteractionEvent, cb, 0)
```

For examples showing the usage of this snippet and changing most of the default parameters, please see: [Slider2D](../Widgets/Slider2D.md) and [KochanekSplineDemo](../PolyData/KochanekSplineDemo.md).
