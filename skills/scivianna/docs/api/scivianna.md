<!-- source: api/scivianna.rst -->

# scivianna package

## Subpackages

- `scivianna.agent` (`scivianna.agent.md`)
- `scivianna.component` (`scivianna.component.md`)
- `scivianna.coupling` (`scivianna.coupling.md`)
- `scivianna.data` (`scivianna.data.md`)
- `scivianna.extension` (`scivianna.extension.md`)
- `scivianna.input_file` (`scivianna.input_file.md`)
- `scivianna.interface` (`scivianna.interface.md`)
- `scivianna.layout` (`scivianna.layout.md`)
- `scivianna.panel` (`scivianna.panel.md`)
- `scivianna.plotter_1d` (`scivianna.plotter_1d.md`)
- `scivianna.plotter_2d` (`scivianna.plotter_2d.md`)
- `scivianna.plotter_3d` (`scivianna.plotter_3d.md`)
- `scivianna.plotter_graph` (`scivianna.plotter_graph.md`)
- `scivianna.utils` (`scivianna.utils.md`)

## Submodules

## scivianna.constants module

Global constants for Scivianna.

This module centralizes all configuration constants, magic numbers, and default values used throughout the Scivianna package.

Constants are organized by category: - Plot elements (XS, YS, CELL_NAMES, etc.) - Default field names (MESH, MATERIAL) - Default file names (GEOMETRY, CSV) - Axis coordinates (X, Y, Z) - Default values (DEFAULT_ORIGIN, DEFAULT_SIZE) - Color constants (COLOR_SCALE_MAX, DEFAULT_EDGE_OFFSET) - Timeout values (QUEUE_TIMEOUT_SHORT, QUEUE_TIMEOUT_LONG) - Logging constants (DEFAULT_LOG_LEVEL) scivianna.enums module ----------------------

Enumeration types for Scivianna.

This module defines all enumeration types used throughout Scivianna for type-safe configuration and state management.

Enums are organized by category: - VisualizationMode: How colors are mapped to data - GeometryType: Dimensionality of geometry (2D or 3D) - DataType: Data representation format (grid or polygons) - UpdateEvent: Triggers for plot updates - UpdatePolicy: Data update strategies for coupling

### `class scivianna.enums.VisualizationMode  — bases: Enum`

Defines how colors are mapped to data in visualizations.

This enum determines whether cell colors are derived from numeric values (using a colormap), string values (using random assignment), or not used at all (mesh-only display).

## Attributes

FROM_VALUE : int  
Color is determined by a colormap based on float values. Use this for continuous fields (temperature, pressure, etc.)

FROM_STRING : int  
Color is randomly assigned based on unique string values. Use this for categorical fields (material names, regions, etc.)

NONE : int  
No coloring is applied; only mesh borders are displayed. Use this for geometry-only visualization.

### `class scivianna.enums.GeometryType  — bases: Enum`

Defines the dimensionality and display mode of geometry.

This enum specifies whether the geometry is 2D or 3D, and whether the display shows a selected window or the entire geometry.

## Attributes

\_2D : int  
2D geometry with selected window display (zoomable).

\_2D_INFINITE : int  
2D geometry with full display (no zoom, everything visible).

\_3D : int  
3D geometry requiring U, V axes and w_value for slicing, with selected window display.

\_3D_INFINITE : int  
3D geometry requiring U, V axes and w_value for slicing, with full display.

### `class scivianna.enums.DataType  — bases: Enum`

Defines the data representation format.

This enum specifies whether spatial data is stored as a regular grid (numpy array) or as an irregular polygon list. This affects which plotter is used and how data is processed.

## Attributes

GRID : int  
Data stored in a numpy array (rasterized representation). Efficient for regular grids, requires rasterization for polygons.

POLYGONS : int  
Data stored as a list of PolygonElement objects. Suitable for irregular meshes, preserves exact geometry.

### `class scivianna.enums.UpdateEvent  — bases: int, Enum`

Defines what triggers a plot update.

This enum specifies the events that cause visualization panels to recompute and redraw. Different panels can be configured to respond to different events, enabling sophisticated inter-panel interactions.

## Attributes

RECOMPUTE : int  
Manual update only (user presses recompute button). Most efficient for expensive computations.

CLIC : int  
Update when mouse clicks on a linked 2D/3D plot. Updates use the click location and cell ID.

MOUSE_POSITION_CHANGE : int  
Update when mouse moves over a linked 2D/3D plot. Updates use the mouse location and cell ID. Can be expensive if triggered frequently.

MOUSE_CELL_CHANGE : int  
Update when mouse enters a new cell. More efficient than MOUSE_POSITION_CHANGE.

PERIODIC : int  
Update at regular time intervals. Used for real-time coupling with simulations.

RANGE_CHANGE : int  
Update when (u, v) ranges or origin change (zoom/pan). Standard for interactive exploration.

AXES_CHANGE : int  
Update when axes (u, v vectors) or origin change. Used when changing slice orientation.

## Note

Multiple events can be specified as a list to trigger updates on any of the events.

### `class scivianna.enums.UpdatePolicy  — bases: Enum`

Defines how code interfaces manage field updates during coupling.

This enum controls whether data is appended (time history) or updated (replaced) during real-time simulation coupling. It also distinguishes between mesh updates and data-only updates.

## Attributes

APPEND_DATA : auto  
Keep mesh constant, append data with time stamps. Use when mesh is static but data evolves (e.g., temperature field).

UPDATE_DATA : auto  
Keep mesh constant, replace data at each time step. Use when only current state matters (e.g., steady-state).

APPEND_MESH : auto  
Append both mesh and data with time stamps. Use when mesh deforms over time (e.g., structural mechanics). Falls back to APPEND_DATA if mesh doesn't change.

UPDATE_MESH : auto  
Replace both mesh and data at each time step. Use when only current deformed state matters. Falls back to UPDATE_DATA if mesh doesn't change. scivianna.notebook_tools module --------------------------------

Notebook and server helpers for Scivianna.

Provides convenience functions to display or serve a visualization panel, with ready-made helpers for MEDCoupling .med files.

### `scivianna.notebook_tools.get_med_panel(geo: str, title='MED') -> Panel2D`

Get the visualisation panel for a MEDCoupling .med file path

## Parameters

geo : str  
.med file path

title : str, optional  
Panel title, by default ""

## Returns

Panel2D  
Geometry visualisation panel

## Raises

TypeError  
Argument type not implemented

### `scivianna.notebook_tools.get_med_layout(geo, title: str='MED Field visualizer')`

Opens a server on localhost to open in a browser

## Parameters

geo : str  
Geometry to display

### `scivianna.notebook_tools.show_med_geometry(geo, title: str='MED Field visualizer')`

Opens a server on localhost to open in a browser

## Parameters

geo : str  
Geometry to display

### `scivianna.notebook_tools.serve_med_geometry(geo, title: str='MED Field visualizer')`

Opens a server on the machine IP adress to open in a browser on any machine of the network

## Parameters

geo : str  
Geometry to display

### `scivianna.notebook_tools.get_med_visualizer(geo, title='') -> pn.viewable.Viewable`

Returns a panel to displays it in a jupyter notebook

## Parameters

geo : str  
Geometry to display scivianna.slave module ----------------------

ComputeSlave and worker process for Scivianna.

This module implements the multiprocessing infrastructure that isolates heavy data computation from the UI thread. The ComputeSlave class manages a background worker process that executes interface methods, preventing GIL issues and keeping large data structures (meshes, fields) in the worker process.

## Key Components

ComputeSlave  
Manages the worker subprocess and provides IPC via multiprocessing Queues

worker  
Worker function that runs in the subprocess and executes interface methods

SlaveCommand  
Enum-like class defining available commands for the worker

## Architecture

Main Process Worker Process ┌───────────────┐ ┌──────────────────┐ │ ComputeSlave │ ──send task── ► │ code_interface()│ │ (UI thread) │ ◄──return result │ (worker func) │ └───────────────┘ └──────────────────┘ │ │ ├─ q_tasks (Queue) ─────────► │ ├─ q_returns (Queue) ◄───────── │ └─ q_errors (Queue) ◄───────── │

### `class scivianna.slave.SlaveCommand`

Class defining the available commands that are forwarded to the compute slaves

### `scivianna.slave.worker(q_tasks: mp.Queue, q_returns: mp.Queue, q_errors: mp.Queue, code_interface: Type[GenericInterface])`

Creates a worker that will forward the panel requests to the GenericInterface on another process

## Parameters

q_tasks : mp.Queue  
Queue containing the tasks

q_returns : mp.Queue  
Queue to return the results

code_interface : Type\[GenericInterface\]  
GenericInterface to instanciate.

### `class scivianna.slave.ComputeSlave(code_interface: Type[GenericInterface], allow_errors: bool=False)`

Class that creates a subprocess to interface with the code.

#### `ComputeSlave.reset(self)`

Kills the worker and create a new one.

#### `ComputeSlave.read_file(self, file_path: str, file_label: str)`

Forwards to the worker a file path to read and its associated label

## Parameters

file_path : str  
File to read

file_label : str  
File label

#### `ComputeSlave.get_labels(self) -> List[str]`

Get from the interface the list of displayable labels (fields list)

## Returns

List\[str\]  
List of labels

#### `ComputeSlave.get_label_coloring_mode(self, field_name: str) -> VisualizationMode`

Returns the coloring mode of the plot

## Parameters

field_name : str  
Name of the displayed field

## Returns

VisualizationMode  
Coloring mode

#### `ComputeSlave.get_file_input_list(self) -> List[Tuple[str, str]]`

Get from the interface the list of files labels and their description

## Returns

List\[Tuple\[str, str\]\]  
List of (file label, description)

#### `ComputeSlave.get_options_dictionnary(self) -> dict[str, Any]`

Returns a current interface state option dictionnary.

## Returns

dict\[str, Any\]  
Option dictionnary to provide to the interface functions

#### `ComputeSlave.compute_2D_data(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float], size_u: float, size_v: float, q_tasks: mp.Queue, coloring_label: str, options: Dict[str, Any], caller: str='API') -> Tuple[Data2D, bool]`

Get the geometry from the interface

## Parameters

u : Tuple\[float, float, float\]  
Horizontal coordinate director vector

v : Tuple\[float, float, float\]  
Vertical coordinate director vector

origin : Tuple\[float, float, float\]  
Physical 3D position of the slice center

size_u : float  
Size of the slice along the u axis

size_v : float  
Size of the slice along the v axis

q_tasks : mp.Queue  
Queue from which get orders from the master.

coloring_label : str  
Field label to display

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

Tuple\[Data2D, bool\]  
Data2D object containing the geometry, whether the polygons were updated

#### `ComputeSlave.get_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

Returns a cell name - field value map for a given field name

## Parameters

value_label : str  
Field name to get values from

cells : List\[Union\[int,str\]\]  
List of cells names

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

Dict\[Union\[int,str\], str\]  
Field value for each requested cell names

#### `ComputeSlave.get_geometry_type(self) -> GeometryType`

Returns the interface geometry type

## Returns

GeometryType  
Interface geometry type

#### `ComputeSlave.compute_graph(self, q_tasks: mp.Queue, coloring_label: str, options: Dict[str, Any], caller: str='API') -> Tuple['DataGraph', bool]`

Get the graph from the interface

A graph has no slice: every node is fitted to its own content, so no u/v axes or origin have to be requested.

## Parameters

q_tasks : mp.Queue  
Queue from which get orders from the master.

coloring_label : str  
Field label to display

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

Tuple\[DataGraph, bool\]  
DataGraph object containing the graph, whether the nodes were updated

#### `ComputeSlave.get_graph_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

Returns a cell name - field value map for a given field name

## Parameters

value_label : str  
Field name to get values from

cells : List\[Union\[int,str\]\]  
List of cells names

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

Dict\[Union\[int,str\], str\]  
Field value for each requested cell names

#### `ComputeSlave.compute_3D_data(self, coloring_label: str, options: Dict[str, Any]) -> Tuple[Data3D, bool]`

Returns a list of polygons that defines the geometry in a given frame

## Parameters

options : Dict\[str, Any\]  
Additional options for frame computation.

## Returns

Data3D  
Geometry to display

bool  
Were the polygons updated compared to the past call

#### `ComputeSlave.get_3d_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

Returns a cell name - field value map for a given field name

## Parameters

value_label : str  
Field name to get values from

cells : List\[Union\[int,str\]\]  
List of cells names

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

Dict\[Union\[int,str\], str\]  
Field value for each requested cell names

#### `ComputeSlave.get_value(self, position: Tuple[float, float, float], cell_index: str, material_name: str, field: str, options: Dict[str, Any]=None) -> Union[str, float]`

Provides the result value of a field from either the (x, y, z) position, the cell index, or the material name.

## Parameters

position : Tuple\[float, float, float\]  
Position at which the value is requested

cell_index : str  
Index of the requested cell

material_name : str  
Name of the requested material

field : str  
Requested field name

options : Dict\[str, Any\], optional  
Additional options for value computation.

## Returns

Union\[str, float\]  
Field value

#### `ComputeSlave.get_values(self, positions: List[Tuple[float, float, float]], cell_indexes: List[str], material_names: List[str], field: str, options: Dict[str, Any]=None) -> List[Union[str, float]]`

Provides the result values at different positions from either the (x, y, z) positions, the cell indexes, or the material names.

## Parameters

positions : List\[Tuple\[float, float, float\]\]  
List of position at which the value is requested

cell_indexes : List\[str\]  
Indexes of the requested cells

material_names : List\[str\]  
Names of the requested materials

field : str  
Requested field name

options : Dict\[str, Any\], optional  
Additional options for value computation.

## Returns

List\[Union\[str, float\]\]  
Field values

#### `ComputeSlave.get_1D_value(self, position: Tuple[float, float, float], cell_index: str, material_name: str, field: str, options: Dict[str, Any]=None) -> Union[pd.Series, List[pd.Series]]`

Provides the 1D value of a field from either the (x, y, z) position, the cell index, or the material name.

## Parameters

position : Tuple\[float, float, float\]  
Position at which the value is requested

cell_index : str  
Index of the requested cell

material_name : str  
Name of the requested material

field : str  
Requested field name

options : Dict\[str, Any\], optional  
Additional options for 1D value computation.

## Returns

Union\[pd.Series, List\[pd.Series\]\]  
Field value

#### `ComputeSlave.get_dataframe(self, cell_id: str, origin: Tuple[float, float, float], options: Dict[str, Any]=None) -> pd.DataFrame`

Returns the data from the interface as a pandas DataFrame.

## Parameters

cell_id : str  
Cell identifier

origin : Tuple\[float, float, float\]  
Origin position

options : Dict\[str, Any\], optional  
Additional options for dataframe computation

## Returns

pd.DataFrame  
Pandas DataFrame containing the data

#### `ComputeSlave.set_time(self, time_: float)`

Set the current time in an interface to associate to the received value.

## Parameters

[time]() : float  
Current time

#### `ComputeSlave.update_data(self, key: str, data: Any)`

Replaces the interface data by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `ComputeSlave.append_data(self, key: str, data: Any)`

Stores the data and associates it to the current time.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `ComputeSlave.update_mesh(self, key: str, data: Any)`

Replaces the interface data and mesh by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `ComputeSlave.append_mesh(self, key: str, data: Any)`

Stores the data and mesh and associate them to the current time.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `ComputeSlave.get_template(self, name: str)`

Returns the template for the C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

#### `ComputeSlave.set_template(self, name: str, template: Any)`

Sets the template returned by C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

template : Any  
Object to set as template

#### `ComputeSlave.update_policy`

Returns the update_policy attribute from the interface

## Returns

Any  
The update_policy value

#### `ComputeSlave.update_policy(self, value)`

Sets the update_policy attribute on the interface

## Parameters

value : Any  
The update_policy value to set

#### `ComputeSlave.duplicate(self) -> 'ComputeSlave'`

Returns a duplicate of the current ComputeSlave. The copy is reseted, and reads the file history.

## Returns

ComputeSlave  
ComputeSlave copy.

#### `ComputeSlave.terminate(self)`

Terminates the subprocess

#### `ComputeSlave.get_result_or_error(self)`

Gets the return value from the process. If an error was sent, raise the error instead.

#### `ComputeSlave.call_custom_function(self, function_name: str, arguments: Dict[str, Any])`

Call an custom function meant to ease extension developments

## Parameters

function_name : str  
Name of the interface function

arguments : Dict\[str, Any\]  
Kwargs of the custom function

## Returns

Any  
Function return

#### `ComputeSlave.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File in which save the file

include_files : bool  
Included loaded file

#### `ComputeSlave.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file Module contents ---------------

Scivianna: SCIentific VIsualizer for simulAtioN aNAlysis

Scivianna is an open-source Python simulation geometry and result visualizer based on Holoviz Panel. It provides a powerful and flexible environment for visualizing 1D plots, 2D geometries, 3D visualizations, and DataFrames simultaneously, with support for real-time simulation result visualization through code coupling.

## Key Features

- Simultaneous 1D, 2D, 3D, and DataFrame visualization
- Real-time code coupling via C3PO/ICOCO interface
- Generic data interfaces for MED, VTK, CSV, and custom formats
- Remote server access for HPC cluster visualization
- Extensible architecture with plugin extensions

## Quick Start

\>\>\> from scivianna import ComputeSlave, Panel2D \>\>\> from scivianna.interface import MEDInterface \>\>\> \>\>\> \# Create a slave with your data interface \>\>\> slave = ComputeSlave(MEDInterface) \>\>\> slave.read_file("path/to/file.med", "geometry") \>\>\> \>\>\> \# Create and display a visualization panel \>\>\> panel = Panel2D(slave, name="My Panel") \>\>\> panel.show()

For more information, see the documentation at: <https://github.com/cea-code-coupling/scivianna>

## Package Version

The package version is read from the VERSION file and stored in \_\_version\_\_.

### `scivianna.get_version() -> str`

Get the Scivianna version string.

## Returns

str  
Version string (e.g., "1.0.0")

### `scivianna.get_info() -> dict`

Get information about the Scivianna installation.

## Returns

dict  
Dictionary containing version and available components
