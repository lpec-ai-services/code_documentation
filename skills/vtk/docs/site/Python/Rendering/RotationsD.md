<!-- source: https://examples.vtk.org/site/Python/Rendering/RotationsD/ -->

# RotationsD

Repository source: [RotationsD](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Rendering/RotationsD.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestRotationsD.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestRotationsD.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/RotationsD/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RotationsD.py**

```python
#!/usr/bin/env python

"""
Rotations, VTK Textbook figure 3-31d.

Note: Make sure Rotations.py is in the same directory as this program.
"""

import Rotations

def main():
    file_name, figure, book_color = Rotations.get_program_parameters()
    # First a rotation about the x-axis, then six rotations about the y-axis.
    figure = 4
    book_color = True
    Rotations.rotate(file_name, figure, book_color)

if __name__ == '__main__':
    main()
```
