<!-- source: https://examples.vtk.org/site/Python/GeometricObjects/TextActor/ -->

# TextActor

Repository source: [TextActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/GeometricObjects/TextActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTextActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/GeometricObjects/TestTextActor.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/TextActor/)), ([Java](https://examples.vtk.org/site/Java/GeometricObjects/TextActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TextActor.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextActor
)

def main():
    colors = vtkNamedColors()

    # Create a rendering window and renderer.
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.SetWindowName('TextActor')
    renWin.AddRenderer(ren)

    # Create a render window interactor.
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Create a text actor.
    txt = vtkTextActor()
    txt.SetInput('Hello World!')
    txtprop = txt.GetTextProperty()
    txtprop.SetFontFamilyToArial()
    txtprop.BoldOn()
    txtprop.SetFontSize(36)
    txtprop.ShadowOn()
    txtprop.SetShadowOffset(4, 4)
    txtprop.SetColor(colors.GetColor3d('Cornsilk'))
    txt.SetDisplayPosition(20, 30)

    # Assign actor to the renderer.
    ren.AddActor(txt)
    ren.SetBackground(colors.GetColor3d('DarkGreen'))

    # Enable user interface interactor.
    iren.Initialize()
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
