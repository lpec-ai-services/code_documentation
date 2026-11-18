<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageGradientMagnitude/ -->

# ImageGradientMagnitude

Repository source: [ImageGradientMagnitude](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageGradientMagnitude.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageGradientMagnitude.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageGradientMagnitude.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageGradientMagnitude/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageGradientMagnitude.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingGeneral import vtkImageGradientMagnitude
from vtkmodules.vtkImagingSources import vtkImageEllipsoidSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Create an image.
    source = vtkImageEllipsoidSource(whole_extent=(0, 20, 0, 20, 0, 0), center=(10, 10, 0), radius=(3, 4, 0))

    gradient_magnitude_filter = vtkImageGradientMagnitude()
    source >> gradient_magnitude_filter

    gradient_magnitude_cast_filter = vtkImageCast()
    gradient_magnitude_cast_filter.SetOutputScalarTypeToUnsignedChar()

    # Create the actors.
    original_actor = vtkImageActor()
    source >> original_actor.mapper

    gradient_magnitude_actor = vtkImageActor()
    source >> gradient_magnitude_filter >> gradient_magnitude_cast_filter >> gradient_magnitude_actor.mapper

    # Define the viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = [0.0, 0.0, 0.5, 1.0]
    gradient_magnitude_viewport = [0.5, 0.0, 1.0, 1.0]

    # Setup the renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('CornflowerBlue'))
    original_renderer.AddActor(original_actor)

    gradient_magnitude_renderer = vtkRenderer(viewport=gradient_magnitude_viewport,
                                              background=colors.GetColor3d('SteelBlue'))
    gradient_magnitude_renderer.AddActor(gradient_magnitude_actor)

    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageGradientMagnitude')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(gradient_magnitude_renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style

    render_window_interactor.render_window = render_window
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
