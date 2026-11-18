<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageDivergence/ -->

# ImageDivergence

Repository source: [ImageDivergence](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageDivergence.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageDivergence.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageDivergence.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageDivergence/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageDivergence.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingGeneral import vtkImageGradient
from vtkmodules.vtkImagingMath import vtkImageDivergence
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
    original_cast_filter.SetOutputScalarTypeToFloat()
    source >> original_cast_filter

    # Compute the gradient (to produce a vector field).
    gradient_filter = vtkImageGradient()
    source >> gradient_filter

    divergence_filter = vtkImageDivergence()
    source >> gradient_filter >> divergence_filter

    divergence_cast_filter = vtkImageCast()
    source >> gradient_filter >> divergence_filter >> divergence_cast_filter

    # Create actors
    original_actor = vtkImageActor()
    original_cast_filter >> original_actor.mapper

    divergence_actor = vtkImageActor()
    divergence_cast_filter >> divergence_actor.mapper

    # Define viewport ranges (x_min, y_min, x_max, y_max).
    left_viewport = (0.0, 0.0, 0.5, 1.0)
    right_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup the renderers.
    original_renderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('Sienna'))
    original_renderer.AddActor(original_actor)

    divergence_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('RoyalBlue'))
    divergence_renderer.AddActor(divergence_actor)

    # Set up the render window.
    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageDivergence')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(divergence_renderer)

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
