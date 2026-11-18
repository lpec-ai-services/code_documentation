<!-- source: https://examples.vtk.org/site/PythonicAPI/Snippets/DrawViewportBorder/ -->

# DrawViewportBorder

### Description

Draw a border around a renderer's viewport.

To use the snippet, click the *Copy to clipboard* at the upper right of the code blocks.

### Implementation

```python
# from dataclasses import dataclass
#
# from vtkmodules.vtkCommonColor import vtkNamedColors
# from vtkmodules.vtkCommonCore import vtkPoints
# from vtkmodules.vtkCommonDataModel import (
#     vtkCellArray,
#     vtkPolyData,
#     vtkPolyLine
# )
# from vtkmodules.vtkRenderingCore import (
#     vtkActor2D,
#     vtkCoordinate,
#     vtkPolyDataMapper2D
# )

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
```

### Usage

```python
border_actor = draw_viewport_border(sides=border, border_color='Yellow', border_width=4)
```
