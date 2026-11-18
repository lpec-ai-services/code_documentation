<!-- source: https://examples.vtk.org/site/Python/Texture/TexturePlane/ -->

# TexturePlane

Repository source: [TexturePlane](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Texture/TexturePlane.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Texture/TestTexturePlane.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Texture/TestTexturePlane.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Texture/TexturePlane/)), ([PythonicAPI](../../PythonicAPI/Texture/TexturePlane.md)), ([Java](https://examples.vtk.org/site/Java/Texture/TexturePlane/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TexturePlane.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkPlaneSource
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTexture
)

def main():
    fileName = get_program_parameters()

    colors = vtkNamedColors()

    # Load in the texture map. A texture is any unsigned char image. If it
    # is not of this type, you will have to map it through a lookup table
    # or by using vtkImageShiftScale.
    #
    readerFactory = vtkImageReader2Factory()
    textureFile = readerFactory.CreateImageReader2(fileName)
    textureFile.SetFileName(fileName)
    textureFile.Update()

    atext = vtkTexture()
    atext.SetInputConnection(textureFile.GetOutputPort())
    atext.InterpolateOn()

    # Create a plane source and actor. The vtkPlanesSource generates
    # texture coordinates.
    #
    plane = vtkPlaneSource()

    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(plane.GetOutputPort())

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    planeActor.SetTexture(atext)

    # Create the RenderWindow, Renderer and Interactor.
    renderer = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size.
    renderer.AddActor(planeActor)
    renderer.SetBackground(colors.GetColor3d('DarkSlateGray'))
    renWin.SetSize(640, 480)
    renWin.SetWindowName('TexturePlane')

    # render the image
    renWin.Render()

    renderer.ResetCamera()
    renderer.GetActiveCamera().Elevation(-30)
    renderer.GetActiveCamera().Roll(-20)
    renderer.ResetCameraClippingRange()
    renWin.Render()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'How to do basic texture mapping.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='masonry.bmp.')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
    main()
```
