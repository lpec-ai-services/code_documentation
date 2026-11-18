<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ImageToPolyDataFilter/ -->

# ImageToPolyDataFilter

Repository source: [ImageToPolyDataFilter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ImageToPolyDataFilter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageToPolyDataFilter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestImageToPolyDataFilter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ImageToPolyDataFilter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageToPolyDataFilter.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkTriangleFilter
from vtkmodules.vtkFiltersHybrid import vtkImageToPolyDataFilter
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingColor import vtkImageQuantizeRGBToIndex
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'ImageToPolyDataFilter.'
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

    # Read the image.
    reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
    reader.file_name = fp

    # Alternatively, use vtkPNGReader.
    # reader = vtkPNGReader(file_name = fp)

    quant = vtkImageQuantizeRGBToIndex(number_of_colors=16)

    i2pd = vtkImageToPolyDataFilter(lookup_table=quant.lookup_table, error=0,
                                    decimation=True, decimation_error=0.0,
                                    sub_image_size=25)
    i2pd.SetColorModeToLUT()
    i2pd.SetOutputStyleToPolygonalize()

    # Need a triangle filter because the polygons are complex and concave.
    tf = vtkTriangleFilter()

    mapper = vtkPolyDataMapper()
    reader >> quant >> i2pd >> tf >> mapper

    actor = vtkActor(mapper=mapper)
    actor.property.SetRepresentationToWireframe()

    # Visualize
    renderer = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    render_window = vtkRenderWindow(size=(300, 250), window_name='ImageToPolyDataFilter')
    render_window.AddRenderer(renderer)
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    renderer.AddActor(actor)

    render_window.Render()
    interactor.Initialize()
    interactor.Start()

if __name__ == '__main__':
    main()
```
