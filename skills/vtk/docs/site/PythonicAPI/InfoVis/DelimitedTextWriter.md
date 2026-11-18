<!-- source: https://examples.vtk.org/site/PythonicAPI/InfoVis/DelimitedTextWriter/ -->

# DelimitedTextWriter

Repository source: [DelimitedTextWriter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/InfoVis/DelimitedTextWriter.py)

### Description

The first line of the output is now `"column-0","column-1","column-2"`.

The first line is the names of the column arrays in the table.

I added them to the example because the example was crashing on Windows builds, where streaming a NULL char* is no bueno. (David Cole)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/InfoVis/DelimitedTextWriter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DelimitedTextWriter.py**

```python
# !/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonCore import (
    vtkVariant,
    vtkVariantArray
)
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkIOCore import vtkDelimitedTextWriter

def get_program_parameters():
    import argparse
    description = 'A Delimited text writer.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('-f', '--filename', default='output.txt',
                        help='An optional filename, the default is output.txt.')
    args = parser.parse_args()
    return args.filename

def main():
    output_filename = get_program_parameters()

    # Construct an empty table.
    table = vtkTable()

    # Add columns and column names.
    for i in range(0, 3):
        col = vtkVariantArray()
        col.name = f'column-{i:<d}'

        col.InsertNextValue(vtkVariant(0.0))
        col.InsertNextValue(vtkVariant(0.0))
        col.InsertNextValue(vtkVariant(0.0))
        table.AddColumn(col)

    # Fill the table with values.
    counter = 0
    for r in range(0, table.number_of_rows):
        for c in range(0, table.number_of_columns):
            table.SetValue(r, c, vtkVariant(counter))
            counter += 1

    writer = vtkDelimitedTextWriter(file_name=output_filename, input_data=table)
    writer.Write()

if __name__ == '__main__':
    main()
```
