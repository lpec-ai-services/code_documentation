<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/ConvexPointSet/ -->

# ConvexPointSet

Repository source: [ConvexPointSet](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/ConvexPointSet.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestConvexPointSet.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestConvexPointSet.png?raw=true target=)

### Description

[vtkConvexPointSet](https://www.vtk.org/doc/nightly/html/classvtkConvexPointSet.html) object represents a 3D cell defined by a convex set of points. An example of such a cell is an octant (from an octree).

[vtkConvexPointSet](https://www.vtk.org/doc/nightly/html/classvtkConvexPointSet.html) uses the ordered triangulations approach ([vtkOrderedTriangulator](https://www.vtk.org/doc/nightly/html/classvtkOrderedTriangulator.html)) to create triangulations guaranteed to be compatible across shared faces.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/ConvexPointSet/)), ([Python](../../Python/GeometricObjects/ConvexPointSet.md)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/ConvexPointSet/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ConvexPointSet.py**

```python
# !/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkConvexPointSet,
    vtkPolyData,
    vtkUnstructuredGrid
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkGlyph3DMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    cps = vtkConvexPointSet()
    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(1, 0, 0)
    points.InsertNextPoint(1, 1, 0)
    points.InsertNextPoint(0, 1, 0)
    points.InsertNextPoint(0, 0, 1)
    points.InsertNextPoint(1, 0, 1)
    points.InsertNextPoint(1, 1, 1)
    points.InsertNextPoint(0, 1, 1)
    points.InsertNextPoint(0.5, 0, 0)
    points.InsertNextPoint(1, 0.5, 0)
    points.InsertNextPoint(0.5, 1, 0)
    points.InsertNextPoint(0, 0.5, 0)
    points.InsertNextPoint(0.5, 0.5, 0)

    for i in range(0, 13):
        cps.GetPointIds().InsertId(i, i)

    ug = vtkUnstructuredGrid(points=points)
    ug.Allocate(1, 1)
    ug.InsertNextCell(cps.GetCellType(), cps.GetPointIds())

    colors = vtkNamedColors()

    mapper = vtkDataSetMapper()
    ug >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d("Tomato")
    actor.property.line_width = 3
    actor.property.edge_visibility = True

    # Glyph the points
    sphere = vtkSphereSource(radius=0.03, phi_resolution=21, theta_resolution=21)

    # Create a polydata to store everything in
    poly_data = vtkPolyData(points=points)

    point_mapper = vtkGlyph3DMapper(input_data=poly_data, source_data=sphere.update().output)

    point_actor = vtkActor(mapper=point_mapper)
    point_actor.property.color = colors.GetColor3d('Peacock')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='ConvexPointSet')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.AddActor(point_actor)

    renderer.ResetCamera()
    renderer.active_camera.Azimuth(210)
    renderer.active_camera.Elevation(30)
    renderer.ResetCameraClippingRange()

    # Render and interact
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
