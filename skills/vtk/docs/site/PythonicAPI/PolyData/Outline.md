<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/Outline/ -->

# Outline

Repository source: [Outline](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/Outline.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestOutline.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestOutline.png?raw=true target=)

### Description

This example shows how to draw the outline of the dataset.

Seealso

[BoundingBox](../Utilities/BoundingBox.md) and [CubeAxesActor2D](../Visualization/CubeAxesActor2D.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/Outline/)), ([Python](../../Python/PolyData/Outline.md)), ([Java](https://examples.vtk.org/site/Java/PolyData/Outline/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Outline.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create a rendering window, renderer and interactor.
    ren = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    ren_win = vtkRenderWindow(window_name='Outline')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Create hte source.
    source = vtkConeSource(center=(0, 0, 0), resolution=100)
    # Mapper
    mapper1 = vtkPolyDataMapper()
    source >> mapper1
    # Actor
    actor1 = vtkActor(mapper=mapper1)
    actor1.property.color = colors.GetColor3d('MistyRose')

    # Outline
    outline = vtkOutlineFilter()
    mapper2 = vtkPolyDataMapper()
    source >> outline >> mapper2
    actor2 = vtkActor(mapper=mapper2)
    actor2.property.color = colors.GetColor3d('Gold')

    # Assign the actors to the renderer.
    ren.AddActor(actor1)
    ren.AddActor(actor2)
    ren.SetBackground(colors.GetColor3d('MidnightBlue'))

    # Enable user interaction.
    iren.Initialize()
    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
