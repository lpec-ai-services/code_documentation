<!-- source: https://examples.vtk.org/site/PythonicAPI/Picking/HighlightSelection/ -->

# HighlightSelection

Repository source: [HighlightSelection](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Picking/HighlightSelection.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Picking/TestHighlightSelection.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Picking/TestHighlightSelection.png?raw=true target=)

### Description

This example demonstrates how to select and highlight cells using [vtkInteractorStyleRubberBandPick](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyleRubberBandPick.html). Press 'r' to enter selection mode.

[vtkExtractPolyDataGeometry](https://www.vtk.org/doc/nightly/html/classvtkExtractPolyDataGeometry.html) selects all cells within the selected area. The cells include those on the visible surface as well as those that exist within the view frustum returned by the interactor.

The example accepts a geometry file as the first argument. Without an argument a [vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html) will be used as the [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Picking/HighlightSelection/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**HighlightSelection.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkGenerateIds
from vtkmodules.vtkFiltersExtraction import vtkExtractPolyDataGeometry
from vtkmodules.vtkFiltersGeometry import vtkDataSetSurfaceFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleRubberBandPick
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkAreaPicker,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Select and highlight cells using vtkInteractorStyleRubberBandPick.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None,
                        help='The polydata source file name,e.g. cow.g.')
    args = parser.parse_args()

    return args.file_name

def main():
    file_name = get_program_parameters()
    poly_data = None
    if file_name:
        if Path(file_name).is_file():
            poly_data = read_poly_data(file_name)
        else:
            print(f'{file_name} not found.')
    if file_name is None or poly_data is None:
        sphere_source = vtkSphereSource(center=(0, 0, 0), radius=0.5, theta_resolution=21, phi_resolution=40)
        poly_data = sphere_source.update().output

    colors = vtkNamedColors()

    # Generate data arrays containing point and cell ids.
    id_filter = vtkGenerateIds(point_ids=True, cell_ids=True, field_data=True,
                               input_data=poly_data,
                               cell_ids_array_name='OriginalIds',
                               point_ids_array_name='OriginalIds'
                               )

    # This is needed to convert the output of vtkGenerateIds (vtkDataSet) back to vtkPolyData.
    surface_filter = vtkDataSetSurfaceFilter()
    id_filter >> surface_filter
    surface_filter.update()

    pd_input = surface_filter.update().output

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper(input_data=poly_data, scalar_visibility=False)
    mapper.ScalarVisibilityOff()

    actor = vtkActor(mapper=mapper)
    actor.property.point_size = 5
    actor.property.diffuse_color = colors.GetColor3d('Peacock')
    # Visualize
    renderer = vtkRenderer(use_hidden_line_removal=True, background=colors.GetColor3d('Tan'))

    render_window = vtkRenderWindow(size=(640, 480), window_name='HighlightSelection')
    render_window.AddRenderer(renderer)

    area_picker = vtkAreaPicker()
    render_window_interactor = vtkRenderWindowInteractor(picker=area_picker)
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    render_window.Render()

    style = HighlightInteractorStyle(pd_input)
    render_window_interactor.interactor_style = style

    render_window_interactor.Start()

# Define interaction style
class HighlightInteractorStyle(vtkInteractorStyleRubberBandPick):

    def __init__(self, poly_data):
        super().__init__()
        self.poly_data = poly_data
        self.colors = vtkNamedColors()
        self.selected_mapper = vtkDataSetMapper()
        self.selected_actor = vtkActor()
        self.selected_actor.mapper = self.selected_mapper
        self.AddObserver('LeftButtonReleaseEvent', self.OnLeftButtonUp)
        # self.AddObserver('LeftButtonPressEvent', self.OnLeftButtonDown)

    def OnLeftButtonUp(self, obj=None, event=None):
        # Forward events.
        super().OnLeftButtonUp()

        frustum = self.GetInteractor().GetPicker().GetFrustum()

        extract_poly_data_geometry = vtkExtractPolyDataGeometry(input_data=self.poly_data, implicit_function=frustum)
        extract_poly_data_geometry.update()

        print(f'Extracted {extract_poly_data_geometry.output.number_of_cells} cells.')
        self.selected_mapper.input_data = extract_poly_data_geometry.output
        self.selected_mapper.scalar_visibility = False

        self.selected_actor.property.color = self.colors.GetColor3d('Tomato')
        self.selected_actor.property.point_size = 5
        self.selected_actor.property.SetRepresentationToWireframe()

        self.interactor.render_window.renderers.first_renderer.AddActor(self.selected_actor)
        self.interactor.render_window.Render()
        self.HighlightProp(None)

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

if __name__ == '__main__':
    main()
```
