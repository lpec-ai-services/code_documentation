<!-- source: https://examples.vtk.org/site/Python/ImageProcessing/Pad/ -->

# Pad

Repository source: [Pad](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImageProcessing/Pad.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestPad.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestPad.png?raw=true target=)

### Description

An important point about the discrete Fourier transform is that it treats the image as a periodic function. This means the pixels on the right border are adjacent to pixels on the left border. Since there is usually no physical relationship between these pixels, the artificial horizontal and vertical edges can distort the frequency spectrum and subsequent processing. To reduce these artifacts, the original image can be multiplied by a window function that becomes zero at the borders.

Another approach removes these artificial edges by smoothing only along the borders.

In both of these approaches, a portion of the original image is lost, so only the central portion of an image can be processed. If this is unacceptable, another solution is to double the dimensions of the original image with a mirror-padding filter. The intermediate image is periodic and continuous.

The left image has been padded with a constant (800). On the right, mirror padding has been used to remove artificial edges introduced by borders.

Info

See [Figure 10-12](../../VTKBook/10Chapter10.md#Figure%2010-12) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/Pad/)), ([PythonicAPI](../../PythonicAPI/ImageProcessing/Pad.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Pad.py**

```python
#!/usr/bin/env python

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
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()

    # Read the image.
    reader_factory = vtkImageReader2Factory()
    reader = reader_factory.CreateImageReader2(file_name)
    reader.SetFileName(file_name)
    reader.Update()

    # Pipelines
    constant_pad = vtkImageConstantPad()
    constant_pad.SetInputConnection(reader.GetOutputPort())
    constant_pad.SetConstant(800)
    constant_pad.SetOutputWholeExtent(-127, 383, -127, 383, 22, 22)

    mirror_pad = vtkImageMirrorPad()
    mirror_pad.SetInputConnection(reader.GetOutputPort())
    mirror_pad.SetOutputWholeExtent(constant_pad.GetOutputWholeExtent())

    # Create actors
    constant_pad_color = vtkImageMapToWindowLevelColors()
    constant_pad_color.SetWindow(2000)
    constant_pad_color.SetLevel(1000)
    constant_pad_color.SetInputConnection(constant_pad.GetOutputPort())

    constant_pad_actor = vtkImageActor()
    constant_pad_actor.GetMapper().SetInputConnection(
        constant_pad_color.GetOutputPort())
    constant_pad_actor.GetProperty().SetInterpolationTypeToNearest()

    mirror_pad_color = vtkImageMapToWindowLevelColors()
    mirror_pad_color.SetWindow(2000)
    mirror_pad_color.SetLevel(1000)
    mirror_pad_color.SetInputConnection(mirror_pad.GetOutputPort())

    mirror_pad_actor = vtkImageActor()
    mirror_pad_actor.GetMapper().SetInputConnection(
        mirror_pad_color.GetOutputPort())
    mirror_pad_actor.GetProperty().SetInterpolationTypeToNearest()

    # Set up the renderers.
    constant_pad_renderer = vtkRenderer()
    constant_pad_renderer.SetViewport(0.0, 0.0, 0.5, 1.0)
    constant_pad_renderer.AddActor(constant_pad_actor)
    constant_pad_renderer.ResetCamera()
    constant_pad_renderer.SetBackground(colors.GetColor3d("SlateGray"))

    mirror_pad_renderer = vtkRenderer()
    mirror_pad_renderer.SetViewport(0.5, 0.0, 1.0, 1.0)
    mirror_pad_renderer.AddActor(mirror_pad_actor)
    mirror_pad_renderer.SetActiveCamera(constant_pad_renderer.GetActiveCamera())
    mirror_pad_renderer.SetBackground(colors.GetColor3d("LightSlateGray"))

    render_window = vtkRenderWindow()
    render_window.SetSize(600, 300)
    render_window.SetWindowName('Pad')
    render_window.AddRenderer(constant_pad_renderer)
    render_window.AddRenderer(mirror_pad_renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()

    render_window_interactor.SetInteractorStyle(style)

    render_window_interactor.SetRenderWindow(render_window)
    constant_pad_renderer.GetActiveCamera().Dolly(1.4)
    constant_pad_renderer.GetActiveCamera().SetWindowCenter(-0.9, 0.013)
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

if __name__ == '__main__':
    main()
```
