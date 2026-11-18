<!-- source: https://examples.vtk.org/site/PythonicAPI/VolumeRendering/RayCastIsosurface/ -->

# RayCastIsosurface

Repository source: [RayCastIsosurface](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VolumeRendering/RayCastIsosurface.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestRayCastIsosurface.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestRayCastIsosurface.png?raw=true target=)

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

### Description

This examples show how volume rendering can produce isosurface-like images. Using [vtkOpenGLGPUVolumeRayCastMapper](https://www.vtk.org/doc/nightly/html/classvtkOpenGLGPUVolumeRayCastMapper.html) with an isosurface blend mode, two isosurfaces are created using appropriate transfer functions. The effect is similar to what is shown in [MedicalDemo2](https://examples.vtk.org/Cxx/Medical/MedicalDemo2/). The user can specify the **.mhd** file and the two isosurface values. The example uses 500 and 1150 for the two isosurface values. The volume rendering "surfaces" are fuzzier than the hard surfaces created by [vtkMarchingCubes](https://www.vtk.org/doc/nightly/html/classvtkMarchingCubes.html) in MedicalDemo3.

Usage

```python
    RayCastIsosurface.py FullHead.mhd 500 1150
```

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VolumeRendering/RayCastIsosurface/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RayCastIsosurface.py**

```python
#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPiecewiseFunction
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkCamera,
    vtkColorTransferFunction,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkVolume,
    vtkVolumeProperty
)
from vtkmodules.vtkRenderingVolumeOpenGL2 import vtkOpenGLGPUVolumeRayCastMapper

def get_program_parameters():
    import argparse
    description = 'Use volume rendering to produce an iso-surface-like image.'
    epilogue = '''

   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename', help='A required filename e.g. FullHead.mhd.')
    parser.add_argument('iso1', default=500, type=int, nargs='?', help='The first iso-contour.')
    parser.add_argument('iso2', default=1150, type=int, nargs='?', help='The second iso-contour.')
    args = parser.parse_args()
    return args.filename, args.iso1, args.iso2

def main():
    fn, iso1, iso2 = get_program_parameters()

    if not Path(fn).is_file():
        print(f'The path: {fn} does not exist.')
        return

    reader = vtkMetaImageReader(file_name=fn)

    colors = vtkNamedColors()

    mapper = vtkOpenGLGPUVolumeRayCastMapper(auto_adjust_sample_distances=False, sample_distance=0.5)
    reader >> mapper
    mapper.SetBlendModeToIsoSurface()

    iso1_rgb_pt_color = tuple(colors.GetColor3d('flesh'))
    iso2_rgb_pt_color = tuple(colors.GetColor3d('ivory'))
    color_transfer_function = vtkColorTransferFunction()
    color_transfer_function.RemoveAllPoints()
    color_transfer_function.AddRGBPoint(iso1, *iso1_rgb_pt_color)
    color_transfer_function.AddRGBPoint(iso2, *iso2_rgb_pt_color)

    scalar_opacity = vtkPiecewiseFunction()
    scalar_opacity.AddPoint(iso1, 0.3)
    scalar_opacity.AddPoint(iso2, 0.6)

    volume_property = vtkVolumeProperty(shade=True,
                                        interpolation_type=VolumeProperty.InterpolationType.VTK_LINEAR_INTERPOLATION,
                                        color=color_transfer_function, scalar_opacity=scalar_opacity)

    volume = vtkVolume(mapper=mapper, property=volume_property)

    renderer = vtkRenderer(background=colors.GetColor3d('cornflower'))
    renderer.AddVolume(volume)
    renderer.ResetCamera()

    render_window = vtkRenderWindow(size=(800, 600), window_name=f'{Path(sys.argv[0]).stem:s}')
    render_window.AddRenderer(renderer)

    style = vtkInteractorStyleTrackballCamera()

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window
    interactor.interactor_style = style

    # Add some contour values to draw iso-surfaces.
    volume_property.iso_surface_values.SetValue(0, iso1)
    volume_property.iso_surface_values.SetValue(1, iso2)

    # Generate a good view.
    camera = vtkCamera()
    camera.view_up = (0, 0, 1)
    camera.position = (0, -1, 0)
    camera.focal_point = (0, 0, 0)

    renderer.active_camera = camera
    renderer.ResetCamera()

    camera.Azimuth(30.0)
    camera.Elevation(30.0)
    camera.Dolly(1.5)
    renderer.ResetCameraClippingRange()

    render_window.Render()

    interactor.Start()

@dataclass(frozen=True)
class VolumeProperty:
    @dataclass(frozen=True)
    class InterpolationType:
        VTK_NEAREST_INTERPOLATION: int = 0
        VTK_LINEAR_INTERPOLATION: int = 1
        VTK_CUBIC_INTERPOLATION: int = 2

if __name__ == '__main__':
    main()
```
