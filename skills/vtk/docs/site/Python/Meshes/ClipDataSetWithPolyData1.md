<!-- source: https://examples.vtk.org/site/Python/Meshes/ClipDataSetWithPolyData1/ -->

# ClipDataSetWithPolyData1

Repository source: [ClipDataSetWithPolyData1](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Meshes/ClipDataSetWithPolyData1.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Meshes/TestClipDataSetWithPolyData1.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Meshes/TestClipDataSetWithPolyData1.png?raw=true target=)

### Description

An example that shows how to use the [vtkClipDataSet](https://www.vtk.org/doc/nightly/html/classvtkClipDataSet.html) to clip a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html) with an arbitrary polydata. [vtkImplicitPolyDataDistance](https://www.vtk.org/doc/nightly/html/classvtkImplicitPolyDataDistance.html) is used to turn the polydata into an implicit function. Every point of the grid is evaluated before sending to [vtkClipDataSet](https://www.vtk.org/doc/nightly/html/classvtkClipDataSet.html). This example uses a [vtkConeSource](https://www.vtk.org/doc/nightly/html/classvtkConeSource.html) to generate polydata to use, however any polydata could be used, including stl files.

Note

This was the original code used to make the C++ example [ClipDataSetWithPolyData](https://examples.vtk.org/site/Cxx/Meshes/ClipDataSetWithPolyData/)

Other languages

See ([PythonicAPI](../../PythonicAPI/Meshes/ClipDataSetWithPolyData1.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ClipDataSetWithPolyData1.py**

```python
#!/usr/bin/env python

import numpy as np
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkRectilinearGrid
from vtkmodules.vtkFiltersCore import vtkImplicitPolyDataDistance
from vtkmodules.vtkFiltersGeneral import vtkClipDataSet
from vtkmodules.vtkFiltersGeometry import vtkRectilinearGridGeometryFilter
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create polydata to slice the grid with. In this case, use a cone. This could
    # be any polydata including a stl file.
    cone = vtkConeSource()
    cone.SetResolution(20)
    cone.Update()

    # implicit function that will be used to slice the mesh
    implicitPolyDataDistance = vtkImplicitPolyDataDistance()
    implicitPolyDataDistance.SetInput(cone.GetOutput())

    # create a grid
    xCoords = vtkFloatArray()
    for x, i in enumerate(np.linspace(-1.0, 1.0, 15)):
        xCoords.InsertNextValue(i)

    yCoords = vtkFloatArray()
    for y, i in enumerate(np.linspace(-1.0, 1.0, 15)):
        yCoords.InsertNextValue(i)

    zCoords = vtkFloatArray()
    for z, i in enumerate(np.linspace(-1.0, 1.0, 15)):
        zCoords.InsertNextValue(i)

    # The coordinates are assigned to the rectilinear grid. Make sure that
    # the number of values in each of the XCoordinates, YCoordinates,
    # and ZCoordinates is equal to what is defined in SetDimensions().
    rgrid = vtkRectilinearGrid()
    rgrid.SetDimensions(x + 1, y + 1, z + 1)
    rgrid.SetXCoordinates(xCoords)
    rgrid.SetYCoordinates(yCoords)
    rgrid.SetZCoordinates(zCoords)

    # Create an array to hold distance information
    signedDistances = vtkFloatArray()
    signedDistances.SetNumberOfComponents(1)
    signedDistances.SetName('SignedDistances')

    # Evaluate the signed distance function at all of the grid points
    for pointId in range(rgrid.GetNumberOfPoints()):
        p = rgrid.GetPoint(pointId)
        signedDistance = implicitPolyDataDistance.EvaluateFunction(p)
        signedDistances.InsertNextValue(signedDistance)

    # add the SignedDistances to the grid
    rgrid.GetPointData().SetScalars(signedDistances)

    # use vtkClipDataSet to slice the grid with the polydata
    clipper = vtkClipDataSet()
    clipper.SetInputData(rgrid)
    clipper.InsideOutOn()
    clipper.SetValue(0.0)
    clipper.Update()

    # --- mappers, actors, render, etc. ---
    # mapper and actor to view the cone
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    # geometry filter to view the background grid
    geometryFilter = vtkRectilinearGridGeometryFilter()
    geometryFilter.SetInputData(rgrid)
    geometryFilter.SetExtent(0, x + 1, 0, y + 1, (z + 1) // 2, (z + 1) // 2)
    geometryFilter.Update()

    rgridMapper = vtkPolyDataMapper()
    rgridMapper.SetInputConnection(geometryFilter.GetOutputPort())

    wireActor = vtkActor()
    wireActor.SetMapper(rgridMapper)
    wireActor.GetProperty().SetRepresentationToWireframe()
    wireActor.GetProperty().SetColor(colors.GetColor3d('Black'))

    # mapper and actor to view the clipped mesh
    clipperMapper = vtkDataSetMapper()
    clipperMapper.SetInputConnection(clipper.GetOutputPort())

    clipperActor = vtkActor()
    clipperActor.SetMapper(clipperMapper)
    clipperActor.GetProperty().SetRepresentationToWireframe()
    clipperActor.GetProperty().SetColor(colors.GetColor3d('Black'))

    # A renderer and render window
    renderer = vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('Snow'))

    # add the actors
    # renderer.AddActor(coneActor)
    renderer.AddActor(wireActor)
    renderer.AddActor(clipperActor)

    renwin = vtkRenderWindow()
    renwin.AddRenderer(renderer)
    renwin.SetWindowName('ClipDataSetWithPolyData')

    # An interactor
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renwin)

    # Start
    interactor.Initialize()
    renwin.Render()
    renderer.GetActiveCamera().SetPosition(0, -1, 0)
    renderer.GetActiveCamera().SetFocalPoint(0, 0, 0)
    renderer.GetActiveCamera().SetViewUp(0, 0, 1)
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)
    renderer.ResetCamera()
    renwin.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
