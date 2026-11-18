<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageData/ClipVolume/ -->

# ClipVolume

Repository source: [ClipVolume](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageData/ClipVolume.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestClipVolume.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestClipVolume.png?raw=true target=)

### Description

This example shows how to use [vtkClipVolume](https://www.vtk.org/doc/nightly/html/classvtkClipVolume.html) and subclasses of [vtkImplicitFunction](https://www.vtk.org/doc/nightly/html/classvtkImplicitFunction.html), producing a [vtkUnstructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html). The output consists of [vtkTetra](https://www.vtk.org/doc/nightly/html/classvtkTetra.html) or other 3D cell types.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageData/ClipVolume/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ClipVolume.py**

```python
# !/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_UNSIGNED_CHAR,
    vtkDoubleArray,
    vtkLookupTable,
    vtkPoints,
    vtkUnsignedCharArray
)
from vtkmodules.vtkCommonDataModel import (
    vtkImageData,
    vtkPlanes
)
from vtkmodules.vtkFiltersGeneral import vtkClipVolume
from vtkmodules.vtkImagingCore import vtkImageMapToColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

IMAGESIZE = 64  # number of checkerboard squares on a side.
CUBESIZE = 20.0  # physical linear dimension of entire system.

# Color for the checkerboard image.
DIM = 0.5  # THe amount to dim the dark squares by.

# Offsets for clipping planes with normals in the X and Y directions.
XOFFSET = 8
YOFFSET = 8

def main():
    # Define the colors.
    colors = vtkNamedColors()
    background_color = colors.GetColor3d('Wheat')
    checker_color = colors.GetColor4d('Tomato')
    fill_color = colors.GetColor4d('Banana')

    renderer = vtkRenderer(background=background_color)

    render_window = vtkRenderWindow(size=(640, 480), window_name='ClipVolume')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    interactor.interactor_style.SetCurrentStyleToTrackballCamera()
    interactor.render_window = render_window

    image = make_image(IMAGESIZE, fill_color, checker_color)

    # Clipping planes in the X and Y direction.
    normals = vtkDoubleArray()
    clip_pts = vtkPoints()
    normals.SetNumberOfComponents(3)
    xnorm = [-1., 0., 0.]
    ynorm = [0., -1., 0.]
    xpt = [XOFFSET, 0., 0.]
    ypt = [0., YOFFSET, 0.]
    normals.InsertNextTuple(xnorm)
    normals.InsertNextTuple(ynorm)
    clip_pts.InsertNextPoint(xpt)
    clip_pts.InsertNextPoint(ypt)
    clip_planes = vtkPlanes(normals=normals, points=clip_pts)

    clipper = vtkClipVolume(clip_function=clip_planes, input_data=image)

    image_mapper = vtkDataSetMapper(
        resolve_coincident_topology=Mapper.ResolveCoincidentTopology.VTK_RESOLVE_POLYGON_OFFSET)
    clipper >> image_mapper
    image_actor = vtkActor(mapper=image_mapper)
    renderer.AddViewProp(image_actor)

    renderer.ResetCamera()
    renderer.active_camera.Azimuth(120)
    renderer.active_camera.Elevation(30)
    renderer.ResetCameraClippingRange()
    render_window.Render()

    interactor.Start()

# Make the image data. A checkerboard pattern is used for simplicity.
def make_image(n, fill_color, checker_color):
    image0 = vtkImageData()
    image0.SetDimensions(n, n, n)
    image0.AllocateScalars(VTK_UNSIGNED_CHAR, 1)
    image0.SetSpacing(CUBESIZE / n, CUBESIZE / n, CUBESIZE / n)
    checkerSize = n // 8
    scalars = vtkUnsignedCharArray()
    for z in range(0, n):
        for y in range(0, n):
            for x in range(0, n):
                v = (x // checkerSize + y // checkerSize + z // checkerSize) % 2
                scalars.InsertNextValue(v)
    image0.GetPointData().SetScalars(scalars)

    lut = vtkLookupTable(number_of_table_values=2, table_range=(0, 1))
    lut.Build()
    lut.SetTableValue(0, fill_color)
    lut.SetTableValue(1, checker_color)

    map_colors = vtkImageMapToColors()
    map_colors.SetLookupTable(lut)
    map_colors.SetOutputFormatToRGBA()
    map_colors.SetInputData(image0)
    map_colors.update()

    return map_colors.output

@dataclass(frozen=True)
class Mapper:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_MODE_DEFAULT: int = 0
        VTK_COLOR_MODE_MAP_SCALARS: int = 1
        VTK_COLOR_MODE_DIRECT_SCALARS: int = 2

    @dataclass(frozen=True)
    class ResolveCoincidentTopology:
        VTK_RESOLVE_OFF: int = 0
        VTK_RESOLVE_POLYGON_OFFSET: int = 1
        VTK_RESOLVE_SHIFT_ZBUFFER: int = 2

    @dataclass(frozen=True)
    class ScalarMode:
        VTK_SCALAR_MODE_DEFAULT: int = 0
        VTK_SCALAR_MODE_USE_POINT_DATA: int = 1
        VTK_SCALAR_MODE_USE_CELL_DATA: int = 2
        VTK_SCALAR_MODE_USE_POINT_FIELD_DATA: int = 3
        VTK_SCALAR_MODE_USE_CELL_FIELD_DATA: int = 4
        VTK_SCALAR_MODE_USE_FIELD_DATA: int = 5

if __name__ == '__main__':
    main()
```
