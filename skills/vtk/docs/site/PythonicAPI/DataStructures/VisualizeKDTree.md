<!-- source: https://examples.vtk.org/site/PythonicAPI/DataStructures/VisualizeKDTree/ -->

# VisualizeKDTree

Repository source: [VisualizeKDTree](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/DataStructures/VisualizeKDTree.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/DataStructures/TestVisualizeKDTree.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/DataStructures/TestVisualizeKDTree.png?raw=true target=)

### Description

This demo displays the levels of a [vtkKdTree](https://www.vtk.org/doc/nightly/html/classvtkKdTree.html) using a slider. A KdTree is an [k-d tree](https://en.wikipedia.org/wiki/K-d_tree). It is used in fast intersection tests, collision detection and point location.

Here's the embedded video:

a

Seealso

[VisualizeOBBTree](VisualizeOBBTree.md) and [VisualizeModifiedBSPTree](VisualizeModifiedBSPTree.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/DataStructures/VisualizeKDTree/)), ([Java](https://examples.vtk.org/site/Java/DataStructures/VisualizeKDTree/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**VisualizeKDTree.py**

```python
#!/usr/bin/env python3
import sys
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Tuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkCommand
)
from vtkmodules.vtkCommonDataModel import vtkPolyData, vtkKdTree
from vtkmodules.vtkFiltersSources import (
    vtkSphereSource
)
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
    vtkSliderWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Display the level of a vtkKdTree using a slider.'
    epilogue = '''
    If no filename is specified,a sphere is used.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', type=str, nargs='?', default='',
                        help='The path to the data file e.g. shark.ply.')
    args = parser.parse_args()
    return args.filename

def main():
    filename = get_program_parameters()
    pth = Path(filename)
    if pth.is_file():
        pd = read_poly_data(pth)
    else:
        source = vtkSphereSource(phi_resolution=50, theta_resolution=50)
        pd = source.update().output

    colors = vtkNamedColors()

    points_mapper = vtkPolyDataMapper(input_data=pd, scalar_visibility=False)

    points_property = vtkProperty(color=colors.GetColor3d("Yellow"), opacity=0.3)
    points_property.SetInterpolationToFlat()

    points_actor = vtkActor(mapper=points_mapper, property=points_property)

    # Create the tree.
    max_levels = 5
    kd_tree = vtkKdTree(data_set=pd, max_level=max_levels)
    kd_tree.BuildLocator()

    # Initialize the representation.
    polydata = vtkPolyData()
    kd_tree.GenerateRepresentation(0, polydata)

    kd_tree_mapper = vtkPolyDataMapper(input_data=polydata)

    kd_tree_property = vtkProperty(color=colors.GetColor3d("SpringGreen"), opacity=0.5, edge_visibility=True)
    kd_tree_property.SetInterpolationToFlat()

    kd_tree_actor = vtkActor(mapper=kd_tree_mapper, property=kd_tree_property)

    ren = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    ren.UseHiddenLineRemovalOn()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(ren)
    # Set a background color for the renderer and set the name and
    # size of the render window (expressed in pixels).
    ren_win = vtkRenderWindow(size=(600, 600),
                              window_name=f'{Path(sys.argv[0]).stem:s}')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    # Add the actors to the scene.
    ren.AddActor(points_actor)
    ren.AddActor(kd_tree_actor)

    ren_win.Render()

    sp = make_slider_2d_properties()
    sp.Range.minimum_value = 0
    sp.Range.maximum_value = kd_tree.max_level
    # Use C++ rounding where 0.5 or -0.5 is rounded away from zero to 1 or -1.
    sp.Range.value = int(Decimal(str(kd_tree.max_level / 2)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

    sp.Text.title = 'Level'

    kd_tree.GenerateRepresentation(sp.Range.value, polydata)
    kd_tree_mapper.update()

    widget = make_2d_slider_widget(sp, iren)
    cb = SliderCallback(kd_tree, polydata)
    widget.AddObserver(vtkCommand.InteractionEvent, cb)

    ren_win.Render()
    iren.Initialize()
    iren.Start()

def read_poly_data(path):
    valid_suffixes = ['.g', '.obj', '.stl', '.ply', '.vtk', '.vtp']
    ext = None
    if path.suffix:
        ext = path.suffix.lower()
    if path.suffix not in valid_suffixes:
        print(f'No reader for this file suffix: {ext}')
        return None
    file_name = str(path.absolute())
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
        return reader.update().output
    else:
        return None

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

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

class SliderCallback:

    def __init__(self, tree, pd, ):
        """
        """
        self.tree = tree
        self.pd = pd

    def __call__(self, caller, ev):
        slider_widget = caller
        # Get the value and do something with it.
        value = slider_widget.representation.value
        # Use C++ rounding where 0.5 or -0.5 is rounded away from zero to 1 or -1.
        level = int(Decimal(str(value)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        self.tree.GenerateRepresentation(level, self.pd)
        slider_widget.representation.value = level

if __name__ == '__main__':
    main()
```
