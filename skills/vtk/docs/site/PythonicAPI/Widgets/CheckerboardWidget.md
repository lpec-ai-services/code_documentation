<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/CheckerboardWidget/ -->

# CheckerboardWidget

Repository source: [CheckerboardWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/CheckerboardWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestCheckerboardWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestCheckerboardWidget.png?raw=true target=)

### Description

Compare two images with a checkerboard. The widget permits interactive control of the number of checkers in the x/y directions. Checkerboards are often used to compare the results of image registration. For an alternative image comparison widget try the [RectilinearWipeWidget](RectilinearWipeWidget.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/CheckerboardWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CheckerboardWidget.py**

```python
# !/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkJPEGReader
from vtkmodules.vtkImagingGeneral import vtkImageCheckerboard
from vtkmodules.vtkInteractionWidgets import vtkCheckerboardWidget
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Checkerboard widget.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name1', help='The first file name to use e.g. Gourds2.jpg.')
    parser.add_argument('file_name2', help='The second file name to use e.g. Ox.jpg.')
    args = parser.parse_args()
    return args.file_name1, args.file_name2

def main():
    file_name1, file_name2 = get_program_parameters()

    # Read the images.
    reader1 = vtkJPEGReader(file_name=file_name1)
    reader2 = vtkJPEGReader(file_name=file_name2)

    # Create a checker pipeline.
    checker = vtkImageCheckerboard(number_of_divisions=(3, 3, 1))
    reader1 >> select_ports(0, checker)
    reader2 >> select_ports(1, checker)

    # Create the RenderWindow, Renderer and both Actors.
    colors = vtkNamedColors()
    ren = vtkRenderer(background=colors.GetColor3d('Wheat'))
    ren_win = vtkRenderWindow(size=(900, 900), window_name='CheckerboardWidget')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    checker_actor = vtkImageActor()
    checker >> checker_actor.mapper

    # VTK widgets consist of two parts: the widget part that handles
    # event processing and the widget representation that defines how
    # the widget appears in the scene,
    # (i.e., matters pertaining to geometry).
    checker_widget = vtkCheckerboardWidget()
    checker_widget.interactor = iren

    checker_widget_rep = checker_widget.representation

    checker_widget_rep.image_actor = checker_actor
    checker_widget_rep.checkerboard = checker

    # Add the actors to the renderer, set the background and size.
    ren.AddActor(checker_actor)

    # Render the image.
    iren.Initialize()
    ren_win.Render()
    checker_widget.On()
    iren.Start()

if __name__ == '__main__':
    main()
```
