<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Disk/ -->

# Disk

Repository source: [Disk](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Disk.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestDisk.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestDisk.png?raw=true target=)

### Description

[vtkDiskSource](https://www.vtk.org/doc/nightly/html/classvtkDiskSource.html) objects creates a polygonal disk with a hole in the center.

The disk has zero height. The user can specify the inner and outer radius of the disk, and the radial and circumferential resolution of the polygonal representation.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Disk/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/Disk/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Disk/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Disk.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkDiskSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    diskSource = vtkDiskSource()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(diskSource.GetOutputPort())

    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d("Cornsilk"))
    actor.SetMapper(mapper)

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName("Disk")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("DarkGreen"))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
