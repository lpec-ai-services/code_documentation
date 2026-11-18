<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/AttachAttributes/ -->

# AttachAttributes

Repository source: [AttachAttributes](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/AttachAttributes.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/AttachAttributes/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AttachAttributes.py**

```python
#!/usr/bin/env python3

from vtkmodules.util.keys import DoubleVectorKey
from vtkmodules.vtkCommonCore import vtkDoubleArray

# This happens in VTK 9.4.0:
# Process finished with exit code 139 (interrupted by signal 11:SIGSEGV)

def main():
    # create a 2-element array
    array = vtkDoubleArray()
    array.SetName('array')
    array.SetNumberOfComponents(1)
    array.SetNumberOfTuples(2)
    array.SetValue(0, 1.0)
    array.SetValue(1, 2.0)

    # Access the info (presently none stored).
    info = array.GetInformation()

    # Add one attribute, a double vector.
    name = 'myKey'
    location = 'MyClass'
    length = 3
    key = DoubleVectorKey.MakeKey(name, location, length)
    values = (0.1, 0.2, 0.3)
    info.Set(key, values[0], values[1], values[2])

    # Extract the key.
    vals = info.Get(key)
    print(f'Extracted values are: ({fmt_floats(vals)})')

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
