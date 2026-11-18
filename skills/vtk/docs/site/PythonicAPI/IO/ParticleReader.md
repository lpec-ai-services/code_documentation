<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/ParticleReader/ -->

# ParticleReader

Repository source: [ParticleReader](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/ParticleReader.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestParticleReader.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestParticleReader.png?raw=true target=)

### Description

This example reads ascii files where each line consists of points with its position (x,y,z) and (optionally) one scalar or binary files in RAW 3d file format.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ParticleReader/)), ([Java](https://examples.vtk.org/site/Java/IO/ParticleReader/)), ([CSharp](https://examples.vtk.org/site/CSharp/IO/ParticleReader/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ParticleReader.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkParticleReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'ParticleReader.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='Particles.raw')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    ifn = get_program_parameters()

    # Check that the file exists.
    ifp = Path(ifn)
    if not ifp.is_file():
        print(f'Nonexistent source: {ifp}')
        return

    # Particles.raw supplied by VTK is big endian encoded.
    # Read the file.
    reader = vtkParticleReader(file_name=ifp)

    # If nothing gets displayed or totally wrong, swap the endianness.
    reader.SetDataByteOrderToBigEndian()
    reader.update()

    # Visualize
    mapper = vtkPolyDataMapper(scalar_range=(4, 9))
    reader >> mapper
    print(f'Number of pieces: {mapper.GetNumberOfPieces()}')

    actor = vtkActor(mapper=mapper)
    actor.property.point_size = 4

    renderer = vtkRenderer()
    render_window = vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.window_name = 'ParticleReader'

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)
    renderer.background = colors.GetColor3d('DarkSlateGray')

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
