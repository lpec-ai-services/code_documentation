<!-- source: https://examples.vtk.org/site/PythonicAPI/ImageData/VoxelsOnBoundary/ -->

# VoxelsOnBoundary

Repository source: [VoxelsOnBoundary](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/ImageData/VoxelsOnBoundary.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestVoxelsOnBoundary.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/ImageData/TestVoxelsOnBoundary.png?raw=true target=)

### Description

This example uses [vtkMultiThreshold](https://www.vtk.org/doc/nightly/html/classvtkMultiThreshold.html) to extract voxels that are inside an isosurface and on the boundary of the isosurface. The result is a [vtkUnstructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html) for each set of voxels. Before processing, [vtkImageShrink3D](https://www.vtk.org/doc/nightly/html/classvtkImageShrink3D.html) reduces the resolution by a factor of 4.

Compare these results with [MedicalDemo1](../Medical/MedicalDemo1.md) that extracts the surface using [vtkFlyingEdges3D](https://www.vtk.org/doc/nightly/html/classvtkFlyingEdges3D.html) or [vtkMarchingCubes](https://www.vtk.org/doc/nightly/html/classvtkMarchingCubes.html) to extract an interpolated isosurface.

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageData/VoxelsOnBoundary/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**VoxelsOnBoundary.py**

```python
# !/usr/bin/env python3

import sys
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkPlane, vtkDataObject
)
from vtkmodules.vtkFiltersGeneral import vtkImageDataToPointSet, vtkMultiThreshold
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import vtkImageShrink3D
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def get_program_parameters():
    import argparse
    description = 'Color the voxels on the boundary of the image.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='The file to use e.g. FullHead.mhd.')
    args = parser.parse_args()
    return args.filename

def main():
    fn = get_program_parameters()
    fp = Path(fn)
    file_check = True
    if not fp.is_file():
        print(f'Missing image file: {fp}.')
        file_check = False
    if not file_check:
        return

    colors = vtkNamedColors()

    # Read the image.
    reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
    reader.file_name = fp
    # Can use this instead.
    # reader = vtkMetaImageReader(file_name=fp)
    reader.update()

    shrink = vtkImageShrink3D(shrink_factors=(4, 4, 4))
    reader >> shrink
    shrink.update()

    # Create a PointSet from the ImageData.
    image_data_to_point_set = vtkImageDataToPointSet()
    reader >> image_data_to_point_set
    shrink >> image_data_to_point_set

    # Extract voxels on the border between the inside and outside.
    threshold = vtkMultiThreshold(input_data=image_data_to_point_set.update().output)
    # Inside points have one or more points above the isosurface.
    inside_id = threshold.AddIntervalSet(501, 20000, vtkMultiThreshold.CLOSED, vtkMultiThreshold.CLOSED,
                                         vtkDataObject.FIELD_ASSOCIATION_POINTS, 'ImageScalars', 0, 0)
    # Border points have points that straddle the boundary
    border_id = threshold.AddIntervalSet(499.9999, 501.0000, vtkMultiThreshold.OPEN, vtkMultiThreshold.OPEN,
                                         vtkDataObject.FIELD_ASSOCIATION_POINTS, 'ImageScalars', 0, 0)

    # Select the intervals to be output
    threshold.OutputSet(inside_id)
    threshold.OutputSet(border_id)
    threshold.Update()

    # Visualize
    colors = vtkNamedColors()
    # outsideColor    = colors.GetColor3d('Crimson')
    inside_color = colors.GetColor3d('Banana')
    border_color = colors.GetColor3d('Mint')
    # surfaceColor    = colors.GetColor3d('Peacock')
    background_color = colors.GetColor3d('Silver')

    input_data_inside = threshold.output.GetBlock(inside_id).GetBlock(0)
    input_data_border = threshold.output.GetBlock(border_id).GetBlock(0)

    normal = (1.0, -1.0, -1.0)
    origin = input_data_inside.GetCenter()
    plane = vtkPlane(origin=origin, normal=normal)

    # Inside
    inside_mapper = vtkDataSetMapper(input_data=input_data_inside, scalar_visibility=False)

    inside_actor = vtkActor(mapper=inside_mapper)
    inside_actor.property.diffuse_color = inside_color
    inside_actor.property.specular = 0.6
    inside_actor.property.specular_power = 30
    inside_actor.property.edge_visibility = True

    # Border
    border_mapper = vtkDataSetMapper(input_data=input_data_border, scalar_visibility=False)

    border_actor = vtkActor(mapper=border_mapper)
    border_actor.property.diffuse_color = border_color
    border_actor.property.specular = 0.6
    border_actor.property.specular_power = 30
    border_actor.property.edge_visibility = True

    renderer = vtkRenderer(use_hidden_line_removal=True, background=background_color)
    render_window = vtkRenderWindow(size=(640, 480), window_name=f'{Path(sys.argv[0]).stem:s}')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    renderer.AddActor(inside_actor)
    renderer.AddActor(border_actor)

    render_window.Render()

    # Set up a good view.
    renderer.active_camera.view_up = (0, 0, 1)
    renderer.active_camera.position = (0, -1, 0)
    renderer.active_camera.focal_point = (0, 0, 0)
    renderer.active_camera.Azimuth(30.0)
    renderer.active_camera.Elevation(30.0)
    renderer.ResetCamera()
    renderer.active_camera.Dolly(1.5)

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
