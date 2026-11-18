<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageSobel2D/ -->

# ImageSobel2D

Repository source: [ImageSobel2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageSobel2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageSobel2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageSobel2D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageSobel2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageSobel2D.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkArrowSource
from vtkmodules.vtkImagingCore import (
    vtkImageExtractComponents,
    vtkImageShiftScale
)
from vtkmodules.vtkImagingGeneral import vtkImageSobel2D
from vtkmodules.vtkImagingMath import vtkImageMathematics
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkGlyph3DMapper,
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    draw_color1 = colors.GetColor3ub('Black')
    draw_color2 = colors.GetColor3ub('Red')

    # Create an image of a rectangle
    source = vtkImageCanvasSource2D(extent=(0, 200, 0, 200, 0, 0))
    source.SetScalarTypeToUnsignedChar()
    source.draw_color = tuple(draw_color1)
    source.FillBox(0, 200, 0, 200)
    source.draw_color = tuple(draw_color2)
    source.FillBox(100, 120, 100, 120)
    source.update()

    # Find the x and y gradients using a sobel filter.
    sobel_filter = vtkImageSobel2D()
    source >> sobel_filter
    sobel_filter.update()

    # Extract the x component of the gradient.
    extract_x_filter = vtkImageExtractComponents(components=0)
    source >> sobel_filter >> extract_x_filter
    extract_x_filter.update()

    x_range = extract_x_filter.output.point_data.scalars.range

    x_image_abs = vtkImageMathematics()
    x_image_abs.SetOperationToAbsoluteValue()
    extract_x_filter >> x_image_abs

    x_scale = 255 / x_range[1]
    x_shift_scale = vtkImageShiftScale(scale=x_scale)
    x_shift_scale.SetOutputScalarTypeToUnsignedChar()
    x_image_abs >> x_shift_scale

    # Extract the y component of the gradient.
    extract_y_filter = vtkImageExtractComponents(components=1)
    source >> sobel_filter >> extract_y_filter
    extract_y_filter.update()

    y_range = extract_y_filter.output.point_data.scalars.range

    y_image_abs = vtkImageMathematics()
    y_image_abs.SetOperationToAbsoluteValue()
    extract_y_filter >> y_image_abs

    y_scale = 255 / y_range[1]
    y_shift_scale = vtkImageShiftScale(scale=y_scale)
    y_shift_scale.SetOutputScalarTypeToUnsignedChar()
    y_image_abs >> y_shift_scale

    # Create the actors.
    original_actor = vtkImageActor()
    source >> original_actor.mapper

    x_actor = vtkImageActor()
    x_shift_scale >> x_actor.mapper

    y_actor = vtkImageActor()
    y_shift_scale >> y_actor.mapper

    arrow_source = vtkArrowSource()

    sobel_filter.output.point_data.active_vectors = 'ImageScalarsGradient'

    sobel_mapper = vtkGlyph3DMapper(scaling=True, scale_factor=0.05, source_connection=arrow_source.output_port,
                                    input_data=sobel_filter.output)

    sobel_actor = vtkActor(mapper=sobel_mapper)

    # Define the viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.25, 1.0)
    x_viewport = (0.25, 0.0, 0.5, 1.0)
    y_viewport = (0.5, 0.0, 0.75, 1.0)
    sobel_viewport = (0.75, 0.0, 1.0, 1.0)

    # Setup the renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('DodgerBlue'))
    original_renderer.AddActor(original_actor)

    x_renderer = vtkRenderer(viewport=x_viewport, background=colors.GetColor3d('CornflowerBlue'))
    x_renderer.AddActor(x_actor)

    y_renderer = vtkRenderer(viewport=y_viewport, background=colors.GetColor3d('CornflowerBlue'))
    y_renderer.AddActor(y_actor)

    sobel_renderer = vtkRenderer(viewport=sobel_viewport, background=colors.GetColor3d('SteelBlue'))
    sobel_renderer.AddActor(sobel_actor)

    render_window = vtkRenderWindow(size=(1000, 250), window_name='ImageSobel2D')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(x_renderer)
    render_window.AddRenderer(y_renderer)
    render_window.AddRenderer(sobel_renderer)

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
