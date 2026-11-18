<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/FileOutputWindow/ -->

# FileOutputWindow

Repository source: [FileOutputWindow](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/FileOutputWindow.py)

### Description

This example shows how to pipe error output to a text file instead of the usual vtk pop-up window. The output will also be written to the console.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/FileOutputWindow/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FileOutputWindow.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonCore import (
    vtkFileOutputWindow,
    vtkOutputWindow
)
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader

def main():
    file_output_window = vtkFileOutputWindow(file_name='FileOutputWindow.txt')

    # Note that the SetInstance function is a static member of vtkOutputWindow.
    vtkOutputWindow.SetInstance(file_output_window)

    # This causes an error intentionally (file name not specified) - this error
    # will be written to the file output.txt
    reader = vtkXMLPolyDataReader()
    reader.Update()

if __name__ == '__main__':
    main()
```
