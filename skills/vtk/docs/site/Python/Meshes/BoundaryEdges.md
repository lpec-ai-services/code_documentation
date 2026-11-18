<!-- source: https://examples.vtk.org/site/Python/Meshes/BoundaryEdges/ -->

# BoundaryEdges

Repository source: [BoundaryEdges](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Meshes/BoundaryEdges.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Meshes/TestBoundaryEdges.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Meshes/TestBoundaryEdges.png?raw=true target=)

### Description

This filter will extract the boundary edges of a mesh. The original mesh is shown with the feature edges shown in red.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/BoundaryEdges/)), ([Java](https://examples.vtk.org/site/Java/Meshes/BoundaryEdges/)), ([CSharp](https://examples.vtk.org/site/CSharp/Meshes/BoundaryEdges/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BoundaryEdges.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkFeatureEdges
from vtkmodules.vtkFiltersSources import vtkDiskSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()
    diskSource = vtkDiskSource()
    diskSource.Update()

    featureEdges = vtkFeatureEdges()
    featureEdges.SetInputConnection(diskSource.GetOutputPort())
    featureEdges.BoundaryEdgesOn()
    featureEdges.FeatureEdgesOff()
    featureEdges.ManifoldEdgesOff()
    featureEdges.NonManifoldEdgesOff()
    featureEdges.ColoringOn()
    featureEdges.Update()

    # Visualize
    edgeMapper = vtkPolyDataMapper()
    edgeMapper.SetInputConnection(featureEdges.GetOutputPort())
    edgeActor = vtkActor()
    edgeActor.SetMapper(edgeMapper)

    diskMapper = vtkPolyDataMapper()
    diskMapper.SetInputConnection(diskSource.GetOutputPort())
    diskActor = vtkActor()
    diskActor.SetMapper(diskMapper)
    diskActor.GetProperty().SetColor(colors.GetColor3d('Gray'))

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('BoundaryEdges')

    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(edgeActor)
    renderer.AddActor(diskActor)
    renderer.SetBackground(colors.GetColor3d('DimGray'))
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
