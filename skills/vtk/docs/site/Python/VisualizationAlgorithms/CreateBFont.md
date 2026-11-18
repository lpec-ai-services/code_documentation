<!-- source: https://examples.vtk.org/site/Python/VisualizationAlgorithms/CreateBFont/ -->

# CreateBFont

Repository source: [CreateBFont](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/VisualizationAlgorithms/CreateBFont.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestCreateBFont.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/VisualizationAlgorithms/TestCreateBFont.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/VisualizationAlgorithms/CreateBFont/)), ([PythonicAPI](../../PythonicAPI/VisualizationAlgorithms/CreateBFont.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CreateBFont.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkClipPolyData
from vtkmodules.vtkFiltersGeometry import vtkImageDataGeometryFilter
from vtkmodules.vtkIOImage import vtkPNMReader
from vtkmodules.vtkImagingGeneral import vtkImageGaussianSmooth
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    fileName = get_program_parameters()

    # Now create the RenderWindow, Renderer and Interactor.
    #
    ren1 = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    imageIn = vtkPNMReader()
    imageIn.SetFileName(fileName)

    gaussian = vtkImageGaussianSmooth()
    gaussian.SetStandardDeviations(2, 2)
    gaussian.SetDimensionality(2)
    gaussian.SetRadiusFactors(1, 1)
    gaussian.SetInputConnection(imageIn.GetOutputPort())

    geometry = vtkImageDataGeometryFilter()
    geometry.SetInputConnection(gaussian.GetOutputPort())

    aClipper = vtkClipPolyData()
    aClipper.SetInputConnection(geometry.GetOutputPort())
    aClipper.SetValue(127.5)
    aClipper.GenerateClipScalarsOff()
    aClipper.InsideOutOn()
    aClipper.GetOutput().GetPointData().CopyScalarsOff()
    aClipper.Update()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(aClipper.GetOutputPort())
    mapper.ScalarVisibilityOff()

    letter = vtkActor()
    letter.SetMapper(mapper)

    ren1.AddActor(letter)
    letter.GetProperty().SetDiffuseColor(colors.GetColor3d("LampBlack"))
    letter.GetProperty().SetRepresentationToWireframe()

    ren1.SetBackground(colors.GetColor3d("WhiteSmoke"))
    ren1.ResetCamera()
    ren1.GetActiveCamera().Dolly(1.2)
    ren1.ResetCameraClippingRange()

    renWin.SetSize(640, 480)
    renWin.SetWindowName('CreateBFont')

    # Render the image.
    #
    renWin.Render()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'A scanned image clipped with a scalar value.'
    epilogue = '''
    A scanned image clipped with a scalar value of 1/2 its maximum intensity
     produces a mixture of quadrilaterals and triangles.
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='B.pgm.')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
