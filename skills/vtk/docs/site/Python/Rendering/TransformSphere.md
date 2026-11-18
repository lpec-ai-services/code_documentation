<!-- source: https://examples.vtk.org/site/Python/Rendering/TransformSphere/ -->

# TransformSphere

Repository source: [TransformSphere](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Rendering/TransformSphere.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestTransformSphere.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestTransformSphere.png?raw=true target=)

### Description

This example extends the pipeline of the [ColoredSphere.py](ColoredSphere.md) example and shows the effects of type checking on the connectivity of process objects. We add a transform filter ([vtkTransformFilter](https://www.vtk.org/doc/nightly/html/classvtkTransformFilter.html)) to nonuniformly scale the sphere in the x-y-z directions. The transform filter only operates on objects with explicit point coordinate representation (i.e., a subclass of [vtkPointSet](https://www.vtk.org/doc/nightly/html/classvtkPointSet.html) ). However, the elevation filter generates the more general form [vtkDataSet](https://www.vtk.org/doc/nightly/html/classvtkDataSet.html) as output. Hence we cannot connect the transform filter to the elevation filter. But we can connect the transform filter to the sphere source, and then the elevation filter to the transform filter. (Note: an alternative method is to use [vtkCastToConcrete](https://www.vtk.org/doc/nightly/html/classvtkCastToConcrete.html) to perform run-time casting.)

Info

See [Figure 4-20](../../VTKBook/04Chapter4.md#Figure%204-20) in [Chapter 4](../../VTKBook/04Chapter4.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/TransformSphere/)), ([PythonicAPI](../../PythonicAPI/Rendering/TransformSphere.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TransformSphere.py**

```python
#!/usr/bin/env python

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
    renderer = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    sphere = vtkSphereSource()
    sphere.SetThetaResolution(12)
    sphere.SetPhiResolution(12)

    aTransform = vtkTransform()
    aTransform.Scale(1, 1.5, 2)

    transFilter = vtkTransformFilter()
    transFilter.SetInputConnection(sphere.GetOutputPort())
    transFilter.SetTransform(aTransform)

    colorIt = vtkElevationFilter()
    colorIt.SetInputConnection(transFilter.GetOutputPort())
    colorIt.SetLowPoint(0, 0, -1)
    colorIt.SetHighPoint(0, 0, 1)

    lut = vtkLookupTable()
    lut.SetHueRange(0.667, 0)
    lut.SetSaturationRange(1, 1)
    lut.SetValueRange(1, 1)

    mapper = vtkDataSetMapper()
    mapper.SetLookupTable(lut)
    mapper.SetInputConnection(colorIt.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("SlateGray"))
    renderer.ResetCamera()
    renderer.GetActiveCamera().Elevation(60.0)
    renderer.GetActiveCamera().Azimuth(30.0)
    renderer.ResetCameraClippingRange()

    renWin.SetSize(640, 480)
    renWin.SetWindowName('TransformSphere')

    renWin.Render()

    # Interact with the data.
    iren.Start()

if __name__ == '__main__':
    main()
```
