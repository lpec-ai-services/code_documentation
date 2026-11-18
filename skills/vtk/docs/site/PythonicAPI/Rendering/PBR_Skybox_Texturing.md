<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/PBR_Skybox_Texturing/ -->

# PBR Skybox Texturing

Repository source: [PBR_Skybox_Texturing](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/PBR_Skybox_Texturing.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestPBR_Skybox_Texturing.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestPBR_Skybox_Texturing.png?raw=true target=)

### Description

Demonstrates physically based rendering (PBR) using image based lighting, texturing and a skybox.

Physically based rendering sets metallicity, roughness, occlusion strength, the emissive factor and normal scaling of the object. Textures are used to set base color, ORM, emissivity and normals. Textures for the image based lighting and the skymap are supplied from a cubemap.

Image based lighting uses a cubemap texture to specify the environment. A Skybox is used to create the illusion of distant three-dimensional surroundings. Textures for the image based lighting and the skybox are supplied from an HDR or JPEG equirectangular Environment map or cubemap consisting of six image files.

A good source for Skybox HDRs and Textures is [Poly Haven](https://polyhaven.com/all). Start with the 4K HDR versions of Skyboxes.

The parameters used to generate the example image are loaded from a JSON file with the same name as the example. In this case:

```python
<DATA>/PBR_Skybox_Texturing.json
```

Where `<DATA>` is the path to `vtk-examples/src/Testing/Data`.

By default we use the equirectangular file to generate the texture for the lighting and skybox. We have optionally provided six individual cubemap files to generate lighting and a skybox.

For information about the parameters in the JSON file, please see [PBR_JSON_format](https://examples.vtk.org/site/Documentation/PBR_JSON_format/).

### Options

```python
Positionals:
 fileName              The path to the JSON file containing the parameters.

Options:
 -h,--help             Print this help message and exit
 -s,--surface          The name of the surface. Overrides the surface entry in the json file.
 -c,--use_cubemap      Build the cubemap from the six cubemap files. Overrides the equirectangular entry in the json file.
 -t, --use_tonemapping Use tone mapping.
```

Additionally, you can save a screenshot by pressing "k".

#### Further Reading

- [Introducing Physically Based Rendering with VTK](https://blog.kitware.com/vtk-pbr/)
- [PBR Journey Part 1: High Dynamic Range Image Based Lighting with VTK](https://blog.kitware.com/pbrj1/)
- [PBR Journey Part 2 : Anisotropy model with VTK](https://blog.kitware.com/pbr-journey-part-2-anisotropy-model-with-vtk/)
- [PBR Journey Part 3 : Clear Coat Model with VTK](https://blog.kitware.com/pbr-journey-part-3-clear-coat-model-with-vtk/)
- [Object Shading Properties](https://gitlab.kitware.com/paraview/paraview-docs/-/blob/master/doc/source/ReferenceManual/objectShadingProperties.rst)

Note

- `<DATA>/PBR_Skybox_Texturing.json` assumes that the skyboxes and textures are in the subfolders `Skyboxes` and `Textures` relative to this file. This allows you to copy this JSON file and the associated subfolders to any other location on your computer.
- You can turn off the skybox in the JSON file by setting `"skybox":false`. Image based lighting will still be active.

Note

- The C++ example requires C++17 as `std::filesystem` is used. If your compiler does not support C++17 comment out the filesystem stuff.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/PBR_Skybox_Texturing/)), ([Python](../../Python/Rendering/PBR_Skybox_Texturing.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**PBR_Skybox_Texturing.py**

```python
#!/usr/bin/env python3

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonComputationalGeometry import (
    vtkParametricBoy,
    vtkParametricMobius,
    vtkParametricRandomHills,
    vtkParametricTorus
)
from vtkmodules.vtkCommonCore import (
    vtkCommand,
    vtkFloatArray
)
from vtkmodules.vtkCommonDataModel import vtkPlane
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import (
    vtkCleanPolyData,
    vtkClipPolyData,
    vtkPolyDataNormals,
    vtkPolyDataTangents,
    vtkTriangleFilter
)
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersModeling import vtkLinearSubdivisionFilter
from vtkmodules.vtkFiltersSources import (
    vtkCubeSource,
    vtkParametricFunctionSource,
    vtkTexturedSphereSource
)
from vtkmodules.vtkIOImage import (
    vtkHDRReader,
    vtkJPEGWriter,
    vtkImageReader2Factory,
    vtkPNGWriter
)
from vtkmodules.vtkImagingCore import vtkImageFlip
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkOrientationMarkerWidget,
    vtkSliderRepresentation2D,
    vtkSliderWidget
)
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCameraPass,
    vtkLightsPass,
    vtkOpaquePass,
    vtkOverlayPass,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderPassCollection,
    vtkRenderWindowInteractor,
    vtkSequencePass,
    vtkSkybox,
    vtkTexture,
    vtkWindowToImageFilter
)
from vtkmodules.vtkRenderingOpenGL2 import (
    vtkToneMappingPass
)

def get_program_parameters():
    import argparse
    description = 'Demonstrates physically based rendering, image based lighting, texturing and a skybox.'
    epilogue = '''
Physically based rendering sets color, metallicity and roughness of the object.
Image based lighting uses a cubemap texture to specify the environment.
Texturing is used to generate lighting effects.
A Skybox is used to create the illusion of distant three-dimensional surroundings.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The path to the JSON file e.g. PBR_Skybox_Texturing.json.')
    parser.add_argument('-s', '--surface', default='',
                        help='The name of the surface. Overrides the surface entry in the json file.')
    parser.add_argument('-c', '--use_cubemap', action='store_true',
                        help='Build the cubemap from the six cubemap files.'
                             ' Overrides the equirectangular entry in the json file.')
    parser.add_argument('-t', '--use_tonemapping', action='store_true',
                        help='Use tone mapping.')
    parser.add_argument('-omw', action='store_false',
                        help='Use an OrientationMarkerWidget instead of a CameraOrientationWidget.')
    args = parser.parse_args()
    return args.file_name, args.surface, args.use_cubemap, args.use_tonemapping, args.omw

def main():
    colors = vtkNamedColors()

    # Default background color.
    # Default background color.
    colors.color = ('BkgColor', (26, 51, 102, 255))
    colors.color = ('VTKBlue', (6, 79, 141, 255))
    # Let's make a complementary colour to VTKBlue.
    colors.color = ('VTKBlueComp', (249, 176, 114, 255))

    fn, surface_name, use_cubemap, use_tonemapping, use_camera_omw = get_program_parameters()

    fn_path = Path(fn)
    if not fn_path.suffix:
        fn_path = fn_path.with_suffix(".json")
    if not fn_path.is_file():
        print('Unable to find: ', fn_path)
        return
    paths_ok, parameters = get_parameters(fn_path)
    if not paths_ok:
        return

    # Check for missing parameters.
    if 'bkgcolor' not in parameters.keys():
        parameters['bkgcolor'] = 'BkgColor'
    if 'objcolor' not in parameters.keys():
        parameters['objcolor'] = 'White'
    if 'skybox' not in parameters.keys():
        parameters['skybox'] = False
    if surface_name:
        parameters['object'] = surface_name

    if not check_for_missing_textures(parameters, ['albedo', 'normal', 'material', 'emissive']):
        return

    res = display_parameters(parameters)
    print('\n'.join(res))
    print()

    # Build the pipeline.
    # ren1 is for the slider rendering,
    # ren2 is for the object rendering.
    ren1 = vtkRenderer(background=colors.GetColor3d('Snow'), viewport=(0.0, 0.0, 0.2, 1.0))
    ren2 = vtkRenderer(background=colors.GetColor3d(parameters['bkgcolor']), viewport=(0.2, 0.0, 1, 1))

    name = Path(sys.argv[0]).stem
    render_window = vtkRenderWindow(size=(1000, 625), window_name=name)
    render_window.AddRenderer(ren1)
    render_window.AddRenderer(ren2)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window
    style = vtkInteractorStyleTrackballCamera()
    interactor.interactor_style = style

    # Set up tone mapping, so we can vary the exposure.
    # Custom Passes.
    camera_p = vtkCameraPass()
    seq = vtkSequencePass()
    opaque = vtkOpaquePass()
    lights = vtkLightsPass()
    overlay = vtkOverlayPass()

    passes = vtkRenderPassCollection()
    passes.AddItem(lights)
    passes.AddItem(opaque)
    passes.AddItem(overlay)
    seq.passes = passes
    camera_p.delegate_pass = seq

    tone_mapping_p = vtkToneMappingPass(delegate_pass=camera_p)

    if use_tonemapping:
        ren2.SetPass(tone_mapping_p)

    skybox = vtkSkybox()

    ren2.env_map_irradiance.irradiance_step = 0.3

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

    # Turn off the default lighting and use image based lighting.
    ren2.automatic_light_creation = False
    ren2.use_image_based_lighting = True
    if is_hdr:
        ren2.use_spherical_harmonics = True
        ren2.SetEnvironmentTexture(env_texture, False)
    else:
        ren2.use_spherical_harmonics = False
        ren2.SetEnvironmentTexture(env_texture, True)

    # Get the textures
    base_color = read_texture(parameters['albedo'])
    base_color.use_srgb_color_space = True
    normal = read_texture(parameters['normal'])
    material = read_texture(parameters['material'])
    emissive = read_texture(parameters['emissive'])
    emissive.use_srgb_color_space = True

    # Get the surface
    surface = parameters['object'].lower()
    available_surfaces = {'boy', 'mobius', 'random hills', 'torus', 'sphere', 'clipped sphere', 'cube', 'clipped cube'}
    if surface not in available_surfaces:
        print(f'\nThe requested surface: {parameters["object"]} is not available.')
        print('Available surfaces are:')
        asl = sorted(list(available_surfaces))
        asl = [asl[i].title() for i in range(0, len(asl))]
        asl = [asl[i:i + 5] for i in range(0, len(asl), 5)]
        for i in range(0, len(asl)):
            s = ', '.join(asl[i])
            if i < len(asl) - 1:
                s += ','
            print(f'   {s}')
        return

    if surface == 'mobius':
        source = get_mobius()
    elif surface == 'random hills':
        source = get_random_hills()
    elif surface == 'torus':
        source = get_torus()
    elif surface == 'sphere':
        source = get_sphere()
    elif surface == 'clipped sphere':
        source = get_clipped_sphere()
    elif surface == 'cube':
        source = get_cube()
    elif surface == 'clipped cube':
        source = get_clipped_cube()
    else:
        source = get_boy()

    mapper = vtkPolyDataMapper()
    source >> mapper

    exposure_coefficient = 1.0
    # Let's use a nonmetallic surface.
    diffuse_coefficient = 1.0
    roughness_coefficient = 0.3
    metallic_coefficient = 0.0
    # Other parameters.
    occlusion_strength = 1.0
    normal_scale = 1.0
    emissive_factor = [1.0, 1.0, 1.0]

    actor = vtkActor(mapper=mapper)
    # Enable PBR on the model.
    actor.property.SetInterpolationToPBR()
    # Configure the basic properties.
    actor.property.color = colors.GetColor3d(parameters['objcolor'])
    actor.property.diffuse = diffuse_coefficient
    actor.property.roughness = roughness_coefficient
    actor.property.metallic = metallic_coefficient
    # Configure textures (needs tcoords on the mesh).
    actor.property.base_color_texture = base_color
    actor.property.o_r_m_texture = material
    actor.property.occlusion_strength = occlusion_strength
    actor.property.emissive_texture = emissive
    actor.property.emissive_factor = emissive_factor
    # Needs tcoords, normals and tangents on the mesh.
    actor.property.normal_texture = normal
    actor.property.normal_scale = normal_scale
    ren2.AddActor(actor)

    if has_skybox:
        if gamma_correct:
            skybox.GammaCorrectOn()
        else:
            skybox.GammaCorrectOff()
        ren2.AddActor(skybox)

    # Create the slider callbacks to manipulate various parameters.
    step_size = 1.0 / 5
    y_val = 0.1
    # Setup a slider widget for each varying parameter.
    slider_properties = make_slider_2d_properties()

    slider_properties.Range.maximum_value = 5.0
    slider_properties.Range.value = exposure_coefficient
    slider_properties.Position.point1 = (0.1, y_val)
    slider_properties.Position.point2 = (0.9, y_val)
    slider_properties.Text.title = 'Exposure'
    if use_tonemapping:
        sw_exposure = make_2d_slider_widget(slider_properties, interactor)
        sw_exposure_cb = SliderCallbackExposure(tone_mapping_p)
        sw_exposure.AddObserver(vtkCommand.InteractionEvent, sw_exposure_cb)

    y_val += step_size
    slider_properties.Range.maximum_value = 1.0
    slider_properties.Range.value = metallic_coefficient
    slider_properties.Position.point1 = (0.1, y_val)
    slider_properties.Position.point2 = (0.9, y_val)
    slider_properties.Text.title = 'Metallicity'
    sw_metallic = make_2d_slider_widget(slider_properties, interactor)
    sw_metallic_cb = SliderCallbackMetallic(actor.GetProperty())
    sw_metallic.AddObserver(vtkCommand.InteractionEvent, sw_metallic_cb)

    y_val += step_size
    slider_properties.Range.maximum_value = 1.0
    slider_properties.Range.value = roughness_coefficient
    slider_properties.Position.point1 = (0.1, y_val)
    slider_properties.Position.point2 = (0.9, y_val)
    slider_properties.Text.title = 'Roughness'
    sw_roughness = make_2d_slider_widget(slider_properties, interactor)
    sw_roughness_cb = SliderCallbackRoughness(actor.GetProperty())
    sw_roughness.AddObserver(vtkCommand.InteractionEvent, sw_roughness_cb)

    y_val += step_size
    slider_properties.Range.maximum_value = 5.0
    slider_properties.Range.value = occlusion_strength
    slider_properties.Position.point1 = (0.1, y_val)
    slider_properties.Position.point2 = (0.9, y_val)
    slider_properties.Text.title = 'Occlusion'
    sw_occlusion_strength = make_2d_slider_widget(slider_properties, interactor)
    sw_occlusion_strength_cb = SliderCallbackOcclusionStrength(actor.GetProperty())
    sw_occlusion_strength.AddObserver(vtkCommand.InteractionEvent, sw_occlusion_strength_cb)

    y_val += step_size
    slider_properties.Range.maximum_value = 5.0
    slider_properties.Range.value = normal_scale
    slider_properties.Position.point1 = (0.1, y_val)
    slider_properties.Position.point2 = (0.9, y_val)
    slider_properties.Text.title = 'Normal'
    sw_normal = make_2d_slider_widget(slider_properties, interactor)
    sw_normal_cb = SliderCallbackNormalScale(actor.GetProperty())
    sw_normal.AddObserver(vtkCommand.InteractionEvent, sw_normal_cb)

    render_window.Render()

    if use_camera_omw:
        cam_orient_manipulator = vtkCameraOrientationWidget()
        cam_orient_manipulator.SetParentRenderer(ren2)
        # Enable the widget.
        cam_orient_manipulator.On()
    else:
        rgb = [0.0] * 4
        colors.GetColor("Carrot", rgb)
        rgb = tuple(rgb[:3])
        widget = vtkOrientationMarkerWidget(orientation_marker=vtkAxesActor(),
                                            interactor=interactor, default_renderer=ren2,
                                            outline_color=rgb, viewport=(0.8, 0.8, 1.0, 1.0),
                                            enabled=True, interactive=True, zoom=1.5)

    print_callback = PrintCallback(interactor, name, 1, False)
    # print_callback = PrintCallback(interactor, name + '.jpg', 1, False)
    interactor.AddObserver('KeyPressEvent', print_callback)

    interactor.Start()

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
                    root = fn_path.parent / Path(v['root'])
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
                fn = fn_path.parent / Path(v)
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

    This assumes that the files corresponding to the images
     are already ordered as:
      [right, left, top, bottom, front, back]
      or [+x, -x, +y, -y, +z, -z]

    :param cubemap: The paths to the six cubemap files.
    :return: The cubemap texture.
    """
    cube_map = vtkTexture(cube_map=True, mipmap=True, interpolate=True)

    flipped_images = list()
    for fn in cubemap:
        # Read the images.
        reader_factory = vtkImageReader2Factory()
        img_reader = reader_factory.CreateImageReader2(str(fn))
        img_reader.file_name = str(fn)

        # Each image must be flipped in Y due to canvas
        #  versus vtk ordering.
        flip = vtkImageFlip(filtered_axis=1)
        img_reader >> flip
        flipped_images.append(flip)

    for i in range(0, len(flipped_images)):
        flipped_images[i] >> select_ports(i, cube_map)

    return cube_map

def read_equirectangular_file(fn_path):
    """
    Read an equirectangular environment file and convert to a texture.

    :param fn_path: The equirectangular file path.
    :return: The texture.
    """
    texture = vtkTexture(cube_map=False, mipmap=True, interpolate=True)

    suffix = fn_path.suffix.lower()
    if suffix in ['.jpeg', '.jpg', '.png']:
        reader_factory = vtkImageReader2Factory()
        img_reader = reader_factory.CreateImageReader2(str(fn_path))
        img_reader.SetFileName(str(fn_path))

        img_reader >> texture

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
        reader >> texture

    return texture

def read_texture(image_path):
    """
    Read an image and convert it to a texture
    :param image_path: The image path.
    :return: The texture.
    """

    suffix = image_path.suffix.lower()
    valid_extensions = ['.jpg', '.png', '.bmp', '.tiff', '.pnm', '.pgm', '.ppm']
    if suffix not in valid_extensions:
        print('Unable to read the texture file (wrong extension):', image_path)
        return None

    # Read the images
    reader_factory = vtkImageReader2Factory()
    img_reader = reader_factory.CreateImageReader2(str(image_path))
    img_reader.file_name = str(image_path)

    texture = vtkTexture(interpolate=True)
    img_reader >> texture

    return texture

def check_for_missing_textures(parameters, wanted_textures):
    """
    Check that the needed textures exist.

    :param parameters: The parameters.
    :param wanted_textures: The wanted textures.
    :return: True if all the wanted textures are present.
    """
    have_textures = True
    for texture_name in wanted_textures:
        if texture_name not in parameters:
            print('Missing texture:', texture_name)
            have_textures = False
        elif not parameters[texture_name]:
            print('No texture path for:', texture_name)
            have_textures = False

    return have_textures

def get_boy():
    surface = vtkParametricBoy()

    u_resolution = 51
    v_resolution = 51
    source = vtkParametricFunctionSource(parametric_function=surface,
                                         u_resolution=u_resolution, v_resolution=v_resolution,
                                         generate_texture_coordinates=True)

    tangents = vtkPolyDataTangents()

    return source >> tangents

def get_mobius():
    minimum_v = -0.25
    maximum_v = 0.25
    surface = vtkParametricMobius(minimum_v=minimum_v, maximum_v=maximum_v, )

    u_resolution = 51
    v_resolution = 51
    source = vtkParametricFunctionSource(parametric_function=surface,
                                         u_resolution=u_resolution, v_resolution=v_resolution,
                                         generate_texture_coordinates=True)

    # Build the tangents.
    tangents = vtkPolyDataTangents()

    transform = vtkTransform()
    transform.RotateX(-90.0)

    transform_filter = vtkTransformFilter(transform=transform)

    return source >> tangents >> transform_filter

def get_random_hills():
    random_seed = 1
    number_of_hills = 30
    # If you want a plane
    # hill_amplitude=0
    surface = vtkParametricRandomHills(random_seed=random_seed, number_of_hills=number_of_hills)

    u_resolution = 51
    v_resolution = 51
    source = vtkParametricFunctionSource(parametric_function=surface,
                                         u_resolution=u_resolution, v_resolution=v_resolution,
                                         generate_texture_coordinates=True)

    # Build the tangents.
    tangents = vtkPolyDataTangents()

    transform = vtkTransform()
    transform.Translate(0.0, 5.0, 15.0)
    transform.RotateX(-90.0)

    transform_filter = vtkTransformFilter(transform=transform)

    return source >> tangents >> transform_filter

def get_sphere():
    theta_resolution = 32
    phi_resolution = 32
    surface = vtkTexturedSphereSource(theta_resolution=theta_resolution, phi_resolution=phi_resolution)

    # Now the tangents.
    tangents = vtkPolyDataTangents()

    return surface >> tangents

def get_clipped_sphere():
    theta_resolution = 32
    phi_resolution = 32
    surface = vtkTexturedSphereSource(theta_resolution=theta_resolution, phi_resolution=phi_resolution)

    clip_plane = vtkPlane(origin=(0, 0.3, 0), normal=(0, -1, 0))

    clipper = vtkClipPolyData(clip_function=clip_plane)
    clipper.GenerateClippedOutputOn()

    # Now the tangents.
    tangents = vtkPolyDataTangents()

    return surface >> clipper >> tangents

def get_torus():
    surface = vtkParametricTorus()

    u_resolution = 51
    v_resolution = 51
    source = vtkParametricFunctionSource(parametric_function=surface,
                                         u_resolution=u_resolution, v_resolution=v_resolution,
                                         generate_texture_coordinates=True)

    # Build the tangents.
    tangents = vtkPolyDataTangents()

    transform = vtkTransform()
    transform.RotateX(-90.0)

    transform_filter = vtkTransformFilter(transform=transform)

    return source >> tangents >> transform_filter

def get_cube():
    surface = vtkCubeSource()

    # Triangulate.
    triangulation = vtkTriangleFilter()
    # Subdivide the triangles.
    subdivide = vtkLinearSubdivisionFilter(number_of_subdivisions=3)
    # Build the tangents.
    tangents = vtkPolyDataTangents()

    return surface >> triangulation >> subdivide >> tangents

def get_clipped_cube():
    surface = vtkCubeSource()

    # Triangulate.
    triangulation = vtkTriangleFilter()

    # Subdivide the triangles
    subdivide = vtkLinearSubdivisionFilter(number_of_subdivisions=5)

    clip_plane = vtkPlane(origin=(0, 0.3, 0), normal=(0, -1, -1))

    clipper = vtkClipPolyData(clip_function=clip_plane)
    clipper.GenerateClippedOutputOn()

    cleaner = vtkCleanPolyData(tolerance=0.005)

    normals = vtkPolyDataNormals(feature_angle=60, flip_normals=True)

    # Now the tangents.
    tangents = vtkPolyDataTangents(compute_cell_tangents=True, compute_point_tangents=True)

    return surface >> triangulation >> subdivide >> clipper >> cleaner >> normals >> tangents

def uv_tcoords(u_resolution, v_resolution, pd):
    """
    Generate u, v texture coordinates on a parametric surface.
    :param u_resolution: u resolution
    :param v_resolution: v resolution
    :param pd: The polydata representing the surface.
    :return: The polydata with the texture coordinates added.
    """
    u0 = 1.0
    v0 = 0.0
    du = 1.0 / (u_resolution - 1)
    dv = 1.0 / (v_resolution - 1)
    num_pts = pd.GetNumberOfPoints()
    t_coords = vtkFloatArray(number_of_components=2, number_of_tuples=num_pts, name='Texture Coordinates')
    pt_id = 0
    u = u0
    for i in range(0, u_resolution):
        v = v0
        for j in range(0, v_resolution):
            tc = [u, v]
            t_coords.SetTuple(pt_id, tc)
            v += dv
            pt_id += 1
        u -= du
    pd.point_data.SetTCoords(t_coords)
    return pd

def make_slider_2d_properties():
    """
    This applies more specific values to the default Slider2DProperties.

    :return: The slider 2D properties.
    """
    sp = Slider2DProperties()

    sp.Colors.bar_color = 'Black'
    sp.Colors.bar_ends_color = 'Indigo'
    sp.Colors.label_color = 'Black'
    sp.Colors.selected_color = 'Lime'
    sp.Colors.slider_color = 'BurlyWood'
    sp.Colors.title_color = 'Black'

    sp.Dimensions.end_cap_length = 0.025
    sp.Dimensions.end_cap_width = 0.025
    sp.Dimensions.label_height = 0.020
    sp.Dimensions.slider_length = 0.075
    sp.Dimensions.slider_width = 0.025
    sp.Dimensions.title_height = 0.025
    sp.Dimensions.tube_width = 0.008

    sp.Position.point1 = (0.3, 0.1)
    sp.Position.point2 = (0.7, 0.1)

    sp.Range.minimum_value = 0.0
    sp.Range.maximum_value = 1.0
    sp.Range.value = 0.0

    return sp

def make_2d_slider_widget(properties, interactor):
    """
    Make a 2D slider widget.

    :param properties: The 2D slider properties.
    :param interactor: The vtkInteractor.
    :return: The slider widget.
    """

    colors = vtkNamedColors()

    slider_rep = vtkSliderRepresentation2D(end_cap_length=properties.Dimensions.end_cap_length,
                                           end_cap_width=properties.Dimensions.end_cap_width,
                                           label_height=properties.Dimensions.label_height,
                                           slider_length=properties.Dimensions.slider_length,
                                           slider_width=properties.Dimensions.slider_width,
                                           title_height=properties.Dimensions.title_height,
                                           tube_width=properties.Dimensions.tube_width,
                                           minimum_value=properties.Range.minimum_value,
                                           maximum_value=properties.Range.maximum_value,
                                           value=properties.Range.value,
                                           title_text=properties.Text.title,
                                           )

    slider_rep.tube_property.color = colors.GetColor3d(properties.Colors.bar_color)
    slider_rep.cap_property.color = colors.GetColor3d(properties.Colors.bar_ends_color)
    slider_rep.label_property.color = colors.GetColor3d(properties.Colors.label_color)
    slider_rep.selected_property.color = colors.GetColor3d(properties.Colors.selected_color)
    slider_rep.slider_property.color = colors.GetColor3d(properties.Colors.slider_color)
    slider_rep.title_property.color = colors.GetColor3d(properties.Colors.title_color)

    slider_rep.point1_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point1_coordinate.value = properties.Position.point1
    slider_rep.point2_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point2_coordinate.value = properties.Position.point2

    label_font_family = properties.Text.label_font_family
    match label_font_family:
        case 'Courier':
            slider_rep.label_property.SetFontFamilyToCourier()
        case 'Times':
            slider_rep.label_property.SetFontFamilyToTimes()
        case _:
            slider_rep.label_property.SetFontFamilyToArial()
    slider_rep.label_property.bold = properties.Text.label_bold
    slider_rep.label_property.italic = properties.Text.label_italic
    slider_rep.label_property.shadow = properties.Text.label_shadow
    title_font_family = properties.Text.title_font_family
    match title_font_family:
        case 'Courier':
            slider_rep.title_property.SetFontFamilyToCourier()
        case 'Times':
            slider_rep.title_property.SetFontFamilyToTimes()
        case _:
            slider_rep.title_property.SetFontFamilyToArial()
    slider_rep.title_property.bold = properties.Text.title_bold
    slider_rep.title_property.italic = properties.Text.title_italic
    slider_rep.title_property.shadow = properties.Text.title_shadow

    widget = vtkSliderWidget(interactor=interactor)
    widget.SetRepresentation(slider_rep)
    widget.enabled = True
    widget.SetAnimationModeToAnimate()

    return widget

class SliderCallbackExposure:
    def __init__(self, tone_mapping_property):
        self.tone_mapping_property = tone_mapping_property

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.tone_mapping_property.exposure = value

class SliderCallbackMetallic:
    def __init__(self, actor_property):
        self.actor_property = actor_property

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.actor_property.metallic = value

class SliderCallbackRoughness:
    def __init__(self, actor_property):
        self.actor_property = actor_property

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.actor_property.roughness = value

class SliderCallbackOcclusionStrength:
    def __init__(self, actor_property):
        self.actor_property = actor_property

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.actor_property.occlusion_strength = value

class SliderCallbackNormalScale:
    def __init__(self, actor_property):
        self.actor_property = actor_property

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        self.actor_property.normal_scale = value

class PrintCallback:
    def __init__(self, caller, file_name, image_quality=1, rgba=True):
        """
        Set the parameters for writing the
         render window view to an image file.

        :param caller: The caller for the callback.
        :param file_name: The image file name.
        :param image_quality: The image quality.
        :param rgba: The buffer type, (if true, there is no background in the screenshot).
        """
        self.caller = caller
        self.image_quality = image_quality
        self.rgba = rgba
        if not file_name:
            self.path = None
            print("A file name is required.")
            return
        pth = Path(file_name).absolute()
        valid_suffixes = ['.jpeg', '.jpg', '.png']
        if pth.suffix:
            ext = pth.suffix.lower()
        else:
            ext = '.png'
        if ext not in valid_suffixes:
            ext = '.png'
        self.suffix = ext
        self.path = Path(str(pth)).with_suffix(ext)

    def __call__(self, caller, ev):
        if not self.path:
            print('A file name is required.')
            return
        # Save the screenshot.
        if caller.GetKeyCode() == 'k':
            w2if = vtkWindowToImageFilter(input=caller.GetRenderWindow(),
                                          scale=(self.image_quality, self.image_quality),
                                          read_front_buffer=True)
            if self.rgba:
                w2if.SetInputBufferTypeToRGBA()
            else:
                w2if.SetInputBufferTypeToRGB()
            if self.suffix in ['.jpeg', '.jpg']:
                writer = vtkJPEGWriter(file_name=self.path)
            else:
                writer = vtkPNGWriter(file_name=self.path)
            w2if >> writer
            writer.Write()
            print('Screenshot saved to:', self.path)

@dataclass(frozen=True)
class Coordinate:
    @dataclass(frozen=True)
    class CoordinateSystem:
        VTK_DISPLAY: int = 0
        VTK_NORMALIZED_DISPLAY: int = 1
        VTK_VIEWPORT: int = 2
        VTK_NORMALIZED_VIEWPORT: int = 3
        VTK_VIEW: int = 4
        VTK_POSE: int = 5
        VTK_WORLD: int = 6
        VTK_USERDEFINED: int = 7

@dataclass
class Slider2DProperties:
    @dataclass
    class Colors:
        # The color of the bar.
        bar_color: str = 'White'
        # The color of the ends of the bar.
        bar_ends_color: str = 'White'
        # The color of the text displaying the value.
        label_color: str = 'White'
        # The color of the knob when the mouse is held on it.
        selected_color: str = 'HotPink'
        # The color of the knob that slides.
        slider_color: str = 'White'
        # The color of the text indicating what the slider controls.
        title_color: str = 'White'

    @dataclass
    class Dimensions:
        end_cap_length: float = 0.005
        end_cap_width: float = 0.05
        label_height: float = 0.025
        slider_length: float = 0.01
        slider_width: float = 0.02
        title_height: float = 0.03
        tube_width: float = 0.008

    @dataclass
    class Position:
        coordinate_system: int = Coordinate.CoordinateSystem.VTK_NORMALIZED_VIEWPORT
        point1: Tuple = (0.1, 0.1)
        point2: Tuple = (0.9, 0.1)

    @dataclass
    class Range:
        minimum_value: float = 0.0
        maximum_value: float = 1.0
        value: float = 0.0

    @dataclass
    class Text:
        # Font families are: Ariel, Courier and Times
        label_font_family = 'Arial'
        label_bold: bool = True
        label_italic: bool = False
        label_shadow: bool = True
        title: str = ''
        title_font_family = 'Arial'
        title_bold: bool = True
        title_italic: bool = False
        title_shadow: bool = True

if __name__ == '__main__':
    main()
```
