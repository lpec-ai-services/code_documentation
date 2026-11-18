<!-- source: https://examples.vtk.org/site/Python/Visualization/HanoiIntermediate/ -->

# HanoiIntermediate

Repository source: [HanoiIntermediate](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/HanoiIntermediate.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestHanoiIntermediate.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestHanoiIntermediate.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/HanoiIntermediate/)), ([PythonicAPI](../../PythonicAPI/Visualization/HanoiIntermediate.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**HanoiIntermediate.py**

```python
#!/usr/bin/env python

"""
HanoiIntermediate

Note: Make sure Hanoi.py is in the same directory as this program.
"""

import Hanoi

def main():
    Hanoi.gv.configuration = 2
    Hanoi.hanoi()

if __name__ == '__main__':
    main()
```
