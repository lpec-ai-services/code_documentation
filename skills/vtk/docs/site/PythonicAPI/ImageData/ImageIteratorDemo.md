<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageData/ImageIteratorDemo/ -->

# ImageIteratorDemo

Repository source: [ImageIteratorDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageData/ImageIteratorDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestImageIteratorDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestImageIteratorDemo.png?raw=true target=)

### Description

Unlike in C++ where [vtkImageIterator](https://www.vtk.org/doc/nightly/html/classvtkImageIterator.html) is an efficient way to access the regions of a [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html). We have to use indexing instead.

The differences from the C++ example are: - We cannot use pointers in Python so we use `SetScalarComponentFromDoubl(...)` and `GetScalarComponentFromDouble(...)` instead of `GetScalarPointer(...)`. - We cannot use [vtkImageIterator](https://www.vtk.org/doc/nightly/html/classvtkImageIterator.html) as it is not wrapped in Python. So we use indexing instead.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageData/ImageIteratorDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageIteratorDemo.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import VTK_UNSIGNED_CHAR
from vtkmodules.vtkCommonCore import reference
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor

def main():
    # We cannot use vtkImageIterator as it is not wrapped in the Python API
    #  so we use indexing to produce the same result as in the C++ example.

    # Create an image data and specify the size and type of the image data.
    image_data = vtkImageData(dimensions=(100, 200, 30))
    image_data.AllocateScalars(VTK_UNSIGNED_CHAR, 3)

    colors = vtkNamedColors()

    rgba = tuple(colors.GetColor4ub('Banana'))

    # Fill every entry of the image data with r, g, b.
    dims = image_data.GetDimensions()
    for z in range(dims[2]):
        for y in range(dims[1]):
            for x in range(dims[0]):
                for i in range(0, 3):
                    image_data.SetScalarComponentFromDouble(x, y, z, i, rgba[i])

    # whole_extent = image_data.GetExtent()
    # Define the extent to be extracted.
    extent = [20, 50, 30, 60, 10, 20]

    # We cannot use vtkImageIterator as it is not wrapped in the Python API so we use indexing.
    # Note that we add 1 to the upper index in extent so that range() works correctly.
    rgba = tuple(colors.GetColor4ub('Tomato'))
    counter = 0
    for z in range(extent[4], extent[5] + 1):
        for y in range(extent[2], extent[3] + 1):
            counter += 1
            for x in range(extent[0], extent[1] + 1):
                for i in range(0, 3):
                    image_data.SetScalarComponentFromDouble(x, y, z, i, rgba[i])

    print(f'Number of spans:      {counter}')
    print(f'Increments:           {fmt_ints(image_data.increments)}')
    inc_x = reference(0)
    inc_y = reference(0)
    inc_z = reference(0)
    image_data.GetContinuousIncrements(extent, inc_x, inc_y, inc_z)
    print(f'ContinuousIncrements: {inc_x}, {inc_y}, {inc_z}')

    # Visualize
    image_viewer = vtkImageViewer2(input_data=image_data)

    style = vtkInteractorStyleImage()
    style.SetInteractionModeToImageSlicing()

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.interactor_style = style
    image_viewer.SetupInteractor(render_window_interactor)
    slice = (extent[5] - extent[4]) // 2 + extent[4]
    image_viewer.slice = slice

    image_viewer.renderer.background = colors.GetColor3d('Slate_grey')
    image_viewer.image_actor.interpolate = False

    image_viewer.Render()
    image_viewer.renderer.ResetCamera()
    image_viewer.render_window.window_name = 'ImageIteratorDemo'

    image_viewer.Render()

    render_window_interactor.Start()

def fmt_ints(v, w=0):
    """
    Pretty print a list or tuple of ints.

    :param v: The list or tuple of ints.
    :param w: Total width of the field.
    :return: A string.
    """
    return ', '.join([f'{element:{w}}' for element in v])

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
