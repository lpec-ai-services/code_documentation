<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/PCAStatistics/ -->

# PCAStatistics

Repository source: [PCAStatistics](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/PCAStatistics.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/PCAStatistics/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PCAStatistics.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonCore import vtkDoubleArray
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkFiltersStatistics import (
    vtkPCAStatistics,
    vtkStatisticsAlgorithm
)

def main():
    # Each one of these arrays is a single component of
    # the data. That is, if you have 3D spatial data (x,y,z)
    # you need to construct an array of all the x values,
    # an array of all the y values, and an array of all the
    # z values.

    # Construct a data set of three 3D points.

    # These would be all of your 'x' values.
    m0_name = 'M0'
    dataset1_arr = vtkDoubleArray(name=m0_name, number_of_components=1)
    dataset1_arr.InsertNextValue(0)
    dataset1_arr.InsertNextValue(1)
    dataset1_arr.InsertNextValue(0)

    # These would be all of your 'y' values.
    m1_name = 'M1'
    dataset2_arr = vtkDoubleArray(name=m1_name, number_of_components=1)
    dataset2_arr.InsertNextValue(0)
    dataset2_arr.InsertNextValue(0)
    dataset2_arr.InsertNextValue(1)

    # These would be all of your 'z' values.
    m2_name = 'M2'
    dataset3_arr = vtkDoubleArray(name=m2_name, number_of_components=1)
    dataset3_arr.InsertNextValue(0)
    dataset3_arr.InsertNextValue(0)
    dataset3_arr.InsertNextValue(0)

    dataset_table = vtkTable()
    dataset_table.AddColumn(dataset1_arr)
    dataset_table.AddColumn(dataset2_arr)
    dataset_table.AddColumn(dataset3_arr)

    pca_statistics = vtkPCAStatistics()
    pca_statistics.SetInputData(vtkStatisticsAlgorithm.INPUT_DATA, dataset_table)
    pca_statistics.SetColumnStatus(m0_name, 1)
    pca_statistics.SetColumnStatus(m1_name, 1)
    pca_statistics.SetColumnStatus(m2_name, 1)
    pca_statistics.RequestSelectedColumns()
    pca_statistics.SetDeriveOption(True)
    pca_statistics.update()

    ###### Eigenvalues ######
    eigenvalues = vtkDoubleArray()
    pca_statistics.GetEigenvalues(eigenvalues)
    for i in range(0, eigenvalues.number_of_tuples):
        print(f'Eigenvalue {i}  = {eigenvalues.GetValue(i):9.6f}')

    ###### Eigenvectors ######
    eigenvectors = vtkDoubleArray()
    pca_statistics.GetEigenvectors(eigenvectors)
    evec = [0] * eigenvectors.GetNumberOfComponents()
    for i in range(0, eigenvectors.number_of_tuples):
        eigenvectors.GetTuple(i, evec)
        s = f'Eigenvector {i} = ({fmt_floats(evec, w=0, d=6)})'
        print(s)

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

if __name__ == '__main__':
    main()
```
