<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/PlanesIntersection/ -->

# PlanesIntersection

Repository source: [PlanesIntersection](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/PlanesIntersection.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/PlanesIntersection/)), ([PythonicAPI](../../PythonicAPI/GeometricObjects/PlanesIntersection.md)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/PlanesIntersection/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/PlanesIntersection/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PlanesIntersection.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkPlanesIntersection
from vtkmodules.vtkFiltersSources import vtkSphereSource

def main():
    sphereSource = vtkSphereSource()
    sphereSource.Update()

    bounds = [0 for i in range(6)]
    sphereSource.GetOutput().GetBounds(bounds)

    box = vtkPoints()

    box.SetNumberOfPoints(8)

    xMin = bounds[0]
    xMax = bounds[1]
    yMin = bounds[2]
    yMax = bounds[3]
    zMin = bounds[4]
    zMax = bounds[5]

    box.SetPoint(0, xMax, yMin, zMax)
    box.SetPoint(1, xMax, yMin, zMin)
    box.SetPoint(2, xMax, yMax, zMin)
    box.SetPoint(3, xMax, yMax, zMax)
    box.SetPoint(4, xMin, yMin, zMax)
    box.SetPoint(5, xMin, yMin, zMin)
    box.SetPoint(6, xMin, yMax, zMin)
    box.SetPoint(7, xMin, yMax, zMax)

    planesIntersection = vtkPlanesIntersection()
    planesIntersection.SetBounds(bounds)

    intersects = planesIntersection.IntersectsRegion(box)
    if intersects == 1:
        res = 'Yes'
    else:
        res = 'No'
    print('Intersects? ', res)

if __name__ == '__main__':
    main()
```
