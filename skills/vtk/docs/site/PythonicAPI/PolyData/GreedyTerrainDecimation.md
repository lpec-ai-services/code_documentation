<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/GreedyTerrainDecimation/ -->

# GreedyTerrainDecimation

Repository source: [GreedyTerrainDecimation](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/GreedyTerrainDecimation.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestGreedyTerrainDecimation.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestGreedyTerrainDecimation.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/GreedyTerrainDecimation/)), ([CSharp](https://examples.vtk.org/site/CSharp/PolyData/GreedyTerrainDecimation/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GreedyTerrainDecimation.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_UNSIGNED_CHAR,
    vtkMath,
    vtkMinimalStandardRandomSequence

)
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkFiltersHybrid import vtkGreedyTerrainDecimation
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # Create an image.
    image = vtkImageData(dimensions=(3, 3, 1))
    image.AllocateScalars(VTK_UNSIGNED_CHAR, 1)

    randomSequence = vtkMinimalStandardRandomSequence()
    randomSequence.SetSeed(8775070)

    dims = image.dimensions
    scalars = image.GetPointData().GetScalars()
    for i in range(0, scalars.GetSize()):
        pixel = vtkMath.Round(randomSequence.GetRangeValue(0.0, 5.0))
        scalars.SetValue(i, pixel)
        randomSequence.Next()
    image.GetPointData().SetScalars(scalars)

    decimation = vtkGreedyTerrainDecimation(input_data=image)

    # Visualize
    mapper = vtkPolyDataMapper()
    decimation >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.SetInterpolationToFlat()
    actor.property.edge_visibility = True
    actor.property.edge_color = colors.GetColor3d('Red')

    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='GreedyTerrainDecimation')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
