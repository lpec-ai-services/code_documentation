<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/ReverseAccess/ -->

# ReverseAccess

Repository source: [ReverseAccess](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/ReverseAccess.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/ReverseAccess/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReverseAccess.py**

```python
#!/usr/bin/env python3

"""
 This example demonstrates how to access the source object
 (e.g. vtkSphereSource) from the actor reversely.
"""

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
# This may be needed in some cases.
# from vtkmodules.vtkCommonExecutionModel import vtkAlgorithmOutput
from vtkmodules.vtkFiltersSources import (
    vtkSphereSource,
)
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
    ren = vtkRenderer(background=colors.GetColor3d('CadetBlue'))
    ren_win = vtkRenderWindow(size=(300, 300), window_name='ReverseAccess')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Create a sphere.
    sphere_source = vtkSphereSource(radius=0.5)
    sphere_mapper = vtkPolyDataMapper()
    sphere_source >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.color = colors.GetColor3d('MistyRose')

    ren.AddActor(sphere_actor)

    """
      Now we retrieve the source object from vtkActor reversely, meaning we
       don't use the sphere source object we instantiated above directly,
       instead we retrieve a reference to the sphere source through the actor.
      An advantage of this concept might be that we don't need to maintain
       the source object anymore in a more complex application.
      To demonstrate that we can modify properties of the sphere source
       through this reference beside changing some properties of the actor
       (in this example we change actor's x-position), we change the radius
       of the sphere source as well.

      The next two lines are the core lines for reverse access.
    """
    algorithm = sphere_actor.mapper.GetInputConnection(0, 0).producer
    src_reference = algorithm
    orig_radius = src_reference.radius
    for i in range(0, 360):
        # Change the radius of the sphere.
        src_reference.radius = orig_radius * (1 + math.sin(i / 180.0 * math.pi))
        # Change the x-position of the actor.
        sphere_actor.position = (math.sin(i / 45.0 * math.pi) * 0.5, 0, 0)
        ren_win.Render()

if __name__ == '__main__':
    main()
```
