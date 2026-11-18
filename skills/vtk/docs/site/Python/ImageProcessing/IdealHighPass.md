<!-- source: https://examples.vtk.org/site/Python/ImageProcessing/IdealHighPass/ -->

# IdealHighPass

Repository source: [IdealHighPass](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImageProcessing/IdealHighPass.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestIdealHighPass.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/ImageProcessing/TestIdealHighPass.png?raw=true target=)

### Description

Low-pass and high-pass filtering become trivial in the frequency domain. A portion of the pixels are simply masked or attenuated. This example shows a high pass Butterworth filter that attenuates the frequency domain image with the function `out(i, j) = 1 / (1 + pow(CutOff/Freq(i,j), 2*Order))`.

The gradual attenuation of the filter is important. The ideal high-pass filter, shown in the same exaample, simply masks a set of pixels in the frequency domain. The abrupt transition causes a ringing effect in the spatial domain.

Info

See [this figure](../../VTKBook/10Chapter10.md#Figure%2010-11) in [Chapter 10](../../VTKBook/10Chapter10.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/ImageProcessing/IdealHighPass/)), ([PythonicAPI](../../PythonicAPI/ImageProcessing/IdealHighPass.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**IdealHighPass.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingColor import vtkImageMapToWindowLevelColors
from vtkmodules.vtkImagingCore import vtkImageExtractComponents
from vtkmodules.vtkImagingFourier import (
    vtkImageButterworthHighPass,
    vtkImageFFT,
    vtkImageIdealHighPass,
    vtkImageRFFT
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    fileName = get_program_parameters()

    # Read the image.
    readerFactory = vtkImageReader2Factory()
    reader = readerFactory.CreateImageReader2(fileName)
    reader.SetFileName(fileName)
    reader.Update()

    fft = vtkImageFFT()
    fft.SetInputConnection(reader.GetOutputPort())

    idealHighPass = vtkImageIdealHighPass()
    idealHighPass.SetInputConnection(fft.GetOutputPort())
    idealHighPass.SetXCutOff(0.1)
    idealHighPass.SetYCutOff(0.1)

    idealRfft = vtkImageRFFT()
    idealRfft.SetInputConnection(idealHighPass.GetOutputPort())

    idealReal = vtkImageExtractComponents()
    idealReal.SetInputConnection(idealRfft.GetOutputPort())
    idealReal.SetComponents(0)

    butterworthHighPass = vtkImageButterworthHighPass()
    butterworthHighPass.SetInputConnection(fft.GetOutputPort())
    butterworthHighPass.SetXCutOff(0.1)
    butterworthHighPass.SetYCutOff(0.1)

    butterworthRfft = vtkImageRFFT()
    butterworthRfft.SetInputConnection(butterworthHighPass.GetOutputPort())

    butterworthReal = vtkImageExtractComponents()
    butterworthReal.SetInputConnection(butterworthRfft.GetOutputPort())
    butterworthReal.SetComponents(0)

    # Create the actors.
    idealColor = vtkImageMapToWindowLevelColors()
    idealColor.SetWindow(500)
    idealColor.SetLevel(0)
    idealColor.SetInputConnection(idealReal.GetOutputPort())

    idealActor = vtkImageActor()
    idealActor.GetMapper().SetInputConnection(idealColor.GetOutputPort())
    idealActor.GetProperty().SetInterpolationTypeToNearest()

    butterworthColor = vtkImageMapToWindowLevelColors()
    butterworthColor.SetWindow(500)
    butterworthColor.SetLevel(0)
    butterworthColor.SetInputConnection(butterworthReal.GetOutputPort())

    butterworthActor = vtkImageActor()
    butterworthActor.GetMapper().SetInputConnection(butterworthColor.GetOutputPort())
    butterworthActor.GetProperty().SetInterpolationTypeToNearest()

    # Setup the renderers.
    idealRenderer = vtkRenderer()
    idealRenderer.SetViewport(0.0, 0.0, 0.5, 1.0)
    idealRenderer.AddActor(idealActor)
    idealRenderer.ResetCamera()
    idealRenderer.SetBackground(colors.GetColor3d("SlateGray"))

    butterworthRenderer = vtkRenderer()
    butterworthRenderer.SetViewport(0.5, 0.0, 1.0, 1.0)
    butterworthRenderer.AddActor(butterworthActor)
    butterworthRenderer.SetActiveCamera(idealRenderer.GetActiveCamera())
    butterworthRenderer.SetBackground(colors.GetColor3d("LightSlateGray"))

    renderWindow = vtkRenderWindow()
    renderWindow.SetSize(600, 300)
    renderWindow.SetWindowName('IdealHighPass')
    renderWindow.AddRenderer(idealRenderer)
    renderWindow.AddRenderer(butterworthRenderer)

    renderWindowInteractor = vtkRenderWindowInteractor()
    style = vtkInteractorStyleImage()

    renderWindowInteractor.SetInteractorStyle(style)

    renderWindowInteractor.SetRenderWindow(renderWindow)
    idealRenderer.GetActiveCamera().Dolly(1.4)
    idealRenderer.ResetCameraClippingRange()
    renderWindowInteractor.Initialize()

    renderWindowInteractor.Start()

def get_program_parameters():
    import argparse
    description = 'This figure shows two high-pass filters in the frequency domain.'
    epilogue = '''
    The Butterworth high-pass filter has a gradual attenuation that avoids ringing
     produced by the ideal high-pass filter with an abrupt transition.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='fullhead15.png.')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
