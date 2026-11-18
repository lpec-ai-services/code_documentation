<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/ProteinRibbons/ -->

# ProteinRibbons

Repository source: [ProteinRibbons](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/ProteinRibbons.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestProteinRibbons.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestProteinRibbons.png?raw=true target=)

## Description

This example reads [Protein Data Bank](http://www.pdb.org/pdb/home/home.do) files. The example expects a file in .pdb format.

Here `src/Testing/Data/2j6g.pdb` is the sample file.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/ProteinRibbons/)), ([Java](https://examples.vtk.org/site/Java/Visualization/ProteinRibbons/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ProteinRibbons.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkDomainsChemistry import vtkProteinRibbonFilter
from vtkmodules.vtkIOChemistry import vtkPDBReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Read a Protein Data Bank file.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='E.g. 2j6g.pdb.')
    args = parser.parse_args()
    return args.filename

def main():
    file_name = get_program_parameters()

    fn = Path(file_name)
    if not fn.is_file():
        print(f'{fn} not found.')
        return

    colors = vtkNamedColors()

    # Read the protein from the pdb.
    reader = vtkPDBReader(file_name=file_name)

    # Set up the ribbon filter.
    ribbon_filter = vtkProteinRibbonFilter()

    # Set up poly data mapper.
    poly_data_mapper = vtkPolyDataMapper()
    reader >> ribbon_filter >> poly_data_mapper

    # Set up the actor.
    actor = vtkActor(mapper=poly_data_mapper)
    actor.property.diffuse = 0.7
    actor.property.specular = 0.5
    actor.property.specular_power = 80.0

    # Set up the render window.
    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    render_window = vtkRenderWindow(multi_samples=0, size=(640, 480), window_name='ProteinRibbons')
    render_window.AddRenderer(renderer)
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    interactor.interactor_style.SetCurrentStyleToTrackballCamera()

    colors = vtkNamedColors()
    renderer.AddActor(actor)

    render_window.Render()
    renderer.ResetCamera()
    renderer.active_camera.Azimuth(45)
    renderer.active_camera.Elevation(45)
    renderer.active_camera.Zoom(1.7)
    renderer.ResetCameraClippingRange()
    render_window.Render()

    # Finally render the scene.
    interactor.Initialize()
    interactor.Start()

if __name__ == '__main__':
    main()
```
