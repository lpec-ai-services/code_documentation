<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/PlatonicSolids/ -->

# PlatonicSolids

Repository source: [PlatonicSolids](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/PlatonicSolids.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPlatonicSolids.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestPlatonicSolids.png?raw=true target=)

### Description

Display all five Platonic solids in a grid.

Platonic solids are regular, convex polyhedrons. They are constructed by congruent (identical in shape and size) regular (all angles equal and all sides equal) polygonal faces with the same number of faces meeting at each vertex.

Five solids satisfy the above criteria:

| Figure | Tetrahedron | Cube | Octahedron | Icosahedron | Dodecahedron |
| --- | --- | --- | --- | --- | --- |
| Vertices | 4 | 8 | 6 (2 × 3) | 12 (4 × 3) | 20 (8 + 4 × 3) |
| Edges | 6 | 12 | 12 | 30 | 30 |
| Faces | 4 | 6 | 8 | 20 | 12 |

The relationship between vertices, edges and faces is given by Euler's formula:

```python
V - E + F = 2
```

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/PlatonicSolids/)), ([PythonicAPI](../../PythonicAPI/GeometricObjects/PlatonicSolids.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PlatonicSolids.py**

```python
#!/usr/bin/env python

from collections import namedtuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkFiltersSources import vtkPlatonicSolidSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkActor2D,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextMapper,
    vtkTextProperty
)

def main():
    colors = vtkNamedColors()

    mappers = list()
    actors = list()
    text_mappers = list()
    text_actors = list()
    renderers = list()

    # Create a common text property.
    text_property = vtkTextProperty()
    text_property.SetFontSize(16)
    text_property.SetJustificationToCentered()

    # Create the render window and interactor.
    ren_win = vtkRenderWindow()
    ren_win.SetWindowName('PlatonicSolids')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    name_orientation = get_name_orientation()
    lut = get_platonic_lut()
    platonic_solids = list()

    for i in range(0, len(name_orientation)):
        platonic_solids.append(vtkPlatonicSolidSource())
        platonic_solids[i].SetSolidType(i)

        mappers.append(vtkPolyDataMapper())
        mappers[i].SetInputConnection(platonic_solids[i].GetOutputPort())
        mappers[i].SetLookupTable(lut)
        mappers[i].SetScalarRange(0, 19)

        actors.append(vtkActor())
        actors[i].SetMapper(mappers[i])

        text_mappers.append(vtkTextMapper())
        text_mappers[i].SetInput(name_orientation[i].name)
        text_mappers[i].SetTextProperty(text_property)

        text_actors.append(vtkActor2D())
        text_actors[i].SetMapper(text_mappers[i])
        text_actors[i].SetPosition(120, 16)

        renderers.append(vtkRenderer())
        renderers[i].AddActor(actors[i])
        renderers[i].AddViewProp(text_actors[i])

        ren_win.AddRenderer(renderers[i])

    # Set up the viewports.
    grid_dimension_x = 3
    grid_dimension_y = 2
    renderer_size = 300
    ren_win.SetSize(renderer_size * grid_dimension_x, renderer_size * grid_dimension_y)
    for row in range(0, grid_dimension_y):
        for col in range(0, grid_dimension_x):
            index = row * grid_dimension_x + col

            # (x_min, y_min, x_max, y_max)
            viewport = [float(col) / grid_dimension_x,
                        float(grid_dimension_y - (row + 1)) / grid_dimension_y,
                        float(col + 1) / grid_dimension_x,
                        float(grid_dimension_y - row) / grid_dimension_y]

            if index > (len(actors) - 1):
                # Add a renderer even if there is no actor.
                # This makes the render window background all the same color.
                ren = vtkRenderer()
                ren.SetBackground(colors.GetColor3d('SlateGray'))
                ren.SetViewport(viewport)
                ren_win.AddRenderer(ren)
                continue

            renderers[index].SetViewport(viewport)
            renderers[index].SetBackground(colors.GetColor3d('SlateGray'))
            renderers[index].ResetCamera()
            renderers[index].GetActiveCamera().Azimuth(name_orientation[index].azimuth)
            renderers[index].GetActiveCamera().Elevation(name_orientation[index].elevation)
            renderers[index].GetActiveCamera().Zoom(name_orientation[index].zoom)
            renderers[index].ResetCameraClippingRange()

    iren.Initialize()
    ren_win.Render()
    iren.Start()

def get_name_orientation():
    """
    Get the platonic solid names and initial orientations.

    :return: The solids and their initial orientations.
    """

    # [[name, azimuth, elevation, zoom] ...]
    res = [['Tetrahedron', 45.0, 30.0, 1.0],
           ['Cube', -60.0, 45.0, 0.8],
           ['Octahedron', -15.0, 10.0, 1.0],
           ['Icosahedron', 4.5, 18.0, 1.0],
           ['Dodecahedron', 171.0, 22.0, 1.0]]

    platonic_solids = namedtuple('platonic_solids', ('name', 'azimuth', 'elevation', 'zoom'))
    # Convert res to a list of named tuples.
    res = [platonic_solids(*row) for row in res]
    return res

def get_platonic_lut():
    """
    Get a specialised lookup table for the platonic solids.

    Since each face of a vtkPlatonicSolidSource has a different
    cell scalar, we create a lookup table with a different colour
    for each face.
    The colors have been carefully chosen so that adjacent cells
    are colored distinctly.

    :return: The lookup table.
    """
    lut = vtkLookupTable()
    lut.SetNumberOfTableValues(20)
    lut.SetTableRange(0.0, 19.0)
    lut.Build()
    lut.SetTableValue(0, 0.1, 0.1, 0.1)
    lut.SetTableValue(1, 0, 0, 1)
    lut.SetTableValue(2, 0, 1, 0)
    lut.SetTableValue(3, 0, 1, 1)
    lut.SetTableValue(4, 1, 0, 0)
    lut.SetTableValue(5, 1, 0, 1)
    lut.SetTableValue(6, 1, 1, 0)
    lut.SetTableValue(7, 0.9, 0.7, 0.9)
    lut.SetTableValue(8, 0.5, 0.5, 0.5)
    lut.SetTableValue(9, 0.0, 0.0, 0.7)
    lut.SetTableValue(10, 0.5, 0.7, 0.5)
    lut.SetTableValue(11, 0, 0.7, 0.7)
    lut.SetTableValue(12, 0.7, 0, 0)
    lut.SetTableValue(13, 0.7, 0, 0.7)
    lut.SetTableValue(14, 0.7, 0.7, 0)
    lut.SetTableValue(15, 0, 0, 0.4)
    lut.SetTableValue(16, 0, 0.4, 0)
    lut.SetTableValue(17, 0, 0.4, 0.4)
    lut.SetTableValue(18, 0.4, 0, 0)
    lut.SetTableValue(19, 0.4, 0, 0.4)
    return lut

if __name__ == '__main__':
    main()
```
