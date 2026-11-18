<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ExtractSelectionUsingCells/ -->

# ExtractSelectionUsingCells

Repository source: [ExtractSelectionUsingCells](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ExtractSelectionUsingCells.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExtractSelectionUsingCells.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExtractSelectionUsingCells.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ExtractSelectionUsingCells/)), ([Python](../../Python/PolyData/ExtractSelectionUsingCells.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractSelectionUsingCells.py**

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

    # colors.SetColor('leftBkg', *(0.6, 0.5, 0.4, 1.0))
    # colors.SetColor('centreBkg', *(0.3, 0.1, 0.4, 1.0))
    # colors.SetColor('rightBkg', *(0.4, 0.5, 0.6, 1.0))

    sphere_source = vtkSphereSource()
    sphere_source.update()

    ids = vtkIdTypeArray(number_of_components=1)
    # Specify that we want to extract cells 10 through 19.
    for i in range(10, 20):
        ids.InsertNextValue(i)

    selection_node = vtkSelectionNode(selection_list=ids, field_type=vtkSelectionNode.CELL,
                                      content_type=vtkSelectionNode.INDICES)

    selection = vtkSelection()
    selection.AddNode(selection_node)

    extract_selection = vtkExtractSelection()
    extract_selection.SetInputData(1, selection)
    sphere_source >> select_ports(0, extract_selection)

    # In selection.
    selected = vtkUnstructuredGrid()
    selected.ShallowCopy(extract_selection.update().output)

    # Get points that are NOT in the selection.
    selection_node.properties.Set(vtkSelectionNode().INVERSE(), 1)  # invert the selection.

    not_selected = vtkUnstructuredGrid()
    not_selected.ShallowCopy(extract_selection.update().output)

    sphere_property = vtkProperty(color=colors.GetColor3d('MistyRose'))
    backfaces = vtkProperty(color=colors.GetColor3d('Gold'))

    input_mapper = vtkDataSetMapper()
    sphere_source.output >> input_mapper
    input_actor = vtkActor(mapper=input_mapper, property=sphere_property, backface_property=backfaces)

    selected_mapper = vtkDataSetMapper()
    selected >> selected_mapper
    selected_actor = vtkActor(mapper=selected_mapper, property=sphere_property, backface_property=backfaces)

    not_selected_mapper = vtkDataSetMapper()
    not_selected >> not_selected_mapper
    not_selected_actor = vtkActor(mapper=not_selected_mapper, property=sphere_property, backface_property=backfaces)

    print(f'There are {sphere_source.output.number_of_points}'
          f' points and {sphere_source.output.number_of_cells} input cells.')
    print(f'There are {selected.number_of_points} points and {selected.number_of_cells} cells in the selection.')
    print(f'There are {not_selected.number_of_points} points'
          f' and {not_selected.number_of_cells} cells not in the selection.')

    # Create one camera for all the renderers.
    render_window = vtkRenderWindow(size=(900, 300), window_name='ExtractSelectionCells')

    # And one interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Define viewport ranges (xmin, ymin, xmax, ymax).
    viewports = {
        'left': (0.0, 0.0, 1.0 / 3.0, 1.0),
        'center': (1.0 / 3.0, 0.0, 2.0 / 3.0, 1.0),
        'right': (2.0 / 3.0, 0.0, 1.0, 1.0),
    }

    # Create a camera for all renderers
    camera = vtkCamera()

    # Setup the renderers.
    left_renderer = vtkRenderer(background=colors.GetColor3d('BurlyWood'), viewport=viewports['left'],
                                active_camera=camera)
    render_window.AddRenderer(left_renderer)

    center_renderer = vtkRenderer(background=colors.GetColor3d('orchid_dark'), viewport=viewports['center'],
                                  active_camera=camera)
    render_window.AddRenderer(center_renderer)

    right_renderer = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'), viewport=viewports['right'],
                                 active_camera=camera)
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
