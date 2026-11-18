<!-- source: https://examples.vtk.org/site/Python/Filtering/CombinePolyData/ -->

# CombinePolyData

Repository source: [CombinePolyData](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Filtering/CombinePolyData.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Filtering/TestCombinePolyData.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Filtering/TestCombinePolyData.png?raw=true target=)

### Description

This example reads two .vtp files (or produces them if not specified as command line arguments), combines them, and displays the result to the screen.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/CombinePolyData/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CombinePolyData.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import (
    vtkAppendPolyData,
    vtkCleanPolyData
)
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkSphereSource
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor('BkgColor', [0.3, 0.2, 0.1, 1.0])

    input1 = vtkPolyData()
    input2 = vtkPolyData()

    sphereSource = vtkSphereSource()
    sphereSource.SetCenter(5, 0, 0)
    sphereSource.Update()

    input1.ShallowCopy(sphereSource.GetOutput())

    coneSource = vtkConeSource()
    coneSource.Update()

    input2.ShallowCopy(coneSource.GetOutput())

    # Append the two meshes
    appendFilter = vtkAppendPolyData()
    appendFilter.AddInputData(input1)
    appendFilter.AddInputData(input2)

    appendFilter.Update()

    #  Remove any duplicate points.
    cleanFilter = vtkCleanPolyData()
    cleanFilter.SetInputConnection(appendFilter.GetOutputPort())
    cleanFilter.Update()

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cleanFilter.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)

    # Render and interact
    renderWindowInteractor.Initialize()
    renderWindow.Render()
    renderWindow.SetWindowName('CombinePolyData')
    renderer.SetBackground(colors.GetColor3d('deep_ochre'))
    renderer.GetActiveCamera().Zoom(0.9)
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
