<!-- source: api/scivianna.plotter_2d.rst -->

# scivianna.plotter_2d package

# Scivianna 2D Plotter Module

The `plotter_2d` module provides plotting backends for rendering two-dimensional geometries and field data in Scivianna. It supports both grid-based and polygon-based visualizations.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `api.py` | Public API exports for 2D plotting using matplotlib |
| `generic_plotter.py` | Base class `GenericPlotter2D` defining the 2D plotting API |
| `grid/` | Grid-based (raster) visualization backend |
| `polygon/` | Polygon-based vector visualization backend |

## Submodules

### Grid Backend (`grid/`)
Renders 2D data as colored grid cells:
- `bokeh.py`: Bokeh-based interactive grid renderer
- `matplotlib.py`: Matplotlib static grid renderer
- `grid_tools.py`: Utility functions for grid manipulation

### Polygon Backend (`polygon/`)
Renders 2D data as vector polygons:
- `bokeh.py`: Bokeh-based interactive polygon renderer
- `matplotlib.py`: Matplotlib static polygon renderer

## GenericPlotter2D (Base Class)

Defines the interface for all 2D plotters:

### Key Methods

| Method | Purpose |
|--------|---------|
| `make_panel()` | Create and return the Panel display object |
| `update_geometry(cells, values)` | Update plot with new geometry and field data |
| `set_colormap(colormap)` | Set the color map for field visualization |
| `set_clim(vmin, vmax)` | Set color scale limits |
| `provide_on_mouse_move_callback(fn)` | Register mouse hover handler |
| `provide_on_clic_callback(fn)` | Register click handler |
| `get_mouse_location()` | Returns current mouse position in 3D world coordinates as `(x, y, z)` |

## Grid vs Polygon Rendering

### Grid Renderer
Best for:
- Regular grids
- Large or complex datasets where polygons are hard to compute

Features:
- Fast rendering for large datasets
- Pixel-based display
- Countour display

### Polygon Renderer
Best for:
- Unstructured meshes
- Irregular cell geometries
- When cell boundaries must be visible

Features:
- Vector-based precise cell shapes
- Cell boundary outlines
- Hover/click per-cell detection

## Interactive Features

Bokeh plotters can send back events when the mouse is moved or clicked on the geometry. Callback functions can be registered using the functions:

```python
def provide_on_mouse_move_callback(self, callback: Callable):
def provide_on_clic_callback(self, callback: Callable):
``` Subpackages -----------

- `scivianna.plotter_2d.grid` (`scivianna.plotter_2d.grid.md`)
- `scivianna.plotter_2d.polygon` (`scivianna.plotter_2d.polygon.md`)

## Submodules

## scivianna.plotter_2d.api module

Public matplotlib plotting API: render a scivianna frame.

### `scivianna.plotter_2d.api.plot_frame_in_axes(slave: Union[ComputeSlave, Geometry2D], coloring_label: str, axes: matplotlib.axes.Axes, u: Tuple[float, float, float]=X, v: Tuple[float, float, float]=Y, origin: Tuple[float, float, float]=None, size_u: float=1.0, size_v: float=1.0, color_map: str='BuRd', display_colorbar: bool=False, edge_width: float=1.0, options={}, plot_options={}, custom_colors: Dict[str, Dict[str, str]]={}, rename_values: Dict[str, Dict[str, str]]={}, legend_options: Dict[str, Any]={}, polygonize: bool=True, caller: str='MatplotlibAPI', color_seed: int=randint(0, 1000), log_scale: bool=False)`

Creates a figure and plots a geometry in it from an already initialized compute slave

## Parameters

slave : Union\[ComputeSlave, Geometry2D\]  
Slave from which get the geometry polygons or Geometry2D interface object

coloring_label : str  
Field to display in the plot

axes : matplotlib.axes.Axes  
matplotlib axis object (obtainable from a plt.subplot call)

u : Tuple\[float, float, float\], optional  
Horizontal coordinate director vector, by default X

v : Tuple\[float, float, float\], optional  
Vertical coordinate director vector, by default Y

origin : Tuple\[float, float, float\], optional  
Physical 3D position of the slice center, by default (0, 0, 0)

size_u : float, optional  
Size of the slice along the u axis, by default 1.

size_v : float, optional  
Size of the slice along the v axis, by default 1.

color_map : str, optional  
Colormap used to color the polygons, by default "BuRd"

edge_width : float, optional  
Cells edge width, by default 1.

display_colorbar : bool, optional  
Display the colorbar, by default False

options : dict, optional  
Extra coloring options, by default {}

plot_options : dict, optional  
Extra plot options given to geopandas, by default {}

custom_colors : Dict\[str, Dict\[str, str\]\], optional  
HTML color code per field value. Expects a dictionnary such as: { MATERIAL:{"iron" : \#ffffff, "water" : \#aa6868ff} } where MATERIAL is a displayed field name, and iron/water are its values. This parameter is only used for string based field.

rename_values : Dict\[str, Dict\[str, str\]\], optional  
Renames the values present in the data for the legend. Expects a dictionnary such as: { MATERIAL:{"iron" : "Iron", "water" : "Water"} } where MATERIAL is a displayed field name, and iron/water are its values. This parameter is only used for string based field.

legend_options : Dict\[str, Any\]  
Dictionnary of options provided when creating the legend

polygonize : bool  
Plot the geometry as polygons

color_seed : int  
Seed used to randomize the colors in FROM_STRING display mode. By default randomized from 0 to 1000.

log_scale : bool  
Use logarithmic scale. By default False.

## Returns

> plt.Figure  
> Figure containing the axes
>
> matplotlib.axes.Axes  
> Axes in which the geometry was plotted

### `scivianna.plotter_2d.api.plot_frame(slave: Union[ComputeSlave, Geometry2D], coloring_label: str, u: Tuple[float, float, float]=X, v: Tuple[float, float, float]=Y, origin: Tuple[float, float, float]=None, size_u: float=1.0, size_v: float=1.0, color_map: str='BuRd', display_colorbar: bool=False, edge_width: float=1.0, options={}, plot_options={}, custom_colors: Dict[str, Dict[str, str]]={}, rename_values: Dict[str, Dict[str, str]]={}, legend_options: Dict[str, Any]={}, polygonize: bool=True, caller: str='MatplotlibAPI', color_seed: int=randint(0, 1000), log_scale: bool=False) -> Tuple[plt.Figure, matplotlib.axes.Axes]`

Creates a figure and plots a geometry in it from an already initialized compute slave

## Parameters

slave : Union\[ComputeSlave, Geometry2D\]  
Slave from which get the geometry polygons or Geometry2D interface object

coloring_label : str  
Field to display in the plot

u : Tuple\[float, float, float\], optional  
Horizontal coordinate director vector, by default X

v : Tuple\[float, float, float\], optional  
Vertical coordinate director vector, by default Y

origin : Tuple\[float, float, float\], optional  
Physical 3D position of the slice center, by default (0, 0, 0)

size_u : float, optional  
Size of the slice along the u axis, by default 1.

size_v : float, optional  
Size of the slice along the v axis, by default 1.

color_map : str, optional  
Colormap used to color the polygons, by default "BuRd"

display_colorbar : bool, optional  
Display the colorbar, by default False

edge_width : float, optional  
Cells edge width, by default 1.

options : dict, optional  
Extra coloring options, by default {}

plot_options : dict, optional  
Extra plot options given to geopandas, by default {}

custom_colors : Dict\[str, Dict\[str, str\]\], optional  
HTML color code per field value. Expects a dictionnary such as: { MATERIAL:{"iron" : \#ffffff, "water" : \#aa6868ff} } where MATERIAL is a displayed field name, and iron/water are its values. This parameter is only used for string based field.

rename_values : Dict\[str, Dict\[str, str\]\], optional  
Renames the values present in the data for the legend. Expects a dictionnary such as: { MATERIAL:{"iron" : "Iron", "water" : "Water"} } where MATERIAL is a displayed field name, and iron/water are its values. This parameter is only used for string based field.

legend_options : Dict\[str, Any\]  
Dictionnary of options provided when creating the legend

polygonize : bool  
Plot the geometry as polygons

color_seed : int  
Seed used to randomize the colors in FROM_STRING display mode. By default randomized from 0 to 1000.

log_scale : bool  
Use logarithmic scale. By default False.

## Returns

> plt.Figure  
> Figure containing the axes
>
> matplotlib.axes.Axes  
> Axes in which the geometry was plotted scivianna.plotter_2d.generic_plotter module ---------------------------------------------

Abstract interface for 2D geometry plotters.

### `class scivianna.plotter_2d.generic_plotter.Plotter2D`

Generic 2D geometry plotter interface

#### `Plotter2D.display_borders(self, display: bool)`

Display or hides the figure borders and axis

## Parameters

display : bool  
Display if true, hides otherwise

#### `Plotter2D.update_colorbar(self, display: bool, value_range: Tuple[float, float], log_scale: bool=False)`

Displays or hide the color bar, if display, updates its range

## Parameters

display : bool  
Display or hides the color bar

value_range : Tuple\[float, float\]  
New colormap range

log_scale : bool  
Use logarithmic scale

#### `Plotter2D.set_color_map(self, color_map_name: str)`

Sets the colorbar color map name

## Parameters

color_map_name : str  
Color map name

#### `Plotter2D.plot_2d_frame(self, data: Data2D)`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data2D  
Data2D object containing the geometry to plot

#### `Plotter2D.update_2d_frame(self, data: Data2D)`

Updates plot to the figure

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Plotter2D.update_colors(self, data: Data2D)`

Updates the colors of the displayed polygons

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Plotter2D.make_panel(self) -> pn.viewable.Viewable`

Makes the Holoviz panel viewable displayed in the web app.

## Returns

pn.viewable.Viewable  
Displayed viewable

#### `Plotter2D.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Plotter2D.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Plotter2D.set_axes(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float])`

Stores the u v axes of the current plot

## Parameters

u : Tuple\[float, float, float\]  
Horizontal axis direction vector

v : Tuple\[float, float, float\]  
Vertical axis direction vector

origin : Tuple\[float, float, float\]  
Frame center

#### `Plotter2D.enable_highlight(self, enable: bool=True)`

Enable hover highlight

## Parameters

enable : bool, optional  
Highlight enabled, by default True

#### `Plotter2D.get_mouse_location(self) -> Tuple[float, float, float]`

Returns the current mouse location (returns the panel exit location if out)

## Returns

Tuple\[float, float, float\]  
Mouse location

#### `Plotter2D.get_mouse_info(self) -> str`

Returns the information on mouse location

## Returns

str  
Information on mouse hovered location Module contents ---------------

2D plot backends for scivianna: abstract interface, public API and polygon/grid renderers.
