<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/MassProperties/ -->

# MassProperties

Repository source: [MassProperties](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/MassProperties.py)

### Description

This example uses [vtkMassProperties](https://www.vtk.org/doc/nightly/html/classvtkMassProperties.html) to compute the volume of a closed mesh. [vtkMassProperties](https://www.vtk.org/doc/nightly/html/classvtkMassProperties.html) requires triangles with consistent ordering. This example uses [vtkFillHolesFilter](https://www.vtk.org/doc/nightly/html/classvtkFillHolesFilter.html) and [vtkTriangleFilter](https://www.vtk.org/doc/nightly/html/classvtkTriangleFilter.html) to ensure a closed, triangulated mesh. [vtkPolyDataNormals](https://www.vtk.org/doc/nightly/html/classvtkPolyDataNormals.html) enforces consistent normals.

If run with no arguments, a [vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html) generates the [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). Or given a file containing [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html), it computes that data's volume and surface area.

Cite

[Alyassin A.M. et al, "Evaluation of new algorithms for the interactive measurement of surface area and volume", Med Phys 21(6) 1994.](https://www.researchgate.net/profile/Abdalmajeid_Alyassin/publication/15264446_Evaluation_of_new_algorithms_for_the_interactive_measurement_of_surface_area_and_volume/links/5497dff10cf29b944826369a.pdf)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/MassProperties/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MassProperties.py**

```python
# !/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersCore import (
    vtkMassProperties,
    vtkPolyDataNormals,
    vtkTriangleFilter
)
from vtkmodules.vtkFiltersModeling import vtkFillHolesFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader

def get_program_parameters():
    import argparse
    description = 'Compute volume and surface area of a closed, triangulated mesh.'
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
            print(f'{file_name} not found.\nUsing a sphere instead.')
    if file_name is None or poly_data is None:
        source = vtkSphereSource(radius=0.5, phi_resolution=51, theta_resolution=51)
        poly_data = source.update().output

    fill_holes_filter = vtkFillHolesFilter(input_data=poly_data, hole_size=1000.0)
    triangle_filter = vtkTriangleFilter()

    # Make the triangle winding order consistent.
    normals = vtkPolyDataNormals(consistency=True, splitting=False)

    mass_properties = vtkMassProperties()
    fill_holes_filter >> triangle_filter >> normals >> mass_properties
    mass_properties.update()
    fmt = '8.6f'
    print(
        f'Volume: {mass_properties.volume:{fmt}}\n'
        f'    VolumeX: {mass_properties.volume_x:{fmt}}\n '
        f'   VolumeY: {mass_properties.volume_y:{fmt}}\n'
        f'    VolumeZ: {mass_properties.volume_z:{fmt}}\n'
        f'Area: {mass_properties.surface_area:{fmt}}\n'
        f'    MinCellArea: {mass_properties.min_cell_area:{fmt}}\n'
        f'    MaxCellArea: {mass_properties.max_cell_area:{fmt}}\n'
        f'NormalizedShapeIndex: {mass_properties.normalized_shape_index:{fmt}}')

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
        return reader.update().output
    else:
        return None

if __name__ == '__main__':
    main()
```
