<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageNonMaximumSuppression/ -->

# ImageNonMaximumSuppression

Repository source: [ImageNonMaximumSuppression](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageNonMaximumSuppression.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageNonMaximumSuppression.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageNonMaximumSuppression.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageNonMaximumSuppression/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageNonMaximumSuppression.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingGeneral import (
    vtkImageGradient,
    vtkImageGradientMagnitude
)
from vtkmodules.vtkImagingMorphological import vtkImageNonMaximumSuppression
from vtkmodules.vtkImagingSources import vtkImageSinusoidSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    source = vtkImageSinusoidSource()

    source_cast_filter = vtkImageCast()
    source_cast_filter.SetOutputScalarTypeToUnsignedChar()

    gradient_filter = vtkImageGradient()

    gradient_magnitude_filter = vtkImageGradientMagnitude()

    gradient_magnitude_cast_filter = vtkImageCast()
    gradient_magnitude_cast_filter.SetOutputScalarTypeToUnsignedChar()

    suppression_filter = vtkImageNonMaximumSuppression(dimensionality=2)
    gradient_magnitude_filter >> select_ports(0, suppression_filter)
    source >> gradient_filter >> select_ports(1, suppression_filter)

    suppression_cast_filter = vtkImageCast()
    suppression_cast_filter.SetOutputScalarTypeToUnsignedChar()

    # Create the actors.
    original_actor = vtkImageActor()
    source >> source_cast_filter >> original_actor.mapper

    gradient_magnitude_actor = vtkImageActor()
    source >> gradient_magnitude_filter >> gradient_magnitude_cast_filter >> gradient_magnitude_actor.mapper

    suppression_actor = vtkImageActor()
    suppression_filter >> suppression_cast_filter >> suppression_actor.mapper

    # Define the viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = [0.0, 0.0, 0.33, 1.0]
    gradient_magnitude_viewport = [0.33, 0.0, 0.66, 1.0]
    suppression_viewport = [0.66, 0.0, 1.0, 1.0]

    # Setup the renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('Mint'))
    original_renderer.AddActor(original_actor)

    gradient_magnitude_renderer = vtkRenderer(viewport=gradient_magnitude_viewport,
                                              background=colors.GetColor3d('Peacock'))
    gradient_magnitude_renderer.AddActor(gradient_magnitude_actor)

    suppression_renderer = vtkRenderer(viewport=suppression_viewport, background=colors.GetColor3d('BlanchedAlmond'))
    suppression_renderer.AddActor(suppression_actor)

    render_window = vtkRenderWindow(size=(900, 300), window_name='ImageNonMaximumSuppression')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(gradient_magnitude_renderer)
    render_window.AddRenderer(suppression_renderer)

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
