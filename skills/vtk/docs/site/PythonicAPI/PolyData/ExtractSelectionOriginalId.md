<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ExtractSelectionOriginalId/ -->

# ExtractSelectionOriginalId

Repository source: [ExtractSelectionOriginalId](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ExtractSelectionOriginalId.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExtractSelectionOriginalId.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExtractSelectionOriginalId.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ExtractSelectionOriginalId/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractSelectionOriginalId.py**

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
from vtkmodules.vtkFiltersSources import vtkPointSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # colors.SetColor('leftBkg', *(0.6, 0.5, 0.4, 1.0))
    # colors.SetColor('centreBkg', *(0.3, 0.1, 0.4, 1.0))
    # colors.SetColor('rightBkg', *(0.4, 0.5, 0.6, 1.0))

    point_source = vtkPointSource(number_of_points=50)
    point_source.update()

    print(f'There are {point_source.output.number_of_points} input points.')

    ids = vtkIdTypeArray(number_of_components=1)
    # Specify that we want to extract points 10 through 19.
    for i in range(10, 20):
        ids.InsertNextValue(i)

    selection_node = vtkSelectionNode(selection_list=ids, field_type=vtkSelectionNode.POINT,
                                      content_type=vtkSelectionNode.INDICES)

    selection = vtkSelection()
    selection.AddNode(selection_node)

    extract_selection = vtkExtractSelection()
    extract_selection.SetInputData(1, selection)
    point_source >> select_ports(0, extract_selection)
    extract_selection.update()

    # In selection.
    selected = vtkUnstructuredGrid()
    selected.ShallowCopy(extract_selection.update().output)

    print(f'There are {selected.number_of_points} points in the selection.')
    # Use this to get :Array 0 name = vtkOriginalPointIds
    # print(selected)

    original_ids = selected.point_data.GetArray('vtkOriginalPointIds')

    for i in range(0, original_ids.number_of_tuples):
        print(f'Point {i:2d} was originally point {original_ids.GetValue(i):2d}')

    for i in range(0, original_ids.number_of_tuples):
        query = original_ids.GetValue(i)
        for j in range(0, original_ids.number_of_tuples):
            if original_ids.GetValue(j) == query:
                print(f'Original Point {query:2d} is now {j:2d}')

    # Get points that are NOT in the selection.
    selection_node.properties.Set(vtkSelectionNode().INVERSE(), 1)  # invert the selection.

    not_selected = vtkUnstructuredGrid()
    not_selected.ShallowCopy(extract_selection.update().output)

    #  A summary.
    print(f'There are {point_source.output.number_of_points}'
          f' points and {point_source.output.number_of_cells} input cells.')
    print(f'There are {selected.number_of_points} points and {selected.number_of_cells} cells in the selection.')
    print(f'There are {not_selected.number_of_points} points'
          f' and {not_selected.number_of_cells} cells not in the selection.')

    input_mapper = vtkDataSetMapper()
    point_source.output >> input_mapper
    input_actor = vtkActor(mapper=input_mapper)
    input_actor.property.color = colors.GetColor3d('MidnightBlue')
    input_actor.property.point_size = 5

    selected_mapper = vtkDataSetMapper()
    selected >> selected_mapper
    selected_actor = vtkActor(mapper=selected_mapper)
    selected_actor.property.color = colors.GetColor3d('MidnightBlue')
    selected_actor.property.point_size = 5

    not_selected_mapper = vtkDataSetMapper()
    not_selected >> not_selected_mapper
    not_selected_actor = vtkActor(mapper=not_selected_mapper)
    not_selected_actor.property.color = colors.GetColor3d('MidnightBlue')
    not_selected_actor.property.point_size = 5

    # There will be one render window
    render_window = vtkRenderWindow(size=(900, 300), window_name='ExtractSelectionOriginalId')

    # And one interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Define viewport ranges (xmin, ymin, xmax, ymax).
    viewports = {
        'left': (0.0, 0.0, 1.0 / 3.0, 1.0),
        'center': (1.0 / 3.0, 0.0, 2.0 / 3.0, 1.0),
        'right': (2.0 / 3.0, 0.0, 1.0, 1.0),
    }

    # Create one camera for all the renderers.
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
