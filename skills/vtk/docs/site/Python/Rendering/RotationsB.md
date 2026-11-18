<!-- source: https://examples.vtk.org/site/Python/Rendering/RotationsB/ -->

# RotationsB

Repository source: [RotationsB](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Rendering/RotationsB.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestRotationsB.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestRotationsB.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/RotationsB/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RotationsB.py**

```python
#!/usr/bin/env python

"""
Rotations, VTK Textbook figure 3-31b.

Note: Make sure Rotations.py is in the same directory as this program.
"""

import Rotations

def main():
    file_name, figure, book_color = Rotations.get_program_parameters()
    # Set up for six rotations about the y-axis.
    figure = 2
    book_color = True
    Rotations.rotate(file_name, figure, book_color)

if __name__ == '__main__':
    main()
```
