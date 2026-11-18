<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/ReadAllPolyDataTypesDemo/ -->

# ReadAllPolyDataTypesDemo

Repository source: [ReadAllPolyDataTypesDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/ReadAllPolyDataTypesDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestReadAllPolyDataTypesDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestReadAllPolyDataTypesDemo.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadAllPolyDataTypesDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadAllPolyDataTypesDemo.py**

```python
#!/usr/bin/env python3

import math
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkPolyLine
)
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
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTextActor,
    vtkTextProperty,
)

def get_program_parameters():
    import argparse
    description = 'Read and display the PolyData types.'
    epilogue = '''
You can specify individual files as follows:
../../../src/Testing/Data -f "teapot.g"  "cowHead.vtp"  "horse.ply"
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path', help='The path to read the polydata files from.')
    parser.add_argument('-f', '--file_names', nargs='+', help='The files to use.',
                        action='append', default=None)
    args = parser.parse_args()
    return args.path, args.file_names

def main():
    colors = vtkNamedColors()

    fp, files = get_program_parameters()
    if not files:
        files = ['teapot.g', 'cowHead.vtp', 'horse.ply', 'trumpet.obj', '42400-IDGH.stl', 'v.vtk']
    else:
        # Flatten the list of lists.
        files = [val for sublist in files for val in sublist]
    if len(files) > 6:
        print('No more than six file names can be specified.')
        return

    path = Path(fp)
    if not path.is_dir():
        print(f'{path} must exist and be a folder.')
        return

    # Create one text property for all.
    text_property = vtkTextProperty(color=colors.GetColor3d('LightGoldenrodYellow'), bold=True, italic=True,
                                    shadow=True, font_family_as_string='Courier',
                                    font_size=16, justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                    vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_CENTERED)

    # Position text according to its length and centered in the viewport.
    text_positions = get_text_positions(files, justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                        vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_BOTTOM,
                                        width=0.5, height=0.1)

    # Setup viewports for the renderers.
    renderer_size = 400
    x_grid_dimensions = 3
    y_grid_dimensions = math.ceil(len(files) / x_grid_dimensions)
    width = renderer_size * x_grid_dimensions
    height = renderer_size * y_grid_dimensions

    # Create the renderer viewports.
    blank = len(files)
    viewports = dict()
    VP_Params = namedtuple('VP_Params', ['viewport', 'border'])
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
            vp_params = VP_Params(viewport, border)
            if index < blank:
                viewports[files[index]] = vp_params
            else:
                viewports[index] = vp_params

    ren_win = vtkRenderWindow(size=(width, height), window_name='ReadAllPolyDataTypesDemo')

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    text_widgets = list()
    for file in files:
        pth = path / file
        # Create a renderer.
        viewport = viewports[file].viewport
        border = viewports[file].border
        renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'), viewport=viewport)
        border_actor = draw_viewport_border(sides=border, border_color='Yellow', border_width=4)
        renderer.AddActor(border_actor)

        if pth.is_file():
            mapper = vtkPolyDataMapper()
            read_poly_data(pth) >> mapper
            actor = vtkActor(mapper=mapper)
            actor.property.diffuse_color = colors.GetColor3d('Light_salmon')
            actor.property.specular = 0.6
            actor.property.specular_power = 30

            renderer.AddActor(actor)

            # Create the text actor and representation.
            text_actor = vtkTextActor(input=file, text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE,
                                      text_property=text_property)

            # Create the text representation. Used for positioning the text actor.
            text_representation = vtkTextRepresentation(enforce_normalized_viewport_bounds=True)
            text_representation.position_coordinate.value = text_positions[file]['p']
            text_representation.position2_coordinate.value = text_positions[file]['p2']

            # Create the text widget, setting the default renderer and interactor.
            text_widget = vtkTextWidget(representation=text_representation, text_actor=text_actor,
                                        default_renderer=renderer, interactor=iren, selectable=False)
            text_widgets.append(text_widget)
        else:
            print(f'Nonexistent file: {pth}')
        ren_win.AddRenderer(renderer)

    for i in range(blank, x_grid_dimensions * y_grid_dimensions):
        viewport = viewports[i].viewport
        border = viewports[i].border
        renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'), viewport=viewport)
        border_actor = draw_viewport_border(sides=border, border_color='Yellow', border_width=4)
        renderer.AddActor(border_actor)
        ren_win.AddRenderer(renderer)

    for tw in text_widgets:
        tw.On()

    ren_win.Render()
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
    main()
```
