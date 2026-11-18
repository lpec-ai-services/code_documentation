<!-- source: https://examples.vtk.org/site/Python/IO/ReadPLOT3D/ -->

# ReadPLOT3D

Repository source: [ReadPLOT3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/ReadPLOT3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadPLOT3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/IO/TestReadPLOT3D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadPLOT3D/)), ([Java](https://examples.vtk.org/site/Java/IO/ReadPLOT3D/)), ([CSharp](https://examples.vtk.org/site/CSharp/IO/ReadPLOT3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadPLOT3D.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeometry import vtkStructuredGridGeometryFilter
from vtkmodules.vtkIOParallel import vtkMultiBlockPLOT3DReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    xyzFile, qFile = get_program_parameters()

    colors = vtkNamedColors()

    reader = vtkMultiBlockPLOT3DReader()
    reader.SetXYZFileName(xyzFile)
    reader.SetQFileName(qFile)
    reader.SetScalarFunctionNumber(100)
    reader.SetVectorFunctionNumber(202)
    reader.Update()

    geometry = vtkStructuredGridGeometryFilter()
    geometry.SetInputData(reader.GetOutput().GetBlock(0))

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(geometry.GetOutputPort())
    mapper.ScalarVisibilityOff()

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    render = vtkRenderer()
    render.AddActor(actor)
    render.SetBackground(colors.GetColor3d('DarkSlateGray'))

    render_win = vtkRenderWindow()
    render_win.AddRenderer(render)
    render_win.SetSize(640, 480)
    render_win.SetWindowName('ReadPLOT3D')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(render_win)

    camera = render.GetActiveCamera()
    camera.SetPosition(5.02611, -23.535, 50.3979)
    camera.SetFocalPoint(9.33614, 0.0414149, 30.112)
    camera.SetViewUp(-0.0676794, 0.657814, 0.750134)
    camera.SetDistance(31.3997)
    camera.SetClippingRange(12.1468, 55.8147)

    render_win.Render()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'Read PLOT3D data files'
    epilogue = '''
    vtkMultiBlockPLOT3DReader is a reader object that reads PLOT3D formatted files 
    and generates structured grid(s) on output.
    PLOT3D is a computer graphics program designed to visualize the grids 
    and solutions of computational fluid dynamics.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename1', help='combxyz.bin.')
    parser.add_argument('filename2', help='combq.bin.')
    args = parser.parse_args()
    return args.filename1, args.filename2

if __name__ == '__main__':
    main()
```
