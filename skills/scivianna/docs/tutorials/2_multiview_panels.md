<!-- source: 2_multiview_panels.ipynb -->

# Tutorial 2: Open a Multiview of Panels

This tutorial shows how to display multiple panels simultaneously using scivianna's layout system, including 3D panels.

## Introduction to Layouts

Scivianna provides two layout classes for displaying multiple panels:

| Layout            | Description                                                          |
|-------------------|----------------------------------------------------------------------|
| `SplitLayout`     | Two panels split vertically or horizontally with a draggable divider |
| `GridStackLayout` | Multiple panels in a grid with drag-and-drop rearrangement           |

Panels can be of different types: `Panel1D`, `Panel2D`, or `Panel3D`. They can interact with each other through **UpdateEvents**.

## Step 1: SplitLayout - Two Panels Side by Side

`SplitLayout` divides the screen into two areas. You can split vertically (side by side) or horizontally (top and bottom).

``` python
from pathlib import Path
from scivianna.slave import ComputeSlave
from scivianna.interface.med_interface import MEDInterface
from scivianna.panel.panel_2d import Panel2D
from scivianna.layout.split import SplitLayout, SplitItem, SplitDirection
from scivianna.constants import GEOMETRY
from scivianna.enums import UpdateEvent
import scivianna.input_file

# Path to a built-in example MED file
med_file_path = Path(scivianna.input_file.__file__).parent / "power.med"
```

### Vertical Split (Side by Side)

Creates two panels displayed left and right with a vertical divider.

``` python
# Create two ComputeSlaves
slave1 = ComputeSlave(MEDInterface)
slave2 = ComputeSlave(MEDInterface)

# Load the same file in both slaves (or different files)
slave1.read_file(med_file_path, GEOMETRY)
slave2.read_file(med_file_path, GEOMETRY)

# Create two Panel2D instances with interaction
panel_left = Panel2D(slave=slave1, name="Left Panel", update_event=UpdateEvent.CLIC)
panel_right = Panel2D(slave=slave2, name="Right Panel", update_event=UpdateEvent.CLIC)

# Create a SplitItem defining the layout
split_item = SplitItem(
    panel_1=panel_left,
    panel_2=panel_right,
    direction=SplitDirection.VERTICAL,  # Side by side
)

# Create the SplitLayout
split_layout = SplitLayout(split_item)

# Display
# split_layout
```

### Horizontal Split (Top and Bottom)

Creates two panels displayed one above the other with a horizontal divider.

``` python
# Create the split item with horizontal direction
split_item_h = SplitItem(
    panel_1=panel_left,
    panel_2=panel_right,
    direction=SplitDirection.HORIZONTAL,  # Top and bottom
)

# Create the SplitLayout
split_layout_h = SplitLayout(split_item_h)

# Display
# split_layout_h
```

### SplitLayout Features

- **Draggable divider**: Click and drag the divider to resize panels
- **Panel switching**: Click on panel icons in the sidebar to switch between panels
- **Duplication**: Use the duplicate button to split a panel further (creating nested splits)
- **Save/Restore**: Layouts can be saved to and restored from zip files

## Step 2: Nested Splits - Multiple Panels

`SplitItem` can be nested to create more complex layouts with multiple panels.

``` python
# Create three slaves and panels
slave_a = ComputeSlave(MEDInterface)
slave_b = ComputeSlave(MEDInterface)
slave_c = ComputeSlave(MEDInterface)

slave_a.read_file(med_file_path, GEOMETRY)
slave_b.read_file(med_file_path, GEOMETRY)
slave_c.read_file(med_file_path, GEOMETRY)

panel_a = Panel2D(slave=slave_a, name="Panel A")
panel_b = Panel2D(slave=slave_b, name="Panel B")
panel_c = Panel2D(slave=slave_c, name="Panel C")

# Create nested split item:
#       +----------+----------+
#       |          |          |
#       |  Panel A |  Panel B |
#       |          |          |
#       +----------+----------+
#       |                     |
#       |       Panel C       │
#       |                     |
#       +----------+----------+

inner_split = SplitItem(
    panel_1=panel_a,
    panel_2=panel_b,
    direction=SplitDirection.VERTICAL,  # A | B
)

# Actually for 3 panels we need a different approach:
# Left: Panel A (top/bottom split with Panel C)
# Right: Panel B

nested_split = SplitItem(
    panel_1=inner_split,
    panel_2=panel_c,
    direction=SplitDirection.HORIZONTAL,  # A over C
)

nested_layout = SplitLayout(nested_split)
# nested_layout/
```

## Step 3: GridStackLayout - Multiple Panels in a Grid

`GridStackLayout` provides a more flexible grid-based layout with drag-and-drop rearrangement.

``` python
from scivianna.layout.gridstack import GridStackLayout

# Create four slaves and panels
slaves = [
    ComputeSlave(MEDInterface) for _ in range(4)
]
panels = {}

for i, slave in enumerate(slaves):
    slave.read_file(med_file_path, GEOMETRY)
    panels[f"Grid Panel {i}"] = Panel2D(slave=slave, name=f"Grid Panel {i}")

# Defining the panels bounds:

#       +----------+----------+
#       |          |          |
#       |    0     |    1     |
#       |          |          |
#       +----------+----------+
#       |          |          |
#       |    2     |    3     |
#       |          |          |
#       +----------+----------+
bounds_x = {
    "Grid Panel 0": [0, 4],
    "Grid Panel 1": [5, 9],
    "Grid Panel 2": [0, 4],
    "Grid Panel 3": [5, 9]
}
bounds_y = {
    "Grid Panel 0": [0, 4],
    "Grid Panel 1": [0, 4],
    "Grid Panel 2": [5, 9],
    "Grid Panel 3": [5, 9]
}

# Create a GridStackLayout with the panels
grid_layout = GridStackLayout(
    visualisation_panels = panels,
    bounds_x = bounds_x,
    bounds_y = bounds_y
)

# Display
# grid_layout
```

### GridStackLayout Features

- **Drag-and-drop**: Drag panel borders to resize cells
- **Resizable grid**: Right-click on a cell to adjust rows/columns
- **Panel switching**: Click on panel icons in the sidebar to switch between panels
- **Save/Restore**: Layouts can be saved to and restored from zip files

## Step 4: Save and Restore Layouts

Layouts can be saved to zip files and restored later.

``` python
# Save the layout to a zip file
# split_layout.save_to_zip("my_layout.zip", include_files=True)

# Restore the layout from a zip file
# restored_layout = SplitLayout.restore_from_zip(
#     "my_layout.zip",
#     include_files=True,
# )
```

## Step 5: Synchronized Fields

Multiple panels can synchronize their displayed field when the sync_field argument is set at True.

``` python
# Create two panels sharing the same slave
shared_slave = ComputeSlave(MEDInterface)
shared_slave.read_file(med_file_path, GEOMETRY)

panel_sync1 = Panel2D(slave=shared_slave, name="Sync Panel 1")
panel_sync2 = Panel2D(slave=shared_slave, name="Sync Panel 2")

panel_sync1.sync_field = True
panel_sync2.sync_field = True

# When you change the field in one panel, both update
sync_split = SplitItem(
    panel_1=panel_sync1,
    panel_2=panel_sync2,
    direction=SplitDirection.VERTICAL,
)

sync_layout = SplitLayout(sync_split)
# sync_layout
```

## Step 6: Adding a 3D Panel

Scivianna supports 3D visualization panels that can be mixed with 2D panels in layouts. 3D panels use VTK/pyvista for rendering and support interactive clip planes for slicing geometry.

To use 3D panels, you need the `3d` optional dependency:

``` bash
pip install scivianna[3d]
```

Here's an example of a 2D + 3D layout:

``` python
try:
    from scivianna.panel.panel_3d import Panel3D
    from scivianna.interface.vtk_interface import VTKInterface
    has_3d = True
except ImportError:
    has_3d = False
    print("3D visualization requires the '3d' optional dependency: pip install scivianna[3d]")

if has_3d:
    # Create a 3D panel with VTK data
    slave_3d = ComputeSlave(VTKInterface)
    # slave_3d.read_file("model.vtu", "GEOMETRY")
    
    panel_3d = Panel3D(
        slave=slave_3d,
        name="3D View",
        update_event=UpdateEvent.AXES_CHANGE,  # Send clip plane changes
    )
    
    # 3D panels support keyboard shortcuts:
    # - C: Toggle clip plane
    # - X/Y/Z: Select clip plane axis
    # - Up/Down arrows: Move clip plane position
    
    print("3D panel created successfully!")
    print("Keyboard shortcuts: C (toggle clip), X/Y/Z (axis), Up/Down (move)")
```

## Step 7: Inter-Panel Communication

When panels share a layout, they can communicate through UpdateEvents. Here's how different panel types interact:

| From → To   |           Panel1D           |            Panel2D             |           Panel3D            |
|-------------|:---------------------------:|:------------------------------:|:----------------------------:|
| **Panel1D** |             \-              |  Updates at clicked location   |              \-              |
| **Panel2D** | Updates at clicked location |  Moves slice origin on click   |  Moves clip plane on click   |
| **Panel3D** |             \-              | Updates slice axes on rotation | Moves clip plane on rotation |

### Example: 2D → 3D Interaction

Clicking in a 2D panel moves the 3D clip plane to the clicked position:

``` python
if has_3d:
    # Create a 2D panel that sends click events
    slave_2d = ComputeSlave(MEDInterface)
    slave_2d.read_file(med_file_path, GEOMETRY)
    
    panel_2d = Panel2D(
        slave=slave_2d,
        name="2D Slice",
        update_event=UpdateEvent.CLIC,  # Send clicks
    )
    
    # Create a 3D panel that receives click events
    slave_3d = ComputeSlave(VTKInterface)
    # slave_3d.read_file("model.vtu", "GEOMETRY")
    
    panel_3d = Panel3D(
        slave=slave_3d,
        name="3D View",
        update_event=UpdateEvent.CLIC,  # Receive clicks
    )
    
    # Put them in a split layout - clicking in the 2D panel moves the 3D clip plane
    mixed_split = SplitItem(
        panel_1=panel_2d,
        panel_2=panel_3d,
        direction=SplitDirection.HORIZONTAL,
    )
    
    # mixed_layout = SplitLayout(mixed_split)
    # mixed_layout
```

## Summary

In this tutorial, you learned:

1.  **SplitLayout**: Two-panel layouts with draggable dividers — vertical (side by side) and horizontal (stacked)
2.  **Nested splits**: Building complex multi-panel layouts by nesting `SplitItem` instances
3.  **GridStackLayout**: Flexible multi-panel grids with drag-and-drop resizing and configurable cell bounds
4.  **Save/Restore**: Persisting layout configurations to zip files with `save_to_zip()` and `restore_from_zip()`
5.  **Field synchronization**: Linking field selections across panels using `sync_field=True`
6.  **3D panels**: Adding `Panel3D` to layouts for VTK-based 3D visualization with clip planes
7.  **Inter-panel communication**: Panels interact through `UpdateEvent` — clicking in one panel updates others

## Next Steps

- [Tutorial 3: 2D-1D Panel Interactions](./3_panel_2d_1d_interactions.ipynb) — Link 2D geometry views with 1D line plots
- [Tutorial 4: Developing an Interface (Dev)](./4_develop_interface.ipynb) — Create custom data interfaces
