<!-- source: https://examples.vtk.org/site/Python/PolyData/RotationAroundLine/ -->

# RotationAroundLine

Repository source: [RotationAroundLine](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/PolyData/RotationAroundLine.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/PolyData/TestRotationAroundLine.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/PolyData/TestRotationAroundLine.png?raw=true target=)

### Description

NOTE: this example shows both the original and the rotated object using different colors. Not exactly equivalent to the C++ example with the same name.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/RotationAroundLine/)), ([Java](https://examples.vtk.org/site/Java/PolyData/RotationAroundLine/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RotationAroundLine.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import vtkTransformPolyDataFilter
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

    # Create a rendering window and renderer
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(640, 480)
    renWin.SetWindowName('RotationAroundLine')

    # Create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Create arrow
    source = vtkArrowSource()

    # Create a transform that rotates the arrow 45° around the z-axis
    transform = vtkTransform()
    transform.RotateWXYZ(45, 0, 0, 1)
    transformFilter = vtkTransformPolyDataFilter()
    transformFilter.SetTransform(transform)
    transformFilter.SetInputConnection(source.GetOutputPort())
    transformFilter.Update()

    # Mapper for the original arrow
    coneMapper1 = vtkPolyDataMapper()
    coneMapper1.SetInputConnection(source.GetOutputPort())

    # Another mapper for the rotated arrow
    coneMapper2 = vtkPolyDataMapper()
    coneMapper2.SetInputConnection(transformFilter.GetOutputPort())

    # Actor for original arrow
    actor1 = vtkActor()
    actor1.SetMapper(coneMapper1)

    # Actor for rotated arrow
    actor2 = vtkActor()
    actor2.SetMapper(coneMapper2)

    # Color the original arrow
    actor1.GetProperty().SetColor(colors.GetColor3d('LightCoral'))
    # Color rotated arrow
    actor2.GetProperty().SetColor(colors.GetColor3d('PaleTurquoise'))

    # Assign actor to the renderer
    ren.AddActor(actor1)
    ren.AddActor(actor2)
    ren.SetBackground(colors.GetColor3d('SlateGray'));

    # Enable the user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
