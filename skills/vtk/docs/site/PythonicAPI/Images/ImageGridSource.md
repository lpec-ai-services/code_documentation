<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageGridSource/ -->

# ImageGridSource

Repository source: [ImageGridSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageGridSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageGridSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageGridSource.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageGridSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageGridSource.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingSources import vtkImageGridSource
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
    source = vtkImageGridSource(fill_value=122)

    cast_filter = vtkImageCast()

    cast_filter.SetOutputScalarTypeToUnsignedChar()

    # Create an actor.
    actor = vtkImageActor()
    source >> cast_filter >> actor.mapper

    # Setup renderer.
    renderer = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'))
    renderer.AddActor(actor)

    # Setup render window.
    render_window = vtkRenderWindow(window_name='ImageGridSource')
    render_window.AddRenderer(renderer)

    # Setup render window interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style

    # Render and start interaction.
    render_window_interactor.render_window = render_window
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
