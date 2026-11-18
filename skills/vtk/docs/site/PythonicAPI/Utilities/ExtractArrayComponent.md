<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/ExtractArrayComponent/ -->

# ExtractArrayComponent

Repository source: [ExtractArrayComponent](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/ExtractArrayComponent.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/ExtractArrayComponent/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractArrayComponent.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonCore import (
    vtkPoints,
    vtkDoubleArray
)
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import vtkArrayCalculator

def main():
    points = vtkPoints()
    points.InsertNextPoint(1.0, 0.0, 0.0)
    points.InsertNextPoint(2.0, 0.0, 0.0)
    points.InsertNextPoint(3.0, 0.0, 0.0)

    array = vtkDoubleArray(name='InputArray', number_of_components=3)
    array.InsertNextTuple3(1, 10, 100)
    array.InsertNextTuple3(2, 20, 200)
    array.InsertNextTuple3(3, 30, 300)

    polydata = vtkPolyData()
    polydata.SetPoints(points)
    polydata.point_data.AddArray(array)

    # Extract component '1' from the InputArray by taking the dot product of each tuple with the vector (0,1,0).
    calc1 = vtkArrayCalculator(input_data=polydata, result_array_name='OutputArray', function='dot(InputArray,jHat)')
    calc1.AddVectorArrayName('InputArray')
    calc1.update()

    output1 = calc1.GetPolyDataOutput().GetPointData().GetArray('OutputArray')

    print('OutputArray value = dot(InputArray,jHat)')
    for i in range(0, output1.GetNumberOfTuples()):
        print(f'  {i:2d}: {output1.GetValue(i):5.1f}')

if __name__ == '__main__':
    main()
```
