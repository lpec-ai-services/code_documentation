<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/TableBasedClipDataSetWithPolyData2/ -->

# TableBasedClipDataSetWithPolyData2

Repository source: [TableBasedClipDataSetWithPolyData2](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/TableBasedClipDataSetWithPolyData2.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestTableBasedClipDataSetWithPolyData2.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestTableBasedClipDataSetWithPolyData2.png?raw=true target=)

### Description

The example that shows how to use the [vtkTableBasedClipDataSet](https://www.vtk.org/doc/nightly/html/classvtkTableBasedClipDataSet.html) to clip a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html) that contains a checkerboard pattern.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/TableBasedClipDataSetWithPolyData2/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TableBasedClipDataSetWithPolyData2.py**

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
    vtkPlanes,
    vtkRectilinearGrid
)
from vtkmodules.vtkFiltersGeneral import vtkTableBasedClipDataSet
from vtkmodules.vtkImagingCore import vtkImageMapToColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def main():
    # The number of checkerboard squares on a side.
    image_size = 64

    # Offsets for clipping planes with normals in the X and Y directions.
    x_offset = 8
    y_offset = 8

    colors = vtkNamedColors()

    renderer = vtkRenderer(background=colors.GetColor3d('Wheat'), use_hidden_line_removal=True)

    render_window = vtkRenderWindow(size=(640, 480), window_name='TableBasedClipDataSetWithPolyData2')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    interactor.interactor_style.SetCurrentStyleToTrackballCamera()
    interactor.render_window = render_window

    image = make_image(image_size)

    # Clipping planes in the X and Y direction.
    normals = vtkDoubleArray()
    clip_pts = vtkPoints()
    normals.SetNumberOfComponents(3)
    xnorm = [-1.0, 0.0, 0.0]
    ynorm = [0.0, -1.0, 0.0]
    xpt = [x_offset, 0.0, 0.0]
    ypt = [0.0, y_offset, 0.0]
    normals.InsertNextTuple(xnorm)
    normals.InsertNextTuple(ynorm)
    clip_pts.InsertNextPoint(xpt)
    clip_pts.InsertNextPoint(ypt)
    clip_planes = vtkPlanes(normals=normals, points=clip_pts)

    clipper = vtkTableBasedClipDataSet(clip_function=clip_planes, input_data=image)

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
def make_image(n):
    cube_size = 20.0  # physical linear dimension of entire system.

    # This is a simplification of a program that uses actual image data
    # as a source for the rectilinear grid.  In order to recreate the
    # same vtk calls, create a dummy image here.

    image0 = vtkImageData()
    image0.SetDimensions(n, n, n)
    image0.AllocateScalars(VTK_UNSIGNED_CHAR, 1)
    image0.SetSpacing(cube_size / n, cube_size / n, cube_size / n)
    checker_size = n // 8
    scalars = vtkUnsignedCharArray()
    for z in range(0, n):
        for y in range(0, n):
            for x in range(0, n):
                v = (x // checker_size + y // checker_size + z // checker_size) % 2
                scalars.InsertNextValue(v)
    image0.GetPointData().SetScalars(scalars)

    colors = vtkNamedColors()

    lut = vtkLookupTable(number_of_table_values=2, table_range=(0, 1))
    lut.Build()
    lut.SetTableValue(0, colors.GetColor4d('Thistle'))
    lut.SetTableValue(1, colors.GetColor4d('DarkSlateBlue'))

    map_colors = vtkImageMapToColors()
    map_colors.SetLookupTable(lut)
    map_colors.SetOutputFormatToRGBA()
    map_colors.SetInputData(image0)
    map_colors.update()

    image = map_colors.output

    extent = list(image.GetExtent())
    for i in range(1, len(extent), 2):
        extent[i] += 1

    rect_grid = vtkRectilinearGrid(extent=extent)

    xcoords = vtkDoubleArray()
    ycoords = vtkDoubleArray()
    zcoords = vtkDoubleArray()
    xcoords.SetNumberOfValues(n + 1)
    ycoords.SetNumberOfValues(n + 1)
    zcoords.SetNumberOfValues(n + 1)

    spacing = image.GetSpacing()
    for i in range(0, n + 1):
        xcoords.InsertValue(i, i * spacing[0])
        ycoords.InsertValue(i, i * spacing[1])
        zcoords.InsertValue(i, i * spacing[2])

    rect_grid.SetXCoordinates(xcoords)
    rect_grid.SetYCoordinates(ycoords)
    rect_grid.SetZCoordinates(zcoords)

    point_data = image.GetPointData()
    cell_data = rect_grid.GetCellData()
    cell_data.ShallowCopy(point_data)
    return rect_grid

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
