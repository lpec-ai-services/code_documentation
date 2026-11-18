<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageProcessing/Pad/ -->

# Pad

Repository source: [Pad](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageProcessing/Pad.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageProcessing/TestPad.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageProcessing/TestPad.png?raw=true target=)

### Description

An important point about the discrete Fourier transform is that it treats the image as a periodic function. This means the pixels on the right border are adjacent to pixels on the left border. Since there is usually no physical relationship between these pixels, the artificial horizontal and vertical edges can distort the frequency spectrum and subsequent processing. To reduce these artifacts, the original image can be multiplied by a window function that becomes zero at the borders.

Another approach removes these artificial edges by smoothing only along the borders.

In both of these approaches, a portion of the original image is lost, so only the central portion of an image can be processed. If this is unacceptable, another solution is to double the dimensions of the original image with a mirror-padding filter. The intermediate image is periodic and continuous.

The left image has been padded with a constant (800). On the right, mirror padding has been used to remove artificial edges introduced by borders.

Info

See [Figure 10-12](../../VTKBook/10Chapter10.md#Figure%2010-12) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/Pad/)), ([Python](../../Python/ImageProcessing/Pad.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Pad.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingColor import vtkImageMapToWindowLevelColors
from vtkmodules.vtkImagingCore import (
    vtkImageConstantPad,
    vtkImageMirrorPad
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkImageProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()

    # Read the image.
    reader = vtkImageReader2Factory().CreateImageReader2(file_name)
    reader.file_name = file_name
    reader.update()

    # Pipelines
    constant_pad = vtkImageConstantPad(constant=800, output_whole_extent=(-127, 383, -127, 383, 22, 22))

    mirror_pad = vtkImageMirrorPad(output_whole_extent=constant_pad.output_whole_extent)

    # Create the actors.
    img_property = vtkImageProperty(interpolation_type=ImageProperty.InterpolationType.VTK_NEAREST_INTERPOLATION)

    constant_pad_color = vtkImageMapToWindowLevelColors(window=2000, level=1000)

    constant_pad_actor = vtkImageActor(property=img_property)
    reader >> constant_pad >> constant_pad_color >> constant_pad_actor.mapper
    mirror_pad_color = vtkImageMapToWindowLevelColors(window=2000, level=1000)

    mirror_pad_actor = vtkImageActor(property=img_property)
    reader >> mirror_pad >> mirror_pad_color >> mirror_pad_actor.mapper

    # Set up the renderers.
    constant_pad_renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'),
                                        viewport=(0.0, 0.0, 0.5, 1.0))
    constant_pad_renderer.AddActor(constant_pad_actor)
    constant_pad_renderer.ResetCamera()

    mirror_pad_renderer = vtkRenderer(background=colors.GetColor3d('LightSlateGray'),
                                      viewport=(0.5, 0.0, 1.0, 1.0),
                                      active_camera=constant_pad_renderer.active_camera)
    mirror_pad_renderer.AddActor(mirror_pad_actor)
    mirror_pad_renderer.ResetCamera()

    render_window = vtkRenderWindow(size=(600, 300), window_name='Pad')
    render_window.AddRenderer(constant_pad_renderer)
    render_window.AddRenderer(mirror_pad_renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()

    render_window_interactor.interactor_style = style

    render_window_interactor.render_window = render_window
    constant_pad_renderer.active_camera.Dolly(1.4)
    constant_pad_renderer.active_camera.window_center = (-0.9, 0.013)
    constant_pad_renderer.ResetCameraClippingRange()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

def get_program_parameters():
    import argparse
    description = 'Demonstrate image padding by using a constant and using mirror padding.'
    epilogue = '''
     The left image has been padded with a constant (800).
     In the right image, mirror padding has been used to remove artificial edges introduced by borders.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    args = parser.parse_args()
    return args.filename

@dataclass(frozen=True)
class ImageProperty:
    @dataclass(frozen=True)
    class InterpolationType:
        VTK_NEAREST_INTERPOLATION: int = 0
        VTK_LINEAR_INTERPOLATION: int = 1
        VTK_CUBIC_INTERPOLATION: int = 2

if __name__ == '__main__':
    main()
```
