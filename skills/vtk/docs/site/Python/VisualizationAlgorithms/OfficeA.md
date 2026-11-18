<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/OfficeA/ -->

# OfficeA

Repository source: [OfficeA](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/OfficeA.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestOfficeA.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestOfficeA.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/OfficeA/)), ([PythonicAPI](../../PythonicAPI/VisualizationAlgorithms/OfficeA.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OfficeA.py**

```python
#!/usr/bin/env python

"""
OfficeA.

Note: Make sure Office.py is in the same directory as this program.
"""

import Office

def main():
    file_name, center = Office.get_program_parameters()
    center = 0
    Office.office(file_name, center)

if __name__ == '__main__':
    main()
```
