<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/ImageClip/ -->

# ImageClip

Repository source: [ImageClip](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/ImageClip.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestImageClip.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestImageClip.png?raw=true target=)

### Description

This example loads an image into the left half of the window. When you move the border widget (the green square in the bottom left corner) over the image, the region that is selected is displayed in the right half of the window.

A perspective projection (`-p`) can be used instead of the parallel camera projection. If this is done, the borders of the widget can appear to be outside the image bounds.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/ImageClip/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageClip.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkMath
from vtkmodules.vtkCommonExecutionModel import vtkStreamingDemandDrivenPipeline
from vtkmodules.vtkIOImage import (
    vtkImageReader2Factory,
    vtkJPEGReader
)
from vtkmodules.vtkImagingCore import vtkImageClip
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
    description = 'Clip an image.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The image file name to use e.g. Gourds2.jpg.')
    parser.add_argument('-p', '--perspective', action='store_false', help='Use perspective projection.')
    args = parser.parse_args()
    return args.file_name, args.perspective

def main():
    fn, parallel_projection = get_program_parameters()
    fp = Path(fn)
    file_check = True
    if not fp.is_file():
        print(f'Missing image file: {fp}.')
        file_check = False
    if not file_check:
        return

    use_factory = True
    # Read the image.
    if use_factory:
        image_reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
        image_reader.file_name = fp
    else:
        image_reader: vtkJPEGReader = vtkJPEGReader(file_name=fp)
        if not image_reader.CanReadFile(fp):
            print(f'Error: cannot read {fp}')
            return
    image_reader.update()

    extent = image_reader.output.extent
    # x_min, x_max, y_min, y_max, z_in, z_max
    print(f'extent: ({fmt_floats(extent, w=0, d=2, pt="f")})')

    colors = vtkNamedColors()

    image_actor = vtkImageActor()
    image_reader >> image_actor.mapper

    render_window = vtkRenderWindow()

    interactor = vtkRenderWindowInteractor()

    style = vtkInteractorStyleImage()
    interactor.interactor_style = style

    rep = vtkBorderRepresentation()
    rep.BuildRepresentation()
    rep.border_color = colors.GetColor3d('Lime')
    border_widget = vtkBorderWidget(interactor=interactor, selectable=False, representation=rep)

    interactor.render_window = render_window

    # Define viewport ranges in normalized coordinates.(x_min, y_min, x_max, y_max).
    left_viewport = (0.0, 0.0, 0.5, 1.0)
    right_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup both renderers.
    left_renderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('DarkSlateGray'))
    render_window.AddRenderer(left_renderer)

    right_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('DimGray'))
    render_window.AddRenderer(right_renderer)

    image_clip = vtkImageClip(clip_data=True)
    image_reader >> image_clip
    image_reader.UpdateInformation()
    image_clip.SetOutputWholeExtent(
        image_reader.GetOutputInformation(0).Get(vtkStreamingDemandDrivenPipeline.WHOLE_EXTENT()))

    clip_actor = vtkImageActor()
    image_clip >> clip_actor.mapper

    left_renderer.AddActor(image_actor)
    right_renderer.AddActor(clip_actor)

    border_callback = BorderCallback(left_renderer, image_actor, image_clip)

    border_widget.AddObserver('InteractionEvent', border_callback)

    render_window.window_name = 'ImageClip'

    left_renderer.active_camera.parallel_projection = parallel_projection
    left_renderer.ResetCamera()
    right_renderer.active_camera.parallel_projection = parallel_projection
    right_renderer.ResetCamera()

    render_window.Render()
    border_widget.On()
    interactor.Start()

class BorderCallback:
    def __init__(self, renderer, actor, clip):
        self.renderer = renderer
        self.image_actor = actor
        self.clip_filter = clip

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
            print(f'Lower left coordinate:  ({fmt_floats(lower_left, w=0, d=2, pt="f")})')
            print(f'Upper right coordinate: ({fmt_floats(upper_right, w=0, d=2, pt="f")})')
            self.clip_filter.SetOutputWholeExtent(
                vtkMath.Round(lower_left[0]), vtkMath.Round(upper_right[0]),
                vtkMath.Round(lower_left[1]), vtkMath.Round(upper_right[1]), 0, 1)
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
