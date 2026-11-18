<!-- source: https://examples.vtk.org/site/PythonicAPI/Meshes/ElevationFilter/ -->

# ElevationFilter

Repository source: [ElevationFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Meshes/ElevationFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestElevationFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Meshes/TestElevationFilter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Meshes/ElevationFilter/)), ([CSharp](https://examples.vtk.org/site/CSharp/Meshes/ElevationFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ElevationFilter.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints, vtkUnsignedCharArray, vtkLookupTable
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import (
    vtkDelaunay2D, vtkElevationFilter
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    named_colors = vtkNamedColors()

    # Create a grid of points (height/terrain map).
    points = vtkPoints()

    grid_size = 10
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            points.InsertNextPoint(x, y, int((x + y) / (y + 1)))

    bounds = points.GetBounds()

    # Add the grid points to a polydata object.
    input_poly_data = vtkPolyData(points=points)

    # Triangulate the grid points.
    delaunay = vtkDelaunay2D()

    elevation_filter = vtkElevationFilter(low_point=(0.0, 0.0, bounds[4]), high_point=(0.0, 0.0, bounds[5]))
    input_poly_data >> delaunay >> elevation_filter

    output = vtkPolyData()
    output.ShallowCopy(elevation_filter.update().output)

    elevation = output.point_data.GetArray('Elevation')

    # Create the color map.
    color_lookup_table = vtkLookupTable(table_range=(bounds[4], bounds[5]))
    color_lookup_table.Build()

    # Generate the colors for each point based on the color map.
    colors = vtkUnsignedCharArray(number_of_components=3, name='Colors')

    for i in range(0, output.number_of_points):
        val = elevation.GetValue(i)
        # print(f'Value: {val}')

        dcolor = [0.0] * 3
        color_lookup_table.GetColor(val, dcolor)
        # print(f'dcolor: ({fmt_floats(dcolor)})')
        color = [0] * 3
        for j in range(0, 3):
            color[j] = int(255 * dcolor[j] / 1.0)
        # print(f'color: ({fmt_ints(color)})')
        colors.InsertNextTypedTuple(color)

    output.point_data.AddArray(colors)

    # Visualize.
    mapper = vtkPolyDataMapper(input_data=output)

    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(background=named_colors.GetColor3d('ForestGreen'))
    render_window = vtkRenderWindow(window_name='ElevationFilter')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    # z-axis points upwards and y-axis is lower right edge.
    camera = renderer.active_camera
    camera.position = (-13.3586, 20.7305, 22.5147)
    camera.focal_point = (4.5, 4.5, 4.5)
    camera.view_up = (0.506199, -0.328212, 0.797521)
    camera.SetDistance(30.1146)
    camera.SetClippingRange(14.3196, 50.0698)

    render_window.Render()

    render_window_interactor.Start()

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

def fmt_ints(v, w=0):
    """
    Pretty print a list or tuple of ints.

    :param v: The list or tuple of ints.
    :param w: Total width of the field.
    :return: A string.
    """
    return ', '.join([f'{element:{w}}' for element in v])

if __name__ == '__main__':
    main()
```
