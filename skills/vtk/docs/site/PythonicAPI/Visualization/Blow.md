<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/Blow/ -->

# Blow

Repository source: [Blow](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/Blow.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestBlow.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestBlow.png?raw=true target=)

### Description

Extrusion blow molding process.

In the extrusion blow molding process, a material is extruded through an annular die to form a hollow cylinder. This cylinder is called a parison. Two mold halves are then closed on the parison, while at the same time the parison is inflated with air. Some of the parison material remains within the mold while some becomes waste material. The material is typically a polymer plastic softened with heat, but blow molding has been used to form metal parts. Plastic bottles are often manufactured using a blow molding process.

In this example the polymer was molded using an isothermal, nonlinear-elastic, incompressible (rubber-like) material. Triangular membrane finite elements were used to model the parison, while a combination of triangular and quadrilateral finite elements were used to model the mold. The mold surface is assumed to be rigid, and the parison is assumed to attach to the mold upon contact. Thus the thinning of the parison is controlled by its stretching during inflation and the sequence in which it contacts the mold.

Ten steps of the analysis are illustrated. The color of the parison indicates its thickness. Using a rainbow scale, red areas are thinnest while blue regions are thickest. Our visualization shows clearly one problem with the analysis technique we are using. Note that while the nodes (i.e., points) of the finite element mesh are prevented from passing through the mold, the interior of the triangular elements are not. This is apparent from the occlusion of the mold wireframe by the parison mesh.

You can also view the individual steps.

Info

See [Figure 12-17](../../VTKBook/12Chapter12.md#Figure%2012-17) in [Chapter 12](../../VTKBook/12Chapter12.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/Blow/)), ([Python](../../Python/Visualization/Blow.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Blow.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkFiltersCore import (
    vtkConnectivityFilter,
    vtkContourFilter,
    vtkPolyDataNormals
)
from vtkmodules.vtkFiltersGeneral import vtkWarpVector
from vtkmodules.vtkFiltersGeometry import vtkGeometryFilter
from vtkmodules.vtkIOLegacy import vtkDataSetReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Produce figure 12-17 from the VTK Textbook.'
    epilogue = '''

        It is a translation of the original blow.tcl.

        data_point allows you to specify which frame is to be displayed.
        If data_point < 0 or data_point > 9 all ten frames are then displayed.

   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename', help='blow.vtk')
    parser.add_argument('-d', '--data_point', default=-1, type=int, nargs='?',
                        help='The frame to display (0...9).')
    args = parser.parse_args()
    return args.filename, args.data_point

def main():
    file_name, data_point = get_program_parameters()

    colors = vtkNamedColors()

    thickness = list()
    displacement = list()
    for i in range(0, 10):
        thickness.append('thickness' + str(i))
        displacement.append('displacement' + str(i))

    renders = list()

    lut = vtkLookupTable(hue_range=(0.0, 0.66667))

    for i in range(0, 10):
        # Create the reader and warp the data with vectors.
        reader = vtkDataSetReader(file_name=file_name, scalars_name=thickness[i], vectors_name=displacement[i])
        reader.update()

        warp = vtkWarpVector()
        reader.unstructured_grid_output >> warp

        # Extract the mold from the mesh using connectivity.
        connect = vtkConnectivityFilter(
            extraction_mode=ConnectivityFilter.ExtractionMode.VTK_EXTRACT_SPECIFIED_REGIONS)
        connect.AddSpecifiedRegion(0)
        connect.AddSpecifiedRegion(1)
        mold = vtkGeometryFilter()
        mold_mapper = vtkDataSetMapper(scalar_visibility=False)
        warp >> connect >> mold >> mold_mapper
        mold_actor = vtkActor(mapper=mold_mapper)
        mold_actor.property.color = colors.GetColor3d('ivory_black')
        mold_actor.property.representation = Property.Representation.VTK_WIREFRAME

        # Extract the parison from the mesh using connectivity.
        connect2 = vtkConnectivityFilter(
            extraction_mode=ConnectivityFilter.ExtractionMode.VTK_EXTRACT_SPECIFIED_REGIONS)
        connect2.AddSpecifiedRegion(2)
        parison = vtkGeometryFilter()
        normals2 = vtkPolyDataNormals(feature_angle=60.0)
        parison_mapper = vtkPolyDataMapper(lookup_table=lut, scalar_range=(0.12, 1.0))
        warp >> connect2 >> parison >> normals2 >> parison_mapper
        parison_actor = vtkActor(mapper=parison_mapper)

        cf = vtkContourFilter()
        cf.SetValue(0, 0.5)
        contour_mapper = vtkPolyDataMapper()
        connect2 >> cf >> contour_mapper
        contours = vtkActor(mapper=contour_mapper)

        renderer = vtkRenderer(background=colors.GetColor3d('AliceBlue'))
        renderer.AddActor(mold_actor)
        renderer.AddActor(parison_actor)
        renderer.AddActor(contours)
        renderer.active_camera.position = (50.973277, 12.298821, 29.102547)
        renderer.active_camera.focal_point = (0.141547, 12.298821, -0.245166)
        renderer.active_camera.view_up = (-0.500000, 0.000000, 0.866025)
        renderer.active_camera.clipping_range = (36.640827, 78.614680)
        renders.append(renderer)

    # Create the RenderWindow and RenderWindowInteractor.
    ren_win = vtkRenderWindow(window_name='Blow')
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    renderer_size_x = 750
    renderer_size_y = 400
    ren_win_scale = 0.5
    if 0 <= data_point < 10:
        ren_win.AddRenderer(renders[data_point])
        ren_win.SetSize(renderer_size_x, renderer_size_y)
    else:
        grid_dimensions_x = 2
        grid_dimensions_y = 5
        ren_win.SetSize(int(renderer_size_x * grid_dimensions_x * ren_win_scale),
                        int(renderer_size_y * grid_dimensions_y * ren_win_scale))
        # Add and position the renders to the render window.
        view_port = list()
        for row in range(0, grid_dimensions_y):
            for col in range(0, grid_dimensions_x):
                idx = row * grid_dimensions_x + col
                # view_port = (x0, y0, x1, y1)
                view_port = (
                    float(col) / grid_dimensions_x,
                    float(grid_dimensions_y - row - 1) / grid_dimensions_y,
                    float(col + 1) / grid_dimensions_x,
                    float(grid_dimensions_y - row) / grid_dimensions_y
                )
                renders[idx].SetViewport(view_port)
                ren_win.AddRenderer(renders[idx])

    iren.Initialize()
    iren.Start()

@dataclass(frozen=True)
class ConnectivityFilter:
    @dataclass(frozen=True)
    class ExtractionMode:
        VTK_EXTRACT_POINT_SEEDED_REGIONS: int = 1
        VTK_EXTRACT_CELL_SEEDED_REGIONS: int = 2
        VTK_EXTRACT_SPECIFIED_REGIONS: int = 3
        VTK_EXTRACT_LARGEST_REGION: int = 4
        VTK_EXTRACT_ALL_REGIONS: int = 5
        VTK_EXTRACT_CLOSEST_POINT_REGION: int = 6

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
