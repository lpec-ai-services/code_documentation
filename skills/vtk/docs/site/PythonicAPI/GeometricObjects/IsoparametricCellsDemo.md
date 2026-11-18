<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/IsoparametricCellsDemo/ -->

# IsoparametricCellsDemo

Repository source: [IsoparametricCellsDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/IsoparametricCellsDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestIsoparametricCellsDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestIsoparametricCellsDemo.png?raw=true target=)

### Description

This example shows the isoparametric cells supported by the VTK. These cells are nonlinear and contain one or more mid-side vertices. Isoparametric elements are typically used in [finite element analysis](https://en.wikipedia.org/wiki/Finite_element_method). The term isoparametric is derived from the use of the same shape functions (or interpolation functions) to define the element's geometric shape as are used to define the displacements within the element.

Options are provided to show a wire frame (`-w`) or to add a back face color (`-b`). You can also remove the plinth with the (`-n`) option. If you want a single object, use `-o` followed by the object number.

This example illustrates each cell's representation using its parametric coordinates (pcoords) as the vertices of the cell. In practice, the vertices will correspond to physical points in a finite element model. Use [vtkTessellatorFilter](https://www.vtk.org/doc/nightly/html/classvtkTessellatorFilter.html) to better see the shape of the cell. See for example, [QuadraticHexahedronDemo](https://examples.vtk.org/site/PythonicAPI/GeometricObjects/QuadraticHexahedronDemo/) and [QuadraticTetraDemo](https://examples.vtk.org/site/PythonicAPI/GeometricObjects/QuadraticTetraDemo/).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/IsoparametricCellsDemo/)), ([Python](../../Python/GeometricObjects/IsoparametricCellsDemo.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IsoparametricCellsDemo.py**

```python
#!/usr/bin/env python3

from collections import namedtuple
from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkPolyData,
    vtkCellArray,
    vtkBiQuadraticQuad,
    vtkBiQuadraticQuadraticHexahedron,
    vtkBiQuadraticQuadraticWedge,
    vtkBiQuadraticTriangle,
    vtkCubicLine,
    vtkPolyLine,
    vtkQuadraticEdge,
    vtkQuadraticHexahedron,
    vtkQuadraticLinearQuad,
    vtkQuadraticLinearWedge,
    vtkQuadraticPolygon,
    vtkQuadraticPyramid,
    vtkQuadraticQuad,
    vtkQuadraticTetra,
    vtkQuadraticTriangle,
    vtkQuadraticWedge,
    vtkTriQuadraticHexahedron,
    vtkUnstructuredGrid
)
# noinspection PyUnresolvedReferences
from vtkmodules.vtkCommonTransforms import vtkTransform
# noinspection PyUnresolvedReferences
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersSources import (
    vtkCubeSource,
    vtkSphereSource
)
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkInteractionWidgets import (
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkActor2D,
    vtkCoordinate,
    vtkDataSetMapper,
    vtkGlyph3DMapper,
    vtkLightKit,
    vtkPolyDataMapper,
    vtkPolyDataMapper2D,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextActor,
    vtkTextProperty
)
from vtkmodules.vtkRenderingLabel import vtkLabeledDataMapper

def get_program_parameters():
    import argparse
    description = 'Demonstrate the isoparametric cell types found in VTK.'
    epilogue = '''
     The numbers define the ordering of the points making the cell.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('-w', '--wireframe', action='store_true',
                        help='Render a wireframe.')
    group1.add_argument('-b', '--backface', action='store_true',
                        help='Display the back face in a different colour.')

    parser.add_argument('-o', '--object_number', type=int, default=None,
                        help='The number corresponding to the object.')
    parser.add_argument('-n', '--no_plinth', action='store_true',
                        help='Remove the plinth.')
    args = parser.parse_args()
    return args.wireframe, args.backface, args.object_number, args.no_plinth

def main():
    wireframe_on, backface_on, object_num, plinth_off = get_program_parameters()

    objects = specify_objects()
    # The order here should match the order in specify_objects().
    object_order = list(objects.keys())

    # Check for a single object.
    single_object = None
    if object_num:
        if object_num in object_order:
            single_object = True
        else:
            print('Object not found.\nPlease enter the number corresponding to the object.')
            print('Available objects are:')
            for obj in object_order:
                print(f'{objects[obj]} (= {str(obj)})')
            return

    colors = vtkNamedColors()

    # Create one sphere for all.
    sphere = vtkSphereSource(phi_resolution=21, theta_resolution=21, radius=0.04)

    cells = get_unstructured_grids()
    # The text to be displayed in the viewport.
    names = list()
    # The keys of the objects selected for display.
    keys = list()
    if single_object:
        names.append(f'{objects[object_num]} (={str(object_num)})')
        keys.append(object_num)
    else:
        for obj in object_order:
            names.append(f'{objects[obj]} (={str(obj)})')
            keys.append(obj)

    add_plinth = (24, 25, 12, 26, 27, 29, 31, 32, 33)
    lines = (21, 35)

    # Set up the viewports.
    grid_column_dimensions = 4
    grid_row_dimensions = 4
    renderer_size = 300
    if single_object:
        grid_column_dimensions = 1
        grid_row_dimensions = 1
        renderer_size = 1200
    window_size = (grid_column_dimensions * renderer_size, grid_row_dimensions * renderer_size)

    viewports = dict()
    VP_Params = namedtuple('VP_Params', ['viewport', 'border'])
    last_col = False
    last_row = False
    blank = len(cells)
    blank_viewports = list()

    for row in range(0, grid_row_dimensions):
        if row == grid_row_dimensions - 1:
            last_row = True
        for col in range(0, grid_column_dimensions):
            if col == grid_column_dimensions - 1:
                last_col = True
            index = row * grid_column_dimensions + col
            # Set the renderer's viewport dimensions (xmin, ymin, xmax, ymax) within the render window.
            # Note that for the Y values, we need to subtract the row index from grid_rows
            #  because the viewport Y axis points upwards, and we want to draw the grid from top to down.
            viewport = (float(col) / grid_column_dimensions,
                        float(grid_row_dimensions - (row + 1)) / grid_row_dimensions,
                        float(col + 1) / grid_column_dimensions,
                        float(grid_row_dimensions - row) / grid_row_dimensions)

            if last_row and last_col:
                border = ViewportBorderSpecifier.tlbr
                last_row = False
                last_col = False
            elif last_col:
                border = ViewportBorderSpecifier.rtl
                last_col = False
            elif last_row:
                border = ViewportBorderSpecifier.tlb
            else:
                border = ViewportBorderSpecifier.tl
            vp_params = VP_Params(viewport, border)
            if index < blank:
                viewports[keys[index]] = vp_params
            else:
                s = f'vp_{col:d}_{row:d}'
                viewports[s] = vp_params
                blank_viewports.append(s)

    text_positions = get_text_positions(names,
                                        justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                        vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_BOTTOM,
                                        width=0.85, height=0.1)

    ren_win = vtkRenderWindow(size=window_size, window_name='LinearCellDemo')
    ren_win.SetWindowName('IsoparametricCellsDemo')
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we always import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    renderers = dict()
    text_representations = list()
    text_actors = list()
    text_widgets = list()

    # Create and link the mappers, actors and renderers together.
    single_object_key = None
    for idx, key in enumerate(keys):
        print('Creating:', names[idx])

        if single_object:
            single_object_key = key

        mapper = vtkDataSetMapper()
        cells[key][0] >> mapper
        actor = vtkActor(mapper=mapper, property=get_actor_property())
        if wireframe_on or key in lines:
            actor.property.representation = Property.Representation.VTK_WIREFRAME
            actor.property.line_width = 2
            actor.property.opacity = 1
            actor.property.color = colors.GetColor3d('Black')
        else:
            if backface_on:
                actor.backface_property = get_back_face_property()

        # Label the points.
        label_property = get_label_property()
        if single_object:
            label_property.SetFontSize(renderer_size // 36)
        else:
            label_property.SetFontSize(renderer_size // 16)

        label_mapper = vtkLabeledDataMapper(label_text_property=label_property)
        cells[key][0] >> label_mapper
        label_actor = vtkActor2D(mapper=label_mapper)

        # Glyph the points.
        point_mapper = vtkGlyph3DMapper(scaling=True, scalar_visibility=False,
                                        source_connection=sphere.output_port)
        cells[key][0] >> point_mapper
        point_actor = vtkActor(mapper=point_mapper, property=get_point_actor_property())

        viewport = viewports[key].viewport
        border = viewports[key].border
        renderer = vtkRenderer(background=colors.GetColor3d('LightSteelBlue'), viewport=viewport)
        border_actor = draw_viewport_border(sides=border, border_color='Yellow', border_width=4)
        renderer.AddActor(border_actor)

        light_kit = vtkLightKit()
        light_kit.AddLightsToRenderer(renderer)

        renderer.AddActor(actor)
        renderer.AddActor(label_actor)
        renderer.AddActor(point_actor)
        if not plinth_off:
            # Add a plinth.
            if key in add_plinth:
                tile_actor = make_tile(cells[key][0].GetBounds(),
                                       expansion_factor=0.5, thickness_ratio=0.01, shift_y=-0.05)
                tile_actor.property = get_tile_property()
                renderer.AddActor(tile_actor)

        # Create the text actor and representation.
        text_property = get_text_property()
        if single_object:
            text_property.SetFontSize(renderer_size // 28)
        else:
            text_property.SetFontSize(renderer_size // 24)

        text_actor = vtkTextActor(input=names[idx],
                                  text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE,
                                  text_property=get_text_property())

        # Create the text representation. Used for positioning the text actor.
        text_representation = vtkTextRepresentation(enforce_normalized_viewport_bounds=True)
        text_representation.position_coordinate.value = text_positions[names[idx]]['p']
        text_representation.position2_coordinate.value = text_positions[names[idx]]['p2']

        # Create the text widget, setting the default renderer and interactor.
        text_widget = vtkTextWidget(representation=text_representation, text_actor=text_actor,
                                    default_renderer=renderer, interactor=iren, selectable=False)

        text_actors.append(text_actor)
        text_representations.append(text_representation)
        text_widgets.append(text_widget)

        renderer.ResetCamera()
        renderer.active_camera.Azimuth(cells[key][1].azimuth)
        renderer.active_camera.Elevation(cells[key][1].elevation)
        renderer.active_camera.Dolly(cells[key][1].zoom)
        renderer.ResetCameraClippingRange()

        renderers[key] = renderer
        ren_win.AddRenderer(renderers[key])

    for name in blank_viewports:
        viewport = viewports[name].viewport
        border = viewports[name].border
        renderer = vtkRenderer(background=colors.GetColor3d('LightSteelBlue'), viewport=viewport)
        border_actor = draw_viewport_border(sides=border, border_color='Yellow', border_width=4)
        renderer.AddActor(border_actor)

        renderers[name] = renderer
        ren_win.AddRenderer(renderers[name])

    for tw in text_widgets:
        tw.On()

    if single_object:
        cam_orient_manipulator = vtkCameraOrientationWidget(parent_renderer=renderers[single_object_key],
                                                            interactor=iren)
        cam_orient_manipulator.On()

    ren_win.Render()
    iren.Initialize()
    iren.Start()

def specify_objects():
    """
    Link the unstructured grid number to the unstructured grid name.

    :return: A dictionary: {index number: unstructured grid name}.
    """
    objects = {
        21: 'VTK_QUADRATIC_EDGE',
        22: 'VTK_QUADRATIC_TRIANGLE',
        23: 'VTK_QUADRATIC_QUAD',
        36: 'VTK_QUADRATIC_POLYGON',
        24: 'VTK_QUADRATIC_TETRA',
        25: 'VTK_QUADRATIC_HEXAHEDRON',
        26: 'VTK_QUADRATIC_WEDGE',
        27: 'VTK_QUADRATIC_PYRAMID',
        28: 'VTK_BIQUADRATIC_QUAD',
        29: 'VTK_TRIQUADRATIC_HEXAHEDRON',
        30: 'VTK_QUADRATIC_LINEAR_QUAD',
        31: 'VTK_QUADRATIC_LINEAR_WEDGE',
        32: 'VTK_BIQUADRATIC_QUADRATIC_WEDGE',
        33: 'VTK_BIQUADRATIC_QUADRATIC_HEXAHEDRON',
        34: 'VTK_BIQUADRATIC_TRIANGLE',
        35: 'VTK_CUBIC_LINE',
    }
    return objects

def get_unstructured_grids():
    """
    Get the unstructured grid names, the unstructured grid and initial orientations.

    :return: A dictionary: {index number: (unstructured grid, orientation)}.
    """

    def make_orientation(azimuth: float = 0, elevation: float = 0, zoom: float = 1.0):
        return Orientation(azimuth, elevation, zoom)

    return {
        21: (make_ug(vtkQuadraticEdge()), make_orientation(0, 0, 0.8)),
        22: (make_ug(vtkQuadraticTriangle()), make_orientation(0, 0, 0)),
        23: (make_ug(vtkQuadraticQuad()), make_orientation(0, 0, 0)),
        36: (make_quadratic_polygon(), make_orientation(0, 0, 0)),
        24: (make_ug(vtkQuadraticTetra()), make_orientation(20, 20, 1.0)),
        25: (make_ug(vtkQuadraticHexahedron()), make_orientation(-30, 12, 0.95)),
        26: (make_ug(vtkQuadraticWedge()), make_orientation(45, 15, 1.0)),
        27: (make_quadratic_pyramid(), make_orientation(-110, 8, 1.0)),
        28: (make_ug(vtkBiQuadraticQuad()), make_orientation(0, 0, 0)),
        29: (make_ug(vtkTriQuadraticHexahedron()), make_orientation(-15, 15, 0.95)),
        30: (make_ug(vtkQuadraticLinearQuad()), make_orientation(0, 0, 0)),
        31: (make_ug(vtkQuadraticLinearWedge()), make_orientation(60, 22.5, 1.0)),
        32: (make_ug(vtkBiQuadraticQuadraticWedge()), make_orientation(70, 22.5, 1.0)),
        33: (make_ug(vtkBiQuadraticQuadraticHexahedron()), make_orientation(-15, 15, 0.95)),
        34: (make_ug(vtkBiQuadraticTriangle()), make_orientation(0, 0, 0)),
        35: (make_ug(vtkCubicLine()), make_orientation(0, 0, 0.85)),
    }

# These functions return a vtkUnstructured grid corresponding to the object.

def make_ug(cell):
    pcoords = cell.GetParametricCoords()
    for i in range(0, cell.number_of_points):
        cell.point_ids.SetId(i, i)
        cell.points.SetPoint(i, (pcoords[3 * i]), (pcoords[3 * i + 1]), (pcoords[3 * i + 2]))

    ug = vtkUnstructuredGrid(points=cell.points)
    ug.InsertNextCell(cell.cell_type, cell.point_ids)
    return ug

def make_quadratic_polygon():
    number_of_vertices = 8

    quadratic_polygon = vtkQuadraticPolygon()

    quadratic_polygon.points.SetNumberOfPoints(8)

    quadratic_polygon.points.SetPoint(0, 0.0, 0.0, 0.0)
    quadratic_polygon.points.SetPoint(1, 2.0, 0.0, 0.0)
    quadratic_polygon.points.SetPoint(2, 2.0, 2.0, 0.0)
    quadratic_polygon.points.SetPoint(3, 0.0, 2.0, 0.0)
    quadratic_polygon.points.SetPoint(4, 1.0, 0.0, 0.0)
    quadratic_polygon.points.SetPoint(5, 2.0, 1.0, 0.0)
    quadratic_polygon.points.SetPoint(6, 1.0, 2.0, 0.0)
    quadratic_polygon.points.SetPoint(7, 0.0, 1.0, 0.0)
    quadratic_polygon.points.SetPoint(5, 3.0, 1.0, 0.0)

    quadratic_polygon.point_ids.SetNumberOfIds(number_of_vertices)
    for i in range(0, number_of_vertices):
        quadratic_polygon.point_ids.SetId(i, i)

    ug = vtkUnstructuredGrid(points=quadratic_polygon.points)
    ug.InsertNextCell(quadratic_polygon.cell_type, quadratic_polygon.point_ids)

    return ug

def make_quadratic_pyramid():
    cell = vtkQuadraticPyramid()
    pcoords = cell.GetParametricCoords()
    for i in range(0, cell.number_of_points):
        cell.point_ids.SetId(i, i)
        cell.points.SetPoint(i, (pcoords[3 * i]), (pcoords[3 * i + 1]), (pcoords[3 * i + 2]))

    ug = vtkUnstructuredGrid(points=cell.points)
    ug.InsertNextCell(cell.cell_type, cell.point_ids)

    t = vtkTransform()
    t.RotateX(-90)
    t.Translate(0, 0, 0)
    tf = vtkTransformFilter(transform=t)

    (ug >> tf).update()
    # Put the transformed points back.
    ug.points = tf.output.points

    return ug

@dataclass(frozen=True)
class Orientation:
    azimuth: float
    elevation: float
    zoom: float

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

def draw_viewport_border(sides, border_color, border_width):
    """
    Set a border around a viewport.

    :param sides: An array of boolean corresponding to [top, left, bottom, right]
    :param border_color: The color of the border.
    :param border_width: The width of the border.
    :return: The border actor.
    """
    colors = vtkNamedColors()

    # Points start at upper right and proceed anti-clockwise.
    points = vtkPoints(number_of_points=4)
    points.InsertPoint(0, 1, 1, 0)
    points.InsertPoint(1, 0, 1, 0)
    points.InsertPoint(2, 0, 0, 0)
    points.InsertPoint(3, 1, 0, 0)

    cells = vtkCellArray()

    if sides[0]:
        # Top
        top = vtkPolyLine()
        top.point_ids.number_of_ids = 2
        top.point_ids.SetId(0, 0)
        top.point_ids.SetId(1, 1)
        cells.InsertNextCell(top)
    if sides[1]:
        # Left
        left = vtkPolyLine()
        left.point_ids.number_of_ids = 2
        left.point_ids.SetId(0, 1)
        left.point_ids.SetId(1, 2)
        cells.InsertNextCell(left)
    if sides[2]:
        # Bottom
        bottom = vtkPolyLine()
        bottom.point_ids.number_of_ids = 2
        bottom.point_ids.SetId(0, 2)
        bottom.point_ids.SetId(1, 3)
        cells.InsertNextCell(bottom)
    if sides[3]:
        # Right
        right = vtkPolyLine()
        right.point_ids.number_of_ids = 2
        right.point_ids.SetId(0, 3)
        right.point_ids.SetId(1, 0)
        cells.InsertNextCell(right)

    # Now make the polydata and display it.
    poly = vtkPolyData(points=points, lines=cells)

    # Use normalized viewport coordinates since
    # they are independent of window size.
    coordinate = vtkCoordinate()
    coordinate.SetCoordinateSystemToNormalizedViewport()

    mapper = vtkPolyDataMapper2D(input_data=poly, transform_coordinate=coordinate)

    actor = vtkActor2D(mapper=mapper)
    actor.property.color = colors.GetColor3d(border_color)
    # Line width should be at least 2 to be visible at extremes.
    actor.property.line_width = border_width

    return actor

@dataclass(frozen=True)
class ViewportBorderSpecifier:
    # Define borders for the viewports  = [top, left, bottom, right].
    t = [True, False, False, False]
    l = [False, True, False, False]
    b = [False, False, True, False]
    r = [False, False, False, True]
    lb = [False, True, True, False]
    lbr = [False, True, True, True]
    tlb = [True, True, True, False]
    tlbr = [True, True, True, True]
    rtl = [True, True, False, True]
    tl = [True, True, False, False]

def make_tile(bounds, expansion_factor=0.5, thickness_ratio=0.05, shift_y=-0.05):
    """
    Make a tile slightly larger or smaller than the bounds in the
      X and Z directions and thinner or thicker in the Y direction.

    A thickness_ratio of zero reduces the tile to an XZ plane.

    :param bounds: The bounds for the tile.
    :param expansion_factor: The expansion factor in the XZ plane.
    :param thickness_ratio: The thickness ratio in the Y direction, >= 0.
    :param shift_y: Used to shift the centre of the plinth in the Y-direction.
    :return: An actor corresponding to the tile.
    """

    d_xyz = (
        bounds[1] - bounds[0],
        bounds[3] - bounds[2],
        bounds[5] - bounds[4]
    )
    thickness = d_xyz[2] * abs(thickness_ratio)
    center = ((bounds[1] + bounds[0]) / 2.0,
              bounds[2] - thickness / 2.0 + shift_y,
              (bounds[5] + bounds[4]) / 2.0)
    x_length = bounds[1] - bounds[0] + (d_xyz[0] * expansion_factor)
    z_length = bounds[5] - bounds[4] + (d_xyz[2] * expansion_factor)

    plane = vtkCubeSource(center=center, x_length=x_length, y_length=thickness, z_length=z_length)

    plane_mapper = vtkPolyDataMapper()
    plane >> plane_mapper

    return vtkActor(mapper=plane_mapper)

def get_text_property():
    colors = vtkNamedColors()

    return vtkTextProperty(color=colors.GetColor3d('Black'),
                           bold=True, italic=False, shadow=False,
                           font_family_as_string='Courier',
                           justification=TextProperty.Justification.VTK_TEXT_CENTERED)

def get_label_property():
    colors = vtkNamedColors()

    return vtkTextProperty(color=colors.GetColor3d('DeepPink'),
                           bold=True, italic=False, shadow=True,
                           font_family_as_string='Courier',
                           justification=TextProperty.Justification.VTK_TEXT_CENTERED)

def get_back_face_property():
    colors = vtkNamedColors()

    return vtkProperty(
        ambient_color=colors.GetColor3d('LightSalmon'),
        diffuse_color=colors.GetColor3d('OrangeRed'),
        specular_color=colors.GetColor3d('White'),
        specular=0.2, diffuse=1.0, ambient=0.2, specular_power=20.0,
        opacity=1.0)

def get_actor_property():
    colors = vtkNamedColors()

    return vtkProperty(
        ambient_color=colors.GetColor3d('DarkSalmon'),
        diffuse_color=colors.GetColor3d('Seashell'),
        specular_color=colors.GetColor3d('White'),
        specular=0.5, diffuse=0.7, ambient=0.5, specular_power=20.0,
        opacity=0.9, edge_visibility=True, line_width=3)

def get_point_actor_property():
    colors = vtkNamedColors()

    return vtkProperty(
        ambient_color=colors.GetColor3d('Gold'),
        diffuse_color=colors.GetColor3d('Yellow'),
        specular_color=colors.GetColor3d('White'),
        specular=0.5, diffuse=0.7, ambient=0.5, specular_power=20.0,
        opacity=1.0)

def get_tile_property():
    colors = vtkNamedColors()

    return vtkProperty(
        ambient_color=colors.GetColor3d('SteelBlue'),
        diffuse_color=colors.GetColor3d('LightSteelBlue'),
        specular_color=colors.GetColor3d('White'),
        specular=0.5, diffuse=0.7, ambient=0.5, specular_power=20.0,
        opacity=0.8, edge_visibility=True, line_width=1)

@dataclass(frozen=True)
class Coordinate:
    @dataclass(frozen=True)
    class CoordinateSystem:
        VTK_DISPLAY: int = 0
        VTK_NORMALIZED_DISPLAY: int = 1
        VTK_VIEWPORT: int = 2
        VTK_NORMALIZED_VIEWPORT: int = 3
        VTK_VIEW: int = 4
        VTK_POSE: int = 5
        VTK_WORLD: int = 6
        VTK_USERDEFINED: int = 7

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

@dataclass(frozen=True)
class TextProperty:
    @dataclass(frozen=True)
    class FontFamily:
        VTK_ARIAL: int = 0
        VTK_COURIER: int = 1
        VTK_TIMES: int = 2
        VTK_UNKNOWN_FONT: int = 3

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

if __name__ == '__main__':
    main()
```
