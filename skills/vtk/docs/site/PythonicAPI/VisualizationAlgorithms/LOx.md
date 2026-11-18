<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/LOx/ -->

# LOx

Repository source: [LOx](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/LOx.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestLOx.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestLOx.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/LOx/)), ([Python](../../Python/VisualizationAlgorithms/LOx.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LOx.py**

```python
#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkFiltersCore import (
    vtkStructuredGridOutlineFilter,
    vtkTubeFilter
)
from vtkmodules.vtkFiltersFlowPaths import vtkStreamTracer
from vtkmodules.vtkFiltersGeometry import vtkStructuredGridGeometryFilter
from vtkmodules.vtkFiltersSources import vtkPointSource
from vtkmodules.vtkIOParallel import vtkMultiBlockPLOT3DReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Streamtubes created by using the computational grid just in front of the post as a source for seeds.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('xyz_file', help='postxyz.bin.')
    parser.add_argument('q_file', help='postq.bin.')
    args = parser.parse_args()
    return args.xyz_file, args.q_file

def main():
    colors = vtkNamedColors()

    xyz_file, q_file = get_program_parameters()

    # Read the data.
    pl3d = vtkMultiBlockPLOT3DReader(xyz_file_name=xyz_file, q_file_name=q_file,
                                     scalar_function_number=153, vector_function_number=200)
    pl3d.AutoDetectFormatOn()
    pl3d.update()

    sg = pl3d.output.GetBlock(0)

    # Blue to red lut.
    lut = vtkLookupTable(hue_range=(0.667, 0.0))

    # The computational planes.
    floor_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(0, 37, 0, 75, 0, 0))
    floor_comp.update()

    floor_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_visibility=False)
    floor_comp >> floor_mapper

    floor_property = vtkProperty(color=colors.GetColor3d('Beige'), line_width=2,
                                 representation=Property.Representation.VTK_WIREFRAME)

    floor_actor = vtkActor(mapper=floor_mapper, property=floor_property)

    sub_floor_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(0, 37, 0, 15, 22, 22))

    sub_floor_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_range=sg.scalar_range)
    sub_floor_comp >> sub_floor_mapper

    sub_floor_actor = vtkActor(mapper=sub_floor_mapper)

    sub_floor2_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(0, 37, 60, 75, 22, 22))

    sub_floor2_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_range=sg.scalar_range)
    sub_floor2_comp >> sub_floor2_mapper

    sub_floor2_actor = vtkActor(mapper=sub_floor2_mapper)

    post_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(10, 10, 0, 75, 0, 37))

    post_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_range=sg.scalar_range)
    post_comp >> post_mapper

    post_property = vtkProperty(color=colors.GetColor3d('Beige'))

    post_actor = vtkActor(mapper=post_mapper, property=post_property)

    fan_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(0, 37, 38, 38, 0, 37))

    fan_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_range=sg.scalar_range)
    fan_comp >> fan_mapper

    fan_property = vtkProperty(color=colors.GetColor3d('Beige'))

    fan_actor = vtkActor(mapper=fan_mapper, property=fan_property)

    fan_actor.SetMapper(fan_mapper)

    # The streamers.

    # Spherical seed points.
    rake = vtkPointSource(center=(-0.74, 0, 0.3), number_of_points=10)

    # A line of seed points.
    seeds_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(10, 10, 37, 39, 1, 27))

    streamers = vtkStreamTracer(input_connection=pl3d.output_port,
                                # source_connection=rake.output_port,
                                source_connection=seeds_comp.output_port,
                                maximum_propagation=250,
                                initial_integration_step=0.2,
                                minimum_integration_step=0.01,
                                integrator_type=2)
    streamers.update()

    tubes = vtkTubeFilter(input_connection=streamers.output_port,
                          number_of_sides=8, radius=0.08, vary_radius=False)

    map_tubes = vtkPolyDataMapper(scalar_range=sg.scalar_range)
    tubes >> map_tubes

    tubes_actor = vtkActor(mapper=map_tubes)

    # The outline.
    outline = vtkStructuredGridOutlineFilter(input_data=sg)

    outline_mapper = vtkPolyDataMapper()
    outline >> outline_mapper

    outline_property = vtkProperty(color=colors.GetColor3d('Beige'))

    outline_actor = vtkActor(mapper=outline_mapper, property=outline_property)

    # Create the graphics stuff.
    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name=f'{Path(sys.argv[0]).stem:s}')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    # Add the actors to the renderer, set the background and size.
    ren.AddActor(outline_actor)
    ren.AddActor(floor_actor)
    # ren.AddActor(sub_floor_actor)
    # ren.AddActor(sub_floor2_actor)
    ren.AddActor(post_actor)
    # ren.AddActor(fan_actor)
    ren.AddActor(tubes_actor)

    camera = vtkCamera()
    camera.focal_point = (2.47736, -0.150024, 2.42361)
    camera.position = (1.57547, -13.4601, 5.47872)
    camera.view_up = (0.00197003, 0.223588, 0.974682)
    camera.clipping_range = (1, 100)

    ren.SetActiveCamera(camera)

    ren_win.Render()
    iren.Start()

@dataclass(frozen=True)
class Property:
    @dataclass(frozen=True)
    class Interpolation:
        VTK_FLAT: int = 0
        VTK_GOURAUD: int = 1
        VTK_PHONG: int = 2
        VTK_PBR: int = 3

    @dataclass(frozen=True)
    class Representation:
        VTK_POINTS: int = 0
        VTK_WIREFRAME: int = 1
        VTK_SURFACE: int = 2

if __name__ == '__main__':
    main()
```
