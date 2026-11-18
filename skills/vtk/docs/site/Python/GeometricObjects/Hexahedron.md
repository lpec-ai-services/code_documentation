<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/Hexahedron/ -->

# Hexahedron

Repository source: [Hexahedron](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/Hexahedron.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestHexahedron.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestHexahedron.png?raw=true target=)

### Description

The hexahedron is a primary three-dimensional cell consisting of six quadrilateral faces, twelve edges, and eight vertices. The hexahedron is defined by an ordered list of eight points. The faces and edges must not intersect any other faces and edges, and the hexahedron must be convex.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Hexahedron/)), ([CSharp](https://examples.vtk.org/site/CSharp/GeometricObjects/Hexahedron/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Hexahedron.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkHexahedron,
    vtkUnstructuredGrid
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor("BkgColor", [51, 77, 102, 255])

    # For the hexahedron setup the coordinates of eight points.
    # The two faces must be in counter clockwise order as viewed from the
    # outside.
    pointCoordinates = list()
    pointCoordinates.append([0.0, 0.0, 0.0])  # Face 1
    pointCoordinates.append([1.0, 0.0, 0.0])
    pointCoordinates.append([1.0, 1.0, 0.0])
    pointCoordinates.append([0.0, 1.0, 0.0])
    pointCoordinates.append([0.0, 0.0, 1.0])  # Face 2
    pointCoordinates.append([1.0, 0.0, 1.0])
    pointCoordinates.append([1.0, 1.0, 1.0])
    pointCoordinates.append([0.0, 1.0, 1.0])

    # Create the points.
    points = vtkPoints()

    # Create a hexahedron from the points.
    hexahedron = vtkHexahedron()

    for i in range(0, len(pointCoordinates)):
        points.InsertNextPoint(pointCoordinates[i])
        hexahedron.GetPointIds().SetId(i, i)

    # Add the hexahedron to a cell array.
    hexs = vtkCellArray()
    hexs.InsertNextCell(hexahedron)

    # Add the points and hexahedron to an unstructured grid.
    uGrid = vtkUnstructuredGrid()
    uGrid.SetPoints(points)
    uGrid.InsertNextCell(hexahedron.GetCellType(), hexahedron.GetPointIds())

    # Visualize.
    mapper = vtkDataSetMapper()
    mapper.SetInputData(uGrid)

    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d("PeachPuff"))
    actor.SetMapper(mapper)

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName("Hexahedron")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("BkgColor"))
    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)

    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
