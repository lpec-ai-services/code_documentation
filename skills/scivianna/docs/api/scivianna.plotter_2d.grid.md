<!-- source: api/scivianna.plotter_2d.grid.rst -->

# scivianna.plotter_2d.grid package

## Submodules

## scivianna.plotter_2d.grid.bokeh module

Bokeh-based 2D grid (rasterized) plotter.

### `class scivianna.plotter_2d.grid.bokeh.Bokeh2DGridPlotter()  — bases: Plotter2D`

2D geometry plotter based on the bokeh python module

#### `Bokeh2DGridPlotter.display_borders(self, display: bool)`

Display or hides the figure borders and axis

## Parameters

display : bool  
Display if true, hides otherwise

#### `Bokeh2DGridPlotter.update_colorbar(self, display: bool, value_range: Tuple[float, float], log_scale: bool=None)`

Displays or hide the color bar, if display, updates its range

## Parameters

display : bool  
Display or hides the color bar

value_range : Tuple\[float, float\]  
New colormap range

log_scale : bool  
Use logarithmic scale. If None, recovers the last used log_scale value.

#### `Bokeh2DGridPlotter.set_color_map(self, color_map_name: str)`

Sets the colorbar color map name

## Parameters

color_map_name : str  
Color map name

#### `Bokeh2DGridPlotter.plot_2d_frame(self, data: Data2D)`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data2D  
Data2D object containing the geometry to plot

#### `Bokeh2DGridPlotter.update_2d_frame(self, data: Data2D)`

Updates plot to the figure

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Bokeh2DGridPlotter.update_colors(self, data: Data2D)`

Updates the colors of the displayed polygons

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Bokeh2DGridPlotter.update_range(self, event: events.RangesUpdate)`

Forward the figure range change to the registered callback.

#### `Bokeh2DGridPlotter.make_panel(self) -> pn.viewable.Viewable`

Makes the Holoviz panel viewable displayed in the web app.

## Returns

pn.viewable.Viewable  
Displayed viewable

#### `Bokeh2DGridPlotter.get_resolution(self) -> Tuple[float, float]`

Returns the current plot resolution to display. For resolution based codes, it will be replaced by the value present in the gui

## Returns

Tuple\[float, float\]  
Resolution if possible, else (None, None)

#### `Bokeh2DGridPlotter.export(self, file_name: str, title='Bokeh 2D plot')`

Exports the plot in a file

## Parameters

file_name : str  
Export file path

#### `Bokeh2DGridPlotter.send_event(self, callback)`

Calling the callback to update the position and current cell_id to the layout

## Parameters

callback : function  
Function to call

#### `Bokeh2DGridPlotter.on_mouse_move(self, _)`

Callback called when the mouse is moved. The mouse location in the grid is saved, and an update is requested at the current location after a timeout.

## Parameters

\_ : Any  
Calling event

#### `Bokeh2DGridPlotter.update_plot_after_mouse_move(self, i: int, j: int)`

Updates the plot after changing the cell at location (i, j) to 0.6. The update is only done if the mouse is currently at (i, j)

## Parameters

i : int  
U coordinate

j : int  
V coordinate

#### `Bokeh2DGridPlotter.reset_hover(self)`

Clear the hovered cell highlight and restore the frame.

#### `Bokeh2DGridPlotter.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Bokeh2DGridPlotter.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Bokeh2DGridPlotter.set_axes(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float])`

Stores the u v axes of the current plot

## Parameters

u : Tuple\[float, float, float\]  
Horizontal axis direction vector

v : Tuple\[float, float, float\]  
Vertical axis direction vector

origin : Tuple\[float, float, float\]  
Frame center

#### `Bokeh2DGridPlotter.get_mouse_location(self) -> Tuple[float, float, float]`

Returns the current mouse location (returns the panel exit location if out)

## Returns

Tuple\[float, float, float\]  
Mouse location

#### `Bokeh2DGridPlotter.get_mouse_info(self) -> str`

Returns a human-readable string describing the hovered cell (coordinates, cell id, value).

Returns an empty string when the mouse is not over this figure.

#### `Bokeh2DGridPlotter.set_range(self, u_range: Tuple[float, float], v_range: Tuple[float, float])`

Updates the plot ranges

## Parameters

u_range : Tuple\[float, float\]  
Range along the horizontal axis

v_range : Tuple\[float, float\]  
Range along the vertical axis scivianna.plotter_2d.grid.grid_tools module ---------------------------------------------

Helpers to build and manipulate 2D grid (rasterized) data.

### `scivianna.plotter_2d.grid.grid_tools.get_grids(data: Data2D, display_edges: bool) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]`

Provides 2D grids and color 3D grid from a Data2D, darkens the edges if requested

## Parameters

data : Data2D  
Data2D to display

display_edges : bool  
Darken edges

## Returns

Tuple\[np.ndarray, np.ndarray, np.ndarray, np.ndarray\]  
Bokeh readable 2D image, 3D color grid, id grid, value grid scivianna.plotter_2d.grid.matplotlib module --------------------------------------------

Matplotlib-based 2D grid (rasterized) plotter.

### `class scivianna.plotter_2d.grid.matplotlib.Matplotlib2DGridPlotter()  — bases: Plotter2D`

2D geometry plotter based on the bokeh python module

#### `Matplotlib2DGridPlotter.display_borders(self, display: bool)`

Display or hides the figure borders and axis

## Parameters

display : bool  
Display if true, hides otherwise

#### `Matplotlib2DGridPlotter.update_colorbar(self, display: bool, value_range: Tuple[float, float], log_scale: bool=None)`

Displays or hide the color bar, if display, updates its range

## Parameters

display : bool  
Display or hides the color bar

value_range : Tuple\[float, float\]  
New colormap range

log_scale : bool  
Use logarithmic scale. If None, recovers the last used log_scale value.

#### `Matplotlib2DGridPlotter.set_color_map(self, color_map_name: str)`

Sets the colorbar color map name

## Parameters

color_map_name : str  
Color map name

#### `Matplotlib2DGridPlotter.plot_2d_frame(self, data: Data2D)`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data2D  
Data2D object containing the geometry to plot

#### `Matplotlib2DGridPlotter.plot_2d_frame_in_axes(self, data: Data2D, axes: matplotlib.axes.Axes, plot_options: Dict[str, Any]={})`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data2D  
Data2D object containing the geometry to plot

axes : matplotlib.axes.Axes  
Axes in which plot the figure

plot_options : Dict\[str, Any\])  
Color options to be passed on to the actual plot function, such as edgecolor, facecolor, linewidth, markersize, alpha.

#### `Matplotlib2DGridPlotter.update_2d_frame(self, data: Data2D)`

Updates plot to the figure

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Matplotlib2DGridPlotter.update_colors(self, data: Data2D)`

Updates the colors of the displayed polygons

## Parameters

data : Data2D  
Data2D object containing the data to update

#### `Matplotlib2DGridPlotter.make_panel(self) -> pn.viewable.Viewable`

Makes the Holoviz panel viewable displayed in the web app.

## Returns

pn.viewable.Viewable  
Displayed viewable

#### `Matplotlib2DGridPlotter.get_resolution(self) -> Tuple[float, float]`

Returns the current plot resolution to display. For resolution based codes, it will be replaced by the value present in the gui

## Returns

Tuple\[float, float\]  
Resolution if possible, else (None, None)

#### `Matplotlib2DGridPlotter.export(self, file_name: str, title='Bokeh 2D plot')`

Exports the plot in a file

## Parameters

file_name : str  
Export file path

#### `Matplotlib2DGridPlotter.set_axes(self, u: Tuple[float, float, float], v: Tuple[float, float, float], origin: Tuple[float, float, float])`

Stores the u v axes of the current plot

## Parameters

u : Tuple\[float, float, float\]  
Horizontal axis direction vector

v : Tuple\[float, float, float\]  
Vertical axis direction vector

origin : Tuple\[float, float, float\]  
Frame center Module contents ---------------

Rasterized (grid) 2D renderers for scivianna.
