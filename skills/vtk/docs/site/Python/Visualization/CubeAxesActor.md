<!-- source: https://examples.vtk.org/site/Python/Visualization/CubeAxesActor/ -->

# CubeAxesActor

Repository source: [CubeAxesActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/CubeAxesActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestCubeAxesActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestCubeAxesActor.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/CubeAxesActor/)), ([PythonicAPI](../../PythonicAPI/Visualization/CubeAxesActor.md)), ([Java](https://examples.vtk.org/site/Java/Visualization/CubeAxesActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CubeAxesActor.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSuperquadricSource
from vtkmodules.vtkRenderingAnnotation import vtkCubeAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    backgroundColor = colors.GetColor3d("DarkSlateGray")
    actorColor = colors.GetColor3d("Tomato")
    axis1Color = colors.GetColor3d("Salmon")
    axis2Color = colors.GetColor3d("PaleGreen")
    axis3Color = colors.GetColor3d("LightSkyBlue")

    # Create a superquadric
    superquadricSource = vtkSuperquadricSource()
    superquadricSource.SetPhiRoundness(3.1)
    superquadricSource.SetThetaRoundness(1.0)
    superquadricSource.Update()  # needed to GetBounds later

    renderer = vtkRenderer()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(superquadricSource.GetOutputPort())

    superquadricActor = vtkActor()
    superquadricActor.SetMapper(mapper)
    superquadricActor.GetProperty().SetDiffuseColor(actorColor)
    superquadricActor.GetProperty().SetDiffuse(.7)
    superquadricActor.GetProperty().SetSpecular(.7)
    superquadricActor.GetProperty().SetSpecularPower(50.0)

    cubeAxesActor = vtkCubeAxesActor()
    cubeAxesActor.SetUseTextActor3D(1)
    cubeAxesActor.SetBounds(superquadricSource.GetOutput().GetBounds())
    cubeAxesActor.SetCamera(renderer.GetActiveCamera())

    cubeAxesActor.GetTitleTextProperty(0).SetColor(axis1Color)
    cubeAxesActor.GetTitleTextProperty(0).SetFontSize(18)
    cubeAxesActor.GetLabelTextProperty(0).SetColor(axis1Color)
    cubeAxesActor.DrawXGridlinesOn()
    cubeAxesActor.XAxisMinorTickVisibilityOff()

    cubeAxesActor.GetTitleTextProperty(1).SetColor(axis2Color)
    cubeAxesActor.GetTitleTextProperty(1).SetFontSize(18)
    cubeAxesActor.GetLabelTextProperty(1).SetColor(axis2Color)
    cubeAxesActor.DrawYGridlinesOn()
    cubeAxesActor.YAxisMinorTickVisibilityOff()

    cubeAxesActor.GetTitleTextProperty(2).SetColor(axis3Color)
    cubeAxesActor.GetTitleTextProperty(2).SetFontSize(18)
    cubeAxesActor.GetLabelTextProperty(2).SetColor(axis3Color)
    cubeAxesActor.DrawZGridlinesOn()
    cubeAxesActor.ZAxisMinorTickVisibilityOff()

    cubeAxesActor.SetGridLineLocation(cubeAxesActor.VTK_GRID_LINES_FURTHEST)
    cubeAxesActor.SetFlyModeToStaticEdges()

    renderer.AddActor(cubeAxesActor)
    renderer.AddActor(superquadricActor)
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(30)

    renderer.ResetCamera()
    renderer.SetBackground(backgroundColor)

    renderWindow = vtkRenderWindow()

    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(640, 480)
    renderWindow.SetWindowName('CubeAxesActor')

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    renderer.GetActiveCamera().Zoom(0.8)
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
```
