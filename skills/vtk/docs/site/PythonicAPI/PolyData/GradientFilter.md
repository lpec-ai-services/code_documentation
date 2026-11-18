<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/GradientFilter/ -->

# GradientFilter

Repository source: [GradientFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/GradientFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestGradientFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestGradientFilter.png?raw=true target=)

### Description

Computes the gradient of a scalar field defined on the points of a data set.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/GradientFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GradientFilter.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkDataSetAttributes
from vtkmodules.vtkFiltersCore import (
    vtkAssignAttribute,
    vtkExtractEdges,
    vtkGlyph3D,
    vtkTubeFilter,
)
from vtkmodules.vtkFiltersGeneral import vtkGradientFilter
from vtkmodules.vtkFiltersSources import vtkArrowSource
from vtkmodules.vtkIOLegacy import vtkUnstructuredGridReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Gradient filter.'
    epilogue = '''
    Computes the gradient of a scalar field defined on the points of a data set.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='uGridEx.vtk')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()
    colors.SetColor('bkg', 84, 89, 109, 255)

    file_name = get_program_parameters()

    # Create the reader for the data.
    # This is the data that will be rendered.
    reader = vtkUnstructuredGridReader(file_name=file_name)

    edges = vtkExtractEdges()

    tubes = vtkTubeFilter(radius=0.0625, vary_radius=False, number_of_sides=32)

    tubes_mapper = vtkPolyDataMapper(scalar_range=(0.0, 26.0))
    reader >> edges >> tubes >> tubes_mapper

    tubes_actor = vtkActor(mapper=tubes_mapper)

    gradients = vtkGradientFilter()

    vectors = vtkAssignAttribute()
    vectors.Assign('Gradients', vtkDataSetAttributes.VECTORS, vtkAssignAttribute.POINT_DATA)
    reader >> gradients >> vectors

    arrow = vtkArrowSource()
    glyphs = vtkGlyph3D(scaling=True, scale_mode=Glyph3D.ScaleMode.VTK_SCALE_BY_VECTOR,
                        scale_factor=0.25, orient=True, clamping=False,
                        vector_mode=Glyph3D.VectorMode.VTK_USE_VECTOR,
                        index_mode=False)
    select_ports(vectors, 0) >> glyphs
    arrow >> select_ports(1, glyphs)

    glyph_mapper = vtkPolyDataMapper(scalar_visibility=False)
    glyphs >> glyph_mapper

    glyph_actor = vtkActor(mapper=glyph_mapper)

    # A renderer, render window and interactor.
    ren = vtkRenderer(background=colors.GetColor3d('bkg'))
    ren_win = vtkRenderWindow(size=(350, 500), window_name='GradientFilter')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    ren.AddActor(tubes_actor)
    ren.AddActor(glyph_actor)

    ren_win.Render()

    camera = ren.active_camera
    camera.Elevation(-80.0)
    camera.OrthogonalizeViewUp()
    camera.Azimuth(135.0)

    iren.Start()

@dataclass(frozen=True)
class Glyph3D:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_BY_SCALE: int = 0
        VTK_COLOR_BY_SCALAR: int = 1
        VTK_COLOR_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class IndexMode:
        VTK_INDEXING_OFF: int = 0
        VTK_INDEXING_BY_SCALAR: int = 1
        VTK_INDEXING_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class ScaleMode:
        VTK_SCALE_BY_SCALAR: int = 0
        VTK_SCALE_BY_VECTOR: int = 1
        VTK_SCALE_BY_VECTORCOMPONENTS: int = 2
        VTK_DATA_SCALING_OFF: int = 3

    @dataclass(frozen=True)
    class VectorMode:
        VTK_USE_VECTOR: int = 0
        VTK_USE_NORMAL: int = 1
        VTK_VECTOR_ROTATION_OFF: int = 2
        VTK_FOLLOW_CAMERA_DIRECTION: int = 3

if __name__ == '__main__':
    main()
```
