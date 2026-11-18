<!-- source: https://examples.vtk.org/site/PythonicAPI/InfoVis/PassThrough/ -->

# PassThrough

Repository source: [PassThrough](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/InfoVis/PassThrough.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/InfoVis/PassThrough/)), ([Java](https://examples.vtk.org/site/Java/InfoVis/PassThrough/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PassThrough.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersCore import vtkPassThrough
from vtkmodules.vtkFiltersSources import vtkSphereSource

def main():
    # Create a sphere
    sphere_source = vtkSphereSource()
    sphere_source.update()

    print(f'Points before: {sphere_source.output.number_of_points}')

    pass_through = vtkPassThrough()
    sphere_source >> pass_through
    pass_through.update()

    output = pass_through.GetOutput()

    print(f'Points after: {output.number_of_points}')

if __name__ == '__main__':
    main()
```
