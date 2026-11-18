<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/PolyhedronAndHexahedron/ -->

# PolyhedronAndHexahedron

Repository source: [PolyhedronAndHexahedron](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/PolyhedronAndHexahedron.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPolyhedronAndHexahedron.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPolyhedronAndHexahedron.png?raw=true target=)

### Description

This is a demonstration of how to construct an unstructured grid containing mixed cells types, polyhedron and hexahedron. It rely on the `SetPolyhedralCells` API. The resulting object is then displayed.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/PolyhedronAndHexahedron/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PolyhedronAndHexahedron.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkPoints,
    vtkUnsignedCharArray
)
from vtkmodules.vtkCommonDataModel import (
    VTK_HEXAHEDRON,
    VTK_POLYHEDRON,
    vtkCellArray,
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

    # create polyhedron (cube)

    ## Create points in an arbitrary order
    points = vtkPoints()
    points.InsertNextPoint(-5.0, -5.0, -10.0)
    points.InsertNextPoint(-5.0, -5.0, 10.0)
    points.InsertNextPoint(-5.0, 5.0, -10.0)
    points.InsertNextPoint(-5.0, 5.0, 10.0)
    points.InsertNextPoint(5.0, -5.0, -10.0)
    points.InsertNextPoint(5.0, -5.0, 10.0)
    points.InsertNextPoint(5.0, 5.0, -10.0)
    points.InsertNextPoint(5.0, 5.0, 10.0)

    ## The ID of the points that compose the polyhedron cell
    pointIds = [0, 1, 2, 3, 4, 5, 6, 7]

    ## The ID of the points that compose each individual faces
    faces = vtkCellArray()
    face0 = [0, 2, 6, 4]
    face1 = [1, 3, 7, 5]
    face2 = [0, 1, 3, 2]
    face3 = [4, 5, 7, 6]
    face4 = [0, 1, 5, 4]
    face5 = [2, 3, 7, 6]

    ## Insert each face
    faces.InsertNextCell(4, face0)
    faces.InsertNextCell(4, face1)
    faces.InsertNextCell(4, face2)
    faces.InsertNextCell(4, face3)
    faces.InsertNextCell(4, face4)
    faces.InsertNextCell(4, face5)

    ## Add the IDs of the faces for the polyhedron cell
    faceLocations = vtkCellArray()
    faceIds = [0, 1, 2, 3, 4, 5]
    faceLocations.InsertNextCell(6, faceIds)

    ## Insert the polyhedron cell   
    cells = vtkCellArray()
    cells.InsertNextCell(8, pointIds)

    ## Insert the type of the cell
    cellTypes = vtkUnsignedCharArray()
    cellTypes.InsertNextValue(VTK_POLYHEDRON);

    # Create hexahedron 

    ## Create points in hexahedron order
    points.InsertNextPoint(-5.0, -5.0, 15.0)
    points.InsertNextPoint(5.0, -5.0, 15.0)
    points.InsertNextPoint(5.0, 5.0, 15.0)
    points.InsertNextPoint(-5.0, 5.0, 15.0)
    points.InsertNextPoint(-5.0, -5.0, 35.0)
    points.InsertNextPoint(5.0, -5.0, 35.0)
    points.InsertNextPoint(5.0, 5.0, 35.0)
    points.InsertNextPoint(-5.0, 5.0, 35.0)

    ## The ID of the points of the hexahedron
    pointIds = [8, 9, 10, 11, 12, 13, 14, 15]

    ## Add the ID of the "faces" for the hexahedon, its empty because hexahedron does not need faces
    ## But we still need faceLocations to have the same size as the number of cells
    faceLocations.InsertNextCell(0)

    ## Insert the hexahedron
    cells.InsertNextCell(8, pointIds)

    ## Insert the cell type
    cellTypes.InsertNextValue(VTK_HEXAHEDRON);

    ## Set points and polyhedral cells
    ugrid0 = vtkUnstructuredGrid()
    ugrid0.SetPoints(points);
    ugrid0.SetPolyhedralCells(cellTypes, cells, faceLocations, faces);

    # Create a mapper and actor
    mapper = vtkDataSetMapper()
    mapper.SetInputData(ugrid0)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(
        colors.GetColor3d('Silver'))

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Polyhedron')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Salmon'))
    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
