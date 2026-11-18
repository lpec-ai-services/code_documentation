<!-- source: https://examples.vtk.org/site/Python/IO/ReadImageData/ -->

# ReadImageData

Repository source: [ReadImageData](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/ReadImageData.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadImageData.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadImageData.png?raw=true target=)

### Description

This example reads an image data (.vti) file.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadImageData/)), ([CSharp](https://examples.vtk.org/site/CSharp/IO/ReadImageData/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadImageData.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOXML import vtkXMLImageDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Read a VTK image data file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='vase.vti')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()

    # Read the source file.
    reader = vtkXMLImageDataReader()
    reader.SetFileName(file_name)

    # Create the mapper that creates graphics elements
    mapper = vtkDataSetMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Create the Actor
    actor = vtkActor()
    actor.SetMapper(mapper)
    # show the edges of the image grid
    actor.GetProperty().SetRepresentationToWireframe()

    # Create the Renderer
    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.ResetCamera()
    renderer.SetBackground(colors.GetColor3d('Silver'))

    # Create the RendererWindow
    renderer_window = vtkRenderWindow()
    renderer_window.AddRenderer(renderer)
    renderer_window.SetWindowName('ReadImageData')

    # Create the RendererWindowInteractor and display the vti file
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderer_window)
    interactor.Initialize()
    interactor.Start()

if __name__ == '__main__':
    main()
```
