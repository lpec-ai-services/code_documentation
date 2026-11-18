<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/3DSImporter/ -->

# 3DSImporter

Repository source: [3DSImporter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/3DSImporter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/Test3DSImporter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/Test3DSImporter.png?raw=true target=)

### Description

This example illustrates Importing files in VTK. An importer creates a [vtkRenderWindow](https://www.vtk.org/doc/nightly/html/classvtkRenderWindow.html) that describes the scene.

Info

See [Figure 4-13](../../VTKBook/04Chapter4.md#Figure%204-13) in [Chapter 4](../../VTKBook/04Chapter4.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/3DSImporter/)), ([Python](../../Python/IO/3DSImporter.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**3DSImporter.py**

```python
#!/usr/bin/env python3

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
    file_name = get_program_parameters()

    importer = vtk3DSImporter(file_name=file_name, compute_normals=True)

    colors = vtkNamedColors()

    renderer = vtkRenderer(gradient_background=True,
                           background=colors.GetColor3d('Wheat'),
                           background2=colors.GetColor3d('Gold'))
    ren_win = vtkRenderWindow(window_name='3DSImporter')
    iren = vtkRenderWindowInteractor()

    ren_win.AddRenderer(renderer)

    iren.render_window = ren_win
    importer.render_window = ren_win
    importer.Update()

    actors = renderer.actors  # This is a vtkActorCollection
    print('There are', actors.number_of_items, 'actors.')

    ren_win.Render()
    camera = vtkCamera()
    camera.position = (0, -1, 0)
    camera.focal_point = (0, 0, 0)
    camera.view_up = (0, 0, 1)
    camera.Azimuth(150)
    camera.Elevation(30)

    renderer.active_camera = camera
    renderer.ResetCamera()
    renderer.ResetCameraClippingRange()

    ren_win.Render()
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
