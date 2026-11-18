<!-- source: api/scivianna.data.rst -->

# scivianna.data package

# Scivianna Data Module

The `data` module provides core data structures and workers for managing simulation data in Scivianna, including 1D plots, 2D geometries, and 3D meshes.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `data_container.py` | Base container class for holding and managing visualization data |
| `data1d.py` | Data structures for 1D plot data (line charts, time series) |
| `data2d.py` | Data structures for 2D geometry data (meshes, fields, polygons) |
| `data3d.py` | Data structures for 3D geometry data (VTK polydata or unstructured mesh, cell values) |
| `data_graph.py` | Data structures for graph data (a set of 2D nodes connected by directed links) |
| `data_2d_worker.py` | Worker process for handling 2D data operations asynchronously |

## Data Types

### Data1D
Handles one-dimensional data for line plots:
- Time series data
- Line charts with multiple variables

### Data2D
Handles two-dimensional geometry data:
- Mesh cells with associated values
- Color maps (RGBA per cell)
- Alpha/transparency values
- Polygon-based or grid-based geometries

### Data3D
Handles three-dimensional VTK-based geometry data:
- VTK PolyData or UnstructuredGrid references
- Cell IDs, values, colors, and edge colors
- Built from `pv.PolyData` or `pv.UnstructuredGrid` objects via `from_vtk()` class method
- Supports deep copy and cell data updates

### DataGraph
Handles a graph of 2D plots connected by directed links (coupling topology):
- `datas`: mapping of node key to its `Data2D` payload (polygons only)
- `locations`: mapping of node key to its `(x, y)` layout position
- `links`: list of `Link` objects connecting nodes, each specifying the side
  (`top`/`bottom`/`left`/`right`) where it attaches to each endpoint

### DataContainer
Base container that manages visualization data properties:
- Stores current field values
- Manages color bar properties
- Tracks data metadata and labels

## Key Features

- **Color Management**: Built-in support for RGBA color arrays (0-255 range)
- **Field Labels**: Automatic tracking of available fields for selection widgets
- **Data Validation**: Methods to verify data integrity before visualization (`check_valid()`)
- **3D Support**: VTK-based 3D data structures with PolyData integration

## Integration

The data module integrates with:
- **Interfaces**: Data is loaded via interface modules (MED, VTK, CSV, structured mesh)
- **Plotters**: Data is rendered by 1D, 2D, 3D and graph plotter backends
- **Agents**: AI agent can manipulate Data2D properties programmatically Submodules ----------

## scivianna.data.data1d module

1D data container for Scivianna.

This module defines the Data1D class, which stores 1D line data (such as time histories or profiles) together with per-line colors and styles.

### `class scivianna.data.data1d.Data1D()  — bases: DataContainer`

Data class containing the 1D line data

#### `Data1D.from_dataframe(cls, df: pd.DataFrame)`

Build a Data1D object from a pandas DataFrame

## Parameters

df : pd.DataFrame  
Pandas dataframe to build the Data1D from

## Returns

Data1D  
Requested Data1D

#### `Data1D.from_serie_dict(cls, series: Dict[str, pd.Series])`

Build a Data1D object from a dict of pandas Series

## Parameters

series : Dict\[str, pd.Series\]  
Dict of pandas Series to build the Data1D with

## Returns

Data1D  
Requested Data1D

#### `Data1D.copy(self) -> 'Data1D'`

Returns a copy of self

## Returns

Data1D  
Identical copy of self

#### `Data1D.check_valid(self)`

Checks if this Data1D is valid, raises an AssertionError otherwise scivianna.data.data2d module ----------------------------

2D data container for Scivianna.

This module defines the Data2D class, which stores 2D geometry data in either polygon or grid format, along with associated field values and colors.

Data2D supports: - Polygon-based representation (unstructured meshes) - Grid-based representation (structured/rasterized data) - Automatic conversion between formats - Arithmetic operations (add, subtract, multiply, divide) - Color mapping and visualization properties

### `class scivianna.data.data2d.Data2D() -> None  — bases: DataContainer`

Container for 2D geometry data with field values and colors.

Data2D is the primary data structure for 2D visualization in Scivianna. It can represent geometry either as a list of polygons (for unstructured meshes) or as a 2D grid (for structured/rasterized data).

The class supports arithmetic operations between Data2D objects or between a Data2D and a scalar, enabling on-the-fly data processing.

## Attributes

data_type : DataType  
Whether data is stored as POLYGONS or GRID

polygons : List\[PolygonElement\]  
List of polygons (only used if data_type == POLYGONS)

grid : np.ndarray  
2D array of cell IDs (only used if data_type == GRID)

u_values : np.ndarray  
Grid point coordinates along horizontal axis

v_values : np.ndarray  
Grid point coordinates along vertical axis

cell_ids : np.ndarray  
Array of unique cell identifiers

cell_values : np.ndarray  
Array of field values (float or string) for each cell

cell_colors : np.ndarray  
Array of RGBA colors (0-255) for each cell

cell_edge_colors : np.ndarray  
Array of RGBA edge colors (0-255) for each cell

simplify : bool  
Whether to simplify polygons when converting from grid

#### `Data2D.from_polygon_list(cls, polygon_list: List[PolygonElement]) -> 'Data2D'`

Create a Data2D object from a list of polygons.

This factory method initializes a Data2D with polygon-based geometry, setting up default colors and empty value arrays. The cell IDs are extracted from the polygon cell_id attributes.

## Parameters

polygon_list : List\[PolygonElement\]  
List of PolygonElement objects defining the geometry. Each polygon should have a valid cell_id attribute.

## Returns

Data2D  
New Data2D object with data_type set to POLYGONS. Initial cell_values are set to NaN, cell_colors to white (255), and edge_colors to dark gray (50).

## Example

\>\>\> from scivianna.utils.polygonize_tools import PolygonElement, PolygonCoords \>\>\> \>\>\> \# Create a simple square polygon \>\>\> exterior = PolygonCoords( ... x_coords=\[0, 1, 1, 0\], ... y_coords=\[0, 0, 1, 1\] ... ) \>\>\> polygon = PolygonElement(exterior_polygon=exterior, holes=\[\], cell_id="cell_1") \>\>\> \>\>\> \# Create Data2D from polygon list \>\>\> data = Data2D.from_polygon_list(\[polygon\]) \>\>\> print(f"Data type: {data.data_type}") \# DataType.POLYGONS \>\>\> print(f"Number of cells: {len(data.cell_ids)}") \# 1

## See Also

from_grid : Create Data2D from 2D grid PolygonElement : Polygon data structure

#### `Data2D.from_grid(cls, grid: np.ndarray, u_values: np.ndarray, v_values: np.ndarray, simplify: bool=False)`

Build a Data2D object from a list of PolygonElement

## Parameters

grid : np.ndarray  
Numpy 2D array defining the 2D geometry

u_values : np.ndarray  
Coordinates of the grid points on the horizontal axis

v_values : np.ndarray  
Coordinates of the grid points on the vertical axis

simplify : bool  
Simplify the polygons when converted to polygon list

## Returns

Data2D  
Requested Data2D

#### `Data2D.convert_to_polygons(self)`

Convert the geometry to polygons

#### `Data2D.get_polygons(self) -> List[PolygonElement]`

Returns the polygon list of the geometry. If defined as grid, the grid is rasterized and self is converted to polygon data.

## Returns

List\[PolygonElement\]  
Polygon list

#### `Data2D.get_grid(self) -> np.ndarray`

Returns the grid associated to the current geometry

## Returns

np.ndarray  
Geometry as a 2D grid

## Raises

NotImplementedError  
Grid extraction from polygon list not implemented yet.

#### `Data2D.copy(self) -> 'Data2D'`

Returns a copy of self

## Returns

Data2D  
Identical copy of self

#### `Data2D.check_valid(self)`

Checks if this Data2D is valid, raises an AssertionError otherwise scivianna.data.data3d module ----------------------------

3D data container for Scivianna.

This module defines the Data3D class, which stores a VTK geometry together with per-cell values and colors used for 3D visualization.

### `class scivianna.data.data3d.Data3D()  — bases: DataContainer`

Data class containing the 3D geometry data

#### `Data3D.from_vtk(cls, polydata: Union['pv.PolyData', 'pv.UnstructuredGrid']) -> 'Data3D'`

Build a Data3D object from a pv.PolyData

## Parameters

polydata : pv.PolyData  
VTK polydata defining the geometry

## Returns

Data3D  
Requested Data3D

#### `Data3D.copy(self) -> 'Data3D'`

Returns a deep copy of self.

#### `Data3D.check_valid(self)`

Checks if this Data3D is valid, raises an AssertionError otherwise

#### `Data3D.update_cell_data(self)`

Updates the cell data stored in the polydata. scivianna.data.data_2d_worker module --------------------------------------

Worker operating on a copy of a Data2D, used by the LLM agent to test generated code.

### `class scivianna.data.data_2d_worker.Data2DWorker(data2d: Data2D)`

Worker that receives a Data2D object and works with it.

#### `Data2DWorker.has_changed(self) -> bool`

Tells if the data_2d was changed by the agent

## Returns

bool  
data_2d changed

#### `Data2DWorker.check_valid(self)`

Check if the Data2D is valid

## Raises

AssertionError  
Current Data2D is not valid

#### `Data2DWorker.get_ids(self) -> np.ndarray`

Returns the cell ID per 2D cell of the geometry

## Returns

np.ndarray  
Numpy array with the ID per cell

#### `Data2DWorker.get_values(self) -> np.ndarray`

Returns the value per 2D cell of the geometry

## Returns

np.ndarray  
Numpy array with the value per cell

#### `Data2DWorker.get_colors(self) -> np.ndarray`

Returns the color per 2D cell of the geometry. The returned object is a np.ndarray of shape (cell_count, 4), with values ranging from 0 to 255.

## Returns

np.ndarray  
Numpy array with the value per cell

#### `Data2DWorker.set_colors(self, colors: np.ndarray) -> bool`

Sets the cells color values, expects a numpy array of integers between 0 and 255 of shape (cell_count, 4). return True if it's ok.

## Parameters

colors : np.ndarray  
np array containing the new per cell colors. expects a numpy array of integers between 0 and 255 of shape (cell_count, 4).

## Returns

bool  
True if the given array is ok

#### `Data2DWorker.set_alphas(self, alphas: np.ndarray) -> bool`

Sets the cells opacity values, expects a numpy array of integers between 0 and 255. return True if it's ok.

## Parameters

alphas : np.ndarray  
Opacity values

## Returns

bool  
True if the given array is ok

#### `Data2DWorker.reset(self)`

Returns to the data2d provided in the initialization

#### `Data2DWorker.get_numpy(self)`

Returns the numpy module scivianna.data.data_container module -------------------------------------

Base class for scivianna data containers.

### `class scivianna.data.data_container.DataContainer`

Common base for the 1D/2D/3D/graph data containers, shared by serialization helpers. scivianna.data.data_graph module ---------------------------------

DataGraph: a graph of 2D plots connected by directed links (coupling topology).

### `class scivianna.data.data_graph.Link  — bases: BaseModel`

Directed connection between two nodes of a `DataGraph`.

A link references its endpoints by their node key in the graph's `datas`/`locations` dictionaries, and specifies on which side of each node the connection attaches. The directions are used to route the connector line around the panels when the graph is laid out.

## Attributes

source_data : str  
Key of the source node in the graph.

target_data : str  
Key of the target node in the graph.

source_direction : {'top', 'bottom', 'left', 'right'}  
Side of the source node where the link attaches.

target_direction : {'top', 'bottom', 'left', 'right'}  
Side of the target node where the link attaches.

label : str, optional  
Optional label displayed on the link.

### `class scivianna.data.data_graph.DataGraph(datas: dict[str, Data2D], locations: dict[str, tuple[float, float]], links: list[Link], labels: Optional[dict[str, Optional[str]]]=None, rotations: Optional[dict[str, float]]=None) -> None  — bases: DataContainer`

Container for a graph of 2D geometry data with field values and colors.

A `DataGraph` models a set of 2D plots (nodes) connected by directed links, as used to visualize the topology of coupled simulations: each node holds a `Data2D` payload (polygons + field values), a 2D position in the layout, and edges describe how data flows between nodes.

## Attributes

datas : dict\[str, Data2D\]  
Mapping of node key to its `Data2D` content. Every entry must use the polygon representation (`DataType.POLYGONS`).

locations : dict\[str, tuple\[float, float\]\]  
Mapping of node key to its `(x, y)` position in the graph layout. Must share exactly the same keys as `datas`.

links : list\[Link\]  
Directed connections between nodes; both endpoints must exist in `datas`.

labels : dict\[str, str \| None\], optional  
Mapping of node key to a display label. Nodes without an entry fall back to their key; a node mapped to `None` (or `""`) has no label.

rotations : dict\[str, float\], optional  
Mapping of node key to a rotation angle in degrees applied to the whole node (figure included). Defaults to 0 for every node. Module contents ---------------

Data containers for Scivianna.

Subpackage holding the data structures (1D, 2D, 3D and graph) exchanged between the code interfaces and the visualization panels.
