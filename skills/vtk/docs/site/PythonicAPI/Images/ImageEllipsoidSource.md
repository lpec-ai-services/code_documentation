<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageEllipsoidSource/ -->

# ImageEllipsoidSource

Repository source: [ImageEllipsoidSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageEllipsoidSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageEllipsoidSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageEllipsoidSource.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageEllipsoidSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageEllipsoidSource.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
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
    source = vtkImageEllipsoidSource(whole_extent=(0, 20, 0, 20, 0, 0), center=(10, 10, 0), radius=(3, 4, 5))

    cast_filter = vtkImageCast()
    cast_filter.SetOutputScalarTypeToUnsignedChar()

    # Create an actor.
    actor = vtkImageActor()
    source >> cast_filter >> actor.mapper

    # Set up the renderers.
    renderer = vtkRenderer(background=colors.GetColor3d('Sienna'))
    renderer.AddActor(actor)

    # Set up the render window.
    render_window = vtkRenderWindow(window_name='ImageEllipsoidSource')
    render_window.AddRenderer(renderer)

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
