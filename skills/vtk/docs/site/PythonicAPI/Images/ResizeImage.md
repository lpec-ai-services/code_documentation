<!-- source: https://examples.vtk.org/site/PythonicAPI/Images/ResizeImage/ -->

# ResizeImage

Repository source: [ResizeImage](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Images/ResizeImage.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestResizeImage.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Images/TestResizeImage.png?raw=true target=)

### Description

Resize an image using a sinc interpolator. Without command line arguments, the example resizes a synthetic image. An image file can be passed on the command lines. The new dimensions can also be passed as well as an integer specifying the window for sinc interpolator. See [vtkImageSincInterpolator](https://www.vtk.org/doc/nightly/html/classvtkImageSincInterpolator.html) for details. A -1 turns off interpolation.

Several window functions are provided. See [this article](https://en.wikipedia.org/wiki/Window_function) for a description of window functions.

[vtkImageResize](https://www.vtk.org/doc/nightly/html/classvtkImageResize.html) maintains the physical size of the image.

Note

This example was inspired by a question asked by *Qiang Wang*.

Seealso

The paper ["Some windows with very good sidelobe behavior"](http://mwlab.pmo.ac.cn/~lzh/about_work/dspfftpaper/Some_Windows_with_Very_Good_Sidelobe_Behavior.pdf) describes the windows implemented in [vtkImageSincInterpolator](https://www.vtk.org/doc/nightly/html/classvtkImageSincInterpolator.html).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Images/ResizeImage/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ResizeImage.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import (
    vtkImageResize,
    vtkImageSincInterpolator
)
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    def to_int_range(x):
        try:
            x = int(x)
        except ValueError:
            raise argparse.ArgumentTypeError(f'This value: {x} is not a integer literal')
        if x < -1 or x > 10:
            raise argparse.ArgumentTypeError(f'The absolute value of {x} must be in the range [-1...10]')
        return x

    import argparse
    description = 'ResizeImage.'
    epilogue = '''
    Try: -f ../../../src/Testing/Data/Gourds2.jpg -sx 1280 -sy 1024 -w 5
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--file_name', default=None, help='The image file name to use e.g. Gourds2.jpg.')
    parser.add_argument('-sx', default=200, type=int, help='Size in the X-direction')
    parser.add_argument('-sy', default=200, type=int, help='Size in the Y-direction')
    parser.add_argument('-w', default=-1, type=to_int_range,
                        help='The  sinc interpolator to use. -1 turns off interpolation.')
    args = parser.parse_args()
    return args.file_name, args.sx, args.sy, args.w

def main():
    new_size = [0, 0, 1]

    fn, new_size[0], new_size[1], window_function = get_program_parameters()
    if fn:
        fp = Path(fn)
        file_check = True
        if not fp.is_file():
            print(f'Missing image file: {fp}.')
            file_check = False
        if not file_check:
            return
    else:
        fp = None

    colors = vtkNamedColors()

    if fp:
        # Read texture file.
        reader: vtkImageReader2Factory = vtkImageReader2Factory().CreateImageReader2(str(fp))
        reader.file_name = fp
        image_data = reader.update().output
    else:
        draw_color1 = colors.GetColor3ub('Gray')
        draw_color2 = colors.GetColor3ub('Aquamarine')
        draw_color3 = colors.GetColor3ub('Violet')

        canvas_source = vtkImageCanvasSource2D(extent=(0, 100, 0, 100, 0, 0), number_of_scalar_components=3)
        canvas_source.draw_color = tuple(draw_color1)
        canvas_source.FillBox(0, 100, 0, 100)
        canvas_source.draw_color = tuple(draw_color2)
        canvas_source.FillTriangle(10, 10, 25, 10, 25, 25)
        canvas_source.draw_color = tuple(draw_color3)
        canvas_source.FillTube(75, 75, 0, 75, 5.0)
        image_data = canvas_source.update().output

    interpolator = vtkImageSincInterpolator(use_window_parameter=True)
    if 0 <= window_function <= 10:
        interpolator.window_function = window_function

    resize = vtkImageResize(input_data=image_data, output_dimensions=new_size,
                            interpolator=interpolator, interpolate=True)
    resize.update()

    print(f'Original dimensions: {image_data.dimensions}')
    print(f'Resized dimensions:  {resize.output.dimensions}')
    if window_function < 0:
        resize.interpolate = False
        print(f'Using nearest neighbor interpolation.')
    else:
        print(f'Using window function : {interpolator.GetWindowFunctionAsString()}')

    # Create an image actor to display the image
    image_actor = vtkImageActor()
    resize >> image_actor.mapper
    image_actor.InterpolateOff()

    # Setup renderer
    renderer = vtkRenderer(background=colors.GetColor3d('Burlywood'))
    renderer.AddActor(image_actor)
    renderer.ResetCamera()
    if fp:
        renderer.active_camera.Dolly(5.0)
    else:
        renderer.active_camera.Dolly(1.0)
    renderer.ResetCameraClippingRange()

    # Setup render window
    render_window = vtkRenderWindow(size=(1280, 1024), window_name='ResizeImage')
    render_window.AddRenderer(renderer)

    # Setup render window interactor
    render_window_interactor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()
    render_window_interactor.interactor_style = style
    render_window_interactor.render_window = render_window

    # Render and start interaction
    render_window.Render()
    render_window_interactor.Initialize()

    render_window_interactor.Start()

if __name__ == '__main__':
    main()
```
