<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/SourceObjectsDemo/ -->

# SourceObjectsDemo

Repository source: [SourceObjectsDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/SourceObjectsDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestSourceObjectsDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestSourceObjectsDemo.png?raw=true target=)

### Description

Examples of source objects that procedurally generate polygonal models. These nine images represent just some of the capability of VTK. From upper left in reading order: sphere, cone, cylinder, cube, plane, text, random point cloud, disk (with or without hole), and line source.

Info

See [Figure 3-26](../../VTKBook/03Chapter3.md#Figure%203-26) in [Chapter 3](../../VTKBook/03Chapter3.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/SourceObjectsDemo/)), ([PythonicAPI](../../PythonicAPI/GeometricObjects/SourceObjectsDemo.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SourceObjectsDemo.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkCubeSource,
    vtkCylinderSource,
    vtkDiskSource,
    vtkLineSource,
    vtkPlaneSource,
    vtkPointSource,
    vtkSphereSource,
    vtkTextSource
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkActor2D,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextMapper,
    vtkTextProperty
)

def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor('BkgColor', [51, 77, 102, 255])

    sourceObjects = list()
    sourceObjects.append(vtkSphereSource())
    sourceObjects[-1].SetPhiResolution(21)
    sourceObjects[-1].SetThetaResolution(21)

    sourceObjects.append(vtkConeSource())
    sourceObjects[-1].SetResolution(51)

    sourceObjects.append(vtkCylinderSource())
    sourceObjects[-1].SetResolution(51)

    sourceObjects.append(vtkCubeSource())
    sourceObjects.append(vtkPlaneSource())
    sourceObjects.append(vtkTextSource())
    sourceObjects[-1].SetText('Hello')
    sourceObjects[-1].BackingOff()

    sourceObjects.append(vtkPointSource())
    sourceObjects[-1].SetNumberOfPoints(500)

    sourceObjects.append(vtkDiskSource())
    sourceObjects[-1].SetCircumferentialResolution(51)

    sourceObjects.append(vtkLineSource())

    renderers = list()
    mappers = list()
    actors = list()
    textmappers = list()
    textactors = list()

    # Create one text property for all.
    textProperty = vtkTextProperty()
    textProperty.SetFontSize(16)
    textProperty.SetJustificationToCentered()
    textProperty.SetColor(colors.GetColor3d('LightGoldenrodYellow'))

    backProperty = vtkProperty()
    backProperty.SetColor(colors.GetColor3d('Tomato'))

    # Create a source, renderer, mapper, and actor
    # for each object.
    for i in range(0, len(sourceObjects)):
        mappers.append(vtkPolyDataMapper())
        mappers[i].SetInputConnection(sourceObjects[i].GetOutputPort())

        actors.append(vtkActor())
        actors[i].SetMapper(mappers[i])
        actors[i].GetProperty().SetColor(colors.GetColor3d('PeachPuff'))
        actors[i].SetBackfaceProperty(backProperty)

        textmappers.append(vtkTextMapper())
        textmappers[i].SetInput(sourceObjects[i].GetClassName())
        textmappers[i].SetTextProperty(textProperty)

        textactors.append(vtkActor2D())
        textactors[i].SetMapper(textmappers[i])
        textactors[i].SetPosition(120, 16)
        renderers.append(vtkRenderer())

    gridDimensions = 3

    # We need a renderer even if there is no actor.
    for i in range(len(sourceObjects), gridDimensions ** 2):
        renderers.append(vtkRenderer())

    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('SourceObjectsDemo')
    rendererSize = 300
    renderWindow.SetSize(rendererSize * gridDimensions, rendererSize * gridDimensions)

    for row in range(0, gridDimensions):
        for col in range(0, gridDimensions):
            index = row * gridDimensions + col
            x0 = float(col) / gridDimensions
            y0 = float(gridDimensions - row - 1) / gridDimensions
            x1 = float(col + 1) / gridDimensions
            y1 = float(gridDimensions - row) / gridDimensions
            renderWindow.AddRenderer(renderers[index])
            renderers[index].SetViewport(x0, y0, x1, y1)

            if index > (len(sourceObjects) - 1):
                continue

            renderers[index].AddActor(actors[index])
            renderers[index].AddActor(textactors[index])
            renderers[index].SetBackground(colors.GetColor3d('BkgColor'))
            renderers[index].ResetCamera()
            renderers[index].GetActiveCamera().Azimuth(30)
            renderers[index].GetActiveCamera().Elevation(30)
            renderers[index].GetActiveCamera().Zoom(0.8)
            renderers[index].ResetCameraClippingRange()

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
