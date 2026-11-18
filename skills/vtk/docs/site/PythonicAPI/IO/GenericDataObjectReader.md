<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/GenericDataObjectReader/ -->

# GenericDataObjectReader

Repository source: [GenericDataObjectReader](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/GenericDataObjectReader.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/GenericDataObjectReader/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GenericDataObjectReader.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkIOLegacy import vtkGenericDataObjectReader

def get_program_parameters():
    import argparse
    description = 'Demonstrate the use of vtkGenericDataObjectReader'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='Path to the input file name e.g. blow.vtk.')
    args = parser.parse_args()
    return args.file_name

def main():
    file_name = get_program_parameters()
    # Get all data from the file.
    reader = vtkGenericDataObjectReader(file_name=file_name)
    reader.update()

    # All the standard data types can be checked and obtained like this:
    if reader.IsFilePolyData():
        print(f'Output is polydata with {reader.poly_data_output.number_of_points} points.')
    if reader.IsFileUnstructuredGrid():
        print(f'Output is unstructured grid with {reader.unstructured_grid_output.number_of_points} points.')
    if reader.IsFileStructuredGrid():
        print(f'Output is unstructured grid with {reader.structured_grid_output.number_of_points} points.')

if __name__ == '__main__':
    main()
```
