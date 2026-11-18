<!-- source: https://examples.vtk.org/site/Python/ImageProcessing/IsoSubsample/ -->

# IsoSubsample

Repository source: [IsoSubsample](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImageProcessing/IsoSubsample.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestIsoSubsample.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestIsoSubsample.png?raw=true target=)

### Description

An artifact called aliasing occurs when sub-sampling and is often associated with stair-stepping edges. Sampling theory proves that discrete sampled signals with spacing S, completely describe continuous functions composed of frequencies less than S/2. When a signal is sub-sampled, its capacity to hold high frequency information is reduced. However, the high frequency energy does not disappear. It wraps around the frequency spectrum appearing as a low frequency alias artifact. The solution, which eliminates this artifact, is to low-pass filter before sub-sampling.

Low-pass smoothing reduces the high frequency range of an image that would cause aliasing. The same aliasing phenomena occurs when acquiring data. If a signal from an analog source contains high frequencies, saving the analog data in a discrete form requires sub-sampling that will introduce alias artifacts. For this reason, it is common practice to acquire data at high resolutions,then smooth and subsample to reduce the image to a manageable size.

This example demonstrates aliasing that occurs when a high-frequency signal is sub-sampled. High frequencies appear as low frequency artifacts. The left image is an isosurface of a skull after sub-sampling. The right image used a low-pass filter before sub-sampling to reduce aliasing.

Info

See [this figure](../../VTKBook/10Chapter10.md#Figure%2010-5) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/IsoSubsample/)), ([PythonicAPI](../../PythonicAPI/ImageProcessing/IsoSubsample.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IsoSubsample.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeneral import vtkImageMarchingCubes
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import vtkImageShrink3D
from vtkmodules.vtkImagingGeneral import vtkImageGaussianSmooth
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
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

    # Smoothed pipeline.
    smooth = vtkImageGaussianSmooth()
    smooth.SetDimensionality(3)
    smooth.SetInputConnection(reader.GetOutputPort())
    smooth.SetStandardDeviations(1.75, 1.75, 0.0)
    smooth.SetRadiusFactor(2)

    subsample_smoothed = vtkImageShrink3D()
    subsample_smoothed.SetInputConnection(smooth.GetOutputPort())
    subsample_smoothed.SetShrinkFactors(4, 4, 1)

    iso_smoothed = vtkImageMarchingCubes()
    iso_smoothed.SetInputConnection(smooth.GetOutputPort())
    iso_smoothed.SetValue(0, 1150)

    iso_smoothed_mapper = vtkPolyDataMapper()
    iso_smoothed_mapper.SetInputConnection(iso_smoothed.GetOutputPort())
    iso_smoothed_mapper.ScalarVisibilityOff()

    iso_smoothed_actor = vtkActor()
    iso_smoothed_actor.SetMapper(iso_smoothed_mapper)
    iso_smoothed_actor.GetProperty().SetColor(colors.GetColor3d("Ivory"))

    # Unsmoothed pipeline.
    # Sub sample the data.
    subsample = vtkImageShrink3D()
    subsample.SetInputConnection(reader.GetOutputPort())
    subsample.SetShrinkFactors(4, 4, 1)

    iso = vtkImageMarchingCubes()
    iso.SetInputConnection(subsample.GetOutputPort())
    iso.SetValue(0, 1150)

    iso_mapper = vtkPolyDataMapper()
    iso_mapper.SetInputConnection(iso.GetOutputPort())
    iso_mapper.ScalarVisibilityOff()

    iso_actor = vtkActor()
    iso_actor.SetMapper(iso_mapper)
    iso_actor.GetProperty().SetColor(colors.GetColor3d("Ivory"))

    # The rendering Pipeline.

    # Setup the render window, renderer, and interactor.
    left_viewport = [0.0, 0.0, 0.5, 1.0]
    right_viewport = [0.5, 0.0, 1.0, 1.0]

    renderer_left = vtkRenderer()
    renderer_left.SetViewport(left_viewport)

    renderer_right = vtkRenderer()
    renderer_right.SetViewport(right_viewport)

    render_window = vtkRenderWindow()
    render_window.AddRenderer(renderer_left)
    render_window.AddRenderer(renderer_right)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(render_window)

    renderer_left.AddActor(iso_actor)
    renderer_right.AddActor(iso_smoothed_actor)

    renderer_left.GetActiveCamera().SetFocalPoint(0.0, 0.0, 0.0)
    renderer_left.GetActiveCamera().SetPosition(0.0, -1.0, 0.0)
    renderer_left.GetActiveCamera().SetViewUp(0.0, 0.0, -1.0)
    renderer_left.ResetCamera()
    renderer_left.GetActiveCamera().Azimuth(-20.0)
    renderer_left.GetActiveCamera().Elevation(20.0)
    renderer_left.ResetCameraClippingRange()

    renderer_left.SetBackground(colors.GetColor3d("SlateGray"))
    renderer_right.SetBackground(colors.GetColor3d("LightSlateGray"))
    renderer_right.SetActiveCamera(renderer_left.GetActiveCamera())

    render_window.SetSize(640, 480)
    render_window.SetWindowName('IsoSubsample')
    render_window.Render()

    render_window_interactor.Start()

def get_program_parameters():
    import argparse
    description = 'This figure demonstrates aliasing that occurs when a high-frequency signal is subsampled.'
    epilogue = '''
    High frequencies appear as low frequency artifacts.
    The left image is an isosurface of a skull after subsampling.
    The right image used a low-pass filter before subsampling to reduce aliasing.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
