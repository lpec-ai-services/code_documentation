<!-- source: https://examples.vtk.org/site/Python/ImageProcessing/MedianComparison/ -->

# MedianComparison

Repository source: [MedianComparison](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImageProcessing/MedianComparison.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestMedianComparison.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestMedianComparison.png?raw=true target=)

### Description

Comparison of Gaussian and Median smoothing for reducing low-probability high-amplitude noise.

Info

See [this figure](../../VTKBook/10Chapter10.md#Figure%2010-3) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/MedianComparison/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MedianComparison.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import (
    vtkImageBinaryThreshold,
    vtkImageCast
)
from vtkmodules.vtkImagingGeneral import (
    vtkImageGaussianSmooth,
    vtkImageMedian3D
)
from vtkmodules.vtkImagingMath import vtkImageMathematics
from vtkmodules.vtkImagingSources import vtkImageNoiseSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    # colors = vtkNamedColors()

    file_name = get_program_parameters()

    # Read the image.
    readerFactory = vtkImageReader2Factory()
    reader = readerFactory.CreateImageReader2(file_name)
    reader.SetFileName(file_name)
    reader.Update()

    scalar_range = [0] * 2
    scalar_range[0] = reader.GetOutput().GetPointData().GetScalars().GetRange()[0]
    scalar_range[1] = reader.GetOutput().GetPointData().GetScalars().GetRange()[1]
    print("Range:", scalar_range)
    middle_slice = (reader.GetOutput().GetExtent()[5] - reader.GetOutput().GetExtent()[4]) // 2

    # Work with double images
    cast = vtkImageCast()
    cast.SetInputConnection(reader.GetOutputPort())
    cast.SetOutputScalarTypeToDouble()
    cast.Update()

    original_data = vtkImageData()
    original_data.DeepCopy(cast.GetOutput())

    noisyData = vtkImageData()

    add_shot_noise(original_data, noisyData, 2000.0, 0.1, reader.GetOutput().GetExtent())
    median = vtkImageMedian3D()
    median.SetInputData(noisyData)
    median.SetKernelSize(5, 5, 1)

    gaussian = vtkImageGaussianSmooth()
    gaussian.SetDimensionality(2)
    gaussian.SetInputData(noisyData)
    gaussian.SetStandardDeviations(2.0, 2.0)
    gaussian.SetRadiusFactors(2.0, 2.0)

    color_window = (scalar_range[1] - scalar_range[0]) * 0.8
    color_level = color_window / 2
    original_actor = vtkImageActor()
    original_actor.GetMapper().SetInputData(original_data)
    original_actor.GetProperty().SetColorWindow(color_window)
    original_actor.GetProperty().SetColorLevel(color_level)
    original_actor.GetProperty().SetInterpolationTypeToNearest()
    original_actor.SetZSlice(middle_slice)

    noisy_actor = vtkImageActor()
    noisy_actor.GetMapper().SetInputData(noisyData)
    noisy_actor.GetProperty().SetColorWindow(color_window)
    noisy_actor.GetProperty().SetColorLevel(color_level)
    noisy_actor.GetProperty().SetInterpolationTypeToNearest()
    noisy_actor.SetZSlice(middle_slice)

    gaussian_actor = vtkImageActor()
    gaussian_actor.GetMapper().SetInputConnection(gaussian.GetOutputPort())
    gaussian_actor.GetProperty().SetColorWindow(color_window)
    gaussian_actor.GetProperty().SetColorLevel(color_level)
    gaussian_actor.GetProperty().SetInterpolationTypeToNearest()
    gaussian_actor.SetZSlice(middle_slice)

    median_actor = vtkImageActor()
    median_actor.GetMapper().SetInputConnection(median.GetOutputPort())
    median_actor.GetProperty().SetColorWindow(color_window)
    median_actor.GetProperty().SetColorLevel(color_level)
    median_actor.GetProperty().SetInterpolationTypeToNearest()
    median_actor.SetZSlice(middle_slice)

    # Setup the renderers.
    original_renderer = vtkRenderer()
    original_renderer.AddActor(original_actor)
    noisy_renderer = vtkRenderer()
    noisy_renderer.AddActor(noisy_actor)
    gauss_renderer = vtkRenderer()
    gauss_renderer.AddActor(gaussian_actor)
    median_renderer = vtkRenderer()
    median_renderer.AddActor(median_actor)

    renderers = list()
    renderers.append(original_renderer)
    renderers.append(noisy_renderer)
    renderers.append(gauss_renderer)
    renderers.append(median_renderer)

    # Setup viewports for the renderers.
    renderer_size = 400
    x_grid_dimensions = 2
    y_grid_dimensions = 2

    render_window = vtkRenderWindow()
    render_window.SetSize(
        renderer_size * x_grid_dimensions, renderer_size * y_grid_dimensions)
    for row in range(0, y_grid_dimensions):
        for col in range(x_grid_dimensions):
            index = row * x_grid_dimensions + col
            # (xmin, ymin, xmax, ymax)
            viewport = [float(col) / x_grid_dimensions, float(y_grid_dimensions - (row + 1)) / y_grid_dimensions,
                        float(col + 1) / x_grid_dimensions, float(y_grid_dimensions - row) / y_grid_dimensions]
            renderers[index].SetViewport(viewport)
            render_window.AddRenderer(renderers[index])
    render_window.SetWindowName('MedianComparison')

    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()

    render_window_interactor.SetInteractorStyle(style)
    render_window_interactor.SetRenderWindow(render_window)

    # The renderers share one camera.
    render_window.Render()
    renderers[0].GetActiveCamera().Dolly(1.5)
    renderers[0].ResetCameraClippingRange()
    for r in range(1, len(renderers)):
        renderers[r].SetActiveCamera(renderers[0].GetActiveCamera())
    render_window_interactor.Initialize()
    render_window_interactor.Start()

def get_program_parameters():
    import argparse
    description = 'Comparison of Gaussian and Median smoothing for reducing low-probability high-amplitude noise.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    args = parser.parse_args()
    return args.filename

def add_shot_noise(input_image, output_image, noise_amplitude, noise_fraction, extent):
    shot_noise_source = vtkImageNoiseSource()
    shot_noise_source.SetWholeExtent(extent)
    shot_noise_source.SetMinimum(0.0)
    shot_noise_source.SetMaximum(1.0)

    shot_noise_thresh_1 = vtkImageBinaryThreshold()
    shot_noise_thresh_1.SetInputConnection(shot_noise_source.GetOutputPort())
    shot_noise_thresh_1.SetThresholdFunction(vtkImageBinaryThreshold.THRESHOLD_UPPER)
    shot_noise_thresh_1.SetLowerThreshold(1.0 - noise_fraction)
    shot_noise_thresh_1.ReplaceInOn()
    shot_noise_thresh_1.ReplaceOutOn()
    shot_noise_thresh_1.SetInValue(0)
    shot_noise_thresh_1.SetOutValue(noise_amplitude)

    shot_noise_thresh_2 = vtkImageBinaryThreshold()
    shot_noise_thresh_2.SetInputConnection(shot_noise_source.GetOutputPort())
    shot_noise_thresh_2.SetThresholdFunction(vtkImageBinaryThreshold.THRESHOLD_UPPER)
    shot_noise_thresh_2.SetLowerThreshold(noise_fraction)
    shot_noise_thresh_2.ReplaceInOn()
    shot_noise_thresh_2.ReplaceOutOn()
    shot_noise_thresh_2.SetInValue(1.0 - noise_amplitude)
    shot_noise_thresh_2.SetOutValue(0.0)

    shot_noise = vtkImageMathematics()
    shot_noise.SetInputConnection(0, shot_noise_thresh_1.GetOutputPort())
    shot_noise.SetInputConnection(1, shot_noise_thresh_2.GetOutputPort())
    shot_noise.SetOperationToAdd()

    add = vtkImageMathematics()
    add.SetInputData(0, input_image)
    add.SetInputConnection(1, shot_noise.GetOutputPort())
    add.SetOperationToAdd()
    add.Update()
    output_image.DeepCopy(add.GetOutput())

if __name__ == '__main__':
    main()
```
