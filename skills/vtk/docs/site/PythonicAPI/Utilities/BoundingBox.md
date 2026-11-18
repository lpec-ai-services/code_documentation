<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/BoundingBox/ -->

# BoundingBox

Repository source: [BoundingBox](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/BoundingBox.py)

### Description

Seealso

[Outline](../PolyData/Outline.md) and [CubeAxesActor2D](../Visualization/CubeAxesActor2D.md)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/BoundingBox/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BoundingBox.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonDataModel import vtkBoundingBox

def fmt_floats(v, w=0, d=6, pt='f'):
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

def main():
    p0 = (0, 0, 0)
    p1 = (0.5, 0.5, 0.5)
    p2 = (1.0, 1.0, 1.0)

    bounding_box = vtkBoundingBox()

    bounds = [0] * 6

    bounding_box.AddPoint(p0)
    bounding_box.GetBounds(bounds)
    print(f'Initial box dimensions: {fmt_floats(bounds, 0, 2)}')

    # After adding this point, the box gets bigger.
    bounding_box.AddPoint(p2)
    bounding_box.GetBounds(bounds)
    print(f'The box gets bigger:    {fmt_floats(bounds, 0, 2)}')

    # After adding this point, the box size does not change as the point is
    #  already inside the box
    bounding_box.AddPoint(p1)
    bounding_box.GetBounds(bounds)
    print(f'No change in box size:  {fmt_floats(bounds), 0, 2}')

if __name__ == '__main__':
    main()
```
