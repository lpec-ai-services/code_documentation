<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/CubeAxesActor2D/ -->

# CubeAxesActor2D

Repository source: [CubeAxesActor2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/CubeAxesActor2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCubeAxesActor2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCubeAxesActor2D.png?raw=true target=)

### Description

The [vtkCubeAxesActor2D](https://www.vtk.org/doc/nightly/html/classvtkCubeAxesActor2D.html) draws axes on the bounding box of the data set and labels the axes with x-y-z coordinates.

Seealso

[BoundingBox](../Utilities/BoundingBox.md) and [Outline](../PolyData/Outline.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/CubeAxesActor2D/)), ([Java](https://examples.vtk.org/site/Java/Visualization/CubeAxesActor2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CubeAxesActor2D.py**

```python
#!/usr/bin/env python3

"""
 The vtkCubeAxesActor2D draws axes on the bounding box of the data set and
 labels the axes with x-y-z coordinates.
"""

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkPolyDataNormals
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkFiltersSources import vtkPlatonicSolidSource
from vtkmodules.vtkRenderingAnnotation import vtkCubeAxesActor2D
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextProperty
)
from vtkmodules.vtkRenderingLOD import vtkLODActor

def main():
    colors = vtkNamedColors()

    icosahedron = vtkPlatonicSolidSource(solid_type=PlatonicSolidSource.SolidType.VTK_SOLID_ICOSAHEDRON)

    # Create a vtkPolyDataNormals filter to calculate the normals of the data set.
    normals = vtkPolyDataNormals()
    icosahedron >> normals

    # Set up the associated mapper and actor.
    icosahedron_mapper = vtkPolyDataMapper()
    icosahedron >> normals >> icosahedron_mapper
    icosahedron_mapper.ScalarVisibilityOff()

    icosahedron_actor = vtkLODActor(mapper=icosahedron_mapper)
    icosahedron_actor.property.color = colors.GetColor3d('Plum')

    # Create a vtkOutlineFilter to draw the bounding box of the data set.
    # Also create the associated mapper and actor.
    outline = vtkOutlineFilter()

    outline_mapper = vtkPolyDataMapper()
    normals >> outline >> outline_mapper

    outline_actor = vtkActor(mapper=outline_mapper)
    outline_actor.property.color = colors.GetColor3d('SeaGreen')
    outline_actor.property.line_width = 2

    # Create the renderers.  Assign them the appropriate viewport
    # coordinates, active camera, and light.
    ren1 = vtkRenderer(viewport=(0, 0, 0.5, 1.0), background=colors.GetColor3d('MidnightBlue'))

    ren2 = vtkRenderer(viewport=(0.5, 0, 1.0, 1.0), background=colors.GetColor3d('MidnightBlue'),
                       active_camera=ren1.active_camera)

    # Create the RenderWindow and RenderWindowInteractor.
    ren_win = vtkRenderWindow(size=(1200, 600), window_name='CubeAxesActor2D')
    ren_win.AddRenderer(ren1)
    ren_win.AddRenderer(ren2)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    # Add the actors to the renderer, and set the background.
    ren1.AddViewProp(icosahedron_actor)
    ren1.AddViewProp(outline_actor)
    ren2.AddViewProp(icosahedron_actor)
    ren2.AddViewProp(outline_actor)

    # Create a text property for both cube axes.
    tprop = vtkTextProperty(color=colors.GetColor3d('Yellow'), shadow=True, font_size=20)
    # Create a vtkCubeAxesActor2D. Use the outer edges of the bounding box to
    # draw the axes. Add the actor to the renderer.
    axes1 = vtkCubeAxesActor2D(view_prop=icosahedron_actor, camera=ren1.active_camera, label_format='%6.4g',
                               fly_mode=vtkCubeAxesActor2D.VTK_FLY_OUTER_EDGES,
                               axis_title_text_property=tprop, axis_label_text_property=tprop)
    axes1.property.line_width = 2
    ren1.AddViewProp(axes1)
    axes2 = vtkCubeAxesActor2D(view_prop=icosahedron_actor, camera=ren1.active_camera, label_format='%6.4g',
                               fly_mode=vtkCubeAxesActor2D.VTK_FLY_CLOSEST_TRIAD,
                               scaling=False, axis_title_text_property=tprop, axis_label_text_property=tprop)
    axes2.property.line_width = 2
    ren2.AddViewProp(axes2)

    ren1.ResetCamera()
    iren.Initialize()
    ren_win.Render()
    iren.Start()

@dataclass(frozen=True)
class PlatonicSolidSource:
    @dataclass(frozen=True)
    class SolidType:
        VTK_SOLID_TETRAHEDRON: int = 0
        VTK_SOLID_CUBE: int = 1
        VTK_SOLID_OCTAHEDRON: int = 2
        VTK_SOLID_ICOSAHEDRON: int = 3
        VTK_SOLID_DODECAHEDRON: int = 4

if __name__ == '__main__':
    main()
```
