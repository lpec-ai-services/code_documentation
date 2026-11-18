<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ThinPlateSplineTransform/ -->

# ThinPlateSplineTransform

Repository source: [ThinPlateSplineTransform](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ThinPlateSplineTransform.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestThinPlateSplineTransform.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestThinPlateSplineTransform.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ThinPlateSplineTransform/)), ([Java](https://examples.vtk.org/site/Java/PolyData/ThinPlateSplineTransform/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ThinPlateSplineTransform.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkLookupTable,
    vtkPoints
)
from vtkmodules.vtkCommonTransforms import vtkThinPlateSplineTransform
from vtkmodules.vtkIOImage import vtkBMPReader
from vtkmodules.vtkImagingCore import (
    vtkImageBlend,
    vtkImageMapToColors,
    vtkImageReslice
)
from vtkmodules.vtkImagingSources import vtkImageGridSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTerrain
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkImageMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Warp an image with a thin plate spline.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help=' Filename.bmp e.g. masonry.bmp.')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()

    fp = Path(file_name)
    if not fp.is_file():
        print(f'{fp} not found.')
        return

    # First, create an image to warp.
    image_grid = vtkImageGridSource(grid_spacing=(16, 16, 0), grid_origin=(0, 0, 0), data_extent=(0, 255, 0, 255, 0, 0))
    image_grid.SetDataScalarTypeToUnsignedChar()

    table = vtkLookupTable(table_range=(0, 1), alpha_range=(0.0, 1.0), hue_range=(0.15, 0.15), saturation_range=(1, 1),
                           value_range=(0, 1))
    table.Build()

    alpha = vtkImageMapToColors(lookup_table=table)
    image_grid >> alpha

    reader = vtkBMPReader(file_name=fp)
    reader.update()
    data_extent = reader.GetDataExtent()
    # Use data_extent[1] and data_extent[3] to set the render window size.

    blend = vtkImageBlend()
    reader >> blend
    alpha >> blend

    # Next, create a ThinPlateSpline transform.

    p1 = vtkPoints(number_of_points=8)
    p1.SetPoint(0, 0, 0, 0)
    p1.SetPoint(1, 0, 255, 0)
    p1.SetPoint(2, 255, 0, 0)
    p1.SetPoint(3, 255, 255, 0)
    p1.SetPoint(4, 96, 96, 0)
    p1.SetPoint(5, 96, 159, 0)
    p1.SetPoint(6, 159, 159, 0)
    p1.SetPoint(7, 159, 96, 0)

    p2 = vtkPoints(number_of_points=8)
    p2.SetPoint(0, 0, 0, 0)
    p2.SetPoint(1, 0, 255, 0)
    p2.SetPoint(2, 255, 0, 0)
    p2.SetPoint(3, 255, 255, 0)
    p2.SetPoint(4, 96, 159, 0)
    p2.SetPoint(5, 159, 159, 0)
    p2.SetPoint(6, 159, 96, 0)
    p2.SetPoint(7, 96, 96, 0)

    transform = vtkThinPlateSplineTransform(source_landmarks=p2, target_landmarks=p1)
    transform.SetBasisToR2LogR()
    # You must invert the transform before passing it to vtkImageReslice.
    transform.Inverse()

    reslice = vtkImageReslice(reslice_transform=transform)

    reslice.SetInterpolationModeToLinear()
    mapper = vtkImageMapper(color_window=255.0, color_level=127.5, z_slice=0)
    blend >> reslice >> mapper
    act = vtkActor2D(mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    renderer.AddActor(act)

    # No background is visible because the window size matches the data extent.
    window = vtkRenderWindow(size=(data_extent[1], data_extent[3]), window_name='ThinPlateSplineTransform')

    window.AddRenderer(renderer)
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = window
    style = vtkInteractorStyleTerrain()
    interactor.interactor_style = style
    window.Render()
    interactor.Initialize()
    interactor.Start()

if __name__ == '__main__':
    main()
```
