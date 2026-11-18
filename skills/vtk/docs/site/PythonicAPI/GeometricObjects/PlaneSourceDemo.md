<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/PlaneSourceDemo/ -->

# PlaneSourceDemo

Repository source: [PlaneSourceDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/PlaneSourceDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestPlaneSourceDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestPlaneSourceDemo.png?raw=true target=)

### Description

The example displays the various instance variables that define a [vtkPlaneSource](https://www.vtk.org/doc/nightly/html/classvtkPlaneSource.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/PlaneSourceDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PlaneSourceDemo.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkMath, vtkMinimalStandardRandomSequence
)
from vtkmodules.vtkCommonMath import vtkMatrix4x4
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersSources import (
    vtkArrowSource,
    vtkPlaneSource,
    vtkSphereSource
)
from vtkmodules.vtkRenderingAnnotation import vtkLegendBoxActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    background_color = colors.GetColor3d('DarkSlateGray')
    legend_background_color = colors.GetColor3d('SlateGray')
    origin_color = colors.GetColor3d('OrangeRed')
    center_color = colors.GetColor3d('Gold')
    point1_color = colors.GetColor3d('MediumSpringGreen')
    point2_color = colors.GetColor3d('Brown')
    x_axis_color = colors.GetColor3d('lime')
    y_axis_color = colors.GetColor3d('orange')
    normal_color = colors.GetColor3d('Raspberry')

    # Create the actors.
    plane_source = vtkPlaneSource(origin=(0.0, 0.0, 0.0), point1=(1.0, 0.0, 0.0), point2=(0.0, 1.0, 0.0))

    bounds = plane_source.update().output.bounds
    length = max(bounds[1] - bounds[0], bounds[3] - bounds[2])
    plane_mapper = vtkPolyDataMapper()
    plane_actor = vtkActor(mapper=plane_mapper)

    sphere_source = vtkSphereSource(radius=length * 0.04)

    origin_mapper = vtkPolyDataMapper()
    origin_mapper.SetInputConnection(sphere_source.GetOutputPort())
    origin_actor = vtkActor(position=plane_source.origin, mapper=origin_mapper)
    origin_actor.property.diffuse_color = origin_color

    center_mapper = vtkPolyDataMapper()
    center_actor = vtkActor(position=plane_source.center, mapper=center_mapper)
    center_actor.property.diffuse_color = center_color

    point1_mapper = vtkPolyDataMapper()
    point1_actor = vtkActor(position=plane_source.point1, mapper=point1_mapper)
    point1_actor.property.diffuse_color = point1_color

    point2_mapper = vtkPolyDataMapper()
    point2_actor = vtkActor(position=plane_source.point2, mapper=point2_mapper)
    point2_actor.property.diffuse_color = point2_color

    # Group the pipelines.
    plane_source >> plane_mapper
    sphere_source >> origin_mapper
    sphere_source >> center_mapper
    sphere_source >> point1_mapper
    sphere_source >> point2_mapper

    normal = [n * length for n in plane_source.normal]

    x_axis_poly_data = create_arrow(length, plane_source.origin, plane_source.point1)
    x_axis_mapper = vtkPolyDataMapper(input_data=x_axis_poly_data)
    x_axis_actor = vtkActor(mapper=x_axis_mapper)
    x_axis_actor.property.diffuse_color = x_axis_color

    y_axis_poly_data = create_arrow(length, plane_source.origin, plane_source.point2)
    y_axis_mapper = vtkPolyDataMapper(input_data=y_axis_poly_data)
    y_axis_actor = vtkActor(mapper=y_axis_mapper)
    y_axis_actor.property.diffuse_color = y_axis_color

    normal_poly_data = create_arrow(length, plane_source.origin, normal)
    normal_mapper = vtkPolyDataMapper(input_data=normal_poly_data)
    normal_actor = vtkActor(mapper=normal_mapper)
    normal_actor.property.diffuse_color = normal_color

    # Create the legend.
    legend = vtkLegendBoxActor()
    legend.SetNumberOfEntries(7)
    legend.UseBackgroundOn()
    legend.SetBackgroundColor(legend_background_color)
    legend.GetPositionCoordinate().SetValue(0.7, 0.7)
    legend.GetPosition2Coordinate().SetValue(0.3, 0.3)

    legend.SetEntry(0, sphere_source.output, 'center', center_color)
    legend.SetEntry(1, sphere_source.output, 'origin', origin_color)
    legend.SetEntry(2, sphere_source.output, 'point1', point1_color)
    legend.SetEntry(3, sphere_source.output, 'point2', point2_color)
    legend.SetEntry(4, x_axis_poly_data, 'xAxis', x_axis_color)
    legend.SetEntry(5, x_axis_poly_data, 'yAxis', y_axis_color)
    legend.SetEntry(6, x_axis_poly_data, 'normal', normal_color)

    # Create the Renderer, RenderWindow and interactor.
    renderer = vtkRenderer(background=background_color)
    render_window = vtkRenderWindow(size=(640, 480), window_name='PlaneSourceDemo')
    render_window.AddRenderer(renderer)
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    renderer.AddActor(plane_actor)
    renderer.AddActor(origin_actor)
    renderer.AddActor(center_actor)
    renderer.AddActor(point1_actor)
    renderer.AddActor(point2_actor)
    renderer.AddActor(x_axis_actor)
    renderer.AddActor(y_axis_actor)
    renderer.AddActor(normal_actor)
    renderer.AddActor(legend)

    render_window.Render()

    renderer.active_camera.position = (1, 0, 0)
    renderer.active_camera.focal_point = (0, 1, 0)
    renderer.active_camera.view_up = (0, 0, 1)
    renderer.active_camera.Azimuth(30)
    renderer.active_camera.Elevation(30)
    renderer.ResetCamera()
    render_window.Render()
    interactor.Start()

def create_arrow(pd_length, start_point, end_point):
    # Create an arrow.
    arrow_source = vtkArrowSource()
    arrow_source.SetShaftRadius(pd_length * 0.01)
    arrow_source.SetShaftResolution(20)
    arrow_source.SetTipLength(pd_length * 0.1)
    arrow_source.SetTipRadius(pd_length * 0.05)
    arrow_source.SetTipResolution(20)
    # Compute a basis
    normalized_x = [0.0] * 3
    normalized_y = [0.0] * 3
    normalized_z = [0.0] * 3
    # The X axis is a vector from start to end.
    vtkMath.Subtract(end_point, start_point, normalized_x)
    length = vtkMath.Norm(normalized_x)
    vtkMath.Normalize(normalized_x)
    # The Z axis is an arbitrary vector cross X.
    rng = vtkMinimalStandardRandomSequence(seed=8775070)
    arbitrary = [0.0] * 3
    for i in range(0, 3):
        rng.Next()
        arbitrary[i] = rng.GetRangeValue(-10, 10)
    vtkMath.Cross(normalized_x, arbitrary, normalized_z)
    vtkMath.Normalize(normalized_z)
    # The Y axis is Z cross X.
    vtkMath.Cross(normalized_z, normalized_x, normalized_y)
    matrix = vtkMatrix4x4()
    # Create the direction cosine matrix.
    matrix.Identity()
    for i in range(0, 3):
        matrix.SetElement(i, 0, normalized_x[i])
        matrix.SetElement(i, 1, normalized_y[i])
        matrix.SetElement(i, 2, normalized_z[i])
    # Apply the transforms.
    transform = vtkTransform()
    transform.Translate(start_point)
    transform.Concatenate(matrix)
    transform.Scale(length, length, length)
    # Transform the polydata.
    transform_pd = vtkTransformFilter(transform=transform, input_connection=arrow_source.output_port)
    arrow_source >> transform_pd

    return transform_pd.update().output

if __name__ == '__main__':
    main()
```
