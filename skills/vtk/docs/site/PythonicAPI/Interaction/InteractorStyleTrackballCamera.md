<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/InteractorStyleTrackballCamera/ -->

# InteractorStyleTrackballCamera

Repository source: [InteractorStyleTrackballCamera](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/InteractorStyleTrackballCamera.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestInteractorStyleTrackballCamera.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestInteractorStyleTrackballCamera.png?raw=true target=)

Other languages

See ([Python](../../Python/Interaction/InteractorStyleTrackballCamera.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**InteractorStyleTrackballCamera.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersSources import (
    vtkPointSource,
    vtkSphereSource
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkGlyph3DMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # create a rendering window and renderer
    ren = vtkRenderer(background=colors.GetColor3d('RoyalBLue'))
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(ren)
    ren_win.SetWindowName('InteractorStyleTrackballCamera')

    # Create a render window interactor.
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    # Create the source, mapper and actor.
    src = vtkPointSource(center=(0, 0, 0), number_of_points=50, radius=5)

    actor = point_to_glyph(src.update().output.GetPoints(), 0.05)
    actor.GetProperty().SetColor(colors.GetColor3d('Gold'))

    ren.AddActor(actor)

    # Enable the user interface interactor.
    iren.Initialize()
    ren_win.Render()
    iren.Start()

def point_to_glyph(points, scale):
    """
    Convert points to glyphs.
    :param points: The points to glyph.
    :param scale: The scale, used to determine the size of the
                  glyph representing the point, expressed as a
                  fraction of the largest side of the bounding
                  box surrounding the points. e.g. 0.05
    :return: The actor.
    """

    bounds = points.bounds
    max_len = 0.0
    for i in range(0, 3):
        max_len = max(bounds[i + 1] - bounds[i], max_len)

    sphere_source = vtkSphereSource(radius=scale * max_len)

    pd = vtkPolyData(points=points)

    mapper = vtkGlyph3DMapper(source_data=sphere_source.update().output, scalar_visibility=False, scaling=False)
    pd >> mapper

    return vtkActor(mapper=mapper)

if __name__ == '__main__':
    main()
```
