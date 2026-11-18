<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/CorrectlyRenderTranslucentGeometry/ -->

# CorrectlyRenderTranslucentGeometry

Repository source: [CorrectlyRenderTranslucentGeometry](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/CorrectlyRenderTranslucentGeometry.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCorrectlyRenderTranslucentGeometry.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCorrectlyRenderTranslucentGeometry.png?raw=true target=)

### Description

- Contributed by: Lars Friedrich

Correctly rendering translucent geometry with OpenGL-functionality in the background (as in the case of VTK) requires non-intersecting polygons and depth-sorted traversal. In general these requirements are not satisfied as the inherent order of scene traversal is object-based. Using a method, namely depth peeling, presented by NVIDIA in 2001 [Interactive Order-Independent Transparency](http://www.nvidia.com/attach/6545), shadow mapping (multi-pass rendering) in conjunction with alpha test can be consulted to achieve correct blending of the rendered objects in the frame buffer.

VTK implements this feature since November 2006 as described in the [VTK WIKI](http://www.vtk.org/Wiki/VTK/Depth_Peeling) (Francois Bertel). Unfortunately depth peeling has several OpenGL extension, context and driver requirements (but also runs on Mesa) which restrict the approach's usage to modern GPUs. Usually this feature slows down the rendering process depending on the configuration (occlusion ratio and maximum number of iterative peels).

However if depth peeling is not available on a certain machine, depth sorting can be accomplished on the CPU using [DepthSortPolyData](DepthSortPolyData.md). This is usually much slower than the GPU-implementation and furthermore brings additional restrictions with it (e.g. poly data must be merged within one set).

This example program generates a set of intersecting (overlapping) spheres that have transparency properties. The program automatically checks whether depth peeling is supported or not. If depth peeling is not supported, CPU-based depth sorting is used. In addition the program tries to determine an average frame rate for the scene.

The following image shows the spheres arrangement (and view position) and compares the different render modes: no special translucency treatment, CPU depth sorting and GPU depth peeling.

### Program Usage

```python
./CorrectlyRenderTranslucentGeometry Theta Phi MaximumPeels OcclusionRatio ForceDepthSortingFlag DoNotUseAnyDepthRelatedAlgorithmFlag
```

Theta ... spheres' THETA resolution

Phi ... spheres' PHI resolution

MaximumPeels ... maximum number of depth peels (multi-pass rendering) for depth peeling mode

OcclusionRatio ... occlusion ratio for depth peeling mode (0.0 for a perfect rendered image, >0.0 for a non-perfect image which is expected to be slower)

ForceDepthSortingFlag ... force depth sorting even if depth peeling is supported

DoNotUseAnyDepthRelatedAlgorithmFlag ... neither use depth peeling nor depth sorting - just render as usual

***Example calls***:

```python
./CorrectlyRenderTranslucentGeometry 100 100 50 0.1 0 0 ... will render the spheres using depth peeling if available (depth sorting otherwise)

./CorrectlyRenderTranslucentGeometry 100 100 50 0.1 1 0 ... will render the spheres using depth sorting even if depth peeling is available

./CorrectlyRenderTranslucentGeometry 100 100 50 0.1 0 1 ... will render the spheres using neither depth peeling nor depth sorting
```

***Resultant frame rates show that depth peeling is usually much faster than the CPU-implementation, however, it will slow down the rendering process due to internal multi-pass rendering.***

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/CorrectlyRenderTranslucentGeometry/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CorrectlyRenderTranslucentGeometry.py**

```python
#!/usr/bin/env python3

"""
 Example application demonstrating correct rendering of translucent geometry.
 It will automatically detect whether depth peeling is supported by the
 hardware and software, and will apply depth peeling if possible. Otherwise
 a fallback strategy is used: depth sorting on the CPU.

 Usage:
 [ProgramName] Theta Phi MaximumPeels OcclusionRatio ForceDepthSortingFlag
 DoNotUseAnyDepthRelatedAlgorithmFlag

 Theta ... spheres' THETA resolution

 Phi ... spheres' PHI resolution

 MaximumPeels ... maximum number of depth peels (multi-pass rendering) for depth peeling mode

 OcclusionRatio ... occlusion ratio for depth peeling mode (0.0 for a perfect rendered image, >0.0 for a non-perfect image which is expected to  be slower)

 ForceDepthSortingFlag ... force depth sorting even if depth peeling is supported

 DoNotUseAnyDepthRelatedAlgorithmFlag ... neither use depth peeling nor depth sorting - just render as usual
"""

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonSystem import vtkTimerLog
from vtkmodules.vtkCommonTransforms import vtkTransform
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
    parser.add_argument('-m', '--maximum_peels', default=50,
                        help='The maximum number of depth peels (multi-pass rendering) for depth peeling mode, default=50.')
    parser.add_argument('-o', '--occlusion_ratio', default=0.1,
                        help='The occlusion ratio for depth peeling mode (0.0 for a perfect rendered image, >0.0 for a non-perfect image which is expected to be slower), default=0.1.')
    parser.add_argument('-f', '--force_depth_sorting_flag', action='store_true',
                        help='Force depth sorting even if depth peeling is supported.')
    parser.add_argument('-d', '--do_not_use_any_depth_related_algorithm_flag', action='store_true',
                        help='Neither use depth peeling nor depth sorting - just render as usual.')
    args = parser.parse_args()

    return args.theta, args.phi, args.maximum_peels, args.occlusion_ratio, args.force_depth_sorting_flag, args.do_not_use_any_depth_related_algorithm_flag

def main():
    theta, phi, max_peels, occulusion_ratio, force_depth_sort, without_any_depth_things = get_program_parameters()

    colors = vtkNamedColors()

    # Generate a translucent sphere poly data set that partially overlaps:
    translucent_geometry = generate_overlapping_bunch_of_spheres(theta, phi)

    # Generate a basic Mapper and Actor.
    mapper = vtkPolyDataMapper()
    translucent_geometry >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.opacity = 0.5  # translucent !!!
    actor.property.color = colors.GetColor3d('Crimson')
    # Put the objects in a position where it is easy to see different overlapping regions.
    actor.RotateX(-72)

    # Create the RenderWindow, Renderer and RenderWindowInteractor
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(size=(600, 400), window_name='CorrectlyRenderTranslucentGeometry')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the renderer.
    renderer.AddActor(actor)

    # Setup the view geometry.
    renderer.ResetCamera()
    renderer.active_camera.Zoom(2.2)  # so the object is larger
    render_window.Render()

    # Answer the key question: Does this box support GPU Depth Peeling?
    use_depth_peeling = is_depth_peeling_supported(render_window, renderer, True)
    if use_depth_peeling:
        print('DEPTH PEELING SUPPORT: YES')
    else:
        print('DEPTH PEELING SUPPORT: NO')

    success = True
    # Use depth peeling if available and not explicitly prohibited, otherwise we
    # use manual depth sorting
    print('CHOSEN MODE: ')
    if use_depth_peeling and not force_depth_sort and not without_any_depth_things:
        # GPU
        print('*** DEPTH PEELING ***')
        # Setup GPU depth peeling with configured parameters
        success = not setup_environment_for_depth_peeling(render_window, renderer, max_peels, occulusion_ratio)
    elif not without_any_depth_things:
        # CPU
        print('*** DEPTH SORTING ***')
        # Setup CPU depth sorting filter
        depth_sort = vtkDepthSortPolyData()
        depth_sort.SetDirectionToBackToFront()
        depth_sort.vector = (1, 1, 1)
        depth_sort.camera = renderer.active_camera
        depth_sort.sort_scalars = False  # do not really need this here
        # Bring it to the mapper's input
        translucent_geometry >> depth_sort >> mapper
        depth_sort.update()
    else:
        print('*** NEITHER DEPTH PEELING NOR DEPTH SORTING ***')

    # Initialize the interaction.
    render_window_interactor.Initialize()

    # Check the average frame rate when rotating the actor
    end_count = 100
    clock = vtkTimerLog()
    # Set a user transform for successively rotating the camera position.
    transform = vtkTransform()
    transform.Identity()
    # Rotate 2 degrees around Y-axis at each iteration.
    transform.RotateY(2.0)
    camera = renderer.active_camera
    # The camera position.
    cam_pos_out = [0.0, 0.0, 0.0]
    # Start the test.
    clock.StartTimer()
    for i in range(0, end_count):
        cam_pos_in = camera.position
        transform.TransformPoint(cam_pos_in, cam_pos_out)
        camera.SetPosition(cam_pos_out)
        render_window.Render()
    clock.StopTimer()
    frame_rate = float(end_count) / clock.GetElapsedTime()
    print(f'AVERAGE FRAME RATE: {frame_rate:g}fps.')

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
