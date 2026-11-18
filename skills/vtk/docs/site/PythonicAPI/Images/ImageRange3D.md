<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageRange3D/ -->

# ImageRange3D

Repository source: [ImageRange3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageRange3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageRange3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageRange3D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageRange3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageRange3D.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingGeneral import vtkImageRange3D
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'ImageRange3D.'
    epilogue = '''
    Replace every pixel with the range of its neighbors according to a kernel.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The image file name to use e.g. Gourds2.jpg.')
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

    # Create actors
    original_actor = vtkImageActor()
    reader >> original_actor.mapper

    range_filter = vtkImageRange3D(kernel_size=(5, 5, 5))

    range_cast_filter = vtkImageCast()
    range_cast_filter.SetOutputScalarTypeToUnsignedChar()

    range_actor = vtkImageActor()
    reader >> range_filter >> range_cast_filter >> range_actor.mapper

    # Define the viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.5, 1.0)
    range_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup renderers
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('CornflowerBlue'))
    original_renderer.AddActor(original_actor)
    original_renderer.ResetCamera()

    range_renderer = vtkRenderer(viewport=range_viewport, background=colors.GetColor3d('SteelBlue'))
    range_renderer.AddActor(range_actor)
    range_renderer.ResetCamera()

    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageRange3D')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(range_renderer)

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
