<!-- source: https://examples.vtk.org/site/Python/IO/ReadPolyData/ -->

# ReadPolyData

Repository source: [ReadPolyData](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/ReadPolyData.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadPolyData.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadPolyData.png?raw=true target=)

### Description

This example reads a polygonal data (.vtp) file, for example `src/Testing/Data/Torso.vtp`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadPolyData/)), ([Java](https://examples.vtk.org/site/Java/IO/ReadPolyData/)), ([CSharp](https://examples.vtk.org/site/CSharp/IO/ReadPolyData/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadPolyData.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Read a polydata file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='Torso.vtp')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    filename = get_program_parameters()

    # Read all the data from the file
    reader = vtkXMLPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()

    # Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('NavajoWhite'))

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkOliveGreen'))
    renderer.GetActiveCamera().Pitch(90)
    renderer.GetActiveCamera().SetViewUp(0, 0, 1)
    renderer.ResetCamera()

    renderWindow.SetSize(600, 600)
    renderWindow.Render()
    renderWindow.SetWindowName('ReadPolyData')
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
