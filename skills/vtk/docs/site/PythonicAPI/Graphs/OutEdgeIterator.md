<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/OutEdgeIterator/ -->

# OutEdgeIterator

Repository source: [OutEdgeIterator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/OutEdgeIterator.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/OutEdgeIterator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OutEdgeIterator.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonDataModel import (
    vtkMutableDirectedGraph,
    vtkMutableUndirectedGraph,
    vtkOutEdgeIterator
)

def main():
    print('Undirected graph')
    undirected()
    print('Directed graph')
    directed()

def undirected():
    g = vtkMutableUndirectedGraph()

    # Create a graph.
    v0 = g.AddVertex()
    v1 = g.AddVertex()
    v2 = g.AddVertex()

    g.AddEdge(v0, v1)
    g.AddEdge(v1, v2)
    g.AddEdge(v0, v2)

    # Find all outgoing edges connected to a vertex.
    print('Finding edges connected to vertex 0:')
    it = vtkOutEdgeIterator()
    g.GetOutEdges(0, it)  # Get the edges connected to vertex 0.

    while it.HasNext():
        edge = it.NextGraphEdge()
        print(f'Edge id: {edge.id} Target: {edge.target}')
    print()

def directed():
    g = vtkMutableDirectedGraph()

    # Create a graph.
    v0 = g.AddVertex()
    v1 = g.AddVertex()
    v2 = g.AddVertex()

    g.AddEdge(v1, v0)
    g.AddEdge(v2, v0)

    print('Finding edges connected to vertex 0:')
    it = vtkOutEdgeIterator()
    g.GetOutEdges(0, it)

    while it.HasNext():
        edge = it.NextGraphEdge()
        print(f'Edge id: {edge.id} Target: {edge.target}')

    print('Nothing should be output, vertex 0 has no outgoing edges!')

    print(f'Finding edges connected to vertex 1:')
    it = vtkOutEdgeIterator()
    g.GetOutEdges(1, it)

    while it.HasNext():
        edge = it.NextGraphEdge()
        print(f'Edge id: {edge.id} Target: {edge.target}')
    print()

if __name__ == '__main__':
    main()
```
