<!-- source: https://examples.vtk.org/site/PythonicAPI/Picking/AreaPicking/ -->

# AreaPicking

Repository source: [AreaPicking](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Picking/AreaPicking.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Picking/TestAreaPicking.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Picking/TestAreaPicking.png?raw=true target=)

### Description

This example creates 3 points+vertices. Currently, the address of the picked prop is 0 (this is not correct). A red bounding box is drawn around every picked prop.

- For `[vtkInteractorStyleTrackballCamera](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyleTrackballCamera.html)` - use 'p' to pick at the current mouse position
- For `[vtkInteractorStyleRubberBandPick](https://www.vtk.org/doc/nightly/html/classvtkInteractorStyleRubberBandPick.html)` - use 'r' and left-mouse to draw a selection box used to pick

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Picking/AreaPicking/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AreaPicking.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData, vtkVertex
)
# noinspection PyUnresolvedReferences
from vtkmodules.vtkInteractionStyle import (
    vtkInteractorStyleRubberBandPick,
    vtkInteractorStyleTrackballCamera
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkPolyDataMapper, vtkAreaPicker
)

def main():
    colors = vtkNamedColors()

    # Create a set of points.
    points = vtkPoints()
    vertex = vtkVertex()
    vertices = vtkCellArray()

    points.InsertNextPoint(1.0, 0.0, 0.0)
    vertex.point_ids.SetId(0, 0)
    vertices.InsertNextCell(vertex)
    points.InsertNextPoint(0.0, 0.0, 0.0)
    vertex.point_ids.SetId(0, 1)
    vertices.InsertNextCell(vertex)
    points.InsertNextPoint(0.0, 1.0, 0.0)
    vertex.point_ids.SetId(0, 2)
    vertices.InsertNextCell(vertex)

    # Create a polydata.
    polydata = vtkPolyData(points=points, verts=vertices)

    # Visualize
    mapper = vtkPolyDataMapper(input_data=polydata)

    actor = vtkActor(mapper=mapper)
    actor.property.point_size = 8
    actor.property.color = colors.GetColor3d('Gold')

    renderer = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    render_window = vtkRenderWindow(window_name='AreaPicking')
    render_window.AddRenderer(renderer)

    renderer.AddActor(actor)

    render_window.Render()

    area_picker = vtkAreaPicker()

    iren = vtkRenderWindowInteractor()
    iren.render_window = render_window
    iren.picker = area_picker

    # For vtkInteractorStyleRubberBandPick - use 'r' and left-mouse to draw a
    # selection box used to pick.
    style = vtkInteractorStyleRubberBandPick(current_renderer=renderer)

    # For vtkInteractorStyleTrackballCamera - use 'p' to pick at the current
    # mouse position.
    # style = vtkInteractorStyleTrackballCamera(current_renderer=renderer)

    iren.interactor_style = style

    area_picker.AddObserver('EndPickEvent', pick_callback_function)

    iren.Start()

def pick_callback_function(caller, ev):
    def print_floats(float_list):
        return ', '.join([f'{element:5.2f}' for element in float_list])

    print('Pick.')
    area_picker = caller
    props = area_picker.GetProp3Ds()
    props.InitTraversal()

    for i in range(0, props.GetNumberOfItems()):
        prop = props.GetNextProp3D()
        position = prop.GetPosition()
        center = prop.GetCenter()
        print(f'position: {print_floats(position)}, center: {print_floats(center)}')

if __name__ == '__main__':
    main()
```
