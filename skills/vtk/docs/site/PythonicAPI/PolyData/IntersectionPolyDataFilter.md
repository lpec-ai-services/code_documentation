<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/IntersectionPolyDataFilter/ -->

# IntersectionPolyDataFilter

Repository source: [IntersectionPolyDataFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/IntersectionPolyDataFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestIntersectionPolyDataFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestIntersectionPolyDataFilter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/IntersectionPolyDataFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IntersectionPolyDataFilter.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeneral import vtkIntersectionPolyDataFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    sphere_source1 = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=2.0)
    sphere1_mapper = vtkPolyDataMapper(scalar_visibility=False)
    sphere_source1 >> sphere1_mapper
    sphere1_actor = vtkActor(mapper=sphere1_mapper)
    sphere1_actor.property.opacity = 0.3
    sphere1_actor.property.color = colors.GetColor3d('Red')

    sphere_source2 = vtkSphereSource(center=(1.0, 0.0, 0.0), radius=2.0)
    sphere2_mapper = vtkPolyDataMapper(scalar_visibility=False)
    sphere_source2 >> sphere2_mapper
    sphere2_actor = vtkActor(mapper=sphere2_mapper)
    sphere2_actor.property.opacity = 0.3
    sphere2_actor.property.color = colors.GetColor3d('Lime')

    intersection_poly_data_filter = vtkIntersectionPolyDataFilter()
    sphere_source1 >> select_ports(0, intersection_poly_data_filter)
    sphere_source2 >> select_ports(1, intersection_poly_data_filter)
    intersection_poly_data_filter.update()

    intersection_mapper = vtkPolyDataMapper(scalar_visibility=False)
    intersection_poly_data_filter >> intersection_mapper
    intersection_actor = vtkActor(mapper=intersection_mapper)
    intersection_actor.property.color = colors.GetColor3d('White')

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='IntersectionPolyDataFilter')
    render_window.AddRenderer(renderer)
    ren_win_interactor = vtkRenderWindowInteractor()
    ren_win_interactor.render_window = render_window

    renderer.AddViewProp(sphere1_actor)
    renderer.AddViewProp(sphere2_actor)
    renderer.AddViewProp(intersection_actor)

    render_window.Render()
    ren_win_interactor.Start()

if __name__ == '__main__':
    main()
```
