<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/Silhouette/ -->

# Silhouette

Repository source: [Silhouette](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/Silhouette.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestSilhouette.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestSilhouette.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/Silhouette/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Silhouette.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkCleanPolyData
from vtkmodules.vtkFiltersHybrid import vtkPolyDataSilhouette
from vtkmodules.vtkFiltersSources import vtkSphereSource
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
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkPolyDataMapper
)

def get_program_parameters():
    import argparse
    description = 'Add a silhouette around a polydata object.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None,
                        help='An optional file name, e.g. cowHead.vtp.')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    fn = get_program_parameters()
    if fn:
        fp = Path(fn)
        if not fp.is_file():
            print(f'The path: {fp} does not exist.')
            return
        pd = read_poly_data(fp)
        clean = vtkCleanPolyData()
        poly_data = (pd >> clean).update().output

    else:
        # Default to a sphere if the path is empty.
        source = vtkSphereSource()
        poly_data = source.update().output

    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='Silhouette')
    render_window.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = render_window

    # Create the mapper and actor for the original model.
    mapper = vtkPolyDataMapper(scalar_visibility=False)
    poly_data >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.interpolation = Property.Interpolation.VTK_FLAT
    actor.property.color = colors.GetColor3d('Banana')

    silhouette = vtkPolyDataSilhouette(input_data=poly_data, camera=renderer.active_camera, enable_feature_angle=False)
    # Create the mapper and actor for the silhouette.
    mapper2 = vtkPolyDataMapper()
    silhouette >> mapper2

    actor2 = vtkActor(mapper=mapper2)
    actor2.property.interpolation = Property.Interpolation.VTK_FLAT
    actor2.property.color = colors.GetColor3d('Tomato')
    actor2.property.line_width = 5

    # The original model.
    renderer.AddActor(actor)
    # The silhouette actor.
    renderer.AddActor(actor2)

    renderer.ResetCamera()
    renderer.active_camera.Azimuth(30)
    renderer.active_camera.Elevation(30)
    renderer.active_camera.Dolly(1.5)

    renderer.ResetCameraClippingRange()

    iren.Start()

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
        reader.update()
        poly_data = reader.output
        return poly_data
    else:
        return None

@dataclass(frozen=True)
class Property:
    @dataclass(frozen=True)
    class Interpolation:
        VTK_FLAT: int = 0
        VTK_GOURAUD: int = 1
        VTK_PHONG: int = 2
        VTK_PBR: int = 3

    @dataclass(frozen=True)
    class Representation:
        VTK_POINTS: int = 0
        VTK_WIREFRAME: int = 1
        VTK_SURFACE: int = 2

if __name__ == '__main__':
    main()
```
