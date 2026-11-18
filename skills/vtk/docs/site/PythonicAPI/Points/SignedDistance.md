<!-- source: https://examples.vtk.org/site/PythonicAPI/Points/SignedDistance/ -->

# SignedDistance

Repository source: [SignedDistance](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Points/SignedDistance.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestSignedDistance.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestSignedDistance.png?raw=true target=)

### Description

Contrast this with the [UnsignedDistance](UnsignedDistance.md) example.

The image was created using the Armadillo dataset, `src/Testing/Data/Armadillo.ply`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Points/SignedDistance/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SignedDistance.py**

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
from vtkmodules.vtkCommonCore import (
    vtkLookupTable,
    vtkMinimalStandardRandomSequence
)
from vtkmodules.vtkFiltersPoints import (
    vtkPCANormalEstimation,
    vtkSignedDistance
)
from vtkmodules.vtkFiltersSources import (
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
from vtkmodules.vtkImagingCore import vtkImageMapToColors
from vtkmodules.vtkRenderingAnnotation import vtkScalarBarActor
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Signed distance.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None, help='A polydata file e.g. Armadillo.ply.')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()
    if file_name:
        fn = Path(file_name)
        if fn.is_file():
            poly_data = read_poly_data(Path(file_name))
        else:
            print('File not found using random points instead.')
            poly_data = random_points()
    else:
        poly_data = random_points()

    bounds = poly_data.bounds
    ranges = list()
    for i in range(0, 3):
        ranges.append(bounds[2 * i + 1] - bounds[2 * i])

    sample_size = poly_data.number_of_points * 0.00005
    if sample_size < 10:
        sample_size = 10

    dimension = 128
    radius = ranges[0] / dimension * 5.0  # ~5 voxels
    print(f'Sample size is: {sample_size}')
    print(f'Range: ({fmt_floats(ranges, 0, 4)})')
    print(f'Radius: {radius:0.6f}')

    normals = vtkPCANormalEstimation(input_data=poly_data, sample_size=sample_size, flip_normals=True)
    normals.SetNormalOrientationToGraphTraversal()

    adjusted_bounds = list()
    for i in range(0, len(bounds)):
        if i % 2 == 0:
            adjusted_bounds.append(bounds[i] - ranges[i // 2] * 0.1)
        else:
            adjusted_bounds.append(bounds[i] + ranges[i // 2] * 0.1)
    dimensions = [dimension] * 3
    distance = vtkSignedDistance(radius=radius, dimensions=dimensions, bounds=adjusted_bounds)
    normals >> distance
    distance.update()
    print(f'Scalar range: ({fmt_floats(distance.output.scalar_range, 0, 6)})')

    hue_lut = hsv_lut(radius)

    sagittal_colors = vtkImageMapToColors(lookup_table=hue_lut)
    distance >> sagittal_colors

    saggital_dimensions = list(map(int, (dimension // 2, dimension // 2, 0, dimension - 1, 0, dimension - 1)))
    sagittal = vtkImageActor(display_extent=saggital_dimensions, force_opaque=True)
    sagittal_colors >> sagittal.mapper

    axial_colors = vtkImageMapToColors(lookup_table=hue_lut)
    distance >> axial_colors

    axial_dimensions = list(map(int, (0, dimension - 1, 0, dimension - 1, dimension // 2, dimension // 2)))
    axial = vtkImageActor(display_extent=axial_dimensions, force_opaque=True)
    axial_colors >> axial.mapper

    coronal_colors = vtkImageMapToColors(lookup_table=hue_lut)
    distance >> coronal_colors

    coronal_dimensions = list(map(int, (0, dimension - 1, dimension // 2, dimension // 2, 0, dimension - 1)))
    coronal = vtkImageActor(display_extent=coronal_dimensions, force_opaque=True)
    coronal_colors >> coronal.mapper

    # Create a scalar bar.
    scalar_bar = vtkScalarBarActor(lookup_table=hue_lut, title='Distance',
                                   number_of_labels=5)

    # Create a ren, render window, and interactor.
    ren = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'))
    ren_win = vtkRenderWindow(size=(600, 400), window_name='SignedDistance')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the ren.
    ren.AddActor(sagittal)
    ren.AddActor(axial)
    ren.AddActor(coronal)
    ren.AddViewProp(scalar_bar)

    # Generate an interesting view.
    ren.ResetCamera()
    ren.active_camera.Azimuth(120)
    ren.active_camera.Elevation(30)
    ren.active_camera.Dolly(1.5)
    ren.ResetCameraClippingRange()

    # Render and interact
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

def random_points():
    random_sequence = vtkMinimalStandardRandomSequence(seed=8775070)

    # random position
    x = random_sequence.GetRangeValue(-100, 100)
    random_sequence.Next()
    y = random_sequence.GetRangeValue(-100, 100)
    random_sequence.Next()
    z = random_sequence.GetRangeValue(-100, 100)
    random_sequence.Next()

    points = vtkPointSource(number_of_points=100000, radius=10.0, center=(x, y, z),
                            distribution=PointSource.Distribution.VTK_POINT_SHELL)
    return points.update().output

def fmt_floats(v, w=0, d=6, pt='f'):
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

def hsv_lut(radius):
    colors = vtkNamedColors()
    # Create a lookup table that consists of the full hue circle (from HSV).
    below_range_color = colors.GetColor4d('Black')
    below_range_color[3] = 0.2
    above_range_color = colors.GetColor4d('White')
    above_range_color[3] = 0.2
    lut = vtkLookupTable(table_range=(-0.99 * radius, 0.99 * radius),
                         hue_range=(0.667, 0), saturation_range=(1, 1), value_range=(1, 1),
                         use_below_range_color=True, below_range_color=below_range_color,
                         use_above_range_color=True, above_range_color=above_range_color,
                         number_of_colors=5)
    lut.Build()
    last = lut.GetTableValue(4)
    lut.SetAboveRangeColor(last[0], last[1], last[2], 0)
    return lut

@dataclass(frozen=True)
class PointSource:
    @dataclass(frozen=True)
    class Distribution:
        VTK_POINT_SHELL: int = 0
        VTK_POINT_UNIFORM: int = 1
        VTK_POINT_EXPONENTIAL: int = 2

if __name__ == '__main__':
    main()
```
