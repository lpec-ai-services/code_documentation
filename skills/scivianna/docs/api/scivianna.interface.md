<!-- source: api/scivianna.interface.rst -->

# scivianna.interface package

# Scivianna Interface Module

The `interface` module provides data interfaces for reading simulation results from various file formats. Interfaces abstract data access and provide a unified API for visualization.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file, registers available interfaces |
| `generic_interface.py` | Base class `GenericInterface` with common functionality |
| `med_interface.py` | Interface for Salome MED file format |
| `vtk_interface.py` | Interface for VTK/VTU file formats |
| `csv_result.py` | Interface for CSV time-series data |
| `structured_mesh_interface.py` | Interface for structured mesh data |
| `time_dataframe.py` | Utility class for time-indexed data frames |

## Interface Hierarchy

### GenericInterface (Base Class)
Provides core functionality for all interfaces:

| Function | Description |
|----------|-------------|
| `read_file(file_path, file_label)` | Reads input files to extract data |
| `get_labels()` | Returns list of available fields/results |
| `get_label_coloring_mode(label)` | Returns whether a field is colored by string or float values |
| `get_file_input_list()` | Returns list of loaded files with descriptions |
| `serialize(obj, key)` | Serializes objects for multiprocessing queue transmission |
| `save(file_path, include_files)` | Saves interface state to a pickle file |
| `load(file_path, include_files)` | Loads interface state from a pickle file |
| `get_slave()` | Returns a ComputeSlave instance for the interface class |

### Data Capability Interfaces
Interfaces inherit from these capability classes based on what they provide:

| Interface | Purpose |
|-----------|---------|
| `Geometry2D` | Provides 2D cell geometry and field values |
| `Geometry2DPolygon` | Provides 2D geometry as a list of polygons |
| `Geometry2DGrid` | Provides 2D geometry as a numpy array (rasterized) |
| `Geometry3D` | Provides 3D geometry and cell values for volumetric visualization |
| `ValueAtLocation` | Provides values at specific locations/cells/materials |
| `Value1DAtLocation` | Provides 1D data profiles at locations |
| `DataFrameInterface` | Provides data as a pandas DataFrame |
| `CouplingInterface` | Supports runtime coupling updates (C3PO/Icoco) |

### Geometry2D Interface
Extends GenericInterface with 2D geometry capabilities:

| Function | Description |
|----------|-------------|
| `compute_2D_data(u, v, origin, size_u, size_v, w_value, q_tasks, options, caller)` | Returns 2D geometry polygons for a given frame |
| `get_value_dict(value_label, cells, options, caller)` | Returns cell name to field value mapping |

### Geometry2DPolygon Interface
Subclass of Geometry2D that provides polygon-based geometry. Inherits all Geometry2D methods.

### Geometry2DGrid Interface
Subclass of Geometry2D that provides grid-based (rasterized) geometry. Inherits all Geometry2D methods.

### Geometry3D Interface
Provides 3D geometry capabilities for volumetric visualization:

| Function | Description |
|----------|-------------|
| `compute_3D_data(options)` | Returns 3D geometry data for visualization |
| `get_3d_value_dict(value_label, cells, options, caller)` | Returns cell name to field value mapping for 3D data |

### ValueAtLocation Interface
Provides point-value access capabilities:

| Function | Description |
|----------|-------------|
| `get_value(position, cell_index, material_name, field, options)` | Returns field value at a specific location/cell/material |
| `get_values(positions, cell_indexes, material_names, field, options)` | Returns field values at multiple locations/cells/materials |

### Value1DAtLocation Interface
Provides 1D data profile access:

| Function | Description |
|----------|-------------|
| `get_1D_value(position, cell_index, material_name, field, options)` | Returns 1D data series (pd.Series) at a specific location/cell/material |

### DataFrameInterface
Provides data as a pandas DataFrame for tabular display via `PanelDataFrame`:

| Function | Description |
|----------|-------------|
| `get_dataframe(cell_id, origin, options)` | Returns the interface data as a pandas DataFrame |

### CouplingInterface
Provides runtime coupling capabilities for C3PO/Icoco integration:

| Function | Description |
|----------|-------------|
| `set_time(time)` | Sets the current time for coupling updates |
| `update_data(key, data)` | Replaces interface data with new value |
| `append_data(key, data)` | Appends data associated with current time |
| `update_mesh(key, data)` | Replaces interface mesh and data with new value |
| `append_mesh(key, data)` | Appends mesh and data associated with current time |
| `get_template(name)` | Returns template for C3PO getOutputxxxFieldTemplate functions |
| `set_template(name, template)` | Sets the template for C3PO functions |

## Available Interfaces

### MED Interface
Reads Salome MED files containing:
- Mesh geometry (2D/3D)
- Field data on cells/nodes
- Time-step information

```python
from scivianna.interface.med_interface import MEDInterface

interface = MEDInterface()
interface.read_file("result.med")
labels = interface.get_labels()  # ["temperature", "pressure", ...]
```

### VTK Interface
Reads VTK/VTU files for unstructured grids:
- Polygon/polyhedron cells
- Point and cell data
- Multiple time steps

### CSV Interface
Reads structured CSV data:
- Time-series results
- Column-based variables
- Automatic parsing with pandas

## Creating Custom Interfaces

Custom interfaces can be easily created, the scivianna.interface.generic_interface file defines what functions need to be provided for a new interface.

```python
from scivianna.interface.generic_interface import GenericInterface, Geometry2D

class MyCustomInterface(GenericInterface, Geometry2D):
    def read_file(self, filepath):
        # Implement file reading logic
        pass
    
    def get_labels(self):
        # Return available field names
        return ["field1", "field2"]
    
    def get_geometry_2d(self, field_name):
        # Return 2D geometry for the field
        pass
```

## Interface Registration

Built-in interfaces are automatically discovered and registered via `__init__.py`. Additional user interfaces can be implemeted by calling:

```
from scivianna.interface import register_interface

register_interface("MyInterfaceKey", MyInterfaceClass)
``` Submodules ----------

## scivianna.interface.csv_result module

CSV file interface.

Reads a CSV file (with a mandatory "cell" column) and exposes its columns as displayable fields, with support for time-stepped data updates during a coupling.

### `class scivianna.interface.csv_result.CSVInterface(csv_file_path: str)  — bases: ValueAtLocation, CouplingInterface`

Interface reading a CSV file (with a mandatory "cell" column) and exposing its columns as fields.

#### `CSVInterface.get_value(self, position: Tuple[float, float, float], cell_index: str, material_name: str, field: str, options: Dict[str, Any]=None)`

Provides the result value of a field from either the (x, y, z) position or the cell index.

## Parameters

position : Tuple\[float, float, float\]  
Position at which the value is requested

cell_index : str  
Index of the requested cell

material_name : str  
Name of the requested material (ignored for CSV interface)

field : str  
Requested field name

options : Dict\[str, Any\], optional  
Additional options for value computation.

## Returns

Union\[str, float\]  
Field value

#### `CSVInterface.get_values(self, positions: List[Tuple[float, float, float]], cell_indexes: List[str], material_names: List[str], field: str, options: Dict[str, Any]=None) -> List[Union[str, float]]`

Provides the result values at different positions from either the (x, y, z) positions or the cell indexes.

## Parameters

positions : List\[Tuple\[float, float, float\]\]  
List of position at which the value is requested

cell_indexes : List\[str\]  
Indexes of the requested cells

material_names : List\[str\]  
Names of the requested materials (ignored for CSV interface)

field : str  
Requested field name

options : Dict\[str, Any\], optional  
Additional options for value computation.

## Returns

List\[Union\[str, float\]\]  
Field values

#### `CSVInterface.get_labels(self) -> List[str]`

Returns the fields names providable.

## Returns

List\[str\]  
Fields names

#### `CSVInterface.set_time(self, time: float)`

This non-Icoco function allows setting the current time in an interface to associate to the received value.

## Parameters

time : float  
Current time

#### `CSVInterface.append_data(self, key: str, data: Any)`

Stores the data and associates it to the current time. Replaces the whole dataframe at the current time step.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CSVInterface.update_data(self, key: str, data: Any)`

Replaces the interface data by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CSVInterface.update_mesh(self, key: str, data: Any)`

Replaces the interface data and mesh by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CSVInterface.append_mesh(self, key: str, data: Any)`

Stores the data and mesh and associate them to the current time. Replaces the whole dataframe at the current time step.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CSVInterface.get_template(self, name: str)`

Returns the template for the C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

#### `CSVInterface.set_template(self, name: str, template: Any)`

Sets the template returned by C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

template : Any  
Object to set as template

#### `CSVInterface.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File in which save the file

include_files : bool  
Included loaded file

#### `CSVInterface.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file

#### `CSVInterface.get_options_dictionnary(self) -> dict[str, Any]`

Returns a current interface state option dictionnary.

## Returns

dict\[str, Any\]  
Option dictionnary to provide to the interface functions scivianna.interface.generic_interface module ---------------------------------------------

Abstract base classes for all code interfaces.

Defines the interface hierarchy (GenericInterface and its 2D/3D/graph/value/coupling specializations) that every concrete code adapter must implement.

### `class scivianna.interface.generic_interface.GenericInterface`

Generic interface class that implement basic functions. This class mutualises functions that are shared between its child classes.

#### `GenericInterface.read_file(self, file_path: str, file_label: str) -> None`

Read a file and store its content in the interface

## Parameters

file_path : str  
File to read

file_label : str  
Label to define the file type

## Raises

NotImplementedError  
Function to override in the code interfaces

#### `GenericInterface.get_labels(self) -> List[str]`

Returns a list of fields names displayable with this interface

## Returns

List\[str\]  
List of fields names

#### `GenericInterface.get_label_coloring_mode(self, label: str) -> VisualizationMode`

Returns wheter the given field is colored based on a string value or a float.

## Parameters

label : str  
Field to color name

## Returns

VisualizationMode  
Coloring mode

## Raises

NotImplementedError  
Function to override in the code interfaces

#### `GenericInterface.get_file_input_list(self) -> List[Tuple[str, str]]`

Returns a list of file label and its description for the GUI

## Returns

List\[Tuple\[str, str\]\]  
List of (file label, description)

## Raises

NotImplementedError  
The function was not implemented in the code interface.

#### `GenericInterface.serialize(self, obj: Any, key: str) -> Any`

This function receives an object that is about to be transmitted at the given key. - If the object can be passed through a python multiprocessing Queue, it can be returned. - If the object can't, it is serialized, and the code returns the file path.

The read function will then be able to expect the returned object at the given key.

By default, this class returns the obj, if the cobject can't be passed, overwrite this function.

## Parameters

obj : Any  
Object that is sent to the generic interface

key : str  
Key associated to the object

## Returns

Any  
Object transmissible through a multiprocessing Queue associated to the given object.

#### `GenericInterface.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File in which save the file

include_files : bool  
Included loaded file

#### `GenericInterface.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file

#### `GenericInterface.get_slave(cls)`

Returns a ComputeSlave instance running this interface class in a worker process.

#### `GenericInterface.get_options_dictionnary(self) -> dict[str, Any]`

Returns a current interface state option dictionnary.

## Returns

dict\[str, Any\]  
Option dictionnary to provide to the interface functions

### `class scivianna.interface.generic_interface.Geometry2D  — bases: GenericInterface`

Interface parent class for classes that can compute geometry 2D slices.

#### `Geometry2D.compute_2D_data(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float], size_u: float, size_v: float, q_tasks: mp.Queue, options: Dict[str, Any], caller: str='API') -> Tuple[Data2D, bool]`

Returns a list of polygons that defines the geometry in a given frame

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

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

Data2D  
Geometry to display

bool  
Were the polygons updated compared to the past call

## Raises

NotImplementedError  
Function to override in the code interfaces

#### `Geometry2D.get_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

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

## Raises

NotImplementedError  
Function to override in the code interfaces

### `class scivianna.interface.generic_interface.Geometry2DPolygon  — bases: Geometry2D`

Interface parent class for classes that can compute geometry 2D slices and provide a list of polygons.

### `class scivianna.interface.generic_interface.Geometry2DGrid  — bases: Geometry2D`

Interface parent class for classes that can compute geometry 2D slices and provide a numpy array.

### `class scivianna.interface.generic_interface.GraphInterface  — bases: GenericInterface`

Interface parent class for classes that can compute a graph of 2D plots connected by directed links.

#### `GraphInterface.compute_graph(self, q_tasks: mp.Queue, options: Dict[str, Any], caller: str='API') -> Tuple['DataGraph', bool]`

Returns a graph of 2D plots connected by directed links to display

## Parameters

q_tasks : mp.Queue  
Queue from which get orders from the master.

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

DataGraph  
Graph to display

bool  
Were the graph nodes updated compared to the past call

## Raises

NotImplementedError  
Function to override in the code interfaces

#### `GraphInterface.get_graph_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

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

## Raises

NotImplementedError  
Function to override in the code interfaces

### `class scivianna.interface.generic_interface.Geometry3D  — bases: GenericInterface`

Interface parent class for classes that can compute geometry 3D polygons.

#### `Geometry3D.compute_3D_data(self, options: Dict[str, Any]) -> Tuple[Data3D, bool]`

Returns a list of polygons that defines the geometry in a given frame

## Parameters

options : Dict\[str, Any\]  
Additional options for frame computation.

## Returns

Data3D  
Geometry to display

bool  
Were the polygons updated compared to the past call

#### `Geometry3D.get_3d_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

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

## Raises

NotImplementedError  
Function to override in the code interfaces

### `class scivianna.interface.generic_interface.ValueAtLocation  — bases: GenericInterface`

Interface parent class to implement a function to get values at a specific location.

#### `ValueAtLocation.get_value(self, position: Tuple[float, float, float], cell_index: str, material_name: str, field: str, options: Dict[str, Any]=None) -> Union[str, float]`

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

#### `ValueAtLocation.get_values(self, positions: List[Tuple[float, float, float]], cell_indexes: List[str], material_names: List[str], field: str, options: Dict[str, Any]=None) -> List[Union[str, float]]`

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

### `class scivianna.interface.generic_interface.Value1DAtLocation  — bases: GenericInterface`

Interface parent class to implement a function to get 1D data at a specific location.

#### `Value1DAtLocation.get_1D_value(self, position: Tuple[float, float, float], cell_index: str, material_name: str, field: str, options: Dict[str, Any]=None) -> Union[pd.Series, List[pd.Series]]`

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

### `class scivianna.interface.generic_interface.DataFrameInterface  — bases: GenericInterface`

Interface parent class for interfaces that provide data as a pandas DataFrame.

#### `DataFrameInterface.get_dataframe(self, cell_id: str, origin: Tuple[float, float, float], options: Dict[str, Any]=None) -> pd.DataFrame`

Returns the data stored in the interface as a pandas DataFrame.

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

## Raises

NotImplementedError  
Function to override in the code interfaces

### `class scivianna.interface.generic_interface.CouplingInterface  — bases: GenericInterface`

Interface parent class to implement the C3PO functions required for a code coupling visualization.

#### `CouplingInterface.set_time(self, time: float)`

This non-Icoco function allows setting the current time in an interface to associate to the received value.

## Parameters

time : float  
Current time

#### `CouplingInterface.update_data(self, key: str, data: Any)`

Replaces the interface data by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CouplingInterface.append_data(self, key: str, data: Any)`

Stores the data and associates it to the current time.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CouplingInterface.update_mesh(self, key: str, data: Any)`

Replaces the interface data and mesh by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CouplingInterface.append_mesh(self, key: str, data: Any)`

Stores the data and mesh and associate them to the current time.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `CouplingInterface.get_template(self, name: str)`

Returns the template for the C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

#### `CouplingInterface.set_template(self, name: str, template: Any)`

Sets the template returned by C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

template : Any  
Object to set as template scivianna.interface.med_interface module -----------------------------------------

MEDCoupling interface for Scivianna.

This module provides an interface for reading and visualizing MED files using the MEDCoupling library. It supports both 2D and 3D visualization with field data extraction.

### `class scivianna.interface.med_interface.MEDCouplingExtension(slave: 'ComputeSlave', plotter: 'Plotter2D', panel: 'VisualizationPanel')  — bases: Extension`

Extension to load files and send them to the slave.

#### `MEDCouplingExtension.provide_options(self) -> Dict[str, float]`

Provide the medcoupling interface options

## Returns

Dict\[str, float\]  
MED options

#### `MEDCouplingExtension.on_field_change(self, field_name: str)`

Saves field name and checks order/iteration values

## Parameters

field_name : str  
New displayed field

#### `MEDCouplingExtension.on_file_load(self, file_path, file_key)`

Catches the file load event to update its data

#### `MEDCouplingExtension.on_slider_change(self, event)`

Updates the panel w coordinate on slider change

#### `MEDCouplingExtension.update_slider_range(self)`

Update slider bounds based on the mesh bounding box

#### `MEDCouplingExtension.on_range_change(self, origin: Tuple[float, float, float], size_u: float, size_v: float)`

Saves the frame bounds on both coordinates

## Parameters

origin : Tuple\[float, float, float\]  
Physical 3D position of the slice center

size_u : float  
Size of the slice along the u axis

size_v : float  
Size of the slice along the v axis

#### `MEDCouplingExtension.on_frame_change(self, u_vector, v_vector)`

Saves new u and v vectors

## Parameters

u_vector : np.ndarray  
Horizontal vector

v_vector : np.ndarray  
Vertical vector

#### `MEDCouplingExtension.check_int_inputs(self, force_valid_values: bool=False)`

Checks iteration and order intinputs values

## Parameters

force_valid_values : bool  
Sets values to valid values if not valid

#### `MEDCouplingExtension.recompute(self, *args, **kwargs)`

Recompute event on intinput changes

#### `MEDCouplingExtension.make_gui(self) -> pn.viewable.Viewable`

Returns a panel viewable to display in the extension tab.

## Returns

pn.viewable.Viewable  
Viewable to display in the extension tab

#### `MEDCouplingExtension.to_json(self) -> dict`

Returns a dictionary with the information required to rebuild the extension.

## Returns

dict  
Information dictionary

#### `MEDCouplingExtension.from_json(cls, extension: 'MEDCouplingExtension', info_dict: dict) -> 'MEDCouplingExtension'`

Restores the extension from its information dict.

## Parameters

extension : MEDCouplingExtension  
Extension instance to restore

info_dict : dict  
Dictionary containing extension state information

## Returns

MEDCouplingExtension  
Restored extension

### `class scivianna.interface.med_interface.MEDInterface()  — bases: Geometry2DPolygon, Geometry3D, CouplingInterface`

Interface for MEDCoupling (.med) files: 2D slices, 3D meshes and C3PO coupling.

#### `MEDInterface.read_file(self, file_path: Union[str, Path, 'medcoupling.MEDCouplingUMesh', 'medcoupling.MEDCouplingFieldDouble'], file_label: str)`

Read a file and store its content in the interface

## Parameters

file_path : str, Path, MEDCouplingUMesh or MEDCouplingFieldDouble  
File to read, or a MEDCoupling mesh/field object provided directly. If a mesh or field object is given, it is stored as-is and no file I/O is performed.

file_label : str  
Label to define the file type

#### `MEDInterface.get_options_dictionnary(self) -> dict[str, Any]`

Returns a current interface state option dictionnary.

## Returns

dict\[str, Any\]  
Option dictionnary to provide to the interface functions

#### `MEDInterface.set_mesh(self, mesh: 'medcoupling.MEDCouplingUMesh', time: float=0.0, replace: bool=True)`

Stores a MEDCoupling mesh directly in the interface without file I/O.

This allows providing the geometry from an in-memory mesh (e.g., built by another code) instead of reading it from a .med file on disk. Field data can then be associated with this mesh via `append_data` / `update_data` or `append_mesh` / `update_mesh`.

## Parameters

mesh : MEDCouplingUMesh  
Mesh to store

time : float, optional  
Simulation time associated with the mesh (default: 0.0)

replace : bool, optional  
If True (default), replaces the current mesh at the last time step. If False, appends a new mesh entry at the given time.

#### `MEDInterface.compute_2D_data(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float], size_u: float, size_v: float, q_tasks: mp.Queue, options: Dict[str, Any], caller: str='API') -> Tuple[Data2D, bool]`

Returns a list of polygons that defines the geometry in a given frame

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

options : Dict\[str, Any\]  
Additional options for frame computation.

caller : str  
Identifier of the caller requesting the computation (default: "API")

## Returns

Data2D  
Geometry to display

bool  
Were the polygons updated compared to the past call

#### `MEDInterface.get_labels(self) -> List[str]`

Returns a list of fields names displayable with this interface

## Returns

List\[str\]  
List of fields names

#### `MEDInterface.get_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

Returns a cell name - field value map for a given field name

## Parameters

value_label : str  
Field name to get values from

cells : List\[Union\[int,str\]\]  
List of cells names

options : Dict\[str, Any\]  
Additional options for frame computation.

## Returns

Dict\[Union\[int,str\], str\]  
Field value for each requested cell names

#### `MEDInterface.get_label_coloring_mode(self, label: str) -> VisualizationMode`

Returns wheter the given field is colored based on a string value or a float.

## Parameters

label : str  
Field to color name

## Returns

VisualizationMode  
Coloring mode

#### `MEDInterface.compute_3D_data(self, options: Dict[str, Any]) -> Tuple[Data3D, bool]`

Returns a list of polygons that defines the geometry in a given frame

## Parameters

options : Dict\[str, Any\]  
Additional options for frame computation.

## Returns

Data3D  
Geometry to display

bool  
Were the polygons updated compared to the past call

#### `MEDInterface.get_3d_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

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

#### `MEDInterface.get_file_input_list(self) -> List[Tuple[str, str]]`

Returns a list of file label and its description for the GUI

## Returns

List\[Tuple\[str, str\]\]  
List of (file label, description)

#### `MEDInterface.set_time(self, time: float)`

This non-Icoco function allows setting the current time in an interface to associate to the received value.

## Parameters

time : float  
Current time

#### `MEDInterface.update_data(self, key: str, data: Any)`

Replaces the interface data by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `MEDInterface.append_data(self, key: str, data: Any)`

Stores the data and associates it to the current time. Mesh is stored at every time step.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `MEDInterface.update_mesh(self, key: str, data: Any)`

Replaces the interface data and mesh by the current value. Replaces the current mesh (last time step, which might be 0).

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `MEDInterface.append_mesh(self, key: str, data: Any)`

Stores the data and mesh and associate them to the current time. Mesh is stored at every time step.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `MEDInterface.get_template(self, name: str)`

Returns the template for the C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

#### `MEDInterface.set_template(self, name: str, template: Any)`

Sets the template returned by C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

template : Any  
Object to set as template (a MED file path or a MEDCouplingUMesh)

#### `MEDInterface.get_iterations(self) -> Dict[str, List[Tuple[int, int]]]`

Returns the fields iterations

## Returns

Dict\[str, List\[Tuple\[int, int\]\]\]  
Iterations/orders per field

#### `MEDInterface.get_bounding_box(self, time: float=None) -> Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]]`

Returns the mesh bounding box

## Parameters

time : float, optional  
Time at which to get the bounding box. If None, uses current_time or 0.

## Returns

Tuple\[Tuple\[float, float\], Tuple\[float, float\], Tuple\[float, float\]\]  
Mesh bounding box : ((minx, maxx), (miny, maxy), (minz, maxz))

#### `MEDInterface.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File in which save the file

include_files : bool  
Included loaded file

#### `MEDInterface.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file scivianna.interface.structured_mesh_interface module ------------------------------------------------------

Interface for structured meshes, to be subclassed by file-specific interfaces.

### `class scivianna.interface.structured_mesh_interface.StructuredMeshInterface()  — bases: Geometry2DPolygon`

StructuredMesh generic interface. This interface is not usable as such as it can't load a file. To use it, the developper must implement another interface inheriting from it implementing the read_file function.

#### `StructuredMeshInterface.read_file(self, file_path: str, file_label: str)`

Read a file and store its content in the interface

## Parameters

file_path : str  
File to read

file_label : str  
Label to define the file type

#### `StructuredMeshInterface.get_options_dictionnary(self) -> dict[str, Any]`

Returns a current interface state option dictionnary.

## Returns

dict\[str, Any\]  
Option dictionnary to provide to the interface functions

#### `StructuredMeshInterface.compute_2D_data(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float], size_u: float, size_v: float, q_tasks: mp.Queue, options: Dict[str, Any], caller: str='API') -> Tuple[Data2D, bool]`

Returns a list of polygons that defines the geometry in a given frame

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

options : Dict\[str, Any\]  
Additional options for frame computation.

## Returns

Data2D  
Geometry to display

bool  
Were the polygons updated compared to the past call

#### `StructuredMeshInterface.get_labels(self) -> List[str]`

Returns a list of fields names displayable with this interface

## Returns

List\[str\]  
List of fields names

#### `StructuredMeshInterface.get_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

Returns a cell name - field value map for a given field name

## Parameters

value_label : str  
Field name to get values from

cells : List\[Union\[int,str\]\]  
List of cells names

options : Dict\[str, Any\]  
Additional options for frame computation.

## Returns

Dict\[Union\[int,str\], str\]  
Field value for each requested cell names

#### `StructuredMeshInterface.get_label_coloring_mode(self, label: str) -> VisualizationMode`

Returns wheter the given field is colored based on a string value or a float.

## Parameters

label : str  
Field to color name

## Returns

VisualizationMode  
Coloring mode

#### `StructuredMeshInterface.get_file_input_list(self) -> List[Tuple[str, str]]`

Returns a list of file label and its description for the GUI

## Returns

List\[Tuple\[str, str\]\]  
List of (file label, description)

#### `StructuredMeshInterface.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File in which save the file

include_files : bool  
Included loaded file

#### `StructuredMeshInterface.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file scivianna.interface.time_dataframe module ------------------------------------------

Interface exposing a time-series DataFrame filled during coupling.

### `class scivianna.interface.time_dataframe.TimeDataFrame()  — bases: Value1DAtLocation, CouplingInterface`

Interface hosting a DataFrame that is filled along a coupling run.

#### `TimeDataFrame.get_labels(self) -> List[str]`

Returns the fields names providable.

## Returns

List\[str\]  
Fields names

#### `TimeDataFrame.get_options_dictionnary(self) -> dict[str, any]`

Returns a current interface state option dictionnary.

## Returns

dict\[str, any\]  
Option dictionnary to provide to the interface functions

#### `TimeDataFrame.get_1D_value(self, position: Tuple[float, float, float], cell_index: str, material_name: str, field: str, options: Dict[str, Any]=None) -> Union[pd.Series, List[pd.Series]]`

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

#### `TimeDataFrame.set_time(self, time: float)`

This non-Icoco function allows setting the current time in an interface to associate to the received value.

## Parameters

time : float  
Current time

#### `TimeDataFrame.append_data(self, key: str, data: Any)`

Stores the data and associates it to the current time.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `TimeDataFrame.update_data(self, key: str, data: Any)`

Replaces the interface data by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `TimeDataFrame.update_mesh(self, key: str, data: Any)`

Replaces the interface data and mesh by the current value

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `TimeDataFrame.append_mesh(self, key: str, data: Any)`

Stores the data and mesh and associate them to the current time.

## Parameters

key : str  
Data associated key

data : Any  
New value

#### `TimeDataFrame.get_template(self, name: str)`

Returns the template for the C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

#### `TimeDataFrame.set_template(self, name: str, template: Any)`

Sets the template returned by C3PO getOutputxxxFieldTemplate functions

## Parameters

name : str  
Field name

template : Any  
Object to set as template

#### `TimeDataFrame.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File in which save the file

include_files : bool  
Included loaded file

#### `TimeDataFrame.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file scivianna.interface.vtk_interface module -----------------------------------------

VTK interface for Scivianna.

This module provides a VTK/PyVista-based interface for reading and visualizing VTK file formats (.pvd, .vtu, .vtp, etc.) in Scivianna. It supports both 2D slice visualization and 3D geometry display, with time-dependent data handling.

## Features

- Read VTK file formats using PyVista
- Time-dependent data visualization
- 2D slice extraction with polygon conversion
- 3D geometry display
- Interactive time slider via VTKExtension

## Classes

VTKInterface  
Main interface class for VTK file handling

VTKExtension  
Extension providing time slider GUI for VTK files

## Example

\>\>\> from scivianna import ComputeSlave \>\>\> from scivianna.interface import VTKInterface \>\>\> \>\>\> slave = ComputeSlave(VTKInterface) \>\>\> slave.read_file("mesh.pvd", "Geometry") \>\>\> panel = Panel2D(slave, name="VTK View") \>\>\> panel.show()

## Dependencies

Requires pyvista and vtk packages. Install with:  
pip install scivianna\[3d\]

### `scivianna.interface.vtk_interface.extract_unstructured_grid(dataset: Any) -> Optional[pv.UnstructuredGrid]`

Extract an UnstructuredGrid from a pyvista dataset.

This function recursively searches through MultiBlock datasets to find and extract unstructured grid data, which is required for VTK visualization.

## Parameters

dataset : Any  
PyVista dataset (UnstructuredGrid, MultiBlock, or other)

## Returns

Optional\[pv.UnstructuredGrid\]  
UnstructuredGrid if found, None otherwise

## Example

\>\>\> multiblock = pv.read("complex_mesh.vtm") \>\>\> unstructured = extract_unstructured_grid(multiblock) \>\>\> if unstructured is not None: ... print(f"Found {unstructured.number_of_cells} cells")

### `class scivianna.interface.vtk_interface.VTKExtension(slave: 'ComputeSlave', plotter: Union[Plotter2D, 'Plotter3D'], panel: 'VisualizationPanel')  — bases: Extension`

Extension for VTK file visualization with time slider control.

This extension provides a GUI with a time slider for navigating through time-dependent VTK data. It allows users to select specific time steps and optionally recompute the mesh when time changes.

## Attributes

time_slider : pmui.DiscreteSlider  
Slider widget for time step selection

recompute_on_change : pmui.Checkbox  
Checkbox to enable/disable mesh recomputation on time change

time_values : List\[float\]  
Available time steps from the VTK file

## Example

\>\>\> \# Extension is automatically added to VTKInterface \>\>\> \# Users can interact via the GUI time slider \>\>\> extension = VTKExtension(slave, plotter, panel) \>\>\> extension.time_slider.value = 5.0 \# Set time to 5.0

#### `VTKExtension.on_file_load(self, file_path: str, file_key: str) -> None`

Handle file load events to update time values.

## Parameters

file_path : str  
Path to the loaded file

file_key : str  
File key/label (e.g., "Geometry")

#### `VTKExtension.provide_options(self) -> Dict[str, Any]`

Provide computation options to the interface.

## Returns

Dict\[str, Any\]  
Dictionary with time and recompute options

#### `VTKExtension.make_gui(self) -> pn.viewable.Viewable`

Build the extension GUI panel.

## Returns

pn.viewable.Viewable  
Panel layout with time slider and options

### `class scivianna.interface.vtk_interface.VTKInterface() -> None  — bases: Geometry2DPolygon, Geometry3D`

VTK file interface for Scivianna visualization.

This interface reads VTK file formats (particularly .pvd files) using PyVista and provides 2D slice and 3D geometry visualization capabilities. It supports time-dependent data with interactive time step selection.

## Features

- Read .pvd, .vtu, .vtp, and other VTK formats
- Time-dependent data visualization
- 2D slice extraction with polygon conversion
- 3D unstructured grid display
- Automatic point-to-cell data conversion

## Attributes

reader : pv.reader  
PyVista reader object for the loaded file

mesh : pv.UnstructuredGrid  
Current mesh data

times : List\[float\]  
Available time steps

current_time : float  
Currently selected time step

data : Dict\[str, Data2D\]  
Cached 2D data per caller

last_computed_frame : Dict\[str, List\[float\]\]  
Cache keys for computed frames per caller

## Example

\>\>\> from scivianna import ComputeSlave \>\>\> from scivianna.interface import VTKInterface \>\>\> \>\>\> slave = ComputeSlave(VTKInterface) \>\>\> slave.read_file("simulation.pvd", "Geometry") \>\>\> labels = slave.get_labels() \>\>\> print(f"Available fields: {labels}")

## See Also

VTKExtension : Extension providing time slider GUI

#### `VTKInterface.read_file(self, file_path: Union[str, Path], file_label: str) -> None`

Read a VTK file and store its content.

Supports .pvd files for time-dependent data and multi-block datasets. Automatically converts point data to cell data for visualization.

## Parameters

file_path : str or Path  
Path to the VTK file (.pvd, .vtu, .vtp, etc.)

file_label : str  
File type label ("Geometry" or "MULTI_BLOCK")

## Raises

ImportError  
If pyvista is not available

NotImplementedError  
If file_label is not supported

FileNotFoundError  
If file does not exist

## Example

\>\>\> interface = VTKInterface() \>\>\> interface.read_file("mesh.pvd", "Geometry") \>\>\> print(f"Loaded {len(interface.times)} time steps")

#### `VTKInterface.load_at_time(self, time: float) -> None`

Load data at a specific time step.

## Parameters

time : float  
Time value to load

## Raises

ValueError  
If time is not in available time steps

## Example

\>\>\> interface.load_at_time(5.0) \# Load data at t=5.0

#### `VTKInterface.get_options_dictionnary(self) -> dict[str, Any]`

Returns a current interface state option dictionnary.

## Returns

dict\[str, Any\]  
Option dictionnary to provide to the interface functions

#### `VTKInterface.compute_2D_data(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float], size_u: float, size_v: float, q_tasks: mp.Queue, options: Dict[str, Any], caller: str='API') -> Tuple[Data2D, bool]`

Compute a 2D slice of the VTK geometry.

Extracts a 2D cross-section from the 3D mesh using the specified plane (defined by u, v axes and origin). Converts the slice to polygons for visualization.

## Parameters

u : Tuple\[float, float, float\]  
Horizontal axis direction vector

v : Tuple\[float, float, float\]  
Vertical axis direction vector

origin : Tuple\[float, float, float\]  
Physical 3D position of slice center

size_u : float  
Size of slice along u axis

size_v : float  
Size of slice along v axis

q_tasks : mp.Queue  
Task queue for multiprocessing

options : Dict\[str, Any\]  
Additional options (time, recompute)

caller : str  
Identifier of the caller

## Returns

Tuple\[Data2D, bool\]  
Data2D object with polygon geometry and whether polygons were updated

## Raises

ValueError  
If u and v vectors are parallel or zero If slice produces no cells

#### `VTKInterface.get_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], Any]`

Get field values for specified cells.

## Parameters

value_label : str  
Field name to retrieve

cells : List\[Union\[int, str\]\]  
List of cell identifiers

options : Dict\[str, Any\]  
Additional options (time, recompute)

caller : str  
Caller identifier

## Returns

Dict\[Union\[int, str\], Any\]  
Mapping of cell IDs to values

## Raises

NotImplementedError  
If field is not available

## Example

\>\>\> values = interface.get_value_dict("Temperature", \[0, 1, 2\], {}) \>\>\> print(f"Cell 0 temperature: {values\[0\]}")

#### `VTKInterface.get_labels(self) -> List[str]`

Get list of displayable field names.

## Returns

List\[str\]  
List of available field names

## Example

\>\>\> labels = interface.get_labels() \>\>\> print(f"Available fields: {labels}")

#### `VTKInterface.get_label_coloring_mode(self, label: str) -> VisualizationMode`

Get coloring mode for a field.

## Parameters

label : str  
Field name

## Returns

VisualizationMode  
Coloring mode (FROM_VALUE, FROM_STRING, or NONE)

#### `VTKInterface.get_file_input_list(self) -> List[Tuple[str, str]]`

Get list of supported file types.

## Returns

List\[Tuple\[str, str\]\]  
List of (file_label, description) tuples

#### `VTKInterface.get_time_values(self) -> List[float]`

Get available time values from the loaded file.

## Returns

List\[float\]  
List of time values

## Example

\>\>\> times = interface.get_time_values() \>\>\> print(f"Time range: {min(times)} to {max(times)}")

#### `VTKInterface.compute_3D_data(self, options: Dict[str, Any]) -> Tuple[Data3D, bool]`

Compute 3D geometry data.

## Parameters

options : Dict\[str, Any\]  
Additional options (time, recompute)

## Returns

Tuple\[Data3D, bool\]  
Data3D object and whether geometry was updated

## Raises

ImportError  
If pyvista is not available

ValueError  
If no mesh is loaded

#### `VTKInterface.get_3d_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], Any]`

Get field values for 3D cells.

## Parameters

value_label : str  
Field name

cells : List\[Union\[int, str\]\]  
Cell identifiers

options : Dict\[str, Any\]  
Additional options

caller : str  
Caller identifier

## Returns

Dict\[Union\[int, str\], Any\]  
Cell ID to value mapping

## Note

This is a wrapper around get_value_dict for 3D visualization.

#### `VTKInterface.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File to which save the slave

include_files : bool  
Included loaded file

#### `VTKInterface.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file

#### `VTKInterface.custom_function(self, function_name: str, arguments: Dict[str, Any]) -> Any`

Call a custom function by name.

This method allows extensions to call interface-specific functions that are not part of the standard interface API.

## Parameters

function_name : str  
Name of the function to call

arguments : Dict\[str, Any\]  
Function arguments

## Returns

Any  
Function result

## Raises

AttributeError  
If function does not exist Module contents ---------------

Interface module for scivianna.

This module provides a registry of all available interfaces.

### `scivianna.interface.register_interface(key: Union[str, GenericInterfaceEnum], interface_class: Type[GenericInterface]) -> None`

Register a new interface class.

## Parameters

key : Union\[str, GenericInterfaceEnum\]  
Key to identify the interface

interface_class : Type\[GenericInterface\]  
Interface class to register

## Raises

TypeError  
If interface_class does not inherit from GenericInterface

### `scivianna.interface.get_interface(key: Union[str, GenericInterfaceEnum]) -> Type[GenericInterface]`

Get an interface class by its key.

## Parameters

key : Union\[str, GenericInterfaceEnum\]  
Key identifying the interface

## Returns

Type\[GenericInterface\]  
Interface class

## Raises

KeyError  
If the interface key is not found

### `scivianna.interface.get_all_interfaces() -> Dict[Union[str, GenericInterfaceEnum], Type[GenericInterface]]`

Get all registered interfaces.

## Returns

Dict\[Union\[str, GenericInterfaceEnum\], Type\[GenericInterface\]\]  
Dictionary of all registered interfaces
