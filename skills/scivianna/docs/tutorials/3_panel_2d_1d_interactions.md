<!-- source: 3_panel_2d_1d_interactions.ipynb -->

# Tutorial 3: Open Two Panels with 2D-1D Interactions

This tutorial shows how to create a coupled 2D + 1D panel setup where interacting with the 2D map panel updates the 1D time-series panel.

## Introduction

Scivianna supports **cross-panel interactions** where selecting a region on the 2D map panel triggers updates in the 1D panel. This is useful for:

- Showing a geographic map with time-series data that updates when you click on a country
- Linking spatial selection to temporal data visualization
- Synchronizing multiple views of the same dataset

## UpdateEvent System

Panel interactions are controlled by the `UpdateEvent` enum. Each panel can be configured to **send** events (when user interacts) and **receive** events (triggering updates from other panels):

| Event                   | Value | Description                              |
|-------------------------|-------|------------------------------------------|
| `RECOMPUTE`             | 0     | Manual recompute only (default)          |
| `CLIC`                  | 1     | Send/receive mouse click events          |
| `MOUSE_POSITION_CHANGE` | 2     | Send/receive mouse move events           |
| `MOUSE_CELL_CHANGE`     | 3     | Send/receive cell hover events           |
| `PERIODIC`              | 4     | Periodic updates for simulation coupling |
| `RANGE_CHANGE`          | 5     | Send/receive zoom/pan range changes      |
| `AXES_CHANGE`           | 6     | Send/receive axes/orientation changes    |

### Interaction Flow

1.  **Sender panel**: Configured with an `update_event` — when the user interacts (clicks, moves mouse), the panel sends event data
2.  **Receiver panel**: Also configured with a matching `update_event` — when it receives event data, it updates its visualization accordingly

## Step 1: Basic Setup

Import the necessary modules and configure the panels using the Europe Grid example.

``` python
from scivianna.slave import ComputeSlave
from scivianna.panel.panel_2d import Panel2D
from scivianna.panel.panel_1d import Panel1D
from scivianna.layout.split import SplitLayout, SplitItem, SplitDirection
from scivianna.enums import UpdateEvent
from pathlib import Path

# Import the Europe Grid interfaces
from scivianna_example.europe_grid.europe_grid import EuropeGridInterface
from scivianna_example.europe_grid.country_time_series import CountryTimeSeriesInterface
```

## Step 2: Create the 2D Map Panel

Create a `ComputeSlave` with the `EuropeGridInterface` and configure the 2D panel to display a geographic map of Europe.

``` python
# Create the ComputeSlave for the 2D map
slave_map = ComputeSlave(EuropeGridInterface)

# Load the time series data linked to the map
time_series_path = str(Path(__file__).parent.parent / 'src' / 'scivianna_example' / 'europe_grid' / 'time_series.csv')
slave_map.read_file(time_series_path, "TimeSeries")

# Create the 2D panel (map)
map_panel = Panel2D(
    slave=slave_map,
    name="Map",
    display_polygons=True,
)

# Set the field to display (e.g., 'solar_pv')
map_panel.set_field("solar_pv")

# Configure update event for mouse cell changes
map_panel.sync_field = True

print(f"2D Panel field: {map_panel.field}")
```

## Step 3: Create a 1D Panel for Time-Series

Create a separate `ComputeSlave` with the `CountryTimeSeriesInterface` for the 1D time-series panel. This panel will display data for the selected country.

``` python
# Create the ComputeSlave for time series data
slave_result = ComputeSlave(CountryTimeSeriesInterface)
slave_result.read_file(time_series_path, "TimeSeries")

# Create the 1D panel (plot)
line_panel = Panel1D(
    slave=slave_result,
    name="Plot",
)

# Set update event to react when the selected cell changes in the 2D map
line_panel.update_event = UpdateEvent.MOUSE_CELL_CHANGE
line_panel.sync_field = True
line_panel.set_field("solar_pv")

print(f"1D Panel update event: {line_panel.update_event}")
```

## Step 4: Create a Coupled Layout

Combine the 2D map panel and 1D time-series panel in a `SplitLayout`. The `sync_field` setting ensures both panels stay synchronized on the selected field.

``` python
# Create the split layout (vertical arrangement: map on top, plot below)
split_item = SplitItem(
    panel_1=map_panel,
    panel_2=line_panel,
    direction=SplitDirection.VERTICAL,
)

# Create the coupled layout
coupled_layout = SplitLayout(
    split_item
)

# Display the layout
coupled_layout
```

### How the Interaction Works

When you **click on a country** in the 2D map panel:

1.  The `MOUSE_CELL_CHANGE` event is triggered with the selected country's cell ID
2.  The 1D panel receives this update and queries the time-series data for that country
3.  The plot updates to show the time-series for the selected country

The `sync_field = True` setting ensures both panels use the same field (e.g., `solar_pv`).

## Summary

In this tutorial, you learned:

1.  How to create a 2D map panel using `EuropeGridInterface` with polygon display
2.  How to create a 1D time-series panel using `CountryTimeSeriesInterface`
3.  How to configure update events (`MOUSE_CELL_CHANGE`) to link panels together
4.  How to use `SplitLayout` to arrange multiple panels in a coupled layout
5.  How cross-panel interactions work: clicking a country on the map updates the time-series plot

## Key Components Used

- **`EuropeGridInterface`**: Handles 2D geographic data for European countries
- **`CountryTimeSeriesInterface`**: Handles time-series data for countries
- **`Panel2D`**: Displays the geographic map with country polygons
- **`Panel1D`**: Displays time-series plots for selected regions
- **`SplitLayout`**: Combines panels in a vertical or horizontal arrangement

## Next Steps

- [Tutorial 4: Developing an Interface (Dev)](./4_develop_interface.ipynb)
- [Tutorial 5: Developing an Extension (Dev)](./5_develop_extension.ipynb)
