<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/MultipleViewports/ -->

# MultipleViewports

Repository source: [MultipleViewports](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/MultipleViewports.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestMultipleViewports.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestMultipleViewports.png?raw=true target=)

### Description

This example creates a window with 4 viewports. Updating the camera position in one viewport will also update the position in the other viewports.

See [MultipleRenderWindows](MultipleRenderWindows.md) for an example using multiple windows.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/MultipleViewports/)), ([Python](../../Python/Visualization/MultipleViewports.md)), ([Java](https://examples.vtk.org/site/Java/Visualization/MultipleViewports/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MultipleViewports.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkCubeSource,
    vtkCylinderSource,
    vtkSphereSource
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

    # One render window, multiple viewports.
    rw = vtkRenderWindow(size=(600, 600), window_name='MultipleViewPorts')
    iren = vtkRenderWindowInteractor()
    iren.render_window = rw

    # Define viewport ranges.
    xmins = [0, .5, 0, .5]
    xmaxs = [0.5, 1, 0.5, 1]
    ymins = [0, 0, .5, .5]
    ymaxs = [0.5, 0.5, 1, 1]

    # Have some fun with colors.
    ren_bkg = ['AliceBlue', 'GhostWhite', 'WhiteSmoke', 'Seashell']
    actor_color = ['Bisque', 'RosyBrown', 'Goldenrod', 'Chocolate']

    sources = get_sources()
    camera = None
    for i in range(4):

        # Create a mapper and actor
        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(sources[i].GetOutputPort())
        actor = vtkActor()
        actor.GetProperty().SetColor(colors.GetColor3d(actor_color[i]))
        actor.SetMapper(mapper)

        ren = vtkRenderer(viewport=(xmins[i], ymins[i], xmaxs[i], ymaxs[i]), background=colors.GetColor3d(ren_bkg[i]))
        rw.AddRenderer(ren)

        ren.AddActor(actor)

        # Share the camera between viewports.
        if i == 0:
            camera = ren.active_camera
            camera.Azimuth(30)
            camera.Elevation(30)
        else:
            ren.active_camera = camera

        ren.ResetCamera()

    rw.Render()
    iren.Start()

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

if __name__ == '__main__':
    main()
```
