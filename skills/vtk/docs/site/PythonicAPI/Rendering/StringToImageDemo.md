<!-- source: https://examples.vtk.org/site/PythonicAPI/Rendering/StringToImageDemo/ -->

# StringToImageDemo

Repository source: [StringToImageDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Rendering/StringToImageDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestStringToImageDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Rendering/TestStringToImageDemo.png?raw=true target=)

### Description

This example demonstrates the use of [vtkFreeTypeTools](https://www.vtk.org/doc/nightly/html/classvtkFreeTypeTools.html) to populate an image with multiple strings converted into images. The final image is created using [vtkImageBlend](https://www.vtk.org/doc/nightly/html/classvtkImageBlend.html) to blend each string image into the final image. If a string image does not fit in the final image or overlaps with an image in final, that sting image is skipped.

This example differs from the C++ example in that [vtkImageIterator](https://www.vtk.org/doc/nightly/html/classvtkImageIterator.html) cannot be used since it is designed for use for C++. Accordingly, we implement the Separating Axis Theorem to determine if the rectangles corresponding to the text overlap.

See: [How to check intersection between 2 rotated rectangles?](https://stackoverflow.com/questions/10962379/how-to-check-intersection-between-2-rotated-rectangles)

Tfe final result differs slightly from the C++ example in that only 15 and not 19 images are rendered.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Rendering/StringToImageDemo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**StringToImageDemo.py**

```python
#!/usr/bin/env python3

import numpy as np

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkMinimalStandardRandomSequence
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkImagingCore import vtkImageBlend
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindowInteractor, vtkTextProperty
)
from vtkmodules.vtkRenderingFreeType import vtkFreeTypeTools

def get_program_parameters():
    import argparse
    description = 'Extract a surface from vtkPolyData points.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('text', nargs='?', default=None,
                        help='The optional text (enclosed in quotes) to convert to an image.')
    args = parser.parse_args()

    return args.text

def main():
    text = get_program_parameters()
    if text is None:
        text = 'Old Guys Rule'

    # Create a blank, black image
    drawing = vtkImageCanvasSource2D(number_of_scalar_components=3, extent=(0, 640, 0, 480, 0, 0), draw_color=(0, 0, 0))
    drawing.SetScalarTypeToUnsignedChar()
    drawing.FillBox(0, 629, 0, 479)

    # Create an image that will hold the final image.
    final = vtkImageBlend()
    drawing >> final
    final.opacity = 0, 1.0
    final.update()

    # Create an image of the string.
    dpi = 150
    free_type = vtkFreeTypeTools.GetInstance()
    free_type.ScaleToPowerTwoOff()

    # Set up a property for the strings containing fixed parameters.
    colors = vtkNamedColors()
    text_property = vtkTextProperty(color=colors.GetColor3d('Tomato'))
    text_property.SetVerticalJustificationToCentered()
    text_property.SetJustificationToCentered()

    random_sequence = vtkMinimalStandardRandomSequence()
    random_sequence.SetSeed(8775070)

    # For each string, create an image and see if it overlaps
    # with other images, if so, skip it.
    tried = 600
    accepted = 0
    count = 0
    valid_extents = list()
    overlap = 0
    for i in range(0, tried):
        font_size = random_sequence.GetRangeValue(6, 42)
        random_sequence.Next()
        text_property.orientation = random_sequence.GetRangeValue(-90, 90)
        random_sequence.Next()
        text_property.font_size = int(font_size)

        text_image = vtkImageData()
        free_type.RenderString(text_property, text, dpi, text_image)

        # Set the extent of the text image.
        bb = [0] * 4
        free_type.GetBoundingBox(text_property, text, dpi, bb)
        offset_x = int(random_sequence.GetRangeValue(0, 640))
        random_sequence.Next()
        offset_y = int(random_sequence.GetRangeValue(0, 480))
        random_sequence.Next()
        # Make sure the text image will fit on the final image.
        good = True
        if offset_x + bb[1] - bb[0] < 639 and offset_y + bb[3] - bb[2] < 479:
            count += 1
            extent = (offset_x, offset_x + bb[1] - bb[0], offset_y, offset_y + bb[3] - bb[2], 0, 0)
            text_image.SetExtent(extent)
            image = vtkImageData()
            final.update()
            # Convert the valid extent to a series of points ordered in a
            # counter-clockwise  direction. This corresponds to the rectangle.
            a = np.array([[extent[0], extent[2]], [extent[1], extent[2]],
                          [extent[1], extent[2]], [extent[1], extent[3]],
                          [extent[1], extent[3]], [extent[0], extent[3]],
                          [extent[0], extent[3]], [extent[0], extent[2]]])

            if i > 1:
                for ext in valid_extents:
                    # Convert the valid extent to a series of points ordered in a
                    # counter-clockwise  direction. This corresponds to the rectangle.
                    b = np.array([[ext[0], ext[2]], [ext[1], ext[2]],
                                  [ext[1], ext[2]], [ext[1], ext[3]],
                                  [ext[1], ext[3]], [ext[0], ext[3]],
                                  [ext[0], ext[3]], [ext[0], ext[2]]])
                    # Do the rectangles intersect?
                    res = do_polygons_intersect(a, b)
                    good = not res and good
                    if res:
                        overlap += 1
                        break
                if good:
                    accepted += 1
                    image.DeepCopy(text_image)
                    final.AddInputData(image)
                    final.opacity = (i + 1, 1.0)  # text: 100% opaque
                    final.Update()
                    valid_extents.append(extent)
            else:
                # The first extent is always valid.
                accepted += 1
                image.DeepCopy(text_image)
                final.AddInputData(image)
                final.opacity = (i + 1, 1.0)  # text: 100% opaque
                final.Update()
                valid_extents.append(extent)

    print(f'Tried {tried}, but only accepted {accepted}.')

    # Display the result.
    interactor = vtkRenderWindowInteractor()

    image_viewer = vtkImageViewer2(size=(640, 512), input_data=final.output)
    image_viewer.SetupInteractor(interactor)
    image_viewer.GetRenderer().background = colors.GetColor3d('Wheat')
    image_viewer.GetRenderer().ResetCamera()
    image_viewer.GetRenderWindow().window_name = 'StringToImageDemo'

    camera = image_viewer.GetRenderer().active_camera
    camera.ParallelProjectionOn()
    camera.SetParallelScale(640 * 0.4)
    image_viewer.GetRenderWindow().Render()
    interactor.Initialize()
    interactor.Start()

def do_polygons_intersect(a, b):
    """
    A function to determine whether there is an intersection
     between the two polygons described by the lists of vertices.

    Uses the Separating Axis Theorem.

    See: [How to check intersection between 2 rotated rectangles?](https://stackoverflow.com/questions/10962379/how-to-check-intersection-between-2-rotated-rectangles)

    :param a: The ndarray of connected points [[x_1, y_1], [x_2, y_2],...] that form a closed polygon
    :param b: The ndarray of connected points [[x_1, y_1], [x_2, y_2],...] that form a closed polygon
    :return: True if there is any intersection between the 2 polygons, False otherwise
    """

    polygons = [a, b]

    for i in range(len(polygons)):

        # For each polygon, look at each edge of the polygon,
        # and determine if it separates the two shapes.
        polygon = polygons[i]
        for i1 in range(len(polygon)):

            # Grab 2 vertices to create an edge.
            i2 = (i1 + 1) % len(polygon)
            p1 = polygon[i1]
            p2 = polygon[i2]

            # Find the line perpendicular to this edge.
            normal = {'x': p2[1] - p1[1], 'y': p1[0] - p2[0]}

            min_a, max_a = None, None
            # For each vertex in the first shape, project it onto the line
            # perpendicular to the edge and keep track of the min and max
            # of these values.
            for j in range(len(a)):
                projected = normal['x'] * a[j][0] + normal['y'] * a[j][1]
                if (min_a is None) or (projected < min_a):
                    min_a = projected

                if (max_a is None) or (projected > max_a):
                    max_a = projected

            # For each vertex in the second shape, project it onto the line
            # perpendicular to the edge and keep track of the min and max
            # of these values.
            min_b, max_b = None, None
            for j in range(len(b)):
                projected = normal['x'] * b[j][0] + normal['y'] * b[j][1]
                if (min_b is None) or (projected < min_b):
                    min_b = projected
                if (max_b is None) or (projected > max_b):
                    max_b = projected

            # If there is no overlap between the projections, the edge we are
            # looking at separates the two polygons, and we know there is no overlap.
            if (max_a < min_b) or (max_b < min_a):
                # print('polygons don't intersect!')
                return False

    return True

if __name__ == '__main__':
    main()
```
