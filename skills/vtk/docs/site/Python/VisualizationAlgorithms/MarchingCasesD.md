<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/MarchingCasesD/ -->

# MarchingCasesD

Repository source: [MarchingCasesD](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/MarchingCasesD.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestMarchingCasesD.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestMarchingCasesD.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/MarchingCasesD/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MarchingCasesD.py**

```python
#!/usr/bin/env python

"""
Marching cubes cases.

Case 7 is rotated 180 degrees about the y-axis with no label.

Note: Make sure MarchingCases.py is in the same directory as this program.
"""

import MarchingCases

def main():
    mc_cases = [7]
    rotation = 2
    label = False
    MarchingCases.marching_cubes(mc_cases, rotation, label)

if __name__ == '__main__':
    main()
```
