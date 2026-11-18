<!-- source: https://examples.vtk.org/site/PythonicAPI/GeometricObjects/Dodecahedron/ -->

# Dodecahedron

Repository source: [Dodecahedron](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/GeometricObjects/Dodecahedron.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestDodecahedron.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/GeometricObjects/TestDodecahedron.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/GeometricObjects/Dodecahedron/)), ([Python](../../Python/GeometricObjects/Dodecahedron.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Dodecahedron.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkIdTypeArray
from vtkmodules.vtkCommonDataModel import vtkCellArray, vtkPolyhedron
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    dodecahedron = make_dodecahedron()

    # Visualize
    mapper = vtkPolyDataMapper(input_data=dodecahedron.poly_data)

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('PapayaWhip')

    renderer = vtkRenderer(background=colors.GetColor3d('CadetBlue'))
    render_window = vtkRenderWindow(window_name='Dodecahedron')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)
    renderer.active_camera.Azimuth(30)
    renderer.active_camera.Elevation(30)

    renderer.ResetCamera()

    render_window.Render()
    render_window_interactor.Start()

def make_dodecahedron():
    dodecahedron = vtkPolyhedron()

    for i in range(0, 20):
        dodecahedron.GetPointIds().InsertNextId(i)

    dodecahedron.points.InsertNextPoint(1.21412, 0, 1.58931)
    dodecahedron.points.InsertNextPoint(0.375185, 1.1547, 1.58931)
    dodecahedron.points.InsertNextPoint(-0.982247, 0.713644, 1.58931)
    dodecahedron.points.InsertNextPoint(-0.982247, -0.713644, 1.58931)
    dodecahedron.points.InsertNextPoint(0.375185, -1.1547, 1.58931)
    dodecahedron.points.InsertNextPoint(1.96449, 0, 0.375185)
    dodecahedron.points.InsertNextPoint(0.607062, 1.86835, 0.375185)
    dodecahedron.points.InsertNextPoint(-1.58931, 1.1547, 0.375185)
    dodecahedron.points.InsertNextPoint(-1.58931, -1.1547, 0.375185)
    dodecahedron.points.InsertNextPoint(0.607062, -1.86835, 0.375185)
    dodecahedron.points.InsertNextPoint(1.58931, 1.1547, -0.375185)
    dodecahedron.points.InsertNextPoint(-0.607062, 1.86835, -0.375185)
    dodecahedron.points.InsertNextPoint(-1.96449, 0, -0.375185)
    dodecahedron.points.InsertNextPoint(-0.607062, -1.86835, -0.375185)
    dodecahedron.points.InsertNextPoint(1.58931, -1.1547, -0.375185)
    dodecahedron.points.InsertNextPoint(0.982247, 0.713644, -1.58931)
    dodecahedron.points.InsertNextPoint(-0.375185, 1.1547, -1.58931)
    dodecahedron.points.InsertNextPoint(-1.21412, 0, -1.58931)
    dodecahedron.points.InsertNextPoint(-0.375185, -1.1547, -1.58931)
    dodecahedron.points.InsertNextPoint(0.982247, -0.713644, -1.58931)

    face_offsets = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    face_conns = [
        0, 1, 2, 3, 4,  # ids
        0, 5, 10, 6, 1,  #
        1, 6, 11, 7, 2,  #
        2, 7, 12, 8, 3,  #
        3, 8, 13, 9, 4,  #
        4, 9, 14, 5, 0,  #
        15, 10, 5, 14, 19,  #
        16, 11, 6, 10, 15,  #
        17, 12, 7, 11, 16,  #
        18, 13, 8, 12, 17,  #
        19, 14, 9, 13, 18,  #
        19, 18, 17, 16, 15  #
    ]

    faces = vtkCellArray()
    offsets_arr = vtkIdTypeArray()
    conns_arr = vtkIdTypeArray()

    for i in face_offsets:
        offsets_arr.InsertNextValue(i)
    for i in face_conns:
        conns_arr.InsertNextValue(i)
    faces.SetData(offsets_arr, conns_arr)
    dodecahedron.SetCellFaces(faces)
    dodecahedron.Initialize()

    return dodecahedron

if __name__ == '__main__':
    main()
```
