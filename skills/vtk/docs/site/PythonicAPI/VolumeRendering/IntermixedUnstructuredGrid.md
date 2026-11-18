<!-- source: https://examples.vtk.org/site/PythonicAPI/VolumeRendering/IntermixedUnstructuredGrid/ -->

# IntermixedUnstructuredGrid

Repository source: [IntermixedUnstructuredGrid](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VolumeRendering/IntermixedUnstructuredGrid.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestIntermixedUnstructuredGrid.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestIntermixedUnstructuredGrid.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VolumeRendering/IntermixedUnstructuredGrid/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IntermixedUnstructuredGrid.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPiecewiseFunction
from vtkmodules.vtkFiltersCore import (
    vtkContourFilter,
    vtkThreshold
)
from vtkmodules.vtkFiltersGeneral import vtkDataSetTriangleFilter
from vtkmodules.vtkIOImage import vtkSLCReader
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkColorTransferFunction,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkVolume,
    vtkVolumeProperty
)
from vtkmodules.vtkRenderingVolume import vtkUnstructuredGridVolumeRayCastMapper

def get_program_parameters():
    import argparse
    description = 'Intermixed Unstructured Grid.'
    epilogue = '''

   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename1', help='A required filename e.g. ironProt.vtk.')
    parser.add_argument('filename2', help='A required filename e.g. neghip.slc.')
    args = parser.parse_args()
    return args.filename1, args.filename2

def main():
    fn1, fn2 = get_program_parameters()

    if not Path(fn1).is_file():
        print(f'The path: {fn1} does not exist.')
        return
    if not Path(fn2).is_file():
        print(f'The path: {fn2} does not exist.')
        return

    colors = vtkNamedColors()
    colors.SetColor('green_bkg', 0.1, 0.4, 0.2, 1.0)

    # Create the reader for the data.
    # This is the data that will be volume rendered.
    reader = vtkStructuredPointsReader()
    reader.SetFileName(fn1)

    # Create a reader for the other data that will
    # be contoured and displayed as a polygonal mesh.
    reader2 = vtkSLCReader()
    reader2.SetFileName(fn2)

    # Convert from vtkImageData to vtkUnstructuredGrid, remove
    # any cells where all values are below 80
    thresh = vtkThreshold(upper_threshold=80, threshold_function=vtkThreshold.THRESHOLD_UPPER, all_scalars=False)

    trifilter = vtkDataSetTriangleFilter()

    # Create a transfer function mapping scalar values to opacity.
    opacity_transfer_function = vtkPiecewiseFunction()
    opacity_transfer_function.AddPoint(80, 0.0)
    opacity_transfer_function.AddPoint(120, 0.2)
    opacity_transfer_function.AddPoint(255, 0.2)

    # Create transfer function mapping scalar values to color.
    color_transfer_function = vtkColorTransferFunction()
    color_transfer_function.AddRGBPoint(80.0, 0.0, 0.0, 0.0)
    color_transfer_function.AddRGBPoint(120.0, 0.0, 0.0, 1.0)
    color_transfer_function.AddRGBPoint(160.0, 1.0, 0.0, 0.0)
    color_transfer_function.AddRGBPoint(200.0, 0.0, 1.0, 0.0)
    color_transfer_function.AddRGBPoint(255.0, 0.0, 1.0, 1.0)

    # The property describes how the data will look.
    volume_property = vtkVolumeProperty(color=color_transfer_function, scalar_opacity=opacity_transfer_function,
                                        shade=False)
    volume_property.SetInterpolationTypeToLinear()

    # The mapper / ray cast function knows how to render the data.
    volume_mapper = vtkUnstructuredGridVolumeRayCastMapper()
    reader >> thresh >> trifilter >> volume_mapper

    ren = vtkRenderer(background=colors.GetColor3d('green_bkg'))
    ren_win = vtkRenderWindow(size=(640, 512), window_name='IntermixedUnstructuredGrid')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Contour the second dataset.
    contour = vtkContourFilter()
    contour.SetValue(0, 80)

    # Create a mapper for the polygonal data.
    mapper = vtkPolyDataMapper(scalar_visibility=False)
    reader2 >> contour >> mapper

    # Create an actor for the polygonal data.
    actor = vtkActor(mapper=mapper)

    ren.AddViewProp(actor)

    volume = vtkVolume()
    volume.SetMapper(volume_mapper)
    volume.SetProperty(volume_property)

    ren.AddVolume(volume)

    ren.ResetCamera()
    ren.active_camera.Zoom(1.5)

    # Render composite. In default mode. For coverage.
    ren_win.Render()

    iren.Start()

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
