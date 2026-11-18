<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/CenterAnImage/ -->

# CenterAnImage

Repository source: [CenterAnImage](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/CenterAnImage.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestCenterAnImage.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestCenterAnImage.png?raw=true target=)

### Description

This moves (0,0) from the bottom left corner of the image to the center of the image.

Move the box widget around to get coordinates in the image.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/CenterAnImage/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CenterAnImage.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import vtkImageChangeInformation
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkInteractionWidgets import (
    vtkBorderRepresentation,
    vtkBorderWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Center an image.'
    epilogue = '''
    Shift the image center to (0,0)
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The image file name to use e.g. Ox.jpg.')
    args = parser.parse_args()
    return args.file_name

def main():
    fn = get_program_parameters()
    fp = Path(fn)
    file_check = True
    if not fp.is_file():
        print(f'Missing image file: {fp}.')
        file_check = False
    if not file_check:
        return

    # Read the image.
    image_reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
    image_reader.file_name = fp

    colors = vtkNamedColors()

    # Shift the image center to (0,0).
    # dims = image_reader.output.dimensions

    change_information = vtkImageChangeInformation(center_image=True)
    image_reader >> change_information

    image = change_information.update().output

    image_actor = vtkImageActor()
    image_actor.mapper.input_data = image

    render_window = vtkRenderWindow()
    interactor = vtkRenderWindowInteractor()

    style = vtkInteractorStyleImage()
    interactor.interactor_style = style

    rep = vtkBorderRepresentation()
    rep.BuildRepresentation()
    rep.border_color = colors.GetColor3d('Chartreuse')
    border_widget = vtkBorderWidget(interactor=interactor, selectable=False, representation=rep)

    interactor.render_window = render_window

    renderer = vtkRenderer(background=colors.GetColor3d('Peru'))
    render_window.AddRenderer(renderer)

    renderer.AddActor(image_actor)

    renderer.ResetCamera()

    border_callback = BorderCallback(renderer, image_actor)

    border_widget.AddObserver('InteractionEvent', border_callback)
    border_widget.On()
    render_window.window_name = 'CenterAnImage'
    render_window.Render()
    interactor.Start()

class BorderCallback:
    def __init__(self, renderer, actor):
        self.renderer = renderer
        self.image_actor = actor

    def __call__(self, caller, ev):
        border_widget = caller

        # Get the world coordinates of the two corners of the box.
        lower_left_coordinate = border_widget.representation.position_coordinate
        lower_left = lower_left_coordinate.GetComputedWorldValue(self.renderer)

        upper_right_coordinate = border_widget.representation.position2_coordinate
        upper_right = upper_right_coordinate.GetComputedWorldValue(self.renderer)

        # Get the bounds (x_min, x_max, y_min, y_max, z_min, z_max)
        bounds = self.image_actor.bounds
        inside = lower_left[0] > bounds[0] and upper_right[0] < bounds[1] and \
                 lower_left[1] > bounds[2] and upper_right[1] < bounds[3]

        if inside:
            print(f'Lower left coordinate: ({fmt_floats(lower_left, w=8, d=2, pt="f")})')
            print(f'Upper right coordinate: ({fmt_floats(upper_right, w=8, d=2, pt="f")})')
        else:
            print('The box is NOT inside the image.')

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
