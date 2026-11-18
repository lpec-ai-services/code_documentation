<!-- source: api/scivianna.panel.rst -->

# scivianna.panel package

# Scivianna Panel Module

The `panel` module provides the core visualization panel classes that display and interact with simulation data. Panels are the primary user interface for visualizing 1D, 2D, and 3D data in Scivianna.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `visualisation_panel.py` | Base class `VisualizationPanel` for all panel types |
| `panel_1d.py` | 1D plot panel for line charts and time series |
| `panel_2d.py` | 2D plot panel for geometry visualization (polygons, grids) |
| `panel_3d.py` | 3D plot panel for VTK-based volumetric visualization |
| `panel_graph.py` | Graph plot panel displaying a set of 2D nodes connected by links (coupling topology) |
| `panel_dataframe.py` | DataFrame panel for displaying pandas DataFrames |
| `gui.py` | GUI manager for panel controls and sidebars |
| `demo.py` | Demonstrator application with example panels |

## VisualizationPanel Class

The `VisualizationPanel` is the base class for all visualization panels:

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `panel_name` | str | Name identifier for the panel |
| `slave` | ComputeSlave | Data slave providing geometry and field data |
| `plotter` | Plotter2D / Plotter3D | Plotting backend (Bokeh/Matplotlib for 2D, VTK.js for 3D) |
| `main_frame` | pmui.Container | Main display container |
| `extensions` | List[Extension] | Attached extension components |
| `figure` | Overlay | Figure with overlay controls |
| `current_data` | DataContainer (Data1D / Data2D / Data3D) | Currently displayed data |
| `update_event` | UpdateEvent | Event triggering panel updates |
| `sync_field` | bool | Whether to sync fields with other panels |

### Key Methods

| Method | Purpose |
|--------|---------|
| `recompute()` | Refresh the panel display |
| `get_slave()` | Return the data slave |
| `duplicate()` | Create a copy of the panel |
| `set_field(field_name)` | Change displayed field |
| `set_colormap(colormap)` | Change color map |
| `outline_color(color)` | Set border color |
| `provide_on_clic_callback(fn)` | Register click handler |
| `provide_on_mouse_move_callback(fn)` | Register mouse move handler |
| `recompute_at(position, cell_id)` | Trigger recompute at location |

## Panel Types

### Panel1D
Displays one-dimensional data:
- Line charts
- Time series plots

### Panel2D
Displays two-dimensional geometries:
- Mesh visualizations (polygon or grid rendering)
- Field color maps
- 2D slices from 3D geometry
- Supports zoom, pan, and interactive clipping

### Panel3D
Displays three-dimensional VTK-based geometry:
- PolyData and UnstructuredGrid visualization
- Interactive clip planes for slicing
- 3D camera controls (rotate, pan, zoom)
- Color mapping on 3D cell values
- Keyboard shortcuts: `C` (toggle clipping), `X`/`Y`/`Z` (clip axis)

### PanelGraph
Displays a graph of 2D plots connected by directed links (work in progress):
- Each node renders a `Data2D` payload at its layout position
- Directed links show how data flows between nodes (coupling topology)
- Rendered by a `PlotterGraph` backend

### PanelDataFrame
Displays pandas DataFrames in an interactive table view:
- Linked to 2/3DD panels via `MOUSE_CELL_CHANGE` events
- Automatically updates when hovering over cells in a linked geometry panel

## UpdateEvent System

Panels can interact with each other through **UpdateEvents**. When panels are placed in the same layout, events from one panel can trigger updates in others.

### Available Events

| Event | Value | Description |
|-------|-------|-------------|
| `RECOMPUTE` | 0 | Manual recompute only (default, no auto-update) |
| `CLIC` | 1 | Update on mouse click (sends/receives mouse location and cell ID) |
| `MOUSE_POSITION_CHANGE` | 2 | Update on mouse move over 2D plot |
| `MOUSE_CELL_CHANGE` | 3 | Update when mouse enters a new cell on 2D plot |
| `PERIODIC` | 4 | Periodic updates for real-time simulation coupling |
| `RANGE_CHANGE` | 5 | Update when zoom/pan bounds change on 2D plot |
| `AXES_CHANGE` | 6 | Update when axes orientation or origin changes |

### Inter-Panel Communication

Panels can send and receive events based on their type:

#### Sending Panel

| Event | Panel1D | Panel2D | Panel3D |
|-------|:-------:|:-------:|:-------:|
| CLIC | - | Sends mouse location and cell ID on click | Sends mouse location and cell ID on click |
| MOUSE_POSITION_CHANGE | - | Sends mouse location and cell ID on mouse move | Sends mouse location and cell ID on mouse move |
| MOUSE_CELL_CHANGE | - | Sends mouse location and cell ID on hovered cell | Sends mouse location and cell ID on hovered cell |
| RANGE_CHANGE | - | Sends frame center and size on zoom/drag | - |
| AXES_CHANGE | - | Sends new axes on axes change | Sends clip plane origin and axes on translation/rotation |

#### Receiving Panel

| Event | Panel1D | Panel2D | Panel3D |
|-------|:-------:|:-------:|:-------:|
| CLIC | Updates at mouse location/cell ID | Updates moving origin to mouse location | Moves clip plane to new origin |
| MOUSE_POSITION_CHANGE | Updates at mouse location/cell ID | Updates moving origin to mouse location | Moves clip plane to new origin |
| MOUSE_CELL_CHANGE | Updates at mouse location/cell ID | Updates moving origin to mouse location | Moves clip plane to new origin |
| RANGE_CHANGE | - | Updates for new origin/range | Moves clip plane to new origin |
| AXES_CHANGE | - | Updates for new origin/axes | Moves clip plane to new origin/axes |

## GUI Integration

Each panel includes a GUI manager (`gui.py`) that handles:
- Extension buttons and sidebars
- Drawer navigation
- Active extension tracking
- Button visibility management

## Usage Example

```python
from scivianna.panel.panel_2d import Panel2D
from scivianna.slave import ComputeSlave
from scivianna.interface.med_interface import MEDInterface
from scivianna.enums import UpdateEvent

# Create slave with interface
slave = ComputeSlave(MEDInterface)
slave.read_file("result.med")

# Create panel with extensions and update event
panel = Panel2D(
    slave=slave,
    name="Temperature View",
    update_event=UpdateEvent.CLIC,  # Update on click
)

# Display the panel
panel.show()
```

## Event Handling

Panels respond to user interactions:
- **Mouse click**: Trigger `on_mouse_clic` callbacks
- **Mouse hover**: Trigger `on_mouse_move` callbacks
- **Field change**: Update all synced panels
- **Zoom/Pan**: Trigger `RANGE_CHANGE` events if configured
- **Axes/Clip changes**: Trigger `AXES_CHANGE` events if configured

## Serialization

Panels can be serialized for save/load:
```python
# Save panel state
state = panel.to_json()

# Restore panel
restored_panel = Panel2D.from_json(state, data_container)
``` Submodules ----------

## scivianna.panel.demo module

Demo components: a multi-app demonstrator and the overlay it displays apps in.

### `class scivianna.panel.demo.DemoOverlay  — bases: ReactiveHTML`

Component that displays a menu overlaid on top of a background app.

### `class scivianna.panel.demo.Demonstrator(guis: Dict[str, Union[VisualizationPanel, GenericLayout]], icons: Dict[str, str])`

Demonstrator that hosts several apps in one window, with a menu to switch between them.

#### `Demonstrator.switch_app(self, *args, **kwargs)`

Function triggered to edit GUIs visibility based on the menu value scivianna.panel.gui module --------------------------

GUI sidebar: the drawer of extension buttons shared by visualization panels and layouts.

### `class scivianna.panel.gui.GUI(extensions: List[Extension])`

Sidebar of a panel or layout: a drawer listing the extension buttons and their toolbars.

#### `GUI.update_colors(self)`

Updates the extension buttons colors: when the drawer is open, the active extension button is highlighted.

#### `GUI.change_drawer(self, _, extension: Tuple[pmui.IconButton, pn.Column])`

Opens the drawer and sets the active extension.

## Parameters

\_ : Any  
Bokeh event

extension : Tuple\[pmui.IconButton, pn.Column\]  
Extension to set active

#### `GUI.open_close_drawer(self, _)`

Toggles the drawer open or closed.

## Parameters

\_ : Any  
Bokeh event

#### `GUI.make_panel(self) -> pn.Row`

Builds the panel viewable of the GUI

## Returns

pn.Row  
GUI panel object

#### `GUI.add_extension(self, extension: Extension)`

Adds an Extension instance to the GUI

## Parameters

extension : Extension  
Extension to add to the GUI

#### `GUI.register_new_extension(self, button: pmui.IconButton, col: pn.Column)`

Register a button and its associated column to the GUI

## Parameters

button : pmui.IconButton  
Extension button

col : pn.Column  
Extension toolbar column scivianna.panel.panel_1d module --------------------------------

Panel1D - 1D visualization panel for Scivianna.

### `class scivianna.panel.panel_1d.Panel1D(slave: ComputeSlave, name: str='', extensions: List[Extension]=default_extensions, extension_jsons: dict[Type[Extension], dict]={})  — bases: VisualizationPanel`

1D Visualisation panel associated to a code.

#### `Panel1D.recompute(self, *args, **kwargs)`

Recomputes the figure based on the new bounds and parameters.

## Parameters

event : Any  
Event to make the function linkable to a button

#### `Panel1D.duplicate(self, keep_name: bool=False) -> 'Panel1D'`

Get a copy of the panel. A panel of the same type is generated, the current display too, but a new slave process is created.

## Parameters

keep_name : bool  
New panel name is the same as the current, if not, a number iterates at the end of the name

## Returns

VisualizationPanel  
Copy of the visualisation panel

#### `Panel1D.get_slave(self) -> ComputeSlave`

Returns the current panel code slave.

## Returns

ComputeSlave  
Panel slave

#### `Panel1D.recompute_at(self, position: Tuple[float, float, float], cell_id: str)`

Triggers a panel recomputation at the provided location. Called by layout update event.

## Parameters

position : Tuple\[float, float, float\]  
Location to provide to the slave

cell_id : str  
cell id to provide to the slave

#### `Panel1D.set_field(self, field_names: List[str])`

Updates the plotted fields. Unknown field names are silently ignored.

## Parameters

field_names : List\[str\]  
Fields to display

#### `Panel1D.provide_field_change_callback(self, callback: Callable)`

Stores a function to call everytime the displayed field is changed. the functions takes a string as argument.

## Parameters

callback : Callable  
Function to call.

#### `Panel1D.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Panel1D.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Panel1D.set_colormap(self, colormap)`

Sets the current color map, not used in the case of a Panel1D

## Parameters

colormap : str  
Color map name

#### `Panel1D.to_json(self) -> Dict`

Returns a dictionnary with the information required to rebuild the visualization panel

## Returns

Dict  
Information dict

#### `Panel1D.from_json(cls, info_dict: Dict, slave: ComputeSlave, extensions: List[Extension], extension_jsons: dict[Type[Extension], dict]) -> 'Panel1D'`

Restores the visualization panel from its information dict

## Parameters

info_dict : Dict  
Dictionnary containing all required information to restore the panel

slave : ComputeSlave  
Panel associated slave

extensions : List\[Extension\]  
Extensions to add to the panel

extension_jsons : dict\[Type\[Extension\], dict\]  
Panel extensions initial options

## Returns

Panel1D  
Restored panel

#### `Panel1D.set_xscale(self, scale: str)`

Sets the X axis scale to either log or lin

## Parameters

scale : str  
Scale to set

#### `Panel1D.set_yscale(self, scale: str)`

Sets the Y axis scale to either log or lin

## Parameters

scale : str  
Scale to set scivianna.panel.panel_2d module --------------------------------

Panel2D - 2D visualization panel for Scivianna.

This module implements Panel2D, a 2D visualization panel that renders geometry slices with field coloring. It supports both polygon and grid representations, with interactive zoom/pan capabilities.

### `class scivianna.panel.panel_2d.PlotterBackend  — bases: Enum`

Enumeration of available 2D plotter backends.

### `class scivianna.panel.panel_2d.Panel2D(slave: ComputeSlave, name='', display_polygons: bool=True, plotter_backend: PlotterBackend=PlotterBackend.BOKEH, extensions: List[Extension]=None, extension_jsons: dict[Type[Extension], dict]={}, data: Data2D=None, displayed_field: str=MESH, colormap: str='BuRd', u: Tuple[float, float, float]=X, v: Tuple[float, float, float]=Y, origin: Tuple[float, float, float]=None, size_u: float=1.0, size_v: float=1.0)  — bases: VisualizationPanel`

2D Visualisation panel associated to a code.

#### `Panel2D.key_pressed(self, *events)`

Callback function triggered when a key is pressed in the overlay component. It updates the `key` parameter of the panel with the last key pressed. If the key is 'X', 'Y', or 'Z', it changes the axes accordingly. If the key is 'F', it flips the u axis.

## Parameters

\*events : tuple  
Event information, not used in this function.

#### `Panel2D.compute_fn(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float], size_u: float, size_v: float) -> Data2D`

Request the slave to compute a new frame, and updates the data to display

## Parameters

u : Tuple\[float, float, float\]  
Direction vector along the horizontal axis

v : Tuple\[float, float, float\]  
Direction vector along the vertical axis

origin : Tuple\[float, float, float\]  
Physical 3D position of the slice center

size_u : float  
Size of the slice along the u axis

size_v : float  
Size of the slice along the v axis

## Returns

Data2D  
Geometry data.

#### `Panel2D.ranges_callback(self, x0: float, x1: float, y0: float, y1: float)`

Updates the bounds FloatInput based on the current frame zoom.

## Parameters

x0 : float  
Horizontal axis minimum value

x1 : float  
Horizontal axis maximum value

y0 : float  
Vertical axis minimum value

y1 : float  
Vertical axis maximum value

#### `Panel2D.get_uv(self) -> Tuple[np.ndarray, np.ndarray]`

Returns the normalized u and v axis direction vectors.

## Returns

Tuple\[np.ndarray, np.ndarray\]  
Normalized vectors u, v

#### `Panel2D.recompute(self, *args, **kwargs)`

Recomputes the figure based on the new bounds and parameters. Public method that triggers the recompute pipeline.

#### `Panel2D.duplicate(self, keep_name: bool=False) -> 'VisualizationPanel'`

Get a copy of the panel. A panel of the same type is generated, the current display too, but a new slave process is created.

## Parameters

keep_name : bool  
New panel name is the same as the current, if not, a number iterates at the end of the name

## Returns

VisualizationPanel  
Copy of the visualisation panel

#### `Panel2D.get_slave(self) -> ComputeSlave`

Returns the current panel code slave

## Returns

ComputeSlave  
Panel slave

#### `Panel2D.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Panel2D.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Panel2D.provide_field_change_callback(self, callback: Callable)`

Stores a function to call everytime the displayed field is changed. the functions takes a string as argument.

## Parameters

callback : Callable  
Function to call.

#### `Panel2D.recompute_at(self, position: Tuple[float, float, float], cell_id: str)`

Triggers a panel recomputation at the provided location. Called by layout update event.

## Parameters

position : Tuple\[float, float, float\]  
Location to provide to the slave

cell_id : str  
cell id to provide to the slave

#### `Panel2D.set_coordinates(self, u: Tuple[float, float, float]=None, v: Tuple[float, float, float]=None, origin: Tuple[float, float, float]=None, size_u: float=None, size_v: float=None)`

Updates the plot coordinates

## Parameters

u : Tuple\[float, float, float\], optional  
Horizontal axis direction vector, by default None

v : Tuple\[float, float, float\], optional  
Vertical axis direction vector, by default None

origin : Tuple\[float, float, float\], optional  
Physical 3D position of the slice center, by default None

size_u : float, optional  
Size of the slice along the u axis, by default None

size_v : float, optional  
Size of the slice along the v axis, by default None

#### `Panel2D.set_field(self, field_name: str)`

Updates the plotted field

## Parameters

field_name : str  
New field to display

#### `Panel2D.set_colormap(self, colormap: str)`

Sets the current color map

## Parameters

colormap : str  
Color map name

#### `Panel2D.to_json(self) -> Dict`

Returns a dictionnary with the information about the visualization panel

## Returns

Dict  
Information dict

#### `Panel2D.from_json(cls, info_dict: Dict, slave: ComputeSlave, data: Data2D, extensions: List[Extension], extension_jsons: dict[Type[Extension], dict]) -> 'Panel2D'`

Restores the visualization panel from its information dict

## Parameters

info_dict : Dict  
Dictionnary containing all required information to restore the panel

slave : ComputeSlave  
Panel associated slave

data : Data2D  
Initial state Data2D

extensions : List\[Extension\]  
Extensions to add to the panel

extension_jsons : dict\[Type\[Extension\], dict\]  
Panel extensions initial options

## Returns

Panel2D  
Restored panel

#### `Panel2D.provide_on_axes_change_callback(self, callback: Callable)`

Stores a function to call everytime the axes are changed. the functions takes two numpy arrays and three values (u, v, origin, size_u, size_v).

## Parameters

callback : Callable  
Function to call. scivianna.panel.panel_3d module --------------------------------

Panel3D - 3D visualization panel for Scivianna.

This module implements Panel3D, a 3D visualization panel that renders geometry with field coloring using VTK.

### `class scivianna.panel.panel_3d.Panel3D(slave: ComputeSlave, name='', extensions: List[Extension]=default_extensions, extension_jsons: dict[Type[Extension], dict]={}, data: Data3D=None, displayed_field: str=MESH, colormap: str='BuRd')  — bases: VisualizationPanel`

3D Visualisation panel associated to a code.

#### `Panel3D.compute_fn(self) -> Data3D`

Request the slave to compute a new frame, and updates the data to display

## Returns

Data3D  
Geometry data.

#### `Panel3D.recompute(self, *args, **kwargs)`

Recomputes the figure based on the new bounds and parameters. Public method that triggers the recompute pipeline.

#### `Panel3D.duplicate(self, keep_name: bool=False) -> 'VisualizationPanel'`

Get a copy of the panel. A panel of the same type is generated, the current display too, but a new slave process is created.

## Parameters

keep_name : bool  
New panel name is the same as the current, if not, a number iterates at the end of the name

## Returns

VisualizationPanel  
Copy of the visualisation panel

#### `Panel3D.get_slave(self) -> ComputeSlave`

Returns the current panel code slave

## Returns

ComputeSlave  
Panel slave

#### `Panel3D.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Panel3D.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Panel3D.provide_field_change_callback(self, callback: Callable)`

Stores a function to call everytime the displayed field is changed. the functions takes a string as argument.

## Parameters

callback : Callable  
Function to call.

#### `Panel3D.provide_on_axes_change_callback(self, callback: Callable)`

Stores a function to call everytime the axes are changed. The function takes the u and v direction vectors, the slice origin and its size.

## Parameters

callback : Callable  
Function to call.

#### `Panel3D.set_field(self, field_name: str)`

Updates the plotted field

## Parameters

field_name : str  
New field to display

#### `Panel3D.set_colormap(self, colormap: str)`

Sets the current color map

## Parameters

colormap : str  
Color map name

#### `Panel3D.to_json(self) -> Dict`

Returns a dictionnary with the information required to rebuild the visualization panel

## Returns

Dict  
Information dict

#### `Panel3D.from_json(cls, info_dict: Dict, slave: ComputeSlave, data: Data3D, extensions: List[Extension], extension_jsons: dict[Type[Extension], dict]) -> 'Panel3D'`

Restores the visualization panel from its information dict

## Parameters

info_dict : Dict  
Dictionnary containing all required information to restore the panel

slave : ComputeSlave  
Panel associated slave

data : Data3D  
Initial state Data3D

extensions : List\[Extension\]  
Extensions to add to the panel

extension_jsons : dict\[Type\[Extension\], dict\]  
Panel extensions initial options

## Returns

Panel3D  
Restored panel

#### `Panel3D.set_coordinates(self, u: Tuple[float, float, float]=None, v: Tuple[float, float, float]=None, origin: Tuple[float, float, float]=None, size_u: float=None, size_v: float=None)`

Updates the plot coordinates

## Parameters

u : Tuple\[float, float, float\], optional  
Horizontal axis direction vector, by default None

v : Tuple\[float, float, float\], optional  
Vertical axis direction vector, by default None

origin : Tuple\[float, float, float\], optional  
Physical 3D position of the slice center, by default None

size_u : float, optional  
Size of the slice along the u axis (not used for 3D but kept for API compatibility), by default None

size_v : float, optional  
Size of the slice along the v axis (not used for 3D but kept for API compatibility), by default None

#### `Panel3D.recompute_at(self, position: Tuple[float, float, float], cell_id: str)`

Triggers a panel recomputation at the provided location. Called by layout update event.

## Parameters

position : Tuple\[float, float, float\]  
Location to provide to the slave

cell_id : str  
cell id to provide to the slave scivianna.panel.visualisation_panel module -------------------------------------------

VisualizationPanel - Base class for visualization panels in Scivianna.

This module provides the abstract base class for all visualization panels, defining the common interface and lifecycle methods.

### `class scivianna.panel.visualisation_panel.VisualizationPanel(slave: ComputeSlave, name='', extensions: List[Extension]=[], extension_jsons: dict[Type[Extension], dict]={})  — bases: pn.viewable.Viewer`

Visualisation panel associated to a code.

#### `VisualizationPanel.key_pressed(self, *events)`

Callback function triggered when a key is pressed in the overlay component. It updates the `key` parameter of the panel with the last key pressed. If the key is 'X', 'Y', or 'Z', it changes the axes accordingly. If the key is 'F', it flips the u axis.

## Parameters

\*events : tuple  
Event information, not used in this function.

#### `VisualizationPanel.duplicate(self, keep_name: bool=False) -> 'VisualizationPanel'`

Get a copy of the panel. A panel of the same type is generated, the current display too, but a new slave process is created.

## Parameters

keep_name : bool  
New panel name is the same as the current, if not, a number iterates at the end of the name

## Returns

VisualizationPanel  
Copy of the visualisation panel

#### `VisualizationPanel.get_slave(self) -> ComputeSlave`

Returns the current panel code slave

## Returns

ComputeSlave  
Panel slave

#### `VisualizationPanel.recompute(self, *args, **kwargs)`

Recomputes the figure based on the new bounds and parameters.

#### `VisualizationPanel.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `VisualizationPanel.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `VisualizationPanel.provide_field_change_callback(self, callback: Callable)`

Stores a function to call everytime the displayed field is changed. the functions takes a string as argument.

## Parameters

callback : Callable  
Function to call.

#### `VisualizationPanel.provide_on_axes_change_callback(self, callback: Callable)`

Stores a function to call everytime the axes are changed. the functions takes a two numpy arrays and three floats (axes, and umin, vmin, w).

## Parameters

callback : Callable  
Function to call.

#### `VisualizationPanel.recompute_at(self, position: Tuple[float, float, float], cell_id: str)`

Triggers a panel recomputation at the provided location. Called by layout update event.

## Parameters

position : Tuple\[float, float, float\]  
Location to provide to the slave

cell_id : str  
cell id to provide to the slave

#### `VisualizationPanel.set_field(self, field_name: str)`

Updates the plotted field

## Parameters

field_name : str  
New field to display

#### `VisualizationPanel.set_colormap(self, colormap: str)`

Sets the current color map

## Parameters

colormap : str  
Color map name

#### `VisualizationPanel.outline_color(self, color: str='lightgray')`

Sets the color of the outlined plot

## Parameters

color : str  
HTML color

#### `VisualizationPanel.rename(self, name: str)`

Rename current panel

## Parameters

name : str  
New name

#### `VisualizationPanel.get_new_name(self) -> str`

Returns an new name iterating on the current one

## Returns

str  
Name different from current name

#### `VisualizationPanel.trigger_on_file_load(self, file_path: str, file_label: str)`

Notifies every extension that a new file has been loaded.

## Parameters

file_path : str  
Path of the loaded file

file_label : str  
Label of the loaded file

#### `VisualizationPanel.to_json(self) -> Dict`

Returns a dictionnary with the information required to rebuild the visualization panel

## Returns

Dict  
Information dict

#### `VisualizationPanel.from_json(self, info_dict: Dict, data: DataContainer) -> 'VisualizationPanel'`

Restores the visualization panel from its information dict

## Parameters

info_dict : Dict  
Dictionnary containing all required information to restore the panel

## Returns

VisualizationPanel  
Dict defined visualization panel Module contents ---------------

Panel package: GUI components for displaying scivianna visualization panels.
