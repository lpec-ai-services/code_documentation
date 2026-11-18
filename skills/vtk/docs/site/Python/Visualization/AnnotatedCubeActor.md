<!-- source: https://examples.vtk.org/site/Python/Visualization/AnnotatedCubeActor/ -->

# AnnotatedCubeActor

Repository source: [AnnotatedCubeActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/AnnotatedCubeActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestAnnotatedCubeActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestAnnotatedCubeActor.png?raw=true target=)

### Description

The example demonstrates how to create and label an annotated cube actor.

To colour the individual cube faces, see: [ColoredAnnotatedCube](ColoredAnnotatedCube.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/AnnotatedCubeActor/)), ([PythonicAPI](../../PythonicAPI/Visualization/AnnotatedCubeActor.md)), ([Java](https://examples.vtk.org/site/Java/Visualization/AnnotatedCubeActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AnnotatedCubeActor.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingAnnotation import vtkAnnotatedCubeActor
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Set up the renderer, window, and interactor.
    #
    ren = vtkRenderer()
    ren.SetBackground(colors.GetColor3d('Wheat'))
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(ren)
    ren_win.SetSize(640, 480)
    ren_win.SetWindowName('AnnotatedCubeActor')
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    cube = vtkAnnotatedCubeActor()
    cube.SetFaceTextScale(2.0 / 3.0)

    # Anatomic labelling.
    #
    cube.SetXPlusFaceText('A')
    cube.SetXMinusFaceText('P')
    cube.SetYPlusFaceText('L')
    cube.SetYMinusFaceText('R')
    cube.SetZPlusFaceText('S')
    cube.SetZMinusFaceText('I')

    # Change the vector text colors.
    #
    cube.GetTextEdgesProperty().SetColor(
        colors.GetColor3d('Black'))
    cube.GetTextEdgesProperty().SetLineWidth(4)

    cube.GetXPlusFaceProperty().SetColor(
        colors.GetColor3d('Turquoise'))
    cube.GetXMinusFaceProperty().SetColor(
        colors.GetColor3d('Turquoise'))
    cube.GetYPlusFaceProperty().SetColor(
        colors.GetColor3d('Mint'))
    cube.GetYMinusFaceProperty().SetColor(
        colors.GetColor3d('Mint'))
    cube.GetZPlusFaceProperty().SetColor(
        colors.GetColor3d('Tomato'))
    cube.GetZMinusFaceProperty().SetColor(
        colors.GetColor3d('Tomato'))

    ren.AddActor(cube)

    # Set up an interesting view.
    #
    camera = ren.GetActiveCamera()
    camera.SetViewUp(0, 0, 1)
    camera.SetFocalPoint(0, 0, 0)
    camera.SetPosition(4.5, 4.5, 2.5)
    ren.ResetCamera()
    camera.Dolly(1.0)
    ren.ResetCameraClippingRange()

    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
