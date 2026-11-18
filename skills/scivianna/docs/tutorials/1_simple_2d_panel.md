<!-- source: 1_simple_2d_panel.ipynb -->

# Tutorial 1: How to Open a Simple 2D Panel

This tutorial shows how to create and display a simple 2D visualization panel in scivianna. You'll learn the complete workflow from importing the library to displaying interactive visualizations of MED mesh/field files.

## Step 1: Import Scivianna

First, import the scivianna module along with supporting classes. These are the core components you'll use throughout all tutorials:

- `ComputeSlave`: The computation engine that manages data processing and interface communication
- `MEDInterface`: The interface for reading MED (MEDCoupling) mesh and field files
- `Panel2D`: The 2D visualization panel widget for displaying geometry and fields
- `GEOMETRY` / `MESH`: Constants used to identify file types and display modes

``` python
import scivianna
from pathlib import Path
from scivianna.slave import ComputeSlave
from scivianna.interface.med_interface import MEDInterface
from scivianna.panel.panel_2d import Panel2D
from scivianna.constants import MESH, GEOMETRY
import scivianna.input_file

print(f"Scivianna version: {scivianna.__version__ if hasattr(scivianna, '__version__') else 'dev'}")
```

## Step 2: Create a Panel Using Convenience Functions

The fastest way to get started is using scivianna's convenience functions. These helper functions encapsulate the common pattern of creating a `ComputeSlave`, loading a file, and wrapping it in a `Panel2D`.

`get_med_panel()` is the simplest approach. It takes a MED file path and returns a ready-to-use `Panel2D` instance:

``` python
from scivianna.notebook_tools import get_med_panel

# Path to a built-in example MED file
med_file_path = Path(scivianna.input_file.__file__).parent / "power.med"

# Create the panel with a single function call
panel = get_med_panel(geo=str(med_file_path), title="MED Visualizer")

# Display the panel - note: while it can work on standard jupyter notebook, it does not through VS-Code due to a bokeh vscode incompatibility
# panel
```

## Step 3: Create a Panel Manually (Advanced)

For more control over the visualization, you can build the panel step by step. This approach gives you access to all customization options:

- `display_polygons`: `True` for polygon-based rendering (cell-by-cell colors), `False` for grid rendering (interpolated field on a mesh grid)
- `displayed_field`: Which field to display by default (e.g., `MESH` for geometry outline, or a field name like temperature)
- `colormap`: The color mapping scheme (e.g., `"BuRd"` for blue-red, `"Viridis"`, etc.)

``` python
# Create a ComputeSlave with the MED interface
slave = ComputeSlave(MEDInterface)

# Load the geometry file (MED format)
slave.read_file(med_file_path, GEOMETRY)

# Create the Panel2D with explicit configuration
panel_manual = Panel2D(
    slave=slave,
    name="Manual 2D Panel",
    display_polygons=True,      # Display as polygons (False for grid mode)
    displayed_field=MESH,        # Display geometry outline by default
    colormap="BuRd",             # Colormap: BuRd, Viridis, Plasma, etc.
)

# panel_manual
```

## Step 4: Panel Interactions

The 2D panel supports several interactive features:

- **Zoom/Pan**: Use the toolbar on the right side of the plot
- **Colormap**: Select from available colormaps in the sidebar
- **Field Selection**: Choose which field to display (geometry, temperature, pressure, etc.)
- **Axes Adjustment**: Change the viewing angle (u, v, w axes) in the sidebar

You can also configure update events to react to user interactions. Update events determine when the panel recomputes the visualization:

``` python
from scivianna.enums import UpdateEvent

# Set panel to recompute when user clicks on the plot
panel.update_event = UpdateEvent.CLIC

# Or multiple events
# panel.update_event = [UpdateEvent.CLIC, UpdateEvent.MOUSE_POSITION_CHANGE]

# Available update events:
# - UpdateEvent.CLIC: Recompute on mouse click (useful for cell inspection)
# - UpdateEvent.MOUSE_POSITION_CHANGE: Recompute on every mouse move
# - UpdateEvent.MOUSE_CELL_CHANGE: Recompute only when entering a new cell
# - UpdateEvent.RANGE_CHANGE: Recompute when zoom/pan bounds change
# - UpdateEvent.RECOMPUTE: Manual recompute only (default, no auto-update)
# - UpdateEvent.PERIODIC: Periodic updates for real-time simulation coupling
```

## Step 5: Programmatic Control

You can control the panel programmatically for automation or custom workflows:

``` python
# Change the displayed field
panel.set_field("TEMPERATURE")

# Change the colormap
panel.set_colormap("Viridis")

# Set custom axes coordinates using the new physical coordinate system:
# - origin: Physical 3D position of the slice corner (u_min*u + v_min*v + w_value*w)
# - size_u, size_v: Size of the slice along each axis (u_max - u_min, v_max - v_min)
panel.set_coordinates(
    u=(1.0, 0.0, 0.0),    # Horizontal axis direction vector
    v=(0.0, 1.0, 0.0),    # Vertical axis direction vector
    origin=(0.0, 0.0, 0.5),  # Physical 3D position of slice corner
    size_u=1.0,            # Extent along u axis (u_max - u_min)
    size_v=1.0,            # Extent along v axis (v_max - v_min)
    w_value=0.5,           # Normal axis position (for 3D slicing)
)

# Get available fields for the loaded geometry
available_fields = slave.get_labels()
print(f"Available fields: {available_fields}")
```

## Step 6: Displaying the Panel Outside a Notebook

When running from a regular Python script (not a Jupyter notebook), you can display the panel using these two approaches:

- **`_show_panel()`**: Opens the panel in a local browser window (blocking call)
- **`_serve_panel()`**: Starts a web server accessible from any machine on the network

These functions are available in `scivianna.notebook_tools`:

``` python
from scivianna.notebook_tools import _show_panel, _serve_panel

# To display in a local browser (uncomment to run):
# _show_panel(panel, title="MED Visualizer")

# To serve on the network (uncomment to run):
# _serve_panel(panel, title="MED Visualizer")
# This starts a web server and opens the panel in your browser at the machine's IP address
```

## Summary

In this tutorial, you learned:

1.  How to import scivianna and its core components (`ComputeSlave`, `MEDInterface`, `Panel2D`)
2.  How to create a 2D panel quickly using convenience functions (`get_med_panel`)
3.  How to create a panel manually with full control over display mode, field, and colormap
4.  How to configure update events for interactive recomputation (click, mouse position, cell change, range change)
5.  How to programmatically control the panel (change fields, colormaps, axes coordinates with origin/size system)
6.  How to display the panel outside a notebook using `_show_panel()` or `_serve_panel()`

## Next Steps

- [Tutorial 2: Multiview Panels](./2_multiview_panels.ipynb) - Display multiple panels side by side
- [Tutorial 3: 2D-1D Panel Interactions](./3_panel_2d_1d_interactions.ipynb) - Link 2D geometry views with 1D line plots
