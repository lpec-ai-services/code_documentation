<!-- source: https://examples.vtk.org/site/Python/Images/Cast/ -->

# Cast

Repository source: [Cast](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Images/Cast.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Images/TestCast.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Images/TestCast.png?raw=true target=)

### Description

Cast an image to a different type.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/Cast/)), ([Java](https://examples.vtk.org/site/Java/Images/Cast/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Cast.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingSources import vtkImageMandelbrotSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create a float image
    source = vtkImageMandelbrotSource()
    source.Update()

    print(source.GetOutput().GetScalarTypeAsString())

    castFilter = vtkImageCast()
    castFilter.SetInputConnection(source.GetOutputPort())
    castFilter.SetOutputScalarTypeToUnsignedChar()
    castFilter.Update()

    # Create an actor
    actor = vtkImageActor()
    actor.GetMapper().SetInputConnection(castFilter.GetOutputPort())

    # Setup renderer
    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkSlateGray'))
    renderer.ResetCamera()

    # Setup render window
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('Cast')

    # Setup render window interactor
    renderWindowInteractor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    renderWindowInteractor.SetInteractorStyle(style)

    # Render and start interaction
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindow.Render()
    renderWindowInteractor.Initialize()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
