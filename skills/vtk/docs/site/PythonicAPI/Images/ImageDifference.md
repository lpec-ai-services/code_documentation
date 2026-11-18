<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageDifference/ -->

# ImageDifference

Repository source: [ImageDifference](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageDifference.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageDifference.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageDifference.png?raw=true target=)

### Description

This example makes a large square and a smaller square and subtracts them, leaving the outline of a square.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageDifference/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageDifference.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageDifference
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    draw_color1 = colors.GetColor3ub('Black')
    draw_color2 = colors.GetColor3ub('Wheat')
    # Create an image
    source1 = vtkImageCanvasSource2D(extent=(0, 100, 0, 100, 0, 0), number_of_scalar_components=3)
    source1.SetScalarTypeToUnsignedChar()
    source1.draw_color = tuple(draw_color1)
    source1.FillBox(0, 100, 0, 100)
    source1.draw_color = tuple(draw_color2)
    source1.FillBox(10, 90, 10, 90)
    source1.update()

    # Create another image
    source2 = vtkImageCanvasSource2D(extent=(0, 100, 0, 100, 0, 0), number_of_scalar_components=3)
    source2.SetScalarTypeToUnsignedChar()
    source2.draw_color = tuple(draw_color1)
    source2.FillBox(0, 100, 0, 100)
    source2.draw_color = tuple(draw_color2)
    source2.FillBox(20, 80, 20, 80)
    source2.update()

    difference_filter = vtkImageDifference(input_connection=source1.output_port, image_connection=source2.output_port)

    # Define viewport ranges (x_min, y_min, x_max, y_max).
    left_viewport = (0.0, 0.0, 0.33, 1.0)
    center_viewport = (0.33, 0.0, 0.66, 1.0)
    right_viewport = (0.66, 0.0, 1.0, 1.0)

    # Set up the render window.
    render_window = vtkRenderWindow(size=(300, 100), window_name='ImageDifference')

    # Set up the renderers and actors.
    left_renderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('Mint'))
    render_window.AddRenderer(left_renderer)
    left_actor = vtkImageActor()
    source1 >> left_actor.mapper
    left_renderer.AddActor(left_actor)

    center_renderer = vtkRenderer(viewport=center_viewport, background=colors.GetColor3d('Mint'))
    render_window.AddRenderer(center_renderer)
    center_actor = vtkImageActor()
    source2 >> center_actor.mapper
    center_renderer.AddActor(center_actor)

    right_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('Peacock'))
    render_window.AddRenderer(right_renderer)
    right_actor = vtkImageActor()
    difference_filter >> right_actor.mapper
    right_renderer.AddActor(right_actor)

    # Set up the render window interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Render and start interaction.
    render_window.Render()
    render_window_interactor.Initialize()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
