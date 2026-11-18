<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/PCADemo/ -->

# PCADemo

Repository source: [PCADemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/PCADemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Utilities/TestPCADemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Utilities/TestPCADemo.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/PCADemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PCADemo.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    reference
)
from vtkmodules.vtkCommonCore import vtkBoxMuellerRandomSequence
from vtkmodules.vtkCommonCore import (
    vtkDoubleArray,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkLine,
    vtkPolyData
)
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import (
    vtkTransformFilter,
    vtkVertexGlyphFilter
)
from vtkmodules.vtkFiltersSources import (
    vtkLineSource,
    vtkSphereSource
)
from vtkmodules.vtkFiltersStatistics import (
    vtkPCAStatistics,
    vtkStatisticsAlgorithm
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkGlyph3DMapper,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    random_sequence = vtkBoxMuellerRandomSequence()

    points = vtkPoints()
    for i in range(0, 200):
        x = random_sequence.GetScaledValue(0, 2)
        random_sequence.Next()
        y = random_sequence.GetScaledValue(0, 5)
        random_sequence.Next()
        points.InsertNextPoint((x, y, 0.0))

    polydata = vtkPolyData(points=points)

    transform = vtkTransform()
    transform.RotateZ(30)

    transform_filter = vtkTransformFilter(transform=transform, input_data=polydata)
    transform_filter.update()

    # These would be all of your 'x' values.
    x_array = vtkDoubleArray(name='x', number_of_components=1)
    # These would be all of your 'y' values.
    y_array = vtkDoubleArray(name='y', number_of_components=1)

    for i in range(0, polydata.number_of_points):
        p = transform_filter.output.GetPoint(i)
        x_array.InsertNextValue(p[0])
        y_array.InsertNextValue(p[1])

    dataset_table = vtkTable()
    dataset_table.AddColumn(x_array)
    dataset_table.AddColumn(y_array)

    pca_statistics = vtkPCAStatistics()
    pca_statistics.SetInputData(vtkStatisticsAlgorithm.INPUT_DATA, dataset_table)
    pca_statistics.SetColumnStatus('x', 1)
    pca_statistics.SetColumnStatus('y', 1)
    pca_statistics.RequestSelectedColumns()
    pca_statistics.SetDeriveOption(True)
    pca_statistics.update()

    ###### Eigenvalues ######
    eigenvalues = vtkDoubleArray()
    pca_statistics.GetEigenvalues(eigenvalues)
    for i in range(0, eigenvalues.number_of_tuples):
        print(f'Eigenvalue {i}  = {eigenvalues.GetValue(i):9.6f}')

    ###### Eigenvectors ######
    eigenvectors = vtkDoubleArray()
    pca_statistics.GetEigenvectors(eigenvectors)
    evec = [0] * eigenvectors.GetNumberOfComponents()
    for i in range(0, eigenvectors.number_of_tuples):
        eigenvectors.GetTuple(i, evec)
        s = f'Eigenvector {i} = ({fmt_floats(evec, w=0, d=6)})'
        print(s)

    evec1 = vtkDoubleArray()
    pca_statistics.GetEigenvector(0, evec1)

    evec2 = vtkDoubleArray()
    pca_statistics.GetEigenvector(1, evec2)

    scale = 3.0

    vector1_source = vtkLineSource()
    vector1_source.SetPoint1(0, 0, 0)
    vector1_source.SetPoint2(scale * evec1.GetValue(0), scale * evec1.GetValue(1), 0)

    vec1_mapper = vtkPolyDataMapper()
    vector1_source >> vec1_mapper

    vector1_actor = vtkActor(mapper=vec1_mapper)
    vector1_actor.property.color = colors.GetColor3d('LimeGreen')
    vector1_actor.property.line_width = 3

    vector2_source = vtkLineSource()
    vector2_source.SetPoint1(0, 0, 0)
    vector2_source.SetPoint2(scale * evec2.GetValue(0), scale * evec2.GetValue(1), 0)

    vec2_mapper = vtkPolyDataMapper()
    vector2_source >> vec2_mapper

    vector2_actor = vtkActor(mapper=vec2_mapper)
    vector2_actor.property.color = colors.GetColor3d('Crimson')
    vector2_actor.property.line_width = 3

    # Project all the points onto the eigenvector with the largest eigenvalues.
    p0 = [0.0] * 3
    p0[0] = -100 * evec1.GetValue(0)
    p0[1] = -100 * evec1.GetValue(1)
    p0[2] = 0
    p1 = [0.0] * 3
    p1[0] = 100 * evec1.GetValue(0)
    p1[1] = 100 * evec1.GetValue(1)
    p1[2] = 0

    projected_points = vtkPoints()
    for i in range(0, polydata.number_of_points):
        p = transform_filter.output.GetPoint(i)
        t = reference(0.0)
        closest_point = [0.0] * 3
        d = 0
        d = vtkLine.DistanceToLine(p, p0, p1, t, closest_point)
        # new_p = [0.0] * 3
        # v = [0.0] * 3
        # vtkMath.Subtract(p1, p0, v)
        # vtkMath.Normalize(v)
        # vtkMath.MultiplyScalar(v, t)
        # vtkMath.Add(p0, v, new_p)
        projected_points.InsertNextPoint(t, 0, 0)

    projected_poly_data = vtkPolyData(points=projected_points)

    projected_glyph_filter = vtkVertexGlyphFilter(input_data=projected_poly_data)
    projected_glyph_filter.update()

    projected_mapper = vtkPolyDataMapper()
    projected_glyph_filter >> projected_mapper
    projected_actor = vtkActor(mapper=projected_mapper)
    projected_actor.property.point_size = 2
    projected_actor.property.color = colors.GetColor3d('Gold')

    glyph_filter = vtkVertexGlyphFilter()
    transform_filter >> glyph_filter
    glyph_filter.update()

    original_mapper = vtkPolyDataMapper()
    glyph_filter >> original_mapper
    original_actor = vtkActor(mapper=original_mapper)
    original_actor.property.point_size = 3
    original_actor.property.color = colors.GetColor3d('Blue')

    # Map the points to spheres
    sphere_actor = point_to_glyph(transform_filter.output.GetPoints(), 0.007)
    sphere_actor.property.color = colors.GetColor3d('Blue')

    # Set up the render window, interactor and renderers.
    render_window = vtkRenderWindow(size=(600, 300), window_name='PCADemo')
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Define viewport ranges
    # (xmin, ymin, xmax, ymax)
    left_viewport = (0.0, 0.0, 0.5, 1.0)
    right_viewport = (0.5, 0.0, 1.0, 1.0)

    # Setup both renderers
    leftRenderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('Burlywood'))
    render_window.AddRenderer(leftRenderer)
    right_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('SlateGray'))
    render_window.AddRenderer(right_renderer)

    # leftRenderer.AddActor(original_actor)
    leftRenderer.AddActor(sphere_actor)
    leftRenderer.AddActor(vector1_actor)
    leftRenderer.AddActor(vector2_actor)

    right_renderer.AddActor(projected_actor)

    leftRenderer.ResetCamera()
    right_renderer.ResetCamera()

    render_window.Render()
    interactor.Start()

def fmt_floats(v, w=0, d=6, pt='f'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

def point_to_glyph(points, scale):
    bounds = points.GetBounds()
    max_len = 0
    for i in range(1, 3):
        max_len = max(bounds[i + 1] - bounds[i], max_len)

    sphere_source = vtkSphereSource(radius=scale * max_len)

    pd = vtkPolyData(points=points)

    mapper = vtkGlyph3DMapper(input_data=pd, source_data=sphere_source.update().output, scalar_visibility=False,
                              scaling=False)
    actor = vtkActor(mapper=mapper)

    return actor

if __name__ == '__main__':
    main()
```
