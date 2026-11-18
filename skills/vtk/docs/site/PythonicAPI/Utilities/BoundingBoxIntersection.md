<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/BoundingBoxIntersection/ -->

# BoundingBoxIntersection

Repository source: [BoundingBoxIntersection](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/BoundingBoxIntersection.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/BoundingBoxIntersection/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BoundingBoxIntersection.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonDataModel import vtkBoundingBox

def main():
    # Note the various ways of initializing the bounding box bounds.
    bounding_box0 = vtkBoundingBox()
    bounding_box0.bounds = (0, 1, 0, 1, 0, 1)
    bounding_box1 = vtkBoundingBox((5, 6, 5, 6, 5, 6))
    bounds = (0.5, 1.5, 0.5, 1.5, 0.5, 1.5)
    bounding_box2 = vtkBoundingBox(bounds)

    intersection_0_1 = bounding_box0.IntersectBox(bounding_box1)
    intersection_0_2 = bounding_box0.IntersectBox(bounding_box2)
    if intersection_0_1 == 0:
        print('No intersection between bounding_box0 and bounding_box1 as expected.')
    if intersection_0_2 == 1:
        print('There is an intersection between bounding_box0 and bounding_box2 as expected.')

if __name__ == '__main__':
    main()
```
