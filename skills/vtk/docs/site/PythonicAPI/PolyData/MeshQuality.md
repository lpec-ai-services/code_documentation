<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/MeshQuality/ -->

# MeshQuality

Repository source: [MeshQuality](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/MeshQuality.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestMeshQuality.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestMeshQuality.png?raw=true target=)

### Description

This example uses one of many selectable methods to determine the quality of a mesh. In this case, we have selected to use the area of the triangles. We show how to retrieve the quality metric computed on each triangle after the process is completed.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/MeshQuality/)), ([Java](https://examples.vtk.org/site/Java/PolyData/MeshQuality/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MeshQuality.py**

```python
# !/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import vtkTriangleFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkFiltersVerdict import vtkMeshQuality
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    triangle_filter = vtkTriangleFilter()
    sphere_source >> triangle_filter
    triangle_filter.update()

    mesh = triangle_filter.output
    print(f'There are {mesh.number_of_cells} cells.')

    quality_filter = vtkMeshQuality(input_data=mesh)
    quality_filter.SetTriangleQualityMeasureToArea()
    quality_filter.update()

    quality_array = quality_filter.output.GetCellData().GetArray('Quality')
    print(f'There are {quality_array.number_of_tuples} values.')

    for i in range(0, quality_array.number_of_tuples):
        print(f'value  {i:2d} : {quality_array.GetValue(i):0.6f}')

    polydata = vtkPolyData()
    polydata.ShallowCopy(quality_filter.output)
    scalar_range = polydata.scalar_range

    # Visualize
    lut = make_lut()
    lut.SetTableRange(scalar_range)
    lut.IndexedLookup = False

    mapper = vtkPolyDataMapper(input_data=polydata, scalar_range=scalar_range, lookup_table=lut)
    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='MeshQuality')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    render_window.Render()
    render_window_interactor.Start()

def make_lut():
    """
    Make the lookup table.

    :return: The lookup table.
    """
    color_series = vtkColorSeries()

    # Select a color scheme.
    color_series_enum = color_series.BREWER_DIVERGING_BROWN_BLUE_GREEN_9
    # color_series_enum = color_series.BREWER_DIVERGING_SPECTRAL_10
    # color_series_enum = color_series.BREWER_DIVERGING_SPECTRAL_3
    # color_series_enum = color_series.BREWER_DIVERGING_PURPLE_ORANGE_9
    # color_series_enum = color_series.BREWER_SEQUENTIAL_BLUE_PURPLE_9
    # color_series_enum = color_series.BREWER_SEQUENTIAL_BLUE_GREEN_9
    # color_series_enum = color_series.BREWER_QUALITATIVE_SET3
    # color_series_enum = color_series.CITRUS

    lut = vtkLookupTable(scale=LookupTable.Scale.VTK_SCALE_LINEAR)
    color_series.color_scheme = color_series_enum
    color_series.BuildLookupTable(lut, color_series.ORDINAL)
    lut.SetNanColor(1, 0, 0, 1)

    return lut

@dataclass(frozen=True)
class LookupTable:
    @dataclass(frozen=True)
    class Scale:
        VTK_SCALE_LINEAR: int = 0
        VTK_SCALE_LOG10: int = 1

if __name__ == '__main__':
    main()
```
