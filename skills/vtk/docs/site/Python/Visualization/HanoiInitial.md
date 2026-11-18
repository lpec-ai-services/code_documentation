<!-- source: https://examples.vtk.org/site/Python/Visualization/HanoiInitial/ -->

# HanoiInitial

Repository source: [HanoiInitial](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/HanoiInitial.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestHanoiInitial.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestHanoiInitial.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/HanoiInitial/)), ([PythonicAPI](../../PythonicAPI/Visualization/HanoiInitial.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**HanoiInitial.py**

```python
#!/usr/bin/env python

"""
HanoiInitial

Note: Make sure Hanoi.py is in the same directory as this program.
"""

import Hanoi

def main():
    Hanoi.gv.configuration = 1
    Hanoi.hanoi()

if __name__ == '__main__':
    main()
```
