<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/InterpolateFieldDataDemo/ -->

# InterpolateFieldDataDemo

Repository source: [InterpolateFieldDataDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/InterpolateFieldDataDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestInterpolateFieldDataDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestInterpolateFieldDataDemo.png?raw=true target=)

### Description

This example uses [vtkPointInterpolator](https://www.vtk.org/doc/nightly/html/classvtkPointInterpolator.html) probe a high resolution dataset with a lower resolution dataset. Then, using [vtkInterpolateDataSetAttributes](https://www.vtk.org/doc/nightly/html/classvtkInterpolateDataSetAttributes.html), interpolate between the original low resolution data and the probed, low resolution data.

Warning

For the [vtkPointInterpolator](https://www.vtk.org/doc/nightly/html/classvtkPointInterpolator.html), point arrays will not be interpolated unless PassPointArrays is off. [vtkPointInterpolator](https://www.vtk.org/doc/nightly/html/classvtkPointInterpolator.html) does not interpolate [vtkFieldData](https://www.vtk.org/doc/nightly/html/classvtkFieldData.html). To interpolate [vtkFieldData](https://www.vtk.org/doc/nightly/html/classvtkFieldData.html) it must be added as the active scalar.

Warning

vtkInterpolateDataSetAttibutes does not interpolate [vtkFieldData](https://www.vtk.org/doc/nightly/html/classvtkFieldData.html). To interpolate [vtkFieldData](https://www.vtk.org/doc/nightly/html/classvtkFieldData.html) it must be added as the active scalar.

Thanks

This example was inspired by Andrew E. Slaughter, Idaho National Laboratory.

Note

In Windows, testing using coarseGrid.e will fail. It seems that this file has UTF-8 characters in it.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/InterpolateFieldDataDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**InterpolateFieldDataDemo.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkStaticPointLocator,
    vtkUnstructuredGrid
)
from vtkmodules.vtkFiltersGeneral import vtkInterpolateDataSetAttributes
from vtkmodules.vtkFiltersGeometry import vtkCompositeDataGeometryFilter
from vtkmodules.vtkFiltersPoints import (
    vtkGaussianKernel,
    vtkPointInterpolator
)
from vtkmodules.vtkIOExodus import vtkExodusIIReader
from vtkmodules.vtkInteractionWidgets import (
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTextActor,
    vtkTextProperty
)

def get_program_parameters():
    import argparse
    description = 'Resample a fine grid and interpolate field data.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('coarse_mesh', help='The coarse mesh, coarseGrid.e.')
    parser.add_argument('fine_mesh', help='The fine mesh, fineGrid.e-s002.')
    args = parser.parse_args()
    return args.coarse_mesh, args.fine_mesh

# This example was derived from a python script created by Andrew E. Slaughter.

def main():
    file0, file1 = get_program_parameters()

    file0 = Path(file0)
    if not file0.is_file():
        print(f'{file0} not found.')
        return
    file1 = Path(file1)
    if not file1.is_file():
        print(f'{file1} not found.')
        return

    color_array_name = 'u'
    scalar_range = (0, 10)

    #####################################
    # FILE 0: COARSE MESH WITH SOLUTION 0
    coarse_reader = vtkExodusIIReader(file_name=file0, time_step=0)
    coarse_reader.UpdateInformation()
    coarse_reader.SetAllArrayStatus(vtkExodusIIReader.NODAL, 1)
    coarse_reader.update()

    coarse_geometry = vtkCompositeDataGeometryFilter()
    coarse_reader >> coarse_geometry
    coarse_geometry.update()

    coarse_mapper = vtkPolyDataMapper(scalar_range=scalar_range,
                                      scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_POINT_FIELD_DATA,
                                      interpolate_scalars_before_mapping=True)
    coarse_geometry >> coarse_mapper
    coarse_mapper.SelectColorArray(color_array_name)

    coarse_actor = vtkActor(mapper=coarse_mapper)
    coarse_actor.property.edge_visibility = True

    ##################################
    # FILE 1: FINE MESH WITH SOLUTION 1

    fine_reader = vtkExodusIIReader(file_name=file1, time_step=0)
    fine_reader.UpdateInformation()
    fine_reader.SetAllArrayStatus(vtkExodusIIReader.NODAL, 1)
    fine_reader.update()

    fine_geometry = vtkCompositeDataGeometryFilter()
    fine_reader >> fine_geometry
    fine_geometry.update()
    fine_geometry.output.point_data.active_scalars = color_array_name

    fine_geometry_mapper = vtkPolyDataMapper(scalar_range=scalar_range,
                                             scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_POINT_FIELD_DATA,
                                             interpolate_scalars_before_mapping=True)
    fine_geometry >> fine_geometry_mapper
    fine_geometry_mapper.SelectColorArray(color_array_name)

    fine_geometry_actor = vtkActor(mapper=fine_geometry_mapper)
    fine_geometry_actor.property.edge_visibility = True

    ###################################
    # PROJECT SOLUTION FROM FILE 0 to GRID FROM FILE 1

    # Build the structure to interpolate onto.
    # The output to be interpolated onto.
    coarse_interpolated_grid = vtkUnstructuredGrid()

    coarse_multi_block = coarse_reader.output.GetBlock(0)
    coarse_interpolated_grid.DeepCopy(coarse_multi_block.GetBlock(0))

    locator = vtkStaticPointLocator(data_set=fine_geometry.output)
    locator.BuildLocator()

    kernel = vtkGaussianKernel(sharpness=4.0, number_of_points=10)
    kernel.SetKernelFootprintToNClosest()

    # Probe the fine geometry with the course geometry.
    # NOTE: The point arrays will not be interpolated unless PassPointArrays is off.
    coarse_interpolator = vtkPointInterpolator(source_data=fine_geometry.output, input_data=coarse_geometry.output,
                                               kernel=kernel, locator=locator, pass_point_arrays=False)
    coarse_interpolator.SetNullPointsStrategyToClosestPoint()
    coarse_interpolator.update()

    coarse_interpolator_mapper = vtkDataSetMapper(scalar_range=scalar_range,
                                                  scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_POINT_FIELD_DATA,
                                                  interpolate_scalars_before_mapping=True)
    coarse_interpolator >> coarse_interpolator_mapper
    coarse_interpolator_mapper.SelectColorArray(color_array_name)

    coarse_interpolator_actor = vtkActor(mapper=coarse_interpolator_mapper)
    coarse_interpolator_actor.property.edge_visibility = True

    # Set the active scalar for the two inputs.
    # NOTE: InterpolateDataSetAttributes does not interpolate field data.
    # To interpolate field data it must be added as the active scalar.
    coarse_interpolated_grid.point_data.SetActiveScalars(color_array_name)
    coarse_interpolator.output.point_data.SetActiveScalars(color_array_name)

    coarse_interpolate_attributes = vtkInterpolateDataSetAttributes(t=0.5)
    coarse_interpolate_attributes.AddInputData(0, coarse_interpolated_grid)
    coarse_interpolate_attributes.AddInputData(0, coarse_interpolator.output)
    coarse_interpolate_attributes.update()

    coarse_interpolate_attributes_mapper = vtkDataSetMapper(scalar_range=scalar_range,
                                                            scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_POINT_FIELD_DATA,
                                                            interpolate_scalars_before_mapping=True)
    coarse_interpolate_attributes >> coarse_interpolate_attributes_mapper
    coarse_interpolate_attributes_mapper.SelectColorArray(color_array_name)

    coarse_interpolate_attributes_actor = vtkActor(mapper=coarse_interpolate_attributes_mapper)
    coarse_interpolate_attributes_actor.property.edge_visibility = True

    text = {0: 'Low Res', 1: 'Interpolated Geometry', 2: 'Interpolated Attributes', 3: 'Hi-res with point data'}

    # Define viewport ranges [x_min, y_min, x_max, y_max]
    viewports = {0: (0, 0, 0.25, 1),
                 1: (0.25, 0, 0.5, 1),
                 2: (0.5, 0, 0.75, 1),
                 3: (0.75, 0, 1, 1)
                 }
    colors = vtkNamedColors()
    backgrounds = {0: colors.GetColor3d('Gainsboro'),
                   1: colors.GetColor3d('LightGrey'),
                   2: colors.GetColor3d('Silver'),
                   3: colors.GetColor3d('DarkGray')
                   }

    # The window holds four viewports of width 320.
    render_window = vtkRenderWindow(size=(1280, 320), window_name='InterpolateFieldDataDemo')
    # Create the interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    camera = None
    # Build the renderers and add them to the render window.
    renderers = list()
    for k in text.keys():
        renderers.append(vtkRenderer(viewport=viewports[k], background=backgrounds[k]))

        # Add the actors.
        if k == 0:
            renderers[k].AddActor(coarse_actor)
        elif k == 1:
            renderers[k].AddActor(coarse_interpolator_actor)
        elif k == 2:
            renderers[k].AddActor(coarse_interpolate_attributes_actor)
        else:
            renderers[k].AddActor(fine_geometry_actor)

        if k == 0:
            camera = renderers[k].active_camera
        else:
            renderers[k].active_camera = camera

        renderers[k].ResetCamera()

        render_window.AddRenderer(renderers[k])

    # Create the text widgets.
    text_actors = list()
    text_representations = list()
    text_widgets = list()
    text_property = vtkTextProperty(color=colors.GetColor3d('Black'), bold=True, italic=False, shadow=False,
                                    font_size=12, font_family_as_string='Courier',
                                    justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                    vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_CENTERED)

    text_positions = get_text_positions(list(text.values()), justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                        vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_BOTTOM
                                        )

    for k, v in text.items():
        text_actors.append(
            vtkTextActor(input=v, text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE, text_property=text_property))

        # Create the text representation. Used for positioning the text actor.
        text_representations.append(vtkTextRepresentation(enforce_normalized_viewport_bounds=True))
        text_representations[k].position_coordinate.value = text_positions[v]['p']
        text_representations[k].position2_coordinate.value = text_positions[v]['p2']

        # Create the TextWidget
        text_widgets.append(
            vtkTextWidget(representation=text_representations[k], text_actor=text_actors[k],
                          default_renderer=renderers[k], interactor=interactor, selectable=False))

    render_window.Render()
    interactor.Initialize()

    for k in text.keys():
        text_widgets[k].On()

    interactor.Start()

def get_text_positions(names, justification=0, vertical_justification=0, width=0.96, height=0.1):
    """
    Get viewport positioning information for a list of names.

    :param names: The list of names.
    :param justification: Horizontal justification of the text, default is left.
    :param vertical_justification: Vertical justification of the text, default is bottom.
    :param width: Width of the bounding_box of the text in screen coordinates.
    :param height: Height of the bounding_box of the text in screen coordinates.
    :return: A list of positioning information.
    """
    # The gap between the left or right edge of the screen and the text.
    dx = 0.02
    width = abs(width)
    if width > 0.96:
        width = 0.96

    y0 = 0.01
    height = abs(height)
    if height > 0.9:
        height = 0.9
    dy = height
    if vertical_justification == TextProperty.VerticalJustification.VTK_TEXT_TOP:
        y0 = 1.0 - (dy + y0)
        dy = height
    if vertical_justification == TextProperty.VerticalJustification.VTK_TEXT_CENTERED:
        y0 = 0.5 - (dy / 2.0 + y0)
        dy = height

    name_len_min = 0
    name_len_max = 0
    first = True
    for k in names:
        sz = len(k)
        if first:
            name_len_min = name_len_max = sz
            first = False
        else:
            name_len_min = min(name_len_min, sz)
            name_len_max = max(name_len_max, sz)
    text_positions = dict()
    for k in names:
        sz = len(k)
        delta_sz = width * sz / name_len_max
        if delta_sz > width:
            delta_sz = width

        if justification == TextProperty.Justification.VTK_TEXT_CENTERED:
            x0 = 0.5 - delta_sz / 2.0
        elif justification == TextProperty.Justification.VTK_TEXT_RIGHT:
            x0 = 1.0 - dx - delta_sz
        else:
            # Default is left justification.
            x0 = dx

        # For debugging!
        # print(
        #     f'{k:16s}: (x0, y0) = ({x0:3.2f}, {y0:3.2f}), (x1, y1) = ({x0 + delta_sz:3.2f}, {y0 + dy:3.2f})'
        #     f', width={delta_sz:3.2f}, height={dy:3.2f}')
        text_positions[k] = {'p': [x0, y0, 0], 'p2': [delta_sz, dy, 0]}

    return text_positions

@dataclass(frozen=True)
class TextProperty:
    @dataclass(frozen=True)
    class Justification:
        VTK_TEXT_LEFT: int = 0
        VTK_TEXT_CENTERED: int = 1
        VTK_TEXT_RIGHT: int = 2

    @dataclass(frozen=True)
    class VerticalJustification:
        VTK_TEXT_BOTTOM: int = 0
        VTK_TEXT_CENTERED: int = 1
        VTK_TEXT_TOP: int = 2

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
