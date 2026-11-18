<!-- source: https://examples.vtk.org/site/PythonicAPI/Filtering/ExtractVisibleCells/ -->

# ExtractVisibleCells

Repository source: [ExtractVisibleCells](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Filtering/ExtractVisibleCells.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestExtractVisibleCells.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestExtractVisibleCells.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/ExtractVisibleCells/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractVisibleCells.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkDataObject
from vtkmodules.vtkFiltersExtraction import vtkExtractSelection
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkHardwareSelector,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def main():
    colors = vtkNamedColors()

    # Create a sphere
    sphere_source = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=5.0)
    sphere_source.update()

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('Tomato')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('Mint'))
    # Turn off antialiasing
    render_window = vtkRenderWindow(multi_samples=0, window_name='ExtractVisibleCells')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    style = KeyPressInteractorStyle(sphere_source.output, renderer)
    style.current_renderer = renderer
    render_window_interactor.interactor_style = style

    # Add the actor to the scene.
    renderer.AddActor(actor)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

class KeyPressInteractorStyle(vtkInteractorStyleTrackballCamera):

    def __init__(self, pd, renderer):
        super().__init__()
        self.pd = pd
        self.renderer = renderer
        self.colors = vtkNamedColors()
        self.AddObserver('KeyPressEvent', self.key_press_event)

    def key_press_event(self, obj, event):
        key = self.GetInteractor().GetKeySym().lower()
        # 's' for 's'elect
        if key == 's':
            selector = vtkHardwareSelector()
            selector.SetRenderer(self.interactor.render_window.renderers.first_renderer)
            # The size (width and height) in pixels.
            temp = self.interactor.render_window.size
            # [xmin, ymin, xmax, ymax]
            window_size = [1] * 4
            window_size[2] = temp[0] - 1
            window_size[3] = temp[1] - 1

            selector.SetArea(window_size)
            selector.SetFieldAssociation(vtkDataObject.FIELD_ASSOCIATION_CELLS)
            selection = selector.Select()
            print(f'Selection has {selection.number_of_nodes} nodes.')

            extract_selection = vtkExtractSelection()
            self.pd >> select_ports(0, extract_selection)
            selection >> select_ports(1, extract_selection)

            mapper = vtkDataSetMapper()
            extract_selection >> mapper

            actor = vtkActor(mapper=mapper)
            actor.property.color = self.colors.GetColor3d('Red')
            self.renderer.AddActor(actor)

            # Forward events
            super().OnKeyPress()

if __name__ == '__main__':
    main()
```
