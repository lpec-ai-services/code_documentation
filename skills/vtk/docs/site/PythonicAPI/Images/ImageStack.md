<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageStack/ -->

# ImageStack

Repository source: [ImageStack](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageStack.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageStack.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageStack.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageStack/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageStack.py**

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
    vtkImageSliceMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)
from vtkmodules.vtkRenderingImage import vtkImageStack

def main():
    colors = vtkNamedColors()

    # Image 1
    image1 = create_color_image(1, 0)

    image_slice_mapper1 = vtkImageSliceMapper(input_data=image1)

    image_slice1 = vtkImageSlice(mapper=image_slice_mapper1)
    image_slice1.property.opacity = 0.5

    # Image 2
    image2 = create_color_image(4, 1)

    image_slice_mapper2 = vtkImageSliceMapper(input_data=image2)

    image_slice2 = vtkImageSlice(mapper=image_slice_mapper2)
    image_slice2.property.opacity = 0.5

    # Stack.
    image_stack = vtkImageStack()
    image_stack.AddImage(image_slice1)
    image_stack.AddImage(image_slice2)
    # image_stack.active_layer = 1

    # Setup renderers.
    renderer = vtkRenderer(background=colors.GetColor3d('SteelBlue'))
    renderer.AddViewProp(image_stack)

    # Setup render window.
    render_window = vtkRenderWindow(window_name='ImageStack')
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

def create_color_image(corner, channel):
    image = vtkImageData(dimensions=(10, 10, 1))
    image.AllocateScalars(VTK_UNSIGNED_CHAR, 3)

    for x in range(0, 10):
        for y in range(0, 10):
            for i in range(0, 3):
                image.SetScalarComponentFromFloat(x, y, 0, i, 0)
    for x in range(corner, corner + 3):
        for y in range(corner, corner + 3):
            for i in range(0, 3):
                if i == channel:
                    image.SetScalarComponentFromFloat(x, y, 0, i, 255)
                else:
                    image.SetScalarComponentFromFloat(x, y, 0, i, 0)

    return image

if __name__ == '__main__':
    main()
```
