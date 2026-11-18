<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/DistanceToCamera/ -->

# DistanceToCamera

Repository source: [DistanceToCamera](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/DistanceToCamera.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestDistanceToCamera.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestDistanceToCamera.png?raw=true target=)

### Description

This example produces two arrows whose scale stays fixed with respect to the distance from the camera (i.e. as you zoom in and out). Standard spheres are drawn for comparison.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/DistanceToCamera/)), ([Java](https://examples.vtk.org/site/Java/Visualization/DistanceToCamera/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DistanceToCamera.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkDataObject
from vtkmodules.vtkFiltersCore import vtkGlyph3D
from vtkmodules.vtkFiltersSources import vtkSphereSource, vtkPointSource, vtkArrowSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor, vtkDistanceToCamera
)

def main():
    colors = vtkNamedColors()

    # ---------------------------------------------------------------------------
    # Draw some arrows that maintain a fixed size during zooming.

    # Create a set of points.
    fixed_point_source = vtkPointSource(number_of_points=2)

    # Calculate the distance to the camera of each point.
    distance_to_camera = vtkDistanceToCamera(screen_size=100.0)
    fixed_point_source >> distance_to_camera

    # Glyph each point with an arrow.
    arrow = vtkArrowSource()
    fixed_glyph = vtkGlyph3D(input_connection=distance_to_camera.output_port, source_connection=arrow.output_port)

    # Scale each point.
    fixed_glyph.SetScaleModeToScaleByScalar()
    fixed_glyph.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_POINTS, 'DistanceToCamera')

    # Create a mapper.
    fixed_mapper = vtkPolyDataMapper(scalar_visibility=False)
    fixed_glyph >> fixed_mapper

    # Create an actor.
    fixed_actor = vtkActor(mapper=fixed_mapper)
    fixed_actor.property.color = colors.GetColor3d('Cyan')

    # ---------------------------------------------------------------------------
    # Draw some spheres that get bigger when zooming in.
    # Create a set of points.
    point_source = vtkPointSource(number_of_points=4)

    # Glyph each point with a sphere.
    sphere = vtkSphereSource()
    glyph = vtkGlyph3D(input_connection=point_source.output_port, source_connection=sphere.output_port)
    glyph.SetScaleFactor(0.1)

    # Create a mapper.
    mapper = vtkPolyDataMapper(scalar_visibility=False)
    glyph >> mapper

    # Create an actor.
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('Yellow')

    # ---------------------------------------------------------------------------

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='DistanceToCamera')
    render_window.AddRenderer(renderer)

    # Give DistanceToCamera a pointer to the renderer.
    distance_to_camera.renderer = renderer

    # Add the actors to the scene.
    renderer.AddActor(fixed_actor)
    renderer.AddActor(actor)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleTrackballCamera()
    render_window_interactor.interactor_style = style
    render_window_interactor.render_window = render_window

    # Render an image (lights and cameras are created automatically).
    render_window.Render()

    # Begin mouse interaction.
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
