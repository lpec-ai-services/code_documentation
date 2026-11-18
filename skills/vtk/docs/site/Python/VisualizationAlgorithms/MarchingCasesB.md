<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/MarchingCasesB/ -->

# MarchingCasesB

Repository source: [MarchingCasesB](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/MarchingCasesB.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestMarchingCasesB.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestMarchingCasesB.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/MarchingCasesB/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MarchingCasesB.py**

```python
#!/usr/bin/env python

"""
Marching cubes complementary cases.

Cases 3c, 6c, 7c, 10c, 12c and 13c are displayed.

Note: Make sure MarchingCases.py is in the same directory as this program.
"""

import MarchingCases

def main():
    mc_cases = [-3, -6, -7, -10, -12, -13]
    MarchingCases.marching_cubes(mc_cases)

if __name__ == '__main__':
    main()
```
