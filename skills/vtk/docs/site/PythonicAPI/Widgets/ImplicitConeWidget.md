<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/ImplicitConeWidget/ -->

# ImplicitConeWidget

Repository source: [ImplicitConeWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/ImplicitConeWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImplicitConeWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImplicitConeWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/ImplicitConeWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImplicitConeWidget.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingUI
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkCommand
from vtkmodules.vtkCommonDataModel import vtkCone
from vtkmodules.vtkFiltersCore import (
    vtkAppendPolyData,
    vtkGlyph3D,
    vtkClipPolyData
)
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkSphereSource
)
from vtkmodules.vtkInteractionWidgets import (
    vtkImplicitConeRepresentation,
    vtkImplicitConeWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()
    colors.SetColor('ParaViewBkg', 82, 87, 110, 255)

    ren = vtkRenderer(background=colors.GetColor3d("ParaViewBkg"))
    ren_win = vtkRenderWindow(size=(640, 640), window_name='ImplicitConeWidget', multi_samples=0)
    ren_win.SetWindowName('ImplicitConeWidget')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we always import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    # Create a mace out of filters.
    sphere = vtkSphereSource()
    cone_source = vtkConeSource()
    glyph = vtkGlyph3D(source_data=cone_source.update().output, scale_factor=0.25,
                       vector_mode=Glyph3D.VectorMode.VTK_USE_NORMAL,
                       scale_mode=Glyph3D.ScaleMode.VTK_SCALE_BY_VECTOR
                       )
    sphere >> glyph

    # The sphere and spikes are appended into a single polydata.
    # This just makes things simpler to manage.
    apd = vtkAppendPolyData()
    (glyph, sphere) >> apd

    mace_mapper = vtkPolyDataMapper()
    apd >> mace_mapper

    mace_actor = vtkActor(mapper=mace_mapper, visibility=True)
    mace_actor.property.color = colors.GetColor3d("LightSteelBlue")

    # This portion of the code clips the mace with the vtkCone's
    # implicit function. The clipped region is colored green.
    cone = vtkCone(is_double_cone=False)

    clipper = vtkClipPolyData(clip_function=cone, inside_out=True)

    select_mapper = vtkPolyDataMapper()
    apd >> clipper >> select_mapper

    select_actor = vtkActor(mapper=select_mapper, scale=(1.01, 1.01, 1.01), visibility=False)
    select_actor.property.color = colors.GetColor3d("Lime")

    # The SetInteractor method is how 3D widgets are associated with the render
    # window interactor. Internally, SetInteractor sets up a bunch of callbacks
    # using the Command/Observer mechanism (AddObserver()).
    myCallback = TICWCallback(cone, select_actor)

    rep = vtkImplicitConeRepresentation(place_factor=1.25)
    rep.PlaceWidget(glyph.update().output.bounds)

    cone_widget = vtkImplicitConeWidget(interactor=iren, representation=rep, enabled=True)
    cone_widget.AddObserver(vtkCommand.InteractionEvent, myCallback)

    ren.AddActor(mace_actor)
    ren.AddActor(select_actor)

    iren.Initialize()
    ren.ResetCamera()
    ren.active_camera.Elevation(30)
    ren.active_camera.Azimuth(30)
    ren.active_camera.SetRoll(-22.5)
    ren.ResetCamera()
    ren.active_camera.Zoom(0.65)

    iren.Start()

class TICWCallback:
    def __init__(self, cone, actor):
        self.cone = cone
        self.actor = actor

    def __call__(self, caller, ev):
        rep = caller.representation
        rep.GetCone(self.cone)
        self.actor.visibility = True

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
