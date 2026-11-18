<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageMask/ -->

# ImageMask

Repository source: [ImageMask](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageMask.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageMask.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageMask.png?raw=true target=)

### Description

This example creates an all red image. Then it creates a mask of a small rectangle. The red pixels in this rectangle are copied to the output image, while the rest of the output image is black. The black region could be set to a different color using SetMaskedOutputValue.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageMask/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageMask.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageMask
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Create an image of a rectangle.
    source = vtkImageCanvasSource2D(extent=(0, 200, 0, 200, 0, 0), number_of_scalar_components=3)
    source.SetScalarTypeToUnsignedChar()

    # Create a red image.
    source.draw_color = (255, 0, 0)
    source.FillBox(0, 200, 0, 200)

    # Create a rectangular mask.
    mask_source = vtkImageCanvasSource2D(extent=(0, 200, 0, 200, 0, 0), number_of_scalar_components=1)
    mask_source.SetScalarTypeToUnsignedChar()

    # Initialize the mask to black.
    mask_source.draw_color = (0, 0, 0)
    mask_source.FillBox(0, 200, 0, 200)

    # Create a square.
    mask_source.draw_color = (255, 255, 255)
    # Anything non-zero means 'make the output
    # pixel equal the input pixel'. If the mask is
    # zero, the output pixel is set to MaskedValue.
    mask_source.FillBox(100, 120, 100, 120)

    mask_filter = vtkImageMask(masked_output_value=(0, 1, 0))
    source >> select_ports(0, mask_filter)
    mask_source >> select_ports(1, mask_filter)

    inverse_mask_filter = vtkImageMask(masked_output_value=(0, 1, 0), not_mask=True)
    source >> select_ports(0, inverse_mask_filter)
    mask_source >> select_ports(1, inverse_mask_filter)

    # Create the actors.
    original_actor = vtkImageActor()
    source >> original_actor.mapper

    mask_actor = vtkImageActor()
    mask_source >> mask_actor.mapper

    masked_actor = vtkImageActor()
    mask_filter >> masked_actor.mapper

    inverse_masked_actor = vtkImageActor()
    inverse_mask_filter >> inverse_masked_actor.mapper

    # Define the viewport ranges.(x_min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.25, 1.0)
    mask_viewport = (0.25, 0.0, 0.5, 1.0)
    masked_viewport = (0.5, 0.0, 0.75, 1.0)
    inverse_masked_viewport = (0.75, 0.0, 1.0, 1.0)

    # Setup the renderers.
    original_renderer = vtkRenderer(background=colors.GetColor3d('SandyBrown'))
    original_renderer.viewport = original_viewport
    original_renderer.AddActor(original_actor)
    original_renderer.ResetCamera()

    mask_renderer = vtkRenderer(viewport=mask_viewport, background=colors.GetColor3d('Peru'))
    mask_renderer.AddActor(mask_actor)

    masked_renderer = vtkRenderer(viewport=masked_viewport, background=colors.GetColor3d('SandyBrown'))
    masked_renderer.AddActor(masked_actor)

    inverse_masked_renderer = vtkRenderer(viewport=inverse_masked_viewport, background=colors.GetColor3d('Peru'))
    inverse_masked_renderer.AddActor(inverse_masked_actor)

    render_window = vtkRenderWindow(size=(1000, 250), window_name='ImageMask')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(mask_renderer)
    render_window.AddRenderer(masked_renderer)
    render_window.AddRenderer(inverse_masked_renderer)

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
