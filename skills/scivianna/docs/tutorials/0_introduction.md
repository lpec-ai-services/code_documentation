<!-- source: 0_introduction.ipynb -->

# Introduction to scivianna

This tutorial introduces the basic concepts of the **scivianna** library, a Python toolkit for visualizing and interacting with simulation data.

## What is scivianna?

scivianna provides:

- **Panel-based layouts**: Organize multiple visualizations in flexible grid or split layouts
- **1D visualization**: Display temporal data from simulation channels
- **2D visualization**: Plot 2D geometries, meshes, field slices, and polygon data
- **3D visualization**: Render VTK-based 3D geometry with interactive clip planes
- **Inter-plot interactions**: Link selections, clicks, and views across multiple panels
- **Real-time coupling**: Connect to simulations via C3PO/ICOCO for live data updates
- **Extension system**: Customize behavior with plugin architectures

## Installation

``` bash
pip install scivianna
```

### Optional Features

``` bash
# MED file support (MEDCoupling)
pip install scivianna[medcoupling]

# 3D visualization (PyVista/VTK)
pip install scivianna[3d]

# AI agent support
pip install scivianna[agent]

# Code coupling (C3PO)
pip install scivianna[coupling]
```

## Quick Start

``` python
from scivianna.slave import ComputeSlave
from scivianna.panel.panel_2d import Panel2D
from scivianna.enums import UpdateEvent

# Create a slave with your data interface
slave = ComputeSlave(YourInterface)
slave.read_file("data.med", "GEOMETRY")

# Create a 2D panel with update-on-click behavior
panel = Panel2D(
    slave=slave,
    name="My View",
    update_event=UpdateEvent.CLIC,
)

# Display the panel
panel.show()
```

## Key Components

| Component         | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| `Panel2D`         | 2D visualization panel for geometries, slices, and fields                     |
| `Panel3D`         | 3D visualization panel for VTK-based geometry with clip planes                |
| `Panel1D`         | 1D temporal data viewer for line charts and time series                       |
| `ComputeSlave`    | Computation engine that manages data processing and interface communication   |
| `GridStackLayout` | Grid-based layout manager for draggable, resizable panels                     |
| `SplitLayout`     | Split-pane layout manager for dividing panels horizontally/vertically         |
| `Extension`       | Base class for custom panel extensions                                        |
| `UpdateEvent`     | Enum defining what triggers panel updates (CLIC, MOUSE_POSITION_CHANGE, etc.) |

## Panel Interactions

Panels can interact with each other through **UpdateEvents**. When panels are placed in the same layout:

- **Clicking** in a 2D panel moves slice origins in other 2D panels and clip planes in 3D panels
- **Hovering** over cells updates linked panels with cell information
- **Zooming/panning** can propagate range changes between panels
- **Rotating** a 3D view can update 2D slice axes

## Next Steps

Continue with Tutorial 1 to create your first 2D panel visualization.
