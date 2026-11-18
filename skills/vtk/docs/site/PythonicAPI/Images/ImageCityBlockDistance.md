<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageCityBlockDistance/ -->

# ImageCityBlockDistance

Repository source: [ImageCityBlockDistance](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageCityBlockDistance.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageCityBlockDistance.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageCityBlockDistance.png?raw=true target=)

### Description

Compute the Manhattan distance from every point to every black point in a binary image.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageCityBlockDistance/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageCityBlockDistance.py**

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
from vtkmodules.vtkImagingGeneral import vtkImageCityBlockDistance
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Center an image.'
    epilogue = '''
    Shift the image center to (0,0)
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The image file name to use e.g. Yinyang.jpg.')
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

    cast_filter = vtkImageCast()
    reader >> cast_filter
    cast_filter.SetOutputScalarTypeToShort()

    city_block_distance_filter = vtkImageCityBlockDistance(dimensionality=2)
    reader >> cast_filter >> city_block_distance_filter

    # Create actors.
    input_cast_filter = vtkImageCast()
    input_cast_filter.SetOutputScalarTypeToUnsignedChar()
    reader >> input_cast_filter

    input_actor = vtkImageActor()
    input_cast_filter >> input_actor.mapper

    distance_cast_filter = vtkImageCast()
    distance_cast_filter.SetOutputScalarTypeToUnsignedChar()
    city_block_distance_filter >> distance_cast_filter

    distance_actor = vtkImageActor()
    distance_cast_filter >> distance_actor.mapper

    # Define viewport ranges.(x_min, y_min, x_max, y_max).
    input_viewport = (0.0, 0.0, 0.5, 1.0)
    distance_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup renderers.
    input_renderer = vtkRenderer(viewport=input_viewport, background=colors.GetColor3d('CornflowerBlue'))
    input_renderer.AddActor(input_actor)

    distance_renderer = vtkRenderer(viewport=distance_viewport, background=colors.GetColor3d('LightSkyBlue'))
    distance_renderer.AddActor(distance_actor)

    # Setup render window.
    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageCityBlockDistance')

    render_window.AddRenderer(input_renderer)
    render_window.AddRenderer(distance_renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()

    render_window_interactor.interactor_style = style

    # Render and start interaction.
    render_window_interactor.render_window = render_window
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
