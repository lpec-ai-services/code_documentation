<!-- source: https://examples.vtk.org/site/Python/IO/ReadDICOM/ -->

# ReadDICOM

Repository source: [ReadDICOM](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/ReadDICOM.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadDICOM.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadDICOM.png?raw=true target=)

### Description

This example reads a DICOM file and displays it on the screen. [DICOM_Prostate](https://raw.githubusercontent.com/Kitware/vtk-examples/gh-pages/src/SupplementaryData/Cxx/IO/DICOM_Prostate.zip) is an example data set.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadDICOM/)), ([PythonicAPI](../../PythonicAPI/IO/ReadDICOM.md)), ([Java](https://examples.vtk.org/site/Java/IO/ReadDICOM/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadDICOM.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor

def get_program_parameters():
    import argparse
    description = 'Read Dicom image data'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='prostate.img')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    input_filename = get_program_parameters()

    # Read the DICOM file
    reader = vtkDICOMImageReader()
    reader.SetFileName(input_filename)
    reader.Update()

    # Visualize
    image_viewer = vtkImageViewer2()
    image_viewer.SetInputConnection(reader.GetOutputPort())
    render_window_interactor = vtkRenderWindowInteractor()
    image_viewer.SetupInteractor(render_window_interactor)
    image_viewer.Render()
    image_viewer.GetRenderer().SetBackground(colors.GetColor3d("SlateGray"))
    image_viewer.GetRenderWindow().SetWindowName("ReadDICOM")
    image_viewer.GetRenderer().ResetCamera()
    image_viewer.Render()

    render_window_interactor.Start()

if __name__ == "__main__":
    main()
```
