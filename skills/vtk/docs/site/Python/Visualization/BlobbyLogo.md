<!-- source: https://examples.vtk.org/site/Python/Visualization/BlobbyLogo/ -->

# BlobbyLogo

Repository source: [BlobbyLogo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/BlobbyLogo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestBlobbyLogo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestBlobbyLogo.png?raw=true target=)

### Description

This is the blobby vtk logo described in chapter 12 of the VTK textbook. The example uses [vtkAppendPolyData](https://www.vtk.org/doc/nightly/html/classvtkAppendPolyData.html) to combine three [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). A [vtkImplicitModeller](https://www.vtk.org/doc/nightly/html/classvtkImplicitModeller.html) creates a [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html) of the distnaces from the polydata triangles. [vtkContourFilter](https://www.vtk.org/doc/nightly/html/classvtkContourFilter.html) extracts an isosurface representing an offset surface.

This examples uses the data `src/Testing/Data/v.vtk`, `src/Testing/Data/t.vtk` and `src/Testing/Data/k.vtk`.

Info

See [Figure 12-13](../../VTKBook/12Chapter12.md#Figure%2012-13) in [Chapter 12](../../VTKBook/12Chapter12.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/BlobbyLogo/)), ([Java](https://examples.vtk.org/site/Java/Visualization/BlobbyLogo/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BlobbyLogo.py**

```python
#!/usr/bin/env python

'''
'''

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import (
    vtkAppendPolyData,
    vtkContourFilter,
    vtkPolyDataNormals
)
from vtkmodules.vtkFiltersGeneral import vtkTransformPolyDataFilter
from vtkmodules.vtkFiltersHybrid import vtkImplicitModeller
from vtkmodules.vtkIOLegacy import vtkPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    fileName1, fileName2, fileName3 = get_program_parameters()
    aRenderer = vtkRenderer()
    aRenderWindow = vtkRenderWindow()
    aRenderWindow.AddRenderer(aRenderer)
    anInteractor = vtkRenderWindowInteractor()
    anInteractor.SetRenderWindow(aRenderWindow)
    aRenderWindow.SetSize(300, 300)
    aRenderWindow.SetWindowName('BlobbyLogo')

    # Read the geometry file containing the letter v.
    letterV = vtkPolyDataReader()
    letterV.SetFileName(fileName1)

    # Read the geometry file containing the letter t.
    letterT = vtkPolyDataReader()
    letterT.SetFileName(fileName2)

    # Read the geometry file containing the letter k.
    letterK = vtkPolyDataReader()
    letterK.SetFileName(fileName3)

    # Create a transform and transform filter for each letter.
    VTransform = vtkTransform()
    VTransformFilter = vtkTransformPolyDataFilter()
    VTransformFilter.SetInputConnection(letterV.GetOutputPort())
    VTransformFilter.SetTransform(VTransform)

    TTransform = vtkTransform()
    TTransformFilter = vtkTransformPolyDataFilter()
    TTransformFilter.SetInputConnection(letterT.GetOutputPort())
    TTransformFilter.SetTransform(TTransform)

    KTransform = vtkTransform()
    KTransformFilter = vtkTransformPolyDataFilter()
    KTransformFilter.SetInputConnection(letterK.GetOutputPort())
    KTransformFilter.SetTransform(KTransform)

    # Now append them all.
    appendAll = vtkAppendPolyData()
    appendAll.AddInputConnection(VTransformFilter.GetOutputPort())
    appendAll.AddInputConnection(TTransformFilter.GetOutputPort())
    appendAll.AddInputConnection(KTransformFilter.GetOutputPort())

    # Create normals.
    logoNormals = vtkPolyDataNormals()
    logoNormals.SetInputConnection(appendAll.GetOutputPort())
    logoNormals.SetFeatureAngle(60)

    # Map to rendering primitives.
    logoMapper = vtkPolyDataMapper()
    logoMapper.SetInputConnection(logoNormals.GetOutputPort())

    # Now an actor.
    logo = vtkActor()
    logo.SetMapper(logoMapper)

    # Now create an implicit model of the same letter.
    blobbyLogoImp = vtkImplicitModeller()
    blobbyLogoImp.SetInputConnection(appendAll.GetOutputPort())
    blobbyLogoImp.SetMaximumDistance(.075)
    blobbyLogoImp.SetSampleDimensions(64, 64, 64)
    blobbyLogoImp.SetAdjustDistance(0.05)

    # Extract an iso surface.
    blobbyLogoIso = vtkContourFilter()
    blobbyLogoIso.SetInputConnection(blobbyLogoImp.GetOutputPort())
    blobbyLogoIso.SetValue(1, 1.5)

    # Map to rendering primitives.
    blobbyLogoMapper = vtkPolyDataMapper()
    blobbyLogoMapper.SetInputConnection(blobbyLogoIso.GetOutputPort())
    blobbyLogoMapper.ScalarVisibilityOff()

    tomato = vtkProperty()
    tomato.SetDiffuseColor(colors.GetColor3d('tomato'))
    tomato.SetSpecular(.3)
    tomato.SetSpecularPower(20)

    banana = vtkProperty()
    banana.SetDiffuseColor(colors.GetColor3d('banana'))
    banana.SetDiffuse(.7)
    banana.SetSpecular(.4)
    banana.SetSpecularPower(20)

    # Now an actor.
    blobbyLogo = vtkActor()
    blobbyLogo.SetMapper(blobbyLogoMapper)
    blobbyLogo.SetProperty(banana)

    # Position the letters.

    VTransform.Translate(-16.0, 0.0, 12.5)
    VTransform.RotateY(40)

    KTransform.Translate(14.0, 0.0, 0.0)
    KTransform.RotateY(-40)

    # Move the polygonal letters to the front.
    logo.SetProperty(tomato)
    logo.SetPosition(0, 0, 6)

    aRenderer.AddActor(logo)
    aRenderer.AddActor(blobbyLogo)

    aRenderer.SetBackground(colors.GetColor3d('SlateGray'))

    aRenderWindow.Render()

    # Interact with the data.
    anInteractor.Start()

def get_program_parameters():
    import argparse
    description = 'Use implicit modeller to create the VTK logo.'
    epilogue = '''
   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename1', help='v.vtk')
    parser.add_argument('filename2', help='t.vtk')
    parser.add_argument('filename3', help='k.vtk')
    args = parser.parse_args()
    return args.filename1, args.filename2, args.filename3

if __name__ == '__main__':
    main()
```
