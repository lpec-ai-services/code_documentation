<!-- source: https://examples.vtk.org/site/PythonicAPI/VolumeRendering/MultiBlockVolumeMapper/ -->

# MultiBlockVolumeMapper

Repository source: [MultiBlockVolumeMapper](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VolumeRendering/MultiBlockVolumeMapper.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestMultiBlockVolumeMapper.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VolumeRendering/TestMultiBlockVolumeMapper.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VolumeRendering/MultiBlockVolumeMapper/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MultiBlockVolumeMapper.py**

```python
# !/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtkmodules.vtkCommonCore import VTK_UNSIGNED_CHAR
from vtkmodules.vtkCommonDataModel import (
    vtkImageData,
    vtkMultiBlockDataSet
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkVolume,
    vtkVolumeProperty
)
from vtkmodules.vtkRenderingVolumeOpenGL2 import vtkMultiBlockVolumeMapper

def main():
    named_colors = vtkNamedColors()

    # Set up vtkMultiBlockDataSet (just a bunch of colored blocks):
    dim = (10, 10, 10)
    spc = (0.1, 0.1, 0.1)
    mb = vtkMultiBlockDataSet()
    colors = vtkColorSeries()
    colors.SetColorScheme(vtkColorSeries.BREWER_QUALITATIVE_SET3)
    for i in range(0, 8):
        img = vtkImageData(dimensions=dim, spacing=spc)
        img.AllocateScalars(VTK_UNSIGNED_CHAR, 4)
        # Position the volumes by their origin:
        # Shift object by the length of a volume in the axis
        #  directions to make them non-overlapping:
        # ofs = (i % 2, (i / 2) % 2,  i / 4 )
        ofs = (i % 2, (i // 2) % 2, i // 4)
        # print(ofs)
        img.origin = (
            ofs[0] * (dim[0] - 1) * spc[0],
            ofs[1] * (dim[1] - 1) * spc[1],
            ofs[2] * (dim[2] - 1) * spc[2]
        )
        # Set colors:
        col = colors.GetColor(i)
        for x in range(0, dim[0]):
            for y in range(0, dim[1]):
                for z in range(0, dim[2]):
                    for c in range(0, 3):
                        img.SetScalarComponentFromDouble(x, y, z, c, col[c])
                    img.SetScalarComponentFromDouble(x, y, z, 3, 255)
        mb.SetBlock(i, img)

    # Setting up the vtkMultiBlockVolumeMapper:
    vol_mapper = vtkMultiBlockVolumeMapper(input_data_object=mb)
    vol_prop = vtkVolumeProperty(independent_components=False)
    volume = vtkVolume(mapper=vol_mapper, property=vol_prop, visibility=True)
    # volume.orientation = (30, -45, 0)

    # An outline provides context around the data.
    outline_data = vtkOutlineFilter(input_data=mb)
    outline_data.SetInputData(mb)
    map_outline = vtkPolyDataMapper()
    outline_data >> map_outline
    outline = vtkActor(mapper=map_outline)
    # outline.orientation = (30, -45, 0)
    outline.property.color = named_colors.GetColor3d('Black')

    # Standard render window, renderer and interactor setup:
    renderer = vtkRenderer(background=named_colors.GetColor3d('ForestGreen'))
    ren_win = vtkRenderWindow(window_name='MultiBlockVolumeMapper')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    renderer.AddVolume(volume)
    renderer.AddActor(outline)

    ren_win.Render()
    camera = renderer.active_camera
    camera.Elevation(30)
    camera.Azimuth(45)
    renderer.ResetCamera()

    iren.Start()

if __name__ == '__main__':
    main()
```
