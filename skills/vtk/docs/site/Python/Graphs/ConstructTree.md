<!-- source: https://examples.vtk.org/site/Python/Graphs/ConstructTree/ -->

# ConstructTree

Repository source: [ConstructTree](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Graphs/ConstructTree.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestConstructTree.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestConstructTree.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/ConstructTree/)), ([PythonicAPI](../../PythonicAPI/Graphs/ConstructTree.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ConstructTree.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonDataModel import (
    vtkMutableDirectedGraph,
    vtkTree
)
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    graph = vtkMutableDirectedGraph()

    v1 = graph.AddVertex()
    v2 = graph.AddChild(v1)
    graph.AddChild(v1)
    graph.AddChild(v2)

    # equivalent to:
    # V1 = g.AddVertex()
    # V2 = g.AddVertex()
    # V3 = g.AddVertex()
    # V4 = g.AddVertex()

    # g.AddEdge ( V1, V2 )
    # g.AddEdge ( V1, V3 )
    # g.AddEdge ( V2, V4 )

    tree = vtkTree()
    success = tree.CheckedShallowCopy(graph)
    print('Success?', success)
    # std::cout << 'Success? ' << success << std::endl

    treeLayoutView = vtkGraphLayoutView()
    treeLayoutView.AddRepresentationFromInput(tree)
    treeLayoutView.SetLayoutStrategyToTree()
    treeLayoutView.ResetCamera()
    treeLayoutView.Render()
    treeLayoutView.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
