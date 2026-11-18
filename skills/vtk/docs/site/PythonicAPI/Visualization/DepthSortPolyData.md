<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/DepthSortPolyData/ -->

# DepthSortPolyData

Repository source: [DepthSortPolyData](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/DepthSortPolyData.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestDepthSortPolyData.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestDepthSortPolyData.png?raw=true target=)

### Description

- Contributed by: Lars Friedrich

This is a C++-port of the VTK example '''DepthSort.py''' found in [VTKSourceDir/Examples/VisualizationAlgorithms/Python(<https://gitlab.kitware.com/vtk/vtk/blob/master/Examples/VisualizationAlgorithms/Python/DepthSort.py>). It was slightly modified. It generates 5 spheres with configurable PHI and THETA resolution. The spheres overlap. Therefore, correct blending and visualization in general requires depth sorting of the underlying polygons which will not happen when simply using a poly data mapper. Depth sorting can be achieved by connecting a *[vtkDepthSortPolyData](https://www.vtk.org/doc/nightly/html/classvtkDepthSortPolyData.html)* filter to the mapper instead of the pure poly data.

### Program Usage

```python
Usage: ./DepthSortPolyData DepthSortFlag ThetaResolution  PhiResolution ScalarVisibilityFlag*

DepthSortFlag ... activate/deactivate the depth sorting algorithm

ThetaResolution ... THETA resolution for the spheres

PhiResolution ... PHI resolution for the spheres

ScalarVisibilityFlag ... show/hide the found depth values as scalars
```

*Example calls:*

```python
./DepthSortPolyData 0 100 100 0
... will render the spheres 'as usual' (without depth sorting); in general you will be confronted with situations (specific view directions) where you cannot determine whether a small sphere is behind or in front of the big center sphere
```

```python
./DepthSortPolyData 1 100 100 0
... will render the spheres using depth sorting; the sphere depth order should now be visually traceable
```

```python
./DepthSortPolyData 1 100 100 1
... will render the spheres using depth sorting; the depth values are mapped to the spheres and renderd on the surfaces
```

Using higher PHI/THETA resolutions shows how depth sorting reduces the frame rate.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/DepthSortPolyData/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DepthSortPolyData.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkAppendPolyData
from vtkmodules.vtkFiltersHybrid import vtkDepthSortPolyData
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Correctly render translucent geometry.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-t', '--theta', default=100,
                        help='THETA resolution, default=100.')
    parser.add_argument('-p', '--phi', default=100,
                        help='PHI resolution, default=100.')
    parser.add_argument('-d', '--depth_sort_flag', action='store_true',
                        help='Activate/deactivate the depth sorting algorithm.')
    parser.add_argument('-s', '--scalar_visibility_flag', action='store_true',
                        help='Show/hide the found depth values as scalars.')
    args = parser.parse_args()

    return args.theta, args.phi, args.depth_sort_flag, args.scalar_visibility_flag

def main():
    theta, phi, do_depth_sort, scalar_visibility = get_program_parameters()

    colors = vtkNamedColors()

    # Generate a translucent sphere poly data set that partially overlaps:
    translucent_geometry = generate_overlapping_bunch_of_spheres(theta, phi)

    # Create the RenderWindow, Renderer and RenderWindowInteractor
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(size=(600, 400), window_name='DepthSortPolyData')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    depth_sort = vtkDepthSortPolyData()
    depth_sort.SetDirectionToBackToFront()
    depth_sort.vector = (1, 1, 1)
    depth_sort.camera = renderer.active_camera
    depth_sort.sort_scalars = True

    mapper = vtkPolyDataMapper(scalar_visibility=scalar_visibility)
    if scalar_visibility:
        mapper.scalar_range = (0, depth_sort.output.number_of_cells)

    if do_depth_sort:
        translucent_geometry >> depth_sort >> mapper
    else:
        translucent_geometry >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.opacity = 0.5  # translucent !!!
    actor.property.color = colors.GetColor3d('Crimson')
    # Put the objects in a position where it is easy to see different overlapping regions.
    actor.RotateX(-72)

    # Add the actors to the renderer.
    renderer.AddActor(actor)

    # Setup the view geometry.
    renderer.ResetCamera()
    renderer.active_camera.Zoom(2.2)  # so the object is larger
    render_window.Render()

    # Initialize the interaction.
    render_window_interactor.Initialize()

    # Start the interaction.
    render_window_interactor.Start()

def generate_overlapping_bunch_of_spheres(theta, phi):
    """
    Generate a bunch of overlapping spheres within one poly data set:
     one big sphere evenly surrounded by four small spheres that intersect the
     centered sphere.

    :param theta: theta sphere sampling resolution (THETA)
    :param phi: phi sphere sampling resolution (PHI)
    :return: Return the set of spheres within one logical poly data set.
    """

    append_data = vtkAppendPolyData()

    for i in range(0, 5):
        # All spheres except the center one should have radius = 0.5.
        sphere_source = vtkSphereSource(radius=0.5, theta_resolution=theta, phi_resolution=phi)
        match i:
            case 0:
                sphere_source.radius = 1
                sphere_source.center = (0, 0, 0)
            case 1:
                sphere_source.center = (1, 0, 0)
            case 2:
                sphere_source.center = (-1, 0, 0)
            case 3:
                sphere_source.center = (0, 1, 0)
            case 4:
                sphere_source.center = (0, -1, 0)

        # If your Python version is less than 3.10:
        # if i == 0:
        #     sphere_source.radius = 1
        #     sphere_source.center = (0, 0, 0)
        # elif i == 1:
        #     sphere_source.center = (1, 0, 0)
        # elif i == 2:
        #     sphere_source.center = (-1, 0, 0)
        # elif i == 3:
        #     sphere_source.center = (0, 1, 0)
        # elif i == 4:
        #     sphere_source.center = (0, -1, 0)
        # else:
        #     continue
        sphere_source.update()
        append_data.AddInputConnection(sphere_source.output_port)
    return append_data

def setup_environment_for_depth_peeling(render_window, renderer, max_no_of_peels, occlusion_ratio):
    """
    Setup the rendering environment for depth peeling (general depth peeling support is requested).
     See is_depth_peeling_supported()

    :param render_window: A valid openGL-supporting render window
    :param renderer: A valid renderer instance.
    :param max_no_of_peels: Maximum number of depth peels (multi-pass rendering).
    :param occlusion_ratio: The occlusion ratio (0.0 means a perfect image,
                            >0.0 means a non-perfect image which in general
                             results in faster rendering)
    :return: True if depth peeling could be set up.
    """
    if not render_window or not renderer:
        return False

    # 1. Use a render window with alpha bits (as initial value is 0 (False)):
    render_window.alpha_bit_planes = True

    # 2. Force to not pick a framebuffer with a multisample buffer (as initial value is 8):
    render_window.multi_samples = 0

    # 3. Choose to use depth peeling (if supported) (initial value is 0 (False)):
    renderer.use_depth_peeling = True

    # 4. Set depth peeling parameters
    # - Set the maximum number of rendering passes (initial value is 4):
    renderer.maximum_number_of_peels = max_no_of_peels
    # - Set the occlusion ratio (initial value is 0.0, exact image):
    renderer.occlusion_ratio = occlusion_ratio

    return True

def is_depth_peeling_supported(render_window, renderer, do_it_off_screen):
    """
    Find out whether this box supports depth peeling. Depth peeling requires a variety of openGL extensions and appropriate drivers.

    :param render_window: A valid openGL-supporting render window
    :param renderer: A valid renderer instance.
    :param do_it_off_screen: Do the test off-screen which means that nothing is
                           rendered to screen (this requires the box to support
                           off-screen rendering).
    :return: True if depth peeling is supported, False otherwise (which means
                that another strategy must be used for correct rendering of translucent
                geometry, e.g. CPU-based depth sorting)
    """
    success = True

    # Save original renderer / render window state
    orig_off_screen_rendering = render_window.off_screen_rendering == 1
    orig_alpha_bit_planes = render_window.alpha_bit_planes == 1
    orig_multi_samples = render_window.multi_samples
    orig_use_depth_peeling = renderer.use_depth_peeling == 1
    orig_max_peels = renderer.maximum_number_of_peels
    orig_occlusion_ratio = renderer.occlusion_ratio

    # Activate off screen rendering on demand
    render_window.OffScreenRendering = do_it_off_screen

    # Setup environment for depth peeling (with some default parametrization)
    success = success and setup_environment_for_depth_peeling(render_window, renderer, 100, 0.1)

    # Do a test render
    render_window.Render()

    # Check whether depth peeling was used
    success = success and renderer.last_rendering_used_depth_peeling == 1

    # recover original state
    render_window.off_screen_rendering = orig_off_screen_rendering
    render_window.alpha_bit_planes = orig_alpha_bit_planes
    render_window.multi_samples = orig_multi_samples
    renderer.use_depth_peeling = orig_use_depth_peeling
    renderer.maximum_number_of_peels = orig_max_peels
    renderer.occlusion_ratio = orig_occlusion_ratio

    return success

if __name__ == '__main__':
    main()
```
