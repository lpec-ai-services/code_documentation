<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/MarchingCasesC/ -->

# MarchingCasesC

Repository source: [MarchingCasesC](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/MarchingCasesC.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestMarchingCasesC.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestMarchingCasesC.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/MarchingCasesC/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MarchingCasesC.py**

```python
#!/usr/bin/env python

"""
Marching cubes cases.

Case 3 is rotated 90 degrees about the y-axis with no label.

Note: Make sure MarchingCases.py is in the same directory as this program.
"""

import MarchingCases

def main():
    mc_cases = [3]
    rotation = 1
    label = False
    MarchingCases.marching_cubes(mc_cases, rotation, label)

if __name__ == '__main__':
    main()
```
