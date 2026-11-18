<!-- source: https://examples.vtk.org/site/PythonicAPI/ImplicitFunctions/ImplicitDataSet/ -->

# ImplicitDataSet

Repository source: [ImplicitDataSet](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImplicitFunctions/ImplicitDataSet.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImplicitFunctions/ImplicitDataSet/)), ([Java](https://examples.vtk.org/site/Java/ImplicitFunctions/ImplicitDataSet/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImplicitDataSet.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonDataModel import vtkImplicitDataSet
from vtkmodules.vtkImagingCore import vtkRTAnalyticSource

def main():
    wavelet_source = vtkRTAnalyticSource()

    implicit_wavelet = vtkImplicitDataSet(data_set=wavelet_source.update().output)

    x = (0.5, 0, 0)
    print(f'The value should roughly be 258.658:\n'
          f'x: {implicit_wavelet.EvaluateFunction(x):0.3f}')

if __name__ == '__main__':
    main()
```
