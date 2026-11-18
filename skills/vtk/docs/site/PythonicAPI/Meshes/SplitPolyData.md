<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/SplitPolyData/ -->

# SplitPolyData

Repository source: [SplitPolyData](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/SplitPolyData.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestSplitPolyData.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestSplitPolyData.png?raw=true target=)

### Description

The [vtkOBBDicer](https://www.vtk.org/doc/nightly/html/classvtkOBBDicer.html) filter breaks up an input mesh into a number of pieces. The resulting mesh contains scalar point data that can be used to extract the individual pieces with a filter like [vtkThreshold](https://www.vtk.org/doc/nightly/html/classvtkThreshold.html). This example stores each piece into a .vtp file.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/SplitPolyData/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SplitPolyData.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtkmodules.vtkFiltersCore import vtkThreshold
from vtkmodules.vtkFiltersGeneral import vtkOBBDicer
from vtkmodules.vtkFiltersGeometry import vtkGeometryFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import (
    vtkXMLPolyDataReader,
    vtkXMLPolyDataWriter
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor, vtkDataSetMapper
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
    parser.add_argument('filename', nargs='?', default=None, help='Enter a polydata file e.g Armadillo.ply.')
    parser.add_argument('-n', '--number_of_pieces', default=4, type=check_positive,
                        help='The number of pieces, default = 4.')
    args = parser.parse_args()
    return args.filename, args.number_of_pieces

def main():
    named_colors = vtkNamedColors()

    file_name, pieces = get_program_parameters()
    poly_data = None
    # The components of the file name used to write out each piece.
    of_stem = 'sphere'
    of_suffix = '.vtp'
    if file_name:
        fn = Path(file_name)
        if fn.is_file():
            poly_data = read_poly_data(file_name)
            of_stem = fn.stem
            of_suffix = fn.suffix
            if not poly_data:
                return
        else:
            print(f'{file_name} not found.')
            return
    if file_name is None or poly_data is None:
        source = vtkSphereSource()
        poly_data = source.update().output

    # Create the pipeline.
    dicer = vtkOBBDicer(input_data=poly_data, number_of_pieces=pieces)
    dicer.SetDiceModeToSpecifiedNumberOfPieces()
    dicer.update()

    selector = vtkThreshold(input_array_to_process=(0, 0, 0, 0, 'vtkOBBDicer_GroupIds'))
    dicer >> selector
    selector.AllScalarsOff()

    # Create the graphics stuff.
    renderer = vtkRenderer(background=named_colors.GetColor3d('NavajoWhite'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name='SplitPolyData')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Use a color series to create a transfer function.
    color_series = vtkColorSeries(color_scheme=vtkColorSeries.BREWER_DIVERGING_SPECTRAL_11)

    # Create an actor for each piece.
    for i in range(0, dicer.number_of_actual_pieces):
        selector.SetLowerThreshold(i)
        selector.SetUpperThreshold(i)
        geometry = vtkGeometryFilter()
        selector >> geometry
        geometry.update()

        mapper = vtkDataSetMapper(input_data=geometry.output, scalar_visibility=False)

        actor = vtkActor(mapper=mapper)

        color = color_series.GetColor(i)
        dbl_color = [v / 255.0 for v in color]
        actor.property.color = dbl_color

        renderer.AddActor(actor)

    ren_win.Render()
    iren.Initialize()
    iren.Start()

    geometry = vtkGeometryFilter()
    selector >> geometry

    writer = vtkXMLPolyDataWriter()
    geometry >> writer
    for i in range(dicer.number_of_actual_pieces):
        piece_name = f'{of_stem}_{i + 1}{of_suffix}'
        selector.SetLowerThreshold(i)
        selector.SetUpperThreshold(i)
        writer.file_name = piece_name
        writer.Write()

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
