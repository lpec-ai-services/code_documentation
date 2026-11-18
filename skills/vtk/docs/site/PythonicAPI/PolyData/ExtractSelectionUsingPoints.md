<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ExtractSelectionUsingPoints/ -->

# ExtractSelectionUsingPoints

Repository source: [ExtractSelectionUsingPoints](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ExtractSelectionUsingPoints.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExtractSelectionUsingPoints.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExtractSelectionUsingPoints.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ExtractSelectionUsingPoints/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractSelectionUsingPoints.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkIdTypeArray
from vtkmodules.vtkCommonDataModel import (
    vtkSelection,
    vtkSelectionNode,
    vtkUnstructuredGrid
)
from vtkmodules.vtkFiltersExtraction import vtkExtractSelection
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkDataSetMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()
    sphere_source.update()

    print(f'There are {sphere_source.output.number_of_points} input points.')
    print(f'There are {sphere_source.output.number_of_cells} input cells.')

    ids = vtkIdTypeArray(number_of_components=1)

    # Set the values that we want.
    for i in range(0, sphere_source.output.number_of_points - 15):
        ids.InsertNextValue(i)

    selection_node = vtkSelectionNode(field_type=vtkSelectionNode.POINT, content_type=vtkSelectionNode.INDICES,
                                      selection_list=ids)
    selection_node.properties.Set(vtkSelectionNode.CONTAINING_CELLS(), 1)

    selection = vtkSelection()
    selection.AddNode(selection_node)

    extract_selection = vtkExtractSelection()
    extract_selection.SetInputData(1, selection)
    sphere_source >> select_ports(0, extract_selection)
    extract_selection.update()

    # In the selection.
    selected = vtkUnstructuredGrid()
    selected.ShallowCopy(extract_selection.output)
    print(f'There are {selected.number_of_points} points in the selection.')
    print(f'There are {selected.number_of_cells} cells in the selection.')

    # Not in the selection.
    selection_node.properties.Set(vtkSelectionNode.INVERSE(), 1)
    extract_selection.update()
    not_selected = vtkUnstructuredGrid()
    not_selected.ShallowCopy(extract_selection.output)

    not_selected = vtkUnstructuredGrid()
    not_selected.ShallowCopy(extract_selection.output)
    print(f'There are {not_selected.number_of_points} points not in the selection.')
    print(f'There are {not_selected.number_of_cells} cells not in the selection.')

    sphere_property = vtkProperty(color=colors.GetColor3d('MistyRose'))
    backfaces = vtkProperty(color=colors.GetColor3d('Gold'))

    input_mapper = vtkDataSetMapper()
    sphere_source >> input_mapper
    input_actor = vtkActor(mapper=input_mapper, property=sphere_property, backface_property=backfaces)

    selected_mapper = vtkDataSetMapper(input_data=selected)
    selected_actor = vtkActor(mapper=selected_mapper, property=sphere_property, backface_property=backfaces)

    not_selected_mapper = vtkDataSetMapper(input_data=not_selected)
    not_selected_actor = vtkActor(mapper=not_selected_mapper, property=sphere_property, backface_property=backfaces)

    # There will be one render window.
    render_window = vtkRenderWindow(size=(900, 300), window_name='ExtractCellsUsingPoints')

    # One interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Define viewport ranges (xmin, ymin, xmax, ymax).
    viewports = {
        'left': (0.0, 0.0, 1.0 / 3.0, 1.0),
        'center': (1.0 / 3.0, 0.0, 2.0 / 3.0, 1.0),
        'right': (2.0 / 3.0, 0.0, 1.0, 1.0),
    }
    backgrounds = {
        'left': colors.GetColor3d('BurlyWood'),
        'center': colors.GetColor3d('orchid_dark'),
        'right': colors.GetColor3d('CornflowerBlue'),
    }

    # Create one camera for all the renderers.
    camera = vtkCamera()

    # Setup the renderers.
    left_renderer = vtkRenderer(background=backgrounds['left'], viewport=viewports['left'], active_camera=camera)
    render_window.AddRenderer(left_renderer)

    center_renderer = vtkRenderer(background=backgrounds['center'], viewport=viewports['center'], active_camera=camera)
    render_window.AddRenderer(center_renderer)

    right_renderer = vtkRenderer(background=backgrounds['right'], viewport=viewports['right'], active_camera=camera)
    render_window.AddRenderer(right_renderer)

    left_renderer.AddActor(input_actor)
    center_renderer.AddActor(selected_actor)
    right_renderer.AddActor(not_selected_actor)

    left_renderer.ResetCamera()

    render_window.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
