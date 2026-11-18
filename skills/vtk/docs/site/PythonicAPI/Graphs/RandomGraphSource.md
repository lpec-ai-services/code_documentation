<!-- source: https://examples.vtk.org/site/PythonicAPI/Graphs/RandomGraphSource/ -->

# RandomGraphSource

Repository source: [RandomGraphSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Graphs/RandomGraphSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Graphs/TestRandomGraphSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Graphs/TestRandomGraphSource.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/RandomGraphSource/)), ([Python](../../Python/Graphs/RandomGraphSource.md)), ([Java](https://examples.vtk.org/site/Java/Graphs/RandomGraphSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RandomGraphSource.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInfovisCore import vtkRandomGraphSource
# noinspection PyUnresolvedReferences
from vtkmodules.vtkInfovisLayout import vtkForceDirectedLayoutStrategy
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

def main():
    colors = vtkNamedColors()

    # seed=123 ensures repeatable results for testing. Remove this off for real use.
    random_graph_source = vtkRandomGraphSource(number_of_vertices=5, number_of_edges=4, seed=123)
    random_graph_source.update()

    # force_directed = vtkForceDirectedLayoutStrategy()

    graph_layout_view = vtkGraphLayoutView()
    graph_layout_view.AddRepresentationFromInput(random_graph_source.output)
    # If we create a layout object directly, just set the pointer through this method.
    # graph_layout_view.SetLayoutStrategy(force_directed)
    graph_layout_view.SetLayoutStrategyToForceDirected()
    graph_layout_view.renderer.background = colors.GetColor3d('Navy')
    graph_layout_view.renderer.background2 = colors.GetColor3d('MidnightBlue')
    graph_layout_view.render_window.window_name = 'RandomGraphSource'
    graph_layout_view.Render()
    graph_layout_view.ResetCamera()
    graph_layout_view.interactor.Start()

if __name__ == '__main__':
    main()
```
