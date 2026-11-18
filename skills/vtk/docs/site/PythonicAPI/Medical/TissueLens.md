<!-- source: https://examples.vtk.org/site/PythonicAPI/Medical/TissueLens/ -->

# TissueLens

Repository source: [TissueLens](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Medical/TissueLens.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Medical/TestTissueLens.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Medical/TestTissueLens.png?raw=true target=)

### Description

Here a "magnifying lens" or "window" effect is generated, allowing users to peek inside a 3D medical dataset—such as a human head CT or MRI scan—by cutting a clean hole into the outer layer (the skin) to reveal the underlying structures (like the brain or bone) inside a specific region.

This example uses two [vtkClipDataSet](https://www.vtk.org/doc/nightly/html/classvtkClipDataSet.html) filters to achieve a "tissue lens" effect. First, a [vtkSphere](https://www.vtk.org/doc/nightly/html/classvtkSphere.html) implicit function is used to clip a spherical hole in the isosurface extracted with [vtkFlyingEdges3D](https://www.vtk.org/doc/nightly/html/classvtkFlyingEdges3D.html) or [vtkMarchingCubes](https://www.vtk.org/doc/nightly/html/classvtkMarchingCubes.html). Then a geometric [vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html) samples the original volume data using a [vtkProbeFilter](https://www.vtk.org/doc/nightly/html/classvtkProbeFilter.html). [vtkClipDataSet](https://www.vtk.org/doc/nightly/html/classvtkClipDataSet.html) uses the resulting scalar point data to clip the sphere surface with the isosurface value.

Usage

TissueLens FullHead.mhd

Note

The skin color was selected from Table 7 in [Improvement of Haar Feature Based Face Detection in OpenCV Incorporating Human Skin Color Characteristic](https://www.researchgate.net/publication/310443424_Improvement_of_Haar_Feature_Based_Face_Detection_in_OpenCV_Incorporating_Human_Skin_Color_Characteristic)

Info

The example uses `src/Testing/Data/FullHead.mhd` which references `src/Testing/Data/FullHead.raw.gz`.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Medical/TissueLens/)), ([Python](../../Python/Medical/TissueLens.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**TissueLens.py**

```python
#!/usr/bin/env python3

import sys
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkLookupTable
)
from vtkmodules.vtkCommonDataModel import vtkSphere
from vtkmodules.vtkCommonMath import vtkMatrix4x4
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import (
    vtkFlyingEdges3D,
    vtkMarchingCubes,
    vtkProbeFilter
)
from vtkmodules.vtkFiltersGeneral import vtkClipDataSet
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkCameraOrientationRepresentation
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkDataSetMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    file_name, use_flying_edges = get_program_parameters()

    colors.SetColor('SkinColor', 240, 184, 160, 255)
    colors.SetColor('BackfaceColor', 255, 229, 200, 255)
    colors.SetColor('BkgColor', 51, 77, 102, 255)

    # Create the renderer, the render window, and the interactor. The renderer
    # draws into the render window, the interactor enables mouse- and
    # keyboard-based interaction with the data within the render window.
    #
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

    # Read the volume data
    reader = vtkMetaImageReader(file_name=file_name)
    reader.update()

    # An isosurface, or contour value of 500 is known to correspond to the
    # skin of the patient.
    if use_flying_edges:
        try:
            skin_extractor = vtkFlyingEdges3D()
        except AttributeError:
            skin_extractor = vtkMarchingCubes()
    else:
        skin_extractor = vtkMarchingCubes()
    skin_extractor.input_connection = reader.output_port
    skin_extractor.SetValue(0, 500)

    clip_center = (-70, 60, -10)

    # Define a spherical clip function to clip the isosurface
    clip_function = vtkSphere(radius=50, center=clip_center)

    # Clip the isosurface with a sphere
    skin_clip = vtkClipDataSet(input_connection=skin_extractor.output_port, clip_function=clip_function, value=0,
                               generate_clip_scalars=True)
    skin_clip.update()

    skin_mapper = vtkDataSetMapper(input_connection=skin_clip.output_port, scalar_visibility=False)

    skin_prop = vtkProperty(diffuse_color=colors.GetColor3d('SkinColor'))
    back_prop = vtkProperty(diffuse_color=colors.GetColor3d('BackfaceColor'))

    skin = vtkActor(mapper=skin_mapper, property=skin_prop, backface_property=back_prop)

    # Define a model for the "lens". Its geometry matches the implicit
    # sphere used to clip the isosurface
    lens_model = vtkSphereSource(radius=50, center=clip_center, phi_resolution=201, theta_resolution=101)

    # Sample the input volume with the lens model geometry
    lens_probe = vtkProbeFilter(input_connection=lens_model.output_port, source_connection=reader.output_port)

    # Clip the lens data with the isosurface value
    lens_clip = vtkClipDataSet(input_connection=lens_probe.output_port, value=500, generate_clip_scalars=False)
    lens_clip.update()

    # Define a suitable grayscale lut
    bw_lut = vtkLookupTable()
    bw_lut.SetTableRange(0, 2048)
    bw_lut.SetSaturationRange(0, 0)
    bw_lut.SetHueRange(0, 0)
    bw_lut.SetValueRange(0.2, 1)
    bw_lut.Build()

    lens_mapper = vtkDataSetMapper(input_connection=lens_clip.output_port, scalar_range=lens_clip.output.scalar_range,
                                   lookup_table=bw_lut)

    lens = vtkActor(mapper=lens_mapper)

    # It is convenient to create an initial view of the data. The FocalPoint
    # and Position form a vector direction. Later on (ResetCamera() method)
    # this vector is used to position the camera to look at the data in
    # this direction.
    camera = vtkCamera()
    camera.Azimuth(30.0)
    camera.Elevation(30.0)

    # This transform positions the actors correctly.
    # The face of the head will now face the observer.
    permute = Permute()
    lsa = permute.get_transform('si')

    #
    # # This transform positions the actors correctly.
    # # Labels are: XYZ -> LSA
    # lsa = vtkTransform()
    # lsa.RotateX(-90)
    lens.user_transform = lsa
    skin.user_transform = lsa

    # Actors are added to the renderer. An initial camera view is created.
    # The Dolly() method moves the camera towards the FocalPoint,
    # thereby enlarging the image.

    ren.AddActor(lens)
    ren.AddActor(skin)
    ren.SetActiveCamera(camera)
    ren.ResetCamera()
    camera.Dolly(1.5)

    # Note that when camera movement occurs (as it does in the Dolly()
    # method), the clipping planes often need adjusting. Clipping planes
    # consist of two planes: near and far along the view direction. The
    # near plane clips out objects in front of the plane the far plane
    # clips out objects behind the plane. This way only what is drawn
    # between the planes is actually rendered.
    ren.ResetCameraClippingRange()

    ren_win.Render()

    cp = COWPlacement()
    cow = cp.make_cow(ren)
    # Enable the widget.
    cow.On()

    # The labels and colors for the various axes.
    category = 'LSA'
    cow1 = cp.make_cow(ren, category, 1)
    cow1.On()

    # Initialize the event loop and then start it.
    iren.Initialize()
    iren.Start()

def get_program_parameters():
    import argparse
    description = ('Generate a "magnifying lens" or "window" effect, allowing'
                   ' users to peek inside a 3D medical dataset')
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='FullHead.mhd.')
    parser.add_argument('-m', '--marching_cubes', action='store_false',
                        help='Use Marching Cubes instead of Flying Edges.')
    args = parser.parse_args()
    return args.filename, args.marching_cubes

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
