<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/FillHoles/ -->

# FillHoles

Repository source: [FillHoles](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/FillHoles.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestFillHoles.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestFillHoles.png?raw=true target=)

### Description

This filter finds holes in a mesh and closes them.

Seealso

[IdentifyHoles](IdentifyHoles.md) fills the holes and then identifies each hole.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/FillHoles/)), ([CSharp](https://examples.vtk.org/site/CSharp/Meshes/FillHoles/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FillHoles.py**

```python
#!/usr/bin/env python3

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
from vtkmodules.vtkCommonDataModel import vtkSelectionNode, vtkSelection
from vtkmodules.vtkFiltersCore import vtkPolyDataNormals
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

    fill_holes_filter = vtkFillHolesFilter(input_data=poly_data, hole_size=100000.0)
    fill_holes_filter.update()

    # Make the triangle winding order consistent
    normals = vtkPolyDataNormals(input_data=fill_holes_filter.output, consistency=True, splitting=False)

    if restore_original_normals:
        # Restore the original normals.
        normals.update().output.point_data.SetNormals(poly_data.point_data.normals)

    # Visualize
    # Define viewport ranges.
    # (xmin, ymin, xmax, ymax)
    left_viewport = [0.0, 0.0, 0.5, 1.0]
    right_viewport = [0.5, 0.0, 1.0, 1.0]

    # Create a mapper and actor.
    original_mapper = vtkPolyDataMapper(input_data=poly_data)

    backface_prop = vtkProperty()
    backface_prop.diffuse_color = colors.GetColor3d('Banana')

    original_actor = vtkActor(mapper=original_mapper)
    original_actor.backface_property = backface_prop
    original_actor.property.diffuse_color = colors.GetColor3d('NavajoWhite')

    filled_mapper = vtkPolyDataMapper()
    normals >> filled_mapper

    filled_actor = vtkActor(mapper=filled_mapper)
    filled_actor.property.diffuse_color = colors.GetColor3d('NavajoWhite')
    filled_actor.backface_property = backface_prop

    # Create the renderers, render window, and interactor.
    left_renderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('SlateGray'))
    right_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('LightSlateGray'))

    render_window = vtkRenderWindow(size=(600, 300), window_name='FillHoles')
    render_window.AddRenderer(left_renderer)
    render_window.AddRenderer(right_renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actor to the scene.
    left_renderer.AddActor(original_actor)
    right_renderer.AddActor(filled_actor)

    left_renderer.active_camera.position = (0, -1, 0)
    left_renderer.active_camera.focal_point = (0, 0, 0)
    left_renderer.active_camera.view_up = (0, 0, 1)
    left_renderer.active_camera.Azimuth(30)
    left_renderer.active_camera.Elevation(30)

    left_renderer.ResetCamera()

    # Share the camera.
    right_renderer.active_camera = left_renderer.active_camera

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

if __name__ == '__main__':
    main()
```
