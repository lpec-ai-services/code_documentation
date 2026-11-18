<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/IdentifyHoles/ -->

# IdentifyHoles

Repository source: [IdentifyHoles](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/IdentifyHoles.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestIdentifyHoles.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestIdentifyHoles.png?raw=true target=)

### Description

This example fills the holes in a mesh and then extracts the filled holes as seprate regions.

The example proceeds as follows:

1. Read the polydata.
2. Fill the holes with [vtkFillHolesFilter](https://www.vtk.org/doc/nightly/html/classvtkFillHolesFilter.html).
3. Create a new polydata that contains the filled holes. To do this we rely on the fact that the fill holes filter stores the original cells first and then adds the new cells that fill the holes. Using [vtkCellIterator](https://www.vtk.org/doc/nightly/html/classvtkCellIterator.html), we skip the original cells and then continue iterating to obtain the new cells.
4. Use [vtkConnectivityFilter](https://www.vtk.org/doc/nightly/html/classvtkConnectivityFilter.html) on the filled polydata to identify the individual holes.

Note

We have to use vtkConnectivtyFilter and not [vtkPolyDataConnectivityFilter](https://www.vtk.org/doc/nightly/html/classvtkPolyDataConnectivityFilter.html) since the later does not create RegionIds cell data.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/IdentifyHoles/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IdentifyHoles.py**

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
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkIdTypeArray
from vtkmodules.vtkCommonDataModel import (
    vtkGenericCell,
    vtkPolyData,
    vtkSelection,
    vtkSelectionNode
)
from vtkmodules.vtkFiltersCore import (
    vtkConnectivityFilter,
    vtkPolyDataNormals
)
from vtkmodules.vtkFiltersExtraction import vtkExtractSelection
from vtkmodules.vtkFiltersGeometry import vtkDataSetSurfaceFilter
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
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Close holes in a mesh and identify the holes.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None,
                        help='The polydata source file name,e.g. Torso.vtp.')
    args = parser.parse_args()

    return args.file_name

def main():
    restore_original_normals = True

    colors = vtkNamedColors()

    file_name = get_program_parameters()
    poly_data = None
    if file_name:
        if Path(file_name).is_file():
            poly_data = read_poly_data(file_name)
        else:
            print(f'{file_name} not found.')
    if file_name is None or poly_data is None:
        poly_data = generate_data()

    fill_holes_filter = vtkFillHolesFilter(input_data=poly_data, hole_size=1000.0)
    fill_holes_filter.update()

    # Make the triangle winding order consistent.
    normals = vtkPolyDataNormals(input_data=fill_holes_filter.output, consistency=True, splitting=False)

    if restore_original_normals:
        # Restore the original normals.
        normals.update().output.point_data.SetNormals(poly_data.point_data.normals)

    # Determine the number of added cells.
    num_original_cells = poly_data.number_of_cells
    num_new_cells = normals.output.number_of_cells

    # Iterate over the original cells.
    it = normals.output.NewCellIterator()
    it.InitTraversal()
    numCells = 0
    while not it.IsDoneWithTraversal() and numCells < num_original_cells:
        it.GoToNextCell()
        numCells += 1
    print(
        f'Num original: {num_original_cells}, Num new: {num_new_cells}, Num added: {num_new_cells - num_original_cells}')

    hole_poly_data = vtkPolyData(points=normals.output.points)
    hole_poly_data.Allocate(normals.output, num_new_cells - num_original_cells)

    # The remaining cells are the new ones from the hole filler.
    cell = vtkGenericCell()
    while not it.IsDoneWithTraversal():
        it.GetCell(cell)
        hole_poly_data.InsertNextCell(it.GetCellType(), cell.GetPointIds())
        it.GoToNextCell()

    # We have to use ConnectivityFilter and not
    # PolyDataConnectivityFilter since the latter does not create
    # RegionIds cell data.
    connectivity = vtkConnectivityFilter(input_data=hole_poly_data, color_regions=True)
    connectivity.SetExtractionModeToAllRegions()
    connectivity.update()
    print(f'Found {connectivity.GetNumberOfExtractedRegions()} holes')

    # Visualize

    # Create a mapper and actor for the fill polydata.
    scalar_range = connectivity.output.cell_data.GetArray('RegionId').range
    filled_mapper = vtkDataSetMapper(scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_CELL_DATA,
                                     scalar_range=scalar_range)
    connectivity >> filled_mapper
    filled_actor = vtkActor(mapper=filled_mapper)
    filled_actor.property.diffuse_color = colors.GetColor3d('Peacock')

    # Create a mapper and actor for the original polydata.
    original_mapper = vtkPolyDataMapper(input_data=poly_data)

    backface_prop = vtkProperty()
    backface_prop.diffuse_color = colors.GetColor3d('Banana')

    original_actor = vtkActor(mapper=original_mapper)
    original_actor.backface_property = backface_prop
    original_actor.property.diffuse_color = colors.GetColor3d('Flesh')
    original_actor.property.SetRepresentationToWireframe()

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('Burlywood'))
    render_window = vtkRenderWindow(size=(512, 512), window_name='IdentifyHoles')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(original_actor)
    renderer.AddActor(filled_actor)

    renderer.active_camera.position = (0, -1, 0)
    renderer.active_camera.focal_point = (0, 0, 0)
    renderer.active_camera.view_up = (0, 0, 1)
    renderer.active_camera.Azimuth(60)
    renderer.active_camera.Elevation(30)

    renderer.ResetCamera()
    # Render and interact.
    render_window.Render()

    render_window_interactor.Start()

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

def generate_data():
    # Create a sphere.
    sphere_source = vtkSphereSource()
    sphere_source.Update()

    # Remove some cells.
    ids = vtkIdTypeArray()
    ids.SetNumberOfComponents(1)

    # Set values.
    ids.InsertNextValue(2)
    ids.InsertNextValue(10)

    selection_node = vtkSelectionNode(field_type=vtkSelectionNode.CELL, content_type=vtkSelectionNode.INDICES,
                                      selection_list=ids)
    selection_node.properties.Set(vtkSelectionNode.INVERSE(), 1)  # invert the selection

    selection = vtkSelection()
    selection.AddNode(selection_node)

    extract_selection = vtkExtractSelection()
    sphere_source >> select_ports(0, extract_selection)
    extract_selection.SetInputData(1, selection)
    extract_selection.update()

    # In selection.
    surface_filter = vtkDataSetSurfaceFilter()
    extract_selection >> surface_filter
    surface_filter.update()

    return surface_filter.output

@dataclass(frozen=True)
class Mapper:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_MODE_DEFAULT: int = 0
        VTK_COLOR_MODE_MAP_SCALARS: int = 1
        VTK_COLOR_MODE_DIRECT_SCALARS: int = 2

    @dataclass(frozen=True)
    class ResolveCoincidentTopology:
        VTK_RESOLVE_OFF: int = 0
        VTK_RESOLVE_POLYGON_OFFSET: int = 1
        VTK_RESOLVE_SHIFT_ZBUFFER: int = 2

    @dataclass(frozen=True)
    class ScalarMode:
        VTK_SCALAR_MODE_DEFAULT: int = 0
        VTK_SCALAR_MODE_USE_POINT_DATA: int = 1
        VTK_SCALAR_MODE_USE_CELL_DATA: int = 2
        VTK_SCALAR_MODE_USE_POINT_FIELD_DATA: int = 3
        VTK_SCALAR_MODE_USE_CELL_FIELD_DATA: int = 4
        VTK_SCALAR_MODE_USE_FIELD_DATA: int = 5

if __name__ == '__main__':
    main()
```
