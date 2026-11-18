<!-- source: https://examples.vtk.org/site/PythonicAPI/Annotation/LegendScaleActor/ -->

# LegendScaleActor

Repository source: [LegendScaleActor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Annotation/LegendScaleActor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Annotation/TestLegendScaleActor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Annotation/TestLegendScaleActor.png?raw=true target=)

### Description

The [vtkLegendScaleActor](https://www.vtk.org/doc/nightly/html/classvtkLegendScaleActor.html) object is used to annotate the render window. Its basic goal is to provide an indication of the scale of the scene. Four axes surrounding the render window indicate (in a variety of ways) the scale of what the camera is viewing. An option also exists for displaying a scale legend.

The axes can be programmed either to display distance scales or x-y coordinate values. By default, the scales display a distance. However, if you know that the view is down the z-axis, the scales can be programmed to display x-y coordinate values.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Annotation/LegendScaleActor/)), ([Java](https://examples.vtk.org/site/Java/Annotation/LegendScaleActor/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LegendScaleActor.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonComputationalGeometry import vtkParametricEnneper
from vtkmodules.vtkFiltersSources import vtkParametricFunctionSource
from vtkmodules.vtkRenderingAnnotation import vtkLegendScaleActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # The source will be a parametric function.
    src = vtkParametricEnneper()
    fn_src = vtkParametricFunctionSource()
    fn_src.SetParametricFunction(src)

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper()
    fn_src >> mapper
    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('SandyBrown')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    render_window = vtkRenderWindow(size=(600, 600), window_name='LegendScaleActor')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    legend_scale_actor = vtkLegendScaleActor()

    axes_prop = legend_scale_actor.axes_property
    axes_prop.color = colors.GetColor3d('Red')

    legend_scale_actor.top_axis.property = axes_prop
    legend_scale_actor.left_axis.property = axes_prop
    legend_scale_actor.bottom_axis.property = axes_prop

    # Add the actor to the scene.
    renderer.AddActor(actor)
    renderer.AddActor(legend_scale_actor)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
