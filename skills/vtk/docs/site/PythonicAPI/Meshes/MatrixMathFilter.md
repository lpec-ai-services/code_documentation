<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/MatrixMathFilter/ -->

# MatrixMathFilter

Repository source: [MatrixMathFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/MatrixMathFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestMatrixMathFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestMatrixMathFilter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/MatrixMathFilter/)), ([CSharp](https://examples.vtk.org/site/CSharp/Meshes/MatrixMathFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MatrixMathFilter.py**

```python
# !/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeometry import vtkDataSetSurfaceFilter
from vtkmodules.vtkFiltersVerdict import vtkMatrixMathFilter
from vtkmodules.vtkIOLegacy import vtkUnstructuredGridReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataWriter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Compute various quantities on cells and points in a mesh.'
    epilogue = '''
'''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None, help='A VTK Poly Data file e.g. tensors.vtk.')

    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    fn = get_program_parameters()
    if fn:
        fn_path = Path(fn)
        if not fn_path.is_file():
            print('Unable to find: ', fn_path)
            return
        else:
            reader = vtkUnstructuredGridReader(file_name=fn_path)
            reader.update()
    else:
        print('A file name is required e.g. tensors.vtk.')
        return

    surface_filter = vtkDataSetSurfaceFilter()

    matrix_math_filter = vtkMatrixMathFilter()
    matrix_math_filter.SetOperationToEigenvalue()
    # matrix_math_filter.SetOperationToDeterminant()
    # matrix_math_filter.SetOperationToInverse()
    p = (reader >> surface_filter >> matrix_math_filter)
    matrix_math_filter.update()
    matrix_math_filter.output.point_data.SetActiveScalars('Eigenvalue')
    # matrix_math_filter.output.point_data.SetActiveScalars('Determinant')
    # matrix_math_filter.output.point_data.SetActiveScalars('Inverse')

    writer = vtkXMLPolyDataWriter(file_name='output.vtp')
    p >> writer
    # writer.Write()

    # Visualize
    mapper = vtkPolyDataMapper()
    p >> mapper
    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('DimGray'))
    render_window = vtkRenderWindow(window_name='MatrixMathFilter')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    renderer.active_camera.Azimuth(45)
    renderer.active_camera.Pitch(-22.5)
    renderer.ResetCamera()
    renderer.active_camera.Zoom(0.95)
    render_window.Render()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
