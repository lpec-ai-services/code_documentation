<!-- source: https://examples.vtk.org/site/Python/Rendering/WalkCowA/ -->

# WalkCowA

Repository source: [WalkCowA](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Rendering/WalkCowA.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestWalkCowA.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestWalkCowA.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/WalkCowA/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**WalkCowA.py**

```python
#!/usr/bin/env python

"""
WalkCow, VTK Textbook figure 3-33a.

Note: Make sure WalkCow.py is in the same directory as this program.
"""

import WalkCow

def main():
    file_name, figure = WalkCow.get_program_parameters()
    figure = 1
    WalkCow.walk_cow(file_name, figure)

if __name__ == '__main__':
    main()
```
