<!-- source: https://examples.vtk.org/site/PythonicAPI/Snippets/COWPlacement/ -->

# COWPlacement

### Description

Define the parameters that label, color and position a vtkCameraOrientationWidget. This allows us to use multiple camera orientation widgets in a window with the provision to relabel the axes labels and change axis colors.

For examples showing the usage of this snippet please see [TissueLens](../Medical/TissueLens.md).

To use the snippet, click the *Copy to clipboard* at the upper right of the code blocks.

### Declaration Section

```python
#!/usr/bin/env python3
import sys
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import (
    vtkCameraOrientationRepresentation, vtkCameraOrientationWidget)
from vtkmodules.vtkRenderingCore import (
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor)
```

### Implementation Section

```python
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
```

### Usage

```python
def main():
    colors = vtkNamedColors()

    ren = vtkRenderer(background=colors.GetColor3d('ParaViewBlueGrayBkg'))
    ren_win = vtkRenderWindow(size=(640, 480), window_name=Path(sys.argv[0]).stem)
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    # Since we import vtkmodules.vtkInteractionStyle we can do this
    # because vtkInteractorStyleSwitch is automatically imported:
    iren.interactor_style.SetCurrentStyleToTrackballCamera()

    owp = COWPlacement()
    # Important: The interactor must be set prior to enabling the widget.
    cow = owp.make_cow(ren)
    cow.On()

    category = 'ADR'
    cow1 = owp.make_cow(ren, category, 1)
    cow1.On()

    category = 'SAL'
    cow2 = owp.make_cow(ren, category, 0)
    cow2.On()

    # Initialize the event loop and then start it.
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
```
