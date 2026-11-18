<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/RubberBandZoom/ -->

# RubberBandZoom

Repository source: [RubberBandZoom](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/RubberBandZoom.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestRubberBandZoom.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestRubberBandZoom.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/RubberBandZoom/)), ([Java](https://examples.vtk.org/site/Java/Interaction/RubberBandZoom/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RubberBandZoom.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleRubberBandZoom
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='RubberBandZoom')
    render_window.AddRenderer(renderer)

    # An interactor
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(actor)

    render_window.Render()

    style = vtkInteractorStyleRubberBandZoom()
    render_window_interactor.interactor_style = style

    renderer.active_camera.Zoom(0.5)

    # Begin mouse interaction.
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
