<!-- source: https://examples.vtk.org/site/Python/IO/ReadUnstructuredGrid/ -->

# ReadUnstructuredGrid

Repository source: [ReadUnstructuredGrid](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/ReadUnstructuredGrid.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadUnstructuredGrid.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadUnstructuredGrid.png?raw=true target=)

### Description

This example demonstrates how to read an unstructured grid (VTU) file. The front facing faces are colored Misty Rose, while the back facing faces are colored Tomato.

An example file to use is `src/Testing/Data/tetra.vtu`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadUnstructuredGrid/)), ([CSharp](https://examples.vtk.org/site/CSharp/IO/ReadUnstructuredGrid/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadUnstructuredGrid.py**

```python
#!/usr/bin/env python3

import vtkmodules.all as vtk

def get_program_parameters():
    import argparse
    description = 'Read an unstructured grid file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='tetra.vtu.')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtk.vtkNamedColors()

    file_name = get_program_parameters()

    # Read the source file.
    reader = vtk.vtkXMLUnstructuredGridReader()
    reader.SetFileName(file_name)
    reader.Update()  # Needed because of GetScalarRange
    output = reader.GetOutput()
    # scalar_range = output.GetScalarRange()

    # Create the mapper that corresponds the objects of the vtk.vtk file
    # into graphics elements
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputData(output)
    # mapper.SetScalarRange(scalar_range)
    mapper.ScalarVisibilityOff()

    # Create the Actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().EdgeVisibilityOn()
    actor.GetProperty().SetLineWidth(2.0)
    actor.GetProperty().SetColor(colors.GetColor3d("MistyRose"))

    backface = vtk.vtkProperty()
    backface.SetColor(colors.GetColor3d('Tomato'))
    actor.SetBackfaceProperty(backface)

    # Create the Renderer
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Wheat'))

    # Create the RendererWindow
    renderer_window = vtk.vtkRenderWindow()
    renderer_window.SetSize(640, 480)
    renderer_window.AddRenderer(renderer)
    renderer_window.SetWindowName('ReadUnstructuredGrid')

    # Create the RendererWindowInteractor and display the vtk_file
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderer_window)
    interactor.Initialize()
    interactor.Start()

if __name__ == '__main__':
    main()
```
