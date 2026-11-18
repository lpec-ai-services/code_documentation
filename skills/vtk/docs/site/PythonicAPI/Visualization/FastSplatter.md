<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/FastSplatter/ -->

# FastSplatter

Repository source: [FastSplatter](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/FastSplatter.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestFastSplatter.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestFastSplatter.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/FastSplatter/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**FastSplatter.py**

```python
# !/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_FLOAT,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkImageData,
    vtkPolyData
)
from vtkmodules.vtkImagingCore import vtkImageShiftScale
from vtkmodules.vtkImagingHybrid import vtkFastSplatter
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindowInteractor
)

def main():
    colors = vtkNamedColors()

    # For the purposes of this example we'll build the splat image by hand.

    splat_image_size = 100
    splat_image = vtkImageData(dimensions=(splat_image_size, splat_image_size, 1))
    splat_image.AllocateScalars(VTK_FLOAT, 1)

    for i in range(0, splat_image_size):
        for j in range(0, splat_image_size):
            x_coord = 1 - abs((i - splat_image_size / 2) / (splat_image_size / 2.0))
            y_coord = 1 - abs((j - splat_image_size / 2) / (splat_image_size / 2.0))

            splat_image.SetScalarComponentFromDouble(i, j, 0, 0, x_coord * y_coord)

    points = vtkPoints(number_of_points=5)

    points.SetPoint(0, (0, 0, 0))
    points.SetPoint(1, (1, 1, 0))
    points.SetPoint(2, (-1, 1, 0))
    points.SetPoint(3, (1, -1, 0))
    points.SetPoint(4, (-1, -1, 0))

    splat_points = vtkPolyData(points=points)

    splatter = vtkFastSplatter(output_dimensions=(2 * splat_image_size, 2 * splat_image_size, 1))
    splat_points >> select_ports(0, splatter)
    splat_image >> select_ports(1, splatter)

    # The image viewers and writers are only happy with unsigned char
    # images.  This will convert the floats into that format.
    result_scale = vtkImageShiftScale(shift=0, scale=255)
    result_scale.SetOutputScalarTypeToUnsignedChar()
    splatter >> result_scale

    # Set up a viewer for the image.  vtkImageViewer and
    # vtkImageViewer2 are convenient wrappers around vtkActor2D,
    # vtkImageMapper, vtkRenderer, and vtkRenderWindow.  All you need
    # to supply is the interactor and hooray, Bob's your uncle.
    image_viewer = vtkImageViewer2(color_level=127, color_window=255, input_data=result_scale.update().output)

    iren = vtkRenderWindowInteractor()
    image_viewer.SetupInteractor(iren)

    image_viewer.Render()
    image_viewer.GetRenderer().background = colors.GetColor3d('SlateGray')
    image_viewer.GetRenderer().ResetCamera()

    image_viewer.GetRenderWindow().window_name = 'FastSplatter'

    image_viewer.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
