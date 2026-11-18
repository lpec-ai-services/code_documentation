<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageSeparableConvolution/ -->

# ImageSeparableConvolution

Repository source: [ImageSeparableConvolution](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageSeparableConvolution.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageSeparableConvolution.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageSeparableConvolution.png?raw=true target=)

### Description

Read in a binary image and convolve it with a separable kernel. The input and output are displayed.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageSeparableConvolution/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageSeparableConvolution.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingGeneral import vtkImageSeparableConvolution
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'ImageSeparableConvolution.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The binary image file name to use e.g. Yinyang.png.')
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

    x_kernel = vtkFloatArray(number_of_tuples=5, number_of_components=1)
    x_kernel.SetValue(0, 1)
    x_kernel.SetValue(1, 1)
    x_kernel.SetValue(2, 1)
    x_kernel.SetValue(3, 1)
    x_kernel.SetValue(4, 1)

    convolution_filter = vtkImageSeparableConvolution(x_kernel=x_kernel)

    original_actor = vtkImageActor()
    reader >> original_actor.mapper

    convolution_cast_filter = vtkImageCast()
    convolution_cast_filter.SetOutputScalarTypeToUnsignedChar()

    convolution_actor = vtkImageActor()
    reader >> convolution_filter >> convolution_cast_filter >> convolution_actor.mapper

    # Define the viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.5, 1.0)
    convolution_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup the renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('CornflowerBlue'))
    original_renderer.AddActor(original_actor)
    original_renderer.ResetCamera()

    convolution_renderer = vtkRenderer(viewport=convolution_viewport, background=colors.GetColor3d('SteelBlue'))
    convolution_renderer.AddActor(convolution_actor)
    convolution_renderer.ResetCamera()

    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageSeparableConvolution')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(convolution_renderer)

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
