<!-- source: https://examples.vtk.org/site/PythonicAPI/ImplicitFunctions/BooleanOperationImplicitFunctions/ -->

# BooleanOperationImplicitFunctions

Repository source: [BooleanOperationImplicitFunctions](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImplicitFunctions/BooleanOperationImplicitFunctions.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImplicitFunctions/TestBooleanOperationImplicitFunctions.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImplicitFunctions/TestBooleanOperationImplicitFunctions.png?raw=true target=)

### Description

Demonstration on how to perform boolean operations with implicit functions.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImplicitFunctions/BooleanOperationImplicitFunctions/)), ([Python](../../Python/ImplicitFunctions/BooleanOperationImplicitFunctions.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BooleanOperationImplicitFunctions.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkBox,
    vtkImplicitBoolean,
    vtkSphere
)
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkImagingHybrid import vtkSampleFunction
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create a sphere.
    sphere = vtkSphere(radius=1.0, center=(1, 0, 0))

    # Create a box.
    box = vtkBox(bounds=(-1, 1, -1, 1, -1, 1))

    # Combine the two implicit functions.
    # You can also experiment with operation types of VTK_UNION or VTK_INTERSECTION.
    boolean = vtkImplicitBoolean(operation_type=vtkImplicitBoolean.VTK_DIFFERENCE)
    boolean.AddFunction(box)
    boolean.AddFunction(sphere)

    # The sample function generates a distance function from the implicit
    # function. This is then contoured to get a polygonal surface.
    sample = vtkSampleFunction(implicit_function=boolean, model_bounds=(-1, 2, -1, 1, -1, 1),
                               sample_dimensions=(40, 40, 40), compute_normals=False)

    # Contour
    surface = vtkContourFilter()
    surface.SetValue(0, 0.0)

    # Mapper
    mapper = vtkPolyDataMapper(scalar_visibility=False)
    sample >> surface >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.edge_visibility = True
    actor.property.color = colors.GetColor3d('AliceBlue')
    actor.property.edge_color = colors.GetColor3d('SteelBlue')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    renwin = vtkRenderWindow(window_name='BooleanOperationImplicitFunctions')
    renwin.AddRenderer(renderer)

    # Add the actor.
    renderer.AddActor(actor)

    # An interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = renwin

    # Start
    interactor.Initialize()
    renwin.Render()

    renderer.active_camera.SetPosition(5.0, -4.0, 1.6)
    renderer.active_camera.SetViewUp(0.1, 0.5, 0.9)
    renderer.active_camera.SetDistance(6.7)
    renwin.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
