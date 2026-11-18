<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/OrientedArrow/ -->

# OrientedArrow

Repository source: [OrientedArrow](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/OrientedArrow.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestOrientedArrow.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestOrientedArrow.png?raw=true target=)

### Description

This example illustrates how to create and display an arrow that passes through two points.

It demonstrates two different ways to apply the transform:

1. Use [vtkTransformFilter](https://www.vtk.org/doc/nightly/html/classvtkTransformFilter.html) to create a new transformed polydata. This method is useful if the transformed polydata is needed later in the pipeline, e.g. vtkGlyph3DFilter.
2. Apply the transform directly to the actor using [vtkProp3D](https://www.vtk.org/doc/nightly/html/classvtkProp3D.html)'s SetUserMatrix. No new data is produced.

Switch between the two methods by #defining USER_MATRIX or leaving out the #define.

Seealso

Compare this example with [OrientedCylinder](OrientedCylinder.md). The transform is different because the cylinder

height direction is along the y-axis and the arrow height is along the x-axis.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/OrientedArrow/)), ([Python](../../Python/GeometricObjects/OrientedArrow.md)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/OrientedArrow/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/OrientedArrow/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OrientedArrow.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkMath,
    vtkMinimalStandardRandomSequence
)
from vtkmodules.vtkCommonMath import vtkMatrix4x4
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersSources import (
    vtkArrowSource,
    vtkSphereSource
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

"""
There are two alternative ways to apply the transform.
 1) Use vtkTransformFilter to create a new transformed polydata.
    This method is useful if the transformed polydata is needed
      later in the pipeline
    To do this, set USER_MATRIX = True
 2) Apply the transform directly to the actor using vtkProp3D's SetUserMatrix.
    No new data is produced.
    To do this, set USER_MATRIX = False
"""
USER_MATRIX = True

def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor('BkgColor', 26, 51, 77, 255)

    # Create an arrow.
    arrow_source = vtkArrowSource()

    # Generate a random start and end point.
    start_point = [0] * 3
    end_point = [0] * 3
    rng = vtkMinimalStandardRandomSequence(seed=8775070)
    # rng.SetSeed(8775070)  # For testing.
    for i in range(0, 3):
        rng.Next()
        start_point[i] = rng.GetRangeValue(-10, 10)
        rng.Next()
        end_point[i] = rng.GetRangeValue(-10, 10)

    # Compute a basis
    normalized_x = [0] * 3
    normalized_y = [0] * 3
    normalized_z = [0] * 3

    # The X axis is a vector from start to end.
    vtkMath.Subtract(end_point, start_point, normalized_x)
    length = vtkMath.Norm(normalized_x)
    vtkMath.Normalize(normalized_x)

    # The Z axis is an arbitrary vector cross X.
    arbitrary = [0] * 3
    for i in range(0, 3):
        rng.Next()
        arbitrary[i] = rng.GetRangeValue(-10, 10)
    vtkMath.Cross(normalized_x, arbitrary, normalized_z)
    vtkMath.Normalize(normalized_z)

    # The Y axis is Z cross X
    vtkMath.Cross(normalized_z, normalized_x, normalized_y)
    matrix = vtkMatrix4x4()

    # Create the direction cosine matrix.
    matrix.Identity()
    for i in range(0, 3):
        matrix.SetElement(i, 0, normalized_x[i])
        matrix.SetElement(i, 1, normalized_y[i])
        matrix.SetElement(i, 2, normalized_z[i])

    # Apply the transforms
    transform = vtkTransform()
    transform.Translate(start_point)
    transform.Concatenate(matrix)
    transform.Scale(length, length, length)

    # Transform the polydata.
    transform_pd = vtkTransformFilter(transform=transform)

    # Create a mapper and actor for the arrow.
    mapper = vtkPolyDataMapper()
    actor = vtkActor()
    if USER_MATRIX:
        arrow_source >> mapper
        actor.user_matrix = transform.matrix
    else:
        arrow_source >> transform_pd >> mapper
    actor.mapper = mapper
    actor.property.color = colors.GetColor3d('Cyan')

    # Create spheres for the start and end points.
    sphere_start_source = vtkSphereSource(center=start_point, radius=0.8)
    sphere_start_mapper = vtkPolyDataMapper()
    sphere_start_source >> sphere_start_mapper
    sphere_start = vtkActor(mapper=sphere_start_mapper)
    sphere_start.property.color = colors.GetColor3d('Yellow')

    sphere_end_source = vtkSphereSource(center=end_point, radius=0.8)
    sphere_end_mapper = vtkPolyDataMapper()
    sphere_end_source >> sphere_end_mapper
    sphere_end = vtkActor(mapper=sphere_end_mapper)
    sphere_end.property.color = colors.GetColor3d('Magenta')

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer(background=colors.GetColor3d('BkgColor'))
    render_window = vtkRenderWindow(window_name='OrientedArrow')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(actor)
    renderer.AddActor(sphere_start)
    renderer.AddActor(sphere_end)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
