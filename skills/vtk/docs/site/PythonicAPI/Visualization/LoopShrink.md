<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/LoopShrink/ -->

# LoopShrink

Repository source: [LoopShrink](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/LoopShrink.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLoopShrink.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLoopShrink.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/LoopShrink/)), ([Python](../../Python/Visualization/LoopShrink.md)), ([Java](https://examples.vtk.org/site/Java/Visualization/LoopShrink/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LoopShrink.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkElevationFilter
from vtkmodules.vtkFiltersGeneral import vtkShrinkFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    renderer = vtkRenderer(background=colors.GetColor3d('LavenderBlush'))
    renderer.GetCullers().RemoveAllItems()

    ren_win = vtkRenderWindow(size=(600, 600), window_name='LoopShrink')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    sphere = vtkSphereSource(theta_resolution=12, phi_resolution=12)

    shrink = vtkShrinkFilter(shrink_factor=0.9)

    color_it = vtkElevationFilter()
    color_it.SetLowPoint(0, 0, -.5)
    color_it.SetHighPoint(0, 0, .5)

    mapper = vtkDataSetMapper()
    sphere >> shrink >> color_it >> mapper

    actor = vtkActor(mapper=mapper)

    renderer.AddActor(actor)

    ren_win.Render()

    renderer.GetActiveCamera().Zoom(1.5)

    #  Interact with the data.
    iren.Start()

if __name__ == '__main__':
    main()
```
