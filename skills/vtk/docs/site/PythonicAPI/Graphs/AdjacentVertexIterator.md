<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/AdjacentVertexIterator/ -->

# AdjacentVertexIterator

Repository source: [AdjacentVertexIterator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/AdjacentVertexIterator.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Graphs/TestAdjacentVertexIterator.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Graphs/TestAdjacentVertexIterator.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/AdjacentVertexIterator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AdjacentVertexIterator.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkLookupTable,
    vtkUnsignedCharArray
)
from vtkmodules.vtkCommonDataModel import vtkAdjacentVertexIterator
from vtkmodules.vtkCommonDataModel import (
    vtkMutableDirectedGraph,
    vtkTree
)
from vtkmodules.vtkViewsCore import vtkViewTheme
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    colors = vtkNamedColors()

    g = vtkMutableDirectedGraph()

    # Create 4 vertices.
    v0 = g.AddVertex()
    v1 = g.AddVertex()
    v2 = g.AddVertex()
    v3 = g.AddVertex()

    # Add the edges.
    g.AddEdge(v0, v1)
    g.AddEdge(v0, v2)
    g.AddEdge(v2, v3)

    tree = vtkTree()
    success = tree.CheckedShallowCopy(g)
    print(f'Is it a tree? {success}')

    # Create the color array.
    vertex_colors = vtkUnsignedCharArray(number_of_components=1, name='Color')

    lookup_table = vtkLookupTable(number_of_table_values=3)
    # Origin
    lookup_table.SetTableValue(0, colors.GetColor4d('Red'))
    # Unconnected vertices
    lookup_table.SetTableValue(1, colors.GetColor4d('Blue'))
    # Connected vertices
    lookup_table.SetTableValue(2, colors.GetColor4d('Green'))
    lookup_table.Build()

    # Set up the colors.
    vertex_colors.InsertNextValue(0)
    vertex_colors.InsertNextValue(1)
    # vertex_colors.InsertNextValue(2)
    # vertex_colors.InsertNextValue(3)

    iterator = vtkAdjacentVertexIterator()
    tree.GetAdjacentVertices(0, iterator)

    i = 2
    while iterator.HasNext():
        next_vertex = iterator.Next()
        print(f'Next adjacent vertex: {next_vertex}')
        vertex_colors.InsertNextValue(i)
        i += 1

    # Add the color array to the graph.
    tree.vertex_data.AddArray(vertex_colors)

    graph_layout_view = vtkGraphLayoutView(vertex_color_array_name='Color', color_vertices=True, layout_strategy='Tree')
    graph_layout_view.AddRepresentationFromInput(tree)

    theme = vtkViewTheme(point_lookup_table=lookup_table, scale_point_lookup_table=False)
    graph_layout_view.ApplyViewTheme(theme)

    graph_layout_view.ResetCamera()
    graph_layout_view.interactor.Initialize()
    graph_layout_view.interactor.Start()

if __name__ == '__main__':
    main()
```
