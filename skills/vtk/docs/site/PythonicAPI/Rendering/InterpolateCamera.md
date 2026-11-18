<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/InterpolateCamera/ -->

# InterpolateCamera

Repository source: [InterpolateCamera](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/InterpolateCamera.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestInterpolateCamera.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestInterpolateCamera.png?raw=true target=)

## Description

This example uses [vtkCameraInterpolator](https://www.vtk.org/doc/nightly/html/classvtkCameraInterpolator.html) to generate a smooth interpolation between camera views. The key points for the camera positions are generated from the [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html)'s bounding box. The camera focal points are at the center of the polydata.

The key points are computed from the corners of the bounding box. They are pushed out along a vector from the center to the corner point. The amount of pushing is a random multiplier of the range of the data.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/InterpolateCamera/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**InterpolateCamera.py**

```python
#!/usr/bin/env python3

from pathlib import Path
from time import sleep

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkMath,
    vtkMinimalStandardRandomSequence
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
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
    vtkCamera,
    vtkCameraInterpolator,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Interpolate camera.'
    epilogue = '''
    '''

    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None, help='A polydata file e.g. spider.ply')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()
    if file_name:
        fn = Path(file_name)
        if not fn.is_file():
            print(f'{fn}\nNot found.')
            return
        else:
            poly_data = read_poly_data(Path(file_name))
    else:
        source = vtkSphereSource()
        poly_data = source.update().output

    center = poly_data.center
    key_points = compute_key_points(poly_data)

    # Setup camera views for interpolation.
    interpolator = vtkCameraInterpolator(interpolation_type=vtkCameraInterpolator.INTERPOLATION_TYPE_SPLINE)

    for i in range(0, len(key_points) + 1):
        cam = vtkCamera(focal_point=center)
        if i < len(key_points):
            cam.position = key_points[i]
        else:
            cam.position = key_points[0]
        cam.view_up = (0.0, 0.0, 1.0)
        interpolator.AddCamera(float(i), cam)

    # Visualize
    mapper = vtkPolyDataMapper(input_data=poly_data, scalar_visibility=False)

    back_prop = vtkProperty()
    back_prop.diffuse_color = colors.GetColor3d('Banana')
    back_prop.diffuse = 0.76
    back_prop.specular = 0.4
    back_prop.specular_power = 30

    actor = vtkActor(mapper=mapper)
    actor.backface_property = back_prop
    actor.property.diffuse_color = colors.GetColor3d('Crimson')
    actor.property.specular = 0.6
    actor.property.specular_power = 30

    renderer = vtkRenderer(background=colors.GetColor3d('Silver'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='InterpolateCamera')
    render_window.AddRenderer(renderer)

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    renderer.AddActor(actor)

    camera = vtkCamera()
    renderer.active_camera = camera

    num_steps = 600
    min_t = interpolator.GetMinimumT()
    max_t = interpolator.GetMaximumT()
    for i in range(0, num_steps):
        t = float(i) * (max_t - min_t) / float((num_steps - 1))
        interpolator.InterpolateCamera(t, camera)
        renderer.ResetCameraClippingRange()
        render_window.Render()
        sleep(50.0e-3)

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

def compute_key_points(poly_data):
    random_sequence = vtkMinimalStandardRandomSequence(seed=4355412)

    # Get Bounding Box.
    bounds = poly_data.bounds

    delta = max(max(bounds[1] - bounds[0], bounds[3] - bounds[2]),
                bounds[5] - bounds[4])

    center = poly_data.center

    points = list()
    points.append([bounds[0], bounds[2], bounds[4]])
    points.append([bounds[1], bounds[2], bounds[4]])
    points.append([bounds[1], bounds[2], bounds[5]])
    points.append([bounds[0], bounds[2], bounds[5]])
    points.append([bounds[0], bounds[3], bounds[4]])
    points.append([bounds[1], bounds[3], bounds[4]])
    points.append([bounds[1], bounds[3], bounds[5]])
    points.append([bounds[0], bounds[3], bounds[5]])

    key_points = list()

    for i in range(0, len(points)):
        key_points.append([0.0] * 3)
        direction = [0.0] * 3
        for j in range(0, 3):
            direction[j] = points[i][j] - center[j]
        vtkMath.Normalize(direction)
        factor = random_sequence.GetRangeValue(1.0, 3.0)
        random_sequence.Next()
        for j in range(0, 3):
            key_points[i][j] = points[i][j] + direction[j] * delta * factor

    return key_points

if __name__ == '__main__':
    main()
```
