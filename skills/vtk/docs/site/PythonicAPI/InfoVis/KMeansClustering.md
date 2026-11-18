<!-- source: https://examples.vtk.org/site/PythonicAPI/InfoVis/KMeansClustering/ -->

# KMeansClustering

Repository source: [KMeansClustering](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/InfoVis/KMeansClustering.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/InfoVis/TestKMeansClustering.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/InfoVis/TestKMeansClustering.png?raw=true target=)

### Description

This example clusters 3D points using the KMeans algorithm. The points are assigned to a cluster by creating an array with each point's cluster id.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/InfoVis/KMeansClustering/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**KMeansClustering.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkIntArray,
    vtkDoubleArray,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkPolyData,
    vtkStatisticalModel,
    vtkTable
)
from vtkmodules.vtkFiltersGeneral import vtkVertexGlyphFilter
from vtkmodules.vtkFiltersStatistics import (
    vtkKMeansStatistics,
    vtkStatisticsAlgorithm,

)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Create 2 clusters, one near (0,0,0) and the other near (3,3,3).
    points = vtkPoints()

    points.InsertNextPoint(0.0, 0.0, 0.0)
    points.InsertNextPoint(3.0, 3.0, 3.0)
    points.InsertNextPoint(0.1, 0.1, 0.1)
    points.InsertNextPoint(3.1, 3.1, 3.1)
    points.InsertNextPoint(0.2, 0.2, 0.2)
    points.InsertNextPoint(3.2, 3.2, 3.2)

    # Get the points into the format needed for KMeans.
    input_data = vtkTable()

    for c in range(0, 3):
        col_name = f'coord {c:0d}'
        double_array = vtkDoubleArray(number_of_components=1, name=col_name, number_of_tuples=points.number_of_points)

        for r in range(0, points.number_of_points):
            p = [0.0] * 3
            points.GetPoint(r, p)

            double_array.SetValue(r, p[c])

        input_data.AddColumn(double_array)

    k_means_statistics = vtkKMeansStatistics(assess_option=True, default_number_of_clusters=2)
    k_means_statistics.SetInputData(vtkStatisticsAlgorithm.INPUT_DATA, input_data)
    k_means_statistics.SetColumnStatus(input_data.GetColumnName(0), 1)
    k_means_statistics.SetColumnStatus(input_data.GetColumnName(1), 1)
    k_means_statistics.SetColumnStatus(input_data.GetColumnName(2), 1)
    k_means_statistics.RequestSelectedColumns()
    k_means_statistics.update()

    # Display the results.
    k_means_statistics.output.Dump()

    cluster_array = vtkIntArray(number_of_components=1, name='ClusterId')

    for r in range(0, k_means_statistics.output.number_of_rows):
        v = k_means_statistics.GetOutput().GetValue(r, k_means_statistics.GetOutput().GetNumberOfColumns() - 1)
        print(f'Point {r} is in cluster {v.ToInt()}')
        cluster_array.InsertNextValue(v.ToInt())

    # Output the cluster centers.
    output_meta_ds = k_means_statistics.GetOutputDataObject(vtkStatisticsAlgorithm.OUTPUT_MODEL)
    if output_meta_ds:
        output_meta = output_meta_ds.GetTable(vtkStatisticalModel.Learned, 0)
        coord0 = output_meta.GetColumnByName('coord 0')
        coord1 = output_meta.GetColumnByName('coord 1')
        coord2 = output_meta.GetColumnByName('coord 2')
        print(f'Cluster centers:')
        number_of_tuples = coord0.number_of_tuples
        for i in range(0, number_of_tuples):
            center = [coord0.GetValue(i), coord1.GetValue(i), coord2.GetValue(i)]
            print(f'Cluster {i}: ({fmt_floats(center)})')
    else:
        print('Cluster centers not found.')

    poly_data = vtkPolyData(points=points)
    poly_data.point_data.SetScalars(cluster_array)

    # Display
    glyph_filter = vtkVertexGlyphFilter(input_data=poly_data)

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    glyph_filter >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.point_size = 10
    actor.property.render_points_as_spheres = True

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('OliveDrab'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='KMeansClustering')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actor to the scene
    renderer.AddActor(actor)

    style = vtkInteractorStyleTrackballCamera()
    render_window_interactor.interactor_style = style

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

def fmt_floats(v, w=0, d=6, pt='g'):
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

if __name__ == '__main__':
    main()
```
