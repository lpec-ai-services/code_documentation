<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/PlatonicSolids/ -->

# PlatonicSolids

Repository source: [PlatonicSolids](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/PlatonicSolids.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestPlatonicSolids.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestPlatonicSolids.png?raw=true target=)

### Description

Display all five Platonic solids in a grid.

Platonic solids are regular, convex polyhedrons. They are constructed by congruent (identical in shape and size) regular (all angles equal and all sides equal) polygonal faces with the same number of faces meeting at each vertex.

Five solids satisfy the above criteria:

| Figure | Tetrahedron | Cube | Octahedron | Icosahedron | Dodecahedron |
| --- | --- | --- | --- | --- | --- |
| Vertices | 4 | 8 | 6 (2 × 3) | 12 (4 × 3) | 20 (8 + 4 × 3) |
| Edges | 6 | 12 | 12 | 30 | 30 |
| Faces | 4 | 6 | 8 | 20 | 12 |

The relationship between vertices, edges and faces is given by Euler's formula:

```python
V - E + F = 2
```

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/PlatonicSolids/)), ([Python](../../Python/GeometricObjects/PlatonicSolids.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PlatonicSolids.py**

```python
#!/usr/bin/env python3

from collections import namedtuple
from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkLookupTable,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkPolyLine
)
from vtkmodules.vtkFiltersSources import vtkPlatonicSolidSource
from vtkmodules.vtkInteractionWidgets import (
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkActor2D,
    vtkCoordinate,
    vtkPolyDataMapper,
    vtkPolyDataMapper2D,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextActor,
    vtkTextProperty
)

def main():
    colors = vtkNamedColors()

    name_orientation = get_name_orientation()
    lut = get_platonic_lut()

    # Set up the viewports.
    x_grid_dimensions = 3
    y_grid_dimensions = 2
    renderer_size = 300
    size = (x_grid_dimensions * renderer_size, y_grid_dimensions * renderer_size)

    VP_Params = namedtuple('VP_Params', ['name', 'viewport', 'border'])
    viewports = dict()
    last_col = False
    last_row = False
    blank = len(name_orientation)

    for row in range(0, y_grid_dimensions):
        if row == y_grid_dimensions - 1:
            last_row = True
        for col in range(0, x_grid_dimensions):
            if col == x_grid_dimensions - 1:
                last_col = True
            index = row * x_grid_dimensions + col
            # (xmin, ymin, xmax, ymax)
            viewport = (float(col) / x_grid_dimensions,
                        float(y_grid_dimensions - (row + 1)) / y_grid_dimensions,
                        float(col + 1) / x_grid_dimensions,
                        float(y_grid_dimensions - row) / y_grid_dimensions)

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
            if index < blank:
                viewports[index] = VP_Params(name_orientation[index].name, viewport, border)
            else:
                viewports[index] = VP_Params('', viewport, border)

    # Create the render window and interactor.
    ren_win = vtkRenderWindow(size=size, window_name='PlatonicSolids')

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Create one text property for all.
    text_property = vtkTextProperty(color=colors.GetColor3d('AliceBlue'), bold=True, italic=True,
                                    shadow=True, font_family_as_string='Courier',
                                    font_size=16, justification=TextProperty.Justification.VTK_TEXT_CENTERED)

    titles = list()
    for n in name_orientation:
        titles.append(n.name)
    # Position text according to its length and centered in the viewport.
    text_positions = get_text_positions(titles, justification=TextProperty.Justification.VTK_TEXT_CENTERED)

    text_representations = list()
    # text_actors = list()
    text_widgets = list()
    renderers = list()

    # Create and link the mappers actors and renderers together.
    for index in range(0, len(viewports)):

        name = viewports[index].name
        viewport = viewports[index].viewport
        border = viewports[index].border

        renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'), viewport=viewport)
        renderer.AddActor(draw_viewport_border(sides=border, border_color='Yellow', border_width=4))
        if not name:
            # Add a renderer even if the border is the only actor.
            # This makes the render window backgrounds all the same color.
            renderers.append(renderer)
            ren_win.AddRenderer(renderer)
            continue

        platonic_solid = vtkPlatonicSolidSource(solid_type=index)
        mapper = vtkPolyDataMapper(lookup_table=lut, scalar_range=(0, 19))
        platonic_solid >> mapper
        actor = vtkActor(mapper=mapper)
        renderer.AddActor(actor)

        text_actor = vtkTextActor(input=name,
                                  text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE,
                                  text_property=text_property)

        # Create the text representation. Used for positioning the text actor.
        text_representations.append(vtkTextRepresentation(enforce_normalized_viewport_bounds=True))
        text_representations[index].position_coordinate.value = text_positions[name]['p']
        text_representations[index].position2_coordinate.value = text_positions[name]['p2']

        # Create the text widget, setting the default renderer and interactor.
        text_widgets.append(
            vtkTextWidget(representation=text_representations[index], text_actor=text_actor,
                          default_renderer=renderer, interactor=iren, selectable=False))

        # Orient the view.
        renderer.ResetCamera()
        renderer.active_camera.Azimuth(name_orientation[index].azimuth)
        renderer.active_camera.Elevation(name_orientation[index].elevation)
        renderer.active_camera.Zoom(name_orientation[index].zoom)
        renderer.ResetCameraClippingRange()

        renderers.append(renderer)
        ren_win.AddRenderer(renderers[index])

    for tw in text_widgets:
        tw.On()

    iren.Initialize()
    ren_win.Render()
    iren.Start()

def get_name_orientation():
    """
    Get the platonic solid names and initial orientations.

    :return: The solids and their initial orientations.
    """

    # [[name, azimuth, elevation, zoom] ...]
    res = [['Tetrahedron', 45.0, 30.0, 1.0],
           ['Cube', -60.0, 45.0, 0.8],
           ['Octahedron', -15.0, 10.0, 1.0],
           ['Icosahedron', 4.5, 18.0, 1.0],
           ['Dodecahedron', 171.0, 22.0, 1.0]]

    platonic_solids = namedtuple('platonic_solids', ('name', 'azimuth', 'elevation', 'zoom'))
    # Convert res to a list of named tuples.
    res = [platonic_solids(*row) for row in res]
    return res

def get_platonic_lut():
    """
    Get a specialised lookup table for the platonic solids.

    Since each face of a vtkPlatonicSolidSource has a different
    cell scalar, we create a lookup table with a different colour
    for each face.
    The colors have been carefully chosen so that adjacent cells
    are colored distinctly.

    :return: The lookup table.
    """
    lut = vtkLookupTable(number_of_table_values=20, table_range=(0.0, 19.0))
    # lut.SetNumberOfTableValues(20)
    # lut.SetTableRange(0.0, 19.0)
    lut.Build()
    lut.SetTableValue(0, 0.1, 0.1, 0.1)
    lut.SetTableValue(1, 0, 0, 1)
    lut.SetTableValue(2, 0, 1, 0)
    lut.SetTableValue(3, 0, 1, 1)
    lut.SetTableValue(4, 1, 0, 0)
    lut.SetTableValue(5, 1, 0, 1)
    lut.SetTableValue(6, 1, 1, 0)
    lut.SetTableValue(7, 0.9, 0.7, 0.9)
    lut.SetTableValue(8, 0.5, 0.5, 0.5)
    lut.SetTableValue(9, 0.0, 0.0, 0.7)
    lut.SetTableValue(10, 0.5, 0.7, 0.5)
    lut.SetTableValue(11, 0, 0.7, 0.7)
    lut.SetTableValue(12, 0.7, 0, 0)
    lut.SetTableValue(13, 0.7, 0, 0.7)
    lut.SetTableValue(14, 0.7, 0.7, 0)
    lut.SetTableValue(15, 0, 0, 0.4)
    lut.SetTableValue(16, 0, 0.4, 0)
    lut.SetTableValue(17, 0, 0.4, 0.4)
    lut.SetTableValue(18, 0.4, 0, 0)
    lut.SetTableValue(19, 0.4, 0, 0.4)
    return lut

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

if __name__ == '__main__':
    main()
```
