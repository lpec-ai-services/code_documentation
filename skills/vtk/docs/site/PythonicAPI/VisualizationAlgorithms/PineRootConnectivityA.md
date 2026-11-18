<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/PineRootConnectivityA/ -->

# PineRootConnectivityA

Repository source: [PineRootConnectivityA](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/PineRootConnectivityA.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestPineRootConnectivityA.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestPineRootConnectivityA.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/PineRootConnectivityA/)), ([Python](../../Python/VisualizationAlgorithms/PineRootConnectivityA.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PineRootConnectivityA.py**

```python
#!/usr/bin/env python3

"""
PineRootConnectivityA

Note: Make sure PineRootConnectivity.py is in the same directory as this program.
"""

import PineRootConnectivity

def main():
    file_name, no_connectivity = PineRootConnectivity.get_program_parameters()
    no_connectivity = True
    PineRootConnectivity.pine_root_connectivity(file_name, no_connectivity)

if __name__ == '__main__':
    main()
```
