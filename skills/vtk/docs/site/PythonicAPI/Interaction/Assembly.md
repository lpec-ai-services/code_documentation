<!-- source: https://examples.vtk.org/site/PythonicAPI/Interaction/Assembly/ -->

# Assembly

Repository source: [Assembly](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Interaction/Assembly.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestAssembly.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Interaction/TestAssembly.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Interaction/Assembly/)), ([Java](https://examples.vtk.org/site/Java/Interaction/Assembly/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Assembly.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersSources import (
    vtkCubeSource,
    vtkSphereSource,
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkAssembly,
    vtkPolyDataMapper,
    vtkPropCollection,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(window_name='Assembly')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Create a sphere.
    sphere_source = vtkSphereSource()
    sphere_mapper = vtkPolyDataMapper()
    sphere_source >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.color = colors.GetColor3d('Banana')

    # Create a cube.
    cube_source = vtkCubeSource(center=(5.0, 0.0, 0.0))
    cube_mapper = vtkPolyDataMapper()
    cube_source >> cube_mapper
    cube_actor = vtkActor(mapper=cube_mapper)
    cube_actor.property.color = colors.GetColor3d('Tomato')

    # Combine the sphere and cube into an assembly.
    assembly = vtkAssembly()
    assembly.AddPart(sphere_actor)
    assembly.AddPart(cube_actor)

    # Apply a transform to the whole assembly.
    transform = vtkTransform()
    transform.PostMultiply()  # This is the key line.
    transform.Translate(5.0, 0, 0)

    assembly.user_transform = transform

    # Extract each actor from the assembly and change its opacity.
    collection = vtkPropCollection()

    assembly.GetActors(collection)
    collection.InitTraversal()
    for i in range(0, collection.number_of_items):
        collection.next_prop.property.opacity = 0.5

    ren.AddActor(assembly)
    ren_win.Render()
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
