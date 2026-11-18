<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/ImplicitAnnulusWidget/ -->

# ImplicitAnnulusWidget

Repository source: [ImplicitAnnulusWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/ImplicitAnnulusWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImplicitAnnulusWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImplicitAnnulusWidget.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/ImplicitAnnulusWidget/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImplicitAnnulusWidget.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingUI
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkAnnulus
from vtkmodules.vtkFiltersCore import (
    vtkAppendPolyData,
    vtkClipPolyData,
    vtkGlyph3D
)
from vtkmodules.vtkFiltersSources import (
    vtkConeSource,
    vtkSphereSource)
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkImplicitAnnulusRepresentation,
    vtkImplicitAnnulusWidget,
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Clip polydata with an implicit annulus.'
    epilogue = '''
    By specifying a .vtp file, the example can operate on arbitrary polydata.
'''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None, help='A VTK Poly Data file e.g. cow.vtp')

    args = parser.parse_args()
    return args.file_name

def main(fn):
    colors = vtkNamedColors()

    fn = get_program_parameters()

    # This portion of the code clips the mace or the input from the reader with
    #  the vtkAnnulus implicit function. The clipped region is colored green.
    annulus = vtkAnnulus()
    clipper = vtkClipPolyData(clip_function=annulus, inside_out=True)

    if fn:
        fp = Path(fn)
        if not (fp.is_file() and fp.suffix == '.vtp'):
            print(f'Expected an existing file name with extension .vtp\n  got: {fp}')
            return

        reader = vtkXMLPolyDataReader(file_name=fp)
        reader >> clipper
        source = reader.update().output
    else:
        mace = create_mace()
        source = mace.output

    clipper.input_data = source
    bounds = source.bounds
    print(f'bounds: ({fmt_floats(bounds)})')

    # Create a mapper and actor.
    mapper = vtkPolyDataMapper(input_data=source)

    back_faces = vtkProperty(diffuse_color=colors.GetColor3d('Gold'))

    actor = vtkActor(backface_property=back_faces, mapper=mapper, visibility=True)

    select_mapper = vtkPolyDataMapper()
    clipper >> select_mapper

    select_actor = vtkActor(mapper=select_mapper, scale=(1.01, 1.01, 1.01), visibility=False)
    select_actor.property.color = colors.GetColor3d('Lime')

    # Create the RenderWindow, Renderer and both Actors
    renderer = vtkRenderer(background=colors.GetColor3d('MidnightBlue'))
    renderer.AddActor(actor)
    renderer.AddActor(select_actor)
    ren_win = vtkRenderWindow(multi_samples=0, size=(600, 600), window_name='ImplicitAnnulusWidget')
    ren_win.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    ren_win.interactor = iren
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    # The SetInteractor method is how 3D widgets are associated with the render
    # window interactor. Internally, SetInteractor sets up a bunch of callbacks
    # using the Command/Observer mechanism (AddObserver()).
    my_callback = TICWCallback(annulus, select_actor)

    radii = list()
    for i in range(1, 6, 2):
        radii.append((bounds[i] - bounds[i - 1]) / 2.0)
    radius = min(radii)

    rep = vtkImplicitAnnulusRepresentation(place_factor=1.25, scale_enabled=False,
                                           inner_radius=radius * 0.5, outer_radius=radius)
    rep.PlaceWidget(bounds)
    print(f'Inner radius: {rep.inner_radius:g}')
    print(f'Outer radius: {rep.outer_radius:g}')

    annulus_widget = vtkImplicitAnnulusWidget(interactor=iren, representation=rep, enabled=True)
    annulus_widget.AddObserver('InteractionEvent', my_callback)

    renderer.active_camera.Azimuth(60)
    renderer.active_camera.Elevation(30)
    renderer.ResetCamera()
    renderer.active_camera.Zoom(1.0)

    cow = vtkCameraOrientationWidget(parent_renderer=renderer)
    # Enable the widget.
    cow.On()

    # Render and interact.
    iren.Initialize()
    ren_win.Render()
    annulus_widget.On()

    # Begin mouse interaction.
    iren.Start()

class TICWCallback:
    def __init__(self, annulus, select_actor):
        self.annulus = annulus
        self.select_actor = select_actor

    def __call__(self, caller, ev):
        rep = caller.representation
        rep.GetAnnulus(self.annulus)
        self.select_actor.visibility = True

def create_mace():
    # Create a mace out of filters.
    sphere = vtkSphereSource()
    cone_source = vtkConeSource()
    glyph = vtkGlyph3D(source_connection=cone_source.output_port,
                       vector_mode=Glyph3D.VectorMode.VTK_USE_NORMAL,
                       scale_mode=Glyph3D.ScaleMode.VTK_SCALE_BY_VECTOR,
                       scale_factor=0.25)
    sphere >> glyph

    # The sphere and spikes are appended into a single polydata.
    # This just makes things simpler to manage.
    apd = vtkAppendPolyData()
    (glyph, sphere) >> apd
    apd.update()
    return apd

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

@dataclass(frozen=True)
class Glyph3D:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_BY_SCALE: int = 0
        VTK_COLOR_BY_SCALAR: int = 1
        VTK_COLOR_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class IndexMode:
        VTK_INDEXING_OFF: int = 0
        VTK_INDEXING_BY_SCALAR: int = 1
        VTK_INDEXING_BY_VECTOR: int = 2

    @dataclass(frozen=True)
    class ScaleMode:
        VTK_SCALE_BY_SCALAR: int = 0
        VTK_SCALE_BY_VECTOR: int = 1
        VTK_SCALE_BY_VECTORCOMPONENTS: int = 2
        VTK_DATA_SCALING_OFF: int = 3

    @dataclass(frozen=True)
    class VectorMode:
        VTK_USE_VECTOR: int = 0
        VTK_USE_NORMAL: int = 1
        VTK_VECTOR_ROTATION_OFF: int = 2
        VTK_FOLLOW_CAMERA_DIRECTION: int = 3

if __name__ == '__main__':
    file_name = get_program_parameters()
    main(file_name)
```
