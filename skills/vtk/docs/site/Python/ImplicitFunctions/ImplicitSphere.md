<!-- source: https://examples.vtk.org/site/Python/ImplicitFunctions/ImplicitSphere/ -->

# ImplicitSphere

Repository source: [ImplicitSphere](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImplicitFunctions/ImplicitSphere.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImplicitFunctions/TestImplicitSphere.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImplicitFunctions/TestImplicitSphere.png?raw=true target=)

### Description

This example creates an isosurface of sampled sphere.

Info

See [Figure 6-23b](../../VTKBook/06Chapter6.md#Figure%206-23b) in [Chapter 6](../../VTKBook/06Chapter6.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImplicitFunctions/ImplicitSphere/)), ([PythonicAPI](../../PythonicAPI/ImplicitFunctions/ImplicitSphere.md)), ([Java](https://examples.vtk.org/site/Java/ImplicitFunctions/ImplicitSphere/)), ([CSharp](https://examples.vtk.org/site/CSharp/ImplicitFunctions/ImplicitSphere/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImplicitSphere.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkSphere
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkImagingHybrid import vtkSampleFunction
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor("BkgColor", [51, 77, 102, 255])

    sphere = vtkSphere()

    # Sample the function
    sample = vtkSampleFunction()
    sample.SetSampleDimensions(50, 50, 50)
    sample.SetImplicitFunction(sphere)
    value = 2.0
    xmin = -value
    xmax = value
    ymin = -value
    ymax = value
    zmin = -value
    zmax = value
    sample.SetModelBounds(xmin, xmax, ymin, ymax, zmin, zmax)

    # Create the 0 isosurface
    contours = vtkContourFilter()
    contours.SetInputConnection(sample.GetOutputPort())
    contours.GenerateValues(1, 1, 1)

    # Map the contours to graphical primitives
    contourMapper = vtkPolyDataMapper()
    contourMapper.SetInputConnection(contours.GetOutputPort())
    contourMapper.ScalarVisibilityOff()

    # Create an actor for the contours
    contourActor = vtkActor()
    contourActor.SetMapper(contourMapper)

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('ImplicitSphere')

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    renderer.AddActor(contourActor)
    renderer.SetBackground(colors.GetColor3d("BkgColor"))

    renderWindow.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
