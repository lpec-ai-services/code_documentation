<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/InteractorStyleTrackballActor/ -->

# InteractorStyleTrackballActor

Repository source: [InteractorStyleTrackballActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/InteractorStyleTrackballActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestInteractorStyleTrackballActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestInteractorStyleTrackballActor.png?raw=true target=)

### Description

Move, rotate, and scale an object in 3D.

Other languages

See ([Python](../../Python/Interaction/InteractorStyleTrackballActor.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**InteractorStyleTrackballActor.py**

```python
#!/usr/bin/env python3

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

    # Create a rendering window and renderer.
    ren = vtkRenderer(background=colors.GetColor3d('PaleGoldenrod'))
    ren_win = vtkRenderWindow(window_name='InteractorStyleTrackballActor')
    ren_win.AddRenderer(ren)

    # Create a render window interactor.
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    style = vtkInteractorStyleTrackballActor()
    iren.interactor_style = style

    # Create the source, mapper and actor.
    sphere_source = vtkSphereSource()

    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.SetMapper(mapper)
    actor.property.color = colors.GetColor3d('Chartreuse')

    # Assign the actor to the renderer.
    ren.AddActor(actor)

    # Enable the user interface interactor.
    iren.Initialize()
    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
