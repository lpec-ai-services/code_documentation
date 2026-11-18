<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/RubberBand3D/ -->

# RubberBand3D

Repository source: [RubberBand3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/RubberBand3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestRubberBand3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestRubberBand3D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/RubberBand3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**RubberBand3D.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleRubberBand3D
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='RubberBand3D')
    render_window.AddRenderer(renderer)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(actor)

    render_window.Render()

    style = MyRubberBand3D()
    render_window_interactor.interactor_style = style

    # Begin the mouse interaction.
    render_window_interactor.Start()

class MyRubberBand3D(vtkInteractorStyleRubberBand3D):
    def __init__(self, parent=None):
        super().__init__()
        self.AddObserver('LeftButtonReleaseEvent', self.OnLeftButtonUp)

    def OnLeftButtonUp(self, obj=None, event=None):
        # Forward events.
        super().OnLeftButtonUp()
        print(f'Start position: ({fmt_floats(self.start_position)})')
        print(f'End position:   ({fmt_floats(self.end_position)})')

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

if __name__ == '__main__':
    main()
```
