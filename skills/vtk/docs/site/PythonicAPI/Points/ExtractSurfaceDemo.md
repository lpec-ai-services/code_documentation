<!-- source: https://examples.vtk.org/site/PythonicAPI/Points/ExtractSurfaceDemo/ -->

# ExtractSurfaceDemo

Repository source: [ExtractSurfaceDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Points/ExtractSurfaceDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestExtractSurfaceDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestExtractSurfaceDemo.png?raw=true target=)

### Description

This example loosely follows the most excellent paper by Curless and Levoy: ["A Volumetric Method for Building Complex Models from Range Images."](https://graphics.stanford.edu/papers/volrange). First it estimates normals from the points, then creates a signed distance field, followed by surface extraction of the zero-level set of the distance field.

This is a demo version of [ExtractSurface](ExtractSurface.md). It displays some sampling of the normals with arrows. It also uses a different color for the front and back surfaces.

The image was created using the Armadillo dataset, `src/Testing/Data/Armadillo.ply`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Points/ExtractSurfaceDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractSurfaceDemo.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkMinimalStandardRandomSequence
from vtkmodules.vtkFiltersCore import (
    vtkGlyph3D,
    vtkMaskPoints
)
from vtkmodules.vtkFiltersPoints import (
    vtkExtractSurface,
    vtkPCANormalEstimation,
    vtkSignedDistance
)
from vtkmodules.vtkFiltersSources import (
    vtkArrowSource,
    vtkPointSource
)
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
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Extract a surface from vtkPolyData points.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None,
                        help='The polydata source file name,e.g. Armadillo.ply.')
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
        poly_data = spherical_shell()

    print(f'Number of points: {poly_data.number_of_points}')

    bounds = poly_data.bounds
    pd_range = [0.0] * 3
    for i in range(0, len(pd_range)):
        pd_range[i] = bounds[2 * i + 1] - bounds[2 * i]

    sample_size = 15

    print(f'Sample size is: {sample_size}')
    # Do we need to estimate normals?
    distance = vtkSignedDistance()
    normals = None
    if poly_data.point_data.normals:
        print('Using normals from the input file')
        distance.SetInputData(poly_data)
    else:
        print('Estimating normals using PCANormalEstimation')
        normals = vtkPCANormalEstimation(input_data=poly_data, sample_size=sample_size, flip_normals=True)
        normals.SetNormalOrientationToGraphTraversal()
        normals >> distance

    print(f'Range: ({fmt_floats(pd_range)})')
    dimension = 512
    radius = pd_range[0] / dimension * 3.0  # ~3 voxels
    print(f'Radius: {radius:g}')

    distance.radius = radius
    distance.SetDimensions(dimension, dimension, dimension)
    distance.SetBounds(bounds[0] - pd_range[0] * 0.1, bounds[1] + pd_range[0] * 0.1,
                       bounds[2] - pd_range[1] * 0.1, bounds[3] + pd_range[1] * 0.1,
                       bounds[4] - pd_range[2] * 0.1, bounds[5] + pd_range[2] * 0.1)

    surface = vtkExtractSurface(radius=radius * 0.99, hole_filling=True)
    distance >> surface

    surface_mapper = vtkPolyDataMapper()
    distance >> surface >> surface_mapper

    colors = vtkNamedColors()

    back_prop = vtkProperty(color=colors.GetColor3d('Banana'))

    surface_actor = vtkActor(mapper=surface_mapper)
    surface_actor.property.color = colors.GetColor3d('Coral')
    surface_actor.backface_property = back_prop

    if poly_data.point_data.normals:
        glyph_3d = make_glyphs(poly_data, radius * 2.0)
    else:
        glyph_3d = make_glyphs(normals.output, radius * 2.0)

    glyph_3d_mapper = vtkPolyDataMapper()
    glyph_3d >> glyph_3d_mapper

    glyph_3d_actor = vtkActor(mapper=glyph_3d_mapper)
    glyph_3d_actor.property.color = colors.GetColor3d('MidnightBlue')

    # Create graphics stuff.
    ren = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name='ExtractSurfaceDemo')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer,set the background and size.
    ren.AddActor(surface_actor)
    ren.AddActor(glyph_3d_actor)

    # Generate an interesting view.
    ren.ResetCamera()
    ren.active_camera.Azimuth(120)
    ren.active_camera.Elevation(30)
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

def spherical_shell():
    """
    Random points on a spherical shell.

    :return: A PolyData of random points.
    """
    random_sequence = vtkMinimalStandardRandomSequence(seed=8775070)

    points = vtkPointSource(number_of_points=1000, radius=1.0)
    # Random position.
    x = random_sequence.GetRangeValue(-1.0, 1.0)
    random_sequence.Next()
    y = random_sequence.GetRangeValue(-1.0, 1.0)
    random_sequence.Next()
    z = random_sequence.GetRangeValue(-1.0, 1.0)
    random_sequence.Next()
    points.center = (x, y, z)
    points.SetDistributionToShell()
    return points.update().output

def make_glyphs(src, size, mask=True):
    """
    Make glyphs.

    :param src: The source polydata.
    :param size: Size of the arrow.
    :param mask: True of points are to be masked.
    :return: The glyphs.
    """

    # Source for the glyph filter.
    arrow = vtkArrowSource(tip_resolution=16, tip_length=0.3, tip_radius=0.1)

    # Input for the glyph filter.
    if mask:
        mask_pts = vtkMaskPoints(on_ratio=20, random_mode=True, input_data=src)
        glyph = vtkGlyph3D(source_connection=arrow.output_port, input_connection=mask_pts.output_port,
                           scale_mode=Glyph3D.ScaleMode.VTK_SCALE_BY_VECTOR, scale_factor=size, orient=True)
    else:
        glyph = vtkGlyph3D(source_connection=arrow.output_port, input_data=src,
                           scale_mode=Glyph3D.ScaleMode.VTK_SCALE_BY_VECTOR, scale_factor=size, orient=True)
    glyph.update()
    return glyph

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

@dataclass(frozen=True)
class Glyph3D:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_BY_SCALE: int = 0
        VTK_COLOR_BY_SCALAR: int = 1
        VTK_COLOR_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class IndexMode:
        VTK_INDEXING_OFF: int = 0
        VTK_INDEXING_BY_SCALAR: int = 1
        VTK_INDEXING_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class ScaleMode:
        VTK_SCALE_BY_SCALAR: int = 0
        VTK_SCALE_BY_VECTOR: int = 1
        VTK_SCALE_BY_VECTORCOMPONENTS: int = 2
        VTK_DATA_SCALING_OFF: int = 3

    @dataclass(frozen=True)
    class VectorMode:
        VTK_USE_VECTOR: int = 0
        VTK_USE_NORMAL: int = 1
        VTK_VECTOR_ROTATION_OFF: int = 2
        VTK_FOLLOW_CAMERA_DIRECTION: int = 3

if __name__ == '__main__':
    main()
```
