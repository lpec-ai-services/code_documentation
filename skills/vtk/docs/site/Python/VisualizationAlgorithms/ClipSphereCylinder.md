<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/ClipSphereCylinder/ -->

# ClipSphereCylinder

Repository source: [ClipSphereCylinder](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/ClipSphereCylinder.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestClipSphereCylinder.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestClipSphereCylinder.png?raw=true target=)

### Description

Clipping is implemented in [vtkClipPolyData](https://www.vtk.org/doc/nightly/html/classvtkClipPolyData.html) . Each polygonal data primitive implements the operation in its Clip() method using case tables. [vtkClipPolyData](https://www.vtk.org/doc/nightly/html/classvtkClipPolyData.html) has methods to control whether an implicit function provides the scalar data or whether the dataset’s scalar data will be used. Compute*ScalarDataOn()* uses the implicit function and *ComputeScalarDataOff()* uses the dataset’s scalar data. Two output polygonal datasets are produced. These are accessed with *GetOutput()* and *GetClippedOutput()* methods. *GetOutput()* returns the polygonal data that is “inside” the clipping region while *GetClippedOutput()* returns polygonal data that is “outside” the region. (Note that *GenerateClippedOutputOn()* must be enabled if you are to get the clipped output.) The meaning of inside and outside can be reversed using the *InsideOutOn()*.

This example shows a plane of quadrilaterals clipped with a boolean implicit function.

Info

See [Figure 9-48](../../VTKBook/09Chapter9.md#Figure%209-48) in [Chapter 9](../../VTKBook/09Chapter9.md) The [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/ClipSphereCylinder/)), ([PythonicAPI](../../PythonicAPI/VisualizationAlgorithms/ClipSphereCylinder.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ClipSphereCylinder.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkCylinder,
    vtkImplicitBoolean,
    vtkSphere
)
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import vtkClipPolyData
from vtkmodules.vtkFiltersSources import vtkPlaneSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Demonstrate the use of clipping on polygonal data
    #

    # create pipeline
    #
    plane = vtkPlaneSource()
    plane.SetXResolution(25)
    plane.SetYResolution(25)
    plane.SetOrigin(-1, -1, 0)
    plane.SetPoint1(1, -1, 0)
    plane.SetPoint2(-1, 1, 0)

    transformSphere = vtkTransform()
    transformSphere.Identity()
    transformSphere.Translate(0.4, -0.4, 0)
    transformSphere.Inverse()

    sphere = vtkSphere()
    sphere.SetTransform(transformSphere)
    sphere.SetRadius(.5)

    transformCylinder = vtkTransform()
    transformCylinder.Identity()
    transformCylinder.Translate(-0.4, 0.4, 0)
    transformCylinder.RotateZ(30)
    transformCylinder.RotateY(60)
    transformCylinder.RotateX(90)
    transformCylinder.Inverse()

    cylinder = vtkCylinder()
    cylinder.SetTransform(transformCylinder)
    cylinder.SetRadius(.3)

    boolean = vtkImplicitBoolean()
    boolean.AddFunction(cylinder)
    boolean.AddFunction(sphere)

    clipper = vtkClipPolyData()
    clipper.SetInputConnection(plane.GetOutputPort())
    clipper.SetClipFunction(boolean)
    clipper.GenerateClippedOutputOn()
    clipper.GenerateClipScalarsOn()
    clipper.SetValue(0)

    clipMapper = vtkPolyDataMapper()
    clipMapper.SetInputConnection(clipper.GetOutputPort())
    clipMapper.ScalarVisibilityOff()

    clipActor = vtkActor()
    clipActor.SetMapper(clipMapper)
    clipActor.GetProperty().SetDiffuseColor(colors.GetColor3d('MidnightBlue'))
    clipActor.GetProperty().SetRepresentationToWireframe()

    clipInsideMapper = vtkPolyDataMapper()
    clipInsideMapper.SetInputData(clipper.GetClippedOutput())
    clipInsideMapper.ScalarVisibilityOff()

    clipInsideActor = vtkActor()
    clipInsideActor.SetMapper(clipInsideMapper)
    clipInsideActor.GetProperty().SetDiffuseColor(colors.GetColor3d('LightBlue'))

    # Create graphics stuff
    #
    ren1 = vtkRenderer()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetWindowName('ClipSphereCylinder')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size
    #
    ren1.AddActor(clipActor)

    ren1.AddActor(clipInsideActor)
    ren1.SetBackground(colors.GetColor3d('Wheat'))
    ren1.ResetCamera()
    ren1.GetActiveCamera().Dolly(1.4)
    ren1.ResetCameraClippingRange()

    renWin.SetSize(640, 480)

    # render the image
    #
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
