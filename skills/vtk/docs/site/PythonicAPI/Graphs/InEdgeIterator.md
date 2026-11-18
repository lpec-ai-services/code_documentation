<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/InEdgeIterator/ -->

# InEdgeIterator

Repository source: [InEdgeIterator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/InEdgeIterator.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/InEdgeIterator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**InEdgeIterator.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonDataModel import (
    vtkInEdgeIterator,
    vtkMutableDirectedGraph,
    vtkMutableUndirectedGraph
)

def main():
    undirected()
    directed()

def undirected():
    g = vtkMutableUndirectedGraph()

    # Create a graph
    v0 = g.AddVertex()
    v1 = g.AddVertex()
    v2 = g.AddVertex()

    g.AddEdge(v0, v1)
    g.AddEdge(v1, v2)
    g.AddEdge(v0, v2)

    # Find all incoming edges connected to a vertex
    it = vtkInEdgeIterator()
    g.GetInEdges(0, it)

    while it.HasNext():
        edge = it.NextGraphEdge()
        print(f'Edge id: {edge.id} Source: {edge.source}')

def directed():
    g = vtkMutableDirectedGraph()

    # Create a graph
    v0 = g.AddVertex()
    v1 = g.AddVertex()
    v2 = g.AddVertex()

    g.AddEdge(v0, v1)
    g.AddEdge(v0, v2)

    print(f'Finding edges connected to vertex 0')
    it = vtkInEdgeIterator()
    g.GetInEdges(0, it)

    while it.HasNext():
        edge = it.NextGraphEdge()
        print(f'Edge id: {edge.Id} Source: {edge.Source}')

    print(f'Nothing should be output, vertex 0 has no incoming edges!')

    print(f'Finding edges connected to vertex 1')
    it = vtkInEdgeIterator()
    g.GetInEdges(1, it)

    while it.HasNext():
        edge = it.NextGraphEdge()
        print(f'Edge id: {edge.id} Source: {edge.source}')

if __name__ == '__main__':
    main()
```
