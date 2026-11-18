<!-- source: https://examples.vtk.org/site/Python/ImplicitFunctions/SampleFunction/ -->

# SampleFunction

Repository source: [SampleFunction](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImplicitFunctions/SampleFunction.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImplicitFunctions/TestSampleFunction.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImplicitFunctions/TestSampleFunction.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImplicitFunctions/SampleFunction/)), ([PythonicAPI](../../PythonicAPI/ImplicitFunctions/SampleFunction.md)), ([Java](https://examples.vtk.org/site/Java/ImplicitFunctions/SampleFunction/)), ([CSharp](https://examples.vtk.org/site/CSharp/ImplicitFunctions/SampleFunction/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SampleFunction.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkSuperquadric
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkImagingHybrid import vtkSampleFunction
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    value = 2.0
    colors = vtkNamedColors()

    implicitFunction = vtkSuperquadric()
    implicitFunction.SetPhiRoundness(2.5)
    implicitFunction.SetThetaRoundness(.5)

    # Sample the function.
    sample = vtkSampleFunction()
    sample.SetSampleDimensions(50, 50, 50)
    sample.SetImplicitFunction(implicitFunction)

    xmin, xmax, ymin, ymax, zmin, zmax = -value, value, -value, value, -value, value
    sample.SetModelBounds(xmin, xmax, ymin, ymax, zmin, zmax)

    # Create the 0 isosurface.
    contours = vtkContourFilter()
    contours.SetInputConnection(sample.GetOutputPort())
    contours.GenerateValues(1, 2.0, 2.0)

    # Map the contours to graphical primitives.
    contourMapper = vtkPolyDataMapper()
    contourMapper.SetInputConnection(contours.GetOutputPort())
    contourMapper.SetScalarRange(0.0, 1.2)

    # Create an actor for the contours.
    contourActor = vtkActor()
    contourActor.SetMapper(contourMapper)

    # Create a box around the function to indicate the sampling volume. 

    # Create outline.
    outline = vtkOutlineFilter()
    outline.SetInputConnection(sample.GetOutputPort())

    # Map it to graphics primitives.
    outlineMapper = vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outline.GetOutputPort())

    # Create an actor.
    outlineActor = vtkActor()
    outlineActor.SetMapper(outlineMapper)
    outlineActor.GetProperty().SetColor(colors.GetColor3d("Black"))

    # Visualize.
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('ImplicitSphere1')

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    renderer.AddActor(contourActor)
    renderer.AddActor(outlineActor)
    renderer.SetBackground(colors.GetColor3d("Tan"))

    # Enable user interface interactor
    renderWindow.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
