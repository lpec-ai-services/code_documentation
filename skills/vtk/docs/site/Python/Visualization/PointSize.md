<!-- source: https://examples.vtk.org/site/Python/Visualization/PointSize/ -->

# PointSize

Repository source: [PointSize](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/PointSize.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestPointSize.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestPointSize.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/PointSize/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PointSize.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkPointSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # create a rendering window and renderer
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('PointSize')

    # create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # create source
    src = vtkPointSource()
    src.SetCenter(0, 0, 0)
    src.SetNumberOfPoints(10)
    src.SetRadius(5)
    src.Update()

    # mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(src.GetOutputPort())

    # actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Yellow'))

    actor.GetProperty().SetPointSize(5)

    # assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('RoyalBLue'))

    # enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
