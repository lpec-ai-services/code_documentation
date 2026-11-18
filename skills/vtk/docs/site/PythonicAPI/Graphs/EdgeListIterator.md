<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/EdgeListIterator/ -->

# EdgeListIterator

Repository source: [EdgeListIterator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/EdgeListIterator.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/EdgeListIterator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**EdgeListIterator.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonDataModel import (
    vtkEdgeListIterator, vtkMutableUndirectedGraph
)

def main():
    g = vtkMutableUndirectedGraph()

    # Create a graph
    v0 = g.AddVertex()
    v1 = g.AddVertex()
    v2 = g.AddVertex()

    g.AddEdge(v0, v1)
    g.AddEdge(v1, v2)
    g.AddEdge(v0, v2)

    edge_list_iterator = vtkEdgeListIterator()
    g.GetEdges(edge_list_iterator)

    while edge_list_iterator.HasNext():
        # For Python use  'NextGraphEdge()' instead of 'Next()'.
        edge = edge_list_iterator.NextGraphEdge()
        print(f'Edge: {edge.id} is from Source: {edge.source} to Target: {edge.target}')

if __name__ == '__main__':
    main()
```
