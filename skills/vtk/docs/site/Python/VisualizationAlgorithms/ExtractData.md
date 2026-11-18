<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/ExtractData/ -->

# ExtractData

Repository source: [ExtractData](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/ExtractData.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestExtractData.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestExtractData.png?raw=true target=)

### Description

This example takes advantage of the properties of implicit functions to select and cut data. In particular it uses the region separation property to select data. Selecting or extracting data with an implicit function means choosing cells and points (and associated attribute data) that lie within a particular region of the function. To determine whether a point x-y-z lies within a region, we simply evaluate the point and examine the sign of the result. A cell lies in a region if all its points lie in the region. Here, two ellipses are used in combination to select voxels within a volume dataset. Note that extracting data often changes the structure of the dataset. In this example the input type is a image data dataset, while the output type is an unstructured grid dataset.

Info

See [Figure 6-24](../../VTKBook/06Chapter6.md#Figure%206-24) in [Chapter 6](../../VTKBook/06Chapter6.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/ExtractData/)), ([PythonicAPI](../../PythonicAPI/VisualizationAlgorithms/ExtractData.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractData.py**

```python
#!/usr/bin/env python

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

    ren1 = vtkRenderer()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    quadric = vtkQuadric()
    quadric.SetCoefficients(0.5, 1, 0.2, 0, 0.1, 0, 0, 0.2, 0, 0)

    sample = vtkSampleFunction()
    sample.SetSampleDimensions(50, 50, 50)
    sample.SetImplicitFunction(quadric)
    sample.ComputeNormalsOff()

    trans = vtkTransform()
    trans.Scale(1, 0.5, 0.333)

    sphere = vtkSphere()
    sphere.SetRadius(0.25)
    sphere.SetTransform(trans)

    trans2 = vtkTransform()
    trans2.Scale(0.25, 0.5, 1.0)

    sphere2 = vtkSphere()
    sphere2.SetRadius(0.25)
    sphere2.SetTransform(trans2)

    booleanUnion = vtkImplicitBoolean()
    booleanUnion.AddFunction(sphere)
    booleanUnion.AddFunction(sphere2)
    booleanUnion.SetOperationType(0)  # boolean Union

    extract = vtkExtractGeometry()
    extract.SetInputConnection(sample.GetOutputPort())
    extract.SetImplicitFunction(booleanUnion)

    shrink = vtkShrinkFilter()
    shrink.SetInputConnection(extract.GetOutputPort())
    shrink.SetShrinkFactor(0.5)

    dataMapper = vtkDataSetMapper()
    dataMapper.SetInputConnection(shrink.GetOutputPort())
    dataActor = vtkActor()
    dataActor.SetMapper(dataMapper)

    # outline
    outline = vtkOutlineFilter()
    outline.SetInputConnection(sample.GetOutputPort())

    outlineMapper = vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outline.GetOutputPort())

    outlineActor = vtkActor()
    outlineActor.SetMapper(outlineMapper)
    outlineActor.GetProperty().SetColor(0, 0, 0)

    # Add the actors to the renderer, set the background and size
    #
    ren1.AddActor(outlineActor)
    ren1.AddActor(dataActor)
    ren1.SetBackground(colors.GetColor3d("SlateGray"))

    renWin.SetSize(640, 480)
    renWin.SetWindowName('ExtractData')

    renWin.Render()
    ren1.GetActiveCamera().Azimuth(30)
    ren1.GetActiveCamera().Elevation(30)

    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
