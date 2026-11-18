<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/DotProduct/ -->

# DotProduct

Repository source: [DotProduct](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/DotProduct.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestDotProduct.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestDotProduct.png?raw=true target=)

### Description

This example demonstrates how to take the pixel-wise dot product of two vector images. The output is a scalar image.

Two images, each 2x2x1, are created and filled with 3-vectors. The dot product of each pair of corresponding pixels is produced by the [vtkImageDotProduct](https://www.vtk.org/doc/nightly/html/classvtkImageDotProduct.html) filter and output to the screen.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/DotProduct/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DotProduct.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import VTK_FLOAT
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkFiltersSources import vtkArrowSource
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingMath import (
    vtkImageDotProduct,
    vtkImageMathematics
)
from vtkmodules.vtkRenderingCore import (
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor, vtkImageActor, vtkGlyph3DMapper, vtkActor
)

def main():
    colors = vtkNamedColors()

    # Create an image
    image1 = vtkImageData(extent=(0, 1, 0, 1, 0, 0))
    image1.AllocateScalars(VTK_FLOAT, 3)

    # Fill the image with vectors.
    coord = [0] * 3
    image1.SetScalarComponentFromFloat(*coord, 0, 1.0)
    image1.SetScalarComponentFromFloat(*coord, 1, 0.0)
    image1.SetScalarComponentFromFloat(*coord, 2, 0.0)

    coord[0] = 0
    coord[1] = 1
    coord[2] = 0
    image1.SetScalarComponentFromFloat(*coord, 0, 0.0)
    image1.SetScalarComponentFromFloat(*coord, 1, 1.0)
    image1.SetScalarComponentFromFloat(*coord, 2, 0.0)

    coord[0] = 1
    coord[1] = 0
    coord[2] = 0
    image1.SetScalarComponentFromFloat(*coord, 0, 1.0)
    image1.SetScalarComponentFromFloat(*coord, 1, 0.0)
    image1.SetScalarComponentFromFloat(*coord, 2, 0.0)

    coord[0] = 1
    coord[1] = 1
    coord[2] = 0
    image1.SetScalarComponentFromFloat(*coord, 0, 0.0)
    image1.SetScalarComponentFromFloat(*coord, 1, 1.0)
    image1.SetScalarComponentFromFloat(*coord, 2, 0.0)

    # Create another image.
    image2 = vtkImageData(extent=(0, 1, 0, 1, 0, 0))
    image2.AllocateScalars(VTK_FLOAT, 3)

    # Fill the image with vectors.
    coord = [0] * 3
    image2.SetScalarComponentFromFloat(*coord, 0, 1.0)
    image2.SetScalarComponentFromFloat(*coord, 1, 0.0)
    image2.SetScalarComponentFromFloat(*coord, 2, 0.0)

    coord[0] = 0
    coord[1] = 1
    coord[2] = 0
    image2.SetScalarComponentFromFloat(*coord, 0, 1.0)
    image2.SetScalarComponentFromFloat(*coord, 1, 0.0)
    image2.SetScalarComponentFromFloat(*coord, 2, 0.0)

    coord[0] = 1
    coord[1] = 0
    coord[2] = 0
    image2.SetScalarComponentFromFloat(*coord, 0, 0.5)
    image2.SetScalarComponentFromFloat(*coord, 1, 0.0)
    image2.SetScalarComponentFromFloat(*coord, 2, 0.0)

    coord[0] = 1
    coord[1] = 1
    coord[2] = 0
    image2.SetScalarComponentFromFloat(*coord, 0, 0.5)
    image2.SetScalarComponentFromFloat(*coord, 1, 0.0)
    image2.SetScalarComponentFromFloat(*coord, 2, 0.0)

    # Compute the dot product of the images pixel wise.
    dot_product_filter = vtkImageDotProduct(input1_data=image1, input2_data=image2)
    dot_product_filter.update()
    print(f'Output is of type: {dot_product_filter.output.GetScalarTypeAsString()}')

    image_math = vtkImageMathematics(constant_k=255.0)
    image_math.SetOperationToMultiplyByK()

    image_cast = vtkImageCast()
    image_cast.SetOutputScalarTypeToUnsignedChar()

    dot_product_actor = vtkImageActor()
    dot_product_filter >> image_math >> image_cast >> dot_product_actor.mapper

    # Display output to the terminal.
    for i in range(0, 2):
        for j in range(0, 2):
            pixel = dot_product_filter.output.GetScalarComponentAsFloat(i, j, 0, 0)
            print(f'Pixel ({i}, {j}): {pixel}')
    image1.GetPointData().SetActiveVectors('ImageScalars')
    image2.GetPointData().SetActiveVectors('ImageScalars')

    arrow_source = vtkArrowSource()

    glyph3d_mapper1 = vtkGlyph3DMapper(source_connection=arrow_source.output_port, input_data=image1)
    actor1 = vtkActor(mapper=glyph3d_mapper1)

    glyph3d_mapper2 = vtkGlyph3DMapper(source_connection=arrow_source.output_port, input_data=image2)
    actor2 = vtkActor(mapper=glyph3d_mapper2)

    # Define viewport ranges (x_min, y_min, x_max, y_max).
    left_viewport = (0.0, 0.0, 0.33, 1.0)
    center_viewport = (0.33, 0.0, 0.66, 1.0)
    right_viewport = (0.66, 0.0, 1.0, 1.0)

    # Set up the render window.
    render_window = vtkRenderWindow(size=(600, 200), window_name='DotProduct')

    # Set up the renderers and actors.
    left_renderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('DimGray'))
    render_window.AddRenderer(left_renderer)
    left_renderer.AddActor(actor1)

    center_renderer = vtkRenderer(viewport=center_viewport, background=colors.GetColor3d('DimGray'))
    render_window.AddRenderer(center_renderer)
    center_renderer.AddActor(actor2)

    right_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('DimGray'))
    render_window.AddRenderer(right_renderer)
    right_renderer.AddActor(dot_product_actor)

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
