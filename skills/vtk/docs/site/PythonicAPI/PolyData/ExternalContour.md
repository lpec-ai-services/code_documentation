<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/ExternalContour/ -->

# ExternalContour

Repository source: [ExternalContour](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/ExternalContour.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExternalContour.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestExternalContour.png?raw=true target=)

### Description

Compute the external contour of a polydata.

At first, it creates a black and white image of a scene containing the polydata and then extracts the contour of the black shape from the image.

Note

A longstanding bug is fixed, see the discussion [here](https://gitlab.kitware.com/vtk/vtk/-/issues/19412).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/ExternalContour/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExternalContour.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import (
    vtkCleanPolyData,
    vtkContourFilter
)
from vtkmodules.vtkFiltersGeneral import (
    vtkTransformFilter
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
# noinspection PyUnresolvedReferences
from vtkmodules.vtkIOImage import vtkPNGWriter
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkWindowToImageFilter
)

def get_program_parameters():
    import argparse
    description = 'ExtractSelection'
    epilogue = """
   """
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None, help='Bunny.vtp')
    args = parser.parse_args()
    return args.file_name

def main():
    colors = vtkNamedColors()

    fn = get_program_parameters()

    if fn:
        fn_path = Path(fn)
        if not fn_path.is_file():
            print('Unable to find: ', fn_path)
            return
        else:
            reader = vtkXMLPolyDataReader(file_name=fn_path)
            data3d = reader.update().output
    else:
        source = vtkSphereSource(center=(0.0, 0.0, 5.0), radius=2.0, theta_resolution=20, phi_resolution=20)
        data3d = source.update().output

    bounds_data = data3d.bounds
    center_data = data3d.center

    #  Black and white scene with the data in order to print the view.
    mapper_data = vtkPolyDataMapper()
    data3d >> mapper_data
    actor_data = vtkActor(mapper=mapper_data)
    actor_data.property.color = colors.GetColor3d("Black")

    tmp_rend = vtkRenderer(background=colors.GetColor3d("White"))

    tmp_rend.AddActor(actor_data)
    tmp_rend.ResetCamera()
    tmp_rend.active_camera.parallel_projection = True

    tmp_rw = vtkRenderWindow(off_screen_rendering=True)
    tmp_rw.AddRenderer(tmp_rend)

    tmp_rw.Render()

    # Get a print of the window.
    window_to_image_filter = vtkWindowToImageFilter(input=tmp_rw, scale=2)
    window_to_image_filter.update()

    # writer = vtkPNGWriter(file_name="ExternalContourWindowPrint.png")
    # window_to_image_filter >> writer
    # writer.Write()

    # Extract the silhouette corresponding to the black limit of the image.
    cont_filter = vtkContourFilter()
    cont_filter.SetValue(0, 255)

    # Clean the data.
    clean = vtkCleanPolyData()
    window_to_image_filter >> cont_filter >> clean
    contour = clean.update().output

    # Make the contour coincide with the data.

    bounds_contour = contour.bounds
    ratio_x = (bounds_data[1] - bounds_data[0]) / (bounds_contour[1] - bounds_contour[0])
    ratio_y = (bounds_data[3] - bounds_data[2]) / (bounds_contour[3] - bounds_contour[2])

    # Rescale the contour so that it shares the same bounds as the input data.
    transform1 = vtkTransform()
    transform1.Scale(ratio_x, ratio_y, 1.0)

    tfilter1 = vtkTransformFilter(transform=transform1, input_data=contour)

    contour = tfilter1.update().output

    # Translate the contour so that it shares the same center as the input data.
    center_contour = contour.center
    trans_x = center_data[0] - center_contour[0]
    trans_y = center_data[1] - center_contour[1]
    trans_z = center_data[2] - center_contour[2]

    transform2 = vtkTransform()
    transform2.Translate(trans_x, trans_y, trans_z)

    tfilter2 = vtkTransformFilter(transform=transform2, input_data=contour)

    contour = tfilter2.update().output

    # Updating the color of the data.
    actor_data.property.color = colors.GetColor3d("MistyRose")

    # Create a mapper and actor of the silhouette.
    mapper_contour = vtkPolyDataMapper(input_data=contour)

    actor_contour = vtkActor(mapper=mapper_contour)
    actor_contour.property.line_width = 2.0

    # Create the renderers, render window, and interactor.

    renderer1 = vtkRenderer(viewport=(0.0, 0.0, 0.5, 1.0), background=colors.GetColor3d("DarkSlateGray"))
    renderer2 = vtkRenderer(viewport=(0.5, 0.0, 1.0, 1.0), background=colors.GetColor3d("MidnightBlue"))

    render_window = vtkRenderWindow(size=(400, 400), window_name="ExternalContour")
    render_window.AddRenderer(renderer1)
    render_window.AddRenderer(renderer2)

    style = vtkInteractorStyleTrackballCamera()

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    render_window_interactor.interactor_style = style

    # Add the actors.
    renderer1.AddActor(actor_data)
    # renderer1.AddActor(actor_contour)
    renderer2.AddActor(actor_contour)

    # Set the same initial view as in renderer1.
    render_window.Render()
    ren2_camera = vtkCamera()
    ren2_camera.DeepCopy(renderer1.active_camera)
    renderer2.active_camera = ren2_camera
    # If you want the views linked.
    # renderer2.active_camera = renderer1.active_camera

    render_window.Render()
    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
