<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/TessellatedBoxSource/ -->

# TessellatedBoxSource

Repository source: [TessellatedBoxSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/TessellatedBoxSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTessellatedBoxSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTessellatedBoxSource.png?raw=true target=)

### Description

Generates a box(cube) using [vtkTessellatedBoxSource](https://www.vtk.org/doc/nightly/html/classvtkTessellatedBoxSource.html) with 6 sides. The faces of the box can be subdivided into multiple triangles or quads.

Seealso

[Cube](Cube.md) generates multiple quads or triangles per side.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/TessellatedBoxSource/)), ([PythonicAPI](../../PythonicAPI/GeometricObjects/TessellatedBoxSource.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TessellatedBoxSource.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonExecutionModel import vtkAlgorithm
from vtkmodules.vtkFiltersGeneral import vtkShrinkFilter
from vtkmodules.vtkFiltersSources import vtkTessellatedBoxSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    bounds = [-10.0, 10.0, 10.0, 20.0, -5.0, 5.0]

    boxSource = vtkTessellatedBoxSource()
    boxSource.SetLevel(3)
    boxSource.QuadsOn()
    boxSource.SetBounds(bounds)
    boxSource.SetOutputPointsPrecision(vtkAlgorithm.SINGLE_PRECISION)

    shrink = vtkShrinkFilter()
    shrink.SetInputConnection(boxSource.GetOutputPort())
    shrink.SetShrinkFactor(.8)

    # Create a mapper and actor.
    mapper = vtkDataSetMapper()
    mapper.SetInputConnection(shrink.GetOutputPort())

    back = vtkProperty()
    back.SetColor(colors.GetColor3d('Tomato'))

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().EdgeVisibilityOn()
    actor.GetProperty().SetColor(colors.GetColor3d('Banana'))
    actor.SetBackfaceProperty(back)

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene.
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Silver'))

    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)
    renderer.ResetCameraClippingRange()

    # Render and interact.
    renderWindow.SetSize(640, 480)
    renderWindow.SetWindowName('TessellatedBoxSource')
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
