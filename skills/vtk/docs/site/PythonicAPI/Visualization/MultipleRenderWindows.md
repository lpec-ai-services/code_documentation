<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/MultipleRenderWindows/ -->

# MultipleRenderWindows

Repository source: [MultipleRenderWindows](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/MultipleRenderWindows.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestMultipleRenderWindows.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestMultipleRenderWindows.png?raw=true target=)

### Description

This example creates four render windows. Three of the windows will close individually and closing one window will close all the others. Guess which one!

You can also press **'q'** or **'e'** to close a window.

If the parameter **'s'** (C++) or **'-s** (Python) is specified, then updating the camera position in one window will also update the position in the other windows. Pressing **'q'** or **'e'** closes all windows. Note that in this mode you **must** use **'q'** or **'e'** to close the windows.

Note

The image you see here is the test image. When you run this program you will see an image similar to [MultipleViewports](MultipleViewports.md) however each object will be in a separate window.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/MultipleRenderWindows/)), ([Python](../../Python/Visualization/MultipleRenderWindows.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MultipleRenderWindows.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkCubeSource,
    vtkCylinderSource,
    vtkSphereSource
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Display multiple render windows.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', default=False, action='store_true',
                        help='Simultaneous camera position updating.')
    args = parser.parse_args()
    return args.s

def main():
    simultaneous_update = get_program_parameters()

    colors = vtkNamedColors()
    # Have some fun with colors
    ren_bkg = ['AliceBlue', 'GhostWhite', 'WhiteSmoke', 'Seashell']
    actor_color = ['Bisque', 'RosyBrown', 'Goldenrod', 'Chocolate']

    # Window sizes and spacing.
    width = 300
    height = 300
    # Add extra space around each window.
    dx = 20
    dy = 40
    w = width + dx
    h = height + dy

    interactors = list()
    running = [True, True, True, True]

    camera = None
    sources = get_sources()

    kpis = list()
    for i in range(0, 4):
        renderer = vtkRenderer(background=colors.GetColor3d(ren_bkg[i]))
        ren_win = vtkRenderWindow(size=(width, height))
        ren_win.window_name = f'MultipleRenderWindows {i:d}'
        ren_win.SetPosition((i % 2) * w, h - (i // 2) * h)
        ren_win.AddRenderer(renderer)
        iren = vtkRenderWindowInteractor()
        interactors.append(iren)
        iren.render_window = ren_win

        # Share the camera between viewports.
        if i == 0:
            camera = renderer.active_camera
            camera.Azimuth(30)
            camera.Elevation(30)
        else:
            renderer.active_camera = camera

        # Create a mapper and actor.
        mapper = vtkPolyDataMapper()
        sources[i] >> mapper

        actor = vtkActor(mapper=mapper)
        actor.property.color = colors.GetColor3d(actor_color[i])

        renderer.AddActor(actor)
        renderer.ResetCamera()

        ren_win.Render()

        running[i] = True
        kpis.append(KeyPressInteractorStyle(parent=iren))
        interactors[i].interactor_style = kpis[i]
        kpis[i].status = running[i]

    if simultaneous_update:
        interactors[0].Initialize()
        while all(x is True for x in running):
            for i in range(0, 4):
                running[i] = kpis[i].status
                if running[i]:
                    interactors[i].ProcessEvents()
                    interactors[i].Render()
                else:
                    interactors[i].TerminateApp()
                    print('Window', i, 'has stopped running.')
    else:
        interactors[0].Start()

def get_sources():
    sources = list()

    # Create a sphere
    sphere = vtkSphereSource(center=(0.0, 0.0, 0.0))
    sources.append(sphere)
    cone = vtkConeSource(center=(0.0, 0.0, 0.0), direction=(0, 1, 0))
    sources.append(cone)
    cube = vtkCubeSource(center=(0.0, 0.0, 0.0))
    sources.append(cube)
    cylinder = vtkCylinderSource(center=(0.0, 0.0, 0.0))
    sources.append(cylinder)

    return sources

class KeyPressInteractorStyle(vtkInteractorStyleTrackballCamera):

    def __init__(self, parent=None, status=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.parent = vtkRenderWindowInteractor()
        self.status = status
        if parent is not None:
            self.parent = parent

        self.AddObserver('KeyPressEvent', self.key_press_event)

    def key_press_event(self, obj, event):
        key = self.parent.GetKeySym().lower()
        if key == 'e' or key == 'q':
            self.status = False
        return

if __name__ == '__main__':
    main()
```
