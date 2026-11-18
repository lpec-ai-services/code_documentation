<!-- source: api/scivianna.utils.rst -->

# scivianna.utils package

# Scivianna Utils Module

The `utils` module provides utility functions and helper classes used throughout Scivianna for mesh processing, file handling, serialization, and visualization tools.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `color_tools.py` | Color manipulation utilities (RGBA handling, colormap generation) |
| `extruded_mesh.py` | Tools for visualizing extruded 2D meshes in 3D |
| `file_cleaner.py` | Utilities for cleaning input files when the visualizer is closed |
| `interface_tools.py` | Helper functions for interface implementations |
| `polygon_sorter.py` | Algorithms for sorting and organizing polygon data |
| `polygonize_tools.py` | Tools for converting grid data to polygon representations |
| `serialization.py` | Save/load functionality for panel states and layouts |
| `structured_mesh.py` | Utilities for structured mesh handling |

## Key Utilities

### Color Tools (`color_tools.py`)
- RGBA color array manipulation
- Colormap generation and application
- Alpha/transparency adjustments
- Color interpolation

### Extruded Mesh (`extruded_mesh.py`)
Converts 2D meshes to 3D extruded representations:
- Takes 2D polygon data
- Extrudes along Z-axis
- Generates 3D visualization coordinates

### Polygonize Tools (`polygonize_tools.py`)
Converts raster/grid data to vector polygons:
- Contour extraction from scalar fields
- Polygon boundary detection
- Mesh cell polygonization

### Serialization (`serialization.py`)
Save and load Scivianna states:
- GridStack layout serialization
- Panel state persistence
- ZIP-based save files

```python
from scivianna.utils.serialization import save_gridstack_to_zip, load_gridstack_from_zip

# Save layout
save_gridstack_to_zip(layout, "my_save.zip")

# Load layout
layout = load_gridstack_from_zip("my_save.zip")
```

### Structured Mesh (`structured_mesh.py`)
Utilities for structured mesh operations:
- Grid generation
- Coordinate transformations
- Cell indexing utilities

### Interface Tools (`interface_tools.py`)
Common helpers for interface implementations:
- Default panel creation
- Interface enumeration
- File validation

### Polygon Sorter (`polygon_sorter.py`)
Algorithms for organizing polygon data:
- Spatial sorting for rendering order
- Adjacency-based ordering
- Performance optimization for large datasets

## Usage Examples

### Color Manipulation
```python
from scivianna.utils.color_tools import rgba_to_hex, hex_to_rgba

# Convert between formats
hex_color = rgba_to_hex([255, 128, 0, 255])  # "#ff8000"
rgba = hex_to_rgba("#ff8000")  # [255, 128, 0, 255]
``` Submodules ----------

## scivianna.utils.color_tools module

Color maps and color interpolation utilities for scivianna plots.

### `scivianna.utils.color_tools.get_edges_colors(face_colors: np.ndarray, offset: int=-20) -> np.ndarray`

Returnds the edge colors from the face colors

## Parameters

face_colors : np.ndarray  
Numpy array containing a list of RBG colors ranging from 0 to 255

offset : int  
The colors are defined in RGB with colors from 0 to 255, this offset tells how many decrease the edge color

## Returns

np.ndarray  
Edge colors

### `scivianna.utils.color_tools.interpolate_cmap_at_values(cmap_name: str, values: np.ndarray) -> np.ndarray`

Returns a numpy array containing the RGBA 255 colors per value in values

## Parameters

cmap_name : str  
Name of the cmaps to get from scivianna.utils.color_tools.color_maps

values : np.ndarray  
Values to interpolate

## Returns

np.ndarray  
RGBA 255 colors per value in values scivianna.utils.extruded_mesh module -------------------------------------

Extruded mesh utilities for Scivianna.

This module provides utilities for creating extruded structured meshes from 2D polygons.

This version uses MEDCoupling (`medcoupling`) instead of VTK/PyVista as the underlying 3D mesh engine.

## Design notes

- The base 2D geometry is triangulated per polygon with `shapely.constrained_delaunay_triangles` (same approach as the original `polygons_to_polydata` helper), so that holes are handled correctly: a polygon with a hole becomes several triangle cells, none of which cover the hole. All triangles coming from the same `PolygonElement` share that element's `cell_id`.
- The 2D triangulated mesh's nodes are merged (`mergeNodes`), mirroring the original `pyvista` `PolyData.clean()` call. This makes adjacent triangles (whether from the same polygon or from touching polygons) share point ids, which is required later to stitch cut edges back into closed loops when slicing.
- The 3D mesh is built with MEDCoupling's native `MEDCouplingUMesh.buildExtrudedMesh`, extruding the 2D triangulated mesh along a 1D path mesh whose nodes sit at `z_coords[i] * extrusion_vector`. Policy `0` ("translation only") reproduces the per-slab translation used by the previous VTK `extrude_trim` implementation. Each 2D triangle becomes one `NORM_PENTA6` (triangular prism) cell per layer, and MEDCoupling numbers the resulting cells level by level (`layer * n_base_cells + base_cell_index`), which is exactly what makes offsetting the `cell_id` field per layer straightforward.
- Because a single logical polygon can be represented by several prism cells (from triangulation) sharing one `cell_id`, slicing needs to reassemble their cut edges into one polygon boundary. `compute_2D_data` below performs that logic on top of the raw slice produced by the MED interface: it takes the per-prism polygons returned by `MEDInterface.compute_2D_data` (one cut loop per elementary 3D cell), maps their cells back to the logical polygon ids, and unions the cut loops belonging to the same id into single polygons.
- Once the MED geometry is built, this class hands it over (mesh + `cell_id` field) to an internal `MEDInterface` instance, which performs all the actual Scivianna operations (2D slicing, 3D data computation, value extraction), so no logic is duplicated between this class and the MED interface.

## Caveats

The exact Python import name (`medcoupling` vs `MEDCoupling`) and the precise signature of `buildSlice3D` / `buildExtrudedMesh` can differ slightly between MEDCoupling releases; adjust as needed for your install.

### `class scivianna.utils.extruded_mesh.ExtrudedStructuredMesh(xy_mesh: List[PolygonElement]=None, z_coords: np.ndarray=None, extrusion_vector: Tuple[float, float, float]=(0, 0, 1))  — bases: Geometry2DPolygon, Geometry3D`

Structured mesh build from a set of PolygonElement on the XY plane, extruded at a set of Z values.

The base polygons, the z bins and the extrusion vector are either given at construction time or provided through `read_file` (which allows driving the interface through a ComputeSlave). The MEDCoupling geometry is built lazily by `build_medcoupling_geometry` before the first `compute_2D_data` / `compute_3D_data` call, then handed over to an internal `MEDInterface`, which performs all the actual Scivianna operations (2D slicing, 3D data, value extraction) so that no logic is duplicated between this class and the MED interface.

#### `ExtrudedStructuredMesh.read_file(self, file_path: str, file_label: str) -> None`

Read a geometry input and store its content in the interface.

The geometry is described by three inputs, each sent through one call of this function:

- `file_path="base_polygons"` with `file_label` a list of `PolygonElement` (the 2D base polygons on the XY plane),
- `file_path="z_coords"` with `file_label` a list of z bins,
- `file_path="extrusion_vector"` with `file_label` a 3D direction vector.

The MEDCoupling geometry itself is not built here; it is built lazily by `build_medcoupling_geometry` before the first `compute_2D_data` / `compute_3D_data` call, once all the inputs are available.

## Parameters

file_path : str  
Geometry input label: "base_polygons", "z_coords" or "extrusion_vector"

file_label : List\[PolygonElement\], list of float, or Tuple\[float, float, float\]  
Value associated to the given geometry input label

## Raises

ValueError  
If the given file_path is not a supported geometry input label.

#### `ExtrudedStructuredMesh.get_labels(self) -> List[str]`

Returns a list of fields names displayable with this interface.

## Returns

List\[str\]  
List of fields names (the mesh itself plus every field set through `set_values`).

#### `ExtrudedStructuredMesh.get_label_coloring_mode(self, label: str) -> VisualizationMode`

Returns wheter the given field is colored based on a string value or a float.

## Parameters

label : str  
Field to color name

## Returns

VisualizationMode  
Coloring mode

#### `ExtrudedStructuredMesh.get_file_input_list(self) -> List[Tuple[str, str]]`

Returns a list of file label and its description for the GUI.

## Returns

List\[Tuple\[str, str\]\]  
List of (file label, description). This interface reads no file, so the list is empty.

#### `ExtrudedStructuredMesh.save(self, file_path: Path, include_files: bool)`

Pickle saves the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File in which save the file

include_files : bool  
Included loaded file

#### `ExtrudedStructuredMesh.load(self, file_path: Path, include_files: bool)`

Pickle loads the slave content to a file, allows slave state reload.

Two modes are available:  
- If **include_files** is at True, all loaded data are saved, the pickled file can be loaded on its own to recover last session.
- If **include_files** is at False, only the computed data are loaded, enabling faster first computation allowing a smaller pickle file size.

## Parameters

file_path : Path  
File from which load the slave

include_files : bool  
Included loaded file

#### `ExtrudedStructuredMesh.build_medcoupling_geometry(self)`

Builds the MEDCoupling 3D unstructured mesh from the list of polygons, using MEDCoupling's native `buildExtrudedMesh`.

#### `ExtrudedStructuredMesh.save_debug_meshes(self, output_dir: str='.', prefix: str='extruded_mesh_debug', write_fields: bool=True) -> Dict[str, str]`

Writes the base 2D (triangulated) mesh and the resulting 3D extruded mesh to `.med` files, for inspection in ParaVis/Salome (or by reloading them with `medcoupling.ReadMeshFromFile`). Handy when an extrusion or a slice doesn't look right and you want to look at the actual MEDCoupling geometry rather than at Scivianna's polygons.

The 3D file also always gets a `cell_id` cell field (matching `self.cell_id_values`), plus - if `write_fields` is True - every field previously registered through `set_values`, so the mapping between mesh cells and Scivianna's logical polygon ids can be checked directly in the viewer.

## Parameters

output_dir : str  
Directory the .med files are written into (created if needed).

prefix : str  
Filename prefix; files are written as `{prefix}_2d.med` and `{prefix}_3d.med`.

write_fields : bool  
If True, also write every field previously registered through `set_values` into the 3D .med file.

## Returns

Dict\[str, str\]  
`{"2d": <path>, "3d": <path>}` of the written files.

#### `ExtrudedStructuredMesh.set_values(self, name: str, grid: Dict[int, Any])`

Setting a dict grid (cell_id -\> value) to the given name.

The values are scattered onto the extruded mesh cells following the `cell_id` mapping and stored in the internal MED interface as a MEDCoupling field, which then serves them for display and extraction.

## Parameters

name : str  
Field name

grid : Dict\[int, Any\]  
Field value, keyed by cell_id

## Raises

RuntimeError  
If the geometry has not been built yet (no base polygons or z coordinates provided).

#### `ExtrudedStructuredMesh.get_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

Returns a cell name - field value map for a given field name.

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

#### `ExtrudedStructuredMesh.compute_3D_data(self, options: Dict[str, Any]) -> Tuple['Data3D', bool]`

Returns the full extruded 3D mesh (with a `cell_id` field and any field previously set via `set_values`) ready for 3D display.

Delegates to the internal MED interface, which converts the MEDCoupling mesh to a PyVista mesh and wraps it into a `Data3D`.

## Parameters

options : Dict\[str, Any\]  
Additional options for frame computation.

## Returns

Data3D  
3D geometry (and any field set via `set_values`) to display

bool  
Whether the data changed since the last call

## Raises

RuntimeError  
If the geometry has not been built yet (no base polygons or z coordinates provided).

#### `ExtrudedStructuredMesh.get_3d_value_dict(self, value_label: str, cells: List[Union[int, str]], options: Dict[str, Any], caller: str='API') -> Dict[Union[int, str], str]`

Returns a cell name - field value map for a given field name on the 3D mesh.

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

RuntimeError  
If the geometry has not been built yet (no base polygons or z coordinates provided), or if the requested field is not defined.

#### `ExtrudedStructuredMesh.compute_2D_data(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float], size_u: float, size_v: float, q_tasks: mp.Queue, options: Dict[str, Any], caller: str='API') -> Tuple[Data2D, bool]`

Returns a list of polygons that defines the geometry in a given frame.

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

RuntimeError  
If the geometry has not been built yet (no base polygons or z coordinates provided). scivianna.utils.file_cleaner module ------------------------------------

File cleaner utility for Scivianna.

This module provides utilities for marking files for deletion on program exit.

### `scivianna.utils.file_cleaner.mark_for_deletion(path: Path)`

Marks a file to be deleted when the visualizer is closed.

## Parameters

path : Path  
File path scivianna.utils.interface_tools module ---------------------------------------

Helpers to discover and instantiate the built-in code interfaces.

### `class scivianna.utils.interface_tools.GenericInterfaceEnum  — bases: Enum`

Names of the built-in code interfaces available in scivianna.

### `scivianna.utils.interface_tools.load_available_interfaces() -> Dict[str, Type[GenericInterface]]`

Loads the built-in available interfaces

## Returns

Dict\[str, Type\[GenericInterface\]\]  
Available interfaces linked to their name

### `scivianna.utils.interface_tools.get_interface_default_panel(interface: Union[GenericInterfaceEnum, str], title: str='')`

Returns the default panel of built-in implemented code interfaces. Returns None if interface is unknown.

## Parameters

interface : GenericInterfaceEnum  
GenericInterfaceEnum representing the code interface

## Returns

VisualizationPanel  
Panel of the code interface, or None scivianna.utils.polygon_sorter module --------------------------------------

Sorting utilities for polygon lists in Data2D objects.

### `class scivianna.utils.polygon_sorter.PolygonSorter()`

Object used to sort a list of polygons per field value.

Sorting the polygons by their value prevents edges of different colors from overlapping in the plot. The sort order is saved so that subsequent calls reapply it without recomputing it.

#### `PolygonSorter.sort_from_value(self, data: Data2D)`

Sorts a set of polygons per field

## Parameters

data : Data2D  
Data2D object containing the geometry properties

#### `PolygonSorter.sort_list(self, data: Data2D)`

Sorts the value and color lists of a Data2D object with the saved sort order.

If no sort order was saved yet (no prior call to `sort_from_value`), it is computed from the cell values first.

## Parameters

data : Data2D  
Data2D object whose lists are sorted in place

#### `PolygonSorter.reset_indexes(self, *args, **kwargs)`

Clears the saved sort indexes. scivianna.utils.polygonize_tools module ----------------------------------------

Polygon tools for Scivianna.

This module provides utilities for polygon manipulation and rasterization.

### `class scivianna.utils.polygonize_tools.PolygonCoords(x_coords: Union[List[float], np.ndarray], y_coords: Union[List[float], np.ndarray])`

Object ontaining the X and Y coordinates of a polygon

#### `PolygonCoords.deepcopy(self) -> 'PolygonCoords'`

Returns a deep copy of this PolygonCoords instance.

## Returns

PolygonCoords  
A new PolygonCoords with independently copied x and y coordinate arrays.

#### `PolygonCoords.translate(self, dx: float, dy: float)`

Translates the PolygonCoords by (dx, dy)

## Parameters

dx : float  
Horizontal offset

dy : float  
Vertical offset

#### `PolygonCoords.rotate(self, origin: Tuple[float, float], angle: float)`

Rotate the PolygonElement by the angle around the origin

## Parameters

origin : Tuple\[float, float\]  
Rotation origin

angle : float  
Angle (in radians)

#### `PolygonCoords.get_closed_coords(self) -> Tuple[np.ndarray, np.ndarray]`

Returns the x and y coordinates of the polygon with the first vertex repeated at the end.

### `class scivianna.utils.polygonize_tools.PolygonElement(exterior_polygon: PolygonCoords, holes: List[PolygonCoords], cell_id: str)`

Object containing the exterior polygon and the holes of a polygonal object

#### `PolygonElement.deepcopy(self) -> 'PolygonElement'`

Returns a deep copy of this PolygonElement instance.

## Returns

PolygonElement  
A new PolygonElement with independently copied exterior, holes, and attributes.

#### `PolygonElement.translate(self, dx: float, dy: float)`

Translates the PolygonElement by (dx, dy)

## Parameters

dx : float  
Horizontal offset

dy : float  
Vertical offset

#### `PolygonElement.rotate(self, origin: Tuple[float, float], angle: float)`

Rotate the PolygonElement by the angle around the origin

## Parameters

origin : Tuple\[float, float\]  
Rotation origin

angle : float  
Angle (in radians)

#### `PolygonElement.to_shapely(self, z_coord: float=None) -> shapely.Polygon`

Returns a shapely Polygon version of self at the vertical coordinate z_coord

## Parameters

z_coord : float, optional  
If provided, the polygon is 3D at the given height, by default None

## Returns

shapely.Polygon  
Shapely polygon

#### `PolygonElement.from_shapely(cls, polygon: shapely.Polygon, cell_id: Union[int, str]) -> 'PolygonElement'`

Creates an instance of PolygonElement from a shapely Polygon.

## Parameters

polygon : shapely.Polygon  
The shapely Polygon to convert from

cell_id : Union\[int, str\]  
Polygon cell id

## Returns

PolygonElement  
An instance of PolygonElement with the polygon's coordinates

### `scivianna.utils.polygonize_tools.numpy_2D_array_to_polygons(x: Union[List[float], np.ndarray], y: Union[List[float], np.ndarray], arr: np.ndarray, simplify: bool) -> List[PolygonElement]`

Converts a 2D array mapping the cell id to a list of PolygonElements using the python module rasterio

## Parameters

x : Union\[List\[float\], np.ndarray\]  
Points coordinates along the X axis

y : Union\[List\[float\], np.ndarray\]  
Points coordinates along the Y acis

arr : np.ndarray  
2D cell index mapping

simplify : bool  
Simplify the polygons to smoothen the edges

## Returns

List\[PolygonElement\]  
List of PolygonElements

### `scivianna.utils.polygonize_tools.cast_to_ascii_arr(arr)`

Convert an array of strings to ASCII-printable characters.

Filters each string in the input array to keep only printable ASCII characters. This is used to handle cell data that may contain non-printable characters which VTK cannot process.

## Parameters

arr : array-like  
Array of strings to filter.

## Returns

numpy.ndarray  
Array containing only the printable ASCII characters from each string.

### `scivianna.utils.polygonize_tools.polygons_to_polydata(polygons: List[PolygonElement], cell_values: List, cell_colors: List, cell_edge_colors: List) -> 'pv.PolyData'`

Convert a list of polygons to a pyvista PolyData object.

## Parameters

polygons : List\[PolygonElement\]  
List of polygon elements with exterior and holes.

cell_values : List  
List of cell values (one per polygon).

cell_colors : List  
List of cell colors (RGBA, 0-255).

## Returns

pv.PolyData  
PolyData object with geometry and cell data. scivianna.utils.serialization module ------------------------------------

Serialization utilities for scivianna components.

This module provides serialization and deserialization functions at different levels: - slave_only: Serialize/deserialize only the ComputeSlave - panel2d_only: Serialize/deserialize only Panel2D (without slave data) - panel1d_only: Serialize/deserialize only Panel1D (without slave data) - layout: Serialize/deserialize complete SplitLayout with all components

Note: To avoid circular imports, actual module imports are done lazily inside functions. Panel3D has an optional dependency (pyvista), so it is imported lazily with a stub fallback.

### `scivianna.utils.serialization.save_slave_to_file(slave: ComputeSlave, file_path: Union[str, Path], include_files: bool=True) -> Path`

Save a ComputeSlave state to a pickle file.

## Parameters

slave : ComputeSlave  
The slave to save

file_path : Union\[str, Path\]  
Path to the output file

include_files : bool = True  
If True, includes loaded files in the serialization

## Returns

Path  
Path to the saved file

### `scivianna.utils.serialization.load_slave_from_file(file_path: Union[str, Path], interface_class: Type[GenericInterface], include_files: bool=True) -> ComputeSlave`

Load a ComputeSlave state from a pickle file.

## Parameters

file_path : Union\[str, Path\]  
Path to the input file

interface_class : Type\[GenericInterface\]  
The interface class for the slave

include_files : bool = True  
If True, includes loaded files in the deserialization

## Returns

ComputeSlave  
The loaded slave

### `scivianna.utils.serialization.save_panel2d_to_file(panel: 'Panel2D', file_path: Union[str, Path], include_files: bool=True) -> Path`

Save a Panel2D to a zip file containing panel configuration and slave data.

The zip file contains: - panel.json: JSON file describing the panel configuration and interface info - slave.pkl: Serialized slave data - current_data.pkl: Serialized current_data for Panel2D

## Parameters

panel : Panel2D  
The panel to save

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

### `scivianna.utils.serialization.load_panel2d_from_file(file_path: Union[str, Path], include_files: bool=True) -> 'Panel2D'`

Load a Panel2D from a zip file. The slave is automatically recreated from the saved data.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

Panel2D  
The loaded panel with its associated slave

### `scivianna.utils.serialization.save_panelgraph_to_file(panel: 'PanelGraph', file_path: Union[str, Path], include_files: bool=True) -> Path`

Save a PanelGraph to a zip file containing panel configuration and slave data.

The zip file contains: - panel.json: JSON file describing the panel configuration and interface info - slave.pkl: Serialized slave data - current_data.pkl: Serialized current_data (DataGraph) for PanelGraph

## Parameters

panel : PanelGraph  
The panel to save

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

### `scivianna.utils.serialization.load_panelgraph_from_file(file_path: Union[str, Path], include_files: bool=True) -> 'PanelGraph'`

Load a PanelGraph from a zip file. The slave is automatically recreated from the saved data.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

PanelGraph  
The loaded panel with its associated slave

### `scivianna.utils.serialization.save_panel1d_to_file(panel: 'Panel1D', file_path: Union[str, Path], include_files: bool=True) -> Path`

Save a Panel1D to a zip file containing panel configuration and slave data.

The zip file contains: - panel.json: JSON file describing the panel configuration and interface info - slave.pkl: Serialized slave data

## Parameters

panel : Panel1D  
The panel to save

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

### `scivianna.utils.serialization.load_panel1d_from_file(file_path: Union[str, Path], include_files: bool=True) -> 'Panel1D'`

Load a Panel1D from a zip file. The slave is automatically recreated from the saved data.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

Panel1D  
The loaded panel with its associated slave

### `scivianna.utils.serialization.save_panel3d_to_file(panel: 'Panel3D', file_path: Union[str, Path], include_files: bool=True) -> Path`

Save a Panel3D to a zip file containing panel configuration and slave data.

The zip file contains: - panel.json: JSON file describing the panel configuration and interface info - slave.pkl: Serialized slave data - current_data.pkl: Serialized current_data (Data3D) for Panel3D

## Parameters

panel : Panel3D  
The panel to save

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

### `scivianna.utils.serialization.load_panel3d_from_file(file_path: Union[str, Path], include_files: bool=True) -> 'Panel3D'`

Load a Panel3D from a zip file. The slave is automatically recreated from the saved data.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

Panel3D  
The loaded panel with its associated slave

### `scivianna.utils.serialization.save_paneldatframe_to_file(panel: 'PanelDataFrame', file_path: Union[str, Path], include_files: bool=True) -> Path`

Save a PanelDataFrame to a zip file containing panel configuration and slave data.

The zip file contains: - panel.json: JSON file describing the panel configuration and interface info - slave.pkl: Serialized slave data - dataframe.pkl: Serialized DataFrame for PanelDataFrame

## Parameters

panel : PanelDataFrame  
The panel to save

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

### `scivianna.utils.serialization.load_paneldatframe_from_file(file_path: Union[str, Path], include_files: bool=True) -> 'PanelDataFrame'`

Load a PanelDataFrame from a zip file. The slave is automatically recreated from the saved data.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

PanelDataFrame  
The loaded panel with its associated slave

### `scivianna.utils.serialization.save_layout_to_zip(layout: 'SplitLayout', file_path: Union[str, Path], include_files: bool=True) -> Path`

Saves the SplitLayout configuration and slave data to a zip file.

The zip file contains: - layout.json: JSON file describing the layout structure, current frame, and for each slave: panel name, slave info, and associated interface name - data/: Folder containing serialized data for each slave

## Parameters

layout : SplitLayout  
The layout to save

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

### `scivianna.utils.serialization.load_layout_from_zip(file_path: Union[str, Path], include_files: bool=True) -> 'SplitLayout'`

Restores a SplitLayout from a zip file.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

SplitLayout  
Restored SplitLayout instance

### `scivianna.utils.serialization.restore_extensions_state(panel: 'VisualizationPanel', split_item_data: Dict, full_data: Dict)`

Restores the state of extensions for a given panel.

## Parameters

panel : VisualizationPanel  
Panel whose extensions to restore

split_item_data : Dict  
Serialized split item data containing extension info

full_data : Dict  
Full layout serialized data

### `scivianna.utils.serialization.save_gridstack_to_zip(layout: 'GridStackLayout', file_path: Union[str, Path], include_files: bool=True) -> Path`

Saves the GridStackLayout configuration and slave data to a zip file.

The zip file contains: - layout.json: JSON file describing the layout structure, current frame, bounds, and for each panel: slave info and associated interface name - data/: Folder containing serialized data for each slave

## Parameters

layout : GridStackLayout  
The layout to save

file_path : Union\[str, Path\]  
Path to the output zip file

include_files : bool = True  
If True, includes loaded files in the slave serialization

## Returns

Path  
Path to the saved zip file

### `scivianna.utils.serialization.load_gridstack_from_zip(file_path: Union[str, Path], include_files: bool=True) -> 'GridStackLayout'`

Restores a GridStackLayout from a zip file.

Uses load_panelX_from_file functions for panel deserialization, extracting panel data into temporary zip files matching the single-panel structure.

## Parameters

file_path : Union\[str, Path\]  
Path to the input zip file

include_files : bool = True  
If True, includes loaded files in the slave deserialization

## Returns

GridStackLayout  
Restored GridStackLayout instance scivianna.utils.structured_mesh module ---------------------------------------

Structured mesh containers used to define structured grid based geometries and results.

### `class scivianna.utils.structured_mesh.StructuredMesh()`

Generic structured mesh class to help users define their own structured mesh based geometries/results

#### `StructuredMesh.set_values(self, name: str, grid: np.ndarray)`

Setting a Numpy array grid to the given name. The numpy array must be of size (nx, ny, nz) and the data are called in the XYZ order.

## Parameters

name : str  
Field name

grid : np.ndarray  
Field value

#### `StructuredMesh.get_cells_values(self, name: str, cell_ids: List[int]) -> np.ndarray`

Returns a field values for a list of cell indexes

## Parameters

name : str  
field name

cell_ids : List\[int\]  
cells indexes

## Returns

np.ndarray  
List of values per cell

## Raises

RuntimeError  
Requested a field before defining it

#### `StructuredMesh.compute_2D_slice(self, origin: Tuple[float, float, float], u: Tuple[float, float, float], v: Tuple[float, float, float]) -> List[PolygonElement]`

Computes the PolygonElement list for a slice of the mesh

## Parameters

origin : Tuple\[float, float, float\]  
Slice origin

u : Tuple\[float, float, float\]  
First axis vector

v : Tuple\[float, float, float\]  
Second axis vector

## Returns

List\[PolygonElement\]  
List of polygon elements defining the cut

## Raises

ValueError  
U and V are either parallel or one is of zero length.

### `class scivianna.utils.structured_mesh.CarthesianStructuredMesh(x_coords: np.ndarray, y_coords: np.ndarray, z_coords: np.ndarray)  — bases: StructuredMesh`

Carthesian structured mesh

### `class scivianna.utils.structured_mesh.CylindricalStructuredMesh(r_coords: np.ndarray, theta_coords: np.ndarray, z_coords: np.ndarray)  — bases: StructuredMesh`

Cylindrical structured mesh

### `class scivianna.utils.structured_mesh.SphericalStructuredMesh(r_coords: np.ndarray, theta_coords: np.ndarray, phi_coords: np.ndarray)  — bases: StructuredMesh`

Spherical structured mesh Module contents ---------------

Utility functions and shared flags for scivianna.
