<!-- source: https://examples.vtk.org/site/PythonicAPI/Parallel/ExodusIIWriter/ -->

# ExodusIIWriter

Repository source: [ExodusIIWriter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Parallel/ExodusIIWriter.py)

### Description

Requires VTK to be built with VTK_USE_PARALLEL.

Other languages

See ([Java](https://examples.vtk.org/site/Java/Parallel/ExodusIIWriter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExodusIIWriter.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkFiltersGeneral import vtkTimeSourceExample
from vtkmodules.vtkIOExodus import vtkExodusIIWriter

def main():
    time_source = vtkTimeSourceExample()

    fn = 'output.exii'
    exodus_writer = vtkExodusIIWriter(file_name=fn, write_all_time_steps=True)
    time_source >> exodus_writer
    exodus_writer.Write()

if __name__ == '__main__':
    main()
```
