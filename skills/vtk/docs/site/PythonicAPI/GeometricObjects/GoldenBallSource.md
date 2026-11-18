<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/GoldenBallSource/ -->

# GoldenBallSource

Repository source: [GoldenBallSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/GoldenBallSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestGoldenBallSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestGoldenBallSource.png?raw=true target=)

### Description

A [vtkGoldenBallSource](https://www.vtk.org/doc/nightly/html/classvtkGoldenBallSource.html) algorithm has been added to provide a method to construct a solid, tetrahedralized ball. It uses a Fibonacci spiral (generated using the “Golden Angle” of 180(√5 - 3)°) which is then projected out of the plane onto a sphere and Delaunay-tetrahedralized into a ball. It includes a “normal” vector field by default which is zero-length at the center of the ball.

Besides the spiral construction this algorithm is also distinct from the existing sphere source because it produces a solid rather than a bounding surface.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/GoldenBallSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GoldenBallSource.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkGoldenBallSource
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
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
    colors.SetColor("ParaViewBkg", 82, 87, 110, 255)

    # Create a golden ball.
    golden_ball_source = vtkGoldenBallSource(center=(0.0, 0.0, 0.0),
                                             radius=5.0, resolution=200,
                                             generate_normals=True,
                                             include_center_point=True)

    mapper = vtkDataSetMapper()
    golden_ball_source >> mapper

    actor_prop = vtkProperty(color=colors.GetColor3d('Gold'), edge_color=colors.GetColor3d('DarkSlateBlue'),
                             edge_visibility=True)
    actor = vtkActor(property=actor_prop, mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('ParaViewBkg'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='GoldenBallSource')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    render_window_interactor.interactor_style.SetCurrentStyleToTrackballCamera()

    renderer.AddActor(actor)
    renderer.ResetCamera()

    cow = vtkCameraOrientationWidget(parent_renderer=renderer,
                                     interactor=render_window_interactor)
    # Enable the widget.
    cow.On()

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
