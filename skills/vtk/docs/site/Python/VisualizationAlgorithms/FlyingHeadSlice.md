<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/FlyingHeadSlice/ -->

# FlyingHeadSlice

Repository source: [FlyingHeadSlice](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/FlyingHeadSlice.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestFlyingHeadSlice.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestFlyingHeadSlice.png?raw=true target=)

### Description

This example generates 2D contour lines on one CT slice through the head. The contours correspond to density values of the tissues and are colored according to density value.

This example is a modification of [HeadSlice](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/HeadSlice/) using [vtkFlyingEdges2D](https://www.vtk.org/doc/nightly/html/classvtkFlyingEdges2D.html) for contouring. However there is an option to use [vtkContourFilter](https://www.vtk.org/doc/nightly/html/classvtkContourFilter.html) instead.

Info

See [Figure 6-11a](../../VTKBook/06Chapter6.md#Figure%206-11a) in [Chapter 6](../../VTKBook/06Chapter6.md) of the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/FlyingHeadSlice/)), ([PythonicAPI](../../PythonicAPI/VisualizationAlgorithms/FlyingHeadSlice.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FlyingHeadSlice.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import (
    vtkContourFilter,
    vtkFlyingEdges2D
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkImagingCore import vtkExtractVOI
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    fileName, useContouring = get_program_parameters()
    if useContouring:
        print('Using vtkContourFilter.')
    else:
        print('Using vtkFlyingEdges2D.')

    colors = vtkNamedColors()

    # Create the RenderWindow, Renderer and Interactor.
    ren1 = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Create the pipeline.
    reader = vtkMetaImageReader()
    reader.SetFileName(fileName)
    reader.Update()

    extractVOI = vtkExtractVOI()
    extractVOI.SetInputConnection(reader.GetOutputPort())
    extractVOI.SetVOI(0, 255, 0, 255, 45, 45)
    # scalarRange = extractVOI.GetOutput().GetScalarRange()
    scalarRange = [500, 1150]
    # print(scalarRange)

    contour = vtkContourFilter()
    flyingEdges = vtkFlyingEdges2D()
    isoMapper = vtkPolyDataMapper()
    if useContouring:
        contour.SetInputConnection(extractVOI.GetOutputPort())
        contour.GenerateValues(12, scalarRange)
        isoMapper.SetInputConnection(contour.GetOutputPort())
    else:
        flyingEdges.SetInputConnection(extractVOI.GetOutputPort())
        flyingEdges.GenerateValues(12, scalarRange)
        isoMapper.SetInputConnection(flyingEdges.GetOutputPort())

    isoMapper.ScalarVisibilityOn()
    isoMapper.SetScalarRange(scalarRange)

    isoActor = vtkActor()
    isoActor.SetMapper(isoMapper)
    isoActor.GetProperty().SetColor(colors.GetColor3d('Wheat'))

    outline = vtkOutlineFilter()
    outline.SetInputConnection(extractVOI.GetOutputPort())

    outlineMapper = vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outline.GetOutputPort())

    outlineActor = vtkActor()
    outlineActor.SetMapper(outlineMapper)

    # Add the actors to the renderer, set the background and size.
    ren1.AddActor(outlineActor)
    ren1.AddActor(isoActor)
    ren1.SetBackground(colors.GetColor3d('SlateGray'))
    ren1.ResetCamera()
    ren1.GetActiveCamera().Dolly(1.5)
    ren1.ResetCameraClippingRange()

    renWin.SetSize(640, 640)
    renWin.SetWindowName('FlyingHeadSlice')
    renWin.Render()

    iren.Start()

def get_program_parameters():
    import argparse
    description = 'Either vtkFlyingEdges2D or vtkContourFilter is used to generate contour lines.'
    epilogue = '''
    Generate 2D contour lines, corresponding to tissue density, on one CT slice through the head.
    The contour lines are colored by the tissue density.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    parser.add_argument('-useContouring', '--useContouring', action='store_true',
                        help='Use vtkContourFilter instead of vtkFlyingEdges2D.')
    args = parser.parse_args()
    return args.filename, args.useContouring

if __name__ == '__main__':
    main()
```
