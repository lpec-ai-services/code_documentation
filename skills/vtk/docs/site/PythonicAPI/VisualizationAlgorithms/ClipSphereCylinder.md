<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/ClipSphereCylinder/ -->

# ClipSphereCylinder

Repository source: [ClipSphereCylinder](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/ClipSphereCylinder.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestClipSphereCylinder.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestClipSphereCylinder.png?raw=true target=)

### Description

Clipping is implemented in [vtkClipPolyData](https://www.vtk.org/doc/nightly/html/classvtkClipPolyData.html) . Each polygonal data primitive implements the operation in its Clip() method using case tables. [vtkClipPolyData](https://www.vtk.org/doc/nightly/html/classvtkClipPolyData.html) has methods to control whether an implicit function provides the scalar data or whether the dataset’s scalar data will be used. Compute*ScalarDataOn()* uses the implicit function and *ComputeScalarDataOff()* uses the dataset’s scalar data. Two output polygonal datasets are produced. These are accessed with *GetOutput()* and *GetClippedOutput()* methods. *GetOutput()* returns the polygonal data that is “inside” the clipping region while *GetClippedOutput()* returns polygonal data that is “outside” the region. (Note that *GenerateClippedOutputOn()* must be enabled if you are to get the clipped output.) The meaning of inside and outside can be reversed using the *InsideOutOn()*.

This example shows a plane of quadrilaterals clipped with a boolean implicit function.

Info

See [Figure 9-48](../../VTKBook/09Chapter9.md#Figure%209-48) in [Chapter 9](../../VTKBook/09Chapter9.md) The [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/ClipSphereCylinder/)), ([Python](../../Python/VisualizationAlgorithms/ClipSphereCylinder.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ClipSphereCylinder.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

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

    # Demonstrate the use of clipping on polygonal data.

    # Create the pipeline.
    plane = vtkPlaneSource(x_resolution=25, y_resolution=25,
                           origin=(-1, -1, 0), point1=(1, -1, 0), point2=(-1, 1, 0))
    plane.update()

    transform_sphere = vtkTransform()
    transform_sphere.Identity()
    transform_sphere.Translate(0.4, -0.4, 0)
    transform_sphere.Inverse()

    sphere = vtkSphere(transform=transform_sphere, radius=0.5)

    transform_cylinder = vtkTransform()
    transform_cylinder.Identity()
    transform_cylinder.Translate(-0.4, 0.4, 0)
    transform_cylinder.RotateZ(30)
    transform_cylinder.RotateY(60)
    transform_cylinder.RotateX(90)
    transform_cylinder.Inverse()

    cylinder = vtkCylinder(radius=0.3, transform=transform_cylinder)

    boolean = vtkImplicitBoolean()
    boolean.AddFunction(cylinder)
    boolean.AddFunction(sphere)

    clipper = vtkClipPolyData(input_connection=plane.output_port, clip_function=boolean,
                              generate_clipped_output=True, generate_clip_scalars=True, value=0)
    clipper.update()

    clip_mapper = vtkPolyDataMapper(scalar_visibility=False)
    clipper >> clip_mapper

    clip_actor = vtkActor(mapper=clip_mapper)
    clip_actor.property.diffuse_color = colors.GetColor3d('MidnightBlue')
    clip_actor.property.representation = Property.Representation.VTK_WIREFRAME

    clip_inside_mapper = vtkPolyDataMapper(input_data=clipper.clipped_output, scalar_visibility=False)

    clip_inside_actor = vtkActor(mapper=clip_inside_mapper)
    clip_inside_actor.property.diffuse_color = colors.GetColor3d('LightBlue')

    # Create the graphics stuff.
    ren = vtkRenderer(background=colors.GetColor3d('Wheat'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name='ClipSphereCylinder')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer.
    ren.AddActor(clip_actor)

    ren.AddActor(clip_inside_actor)
    ren.ResetCamera()
    ren.active_camera.Dolly(1.4)
    ren.ResetCameraClippingRange()

    # Render the image.
    ren_win.Render()
    iren.Start()

@dataclass(frozen=True)
class Property:
    @dataclass(frozen=True)
    class Interpolation:
        VTK_FLAT: int = 0
        VTK_GOURAUD: int = 1
        VTK_PHONG: int = 2
        VTK_PBR: int = 3

    @dataclass(frozen=True)
    class Representation:
        VTK_POINTS: int = 0
        VTK_WIREFRAME: int = 1
        VTK_SURFACE: int = 2

if __name__ == '__main__':
    main()
```
