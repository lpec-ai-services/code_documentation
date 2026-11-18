<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/MergeSelections/ -->

# MergeSelections

Repository source: [MergeSelections](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/MergeSelections.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestMergeSelections.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestMergeSelections.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/MergeSelections/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MergeSelections.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtkmodules.vtkCommonCore import vtkIdTypeArray
from vtkmodules.vtkCommonDataModel import (
    vtkSelection,
    vtkSelectionNode
)
from vtkmodules.vtkFiltersExtraction import vtkExtractSelection
from vtkmodules.vtkFiltersSources import vtkPointSource
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

    # A nifty way of setting backgrounds in multiple renderers.
    color_series = vtkColorSeries()
    color_series.SetColorSchemeByName('Brewer Qualitative Pastel2')
    colors.SetColor('ren0', color_series.GetColor(0))
    colors.SetColor('ren1', color_series.GetColor(1))
    colors.SetColor('ren2', color_series.GetColor(2))
    colors.SetColor('ren3', color_series.GetColor(3))

    point_source = vtkPointSource(number_of_points=50)
    point_source.update()

    print(f'There are {point_source.output.number_of_points} input points.')

    # Two sets of overlapping points are selected.
    ids1 = vtkIdTypeArray(number_of_components=1)
    # Specify that we want to extract points 10 through 19.
    for i in range(10, 20):
        ids1.InsertNextValue(i)

    ids2 = vtkIdTypeArray(number_of_components=1)
    # Specify that we want to extract points 15 through 29.
    for i in range(15, 30):
        ids2.InsertNextValue(i)

    selection_node1 = vtkSelectionNode(field_type=vtkSelectionNode.POINT, content_type=vtkSelectionNode.INDICES,
                                       selection_list=ids1)
    # selection_node1.properties.Set(vtkSelectionNode.CONTAINING_CELLS(), 0)

    selection1 = vtkSelection()
    selection1.AddNode(selection_node1)

    selection_node2 = vtkSelectionNode(field_type=vtkSelectionNode.POINT, content_type=vtkSelectionNode.INDICES,
                                       selection_list=ids2)
    # selection_node2.properties.Set(vtkSelectionNode.CONTAINING_CELLS(), 0)

    selection2 = vtkSelection()
    selection2.AddNode(selection_node2)

    selection_combined = vtkSelection()
    selection_combined.AddNode(selection_node1)
    selection_combined.Union(selection_node2)

    extract_selection1 = vtkExtractSelection()
    extract_selection1.SetInputData(1, selection1)
    point_source >> select_ports(0, extract_selection1)
    extract_selection1.update()

    extract_selection2 = vtkExtractSelection()
    extract_selection2.SetInputData(1, selection2)
    point_source >> select_ports(0, extract_selection2)
    extract_selection2.update()

    extract_selection_combined = vtkExtractSelection()
    extract_selection_combined.SetInputData(1, selection_combined)
    point_source >> select_ports(0, extract_selection_combined)
    extract_selection_combined.update()

    # In the selections.
    print(f'In the first selection, there are {extract_selection1.output.number_of_points}'
          f' points and {extract_selection1.output.number_of_cells} cells.')
    print(f'In the second selection, there are {extract_selection2.output.number_of_points}'
          f' points and {extract_selection2.output.number_of_cells} cells.')
    print(f'In the combined selection, there are {extract_selection_combined.output.number_of_points}'
          f' points and {extract_selection_combined.output.number_of_cells} cells'
          f' and {selection_combined.number_of_nodes} nodes.')

    '''
    # Not in selection.
    # Here we invert the selections.
    selection_node1.properties.Set(vtkSelectionNode.INVERSE(), 1)
    selection_node2.properties.Set(vtkSelectionNode.INVERSE(), 1)
    extract_selection_combined.update()
    print(f'In the combined inverse selection, there are {extract_selection_combined.output.number_of_points}'
          f' points and {extract_selection_combined.output.number_of_cells} cells'
          f' and {selection_combined.number_of_nodes} nodes.')
    '''

    # Visualize
    mapper_original = vtkDataSetMapper(scalar_visibility=False)
    point_source >> mapper_original

    mapper1 = vtkDataSetMapper(scalar_visibility=False)
    extract_selection1 >> mapper1

    mapper2 = vtkDataSetMapper(scalar_visibility=False)
    extract_selection2 >> mapper2

    mapper_combined = vtkDataSetMapper(scalar_visibility=False)
    extract_selection_combined >> mapper_combined

    points_property = vtkProperty(color=colors.GetColor3d('black'), point_size=5)

    original_actor = vtkActor(mapper=mapper_original, property=points_property)
    actor1 = vtkActor(mapper=mapper1, property=points_property)
    actor2 = vtkActor(mapper=mapper2, property=points_property)
    actor_combined = vtkActor(mapper=mapper_combined, property=points_property)

    # Define viewport ranges (xmin, ymin, xmax, ymax).
    viewports = {
        'original': (0.0, 0.0, 0.25, 1.0),
        'selection1': (0.25, 0.0, 0.5, 1.0),
        'selection2': (0.5, 0.0, 0.750, 1.0),
        'combined': (0.75, 0.0, 1.0, 1.0),
    }

    backgrounds = {
        'original': colors.GetColor3d('ren0'),
        'selection1': colors.GetColor3d('ren1'),
        'selection2': colors.GetColor3d('ren2'),
        'combined': colors.GetColor3d('ren3'),
    }

    # There will be one render window.
    render_window = vtkRenderWindow(size=(1000, 250), window_name='MergeSelections')

    # One interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Create one camera for all the renderers.
    camera = vtkCamera()

    # Setup the renderers.
    original_renderer = vtkRenderer(background=backgrounds['original'], viewport=viewports['original'],
                                    active_camera=camera)
    render_window.AddRenderer(original_renderer)

    selection1_renderer = vtkRenderer(background=backgrounds['selection1'], viewport=viewports['selection1'],
                                      active_camera=camera)
    render_window.AddRenderer(selection1_renderer)

    selection2_renderer = vtkRenderer(background=backgrounds['selection2'], viewport=viewports['selection2'],
                                      active_camera=camera)
    render_window.AddRenderer(selection2_renderer)

    combined_renderer = vtkRenderer(background=backgrounds['combined'], viewport=viewports['combined'],
                                    active_camera=camera)
    render_window.AddRenderer(combined_renderer)

    original_renderer.AddActor(original_actor)
    selection1_renderer.AddActor(actor1)
    selection2_renderer.AddActor(actor2)
    combined_renderer.AddActor(actor_combined)

    original_renderer.ResetCamera()

    render_window.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
