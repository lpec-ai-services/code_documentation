<!-- source: https://examples.vtk.org/site/PythonicAPI/Math/MatrixTranspose/ -->

# MatrixTranspose

Repository source: [MatrixTranspose](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Math/MatrixTranspose.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Math/MatrixTranspose/)), ([Java](https://examples.vtk.org/site/Java/Math/MatrixTranspose/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MatrixTranspose.py**

```python
# !/usr/bin/env python3

import numpy as np

from vtkmodules.vtkCommonMath import vtkMatrix3x3

def main():
    shape = (3, 3)
    m = vtkMatrix3x3()
    m.SetElement(2, 1, 2.0)  # Set element (2,1) to 2.0
    print('Original matrix:')
    print_matrix(m.data, shape)
    m.Transpose()
    print('Transpose:')
    print_matrix(m.data, shape)

def print_matrix(m, shape):
    data = np.array(m)
    data = data.reshape(shape)
    print(data)

if __name__ == '__main__':
    main()
```
