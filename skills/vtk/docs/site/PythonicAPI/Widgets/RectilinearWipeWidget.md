<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/RectilinearWipeWidget/ -->

# RectilinearWipeWidget

Repository source: [RectilinearWipeWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/RectilinearWipeWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestRectilinearWipeWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestRectilinearWipeWidget.png?raw=true target=)

### Description

This example illustrates the Rectilinear Wipe widget. This widget is useful for comparing two images. There are 7 different image comparison modes. A rectilinear wipe is a 2x2 checkerboard pattern created by combining two separate images, where various combinations of the checker squares are possible. Using this widget, the user can adjust the layout of the checker pattern, such as moving the center point, moving the horizontal separator, or moving the vertical separator.

Pressing keys 0-6 select the various wipe modes.

For an alternative image comparison widget try the [Checkerboard widget](CheckerboardWidget.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/RectilinearWipeWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RectilinearWipeWidget.py**

```python
# !/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingHybrid import vtkImageRectilinearWipe
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkInteractionWidgets import vtkRectilinearWipeWidget
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Rectilinear Wipe Widget.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name1', help='The first file name to use e.g. Gourds2.jpg.')
    parser.add_argument('file_name2', help='The second file name to use e.g. Ox.jpg.')
    parser.add_argument('-w', '--wipe_mode', required=False, type=int, choices=range(0, 7), default=0, metavar="[0-6]",
                        help='Image comparison modes. Default is 0.')
    args = parser.parse_args()
    return args.file_name1, args.file_name2, args.wipe_mode

def main():
    file_name1, file_name2, wipe_mode = get_program_parameters()

    # Read the images.
    reader1 = vtkImageReader2Factory().CreateImageReader2(file_name1)
    reader1.file_name = file_name1
    reader2 = vtkImageReader2Factory().CreateImageReader2(file_name2)
    reader2.file_name = file_name2

    # Create a wipe pipeline.
    wipe = vtkImageRectilinearWipe(position=(256, 256), wipe=wipe_mode)
    reader1 >> select_ports(0, wipe)
    reader2 >> select_ports(1, wipe)

    # Create the RenderWindow, Renderer and both Actors.
    colors = vtkNamedColors()
    ren = vtkRenderer(background=colors.GetColor3d('Wheat'))
    ren_win = vtkRenderWindow(size=(900, 900), window_name='RectilinearWipeWidget')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleImage()
    iren.interaction_style = style

    wipe_actor = vtkImageActor()
    wipe >> wipe_actor.mapper

    # VTK widgets consist of two parts: the widget part that handles
    # event processing and the widget representation that defines how
    # the widget appears in the scene,
    # (i.e., matters pertaining to geometry).
    wipe_widget = vtkRectilinearWipeWidget()
    wipe_widget.interactor = iren

    wipe_widget_rep = wipe_widget.representation
    wipe_widget_rep.image_actor = wipe_actor
    wipe_widget_rep.rectilinear_wipe = wipe
    wipe_widget_rep.property.line_width = 2.0
    wipe_widget_rep.property.opacity = 0.75

    # Add the actors to the renderer, set the background and size.
    ren.AddActor(wipe_actor)

    iren.Initialize()

    wis = WipeInteractorStyle(wipe, ren_win)
    iren.AddObserver('KeyPressEvent', wis.select_layer)

    # Render the image.
    ren_win.Render()
    wipe_widget.On()
    iren.Start()

def build_keys():
    keycodes = [
        '0', 'KP_0',
        '1', 'KP_1',
        '2', 'KP_2',
        '3', 'KP_3',
        '4', 'KP_4',
        '5', 'KP_5',
        '6', 'KP_6',
        # '7', 'KP_7',
        # '8', 'KP_8',
        # '9', 'KP_0',
    ]
    kv = dict()
    for v in keycodes:
        if 'KP_' in v:
            x = int(v.split('_')[1])
        else:
            x = int(v)
        kv[v] = x
    return kv

class WipeInteractorStyle():
    def __init__(self, wipe, ren_win):
        super().__init__()
        self.wipe = wipe
        self.ren_win = ren_win
        self.keys = build_keys()
        print(self.keys)

    def select_layer(self, caller, ev):
        """
        Select the layer to manipulate.
        :param caller:
        :param ev:
        :return:
        """
        iren = caller

        key = iren.key_sym
        if key in self.keys:
            self.wipe.SetWipe(self.keys[key])
        self.ren_win.Render()

@dataclass(frozen=True)
class InteractorStyleImage:
    @dataclass(frozen=True)
    class Style:
        VTKIS_IMAGE2D: int = 2
        VTKIS_IMAGE3D: int = 3
        VTKIS_IMAGE_SLICING: int = 4

    @dataclass(frozen=True)
    class Motion:
        VTKIS_WINDOW_LEVEL: int = 1024
        VTKIS_SLICE: int = 1025

if __name__ == '__main__':
    main()
```
