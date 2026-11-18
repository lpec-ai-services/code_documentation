<!-- source: https://examples.vtk.org/site/PythonicAPI/Points/FitImplicitFunction/ -->

# FitImplicitFunction

Repository source: [FitImplicitFunction](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Points/FitImplicitFunction.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestFitImplicitFunction.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestFitImplicitFunction.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Points/FitImplicitFunction/)), ([Java](https://examples.vtk.org/site/Java/Points/FitImplicitFunction/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FitImplicitFunction.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkSphere
from vtkmodules.vtkFiltersCore import vtkGlyph3D
from vtkmodules.vtkFiltersPoints import (
    vtkBoundedPointSource,
    vtkFitImplicitFunction
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    radius = 1.0
    sphere = vtkSphere(radius=radius)

    points = vtkBoundedPointSource(number_of_points=1000000, bounds=(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0))

    fit = vtkFitImplicitFunction(implicit_function=sphere, threshold=0.01)
    points >> fit
    fit.update()
    print(f'{fit.output.number_of_points} out of {points.output.number_of_points}'
          f' points are within {fit.threshold} of the implicit function.')

    sphere_source = vtkSphereSource(radius=radius * 0.05)

    glyph3d = vtkGlyph3D(source_connection=sphere_source.output_port, scaling=False)
    fit >> glyph3d

    glyph3d_mapper = vtkPolyDataMapper()
    glyph3d >> glyph3d_mapper

    glyph3d_actor = vtkActor(mapper=glyph3d_mapper)
    glyph3d_actor.property.color = colors.GetColor3d('Banana')

    # Create the graphics stuff.
    ren = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name='FitImplicitFunction')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer, set the background and size.
    ren.AddActor(glyph3d_actor)

    # Generate an interesting view.
    ren.ResetCamera()
    ren.active_camera.Azimuth(120)
    ren.active_camera.Elevation(30)
    ren.active_camera.Dolly(1.0)
    ren.ResetCameraClippingRange()

    ren_win.Render()
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
