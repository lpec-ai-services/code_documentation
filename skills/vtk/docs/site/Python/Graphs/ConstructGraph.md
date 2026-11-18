<!-- source: https://examples.vtk.org/site/Python/Graphs/ConstructGraph/ -->

# ConstructGraph

Repository source: [ConstructGraph](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Graphs/ConstructGraph.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestConstructGraph.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestConstructGraph.png?raw=true target=)

### Description

This example shows how to construct a simple graph.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/ConstructGraph/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ConstructGraph.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkMutableUndirectedGraph
from vtkmodules.vtkInfovisLayout import vtkForceDirectedLayoutStrategy
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    colors = vtkNamedColors()

    g = vtkMutableUndirectedGraph()

    v1 = g.AddVertex()
    v2 = g.AddVertex()

    g.AddEdge(v1, v2)
    print('Number of vertices:', g.GetNumberOfVertices())
    print('Number of edges:', g.GetNumberOfEdges())

    g.AddEdge(v1, v2)
    print('Number of vertices:', g.GetNumberOfVertices())
    print('Number of edges:', g.GetNumberOfEdges())

    force_directed = vtkForceDirectedLayoutStrategy()

    graph_layout_view = vtkGraphLayoutView()
    graph_layout_view.AddRepresentationFromInput(g)
    # If we create a layout object directly, just set the pointer through this method.
    # graph_layout_view.SetLayoutStrategy(force_directed)
    graph_layout_view.SetLayoutStrategyToForceDirected()
    graph_layout_view.ResetCamera()
    graph_layout_view.GetRenderer().SetBackground(colors.GetColor3d('Navy'))
    graph_layout_view.GetRenderer().SetBackground2(colors.GetColor3d('MidnightBlue'))
    graph_layout_view.GetRenderWindow().SetWindowName('ConstructGraph')
    graph_layout_view.Render()
    graph_layout_view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
