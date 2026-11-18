<!-- source: https://examples.vtk.org/site/PythonicAPI/InfoVis/MutableGraphHelper/ -->

# MutableGraphHelper

Repository source: [MutableGraphHelper](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/InfoVis/MutableGraphHelper.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/InfoVis/TestMutableGraphHelper.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/InfoVis/TestMutableGraphHelper.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/InfoVis/MutableGraphHelper/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MutableGraphHelper.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkMutableUndirectedGraph
from vtkmodules.vtkInfovisCore import vtkMutableGraphHelper
# noinspection PyUnresolvedReferences
from vtkmodules.vtkInfovisLayout import vtkTreeLayoutStrategy
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    colors = vtkNamedColors()

    g = vtkMutableUndirectedGraph()

    graph_helper = vtkMutableGraphHelper()
    graph_helper.SetGraph(g)
    v0 = graph_helper.AddVertex()
    v1 = graph_helper.AddVertex()

    graph_helper.AddEdge(v0, v1)

    # Can also do this:
    # graph_helper.RemoveEdge(0)

    tree_layout_view = vtkGraphLayoutView()
    tree_layout_view.AddRepresentationFromInput(graph_helper.graph)
    # Layout only works on vtkTree if VTK::InfovisBoostGraphAlgorithms is available.
    # tree_layout_view.SetLayoutStrategyToTree()
    tree_layout_view.renderer.background = colors.GetColor3d('Navy')
    tree_layout_view.renderer.background2 = colors.GetColor3d('MidnightBlue')
    tree_layout_view.render_window.window_name = 'MutableGraphHelper'
    tree_layout_view.Render()
    tree_layout_view.ResetCamera()
    tree_layout_view.interactor.Start()

if __name__ == '__main__':
    main()
```
