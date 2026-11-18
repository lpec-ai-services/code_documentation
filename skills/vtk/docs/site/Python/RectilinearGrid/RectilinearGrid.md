<!-- source: https://examples.vtk.org/site/Python/RectilinearGrid/RectilinearGrid/ -->

# RectilinearGrid

Repository source: [RectilinearGrid](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/RectilinearGrid/RectilinearGrid.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/RectilinearGrid/TestRectilinearGrid.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/RectilinearGrid/TestRectilinearGrid.png?raw=true target=)

### Description

Shows how to create a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/RectilinearGrid/RectilinearGrid/)), ([Java](https://examples.vtk.org/site/Java/RectilinearGrid/RectilinearGrid/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RectilinearGrid.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkDoubleArray
from vtkmodules.vtkCommonDataModel import vtkRectilinearGrid
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create a grid
    grid = vtkRectilinearGrid()
    grid.SetDimensions(2, 3, 1)

    xArray = vtkDoubleArray()
    xArray.InsertNextValue(0.0)
    xArray.InsertNextValue(2.0)

    yArray = vtkDoubleArray()
    yArray.InsertNextValue(0.0)
    yArray.InsertNextValue(1.0)
    yArray.InsertNextValue(2.0)

    zArray = vtkDoubleArray()
    zArray.InsertNextValue(0.0)

    grid.SetXCoordinates(xArray)
    grid.SetYCoordinates(yArray)
    grid.SetZCoordinates(zArray)

    print('There are', grid.GetNumberOfPoints(), 'points.')
    print('There are', grid.GetNumberOfCells(), 'cells.')

    for id in range(0, grid.GetNumberOfPoints()):
        p = [0] * 3
        p = grid.GetPoint(id)
        print('Point', id, ':(', p[0], ',', p[1], ',', p[2], ')')

    # Create a mapper and actor
    mapper = vtkDataSetMapper()
    mapper.SetInputData(grid)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('PeachPuff'))

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('RectilinearGrid')

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))

    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
