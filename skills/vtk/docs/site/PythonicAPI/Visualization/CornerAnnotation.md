<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/CornerAnnotation/ -->

# CornerAnnotation

Repository source: [CornerAnnotation](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/CornerAnnotation.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCornerAnnotation.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCornerAnnotation.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/CornerAnnotation/)), ([Java](https://examples.vtk.org/site/Java/Visualization/CornerAnnotation/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CornerAnnotation.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingAnnotation import vtkCornerAnnotation
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # Visualize
    renderer = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    render_window = vtkRenderWindow(window_name='CornerAnnotation')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    corner_annotation = vtkCornerAnnotation(linear_font_scale_factor=2, nonlinear_font_scale_factor=1,
                                            maximum_font_size=20)
    corner_annotation.SetText(0, 'lower left')
    corner_annotation.SetText(1, 'lower right')
    corner_annotation.SetText(2, 'upper left')
    corner_annotation.SetText(3, 'upper right')
    corner_annotation.GetTextProperty().color = colors.GetColor3d('Gold')

    renderer.AddViewProp(corner_annotation)

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
