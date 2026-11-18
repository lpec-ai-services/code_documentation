<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/SelectedVerticesAndEdges/ -->

# SelectedVerticesAndEdges

Repository source: [SelectedVerticesAndEdges](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/SelectedVerticesAndEdges.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Graphs/TestSelectedVerticesAndEdges.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Graphs/TestSelectedVerticesAndEdges.png?raw=true target=)

### Description

- Thanks to Eric Monson

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/SelectedVerticesAndEdges/)), ([Python](../../Python/Graphs/SelectedVerticesAndEdges.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SelectedVerticesAndEdges.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkSelectionNode
from vtkmodules.vtkInfovisCore import vtkRandomGraphSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleRubberBand2D
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    colors = vtkNamedColors()

    source = vtkRandomGraphSource()

    view = vtkGraphLayoutView()
    view.AddRepresentationFromInputConnection(source.output_port)

    view.render_window.size = (600, 600)
    view.render_window.window_name = 'SelectedVerticesAndEdges'
    view.renderer.background = colors.GetColor3d('MidnightBlue')
    view.renderer.background2 = colors.GetColor3d('RoyalBlue')

    style = RubberBandStyle(view)
    view.interactor_style = style

    view.ResetCamera()
    view.Render()
    view.interactor.Start()

class RubberBandStyle(vtkInteractorStyleRubberBand2D):

    def __init__(self, view):
        self.view = view
        super().__init__()

        self.AddObserver('LeftButtonReleaseEvent', self.OnLeftButtonUp)
        # self.AddObserver('LeftButtonPressEvent', self.OnLeftButtonDown)

    def OnLeftButtonUp(self, obj=None, event=None):
        # Forward events.
        super().OnLeftButtonUp()

        sel = self.view.GetRepresentation(0).annotation_link.current_selection
        vertices = vtkSelectionNode()
        edges = vtkSelectionNode()
        node0 = sel.GetNode(0)
        node0_field_type = node0.field_type
        if node0_field_type == vtkSelectionNode.VERTEX:
            vertices = node0
        elif node0_field_type == vtkSelectionNode.EDGE:
            edges = node0

        node1 = sel.GetNode(1)
        if node1:
            node1_field_type = node1.field_type
            if node1_field_type == vtkSelectionNode.VERTEX:
                vertices = node1
            elif node1_field_type == vtkSelectionNode.EDGE:
                edges = node1

        vertex_list = vertices.selection_list
        if vertex_list:
            print(f'There are {vertex_list.number_of_tuples} vertices selected.')
        has_vertices = vertex_list and vertex_list.number_of_tuples > 0
        if has_vertices:
            vertex_ids = list()
            for i in range(0, vertex_list.number_of_tuples):
                vertex_ids.append(vertex_list.GetValue(i))
            print(f'Vertex IDs: {", ".join(map(str, vertex_ids))}')

        edge_list = edges.selection_list
        if edge_list:
            print(f'There are {edge_list.number_of_tuples} edges selected.')
        has_edges = edge_list and edge_list.number_of_tuples > 0
        if has_edges:
            edge_ids = list()
            for i in range(0, edge_list.number_of_tuples):
                edge_ids.append(edge_list.GetValue(i))
            print(f'Edge IDs: {", ".join(map(str, edge_ids))}')

        if has_vertices or has_edges:
            print('- - -')
        else:
            print()

# def OnLeftButtonDown(self, obj=None, event=None):
#         # Forward events.
#         super().OnLeftButtonDown()

if __name__ == '__main__':
    main()
```
