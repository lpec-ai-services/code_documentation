<!-- source: https://examples.vtk.org/site/Python/Arrays/GetValues/ -->

# GetValues

Repository source: [GetValues](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Arrays/GetValues.py)

### Description

Get values from a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html) source, normals in this case.

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GetValues.py**

```python
#!/usr/bin/env python

from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersSources import vtkSphereSource

def main():
    # setup sphere
    sphereSource = vtkSphereSource()
    sphereSource.Update()

    polydata = vtkPolyData()
    polydata.ShallowCopy(sphereSource.GetOutput())

    normals = polydata.GetPointData().GetNormals()
    normal0 = normals.GetTuple3(0)

    print('Normal0: {:3.1f} {:3.1f} {:3.1f}'.format(normal0[0], normal0[1], normal0[2]))

if __name__ == '__main__':
    main()
```
