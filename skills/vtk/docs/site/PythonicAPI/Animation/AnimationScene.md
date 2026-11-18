<!-- source: https://examples.vtk.org/site/PythonicAPI/Animation/AnimationScene/ -->

# AnimationScene

Repository source: [AnimationScene](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Animation/AnimationScene.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Animation/TestAnimationScene.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Animation/TestAnimationScene.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Animation/AnimationScene/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AnimationScene.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkAnimationCue
from vtkmodules.vtkCommonDataModel import vtkAnimationScene
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkProperty
)

def get_program_parameters():
    import argparse
    description = 'Animation Scene.'
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
    background_color = colors.GetColor3d('MistyRose')

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=background_color)
    ren_win = vtkRenderWindow(window_name='AnimateSphere')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    ren_win.Render()

    scene = vtkAnimationScene(loop=0, frame_rate=5, start_time=3, end_time=20)
    if scene_mode:
        scene.SetModeToRealTime()
        print('real-time mode')
    else:
        scene.SetModeToSequence()
        print('sequence mode')

    cue = vtkAnimationCue(start_time=5, end_time=23)
    scene.AddCue(cue)

    # Create cue animator
    animator = CueAnimator()

    # Create Cue observer.
    observer = AnimationCueObserver(ren, ren_win, animator)

    cue.AddObserver('StartAnimationCueEvent', observer)
    cue.AddObserver('EndAnimationCueEvent', observer)
    cue.AddObserver('AnimationCueTickEvent', observer)

    scene.Play()
    scene.Stop()

    iren.Start()

class CueAnimator:
    def __init__(self):
        self.source = None
        self.mapper = None
        self.actor = None

    def start_cue(self, info, ren):
        colors = vtkNamedColors()

        sphere_property = vtkProperty(color=colors.GetColor3d('Peacock'), specular=0.6, specular_power=30.0)

        # Create a sphere.
        self.source = vtkSphereSource(radius=0.5)
        self.mapper = vtkPolyDataMapper()
        self.source >> self.mapper
        self.actor = vtkActor(mapper=self.mapper, property=sphere_property)

        ren.AddActor(self.actor)

    def tick(self, info):
        new_radius = 0.1 + (info.animation_time - info.start_time) / (info.end_time - info.start_time) * 1
        # print(f'animation: {info.animation_time:5.2f}, start: {info.start_time:5.2f},'
        #       f' end: {info.end_time:5.2f}, radius: {new_radius:5.2f}')
        self.source.SetRadius(new_radius)
        self.source.update()

    def end_cue(self, info, ren):
        # Don't remove the actor for the regression image.
        # ren.RemoveActor(self.actor)
        pass

class AnimationCueObserver:
    def __init__(self, renderer, ren_win, animator):
        self.ren_win = ren_win
        self.renderer = renderer
        self.animator = animator

    def __call__(self, info, event):
        if self.animator and self.renderer:
            if event == 'StartAnimationCueEvent':
                self.animator.start_cue(info, self.renderer)
            if event == 'AnimationCueTickEvent':
                self.animator.tick(info)
            if event == 'EndAnimationCueEvent':
                self.animator.end_cue(info, self.renderer)
        if self.ren_win:
            self.ren_win.Render()

if __name__ == '__main__':
    main()
```
