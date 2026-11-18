<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/CameraOrientationWidget/ -->

# CameraOrientationWidget

Repository source: [CameraOrientationWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/CameraOrientationWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestCameraOrientationWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestCameraOrientationWidget.png?raw=true target=)

### Description

This example demonstrates the usage and versatility of the [vtkCameraOrientationWidget](https://www.vtk.org/doc/nightly/html/classvtkCameraOrientationWidget.html), also, for comparison, a [vtkOrientationMarkerWidget](https://www.vtk.org/doc/nightly/html/classvtkOrientationMarkerWidget.html) is provided.

The ability to automatically change axes labels and colors depending upon the object being viewed is demonstrated. To do this, just load any one of the following files from the vtk-examples testing data.

```python
"Human.vtp", "Torso.vtp", "cow.vtp", "cowHead.vtp", "horse.vtp", "Bunny.vtp"
```

These files are found in `vtk-examples/src/Testing/Data`.

If no file name is entered, a cone is rendered.

The option **-r** will move the camera orientation marker to upper left and the orientation marker widget to upper right.

The vtkCameraOrientationWidget has shafts and little spheres with text on them. The spheres always follow the camera.

The widget representation's orientation is synchronized with the camera of the parent renderer.

To look down on any particular axis, simply click on a handle.

To rotate the camera and get a feel of the camera orientation, either move the mouse in the render window or click on a handle and move it around.

Some history:

- The [vtkCameraOrientationWidget](https://www.vtk.org/doc/nightly/html/classvtkCameraOrientationWidget.html) was introduced in the MR: [!8156](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8156), 18 July, 2021.
- Labelling of the vertices was introduced in the MR: [!11665](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/11665), 16 November, 2024.
- Coloring of the vertices was introduced in the MR: [!12489](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/12489), 01 October, 2025

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/CameraOrientationWidget/)), ([Python](../../Python/Widgets/CameraOrientationWidget.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CameraOrientationWidget.py**

```python
#!/usr/bin/env python3

# This example demonstrates how to use the vtkCameraOrientationWidget to control
# a renderer's camera orientation.

import math
from pathlib import Path
from sys import argv

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkIOGeometry import (
    vtkBYUReader,
    vtkOBJReader,
    vtkSTLReader
)
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkIOPLY import vtkPLYReader
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkOrientationMarkerWidget
)
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Demonstrates the use of the Camera Orientation Widget.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('fname', nargs='?', default=None, help='The path to the file to render e.g. Human.vtp.')
    parser.add_argument('-r', '--reposition', action='store_true',
                        help='Move the camera orientation marker to upper left'
                             ' and the orientation marker widget to upper right.')
    args = parser.parse_args()
    return args.fname, args.reposition

def main():
    colors = vtkNamedColors()
    colors.SetColor('ParaViewBlueGrayBkg', 84, 89, 109, 255)
    colors.SetColor('ParaViewWarmGrayBkg', 98, 93, 90, 255)

    file_name, reposition = get_program_parameters()
    path = None

    if file_name:
        path = Path(file_name)
        if not path.is_file():
            print(f'Unable to find: {path}')
            return
        poly_data = read_poly_data(path)
    else:
        # Use a cone as a source with the golden ratio (φ) for the height. Because we can!
        # If the short side is one then φ = 2 × sin(54°) or φ = 1/2 + √5 / 2
        cone_source = vtkConeSource(center=(0, 0, 0), radius=1, height=(1.0 + math.sqrt(5.0)) / 2.0, resolution=64,
                                    direction=(0, 1, 0))
        poly_data = cone_source.update().output

    # Assign a category for the labels and colors.
    category = 'xyz'
    if path is not None:
        if path.name in ['Human.vtp', 'Torso.vtp']:
            category = 'lrsiap'
        if path.name in ['horse.vtp', 'Bunny.vtp']:
            category = 'padvlr'
        elif path.name in ['cow.vtp', 'cowHead.vtp']:
            category = 'apdvrl'

    # The labels and colors for the various axes.
    alc = get_axes_params(colors)

    # Transform the polydata.
    tran = vtkTransform()
    tran.Identity()
    if path is not None:
        if path.name == 'Human.vtp':
            tran.RotateX(-90)
            tran.RotateZ(180)
        if path.name == 'Torso.vtp':
            tran.RotateX(-90)
        if path.name == 'horse.vtp':
            tran.RotateX(-90)
            tran.RotateZ(90)
    tf = vtkTransformFilter(transform=tran)
    surf = poly_data >> tf

    mapper = vtkPolyDataMapper()
    surf >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.color = colors.GetColor3d('Tan')

    ren = vtkRenderer(background=colors.GetColor3d('ParaViewBLueGrayBkg'))
    if path is None:
        ren_win = vtkRenderWindow(size=(600, 600), window_name=f'{Path(argv[0]).name:s}')
    else:
        ren_win = vtkRenderWindow(size=(600, 600), window_name=f'{Path(argv[0]).name:s} {path.name}')
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    # Important: The interactor must be set prior
    #  to enabling the Camera Orientation Widget.
    iren.render_window = ren_win
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    ren.AddActor(actor)

    cow = make_camera_orientation_widget(ren, alc[category], colors, reposition)
    omw = make_orientation_marker_widget(ren, iren, alc[category], colors, reposition)

    ren.ResetCamera()
    ren_win.Render()
    iren.Initialize()
    iren.Start()

def read_poly_data(path):
    """
    Use a vtk file reader to get the polydata.

    :param path: The pathlib Path to the file.
    :return:
    """
    if path is None:
        print(f'No file name.')
        return None

    valid_suffixes = ['.g', '.obj', '.stl', '.ply', '.vtk', '.vtp']
    ext = None
    if path.suffix:
        ext = path.suffix.lower()
    if path.suffix not in valid_suffixes:
        print(f'No reader for this file suffix: {ext}')
        return None

    reader = None
    if ext == '.ply':
        reader = vtkPLYReader(file_name=path)
    elif ext == '.vtp':
        reader = vtkXMLPolyDataReader(file_name=path)
    elif ext == '.obj':
        reader = vtkOBJReader(file_name=path)
    elif ext == '.stl':
        reader = vtkSTLReader(file_name=path)
    elif ext == '.vtk':
        reader = vtkPolyDataReader(file_name=path)
    elif ext == '.g':
        reader = vtkBYUReader(file_name=path)

    if reader:
        return reader.update().output
    else:
        return None

def set_axes_labels():
    return {
        # Labels are: Anterior, Posterior, Dorsal, Ventral, Left, Right
        'apdvlr': {'+X': 'A', '-X': 'P', '+Y': 'D', '-Y': 'V', '+Z': 'L', '-Z': 'R'},
        'apdvrl': {'+X': 'A', '-X': 'P', '+Y': 'D', '-Y': 'V', '+Z': 'R', '-Z': 'L'},
        'padvlr': {'+X': 'P', '-X': 'A', '+Y': 'D', '-Y': 'V', '+Z': 'L', '-Z': 'R'},
        # Labels are: Left, Right, Superior, Inferior, Anterior, Posterior
        'lrsiap': {'+X': 'L', '-X': 'R', '+Y': 'S', '-Y': 'I', '+Z': 'A', '-Z': 'P'},
        # Default labels
        'xyz': None
    }

def set_axes_colors(colors):
    return {
        'apdvlr': {'+X': 'IndianRed', '-X': 'FireBrick', '+Y': 'LimeGreen', '-Y': 'DarkGreen', '+Z': 'Blue',
                   '-Z': 'SteelBlue'},
        'apdvrl': {'+X': 'IndianRed', '-X': 'FireBrick', '+Y': 'LimeGreen', '-Y': 'DarkGreen', '+Z': 'Blue',
                   '-Z': 'SteelBlue'},
        'padvlr': {'+X': 'IndianRed', '-X': 'FireBrick', '+Y': 'LimeGreen', '-Y': 'DarkGreen', '+Z': 'Blue',
                   '-Z': 'SteelBlue'},
        'lrsiap': {'+X': 'Blue', '-X': 'SteelBlue', '+Y': 'LimeGreen', '-Y': 'DarkGreen', '+Z': 'IndianRed',
                   '-Z': 'FireBrick'},
        # Default colors.
        'xyz': None
    }

def get_axes_params(colors):
    """
    Gather the axes labels and colors into a dictionary.
    :param colors: vtkNamedColors object.
    :return: The dictionary of axes labels and colors.
    """
    # The keys must be the same.
    axes_labels = set_axes_labels()
    axes_colors = set_axes_colors(colors)
    label_keys = set(axes_labels.keys())
    color_keys = set(axes_colors.keys())
    common_keys = label_keys.intersection(color_keys)
    alc = dict()
    for k in common_keys:
        alc[k] = (axes_labels[k], axes_colors[k])
    return alc

def make_camera_orientation_widget(ren, alc, colors, reposition):
    """
    Make a camera orientation widget for a given renderer.

    :param ren: The renderer.
    :param alc: A dictionary of labels and colors for the axis.
    :param colors: vtkNamedColors object.
    :param reposition: Move the camera orientation widget to upper left.
    :return: The camera orientation widget.
    """

    cow = vtkCameraOrientationWidget(parent_renderer=ren, enabled=True)
    cow.On()

    rep = cow.representation

    if reposition:
        rep.AnchorToUpperLeft()

    if not alc[0] is None:
        rep.SetXPlusLabelText(alc[0]['+X'])
        rep.SetXMinusLabelText(alc[0]['-X'])
        rep.SetYPlusLabelText(alc[0]['+Y'])
        rep.SetYMinusLabelText(alc[0]['-Y'])
        rep.SetZPlusLabelText(alc[0]['+Z'])
        rep.SetZMinusLabelText(alc[0]['-Z'])

        rep.SetXAxisColor(colors.GetColor3d(alc[1]['+X']))
        rep.SetYAxisColor(colors.GetColor3d(alc[1]['+Y']))
        rep.SetZAxisColor(colors.GetColor3d(alc[1]['+Z']))

    cow.SetRepresentation(rep)

    return cow

def make_axes_actor(alc, colors):
    """
    Make an Axes actor.

    :param alc: A dictionary of labels and colors for the axis.
    :param colors: vtkNamedColors object.
    :return: The axis actor.
    """
    axes = vtkAxesActor()
    if alc[0] is None:
        # Use the default vtkAxesActor.
        pass
    else:
        axes.SetXAxisLabelText(alc[0]['+X'])
        axes.SetYAxisLabelText(alc[0]['+Y'])
        axes.SetZAxisLabelText(alc[0]['+Z'])

        x_shaft_prop = axes.x_axis_shaft_property
        x_shaft_prop.color = colors.GetColor3d(alc[1]['+X'])
        x_tip_prop = axes.x_axis_tip_property
        x_tip_prop.color = colors.GetColor3d(alc[1]['+X'])

        y_shaft_prop = axes.y_axis_shaft_property
        y_shaft_prop.color = colors.GetColor3d(alc[1]['+Y'])
        y_tip_prop = axes.y_axis_tip_property
        y_tip_prop.color = colors.GetColor3d(alc[1]['+Y'])

        z_shaft_prop = axes.z_axis_shaft_property
        z_shaft_prop.color = colors.GetColor3d(alc[1]['+Z'])
        z_tip_prop = axes.z_axis_tip_property
        z_tip_prop.color = colors.GetColor3d(alc[1]['+Z'])

    return axes

def make_orientation_marker_widget(ren, iren, alc, colors, reposition):
    """
    Make an orientation marker widget.

    :param iren: Interactor
    :param ren: Renderer
    :param alc: A dictionary of labels and colors for the axis.
    :param colors: vtkNamedColors object.
    :param reposition: Move the orientation marker widget to upper right.
    :return: The orientation marker widget.
    """
    axes = make_axes_actor(alc, colors)
    rgba = [0.0] * 4
    colors.GetColor('Carrot', rgba)
    rgb = tuple(rgba[:3])
    ll = (0.0, 0.0, 0.2, 0.2)
    ur = (0.8, 0.8, 1.0, 1.0)
    widget = vtkOrientationMarkerWidget(orientation_marker=axes,
                                        interactor=iren, default_renderer=ren,
                                        outline_color=rgb, viewport=ll,
                                        enabled=True, interactive=True, zoom=1.0)
    if reposition:
        widget.viewport = ur
    return widget

if __name__ == '__main__':
    main()
```
