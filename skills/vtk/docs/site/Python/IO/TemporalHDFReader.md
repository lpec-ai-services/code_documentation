<!-- source: https://examples.vtk.org/site/Python/IO/TemporalHDFReader/ -->

# TemporalHDFReader

Repository source: [TemporalHDFReader](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/IO/TemporalHDFReader.py)

### Description

That example uses a feature of vtk_hdf5 that is only available in [vtk/master](https://gitlab.kitware.com/vtk/vtk) and will be released with VTK 9.3. See [this blog post](https://www.kitware.com/how-to-write-time-dependent-data-in-vtkhdf-files/) for more information.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/TemporalHDFReader/)), ([PythonicAPI](../../PythonicAPI/IO/TemporalHDFReader.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TemporalHDFReader.py**

```python
#!/usr/bin/env python3

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
    reader = vtkHDFReader()
    reader.SetFileName(fn)
    reader.Update()
    print('Number of steps: ', reader.GetNumberOfSteps())

    # Render the dataset.
    mapper = vtkCompositePolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper.SetLookupTable(get_ctf())
    mapper.SetScalarModeToUsePointFieldData()
    mapper.SelectColorArray('SpatioTemporalHarmonics')

    actor = vtkActor()
    actor.SetMapper(mapper)

    renderer = vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('AntiqueWhite'))
    renderer.UseHiddenLineRemovalOn()
    renderer.AddActor(actor)

    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer)
    ren_win.SetWindowName('TemporalHDFReader')
    ren_win.SetSize(1024, 512)
    ren_win.Render()

    # Add the interactor.
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # Add the animation callback.
    observer = AnimationObserver(iren, reader)

    # You must initialize the vtkRenderWindowInteractor
    # before adding the observer and setting the repeating timer.
    iren.Initialize()
    iren.AddObserver('TimerEvent', observer)
    iren.CreateRepeatingTimer(50)

    i_style = vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(i_style)

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
        step = 0 if (self.reader.GetStep() == self.reader.GetNumberOfSteps() - 1) else self.reader.GetStep() + 1
        self.reader.SetStep(step)
        print('Current step: ', self.reader.GetStep())
        self.reader.Update()
        self.interactor.Render()

if __name__ == '__main__':
    main()
```
