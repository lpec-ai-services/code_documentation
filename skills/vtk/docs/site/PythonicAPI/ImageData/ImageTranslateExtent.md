<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageData/ImageTranslateExtent/ -->

# ImageTranslateExtent

Repository source: [ImageTranslateExtent](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageData/ImageTranslateExtent.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestImageTranslateExtent.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestImageTranslateExtent.png?raw=true target=)

### Description

If you are looking to change the extent to change the "origin" of the image from the corner to the center, see [vtkImageChangeInformation](https://www.vtk.org/doc/nightly/html/classvtkImageChangeInformation.html) in [CenterAnImage](../Images/CenterAnImage.md).

Currently, this method changes the extent (shown by the terminal output in the example), but does not change where the corner of the image is displayed relative to the sphere at (0,0,0).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageData/ImageTranslateExtent/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageTranslateExtent.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import VTK_UNSIGNED_CHAR
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkImagingCore import vtkImageTranslateExtent
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor, vtkRenderWindow, vtkRenderer, vtkImageSlice, \
    vtkImageSliceMapper, vtkActor, vtkPolyDataMapper

def main():
    colors = vtkNamedColors()

    # This image has (0,0) in the bottom left corner.
    colorImage = create_color_image()

    extent = colorImage.extent
    print(f'Old extent: ({fmt_ints(extent)})')

    # This moves the (0,0) position in the image to the center of the image.
    new_extent = list()
    # for i in range(0, 6, 2):
    #     new_extent.append(int(extent[i] - (extent[i + 1] - extent[i]) / 2))
    #     new_extent.append(int(extent[i] + (extent[i + 1] - extent[i]) / 2))
    #     print(new_extent[i], new_extent[i + 1])
    # colorImage.extent = new_extent

    dimensions = colorImage.dimensions

    td = [int(x) for x in [-dimensions[0] / 2, -dimensions[1] / 2, 0]]
    translate_extent = vtkImageTranslateExtent(translation=td, input_data=colorImage)
    # translate_extent = vtkImageTranslateExtent(translation=td)(colorImage)
    colorImage.DeepCopy(translate_extent.update().output)

    extent = colorImage.GetExtent()
    print(f'New extent: ({fmt_ints(extent)})')

    sphere_source = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=1.0)

    sphere_mapper = vtkPolyDataMapper()
    sphere_source >> sphere_mapper

    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.color = colors.GetColor3d('PeachPuff')

    image_slice_mapper = vtkImageSliceMapper(input_data=colorImage)

    image_slice = vtkImageSlice(position=(0, 0, 0), mapper=image_slice_mapper)

    # Setup the renderer.
    renderer = vtkRenderer(background=colors.GetColor3d('SteelBlue'))
    renderer.AddViewProp(image_slice)
    renderer.AddViewProp(sphere_actor)
    renderer.ResetCamera()

    # Set up the render window.
    render_window = vtkRenderWindow(size=(300, 300), window_name='ImageTranslateExtent')
    render_window.AddRenderer(renderer)

    # Set up the render window interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style
    render_window_interactor.render_window = render_window

    # Render and start the interaction.
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

def create_color_image():
    image = vtkImageData(dimensions=(10, 10, 1))
    image.AllocateScalars(VTK_UNSIGNED_CHAR, 3)

    colors = vtkNamedColors()
    pixelColor = colors.GetColor3ub('Thistle')

    for x in range(0, 10):
        for y in range(0, 10):
            for i in range(0, 3):
                image.SetScalarComponentFromFloat(x, y, 0, i, pixelColor[i])

    return image

def fmt_ints(v, w=0):
    """
    Pretty print a list or tuple of ints.

    :param v: The list or tuple of ints.
    :param w: Total width of the field.
    :return: A string.
    """
    return ', '.join([f'{element:{w}}' for element in v])

if __name__ == '__main__':
    main()
```
