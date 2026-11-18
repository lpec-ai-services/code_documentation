<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/ImportPolyDataScene/ -->

# ImportPolyDataScene

Repository source: [ImportPolyDataScene](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/ImportPolyDataScene.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestImportPolyDataScene.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestImportPolyDataScene.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ImportPolyDataScene/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImportPolyDataScene.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkDataObjectTreeIterator
from vtkmodules.vtkIOXML import vtkXMLMultiBlockDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkProperty
)

def get_program_parameters():
    import argparse
    description = 'Import a polydata scene using multiblock datasets.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='ExportBunny.vtp.')
    args = parser.parse_args()
    return args.filename

def main():
    file_name = get_program_parameters()

    fn = Path(file_name)
    if not fn.is_file():
        print(f'{fn} not found.')
        return

    colors = vtkNamedColors()
    # Visualization
    colors = vtkNamedColors()
    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='ImportPolyDataScene')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    import_multi_block_scene(renderer, fn)
    render_window.Render()

    render_window.Render()
    render_window_interactor.Start()

def import_multi_block_scene(renderer, fileName):
    camera = renderer.active_camera

    # Read the multiblock data.
    reader = vtkXMLMultiBlockDataReader(file_name=fileName)
    reader.Update()
    print(f'Importing {reader.output.number_of_blocks} actors.')

    input = reader.output

    iter = vtkDataObjectTreeIterator(data_set=input, skip_empty_nodes=True, visit_only_leaves=True)
    iter.InitTraversal()
    while not iter.IsDoneWithTraversal():
        iter.GoToNextItem()

        dso = iter.current_data_object
        pd = dso
        restore_camera_from_field_data('Camera', camera, pd)
        mapper = vtkPolyDataMapper(input_data=pd)

        actor = vtkActor(mapper=mapper)
        restore_property_from_field_data('Property', actor.property, pd)
        actor.backface_property = vtkProperty()
        restore_property_from_field_data('BackfaceProperty', actor.backface_property, pd)
        restore_actor_from_field_data('Actor', actor, pd)
        renderer.AddActor(actor)

"""
   These functions need to be written.
   def restore_mapper_from_field_data(name, mapper, poly_data):
   def restore_lookup_table_from_field_data(name, scalars_to_colors, poly_data):

   The functions gt0() and gt1() are used to provide values
    that need to be converted from float to int or boolean.
"""

def gt0(fd, array_prefix, name):
    return fd.GetArray(f'{array_prefix}:{name}').GetTuple(0)

def gt1(fd, array_prefix, name):
    return fd.GetArray(f'{array_prefix}:{name}').GetTuple1(0)

def restore_camera_from_field_data(array_prefix, camera, pd):
    if pd:
        fd = pd.GetFieldData()
        camera.focal_point = fd.GetArray(f'{array_prefix}:FocalPoint').GetTuple(0)
        camera.position = fd.GetArray(f'{array_prefix}:Position').GetTuple(0)
        camera.view_up = fd.GetArray(f'{array_prefix}:ViewUp').GetTuple(0)
        camera.clipping_range = fd.GetArray(f'{array_prefix}:ClippingRange').GetTuple(0)
        camera.view_angle = fd.GetArray(f'{array_prefix}:ViewAngle').GetTuple1(0)

def restore_property_from_field_data(array_prefix, fd_property, pd):
    if fd_property:
        if pd:
            fd = pd.GetFieldData()
            fd_property.ambient = fd.GetArray(f'{array_prefix}:Ambient').GetTuple1(0)
            fd_property.ambient_color = fd.GetArray(f'{array_prefix}:AmbientColor').GetTuple(0)
            fd_property.diffuse = fd.GetArray(f'{array_prefix}:Diffuse').GetTuple1(0)
            fd_property.diffuse_color = fd.GetArray(f'{array_prefix}:DiffuseColor').GetTuple(0)
            fd_property.specular = fd.GetArray(f'{array_prefix}:Specular').GetTuple1(0)
            fd_property.specular_color = fd.GetArray(f'{array_prefix}:SpecularColor').GetTuple(0)
            fd_property.specular_power = fd.GetArray(f'{array_prefix}:SpecularPower').GetTuple1(0)
            fd_property.edge_color = fd.GetArray(f'{array_prefix}:EdgeColor').GetTuple(0)
            x = gt1(fd, array_prefix, 'EdgeVisibility') == 1
            fd_property.edge_visibility = x
            fd_property.vertex_color = fd.GetArray(f'{array_prefix}:VertexColor').GetTuple(0)
            x = gt1(fd, array_prefix, 'VertexVisibility') == 1
            fd_property.vertex_visibility = x
            x = gt1(fd, array_prefix, 'Interpolation') == 1
            fd_property.interpolation = x
            x = gt1(fd, array_prefix, 'Opacity')
            fd_property.opacity = x
            x = int(gt1(fd, array_prefix, 'Representation'))
            fd_property.representation = x
            x = gt1(fd, array_prefix, 'BackfaceCulling') == 1
            fd_property.backface_culling = x
            x = gt1(fd, array_prefix, 'FrontfaceCulling') == 1
            fd_property.frontface_culling = x
            fd_property.point_size = fd.GetArray(f'{array_prefix}:PointSize').GetTuple1(0)
            fd_property.line_width = fd.GetArray(f'{array_prefix}:LineWidth').GetTuple1(0)
            x = gt1(fd, array_prefix, 'LineStipplePattern')
            fd_property.line_stipple_pattern = int(x)
            x = gt1(fd, array_prefix, 'LineStippleRepeatFactor')
            fd_property.line_stipple_repeat_factor = int(x)
            x = gt1(fd, array_prefix, 'Lighting') == 1
            fd_property.lighting = x
            x = gt1(fd, array_prefix, 'RenderPointsAsSpheres') == 1
            fd_property.render_points_as_spheres = x
            x = gt1(fd, array_prefix, 'RenderLinesAsTubes') == 1
            fd_property.render_lines_as_tubes = x
            x = gt1(fd, array_prefix, 'Shading') == 1
            fd_property.shading = x

def restore_actor_from_field_data(array_prefix, actor, pd):
    if pd:
        fd = pd.GetFieldData()
        x = gt1(fd, array_prefix, 'Dragable') == 1
        actor.dragable = x
        x = gt1(fd, array_prefix, 'Pickable') == 1
        actor.pickable = x
        actor.position = fd.GetArray(f'{array_prefix}:Position').GetTuple(0)
        actor.orientation = fd.GetArray(f'{array_prefix}:Orientation').GetTuple(0)
        actor.origin = fd.GetArray(f'{array_prefix}:Origin').GetTuple(0)
        actor.scale = fd.GetArray(f'{array_prefix}:Scale').GetTuple(0)
        x = gt1(fd, array_prefix, 'ForceOpaque') == 1
        actor.force_opaque = x
        x = gt1(fd, array_prefix, 'ForceTranslucent') == 1
        actor.force_translucent = x

if __name__ == '__main__':
    main()
```
