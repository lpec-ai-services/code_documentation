<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Arrow/ -->

# Arrow

Repository source: [Arrow](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Arrow.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestArrow.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestArrow.png?raw=true target=)

### Description

[vtkArrowSource](https://www.vtk.org/doc/nightly/html/classvtkArrowSource.html) object appends a cylinder to a cone to form an arrow.

The shaft base is always at (0,0,0). The arrow tip is always at (1,0,0). If "Invert" is true, then the ends are flipped i.e. tip is at (0,0,0) while base is at (1, 0, 0).

The resolution of the cone and shaft can be set and default to 6.

The radius of the cone and shaft can be set and default to 0.03 and 0.1. The length of the tip can also be set, and defaults to 0.35.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Arrow/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/Arrow/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Arrow/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Arrow.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkArrowSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    arrowSource = vtkArrowSource()
    # arrowSource.SetShaftRadius(0.01)
    # arrowSource.SetTipLength(.9)

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(arrowSource.GetOutputPort())
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Arrow')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('MidnightBlue'))

    renderWindow.SetWindowName('Arrow')
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
