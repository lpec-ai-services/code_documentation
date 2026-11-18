<!-- source: https://examples.vtk.org/site/PythonicAPI/Annotation/PolarAxesActor/ -->

# PolarAxesActor

Repository source: [PolarAxesActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Annotation/PolarAxesActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Annotation/TestPolarAxesActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Annotation/TestPolarAxesActor.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Annotation/PolarAxesActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PolarAxesActor.py**

```python
#!/usr/bin/env python3

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonComputationalGeometry import vtkParametricEnneper
from vtkmodules.vtkFiltersSources import vtkParametricFunctionSource
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingAnnotation import vtkPolarAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # The source will be a parametric function.
    src = vtkParametricEnneper()
    fn_src = vtkParametricFunctionSource()
    fn_src.SetParametricFunction(src)

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    fn_src >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('CornflowerBlue')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='PolarAxesActor')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    render_window_interactor.interactor_style.SetCurrentStyleToTrackballCamera()

    bounds = fn_src.update().output.bounds
    radius = math.sqrt(abs(dot_product((bounds[0], bounds[2]), (bounds[1], bounds[3]))))
    pole = (0.0, 0.0, bounds[5])

    polar_axes_actor = vtkPolarAxesActor(pole=pole, maximum_radius=radius,
                                         requested_number_of_polar_axes=5,
                                         minimum_angle=-45.0, maximum_angle=135.0)

    axes_prop = polar_axes_actor.polar_axis_property
    axes_prop.color = colors.GetColor3d('Red')
    arcs_prop = polar_axes_actor.polar_arcs_property
    arcs_prop.color = colors.GetColor3d('Yellow')
    arcs_prop.line_width = 1.0

    polar_axes_actor.secondary_radial_axes_property = axes_prop
    polar_axes_actor.last_radial_axis_property = axes_prop
    polar_axes_actor.secondary_polar_arcs_property = arcs_prop

    # Add the actor to the scene.
    renderer.AddActor(actor)
    renderer.AddActor(polar_axes_actor)

    renderer.active_camera.parallel_projection = True
    polar_axes_actor.SetCamera(renderer.active_camera)
    renderer.ResetCamera()

    cow = vtkCameraOrientationWidget(parent_renderer=renderer,
                                     interactor=render_window_interactor)
    # Enable the widget.
    cow.On()

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

def dot_product(v1, v2):
    total = 0.0
    for x, y in zip(v1, v2):
        total += x * y
    return total

if __name__ == '__main__':
    main()
```
