<!-- source: https://examples.vtk.org/site/Python/Medical/MedicalDemo3/ -->

# MedicalDemo3

Repository source: [MedicalDemo3](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Medical/MedicalDemo3.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Medical/TestMedicalDemo3.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Medical/TestMedicalDemo3.png?raw=true target=)

### Description

Composite image of three planes and translucent skin

Usage

MedicalDemo3 FullHead.mhd

Note

The skin color was selected from Table 7 in [Improvement of Haar Feature Based Face Detection in OpenCV Incorporating Human Skin Color Characteristic](https://www.researchgate.net/publication/310443424_Improvement_of_Haar_Feature_Based_Face_Detection_in_OpenCV_Incorporating_Human_Skin_Color_Characteristic)

Note

This original source code for this example is [here](https://gitlab.kitware.com/vtk/vtk/blob/395857190c8453508d283958383bc38c9c2999bf/Examples/Medical/Cxx/Medical3.cxx).

Info

See [Figure 12-4](../../VTKBook/12Chapter12.md#Figure%2012-4) in [Chapter 12](../../VTKBook/12Chapter12.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Medical/MedicalDemo3/)), ([PythonicAPI](../../PythonicAPI/Medical/MedicalDemo3.md)), ([Java](https://examples.vtk.org/site/Java/Medical/MedicalDemo3/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MedicalDemo3.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_VERSION_NUMBER,
    vtkLookupTable,
    vtkVersion
)
from vtkmodules.vtkCommonDataModel import (
    vtkPlane
)
from vtkmodules.vtkFiltersCore import (
    vtkFlyingEdges3D,
    vtkMarchingCubes,
    vtkStripper
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkImagingCore import vtkImageMapToColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkImageSlice,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from vtkmodules.vtkRenderingImage import vtkImageResliceMapper

def main():
    # vtkFlyingEdges3D was introduced in VTK >= 8.2
    use_flying_edges = vtk_version_ok(8, 2, 0)

    colors = vtkNamedColors()

    file_name = get_program_parameters()

    colors.SetColor('SkinColor', [240, 184, 160, 255])
    colors.SetColor('BkgColor', [51, 77, 102, 255])

    # Create the renderer, the render window, and the interactor. The
    # renderer draws into the render window, the interactor enables
    # mouse- and keyboard-based interaction with the data within the
    # render window.
    #
    ren = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    # Set a background color for the renderer and set the size of the
    # render window (expressed in pixels).
    ren.SetBackground(colors.GetColor3d('BkgColor'))
    ren_win.SetSize(640, 480)

    # The following reader is used to read a series of 2D slices (images)
    # that compose the volume. The slice dimensions are set, and the
    # pixel spacing. The data Endianness must also be specified. The
    # reader uses the FilePrefix in combination with the slice number to
    # construct filenames using the format FilePrefix.%d. (In this case
    # the FilePrefix is the root name of the file: quarter.)
    reader = vtkMetaImageReader()
    reader.SetFileName(file_name)
    reader.Update()

    # An isosurface, or contour value of 500 is known to correspond to
    # the skin of the patient.
    # The triangle stripper is used to create triangle
    # strips from the isosurface these render much faster on may
    # systems.
    if use_flying_edges:
        try:
            skin_extractor = vtkFlyingEdges3D()
        except AttributeError:
            skin_extractor = vtkMarchingCubes()
    else:
        skin_extractor = vtkMarchingCubes()
    skin_extractor.SetInputConnection(reader.GetOutputPort())
    skin_extractor.SetValue(0, 500)
    skin_extractor.Update()

    skin_stripper = vtkStripper()
    skin_stripper.SetInputConnection(skin_extractor.GetOutputPort())
    skin_stripper.Update()

    skin_mapper = vtkPolyDataMapper()
    skin_mapper.SetInputConnection(skin_stripper.GetOutputPort())
    skin_mapper.ScalarVisibilityOff()

    bounds = skin_mapper.GetBounds()
    centroid = list(map(lambda x, y: x + (y - x) / 2, bounds[0::2], bounds[1::2]))

    skin = vtkActor()
    skin.SetMapper(skin_mapper)
    skin.GetProperty().SetDiffuseColor(colors.GetColor3d('SkinColor'))
    skin.GetProperty().SetSpecular(0.3)
    skin.GetProperty().SetSpecularPower(20)

    # An isosurface, or contour value of 1150 is known to correspond to
    # the bone of the patient.
    # The triangle stripper is used to create triangle
    # strips from the isosurface these render much faster on may
    # systems.
    if use_flying_edges:
        try:
            bone_extractor = vtkFlyingEdges3D()
        except AttributeError:
            bone_extractor = vtkMarchingCubes()
    else:
        bone_extractor = vtkMarchingCubes()
    bone_extractor.SetInputConnection(reader.GetOutputPort())
    bone_extractor.SetValue(0, 1150)

    bone_stripper = vtkStripper()
    bone_stripper.SetInputConnection(bone_extractor.GetOutputPort())

    bone_mapper = vtkPolyDataMapper()
    bone_mapper.SetInputConnection(bone_stripper.GetOutputPort())
    bone_mapper.ScalarVisibilityOff()

    bone = vtkActor()
    bone.SetMapper(bone_mapper)
    bone.GetProperty().SetDiffuseColor(colors.GetColor3d('Ivory'))

    # An outline provides context around the data.
    #
    outline_data = vtkOutlineFilter()
    outline_data.SetInputConnection(reader.GetOutputPort())
    outline_data.Update()

    outline_mapper = vtkPolyDataMapper()
    outline_mapper.SetInputConnection(outline_data.GetOutputPort())

    outline = vtkActor()
    outline.SetMapper(outline_mapper)
    outline.GetProperty().SetColor(colors.GetColor3d('Black'))

    # Now we are creating three orthogonal planes passing through the
    # volume. Each plane uses a different texture map and therefore has
    # different coloration.

    # Start by creating a black/white lookup table.
    bw_lut = vtkLookupTable()
    bw_lut.SetTableRange(0, 2000)
    bw_lut.SetSaturationRange(0, 0)
    bw_lut.SetHueRange(0, 0)
    bw_lut.SetValueRange(0, 1)
    bw_lut.Build()  # effective built

    # Now create a lookup table that consists of the full hue circle
    # (from HSV).
    hue_lut = vtkLookupTable()
    hue_lut.SetTableRange(0, 2000)
    hue_lut.SetHueRange(0, 1)
    hue_lut.SetSaturationRange(1, 1)
    hue_lut.SetValueRange(1, 1)
    hue_lut.Build()  # effective built

    # Finally, create a lookup table with a single hue but having a range
    # in the saturation of the hue.
    sat_lut = vtkLookupTable()
    sat_lut.SetTableRange(0, 2000)
    sat_lut.SetHueRange(0.6, 0.6)
    sat_lut.SetSaturationRange(0, 1)
    sat_lut.SetValueRange(1, 1)
    sat_lut.Build()  # effective built

    # Use vtkImageMapToColors to map the scalar components of an input image
    # through a lookup table to produce an RGBA or RGB output imag
    # Then create a slice planes through a 3D image volume using
    # vtkImageSlice, combining it with a vtkImageResliceMapper and a vtkPlane.

    # Create the first (saggital) plane of the three planes.
    sagittal_colors = vtkImageMapToColors()
    sagittal_colors.SetInputConnection(reader.GetOutputPort())
    sagittal_colors.SetLookupTable(bw_lut)
    sagittal_colors.Update()

    sp = vtkPlane()
    sp.SetOrigin(centroid)
    sp.SetNormal(1, 0, 0)

    sagittal_mapper = vtkImageResliceMapper()
    sagittal_mapper.SetInputConnection(sagittal_colors.GetOutputPort())
    sagittal_mapper.SetSlicePlane(sp)  # Apply the custom slice plane

    sagittal_slice = vtkImageSlice()
    sagittal_slice.SetMapper(sagittal_mapper)

    # Create the second (axial) plane of the three planes. We use the
    # same approach as before except that the extent differs.
    axial_colors = vtkImageMapToColors()
    axial_colors.SetInputConnection(reader.GetOutputPort())
    axial_colors.SetLookupTable(hue_lut)
    axial_colors.Update()

    ap = vtkPlane()
    ap.SetOrigin(centroid)
    ap.SetNormal(0, 0, 1)

    axial_mapper = vtkImageResliceMapper()
    axial_mapper.SetInputConnection(axial_colors.GetOutputPort())
    axial_mapper.SetSlicePlane(ap)  # Apply the custom slice plane

    axial_slice = vtkImageSlice()
    axial_slice.SetMapper(axial_mapper)

    # Create the third (coronal) plane of the three planes. We use
    # the same approach as before except that the extent differs.
    coronal_colors = vtkImageMapToColors()
    coronal_colors.SetInputConnection(reader.GetOutputPort())
    coronal_colors.SetLookupTable(sat_lut)
    coronal_colors.Update()

    cp = vtkPlane()
    cp.SetOrigin(centroid)
    cp.SetNormal(0, 1, 0)

    coronal_mapper = vtkImageResliceMapper()
    coronal_mapper.SetInputConnection(coronal_colors.GetOutputPort())
    coronal_mapper.SetSlicePlane(cp)  # Apply the custom slice plane

    coronal_slice = vtkImageSlice()
    coronal_slice.SetMapper(coronal_mapper)

    # It is convenient to create an initial view of the data. The
    # FocalPoint and Position form a vector direction. Later on
    # (ResetCamera() method) this vector is used to position the camera
    # to look at the data in this direction.
    camera = vtkCamera()
    camera.SetViewUp(0, 0, 1)
    camera.SetPosition(0, -1, 0)
    camera.SetFocalPoint(0, 0, 0)
    camera.ComputeViewPlaneNormal()
    camera.Azimuth(30.0)
    camera.Elevation(30.0)

    # Actors are added to the renderer.
    ren.AddActor(outline)
    ren.AddActor(sagittal_slice)
    ren.AddActor(axial_slice)
    ren.AddActor(coronal_slice)
    ren.AddActor(skin)
    ren.AddActor(bone)

    # Turn off bone for this example.
    bone.VisibilityOff()

    # Set skin to semi-transparent.
    skin.GetProperty().SetOpacity(0.5)

    # An initial camera view is created.  The Dolly() method moves
    # the camera towards the FocalPoint, thereby enlarging the image.
    ren.SetActiveCamera(camera)

    # Calling Render() directly on a vtkRenderer is strictly forbidden.
    # Only calling Render() on the vtkRenderWindow is a valid call.
    ren_win.SetWindowName('MedicalDemo3')
    ren_win.Render()

    ren.ResetCamera()
    camera.Dolly(1.5)

    # Note that when camera movement occurs (as it does in the Dolly()
    # method), the clipping planes often need adjusting. Clipping planes
    # consist of two planes: near and far along the view direction. The
    # near plane clips out objects in front of the plane; the far plane
    # clips out objects behind the plane. This way only what is drawn
    # between the planes is actually rendered.
    ren.ResetCameraClippingRange()

    # Interact with the data.
    ren_win.Render()
    iren.Initialize()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'The skin and bone is extracted from a CT dataset of the head.'
    epilogue = '''
    Derived from VTK/Examples/Cxx/Medical3.cxx
    This example reads a volume dataset, extracts two isosurfaces that
     represent the skin and bone, creates three orthogonal planes
     (sagittal, axial, coronal), and displays them.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    args = parser.parse_args()
    return args.filename

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
