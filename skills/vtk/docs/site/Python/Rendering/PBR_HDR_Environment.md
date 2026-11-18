<!-- source: https://examples.vtk.org/site/Python/Rendering/PBR_HDR_Environment/ -->

# PBR HDR Environment

Repository source: [PBR_HDR_Environment](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Rendering/PBR_HDR_Environment.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestPBR_HDR_Environment.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Rendering/TestPBR_HDR_Environment.png?raw=true target=)

### Description

This example is based on [TestPBRHdrEnvironment.cxx](https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenGL2/Testing/Cxx/TestPBRHdrEnvironment.cxx) and renders spheres with different materials using a skybox as image based lighting.

Physically based rendering sets metallicity, roughness, occlusion strength and normal scaling of the object. Textures are used to set base color, ORM, anisotropy and normals. Textures for the image based lighting and the skymap are supplied from a cubemap.

Image based lighting uses a cubemap texture to specify the environment. A Skybox is used to create the illusion of distant three-dimensional surroundings. Textures for the image based lighting and the skybox are supplied from a HDR or JPEG equirectangular Environment map or cubemap consisting of six image files.

A good source for Skybox HDRs and Textures is [Poly Haven](https://polyhaven.com/all). Start with the 4K HDR versions of Skyboxes.

The parameters used to generate the example image are loaded from a generic JSON file, not all the parameters are used:

```python
<DATA>/PBR_Parameters.json
```

Where `<DATA>` is the path to `vtk-examples/src/Testing/Data`.

For information about the parameters in the JSON file, please see [PBR_JSON_format](https://examples.vtk.org/site/Documentation/PBR_JSON_format/).

#### Further Reading

- [Introducing Physically Based Rendering with VTK](https://blog.kitware.com/vtk-pbr/)
- [PBR Journey Part 1: High Dynamic Range Image Based Lighting with VTK](https://blog.kitware.com/pbrj1/)
- [PBR Journey Part 2 : Anisotropy model with VTK](https://blog.kitware.com/pbr-journey-part-2-anisotropy-model-with-vtk/)
- [PBR Journey Part 3 : Clear Coat Model with VTK](https://blog.kitware.com/pbr-journey-part-3-clear-coat-model-with-vtk/)
- [Object Shading Properties](https://gitlab.kitware.com/paraview/paraview-docs/-/blob/master/doc/source/ReferenceManual/objectShadingProperties.rst)

Note

- `<DATA>/PBR_Parameters.json` assumes that the skyboxes and textures are in the subfolders `Skyboxes` and `Textures` relative to this file This allows you to copy this JSON file and the associated subfolders to any other location on your computer.
- You can turn off the skybox in the JSON file by setting `"skybox":false`. Image based lighting will still be active.

Note

- The C++ example requires C++17 as `std::filesystem` is used. If your compiler does not support C++17 comment out the filesystem stuff.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/PBR_HDR_Environment/)), ([PythonicAPI](../../PythonicAPI/Rendering/PBR_HDR_Environment.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PBR_HDR_Environment.py**

```python
#!/usr/bin/env python3

import json
from pathlib import Path

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOImage import (
    vtkHDRReader,
    vtkImageReader2Factory
)
from vtkmodules.vtkImagingCore import vtkImageFlip
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkSkybox,
    vtkTexture
)
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLRenderer

def get_program_parameters():
    import argparse
    description = 'Renders spheres with different materials using a skybox as image based lighting.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The path to the JSON file.')
    parser.add_argument('-c', '--use_cubemap', action='store_true',
                        help='Build the cubemap from the six cubemap files.'
                             ' Overrides the equirectangular entry in the json file.')
    args = parser.parse_args()
    return args.file_name, args.use_cubemap

def main():
    fn, use_cubemap = get_program_parameters()
    fn_path = Path(fn)
    if not fn_path.suffix:
        fn_path = fn_path.with_suffix(".json")
    if not fn_path.is_file():
        print('Unable to find: ', fn_path)
    paths_ok, parameters = get_parameters(fn_path)
    if not paths_ok:
        return
    res = display_parameters(parameters)
    print('\n'.join(res))
    print()

    colors = vtkNamedColors()

    ren = vtkOpenGLRenderer()
    ren.SetBackground(colors.GetColor3d('Black'))

    ren_win = vtkRenderWindow()
    ren_win.SetSize(600, 600)
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    style = vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)

    skybox = vtkSkybox()

    irradiance = ren.GetEnvMapIrradiance()
    irradiance.SetIrradianceStep(0.3)

    # Choose how to generate the skybox.
    is_hdr = False
    has_skybox = False
    gamma_correct = False

    if use_cubemap and 'cubemap' in parameters.keys():
        print('Using the cubemap files to generate the environment texture.')
        env_texture = read_cubemap(parameters['cubemap'])
        if parameters['skybox']:
            skybox.SetTexture(env_texture)
            has_skybox = True
    elif 'equirectangular' in parameters.keys():
        print('Using the equirectangular file to generate the environment texture.')
        env_texture = read_equirectangular_file(parameters['equirectangular'])
        if parameters['equirectangular'].suffix.lower() in '.hdr .pic':
            gamma_correct = True
            is_hdr = True
        if parameters['skybox']:
            # Generate a skybox.
            skybox.SetFloorRight(0, 0, 1)
            skybox.SetProjection(vtkSkybox.Sphere)
            skybox.SetTexture(env_texture)
            has_skybox = True
    else:
        print('An environment texture is required,\n'
              'please add the necessary equirectangular'
              ' or cubemap file paths to the json file.')
        return

    ren.UseImageBasedLightingOn()
    if is_hdr:
        ren.UseSphericalHarmonicsOn()
        ren.SetEnvironmentTexture(env_texture, False)
    else:
        ren.UseSphericalHarmonicsOff()
        ren.SetEnvironmentTexture(env_texture, True)

    sphere = vtkSphereSource()
    sphere.SetThetaResolution(75)
    sphere.SetPhiResolution(75)

    pd_sphere = vtkPolyDataMapper()
    pd_sphere.SetInputConnection(sphere.GetOutputPort())

    for i in range(0, 6):
        actor_sphere = vtkActor()
        actor_sphere.SetPosition(i, 0.0, 0.0)
        actor_sphere.SetMapper(pd_sphere)
        actor_sphere.GetProperty().SetInterpolationToPBR()
        actor_sphere.GetProperty().SetColor(colors.GetColor3d('White'))
        actor_sphere.GetProperty().SetMetallic(1.0)
        actor_sphere.GetProperty().SetRoughness(i / 5.0)
        ren.AddActor(actor_sphere)

    if has_skybox:
        if gamma_correct:
            skybox.GammaCorrectOn()
        else:
            skybox.GammaCorrectOff()
        ren.AddActor(skybox)

    ren_win.SetWindowName('PBR_HDR_Environment')

    ren_win.Render()
    iren.Start()

def get_parameters(fn_path):
    """
    Read the parameters from a JSON file and check that the file paths exist.

    :param fn_path: The path to the JSON file.
    :return: True if the paths correspond to files and the parameters.
    """
    with open(fn_path) as data_file:
        json_data = json.load(data_file)
    parameters = dict()

    # Extract the values.
    keys_no_paths = {'title', 'object', 'objcolor', 'bkgcolor', 'skybox'}
    keys_with_paths = {'cubemap', 'equirectangular', 'albedo', 'normal', 'material', 'coat', 'anisotropy', 'emissive'}
    paths_ok = True
    for k, v in json_data.items():
        if k in keys_no_paths:
            parameters[k] = v
            continue
        if k in keys_with_paths:
            if k == 'cubemap':
                if ('root' in v) and ('files' in v):
                    root = Path(v['root'])
                    if not root.exists():
                        print(f'Bad cubemap path: {root}')
                        paths_ok = False
                    elif len(v['files']) != 6:
                        print(f'Expect six cubemap file names.')
                        paths_ok = False
                    else:
                        cm = list(map(lambda p: root / p, v['files']))
                        for fn in cm:
                            if not fn.is_file():
                                paths_ok = False
                                print(f'Not a file {fn}')
                        if paths_ok:
                            parameters['cubemap'] = cm
                else:
                    paths_ok = False
                    print('Missing the key "root" and/or the key "fíles" for the cubemap.')
            else:
                fn = Path(v)
                if not fn.exists():
                    print(f'Bad {k} path: {fn}')
                    paths_ok = False
                else:
                    parameters[k] = fn

    # Set Boy as the default surface.
    if ('object' in parameters.keys() and not parameters['object']) or 'object' not in parameters.keys():
        parameters['object'] = 'Boy'

    return paths_ok, parameters

def display_parameters(parameters):
    res = list()
    parameter_keys = ['title', 'object', 'objcolor', 'bkgcolor', 'skybox', 'cubemap', 'equirectangular', 'albedo',
                      'normal', 'material', 'coat', 'anisotropy', 'emissive']
    for k in parameter_keys:
        if k != 'cubemap':
            if k in parameters:
                res.append(f'{k:15}: {parameters[k]}')
        else:
            if k in parameters:
                for idx in range(len(parameters[k])):
                    if idx == 0:
                        res.append(f'{k:15}: {parameters[k][idx]}')
                    else:
                        res.append(f'{" " * 17}{parameters[k][idx]}')
    return res

def read_cubemap(cubemap):
    """
    Read six images forming a cubemap.

    :param cubemap: The paths to the six cubemap files.
    :return: The cubemap texture.
    """
    cube_map = vtkTexture()
    cube_map.CubeMapOn()

    i = 0
    for fn in cubemap:
        # Read the images.
        reader_factory = vtkImageReader2Factory()
        img_reader = reader_factory.CreateImageReader2(str(fn))
        img_reader.SetFileName(str(fn))

        # Each image must be flipped in Y due to canvas
        #  versus vtk ordering.
        flip = vtkImageFlip()
        flip.SetInputConnection(img_reader.GetOutputPort(0))
        flip.SetFilteredAxis(1)  # flip y axis
        cube_map.SetInputConnection(i, flip.GetOutputPort())
        i += 1

    cube_map.MipmapOn()
    cube_map.InterpolateOn()

    return cube_map

def read_equirectangular_file(fn_path):
    """
    Read an equirectangular environment file and convert to a texture.

    :param fn_path: The equirectangular file path.
    :return: The texture.
    """
    texture = vtkTexture()

    suffix = fn_path.suffix.lower()
    if suffix in ['.jpeg', '.jpg', '.png']:
        reader_factory = vtkImageReader2Factory()
        img_reader = reader_factory.CreateImageReader2(str(fn_path))
        img_reader.SetFileName(str(fn_path))

        texture.SetInputConnection(img_reader.GetOutputPort(0))

    else:
        reader = vtkHDRReader()
        extensions = reader.GetFileExtensions()
        # Check the image can be read.
        if not reader.CanReadFile(str(fn_path)):
            print('CanReadFile failed for ', fn_path)
            return None
        if suffix not in extensions:
            print('Unable to read this file extension: ', suffix)
            return None
        reader.SetFileName(str(fn_path))

        texture.SetColorModeToDirectScalars()
        texture.SetInputConnection(reader.GetOutputPort())

    texture.MipmapOn()
    texture.InterpolateOn()

    return texture

if __name__ == '__main__':
    main()
```
