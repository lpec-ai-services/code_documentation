<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/ShrinkCube/ -->

# ShrinkCube

Repository source: [ShrinkCube](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/ShrinkCube.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestShrinkCube.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestShrinkCube.png?raw=true target=)

### Description

Generates a cube using [vtkCubeSource](https://www.vtk.org/doc/nightly/html/classvtkCubeSource.html), then a shrink filter is applied.

[vtkShrinkFilter](https://www.vtk.org/doc/nightly/html/classvtkShrinkFilter.html) object shrinks cells composing an arbitrary data set towards their centroid. The centroid of a cell is computed as the average position of the cell points. Shrinking results in disconnecting the cells from one another.

Seealso

[TessellatedBoxSource](TessellatedBoxSource.md) generates multiple quads or triangles per side.

Info

See [Figure 5-17](../../VTKBook/05Chapter5.md#Figure%205-17) in [Chapter 5](../../VTKBook/05Chapter5.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/ShrinkCube/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/ShrinkCube/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ShrinkCube.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeneral import vtkShrinkFilter
from vtkmodules.vtkFiltersSources import vtkCubeSource
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

    # Create a cube.
    cubeSource = vtkCubeSource()

    shrink = vtkShrinkFilter()
    shrink.SetInputConnection(cubeSource.GetOutputPort())
    shrink.SetShrinkFactor(0.9)

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

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Silver'))

    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)
    renderer.ResetCameraClippingRange()

    # Render and interact
    renderWindow.SetWindowName('ShrinkCube')
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
