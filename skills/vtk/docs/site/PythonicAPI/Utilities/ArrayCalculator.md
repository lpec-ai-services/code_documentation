<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/ArrayCalculator/ -->

# ArrayCalculator

Repository source: [ArrayCalculator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/ArrayCalculator.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/ArrayCalculator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ArrayCalculator.py**

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

    array = vtkDoubleArray(name='orig')
    array.InsertNextValue(1.0)
    array.InsertNextValue(2.0)
    array.InsertNextValue(3.0)

    polydata = vtkPolyData()
    polydata.SetPoints(points)
    polydata.point_data.AddArray(array)

    calc1 = vtkArrayCalculator(input_data=polydata, result_array_name='orig', function='orig+1')
    calc1.AddScalarArrayName('orig')
    calc1.update()

    output1 = calc1.GetPolyDataOutput().GetPointData().GetArray('orig')

    print('output1 value = orig+1')
    for i in range(0, output1.GetNumberOfTuples()):
        print(f'  {i:2d}: {output1.GetValue(i):5.1f}')

    calc2 = vtkArrayCalculator(input_data=polydata, result_array_name='new', function='if(orig=2,1,orig)')
    calc2.AddScalarArrayName('orig')
    calc2.update()

    output2 = calc2.GetPolyDataOutput().GetPointData().GetArray('new')

    print('output2 value = if(orig=2,1,orig)')
    for i in range(0, output2.GetNumberOfTuples()):
        print(f'  {i:2d}: {output2.GetValue(i):5.1f}')

if __name__ == '__main__':
    main()
```
