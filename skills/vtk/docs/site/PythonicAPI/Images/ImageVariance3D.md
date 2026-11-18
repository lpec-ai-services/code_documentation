<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageVariance3D/ -->

# ImageVariance3D

Repository source: [ImageVariance3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageVariance3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageVariance3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageVariance3D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageVariance3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageVariance3D.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingGeneral import vtkImageVariance3D
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
    source = vtkImageEllipsoidSource(whole_extent=(0, 20, 0, 20, 0, 0), center=(10, 10, 0), radius=(3, 4, 0))

    variance_filter = vtkImageVariance3D(kernel_size=(5, 4, 3))

    variance_cast_filter = vtkImageCast(output_scalar_type=ImageCast.OutputScalarType.VTK_FLOAT)

    # Create the actors.
    original_actor = vtkImageActor()
    source >> original_actor.mapper

    variance_actor = vtkImageActor()
    source >> variance_filter >> variance_cast_filter >> variance_actor.mapper

    # Define the viewport ranges (min, y_min, x_max, y_max).
    original_viewport = (0.0, 0.0, 0.5, 1.0)
    variance_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup renderers.
    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('CornflowerBlue'))
    original_renderer.AddActor(original_actor)
    # original_renderer.background = (0.4, 0.5, 0.6)

    variance_renderer = vtkRenderer(viewport=variance_viewport, background=colors.GetColor3d('SteelBlue'))
    variance_renderer.AddActor(variance_actor)

    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageVariance3D')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(variance_renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style

    render_window_interactor.render_window = render_window
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

@dataclass(frozen=True)
class ImageCast:
    @dataclass(frozen=True)
    class OutputScalarType:
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
