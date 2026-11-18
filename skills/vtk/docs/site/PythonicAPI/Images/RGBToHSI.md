<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/RGBToHSI/ -->

# RGBToHSI

Repository source: [RGBToHSI](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/RGBToHSI.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestRGBToHSI.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestRGBToHSI.png?raw=true target=)

### Description

Convert RGB channels to HSI channels. See [this article](https://en.wikipedia.org/wiki/HSL_and_HSV) for a description of the HSI colormodel.

Seealso

[RGBToYIQ](RGBToYIQ.md) and [RGBToHSV](RGBToHSV.md)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/RGBToHSI/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RGBToHSI.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingColor import vtkImageRGBToHSI
from vtkmodules.vtkImagingCore import vtkImageExtractComponents
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
    description = 'RGBToHSI.'
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

    colors = vtkNamedColors()

    # Read the image.
    reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
    reader.file_name = fp

    # Alternatively, use vtkPNGReader.
    # reader = vtkJPEGReader(file_name = fp)

    hsi_filter = vtkImageRGBToHSI()

    extract_h_filter = vtkImageExtractComponents(components=0)
    extract_s_filter = vtkImageExtractComponents(components=1)
    extract_i_filter = vtkImageExtractComponents(components=2)

    # Create the actors.
    input_actor = vtkImageActor()
    reader >> input_actor.mapper

    h_actor = vtkImageActor()
    reader >> hsi_filter >> extract_h_filter >> h_actor.mapper

    s_actor = vtkImageActor()
    reader >> hsi_filter >> extract_s_filter >> s_actor.mapper

    i_actor = vtkImageActor()
    reader >> hsi_filter >> extract_i_filter >> i_actor.mapper

    # Define the viewport ranges (x_min, y_min, x_max, y_max).
    input_viewport = (0.0, 0.0, 0.25, 1.0)
    h_viewport = (0.25, 0.0, 0.5, 1.0)
    s_viewport = (0.5, 0.0, 0.75, 1.0)
    i_viewport = (0.75, 0.0, 1.0, 1.0)

    # Shared camera.
    shared_camera = vtkCamera()

    # Set up the renderers.
    input_renderer = vtkRenderer(viewport=input_viewport, background=colors.GetColor3d('CornflowerBlue'))
    input_renderer.AddActor(input_actor)
    input_renderer.active_camera = shared_camera

    h_renderer = vtkRenderer(viewport=h_viewport, background=colors.GetColor3d('MistyRose'))
    h_renderer.AddActor(h_actor)
    h_renderer.active_camera = shared_camera

    s_renderer = vtkRenderer(viewport=s_viewport, background=colors.GetColor3d('LavenderBlush'))
    s_renderer.AddActor(s_actor)
    s_renderer.active_camera = shared_camera

    i_renderer = vtkRenderer(viewport=i_viewport, background=colors.GetColor3d('Lavender'))
    i_renderer.AddActor(i_actor)
    i_renderer.active_camera = shared_camera

    # Setup render window.
    render_window = vtkRenderWindow(size=(1000, 250), window_name='RGBToHSI')
    render_window.AddRenderer(input_renderer)
    render_window.AddRenderer(h_renderer)
    render_window.AddRenderer(s_renderer)
    render_window.AddRenderer(i_renderer)
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
