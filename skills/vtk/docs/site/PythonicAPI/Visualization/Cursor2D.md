<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/Cursor2D/ -->

# Cursor2D

Repository source: [Cursor2D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/Cursor2D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCursor2D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCursor2D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/Cursor2D/)), ([Java](https://examples.vtk.org/site/Java/Visualization/Cursor2D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Cursor2D.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeneral import vtkCursor2D
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Create a sphere.
    sphere_source = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=5.0)

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    render_window = vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.window_name = 'Cursor2D'

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actor to the scene.
    renderer.AddActor(actor)

    cursor = vtkCursor2D(model_bounds=(-10, 10, -10, 10, 0, 0), focal_point=(5.0, 5.0, 0.0))
    cursor.AllOn()
    cursor.OutlineOn()

    cursor_mapper = vtkPolyDataMapper(input_connection=cursor.output_port)
    cursor >> cursor_mapper
    cursor_actor = vtkActor(mapper=cursor_mapper)
    cursor_actor.property.color = colors.GetColor3d('Red')

    renderer.AddActor(cursor_actor)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
