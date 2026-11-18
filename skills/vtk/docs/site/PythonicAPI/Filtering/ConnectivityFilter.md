<!-- source: https://examples.vtk.org/site/PythonicAPI/Filtering/ConnectivityFilter/ -->

# ConnectivityFilter

Repository source: [ConnectivityFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Filtering/ConnectivityFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestConnectivityFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestConnectivityFilter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/ConnectivityFilter/)), ([Python](../../Python/Filtering/ConnectivityFilter.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ConnectivityFilter.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import (
    vtkAppendFilter,
    vtkConnectivityFilter,
    vtkDelaunay3D
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    append_filter = vtkAppendFilter()
    vtkSphereSource() >> vtkDelaunay3D() >> append_filter
    vtkSphereSource(center=(5, 0, 0)) >> vtkDelaunay3D() >> append_filter

    connectivity_filter = vtkConnectivityFilter(
        color_regions=True,
        extraction_mode=ConnectivityFilter.ExtractionMode.VTK_EXTRACT_ALL_REGIONS
    )

    # Visualize
    mapper = vtkDataSetMapper()
    append_filter >> connectivity_filter >> mapper

    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('deep_ochre'))
    renderer.AddActor(actor)

    ren_window = vtkRenderWindow(window_name='ConnectivityFilter')
    ren_window.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_window

    ren_window.Render()
    renderer.active_camera.Zoom(0.9)
    ren_window.Render()
    iren.Start()

@dataclass(frozen=True)
class ConnectivityFilter:
    @dataclass(frozen=True)
    class ExtractionMode:
        VTK_EXTRACT_POINT_SEEDED_REGIONS: int = 1
        VTK_EXTRACT_CELL_SEEDED_REGIONS: int = 2
        VTK_EXTRACT_SPECIFIED_REGIONS: int = 3
        VTK_EXTRACT_LARGEST_REGION: int = 4
        VTK_EXTRACT_ALL_REGIONS: int = 5
        VTK_EXTRACT_CLOSEST_POINT_REGION: int = 6

if __name__ == '__main__':
    main()
```
