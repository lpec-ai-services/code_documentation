<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/PineRootDecimation/ -->

# PineRootDecimation

Repository source: [PineRootDecimation](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/PineRootDecimation.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestPineRootDecimation.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestPineRootDecimation.png?raw=true target=)

### Description

Demonstrates how to apply the decimation filter to get a reduced data size and then the connectivity filter to remove noisy isosurfaces. The data is from the root system of a pine tree.

To count the number of triangles in the polydata we do the following:

#### C++

We use a lambda function

```python
auto NumberofTriangles = [](auto *pd)
```

#### Python

We just implement:

```python
def number_of_triangles(pd):
```

within the scope of the calling function.

Info

See [Figure 9-52](../../VTKBook/09Chapter9.md#Figure%209-52b) in [Chapter 9](../../VTKBook/09Chapter9.md) in the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/PineRootDecimation/)), ([Python](../../Python/VisualizationAlgorithms/PineRootDecimation.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PineRootDecimation.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import (
    vtkConnectivityFilter,
    vtkDecimatePro
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOGeometry import vtkMCubesReader
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
    description = 'Applying connectivity and decimation filters to remove noisy isosurfaces and reduce data size.'
    epilogue = '''
        Applying connectivity and decimation filters to remove noisy isosurfaces and reduce data size..

This example demonstrates how to use the vtkConnectivityFilter and vtkDecimate.

   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='pine_root.tri.')
    args = parser.parse_args()
    return args.filename

def main():
    def number_of_triangles(pd):
        """
        Count the number of triangles.
        :param pd: vtkPolyData.
        :return: The number of triangles.
        """
        cells = pd.GetPolys()
        num_of_triangles = 0
        cell_iter = cells.NewIterator()
        # cell_iter.GoToFirstCell()
        while not cell_iter.IsDoneWithTraversal():
            cell = cell_iter.GetCurrentCell()
            if not cell:
                continue
            if cell.GetNumberOfIds() == 3:
                num_of_triangles += 1
            cell_iter.GoToNextCell()
        return num_of_triangles

    colors = vtkNamedColors()

    file_name = get_program_parameters()

    # Create the pipeline.
    reader = vtkMCubesReader(file_name=file_name, flip_normals=False)
    deci = vtkDecimatePro(target_reduction=0.9, absolute_error=0.0005, feature_angle=30,
                          error_is_absolute=True, accumulate_error=True)
    deci.MaximumIterations = 6
    connect = vtkConnectivityFilter(
        extraction_mode=ConnectivityFilter.ExtractionMode.VTK_EXTRACT_LARGEST_REGION)
    iso_mapper = vtkDataSetMapper(scalar_visibility=False)
    (reader >> deci >> connect >> iso_mapper).update()
    #  Now we have done the update, we can print out the count of triangles.
    print(f'Before Decimation.\nThere are: {number_of_triangles(reader.output)} triangles')
    print(f'After Decimation.\nThere are: {number_of_triangles(deci.output)} triangles')
    print(f'After Connectivity.\nThere are: {number_of_triangles(connect.output)} triangles')
    iso_actor = vtkActor(mapper=iso_mapper)
    iso_actor.property.color = colors.GetColor3d('raw_sienna')

    # Get an outline of the data set for context.
    outline = vtkOutlineFilter()
    outline_mapper = vtkPolyDataMapper()
    reader >> outline >> outline_mapper
    outline_actor = vtkActor(mapper=outline_mapper)
    outline_actor.property.color = colors.GetColor3d('Black')

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name='PineRootDecimation')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer, set the background and size.
    ren.AddActor(outline_actor)
    ren.AddActor(iso_actor)

    cam = ren.active_camera
    cam.focal_point = (40.6018, 37.2813, 50.1953)
    cam.position = (40.6018, -280.533, 47.0172)
    cam.ComputeViewPlaneNormal()
    cam.clipping_range = (26.1073, 1305.36)
    cam.view_angle = 20.9219
    cam.view_up = (0.0, 0.0, 1.0)

    iren.Initialize()
    ren_win.Render()
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

if __name__ == '__main__':
    main()
```
