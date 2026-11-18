<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/CarotidFlow/ -->

# CarotidFlow

Repository source: [CarotidFlow](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/CarotidFlow.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestCarotidFlow.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestCarotidFlow.png?raw=true target=)

### Description

This example generates streamtubes of blood velocity. an isosurface of speed provides context. The starting positions for the streamtubes were determined by experimenting with the data. Because of the way the data was measured and the resolution of the velocity field, many streamers travel outside the artery. This is because the boundary layer of the blood flow is not captured due to limitations in data resolution. Consequently, as the blood flows around curves, there is a component of the velocity field that directs the streamtube outside the artery. As a result it is hard to find starting positions for the streamtubes that yield interesting results. The examples uses the source object [vtkPointSource](https://www.vtk.org/doc/nightly/html/classvtkPointSource.html) in combination with [vtkThresholdPoints](https://www.vtk.org/doc/nightly/html/classvtkThresholdPoints.html) to work around this problem. [vtkPointSource](https://www.vtk.org/doc/nightly/html/classvtkPointSource.html) generates random points centered around a sphere of a specified radius. We need only find an approximate position for the starting points of the streamtubes and then generate a cloud of random seed points. [vtkThresholdPoints](https://www.vtk.org/doc/nightly/html/classvtkThresholdPoints.html) is used to cull points that may be generated outside the regions of high flow velocity.

Cite

See [*3D Phase Contrast MRI of Cerebral Blood Flow and Surface Anatomy*](http://marchingcubes.org/images/c/c6/3DPhaseContrastMRIofCerebralBloodFlowandSurfaceAnatomy.pdf) for background.

Info

See [Figure 6-44](../../VTKBook/06Chapter6.md#Figure%206-44) in [Chapter 6](../../VTKBook/06Chapter6.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/CarotidFlow/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CarotidFlow.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkFiltersCore import (
    vtkContourFilter,
    vtkThresholdPoints,
    vtkTubeFilter
)
from vtkmodules.vtkFiltersFlowPaths import vtkStreamTracer
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkFiltersSources import vtkPointSource
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    fileName = get_program_parameters()

    colors = vtkNamedColors()

    ren1 = vtkRenderer()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Create the pipeline.
    #
    reader = vtkStructuredPointsReader()
    reader.SetFileName(fileName)

    psource = vtkPointSource()
    psource.SetNumberOfPoints(25)
    psource.SetCenter(133.1, 116.3, 5.0)
    psource.SetRadius(2.0)

    threshold = vtkThresholdPoints()
    threshold.SetInputConnection(reader.GetOutputPort())
    threshold.ThresholdByUpper(275)

    streamers = vtkStreamTracer()
    streamers.SetInputConnection(reader.GetOutputPort())
    streamers.SetSourceConnection(psource.GetOutputPort())
    # streamers.SetMaximumPropagationUnitToTimeUnit()
    streamers.SetMaximumPropagation(100.0)
    # streamers.SetInitialIntegrationStepUnitToCellLengthUnit()
    streamers.SetInitialIntegrationStep(0.2)
    streamers.SetTerminalSpeed(.01)
    streamers.Update()
    scalarRange = [0] * 2
    scalarRange[0] = streamers.GetOutput().GetPointData().GetScalars().GetRange()[0]
    scalarRange[1] = streamers.GetOutput().GetPointData().GetScalars().GetRange()[1]
    print("range: ", scalarRange[0], ", ", scalarRange[1])

    tubes = vtkTubeFilter()
    tubes.SetInputConnection(streamers.GetOutputPort())
    tubes.SetRadius(0.3)
    tubes.SetNumberOfSides(6)
    tubes.SetVaryRadius(0)

    lut = vtkLookupTable()
    lut.SetHueRange(.667, 0.0)
    lut.Build()

    streamerMapper = vtkPolyDataMapper()
    streamerMapper.SetInputConnection(tubes.GetOutputPort())
    streamerMapper.SetScalarRange(scalarRange[0], scalarRange[1])
    streamerMapper.SetLookupTable(lut)

    streamerActor = vtkActor()
    streamerActor.SetMapper(streamerMapper)

    # Speed contours.
    iso = vtkContourFilter()
    iso.SetInputConnection(reader.GetOutputPort())
    iso.SetValue(0, 175)

    isoMapper = vtkPolyDataMapper()
    isoMapper.SetInputConnection(iso.GetOutputPort())
    isoMapper.ScalarVisibilityOff()

    isoActor = vtkActor()
    isoActor.SetMapper(isoMapper)
    isoActor.GetProperty().SetRepresentationToWireframe()
    isoActor.GetProperty().SetOpacity(0.25)

    # Outline
    outline = vtkOutlineFilter()
    outline.SetInputConnection(reader.GetOutputPort())

    outlineMapper = vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outline.GetOutputPort())

    outlineActor = vtkActor()
    outlineActor.SetMapper(outlineMapper)
    outlineActor.GetProperty().SetColor(colors.GetColor3d("Black"))

    # Add the actors to the renderer, set the background and size.
    #
    ren1.AddActor(outlineActor)
    ren1.AddActor(streamerActor)
    ren1.AddActor(isoActor)
    ren1.SetBackground(colors.GetColor3d("Wheat"))
    renWin.SetSize(640, 480)
    renWin.SetWindowName('CarotidFlow')

    cam1 = vtkCamera()
    cam1.SetClippingRange(17.4043, 870.216)
    cam1.SetFocalPoint(136.71, 104.025, 23)
    cam1.SetPosition(204.747, 258.939, 63.7925)
    cam1.SetViewUp(-0.102647, -0.210897, 0.972104)
    cam1.Zoom(1.2)
    ren1.SetActiveCamera(cam1)

    # Render the image.
    #
    renWin.Render()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'Visualizing blood flow in human carotid arteries.'
    epilogue = '''
    Streamtubes of blood velocity are generated. 
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='carotid.vtk')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
