<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ImplicitDataSetClipping/ -->

# ImplicitDataSetClipping

Repository source: [ImplicitDataSetClipping](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ImplicitDataSetClipping.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestImplicitDataSetClipping.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestImplicitDataSetClipping.png?raw=true target=)

### Description

This example demonstrates how to clip one object with another.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ImplicitDataSetClipping/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImplicitDataSetClipping.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkBox
from vtkmodules.vtkFiltersCore import (
    vtkClipPolyData,
    vtkGenerateIds
)
from vtkmodules.vtkFiltersSources import (
    vtkCubeSource,
    vtkSphereSource
)
from vtkmodules.vtkIOLegacy import vtkDataSetWriter
from vtkmodules.vtkIOXML import vtkXMLPolyDataWriter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Implicit Data Set Clipping.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-o', '--output_files', action='store_false',
                        help='Write out the vtk files.')
    args = parser.parse_args()
    return args.output_files

def main():
    output_files = get_program_parameters()

    colors = vtkNamedColors()

    # colors.color = 'Bkg', 0.2, 0.3, 0.4)

    res = 10
    sphere_source = vtkSphereSource(center=(0.75, 0.0, 0.0), theta_resolution=res, phi_resolution=res)
    sphere_source.update()

    print(
        f'The sphere has {sphere_source.output.number_of_points} points'
        f' and {sphere_source.output.number_of_cells} cells.')

    # Add ids to the points and cells of the sphere.
    cell_id_filter = vtkGenerateIds(cell_ids_array_name='CellIds', cell_ids=True, point_ids=False)
    sphere_source >> cell_id_filter
    cell_id_filter.update()

    if output_files:
        write_data_set(cell_id_filter.output, 'IDSCellIdFilter.vtp')

    point_id_filter = vtkGenerateIds(point_ids_array_name='PointIds', cell_ids=False, point_ids=True)
    cell_id_filter >> point_id_filter
    point_id_filter.update()

    sphere_with_ids = point_id_filter.output

    if output_files:
        write_data_set(sphere_with_ids, 'IDSBothIdFilter.vtp')

    cube_source = vtkCubeSource()
    cube_source.Update()

    implicit_cube = vtkBox()
    implicit_cube.SetBounds(cube_source.output.bounds)

    clipper = vtkClipPolyData(clip_function=implicit_cube, input_data=sphere_with_ids, inside_out=True)
    clipper.update()

    if output_files:
        write_data_set(clipper.output, 'IDSClipper.vtp')

    # Get the clipped cell ids.
    clipped = clipper.GetOutput()

    print(f'There are {clipped.number_of_points} clipped points.')
    print(f'There are {clipped.number_of_cells} clipped cells.')

    clipped_cell_ids = clipped.GetCellData().GetArray('CellIds')

    for i in range(0, clipped_cell_ids.number_of_tuples):
        print(f'Clipped cell id {i:3d}: {clipped_cell_ids.GetValue(i)}')

    # Create a mapper and actor for clipped sphere.
    clipped_mapper = vtkPolyDataMapper(scalar_visibility=False)
    clipper >> clipped_mapper

    clipped_actor = vtkActor(mapper=clipped_mapper)
    clipped_actor.property.representation = Property.Representation.VTK_WIREFRAME
    clipped_actor.property.color = colors.GetColor3d('Yellow')

    # Create a mapper and actor for cube.
    cube_mapper = vtkPolyDataMapper()
    cube_source >> cube_mapper

    cube_actor = vtkActor(mapper=cube_mapper)
    cube_actor.property.representation = Property.Representation.VTK_WIREFRAME
    cube_actor.property.opacity = 0.5
    cube_actor.property.color = colors.GetColor3d('Blue')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='ImplicitDataSetClipping')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actor to the scene.
    renderer.AddActor(clipped_actor)
    renderer.AddActor(cube_actor)

    # Generate an interesting view.
    renderer.ResetCamera()
    renderer.active_camera.Azimuth(-30)
    renderer.active_camera.Elevation(30)
    renderer.active_camera.Dolly(1.0)
    renderer.ResetCameraClippingRange()

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

def write_poly_data(poly_data, filename):
    writer = vtkXMLPolyDataWriter(file_name=filename, input_data=poly_data)
    writer.Write()

def write_data_set(data_set, filename):
    writer = vtkDataSetWriter(file_name=filename, input_data=data_set)
    writer.Write()

@dataclass(frozen=True)
class Property:
    @dataclass(frozen=True)
    class Interpolation:
        VTK_FLAT: int = 0
        VTK_GOURAUD: int = 1
        VTK_PHONG: int = 2
        VTK_PBR: int = 3

    @dataclass(frozen=True)
    class Representation:
        VTK_POINTS: int = 0
        VTK_WIREFRAME: int = 1
        VTK_SURFACE: int = 2

if __name__ == '__main__':
    main()
```
