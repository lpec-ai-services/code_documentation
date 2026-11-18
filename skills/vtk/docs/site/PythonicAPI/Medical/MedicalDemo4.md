<!-- source: https://examples.vtk.org/site/PythonicAPI/Medical/MedicalDemo4/ -->

# MedicalDemo4

Repository source: [MedicalDemo4](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Medical/MedicalDemo4.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Medical/TestMedicalDemo4.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Medical/TestMedicalDemo4.png?raw=true target=)

### Description

Volume rendering of the dataset.

Usage

MedicalDemo4 FullHead.mhd

Note

The original source code for this example is [here](https://gitlab.kitware.com/vtk/vtk/blob/395857190c8453508d283958383bc38c9c2999bf/Examples/Medical/Cxx/Medical4.cxx).

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Medical/MedicalDemo4/)), ([Python](../../Python/Medical/MedicalDemo4.md)), ([Java](https://examples.vtk.org/site/Java/Medical/MedicalDemo4/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MedicalDemo4.py**

```python
#!/usr/bin/env python3

import sys
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingVolumeOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPiecewiseFunction
from vtkmodules.vtkCommonMath import vtkMatrix4x4
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkImagingCore import vtkImageChangeInformation
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkCameraOrientationRepresentation
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkColorTransferFunction,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkVolume,
    vtkVolumeProperty
)
from vtkmodules.vtkRenderingVolume import vtkFixedPointVolumeRayCastMapper

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()

    colors.SetColor('BkgColor', 51, 77, 102, 255)

    # Create the renderer, the render window, and the interactor. The renderer
    # draws into the render window, the interactor enables mouse- and
    # keyboard-based interaction with the scene.
    ren = vtkRenderer()
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(ren)
    # Set a background color for the renderer and set the name and
    # size of the render window (expressed in pixels).
    ren = vtkRenderer(background=colors.GetColor3d('BkgColor'))
    ren_win = vtkRenderWindow(size=(640, 480),
                              window_name=f'{Path(sys.argv[0]).stem:s}')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    # The following reader is used to read a series of 2D slices (images)
    # that compose the volume. The slice dimensions are set, and the
    # pixel spacing. The data Endianness must also be specified. The reader
    # uses the FilePrefix in combination with the slice number to construct
    # filenames using the format FilePrefix.%d. (In this case the FilePrefix
    # is the root name of the file: quarter.)
    reader = vtkMetaImageReader(file_name=file_name)
    reader.SetDataByteOrderToLittleEndian()
    reader.update()

    # Get the image metadata.
    extent = reader.data_extent
    spacing = reader.data_spacing
    origin = reader.data_origin

    # Calculate the dimensions in voxels.
    dims_v = list()
    for i in range(0, 6, 2):
        dims_v.append(extent[i + 1] - extent[i] + 1)
    # Calculate the physical center of the volume.
    center = list()
    for i in range(0, 3):
        center.append(origin[i] + 0.5 * spacing[i] * dims_v[i])

    # Apply the shift using vtkImageChangeInformation.
    change_information = vtkImageChangeInformation()
    reader >> change_information
    # Center the image by shifting it by the negative center coordinates.
    change_information.output_origin = (list(map(lambda x: -x, center)))

    # An outline provides context around the data.
    outline_filter = vtkOutlineFilter()
    change_information >> outline_filter
    # We need to transform the outline so that it outlines the head.
    transform = vtkTransform()
    # Move the outline from the origin to the new center inside the head.
    transform.Translate(center[0] * 2, 0.0, center[2] * 2)
    # Apply the transform to the geometry.
    transform_filter = vtkTransformFilter(input_connection=outline_filter.output_port, transform=transform)
    transform_filter.update()

    outline_mapper = vtkPolyDataMapper()
    transform_filter >> outline_mapper
    outline_property = vtkProperty(diffuse_color=colors.GetColor3d('Black'))
    outline = vtkActor(mapper=outline_mapper, property=outline_property)

    # The volume will be displayed by ray-cast alpha compositing.
    # A ray-cast mapper is needed to do the ray-casting.
    volume_mapper = vtkFixedPointVolumeRayCastMapper()
    change_information >> volume_mapper

    # The color transfer function maps voxel intensities to colors.
    # It is modality-specific, and often anatomy-specific as well.
    # The goal is to one color for flesh (between 500 and 1000)
    # and another color for bone (1150 and over).
    volume_color = vtkColorTransferFunction()
    volume_color.AddRGBPoint(0, 0.0, 0.0, 0.0)
    volume_color.AddRGBPoint(500, 240.0 / 255.0, 184.0 / 255.0, 160.0 / 255.0)
    volume_color.AddRGBPoint(1000, 240.0 / 255.0, 184.0 / 255.0, 160.0 / 255.0)
    volume_color.AddRGBPoint(1150, 1.0, 1.0, 240.0 / 255.0)  # Ivory

    # The opacity transfer function is used to control the opacity
    # of different tissue types.
    volume_scalar_opacity = vtkPiecewiseFunction()
    volume_scalar_opacity.AddPoint(0, 0.00)
    volume_scalar_opacity.AddPoint(500, 0.15)
    volume_scalar_opacity.AddPoint(1000, 0.15)
    volume_scalar_opacity.AddPoint(1150, 0.85)

    # The gradient opacity function is used to decrease the opacity
    # in the 'flat' regions of the volume while maintaining the opacity
    # at the boundaries between tissue types.  The gradient is measured
    # as the amount by which the intensity changes over unit distance.
    # For most medical data, the unit distance is 1mm.
    volume_gradient_opacity = vtkPiecewiseFunction()
    volume_gradient_opacity.AddPoint(0, 0.0)
    volume_gradient_opacity.AddPoint(90, 0.5)
    volume_gradient_opacity.AddPoint(100, 1.0)

    # The VolumeProperty attaches the color and opacity functions to the
    # volume, and sets other volume properties.  The interpolation should
    # be set to linear in order to do a high-quality rendering.
    # The ShadeOn option turns on directional lighting, which will usually
    # enhance the appearance of the volume and make it look more '3D'.
    # However, the quality of the shading depends on how accurately the gradient
    # of the volume can be calculated, and for noisy data the gradient
    # estimation will be very poor. The impact of the shading can be
    # decreased by increasing the Ambient coefficient while decreasing
    # the Diffuse and Specular coefficient. To increase the impact
    # of shading, decrease the Ambient and increase the Diffuse and Specular.
    volume_property = vtkVolumeProperty(color=volume_color, scalar_opacity=volume_scalar_opacity,
                                        gradient_opacity=volume_gradient_opacity, shade=True,
                                        ambient=0.4, diffuse=0.6, specular=0.2)
    volume_property.SetInterpolationTypeToLinear()

    # The vtkVolume is a vtkProp3D (like a vtkActor) and controls the position
    # and orientation of the volume in world coordinates.
    volume = vtkVolume(property=volume_property, mapper=volume_mapper)

    # This transform positions the actors correctly.
    # The face of the head will now face to the left.
    permute = Permute()
    rsp = permute.get_transform('hfis')

    outline.user_transform = rsp
    volume.user_transform = rsp

    # Finally, add the volume and outline to the renderer
    ren.AddActor(volume)
    ren.AddActor(outline)

    # Set up an initial view of the volume.  The focal point will be the
    # center of the volume, and the camera position will be 400mm to the
    # patient's left (which is our right).
    # camera.ComputeViewPlaneNormal()
    camera = vtkCamera(position=(-400, 0, 0))
    camera.Elevation(30.0)
    ren.SetActiveCamera(camera)
    camera.Dolly(0.8)
    ren.ResetCameraClippingRange()

    ren_win.Render()

    category = 'RSP'
    cp = COWPlacement()
    cow = cp.make_cow(ren, category)
    # Enable the widget.
    cow.On()

    iren.Initialize()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'Read a volume dataset and display it via volume rendering.'
    epilogue = '''
    Derived from VTK/Examples/Cxx/Medical4.cxx
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    args = parser.parse_args()
    return args.filename

class Permute:
    """
    These transformations permute image and other geometric data to maintain proper
     orientation regardless of the acquisition order. After applying these transforms with
    vtkTransformFilter, a view up of 0, -1, 0 will result in the body part
    facing the viewer.
    NOTE: some transformations have a -1 scale factor for one of the components.
          To ensure proper polygon orientation and normal direction, you must
          apply the vtkPolyDataNormals filter.

    Naming (the nomenclature is medical):
    si - superior to inferior (top to bottom)
    is - inferior to superior (bottom to top)
    ap - anterior to posterior (front to back)
    pa - posterior to anterior (back to front)
    lr - left to right
    rl - right to left
    """

    def __init__(self):
        self.si_mat = vtkMatrix4x4([[1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
        self.is_mat = vtkMatrix4x4([[1, 0, 0, 0], [0, 0, -1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
        self.lr_mat = vtkMatrix4x4([[0, 0, -1, 0], [0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1]])
        self.rl_mat = vtkMatrix4x4([[0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1]])

        self.transform = dict()
        self.generate_transforms()

    def generate_transforms(self):
        """
        Generate the transforms and collect them into a dict.
        """
        si_trans = vtkTransform()
        si_trans.SetMatrix(self.si_mat)
        self.transform['si'] = si_trans

        is_trans = vtkTransform()
        is_trans.SetMatrix(self.is_mat)
        self.transform['is'] = is_trans

        ap_trans = vtkTransform()
        ap_trans.Scale(1, -1, 1)
        self.transform['ap'] = ap_trans

        pa_trans = vtkTransform()
        pa_trans.Scale(1, -1, -1)
        self.transform['pa'] = pa_trans

        lr_trans = vtkTransform()
        lr_trans.SetMatrix(self.lr_mat)
        self.transform['lr'] = lr_trans

        rl_trans = vtkTransform()
        rl_trans.SetMatrix(self.rl_mat)
        self.transform['rl'] = rl_trans

        """
        The previous transforms assume radiological views of the slices
         (viewed from the feet).
        Other modalities such as physical sectioning may view from the head.
        The following transforms modify the original with a 180° rotation
         about the y-axis.
        """

        self.hf_mat = vtkMatrix4x4([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
        hf_trans = vtkTransform()
        hf_trans.SetMatrix(self.hf_mat)
        self.transform['hf'] = hf_trans

        hf_si_trans = vtkTransform()
        hf_si_trans.SetMatrix(self.hf_mat)
        hf_si_trans.Concatenate(self.si_mat)
        self.transform['hfsi'] = hf_si_trans

        hf_is_trans = vtkTransform()
        hf_is_trans.SetMatrix(self.hf_mat)
        hf_is_trans.Concatenate(self.is_mat)
        self.transform['hfis'] = hf_is_trans

        hf_ap_trans = vtkTransform()
        hf_ap_trans.SetMatrix(self.hf_mat)
        hf_ap_trans.Scale(1, -1, 1)
        self.transform['hfap'] = hf_ap_trans

        hf_pa_trans = vtkTransform()
        hf_pa_trans.SetMatrix(self.hf_mat)
        hf_pa_trans.Scale(1, -1, -1)
        self.transform['hfpa'] = hf_pa_trans

        hf_lr_trans = vtkTransform()
        hf_lr_trans.SetMatrix(self.hf_mat)
        hf_lr_trans.Concatenate(self.lr_mat)
        self.transform['hflr'] = hf_lr_trans

        hf_rl_trans = vtkTransform()
        hf_rl_trans.SetMatrix(self.hf_mat)
        hf_rl_trans.Concatenate(self.rl_mat)
        self.transform['hfrl'] = hf_rl_trans

        # Identity
        self.transform['I'] = vtkTransform()

        # Zero
        z_trans = vtkTransform()
        z_trans.Scale(0, 0, 0)
        self.transform['Z'] = z_trans

    def print_transform(self, permutation):
        """
        Print the homogenous matrix corresponding to the permutation.
        :param permutation: The permutation.
        :return:
        """
        print(permutation)
        m = self.transform[permutation].GetMatrix()
        for i in range(0, 4):
            row = list()
            for j in range(0, 4):
                row.append(f'{m.GetElement(i, j):>6.2g}')
            print(' '.join(row))

    def print_all_transforms(self):
        """
        Print all the homogenous matrices corresponding to the permutations.
        :return:
        """
        print(self.transform.keys())
        for k in self.transform.keys():
            self.print_transform(k)

    def get_transform(self, permutation):
        """
        Returns the vtkTransform corresponding to the permutation.

        :param permutation: The permutation.
        :return: The vtkTransform to use.
        """
        if permutation in self.transform.keys():
            return self.transform[permutation]
        else:
            s = 'No such transform "{:s}" exists.'.format(permutation)
            raise Exception(s)

class COWPlacement:
    def __init__(self=None):
        self.label_color = dict()
        self.make_label_color()

    def make_label_color(self):
        # Define the axes labels.
        # The three digit key refers to the positive X,Y,Z axes.
        labels = {
            # Labels are: Anterior, Posterior, Dorsal, Ventral, Left, Right
            'ADL': {'+X': 'A', '+Y': 'D', '+Z': 'L', '-X': 'P', '-Y': 'V', '-Z': 'R'},
            'ALV': {'+X': 'A', '+Y': 'L', '+Z': 'V', '-X': 'P', '-Y': 'R', '-Z': 'D'},
            'ADR': {'+X': 'A', '+Y': 'D', '+Z': 'R', '-X': 'P', '-Y': 'V', '-Z': 'L'},
            'ARV': {'+X': 'A', '+Y': 'R', '+Z': 'V', '-X': 'P', '-Y': 'L', '-Z': 'D'},
            'PDL': {'+X': 'P', '+Y': 'D', '+Z': 'L', '-X': 'A', '-Y': 'V', '-Z': 'R'},
            # Labels are: Left, Right, Superior, Inferior, Anterior, Posterior
            'LAS': {'+X': 'L', '+Y': 'A', '+Z': 'S', '-X': 'R', '-Y': 'P', '-Z': 'I'},
            'LPA': {'+X': 'L', '+Y': 'P', '+Z': 'A', '-X': 'R', '-Y': 'A', '-Z': 'S'},
            'LPS': {'+X': 'L', '+Y': 'P', '+Z': 'S', '-X': 'R', '-Y': 'A', '-Z': 'I'},
            'LSA': {'+X': 'L', '+Y': 'S', '+Z': 'A', '-X': 'R', '-Y': 'I', '-Z': 'A'},
            'RAP': {'+X': 'R', '+Y': 'A', '+Z': 'P', '-X': 'L', '-Y': 'I', '-Z': 'S'},
            'RAS': {'+X': 'R', '+Y': 'A', '+Z': 'S', '-X': 'L', '-Y': 'P', '-Z': 'I'},
            'RPS': {'+X': 'R', '+Y': 'P', '+Z': 'S', '-X': 'L', '-Y': 'A', '-Z': 'I'},
            'RSP': {'+X': 'R', '+Y': 'S', '+Z': 'P', '-X': 'L', '-Y': 'I', '-Z': 'A'},
            'SAL': {'+X': 'S', '+Y': 'A', '+Z': 'L', '-X': 'I', '-Y': 'P', '-Z': 'R'},
            # Default labels
            'XYZ': None,
        }
        # Label colors.
        c1 = {'+X': 'IndianRed', '-X': 'FireBrick',
              '+Y': 'LimeGreen', '-Y': 'DarkGreen',
              '+Z': 'SkyBlue', '-Z': 'DeepSkyBlue'}
        colors = {
            'ADL': c1,
            'ALV': c1,
            'ADR': c1,
            'ARV': c1,
            'PDL': c1,
            # Default colors.
            'LAS': None,
            'LPS': None,
            'LPA': None,
            'LSA': None,
            'RAP': None,
            'RAS': None,
            'RPS': None,
            'RSP': None,
            'SAL': None,
            # The default.
            'XYZ': None,
        }

        # Gather the defined axes labels and colors into a dictionary.
        # The keys must be the same.
        label_keys = set(labels.keys())
        color_keys = set(colors.keys())
        common_keys = label_keys.intersection(color_keys)
        for k in common_keys:
            self.label_color[k] = (labels[k], colors[k])

    def make_cow(self, ren, lc_key='XYZ', position=3):
        """
        Make a camera orientation widget for a given renderer.

        position has these values
            0: LowerLeft,
            1: UpperLeft,
            2: LowerRight,
            3: UpperRight - the default

        :param ren: The renderer.
        :param lc_key: The key specifying the desired labels and colors for the axes.
        :param position: Where to position the camera orientation widget.
        :return: The camera orientation widget.
        """
        if lc_key not in self.label_color:
            print(
                f'Invalid key for axes labels and colors.'
                f'\nValid keys are: {sorted(self.label_color.keys())}'
                f'\nUsing the key: XYZ.')
            lc_key = 'XYZ'

        lc = self.label_color[lc_key]

        rep = vtkCameraOrientationRepresentation()

        match position:
            case 0:
                rep.AnchorToLowerLeft()
            case 1:
                rep.AnchorToUpperLeft()
            case 2:
                rep.AnchorToLowerRight()
            case _:
                rep.AnchorToUpperRight()

        if not lc[0] is None:
            rep.x_plus_label_text = lc[0]['+X']
            rep.x_minus_label_text = lc[0]['-X']
            rep.y_plus_label_text = lc[0]['+Y']
            rep.y_minus_label_text = lc[0]['-Y']
            rep.z_plus_label_text = lc[0]['+Z']
            rep.z_minus_label_text = lc[0]['-Z']

        if not lc[1] is None:
            colors = vtkNamedColors()
            rep.x_axis_color = colors.GetColor3d(lc[1]['+X'])
            rep.y_axis_color = colors.GetColor3d(lc[1]['+Y'])
            rep.z_axis_color = colors.GetColor3d(lc[1]['+Z'])

        cow = vtkCameraOrientationWidget(parent_renderer=ren, representation=rep, enabled=False)

        return cow

if __name__ == '__main__':
    main()
```
