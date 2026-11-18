<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/ImageTracerWidgetInsideContour/ -->

# ImageTracerWidgetInsideContour

Repository source: [ImageTracerWidgetInsideContour](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/ImageTracerWidgetInsideContour.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImageTracerWidgetInsideContour.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestImageTracerWidgetInsideContour.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/ImageTracerWidgetInsideContour/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ImageTracerWidgetInsideContour.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkCallbackCommand
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkImagingStatistics import vtkImageAccumulate
from vtkmodules.vtkImagingStencil import (
    vtkImageStencilToImage,
    vtkPolyDataToImageStencil,
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkInteractionWidgets import vtkImageTracerWidget
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    image = create_image1()

    actor = vtkImageActor()
    actor.mapper.input_data = image

    renderer = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    renderer.AddActor(actor)

    render_window = vtkRenderWindow(window_name='ImageTracerWidgetInsideContour')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window
    style = vtkInteractorStyleImage()
    interactor.interactor_style = style

    tracer = vtkImageTracerWidget()
    tracer.line_property.line_width = 5
    tracer.interactor = interactor
    tracer.view_prop = actor
    tracer.auto_close = True
    render_window.Render()

    # The observer must be added BEFORE the On() call.
    callback = AffineCallback(image, tracer)
    tracer.AddObserver(vtkCallbackCommand.EndInteractionEvent, callback)

    tracer.On()
    interactor.Start()

class AffineCallback:
    def __init__(self, image, tracer_widget):
        self.image = image
        self.tracer_widget = tracer_widget

    def __call__(self, caller, ev):
        path = vtkPolyData()

        if not self.tracer_widget.IsClosed():
            print(f'Path not closed!')
            return

        self.tracer_widget.GetPath(path)
        print(f'There are {path.number_of_points} points in the path.')

        poly_data_to_image_stencil = vtkPolyDataToImageStencil(tolerance=0, input_data=path,
                                                               output_origin=self.image.origin,
                                                               output_spacing=self.image.spacing,
                                                               output_whole_extent=self.image.extent)
        poly_data_to_image_stencil.update()

        image_stencil_to_image = vtkImageStencilToImage(inside_value=255)
        poly_data_to_image_stencil >> image_stencil_to_image
        image_stencil_to_image.update()

        image_accumulate = vtkImageAccumulate(input_data=self.image,
                                              stencil_data=poly_data_to_image_stencil.output)
        image_accumulate.update()
        print(f'Voxel count: {image_accumulate.voxel_count}')

def create_image1():
    colors = vtkNamedColors()

    draw_color1 = colors.GetColor3ub('DarkGray')

    canvas_source = vtkImageCanvasSource2D(extent=(0, 20, 0, 50, 0, 0), number_of_scalar_components=1)
    canvas_source.SetScalarTypeToUnsignedChar()
    canvas_source.draw_color = tuple(draw_color1)
    canvas_source.FillBox(0, 20, 0, 50)

    # image = vtkImageData()
    image = canvas_source.update().output
    return image

if __name__ == '__main__':
    main()
```
