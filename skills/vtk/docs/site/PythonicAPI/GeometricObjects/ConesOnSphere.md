<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/ConesOnSphere/ -->

# ConesOnSphere

Repository source: [ConesOnSphere](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/ConesOnSphere.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestConesOnSphere.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestConesOnSphere.png?raw=true target=)

### Description

Generate a sphere and position a cone at the center of each cell on the sphere, aligned with the face normal.

Taken from [VTK 9.4: A Step Closer to the Ways of Python](https://www.kitware.com/vtk-9-4-a-step-closer-to-the-ways-of-python/)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/ConesOnSphere/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ConesOnSphere.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import (
    vtkCellCenters,
    vtkGlyph3D,
    vtkPolyDataNormals
)
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkSphereSource
)
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()
    colors.SetColor("ParaViewBkg", 82, 87, 110, 255)

    sphere_source = vtkSphereSource(
        radius=0.5,
        theta_resolution=16,
        phi_resolution=16,
        lat_long_tessellation=False
    )

    cone_source = vtkConeSource(
        radius=0.08,
        height=0.03,
        resolution=30,
    )

    glyph_filter = vtkGlyph3D(
        source_connection=cone_source.output_port,
        orient=True,
        vector_mode=Glyph3D.VectorMode.VTK_USE_NORMAL,  # normals
    )

    pipeline = (
            sphere_source
            >> vtkPolyDataNormals(compute_cell_normals=1)
            >> vtkCellCenters()
            >> glyph_filter
    )

    mapper = vtkPolyDataMapper()
    pipeline >> mapper

    actor_prop = vtkProperty(color=colors.GetColor3d('Peru'), edge_color=colors.GetColor3d('DarkSlateBlue'),
                             edge_visibility=False)
    actor = vtkActor(property=actor_prop, mapper=mapper)

    renderer = vtkRenderer(background=colors.GetColor3d('ParaViewBkg'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='ConesOnSphere')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    render_window_interactor.interactor_style.SetCurrentStyleToTrackballCamera()

    renderer.AddActor(actor)

    cow = vtkCameraOrientationWidget(parent_renderer=renderer,
                                     interactor=render_window_interactor)
    # Enable the widget.
    cow.On()

    render_window.Render()
    render_window_interactor.Start()

@dataclass(frozen=True)
class Glyph3D:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_BY_SCALE: int = 0
        VTK_COLOR_BY_SCALAR: int = 1
        VTK_COLOR_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class IndexMode:
        VTK_INDEXING_OFF: int = 0
        VTK_INDEXING_BY_SCALAR: int = 1
        VTK_INDEXING_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class ScaleMode:
        VTK_SCALE_BY_SCALAR: int = 0
        VTK_SCALE_BY_VECTOR: int = 1
        VTK_SCALE_BY_VECTORCOMPONENTS: int = 2
        VTK_DATA_SCALING_OFF: int = 3

    @dataclass(frozen=True)
    class VectorMode:
        VTK_USE_VECTOR: int = 0
        VTK_USE_NORMAL: int = 1
        VTK_VECTOR_ROTATION_OFF: int = 2
        VTK_FOLLOW_CAMERA_DIRECTION: int = 3

if __name__ == '__main__':
    main()
```
