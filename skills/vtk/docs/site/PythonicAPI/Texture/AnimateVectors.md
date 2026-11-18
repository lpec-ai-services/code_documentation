<!-- source: https://examples.vtk.org/site/PythonicAPI/Texture/AnimateVectors/ -->

# AnimateVectors

Repository source: [AnimateVectors](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Texture/AnimateVectors.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Texture/TestAnimateVectors.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Texture/TestAnimateVectors.png?raw=true target=)

### Description

Texture maps can be animated as a function of time. By choosing a texture map whose intensity varies monotonically from dark to light, and then “moving” the texture along an object,the object appears to crawl in the direction of the texture map motion. We can use this technique to add apparent motion to things like hedgehogs to show vector magnitude. This example uses texture map animation to simulate vector field motion.

Cite

See [B. Yamrom and K. M. Martin. *Vector Field Animation with Texture Maps.*](http://ieeexplore.ieee.org/abstract/document/365001/) IEEE Computer Graphics and Applications. 15(2):22–24, 1995 for background.

Info

See [Figure 7-3](../../VTKBook/07Chapter7.md#Figure%207-3) in [Chapter 7](../../VTKBook/07Chapter7.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Texture/AnimateVectors/)), ([Python](../../Python/Texture/AnimateVectors.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**AnimateVectors.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import (
    vtkGlyph3D,
    vtkThresholdPoints
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkFiltersSources import vtkLineSource
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTexture
)

def main():
    vec_anim_paths = list()
    fn1, fn2 = get_program_parameters()
    vec_anim_paths.append(Path(fn1))
    vec_anim_paths.append(Path(fn2))

    # Generate the other vecAnim file names. There are 8 of them.
    old_stem = vec_anim_paths[1].stem
    stem = old_stem[:-1]
    for i in range(2, 9):
        new_stem = stem + str(i)
        vec_anim_paths.append(vec_anim_paths[1].with_stem(new_stem))

    colors = vtkNamedColors()

    # Set up the render window, renderer, and interactor.
    renderer = vtkRenderer(background=colors.GetColor3d('Wheat'))
    render_window = vtkRenderWindow(size=(640, 480), window_name='AnimateVectors')
    render_window.AddRenderer(renderer)
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Read the data and greate the pipeline.
    reader = vtkStructuredPointsReader(file_name=vec_anim_paths[0])

    threshold = vtkThresholdPoints()
    threshold.SetUpperThreshold(200)
    threshold.SetThresholdFunction(vtkThresholdPoints.THRESHOLD_UPPER)

    line = vtkLineSource(resolution=1)

    lines = vtkGlyph3D(source_connection=line.output_port, scale_factor=0.005,
                       scale_mode=Glyph3D.ScaleMode.VTK_SCALE_BY_SCALAR
                       )
    reader >> threshold >> lines
    scalar_range = lines.update().output.scalar_range

    vector_mapper = vtkPolyDataMapper(scalar_range=scalar_range)
    lines >> vector_mapper

    vector_actor = vtkActor(mapper=vector_mapper)
    vector_actor.property.opacity = 0.99
    vector_actor.property.line_width = 1.5

    # Outline
    outline = vtkOutlineFilter()
    reader >> outline

    outline_mapper = vtkPolyDataMapper()
    reader >> outline >> outline_mapper

    outline_actor = vtkActor(mapper=outline_mapper)
    outline_actor.property.color = colors.GetColor3d('Black')

    #  Texture maps.
    texture_maps = list()
    for i in range(1, len(vec_anim_paths)):
        tmap = vtkStructuredPointsReader(file_name=vec_anim_paths[i])

        texture = vtkTexture(interpolate=False, repeat=False)
        tmap >> texture
        texture_maps.append(texture)

    vector_actor.SetTexture(texture_maps[0])

    # Add the actors to the renderer.
    renderer.AddActor(vector_actor)
    renderer.AddActor(outline_actor)

    cam1 = vtkCamera()
    cam1.clipping_range = (17.4043, 870.216)
    cam1.focal_point = (136.71, 104.025, 23)
    cam1.position = (204.747, 258.939, 63.7925)
    cam1.view_up = (-0.102647, -0.210897, 0.972104)
    cam1.Zoom(1.2)
    renderer.active_camera = cam1
    # Go into a loop.
    for j in range(0, 100):
        for i in range(0, len(texture_maps)):
            vector_actor.texture = texture_maps[i]
            render_window.Render()
    interactor.Start()

def get_program_parameters():
    import argparse
    description = 'Texture maps can be animated as a function of time.'
    epilogue = '''
    This example uses texture map animation to simulate vector field motion.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename1', help='carotid.vtk.')
    parser.add_argument('filename2', help='VectorAnimation/vecAnim1.vtk.')
    args = parser.parse_args()
    return args.filename1, args.filename2

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
    main()
```
