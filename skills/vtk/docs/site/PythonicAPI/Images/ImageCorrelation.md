<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageCorrelation/ -->

# ImageCorrelation

Repository source: [ImageCorrelation](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageCorrelation.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageCorrelation.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageCorrelation.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageCorrelation/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageCorrelation.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast, vtkImageShiftScale
from vtkmodules.vtkImagingGeneral import vtkImageCorrelation
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

    # Create an image.
    draw_color1 = colors.GetColor3ub('Black')
    draw_color2 = colors.GetColor3ub('Wheat')

    image_source = vtkImageCanvasSource2D(extent=(0, 300, 0, 300, 0, 0), number_of_scalar_components=3)
    image_source.SetScalarTypeToUnsignedChar()
    image_source.draw_color = tuple(draw_color1)
    image_source.FillBox(0, 300, 0, 300)
    image_source.draw_color = tuple(draw_color2)
    image_source.FillTriangle(10, 100, 190, 150, 40, 250)
    image_source.update()

    # Create an actor.
    original_actor = vtkImageActor()
    image_source >> original_actor.mapper

    # Create a kernel.
    kernel_source = vtkImageCanvasSource2D(extent=(0, 30, 0, 30, 0, 0), number_of_scalar_components=3)
    kernel_source.SetScalarTypeToUnsignedChar()
    kernel_source.draw_color = tuple(draw_color1)
    kernel_source.FillBox(0, 30, 0, 30)
    kernel_source.draw_color = tuple(draw_color2)
    kernel_source.FillTriangle(10, 1, 25, 10, 1, 5)
    kernel_source.Update()

    # Create an actor.
    kernel_actor = vtkImageActor()
    kernel_source >> kernel_actor.mapper

    # Compute the correlation.
    correlation_filter = vtkImageCorrelation()
    image_source >> select_ports(0, correlation_filter)
    kernel_source >> select_ports(1, correlation_filter)
    correlation_filter.update()

    # At this point, corr pixels are doubles so, get the scalar range.
    corr = correlation_filter.output
    corr_range = corr.point_data.scalars.range
    scale = 255 / corr_range[1]

    # Rescale the correlation filter output. Note that it implies that
    # minimum correlation is always zero.
    image_scale = vtkImageShiftScale(scale=scale, input_connection=correlation_filter.output_port)
    image_scale.SetOutputScalarTypeToUnsignedChar()

    correlation_cast_filter = vtkImageCast()
    correlation_cast_filter.SetOutputScalarTypeToUnsignedChar()

    # Create an actor.
    correlation_actor = vtkImageActor()
    correlation_filter >> image_scale >> correlation_cast_filter >> correlation_actor.mapper

    # Define viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.33, 1.0)
    kernel_viewport = (0.33, 0.0, 0.66, 1.0)
    correlation_viewport = (0.66, 0.0, 1.0, 1.0)

    # Setup the renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('Mint'))
    original_renderer.AddActor(original_actor)

    kernel_renderer = vtkRenderer(viewport=kernel_viewport, background=colors.GetColor3d('Mint'))
    kernel_renderer.AddActor(kernel_actor)

    correlation_renderer = vtkRenderer(viewport=correlation_viewport, background=colors.GetColor3d('Peacock'))
    correlation_renderer.AddActor(correlation_actor)

    # Set up the render window.
    render_window = vtkRenderWindow(size=(900, 300), window_name='ImageCorrelation')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(kernel_renderer)
    render_window.AddRenderer(correlation_renderer)

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
