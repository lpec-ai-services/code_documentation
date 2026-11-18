<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/DistancePolyDataFilter/ -->

# DistancePolyDataFilter

Repository source: [DistancePolyDataFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/DistancePolyDataFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestDistancePolyDataFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestDistancePolyDataFilter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/DistancePolyDataFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DistancePolyDataFilter.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkCleanPolyData
from vtkmodules.vtkFiltersGeneral import vtkDistancePolyDataFilter
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
    vtkScalarBarRepresentation,
    vtkScalarBarWidget
)
from vtkmodules.vtkRenderingAnnotation import vtkScalarBarActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextProperty
)

def get_program_parameters():
    import argparse
    description = 'Compute the distance function from one vtkPolyData to another.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename1', default=None, nargs='?', help='Enter the first polydata file name.')
    parser.add_argument('filename2', default=None, nargs='?', help='Enter the second polydata filename.')
    args = parser.parse_args()
    return args.filename1, args.filename2

def main():
    file_name1, file_name2 = get_program_parameters()
    input1 = None
    input2 = None
    if file_name1 and file_name2:
        input1 = read_poly_data(file_name1)
        input2 = read_poly_data(file_name1)
    if input1 is None or input2 is None:
        sphere_source1 = vtkSphereSource(center=(1, 0, 0), phi_resolution=21, theta_resolution=21)
        input1 = sphere_source1.update().output
        sphere_source2 = vtkSphereSource(phi_resolution=21, theta_resolution=21)
        input2 = sphere_source2.update().output

    colors = vtkNamedColors()

    clean1 = vtkCleanPolyData(input_data=input1)
    clean2 = vtkCleanPolyData(input_data=input2)

    distance_filter = vtkDistancePolyDataFilter()
    distance_filter.input_connection = (0, clean1.output_port)
    distance_filter.input_connection = (1, clean2.output_port)
    distance_filter.update()
    scalar_range = distance_filter.output.point_data.scalars.range

    mapper = vtkPolyDataMapper(scalar_range=scalar_range)
    distance_filter >> mapper

    actor = vtkActor(mapper=mapper)

    scalar_bar_properties = ScalarBarProperties()
    scalar_bar_properties.lut = mapper.lookup_table
    scalar_bar_properties.orientation = True
    scalar_bar_properties.title_text = 'Distance'
    scalar_bar_properties.number_of_labels = 4

    text_property = vtkTextProperty(color=colors.GetColor3d('MidnightBlue'), bold=True, italic=True, shadow=True,
                                    font_size=16,
                                    justification=TextProperty.Justification.VTK_TEXT_LEFT)
    label_text_property = vtkTextProperty(color=colors.GetColor3d('MidnightBlue'), bold=True, italic=True, shadow=True,
                                          font_size=12,
                                          justification=TextProperty.Justification.VTK_TEXT_LEFT)

    renderer = vtkRenderer(gradient_background=True, background=colors.GetColor3d('Silver'),
                           background2=colors.GetColor3d('Gold'))

    ren_win = vtkRenderWindow(size=(600, 500), window_name='DistancePolyDataFilter')
    ren_win.AddRenderer(renderer)

    ren_win_interactor = vtkRenderWindowInteractor()
    ren_win_interactor.render_window = ren_win

    renderer.AddActor(actor)

    scalar_bar_widget = make_scalar_bar_widget(scalar_bar_properties, text_property, label_text_property,
                                               ren_win_interactor)

    ren_win.Render()
    scalar_bar_widget.On()
    ren_win_interactor.Start()

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

class ScalarBarProperties:
    """
    The properties needed for scalar bars.
    """
    named_colors = vtkNamedColors()

    lut = None
    # These are in pixels
    maximum_dimensions = {'width': 100, 'height': 260}
    title_text = '',
    number_of_labels: int = 5
    # Orientation vertical=True, horizontal=False
    orientation: bool = True
    # Horizontal and vertical positioning
    position_v = {'point1': (0.85, 0.1), 'point2': (0.1, 0.7)}
    position_h = {'point1': (0.10, 0.1), 'point2': (0.7, 0.1)}

def make_scalar_bar_widget(scalar_bar_properties, text_property, label_text_property, interactor):
    """
    Make a scalar bar widget.

    :param scalar_bar_properties: The lookup table, title name, maximum dimensions in pixels and position.
    :param text_property: The properties for the title.
    :param label_text_property: The properties for the labels.
    :param interactor: The vtkInteractor.
    :return: The scalar bar widget.
    """
    sb_actor = vtkScalarBarActor(lookup_table=scalar_bar_properties.lut, title=scalar_bar_properties.title_text,
                                 unconstrained_font_size=False, number_of_labels=scalar_bar_properties.number_of_labels,
                                 label_text_property=label_text_property, title_text_property=text_property
                                 )

    sb_rep = vtkScalarBarRepresentation(enforce_normalized_viewport_bounds=True,
                                        orientation=scalar_bar_properties.orientation)

    # Set the position
    sb_rep.position_coordinate.SetCoordinateSystemToNormalizedViewport()
    sb_rep.position2_coordinate.SetCoordinateSystemToNormalizedViewport()
    if scalar_bar_properties.orientation:
        sb_rep.position_coordinate.value = scalar_bar_properties.position_v['point1']
        sb_rep.position2_coordinate.value = scalar_bar_properties.position_v['point2']
    else:
        sb_rep.position_coordinate.value = scalar_bar_properties.position_h['point1']
        sb_rep.position2_coordinate.value = scalar_bar_properties.position_h['point2']

    widget = vtkScalarBarWidget(representation=sb_rep, scalar_bar_actor=sb_actor, interactor=interactor, enabled=True)

    return widget

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
