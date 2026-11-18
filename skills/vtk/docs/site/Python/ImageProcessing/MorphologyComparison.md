<!-- source: https://examples.vtk.org/site/Python/ImageProcessing/MorphologyComparison/ -->

# MorphologyComparison

Repository source: [MorphologyComparison](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImageProcessing/MorphologyComparison.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestMorphologyComparison.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestMorphologyComparison.png?raw=true target=)

### Description

Although preprocessing can do a lot to improve segmentation results, postprocessing can also be useful. Morphological filters, which operate on binary or discrete images, can be useful for manipulating the shape of the segmented regions. In this brief discussion we will only consider operations that use circular footprints, even though these morphological filters can be defined much more generally.

Erosion is implemented by removing pixels within a specified distance of a border. For each pixel not in the segmented region, all the neighbors in a circular region around the pixels are turned off. This erosion filter shrinks the segmented region and small isolated regions disappear.

The opposite of erosion is dilation. This filter grows the area of segmented regions. Small holes in the segmented region are completely closed. Any pixel not in the segmented region but near the region is turned on.

Dilation and erosion are dual filters with nearly identical implementations. Dilating the “on” pixels is equivalent to eroding “off” pixels in a binary image. Holes in the map disappear. However, dilation alone also grows the boundaries of the segmented regions. When dilation is followed by erosion in a closing operation, small holes are removed; however, the boundary of the segmented regions remain in the same general location.

Opening is the dual of closing. Opening removes small islands of pixels. It is implemented with an initial erosion, followed by a dilation.

Connectivity filters can also remove small regions without affecting the remaining boundaries of segmented regions. This set of filters separate the segmented pixels into equivalence classes based on a neighbor relation. Two pixels belong to the same class if they are touching. There are two common neighbor relations in two-dimensional images: four connectivity considers pixels neighbors if they are edge neighbors, and eight connectivity considers pixels neighbors if pixels share any vertex.

This example demonstrates various binary filters that can alter the shape of segmented regions. From left to right, top to bottom: original image, connectivity, erosion, dilation, opening, closing.

Info

See [this figure](../../VTKBook/10Chapter10.md#Figure%2010-14) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/MorphologyComparison/)), ([PythonicAPI](../../PythonicAPI/ImageProcessing/MorphologyComparison.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MorphologyComparison.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingMorphological import (
    vtkImageDilateErode3D,
    vtkImageSeedConnectivity
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    # colors = vtkNamedColors()

    fileName = get_program_parameters()

    # Read the image.
    readerFactory = vtkImageReader2Factory()
    reader = readerFactory.CreateImageReader2(fileName)
    reader.SetFileName(fileName)
    reader.Update()

    # Dilate
    dilate = vtkImageDilateErode3D()
    dilate.SetInputConnection(reader.GetOutputPort())
    dilate.SetDilateValue(0)
    dilate.SetErodeValue(255)
    dilate.SetKernelSize(31, 31, 1)

    # Erode
    erode = vtkImageDilateErode3D()
    erode.SetInputConnection(reader.GetOutputPort())
    erode.SetDilateValue(255)
    erode.SetErodeValue(0)
    erode.SetKernelSize(31, 31, 1)

    # Opening - dilate then erode.
    dilate1 = vtkImageDilateErode3D()
    dilate1.SetInputConnection(reader.GetOutputPort())
    dilate1.SetDilateValue(0)
    dilate1.SetErodeValue(255)
    dilate1.SetKernelSize(31, 31, 1)

    erode1 = vtkImageDilateErode3D()
    erode1.SetInputConnection(dilate1.GetOutputPort())
    erode1.SetDilateValue(255)
    erode1.SetErodeValue(0)
    erode1.SetKernelSize(31, 31, 1)

    # Closing - erode then dilate.
    erode2 = vtkImageDilateErode3D()
    erode2.SetInputConnection(reader.GetOutputPort())
    erode2.SetDilateValue(255)
    erode2.SetErodeValue(0)
    erode2.SetKernelSize(31, 31, 1)

    dilate2 = vtkImageDilateErode3D()
    dilate2.SetInputConnection(erode2.GetOutputPort())
    dilate2.SetDilateValue(0)
    dilate2.SetErodeValue(255)
    dilate2.SetKernelSize(31, 31, 1)

    # Connectivity
    con = vtkImageSeedConnectivity()
    con.SetInputConnection(reader.GetOutputPort())
    con.AddSeed(300, 200)
    con.SetInputConnectValue(0)
    con.SetOutputConnectedValue(0)
    con.SetOutputUnconnectedValue(255)

    # Actors
    originalActor = vtkImageActor()
    originalActor.GetMapper().SetInputConnection(reader.GetOutputPort())
    originalActor.GetProperty().SetInterpolationTypeToNearest()

    connectedActor = vtkImageActor()
    connectedActor.GetMapper().SetInputConnection(con.GetOutputPort())
    connectedActor.GetProperty().SetInterpolationTypeToNearest()

    erodeActor = vtkImageActor()
    erodeActor.GetMapper().SetInputConnection(erode.GetOutputPort())
    erodeActor.GetProperty().SetInterpolationTypeToNearest()

    dilateActor = vtkImageActor()
    dilateActor.GetMapper().SetInputConnection(dilate.GetOutputPort())
    dilateActor.GetProperty().SetInterpolationTypeToNearest()

    openingActor = vtkImageActor()
    openingActor.GetMapper().SetInputConnection(dilate2.GetOutputPort())
    openingActor.GetProperty().SetInterpolationTypeToNearest()

    closingActor = vtkImageActor()
    closingActor.GetMapper().SetInputConnection(erode1.GetOutputPort())
    closingActor.GetProperty().SetInterpolationTypeToNearest()

    # Setup renderers
    originalRenderer = vtkRenderer()
    originalRenderer.AddActor(originalActor)
    connectedRenderer = vtkRenderer()
    connectedRenderer.AddActor(connectedActor)
    dilateRenderer = vtkRenderer()
    dilateRenderer.AddActor(dilateActor)
    erodeRenderer = vtkRenderer()
    erodeRenderer.AddActor(erodeActor)
    closingRenderer = vtkRenderer()
    closingRenderer.AddActor(closingActor)
    openingRenderer = vtkRenderer()
    openingRenderer.AddActor(openingActor)

    renderers = list()
    renderers.append(originalRenderer)
    renderers.append(connectedRenderer)
    renderers.append(erodeRenderer)
    renderers.append(dilateRenderer)
    renderers.append(openingRenderer)
    renderers.append(closingRenderer)

    # Setup viewports for the renderers
    rendererSize = 300
    xGridDimensions = 2
    yGridDimensions = 3

    renderWindow = vtkRenderWindow()
    renderWindow.SetSize(
        rendererSize * xGridDimensions, rendererSize * yGridDimensions)
    for row in range(0, yGridDimensions):
        for col in range(xGridDimensions):
            index = row * xGridDimensions + col
            # (xmin, ymin, xmax, ymax)
            viewport = [float(col) / xGridDimensions, float(yGridDimensions - (row + 1)) / yGridDimensions,
                        float(col + 1) / xGridDimensions, float(yGridDimensions - row) / yGridDimensions]
            renderers[index].SetViewport(viewport)
            renderWindow.AddRenderer(renderers[index])
    renderWindow.SetWindowName('MorphologyComparison')

    renderWindowInteractor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()

    renderWindowInteractor.SetInteractorStyle(style)
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # The renderers share one camera.
    renderWindow.Render()
    renderers[0].GetActiveCamera().Dolly(1.5)
    renderers[0].ResetCameraClippingRange()

    for r in range(1, len(renderers)):
        renderers[r].SetActiveCamera(renderers[0].GetActiveCamera())
    renderWindowInteractor.Initialize()
    renderWindowInteractor.Start()

def get_program_parameters():
    import argparse
    description = 'Demonstrate various binary filters that can alter the shape of segmented regions.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='binary.pgm.')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
