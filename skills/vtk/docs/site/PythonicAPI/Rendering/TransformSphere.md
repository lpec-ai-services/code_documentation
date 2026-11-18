<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/TransformSphere/ -->

# TransformSphere

Repository source: [TransformSphere](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/TransformSphere.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestTransformSphere.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestTransformSphere.png?raw=true target=)

### Description

This example extends the pipeline of the [ColoredSphere.py](ColoredSphere.md) example and shows the effects of type checking on the connectivity of process objects. We add a transform filter ([vtkTransformFilter](https://www.vtk.org/doc/nightly/html/classvtkTransformFilter.html)) to nonuniformly scale the sphere in the x-y-z directions. The transform filter only operates on objects with explicit point coordinate representation (i.e., a subclass of [vtkPointSet](https://www.vtk.org/doc/nightly/html/classvtkPointSet.html) ). However, the elevation filter generates the more general form [vtkDataSet](https://www.vtk.org/doc/nightly/html/classvtkDataSet.html) as output. Hence we cannot connect the transform filter to the elevation filter. But we can connect the transform filter to the sphere source, and then the elevation filter to the transform filter. (Note: an alternative method is to use [vtkCastToConcrete](https://www.vtk.org/doc/nightly/html/classvtkCastToConcrete.html) to perform run-time casting.)

Info

See [Figure 4-20](../../VTKBook/04Chapter4.md#Figure%204-20) in [Chapter 4](../../VTKBook/04Chapter4.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/TransformSphere/)), ([Python](../../Python/Rendering/TransformSphere.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TransformSphere.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import vtkElevationFilter
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphere = vtkSphereSource(phi_resolution=12, theta_resolution=12)

    a_transform = vtkTransform()
    a_transform.Scale(1, 1.5, 2)

    trans_filter = vtkTransformFilter(transform=a_transform)

    color_it = vtkElevationFilter(low_point=(0, 0, -1), high_point=(0, 0, 1))

    lut = vtkLookupTable(hue_range=(0.667, 0), saturation_range=(1, 1), value_range=(1, 1))

    mapper = vtkDataSetMapper(lookup_table=lut)
    sphere >> trans_filter >> color_it >> mapper

    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name='TransformSphere')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    renderer.AddActor(actor)
    renderer.ResetCamera()
    renderer.active_camera.Elevation(60.0)
    renderer.active_camera.Azimuth(30.0)
    renderer.ResetCameraClippingRange()

    ren_win.Render()

    # Interact with the data.
    iren.Start()

if __name__ == '__main__':
    main()
```
