<!-- source: https://examples.vtk.org/site/Python/Rendering/SpecularSpheres/ -->

# SpecularSpheres

Repository source: [SpecularSpheres](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Rendering/SpecularSpheres.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestSpecularSpheres.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestSpecularSpheres.png?raw=true target=)

### Description

Note

The original source code for this example is [here](https://gitlab.kitware.com/vtk/vtk/blob/73465690278158b9e89661cd6aed26bead781378/Examples/Rendering/Cxx/SpecularSpheres.cxx).

Info

See [Figure 3-10](../../VTKBook/03Chapter3.md#Figure%203-10) in [Chapter 3](../../VTKBook/03Chapter3.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Info

Similar examples setting the ambient and diffuse properties are: See [AmbientSpheres.cxx](https://examples.vtk.org/site/Cxx/Rendering/AmbientSpheres/), [AmbientSpheres.py](AmbientSpheres.md), [AmbientSpheres.java](https://examples.vtk.org/site/Java/Rendering/AmbientSpheres/) and [DiffuseSpheres.cxx](https://examples.vtk.org/site/Cxx/Rendering/DiffuseSpheres/), [DiffuseSpheres.py](DiffuseSpheres.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/SpecularSpheres/)), ([Java](https://examples.vtk.org/site/Java/Rendering/SpecularSpheres/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SpecularSpheres.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkLight,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor('bkg', [26, 51, 102, 255])

    # The following lines create a sphere represented by polygons.
    #
    sphere = vtkSphereSource()
    sphere.SetThetaResolution(100)
    sphere.SetPhiResolution(50)

    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other attributes
    # are defined.
    #
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphere.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # In this example we create eight different spheres (two rows of four
    # spheres) and set the specular lighting coefficients. A little ambient
    # is turned on so the sphere is not completely black on the back side.
    #
    numberOfSpheres = 8
    spheres = list()
    ambient = 0.3
    diffuse = 0.5
    specular = 1.0
    spBase = 5.0
    spScale = 1.0
    position = [0, 0, 0]
    for i in range(0, numberOfSpheres):
        specularPower = spBase * spScale
        spheres.append(vtkActor())
        spheres[i].SetMapper(sphereMapper)
        spheres[i].GetProperty().SetColor(colors.GetColor3d('Red'))
        spheres[i].GetProperty().SetAmbient(ambient)
        spheres[i].GetProperty().SetDiffuse(diffuse)
        spheres[i].GetProperty().SetSpecular(specular)
        spheres[i].GetProperty().SetSpecularPower(specularPower)
        spheres[i].GetProperty().SetSpecularColor(colors.GetColor3d('White'))
        spheres[i].AddPosition(position)
        spScale = spScale * 2.0
        position[0] += 1.25
        if i == 3:
            specular = 0.5
            spScale = 1.0
            position[0] = 0
            position[1] = 1.25

    # Create the graphics structure. The renderer renders into the
    # render window. The render window interactor captures mouse events
    # and will perform appropriate camera or actor manipulation
    # depending on the nature of the events.
    #
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size.
    #
    for i in range(0, numberOfSpheres):
        ren.AddActor(spheres[i])

    ren.SetBackground(colors.GetColor3d('bkg'))
    renWin.SetSize(640, 480)
    renWin.SetWindowName('SpecularSpheres')

    # Set up the lighting.
    #
    light = vtkLight()
    light.SetFocalPoint(1.875, 0.6125, 0)
    light.SetPosition(0.875, 1.6125, 1)
    ren.AddLight(light)

    # We want to eliminate perspective effects on the apparent lighting.
    # Parallel camera projection will be used. To zoom in parallel projection
    # mode, the ParallelScale is set.
    #
    ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
    ren.GetActiveCamera().SetPosition(0, 0, 1)
    ren.GetActiveCamera().SetViewUp(0, 1, 0)
    ren.GetActiveCamera().ParallelProjectionOn()
    ren.ResetCamera()
    ren.GetActiveCamera().SetParallelScale(2.0)
    # This starts the event loop and invokes an initial render.
    #
    iren.Initialize()
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
