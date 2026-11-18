<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/RGBToYIQ/ -->

# RGBToYIQ

Repository source: [RGBToYIQ](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/RGBToYIQ.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestRGBToYIQ.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestRGBToYIQ.png?raw=true target=)

### Description

Convert RGB channels to YIQ channels. See [this article](https://en.wikipedia.org/wiki/YIQ) for a description of the YIQ colormodel.

Seealso

[RGBToHSV](RGBToHSV.md) and [RGBToHSI](RGBToHSI.md)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/RGBToYIQ/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RGBToYIQ.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingColor import vtkImageRGBToYIQ
from vtkmodules.vtkImagingCore import vtkImageExtractComponents, vtkImageCast
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkCamera,
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'RGBToYIQ.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The image file name to use e.g. Gourds.png.')
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

    # Convert data to float for conversion (YIQ is signed).
    cast = vtkImageCast()
    cast.SetOutputScalarTypeToFloat()

    yiq_filter = vtkImageRGBToYIQ()

    extract_y_filter = vtkImageExtractComponents(components=0)
    extract_i_filter = vtkImageExtractComponents(components=1)
    extract_q_filter = vtkImageExtractComponents(components=2)

    #  Cast back to unsigned char.
    y_cast = vtkImageCast()
    y_cast.SetOutputScalarTypeToUnsignedChar()

    i_cast = vtkImageCast()
    i_cast.SetOutputScalarTypeToUnsignedChar()

    q_cast = vtkImageCast()
    q_cast.SetOutputScalarTypeToUnsignedChar()

    # Create the actors.
    input_actor = vtkImageActor()
    reader >> input_actor.mapper

    y_actor = vtkImageActor()
    reader >> cast >> yiq_filter >> extract_y_filter >> y_cast >> y_actor.mapper

    i_actor = vtkImageActor()
    reader >> cast >> yiq_filter >> extract_i_filter >> i_cast >> i_actor.mapper

    q_actor = vtkImageActor()
    reader >> cast >> yiq_filter >> extract_q_filter >> q_cast >> q_actor.mapper

    # Define the viewport ranges.(x_min, y_min, x_max, y_max).
    input_viewport = (0.0, 0.0, 0.25, 1.0)
    y_viewport = (0.25, 0.0, 0.5, 1.0)
    i_viewport = (0.5, 0.0, 0.75, 1.0)
    q_viewport = (0.75, 0.0, 1.0, 1.0)

    # Shared camera.
    shared_camera = vtkCamera()

    # Set up the renderers.
    input_renderer = vtkRenderer(viewport=input_viewport, background=colors.GetColor3d('CornflowerBlue'))
    input_renderer.AddActor(input_actor)
    input_renderer.active_camera = shared_camera

    y_renderer = vtkRenderer(viewport=y_viewport, background=colors.GetColor3d('MistyRose'))
    y_renderer.AddActor(y_actor)
    y_renderer.active_camera = shared_camera

    i_renderer = vtkRenderer(viewport=i_viewport, background=colors.GetColor3d('LavenderBlush'))
    i_renderer.AddActor(i_actor)
    i_renderer.active_camera = shared_camera

    q_renderer = vtkRenderer(viewport=q_viewport, background=colors.GetColor3d('Lavender'))
    q_renderer.AddActor(q_actor)
    q_renderer.active_camera = shared_camera

    # Setup render window.
    render_window = vtkRenderWindow(size=(1000, 250), window_name='RGBToYIQ')
    render_window.AddRenderer(input_renderer)
    render_window.AddRenderer(y_renderer)
    render_window.AddRenderer(i_renderer)
    render_window.AddRenderer(q_renderer)
    input_renderer.ResetCamera()

    # Setup the render window interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style

    # Render and start the interaction.
    render_window_interactor.render_window = render_window
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
