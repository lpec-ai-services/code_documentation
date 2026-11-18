<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/CombiningRGBChannels/ -->

# CombiningRGBChannels

Repository source: [CombiningRGBChannels](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/CombiningRGBChannels.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestCombiningRGBChannels.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestCombiningRGBChannels.png?raw=true target=)

### Description

This example creates three images of a square. Each square slightly overlaps the previous square. These three layers are then interpreted as the R, G, and B channel of an RGB image, by the use of [vtkImageAppendComponents](https://www.vtk.org/doc/nightly/html/classvtkImageAppendComponents.html).

Note

You MUST add 3 inputs or no output will be produced.

Seealso

For the reverse operation, see [ExtractComponents](ExtractComponents.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/CombiningRGBChannels/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CombiningRGBChannels.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageAppendComponents
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

    draw_color1 = colors.GetColor4ub('Black')
    draw_color2 = colors.GetColor4ub('White')

    # Set the alpha to 0.
    draw_color1[3] = 0
    draw_color2[3] = 0

    # Create an image (will be used as the R channel).
    red = vtkImageCanvasSource2D(number_of_scalar_components=1,
                                 scalar_type=ImageCanvasSource2D.ScalarType.VTK_UNSIGNED_CHAR,
                                 extent=(0, 100, 0, 100, 0, 0))
    red.draw_color = tuple(draw_color1)
    red.FillBox(0, 100, 0, 100)
    red.draw_color = tuple(draw_color2)
    red.FillBox(20, 40, 20, 40)

    # Create an image (will be used as the G channel).
    green = vtkImageCanvasSource2D(number_of_scalar_components=1,
                                   scalar_type=ImageCanvasSource2D.ScalarType.VTK_UNSIGNED_CHAR,
                                   extent=(0, 100, 0, 100, 0, 0))
    green.draw_color = tuple(draw_color1)
    green.FillBox(0, 100, 0, 100)
    green.draw_color = tuple(draw_color2)
    green.FillBox(30, 50, 30, 50)

    # Create an image (will be used as the B channel).
    blue = vtkImageCanvasSource2D(number_of_scalar_components=1,
                                  scalar_type=ImageCanvasSource2D.ScalarType.VTK_UNSIGNED_CHAR,
                                  extent=(0, 100, 0, 100, 0, 0))
    blue.draw_color = tuple(draw_color1)
    blue.FillBox(0, 100, 0, 100)
    blue.draw_color = tuple(draw_color2)
    blue.FillBox(40, 60, 40, 60)

    append_filter = vtkImageAppendComponents()
    (red, green, blue) >> append_filter

    # Create the actors.
    red_actor = vtkImageActor()
    red >> red_actor.mapper

    green_actor = vtkImageActor()
    green >> green_actor.mapper

    blue_actor = vtkImageActor()
    blue >> blue_actor.mapper

    combined_actor = vtkImageActor()
    append_filter >> combined_actor.mapper

    # Define the viewport ranges (xmin, ymin, xmax, ymax).
    red_viewport = (0.0, 0.0, 0.25, 1.0)
    green_viewport = (0.25, 0.0, 0.5, 1.0)
    blue_viewport = (0.5, 0.0, 0.75, 1.0)
    combined_viewport = (0.75, 0.0, 1.0, 1.0)

    # Set up the renderers.
    red_renderer = vtkRenderer(background=colors.GetColor3d('Tomato'))
    red_renderer.viewport = red_viewport
    red_renderer.AddActor(red_actor)

    green_renderer = vtkRenderer(background=colors.GetColor3d('Mint'))
    green_renderer.viewport = green_viewport
    green_renderer.AddActor(green_actor)

    blue_renderer = vtkRenderer(background=colors.GetColor3d('Peacock'))
    blue_renderer.viewport = blue_viewport
    blue_renderer.AddActor(blue_actor)

    combined_renderer = vtkRenderer(background=colors.GetColor3d('DarkGray'))
    combined_renderer.viewport = combined_viewport
    combined_renderer.AddActor(combined_actor)

    # Set up the render window.
    render_window = vtkRenderWindow(window_name='CombiningRGBChannels')
    render_window.size = (1000, 250)
    render_window.AddRenderer(red_renderer)
    render_window.AddRenderer(green_renderer)
    render_window.AddRenderer(blue_renderer)
    render_window.AddRenderer(combined_renderer)

    # Set up the render window interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style
    render_window_interactor.render_window = render_window

    # Render and start interaction.
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

@dataclass(frozen=True)
class ImageCanvasSource2D:
    @dataclass(frozen=True)
    class ScalarType:
        VTK_CHAR: int = 2
        VTK_UNSIGNED_CHAR: int = 3
        VTK_SHORT: int = 4
        VTK_UNSIGNED_SHORT: int = 5
        VTK_INT: int = 6
        VTK_UNSIGNED_INT: int = 7
        VTK_LONG: int = 8
        VTK_UNSIGNED_LONG: int = 9
        VTK_FLOAT: int = 10
        VTK_DOUBLE: int = 11

if __name__ == '__main__':
    main()
```
