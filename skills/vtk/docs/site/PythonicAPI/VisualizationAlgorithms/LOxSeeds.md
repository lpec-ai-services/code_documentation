<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/LOxSeeds/ -->

# LOxSeeds

Repository source: [LOxSeeds](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/LOxSeeds.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestLOxSeeds.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestLOxSeeds.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/LOxSeeds/)), ([Python](../../Python/VisualizationAlgorithms/LOxSeeds.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LOxSeeds.py**

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
from vtkmodules.vtkFiltersCore import vtkTubeFilter
from vtkmodules.vtkFiltersFlowPaths import vtkStreamTracer
from vtkmodules.vtkFiltersGeometry import vtkStructuredGridGeometryFilter
from vtkmodules.vtkFiltersSources import vtkPointSource
from vtkmodules.vtkIOParallel import vtkMultiBlockPLOT3DReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkProperty
)

def get_program_parameters():
    import argparse
    description = 'Streamlines seeded with a spherical cloud of points.'
    epilogue = '''
     Four separate cloud positions are shown.
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

    seeds = [[-0.74, 0.0, 0.3], [-0.74, 0.0, 1.0], [-0.74, 0.0, 2.0], [-0.74, 0.0, 3.0]]

    renderers = list()

    for s in range(0, len(seeds)):
        # The computational planes.
        floor_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(0, 37, 0, 75, 0, 0))
        floor_comp.update()

        floor_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_visibility=False)
        floor_comp >> floor_mapper

        floor_property = vtkProperty(color=colors.GetColor3d('Black'), line_width=2,
                                     representation=Property.Representation.VTK_WIREFRAME)

        floor_actor = vtkActor(mapper=floor_mapper, property=floor_property)

        post_comp = vtkStructuredGridGeometryFilter(input_data=sg, extent=(10, 10, 0, 75, 0, 37))

        post_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_range=sg.scalar_range)
        post_comp >> post_mapper

        post_property = vtkProperty(color=colors.GetColor3d('Black'))

        post_actor = vtkActor(mapper=post_mapper, property=post_property)

        # The streamers.

        # Spherical seed points.
        rake = vtkPointSource(center=seeds[s], number_of_points=10)

        streamers = vtkStreamTracer(input_connection=pl3d.output_port,
                                    source_connection=rake.output_port,
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

        ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))

        ren.AddActor(floor_actor)
        ren.AddActor(post_actor)
        ren.AddActor(tubes_actor)
        renderers.append(ren)

    ren_win = vtkRenderWindow(window_name=f'{Path(sys.argv[0]).stem:s}')

    # Setup the viewports for the renderers.
    renderer_size = 256
    x_grid_dimensions = 2
    y_grid_dimensions = 2
    ren_win.SetSize(renderer_size * x_grid_dimensions, renderer_size * y_grid_dimensions)
    for row in range(0, y_grid_dimensions):
        for col in range(x_grid_dimensions):
            index = row * x_grid_dimensions + col
            # (xmin, ymin, xmax, ymax)
            viewport = [float(col) / x_grid_dimensions, float(y_grid_dimensions - (row + 1)) / y_grid_dimensions,
                        float(col + 1) / x_grid_dimensions, float(y_grid_dimensions - row) / y_grid_dimensions]
            renderers[index].SetViewport(viewport)

    camera = vtkCamera()
    camera.SetFocalPoint(0.918037, -0.0779233, 2.69513)
    camera.SetPosition(0.840735, -23.6176, 8.50211)
    camera.SetViewUp(0.00227904, 0.239501, 0.970893)
    camera.SetClippingRange(1, 100)

    renderers[0].SetActiveCamera(camera)
    for r in range(0, len(renderers)):
        ren_win.AddRenderer(renderers[r])
        if r > 0:
            renderers[r].SetActiveCamera(camera)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

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
