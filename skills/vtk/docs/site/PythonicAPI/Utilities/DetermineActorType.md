<!-- source: https://examples.vtk.org/site/PythonicAPI/Utilities/DetermineActorType/ -->

# DetermineActorType

Repository source: [DetermineActorType](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Utilities/DetermineActorType.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Utilities/TestDetermineActorType.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Utilities/TestDetermineActorType.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Utilities/DetermineActorType/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DetermineActorType.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkSphereSource,
)
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

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    ren_win = vtkRenderWindow(window_name='DetermineActorType')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    # Create a sphere.
    sphere_source = vtkSphereSource()
    mapper = vtkPolyDataMapper()
    sphere_source >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # Cube axes.
    cube_axes_actor = vtkCubeAxesActor(camera=ren.active_camera)

    cube_axes_actor.x_axes_title_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.y_axes_title_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.z_axes_title_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.x_axes_lines_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.y_axes_lines_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.z_axes_lines_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.x_axes_label_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.y_axes_label_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.z_axes_label_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.x_axes_gridlines_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.y_axes_gridlines_property.color = colors.GetColor3d('Gold')
    cube_axes_actor.z_axes_gridlines_property.color = colors.GetColor3d('Gold')

    cube_axes_actor.draw_x_gridlines = False
    cube_axes_actor.draw_y_gridlines = False
    cube_axes_actor.draw_z_gridlines = False
    cube_axes_actor.grid_line_location = vtkCubeAxesActor.VTK_GRID_LINES_FURTHEST

    cube_axes_actor.x_axis_minor_tick_visibility = True
    cube_axes_actor.y_axis_minor_tick_visibility = True
    cube_axes_actor.z_axis_minor_tick_visibility = True

    # cube_axes_actor.fly_mode = vtkCubeAxesActor.VTK_FLY_STATIC_EDGES

    ren.AddActor(actor)
    ren.AddActor(cube_axes_actor)

    wanted_class = 'vtkCubeAxesActor'
    actor_collection = ren.actors

    # Determine the types of the actors - method 1.
    print('Method 1:')
    actor_collection.InitTraversal()
    for i in range(0, actor_collection.number_of_items):
        next_actor = actor_collection.next_item
        class_name = next_actor.GetClassName()
        print(f'next_actor {i} : {class_name}')
        if class_name == wanted_class:
            print(f'next_actor {i} is a {wanted_class}')
        else:
            print(f'next_actor {i} is not a {wanted_class}')
    print()

    # Determine the types of the actors - method 2.
    print('Method 2:')
    actor_collection.InitTraversal()
    for i in range(0, actor_collection.number_of_items):
        next_actor = actor_collection.next_item
        print(f'next_actor {i} : {next_actor.GetClassName()}')
        if next_actor.IsA(wanted_class):
            print(f'next_actor {i} is a {wanted_class}')
        else:
            print(f'next_actor {i} is not a {wanted_class}')
    print()

    # Determine the types of the actors - method 3.
    print('Method 3:')
    actor_collection.InitTraversal()
    for i in range(0, actor_collection.number_of_items):
        next_actor = actor_collection.next_item
        print(f'next_actor {i} : {next_actor.GetClassName()}')
        if type(next_actor) is wanted_class:
            print(f'next_actor {i} is a {wanted_class}')
        else:
            print(f'next_actor {i} is not a {wanted_class}')

    ren_win.Render()
    camera = ren.GetActiveCamera()
    camera.position = (0, 0, 8.09748)
    camera.focal_point = (0, 0, 0)
    camera.view_up = (0, 1, 0)
    camera.distance = 8.09748
    camera.clipping_range = (6.0265, 10.7239)
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
