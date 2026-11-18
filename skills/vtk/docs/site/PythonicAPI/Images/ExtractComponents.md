<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ExtractComponents/ -->

# ExtractComponents

Repository source: [ExtractComponents](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ExtractComponents.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestExtractComponents.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestExtractComponents.png?raw=true target=)

### Description

This example separates an image into the red channel, the green channel, and the blue channel using [vtkImageExtractComponents](https://www.vtk.org/doc/nightly/html/classvtkImageExtractComponents.html).

Seealso

For the reverse operation, see [CombiningRGBChannels](CombiningRGBChannels.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ExtractComponents/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractComponents.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import vtkImageExtractComponents
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Extract components of an image.'
    epilogue = '''
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

    # Read the image.
    reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
    reader.file_name = fp

    colors = vtkNamedColors()

    extract_red_filter = vtkImageExtractComponents(components=0)
    extract_green_filter = vtkImageExtractComponents(components=1)
    extract_blue_filter = vtkImageExtractComponents(components=2)

    # Create the actors.
    input_actor = vtkImageActor()
    reader >> input_actor.mapper

    red_actor = vtkImageActor()
    reader >> extract_red_filter >> red_actor.mapper

    green_actor = vtkImageActor()
    reader >> extract_green_filter >> green_actor.mapper

    blue_actor = vtkImageActor()
    reader >> extract_blue_filter >> blue_actor.mapper

    # Define the viewport ranges (xmin, ymin, xmax, ymax).
    red_viewport = (0.0, 0.0, 0.25, 1.0)
    green_viewport = (0.25, 0.0, 0.5, 1.0)
    blue_viewport = (0.5, 0.0, 0.75, 1.0)
    combined_viewport = (0.75, 0.0, 1.0, 1.0)

    # Set up the renderers.
    red_renderer = vtkRenderer(background=colors.GetColor3d('Tomato'))
    red_renderer.viewport = red_viewport
    red_renderer.AddActor(red_actor)

    green_renderer = vtkRenderer(background=colors.GetColor3d('Mint'))
    green_renderer.viewport = green_viewport
    green_renderer.AddActor(green_actor)

    blue_renderer = vtkRenderer(background=colors.GetColor3d('Peacock'))
    blue_renderer.viewport = blue_viewport
    blue_renderer.AddActor(blue_actor)

    combined_renderer = vtkRenderer(background=colors.GetColor3d('DarkGray'))
    combined_renderer.viewport = combined_viewport
    combined_renderer.AddActor(input_actor)

    # Set up the render window.
    render_window = vtkRenderWindow(window_name='CombiningRGBChannels')
    render_window.size = (1000, 250)
    render_window.AddRenderer(red_renderer)
    render_window.AddRenderer(green_renderer)
    render_window.AddRenderer(blue_renderer)
    render_window.AddRenderer(combined_renderer)

    # Set up the render window interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style
    render_window_interactor.render_window = render_window

    # Render and start interaction.
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
