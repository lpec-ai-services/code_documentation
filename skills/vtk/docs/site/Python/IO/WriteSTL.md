<!-- source: https://examples.vtk.org/site/Python/IO/WriteSTL/ -->

# WriteSTL

Repository source: [WriteSTL](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/WriteSTL.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestWriteSTL.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestWriteSTL.png?raw=true target=)

### Description

An [STL file](https://en.wikipedia.org/wiki/STL_(file_format)) describes a triangulated three-dimensional surface by the unit normal and vertices (ordered by the right-hand rule) of the triangles. This example saves 3D geometric data stored in a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html) object to an STL file using [vtkSTLWriter](https://www.vtk.org/doc/nightly/html/classvtkSTLWriter.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/WriteSTL/)), ([PythonicAPI](../../PythonicAPI/IO/WriteSTL.md)), ([Java](https://examples.vtk.org/site/Java/IO/WriteSTL/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**WriteSTL.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import (
    vtkSTLReader,
    vtkSTLWriter
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
    description = 'Generate image data, then write a .stl file.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename', help='A required stl filename.', nargs='?',
                        const='TestWriteSTL.ply',
                        type=str, default='TestWriteSTL.ply')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    filename = get_program_parameters()

    sphereSource = vtkSphereSource()
    sphereSource.Update()

    # Write the stl file to disk
    stlWriter = vtkSTLWriter()
    stlWriter.SetFileName(filename)
    stlWriter.SetInputConnection(sphereSource.GetOutputPort())
    stlWriter.Write()

    # Read and display for verification
    reader = vtkSTLReader()
    reader.SetFileName(filename)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    # Create a rendering window and renderer
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('WriteSTL')

    # Create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('cobalt_green'))

    # Enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
