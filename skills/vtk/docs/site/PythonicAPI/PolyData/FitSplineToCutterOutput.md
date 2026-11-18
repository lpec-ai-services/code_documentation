<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/FitSplineToCutterOutput/ -->

# FitSplineToCutterOutput

Repository source: [FitSplineToCutterOutput](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/FitSplineToCutterOutput.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestFitSplineToCutterOutput.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestFitSplineToCutterOutput.png?raw=true target=)

### Description

This examples cuts a vtkPolydata and fits a [vtkKochanekSpline](https://www.vtk.org/doc/nightly/html/classvtkKochanekSpline.html) to the resulting polylines. The cut lines are passed through [vtkStripper](https://www.vtk.org/doc/nightly/html/classvtkStripper.html) to make them into connected polylines. Then, the lines are passed through [vtkTubeFilter](https://www.vtk.org/doc/nightly/html/classvtkTubeFilter.html) to improve the visualization.

The example takes an optional argument that specifies a vtk polydata file (.vtp). If run without an argument, it processes a sphere.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/FitSplineToCutterOutput/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FitSplineToCutterOutput.py**

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
from vtkmodules.vtkCommonComputationalGeometry import vtkKochanekSpline
from vtkmodules.vtkCommonDataModel import vtkPlane
from vtkmodules.vtkFiltersCore import vtkCutter, vtkStripper, vtkTubeFilter
from vtkmodules.vtkFiltersGeneral import vtkSplineFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Fit a spline to cutter output.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None, help='A polydata file e.g. cowHead.vtp.')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()
    if file_name:
        fp = Path(file_name)
        if not (fp.is_file() and fp.suffix == '.vtp'.lower()):
            print(f'Expected an existing file name with extension .vtp\n  got: {fp}')
            return
        else:
            reader = vtkXMLPolyDataReader(file_name=fp)
            poly_data = reader.update().output
    else:
        model_source = vtkSphereSource()
        poly_data = model_source.update().output

    model_mapper = vtkPolyDataMapper()
    poly_data >> model_mapper

    model = vtkActor(mapper=model_mapper)
    model.property.color = colors.GetColor3d('Tomato')
    model.property.SetInterpolationToFlat()

    length = poly_data.length

    plane = vtkPlane(normal=(0, 1, 1), origin=poly_data.center)

    cutter = vtkCutter(input_data=poly_data, cut_function=plane)
    cutter.GenerateValues(1, 0.0, 0.0)

    stripper = vtkStripper()

    spline = vtkKochanekSpline(default_tension=0.5)

    sf = vtkSplineFilter(spline=spline, number_of_subdivisions=50)
    sf.SetSubdivideToSpecified()
    sf.spline.closed = True

    tubes = vtkTubeFilter(number_of_sides=8, radius=length / 100.0)

    lines_mapper = vtkPolyDataMapper(scalar_visibility=False)
    cutter >> stripper >> sf >> tubes >> lines_mapper

    lines = vtkActor(mapper=lines_mapper)
    lines.property.color = colors.GetColor3d('Banana')

    renderer = vtkRenderer(use_hidden_line_removal=True, background=colors.GetColor3d('SlateGray'))

    render_window = vtkRenderWindow(size=(640, 480), window_name='FitSplineToCutterOutput')
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Add the actors to the renderer.
    renderer.AddActor(model)
    renderer.AddActor(lines)

    renderer.ResetCamera()
    renderer.active_camera.Azimuth(300)
    renderer.active_camera.Elevation(30)
    render_window.AddRenderer(renderer)

    # This starts the event loop and as a side effect causes an initial
    # render.
    render_window.Render()
    interactor.Start()

    # Extract the lines from the polydata.
    number_of_lines = cutter.output.GetNumberOfLines()

    print('-----------Lines without using vtkStripper')
    if number_of_lines == 1:
        print(f'There is {number_of_lines} line in the polydata')
    else:
        print(f'There are {number_of_lines} lines in the polydata')

    number_of_lines = stripper.output.GetNumberOfLines()
    print('-----------Lines using vtkStripper')
    if number_of_lines == 1:
        print(f'There is {number_of_lines} line in the polydata')
    else:
        print(f'There are {number_of_lines} lines in the polydata')

    points = stripper.output.GetPoints()
    cells = stripper.output.GetLines()

    cell_iter = cells.NewIterator()
    while not cell_iter.IsDoneWithTraversal():
        print(f'Line {cell_iter.GetCurrentCellId()}:')
        cell = cell_iter.GetCurrentCell()
        for i in range(0, cell.GetNumberOfIds()):
            point = points.GetPoint(cell.GetId(i))
            print(f'{" " * 6:s} {fmt_floats(point, 9)}')
        cell_iter.GoToNextCell()

def fmt_floats(v, w=0, d=6, pt='f'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
