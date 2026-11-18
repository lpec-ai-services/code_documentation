<!-- source: https://examples.vtk.org/site/PythonicAPI/VolumeRendering/MinIntensityRendering/ -->

# MinIntensityRendering

Repository source: [MinIntensityRendering](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VolumeRendering/MinIntensityRendering.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestMinIntensityRendering.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestMinIntensityRendering.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VolumeRendering/MinIntensityRendering/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MinIntensityRendering.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPiecewiseFunction
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkImagingCore import vtkImageClip
from vtkmodules.vtkRenderingCore import (
    vtkColorTransferFunction,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkVolume,
    vtkVolumeProperty
)
from vtkmodules.vtkRenderingVolume import vtkFixedPointVolumeRayCastMapper

def get_program_parameters():
    import argparse
    description = 'Minimum intensity rendering.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The file name to use e.g. ironProt.vtk.')
    args = parser.parse_args()
    return args.file_name

def main():
    fn = get_program_parameters()
    fp = Path(fn)
    file_check = True
    if not fp.is_file():
        print(f'Missing image file: {fp}.')
        file_check = False
    if not file_check:
        return

    colors = vtkNamedColors()

    # Create the renderers, render window, and interactor.
    ren_win = vtkRenderWindow()
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    ren = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    ren_win.AddRenderer(ren)
    ren_win.window_name = 'MinIntensityRendering'

    # Read the data from a vtk file.
    reader = vtkStructuredPointsReader(file_name=fp)

    # Create a transfer function mapping scalar value to opacity.
    opacity_tf = vtkPiecewiseFunction()
    opacity_tf.AddSegment(0, 1.0, 256, 0.1)

    color_tf = vtkColorTransferFunction()
    color_tf.AddRGBPoint(0, 1.0, 1.0, 1.0)
    color_tf.AddRGBPoint(255, 1.0, 1.0, 1.0)

    # Need to crop to actually see the minimum intensity.
    clip = vtkImageClip(output_whole_extent=(0, 66, 0, 66, 30, 37), clip_data=True)

    property = vtkVolumeProperty()
    property.scalar_opacity = opacity_tf
    property.color = color_tf
    property.SetInterpolationTypeToLinear()

    mapper = vtkFixedPointVolumeRayCastMapper()
    mapper.SetBlendModeToMinimumIntensity()
    reader >> clip >> mapper

    volume = vtkVolume(mapper=mapper)
    volume.property = property

    ren.AddViewProp(volume)

    ren_win.Render()

    ren.active_camera.Zoom(1.3)

    iren.Start()

if __name__ == '__main__':
    main()
```
