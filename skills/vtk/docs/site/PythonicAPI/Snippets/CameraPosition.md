<!-- source: https://examples.vtk.org/site/PythonicAPI/Snippets/CameraPosition/ -->

# CameraPosition

### Description

A callback that gives you the camera position and focal point.

To use the snippet, click the *Copy to clipboard* at the upper right of the code blocks.

### Implementation

```python
def camera_modified_callback(caller, event):
    """
     Used to estimate positions similar to the book illustrations.
    :param caller:
    :param event:
    :return:
    """
    flt_fmt = '0.6g'
    # print(caller.class_name, "modified")
    # Print the interesting stuff.
    res = list()
    res.append(f'camera = ren.active_camera')
    res.append(f'camera.position = ({fmt_floats(caller.position)})')
    res.append(f'camera.focal_point = ({fmt_floats(caller.focal_point)})')
    res.append(f'camera.view_up = ({fmt_floats(caller.view_up)})')
    res.append(f'camera.distance = {caller.distance:{flt_fmt}}')
    res.append(f'camera.clipping_range = ({fmt_floats(caller.clipping_range)})')
    indent = ' ' * 4
    lf_indent = f'\n{indent}'
    s = f'{indent}' + '|'.join(res) + '\n'
    print(s.replace('|', lf_indent))

def fmt_floats(v, w=0, d=6, pt='g'):
    """
    Pretty print a list or tuple of floats.

    :param v: The list or tuple of floats.
    :param w: Total width of the field.
    :param d: The number of decimal places.
    :param pt: The presentation type, 'f', 'g' or 'e'.
    :return: A string.
    """
    pt = pt.lower()
    if pt not in ['f', 'g', 'e']:
        pt = 'f'
    return ', '.join([f'{element:{w}.{d}{pt}}' for element in v])
```

### Usage

```python
    ren_win.Render()
    ren.active_camera.AddObserver('ModifiedEvent', camera_modified_callback)
```

Once you have the output, replace the `ren.active_camera.AddObserver(...)` line with the output data.
