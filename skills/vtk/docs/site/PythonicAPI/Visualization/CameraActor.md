<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/CameraActor/ -->

# CameraActor

Repository source: [CameraActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/CameraActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCameraActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCameraActor.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/CameraActor/)), ([Java](https://examples.vtk.org/site/Java/Visualization/CameraActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CameraActor.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor, vtkCameraActor, vtkCamera, vtkPolyDataMapper
)

def main():
    named_colors = vtkNamedColors()

    # Sphere
    sphere_source = vtkSphereSource(radius=400)

    sphere_mapper = vtkPolyDataMapper()
    sphere_source >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.diffuse_color = named_colors.GetColor3d('Tomato')

    # Camera
    camera = vtkCamera()

    camera_actor = vtkCameraActor()
    camera_actor.SetCamera(camera)
    camera_actor.property.color = named_colors.GetColor3d('Black')

    # (Xmin,Xmax,Ymin,Ymax,Zmin,Zmax).
    bounds = camera_actor.bounds
    print(f'Bounds: ({fmt_floats(bounds, 0, 6, "g")})')

    # Visualize
    renderer = vtkRenderer(background=named_colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetWindowName('CameraActor')

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(sphere_actor)
    # Compute the active camera parameters.
    renderer.ResetCamera()

    # Set the camera parameters for the camera actor.
    camera.DeepCopy(renderer.active_camera)
    renderer.AddActor(camera_actor)

    # Position the camera so that we can see the camera actor.
    renderer.active_camera.SetPosition(1, 0, 0)
    renderer.active_camera.SetFocalPoint(0, 0, 0)
    renderer.active_camera.SetViewUp(0, 1, 0)
    renderer.active_camera.Azimuth(30)
    renderer.active_camera.Elevation(30)

    renderer.ResetCamera()

    render_window.Render()
    render_window_interactor.Start()

def fmt_floats(v, w=0, d=6, pt='f'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
