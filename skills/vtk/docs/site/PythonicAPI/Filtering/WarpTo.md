<!-- source: https://examples.vtk.org/site/PythonicAPI/Filtering/WarpTo/ -->

# WarpTo

Repository source: [WarpTo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Filtering/WarpTo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestWarpTo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestWarpTo.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/WarpTo/)), ([Python](../../Python/Filtering/WarpTo.md)), ([Java](https://examples.vtk.org/site/Java/Filtering/WarpTo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**WarpTo.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkTubeFilter
from vtkmodules.vtkFiltersGeneral import vtkWarpTo
from vtkmodules.vtkFiltersSources import vtkLineSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()
    # Create the RenderWindow, Renderer and both Actors.
    renderer = vtkRenderer(background=colors.GetColor3d('Green'))
    ren_win = vtkRenderWindow(window_name='WarpTo')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Create a line.
    line_source = vtkLineSource(point1=(0.0, 0.0, 0.0), point2=(0.0, 1.0, 0.0), resolution=20)

    # Create a tube (cylinder) around the line.
    # Default for radius is 0.5.
    tube_filter = vtkTubeFilter(radius=0.01, number_of_sides=50)

    warp_to = vtkWarpTo(position=(10, 1, 0), scale_factor=5, absolute=True)

    mapper = vtkDataSetMapper(scalar_visibility=False)
    line_source >> tube_filter >> warp_to >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('Gold')

    renderer.AddActor(actor)

    ren_win.Render()

    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
