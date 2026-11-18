<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageData/ImageIterator/ -->

# ImageIterator

Repository source: [ImageIterator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageData/ImageIterator.py)

### Description

Extracts an extent from an image.

The differences from the C++ example are: - We cannot use pointers in Python so we use `SetScalarComponentFromDoubl(...)` and `GetScalarComponentFromDouble(...)` instead of `GetScalarPointer(...)`. - We cannot use [vtkImageIterator](https://www.vtk.org/doc/nightly/html/classvtkImageIterator.html) as it is not wrapped in Python. So we use indexing instead.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageData/ImageIterator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageIterator.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import VTK_DOUBLE
from vtkmodules.vtkCommonDataModel import vtkImageData

def main():
    # We cannot use vtkImageIterator as it is not wrapped in the Python API
    #  so we use indexing to produce the same result as in the C++ example.

    # Create an image data and specify the size and type of the image data.
    image_data = vtkImageData(dimensions=(10, 20, 30))
    image_data.AllocateScalars(VTK_DOUBLE, 3)

    # Fill every entry of the image data with x,y,z.
    dims = image_data.GetDimensions()
    for z in range(dims[2]):
        for y in range(dims[1]):
            for x in range(dims[0]):
                image_data.SetScalarComponentFromDouble(x, y, z, 0, x)
                image_data.SetScalarComponentFromDouble(x, y, z, 1, y)
                image_data.SetScalarComponentFromDouble(x, y, z, 2, z)

    # Define the extent to be extracted.
    extent = [2, 5, 2, 5, 15, 15]

    # Retrieve the entries from the image data and print them to the screen.
    # We cannot use vtkImageIterator as it is not wrapped in the Python API so we use indexing.
    # Note that we add 1 to the upper index in extent so that range() works correctly.
    for z in range(extent[4], extent[5] + 1):
        for y in range(extent[2], extent[3] + 1):
            res = list()
            for x in range(extent[0], extent[1] + 1):
                zyx = list()
                for i in reversed(range(0, 3)):
                    zyx.append(image_data.GetScalarComponentAsDouble(x, y, z, i))
                res.append(f'({fmt_floats(zyx)})')
            print(' '.join(res))

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
