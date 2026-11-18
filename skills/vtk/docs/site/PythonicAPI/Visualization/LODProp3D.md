<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/LODProp3D/ -->

# LODProp3D

Repository source: [LODProp3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/LODProp3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLODProp3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLODProp3D.png?raw=true target=)

### Description

If you have a fast graphics card, you may not see a difference.

Use fullscreen and spin the object.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/LODProp3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LODProp3D.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkSphereSource,
)
from vtkmodules.vtkRenderingCore import (
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor, vtkLODProp3D
)

def main():
    colors = vtkNamedColors()

    # High-res sphere.
    res = 100
    high_res_mapper = vtkPolyDataMapper()
    vtkSphereSource(theta_resolution=res, phi_resolution=res) >> high_res_mapper

    # Low res sphere.
    low_res_mapper = vtkPolyDataMapper()
    vtkSphereSource() >> low_res_mapper

    property_low_res = vtkProperty(diffuse_color=colors.GetColor3d('BlanchedAlmond'),
                                   interpolation=Property.Interpolation.VTK_FLAT)
    property_high_res = vtkProperty(diffuse_color=colors.GetColor3d('MistyRose'),
                                    interpolation=Property.Interpolation.VTK_FLAT)

    prop = vtkLODProp3D(automatic_lod_selection=True)
    prop.AddLOD(low_res_mapper, property_low_res, 0.0)
    prop.AddLOD(high_res_mapper, property_high_res, 0.0)
    print(f'There are {prop.GetNumberOfLODs()} LODs')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='LODProp3D')
    render_window.AddRenderer(renderer)
    # prop.SetAllocatedRenderTime(1.0e-6,renderer)
    prop.SetAllocatedRenderTime(1.0e-12, renderer)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(prop)

    render_window.Render()

    #  Decide what approach to use.
    use_function_callback = True
    if use_function_callback:
        refresh_callback.prop = prop
        # Register the callback with the object that it is observing.
        render_window.AddObserver('ModifiedEvent', refresh_callback)
    else:
        render_window.AddObserver('ModifiedEvent', RefreshObserver(prop))
        # Or:
        # observer = RefreshObserver(prop)
        # render_window.AddObserver('ModifiedEvent',observer)

    # Begin mouse interaction.
    render_window_interactor.Start()

def refresh_callback(caller, event):
    """
    We must do this before we register the callback in the calling function:
       refresh_callback.prop = prop

    :param caller:
    :param event:
    :return:
    """
    print(f'Last rendered LOD ID: {refresh_callback.prop.last_rendered_lodid}')

class RefreshObserver:
    """
    The alternative approach using a class.
    """

    def __init__(self, prop):
        self.prop = prop

    def __call__(self, caller, ev):
        print(f'Last rendered LOD ID: {self.prop.last_rendered_lodid}')

@dataclass(frozen=True)
class Property:
    @dataclass(frozen=True)
    class Interpolation:
        VTK_FLAT: int = 0
        VTK_GOURAUD: int = 1
        VTK_PHONG: int = 2
        VTK_PBR: int = 3

    @dataclass(frozen=True)
    class Representation:
        VTK_POINTS: int = 0
        VTK_WIREFRAME: int = 1
        VTK_SURFACE: int = 2

if __name__ == '__main__':
    main()
```
