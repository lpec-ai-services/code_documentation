<!-- source: https://examples.vtk.org/site/PythonicAPI/StructuredPoints/Vol/ -->

# Vol

Repository source: [Vol](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/StructuredPoints/Vol.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/StructuredPoints/TestVol.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/StructuredPoints/TestVol.png?raw=true target=)

### Description

Creating a image data dataset. Scalar data is generated from the equation for a sphere. Volume dimensions are 26^3.

Info

See [Figure 5-18](../../VTKBook/05Chapter5.md#Figure%205-18) in [Chapter 5](../../VTKBook/05Chapter5.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/StructuredPoints/Vol/)), ([Python](../../Python/StructuredPoints/Vol.md)), ([Java](https://examples.vtk.org/site/Java/StructuredPoints/Vol/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Vol.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkDoubleArray
from vtkmodules.vtkCommonDataModel import vtkStructuredPoints
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name='Vol')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    sp = 1.0 / 25.0
    scalars = vtkDoubleArray(number_of_components=1, number_of_tuples=26)
    for k in range(0, 26):
        z = -0.5 + k * sp
        k_offset = k * 26 * 26
        for j in range(0, 26):
            y = -0.5 + j * sp
            j_offset = j * 26
            for i in range(0, 26):
                x = -0.5 + i * sp
                s = x * x + y * y + z * z - (0.4 * 0.4)
                offset = i + j_offset + k_offset
                scalars.InsertTuple1(offset, s)

    # print((sp,)*3)
    vol = vtkStructuredPoints(dimensions=(26, 26, 26), origin=(-0.5, -0.5, -0.5), spacing=(sp,) * 3)
    vol.point_data.SetScalars(scalars)

    contour = vtkContourFilter()
    contour.SetValue(0, 0.0)
    contour.SetInputData(vol)

    vol_mapper = vtkPolyDataMapper(scalar_visibility=False)
    vol >> contour >> vol_mapper

    vol_actor = vtkActor(mapper=vol_mapper)
    vol_actor.property.edge_visibility = True
    vol_actor.property.color = colors.GetColor3d('Salmon')

    renderer.AddActor(vol_actor)

    # Interact with the data.
    ren_win.Render()

    iren.Start()

if __name__ == '__main__':
    main()
```
