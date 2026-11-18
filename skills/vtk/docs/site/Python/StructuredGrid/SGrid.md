<!-- source: https://examples.vtk.org/site/Python/StructuredGrid/SGrid/ -->

# SGrid

Repository source: [SGrid](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/StructuredGrid/SGrid.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/StructuredGrid/TestSGrid.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/StructuredGrid/TestSGrid.png?raw=true target=)

### Description

Creating a structured grid dataset of a semicylinder. Vectors are created whose magnitude is proportional to radius and oriented in tangential direction.

Info

See [Figure 5-19](../../VTKBook/05Chapter5.md#Figure%205-19) in [Chapter 5](../../VTKBook/05Chapter5.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/StructuredGrid/SGrid/)), ([PythonicAPI](../../PythonicAPI/StructuredGrid/SGrid.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SGrid.py**

```python
#!/usr/bin/env python3

"""
This example shows how to manually create a structured grid.
The basic idea is to instantiate vtkStructuredGrid, set its dimensions,
 and then assign points defining the grid coordinate. The number of
 points must equal the number of points implicit in the dimensions
 (i.e., dimX*dimY*dimZ). Also, data attributes (either point or cell)
 can be added to the dataset.
"""

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkDoubleArray,
    vtkMath,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import vtkStructuredGrid
from vtkmodules.vtkFiltersCore import vtkHedgeHog
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    r_min = 0.5
    r_max = 1.0
    dims = [13, 11, 11]

    # Create the structured grid.
    sgrid = vtkStructuredGrid()
    sgrid.SetDimensions(dims)

    # We also create the points and vectors. The points
    # form a hemi-cylinder of data.
    vectors = vtkDoubleArray()
    vectors.SetNumberOfComponents(3)
    vectors.SetNumberOfTuples(dims[0] * dims[1] * dims[2])
    points = vtkPoints()
    points.Reserve(dims[0] * dims[1] * dims[2])

    delta_z = 2.0 / (dims[2] - 1)
    delta_rad = (r_max - r_min) / (dims[1] - 1)
    x = [0.0] * 3
    v = [0.0] * 3
    for k in range(0, dims[2]):
        x[2] = -1.0 + k * delta_z
        k_offset = k * dims[0] * dims[1]
        for j in range(0, dims[1]):
            radius = r_min + j * delta_rad
            j_offset = j * dims[0]
            for i in range(0, dims[0]):
                theta = i * vtkMath.RadiansFromDegrees(15.0)
                x[0] = radius * math.cos(theta)
                x[1] = radius * math.sin(theta)
                v[0] = -x[1]
                v[1] = x[0]
                offset = i + j_offset + k_offset
                points.InsertPoint(offset, x)
                vectors.InsertTuple(offset, v)
    sgrid.SetPoints(points)
    sgrid.GetPointData().SetVectors(vectors)

    # We create a simple pipeline to display the data.
    hedgehog = vtkHedgeHog()
    hedgehog.SetInputData(sgrid)
    hedgehog.SetScaleFactor(0.1)

    sgrid_mapper = vtkPolyDataMapper()
    sgrid_mapper.SetInputConnection(hedgehog.GetOutputPort())
    sgrid_actor = vtkActor()
    sgrid_actor.SetMapper(sgrid_mapper)
    sgrid_actor.GetProperty().SetColor(colors.GetColor3d('Gold'))

    # Create the usual rendering stuff
    renderer = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer)
    ren_win.SetWindowName('SGrid')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    renderer.AddActor(sgrid_actor)
    renderer.SetBackground(colors.GetColor3d('MidnightBlue'))
    renderer.ResetCamera()
    renderer.GetActiveCamera().Elevation(60.0)
    renderer.GetActiveCamera().Azimuth(30.0)
    renderer.GetActiveCamera().Dolly(1.0)
    ren_win.SetSize(640, 480)

    # Interact with the data.
    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
