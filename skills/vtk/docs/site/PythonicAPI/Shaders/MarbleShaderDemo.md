<!-- source: https://examples.vtk.org/site/PythonicAPI/Shaders/MarbleShaderDemo/ -->

# MarbleShaderDemo

Repository source: [MarbleShaderDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Shaders/MarbleShaderDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Shaders/TestMarbleShaderDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Shaders/TestMarbleShaderDemo.png?raw=true target=)

### Description

Makes solid marble texture with strong veins. The "veincolor" parameter controls the color of the veins. The background color is given by the surface's DiffuseColor.

Explore the parameter space with the [vtkSliderWidget](https://www.vtk.org/doc/nightly/html/classvtkSliderWidget.html).

The file for the shader code is `src/Testing/Data/Shaders/PerlinNoise.glsl`.

#### Parameters

- *veinfreq* - controls the lowest frequency of the color veins e.g. 10
- *veinlevels* - how many "levels" of vein tendrils it has e.g. 2
- *warpfreq* - lowest frequency of the turbulent warping in the marble e.g. 10
- *warping* - controls how much turbulent warping there will be e.g. 0.5
- *veincolor* - the color of the veins e.g. white: 1 1 1
- *sharpness* - controls how sharp or fuzzy the veins are (higher = sharper) e.g. 8

Cite

Perlin's original Siggraph Paper: [Perlin, K. 1985. "An Image Synthesizer." Computer Graphics 19(3)](https://dl.acm.org/doi/10.1145/325165.325247).

Cite

This shader is inspired by Larry Gritz's veined marble shader.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Shaders/MarbleShaderDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MarbleShaderDemo.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path
from time import sleep
from typing import Tuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.misc import calldata_type
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_OBJECT,
    vtkCommand,
)
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import (
    vtkTriangleFilter,
    vtkTriangleMeshPointNormals
)
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkSliderRepresentation2D,
    vtkSliderWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLPolyDataMapper

# Delay time in milliseconds.
# DELAY=200
DELAY = 20
# Convert to seconds.
DELAY = DELAY / 1000.0

def get_program_parameters():
    import argparse
    description = 'MarbleShaderDemo.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('shader', help='The shader e.g. PerlnNoise.glsl.')
    parser.add_argument('-f', '--pd_file', default=None, help='Enter a polydata file e.g teapot.g.')
    parser.add_argument('--veinfreq', default=7.5, help='Controls the lowest frequency of the color veins e.g. 10')
    parser.add_argument('--veinlevels', default=3, help='Controls how many "levels" of vein tendrils it has e.g. 3')
    parser.add_argument('--warpfreq', default=1.5,
                        help='Controls the lowest frequency of the turbulent warping in the marble e.g. 1.5')
    parser.add_argument('--warping', default=0.5, help='Controls how much turbulent warping there will be e.g. 0.5')
    parser.add_argument('--vein_color', default="Green", help='The color of the veins e.g. green')
    parser.add_argument('--sharpness', default=8,
                        help='Controls how sharp or fuzzy the veins are (higher = sharper) e.g. 8')
    args = parser.parse_args()
    return args.shader, args.pd_file, args.veinfreq, args.veinlevels, args.warpfreq, args.warping, args.vein_color, args.sharpness

def main():
    shader, pd_file, veinfreq, veinlevels, warpfreq, warping, vein_color, sharpness = get_program_parameters()

    shader_file = Path(shader)
    if not shader_file.is_file():
        print(f'{shader_file} not found.')
        return

    name = None
    poly_data = None
    if pd_file:
        fn = Path(pd_file)
        if fn.is_file():
            poly_data = read_poly_data(pd_file)
            if not poly_data:
                return
            name = fn.name
        else:
            print(f'{fn} not found.')
            return
    if pd_file is None or poly_data is None:
        source = vtkSphereSource(phi_resolution=25, theta_resolution=25)
        poly_data = source.update().output
        name = 'Generated Sphere'
    colors = vtkNamedColors()
    colors.SetColor('Bkg', 26, 51, 102, 255)

    ShaderProperties.veinfreq = veinfreq
    ShaderProperties.veinlevels = veinlevels
    ShaderProperties.warpfreq = warpfreq
    ShaderProperties.warping = warping
    ShaderProperties.veincolor = tuple(colors.GetColor3d(vein_color))
    ShaderProperties.sharpness = sharpness

    shader_code = shader_file.read_text()

    # Create a transform to rescale the model.
    center = poly_data.center
    bounds = poly_data.bounds
    max_bound = max(get_ranges(bounds))

    # Build the pipeline.
    # ren1 is for the slider rendering,
    # ren2 is for the object rendering.
    ren1 = vtkRenderer(viewport=(0.0, 0.0, 0.2, 1.0), background=colors.GetColor3d('Snow'))
    ren2 = vtkRenderer(viewport=(0.2, 0.0, 1, 1), background=colors.GetColor3d('SlateGray'))

    render_window = vtkRenderWindow(size=(800, 480), window_name='MarbleShaderDemo')
    # The order here is important.
    # This ensures that the sliders will be in ren1.
    render_window.AddRenderer(ren2)
    render_window.AddRenderer(ren1)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window
    style = vtkInteractorStyleTrackballCamera()
    interactor.interactor_style = style

    # Rescale the polydata to [-1,1].
    user_transform = vtkTransform()
    user_transform.Translate(-center[0], -center[1], -center[2])
    user_transform.Scale(1.0 / max_bound, 1.0 / max_bound, 1.0 / max_bound)
    transform = vtkTransformFilter(transform=user_transform, input_data=poly_data)

    triangles = vtkTriangleFilter()

    norms = vtkTriangleMeshPointNormals()

    mapper = vtkOpenGLPolyDataMapper(scalar_visibility=False)
    transform >> triangles >> norms >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.diffuse = 1.0
    actor.property.diffuse_color = colors.GetColor3d('Wheat')
    actor.property.specular = .5
    actor.property.specular_power = 50

    ren2.AddActor(actor)

    # Modify the vertex shader to pass the position of the vertex.
    sp = actor.GetShaderProperty()
    cmd = get_vertex_shader_replacement1()
    sp.AddVertexShaderReplacement(*cmd)

    cmd = get_vertex_shader_replacement2()
    sp.AddVertexShaderReplacement(*cmd)

    # Add the code to generate noise.
    # These functions need to be defined outside of main.
    # Use the System.Dec to declare and implement.
    cmd = get_fragment_shader_replacement1(shader_code)
    sp.AddFragmentShaderReplacement(*cmd)

    # Define varying and uniforms for the fragment shader here.
    cmd = get_fragment_shader_replacement2()
    sp.AddFragmentShaderReplacement(*cmd)

    cmd = get_fragment_shader_replacement3()
    sp.AddFragmentShaderReplacement(*cmd)

    print(f'------------\nInput: {name}')
    disp_parameters()
    shader_callback = ShaderCallback()
    mapper.AddObserver(vtkCommand.UpdateShaderEvent, shader_callback.vtk_shader_callback)

    # Set up a slider widget and callback for each varying parameter.

    step_size = 1.0 / 5.0
    pos_y = 0.1
    pos_x0 = 0.1
    pos_x1 = 0.9

    sp = make_slider_properties()

    # Slider values
    sp.Range.minimum_value = 1.0
    sp.Range.value = ShaderProperties.veinfreq
    sp.Range.maximum_value = 15.0
    sp.Text.title = 'Vein Frequency'
    #  Screen coordinates.
    sp.Position.point1 = (pos_x0, pos_y)
    sp.Position.point2 = (pos_x1, pos_y)

    widget_vein_freq = make_2d_slider_widget(sp, ren1, interactor)
    cb_vein_freq = SliderCallbackVeinFreq()
    widget_vein_freq.AddObserver(vtkCommand.InteractionEvent, cb_vein_freq)

    pos_y += step_size

    # Slider values
    sp.Range.minimum_value = 1
    sp.Range.value = ShaderProperties.veinlevels
    sp.Range.maximum_value = 5
    sp.Text.title = 'Vein Levels'
    #  Screen coordinates.
    sp.Position.point1 = (pos_x0, pos_y)
    sp.Position.point2 = (pos_x1, pos_y)

    widget_vein_levels = make_2d_slider_widget(sp, ren1, interactor)
    cb_vein_levels = SliderCallbackVeinLevels()
    widget_vein_levels.AddObserver(vtkCommand.EndInteractionEvent, cb_vein_levels)

    pos_y += step_size

    # Slider values
    sp.Range.minimum_value = 1
    sp.Range.value = ShaderProperties.warpfreq
    sp.Range.maximum_value = 2
    sp.Text.title = 'Warp Frequency'
    #  Screen coordinates.
    sp.Position.point1 = (pos_x0, pos_y)
    sp.Position.point2 = (pos_x1, pos_y)

    widget_warp_freq = make_2d_slider_widget(sp, ren1, interactor)
    cb_warp_freq = SliderCallbackWarpFreq()
    widget_warp_freq.AddObserver(vtkCommand.InteractionEvent, cb_warp_freq)

    pos_y += step_size

    # Slider values
    sp.Range.minimum_value = 0.0
    sp.Range.value = ShaderProperties.warping
    sp.Range.maximum_value = 1.0
    sp.Text.title = 'Warping'
    #  Screen coordinates.
    sp.Position.point1 = (pos_x0, pos_y)
    sp.Position.point2 = (pos_x1, pos_y)

    widget_warping = make_2d_slider_widget(sp, ren1, interactor)
    cb_warping = SliderCallbackWarping()
    widget_warping.AddObserver(vtkCommand.InteractionEvent, cb_warping)

    pos_y += step_size

    # Slider values
    sp.Range.minimum_value = 0.01
    sp.Range.value = ShaderProperties.sharpness
    sp.Range.maximum_value = 10.0
    sp.Text.title = 'Sharpness'
    #  Screen coordinates.
    sp.Position.point1 = (pos_x0, pos_y)
    sp.Position.point2 = (pos_x1, pos_y)

    widget_sharpness = make_2d_slider_widget(sp, ren1, interactor)
    cb_sharpness = SliderCallbackSharpness()
    widget_sharpness.AddObserver(vtkCommand.InteractionEvent, cb_sharpness)

    render_window.Render()
    cow = vtkCameraOrientationWidget()
    cow.SetParentRenderer(ren2)
    # Enable the widget.
    cow.On()

    ren2.ResetCamera()
    ren2.active_camera.Zoom(1.0)
    render_window.Render()
    interactor.Start()

    bounds = transform.output.bounds
    ranges = get_ranges(bounds)
    print(f'------------\nRange:'
          f' x: {ranges[0]:8.6f}'
          f' y: {ranges[1]:8.6f}'
          f' z: {ranges[2]:8.6f}'
          f'\n------------')

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

def get_ranges(bounds):
    ranges = list()
    for i in range(0, 6, 2):
        ranges.append(bounds[i + 1] - bounds[i])
    return ranges

def get_vertex_shader_replacement1():
    res = (
        '//VTK::Normal::Dec',  # replace the normal block
        True,  # before the standard replacements
        '//VTK::Normal::Dec\n' +
        '   out vec4 myVertexMC;\n',  # we still want the default
        False  # only do it once
    )
    return res

def get_vertex_shader_replacement2():
    res = (
        '//VTK::Normal::Impl',  # replace the normal block
        True,  # before the standard replacements
        '//VTK::Normal::Impl\n' +
        '  myVertexMC = vertexMC;\n',  # we still want the default
        False  # only do it once
    )
    return res

def get_fragment_shader_replacement1(shader_code):
    res = (
        '//VTK::System::Dec',
        False,  # before the standard replacements
        shader_code,
        False  # only do it once
    )
    return res

def get_fragment_shader_replacement2():
    res = (
        '//VTK::Normal::Dec',  # replace the normal block
        True,  # before the standard replacements
        '//VTK::Normal::Dec\n'  # we still want the default
        '  varying vec4 myVertexMC;\n'
        '  uniform vec3 veincolor = vec3(1.0, 1.0, 1.0);\n'
        '  uniform float veinfreq = 10.0;\n'
        '  uniform int veinlevels = 2;\n'
        '  uniform float warpfreq = 1;\n'
        '  uniform float warping = 0.5;\n'
        '  uniform float sharpness = 8.0;\n',
        False  # only do it once
    )
    return res

def get_fragment_shader_replacement3():
    res = (
        '//VTK::Light::Impl',  # replace the light block
        False,  # before the standard replacements
        '//VTK::Light::Impl\n'  # we still want the default calc
        '\n'
        '#define pnoise(x) ((noise(x) + 1.0) / 2.0)\n'
        '#define snoise(x) (2.0 * pnoise(x) - 1.0)\n'
        '  vec3 Ct;\n'
        '  int i;\n'
        '  float turb, freq;\n'
        '  float turbsum;\n'
        '  /* perturb the lookup */\n'
        '  freq = 1.0;\n '
        ' vec4 offset = vec4(0.0,0.0,0.0,0.0);\n'
        '  vec4 noisyPoint;\n'
        '  vec4 myLocalVertexMC = myVertexMC;\n'
        '\n'
        '    for (i = 0;  i < 6;  i += 1) {\n'
        'noisyPoint[0] = snoise(warpfreq * freq * myLocalVertexMC);\n'
        'noisyPoint[1] = snoise(warpfreq * freq * myLocalVertexMC);\n'
        'noisyPoint[2] = snoise(warpfreq * freq * myLocalVertexMC);\n'
        'noisyPoint[3] = 1.0;\n'
        'offset += 2.0 * warping * (noisyPoint - 0.5)  / freq;\n'
        'freq *= 2.0;\n'
        '    }\n'
        '    myLocalVertexMC.x += offset.x;\n'
        '    myLocalVertexMC.y += offset.y;\n'
        '    myLocalVertexMC.z += offset.z;\n'
        '\n'
        '    /* Now calculate the veining function for the lookup area */\n'
        '    turbsum = 0.0;  freq = 1.0;\n'
        '    myLocalVertexMC *= veinfreq;\n '
        '   for (i = 0;  i < veinlevels;  i += 1) {\n'
        '     turb = abs (snoise (myLocalVertexMC));\n'
        '     turb = pow (smoothstep (0.8, 1.0, 1.0 - turb), sharpness) / freq;\n'
        '     turbsum += (1.0-turbsum) * turb;\n'
        '     freq *= 1.5;\n'
        '     myLocalVertexMC *= 1.5;\n'
        '   }\n'
        '\n'
        '    Ct = mix (diffuseColor, veincolor, turbsum);\n'
        '\n'
        '  fragOutput0.rgb = opacity * (ambientColor + Ct + specular);\n'
        '  fragOutput0.a = opacity;\n',
        False  # only do it once
    )
    return res

class ShaderCallback:

    def __init__(self):
        self.veincolor = None
        self.veinfreq = None
        self.veinlevels = None
        self.warpfreq = None
        self.warping = None
        self.sharpness = None
        self.update()

    @calldata_type(VTK_OBJECT)
    def vtk_shader_callback(self, caller, event, calldata):
        program = calldata
        if program is not None:
            # diffuseColor = [0.4, 0.7, 0.6]
            # program.SetUniform3f("diffuseColorUniform", diffuseColor)
            program.SetUniform3f("veincolor", ShaderProperties.veincolor)
            program.SetUniformf("veinfreq", ShaderProperties.veinfreq)
            program.SetUniformi("veinlevels", ShaderProperties.veinlevels)
            program.SetUniformf("warpfreq", ShaderProperties.warpfreq)
            program.SetUniformf("warping", ShaderProperties.warping)
            program.SetUniformf("sharpness", ShaderProperties.sharpness)

            if self.has_changed():
                disp_parameters()
                self.update()

    def update(self):
        self.veincolor = ShaderProperties.veincolor
        self.veinfreq = ShaderProperties.veinfreq
        self.veinlevels = ShaderProperties.veinlevels
        self.warpfreq = ShaderProperties.warpfreq
        self.warping = ShaderProperties.warping
        self.sharpness = ShaderProperties.sharpness

    def has_changed(self):
        if self.veincolor != ShaderProperties.veincolor:
            return True
        if self.veinfreq != ShaderProperties.veinfreq:
            return True
        if self.veinlevels != ShaderProperties.veinlevels:
            return True
        if self.warpfreq != ShaderProperties.warpfreq:
            return True
        if self.warping != ShaderProperties.warping:
            return True
        if self.sharpness != ShaderProperties.sharpness:
            return True

        return False

def disp_parameters():
    print(
        f'------------\n'
        f'veincolor:  ({fmt_floats(ShaderProperties.veincolor, 8, 6, "f")})\n'
        f'veinfreq:   {ShaderProperties.veinfreq:5.2f}\n'
        f'veinlevels: {ShaderProperties.veinlevels:2d}\n'
        f'warpfreq:   {ShaderProperties.warpfreq:5.2f}\n'
        f'warping:    {ShaderProperties.warping:5.2f}\n'
        f'sharpness:  {ShaderProperties.sharpness:5.2f}\n'
        f'------------'
    )

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])

def make_slider_properties():
    sp = Slider2DProperties()
    sp.Range.minimum_value = 0
    sp.Range.maximum_value = 1
    sp.Position.point1 = (0.3, 0.1)
    sp.Position.point2 = (0.7, 0.1)
    sp.Dimensions.slider_length = 0.075
    sp.Dimensions.slider_width = 0.025
    sp.Dimensions.end_cap_length = 0.025
    sp.Dimensions.end_cap_width = 0.025
    sp.Dimensions.title_height = 0.025
    sp.Dimensions.label_height = 0.025
    # Set color properties:
    # Change the color of the knob that slides.
    sp.Colors.slider_color = 'Green'
    # Change the color of the text indicating what the slider controls.
    sp.Colors.title_color = 'Black'
    # Change the color of the text displaying the value.
    sp.Colors.label_color = 'DarkSlateGray'
    # Change the color of the knob when the mouse is held on it.
    sp.Colors.selected_color = 'Lime'
    # Change the color of the bar.
    sp.Colors.bar_color = 'Black'
    # Change the color of the ends of the bar.
    sp.Colors.bar_ends_color = 'Indigo'
    # Change the color of the ends of the bar.
    sp.Colors.slider_color = 'BurlyWood'

    return sp

def make_2d_slider_widget(properties, current_renderer, interactor):
    """
    Make a 2D slider widget.

    :param properties: The 2D slider properties.
    :param current_renderer: The current vtkRenderer (where the slider is rendered).
    :param interactor: The vtkInteractor.
    :return: The slider widget.
    """
    colors = vtkNamedColors()

    slider_rep = vtkSliderRepresentation2D(minimum_value=properties.Range.minimum_value,
                                           maximum_value=properties.Range.maximum_value,
                                           value=properties.Range.value,
                                           title_text=properties.Text.title,
                                           tube_width=properties.Dimensions.tube_width,
                                           slider_length=properties.Dimensions.slider_length,
                                           slider_width=properties.Dimensions.slider_width,
                                           end_cap_length=properties.Dimensions.end_cap_length,
                                           end_cap_width=properties.Dimensions.end_cap_width,
                                           title_height=properties.Dimensions.title_height,
                                           label_height=properties.Dimensions.label_height,
                                           )

    # Set the color properties.
    slider_rep.title_property.color = colors.GetColor3d(properties.Colors.title_color)
    slider_rep.label_property.color = colors.GetColor3d(properties.Colors.label_color)
    slider_rep.tube_property.color = colors.GetColor3d(properties.Colors.bar_color)
    slider_rep.cap_property.color = colors.GetColor3d(properties.Colors.bar_ends_color)
    slider_rep.slider_property.color = colors.GetColor3d(properties.Colors.slider_color)
    slider_rep.selected_property.color = colors.GetColor3d(properties.Colors.selected_color)

    # Set the position.
    slider_rep.point1_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point1_coordinate.value = properties.Position.point1
    slider_rep.point2_coordinate.coordinate_system = properties.Position.coordinate_system
    slider_rep.point2_coordinate.value = properties.Position.point2

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

    widget = vtkSliderWidget(representation=slider_rep, current_renderer=current_renderer, interactor=interactor,
                             enabled=True)
    widget.number_of_animation_steps = 10
    widget.SetAnimationModeToAnimate()

    return widget

class SliderCallbackVeinFreq:

    def __init__(self):
        """
        """
        pass

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        ShaderProperties.veinfreq = value
        sleep(DELAY)

class SliderCallbackVeinLevels:

    def __init__(self):
        """
        """
        pass

    def __call__(self, caller, ev):
        slider_widget = caller
        value = round(slider_widget.representation.value)
        slider_widget.representation.value = value
        ShaderProperties.veinlevels = value
        sleep(DELAY)

class SliderCallbackWarpFreq:

    def __init__(self):
        """
        """
        pass

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        ShaderProperties.warpfreq = value
        sleep(DELAY)

class SliderCallbackWarping:

    def __init__(self):
        """
        """
        pass

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        ShaderProperties.warping = value
        sleep(DELAY)

class SliderCallbackSharpness:

    def __init__(self):
        """
        """
        pass

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        ShaderProperties.sharpness = value
        sleep(DELAY)

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
        title_color: str = 'White'
        label_color: str = 'White'
        slider_color: str = 'White'
        selected_color: str = 'HotPink'
        bar_color: str = 'White'
        bar_ends_color: str = 'White'

    @dataclass
    class Dimensions:
        tube_width: float = 0.008
        slider_length: float = 0.01
        slider_width: float = 0.02
        end_cap_length: float = 0.005
        end_cap_width: float = 0.05
        title_height: float = 0.03
        label_height: float = 0.025

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
        title: str = ''
        title_font_family = 'Arial'
        title_bold: bool = True
        title_italic: bool = False
        title_shadow: bool = True
        label_font_family = 'Arial'
        label_bold: bool = True
        label_italic: bool = False
        label_shadow: bool = True

@dataclass
class ShaderProperties:
    veincolor: Tuple = (0.0, 0.501961, 0.0)
    veinfreq: float = 7.5
    veinlevels: float = 3
    warpfreq: float = 1.5
    warping: float = 0.5
    sharpness: float = 8.0

if __name__ == '__main__':
    main()
```
