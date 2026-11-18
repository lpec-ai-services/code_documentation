<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ImplicitSelectionLoop/ -->

# ImplicitSelectionLoop

Repository source: [ImplicitSelectionLoop](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ImplicitSelectionLoop.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestImplicitSelectionLoop.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestImplicitSelectionLoop.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ImplicitSelectionLoop/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImplicitSelectionLoop.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkImplicitSelectionLoop
from vtkmodules.vtkFiltersCore import vtkClipPolyData
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)
from vtkmodules.vtkRenderingLOD import vtkLODActor

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource(phi_resolution=100, theta_resolution=100)

    selection_points = vtkPoints()

    selection_points.InsertPoint(0, -0.16553, 0.135971, 0.451972)
    selection_points.InsertPoint(1, -0.0880123, -0.134952, 0.4747)
    selection_points.InsertPoint(2, 0.00292618, -0.134604, 0.482459)
    selection_points.InsertPoint(3, 0.0641941, 0.067112, 0.490947)
    selection_points.InsertPoint(4, 0.15577, 0.0734765, 0.469245)
    selection_points.InsertPoint(5, 0.166667, -0.129217, 0.454622)
    selection_points.InsertPoint(6, 0.241259, -0.123363, 0.420581)
    selection_points.InsertPoint(7, 0.240334, 0.0727106, 0.432555)
    selection_points.InsertPoint(8, 0.308529, 0.0844311, 0.384357)
    selection_points.InsertPoint(9, 0.32672, -0.121674, 0.359187)
    selection_points.InsertPoint(10, 0.380721, -0.117342, 0.302527)
    selection_points.InsertPoint(11, 0.387804, 0.0455074, 0.312375)
    selection_points.InsertPoint(12, 0.43943, -0.111673, 0.211707)
    selection_points.InsertPoint(13, 0.470984, -0.0801913, 0.147919)
    selection_points.InsertPoint(14, 0.436777, 0.0688872, 0.233021)
    selection_points.InsertPoint(15, 0.44874, 0.188852, 0.109882)
    selection_points.InsertPoint(16, 0.391352, 0.254285, 0.176943)
    selection_points.InsertPoint(17, 0.373274, 0.154162, 0.294296)
    selection_points.InsertPoint(18, 0.274659, 0.311654, 0.276609)
    selection_points.InsertPoint(19, 0.206068, 0.31396, 0.329702)
    selection_points.InsertPoint(20, 0.263789, 0.174982, 0.387308)
    selection_points.InsertPoint(21, 0.213034, 0.175485, 0.417142)
    selection_points.InsertPoint(22, 0.169113, 0.261974, 0.390286)
    selection_points.InsertPoint(23, 0.102552, 0.25997, 0.414814)
    selection_points.InsertPoint(24, 0.131512, 0.161254, 0.454705)
    selection_points.InsertPoint(25, 0.000192443, 0.156264, 0.475307)
    selection_points.InsertPoint(26, -0.0392091, 0.000251724, 0.499943)
    selection_points.InsertPoint(27, -0.096161, 0.159646, 0.46438)

    loop = vtkImplicitSelectionLoop(loop=selection_points)

    clip = vtkClipPolyData(clip_function=loop, value=0.0)

    clip_mapper = vtkPolyDataMapper(scalar_visibility=False)
    sphere_source >> clip >> clip_mapper

    back_prop = vtkProperty()
    back_prop.color = colors.GetColor3d('Tomato')

    clip_actor = vtkLODActor(mapper=clip_mapper, backface_property=back_prop)
    clip_actor.property.color = colors.GetColor3d('Banana')

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))

    render_window = vtkRenderWindow(size=(500, 500), window_name='ImplicitSelectionLoop')
    render_window.AddRenderer(renderer)

    renderer.AddActor(clip_actor)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Get a good orientation.
    renderer.ResetCamera()
    renderer.active_camera.Azimuth(22.5)
    renderer.active_camera.Elevation(10.0)
    renderer.active_camera.Zoom(1.5)

    render_window.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
