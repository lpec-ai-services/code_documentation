<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/ExtractData/ -->

# ExtractData

Repository source: [ExtractData](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/ExtractData.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestExtractData.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestExtractData.png?raw=true target=)

### Description

This example takes advantage of the properties of implicit functions to select and cut data. In particular it uses the region separation property to select data. Selecting or extracting data with an implicit function means choosing cells and points (and associated attribute data) that lie within a particular region of the function. To determine whether a point x-y-z lies within a region, we simply evaluate the point and examine the sign of the result. A cell lies in a region if all its points lie in the region. Here, two ellipses are used in combination to select voxels within a volume dataset. Note that extracting data often changes the structure of the dataset. In this example the input type is a image data dataset, while the output type is an unstructured grid dataset.

Info

See [Figure 6-24](../../VTKBook/06Chapter6.md#Figure%206-24) in [Chapter 6](../../VTKBook/06Chapter6.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/ExtractData/)), ([Python](../../Python/VisualizationAlgorithms/ExtractData.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractData.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkImplicitBoolean,
    vtkQuadric,
    vtkSphere
)
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersExtraction import vtkExtractGeometry
from vtkmodules.vtkFiltersGeneral import vtkShrinkFilter
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkImagingHybrid import vtkSampleFunction
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    quadric = vtkQuadric(coefficients=(0.5, 1, 0.2, 0, 0.1, 0, 0, 0.2, 0, 0))

    sample = vtkSampleFunction(implicit_function=quadric, sample_dimensions=(50, 50, 50), compute_normals=False)

    trans = vtkTransform()
    trans.Scale(1, 0.5, 0.333)

    sphere = vtkSphere(radius=0.25)
    sphere.SetTransform(trans)

    trans2 = vtkTransform()
    trans2.Scale(0.25, 0.5, 1.0)

    sphere2 = vtkSphere(radius=0.25)
    sphere2.SetTransform(trans2)

    boolean_union = vtkImplicitBoolean(operation_type=vtkImplicitBoolean.VTK_UNION)
    boolean_union.AddFunction(sphere)
    boolean_union.AddFunction(sphere2)

    extract = vtkExtractGeometry()
    extract.SetImplicitFunction(boolean_union)

    shrink = vtkShrinkFilter(shrink_factor=0.5)

    data_mapper = vtkDataSetMapper()
    sample >> extract >> shrink >> data_mapper
    data_actor = vtkActor(mapper=data_mapper)

    # outline
    outline = vtkOutlineFilter()

    outline_mapper = vtkPolyDataMapper()
    sample >> outline >> outline_mapper

    outline_actor = vtkActor(mapper=outline_mapper)
    outline_actor.property.color = colors.GetColor3d('Black')

    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))

    ren_win = vtkRenderWindow(size=(640, 480), window_name='ExtractData')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer.
    ren.AddActor(outline_actor)
    ren.AddActor(data_actor)

    ren_win.Render()
    ren.active_camera.Azimuth(30)
    ren.active_camera.Elevation(30)

    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
