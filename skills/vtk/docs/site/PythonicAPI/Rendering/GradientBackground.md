<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/GradientBackground/ -->

# GradientBackground

Repository source: [GradientBackground](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/GradientBackground.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestGradientBackground.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestGradientBackground.png?raw=true target=)

### Description

Demonstrates the gradient backgrounds available in VTK.

The gradient background modes are:

- Vertical
- Horizontal
- Radial Farthest Side
- Radial Farthest Corner

The user can also edit the code to change the stop colors marking the beginning and end points in a gradient.

An option is provided for the user to read in a data file so that more interesting objects can be viewed.

The viewport border can also be set and colored.

For more information, see [New in VTK 9.3: Radial Gradient Background](https://www.kitware.com/new-in-vtk-9-3-radial-gradient-background/)

!!! note VTK 9.3 or later is required.

!!! note The C++ version requires C++ 17 or later as std::filesystem is used.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/GradientBackground/)), ([Python](../../Python/Rendering/GradientBackground.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GradientBackground.py**

```python
#!/usr/bin/env python3

# Based on:
#  https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/Core/Testing/Cxx/TestGradientBackground.cxx?ref_type=heads
# See:
#  [New in VTK 9.3: Radial Gradient Background](https://www.kitware.com/new-in-vtk-9-3-radial-gradient-background/)

from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkPolyLine
)
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
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
    vtkTextProperty,
    vtkViewport
)

def get_program_parameters(argv):
    import argparse
    description = 'Demonstrates the background shading options.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None,
                        help='An optional file name, e.g. star-wars-vader-tie-fighter.obj.')
    args = parser.parse_args()
    return args.file_name

def main(fn):
    if fn:
        fp = Path(fn)
        if not fp.is_file():
            print(f'The path: {fp} does not exist.')
            return
    else:
        fp = None

    pd = read_poly_data(fp)
    if not pd:
        # Default to a cone if the path is empty.
        source = vtkConeSource(resolution=25, direction=(0, 1, 0), height=1)
        pd = source.update().output

    colors = vtkNamedColors()

    mapper = vtkPolyDataMapper()
    pd >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('Honeydew')
    actor.property.specular = 0.3
    actor.property.specular_power = 60.0

    # Here we select and name the colors.
    # Feel free to change colors.
    bottom_color = colors.GetColor3d('Gold')
    top_color = colors.GetColor3d('OrangeRed')
    left_color = colors.GetColor3d('Gold')
    right_color = colors.GetColor3d('OrangeRed')
    center_color = colors.GetColor3d('Gold')
    side_color = colors.GetColor3d('OrangeRed')
    corner_color = colors.GetColor3d('OrangeRed')

    # For each gradient specify the mode.
    modes = [
        vtkViewport.GradientModes.VTK_GRADIENT_VERTICAL,
        vtkViewport.GradientModes.VTK_GRADIENT_HORIZONTAL,
        vtkViewport.GradientModes.VTK_GRADIENT_RADIAL_VIEWPORT_FARTHEST_SIDE,
        vtkViewport.GradientModes.VTK_GRADIENT_RADIAL_VIEWPORT_FARTHEST_CORNER,
    ]

    viewport_titles = (
        'Vertical',
        'Horizontal',
        'Radial Farthest Side',
        'Radial Farthest Corner',
    )
    text_positions = get_text_positions(viewport_titles, justification=TextProperty.Justification.VTK_TEXT_CENTERED)

    text_property = vtkTextProperty(color=colors.GetColor3d('MidnightBlue'),
                                    bold=False, italic=False, shadow=False,
                                    font_size=12, font_family_as_string='Courier',
                                    justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                    vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_CENTERED)

    # Setup viewports for the renderers.
    x_grid_dimensions = 2
    y_grid_dimensions = 2
    width = 640
    height = 480

    # Create the renderer viewports.
    blank = len(viewport_titles)
    viewports = dict()
    VP_Params = namedtuple('VP_Params', ['name', 'viewport', 'border'])
    last_col = False
    last_row = False
    for row in range(0, y_grid_dimensions):
        if row == y_grid_dimensions - 1:
            last_row = True
        for col in range(0, x_grid_dimensions):
            if col == x_grid_dimensions - 1:
                last_col = True
            index = row * x_grid_dimensions + col
            viewport = (
                col / x_grid_dimensions,
                (y_grid_dimensions - (row + 1)) / y_grid_dimensions,
                (col + 1) / x_grid_dimensions,
                (y_grid_dimensions - row) / y_grid_dimensions,
            )

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
                viewports[index] = VP_Params(viewport_titles[index], viewport, border)
            else:
                viewports[index] = VP_Params("", viewport, border)

    ren_win = vtkRenderWindow(size=(width, height), window_name='GradientBackground')

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    border_color = "Black"
    border_width = 4

    text_widgets = list()
    for i in range(0, len(viewports)):
        name = viewports[i].name
        viewport = viewports[i].viewport
        border = viewports[i].border
        renderer = vtkRenderer(background=bottom_color, viewport=viewport)
        border_actor = draw_viewport_border(sides=border, border_color=border_color, border_width=border_width)
        renderer.AddActor(border_actor)
        if not name:
            # Add a renderer even if the border is the only actor.
            # This makes the render window backgrounds have similar colors.
            ren_win.AddRenderer(renderer)
            continue
        renderer.gradient_background = True
        renderer.gradient_mode = modes[i]

        if i == 1:
            # Horizontal
            renderer.background = left_color
            renderer.background2 = right_color
        elif i == 2:
            # Radial Farthest Side
            renderer.background = center_color
            renderer.background2 = side_color
        elif i == 3:
            # Radial Farthest Corner
            renderer.background = center_color
            renderer.background2 = corner_color
        else:
            # Vertical
            renderer.background = bottom_color
            renderer.background2 = top_color

        renderer.AddActor(actor)

        # Create the text actor and representation.
        text_actor = vtkTextActor(input=name, text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE,
                                  text_property=text_property)

        # Create the text representation. Used for positioning the text actor.
        text_representation = vtkTextRepresentation(enforce_normalized_viewport_bounds=True)
        text_representation.position_coordinate.value = text_positions[name]['p']
        text_representation.position2_coordinate.value = text_positions[name]['p2']

        # Create the text widget, setting the default renderer and interactor.
        text_widget = vtkTextWidget(representation=text_representation, text_actor=text_actor,
                                    default_renderer=renderer, interactor=iren, selectable=False)
        text_widgets.append(text_widget)
        ren_win.AddRenderer(renderer)

    for tw in text_widgets:
        tw.On()

    ren_win.Render()
    iren.UpdateSize(width * 2, height * 2)
    iren.Start()

def read_poly_data(file_name):
    if not file_name:
        # print(f'No file name.')
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
    import sys

    file_path = get_program_parameters(sys.argv)
    main(file_path)
```
