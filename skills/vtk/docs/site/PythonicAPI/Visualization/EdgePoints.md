<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/EdgePoints/ -->

# EdgePoints

Repository source: [EdgePoints](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/EdgePoints.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestEdgePoints.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestEdgePoints.png?raw=true target=)

## Description

This example uses [vtkEdgePoints](https://www.vtk.org/doc/nightly/html/classvtkEdgePoints.html) to generate a set of points that lie on an isosurface. Points are generated along the edges of cells that straddle the given iso value. Unlike [vtkMarchingCubes](https://www.vtk.org/doc/nightly/html/classvtkMarchingCubes.html) it does not generate normals at the points.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/EdgePoints/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**EdgePoints.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersGeneral import vtkEdgePoints
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkRenderingCore import (
    vtkCamera,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkPolyDataMapper, vtkActor
)

def get_program_parameters():
    import argparse
    description = 'Edge Points.'
    epilogue = '''

   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename', help='A required filename e.g. FullHead.mhd.')
    parser.add_argument('iso', default=100, type=int, nargs='?', help='The first iso-contour.')
    args = parser.parse_args()
    return args.filename, args.iso

def main():
    fn, iso_value = get_program_parameters()

    if not Path(fn).is_file():
        print(f'The path: {fn} does not exist.')
        return

    colors = vtkNamedColors()
    colors.SetColor('IsoColor', 255, 125, 64, 255)
    colors.SetColor('BkgColor', 51, 77, 102, 255)

    # Set a background color for the renderer and set the size of the
    # render window (expressed in pixels).
    renderer = vtkRenderer(background=colors.GetColor3d('BkgColor'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name='EdgePoints')
    ren_win.AddRenderer(renderer)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    reader = vtkMetaImageReader(file_name=fn)

    iso_extractor = vtkEdgePoints(value=iso_value)

    iso_mapper = vtkPolyDataMapper(scalar_visibility=False)
    reader >> iso_extractor >> iso_mapper

    iso = vtkActor(mapper=iso_mapper)
    iso.property.diffuse_color = colors.GetColor3d('Bisque')

    # An outline provides context around the data.
    outline_data = vtkOutlineFilter()

    outline_mapper = vtkPolyDataMapper()
    reader >> outline_data >> outline_mapper

    outline = vtkActor(mapper=outline_mapper)
    outline.property.color = colors.GetColor3d('Black')

    # It is convenient to create an initial view of the data. The FocalPoint
    # and Position form a vector direction. Later on (ResetCamera() method)
    # this vector is used to position the camera to look at the data in
    # this direction.
    camera = vtkCamera()
    camera.view_up = (0, 0, -1)
    camera.position = (0, -1, 0)
    camera.focal_point = (0, 0, 0)
    camera.ComputeViewPlaneNormal()
    camera.Azimuth(30.0)
    camera.Elevation(30.0)

    # Actors are added to the renderer. An initial camera view is created.
    # The Dolly() method moves the camera towards the FocalPoint,
    # thereby enlarging the image.
    renderer.AddActor(outline)
    renderer.AddActor(iso)
    renderer.active_camera = camera
    renderer.ResetCamera()
    camera.Dolly(1.1)

    # Note that when camera movement occurs (as it does in the Dolly()
    # method), the clipping planes often need adjusting. Clipping planes
    # consist of two planes: near and far along the view direction. The
    # near plane clips out objects in front of the plane the far plane
    # clips out objects behind the plane. This way only what is drawn
    # between the planes is actually rendered.
    renderer.ResetCameraClippingRange()

    # Initialize the event loop and then start it.
    ren_win.Render()
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
