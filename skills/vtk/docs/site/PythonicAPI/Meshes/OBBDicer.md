<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/OBBDicer/ -->

# OBBDicer

Repository source: [OBBDicer](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/OBBDicer.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestOBBDicer.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestOBBDicer.png?raw=true target=)

### Description

The [vtkOBBDicer](https://www.vtk.org/doc/nightly/html/classvtkOBBDicer.html) filter breaks up an input mesh into a number of pieces. The resulting mesh contains scalar point data that can be used to extract the individual pieces with a filter like vtkThresholdFilter. This examples displays the output of [vtkOBBDicer](https://www.vtk.org/doc/nightly/html/classvtkOBBDicer.html) with a different color for each piece.

The first argument is a filename for a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html) reader. If not specified, then a [vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html) generates the [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). The second argument is the number of pieces and is optional. The default is 4.

The example was run with these arguments:

```python
   OBBDicer Armadillo.ply 20
```

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/OBBDicer/)), ([CSharp](https://examples.vtk.org/site/CSharp/Meshes/OBBDicer/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OBBDicer.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkLookupTable,
    vtkMinimalStandardRandomSequence
)
from vtkmodules.vtkFiltersGeneral import vtkOBBDicer
from vtkmodules.vtkFiltersSources import vtkOutlineCornerFilter
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    def check_positive(value):
        ival = int(value)
        if ival <= 0:
            raise argparse.ArgumentTypeError('Value must be positive.')
        return ival

    import argparse
    description = 'OBBDicer.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('filename', help='Enter a polydata file e.g Armadillo.ply.')
    parser.add_argument('-n', '--number_of_pieces', default=4, type=check_positive,
                        help='The number of pieces, default = 4.')
    args = parser.parse_args()
    return args.filename, args.number_of_pieces

def main():
    file_name, pieces = get_program_parameters()
    poly_data = None
    if file_name:
        if Path(file_name).is_file():
            poly_data = read_poly_data(file_name)
            if not poly_data:
                return
        else:
            print(f'{file_name} not found.')
            return

    # Create pipeline
    dicer = vtkOBBDicer(input_data=poly_data, number_of_pieces=pieces)
    dicer.SetDiceModeToSpecifiedNumberOfPieces()
    dicer.update()

    number_of_regions = dicer.number_of_actual_pieces

    # Fill in a few known colors, the rest will be generated if needed.
    colors = vtkNamedColors()

    lut = vtkLookupTable()
    lut.number_of_table_values = max(number_of_regions, 10)
    lut.Build()
    lut.SetTableValue(0, colors.GetColor4d('Gold'))
    lut.SetTableValue(1, colors.GetColor4d('Banana'))
    lut.SetTableValue(2, colors.GetColor4d('Tomato'))
    lut.SetTableValue(3, colors.GetColor4d('Wheat'))
    lut.SetTableValue(4, colors.GetColor4d('Lavender'))
    lut.SetTableValue(5, colors.GetColor4d('Flesh'))
    lut.SetTableValue(6, colors.GetColor4d('Raspberry'))
    lut.SetTableValue(7, colors.GetColor4d('Salmon'))
    lut.SetTableValue(8, colors.GetColor4d('Mint'))
    lut.SetTableValue(9, colors.GetColor4d('Peacock'))

    if number_of_regions > 9:
        rng = vtkMinimalStandardRandomSequence(seed=8775070)
        value_range = (0.6, 1.0)
        for i in range(10, number_of_regions):
            r = rng.GetRangeValue(*value_range)
            rng.Next()
            g = rng.GetRangeValue(*value_range)
            rng.Next()
            b = rng.GetRangeValue(*value_range)
            rng.Next()
            lut.SetTableValue(i, r, g, b, 1.0)

    input_mapper = vtkPolyDataMapper(scalar_range=(0, dicer.number_of_actual_pieces), lookup_table=lut)
    dicer >> input_mapper

    print(f'Asked for:  {dicer.number_of_pieces}  pieces, got: {dicer.number_of_actual_pieces}')

    input_actor = vtkActor(mapper=input_mapper)
    input_actor.property.SetInterpolationToFlat()

    outline = vtkOutlineCornerFilter(input_data=poly_data)

    outline_mapper = vtkPolyDataMapper()
    outline >> outline_mapper

    outline_actor = vtkActor(mapper=outline_mapper)
    outline_actor.property.color = colors.GetColor3d('Black')

    renderer = vtkRenderer(use_hidden_line_removal=True, background=colors.GetColor3d('SlateGray'))

    render_window = vtkRenderWindow(window_name='OBBDicer')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Add the actors to the renderer.
    renderer.AddActor(outline_actor)
    renderer.AddActor(input_actor)

    renderer.active_camera.Azimuth(150)
    renderer.active_camera.Elevation(15)
    renderer.ResetCamera()

    # Render the image
    render_window.Render()

    interactor.Start()

def read_poly_data(file_name):
    if not file_name:
        print(f'No file name.')
        return None

    valid_suffixes = ['.g', '.obj', '.stl', '.ply', '.vtk', '.vtp']
    path = Path(file_name)
    ext = None
    if path.suffix:
        ext = path.suffix.lower()
    if path.suffix not in valid_suffixes:
        print(f'No reader for this file suffix: {ext}')
        return None

    reader = None
    if ext == '.ply':
        reader = vtkPLYReader(file_name=file_name)
    elif ext == '.vtp':
        reader = vtkXMLPolyDataReader(file_name=file_name)
    elif ext == '.obj':
        reader = vtkOBJReader(file_name=file_name)
    elif ext == '.stl':
        reader = vtkSTLReader(file_name=file_name)
    elif ext == '.vtk':
        reader = vtkPolyDataReader(file_name=file_name)
    elif ext == '.g':
        reader = vtkBYUReader(file_name=file_name)

    if reader:
        return reader.update().output
    else:
        return None

if __name__ == '__main__':
    main()
```
