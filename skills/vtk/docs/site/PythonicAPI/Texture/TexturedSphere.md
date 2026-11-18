<!-- source: https://examples.vtk.org/site/PythonicAPI/Texture/TexturedSphere/ -->

# TexturedSphere

Repository source: [TexturedSphere](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Texture/TexturedSphere.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Texture/TestTexturedSphere.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Texture/TestTexturedSphere.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Texture/TexturedSphere/)), ([Java](https://examples.vtk.org/site/Java/Texture/TexturedSphere/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TexturedSphere.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkTexturedSphereSource
from vtkmodules.vtkFiltersTexture import vtkTransformTextureCoords
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTexture,
)

def get_program_parameters():
    def to_float_range(x):
        try:
            x = float(x)
        except ValueError:
            raise argparse.ArgumentTypeError(f'This value: {x} is not a floating-point literal')
        if abs(x) < 0.0 or abs(x) > 1.0:
            raise argparse.ArgumentTypeError(f'The absolute value of {x} must be in the range [0...1]')
        return x

    import argparse
    description = 'TexturedSphere.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The texture(.png/.ppm) file name to use e.g. earth.ppm.')
    parser.add_argument('-t', '--translate', type=to_float_range, default=0.25, help='Translation for the x-direction.')
    args = parser.parse_args()
    return args.file_name, args.translate

def main():
    translate = [0.0] * 3

    fn, translate[0] = get_program_parameters()
    fp = Path(fn)
    file_check = True
    if not fp.is_file():
        print(f'Missing image file: {fp}.')
        file_check = False
    elif not fp.suffix.lower() in ['.ppm', '.png']:
        file_check = False
        print(f'Bad extension: only .ppm or .png extensions are allowed.')
    if not file_check:
        return

    print(f'Translate: ({fmt_floats(translate)})')
    colors = vtkNamedColors()

    # Create a sphere with texture coordinates
    source = vtkTexturedSphereSource(theta_resolution=100, phi_resolution=100)

    # Read texture file.
    reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
    reader.file_name = fp

    # Create the texture.
    texture = vtkTexture()
    reader >> texture

    transform_texture = vtkTransformTextureCoords(position=translate)

    mapper = vtkPolyDataMapper()
    source >> transform_texture >> mapper

    actor = vtkActor(mapper=mapper, texture=texture)

    renderer = vtkRenderer(background=colors.GetColor3d('Black'))
    renderer.AddActor(actor)

    render_window = vtkRenderWindow(window_name='TexturedSphere')
    render_window.AddRenderer(renderer)

    renderer.ResetCamera()
    # Orient so we are directly above Null Island!
    # The location is at (0°N 0°E), i.e., where the
    #  prime meridian and the equator intersect.
    renderer.active_camera.Elevation(-90)

    ren_win_interactor = vtkRenderWindowInteractor()
    ren_win_interactor.render_window = render_window

    render_window.Render()
    ren_win_interactor.Start()

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
