<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageProcessing/IsoSubsample/ -->

# IsoSubsample

Repository source: [IsoSubsample](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageProcessing/IsoSubsample.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageProcessing/TestIsoSubsample.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageProcessing/TestIsoSubsample.png?raw=true target=)

### Description

An artifact called aliasing occurs when sub-sampling and is often associated with stair-stepping edges. Sampling theory proves that discrete sampled signals with spacing S, completely describe continuous functions composed of frequencies less than S/2. When a signal is sub-sampled, its capacity to hold high frequency information is reduced. However, the high frequency energy does not disappear. It wraps around the frequency spectrum appearing as a low frequency alias artifact. The solution, which eliminates this artifact, is to low-pass filter before sub-sampling.

Low-pass smoothing reduces the high frequency range of an image that would cause aliasing. The same aliasing phenomena occurs when acquiring data. If a signal from an analog source contains high frequencies, saving the analog data in a discrete form requires sub-sampling that will introduce alias artifacts. For this reason, it is common practice to acquire data at high resolutions,then smooth and subsample to reduce the image to a manageable size.

This example demonstrates aliasing that occurs when a high-frequency signal is sub-sampled. High frequencies appear as low frequency artifacts. The left image is an isosurface of a skull after sub-sampling. The right image used a low-pass filter before sub-sampling to reduce aliasing.

Info

See [this figure](../../VTKBook/10Chapter10.md#Figure%2010-5) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/IsoSubsample/)), ([Python](../../Python/ImageProcessing/IsoSubsample.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IsoSubsample.py**

```python
#!/usr/bin/env python3

import sys
from pathlib import Path

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
    reader = vtkImageReader2Factory().CreateImageReader2(file_name)
    reader.file_name = file_name

    # Smoothed pipeline.
    smooth = vtkImageGaussianSmooth(dimensionality=3, standard_deviations=(1.75, 1.75, 0.0), radius_factor=2)

    subsample_smoothed = vtkImageShrink3D(shrink_factors=(4, 4, 1))

    iso_smoothed = vtkImageMarchingCubes()
    iso_smoothed.SetValue(0, 1150)

    iso_smoothed_mapper = vtkPolyDataMapper(scalar_visibility=False)
    reader >> smooth >> subsample_smoothed >> iso_smoothed >> iso_smoothed_mapper

    iso_smoothed_actor = vtkActor(mapper=iso_smoothed_mapper)
    iso_smoothed_actor.SetMapper(iso_smoothed_mapper)
    iso_smoothed_actor.property.color = colors.GetColor3d('Ivory')

    # Unsmoothed pipeline.
    # Subsample the data.
    subsample = vtkImageShrink3D(shrink_factors=(4, 4, 1))

    iso = vtkImageMarchingCubes()
    iso.SetValue(0, 1150)

    iso_mapper = vtkPolyDataMapper(scalar_visibility=False)
    reader >> subsample >> iso >> iso_mapper

    iso_actor = vtkActor(mapper=iso_mapper)
    iso_actor.property.color = colors.GetColor3d('Ivory')

    # The rendering Pipeline.

    # Set up the render window, renderer, and interactor.
    left_viewport = [0.0, 0.0, 0.5, 1.0]
    right_viewport = [0.5, 0.0, 1.0, 1.0]

    renderer_left = vtkRenderer(background=colors.GetColor3d('SlateGray'), viewport=left_viewport)
    renderer_left.AddActor(iso_actor)

    renderer_right = vtkRenderer(background=colors.GetColor3d('LightSlateGray'), viewport=right_viewport)
    renderer_right.AddActor(iso_smoothed_actor)

    render_window = vtkRenderWindow(size=(640, 480), window_name=f'{Path(sys.argv[0]).stem:s}')
    render_window.AddRenderer(renderer_left)
    render_window.AddRenderer(renderer_right)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer_left.active_camera.focal_point = (0.0, 0.0, 0.0)
    renderer_left.active_camera.position = (0.0, -1.0, 0.0)
    renderer_left.active_camera.view_up = (0.0, 0.0, 1.0)
    renderer_left.ResetCamera()
    renderer_left.active_camera.Azimuth(-20.0)
    renderer_left.active_camera.Elevation(20.0)
    renderer_left.active_camera.Dolly(1.5)
    renderer_left.ResetCameraClippingRange()

    renderer_right.active_camera = renderer_left.active_camera

    render_window.Render()

    render_window_interactor.Start()

def get_program_parameters():
    import argparse
    description = 'Demonstrate aliasing that occurs when a high-frequency signal is subsampled.'
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
