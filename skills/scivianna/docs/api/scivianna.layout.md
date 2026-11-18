<!-- source: api/scivianna.layout.rst -->

# scivianna.layout package

# Scivianna Layout Module

The `layout` module provides layout managers for arranging multiple visualization panels in flexible, interactive configurations.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `generic_layout.py` | Base class `GenericLayout` with common layout functionality |
| `gridstack.py` | GridStack-based layout manager for draggable, resizable panels |
| `split.py` | Split-pane layout manager for dividing panels horizontally/vertically |

## Layout Managers

### GenericLayout (Base Class)
Provides core functionality for all layout types:
- Panel registration and management
- Frame switching between active panels
- Mouse interaction callbacks (click, hover)
- Field synchronization across panels
- Time widget integration for coupling

### GridStack Layout
Implements a grid-based layout system:
- Panels can be dragged to new positions
- Panels can be resized dynamically
- Supports multiple panels in a single view
- Serializable layout state

### Split Layout
Provides binary split divisions:
- Split horizontally or vertically
- Draggable divider between sections
- Recursive splitting for complex layouts

## Key Features

### Panel Management
```python
from scivianna.layout.split import SplitLayout, SplitItem, SplitDirection

# Create layout with multiple panels
split_panel = SplitLayout(
    SplitItem(
        map_panel,
        line_panel,
        SplitDirection.VERTICAL
    )
)

```

### Frame Switching
Navigate between panels using the frame selector:
```python
layout.set_to_frame("panel1")  # Switch to panel1
layout.current_frame  # Get active panel name
```

### Mouse Interaction Callbacks
The layout handles and distributes mouse events:

| Callback | Trigger |
|----------|---------|
| `on_clic_callback` | User clicks on a plot |
| `mouse_move_callback` | User moves mouse over a plot |
| `field_change_callback` | User changes displayed field |

### Update Events

Panels can be configured to update on different events via `UpdateEvent`:

| Event | Value | Description |
|-------|-------|-------------|
| `UpdateEvent.RECOMPUTE` | 0 | Manual recompute only (default) |
| `UpdateEvent.CLIC` | 1 | Update on mouse click (sends/receives mouse location and cell ID) |
| `UpdateEvent.MOUSE_POSITION_CHANGE` | 2 | Update on mouse move over 2D plot |
| `UpdateEvent.MOUSE_CELL_CHANGE` | 3 | Update when hovered cell changes on 2D plot |
| `UpdateEvent.PERIODIC` | 4 | Periodic updates for real-time simulation coupling |
| `UpdateEvent.RANGE_CHANGE` | 5 | Update when zoom/pan bounds change (2D) or clip plane origin changes (3D) |
| `UpdateEvent.AXES_CHANGE` | 6 | Update when axes orientation or origin changes (2D axes or 3D clip plane) |

### Time Widget Integration
For coupled simulations, add time management:
```python
layout.add_time_widget()  # Adds play/pause and time navigation
```

## Synchronization

Panels can be synchronized to update together:
```python
# Enable field sync - changing field in one panel updates others
panel.sync_field = True
```

## Periodic Updates

For real-time coupling, enable periodic refresh (updates only if changes were done using the Icoco coupling interface):
```python
layout.add_periodic_update()  # Start 100ms refresh loop
layout.stop_periodic_update()  # Stop refresh
```

## Inter-Panel Communication

When panels share a layout and have compatible `update_event` settings, they can communicate:

1. **2D → 2D**: Clicking in one panel moves the slice origin in others
2. **2D → 3D**: Clicking in a 2D panel moves the 3D clip plane
3. **3D → 2D**: Rotating/panning the 3D view updates 2D slice axes
4. **3D → 3D**: Clip plane changes propagate between 3D panels
5. **2D → 1D**: Clicking or moving in one panel changes the plot location/cell id data
6. **3D → 1D**: Clicking or moving in one panel changes the plot location/cell id data Submodules ----------

## scivianna.layout.generic_layout module

Generic layout for Scivianna visualization panels.

This module provides the base layout class for arranging multiple visualization panels.

### `class scivianna.layout.generic_layout.GenericLayout(visualisation_panels: Dict[str, VisualizationPanel])`

Base layout arranging several VisualizationPanels, with a shared extensions sidebar.

#### `GenericLayout.register_panel(self, panel: VisualizationPanel)`

Registers a panel in the layout: wires its callbacks and adds its extension buttons to the shared sidebar.

## Parameters

panel : VisualizationPanel  
Panel to register

#### `GenericLayout.change_code_interface(self, event)`

Replaces the panel to one linked to the code interface

## Parameters

event : Any  
Event to make the function linkable to the gridstack

#### `GenericLayout.change_current_frame(self, *args, **kwargs)`

Swap the the active panel

## Parameters

event : Any  
Event to make the function linkable to the gridstack

#### `GenericLayout.set_to_frame(self, frame_name: str)`

Updates the Select widget to the active panel

## Parameters

frame_name : str  
Name of the active panel

## Raises

ValueError  
The provided name is not in the Select options

#### `GenericLayout.outline_panels(self, *args, **kwargs)`

Updates the figures outline colors

#### `GenericLayout.duplicate(self, horizontal: bool)`

Split the panel, the new panel is a copy of the first, all panels are duplicated.

## Parameters

horizontal : bool  
Whether the cut should be horizontal or vertical

#### `GenericLayout.get_panel(self, panel_name: str) -> VisualizationPanel`

Returns the VisualizationPanel associated to the given name

## Parameters

panel_name : str  
Name of the panel

## Returns

VisualizationPanel  
Requested panel

## Raises

ValueError  
No panel at the given name

#### `GenericLayout.set_panel(self, panel_name: str, panel: VisualizationPanel)`

Updates the VisualizationPanel associated to the given name

## Parameters

panel_name : str  
Name of the panel

panel:VisualizationPanel  
New panel value

#### `GenericLayout.stop_periodic_update(self)`

Stops the periodic task that automatically updates the plots.

#### `GenericLayout.add_periodic_update(self)`

Starts a periodic task (every 100 ms) to automatically update the plots.

#### `GenericLayout.recompute(self)`

Schedules updates on marked panels via add_next_tick_callback.

#### `GenericLayout.recompute_all(self)`

Marks all panels to recompute, and calls the recompute function.

#### `GenericLayout.mark_to_recompute(self, panels_to_recompute)`

Marks the given panels to be recomputed on the next update.

## Parameters

panels_to_recompute : List\[str\]  
Names of the panels to recompute

#### `GenericLayout.on_clic_callback(self, screen_location: Tuple[float, float], space_location: Tuple[float, float, float], cell_id: Union[str, int])`

Function called when the user clicks on a plot.

Panels whose update event is CLIC are recomputed at the clicked location.

## Parameters

screen_location : Tuple\[float, float\]  
Mouse location on screen

space_location : Tuple\[float, float, float\]  
Mouse targeted location in space

cell_id : Union\[str, int\]  
Currently hovered cell

#### `GenericLayout.mouse_move_callback(self, screen_location: Tuple[float, float], space_location: Tuple[float, float, float], cell_id: Union[str, int])`

Function called when the mouse moves on the plot

## Parameters

screen_location : Tuple\[float, float\]  
Mouse location on screen

space_location : Tuple\[float, float, float\]  
Mouse targeted location in space

cell_id : Union\[str, int\]  
Currently hovered cell

#### `GenericLayout.field_change_callback(self, new_field: str)`

Function calling panels update a field change

## Parameters

new_field : str  
New field to set

#### `GenericLayout.on_axes_change_callback(self, u: np.ndarray, v: np.ndarray, origin: Tuple[float, float, float]=None, size_u: float=None, size_v: float=None)`

Function calling panels update when axes change.

## Parameters

u : np.ndarray  
u axis direction vector

v : np.ndarray  
v axis direction vector

origin : Tuple\[float, float, float\], optional  
Physical 3D position of the slice center

size_u : float, optional  
Size of the slice along the u axis

size_v : float, optional  
Size of the slice along the v axis

#### `GenericLayout.add_time_widget(self)`

Adds a time management widget to the layout

#### `GenericLayout.toggle_outlines(self, *args, **kwargs)`

Function called when the sidebar is opened or closed, edits the frames visibility.

#### `GenericLayout.button_change_to_frame(self, event, frame_name: str)`

Triggers a frame change from clicking on a button

## Parameters

event : Any  
Bokeh triggering event

frame_name : str  
Frame to change to

#### `GenericLayout.show(self, *args, **kwargs)`

Shows the layout in a browser window.

#### `GenericLayout.servable(self, *args, **kwargs)`

Serves the layout on a web server.

#### `GenericLayout.open_time_panel(self)`

Changes current GUI to the coupling extension scivianna.layout.gridstack module ---------------------------------

GridStackLayout - layout arranging visualization panels on a resizable grid.

### `class scivianna.layout.gridstack.GridStackLayout(visualisation_panels: Dict[str, VisualizationPanel], bounds_x: Dict[str, Tuple[int]], bounds_y: Dict[str, Tuple[int]])  — bases: GenericLayout`

Layout arranging several VisualizationPanels on a resizable grid.

#### `GridStackLayout.change_code_interface(self, event)`

Replaces the current panel with one linked to the new code interface and rebuilds the grid.

## Parameters

event : Any  
Event to make the function linkable to the gridstack

#### `GridStackLayout.change_current_frame(self, *args, **kwargs)`

Swap the the active panel

## Parameters

event : Any  
Event to make the function linkable to the gridstack

#### `GridStackLayout.get_grid(self) -> CustomGridStack`

Returns the gridstack object

## Returns

GridStack  
Currently displayed gridstack

#### `GridStackLayout.enable_disable_pan(self)`

Enable - disable figure panning

#### `GridStackLayout.make_grid_stack(self)`

Updates the displayed gridstack object (called after a panel split/delete)

#### `GridStackLayout.disable_figures_pan(self)`

Disable all figures pan

#### `GridStackLayout.enable_figures_pan(self)`

Enable all figures pan

#### `GridStackLayout.duplicate(self, horizontal: bool)`

Split the panel, the new panel is a copy of the first, all panels are duplicated.

## Parameters

horizontal : bool  
Whether the cut should be horizontal or vertical

#### `GridStackLayout.reset_interface(self)`

Rebuilds the interface based on up-to-date bounds

#### `GridStackLayout.save_to_zip(self, file_path: Union[str, Path], include_files: bool=True) -> Path`

Saves the GridStackLayout configuration and slave data to a zip file.

The zip file contains: - layout.json: JSON file describing the layout structure, current frame, bounds, and for each panel: slave info and associated interface name - data/: Folder containing serialized data for each slave

## Parameters

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

#### `GridStackLayout.restore_from_zip(cls, file_path: Union[str, Path], include_files: bool=True) -> 'GridStackLayout'`

Restores a GridStackLayout from a zip file.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

GridStackLayout  
Restored GridStackLayout instance scivianna.layout.split module -----------------------------

SplitLayout - layout arranging visualization panels in nested resizable splits.

### `class scivianna.layout.split.SplitDirection  — bases: Enum`

Enum defining the direction of the split.

### `class scivianna.layout.split.SplitItem`

One node of the split tree: two panels (or sub-splits) and their divider.

### `class scivianna.layout.split.SplitLayout(split_item: SplitItem)  — bases: GenericLayout`

Layout arranging several VisualizationPanels in nested resizable splits.

#### `SplitLayout.change_code_interface(self, event)`

Replaces the current panel with one linked to the new code interface and rebuilds the splits.

## Parameters

event : Any  
Event to make the function linkable to the split

#### `SplitLayout.current_split_item(self, panel_name: str, item: Union[SplitItem, VisualizationPanel]) -> Tuple[Union[SplitItem, VisualizationPanel], int]`

Recursively looks for a VisualizationPanel named panel_name in the given item

## Parameters

panel_name : str  
Panel name to find

item : Union\[SplitItem, VisualizationPanel\]  
Intricated item in which find the panel

## Raises

TypeError  
provided split_item is neither a SplitItem or a VisualizationPanel

#### `SplitLayout.build_split_item(self, split_item: Union[SplitItem, VisualizationPanel]) -> Union[SplitJSVertical, SplitJSHorizontal]`

Converts a SplitItem object in its Viewable counterpart

## Parameters

split_item : SplitItem  
SplitItem to convert in its GUI version

## Returns

Union\[SplitJSVertical, SplitJSHorizontal\]  
GUI element to display in self.main_frame

## Raises

TypeError  
provided split_item is neither a SplitItem or a VisualizationPanel

#### `SplitLayout.update_interface_in_split_item(self, panel_name: str, new_panel: VisualizationPanel, split_item: Union[SplitItem, VisualizationPanel])`

Replaces a panel in the split item object

## Parameters

panel_name : str  
Panel name

new_panel : VisualizationPanel  
New visualization panel

split_item : Union\[SplitItem, VisualizationPanel\]  
SplitItem in which replace the panel

## Raises

TypeError  
provided split_item is neither a SplitItem or a VisualizationPanel

#### `SplitLayout.get_panels_dict(self, split_item: SplitItem) -> Dict[str, VisualizationPanel]`

Returns all provided VisualizationPanels in a dictionnary

## Parameters

split_item : SplitItem  
SplitItem recursively containing VisualizationPanels

## Returns

Dict\[str, VisualizationPanel\]  
VisualizationPanels dictionnary

#### `SplitLayout.reset_interface(self)`

Rebuilds the interface based on up-to-date SplitItem

#### `SplitLayout.duplicate(self, horizontal: bool)`

Split the panel, the new panel is a copy of the first, all panels are duplicated.

## Parameters

horizontal : bool  
Whether the cut should be horizontal or vertical

#### `SplitLayout.save_to_zip(self, file_path: Union[str, Path], include_files: bool=True)`

Saves the layout configuration and slave data to a zip file.

The zip file contains: - layout.json: JSON file describing the layout structure, current frame, and for each slave: panel name, slave info, and associated interface name - data/: Folder containing serialized data for each slave

## Parameters

file_path : Union\[str, Path\]  
Path to the zip file to create

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the created zip file

#### `SplitLayout.restore_from_zip(cls, file_path: Union[str, Path], include_files: bool=True) -> 'SplitLayout'`

Restores a SplitLayout from a zip file.

## Parameters

file_path : Union\[str, Path\]  
Path to the zip file to restore from

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

SplitLayout  
Restored SplitLayout instance Module contents ---------------

Layout package: classes for arranging several visualization panels in a displayable layout.
