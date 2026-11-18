<!-- source: https://examples.vtk.org/site/Python/Graphs/RandomGraphSource/ -->

# RandomGraphSource

Repository source: [RandomGraphSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Graphs/RandomGraphSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestRandomGraphSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestRandomGraphSource.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/RandomGraphSource/)), ([PythonicAPI](../../PythonicAPI/Graphs/RandomGraphSource.md)), ([Java](https://examples.vtk.org/site/Java/Graphs/RandomGraphSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RandomGraphSource.py**

```python
#!/usr/bin/env python
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInfovisCore import vtkRandomGraphSource
from vtkmodules.vtkInfovisLayout import vtkForceDirectedLayoutStrategy
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    colors = vtkNamedColors()

    random_graph_source = vtkRandomGraphSource()
    random_graph_source.SetNumberOfVertices(5)
    random_graph_source.SetNumberOfEdges(4)
    # This ensures repeatable results for testing. Turn this off for real use.
    random_graph_source.SetSeed(123)
    random_graph_source.Update()

    force_directed = vtkForceDirectedLayoutStrategy()

    graph_layout_view = vtkGraphLayoutView()
    graph_layout_view.AddRepresentationFromInput(random_graph_source.GetOutput())
    # If we create a layout object directly, just set the pointer through this method.
    # graph_layout_view.SetLayoutStrategy(force_directed)
    graph_layout_view.SetLayoutStrategyToForceDirected()
    graph_layout_view.GetRenderer().SetBackground(colors.GetColor3d('Navy'))
    graph_layout_view.GetRenderer().SetBackground2(colors.GetColor3d('MidnightBlue'))
    graph_layout_view.GetRenderWindow().SetWindowName('RandomGraphSource')
    graph_layout_view.Render()
    graph_layout_view.ResetCamera()
    graph_layout_view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
