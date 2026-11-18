<!-- source: https://examples.vtk.org/site/PythonicAPI/IO/ReadCML/ -->

# ReadCML

Repository source: [ReadCML](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/IO/ReadCML.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestReadCML.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/IO/TestReadCML.png?raw=true target=)

## Description

This example uses [vtkCMLMoleculeReader](https://www.vtk.org/doc/nightly/html/classvtkCMLMoleculeReader.html) to read a [Chemistry Markup Language](http://www.xml-cml.org/) file. CML has been developed by Peter Murray-Rust and Henry Rzepa since 1995. It is the de facto XML for chemistry, accepted by publishers and with more than 1 million lines of Open Source code supporting it.

Info

This example uses the file porphyrin.cml. A description of the molecule Porphyrin is described [here](https://en.wikipedia.org/wiki/Porphyrin).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/IO/ReadCML/)), ([Java](https://examples.vtk.org/site/Java/IO/ReadCML/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ReadCML.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkDomainsChemistry import vtkMoleculeMapper
from vtkmodules.vtkIOChemistry import vtkCMLMoleculeReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Read CML.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', help='The CML filename e.g. porphyrin.cml')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()
    fn = Path(file_name)
    if not fn.is_file():
        print(f'{fn}\nNot found.')
        return

    cml_source = vtkCMLMoleculeReader(file_name=fn)

    molmapper = vtkMoleculeMapper()
    molmapper.UseBallAndStickSettings()
    cml_source >> molmapper

    actor = vtkActor(mapper=molmapper)
    actor.property.diffuse = 0.7
    actor.property.specular = 0.5
    actor.property.specular_power = 20.0

    ren = vtkRenderer(background=colors.GetColor3d('Silver'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name='ReadCML', multi_samples=0)
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    ren.AddActor(actor)

    ren_win.Render()
    ren.active_camera.Zoom(2.0)

    # Finally render the scene.
    ren_win.interactor.Initialize()
    ren_win.interactor.Start()

if __name__ == '__main__':
    main()
```
