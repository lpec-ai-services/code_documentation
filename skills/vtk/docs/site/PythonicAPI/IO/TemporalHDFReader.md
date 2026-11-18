<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/TemporalHDFReader/ -->

# TemporalHDFReader

Repository source: [TemporalHDFReader](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/TemporalHDFReader.py)

### Description

That example uses a feature of vtk_hdf5 that is only available in [vtk/master](https://gitlab.kitware.com/vtk/vtk) and will be released with VTK 9.3. See [this blog post](https://www.kitware.com/how-to-write-time-dependent-data-in-vtkhdf-files/) for more information.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/TemporalHDFReader/)), ([Python](../../Python/IO/TemporalHDFReader.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TemporalHDFReader.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
from vtkmodules.vtkCommonColor import (vtkNamedColors,
                                       vtkColorSeries)
from vtkmodules.vtkIOHDF import vtkHDFReader
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCompositePolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Read temporal data written inside a vtkhdf file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='warping_spheres.vtkhdf')
    args = parser.parse_args()
    return args.file_name

def main():
    fn = get_program_parameters()

    colors = vtkNamedColors()

    # Read the dataset.
    reader = vtkHDFReader(file_name=fn)
    reader.update()
    print('Number of steps: ', reader.GetNumberOfSteps())

    # Render the dataset.
    mapper = vtkCompositePolyDataMapper(lookup_table=get_ctf(),
                                        scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_POINT_FIELD_DATA)
    mapper.SelectColorArray('SpatioTemporalHarmonics')
    reader >> mapper

    actor = vtkActor(mapper=mapper)

    renderer = vtkRenderer(use_hidden_line_removal=True, background=colors.GetColor3d('AntiqueWhite'))
    renderer.AddActor(actor)

    ren_win = vtkRenderWindow(size=(1024, 512), window_name='TemporalHDFReader')
    ren_win.AddRenderer(renderer)
    ren_win.Render()

    # Add the interactor.
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the animation callback.
    observer = AnimationObserver(iren, reader)

    # You must initialize the vtkRenderWindowInteractor
    # before adding the observer and setting the repeating timer.
    iren.Initialize()
    iren.AddObserver('TimerEvent', observer)
    iren.CreateRepeatingTimer(50)

    i_style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = i_style

    iren.Start()

def get_ctf():
    series = vtkColorSeries()
    series.SetColorScheme(vtkColorSeries.WARM)

    return series.CreateLookupTable(vtkColorSeries.ORDINAL)

class AnimationObserver(object):
    def __init__(self, interactor, reader):
        self.interactor = interactor
        self.reader = reader

    def __call__(self, caller, ev):
        step = 0 if (self.reader.step == self.reader.GetNumberOfSteps() - 1) else self.reader.step + 1
        self.reader.step = step
        print(f'Current step: {self.reader.step:3d}')
        self.reader.update()
        self.interactor.Render()

@dataclass(frozen=True)
class ColorTransferFunction:
    @dataclass(frozen=True)
    class ColorSpace:
        VTK_CTF_RGB: int = 0
        VTK_CTF_HSV: int = 1
        VTK_CTF_LAB: int = 2
        VTK_CTF_DIVERGING: int = 3
        VTK_CTF_LAB_CIEDE2000: int = 4
        VTK_CTF_STEP: int = 5

    @dataclass(frozen=True)
    class Scale:
        VTK_CTF_LINEAR: int = 0
        VTK_CTF_LOG10: int = 1

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
