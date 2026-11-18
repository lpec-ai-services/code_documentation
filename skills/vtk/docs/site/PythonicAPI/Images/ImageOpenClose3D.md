<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageOpenClose3D/ -->

# ImageOpenClose3D

Repository source: [ImageOpenClose3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageOpenClose3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageOpenClose3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageOpenClose3D.png?raw=true target=)

### Description

This example reads a binary image and performs opening on one value and closing on another (morphological operations).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageOpenClose3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageOpenClose3D.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingMorphological import vtkImageOpenClose3D
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'ImageOpenClose3D.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The image file name to use e.g. Yinyang.png.')
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

    colors = vtkNamedColors()

    # Read the image.
    reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
    reader.file_name = fp

    # Alternatively, use vtkPNGReader.
    # reader = vtkPNGReader(file_name = fp)

    reader.Update()

    open_close = vtkImageOpenClose3D(open_value=0, close_value=255, kernel_size=(5, 5, 3), release_data_flag=False)
    reader >> open_close

    original_actor = vtkImageActor()
    reader >> original_actor.mapper

    open_close_actor = vtkImageActor()
    open_close >> open_close_actor.mapper

    # Define the viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.5, 1.0)
    open_close_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup the renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('Sienna'))
    original_renderer.AddActor(original_actor)

    open_close_renderer = vtkRenderer(viewport=open_close_viewport, background=colors.GetColor3d('RoyalBlue'))
    open_close_renderer.AddActor(open_close_actor)
    open_close_renderer.ResetCamera()

    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageOpenClose3D')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(open_close_renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style

    render_window_interactor.render_window = render_window
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
