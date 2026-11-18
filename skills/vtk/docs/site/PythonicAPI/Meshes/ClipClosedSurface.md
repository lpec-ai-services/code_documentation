<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/ClipClosedSurface/ -->

# ClipClosedSurface

Repository source: [ClipClosedSurface](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/ClipClosedSurface.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestClipClosedSurface.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestClipClosedSurface.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/ClipClosedSurface/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ClipClosedSurface.py**

```python
# !/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkPlane,
    vtkPlaneCollection
)
from vtkmodules.vtkFiltersGeneral import vtkClipClosedSurface
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def get_program_parameters():
    import argparse
    description = 'Demonstrate the clipping of polygonal data.'
    epilogue = '''
'''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None, help='A VTK Poly Data file e.g. cow.vtp')

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
            reader = vtkXMLPolyDataReader(file_name=fn_path)
            poly_data = reader.update().output
    else:
        source = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=1.0, theta_resolution=20, phi_resolution=11)
        poly_data = source.update().output

    center = poly_data.GetCenter()
    plane1 = vtkPlane(origin=(center[0], center[1], center[2]), normal=(0.0, -1.0, 0.0))
    plane2 = vtkPlane(origin=(center[0], center[1], center[2]), normal=(0.0, 0.0, 1.0))
    plane3 = vtkPlane(origin=(center[0], center[1], center[2]), normal=(-1.0, 0.0, 0.0))

    planes = vtkPlaneCollection()
    planes.AddItem(plane1)
    planes.AddItem(plane2)
    planes.AddItem(plane3)

    clipper = vtkClipClosedSurface(input_data=poly_data, clipping_planes=planes, active_plane_id=2,
                                   scalar_mode=ClipClosedSurface.ScalarMode.VTK_CCS_SCALAR_MODE_COLORS)
    clipper.clip_color = colors.GetColor3d('Banana')
    clipper.base_color = colors.GetColor3d('Tomato')
    clipper.active_plane_color = colors.GetColor3d('SandyBrown')

    clip_mapper = vtkDataSetMapper()
    clipper >> clip_mapper

    clip_actor = vtkActor(mapper=clip_mapper)
    clip_actor.property.color = colors.GetColor3d('Tomato')
    clip_actor.property.interpolation = Property.Interpolation.VTK_FLAT

    # Create the graphics stuff.
    ren = vtkRenderer(background=colors.GetColor3d('SteelBlue'))

    ren_win = vtkRenderWindow(size=(512, 512), window_name='ClipClosedSurface')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer, set the background and size.
    ren.AddActor(clip_actor)

    # Generate an interesting view.
    ren.ResetCamera()
    ren.active_camera.Azimuth(120)
    ren.active_camera.Elevation(30)
    ren.active_camera.Dolly(1.0)
    ren.ResetCameraClippingRange()

    ren_win.Render()
    iren.Initialize()
    iren.Start()

@dataclass(frozen=True)
class ClipClosedSurface:
    @dataclass(frozen=True)
    class ScalarMode:
        VTK_CCS_SCALAR_MODE_NONE: int = 0
        VTK_CCS_SCALAR_MODE_COLORS: int = 1
        VTK_CCS_SCALAR_MODE_LABELS: int = 2

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
