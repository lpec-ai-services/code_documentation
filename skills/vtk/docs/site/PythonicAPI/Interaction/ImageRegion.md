<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/ImageRegion/ -->

# ImageRegion

Repository source: [ImageRegion](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/ImageRegion.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestImageRegion.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestImageRegion.png?raw=true target=)

### Description

This example shows how to get the image coordinates of the corners of a BorderWidget.

A perspective projection (`-p`) can be used instead of the parallel camera projection. If this is done, the borders of the widget can appear to be outside the image bounds.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/ImageRegion/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageRegion.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import (
    vtkImageReader2Factory,
    vtkJPEGReader
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkInteractionWidgets import (
    vtkBorderRepresentation,
    vtkBorderWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkPropPicker,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Get the coordinates of a region in an image.'
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

    # Setup both renderers.
    renderer = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    render_window.AddRenderer(renderer)

    renderer.AddActor(image_actor)

    renderer.active_camera.parallel_projection = parallel_projection
    renderer.ResetCamera()

    border_callback = BorderCallback(renderer, image_actor)

    border_widget.AddObserver('InteractionEvent', border_callback)

    render_window.window_name = 'ImageRegion'
    render_window.Render()
    border_widget.On()
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
        # lower_left = lower_left_coordinate.GetComputedViewportValue(self.renderer)

        upper_right_coordinate = border_widget.representation.position2_coordinate
        upper_right = upper_right_coordinate.GetComputedWorldValue(self.renderer)

        # Get the bounds (x_min, x_max, y_min, y_max, z_min, z_max)
        bounds = self.image_actor.bounds
        inside = lower_left[0] > bounds[0] and upper_right[0] < bounds[1] and \
                 lower_left[1] > bounds[2] and upper_right[1] < bounds[3]

        if inside:
            print(f'Lower left coordinate:  ({fmt_floats(lower_left, w=0, d=2, pt="f")})')
            print(f'Upper right coordinate: ({fmt_floats(upper_right, w=0, d=2, pt="f")})')
            picker = vtkPropPicker()
            ll_pt = list(lower_left)
            ll_pt[2] = 0.0
            picker.Pick3DPoint(ll_pt, self.renderer)
            # picker.Pick(ll_pt, self.renderer)
            path = picker.GetPath()
            valid_pick = False
            if path:
                num_items = path.number_of_items
                if num_items == 1:
                    print(f'There is {num_items} item in the path.')
                else:
                    print(f'There are {num_items} items in the path.')
                path.InitTraversal()
                for i in range(0, num_items):
                    node = path.GetNextNode()
                    picked_prop = node.view_prop
                    if self.image_actor == picked_prop:
                        print('Correct actor picked.')
                        valid_pick = True
                        break
            if valid_pick:
                # pos = picker.pick_position
                pos = picker.selection_point
                print(f'Lower left pick:  ({fmt_floats(pos, w=0, d=2, pt="f")})')

            ur_pt = list(upper_right)
            ur_pt[2] = 0.0
            picker.Pick3DPoint(ur_pt, self.renderer)
            path = picker.GetPath()
            valid_pick = False
            if path:
                num_items = path.number_of_items
                if num_items == 1:
                    print(f'There is {num_items} item in the path.')
                else:
                    print(f'There are {num_items} items in the path.')
                path.InitTraversal()
                for i in range(0, num_items):
                    node = path.GetNextNode()
                    picked_prop = node.view_prop
                    if self.image_actor == picked_prop:
                        print('Correct actor picked.')
                        valid_pick = True
                        break
            if valid_pick:
                # pos = picker.pick_position
                pos = picker.selection_point
                print(f'Upper right pick:  ({fmt_floats(pos, w=0, d=2, pt="f")})')
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
