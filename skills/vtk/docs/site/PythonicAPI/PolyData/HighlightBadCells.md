<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/HighlightBadCells/ -->

# HighlightBadCells

Repository source: [HighlightBadCells](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/HighlightBadCells.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestHighlightBadCells.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestHighlightBadCells.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/HighlightBadCells/)), ([CSharp](https://examples.vtk.org/site/CSharp/PolyData/HighlightBadCells/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**HighlightBadCells.py**

```python
# !/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkDataObject,
    vtkDataSetAttributes
)
from vtkmodules.vtkFiltersCore import (
    vtkThreshold,
    vtkTriangleFilter
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkFiltersVerdict import vtkMeshQuality
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

LOWER_THRESHOLD = 0.02

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    triangle_filter = vtkTriangleFilter()
    sphere_source >> triangle_filter
    triangle_filter.Update()
    # Create a mapper and actor.
    sphere_mapper = vtkDataSetMapper()
    sphere_source >> triangle_filter >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.color = colors.GetColor3d('MistyRose')

    mesh = triangle_filter.update().output
    print(f'There are {mesh.number_of_cells} cells.')

    quality_filter = vtkMeshQuality(input_data=mesh)
    quality_filter.SetTriangleQualityMeasureToArea()

    quality_mesh = quality_filter.update().output

    quality_array = quality_mesh.GetCellData().GetArray('Quality')
    print(f'There are {quality_array.number_of_tuples} values.')

    for i in range(0, quality_array.number_of_tuples):
        print(f'value  {i:2d} : {quality_array.GetValue(i):0.6f}')

    select_cells = vtkThreshold(lower_threshold=LOWER_THRESHOLD, input_data=quality_mesh)
    select_cells.SetThresholdFunction(vtkThreshold.THRESHOLD_LOWER)
    select_cells.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_CELLS, vtkDataSetAttributes.SCALARS)
    select_cells.update()
    bad_values = dict()
    for i in range(0, quality_array.number_of_tuples):
        val = quality_array.GetValue(i)
        if val <= LOWER_THRESHOLD:
            bad_values[i] = val
    print(f'Number of values <= {LOWER_THRESHOLD} : {len(bad_values)}')
    for k, v in bad_values.items():
        print(f'value {k} : {v:0.6f}')

    ug = select_cells.output

    # Create a mapper and actor.
    mapper = vtkDataSetMapper(input_data=ug)
    actor = vtkActor(mapper=mapper)
    actor.property.SetRepresentationToWireframe()
    actor.property.line_width = 5
    actor.property.color = colors.GetColor3d('Red')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='HighlightBadCells')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(actor)
    renderer.AddActor(sphere_actor)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
