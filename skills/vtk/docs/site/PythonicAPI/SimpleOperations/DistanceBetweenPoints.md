<!-- source: https://examples.vtk.org/site/PythonicAPI/SimpleOperations/DistanceBetweenPoints/ -->

# DistanceBetweenPoints

Repository source: [DistanceBetweenPoints](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/SimpleOperations/DistanceBetweenPoints.py)

### Description

This example finds the squared distance and the Euclidean distance between two 3D points.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/SimpleOperations/DistanceBetweenPoints/)), ([Python](../../Python/SimpleOperations/DistanceBetweenPoints.md)), ([Java](https://examples.vtk.org/site/Java/SimpleOperations/DistanceBetweenPoints/)), ([CSharp](https://examples.vtk.org/site/CSharp/SimpleOperations/DistanceBetweenPoints/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DistanceBetweenPoints.py**

```python
# !/usr/bin/env python3

import math

from vtkmodules.vtkCommonCore import vtkMath

def main():
    p0 = (0, 0, 0)
    p1 = (1, 1, 1)

    dist_squared = vtkMath.Distance2BetweenPoints(p0, p1)

    dist = math.sqrt(dist_squared)

    print('p0 = ', p0)
    print('p1 = ', p1)
    print('distance squared = ', dist_squared)
    print(f'distance = {dist:9.6}')

if __name__ == '__main__':
    main()
```
