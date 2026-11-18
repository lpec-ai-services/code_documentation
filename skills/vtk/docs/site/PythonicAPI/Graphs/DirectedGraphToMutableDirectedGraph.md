<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/DirectedGraphToMutableDirectedGraph/ -->

# DirectedGraphToMutableDirectedGraph

Repository source: [DirectedGraphToMutableDirectedGraph](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/DirectedGraphToMutableDirectedGraph.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/DirectedGraphToMutableDirectedGraph/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DirectedGraphToMutableDirectedGraph.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkDirectedGraph,
    vtkMutableDirectedGraph
)

def main():
    # vtkDirectedGraph is a collection of vertices along with a collection of
    # directed edges (edges that have a source and target). ShallowCopy() and
    # DeepCopy() (and CheckedShallowCopy(), CheckedDeepCopy()) accept instances
    # of vtkTree and vtkMutableDirectedGraph. vtkDirectedGraph is read-only.

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
    points.InsertNextPoint(0.0, 0.0, 2.0)

    # Add the coordinates of the points to the graph.
    mdg.points = points

    print(
        f'MDG:\n Type: {mdg.GetClassName()}\n Vertices: {mdg.GetNumberOfVertices()}\n Edges: {mdg.GetNumberOfEdges()}')

    dg = vtkDirectedGraph()
    if not dg.CheckedShallowCopy(mdg):
        print('Could not convert mutable directed graph to directed graph!')
        return

    print(f'DG:\n Type: {dg.GetClassName()}\n Vertices: {dg.GetNumberOfVertices()}\n Edges: {dg.GetNumberOfEdges()}')

    mdg2 = vtkMutableDirectedGraph()

    if not mdg2.CheckedShallowCopy(mdg):
        print('Could not convert directed graph to mutable directed graph!')
        return

    print(
        f'MDG2:\n Type: {mdg2.GetClassName()}\n Vertices: {mdg2.GetNumberOfVertices()}\n Edges: {mdg2.GetNumberOfEdges()}')

if __name__ == '__main__':
    main()
```
