<!-- source: https://examples.vtk.org/site/Python/Visualization/ComplexV/ -->

# ComplexV

Repository source: [ComplexV](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/ComplexV.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestComplexV.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestComplexV.png?raw=true target=)

### Description

ComplexV from the VTK Textbook. The original example was written in TCL.

The example shows 167,000 3D vectors (using oriented and scaled lines) in the region of the human carotid artery. The larger vectors lie inside the arteries, the smaller vectors lie outside the arteries and are randomly oriented (measurement error) but small in magnitude. Clearly the details of the vector field are not discernible from this image.

Info

See [Figure 6-13](../../VTKBook/06Chapter6.md#Figure%206-13) in [Chapter 6](../../VTKBook/06Chapter6.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/ComplexV/)), ([Java](https://examples.vtk.org/site/Java/Visualization/ComplexV/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ComplexV.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkFiltersCore import vtkHedgeHog
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    fileName = get_program_parameters()

    colors = vtkNamedColors()

    reader = vtkStructuredPointsReader()
    reader.SetFileName(fileName)

    hhog = vtkHedgeHog()
    hhog.SetInputConnection(reader.GetOutputPort())
    hhog.SetScaleFactor(0.3)

    lut = vtkLookupTable()
    # lut.SetHueRange(.667, 0.0)
    lut.Build()

    hhogMapper = vtkPolyDataMapper()
    hhogMapper.SetInputConnection(hhog.GetOutputPort())
    hhogMapper.SetScalarRange(50, 550)
    hhogMapper.SetLookupTable(lut)

    hhogActor = vtkActor()
    hhogActor.SetMapper(hhogMapper)

    outline = vtkOutlineFilter()
    outline.SetInputConnection(reader.GetOutputPort())

    outlineMapper = vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outline.GetOutputPort())

    outlineActor = vtkActor()
    outlineActor.SetMapper(outlineMapper)
    outlineActor.GetProperty().SetColor(colors.GetColor3d('Black'))

    aRenderer = vtkRenderer()
    aRenderWindow = vtkRenderWindow()
    aRenderWindow.AddRenderer(aRenderer)
    anInteractor = vtkRenderWindowInteractor()
    anInteractor.SetRenderWindow(aRenderWindow)
    aRenderWindow.SetSize(640, 480)
    aRenderWindow.SetWindowName('ComplexV')

    aRenderer.AddActor(outlineActor)
    aRenderer.AddActor(hhogActor)

    aRenderer.SetBackground(colors.GetColor3d('SlateGray'))

    # Generate an interesting view.

    aRenderer.GetActiveCamera().SetFocalPoint(0, 0, 0)
    aRenderer.GetActiveCamera().SetPosition(1, 0, 0)
    aRenderer.GetActiveCamera().SetViewUp(0, 0, 1)
    aRenderer.ResetCamera()

    aRenderer.GetActiveCamera().Azimuth(60)
    aRenderer.GetActiveCamera().Elevation(30)
    aRenderer.GetActiveCamera().Dolly(1.1)
    aRenderer.ResetCameraClippingRange()

    aRenderWindow.Render()

    # Interact with the data.
    anInteractor.Start()

def get_program_parameters():
    import argparse
    description = 'Vector visualization techniques.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='carotid.vtk')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
