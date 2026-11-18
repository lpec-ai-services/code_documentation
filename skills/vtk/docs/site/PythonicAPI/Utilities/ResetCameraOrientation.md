<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/ResetCameraOrientation/ -->

# ResetCameraOrientation

Repository source: [ResetCameraOrientation](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/ResetCameraOrientation.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Utilities/TestResetCameraOrientation.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Utilities/TestResetCameraOrientation.png?raw=true target=)

### Description

This example demonstrates how to reset the camera orientation.

In this case, the original orientation is stored, a new orientation calculated, and, finally the original orientation is restored. The original, new and restored orientations of the cone are displayed in one second intervals. After this you can interact with the scene.

To set the camera position, you can use:

- `SetPosition`, `SetFocalPoint`, `SetViewUp`, `SetDistance`, `SetClippingRange`
- `Roll`, `Elevation`, `Azimuth`
- `SetRoll`, `Pitch`, `Yaw`

If you haven't used `SetDistance` or `SetClippingRange` remember to `ren->ResetCamera();` or `ren.ResetCamera()`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/ResetCameraOrientation/)), ([Python](../../Python/Utilities/ResetCameraOrientation.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ResetCameraOrientation.py**

```python
from time import sleep

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
# noinspection PyUnresolvedReferences
from vtkmodules.vtkInteractionStyle import (
    vtkInteractorStyleTrackballCamera)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def comma_separated_list(v, precision=6, width=10):
    """
    Produce a comma-separated string of numbers from a list.
    :param v: The list of floats.
    :param precision: Number of decimal places.
    :param width: The width.
    :return: A comma-separated string.
    """
    res = list()
    for p in v:
        res.append(f'{p:{width}.{precision}f}')
    return ','.join(res)

def get_orientation(ren):
    """
    Get the camera orientation.
    :param ren: The renderer.
    :return: The orientation parameters.
    """
    p = dict()
    camera = ren.active_camera
    p['position'] = camera.position
    p['focal point'] = camera.focal_point
    p['view up'] = camera.view_up
    p['distance'] = camera.distance
    p['clipping range'] = camera.clipping_range
    p['orientation'] = camera.orientation
    return p

def set_orientation(ren, p):
    """
    Set the orientation of the camera.
    :param ren: The renderer.
    :param p: The orientation parameters.
    :return:
    """
    camera = ren.active_camera
    camera.position = p['position']
    camera.focal_point = p['focal point']
    camera.view_up = p['view up']
    camera.distance = p['distance']
    camera.clipping_range = p['clipping range']

def main(argv):
    colors = vtkNamedColors()

    cone = vtkConeSource(height=3.0, radius=1.0, resolution=10)

    cone_mapper = vtkPolyDataMapper()
    cone >> cone_mapper

    cone_actor = vtkActor(mapper=cone_mapper)
    cone_actor.property.color = colors.GetColor3d('Bisque')

    ren = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    ren.AddActor(cone_actor)

    ren_win = vtkRenderWindow(size=(600, 600), window_name='ResetCameraOrientation')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    camera = ren.active_camera
    camera.SetRoll(15)
    camera.Elevation(-15)
    camera.Azimuth(30)
    ren.ResetCamera()

    ren_win.Render()
    original_orient = get_orientation(ren)
    s = f'{"Original orientation:":23s}'
    s += comma_separated_list(original_orient["orientation"])
    print(s)
    sleep(1)

    camera.position = (-3.568189, 5.220048, 2.352639)
    camera.focal_point = (-0.399044, -0.282865, 0.131438)
    camera.view_up = (0.623411, 0.573532, -0.531431)
    camera.distance = 6.727500
    camera.clipping_range = (3.001430, 11.434082)
    # No need to use ren.ResetCamera() as we have all the parameters.
    ren_win.Render()
    new_orient = get_orientation(ren)
    s = f'{"New orientation:":23s}'
    s += comma_separated_list(new_orient["orientation"])
    print(s)
    sleep(1)

    print('Reloading the original orientation.')
    set_orientation(ren, original_orient)
    ren_win.Render()
    check = get_orientation(ren)
    s = f'{"Final orientation:":23s}'
    s += comma_separated_list(check["orientation"])
    print(s)
    sleep(1)

    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    import sys

    main(sys.argv)
```
