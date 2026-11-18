<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/OrientedBoundingCylinder/ -->

# OrientedBoundingCylinder

Repository source: [OrientedBoundingCylinder](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/OrientedBoundingCylinder.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestOrientedBoundingCylinder.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestOrientedBoundingCylinder.png?raw=true target=)

### Description

This example creates an oriented cylinder that encloses a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). The axis of the cylinder is aligned with the longest axis of the [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html).

The example proceeds as follows:

1. A [vtkOBBTree](https://www.vtk.org/doc/nightly/html/classvtkOBBTree.html) creates an oriented bounding box. The z dimension of the box is aligned with the longest axis.
2. A [vtkQuad](https://www.vtk.org/doc/nightly/html/classvtkQuad.html) finds the center of each face of the bounding box.
3. A [vtkLineSource](https://www.vtk.org/doc/nightly/html/classvtkLineSource.html) creates a line from the centers of the long axis faces.
4. [vtkTubeFilter](https://www.vtk.org/doc/nightly/html/classvtkTubeFilter.html) creates a "cylinder" from the lines with a radius equal to the an inner circle of bounding box.
5. [vtkExtractEnclosedPoints](https://www.vtk.org/doc/nightly/html/classvtkExtractEnclosedPoints.html) determines if there are points outside the initial guess.
6. If there are points outside, the example does a linear search from the initial radius to the outer circle.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/OrientedBoundingCylinder/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OrientedBoundingCylinder.py**

```python
#!/usr/bin/env python3

import math
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import reference
from vtkmodules.vtkCommonCore import (
    vtkPoints, vtkMath
)
from vtkmodules.vtkCommonDataModel import (
    vtkPolyData,
    vtkQuad
)
from vtkmodules.vtkFiltersCore import vtkTubeFilter, vtkCleanPolyData
from vtkmodules.vtkFiltersGeneral import vtkOBBTree
from vtkmodules.vtkFiltersPoints import vtkExtractEnclosedPoints
from vtkmodules.vtkFiltersSources import (
    vtkLineSource,
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
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

def get_program_parameters():
    import argparse
    description = 'Create an oriented cylinder that encloses a vtkPolyData.'
    epilogue = '''
     The axis of the cylinder is aligned with the longest axis of the vtkPolyData.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None,
                        help='The polydata source file name,e.g. Torso.vtp.')
    args = parser.parse_args()

    return args.file_name

def main():
    file_name = get_program_parameters()
    poly_data = None
    if file_name:
        if Path(file_name).is_file():
            poly_data = read_poly_data(file_name)
        else:
            print(f'{file_name} not found.')
    if file_name is None or poly_data is None:
        sphere_source = vtkSphereSource(center=(0, 0, 0), radius=0.5, theta_resolution=20, phi_resolution=11)
        poly_data = sphere_source.update().output

    colors = vtkNamedColors()

    # Get the bounds of the polydata.
    # bounds = poly_data.bounds

    # Create the tree.
    obb_tree = vtkOBBTree(data_set=poly_data, max_level=1)
    obb_tree.BuildLocator()

    # Get the PolyData for the OBB.
    obb_polydata = vtkPolyData()
    obb_tree.GenerateRepresentation(0, obb_polydata)

    # Get the points of the OBB.
    obb_points = vtkPoints()
    obb_points.DeepCopy(obb_polydata.GetPoints())

    points = list()
    # Transfer the points to a list.
    for i in range(0, obb_points.number_of_points):
        points.append(obb_points.GetPoint(i))

    centers = list()
    face_points = list()
    end_points = list()
    radii = list()
    lengths = list()

    # x face.
    # ids[0] = 2 ids[1] = 3 ids[2] = 7 ids[3] = 6
    face_points.append(points[2])
    face_points.append(points[3])
    face_points.append(points[7])
    face_points.append(points[6])
    length, center = make_a_quad(face_points)
    radii.append(length)
    centers.append(center)
    # ids[0] = 0 ids[1] = 4 ids[2] = 5 ids[3] = 1
    face_points[0] = points[0]
    face_points[1] = points[4]
    face_points[2] = points[5]
    face_points[3] = points[1]
    length, end_point = make_a_quad(face_points)
    end_points.append(end_point)
    d = math.sqrt(vtkMath.Distance2BetweenPoints(centers[0], end_points[0]))
    lengths.append(math.sqrt(vtkMath.Distance2BetweenPoints(centers[0], end_points[0])) / 2.0)

    # y face.
    # ids[0] = 0 ids[1] = 1 ids[2] = 2 ids[3] = 0
    face_points[0] = points[0]
    face_points[1] = points[1]
    face_points[2] = points[2]
    face_points[3] = points[3]
    length, center = make_a_quad(face_points)
    radii.append(length)
    centers.append(center)

    face_points[0] = points[4]
    face_points[1] = points[6]
    face_points[2] = points[7]
    face_points[3] = points[5]
    length, end_point = make_a_quad(face_points)
    end_points.append(end_point)
    lengths.append(math.sqrt(vtkMath.Distance2BetweenPoints(centers[0], end_points[0])) / 2.0)

    # z face.
    # ids[0] = 0 ids[1] = 2 ids[2] = 6 ids[3] = 4
    face_points[0] = points[0]
    face_points[1] = points[2]
    face_points[2] = points[6]
    face_points[3] = points[4]
    length, center = make_a_quad(face_points)
    radii.append(math.sqrt(vtkMath.Distance2BetweenPoints(points[0], points[2])) / 2.0)
    outer_radius = math.sqrt(vtkMath.Distance2BetweenPoints(points[0], points[6])) / 2.0
    centers.append(center)
    # ids[0] = 1 ids[1] = 3 ids[2] = 7 ids[3] = 5
    face_points[0] = points[1]
    face_points[1] = points[5]
    face_points[2] = points[7]
    face_points[3] = points[3]
    length, end_point = make_a_quad(face_points)
    end_points.append(end_point)
    lengths.append(math.sqrt(vtkMath.Distance2BetweenPoints(centers[2], end_points[2]) / 2.0))

    # Find long axis.
    long_axis = lengths.index(max(lengths))
    length = lengths[long_axis]
    radius = radii[long_axis]
    print(f'Long axis: {long_axis}\nRadii: {fmt_floats(radii)}')
    print(f'Radius: {radius:g} Outer radius: {outer_radius:g}')
    center = centers[long_axis]
    end_point = end_points[long_axis]

    line_source = vtkLineSource(point1=center, point2=end_point)

    tube = vtkTubeFilter(radius=radius, number_of_sides=51, capping=True)
    line_source >> tube

    # See if all points lie inside the cylinder.
    clean = vtkCleanPolyData(input_data=tube.update().output)

    enclosed_points = vtkExtractEnclosedPoints(surface_data=clean.update().output, input_data=poly_data,
                                               tolerance=0.0001, generate_outliers=True, check_surface=True)
    enclosed_points.update()

    print(
        f'Total number of points: {poly_data.GetPoints().number_of_points},  Excluded points: {enclosed_points.GetOutput(1).GetPoints().number_of_points}')

    rep_mapper = vtkPolyDataMapper(input_data=obb_polydata)
    rep_mapper.SetInputData(obb_polydata)
    rep_actor = vtkActor(mapper=rep_mapper)
    rep_actor.property.color = colors.GetColor3d('peacock')
    rep_actor.property.opacity = 0.6

    # Create a mapper and actor for the cylinder.
    cylinder_mapper = vtkPolyDataMapper()
    tube >> cylinder_mapper

    cylinder_actor = vtkActor(mapper=cylinder_mapper)
    cylinder_actor.property.color = colors.GetColor3d('banana')
    cylinder_actor.property.opacity = 0.5

    original_mapper = vtkPolyDataMapper(input_data=poly_data)
    original_actor = vtkActor(mapper=original_mapper)
    original_actor.property.color = colors.GetColor3d('tomato')

    # Create a renderer, render window, and interactor.
    renderer = vtkRenderer(use_hidden_line_removal=True, gradient_background=True,
                           background2=colors.GetColor3d('LightSeaGreen'), background=colors.GetColor3d('SkyBlue'))

    # Display all centers and endpoints.
    cs = list()
    cs.append(colors.GetColor3d('red'))
    cs.append(colors.GetColor3d('green'))
    cs.append(colors.GetColor3d('blue'))
    for i in range(0, 3):
        ps1 = vtkSphereSource(center=centers[i], radius=length * 0.04,
                              phi_resolution=21, theta_resolution=41)
        pm1 = vtkPolyDataMapper()
        ps1 >> pm1
        pa1 = vtkActor(mapper=pm1)
        pa1.property.color = cs[i]
        pa1.property.specular_power = 50
        pa1.property.specular = 0.4
        pa1.property.diffuse = 0.6
        renderer.AddActor(pa1)

        ps2 = vtkSphereSource(center=end_points[i], radius=length * 0.04,
                              phi_resolution=21, theta_resolution=41)
        pm2 = vtkPolyDataMapper()
        ps2 >> pm2
        pa2 = vtkActor(mapper=pm2)
        pa2.property.color = cs[i]
        renderer.AddActor(pa2)

    render_window = vtkRenderWindow(size=(640, 480), window_name='OrientedBoundingCylinder')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    # Add the actors to the scene.
    renderer.AddActor(original_actor)
    renderer.AddActor(cylinder_actor)

    adjusted_incr = (outer_radius - radius) / 20.0
    if enclosed_points.GetOutput(1).GetPoints().GetNumberOfPoints() > 4:
        print('Improving...')
        r = radius
        encl_pts = enclosed_points.GetOutput(1).GetPoints()
        while encl_pts.number_of_points > 4:
            tube.radius = r
            tube.update()
            clean.update()
            enclosed_points.update()
            encl_pts = enclosed_points.GetOutput(1).GetPoints()
            if encl_pts is not None:
                print(f'Radius: {r:g} Excluded points: {encl_pts.number_of_points}')
                render_window.Render()
            else:
                break
            r += adjusted_incr

    # Generate an interesting view.
    renderer.ResetCamera()
    renderer.active_camera.Azimuth(-60)
    renderer.active_camera.Elevation(-15)
    renderer.active_camera.Dolly(1.3)
    renderer.ResetCameraClippingRange()

    cam_orient_manipulator = vtkCameraOrientationWidget(parent_renderer=renderer,
                                                        interactor=render_window_interactor)
    # Enable the widget.
    cam_orient_manipulator.On()

    # Render and interact.
    render_window_interactor.Start()

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
        reader.update()
        poly_data = reader.output
        return poly_data
    else:
        return None

def make_a_quad(points):
    # Use a quad to find centers of OBB faces.
    quad = vtkQuad()
    quad.GetPoints().SetPoint(0, points[0])
    quad.GetPoints().SetPoint(1, points[1])
    quad.GetPoints().SetPoint(2, points[2])
    quad.GetPoints().SetPoint(3, points[3])
    quad.GetPointIds().SetId(0, 0)
    quad.GetPointIds().SetId(1, 1)
    quad.GetPointIds().SetId(2, 2)
    quad.GetPointIds().SetId(3, 3)

    pcenter = [0.0] * 3
    quad.GetParametricCenter(pcenter)
    cweights = [quad.number_of_points] * 3
    p_sub_id = reference(0)
    center = [0.0] * 3
    quad.EvaluateLocation(p_sub_id, pcenter, center, cweights)

    print(f'Center: ({fmt_floats(center)})')
    length = math.sqrt(quad.GetLength2()) / 2.0

    return length, center

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

if __name__ == '__main__':
    main()
```
