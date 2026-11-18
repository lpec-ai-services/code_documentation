<!-- source: https://examples.vtk.org/site/Python/IO/ReadSLC/ -->

# ReadSLC

Repository source: [ReadSLC](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/ReadSLC.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadSLC.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadSLC.png?raw=true target=)

### Description

In this example you will familiarize yourself with the stages required to read a .slc file and create a visualization pipeline in VTK. Following is the three-step procedure:

1. Read the data from .slc file using [vtkSLCReader](https://www.vtk.org/doc/nightly/html/classvtkSLCReader.html)
2. Implement Marching cubes Algorithm using [vtkContourFilter](https://www.vtk.org/doc/nightly/html/classvtkContourFilter.html)
3. Create Visualization pipeline to visualize data using an actor, mapper and rendering window

Cite

This example was provided by Bharatesh Chakravarthi from Virtual Environment Lab, Chung-Ang University, Seoul, South Korea

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadSLC/)), ([PythonicAPI](../../PythonicAPI/IO/ReadSLC.md)), ([Java](https://examples.vtk.org/site/Java/IO/ReadSLC/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadSLC.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkSLCReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    InputFilename, iso_value = get_program_parameters()

    colors = vtkNamedColors()

    # vtkSLCReader to read.
    reader = vtkSLCReader()
    reader.SetFileName(InputFilename)
    reader.Update()

    # Create a mapper.
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Implementing Marching Cubes Algorithm to create the surface using vtkContourFilter object.
    contourFilter = vtkContourFilter()
    contourFilter.SetInputConnection(reader.GetOutputPort())
    # Change the range(2nd and 3rd Parameter) based on your
    # requirement. recommended value for 1st parameter is above 1
    # contourFilter.GenerateValues(5, 80.0, 100.0)
    contourFilter.SetValue(0, iso_value)

    outliner = vtkOutlineFilter()
    outliner.SetInputConnection(reader.GetOutputPort())
    outliner.Update()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(contourFilter.GetOutputPort())
    mapper.SetScalarVisibility(0)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuse(0.8)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d('Ivory'))
    actor.GetProperty().SetSpecular(0.8)
    actor.GetProperty().SetSpecularPower(120.0)

    # Create a rendering window and renderer.
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(500, 500)

    # Create a renderwindowinteractor.
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Assign actor to the renderer.
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))

    # Pick a good view
    cam1 = renderer.GetActiveCamera()
    cam1.SetFocalPoint(0.0, 0.0, 0.0)
    cam1.SetPosition(0.0, -1.0, 0.0)
    cam1.SetViewUp(0.0, 0.0, -1.0)
    cam1.Azimuth(-90.0)
    renderer.ResetCamera()
    renderer.ResetCameraClippingRange()

    renderWindow.SetWindowName('ReadSLC')
    renderWindow.SetSize(640, 512)
    renderWindow.Render()

    # Enable user interface interactor.
    renderWindowInteractor.Initialize()
    renderWindow.Render()
    renderWindowInteractor.Start()

def get_program_parameters():
    import argparse
    description = 'Read a .slc file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='vw_knee.slc.')
    parser.add_argument('iso_value', nargs='?', type=float, default=72.0, help='Defaullt 72.')
    args = parser.parse_args()
    return args.filename, args.iso_value

if __name__ == '__main__':
    main()
```
