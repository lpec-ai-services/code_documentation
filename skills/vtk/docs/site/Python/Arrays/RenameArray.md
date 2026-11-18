<!-- source: https://examples.vtk.org/site/Python/Arrays/RenameArray/ -->

# RenameArray

Repository source: [RenameArray](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Arrays/RenameArray.py)

### Description

Renaming the normals array.

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RenameArray.py**

```python
#!/usr/bin/env python

from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOXML import vtkXMLPolyDataWriter

def main():
    # setup sphere
    sphereSource = vtkSphereSource()
    sphereSource.Update()

    polydata = vtkPolyData()
    polydata.ShallowCopy(sphereSource.GetOutput())

    normals = polydata.GetPointData().GetNormals()
    normals.SetName('TestN')

    writer = vtkXMLPolyDataWriter()
    writer.SetFileName('Test.vtp')
    writer.SetInputData(polydata)
    writer.Write()

if __name__ == '__main__':
    main()
```
