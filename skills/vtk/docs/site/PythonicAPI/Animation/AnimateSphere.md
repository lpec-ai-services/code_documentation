<!-- source: https://examples.vtk.org/site/PythonicAPI/Animation/AnimateSphere/ -->

# AnimateSphere

Repository source: [AnimateSphere](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Animation/AnimateSphere.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Animation/TestAnimateSphere.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Animation/TestAnimateSphere.png?raw=true target=)

### Description

Animate a sphere by opening it to an angle of 90°. The edge of the opened sphere is colored red.

This example was inspired by this discussion: [How to get a Python version of the User Guide vtkAnimationScene example running?](https://discourse.vtk.org/t/how-to-get-a-python-version-of-the-user-guide-vtkanimationscene-example-running/11440/).

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AnimateSphere.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkAnimationCue
)
from vtkmodules.vtkCommonDataModel import vtkAnimationScene
from vtkmodules.vtkFiltersCore import vtkFeatureEdges
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
)

def get_program_parameters():
    import argparse
    description = 'Animate Sphere.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-r', '--real_time', action='store_true',
                        help='Sets the scene mode to real time instead of the default sequence mode.')
    args = parser.parse_args()
    return args.real_time

def main():
    scene_mode = get_program_parameters()

    colors = vtkNamedColors()
    sphere_color = colors.GetColor3d('Gold')
    background_color = colors.GetColor3d('DarkSlateBlue')
    backface_color = colors.GetColor3d('DarkSlateGray')

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=background_color)
    ren_win = vtkRenderWindow(window_name='AnimateSphere')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    scene = vtkAnimationScene(loop=0, frame_rate=30, start_time=0, end_time=10)
    if scene_mode:
        scene.SetModeToRealTime()
        print('real-time mode')
    else:
        scene.SetModeToSequence()
        print('sequence mode')

    cue = vtkAnimationCue(start_time=0, end_time=1.0)
    cue.SetTimeModeToNormalized()

    sphere_backface_property = vtkProperty(color=backface_color)
    sphere_property = vtkProperty(color=sphere_color, diffuse=0.8, specular=0.3, specular_power=30.0)

    # Create a sphere.
    sphere = vtkSphereSource(phi_resolution=31, theta_resolution=31)
    mapper = vtkPolyDataMapper()
    sphere >> mapper
    actor = vtkActor(mapper=mapper, property=sphere_property, backface_property=sphere_backface_property)

    feature_edges = vtkFeatureEdges(boundary_edges=True, feature_edges=False, manifold_edges=False,
                                    non_manifold_edges=False,
                                    coloring=True)

    edge_mapper = vtkPolyDataMapper()
    sphere >> feature_edges >> edge_mapper
    edge_actor = vtkActor(mapper=edge_mapper)

    ren.AddActor(actor)
    ren.AddActor(edge_actor)

    sphere_animator = SphereAnimator(ren_win, sphere)
    cue.AddObserver('AnimationCueTickEvent', sphere_animator)

    scene.AddCue(cue)

    ren_win.Render()
    ren.active_camera.Yaw(45)
    ren.active_camera.Pitch(-15)
    ren.ResetCamera()
    iren.Initialize()

    scene.Play()
    scene.Stop()

    iren.Start()

class SphereAnimator:
    def __init__(self, ren_win, sphere):
        self.ren_win = ren_win
        self.sphere = sphere

    def __call__(self, obj, event):
        new_st = obj.animation_time * 90
        self.sphere.start_theta = new_st
        self.ren_win.Render()

if __name__ == '__main__':
    main()
```
