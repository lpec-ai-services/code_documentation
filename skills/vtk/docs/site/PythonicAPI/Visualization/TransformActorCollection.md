<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/TransformActorCollection/ -->

# TransformActorCollection

Repository source: [TransformActorCollection](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/TransformActorCollection.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestTransformActorCollection.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestTransformActorCollection.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/TransformActorCollection/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TransformActorCollection.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkCubeSource,
    vtkSphereSource,
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkActorCollection,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(window_name='TransformActorCollection')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Create a cone.
    cone_source = vtkConeSource(height=3)
    cone_mapper = vtkPolyDataMapper()
    cone_source >> cone_mapper
    cone_actor = vtkActor(mapper=cone_mapper)
    cone_actor.property.color = colors.GetColor3d('MistyRose')

    # Create a cube.
    cube_source = vtkCubeSource(center=(0.0, 0.0, 0.0))
    cube_mapper = vtkPolyDataMapper()
    cube_source >> cube_mapper
    cube_actor = vtkActor(mapper=cube_mapper)
    cube_actor.property.color = colors.GetColor3d('Cornsilk')

    # Create a sphere.
    sphere_source = vtkSphereSource()
    sphere_mapper = vtkPolyDataMapper()
    sphere_source >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.color = colors.GetColor3d('Lavender')

    # Add the cube and cone into a collection.
    actor_collection = vtkActorCollection()
    actor_collection.AddItem(cube_actor)
    actor_collection.AddItem(cone_actor)
    actor_collection.InitTraversal()

    # Apply a transform to each actor in the collection.
    transform = vtkTransform()
    transform.PostMultiply()  # This is the key line.
    transform.Translate(5.0, 0, 0)

    actor_collection.InitTraversal()
    for i in range(0, actor_collection.number_of_items):
        actor = actor_collection.next_actor
        actor.user_transform = transform
        # Of course, we can modify the properties of
        # individual actors, the cube in this case.
        if i == 0:
            actor.property.opacity = 0.8
        ren.AddActor(actor)

    ren.AddActor(sphere_actor)

    ren_win.Render()
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
