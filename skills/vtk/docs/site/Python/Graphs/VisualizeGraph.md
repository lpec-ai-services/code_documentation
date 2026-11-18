<!-- source: https://examples.vtk.org/site/Python/Graphs/VisualizeGraph/ -->

# VisualizeGraph

Repository source: [VisualizeGraph](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Graphs/VisualizeGraph.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestVisualizeGraph.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestVisualizeGraph.png?raw=true target=)

### Description

- Contributed by Jim McCusker

Note

AddEdge() is not enabled through python, but AddGraphEdge() is.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/VisualizeGraph/)), ([Java](https://examples.vtk.org/site/Java/Graphs/VisualizeGraph/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**VisualizeGraph.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonDataModel import vtkMutableDirectedGraph
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    g = vtkMutableDirectedGraph()

    v1 = g.AddVertex()
    v2 = g.AddVertex()

    g.AddGraphEdge(v1, v2)
    g.AddGraphEdge(v1, v2)

    graphLayoutView = vtkGraphLayoutView()
    graphLayoutView.AddRepresentationFromInput(g)
    graphLayoutView.SetLayoutStrategy('Simple 2D')
    graphLayoutView.ResetCamera()
    graphLayoutView.Render()

    graphLayoutView.GetLayoutStrategy().SetRandomSeed(0)

    graphLayoutView.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
