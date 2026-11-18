<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/PolygonalSurfacePointPlacer/ -->

# PolygonalSurfacePointPlacer

Repository source: [PolygonalSurfacePointPlacer](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/PolygonalSurfacePointPlacer.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestPolygonalSurfacePointPlacer.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestPolygonalSurfacePointPlacer.png?raw=true target=)

### Description

This example demonstrates how to draw curves on a surface.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/PolygonalSurfacePointPlacer/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PolygonalSurfacePointPlacer.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkCallbackCommand
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkInteractionWidgets import (
    vtkContourWidget,
    vtkPolygonalSurfacePointPlacer
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

    sphere_source = vtkSphereSource(radius=5)

    mapper = vtkPolyDataMapper()
    sphere_source >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('MistyRose')

    # Create the RenderWindow, Renderer.
    renderer = vtkRenderer(background=colors.GetColor3d('CadetBlue'))
    render_window = vtkRenderWindow(window_name='PolygonalSurfacePointPlacer')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    renderer.AddActor(actor)

    contour_widget = vtkContourWidget()
    contour_widget.interactor = interactor

    rep = contour_widget.GetRepresentation()

    callback = MyCallback(rep)

    contour_widget.AddObserver(vtkCallbackCommand.InteractionEvent, callback)

    point_placer = vtkPolygonalSurfacePointPlacer()
    point_placer.AddProp(actor)
    point_placer.GetPolys().AddItem(sphere_source.GetOutput())

    rep.GetLinesProperty().color = colors.GetColor3d('Crimson')
    rep.GetLinesProperty().SetLineWidth(3.0)
    rep.SetPointPlacer(point_placer)

    contour_widget.EnabledOn()
    renderer.ResetCamera()
    render_window.Render()
    interactor.Initialize()

    interactor.Start()

class MyCallback:
    def __init__(self, representation):
        self.representation = representation

    def __call__(self, caller, ev):
        print('There are ', self.representation.GetNumberOfNodes(), ' nodes.')

if __name__ == '__main__':
    main()
```
