<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageOrientation/ -->

# ImageOrientation

Repository source: [ImageOrientation](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageOrientation.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageOrientation.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageOrientation.png?raw=true target=)

### Description

Reorder the axes of the image.

This is a duplicate of [ImagePermute](ImagePermute.md)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageOrientation/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageOrientation.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImagePermute
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
    source = vtkImageEllipsoidSource(whole_extent=(0, 20, 0, 20, 0, 0), center=(10, 10, 0), radius=(2, 5, 0))
    source.SetOutputScalarTypeToUnsignedChar()

    # The filtered axes are the input axes that get relabeled to X,Y,Z.
    #  Here we swap X and Y.
    permute_filter = vtkImagePermute(filtered_axes=(1, 0, 2))
    source >> permute_filter

    # Create the actors.
    original_actor = vtkImageActor()
    source >> original_actor.mapper

    permuted_actor = vtkImageActor()
    permute_filter >> permuted_actor.mapper

    # Define viewport ranges (x_min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.5, 1.0)
    permuted_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('CornflowerBlue'))
    original_renderer.AddActor(original_actor)

    permuted_renderer = vtkRenderer(viewport=permuted_viewport, background=colors.GetColor3d('SteelBlue'))
    permuted_renderer.AddActor(permuted_actor)

    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageOrientation')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(permuted_renderer)

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
