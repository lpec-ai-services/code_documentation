<!-- source: https://examples.vtk.org/site/PythonicAPI/Points/ExtractClusters/ -->

# ExtractClusters

Repository source: [ExtractClusters](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Points/ExtractClusters.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestExtractClusters.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Points/TestExtractClusters.png?raw=true target=)

### Description

This example extracts clusters of points. The points lie on spheres that are randomly placed. Each cluster has a different color. The number of extracted clusters may be less that the number of random spheres, if the points on one sphere are within the specified distance of points on another sphere.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Points/ExtractClusters/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractClusters.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable, vtkMinimalStandardRandomSequence
from vtkmodules.vtkFiltersCore import vtkAppendPolyData, vtkGlyph3D
from vtkmodules.vtkFiltersPoints import vtkEuclideanClusterExtraction
from vtkmodules.vtkFiltersSources import vtkSphereSource, vtkPointSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor, vtkPolyDataMapper
)

def main():
    colors = vtkNamedColors()

    randomSequence = vtkMinimalStandardRandomSequence(seed=4355412)
    # randomSequence.SetSeed(8775070)

    limits = 10
    radius = 0.5

    append = vtkAppendPolyData()
    for i in range(0, 30):
        points = vtkPointSource()

        points.SetNumberOfPoints(800)
        points.SetRadius(2.5 * radius)
        # A random position.
        x = randomSequence.GetRangeValue(-limits, limits)
        randomSequence.Next()
        y = randomSequence.GetRangeValue(-limits, limits)
        randomSequence.Next()
        z = randomSequence.GetRangeValue(-limits, limits)
        randomSequence.Next()
        points.center = (x, y, z)
        points.SetDistributionToShell()

        append.AddInputConnection(points.output_port)

    cluster = vtkEuclideanClusterExtraction(radius=radius, color_clusters=True)
    append >> cluster
    cluster.SetExtractionModeToAllClusters()
    cluster.update()

    print(f'Found {cluster.number_of_extracted_clusters} clusters within radius {radius}')

    # Create a lookup table to map point data to colors.
    lut = vtkLookupTable()
    tableSize = cluster.number_of_extracted_clusters
    lut.SetNumberOfTableValues(tableSize)
    lut.Build()

    # Fill in the lookup table.
    for i in range(0, tableSize):
        r = randomSequence.GetRangeValue(0.25, 1.0)
        randomSequence.Next()
        g = randomSequence.GetRangeValue(0.25, 1.0)
        randomSequence.Next()
        b = randomSequence.GetRangeValue(0.25, 1.0)
        randomSequence.Next()
        lut.SetTableValue(i, r, g, b, 1.0)

    sphere = vtkSphereSource(radius=radius / 2.0)

    glyphs = vtkGlyph3D(input_connection=cluster.output_port, source_connection=sphere.output_port, scaling=False)
    glyphs.Update()

    mapper = vtkPolyDataMapper(scalar_range=(0, tableSize - 1), lookup_table=lut)
    glyphs >> mapper

    actor = vtkActor(mapper=mapper)

    # Create the graphics stuff.
    ren1 = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(640, 512), window_name='ExtractClusters')
    ren_win.AddRenderer(ren1)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer.
    ren1.AddActor(actor)

    # Generate an interesting view.
    ren1.ResetCamera()
    ren1.active_camera.Azimuth(120)
    ren1.active_camera.Elevation(30)
    ren1.active_camera.Dolly(1.5)
    ren1.ResetCameraClippingRange()

    ren_win.Render()
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
