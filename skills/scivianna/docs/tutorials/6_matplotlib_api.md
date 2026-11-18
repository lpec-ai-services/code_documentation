<!-- source: 6_matplotlib_api.ipynb -->

# Tutorial 6: Matplotlib API for 2D Visualization

While scivianna's primary visualization is built on **Panel** and **Bokeh** for interactive web-based displays, the library also provides a **Matplotlib-based API** for generating static publication-quality plots, integrating with traditional Python scientific workflows, or embedding visualizations in notebooks without a Bokeh server.

## When to Use the Matplotlib API

| Use Case                              | Recommended Approach                 |
|---------------------------------------|--------------------------------------|
| Interactive web dashboard             | Panel + Bokeh (Panel2D)              |
| Static figure for publication         | Matplotlib API                       |
| Batch processing / automated reports  | Matplotlib API                       |
| Jupyter notebook without Bokeh server | Matplotlib API                       |
| Custom multi-panel layouts            | Matplotlib API + matplotlib gridspec |

## Setup

First, import the necessary modules:

``` python
import matplotlib.pyplot as plt
from pathlib import Path

import scivianna.input_file
from scivianna.interface.med_interface import MEDInterface
from scivianna.slave import ComputeSlave
from scivianna.plotter_2d.api import plot_frame, plot_frame_in_axes
```

## Loading Data

The Matplotlib API works with a **ComputeSlave** (or a **Geometry2D** interface). The ComputeSlave wraps an interface and handles data communication. Let's load a MED file:

``` python
# Create a ComputeSlave with the MED interface
slave = ComputeSlave(MEDInterface)

# Load the geometry file (using the bundled test file)
from scivianna.constants import GEOMETRY, MESH
input_file_path = Path(scivianna.input_file.__file__).parent / 'power.med'

if input_file_path.exists():
    slave.read_file(input_file_path, GEOMETRY)
    print(f"Loaded: {input_file_path}")
else:
    print(f"File not found: {input_file_path}")
    print("Please provide a valid .med file path in the next cell.")
```

## Basic Plotting

The simplest way to create a plot is using `plot_frame()`. It creates a new figure and axes, then plots the geometry:

``` python
# Create a basic plot
# coloring_label specifies which field to use for coloring the polygons
print("Available fields :", slave.get_labels())
fig, ax = plot_frame(
    slave=slave,
    coloring_label='INTEGRATED_POWER',  # Field name to color by
    color_map='BuRd',           # Colormap for numeric fields
    edge_width=0.5              # Line width for polygon edges
)

ax.set_title('2D Geometry - Material Distribution')
fig.tight_layout()
plt.show()
```

## Plotting on Existing Axes

For more control, use `plot_frame_in_axes()` to plot onto an existing matplotlib axis. This is useful for custom layouts:

``` python
# Create a figure with multiple subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot on the left axis - using INTEGRATED_POWER field
plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=axes[0],
    edge_width=0.5
)
axes[0].set_title('Power distribution')

# Plot on the right axis - using a different field (if available)
# Try with MESH label for geometry-only view
plot_frame_in_axes(
    slave=slave,
    coloring_label=MESH,
    axes=axes[1],
    edge_width=0.5
)
axes[1].set_title('Geometry Zones')

fig.tight_layout()
plt.show()
```

## Coloring Options

### Numeric Fields with Colormaps

For numeric fields, you can specify a colormap and value range:

``` python
# Numeric field with colormap
fig, ax = plt.subplots(figsize=(8, 6))

plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',  # Example numeric field name
    axes=ax,
    color_map='viridis',           # Any matplotlib colormap
    display_colorbar=True,         # Show colorbar for numeric fields
    edge_width=0.3
)

ax.set_title('Numeric Field - Power (example)')
fig.tight_layout()
plt.show()
```

## Projection Axes (u, v) and Slice Position

3D geometries can be projected onto a 2D plane defined by director vectors **u** and **v**. The slice position is controlled via the **origin** (physical 3D position of the slice corner) and the **size_u**/ **size_v** extents (the visible window size along each axis).

Note: The matplotlib API does not expose a `w_value` parameter directly. Instead, use `origin` to position the slice in 3D space:

``` python
# Different projection planes
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# View along X axis (u=X, v=Y)
from scivianna.constants import X, Y, Z

plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=axes[0],
    u=X, v=Y,              # Director vectors for the projection plane
    origin=(0.0, 0.0, 0.0), # Physical 3D position of slice corner
    size_u=1.0,             # Extent along u axis
    size_v=1.0,             # Extent along v axis
    edge_width=0.5
)
axes[0].set_title('XY Plane')

# View along Y axis
plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=axes[1],
    u=Y, v=Z,
    origin=(0.0, 0.0, 0.0),
    size_u=1.0,
    size_v=1.0,
    edge_width=0.5
)
axes[1].set_title('YZ Plane')

# View along Z axis
plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=axes[2],
    u=X, v=Z,
    origin=(0.0, 0.0, 0.0),
    size_u=1.0,
    size_v=1.0,
    edge_width=0.5
)
axes[2].set_title('XZ Plane')

fig.tight_layout()
```

## Advanced: Multi-Panel Layout with Colorbars

Create a sophisticated multi-panel figure with proper colorbars and legends:

``` python
# Create a complex layout
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Main view (large, top-left)
ax_main = fig.add_subplot(gs[0:2, 0:2])
plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=ax_main,
    edge_width=0.8
)
ax_main.set_title('Main View - Power Distribution')

# Detail views (smaller, right side)
ax_detail1 = fig.add_subplot(gs[0, 2])
plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=ax_detail1,
    edge_width=0.3
)
ax_detail1.set_title('View 1')

ax_detail2 = fig.add_subplot(gs[1, 2])
plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=ax_detail2,
    edge_width=0.3
)
ax_detail2.set_title('View 2')

# Bottom row for additional fields
ax_bottom = fig.add_subplot(gs[2, :])
plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=ax_bottom,
    edge_width=0.5
)
ax_bottom.set_title('Full Domain')

plt.show()
```

## Saving Figures

Matplotlib figures can be saved in any format supported by matplotlib:

``` python
# Create and save a figure
fig, ax = plt.subplots(figsize=(10, 8))

plot_frame_in_axes(
    slave=slave,
    coloring_label='INTEGRATED_POWER',
    axes=ax,
    edge_width=0.8
)
ax.set_title('2D Geometry - Material Distribution')
fig.tight_layout()

# Save in various formats
output_dir = Path(".").parent / 'outputs'
output_dir.mkdir(exist_ok=True)

fig.savefig(output_dir / 'geometry_material.png', dpi=150, bbox_inches='tight')
print(f"Saved PNG to: {output_dir / 'geometry_material.png'}")
```

## API Reference

### `plot_frame()`

Creates a new figure and plots geometry on it.

| Parameter          | Type                          | Default   | Description                              |
|--------------------|-------------------------------|-----------|------------------------------------------|
| `slave`            | ComputeSlave / Geometry2D     | \-        | Data source                              |
| `coloring_label`   | str                           | \-        | Field name to color by                   |
| `u`                | Tuple\[float, float, float\]  | X         | Horizontal director vector               |
| `v`                | Tuple\[float, float, float\]  | Y         | Vertical director vector                 |
| `origin`           | Tuple\[float, float, float\]  | (0, 0, 0) | Physical 3D position of the slice corner |
| `size_u`           | float                         | 1\.       | Size of the slice along the u axis       |
| `size_v`           | float                         | 1\.       | Size of the slice along the v axis       |
| `color_map`        | str                           | "BuRd"    | Matplotlib colormap name                 |
| `display_colorbar` | bool                          | False     | Show colorbar                            |
| `edge_width`       | float                         | 1\.       | Polygon edge line width                  |
| `custom_colors`    | Dict\[str, Dict\[str, str\]\] | {}        | Custom HTML colors per field value       |
| `rename_values`    | Dict\[str, Dict\[str, str\]\] | {}        | Rename values in legend                  |
| `legend_options`   | Dict\[str, Any\]              | {}        | Options for `ax.legend()`                |
| `polygonize`       | bool                          | True      | Plot as polygons (vs grid)               |
| `options`          | Dict                          | {}        | Extra computation options                |
| `plot_options`     | Dict                          | {}        | Passed to plotter                        |

**Returns:** `(plt.Figure, matplotlib.axes.Axes)`

### `plot_frame_in_axes()`

Plots geometry onto an existing matplotlib axis. Same parameters as `plot_frame()` plus:

| Parameter | Type                 | Description              |
|-----------|----------------------|--------------------------|
| `axes`    | matplotlib.axes.Axes | Target axis for plotting |

**Returns:** None

## Next Steps

This tutorial covered the Matplotlib-based static plotting API in scivianna. For interactive visualization, see:

- [Tutorial 1: Simple 2D Panel](./1_simple_2d_panel.ipynb) - Interactive Bokeh-based panels
- [Tutorial 2: Multiview Panels](./2_multiview_panels.ipynb) - Multiple synchronized views
- [Tutorial 3: 2D-1D Panel Interactions](./3_panel_2d_1d_interactions.ipynb) - Cross-panel interactions

For development, see:

- [Tutorial 4: Developing an Interface](./4_develop_interface.ipynb)
- [Tutorial 5: Developing an Extension](./5_develop_extension.ipynb)
