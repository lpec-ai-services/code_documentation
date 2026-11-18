<!-- source: https://examples.vtk.org/site/PythonicAPI/ImplicitFunctions/IsoContours/ -->

# IsoContours

Repository source: [IsoContours](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImplicitFunctions/IsoContours.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImplicitFunctions/TestIsoContours.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImplicitFunctions/TestIsoContours.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImplicitFunctions/IsoContours/)), ([CSharp](https://examples.vtk.org/site/CSharp/ImplicitFunctions/IsoContours/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IsoContours.py**

```python
#!/usr/bin/env python3

import math
from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import VTK_DOUBLE, vtkCommand
from vtkmodules.vtkCommonDataModel import (
    vtkImageData
)
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleUser
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

    data = create_data()

    # Create an isosurface.
    contour_filter = vtkContourFilter(input_data=data)
    # (num_contours, range_start, range_end)
    contour_filter.GenerateValues(1, 10, 10)

    # Map the contours to graphical primitives.
    contour_mapper = vtkPolyDataMapper()
    contour_filter >> contour_mapper

    # Create an actor for the contours.
    contour_actor = vtkActor(mapper=contour_mapper)
    contour_actor.property.line_width = 5

    # Create the outline.
    outline_filter = vtkOutlineFilter(input_data=data)

    outline_mapper = vtkPolyDataMapper()
    outline_filter >> outline_mapper
    outline_actor = vtkActor(mapper=outline_mapper)
    outline_actor.property.color = colors.GetColor3d('BlueViolet')
    outline_actor.property.line_width = 3

    # Visualize
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(size=(500, 500), window_name='IsoContours')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    renderer.AddActor(contour_actor)
    renderer.AddActor(outline_actor)

    sp = SliderProperties()
    sp.title_text = 'Contour value'

    widget = make_slider_widget(sp, interactor)
    cb = SliderCallback(contour_filter)
    widget.AddObserver(vtkCommand.InteractionEvent, cb)

    # This style is designed to NOT provide any default functionality.
    # You must specify how to handle every event that you want handled.
    # In this case we use a slider callback.
    style = vtkInteractorStyleUser()
    interactor.interactor_style = style

    render_window.Render()
    interactor.Start()

def create_data():
    data = vtkImageData(extent=(-25, 25, -25, 25, 0, 0))
    data.AllocateScalars(VTK_DOUBLE, 1)

    extent = data.GetExtent()
    for y in range(extent[2], extent[3] + 1):
        for x in range(extent[0], extent[1] + 1):
            data.SetScalarComponentFromDouble(x, y, 0, 0, math.sqrt(x ** 2.0 + y ** 2.0))
    return data

class SliderProperties:
    dimensions = {
        'tube_width': 0.025,
        'slider_length': 0.1, 'slider_width': 0.2,
        'end_cap_length': 0.1, 'end_cap_width': 0.1,
        'title_height': 0.15, 'label_height': 0.1,
    }
    colors = {
        'title_color': 'AliceBlue', 'label_color': 'AliceBlue', 'slider_color': 'peacock',
        'selected_color': 'violet_red', 'bar_color': 'Black', 'bar_ends_color': 'Indigo',
        'value_color': 'DarkSlateGray'
    }
    range = {'minimum_value': 0.0, 'maximum_value': 30.0, 'value': 10.0}
    title_text = '',
    position = {'point1': (-15.0, -40.0, 0.0), 'point2': (15.0, -40.0, 0.0)}

def make_slider_widget(slider_properties, interactor):
    """
    Make a slider widget.
    :param slider_properties: range, title name, dimensions, colors, and position.
    :param interactor: The vtkInteractor.
    :return: The slider widget.
    """
    colors = vtkNamedColors()

    slider_rep = vtkSliderRepresentation3D(minimum_value=slider_properties.range['minimum_value'],
                                           maximum_value=slider_properties.range['maximum_value'],
                                           value=slider_properties.range['value'],
                                           title_text=slider_properties.title_text,
                                           tube_width=slider_properties.dimensions['tube_width'],
                                           slider_length=slider_properties.dimensions['slider_length'],
                                           slider_width=slider_properties.dimensions['slider_width'],
                                           end_cap_length=slider_properties.dimensions['end_cap_length'],
                                           end_cap_width=slider_properties.dimensions['end_cap_width'],
                                           title_height=slider_properties.dimensions['title_height'],
                                           label_height=slider_properties.dimensions['label_height'],
                                           )

    # Set the color properties.
    # slider_rep.title_property.color = colors.GetColor3d(slider_properties.colors['title_color'])
    # slider_rep.label_property.color = colors.GetColor3d(slider_properties.colors['label_color'])
    slider_rep.tube_property.color = colors.GetColor3d(slider_properties.colors['bar_color'])
    slider_rep.cap_property.color = colors.GetColor3d(slider_properties.colors['bar_ends_color'])
    slider_rep.slider_property.color = colors.GetColor3d(slider_properties.colors['slider_color'])
    slider_rep.selected_property.color = colors.GetColor3d(slider_properties.colors['selected_color'])

    # Set the position.
    slider_rep.point1_coordinate.coordinate_system = Coordinate.CoordinateSystem.VTK_WORLD
    slider_rep.point1_coordinate.value = slider_properties.position['point1']
    slider_rep.point2_coordinate.coordinate_system = Coordinate.CoordinateSystem.VTK_WORLD
    slider_rep.point2_coordinate.value = slider_properties.position['point2']

    widget = vtkSliderWidget(representation=slider_rep, interactor=interactor, enabled=True)
    widget.SetAnimationModeToAnimate()

    return widget

class SliderCallback:
    def __init__(self, contour_filter):
        """
        """
        self.contour_filter = contour_filter

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.contour_filter.GenerateValues(1, value, value)

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

if __name__ == '__main__':
    main()
```
