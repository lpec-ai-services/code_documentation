<!-- source: api/scivianna.plotter_2d.polygon.rst -->

# scivianna.plotter_2d.polygon package

## Submodules

## scivianna.plotter_2d.polygon.bokeh module

Bokeh-based 2D polygon plotter with colorbar and hover support.

### `class scivianna.plotter_2d.polygon.bokeh.Bokeh2DPolygonPlotter()  — bases: Plotter2D`

2D geometry plotter based on the bokeh python module

#### `Bokeh2DPolygonPlotter.display_borders(self, display: bool)`

Display or hides the figure borders and axis

## Parameters

display : bool  
Display if true, hides otherwise

#### `Bokeh2DPolygonPlotter.update_colorbar(self, display: bool, value_range: Tuple[float, float], log_scale: bool=None)`

Displays or hide the color bar, if display, updates its range

## Parameters

display : bool  
Display or hides the color bar

value_range : Tuple\[float, float\]  
New colormap range

log_scale : bool  
Use logarithmic scale. If None, recovers the last used log_scale value.

#### `Bokeh2DPolygonPlotter.set_color_map(self, color_map_name: str)`

Sets the colorbar color map name

## Parameters

color_map_name : str  
Color map name

#### `Bokeh2DPolygonPlotter.plot_2d_frame(self, data: Data2D)`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data2D  
Data2D object containing the geometry to plot

#### `Bokeh2DPolygonPlotter.update_2d_frame(self, data: Data2D)`

Updates plot to the figure

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Bokeh2DPolygonPlotter.update_colors(self, data: Data2D)`

Updates the colors of the displayed polygons

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Bokeh2DPolygonPlotter.update_range(self, event: events.RangesUpdate)`

Forward the figure range change to the registered callback.

#### `Bokeh2DPolygonPlotter.make_panel(self) -> pn.viewable.Viewable`

Makes the Holoviz panel viewable displayed in the web app.

## Returns

pn.viewable.Viewable  
Displayed viewable

#### `Bokeh2DPolygonPlotter.get_resolution(self) -> Tuple[float, float]`

Returns the current plot resolution to display. For resolution based codes, it will be replaced by the value present in the gui

## Returns

Tuple\[float, float\]  
Resolution if possible, else (None, None)

#### `Bokeh2DPolygonPlotter.export(self, file_name: str, title='Bokeh 2D plot')`

Exports the plot in a file

## Parameters

file_name : str  
Export file path

#### `Bokeh2DPolygonPlotter.send_event(self, callback)`

Call the mouse callback with the current hover position and cell.

#### `Bokeh2DPolygonPlotter.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Bokeh2DPolygonPlotter.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Bokeh2DPolygonPlotter.set_axes(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float])`

Stores the u v axes of the current plot

## Parameters

u : Tuple\[float, float, float\]  
Horizontal axis direction vector

v : Tuple\[float, float, float\]  
Vertical axis direction vector

origin : Tuple\[float, float, float\]  
Frame center

#### `Bokeh2DPolygonPlotter.get_mouse_location(self) -> Tuple[float, float, float]`

Returns the current mouse location (returns the panel exit location if out)

## Returns

Tuple\[float, float, float\]  
Mouse location

#### `Bokeh2DPolygonPlotter.get_mouse_info(self) -> str`

Returns a human-readable string describing the hovered cell (coordinates, cell id, value).

Returns an empty string when the mouse is not over this figure. scivianna.plotter_2d.polygon.matplotlib module -----------------------------------------------

Matplotlib-based 2D polygon plotter (used by the public plotting API).

### `class scivianna.plotter_2d.polygon.matplotlib.Matplotlib2DPolygonPlotter()  — bases: Plotter2D`

2D geometry plotter based on the bokeh python module

#### `Matplotlib2DPolygonPlotter.display_borders(self, display: bool)`

Display or hides the figure borders and axis

## Parameters

display : bool  
Display if true, hides otherwise

#### `Matplotlib2DPolygonPlotter.update_colorbar(self, display: bool, value_range: Tuple[float, float], log_scale: bool=None)`

Displays or hide the color bar, if display, updates its range

## Parameters

display : bool  
Display or hides the color bar

value_range : Tuple\[float, float\]  
New colormap range

log_scale : bool  
Use logarithmic scale. If None, recovers the last used log_scale value.

#### `Matplotlib2DPolygonPlotter.set_color_map(self, color_map_name: str)`

Sets the colorbar color map name

## Parameters

color_map_name : str  
Color map name

#### `Matplotlib2DPolygonPlotter.plot_2d_frame(self, data: Data2D)`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data2D  
Data2D object containing the geometry to plot

#### `Matplotlib2DPolygonPlotter.plot_2d_frame_in_axes(self, data: Data2D, axes: matplotlib.axes.Axes, plot_options: Dict[str, Any]={})`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data2D  
Geometry data

axes : matplotlib.axes.Axes  
Axes in which plot the figure

plot_options : Dict\[str, Any\])  
Color options to be passed on to the actual plot function, such as edgecolor, facecolor, linewidth, markersize, alpha.

#### `Matplotlib2DPolygonPlotter.update_2d_frame(self, data: Data2D)`

Updates plot to the figure

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Matplotlib2DPolygonPlotter.update_colors(self, data: Data2D)`

Updates the colors of the displayed polygons

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Matplotlib2DPolygonPlotter.make_panel(self) -> pn.viewable.Viewable`

Makes the Holoviz panel viewable displayed in the web app.

## Returns

pn.viewable.Viewable  
Displayed viewable

#### `Matplotlib2DPolygonPlotter.get_resolution(self) -> Tuple[float, float]`

Returns the current plot resolution to display. For resolution based codes, it will be replaced by the value present in the gui

## Returns

Tuple\[float, float\]  
Resolution if possible, else (None, None)

#### `Matplotlib2DPolygonPlotter.export(self, file_name: str, title='Bokeh 2D plot')`

Exports the plot in a file

## Parameters

file_name : str  
Export file path

#### `Matplotlib2DPolygonPlotter.set_axes(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float])`

Stores the u v axes of the current plot

## Parameters

u : Tuple\[float, float, float\]  
Horizontal axis direction vector

v : Tuple\[float, float, float\]  
Vertical axis direction vector

origin : Tuple\[float, float, float\]  
Frame center Module contents ---------------

Polygon-based 2D renderers for scivianna.
