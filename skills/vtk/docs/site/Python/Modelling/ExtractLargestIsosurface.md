<!-- source: https://examples.vtk.org/site/Python/Modelling/ExtractLargestIsosurface/ -->

# ExtractLargestIsosurface

Repository source: [ExtractLargestIsosurface](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Modelling/ExtractLargestIsosurface.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Modelling/TestExtractLargestIsosurface.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Modelling/TestExtractLargestIsosurface.png?raw=true target=)

### Description

- Contributed by: Jinyoung Hwang

This example reads a structured points dataset stored in a .vtk file and constructs a 3D model using [vtkFlyingEdges3D](https://www.vtk.org/doc/nightly/html/classvtkFlyingEdges3D.html) or [vtkMarchingCubes](https://www.vtk.org/doc/nightly/html/classvtkMarchingCubes.html), [vtkPolyDataConnectivityFilter](https://www.vtk.org/doc/nightly/html/classvtkPolyDataConnectivityFilter.html) is used to extract the largest isosurface.

Data is available at:

1. test.vtk: <http://web.kaist.ac.kr/~hjy/test.vtk>
2. brainweb.img: <http://web.kaist.ac.kr/~hjy/brainweb.img>
3. brainweb.hdr: <http://web.kaist.ac.kr/~hjy/brainweb.hdr>

Second and third datasets can be downloaded from [BrainWeb](http://www.bic.mni.mcgill.ca/brainweb/), which is free of charge in use for a research. "test.vtk" was converted from "brainweb.img" using a program by Erik Vidholm (<http://www.cb.uu.se/~erik/vtk/rawToVTK.cpp>).

The examples expects 2 or 3 argments:

```python
 ExtractLargestIsosurface InputFilename Threshold (ExtractLargest)
```

if ExtractLargest is omitted or 1, the largest isosurface is extracted

if ExtractLargest is 0 (or -a in Python), all of the isosurfaces are extracted

Try

ExtractLargestIsosurface test.vtk 50

and compare the results to

ExtractLargestIsosurface test.vtk 50 0

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Modelling/ExtractLargestIsosurface/)), ([PythonicAPI](../../PythonicAPI/Modelling/ExtractLargestIsosurface.md)), ([CSharp](https://examples.vtk.org/site/CSharp/Modelling/ExtractLargestIsosurface/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**ExtractLargestIsosurface.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_VERSION_NUMBER,
    vtkVersion
)
from vtkmodules.vtkFiltersCore import (
    vtkFlyingEdges3D,
    vtkMarchingCubes,
    vtkPolyDataConnectivityFilter
)
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    # vtkFlyingEdges3D was introduced in VTK >= 8.2
    use_flying_edges = vtk_version_ok(8, 2, 0)

    colors = vtkNamedColors()

    colors.SetColor('SkinColor', [240, 184, 160, 255])
    colors.SetColor('BackfaceColor', [255, 229, 200, 255])
    colors.SetColor('BkgColor', [51, 77, 102, 255])

    file_name, threshold, largest_surface = get_program_parameters()

    # Load data
    reader = vtkStructuredPointsReader()
    reader.SetFileName(file_name)

    # Create a 3D model using flying edges or marching cubes
    if use_flying_edges:
        try:
            mc = vtkFlyingEdges3D()
        except AttributeError:
            mc = vtkMarchingCubes()
    else:
        mc = vtkMarchingCubes()

    mc.SetInputConnection(reader.GetOutputPort())
    mc.ComputeNormalsOn()
    mc.ComputeGradientsOn()
    mc.SetValue(0, threshold)  # second value acts as threshold

    # To remain largest region
    confilter = vtkPolyDataConnectivityFilter()
    confilter.SetInputConnection(mc.GetOutputPort())
    confilter.SetExtractionModeToLargestRegion()

    # Create a mapper
    mapper = vtkPolyDataMapper()
    if largest_surface:
        mapper.SetInputConnection(confilter.GetOutputPort())
    else:
        mapper.SetInputConnection(mc.GetOutputPort())
    mapper.ScalarVisibilityOff()

    # Visualize
    actor = vtkActor()
    actor.GetProperty().SetColor(colors.GetColor3d('SkinColor'))
    back_prop = vtkProperty()
    back_prop.SetDiffuseColor(colors.GetColor3d('BackfaceColor'))
    actor.SetBackfaceProperty(back_prop)
    actor.SetMapper(mapper)

    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))
    renderer.GetActiveCamera().SetViewUp(0.0, 0.0, 1.0)
    renderer.GetActiveCamera().SetPosition(0.0, 1.0, 0.0)
    renderer.GetActiveCamera().SetFocalPoint(0.0, 0.0, 0.0)
    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30.0)
    renderer.GetActiveCamera().Elevation(30.0)
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer)
    ren_win.SetSize(640, 480)
    ren_win.SetWindowName('ExtractLargestIsosurface')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    ren_win.Render()
    iren.Initialize()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'Reads a structured points dataset stored in a .vtk file and constructs a 3D model.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='E.g. brain.vtk.')
    parser.add_argument('threshold', type=int, help='The threshold, e.g. 50.')
    parser.add_argument('-a', action='store_false', default=True, help='Extract all surfaces.')
    args = parser.parse_args()
    return args.filename, args.threshold, args.a

def vtk_version_ok(major, minor, build):
    """
    Check the VTK version.

    :param major: Major version.
    :param minor: Minor version.
    :param build: Build version.
    :return: True if the requested VTK version is greater or equal to the actual VTK version.
    """
    needed_version = 10000000000 * int(major) + 100000000 * int(minor) + int(build)
    try:
        vtk_version_number = VTK_VERSION_NUMBER
    except AttributeError:  # as error:
        ver = vtkVersion()
        vtk_version_number = 10000000000 * ver.GetVTKMajorVersion() + 100000000 * ver.GetVTKMinorVersion() \
                             + ver.GetVTKBuildVersion()
    if vtk_version_number >= needed_version:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
```
