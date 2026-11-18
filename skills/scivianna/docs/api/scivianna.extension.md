<!-- source: api/scivianna.extension.rst -->

# scivianna.extension package

# Scivianna Extension Module

The `extension` module provides extensible components that add functionality to visualization panels in Scivianna. Extensions can be attached to panels to provide additional controls, tools, and features.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `extension.py` | Base class for all panel extensions |
| `axes.py` | 3D coordinates and axis configuration extension |
| `coupling.py` | Coupling-specific controls (time widget, play button) |
| `field_selector.py` | Widget for selecting displayed fields |
| `file_loader.py` | File upload and loading interface |
| `layout.py` | Layout management and panel arrangement tools |
| `line_selector.py` | Tool for setting 1D plots |
| `save_load_extension.py` | Serialization and state save/load functionality |
| `slice_3d.py` | 3D clip plane controls for slicing geometry |
| `ai_assistant.py` | AI-powered assistant for visualization help |
| `icons/` | Icon images for extension UI elements |

## Extension System

Extensions are modular components that can be:
- Added to any visualization panel
- Configured independently
- Serialized and restored with panel state
- Triggered by user interactions or events

## Built-in Extensions

### Layout Extension (`layout.py`)
Manages panel arrangement, frame switching, and interface selection.

### Coupling Extension (`coupling.py`)
Provides time management widget and play/pause controls for coupled simulations.

### Field Selector (`field_selector.py`)
Dropdown widget for selecting which data field to visualize.

### File Loader (`file_loader.py`)
Interface for uploading and loading data files from local or server storage.

### Line Selector (`line_selector.py`)
Interactive tool for setting 1D plots.

### Axes Extension (`axes.py`)
Controls for 3D coordinate display and axis configuration.

### Slice Plane Extension (`slice_3d.py`)
Interactive 3D clip plane controls:
- Enable/disable clipping with checkbox
- Select clipping axis (X, Y, Z)
- Adjust clip plane position with slider
- Keyboard shortcuts in 3D viewer: `C` (toggle), `X`/`Y`/`Z` (axis), `↑`/`↓` (move)

### Save/Load Extension (`save_load_extension.py`)
Enables saving panel configurations and restoring them later.

### AI Assistant (`ai_assistant.py`)
Provides AI-powered help and suggestions for visualization tasks.

## Creating Custom Extensions

Custom extensions can be created, see the extension.py file for full API.

```python
from scivianna.extension.extension import Extension

class MyCustomExtension(Extension):
    def __init__(self, slave, plotter, panel):
        super().__init__(slave, plotter, panel)
        # Initialize extension
        
    def make_panel(self):
        # Return Panel UI for this extension
        return pn.Column(...)
        
    def on_mouse_clic(self, screen_location, space_location, cell_id):
        # Handle mouse click events
        pass
        
    def on_file_load(self, file_path, file_label):
        # Handle file loading events
        pass
```

## Extension Lifecycle

1. **Creation**: Extensions are instantiated with slave, plotter, and panel references
2. **Panel Building**: `make_panel()` returns the UI components
3. **Event Registration**: Callbacks are registered for mouse events, file loads, etc.
4. **State Management**: `to_json()` and `from_json()` handle serialization

### Callback Signatures

| Callback | Parameters | Description |
|----------|-----------|-------------|
| `on_file_load(file_path, file_label)` | `str`, `str` | Called when a file is loaded |
| `on_field_change(field_name)` | `str` | Called when displayed field changes |
| `on_updated_data(data)` | `Data2D` / `Data3D` | Called when displayed data updates |
| `on_range_change(u_bounds, v_bounds, w_value)` | `tuple`, `tuple`, `float` | Called when viewport zoom/pan changes |
| `on_frame_change(u_vector, v_vector)` | `tuple`, `tuple` | Called when viewport orientation changes |
| `on_mouse_move(screen_location, space_location, cell_id)` | `tuple`, `tuple`, `str/int` | Called on mouse hover over plot |
| `on_mouse_clic(screen_location, space_location, cell_id)` | `tuple`, `tuple`, `str/int` | Called on mouse click on plot |
| `on_key_pressed(key)` | `str` | Called when a keyboard key is pressed while the mouse hovers the panel |
| `on_scale_change(axis_name, value)` | `str`, `str` | Called when the 1D plot scale is changed |

### Mouse Event Parameters

- **screen_location**: `(x, y)` - Mouse position in screen coordinates (pixels from top-left)
- **space_location**: `(x, y, z)` - Mouse position in 3D world coordinates
- **cell_id**: `str` or `int` - ID of the cell currently under the mouse / clicked Submodules ----------

## scivianna.extension.ai_assistant module

AI Assistant extension for Scivianna.

This module provides AI-assisted code generation for data transformation.

### `class scivianna.extension.ai_assistant.AIAssistant(slave: ComputeSlave, plotter: Plotter2D, panel: 'VisualizationPanel')  — bases: Extension`

Extension providing AI-assisted code generation to edit the plot cell colors.

#### `AIAssistant.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `AIAssistant.on_updated_data(self, data: Data2D)`

Function called when the displayed data is being updated. Extension can edit the data on its way to the plotter.

## Parameters

data : Data2D  
Data to display scivianna.extension.axes module -------------------------------

Extension to customize the 2D plot axes: direction vectors, origin and slice size.

### `class scivianna.extension.axes.Axes(slave: 'ComputeSlave', plotter: Plotter2D, panel: 'VisualizationPanel')  — bases: Extension`

Extension to customize the 2D plot axes: direction vectors, origin and slice size.

#### `Axes.toggle_axis_visibility(self, *args, **kwargs)`

Hides and shows the figure axis

## Parameters

\_ : Any  
Button clic event

#### `Axes.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `Axes.on_range_change(self, origin, size_u, size_v)`

Called when the range/coordinates change.

## Parameters

origin : tuple  
Physical 3D position of the slice center (x, y, z)

size_u : float  
Size of the slice along the u axis

size_v : float  
Size of the slice along the v axis

#### `Axes.on_frame_change(self, u_vector, v_vector)`

Sync the axis vector widgets when the frame axes change in the figure.

#### `Axes.update_data(self)`

Push the pending axis/origin/size changes into the widgets and recompute if needed.

#### `Axes.async_update_data(self)`

Async wrapper around update_data, run on the next Bokeh tick.

#### `Axes.update_widgets_visibility(self)`

Show or hide the axis widgets according to the geometry type.

#### `Axes.trigger_update(self, *args, **kwargs)`

Send the current axes, origin and size to the panel for a recompute.

#### `Axes.get_uv(self) -> Tuple[np.ndarray, np.ndarray]`

Gets the normal direction vectors from the FloatInput objects.

## Returns

Tuple\[np.ndarray, np.ndarray\]  
Vectors U, V

#### `Axes.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension.

## Returns

dict  
Information dictionary

#### `Axes.from_json(cls, extension: 'Axes', info_dict: dict) -> 'Axes'`

Restores the extension from its information dict.

## Parameters

extension : Axes  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

Axes  
Restored extension scivianna.extension.coupling module -----------------------------------

Extension that starts and stops C3PO coupled simulations from the panel, and selects the current display time.

### `class scivianna.extension.coupling.CouplingExtension(layout: 'GenericLayout', slave: ComputeSlave, plotter: Plotter2D, panel: 'VisualizationPanel', **params)  — bases: Extension, param.Parameterized`

Extension to start coupling simulations.

#### `CouplingExtension.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `CouplingExtension.request_recompute(self, event)`

Request a recompute task on all panels, which will trigger the addition of a periodict update on the panels

## Parameters

event : bool  
If the call is from a button press or release

#### `CouplingExtension.provide_options(self) -> dict[str, Any]`

Provide the option extension option dictionnary

## Returns

Dict\[str, Any\]  
Extension option dictionnary

#### `CouplingExtension.add_time_value(self, value: float)`

Adds a new time value to the slide widget

## Parameters

value : float  
Time value to add

#### `CouplingExtension.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension. The show_play_button is willingly not saved as it doesn't make sense to restore it.

## Returns

dict  
Information dictionary

#### `CouplingExtension.from_json(cls, extension: 'CouplingExtension', info_dict: dict) -> 'CouplingExtension'`

Restores the extension from its information dict. The show_play_button is willingly not saved as it doesn't make sense to restore it.

## Parameters

extension : CouplingExtension  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

CouplingExtension  
Restored extension scivianna.extension.extension module ------------------------------------

Base class for scivianna extensions: plugins that customize a visualization panel.

### `class scivianna.extension.extension.Extension(title: str, icon: str, slave: 'ComputeSlave', plotter: Plotter2D, panel: 'VisualizationPanel')`

Definition of a generic scivianna extension. An extension provides a range of tools to customize and interract with the plotting panel and slave.

#### `Extension.on_file_load(self, file_path: str, file_key: str)`

Function called when the user requests a change of field on the GUI

## Parameters

file_path : str  
Path of the loaded file

file_key : str  
Key associated to the loaded file

#### `Extension.on_field_change(self, field_name: str)`

Function called when the user requests a displayed field change

## Parameters

field_name : str  
Name of the new displayed field

#### `Extension.on_updated_data(self, data: Data2D)`

Function called when the displayed data is being updated. Extension can edit the data on its way to the plotter.

## Parameters

data : Data2D  
Data to display

#### `Extension.on_range_change(self, origin: Tuple[float, float, float], size_u: float, size_v: float)`

Function called when the viewport range was updated.

## Parameters

origin : Tuple\[float, float, float\]  
Physical 3D position of the slice center

size_u : float  
Size of the slice along the u axis

size_v : float  
Size of the slice along the v axis

#### `Extension.on_frame_change(self, u_vector: Tuple[float, float, float], v_vector: Tuple[float, float, float])`

Function called when the 2D viewport updates its u and v vectors

## Parameters

u_vector : Tuple\[float, float, float\]  
Horizontal vector

v_vector : Tuple\[float, float, float\]  
Vertical vector

#### `Extension.on_mouse_move(self, screen_location: Tuple[float, float], space_location: Tuple[float, float, float], cell_id: Union[str, int])`

Function called when the mouse moves on the plot

## Parameters

screen_location : Tuple\[float, float\]  
Mouse location on screen

space_location : Tuple\[float, float, float\]  
Mouse targeted location in space

cell_id : Union\[str, int\]  
Currently hovered cell

#### `Extension.on_mouse_clic(self, screen_location: Tuple[float, float], space_location: Tuple[float, float, float], cell_id: Union[str, int])`

Function called when the mouse clics on the plot

## Parameters

screen_location : Tuple\[float, float\]  
Mouse location on screen

space_location : Tuple\[float, float, float\]  
Mouse targeted location in space

cell_id : Union\[str, int\]  
Currently hovered cell

#### `Extension.on_node_selection_change(self, selected_nodes: List[str])`

Function called when the selection of nodes changes on a graph plot.

## Parameters

selected_nodes : List\[str\]  
Ids of the currently selected nodes (empty list when nothing is selected).

#### `Extension.on_nodes_moved(self, moved_nodes: List[Dict[str, float]])`

Function called when one or several nodes are moved on a graph plot.

## Parameters

moved_nodes : List\[Dict\[str, float\]\]  
One entry per moved node: {"id": node key, "x": new x position, "y": new y position}.

#### `Extension.on_coupling_update(self)`

Function called at the end of a coupling time step

#### `Extension.on_scale_change(self, axis_name: str, value: str)`

Function called when the scale is changed

## Parameters

axis_name : str  
Name of the axis changing its scale

value : str  
New scale value

#### `Extension.on_key_pressed(self, key: str)`

Function called when a keyboard key is pressent and the mouse is hovering the panel

## Parameters

key : str  
Keyboard key name

#### `Extension.provide_options(self) -> Dict[str, Any]`

Provide a set of options to give to the slave for its update

## Returns

Dict\[str, Any\]  
Options dictionnary

#### `Extension.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `Extension.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension.

## Returns

dict  
Information dictionary

#### `Extension.from_json(cls, extension: 'Extension', info_dict: dict) -> 'Extension'`

Restores the extension from its information dict.

## Parameters

extension : Extension  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

Extension  
Restored extension scivianna.extension.field_selector module ------------------------------------------

FieldSelector extension for Scivianna.

This module provides field selection and colormap configuration for visualization panels.

### `scivianna.extension.field_selector.hash_string(s: str, seed: int=42) -> int`

Hashes the string using a given seed for reproductibility

## Parameters

s : str  
String to hash

seed : int, optional  
Random seed, by default 42

## Returns

int  
Hashed string

### `scivianna.extension.field_selector.set_colors_list(data: Data2D, slave: 'ComputeSlave', coloring_label: str, color_map: str, center_colormap_on_zero: bool, options: Dict[str, Any], min_value: float=None, max_value: float=None, offset: int=-20, seed: int=42, log_scale: bool=False)`

Sets in a Data2D the list of colors for a field per polygon.

## Parameters

data : Data2D  
Geometry data

slave : ComputeSlave  
Slave to which request values

coloring_label : str  
Field to color

color_map : str  
Colormap in which select colors

center_colormap_on_zero : bool  
Center the color map on zero

options : Dict\[str, Any\]  
Plot extra options

min_value : float  
Force scale minimum value

max_value : float  
Force scale maximum value

offset : int  
The colors are defined in RGB with colors from 0 to 255, this offset tells how many decrease the edge color

seed : int  
String hasing seed for FROM_STRING display mode

log_scale : int  
Sets colors from values logarithmic in FROM_VALUE display mode, by default False

## Raises

NotImplementedError  
The field visualisation mode is not implemented.

### `scivianna.extension.field_selector.set_graph_colors_list(graph: 'DataGraph', color_map: str, coloring_mode: VisualizationMode=VisualizationMode.FROM_VALUE, color_scale: str='linear', center_colormap_on_zero: bool=False, min_value: float=None, max_value: float=None, offset: int=-20, seed: int=42) -> Tuple[Optional[float], Optional[float]]`

Sets the colors of every node of a DataGraph.

All nodes share one global value range (the min/max over the whole graph), so their colors are comparable between nodes. With `color_scale="log"` only values \> 0 are colored, the others are drawn as missing values.

## Parameters

graph : DataGraph  
Graph whose nodes are colored (in place).

color_map : str  
Colormap in which to select the colors.

coloring_mode : VisualizationMode  
How the cell values map onto colors, as in `set_colors_list`. `FROM_STRING` assigns a random color to each distinct string value; `FROM_VALUE` (the default) maps numeric values through the colormap. Any other mode raises `NotImplementedError`.

color_scale : {"linear", "log"}  
How the values are mapped onto the colormap (`FROM_VALUE` only).

center_colormap_on_zero : bool  
Center the color map on zero, as in `set_colors_list`. Ignored when `color_scale` is "log" (a log scale cannot span zero) or in `FROM_STRING` mode.

min_value : float  
Force the global scale minimum value (`FROM_VALUE` only).

max_value : float  
Force the global scale maximum value (`FROM_VALUE` only).

offset : int  
Offset added to the edge colors, as in `set_colors_list`.

seed : int  
String hashing seed for `FROM_STRING` mode, as in `set_colors_list`.

## Returns

Tuple\[Optional\[float\], Optional\[float\]\]  
The global (vmin, vmax) used for normalization, or (None, None) if no finite value was found (or in `FROM_STRING` mode).

## Raises

NotImplementedError  
If `coloring_mode` is neither `FROM_VALUE` nor `FROM_STRING`.

### `class scivianna.extension.field_selector.FieldSelector(slave: 'ComputeSlave', plotter: Plotter2D, panel: 'VisualizationPanel')  — bases: Extension`

Extension used to select the displayed field and edit its colors.

#### `FieldSelector.update_range_visibility(self, *args, **kwargs)`

Updates range visibility based on the field type

#### `FieldSelector.enable_disable_bounds(self, *args, **kwargs)`

Enable/disable min max widgets

#### `FieldSelector.trigger_field_change(self, *args, **kwargs)`

Trigger a field change in the visualization panel

#### `FieldSelector.update_widget_visibility(self, *args, **kwargs)`

#### `FieldSelector.receive_colormap_change(self, *args, **kwargs)`

Receive a field change from the visualization panel

#### `FieldSelector.trigger_colormap_change(self, *args, **kwargs)`

Trigger a field change in the visualization panel

#### `FieldSelector.trigger_update(self, *args, **kwargs)`

Trigger a color map change in the visualization panel

#### `FieldSelector.on_file_load(self, file_path: str, file_key: str)`

Function called when the user requests a change of field on the GUI

## Parameters

file_path : str  
Path of the loaded file

file_key : str  
Key associated to the loaded file

#### `FieldSelector.on_updated_data(self, data: Union[Data2D, 'DataGraph'])`

Function called when the displayed data is being updated. Extension can edit the data on its way to the plotter.

## Parameters

data : Data2D or DataGraph  
Data to display. A DataGraph (graph panel) is colored node by node with a global value range, see `set_graph_colors_list`.

#### `FieldSelector.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `FieldSelector.on_field_change(self, field_name: str)`

Function called when the user requests a displayed field change

## Parameters

field_name : str  
Name of the new displayed field

#### `FieldSelector.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension.

## Returns

dict  
Information dictionary

#### `FieldSelector.from_json(cls, extension: 'FieldSelector', info_dict: dict) -> 'FieldSelector'`

Restores the extension from its information dict.

## Parameters

extension : FieldSelector  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

FieldSelector  
Restored extension

#### `FieldSelector.on_coupling_update(self)`

Function called at the end of a coupling time step scivianna.extension.file_loader module ---------------------------------------

Extension that lets the user pick and load files into the slave.

### `class scivianna.extension.file_loader.FileLoader(slave: 'ComputeSlave', plotter: Plotter2D, panel: 'VisualizationPanel')  — bases: Extension`

Extension to load files and send them to the slave.

#### `FileLoader.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `FileLoader.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension.

## Returns

dict  
Information dictionary

#### `FileLoader.from_json(cls, extension: 'FileLoader', info_dict: dict) -> 'FileLoader'`

Restores the extension from its information dict.

## Parameters

extension : FileLoader  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

FileLoader  
Restored extension scivianna.extension.layout module ---------------------------------

Extension to manage the layout: switch frames and change the code interface.

### `class scivianna.extension.layout.LayoutExtension(layout: 'GenericLayout', slave: ComputeSlave, plotter: Plotter2D, panel: 'VisualizationPanel')  — bases: Extension`

Extension to manage the layout: select the edited frame and change its code interface.

#### `LayoutExtension.add_widget(self, widget: pn.widgets.Widget)`

Append a widget to the layout parameter card in the sidebar.

#### `LayoutExtension.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `LayoutExtension.change_code_interface(self, *args, **kwargs)`

Relay the interface selector change to the layout.

#### `LayoutExtension.set_to_frame(self, *args, **kwargs)`

Make the selected frame the currently edited one.

#### `LayoutExtension.change_to_frame(self, frame_name: str)`

Refresh the selectors so they point at the given frame. scivianna.extension.line_selector module -----------------------------------------

Extension to select the displayed line and axis scales in a Panel1D.

### `class scivianna.extension.line_selector.LineSelector(slave: 'ComputeSlave', plotter: Plotter1D, panel: 'VisualizationPanel')  — bases: Extension`

Extension used to select the displayed line in a Panel1D.

#### `LineSelector.set_x_scale(self, *args, **kwargs)`

Apply the selected x-axis scale to the plotter.

#### `LineSelector.set_y_scale(self, *args, **kwargs)`

Apply the selected y-axis scale to the plotter.

#### `LineSelector.trigger_field_change(self, *args, **kwargs)`

Trigger a field change in the visualization panel

#### `LineSelector.on_file_load(self, file_path: str, file_key: str)`

Function called when the user requests a change of field on the GUI

## Parameters

file_path : str  
Path of the loaded file

file_key : str  
Key associated to the loaded file

#### `LineSelector.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `LineSelector.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension.

## Returns

dict  
Information dictionary

#### `LineSelector.from_json(cls, extension: 'LineSelector', info_dict: dict) -> 'LineSelector'`

Restores the extension from its information dict.

## Parameters

extension : LineSelector  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

LineSelector  
Restored extension

#### `LineSelector.on_coupling_update(self)`

Function called at the end of a coupling time step

#### `LineSelector.on_field_change(self, field_name: str)`

Function called when the user requests a displayed field change

## Parameters

field_name : str  
Name of the new displayed field

#### `LineSelector.on_scale_change(self, axis_name: str, value: str)`

Function called When the scale is changed

## Parameters

axis_name : str  
Name of the axis changing its scale

value : str  
New scale value scivianna.extension.save_load_extension module ------------------------------------------------

Extension to save and load the state of a frame (and optionally its files).

### `class scivianna.extension.save_load_extension.SaveLoadExtension(slave: ComputeSlave, plotter: Plotter2D, panel: 'VisualizationPanel')  — bases: Extension`

Extension to save a frame state to a pickle file and load it back later.

#### `SaveLoadExtension.save_file(self, *args, **kwargs)`

Save frame in file

#### `SaveLoadExtension.load_file(self, *args, **kwargs)`

Load frame from file

#### `SaveLoadExtension.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab scivianna.extension.slice_3d module ------------------------------------

Slice3D extension for Scivianna.

This module provides 3D clip plane controls for slicing geometry. Works with both Panel3D and Panel2D (when using VTK backend).

### `class scivianna.extension.slice_3d.Slice3D(slave: 'ComputeSlave', plotter: Union['Plotter3D', 'VTK2DPolygonPlotter'], panel: Union['Panel3D', 'Panel2D'])  — bases: Extension`

Extension to control the clip plane for slicing geometry.

This extension provides interactive controls to enable/disable clipping, select the clipping axis (X, Y, Z), and adjust the clip plane position.

Works with both Panel3D and Panel2D (when using VTK backend).

#### `Slice3D.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `Slice3D.on_file_load(self, file_path: str, file_key: str)`

Function called when the user loads a new file.

## Parameters

file_path : str  
Path of the loaded file

file_key : str  
Key associated to the loaded file

#### `Slice3D.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension.

## Returns

dict  
Information dictionary

#### `Slice3D.from_json(cls, extension: 'Slice3D', info_dict: dict) -> 'Slice3D'`

Restores the extension from its information dict.

## Parameters

extension : Slice3D  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

Slice3D  
Restored extension

#### `Slice3D.on_updated_data(self, data)`

Called when the data is updated.

If more than 100k cells, disables the info option once with a warning message.

## Parameters

data : Data2D or Data3D  
The updated data object. Module contents ---------------

Extension package for Scivianna.

Provides the Extension base class and the built-in extensions (axes, field selector, file loader, etc.) that customize visualization panels.
