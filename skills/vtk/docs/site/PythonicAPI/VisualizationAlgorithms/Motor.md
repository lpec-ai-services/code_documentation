<!-- source: https://examples.vtk.org/site/PythonicAPI/VisualizationAlgorithms/Motor/ -->

# Motor

Repository source: [Motor](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/VisualizationAlgorithms/Motor.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestMotor.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/VisualizationAlgorithms/TestMotor.png?raw=true target=)

### Description

This is an example of texture clipping using a transparent texture map. The motor shown consists of five complex parts, some of which are hidden by the outer casing. To see the inside of the motor, we define an implicit clipping function. This function is simply the intersection of two planes to form a clipping "corner". The object **[vtkImplicitTextureCoords](https://www.vtk.org/doc/nightly/html/classvtkImplicitTextureCoords.html)** is used in combination with this implicit function to generate texture coordinates. These objects are then rendered with the appropriate texture map and the internal parts of the motor can be seen.

The texture map consists of three regions (as described previously in the chapter). The concealed region is transparent. The transition region is opaque but with a black (zero intensity) color. The highlighted region is full intensity and opaque. As can be seen from the result , the boundaries appear as black borders giving a nice visual effect.

Info

See [Figure 9-53](../../VTKBook/09Chapter9.md#Figure%209-53) in [Chapter 9](../../VTKBook/09Chapter9.md) The [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/Motor/)), ([Python](../../Python/VisualizationAlgorithms/Motor.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Motor.py**

```python
#!/usr/bin/env python3

import sys
from pathlib import Path

# This code is based on the VTK file: /IO/Geometry/Testing/Python/motor.py.

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkFloatArray,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import vtkPlanes
from vtkmodules.vtkFiltersCore import vtkPolyDataNormals
from vtkmodules.vtkFiltersTexture import vtkImplicitTextureCoords
from vtkmodules.vtkIOGeometry import vtkBYUReader
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTexture
)

def get_program_parameters():
    import argparse
    description = 'Texture clipping using a transparent texture map.'
    epilogue = '''
        Texture clipping using a transparent texture map.
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('textureFile', help='The texture file: texThres2.vtk')
    parser.add_argument('motorFile', help='The motor file: motor.g.')
    args = parser.parse_args()
    return args.textureFile, args.motorFile

def main():
    colors = vtkNamedColors()

    texture_file, motor_file = get_program_parameters()

    # Create the Renderer, RenderWindow and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    ren_win = vtkRenderWindow(size=(512, 512), window_name=f'{Path(sys.argv[0]).stem:s}')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    # Create the cutting planes.
    planes = vtkPlanes()
    points = vtkPoints()
    norms = vtkFloatArray()

    norms.number_of_components = 3
    points.InsertPoint(0, 0.0, 0.0, 0.0)
    norms.InsertTuple3(0, 0.0, 0.0, 1.0)
    points.InsertPoint(1, 0.0, 0.0, 0.0)
    norms.InsertTuple3(1, -1.0, 0.0, 0.0)
    planes.points = points
    planes.normals = norms

    # Get the texture.
    tex_reader = vtkStructuredPointsReader(file_name=texture_file)
    texture = vtkTexture(interpolate=False,repeat=False)
    tex_reader >> texture

    # Set up the pipelines for the parts of the motor.
    number_of_parts = 5
    part_colors = ['cold_grey', 'peacock', 'raw_sienna', 'banana', 'peach_puff']
    # Use this to control which parts to display.
    display_parts = [True] * number_of_parts
    # If display_parts[2] = False then an image like that in the VTK tests is produced.

    # Build the pipelines.
    for i in range(0, number_of_parts):
        byu=vtkBYUReader(geometry_file_name=motor_file,part_number=i+1)

        normals = vtkPolyDataNormals()

        tex = vtkImplicitTextureCoords(r_function=planes, flip_texture=False)

        byu_mapper = vtkDataSetMapper()

        byu >> normals >> tex >> byu_mapper

        byu_actor = vtkActor(mapper=byu_mapper, texture=texture)
        byu_actor.property.color = colors.GetColor3d(part_colors[i])

        if display_parts[i]:
            byu_actor.VisibilityOn()
        else:
            byu_actor.VisibilityOff()

        ren.AddActor(byu_actor)

    camera = vtkCamera()
    camera.SetFocalPoint(0.0286334, 0.0362996, 0.0379685)
    camera.SetPosition(1.37067, 1.08629, -1.30349)
    camera.SetViewAngle(17.673)
    camera.SetClippingRange(1, 10)
    camera.SetViewUp(-0.376306, -0.5085, -0.774482)
    ren.SetActiveCamera(camera)

    # Render the image.
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
