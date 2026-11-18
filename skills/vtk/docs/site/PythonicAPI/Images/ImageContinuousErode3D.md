<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageContinuousErode3D/ -->

# ImageContinuousErode3D

Repository source: [ImageContinuousErode3D](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageContinuousErode3D.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageContinuousErode3D.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageContinuousErode3D.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageContinuousErode3D/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageContinuousErode3D.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingMorphological import vtkImageContinuousErode3D
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'ImageContinuousErode3D.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None, help='The image file name to use e.g. Gourds.png.')
    args = parser.parse_args()
    return args.file_name

def main():
    fn = get_program_parameters()
    fp = None
    if fn:
        fp = Path(fn)
        file_check = True
        if not fp.is_file():
            print(f'Missing image file: {fp}.')
            file_check = False
        if not file_check:
            return

    colors = vtkNamedColors()

    image = vtkImageData()

    if not fp:
        draw_color1 = colors.GetColor3ub('Black')
        draw_color2 = colors.GetColor3ub('White')

        # Create an image.
        source = vtkImageCanvasSource2D(extent=(0, 200, 0, 200, 0, 0))
        source.SetScalarTypeToUnsignedChar()
        source.draw_color = tuple(draw_color1)
        source.FillBox(0, 200, 0, 200)
        source.draw_color = tuple(draw_color2)
        source.FillBox(100, 150, 100, 150)
        source.update()
        image.ShallowCopy(source.output)
    else:
        reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
        reader.file_name = fp
        reader.update()
        image.ShallowCopy(reader.output)

    original_mapper = vtkDataSetMapper(input_data=image)
    original_actor = vtkActor(mapper=original_mapper)

    erode_filter = vtkImageContinuousErode3D(input_data=image, kernel_size=(10, 10, 1))
    erode_filter.update()
    eroded_mapper = vtkDataSetMapper()
    erode_filter >> eroded_mapper
    eroded_actor = vtkActor(mapper=eroded_mapper)

    # Visualize
    left_viewport = (0.0, 0.0, 0.5, 1.0)
    right_viewport = (0.5, 0.0, 1.0, 1.0)

    render_window = vtkRenderWindow(size=(600, 300), window_name='ImageContinuousErode3D')

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    left_renderer = vtkRenderer(viewport=left_viewport, background=colors.GetColor3d('Sienna'))
    render_window.AddRenderer(left_renderer)

    right_renderer = vtkRenderer(viewport=right_viewport, background=colors.GetColor3d('RoyalBlue'))
    render_window.AddRenderer(right_renderer)

    left_renderer.AddActor(original_actor)
    right_renderer.AddActor(eroded_actor)

    left_renderer.ResetCamera()
    right_renderer.active_camera = left_renderer.active_camera

    render_window.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
```
