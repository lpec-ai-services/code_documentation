<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/CannyEdgeDetector/ -->

# CannyEdgeDetector

Repository source: [CannyEdgeDetector](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/CannyEdgeDetector.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestCannyEdgeDetector.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestCannyEdgeDetector.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/CannyEdgeDetector/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CannyEdgeDetector.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonExecutionModel import vtkImageToStructuredPoints
from vtkmodules.vtkFiltersCore import (
    vtkStripper,
    vtkThreshold)
from vtkmodules.vtkFiltersGeneral import (
    vtkLinkEdgels,
    vtkSubPixelPositionEdgels
)
from vtkmodules.vtkFiltersGeometry import vtkGeometryFilter
from vtkmodules.vtkIOImage import vtkPNGReader
from vtkmodules.vtkImagingColor import vtkImageLuminance
from vtkmodules.vtkImagingCore import (
    vtkImageCast,
    vtkImageConstantPad
)
from vtkmodules.vtkImagingGeneral import (
    vtkImageGaussianSmooth,
    vtkImageGradient
)
from vtkmodules.vtkImagingMath import vtkImageMagnitude
from vtkmodules.vtkImagingMorphological import vtkImageNonMaximumSuppression
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkImageActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'CannyEdgeDetector.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', help='The image file name to use e.g. Gourds.png.')
    args = parser.parse_args()
    return args.file_name

def main():
    fn = get_program_parameters()
    fp = Path(fn)
    file_check = True
    if not fp.is_file():
        print(f'Missing image file: {fp}.')
        file_check = False
    if not file_check:
        return

    colors = vtkNamedColors()

    # Define viewport ranges (x_min, y_min, x_max, y_max)
    original_viewport = (0.0, 0.0, 0.5, 1.0)
    edge_viewport = (0.5, 0.0, 1.0, 1.0)

    original_renderer = vtkRenderer(viewport=original_viewport, background=colors.GetColor3d('SlateGray'))
    edge_renderer = vtkRenderer(viewport=edge_viewport, background=colors.GetColor3d('LightSlateGray'))

    render_window = vtkRenderWindow(multi_samples=0, size=(600, 300), window_name='CannyEdgeDetector')
    render_window.AddRenderer(original_renderer)
    render_window.AddRenderer(edge_renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    image_in = vtkPNGReader(file_name=fp)

    image_actor = vtkImageActor(input_data=image_in.output)

    original_renderer.AddActor(image_actor)

    il = vtkImageLuminance()

    ic = vtkImageCast(output_scalar_type=ImageCast.OutputScalarType.VTK_FLOAT)

    # Smooth the image.
    gs = vtkImageGaussianSmooth(dimensionality=2, radius_factors=(1, 1, 0))

    # Gradient the image.
    img_gradient = vtkImageGradient(dimensionality=2)

    img_magnitude = vtkImageMagnitude()
    image_in >> il >> ic >> gs >> img_gradient >> img_magnitude

    # Non maximum suppression.
    non_max = vtkImageNonMaximumSuppression(dimensionality=2,
                                            input_data=img_magnitude.output,
                                            vector_input_data=img_gradient.update().output)

    pad = vtkImageConstantPad(output_number_of_scalar_components=3, constant=0)
    image_in >> il >> ic >> gs >> img_gradient >> pad
    pad.update()

    i2sp1 = vtkImageToStructuredPoints(vector_input_data=pad.output)

    # Link edgles.
    img_link = vtkLinkEdgels(gradient_threshold=2)

    # Threshold links.
    threshold_edges = vtkThreshold(threshold_function=vtkThreshold.THRESHOLD_UPPER, upper_threshold=10,
                                   all_scalars=False)

    gf = vtkGeometryFilter()
    non_max >> i2sp1 >> img_link >> threshold_edges >> gf

    i2sp = vtkImageToStructuredPoints(vector_input_data=pad.output)
    image_in >> il >> ic >> gs >> img_gradient >> img_magnitude >> i2sp

    # Subpixel them.
    spe = vtkSubPixelPositionEdgels(grad_maps_data=i2sp.structured_points_output)
    gf >> spe
    i2sp.update()

    strip = vtkStripper()

    dsm = vtkPolyDataMapper(scalar_visibility=False)
    spe >> strip >> dsm

    plane_actor = vtkActor(mapper=dsm)
    plane_actor.property.ambient = 1.0
    plane_actor.property.diffuse = 0.0
    plane_actor.property.color = colors.GetColor3d('GhostWhite')

    # Add the actors to the renderer, set the background and size.
    edge_renderer.AddActor(plane_actor)

    # Render the image.
    interactor.Initialize()
    render_window.Render()
    render_window.Render()

    interactor.Start()

@dataclass(frozen=True)
class ImageCast:
    @dataclass(frozen=True)
    class OutputScalarType:
        VTK_CHAR: int = 2
        VTK_UNSIGNED_CHAR: int = 3
        VTK_SHORT: int = 4
        VTK_UNSIGNED_SHORT: int = 5
        VTK_INT: int = 6
        VTK_UNSIGNED_INT: int = 7
        VTK_LONG: int = 8
        VTK_UNSIGNED_LONG: int = 9
        VTK_FLOAT: int = 10
        VTK_DOUBLE: int = 11

if __name__ == '__main__':
    main()
```
