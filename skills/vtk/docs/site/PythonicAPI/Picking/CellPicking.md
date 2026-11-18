<!-- source: https://examples.vtk.org/site/PythonicAPI/Picking/CellPicking/ -->

# CellPicking

Repository source: [CellPicking](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Picking/CellPicking.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Picking/TestCellPicking.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Picking/TestCellPicking.png?raw=true target=)

### Description

This example demonstrates how to get the coordinates of the point on an actor that is clicked with the left mouse button. It also indicates which cell the selected point belongs to by highlighting the edges of that cell.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Picking/CellPicking/)), ([Python](../../Python/Picking/CellPicking.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CellPicking.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkIdTypeArray
from vtkmodules.vtkCommonDataModel import (
    vtkSelection,
    vtkSelectionNode,
    vtkUnstructuredGrid
)
from vtkmodules.vtkFiltersCore import vtkTriangleFilter
from vtkmodules.vtkFiltersExtraction import vtkExtractSelection
from vtkmodules.vtkFiltersSources import vtkPlaneSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCellPicker,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

class MouseInteractorStyle(vtkInteractorStyleTrackballCamera):
    """
    Catch mouse events.
    """

    def __init__(self, data):
        super().__init__()

        self.AddObserver('LeftButtonPressEvent', self.left_button_press_event)

        self.data = data
        self.selected_mapper = vtkDataSetMapper()
        self.selected_actor = vtkActor(mapper=self.selected_mapper)

    def left_button_press_event(self, obj, event):
        colors = vtkNamedColors()

        # Get the location of the click (in window coordinates)
        pos = self.interactor.GetEventPosition()

        picker = vtkCellPicker(tolerance=0.0005)

        # Pick from this location.
        picker.Pick(pos[0], pos[1], 0, self.default_renderer)

        world_position = picker.pick_position
        print(f'Cell id is: {picker.cell_id}')

        if picker.cell_id != -1:
            print(f'Pick position is: ({world_position[0]:.6g}, {world_position[1]:.6g}, {world_position[2]:.6g})')

            ids = vtkIdTypeArray(number_of_components=1)
            ids.InsertNextValue(picker.cell_id)

            selection_node = vtkSelectionNode(field_type=vtkSelectionNode.CELL,
                                              content_type=vtkSelectionNode.INDICES,
                                              selection_list=ids)

            selection = vtkSelection()
            selection.AddNode(selection_node)

            extract_selection = vtkExtractSelection()
            extract_selection.SetInputData(0, self.data)
            extract_selection.SetInputData(1, selection)
            extract_selection.update()

            # In selection
            selected = vtkUnstructuredGrid()
            selected.ShallowCopy(extract_selection.output)

            print(f'Number of points in the selection: {selected.number_of_points}')
            print(f'Number of cells in the selection : {selected.number_of_cells}')

            selected >> self.selected_mapper
            self.selected_actor.property.edge_visibility = True
            self.selected_actor.property.color = colors.GetColor3d('Tomato')
            self.selected_actor.property.line_width = 3

            self.interactor.render_window.renderers.first_renderer.AddActor(self.selected_actor)

        # Forward events
        self.OnLeftButtonDown()

def main(argv):
    colors = vtkNamedColors()

    plane_source = vtkPlaneSource()

    triangle_filter = vtkTriangleFilter()

    mapper = vtkPolyDataMapper()
    plane_source >> triangle_filter >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('SeaGreen')

    renderer = vtkRenderer(background=colors.GetColor3d('PaleTurquoise'))
    ren_win = vtkRenderWindow(window_name='CellPicking')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    renderer.AddActor(actor)

    # Add the custom style.
    style = MouseInteractorStyle(triangle_filter.output)
    style.default_renderer = renderer
    iren.interactor_style = style

    ren_win.Render()
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    import sys

    main(sys.argv)
```
