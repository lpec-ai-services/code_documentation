<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/SphereSource/ -->

# SphereSource

Repository source: [SphereSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/SphereSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestSphereSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestSphereSource.png?raw=true target=)

### Description

[vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html) object creates a sphere (represented by polygons) of specified radius centered at the origin.

The resolution (polygonal discretization) in both the latitude (phi) and longitude (theta) directions can be specified.

It also is possible to create partial spheres by specifying maximum phi and theta angles. By default, the surface tessellation of the sphere uses triangles; however you can set LatLongTessellation to produce a tessellation using quadrilaterals.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/SphereSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SphereSource.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkProperty
)

def main():
    colors = vtkNamedColors()
    colors.SetColor("ParaViewBkg", 82, 87, 110, 255)

    # Create a sphere.
    sphere_source = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=5.0,
                                    phi_resolution=50, theta_resolution=50,
                                    lat_long_tessellation=False)

    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor_prop = vtkProperty(color=colors.GetColor3d('Peru'), edge_color=colors.GetColor3d('DarkSlateBlue'),
                             edge_visibility=True)
    actor = vtkActor(property=actor_prop, mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('ParaViewBkg'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='SphereSource')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    render_window_interactor.interactor_style.SetCurrentStyleToTrackballCamera()

    renderer.AddActor(actor)

    cow = vtkCameraOrientationWidget(parent_renderer=renderer,
                                     interactor=render_window_interactor)
    # Enable the widget.
    cow.On()

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
