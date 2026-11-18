<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/EllipticalButton/ -->

# EllipticalButton

Repository source: [EllipticalButton](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/EllipticalButton.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestEllipticalButton.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestEllipticalButton.png?raw=true target=)

### Description

This example creates a 3D button using vtkEllipsoidalButton. Interaction is done by assigning the button to a [vtkProp3DButtonRepresentation](https://www.vtk.org/doc/nightly/html/classvtkProp3DButtonRepresentation.html). Then a callback for a [vtkButtonWidget](https://www.vtk.org/doc/nightly/html/classvtkButtonWidget.html) controls the color of the button and the displayed geometry. Click on the button to see the color of both the button and geometry change.

Warning

There is a bug in [vtkEllipticalButtonSource](https://www.vtk.org/doc/nightly/html/classvtkEllipticalButtonSource.html). If CircumferentialResolution is odd, improper geometry is created.

Warning

Values close to 1.0 for RadialRatio can cause shading artifacts at the corners of the button.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/EllipticalButton/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**EllipticalButton.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonExecutionModel import vtkAlgorithm
from vtkmodules.vtkFiltersSources import (
    vtkEllipticalButtonSource,
    vtkSuperquadricSource
)
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkInteractionWidgets import (
    vtkButtonWidget,
    vtkProp3DButtonRepresentation
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTexture
)

def get_program_parameters():
    import argparse
    description = 'Elliptical Button.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', help='The image filename e.g. YinYang.png')
    args = parser.parse_args()
    return args.file_name

def main():
    color = vtkNamedColors()

    file_name = get_program_parameters()
    fn = Path(file_name)
    if not fn.is_file():
        print(f'{fn}\nNot found.')
        return

    source = vtkSuperquadricSource(phi_resolution=64, theta_resolution=64, theta_roundness=1.5, thickness=1.5, size=2)
    mapper = vtkPolyDataMapper()
    source >> mapper
    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=color.GetColor3d('Burlywood'))
    renderer.AddActor(actor)

    render_window = vtkRenderWindow(size=(200, 200), window_name='EllipticalButton')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Create the widget and its representation.
    button_actor1 = create_button_actor(fn)
    button_actor1.property.color = color.GetColor3d('Tomato')
    button_actor2 = create_button_actor(fn)
    button_actor2.property.color = color.GetColor3d('Banana')

    button_representation = vtkProp3DButtonRepresentation(follow_camera=True)
    button_representation.SetNumberOfStates(2)
    button_representation.SetButtonProp(0, button_actor1)
    button_representation.SetButtonProp(1, button_actor2)

    render_window_interactor.Initialize()

    button_callback = ButtonCallback(actor)
    actor.property.color = button_representation.GetButtonProp(0).property.color

    button_widget = vtkButtonWidget(interactor=render_window_interactor, representation=button_representation,
                                    enabled=True)
    button_widget.AddObserver('StateChangedEvent', button_callback.on_button_callback)

    renderer.ResetCamera()
    renderer.Render()

    render_window_interactor.Start()

def create_button_actor(texture_file):
    # Read the image.
    reader = vtkImageReader2Factory().CreateImageReader2(str(texture_file))
    reader.file_name = texture_file

    reader.update()

    # Aspect ratio of the image.
    dims = reader.output.dimensions
    aspect = float(dims[0]) / float(dims[1])

    texture = vtkTexture()
    reader >> texture

    elliptical_button_source = vtkEllipticalButtonSource(
        circumferential_resolution=50, shoulder_resolution=10, texture_resolution=10,
        radial_ratio=1.05, shoulder_texture_coordinate=(0.0, 0.0),
        texture_dimensions=(dims[0], dims[1]),
        texture_style=ButtonSource.TextureStyle.VTK_TEXTURE_STYLE_PROPORTIONAL,
        two_sided=True, width=aspect, height=1.0, depth=0.15, center=(2, 2, 0),
        output_points_precision=vtkAlgorithm.SINGLE_PRECISION)

    button_mapper = vtkPolyDataMapper()
    elliptical_button_source >> button_mapper

    button_actor = vtkActor(mapper=button_mapper, texture=texture)

    return button_actor

class ButtonCallback:

    def __init__(self, actor):
        self.actor = actor

    def on_button_callback(self, caller, event):
        button_widget = caller
        rep = button_widget.representation
        state = rep.state
        self.actor.property.color = rep.GetButtonProp(state).property.color
        print(f'State: {state}')

@dataclass(frozen=True)
class ButtonSource:
    @dataclass(frozen=True)
    class TextureStyle:
        VTK_TEXTURE_STYLE_FIT_IMAGE: int = 0
        VTK_TEXTURE_STYLE_PROPORTIONAL: int = 1

if __name__ == '__main__':
    main()
```
