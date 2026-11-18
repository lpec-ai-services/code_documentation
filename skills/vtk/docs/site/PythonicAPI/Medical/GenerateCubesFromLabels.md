<!-- source: https://examples.vtk.org/site/PythonicAPI/Medical/GenerateCubesFromLabels/ -->

# GenerateCubesFromLabels

Repository source: [GenerateCubesFromLabels](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Medical/GenerateCubesFromLabels.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Medical/TestGenerateCubesFromLabels.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Medical/TestGenerateCubesFromLabels.png?raw=true target=)

### Description

Sometimes it is helpful to view the results of a segmentation without any post processing. This example converts the point data from a labeled volume into cell data. The surfaces are displayed as vtkPolydata. If you want to created smoothed polydata models from your segmented volumes, see the example [GenerateModelsFromLabels](GenerateModelsFromLabels.md). The input volume must be in [MetaIO format](http://www.vtk.org/Wiki/MetaIO/Documentation).

```python
 Usage: GenerateCubesFromLabels InputVolume.mhd StartLabel EndLabel
      where
        InputVolume is a meta file containing a 3 volume of discrete labels.
        StartLabel is the first label to be processed
        EndLabel is the last label to be processed
        NOTE: There can be gaps in the labeling. If a label does not exist in the volume, it will be skipped.
```

Note

This original source code for this example is [here](https://gitlab.kitware.com/vtk/vtk/blob/395857190c8453508d283958383bc38c9c2999bf/Examples/Medical/Cxx/GenerateCubesFromLabels.cxx).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Medical/GenerateCubesFromLabels/)), ([Python](../../Python/Medical/GenerateCubesFromLabels.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GenerateCubesFromLabels.py**

```python
#!/usr/bin/env python3
import sys
from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkDataObject,
    vtkDataSetAttributes
)
from vtkmodules.vtkCommonMath import vtkMatrix4x4
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import vtkThreshold
from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from vtkmodules.vtkFiltersGeometry import vtkGeometryFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkImagingCore import vtkImageWrapPad
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationWidget,
    vtkCameraOrientationRepresentation
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    file_name, start_label, end_label = get_program_parameters()
    if start_label > end_label:
        end_label, start_label = start_label, end_label

    # Generate cubes from labels
    # 1) Read the meta file
    # 2) Convert point data to cell data
    # 3) Convert to geometry and display

    reader = vtkMetaImageReader(file_name=file_name)
    reader.update()

    # Pad the volume so that we can change the point data into cell
    # data.
    extent = reader.output.extent
    padded_extent = (extent[0], extent[1] + 1, extent[2], extent[3] + 1, extent[4], extent[5] + 1)
    pad = vtkImageWrapPad(output_whole_extent=padded_extent)
    (reader >> pad).update()

    # Copy the scalar point data of the volume into the scalar cell data
    pad.output.cell_data.SetScalars(reader.output.point_data.scalars)

    selector = vtkThreshold(input_array_to_process=(0, 0, 0,
                                                    vtkDataObject.FIELD_ASSOCIATION_CELLS,
                                                    vtkDataSetAttributes.SCALARS),
                            lower_threshold=start_label, upper_threshold=end_label)

    # Shift the geometry by 1/2
    transform = vtkTransform()
    transform.Translate(-0.5, -0.5, -0.5)

    transform_model = vtkTransformFilter(transform=transform)

    geometry = vtkGeometryFilter()

    mapper = vtkPolyDataMapper(scalar_range=(start_label, end_label),
                               scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_CELL_DATA,
                               color_mode=Mapper.ColorMode.VTK_COLOR_MODE_MAP_SCALARS)
    pad >> selector >> transform_model >> geometry >> mapper

    actor = vtkActor(mapper=mapper)

    ren = vtkRenderer(background=colors.GetColor3d('DarkSlateBlue'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name=Path(sys.argv[0]).stem)
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    # This transform positions the actors correctly.
    # The right side of the frog will now face the observer.
    permute = Permute()
    adr = permute.get_transform('is')

    actor.SetUserTransform(adr)

    ren.AddActor(actor)

    ren_win.Render()

    camera = vtkCamera()
    camera.Azimuth(-45.0)
    camera.Elevation(45.0)
    ren.SetActiveCamera(camera)
    ren.ResetCamera()
    camera.Dolly(1.2)

    owp = COWPlacement()
    # Important: The interactor must be set prior to enabling the widget.
    cow = owp.make_cow(ren)
    cow.On()

    category = 'ADR'
    cow1 = owp.make_cow(ren, category, 1)
    cow1.On()

    # Initialize the event loop and then start it.
    iren.Initialize()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'View the results of a segmentation without any post processing.'
    epilogue = '''
    The point data from a labeled volume is converted into cell data.
     '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='Input volume e.g. Frog/frogtissue.mhd.')
    parser.add_argument('startlabel', nargs='?', type=int, default=1,
                        help='The starting label in the input volume, e,g, 1.')
    parser.add_argument('endlabel', nargs='?', type=int, default=29,
                        help='The ending label in the input volume e.g. 29')
    args = parser.parse_args()
    return args.filename, args.startlabel, args.endlabel

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

@dataclass(frozen=True)
class Mapper:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_MODE_DEFAULT: int = 0
        VTK_COLOR_MODE_MAP_SCALARS: int = 1
        VTK_COLOR_MODE_DIRECT_SCALARS: int = 2

    @dataclass(frozen=True)
    class ResolveCoincidentTopology:
        VTK_RESOLVE_OFF: int = 0
        VTK_RESOLVE_POLYGON_OFFSET: int = 1
        VTK_RESOLVE_SHIFT_ZBUFFER: int = 2

    @dataclass(frozen=True)
    class ScalarMode:
        VTK_SCALAR_MODE_DEFAULT: int = 0
        VTK_SCALAR_MODE_USE_POINT_DATA: int = 1
        VTK_SCALAR_MODE_USE_CELL_DATA: int = 2
        VTK_SCALAR_MODE_USE_POINT_FIELD_DATA: int = 3
        VTK_SCALAR_MODE_USE_CELL_FIELD_DATA: int = 4
        VTK_SCALAR_MODE_USE_FIELD_DATA: int = 5

if __name__ == '__main__':
    main()
```
