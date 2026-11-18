<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageHistogram/ -->

# ImageHistogram

Repository source: [ImageHistogram](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageHistogram.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageHistogram.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageHistogram.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageHistogram/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageHistogram.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingStatistics import vtkImageHistogram
from vtkmodules.vtkRenderingCore import (
    vtkImageSlice,
    vtkImageSliceMapper,
    vtkInteractorStyle,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'ImageHistogram.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='The file to use e.g. Pileated.jpg.')
    args = parser.parse_args()
    return args.filename

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
    reader.update()

    iren = vtkRenderWindowInteractor()
    style = vtkInteractorStyle()
    ren_win = vtkRenderWindow(size=(640, 480), window_name='ImageHistogram')
    iren.render_window = ren_win
    iren.interactor_style = style

    histogram = vtkImageHistogram(generate_histogram_image=True, histogram_image_size=(256, 256),
                                  automatic_binning=True, input_connection=reader.output_port)
    reader >> histogram
    histogram.SetHistogramImageScaleToSqrt()
    histogram.update()

    nbins = histogram.number_of_bins
    bin_range = list()
    bin_range.append(histogram.bin_origin)
    bin_range.append(bin_range[0] + (nbins - 1) * histogram.bin_spacing)

    for i in range(0, len(bin_range)):
        viewport = [0.5 * (i and 1), 0.0, 0.5 + 0.5 * (i and 1), 1.0]
        renderer = vtkRenderer(viewport=viewport)
        camera = renderer.active_camera
        ren_win.AddRenderer(renderer)

        image_mapper = vtkImageSliceMapper()
        # Compute the y range.
        if i == 0:
            reader >> image_mapper
            extent = reader.output.extent
        else:
            histogram >> image_mapper
            image_mapper.BorderOn()
            extent = histogram.output.extent
        dy = extent[3] - extent[2] + 1

        bounds = image_mapper.bounds
        point = list()
        for j in range(0, 6, 2):
            point.append(0.5 * (bounds[j] + bounds[j + 1]))

        camera.focal_point = point
        point[image_mapper.GetOrientation()] += 1000
        camera.position = point
        camera.view_up = (0.0, 1.0, 0.0)
        camera.ParallelProjectionOn()
        # Set scale so that vertical dimension fills the window.
        camera.parallel_scale = 0.5 * dy

        image = vtkImageSlice()
        image.mapper = image_mapper

        renderer.AddViewProp(image)

        if i == 0:
            image.property.color_level = bin_range[1] - bin_range[0]
            image.property.color_level = 0.5 * (bin_range[0] + bin_range[1])
        else:
            image.property.SetInterpolationTypeToNearest()
            image.property.color_window = 255.0
            image.property.color_level = 127.5

    iren.Initialize()
    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
