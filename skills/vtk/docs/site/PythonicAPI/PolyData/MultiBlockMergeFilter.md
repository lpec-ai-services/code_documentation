<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/MultiBlockMergeFilter/ -->

# MultiBlockMergeFilter

Repository source: [MultiBlockMergeFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/MultiBlockMergeFilter.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/MultiBlockMergeFilter/)), ([CSharp](https://examples.vtk.org/site/CSharp/PolyData/MultiBlockMergeFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MultiBlockMergeFilter.py**

```python
# !/usr/bin/env python3

from vtkmodules.vtkCommonDataModel import vtkMultiBlockDataSet
from vtkmodules.vtkFiltersGeneral import vtkMultiBlockMergeFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource

def main():
    sphere_source1 = vtkSphereSource()

    sphere_source2 = vtkSphereSource(center=(10, 10, 10))

    multi_block_data_set1 = vtkMultiBlockDataSet(number_of_blocks=1)
    multi_block_data_set1.SetBlock(0, sphere_source1.update().output)

    multi_block_data_set2 = vtkMultiBlockDataSet(number_of_blocks=1)
    multi_block_data_set2.SetBlock(0, sphere_source2.update().output)

    multi_block_merge_filter = vtkMultiBlockMergeFilter()
    multi_block_merge_filter.AddInputData(multi_block_data_set1)
    multi_block_merge_filter.AddInputData(multi_block_data_set2)
    multi_block_merge_filter.update()

if __name__ == '__main__':
    main()
```
