<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ResamplePolyLine/ -->

# ResamplePolyLine

Repository source: [ResamplePolyLine](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ResamplePolyLine.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestResamplePolyLine.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestResamplePolyLine.png?raw=true target=)

### Description

This example resamples a polyline with a [vtkCardinalSpline](https://www.vtk.org/doc/nightly/html/classvtkCardinalSpline.html). The resampled line will have 10 times the number of points contained in the original polyline. If no XML file is provided, a random polyline is generated.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ResamplePolyLine/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ResamplePolyLine.py**

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
from vtkmodules.vtkCommonComputationalGeometry import vtkCardinalSpline
from vtkmodules.vtkCommonCore import (
    vtkMinimalStandardRandomSequence, vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData)
from vtkmodules.vtkFiltersCore import vtkGlyph3D
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
    description = 'Resample PolyLine.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None,
                        help='A polydata file containing the polyline with extension .vtp')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()
    if file_name:
        fn = Path(file_name)
        if not fn.is_file():
            print(f'{fn}\nNot found.')
            return
        else:
            reader = vtkXMLPolyDataReader(file_name=file_name)
            poly_data = reader.GetOutput()

    else:
        number_of_points = 10
        points = vtkPoints()
        random_sequence = vtkMinimalStandardRandomSequence(seed=8775070)
        for i in range(0, number_of_points):
            # Random position and radius.
            x = random_sequence.GetRangeValue(-1.0, 1.0)
            random_sequence.Next()
            y = random_sequence.GetRangeValue(-1.0, 1.0)
            random_sequence.Next()
            z = random_sequence.GetRangeValue(-1.0, 1.0)
            random_sequence.Next()
            points.InsertNextPoint(x, y, z)

        lines = vtkCellArray()
        lines.InsertNextCell(number_of_points)
        for i in range(0, number_of_points):
            lines.InsertCellPoint(i)

        poly_data = vtkPolyData(points=points, lines=lines)

    spline = vtkCardinalSpline(left_constraint=2, left_value=0.0, right_constraint=2, right_value=0.0)

    spline_filter = vtkSplineFilter(input_data=poly_data, spline=spline,
                                    number_of_subdivisions=poly_data.number_of_points * 10)

    spline_mapper = vtkPolyDataMapper()
    spline_filter >> spline_mapper

    spline_actor = vtkActor(mapper=spline_mapper)

    original_nodes = vtkSphereSource(radius=0.04, phi_resolution=10, theta_resolution=10)

    glyph_original = vtkGlyph3D(input_data=poly_data, source_data=original_nodes.update().output)

    new_nodes = vtkSphereSource(radius=0.02, phi_resolution=10, theta_resolution=10)

    glyph_new = vtkGlyph3D(source_data=new_nodes.update().output, source_connection=new_nodes.output_port)
    spline_filter >> glyph_new

    original_mapper = vtkPolyDataMapper()
    glyph_original >> original_mapper

    original_actor = vtkActor(mapper=original_mapper)
    original_actor.property.color = colors.GetColor3d('Banana')
    original_actor.property.opacity = 0.6

    new_mapper = vtkPolyDataMapper()
    glyph_new >> new_mapper

    new_actor = vtkActor(mapper=new_mapper)
    # new_actor.SetMapper(new_mapper)
    new_actor.property.color = colors.GetColor3d('Tomato')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SteelBlue'))

    render_window = vtkRenderWindow(window_name='ResamplePolyLine')
    render_window.AddRenderer(renderer)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(original_actor)
    renderer.AddActor(new_actor)
    renderer.AddActor(spline_actor)

    render_window.Render()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
