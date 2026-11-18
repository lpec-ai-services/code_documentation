<!-- source: https://examples.vtk.org/site/PythonicAPI/Points/MaskPointsFilter/ -->

# MaskPointsFilter

Repository source: [MaskPointsFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Points/MaskPointsFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestMaskPointsFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestMaskPointsFilter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Points/MaskPointsFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MaskPointsFilter.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

import vtk
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import VTK_DOUBLE
from vtkmodules.vtkCommonDataModel import vtkCone, vtkImageData
from vtkmodules.vtkFiltersCore import vtkGlyph3D
from vtkmodules.vtkFiltersGeneral import vtkSampleImplicitFunctionFilter
from vtkmodules.vtkFiltersPoints import vtkBoundedPointSource, vtkMaskPointsFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkImagingCore import vtkImageBinaryThreshold
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Extract points within an image mask.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-f', '--file_name', help='The volume data e.g. FullHead.mhd.')
    parser.add_argument('-u', '--upper_threshold', type=int, default=1100, help='The upper threshold, default is 1100.')
    args = parser.parse_args()
    return args.file_name, args.upper_threshold

def main():
    colors = vtkNamedColors()

    fn, upper = get_program_parameters()

    if fn:
        fn_path = Path(fn)
        if not fn_path.is_file():
            print('Unable to find: ', fn_path)
            return

        reader = vtkMetaImageReader(file_name=fn_path)
        reader.update()

        threshold = vtkImageBinaryThreshold(in_value=255, out_value=0,
                                            output_scalar_type=vtk.VTK_UNSIGNED_CHAR,
                                            threshold_function=vtkImageBinaryThreshold.THRESHOLD_UPPER,
                                            lower_threshold=upper,
                                            replace_in=True, replace_out=True)

        reader >> threshold
        image_mask = threshold.update().output

    else:
        image_mask = create_points()

    point_source = vtkBoundedPointSource(number_of_points=1000000, bounds=image_mask.bounds)

    mask_points = vtkMaskPointsFilter(mask_data=image_mask)
    point_source >> mask_points

    radius = image_mask.GetSpacing()[0] * 4.0
    sphere_source = vtkSphereSource(radius=radius)

    glyph3d = vtkGlyph3D(source_connection=sphere_source.output_port, scaling=False)
    mask_points >> glyph3d

    glyph3d_mapper = vtkPolyDataMapper(scalar_visibility=False)
    glyph3d >> glyph3d_mapper

    glyph3d_actor = vtkActor(mapper=glyph3d_mapper)
    glyph3d_actor.property.color = colors.GetColor3d('Banana')

    # Create the graphics stuff.
    ren = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name='MaskPointsFilter')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer, set the background and size.
    ren.AddActor(glyph3d_actor)

    # Generate an interesting view.
    ren_win.Render()
    ren.active_camera.position = (1, 0, 0)
    ren.active_camera.focal_point = (0, 1, 0)
    ren.active_camera.view_up = (0, 0, -1)
    ren.active_camera.Azimuth(30)
    ren.active_camera.Elevation(30)
    ren.ResetCamera()
    ren.active_camera.Dolly(1.0)
    ren.ResetCameraClippingRange()

    ren_win.Render()
    iren.Initialize()
    iren.Start()

def create_points():
    image = vtkImageData(dimensions=(256, 256, 256), spacing=(5.0 / 255.0, 5.0 / 255.0, 5.0 / 255.0),
                         origin=(-2.5, -2.5, -2.5))
    image.AllocateScalars(VTK_DOUBLE, 1)
    implicit_function = vtkCone()
    sample = vtkSampleImplicitFunctionFilter(implicit_function=implicit_function, input_data=image)

    threshold = vtkImageBinaryThreshold(in_value=255, out_value=0,
                                        output_scalar_type=vtk.VTK_UNSIGNED_CHAR,
                                        threshold_function=vtkImageBinaryThreshold.THRESHOLD_LOWER,
                                        upper_threshold=0.5,
                                        replace_in=True, replace_out=True)

    sample >> threshold

    return threshold.update().output

@dataclass(frozen=True)
class ImageThreshold:
    @dataclass(frozen=True)
    class ScalarType:
        VTK_CHAR: int = 2
        VTK_SIGNED_CHAR: int = 15
        VTK_UNSIGNED_CHAR: int = 3
        VTK_SHORT: int = 4
        VTK_UNSIGNED_SHORT: int = 5
        VTK_INT: int = 6
        VTK_UNSIGNED_INT: int = 7
        VTK_LONG: int = 8
        VTK_UNSIGNED_LONG: int = 9
        VTK_FLOAT: int = 10
        VTK_DOUBLE: int = 11

if __name__ == '__main__':
    main()
```
