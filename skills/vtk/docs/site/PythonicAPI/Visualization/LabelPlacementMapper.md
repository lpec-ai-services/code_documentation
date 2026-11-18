<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/LabelPlacementMapper/ -->

# LabelPlacementMapper

Repository source: [LabelPlacementMapper](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/LabelPlacementMapper.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLabelPlacementMapper.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLabelPlacementMapper.png?raw=true target=)

### Description

This example demonstrates how to add labels from an array to points. Each point is given a priority that determines which labels are visible when space is limited.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/LabelPlacementMapper/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LabelPlacementMapper.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkIntArray,
    vtkStringArray
)
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersSources import (
    vtkPointSource,
    vtkSphereSource
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkActor2D,
    vtkGlyph3DMapper,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)
from vtkmodules.vtkRenderingLabel import (
    vtkLabelPlacementMapper,
    vtkPointSetToLabelHierarchy,
)

def main():
    colors = vtkNamedColors()

    # Create a point set.
    point_source = vtkPointSource(number_of_points=6)
    point_source.update()

    # Add label array.
    labels = vtkStringArray(name='labels')
    labels.SetNumberOfValues(6)
    # labels.SetName('labels')
    labels.SetValue(0, 'Priority 10')
    labels.SetValue(1, 'Priority 7')
    labels.SetValue(2, 'Priority 6')
    labels.SetValue(3, 'Priority 4')
    labels.SetValue(4, 'Priority 4')
    labels.SetValue(5, 'Priority 4')
    point_source.output.point_data.AddArray(labels)

    # Add priority array.
    sizes = vtkIntArray(name='sizes')
    sizes.SetNumberOfValues(6)
    sizes.SetValue(0, 10)
    sizes.SetValue(1, 7)
    sizes.SetValue(2, 6)
    sizes.SetValue(3, 4)
    sizes.SetValue(4, 4)
    sizes.SetValue(5, 4)
    point_source.output.point_data.AddArray(sizes)

    # Create a mapper and actor for the points.
    point_mapper = vtkPolyDataMapper()
    point_source >> point_mapper
    point_actor = vtkActor(mapper=point_mapper)

    # Map the points to spheres.
    sphere_actor = point_to_glyph(point_source.output.GetPoints(), 0.05)
    sphere_actor.property.color = colors.GetColor3d('MistyRose')

    # Generate the label hierarchy.
    point_set_to_label_hierarchy_filter = vtkPointSetToLabelHierarchy(label_array_name='labels',
                                                                      size_array_name='sizes')
    point_source >> point_set_to_label_hierarchy_filter

    # Create a mapper and actor for the labels.
    label_mapper = vtkLabelPlacementMapper()
    point_source >> point_set_to_label_hierarchy_filter >> label_mapper
    label_actor = vtkActor2D(mapper=label_mapper)
    # label_actor.property.color = colors.GetColor3d('Yellow')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    render_window = vtkRenderWindow(window_name='LabelPlacementMapper')
    render_window.AddRenderer(renderer)
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(point_actor)
    renderer.AddActor(sphere_actor)
    renderer.AddActor(label_actor)

    # Render and interact.
    render_window.Render()
    render_window_interactor.Start()

def point_to_glyph(points, scale):
    bounds = points.bounds
    max_len = 0.0
    for i in range(0, 3):
        max_len = max(bounds[i + 1] - bounds[i], max_len)
    sphere_source = vtkSphereSource(radius=scale * max_len)
    pd = vtkPolyData(points=points)
    mapper = vtkGlyph3DMapper(input_data=pd,
                              source_connection=sphere_source.output_port,
                              scalar_visibility=False,
                              scaling=False)

    return vtkActor(mapper=mapper)

if __name__ == '__main__':
    main()
```
