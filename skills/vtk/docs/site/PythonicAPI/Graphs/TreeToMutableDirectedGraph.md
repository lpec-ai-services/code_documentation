<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/TreeToMutableDirectedGraph/ -->

# TreeToMutableDirectedGraph

Repository source: [TreeToMutableDirectedGraph](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/TreeToMutableDirectedGraph.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/TreeToMutableDirectedGraph/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TreeToMutableDirectedGraph.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkMutableDirectedGraph, vtkTree
)

def main():
    # vtkTree is a read-only data structure. To construct a tree, create an
    # instance of vtkMutableDirectedGraph. Add vertices and edges with
    # AddVertex() and AddEdge(). After building the tree, call
    # tree->CheckedShallowCopy(graph) to copy the structure into a vtkTree.

    # Create a graph.
    mdg = vtkMutableDirectedGraph()

    # Add 4 vertices to the graph.
    v1 = mdg.AddVertex()
    v2 = mdg.AddVertex()
    v3 = mdg.AddVertex()
    v4 = mdg.AddVertex()

    # Add 3 edges to the graph.
    mdg.AddEdge(v1, v2)
    mdg.AddEdge(v1, v3)
    mdg.AddEdge(v1, v4)

    # Create 4 points - one for each vertex.
    points = vtkPoints()
    points.InsertNextPoint(0.0, 0.0, 0.0)
    points.InsertNextPoint(1.0, 0.0, 0.0)
    points.InsertNextPoint(0.0, 1.0, 0.0)
    points.InsertNextPoint(0.0, 0.0, 1.0)

    # Add the coordinates of the points to the graph.
    mdg.points = points

    print(
        f'MDG:\n Type: {mdg.GetClassName()}\n Vertices: {mdg.GetNumberOfVertices()}\n Edges: {mdg.GetNumberOfEdges()}')

    tree = vtkTree()
    if not tree.CheckedShallowCopy(mdg):
        print('Could not convert graph to tree!')
        return

    print(
        f'TREE:\n Type: {tree.GetClassName()}\n Vertices: {tree.GetNumberOfVertices()}\n Edges: {tree.GetNumberOfEdges()}')

    mdg2 = vtkMutableDirectedGraph()

    if not mdg2.CheckedShallowCopy(tree):
        print('Could not convert tree to mutable directed graph!')
        return

    print(
        f'MDG2:\n Type: {mdg2.GetClassName()}\n Vertices: {mdg2.GetNumberOfVertices()}\n Edges: {mdg2.GetNumberOfEdges()}')

if __name__ == '__main__':
    main()
```
