<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/BoxClipStructuredPoints/ -->

# BoxClipStructuredPoints

Repository source: [BoxClipStructuredPoints](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/BoxClipStructuredPoints.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestBoxClipStructuredPoints.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestBoxClipStructuredPoints.png?raw=true target=)

### Description

Note

The image was generated with this volume data: `src/Testing/Data/HeadMRVolume.mhd`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/BoxClipStructuredPoints/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BoxClipStructuredPoints.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkFiltersGeneral import vtkBoxClipDataSet
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'BoxClipStructuredPoints.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename', help='HeadMRVolume.mhd')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()
    ifn = get_program_parameters()

    # Read the data.
    reader = vtkMetaImageReader(file_name=ifn)
    reader.update()

    bounds = reader.output.bounds
    scalar_range = reader.output.scalar_range

    min_box_point = list()
    max_box_point = list()
    # Used to reposition the outside actor.
    for i in range(1, len(bounds), 2):
        j = i - 1
        min_box_point.append((bounds[i] - bounds[j]) / 2.0 + bounds[j])
        max_box_point.append(bounds[i])

    minus_x = (-1.0, -0.5, 0.0)
    minus_y = (0.0, -1.0, 0.0)
    minus_z = (0.0, 0.0, -1.0)
    plus_x = (1.0, 0.0, 0.0)
    plus_y = (0.0, 1.0, 0.0)
    plus_z = (0.0, 0.0, 1.0)

    box_clip = vtkBoxClipDataSet(generate_clipped_output=True,
                                 box_clip=(minus_x, min_box_point, minus_y, min_box_point, minus_z, min_box_point,
                                           plus_x, max_box_point, plus_y, max_box_point, plus_z, max_box_point))
    reader >> box_clip

    lut1 = vtkLookupTable(hue_range=(0.667, 0))

    mapper_in = vtkDataSetMapper(scalar_range=scalar_range, lookup_table=lut1,
                                 color_mode=Mapper.ColorMode.VTK_COLOR_MODE_MAP_SCALARS)
    select_ports(box_clip, 0) >> mapper_in

    actor_in = vtkActor(mapper=mapper_in)

    mapper_out = vtkDataSetMapper(scalar_range=scalar_range, lookup_table=lut1,
                                  color_mode=Mapper.ColorMode.VTK_COLOR_MODE_MAP_SCALARS)
    select_ports(box_clip, 1) >> mapper_out

    # Move the outside actor.
    position = list()
    for i in range(0, len(max_box_point)):
        position.append(-0.5 * (max_box_point[i] - min_box_point[i]))
    actor_out = vtkActor(mapper=mapper_out)
    actor_out.SetMapper(mapper_out)
    actor_out.AddPosition(position)

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(use_hidden_line_removal=True, background=colors.GetColor3d('Silver'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='BoxClipStructuredPoints')
    render_window_interactor = vtkRenderWindowInteractor()
    render_window.AddRenderer(renderer)
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(actor_in)
    renderer.AddActor(actor_out)

    # Generate an interesting view.
    renderer.ResetCamera()
    renderer.active_camera.Azimuth(120)
    renderer.active_camera.Elevation(30)
    renderer.active_camera.Dolly(1.0)
    renderer.ResetCameraClippingRange()

    # Render and interact
    render_window.Render()
    render_window_interactor.Start()

@dataclass(frozen=True)
class Mapper:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_MODE_DEFAULT: int = 0
        VTK_COLOR_MODE_MAP_SCALARS: int = 1
        VTK_COLOR_MODE_DIRECT_SCALARS: int = 2

    @dataclass(frozen=True)
    class ResolveCoincidentTopology:
        VTK_RESOLVE_OFF: int = 0
        VTK_RESOLVE_POLYGON_OFFSET: int = 1
        VTK_RESOLVE_SHIFT_ZBUFFER: int = 2

    @dataclass(frozen=True)
    class ScalarMode:
        VTK_SCALAR_MODE_DEFAULT: int = 0
        VTK_SCALAR_MODE_USE_POINT_DATA: int = 1
        VTK_SCALAR_MODE_USE_CELL_DATA: int = 2
        VTK_SCALAR_MODE_USE_POINT_FIELD_DATA: int = 3
        VTK_SCALAR_MODE_USE_CELL_FIELD_DATA: int = 4
        VTK_SCALAR_MODE_USE_FIELD_DATA: int = 5

if __name__ == '__main__':
    main()
```
