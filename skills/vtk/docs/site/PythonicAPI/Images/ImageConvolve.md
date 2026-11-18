<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageConvolve/ -->

# ImageConvolve

Repository source: [ImageConvolve](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageConvolve.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageConvolve.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageConvolve.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageConvolve/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageConvolve.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingGeneral import vtkImageConvolve
from vtkmodules.vtkImagingSources import vtkImageMandelbrotSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor, vtkImageActor
)

def main():
    colors = vtkNamedColors()

    # Create an image.
    source = vtkImageMandelbrotSource()

    original_cast_filter = vtkImageCast()
    original_cast_filter.SetOutputScalarTypeToUnsignedChar()

    kernel = [1] * 9
    convolve_filter = vtkImageConvolve(kernel3x3=kernel)
    convolve_filter.SetKernel3x3(kernel)

    convolved_cast_filter = vtkImageCast()
    convolved_cast_filter.SetOutputScalarTypeToUnsignedChar()

    # Create an actor
    original_actor = vtkImageActor()
    source >> original_cast_filter >> original_actor.mapper

    convolved_actor = vtkImageActor()
    source >> convolve_filter >> convolved_cast_filter >> convolved_actor.mapper

    # Define viewport ranges (x_min, y_min, x_max, y_max).
    left_viewport = (0.0, 0.0, 0.5, 1.0)
    right_viewport = (0.5, 0.0, 1.0, 1.0)

    # Set up the renderers.
    original_renderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('Sienna'))
    original_renderer.AddActor(original_actor)

    convolved_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('RoyalBlue'))
    convolved_renderer.AddActor(convolved_actor)

    # Set up the render window.
    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageConvolve')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(convolved_renderer)

    # Set up the render window interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style

    # Render and start the interaction.
    render_window_interactor.render_window = render_window
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
