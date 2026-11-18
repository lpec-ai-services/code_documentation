<!-- source: https://examples.vtk.org/site/Python/IO/WritePLY/ -->

# WritePLY

Repository source: [WritePLY](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/WritePLY.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestWritePLY.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestWritePLY.png?raw=true target=)

### Description

Note

Unlike vtkPolyDataXMLWriter and most other VTK writers, to write colors to the .ply file you must specify to the [vtkPLYWriter](https://www.vtk.org/doc/nightly/html/classvtkPLYWriter.html):

plyWriter->SetArrayName("Colors");

where your color array was created/named like this:

[vtkNew](https://www.vtk.org/doc/nightly/html/classvtkNew.html)<[vtkUnsignedCharArray](https://www.vtk.org/doc/nightly/html/classvtkUnsignedCharArray.html)> colors; colors->SetNumberOfComponents(3); colors->SetName("Colors");

(This was found in response to a user question on StackOverflow: <http://stackoverflow.com/questions/17783612/save-mesh-with-rgb-in-vtk/19525938>)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/WritePLY/)), ([PythonicAPI](../../PythonicAPI/IO/WritePLY.md)), ([Java](https://examples.vtk.org/site/Java/IO/WritePLY/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**WritePLY.py**

```python
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOPLY import (
    vtkPLYReader,
    vtkPLYWriter
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Generate image data, then write a .ply file.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename', help='A required ply filename.', nargs='?',
                        const='TestWritePLY.ply',
                        type=str, default='TestWritePLY.ply')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    filename = get_program_parameters()

    sphereSource = vtkSphereSource()
    sphereSource.Update()

    plyWriter = vtkPLYWriter()
    plyWriter.SetFileName(filename)
    plyWriter.SetInputConnection(sphereSource.GetOutputPort())
    plyWriter.Write()

    # Read and display for verification
    reader = vtkPLYReader()
    reader.SetFileName(filename)
    reader.Update()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('WritePLY')

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('cobalt_green'))

    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
