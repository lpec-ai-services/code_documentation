<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/FireFlowDemo/ -->

# FireFlowDemo

Repository source: [FireFlowDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/FireFlowDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestFireFlowDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestFireFlowDemo.png?raw=true target=)

### Description

This example adds interaction to [FireFlow](FireFlow.md).

The example uses [vtkSliderWidget](https://www.vtk.org/doc/nightly/html/classvtkSliderWidget.html)'s to manipulate the center of the [vtkPointSource](https://www.vtk.org/doc/nightly/html/classvtkPointSource.html) that provides seed for the streamlines. As the X, Y, or Z center corrdiantes change, the streamlines are changed. The range of the x, y, and z coordinates are limited to the bounds of the solution dataset. There is a built in delay of 500 milliseconds to make the animation between selections consistent.

Here's the embedded video

showing the interactive movement of the seeding sphere.

Cite

The solution and geometry data is from the [Mayavi](https://docs.enthought.com/mayavi/mayavi/)  project. Mayavi is a python application that provides an easy to use interface to many vtk filters. Both a command-line and GUI interface are provided. If you use the Mayavi data or the Mayavi application, please use the following citation in any published work: **Ramachandran, P. and Varoquaux, G., `Mayavi: 3D Visualization of Scientific Data` IEEE Computing in Science & Engineering, 13 (2), pp. 40-51 (2011).**

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/FireFlowDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FireFlowDemo.py**

```python
#!/usr/bin/env python3

import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkCommand
from vtkmodules.vtkFiltersCore import (
    vtkContourFilter,
    vtkTubeFilter
)
from vtkmodules.vtkFiltersFlowPaths import vtkStreamTracer
from vtkmodules.vtkFiltersSources import (
    vtkPointSource,
    vtkSphereSource)
from vtkmodules.vtkIOImport import vtkVRMLImporter
from vtkmodules.vtkIOXML import vtkXMLUnstructuredGridReader
from vtkmodules.vtkInteractionWidgets import (
    vtkSliderRepresentation2D,
    vtkSliderWidget)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Fire Flow Demonstration.'
    epilogue = '''
    The example illustrates how to combine a geometric description of a scene with a fluid flow solution.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('geometry',
                        help='The path to the geometry wrl file, e.g. room_vis.wrl.')
    parser.add_argument('velocity',
                        help='The path to the velocity vtu file, e.g. fire_ug.vtu.')
    parser.add_argument('-d', '--delay', type=int, default=100,
                        help='The delay in milliseconds, default=100ms.')
    args = parser.parse_args()
    return args.geometry, args.velocity, args.delay

def main():
    geometry_fn, velocity_fn, delay = get_program_parameters()
    geometry_path = Path(geometry_fn)
    velocity_path = Path(velocity_fn)
    file_check = True
    if not geometry_path.is_file():
        print(f'Missing geometry file: {geometry_path}.')
        file_check = False
    else:
        if geometry_path.suffix.lower() != '.wrl':
            print(f'The geometry file : {geometry_path} must have a .wrl suffix.')
            file_check = False

    if not Path(velocity_path).is_file():
        print(f'Missing velocity file: {velocity_path}.')
        file_check = False
    else:
        if velocity_path.suffix.lower() != '.vtu':
            print(f'The velocity file : {velocity_path} must have a .vtu suffix.')
            file_check = False
    if not file_check:
        return

    colors = vtkNamedColors()
    iso_surface_color = colors.GetColor3d('WhiteSmoke')
    sphere_color = colors.GetColor3d('HotPink')
    background_color = colors.GetColor3d('SlateGray')

    renderer = vtkRenderer(use_hidden_line_removal=True, background=background_color)

    render_window = vtkRenderWindow(size=(640, 512), window_name=f'{Path(sys.argv[0]).stem:s}')
    render_window.AddRenderer(renderer)
    render_window.Initialize()

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    render_window_interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    # Import the VRML Files that define the geometry.
    vrml_import = vtkVRMLImporter(file_name=geometry_path, render_window=render_window)
    vrml_import.Update()

    # Read the UnstructuredGrid define the solution.
    solution = vtkXMLUnstructuredGridReader(file_name=velocity_path)
    solution.update()

    bounds = solution.output.bounds
    center = list()
    # for i in range(0, 6, 2):
    #      center.append((bounds[i + 1] - bounds[i]) / 2.0)
    center = (3.0, 1.6, 1.25)
    scalar_range = solution.output.scalar_range

    # Create Seeds.
    seeds = vtkPointSource(radius=0.2, center=center, number_of_points=50)

    # Create streamlines.
    stream_tracer = vtkStreamTracer(source_connection=seeds.output_port,
                                    maximum_propagation=50, initial_integration_step=0.2, minimum_integration_step=0.01,
                                    integrator_type=2, compute_vorticity=True)
    stream_tracer.SetIntegrationDirectionToBoth()

    tubes = vtkTubeFilter(number_of_sides=8, radius=0.02, vary_radius=False)

    map_tubes = vtkPolyDataMapper(scalar_range=scalar_range)
    solution >> stream_tracer >> tubes >> map_tubes

    tubes_actor = vtkActor(mapper=map_tubes)

    # Create an Isosurface.
    iso_surface = vtkContourFilter()
    iso_surface.SetValue(0, 500.0)

    iso_surface_mapper = vtkPolyDataMapper(scalar_visibility=False)
    solution >> iso_surface >> iso_surface_mapper

    iso_surface_actor = vtkActor(mapper=iso_surface_mapper)
    iso_surface_actor.property.opacity = 0.5
    iso_surface_actor.property.diffuse_color = iso_surface_color

    sphere = vtkSphereSource(center=seeds.center, radius=seeds.radius,
                             theta_resolution=20, phi_resolution=11)
    sphere_mapper = vtkPolyDataMapper()
    sphere >> sphere_mapper

    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.opacity = 1.0
    sphere_actor.property.specular = 0.4
    sphere_actor.property.specular_power = 80
    sphere_actor.property.diffuse_color = sphere_color

    sp = make_slider_2d_properties()
    sp.Position.point1 = (0.1, 0.08)
    sp.Position.point2 = (0.3, 0.08)
    sp.Range.minimum_value = bounds[0]
    sp.Range.maximum_value = bounds[1]
    sp.Range.value = seeds.center[0]
    sp.Text.title = 'X'
    widget_x = make_2d_slider_widget(sp, render_window_interactor)
    cb_x = SliderCallback(0, seeds, sphere, delay)
    widget_x.AddObserver(vtkCommand.InteractionEvent, cb_x)

    sp.Position.point1 = (0.4, 0.08)
    sp.Position.point2 = (0.6, 0.08)
    sp.Range.minimum_value = bounds[2]
    sp.Range.maximum_value = bounds[3]
    sp.Range.value = seeds.center[1]
    sp.Text.title = 'Y'
    widget_y = make_2d_slider_widget(sp, render_window_interactor)
    cb_y = SliderCallback(1, seeds, sphere, delay)
    widget_y.AddObserver(vtkCommand.InteractionEvent, cb_y)

    sp.Range.minimum_value = bounds[4]
    sp.Range.maximum_value = bounds[5]
    sp.Range.value = seeds.center[2]
    sp.Position.point1 = (0.7, 0.08)
    sp.Position.point2 = (0.9, 0.08)
    sp.Text.title = 'Z'
    widget_z = make_2d_slider_widget(sp, render_window_interactor)
    cb_z = SliderCallback(2, seeds, sphere, delay)
    widget_z.AddObserver(vtkCommand.InteractionEvent, cb_z)

    renderer.AddActor(tubes_actor)
    renderer.AddActor(sphere_actor)
    renderer.AddActor(iso_surface_actor)

    render_window.Render()

    renderer.active_camera.Azimuth(20.0)
    renderer.active_camera.Elevation(10.0)
    renderer.active_camera.Dolly(1.25)
    renderer.ResetCameraClippingRange()

    render_window.Render()

    render_window_interactor.Initialize()
    render_window_interactor.Start()

def make_slider_2d_properties():
    """
    This applies more specific values to the default Slider2DProperties.

    :return: The slider 2D properties.
    """
    sp = Slider2DProperties()

    sp.Colors.bar_color = 'Black'
    sp.Colors.bar_ends_color = 'Indigo'
    sp.Colors.label_color = 'AliceBlue'
    sp.Colors.selected_color = 'Lime'
    sp.Colors.slider_color = 'BurlyWood'
    sp.Colors.title_color = 'AliceBlue'

    sp.Dimensions.end_cap_length = 0.015
    sp.Dimensions.end_cap_width = 0.05
    sp.Dimensions.label_height = 0.025
    sp.Dimensions.slider_length = 0.02
    sp.Dimensions.slider_width = 0.05
    sp.Dimensions.title_height = 0.03

    sp.Position.point1 = (0.3, 0.1)
    sp.Position.point2 = (0.7, 0.1)

    sp.Range.minimum_value = 3
    sp.Range.maximum_value = 20

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

    # Set the color properties.
    slider_rep.tube_property.color = colors.GetColor3d(properties.Colors.bar_color)
    slider_rep.cap_property.color = colors.GetColor3d(properties.Colors.bar_ends_color)
    slider_rep.label_property.color = colors.GetColor3d(properties.Colors.label_color)
    slider_rep.selected_property.color = colors.GetColor3d(properties.Colors.selected_color)
    slider_rep.slider_property.color = colors.GetColor3d(properties.Colors.slider_color)
    slider_rep.title_property.color = colors.GetColor3d(properties.Colors.title_color)

    # Set the position.
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

class SliderCallback:
    def __init__(self, axis, seeds, sphere, delay=500):
        """
        The delay is used to make the animation between selections consistent.

        :paran: axis: The axis [0..3) corresponding to X, Y, Z.
        :param seeds: The vtkPointSource seeds.
        :param sphere: The vtkSphereSource.
        :param delay: Delay in milliseconds.
        """
        self.axis = axis
        self.seeds = seeds
        self.sphere = sphere
        self.delay = delay

    def __call__(self, caller, ev):
        slider_widget = caller
        value = slider_widget.representation.value
        center = list(self.seeds.center)
        center[self.axis] = value
        self.seeds.center = center
        self.sphere.center = center
        # Sleep for delay miliseconds.
        time.sleep(self.delay / 1000)

if __name__ == '__main__':
    main()
```
