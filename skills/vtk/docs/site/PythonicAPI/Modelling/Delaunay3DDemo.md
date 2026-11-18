<!-- source: https://examples.vtk.org/site/PythonicAPI/Modelling/Delaunay3DDemo/ -->

# Delaunay3DDemo

Repository source: [Delaunay3DDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Modelling/Delaunay3DDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Modelling/TestDelaunay3DDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Modelling/TestDelaunay3DDemo.png?raw=true target=)

### Description

This example creates a tetrahedral mesh from unorganized points. The example uses the [vtkDelaunay3D](https://www.vtk.org/doc/nightly/html/classvtkDelaunay3D.html) filter. The resulting mesh will be a solid convex hull of the original points. The example takes the points from a XML PolyData file (.vtp) produces the 3D Delaunay tetrahedralization (both with alpha = 0 and a non-zero alpha), and displays the result on the screen.

For alpha != 0 (right window), the tetra are yellow, the lines are blue and the triangles are red.

Alpha can be changed interactively to see its effect on the resulting surface.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Modelling/Delaunay3DDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Delaunay3DDemo.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkUnsignedCharArray, vtkCommand
)
from vtkmodules.vtkCommonDataModel import (
    VTK_LINE, VTK_TETRA, VTK_TRIANGLE, VTK_VERTEX
)
from vtkmodules.vtkFiltersCore import (
    vtkCleanPolyData,
    vtkDelaunay3D
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionWidgets import (
    vtkSliderRepresentation2D,
    vtkSliderWidget,
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTextProperty,
    vtkTextActor
)

def get_program_parameters():
    import argparse
    description = 'Delaunay 3D demonstration.'
    epilogue = '''
    If no filename is specified, a sphere is used.
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', type=str, nargs='?', default='',
                        help='The path to the polydata file e.g. Bunny.vtp.')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()

    if file_name:
        fn = Path(file_name)
        if not fn.is_file():
            print(f'{fn}\nNot found.')
            return
        else:
            poly_data = read_poly_data(file_name=fn)
    else:
        source = vtkSphereSource(phi_resolution=50, theta_resolution=50)
        poly_data = source.update().output

    original_mapper = vtkDataSetMapper(input_data=poly_data, scalar_visibility=False,
                                       scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_CELL_DATA)

    original_actor = vtkActor(mapper=original_mapper)
    original_actor.property.color = colors.GetColor3d('Tomato')
    original_actor.property.interpolation = Property.Interpolation.VTK_FLAT

    # Clean the polydata. This will remove duplicate points that may be
    # present in the input data.
    cleaner = vtkCleanPolyData(input_data=poly_data)

    # Generate a tetrahedral mesh from the input points. By
    # default, the generated volume is the convex hull of the points.
    delaunay_3d = vtkDelaunay3D()

    delaunay_mapper = vtkDataSetMapper(scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_CELL_DATA)
    cleaner >> delaunay_3d >> delaunay_mapper

    delaunay_actor = vtkActor(mapper=delaunay_mapper)
    delaunay_actor.SetMapper(delaunay_mapper)
    delaunay_actor.property.color = colors.GetColor3d('Banana')
    delaunay_actor.property.interpolation = Property.Interpolation.VTK_FLAT

    # Generate a mesh from the input points. If Alpha is non-zero, then
    # tetrahedra, triangles, edges and vertices that lie within the
    # alpha radius are output.
    delaunay_3d_alpha = vtkDelaunay3D(alpha=0.0105)
    cleaner >> delaunay_3d_alpha
    # delaunay_3d_alpha.update()

    cell_data, num_tetras, num_lines, num_tris, num_verts = get_cell_types(delaunay_3d_alpha, colors)
    print(f'Tetras: {num_tetras} Lines:  {num_lines} Triangles: {num_tris} Vertices: {num_verts}')
    ss = f'   Tetras: {num_tetras:3d}\n    Lines: {num_lines:3d}\nTriangles: {num_tris:3d}\n Vertices: {num_verts:3d}'

    # Set the cell color depending on cell type.
    delaunay_3d_alpha.output.GetCellData().SetScalars(cell_data)

    delaunay_alpha_mapper = vtkDataSetMapper(scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_CELL_DATA)
    cleaner >> delaunay_3d_alpha >> delaunay_alpha_mapper

    delaunay_alpha_actor = vtkActor(mapper=delaunay_alpha_mapper)
    delaunay_alpha_actor.property.point_size = 5.0
    delaunay_alpha_actor.property.interpolation = Property.Interpolation.VTK_FLAT

    # Visualize
    # Define viewport ranges.
    # (xmin, ymin, xmax, ymax)
    left_viewport = [0.0, 0.0, 0.33, 1.0]
    center_viewport = [0.33, 0.0, 0.66, 1.0]
    right_viewport = [0.66, 0.0, 1.0, 1.0]

    # Shared camera
    shared_camera = vtkCamera()

    # Create the renderers, render window, and interactor.
    original_renderer = vtkRenderer(viewport=left_viewport, use_hidden_line_removal=True,
                                    background=colors.GetColor3d('Slate_Grey'), active_camera=shared_camera)
    delaunay_renderer = vtkRenderer(viewport=center_viewport, use_hidden_line_removal=True,
                                    background=colors.GetColor3d('Light_Grey'), active_camera=shared_camera)
    delaunay_alpha_renderer = vtkRenderer(viewport=right_viewport, use_hidden_line_removal=True,
                                          background=colors.GetColor3d('Grey'), active_camera=shared_camera)

    render_window = vtkRenderWindow(size=(1200, 400), window_name='Delaunay3DDemo')

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(delaunay_renderer)
    render_window.AddRenderer(delaunay_alpha_renderer)

    text_property = vtkTextProperty(color=colors.GetColor3d('Black'), bold=True, italic=False, shadow=False,
                                    line_spacing=1.0, font_family_as_string='Courier',
                                    font_size=24,
                                    justification=TextProperty.Justification.VTK_TEXT_LEFT,
                                    vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_BOTTOM)
    text_actor = vtkTextActor(input=ss, text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_VIEWPORT,
                              text_property=text_property)
    # Create the text representation. Used for positioning the text actor.
    text_representation = vtkTextRepresentation(enforce_normalized_viewport_bounds=True)
    text_representation.position_coordinate.value = (0.005, 0.005)
    text_representation.position2_coordinate.value = (0.3, 0.2)

    # Create the text widget, setting the default renderer and interactor.
    text_widget = vtkTextWidget(representation=text_representation, text_actor=text_actor,
                                default_renderer=delaunay_alpha_renderer, interactor=render_window_interactor,
                                selectable=False)

    # Set up a slider widget for each varying parameter.
    slider_properties = make_slider_2d_properties()

    slider_properties.Colors.bar_ends_color = 'DarkSlateBlue'
    slider_properties.Colors.bar_color = 'Gold'
    slider_properties.Colors.title_color = 'Black'
    slider_properties.Colors.label_color = 'Black'

    slider_properties.Range.maximum_value = 0.0233
    slider_properties.Range.minimum_value = 0.0001
    slider_properties.Range.value = 0.0105

    slider_properties.Dimensions.tube_width = 0.02
    slider_properties.Dimensions.slider_length = 0.04
    slider_properties.Dimensions.slider_width = 0.04
    slider_properties.Dimensions.end_cap_length = slider_properties.Dimensions.tube_width * 1.5
    slider_properties.Dimensions.slider_width = slider_properties.Dimensions.tube_width * 1.5
    slider_properties.Dimensions.label_height = 0.035
    slider_properties.Dimensions.title_height = 0.045

    slider_properties.Position.point1 = (0.1, 0.1)
    slider_properties.Position.point2 = (0.9, 0.1)

    slider_properties.Text.title = 'Alpha'
    slider_properties.Text.title_shadow = False
    slider_properties.Text.label_shadow = False

    slider_widget_alpha = make_2d_slider_widget(slider_properties, render_window_interactor)
    slider_widget_alpha.AddObserver(vtkCommand.InteractionEvent,
                                    SliderCallbackAlpha(delaunay_3d_alpha, text_actor, colors))

    original_renderer.AddActor(original_actor)
    delaunay_renderer.AddActor(delaunay_actor)
    delaunay_alpha_renderer.AddActor(delaunay_alpha_actor)
    delaunay_alpha_renderer.AddViewProp(text_actor)

    original_renderer.ResetCamera()
    render_window.Render()

    text_widget.On()

    # Render and interact.
    render_window_interactor.Start()

def make_slider_2d_properties():
    """
    This applies more specific values to the default Slider2DProperties.

    :return: The slider 2D properties.
    """
    sp = Slider2DProperties()

    sp.Colors.title_color = 'AliceBlue'
    sp.Colors.label_color = 'AliceBlue'
    sp.Colors.slider_color = 'Green'
    sp.Colors.bar_color = 'MistyRose'
    sp.Colors.bar_ends_color = 'Yellow'
    sp.Colors.selected_color = 'DeepPink'

    sp.Dimensions.slider_length = 0.05
    sp.Dimensions.slider_width = 0.025
    sp.Dimensions.end_cap_length = 0.02
    sp.Dimensions.title_height = 0.045
    sp.Dimensions.label_height = 0.035

    sp.Position.point1 = (0.3, 0.1)
    sp.Position.point2 = (0.7, 0.1)

    sp.Range.minimum_value = 3
    sp.Range.maximum_value = 20

    return sp

def make_2d_slider_widget(properties, interactor):
    """
    Make a 2D slider widget.

    :param properties: The 2D slider properties.
    :param interactor: The vtkInteractor.
    :return: The slider widget.
    """
    colors = vtkNamedColors()

    slider_rep = vtkSliderRepresentation2D(minimum_value=properties.Range.minimum_value,
                                           maximum_value=properties.Range.maximum_value,
                                           value=properties.Range.value,
                                           title_text=properties.Text.title,
                                           tube_width=properties.Dimensions.tube_width,
                                           slider_length=properties.Dimensions.slider_length,
                                           slider_width=properties.Dimensions.slider_width,
                                           end_cap_length=properties.Dimensions.end_cap_length,
                                           end_cap_width=properties.Dimensions.end_cap_width,
                                           title_height=properties.Dimensions.title_height,
                                           label_height=properties.Dimensions.label_height,
                                           )

    # Set the color properties.
    slider_rep.title_property.color = colors.GetColor3d(properties.Colors.title_color)
    slider_rep.label_property.color = colors.GetColor3d(properties.Colors.label_color)
    slider_rep.tube_property.color = colors.GetColor3d(properties.Colors.bar_color)
    slider_rep.cap_property.color = colors.GetColor3d(properties.Colors.bar_ends_color)
    slider_rep.slider_property.color = colors.GetColor3d(properties.Colors.slider_color)
    slider_rep.selected_property.color = colors.GetColor3d(properties.Colors.selected_color)

    # Set the position.
    slider_rep.point1_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point1_coordinate.value = properties.Position.point1
    slider_rep.point2_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point2_coordinate.value = properties.Position.point2

    title_font_family = properties.Text.title_font_family
    match title_font_family:
        case 'Courier':
            slider_rep.title_property.SetFontFamilyToCourier()
        case 'Times':
            slider_rep.title_property.SetFontFamilyToTimes()
        case _:
            slider_rep.title_property.SetFontFamilyToArial()
    slider_rep.title_property.bold = properties.Text.title_bold
    slider_rep.title_property.italic = properties.Text.title_italic
    slider_rep.title_property.shadow = properties.Text.title_shadow
    label_font_family = properties.Text.label_font_family
    match label_font_family:
        case 'Courier':
            slider_rep.label_property.SetFontFamilyToCourier()
        case 'Times':
            slider_rep.label_property.SetFontFamilyToTimes()
        case _:
            slider_rep.label_property.SetFontFamilyToArial()
    slider_rep.label_property.bold = properties.Text.label_bold
    slider_rep.label_property.italic = properties.Text.label_italic
    slider_rep.label_property.shadow = properties.Text.label_shadow

    # widget = vtkSliderWidget(representation=slider_rep, interactor=interactor, enabled=True)
    widget = vtkSliderWidget(interactor=interactor)
    widget.SetRepresentation(slider_rep)
    widget.EnabledOn()
    widget.SetAnimationModeToAnimate()
    widget.number_of_animation_steps = 2

    return widget

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

@dataclass
class Slider2DProperties:
    @dataclass
    class Colors:
        # The color of the text indicating what the slider controls.
        title_color: str = 'White'
        # The color of the text displaying the value.
        label_color: str = 'White'
        # The color of the knob that slides.
        slider_color: str = 'White'
        # The color of the knob when the mouse is held on it.
        selected_color: str = 'HotPink'
        # The color of the bar.
        bar_color: str = 'White'
        # The color of the ends of the bar.
        bar_ends_color: str = 'White'

    @dataclass
    class Dimensions:
        tube_width: float = 0.008
        slider_length: float = 0.01
        slider_width: float = 0.02
        end_cap_length: float = 0.005
        end_cap_width: float = 0.05
        title_height: float = 0.03
        label_height: float = 0.025

    @dataclass
    class Position:
        coordinate_system: int = Coordinate.CoordinateSystem.VTK_NORMALIZED_VIEWPORT
        point1: Tuple = (0.1, 0.1)
        point2: Tuple = (0.9, 0.1)

    @dataclass
    class Range:
        minimum_value: float = 0.0
        maximum_value: float = 1.0
        value: float = 0.0

    @dataclass
    class Text:
        # Font families are: Ariel, Courier and Times
        title: str = ''
        title_font_family = 'Arial'
        title_bold: bool = True
        title_italic: bool = False
        title_shadow: bool = True
        label_font_family = 'Arial'
        label_bold: bool = True
        label_italic: bool = False
        label_shadow: bool = True

# This callback does the actual work.
class SliderCallbackAlpha:
    def __init__(self, delaunay, text_mapper, colors):
        self.delaunay = delaunay
        self.text_mapper = text_mapper
        self.colors = colors

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.delaunay.alpha = value
        cell_data, num_tetras, num_lines, num_tris, num_verts = get_cell_types(self.delaunay, self.colors)
        # Set the cell color depending on cell type.
        self.delaunay.output.GetCellData().SetScalars(cell_data)

        ss = (f'   Tetras: {num_tetras:3d}\n    Lines: {num_lines:3d}\n'
              f'Triangles: {num_tris:3d}\n Vertices: {num_verts:3d}')
        self.text_mapper.SetInput(ss)

def get_cell_types(cells, colors):
    cell_data = vtkUnsignedCharArray()
    cell_data.SetNumberOfComponents(3)

    num_tetras = 0
    num_lines = 0
    num_tris = 0
    num_verts = 0

    it = cells.update().output.NewCellIterator()

    while not it.IsDoneWithTraversal():
        if it.GetCellType() == VTK_TETRA:
            num_tetras += 1
            cell_data.InsertNextTypedTuple(colors.GetColor3ub('Banana'))
        if it.GetCellType() == VTK_LINE:
            num_lines += 1
            cell_data.InsertNextTypedTuple(colors.GetColor3ub('Peacock'))
        if it.GetCellType() == VTK_TRIANGLE:
            num_tris += 1
            cell_data.InsertNextTypedTuple(colors.GetColor3ub('Tomato'))
        if it.GetCellType() == VTK_VERTEX:
            num_verts += 1
            cell_data.InsertNextTypedTuple(colors.GetColor3ub('Lime'))
        it.GoToNextCell()

    return cell_data, num_tetras, num_lines, num_tris, num_verts

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
