<!-- source: https://examples.vtk.org/site/PythonicAPI/ImplicitFunctions/ImplicitSphere1/ -->

# ImplicitSphere1

Repository source: [ImplicitSphere1](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImplicitFunctions/ImplicitSphere1.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImplicitFunctions/TestImplicitSphere1.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImplicitFunctions/TestImplicitSphere1.png?raw=true target=)

### Description

Shows how to create a surface representing a sphere by creating an implicit sphere, sampling the implicit function, and finally contouring the sampled data to produce the surface.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImplicitFunctions/ImplicitSphere1/)), ([Python](../../Python/ImplicitFunctions/ImplicitSphere1.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImplicitSphere1.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkSphere
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

    sphere = vtkSphere(radius=0.5, center=(0, 0, 0))

    # The sample function generates a distance function from the implicit
    # function. This is then contoured to get a polygonal surface.
    sample = vtkSampleFunction(implicit_function=sphere, model_bounds=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5),
                               sample_dimensions=(20, 20, 20), compute_normals=False)

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

    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    renwin = vtkRenderWindow(window_name='ImplicitSphere1')
    renwin.AddRenderer(renderer)

    # Add the actor.
    renderer.AddActor(actor)

    # An interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = renwin

    # Start
    interactor.Initialize()
    renwin.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
