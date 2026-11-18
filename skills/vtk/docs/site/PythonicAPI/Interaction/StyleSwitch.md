<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/StyleSwitch/ -->

# StyleSwitch

Repository source: [StyleSwitch](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/StyleSwitch.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestStyleSwitch.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestStyleSwitch.png?raw=true target=)

### Description

The class [vtkInteractorStyleSwitch](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyleSwitch.html) allows handles interactively switching between four interactor styles -- joystick actor, joystick camera, trackball actor, and trackball camera. Type 'j' or 't' to select joystick or trackball, and type 'c' or 'a' to select camera or actor. The default interactor style is joystick camera.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/StyleSwitch/)), ([Java](https://examples.vtk.org/site/Java/Interaction/StyleSwitch/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**StyleSwitch.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleSwitch
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
    render_window = vtkRenderWindow(window_name='StyleSwitch')
    render_window.AddRenderer(renderer)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    style = vtkInteractorStyleSwitch()
    render_window_interactor.interactor_style = style

    # Add the actors to the scene.
    renderer.AddActor(actor)

    # Render
    render_window.Render()

    # Begin mouse interaction.
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
