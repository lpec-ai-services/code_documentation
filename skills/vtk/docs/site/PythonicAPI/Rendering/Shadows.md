<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/Shadows/ -->

# Shadows

Repository source: [Shadows](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/Shadows.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestShadows.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestShadows.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/Shadows/)), ([Python](../../Python/Rendering/Shadows.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Shadows.py**

```python
#!/usr/bin/env python3

import sys
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkCubeSource,
    vtkSphereSource
)
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCameraPass,
    vtkLight,
    vtkPolyDataMapper,
    vtkRenderPassCollection,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkSequencePass, vtkProperty,
)
from vtkmodules.vtkRenderingOpenGL2 import vtkShadowMapPass

def get_program_parameters():
    import argparse
    description = 'Read a polydata file of a surface and display it with shadows.'
    epilogue = '''
    If no file is entered a sphere is used.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', default=None, nargs='?',
                        help='Enter a polydata file e.g dragon.ply.')
    args = parser.parse_args()
    return args.filename

def main():
    fn = get_program_parameters()
    if fn:
        poly_data = read_poly_data(fn)
    else:
        # Use a sphere
        source = vtkSphereSource(theta_resolution=100, phi_resolution=100)
        source.SetThetaResolution(100)
        source.update()
        poly_data = source.output

    colors = vtkNamedColors()
    colors.SetColor('HighNoonSun', [255, 255, 251, 255])  # Color temp. 5400°K
    colors.SetColor('100W Tungsten', [255, 214, 170, 255])  # Color temp. 2850°K

    ren = vtkRenderer(background=colors.GetColor3d('Silver'))

    ren_win = vtkRenderWindow(size=(640, 480), multi_samples=0,
                              window_name=f'{Path(sys.argv[0]).stem:s}')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    light1 = vtkLight(focal_point=(0, 0, 0), position=(0, 1, 0.2),
                      color=colors.GetColor3d('HighNoonSun'),
                      intensity=0.3)
    ren.AddLight(light1)

    light2 = vtkLight(focal_point=(0, 0, 0), position=(1.0, 1.0, 1.0),
                      color=colors.GetColor3d('100W Tungsten'),
                      intensity=0.8)
    ren.AddLight(light2)

    mapper = vtkPolyDataMapper(input_data=poly_data)

    actor_prop = vtkProperty(ambient_color=colors.GetColor3d('SaddleBrown'),
                             diffuse_color=colors.GetColor3d('Sienna'),
                             specular_color=colors.GetColor3d('White'),
                             specular=0.51, diffuse=0.7, ambient=0.7,
                             specular_power=30.0, opacity=1.0)

    actor = vtkActor(mapper=mapper, property=actor_prop)

    ren.AddActor(actor)

    # Add a plane
    bounds = poly_data.bounds

    rnge = [0] * 3
    rnge[0] = bounds[1] - bounds[0]
    rnge[1] = bounds[3] - bounds[2]
    rnge[2] = bounds[5] - bounds[4]
    # print('Range: ', ', '.join(['{:g}'.format(i) for i in rnge]))
    expand = 1.0
    thickness = rnge[2] * 0.1
    plane = vtkCubeSource()
    plane.SetCenter((bounds[1] + bounds[0]) / 2.0,
                    bounds[2] - thickness / 2.0,
                    (bounds[5] + bounds[4]) / 2.0)
    plane.SetXLength(bounds[1] - bounds[0] + (rnge[0] * expand))
    plane.SetYLength(thickness)
    plane.SetZLength(bounds[5] - bounds[4] + (rnge[2] * expand))

    plane_mapper = vtkPolyDataMapper()
    plane_mapper.SetInputConnection(plane.GetOutputPort())

    plane_actor = vtkActor(mapper=plane_mapper)

    ren.AddActor(plane_actor)

    shadows = vtkShadowMapPass()

    passes = vtkRenderPassCollection()
    passes.AddItem(shadows.GetShadowMapBakerPass())
    passes.AddItem(shadows)

    seq = vtkSequencePass(passes=passes)

    camera_p = vtkCameraPass(delegate_pass=seq)

    # Tell the renderer to use our render pass pipeline
    glren = ren
    glren.SetPass(camera_p)

    ren.GetActiveCamera().SetPosition(-0.2, 0.2, 1)
    ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
    ren.GetActiveCamera().SetViewUp(0, 1, 0)
    ren.ResetCamera()
    ren.GetActiveCamera().Dolly(2.25)
    ren.ResetCameraClippingRange()

    ren_win.Render()

    iren.Start()

def read_poly_data(file_name):
    if not file_name:
        print(f'No file name.')
        return None

    valid_suffixes = ['.g', '.obj', '.stl', '.ply', '.vtk', '.vtp']
    path = Path(file_name)
    ext = None
    if path.suffix:
        ext = path.suffix.lower()
    if path.suffix not in valid_suffixes:
        print(f'No reader for this file suffix: {ext}')
        return None

    reader = None
    if ext == '.ply':
        reader = vtkPLYReader(file_name=file_name)
    elif ext == '.vtp':
        reader = vtkXMLPolyDataReader(file_name=file_name)
    elif ext == '.obj':
        reader = vtkOBJReader(file_name=file_name)
    elif ext == '.stl':
        reader = vtkSTLReader(file_name=file_name)
    elif ext == '.vtk':
        reader = vtkPolyDataReader(file_name=file_name)
    elif ext == '.g':
        reader = vtkBYUReader(file_name=file_name)

    if reader:
        return reader.update().output
    else:
        return None

if __name__ == '__main__':
    main()
```
