<!-- source: https://examples.vtk.org/site/PythonicAPI/Filtering/SpatioTemporalHarmonicsSource/ -->

# SpatioTemporalHarmonicsSource

Repository source: [SpatioTemporalHarmonicsSource](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Filtering/SpatioTemporalHarmonicsSource.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestSpatioTemporalHarmonicsSource.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Filtering/TestSpatioTemporalHarmonicsSource.png?raw=true target=)

### Description

Generate image data containing spatio-temporal harmonic data.

This source allows you to specify the uniform grid extent. It also lets you choose the harmonics you want.

The source has an embedded filter allowing you to add mutiple harmonics defined by their amplitude, temporal frequency, wave vector, and phase. The sum of these will be computed using the sine function for each point. Note that there is no cosine in this function. If no harmonic is specified, values will be null.

The source can also generate time steps by specifying time values.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Filtering/SpatioTemporalHarmonicsSource/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SpatioTemporalHarmonicsSource.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingUI
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSpatioTemporalHarmonicsSource
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

MAX_EXTENT = 10

def main():
    colors = vtkNamedColors()

    # Create the source
    extent = (-MAX_EXTENT, MAX_EXTENT) * 3
    source = vtkSpatioTemporalHarmonicsSource(whole_extent=extent)

    source.ClearHarmonics()
    source.AddHarmonic(1.0, 1.0, 1.0, 0.0, 0.0, 0.0)
    source.AddHarmonic(2.0, 1.0, 0.0, 1.0, 0.0, 0.0)
    source.AddHarmonic(4.0, 1.0, 0.0, 0.0, 1.0, 0.0)

    source.ClearTimeStepValues()
    source.AddTimeStepValue(0.0)
    source.AddTimeStepValue(1.0)
    source.AddTimeStepValue(2.0)

    # Create the mapper and actor.
    mapper = vtkDataSetMapper(scalar_range=(-6.0, 6.0))
    source >> mapper
    actor = vtkActor(mapper=mapper)

    # Create a renderer, render window, and interactor.
    ren = vtkRenderer(background=colors.GetColor3d('Gray'))
    ren_win = vtkRenderWindow(size=(600, 600), window_name='SpatioTemporalHarmonicsSource')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    ren.ResetCamera()
    ren.active_camera.position = (50.0, 40.0, 30.0)
    ren.active_camera.focal_point = (0.0, 0.0, 0.0)
    ren.ResetCameraClippingRange()

    # Add the actor, render and interact.
    ren.AddActor(actor)
    ren_win.Render()

    cow = vtkCameraOrientationWidget()
    cow.SetParentRenderer(ren)

    # Enable the widget.
    cow.On()
    iren.Start()

if __name__ == '__main__':
    main()
```
