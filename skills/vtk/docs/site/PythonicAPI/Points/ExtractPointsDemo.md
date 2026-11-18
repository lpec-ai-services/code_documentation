<!-- source: https://examples.vtk.org/site/PythonicAPI/Points/ExtractPointsDemo/ -->

# ExtractPointsDemo

Repository source: [ExtractPointsDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Points/ExtractPointsDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestExtractPointsDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestExtractPointsDemo.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Points/ExtractPointsDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractPointsDemo.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

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
    vtkCone,
    vtkCylinder,
    vtkPolyData,
    vtkPolyLine,
    vtkSphere,
    vtkSuperquadric
)
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersPoints import (
    vtkBoundedPointSource,
    vtkExtractPoints
)
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkCylinderSource,
    vtkSphereSource,
    vtkSuperquadricSource
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkActor2D,
    vtkCoordinate,
    vtkGlyph3DMapper,
    vtkPolyDataMapper,
    vtkPolyDataMapper2D,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTextActor,
    vtkTextProperty
)

def get_program_parameters():
    import argparse
    description = 'Extracting points inside implicit functions.'
    epilogue = '''
        Points corresponding to the interior of implicit functions are extracted and rendered.
        Additionally, a corresponding source object is provided to help the visualisation.
        An option is provided to control the opacity of the source object.
    '''

    def to_float(s):
        res = float(s)
        res = abs(res)
        if res > 1:
            res = 1
        return res

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-o', '--opacity', type=to_float, default=0.1, help='Set the opacity of the source object.')
    args = parser.parse_args()
    return args.opacity

def main():
    src_opacity = get_program_parameters()

    # Create source functions.
    cone = vtkConeSource(angle=30.0)
    trans = vtkTransform()
    trans.RotateY(180)
    trans.Translate(-0.5, 0, 0)
    tf = vtkTransformFilter(transform=trans)
    cone >> tf

    src_functions = dict()
    src_functions['Sphere'] = vtkSphereSource()
    src_functions['Cone'] = tf
    src_functions['Cylinder'] = vtkCylinderSource(height=2)
    src_functions['Superquadric'] = vtkSuperquadricSource(phi_roundness=2.5, theta_roundness=0.5)

    # Create implicit functions.
    functions = dict()
    functions['Sphere'] = vtkSphere()
    functions['Cone'] = vtkCone(angle=30.0, is_double_cone=False)
    functions['Cylinder'] = vtkCylinder()
    functions['Superquadric'] = vtkSuperquadric(phi_roundness=2.5, theta_roundness=0.5)

    renderer_size = 512
    iren = vtkRenderWindowInteractor()
    ren_win = vtkRenderWindow(size=(renderer_size, renderer_size), window_name='ExtractPointsDemo')
    ren_win.interactor = iren

    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    renderers = dict()

    colors = vtkNamedColors()
    obj_names = ['SphereBkg', 'ConeBkg', 'CylinderBkg', 'SuperquadricBkg']
    bkg = (102, 128, 154, 154, 128, 102)
    for name in obj_names:
        colors.SetColor(name, *bkg[:3])
        # Left rotate by one position.
        bkg = bkg[1:] + bkg[:1]

    # Parameters for the renderers.
    # Viewport bounds: (x0, y0, x1, y1), renderer background color
    #  and borders for the viewports: (top, left, bottom, right).
    ren_params = {
        'Sphere': VParams((0.0, 0.5, 0.5, 1.0), colors.GetColor3d('SphereBkg'), (True, True, True, False)),
        'Cone': VParams((0.5, 0.5, 1.0, 1.0), colors.GetColor3d('ConeBkg'), (True, True, True, True)),
        'Cylinder': VParams((0.0, 0.0, 0.5, 0.5), colors.GetColor3d('CylinderBkg'), (False, True, True, False)),
        'Superquadric': VParams((0.5, 0.0, 1.0, 0.5), colors.GetColor3d('SuperquadricBkg'), (False, True, True, True)),
    }

    # Position text according to its length and centered in the viewport.
    text_positions = get_text_positions(ren_params.keys(),
                                        justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                        vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_BOTTOM,
                                        width=0.85, height=0.1)

    text_representations = dict()
    text_actors = dict()
    text_widgets = dict()

    border_color = 'DarkGreen'
    border_width = 4.0

    point_source = vtkBoundedPointSource(number_of_points=100000)
    # Glyphs
    radius = 0.02
    sphere_source = vtkSphereSource(radius=radius)
    sphere_source.SetRadius(radius)

    for k in ren_params.keys():

        mapper = vtkPolyDataMapper()
        src_functions[k] >> mapper
        actor = vtkActor(mapper=mapper)
        actor.property.color = colors.GetColor3d('CornflowerBlue')
        actor.property.opacity = src_opacity
        actor.property.edge_visibility = True

        extract = vtkExtractPoints(implicit_function=functions[k])
        point_source >> extract

        glyph_mapper = vtkGlyph3DMapper(source_data=sphere_source.update().output, scaling=False)
        extract >> glyph_mapper
        glyph_actor = vtkActor(mapper=glyph_mapper)
        glyph_actor.property.color = colors.GetColor3d('MistyRose')

        renderer = vtkRenderer(background=ren_params[k].bkg_color)
        renderer.SetViewport(ren_params[k].viewport)
        viewport_border(renderer, ren_params[k].borders, border_color, border_width)

        renderer.AddActor(actor)
        renderer.AddActor(glyph_actor)

        # Create the text actor and representation.
        text_property = get_text_property()
        text_property.SetFontSize(renderer_size // 24)
        text_actor = vtkTextActor(input=k,
                                  text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE,
                                  text_property=text_property)
        # Create the text representation. Used for positioning the text actor.
        text_representation = vtkTextRepresentation(enforce_normalized_viewport_bounds=True)
        text_representation.position_coordinate.value = text_positions[k]['p']
        text_representation.position2_coordinate.value = text_positions[k]['p2']
        # Create the text widget, setting the default renderer and interactor.
        text_widget = vtkTextWidget(representation=text_representation, text_actor=text_actor,
                                    default_renderer=renderer, interactor=iren, selectable=False)

        text_actors[k] = text_actor
        text_representations[k] = text_representation
        text_widgets[k] = text_widget

        renderer.ResetCamera()
        renderer.active_camera.Azimuth(30)
        renderer.active_camera.Elevation(-30)
        if k == "Cylinder":
            renderer.active_camera.Dolly(0.8)
        else:
            renderer.active_camera.Dolly(1.0)
        renderer.ResetCameraClippingRange()

        renderers[k] = renderer

        ren_win.AddRenderer(renderer)

    for k in ren_params.keys():
        text_widgets[k].On()

    ren_win.Render()

    iren.Initialize()
    iren.UpdateSize(renderer_size * 2, renderer_size * 2)

    iren.Start()

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

def get_text_property():
    colors = vtkNamedColors()

    return vtkTextProperty(color=colors.GetColor3d('MidnightBlue'),
                           bold=True, italic=False, shadow=False,
                           font_family_as_string='Courier',
                           justification=TextProperty.Justification.VTK_TEXT_CENTERED)

def viewport_border(renderer, sides, border_color, border_width):
    """
    Set a border around a viewport.

    :param renderer: The renderer corresponding to the viewport.
    :param sides: An array of boolean corresponding to [top, left, bottom, right]
    :param border_color: The color of the border.
    :param border_width: The width of the border.
    :return:
    """
    colors = vtkNamedColors()

    # Points start at upper right and proceed anti-clockwise.
    points = vtkPoints()
    points.SetNumberOfPoints(4)
    points.InsertPoint(0, 1, 1, 0)
    points.InsertPoint(1, 0, 1, 0)
    points.InsertPoint(2, 0, 0, 0)
    points.InsertPoint(3, 1, 0, 0)

    cells = vtkCellArray()
    cells.Initialize()

    if sides[0]:
        # Top
        top = vtkPolyLine()
        top.GetPointIds().SetNumberOfIds(2)
        top.GetPointIds().SetId(0, 0)
        top.GetPointIds().SetId(1, 1)
        cells.InsertNextCell(top)
    if sides[1]:
        # Left
        left = vtkPolyLine()
        left.GetPointIds().SetNumberOfIds(2)
        left.GetPointIds().SetId(0, 1)
        left.GetPointIds().SetId(1, 2)
        cells.InsertNextCell(left)
    if sides[2]:
        # Bottom
        bottom = vtkPolyLine()
        bottom.GetPointIds().SetNumberOfIds(2)
        bottom.GetPointIds().SetId(0, 2)
        bottom.GetPointIds().SetId(1, 3)
        cells.InsertNextCell(bottom)
    if sides[3]:
        # Right
        right = vtkPolyLine()
        right.GetPointIds().SetNumberOfIds(2)
        right.GetPointIds().SetId(0, 3)
        right.GetPointIds().SetId(1, 0)
        cells.InsertNextCell(right)

    # Now make the polydata and display it.
    poly = vtkPolyData()
    poly.Initialize()
    poly.SetPoints(points)
    poly.SetLines(cells)

    # Use normalized viewport coordinates since
    # they are independent of window size.
    coordinate = vtkCoordinate()
    coordinate.SetCoordinateSystemToNormalizedViewport()

    mapper = vtkPolyDataMapper2D()
    mapper.SetInputData(poly)
    mapper.SetTransformCoordinate(coordinate)

    actor = vtkActor2D()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d(border_color))

    # Line width should be at least 2 to be visible at extremes.
    actor.GetProperty().SetLineWidth(border_width)

    renderer.AddViewProp(actor)

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

@dataclass
class VParams:
    # The bounds for the viewport: (x0, y0, x1, y1)
    viewport: tuple
    # The color (r, g, b)
    bkg_color: list
    # The borders for the viewports: (top, left, bottom, right).
    borders: tuple

if __name__ == '__main__':
    main()
```
