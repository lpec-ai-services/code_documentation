<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageSlice/ -->

# ImageSlice

Repository source: [ImageSlice](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageSlice.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageSlice.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageSlice.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageSlice/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageSlice.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import VTK_UNSIGNED_CHAR
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageSlice,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)
from vtkmodules.vtkRenderingImage import vtkImageResliceMapper

def main():
    colors = vtkNamedColors()

    color_image = create_color_image()

    image_reslice_mapper = vtkImageResliceMapper(input_data=color_image)

    image_slice = vtkImageSlice()
    image_slice.mapper = image_reslice_mapper

    # Setup renderers.
    renderer = vtkRenderer(background=colors.GetColor3d('NavajoWhite'))
    renderer.AddViewProp(image_slice)

    # Set up the render window.
    render_window = vtkRenderWindow(size=(300, 300), window_name='ImageSlice')
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

def create_color_image():
    image = vtkImageData(dimensions=(10, 10, 1))
    image.AllocateScalars(VTK_UNSIGNED_CHAR, 3)

    colors = vtkNamedColors()
    pixelColor = colors.GetColor3ub('Turquoise')

    for x in range(0, 10):
        for y in range(0, 10):
            for i in range(0, 3):
                image.SetScalarComponentFromFloat(x, y, 0, i, pixelColor[i])

    return image

if __name__ == '__main__':
    main()
```
