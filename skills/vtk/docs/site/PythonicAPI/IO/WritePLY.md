<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/WritePLY/ -->

# WritePLY

Repository source: [WritePLY](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/WritePLY.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestWritePLY.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestWritePLY.png?raw=true target=)

### Description

Note

Unlike vtkPolyDataXMLWriter and most other VTK writers, to write colors to the .ply file you must specify to the [vtkPLYWriter](https://www.vtk.org/doc/nightly/html/classvtkPLYWriter.html):

plyWriter->SetArrayName("Colors");

where your color array was created/named like this:

[vtkNew](https://www.vtk.org/doc/nightly/html/classvtkNew.html)<[vtkUnsignedCharArray](https://www.vtk.org/doc/nightly/html/classvtkUnsignedCharArray.html)> colors; colors->SetNumberOfComponents(3); colors->SetName("Colors");

(This was found in response to a user question on StackOverflow: <http://stackoverflow.com/questions/17783612/save-mesh-with-rgb-in-vtk/19525938>)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/WritePLY/)), ([Python](../../Python/IO/WritePLY.md)), ([Java](https://examples.vtk.org/site/Java/IO/WritePLY/))

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

    file_name = get_program_parameters()

    sphere_source = vtkSphereSource()

    ply_writer = vtkPLYWriter(file_name=file_name)
    sphere_source >> ply_writer
    ply_writer.Write()

    # Read and display for verification.
    reader = vtkPLYReader(file_name=file_name)

    mapper = vtkPolyDataMapper()
    reader >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    renderer = vtkRenderer(background=colors.GetColor3d('cobalt_green'))
    render_window = vtkRenderWindow(window_name='WritePLY')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
