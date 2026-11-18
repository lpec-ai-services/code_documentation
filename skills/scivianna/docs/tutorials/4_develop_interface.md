<!-- source: 4_develop_interface.ipynb -->

# Tutorial 4: Developing a Custom Interface (Dev)

This tutorial shows how to create a custom data interface for scivianna, enabling visualization of any data source through the GUI.

## What is an Interface?

An **Interface** in scivianna is a bridge between your data and the visualization panels. It tells scivianna:

- How to load your data from files
- What fields are available for display
- How to compute 2D slices for geometry panels
- How to get values at specific points (optional)

## Interface Class Hierarchy

    GenericInterface          - Base class: file I/O, serialization
        └── Geometry2D        - Adds 2D geometry slice computation
            ├── Geometry2DPolygon  - Returns polygon vertex lists
            └── Geometry2DGrid     - Returns rasterized grid data
        └── Geometry3D        - Adds 3D geometry and cell values
    ValueAtLocation           - Mixin: point value queries
    Value1DAtLocation         - Mixin: 1D line value queries
    DataFrameInterface        - Mixin: returns data as pandas DataFrame
    CouplingInterface         - Mixin: C3PO coupling functions

**You compose interfaces by inheriting from multiple classes.** For example:

``` python
class MyInterface(Geometry2DPolygon, ValueAtLocation):
    pass
```

## Class Attributes

| Attribute       | Description                                             |
|-----------------|---------------------------------------------------------|
| `extensions`    | List of extension classes to attach to this interface   |
| `geometry_type` | GeometryType enum (2D, 3D, etc.)                        |
| `data_type`     | DataType enum (DATA_POLYGON, DATA_GRID)                 |
| `rasterized`    | Boolean: True if geometry comes from grid rasterization |

## Complete Example: DummyTestInterface

Here's a complete example of a simple interface that creates 3 rectangular polygons. This is the same interface used in the test suite.

### How It Works

1.  **`__init__`**: Initializes storage for computed data, file paths, and frame tracking
2.  **`read_file`**: Stores file paths (this example doesn't actually parse files)
3.  **`compute_2D_data`**: Creates 3 rectangles that shift based on the `w_value` (z-coordinate)
4.  **`get_labels`**: Returns available field names: MESH, MATERIAL, VALUE
5.  **`get_value_dict`**: Returns different values depending on the selected field
6.  **`get_label_coloring_mode`**: Tells scivianna how to color each field type

``` python
from scivianna.interface.generic_interface import Geometry2DPolygon
from scivianna.data.data2d import Data2D
from scivianna.enums import GeometryType, VisualizationMode
from scivianna.utils.polygonize_tools import PolygonElement, PolygonCoords
from typing import Tuple, Dict, Any, List, Union
import multiprocessing as mp

class DummyTestInterface(Geometry2DPolygon):
    """A simple interface that creates 3 rectangular polygons.
    
    This is a minimal example showing how to:
    - Define geometry using PolygonElement and PolygonCoords
    - Return Data2D for visualization
    - Handle multiple field types (MESH, MATERIAL, VALUE)
    """
    
    # Required class attribute - tells scivianna this is a 3D infinite geometry
    geometry_type: GeometryType = GeometryType._3D_INFINITE
    
    def __init__(self):
        """Initialize the interface.
        
        Sets up dictionaries to store:
        - Computed Data2D objects per caller
        - File paths per file label
        - Last computed frame parameters for caching
        """
        self.data: Dict[str, Data2D] = {}
        self.file_path: Dict[str, str] = {}
        self.current_field = None
        self.last_computed_frame: Dict[str, List[float]] = {}

    def read_file(self, file_path: str, file_label: str):
        """Store the file path (this example doesn't actually read files).
        
        Parameters
        ----------
        file_path : str
            Path to the file
        file_label : str
            Label identifying the file type (e.g., 'GEOMETRY', 'CSV')
        """
        self.file_path[file_label] = file_path

    def compute_2D_data(
        self,
        u: Tuple[float, float, float],
        v: Tuple[float, float, float],
        origin: Tuple[float, float, float],
        size_u: float,
        size_v: float,
        w_value: float,
        q_tasks: mp.Queue,
        options: Dict[str, Any],
        caller: str = "API",
    ) -> Tuple[Data2D, bool]:
        """Compute and return 2D geometry data.
        
        This method creates 3 rectangles offset by w_value. The geometry
        is cached to avoid recomputation when the frame hasn't changed.
        
        Parameters
        ----------
        u, v : Tuple[float, float, float]
            Direction vectors for the 2D viewport. These define the plane
            in which we're slicing the 3D geometry.
        origin : Tuple[float, float, float]
            Physical 3D position of the slice corner (u_min*u + v_min*v + w_value*w)
        size_u, size_v : float
            Size of the slice along the u and v axes (u_max - u_min, v_max - v_min)
        w_value : float
            Coordinate perpendicular to the 2D plane (depth coordinate)
        q_tasks : mp.Queue
            Queue for slave communication - used for inter-process messaging
        options : Dict[str, Any]
            Additional computation options passed from the GUI
        caller : str
            Identifier of the caller (e.g., "API", "GUI"). Allows different
            callers to have separate cached data.
            
        Returns
        -------
        Tuple[Data2D, bool]
            Data2D object containing geometry, and True if data was updated
        """
        # Check if we already computed this frame (caching mechanism)
        last_frame_key = (*origin, size_u, size_v, w_value)
        if (caller in self.last_computed_frame) and (
            self.last_computed_frame[caller] == last_frame_key
        ) and (caller in self.data):
            print("Skipping polygon computation (cached).")
            return self.data[caller], False

        # Create 3 rectangles offset by w_value
        # v_offset shifts the rectangles based on the view direction and depth
        # In this example, we don't read the axes bounds as we know the whole slice geometry.
        v_offset = v[1] + 10 * w_value
        polygons = [
            PolygonElement(
                exterior_polygon=PolygonCoords(
                    x_coords=[i, i, i+1, i+1],
                    y_coords=[0+v_offset, 1+v_offset, 1+v_offset, 0+v_offset]
                ),
                holes=[],
                cell_id=i
            )
            for i in range(3)
        ]

        print(f"Offset: {v_offset}")

        # Cache and return the result
        self.last_computed_frame[caller] = last_frame_key
        self.data[caller] = Data2D.from_polygon_list(polygons)
        return self.data[caller], True

    def get_labels(self) -> List[str]:
        """Return available field names.
        
        Returns
        -------
        List[str]
            List of field names that can be displayed
        """
        return ["MESH", "MATERIAL", "VALUE"]

    def get_value_dict(
        self, 
        value_label: str, 
        cells: List[Union[int, str]], 
        options: Dict[str, Any], 
        caller: str = "API"
    ) -> Dict[Union[int, str], Union[float, str]]:
        """Return field values for each cell.
        
        This method is called when the GUI needs to display cell labels
        or color the geometry based on field values.
        
        Parameters
        ----------
        value_label : str
            Field name to get values for (e.g., "MESH", "MATERIAL")
        cells : List[Union[int, str]]
            List of cell IDs requesting values
        options : Dict[str, Any]
            Additional options from the GUI
            
        Returns
        -------
        Dict[Union[int, str], Union[float, str]]
            Mapping of cell ID to value
        """
        self.current_field = value_label
        
        if value_label == "MESH":
            # MESH returns NaN - no labels displayed
            return {cell_id: float('nan') for cell_id in cells}
        if value_label == "MATERIAL":
            # MATERIAL returns the cell ID as a string
            return {cell_id: str(cell_id) for cell_id in cells}
        if value_label == "VALUE":
            # VALUE returns the cell ID as a float
            return {cell_id: float(cell_id) for cell_id in cells}

        raise NotImplementedError(
            f"Field '{value_label}' not implemented. Available: {self.get_labels()}"
        )

    def get_label_coloring_mode(self, label: str) -> VisualizationMode:
        """Return the visualization mode for a field.
        
        This tells scivianna how to interpret and color the data:
        - NONE: Don't display this field
        - FROM_STRING: Use categorical colors for string values
        - FROM_VALUE: Use a colormap for numeric values
        
        Parameters
        ----------
        label : str
            Field name
            
        Returns
        -------
        VisualizationMode
            NONE for MESH, FROM_STRING for MATERIAL, FROM_VALUE otherwise
        """
        if label == "MESH":
            return VisualizationMode.NONE
        if label == "MATERIAL":
            return VisualizationMode.FROM_STRING
        return VisualizationMode.FROM_VALUE

    def get_file_input_list(self) -> List[Tuple[str, str]]:
        """Return file type filters for the GUI.
        
        These appear in the file picker dialog to help users select
        appropriate files.
        
        Returns
        -------
        List[Tuple[str, str]]
            List of (label, description) tuples
        """
        return [("GEOMETRY", "Geometry file."), ("CSV", "CSV result file.")]

# Test the interface
if __name__ == "__main__":
    iface = DummyTestInterface()
    
    # Simulate reading a file
    iface.read_file("/path/to/geometry.extension", "GEOMETRY")
    print(f"File path: {iface.file_path}")
    
    # Get available fields
    print(f"Labels: {iface.get_labels()}")
    
    # Get value dict for each field type
    cells = [0, 1, 2]
    for label in iface.get_labels():
        values = iface.get_value_dict(label, cells, {})
        print(f"{label}: {values}")
```

## Using the Interface with Panel2D

To use your interface in the GUI, you need to create a `ComputeSlave` and `Panel2D`:

``` python
from scivianna.slave import ComputeSlave
from scivianna.panel.panel_2d import Panel2D

# Create a slave with your interface
slave = ComputeSlave(DummyTestInterface)

# Create the panel
panel = Panel2D(slave, name="My View")

# The panel now displays your 3 rectangles!
# In a real application, you would show it in a window
```

## API Reference: Methods by Base Class

### GenericInterface Methods

| Method                             | Description                                                          |
|------------------------------------|----------------------------------------------------------------------|
| `read_file(file_path, file_label)` | Load data from a file. Required.                                     |
| `get_labels()`                     | Return list of available field names. Default: `[MESH, MATERIAL]`.   |
| `get_label_coloring_mode(label)`   | Return visualization mode (NONE, FROM_STRING, FROM_VALUE). Required. |
| `get_file_input_list()`            | Return file type filters for GUI picker. Required.                   |
| `serialize(obj, key)`              | Prepare object for multiprocessing transmission.                     |
| `save(file_path, include_files)`   | Save interface state to pickle file.                                 |
| `load(file_path, include_files)`   | Load interface state from pickle file.                               |

### Geometry2D Methods (for 2D visualization)

| Method                                                                             | Description                                                      |
|------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `compute_2D_data(u, v, origin, size_u, size_v, w_value, q_tasks, options, caller)` | Compute and return 2D geometry data. Required for 2D interfaces. |
| `get_value_dict(value_label, cells, options, caller)`                              | Return field values for each cell. Required for 2D interfaces.   |

### ValueAtLocation Methods (optional mixins)

| Method                                                                | Description                                     |
|-----------------------------------------------------------------------|-------------------------------------------------|
| `get_value(position, cell_index, material_name, field, options)`      | Get field value at a specific 3D location.      |
| `get_values(positions, cell_indexes, material_names, field, options)` | Get field values at multiple locations (batch). |

### Value1DAtLocation Methods (optional mixins)

| Method                                                              | Description                                        |
|---------------------------------------------------------------------|----------------------------------------------------|
| `get_1D_value(position, cell_index, material_name, field, options)` | Get 1D data (time series, spectrum) at a location. |

### Geometry3D Methods (for 3D visualization)

| Method                                                   | Description                                                          |
|----------------------------------------------------------|----------------------------------------------------------------------|
| `compute_3D_data(options)`                               | Compute and return 3D geometry data. Required for 3D interfaces.     |
| `get_3d_value_dict(value_label, cells, options, caller)` | Return field values for each cell in 3D. Required for 3D interfaces. |

### DataFrameInterface Methods (for tabular display)

| Method                                    | Description                                                                     |
|-------------------------------------------|---------------------------------------------------------------------------------|
| `get_dataframe(cell_id, origin, options)` | Return the interface data as a pandas DataFrame. Required for DataFrame panels. |

### CouplingInterface Methods (for C3PO coupling)

| Method                         | Description                               |
|--------------------------------|-------------------------------------------|
| `set_time(time)`               | Set current time for time-dependent data. |
| `update_data(key, data)`       | Replace data for a given key.             |
| `append_data(key, data)`       | Append data with current time stamp.      |
| `update_mesh(key, data)`       | Replace mesh and data.                    |
| `append_mesh(key, data)`       | Append mesh and data with time stamp.     |
| `get_template(name)`           | Get field template for C3PO.              |
| `set_template(name, template)` | Set field template for C3PO.              |

## Summary

To create a custom interface:

1.  **Inherit from the appropriate base class**:

    - `Geometry2DPolygon` for polygon/line geometry
    - `Geometry2DGrid` for raster/grid data
    - `Geometry3D` for 3D volumetric geometry
    - Add mixins as needed: `ValueAtLocation`, `Value1DAtLocation`, `DataFrameInterface`, `CouplingInterface`

2.  **Set class attributes**:

    - `geometry_type`: GeometryType enum
    - `data_type`: DataType enum
    - `extensions`: List of extension classes (optional)

3.  **Implement required methods** based on your base class:

    - All: `read_file()`, `get_labels()`, `get_label_coloring_mode()`, `get_file_input_list()`
    - Geometry2D: `compute_2D_data()`, `get_value_dict()`
    - Geometry3D: `compute_3D_data()`, `get_3d_value_dict()`
    - DataFrameInterface: `get_dataframe()`
    - ValueAtLocation: `get_value()`

4.  **Use `Data2D.from_polygon_list()`** to create polygon data easily

5.  **Cache computed frames** to avoid unnecessary recomputation

6.  **Register your interface** so it can be discovered by the framework:

    ``` python
    from scivianna.interface import register_interface
    register_interface("MyInterfaceKey", MyInterfaceClass)
    ```
