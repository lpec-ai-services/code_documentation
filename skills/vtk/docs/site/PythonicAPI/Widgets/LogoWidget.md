<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/LogoWidget/ -->

# LogoWidget

Repository source: [LogoWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/LogoWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestLogoWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestLogoWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/LogoWidget/)), ([Java](https://examples.vtk.org/site/Java/Widgets/LogoWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LogoWidget.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingUI
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkInteractionWidgets import (
    vtkLogoRepresentation,
    vtkLogoWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # A sphere.
    sphere_source = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=4.0, phi_resolution=4, theta_resolution=8)
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # A renderer, render window and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('MidnightBLue'))
    render_window = vtkRenderWindow(window_name='LogoWidget')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    # Create an image.
    drawing = vtkImageCanvasSource2D()
    drawing.SetScalarTypeToUnsignedChar()
    drawing.SetNumberOfScalarComponents(3)
    drawing.SetExtent(0, 200, 0, 200, 0, 0)
    draw_color1 = colors.GetColor3ub('Coral')
    draw_color2 = colors.GetColor3ub('Black')

    # Clear the image.
    # Note: SetDrawColour() uses double values of the rgb colors in the
    #       range [0 ... 255]
    #       So SetDrawColour(255, 255, 255) is white.
    drawing.SetDrawColor(*draw_color1)
    drawing.FillBox(0, 200, 0, 200)
    drawing.SetDrawColor(*draw_color2)
    drawing.DrawCircle(100, 100, 50)

    logo_representation = vtkLogoRepresentation(image=drawing.update().output, position=(0, 0), position2=(0.4, 0.4))
    logo_representation.image_property.opacity = 0.7
    logo_widget = vtkLogoWidget(interactor=render_window_interactor, representation=logo_representation)

    render_window.Render()
    logo_widget.On()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
