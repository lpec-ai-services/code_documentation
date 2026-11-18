<!-- source: https://examples.vtk.org/site/Python/Interaction/InteractorStyleTrackballActor/ -->

# InteractorStyleTrackballActor

Repository source: [InteractorStyleTrackballActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Interaction/InteractorStyleTrackballActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Interaction/TestInteractorStyleTrackballActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Interaction/TestInteractorStyleTrackballActor.png?raw=true target=)

### Description

Move, rotate, and scale an object in 3D.

Other languages

See ([PythonicAPI](../../PythonicAPI/Interaction/InteractorStyleTrackballActor.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**InteractorStyleTrackballActor.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballActor
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
    renWin.SetWindowName('InteractorStyleTrackballActor')

    # create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    style = vtkInteractorStyleTrackballActor()
    iren.SetInteractorStyle(style)

    # create source
    sphereSource = vtkSphereSource()

    # mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())

    # actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Chartreuse'))

    # assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('PaleGoldenrod'))

    # enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
