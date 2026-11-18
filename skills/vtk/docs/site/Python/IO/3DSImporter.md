<!-- source: https://examples.vtk.org/site/Python/IO/3DSImporter/ -->

# 3DSImporter

Repository source: [3DSImporter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/3DSImporter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/Test3DSImporter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/Test3DSImporter.png?raw=true target=)

### Description

This example illustrates Importing files in VTK. An importer creates a [vtkRenderWindow](https://www.vtk.org/doc/nightly/html/classvtkRenderWindow.html) that describes the scene.

Info

See [Figure 4-13](../../VTKBook/04Chapter4.md#Figure%204-13) in [Chapter 4](../../VTKBook/04Chapter4.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/3DSImporter/)), ([PythonicAPI](../../PythonicAPI/IO/3DSImporter.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**3DSImporter.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImport import vtk3DSImporter
from vtkmodules.vtkRenderingCore import (
    vtkCamera,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    fileName = get_program_parameters()

    importer = vtk3DSImporter()
    importer.SetFileName(fileName)
    importer.ComputeNormalsOn()

    colors = vtkNamedColors()

    renderer = vtkRenderer()
    renWin = vtkRenderWindow()
    iren = vtkRenderWindowInteractor()

    renWin.AddRenderer(renderer)
    renderer.SetBackground2(colors.GetColor3d('Gold'))
    renderer.SetBackground(colors.GetColor3d('Wheat'))
    renderer.GradientBackgroundOn()

    iren.SetRenderWindow(renWin)
    importer.SetRenderWindow(renWin)
    importer.Update()

    # actors = vtkActorCollection()
    actors = renderer.GetActors()
    print('There are', actors.GetNumberOfItems(), 'actors.')

    renWin.SetWindowName('3DSImporter')
    renWin.Render()
    camera = vtkCamera()
    camera.SetPosition(0, -1, 0)
    camera.SetFocalPoint(0, 0, 0)
    camera.SetViewUp(0, 0, 1)
    camera.Azimuth(150)
    camera.Elevation(30)

    renderer.SetActiveCamera(camera)
    renderer.ResetCamera()
    renderer.ResetCameraClippingRange()

    renWin.Render()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'Importing a 3ds file.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='iflamingo.3ds.')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
