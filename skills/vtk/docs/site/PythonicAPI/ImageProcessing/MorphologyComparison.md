<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageProcessing/MorphologyComparison/ -->

# MorphologyComparison

Repository source: [MorphologyComparison](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageProcessing/MorphologyComparison.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageProcessing/TestMorphologyComparison.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageProcessing/TestMorphologyComparison.png?raw=true target=)

### Description

Although preprocessing can do a lot to improve segmentation results, postprocessing can also be useful. Morphological filters, which operate on binary or discrete images, can be useful for manipulating the shape of the segmented regions. In this brief discussion we will only consider operations that use circular footprints, even though these morphological filters can be defined much more generally.

Erosion is implemented by removing pixels within a specified distance of a border. For each pixel not in the segmented region, all the neighbors in a circular region around the pixels are turned off. This erosion filter shrinks the segmented region and small isolated regions disappear.

The opposite of erosion is dilation. This filter grows the area of segmented regions. Small holes in the segmented region are completely closed. Any pixel not in the segmented region but near the region is turned on.

Dilation and erosion are dual filters with nearly identical implementations. Dilating the “on” pixels is equivalent to eroding “off” pixels in a binary image. Holes in the map disappear. However, dilation alone also grows the boundaries of the segmented regions. When dilation is followed by erosion in a closing operation, small holes are removed; however, the boundary of the segmented regions remain in the same general location.

Opening is the dual of closing. Opening removes small islands of pixels. It is implemented with an initial erosion, followed by a dilation.

Connectivity filters can also remove small regions without affecting the remaining boundaries of segmented regions. This set of filters separate the segmented pixels into equivalence classes based on a neighbor relation. Two pixels belong to the same class if they are touching. There are two common neighbor relations in two-dimensional images: four connectivity considers pixels neighbors if they are edge neighbors, and eight connectivity considers pixels neighbors if pixels share any vertex.

This example demonstrates various binary filters that can alter the shape of segmented regions. From left to right, top to bottom: original image, connectivity, erosion, dilation, opening, closing.

Info

See [this figure](../../VTKBook/10Chapter10.md#Figure%2010-14) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/MorphologyComparison/)), ([Python](../../Python/ImageProcessing/MorphologyComparison.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MorphologyComparison.py**

```python
#!/usr/bin/env python3

from collections import namedtuple
from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkCellArray, vtkPolyData, vtkPolyLine
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingMorphological import (
    vtkImageDilateErode3D,
    vtkImageSeedConnectivity
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkInteractionWidgets import (
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkCoordinate,
    vtkImageActor,
    vtkImageProperty,
    vtkPolyDataMapper2D,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTextActor,
    vtkTextProperty
)

def get_program_parameters():
    import argparse
    description = 'Demonstrate various binary filters that can alter the shape of segmented regions.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='binary.pgm')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()

    # Read the image.
    reader = vtkImageReader2Factory().CreateImageReader2(file_name)
    reader.file_name = file_name

    kernel_size = (31, 31, 1)

    img_property = vtkImageProperty(interpolation_type=ImageProperty.InterpolationType.VTK_NEAREST_INTERPOLATION)

    # Dilate
    dilate = vtkImageDilateErode3D(dilate_value=0, erode_value=255, kernel_size=kernel_size)

    # Erode
    erode = vtkImageDilateErode3D(dilate_value=255, erode_value=0, kernel_size=kernel_size)

    # Opening - dilate then erode.
    dilate1 = vtkImageDilateErode3D(dilate_value=0, erode_value=255, kernel_size=kernel_size)
    erode1 = vtkImageDilateErode3D(dilate_value=255, erode_value=0, kernel_size=kernel_size)

    # Closing - erode then dilate.
    erode2 = vtkImageDilateErode3D(dilate_value=255, erode_value=0, kernel_size=kernel_size)
    dilate2 = vtkImageDilateErode3D(dilate_value=0, erode_value=255, kernel_size=kernel_size)

    # Connectivity
    con = vtkImageSeedConnectivity(input_connect_value=0, output_connected_value=0, output_unconnected_value=255)
    con.AddSeed(300, 200)

    # Link the actors to the pipelines.
    actors = dict()

    actors['Original'] = vtkImageActor(property=img_property)
    reader >> actors['Original'].mapper

    actors['Connectivity'] = vtkImageActor(property=img_property)
    reader >> con >> actors['Connectivity'].mapper

    actors['Erosion'] = vtkImageActor(property=img_property)
    reader >> erode >> actors['Erosion'].mapper

    actors['Dilation'] = vtkImageActor(property=img_property)
    reader >> dilate >> actors['Dilation'].mapper

    actors['Opening'] = vtkImageActor(property=img_property)
    reader >> erode2 >> dilate2 >> actors['Opening'].mapper

    actors['Closing'] = vtkImageActor(property=img_property)
    reader >> dilate1 >> erode1 >> actors['Closing'].mapper

    keys = list(actors.keys())

    # Define the size of the grid that will hold the objects.
    grid_cols = 2
    grid_rows = 3
    # Define side length (in pixels) of each renderer rectangle.
    col_size = 595
    row_size = 428
    size = (col_size * grid_cols, row_size * grid_rows)
    ren_win = vtkRenderWindow(size=size, window_name='MorphologyComparison')

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleImage()
    iren.interactor_stype = style

    viewports = dict()
    VP_Params = namedtuple('VP_Params', ['viewport', 'border'])
    last_col = False
    last_row = False
    for row in range(0, grid_rows):
        if row == grid_rows - 1:
            last_row = True
        for col in range(0, grid_cols):
            if col == grid_cols - 1:
                last_col = True
            index = row * grid_cols + col
            # (x_min, y_min, x_max, y_max)
            viewport = (
                float(col) / grid_cols,
                float(grid_rows - row - 1) / grid_rows,
                float(col + 1) / grid_cols,
                float(grid_rows - row) / grid_rows
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
            viewports[keys[index]] = vp_params

    # Add the actors to the renderers.
    renderers = dict()
    for k in actors.keys():
        renderers[k] = vtkRenderer(background=colors.GetColor3d("LightSlateGray"), viewport=viewports[k].viewport)
        renderers[k].AddActor(actors[k])
        ren_win.AddRenderer(renderers[k])

    # Create one text property for all.
    text_property = vtkTextProperty(color=colors.GetColor3d('LightGoldenrodYellow'), bold=True, italic=True,
                                    shadow=True, font_family_as_string='Courier',
                                    font_size=16, justification=TextProperty.Justification.VTK_TEXT_CENTERED)
    text_positions = get_text_positions(keys, justification=TextProperty.Justification.VTK_TEXT_CENTERED, width=0.5)

    # Create the text widgets.
    text_representations = list()
    text_actors = list()
    text_widgets = list()
    index = 0
    for k in actors.keys():
        # Create the text actor and representation.
        text_actors.append(
            vtkTextActor(input=k,
                         text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE,
                         text_property=text_property))

        # Create the text representation. Used for positioning the text actor.
        text_representations.append(vtkTextRepresentation(enforce_normalized_viewport_bounds=True))
        text_representations[index].position_coordinate.value = text_positions[k]['p']
        text_representations[index].position2_coordinate.value = text_positions[k]['p2']

        # Create the text widget, setting the default renderer and interactor.
        text_widgets.append(
            vtkTextWidget(representation=text_representations[index], text_actor=text_actors[index],
                          default_renderer=renderers[k], interactor=iren, selectable=False))
        index += 1

    # Draw a line around the viewport of each renderer.
    for k in actors.keys():
        border = viewports[k].border
        border_actor = draw_viewport_border(sides=border, border_color='Yellow', border_width=4)
        renderers[k].AddActor(border_actor)

    # The renderers share one camera.
    ren_win.Render()
    renderers['Original'].active_camera.Dolly(1.35)
    renderers['Original'].ResetCameraClippingRange()
    camera = renderers['Original'].active_camera
    for k in actors.keys():
        if k != 'Original':
            renderers[k].SetActiveCamera(camera)
    ren_win.Render()

    for tw in text_widgets:
        tw.On()

    iren.Initialize()
    iren.Start()

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
class ImageProperty:
    @dataclass(frozen=True)
    class InterpolationType:
        VTK_NEAREST_INTERPOLATION: int = 0
        VTK_LINEAR_INTERPOLATION: int = 1
        VTK_CUBIC_INTERPOLATION: int = 2

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
