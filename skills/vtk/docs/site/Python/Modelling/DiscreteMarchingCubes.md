<!-- source: https://examples.vtk.org/site/Python/Modelling/DiscreteMarchingCubes/ -->

# DiscreteMarchingCubes

Repository source: [DiscreteMarchingCubes](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Modelling/DiscreteMarchingCubes.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Modelling/TestDiscreteMarchingCubes.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Modelling/TestDiscreteMarchingCubes.png?raw=true target=)

### Description

Creates surfaces from labeled data. Volume data does not always contain samples of continuous data. A volume may contain discrete integer values, often the result of segmentation. [vtkDiscreteFlyingEdges3D](https://www.vtk.org/doc/nightly/html/classvtkDiscreteFlyingEdges3D.html) or [vtkDiscreteMarchingCubes](https://www.vtk.org/doc/nightly/html/classvtkDiscreteMarchingCubes.html) create surfaces from these segmented volumes using a modified flying edges or marching cubes algorithm. The algorithm generates one or more models representing the boundaries between the specified label and the adjacent structures. One or more label values must be specified to generate the models. The boundary positions are always defined to be half-way between adjacent voxels.

Seealso

[SmoothDiscreteMarchingCubes](SmoothDiscreteMarchingCubes.md) produces smooth models.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Modelling/DiscreteMarchingCubes/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DiscreteMarchingCubes.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_VERSION_NUMBER,
    vtkLookupTable,
    vtkMinimalStandardRandomSequence,
    vtkVersion
)
from vtkmodules.vtkCommonDataModel import (
    vtkImageData,
    vtkSphere
)
from vtkmodules.vtkFiltersGeneral import (
    vtkDiscreteFlyingEdges3D,
    vtkDiscreteMarchingCubes
)
from vtkmodules.vtkImagingCore import vtkImageBinaryThreshold
from vtkmodules.vtkImagingHybrid import vtkSampleFunction
from vtkmodules.vtkImagingMath import vtkImageMathematics
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    # vtkDiscreteFlyingEdges3D was introduced in VTK >= 8.2
    use_flying_edges = vtk_version_ok(8, 2, 0)

    n = 20
    radius = 8
    blob = make_blob(n, radius)

    if use_flying_edges:
        try:
            discrete = vtkDiscreteFlyingEdges3D()
        except AttributeError:
            discrete = vtkDiscreteMarchingCubes()
    else:
        discrete = vtkDiscreteMarchingCubes()
    discrete.SetInputData(blob)
    discrete.GenerateValues(n, 1, n)

    lut = make_colors(n)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(discrete.GetOutputPort())
    mapper.SetLookupTable(lut)
    mapper.SetScalarRange(0, lut.GetNumberOfColors())

    # Create the RenderWindow, Renderer and both Actors
    #
    ren = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(ren)
    ren_win.SetWindowName('DiscreteMarchingCubes')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    actor = vtkActor()
    actor.SetMapper(mapper)

    ren.AddActor(actor)

    colors = vtkNamedColors()
    ren.SetBackground(colors.GetColor3d('Burlywood'))

    ren_win.Render()

    iren.Start()

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

def make_blob(n, radius):
    blob_image = vtkImageData()

    max_r = 50 - 2.0 * radius
    random_sequence = vtkMinimalStandardRandomSequence()
    random_sequence.SetSeed(5071)
    for i in range(0, n):

        sphere = vtkSphere()
        sphere.SetRadius(radius)

        x = random_sequence.GetRangeValue(-max_r, max_r)
        random_sequence.Next()
        y = random_sequence.GetRangeValue(-max_r, max_r)
        random_sequence.Next()
        z = random_sequence.GetRangeValue(-max_r, max_r)
        random_sequence.Next()

        sphere.SetCenter(int(x), int(y), int(z))

        sampler = vtkSampleFunction()
        sampler.SetImplicitFunction(sphere)
        sampler.SetOutputScalarTypeToFloat()
        sampler.SetSampleDimensions(100, 100, 100)
        sampler.SetModelBounds(-50, 50, -50, 50, -50, 50)

        thres = vtkImageBinaryThreshold()
        thres.SetInputConnection(sampler.GetOutputPort())
        thres.SetThresholdFunction(vtkImageBinaryThreshold.THRESHOLD_LOWER)
        thres.SetUpperThreshold(radius * radius)
        thres.ReplaceInOn()
        thres.ReplaceOutOn()
        thres.SetInValue(i + 1)
        thres.SetOutValue(0)

        thres.Update()
        if i == 0:
            blob_image.DeepCopy(thres.GetOutput())

        max_value = vtkImageMathematics()
        max_value.SetInputData(0, blob_image)
        max_value.SetInputData(1, thres.GetOutput())
        max_value.SetOperationToMax()
        max_value.Modified()
        max_value.Update()

        blob_image.DeepCopy(max_value.GetOutput())

    return blob_image

def make_colors(n):
    """
    Generate some random colors
    :param n: The number of colors.
    :return: The lookup table.
    """

    lut = vtkLookupTable()
    lut.SetNumberOfColors(n)
    lut.SetTableRange(0, n - 1)
    lut.SetScaleToLinear()
    lut.Build()
    lut.SetTableValue(0, 0, 0, 0, 1)

    random_sequence = vtkMinimalStandardRandomSequence()
    random_sequence.SetSeed(5071)
    for i in range(1, n):
        r = random_sequence.GetRangeValue(0.4, 1)
        random_sequence.Next()
        g = random_sequence.GetRangeValue(0.4, 1)
        random_sequence.Next()
        b = random_sequence.GetRangeValue(0.4, 1)
        random_sequence.Next()
        lut.SetTableValue(i, r, g, b, 1.0)

    return lut

if __name__ == '__main__':
    main()
```
