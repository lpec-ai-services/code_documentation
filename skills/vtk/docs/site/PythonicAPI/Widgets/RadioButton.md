<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/RadioButton/ -->

# RadioButton

Repository source: [RadioButton](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/RadioButton.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestRadioButton.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestRadioButton.png?raw=true target=)

### Description

Display a sphere and three radio buttons controlling the appearance of the sphere.

This example is based on this discussion [How to implement radio buttons in C++ with [vtkButtonWidget](https://www.vtk.org/doc/nightly/html/classvtkButtonWidget.html) using VTK 9.3?](https://discourse.vtk.org/t/how-to-implement-radio-buttons-in-c-with-vtkbuttonwidget-using-vtk-9-3/15907/1).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/RadioButton/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RadioButton.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import VTK_UNSIGNED_CHAR
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkButtonWidget,
    vtkTexturedButtonRepresentation2D)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
)

def main():
    colors = vtkNamedColors()
    colors.SetColor("ParaViewBlueGrayBkg", 84, 89, 109, 255)
    colors.SetColor("ParaViewWarmGrayBkg", 98, 93, 90, 255)

    # Set up the renderer, render window and interactor.
    # renderer = vtkRenderer(background=colors.GetColor3d('ParaViewBlueGrayBkg'))
    renderer = vtkRenderer(background=colors.GetColor3d('ParaViewWarmGrayBkg'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='RadioButton')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    render_window_interactor.interactor_style.SetCurrentStyleToTrackballCamera()

    # Create some geometry.
    sphere_source = vtkSphereSource()

    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor_prop = vtkProperty(color=colors.GetColor3d('Peru'), edge_color=colors.GetColor3d('DarkSlateBlue'),
                             edge_visibility=True)
    actor = vtkActor(property=actor_prop, mapper=mapper)

    on_colors = ('Lavender', 'GreenYellow', 'Cornsilk')
    off_colors = ('Indigo', 'ForestGreen', 'Sienna')
    on_images = list()
    off_images = list()
    for i in range(0, 3):
        on_images.append(create_color_image(on_colors[i]))
        off_images.append(create_color_image(off_colors[i]))

    num_radio_buttons = 3
    # A dataclass is used to ensure that there is only ever one instance of the buttons.
    radio_buttons = Buttons()
    for i in range(0, num_radio_buttons):
        button_representation = vtkTexturedButtonRepresentation2D(number_of_states=2)
        button_representation.SetButtonTexture(0, off_images[i])
        button_representation.SetButtonTexture(1, on_images[i])

        # Place the buttons in the scene.
        bounds = [0.0, 0.0, 0.0, 100.0, 0.0, 0.0]
        bounds[0] = 215.0 + i * 60.0  # Adjust for spacing.
        bounds[1] = bounds[0] + 50.0
        button_representation.PlaceWidget(bounds)

        button_widget = vtkButtonWidget(interactor=render_window_interactor, representation=button_representation,
                                        enabled=True)
        radio_buttons.buttons.append(button_widget)

    renderer.AddActor(actor)

    callback = RadioButtonCallback(radio_buttons=radio_buttons, interactor=render_window_interactor, actor=actor)
    for i in range(0, num_radio_buttons):
        radio_buttons.buttons[i].AddObserver('StateChangedEvent', callback)

    if radio_buttons:
        radio_buttons.buttons[0].GetButtonRepresentation().SetState(1)

    cow = vtkCameraOrientationWidget(parent_renderer=renderer,
                                     interactor=render_window_interactor)
    # Enable the widget.
    cow.On()

    render_window.Render()
    render_window_interactor.Start()

def create_color_image(color):
    image = vtkImageData(dimensions=(10, 10, 1))
    image.AllocateScalars(VTK_UNSIGNED_CHAR, 3)

    colors = vtkNamedColors()
    pixel_color = colors.GetColor3ub(color)

    for x in range(0, 10):
        for y in range(0, 10):
            for i in range(0, 3):
                image.SetScalarComponentFromFloat(x, y, 0, i, pixel_color[i])

    return image

class RadioButtonCallback:
    def __init__(self, radio_buttons, actor, interactor):
        self.buttons = radio_buttons
        self.actor = actor
        self.interactor = interactor

    def __call__(self, caller, ev):
        # Just do this to demonstrate who called callback and the event that triggered it.
        # print(f'Caller: {caller.class_name}, Event Id: {ev}')
        pressed_button_index = -1
        #  Find the index of the pressed button.
        for i in range(0, len(self.buttons.buttons)):
            if self.buttons.buttons[i] == caller:
                pressed_button_index = i
        # If the pressed button is not already "on", turn it "on" and others
        # "off" Assuming 0 is "off" and 1 is "on".
        for i in range(0, len(self.buttons.buttons)):
            if i != pressed_button_index:
                self.buttons.buttons[i].GetButtonRepresentation().SetState(0)
            else:
                self.buttons.buttons[i].GetButtonRepresentation().SetState(1)

        # --- Add your radio button specific actions here ---
        # For example, you might print a message indicating
        #  the button pressed and surface selected:
        s = f'Radio button {pressed_button_index} selected -> '
        match pressed_button_index:
            case 1:
                s += "Wireframe"
                self.actor.property.representation = Property.Representation.VTK_WIREFRAME
            case 2:
                s += "Points"
                self.actor.GetProperty().point_size = 10
                self.actor.property.representation = Property.Representation.VTK_POINTS
            case _:
                s += "Surface"
                self.actor.property.representation = Property.Representation.VTK_SURFACE
        print(s)
        if self.interactor:
            self.interactor.Render()

@dataclass
class Buttons:
    buttons = list()

@dataclass(frozen=True)
class Property:
    @dataclass(frozen=True)
    class Interpolation:
        VTK_FLAT: int = 0
        VTK_GOURAUD: int = 1
        VTK_PHONG: int = 2
        VTK_PBR: int = 3

    @dataclass(frozen=True)
    class Representation:
        VTK_POINTS: int = 0
        VTK_WIREFRAME: int = 1
        VTK_SURFACE: int = 2

if __name__ == '__main__':
    main()
```
