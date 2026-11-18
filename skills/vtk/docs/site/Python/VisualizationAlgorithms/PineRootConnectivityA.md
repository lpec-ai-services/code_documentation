<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/PineRootConnectivityA/ -->

# PineRootConnectivityA

Repository source: [PineRootConnectivityA](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/PineRootConnectivityA.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestPineRootConnectivityA.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestPineRootConnectivityA.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/PineRootConnectivityA/)), ([PythonicAPI](../../PythonicAPI/VisualizationAlgorithms/PineRootConnectivityA.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PineRootConnectivityA.py**

```python
#!/usr/bin/env python

"""
PineRootConnectivityA

Note: Make sure PineRootConnectivity.py is in the same directory as this program.
"""

import PineRootConnectivity

def main():
    fileName, noConnectivity = PineRootConnectivity.get_program_parameters()
    noConnectivity = 1
    PineRootConnectivity.pine_root_connectivity(fileName, noConnectivity)

if __name__ == '__main__':
    main()
```
