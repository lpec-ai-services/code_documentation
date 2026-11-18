<!-- source: https://examples.vtk.org/site/Python/Widgets/CameraOrientationWidget/ -->

# CameraOrientationWidget

Repository source: [CameraOrientationWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Widgets/CameraOrientationWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Widgets/TestCameraOrientationWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Widgets/TestCameraOrientationWidget.png?raw=true target=)

### Description

This example demonstrates a 3D camera orientation gizmo.

The widget representation has shafts and little spheres with text on them. The spheres always follow the camera.

The widget representation's orientation is synchronized with the camera of the parent renderer.

To look down on any particular axis, simply click on a handle.

To rotate the camera and get a feel of the camera orientation, either move mouse in the renderer or click on a handle and move it around.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/CameraOrientationWidget/)), ([PythonicAPI](../../PythonicAPI/Widgets/CameraOrientationWidget.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CameraOrientationWidget.py**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This example demonstrates how to use the vtkCameraOrientationWidget to control
# a renderer's camera orientation.

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Demonstrates a 3D camera orientation widget.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path', help='The path to the file to render e.g. cow.vtp.')
    args = parser.parse_args()
    return args.path

def main():
    colors = vtkNamedColors()

    path = get_program_parameters()
    if not Path(path).is_file():
        print('Unable to find the file:', path)
        return

    renderer = vtkRenderer()
    ren_win = vtkRenderWindow()
    interactor = vtkRenderWindowInteractor()

    reader = vtkXMLPolyDataReader()
    reader.SetFileName(path)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d('Beige'))
    actor.SetMapper(mapper)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DimGray'))

    ren_win.AddRenderer(renderer)
    ren_win.SetSize(600, 600)
    ren_win.SetWindowName('CameraOrientationWidget')

    # Important: The interactor must be set prior to enabling the widget.
    interactor.SetRenderWindow(ren_win)

    cam_orient_manipulator = vtkCameraOrientationWidget()
    cam_orient_manipulator.SetParentRenderer(renderer)
    # Enable the widget.
    cam_orient_manipulator.On()

    ren_win.Render()
    interactor.Initialize()
    interactor.Start()

if __name__ == "__main__":
    main()
```
