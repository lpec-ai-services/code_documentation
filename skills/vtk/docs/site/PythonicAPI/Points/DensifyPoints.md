<!-- source: https://examples.vtk.org/site/PythonicAPI/Points/DensifyPoints/ -->

# DensifyPoints

Repository source: [DensifyPoints](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Points/DensifyPoints.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestDensifyPoints.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestDensifyPoints.png?raw=true target=)

### Description

In this example, the original points are yellow and the added points are red.

The image was produced using `src/Testing/Data/Torso.vtp`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Points/DensifyPoints/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DensifyPoints.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersPoints import vtkDensifyPointCloudFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkGlyph3DMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Densify points.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None,
                        help='The polydata source file name,e.g. Torso.vtp.')
    args = parser.parse_args()

    return args.file_name

def main():
    file_name = get_program_parameters()
    poly_data = None
    if file_name:
        if Path(file_name).is_file():
            poly_data = read_poly_data(file_name)
        else:
            print(f'{file_name} not found.')
    if file_name is None or poly_data is None:
        sphere_source = vtkSphereSource(center=(0, 0, 0), radius=1, theta_resolution=6, phi_resolution=6)
        poly_data = sphere_source.update().output

    bounds = poly_data.bounds
    data_range = list()
    for i in range(0, 3):
        data_range.append(bounds[2 * i + 1] - bounds[2 * i])

    print(f'Range: ({fmt_floats(data_range)})')
    max_range = max(max(data_range[0], data_range[1]), data_range[2])

    print(f'Number of original points:  {poly_data.number_of_points}')
    densify = vtkDensifyPointCloudFilter(input_data=poly_data, maximum_number_of_iterations=5,
                                         target_distance=max_range * 0.03, number_of_closest_points=10)
    densify.update()
    print(f'Number of densified points: {densify.output.number_of_points}')

    colors = vtkNamedColors()
    radius = max_range * 0.01
    sphere_source1 = vtkSphereSource(radius=radius)

    glyph_3d1 = vtkGlyph3DMapper(input_data=poly_data, source_data=sphere_source1.update().output,
                                 scalar_visibility=False, scaling=False)

    glyph_3d_actor1 = vtkActor(mapper=glyph_3d1)
    glyph_3d_actor1.property.color = colors.GetColor3d('Banana')

    sphere_source2 = vtkSphereSource()
    sphere_source2.SetRadius(radius * 0.75)
    sphere_source2.update()

    glyph_3d2 = vtkGlyph3DMapper(source_data=sphere_source2.update().output,
                                 scalar_visibility=False, scaling=False)
    densify >> glyph_3d2

    glyph_3d_actor2 = vtkActor(mapper=glyph_3d2)
    glyph_3d_actor2.property.color = colors.GetColor3d('Tomato')

    # Create the graphics stuff.
    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name='DensifyPoints')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer.
    ren.AddActor(glyph_3d_actor1)
    ren.AddActor(glyph_3d_actor2)

    # Generate an interesting view.
    ren.active_camera.position = (1, 0, 0)
    ren.active_camera.focal_point = (0, 1, 0)
    ren.active_camera.view_up = (0, 0, 1)
    ren.ResetCamera()
    ren.active_camera.Dolly(1.0)
    ren.ResetCameraClippingRange()

    ren_win.Render()
    iren.Initialize()
    iren.Start()

def read_poly_data(file_name):
    if not file_name:
        print(f'No file name.')
        return None

    valid_suffixes = ['.g', '.obj', '.stl', '.ply', '.vtk', '.vtp']
    path = Path(file_name)
    ext = None
    if path.suffix:
        ext = path.suffix.lower()
    if path.suffix not in valid_suffixes:
        print(f'No reader for this file suffix: {ext}')
        return None

    reader = None
    if ext == '.ply':
        reader = vtkPLYReader(file_name=file_name)
    elif ext == '.vtp':
        reader = vtkXMLPolyDataReader(file_name=file_name)
    elif ext == '.obj':
        reader = vtkOBJReader(file_name=file_name)
    elif ext == '.stl':
        reader = vtkSTLReader(file_name=file_name)
    elif ext == '.vtk':
        reader = vtkPolyDataReader(file_name=file_name)
    elif ext == '.g':
        reader = vtkBYUReader(file_name=file_name)

    if reader:
        reader.update()
        poly_data = reader.output
        return poly_data
    else:
        return None

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
