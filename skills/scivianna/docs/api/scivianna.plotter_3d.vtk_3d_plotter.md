<!-- source: api/scivianna.plotter_3d.vtk_3d_plotter.rst -->

# scivianna.plotter_3d.vtk_3d_plotter module

VTK-based 3D plotter wrapping the scivianna_vtk VTKPlotter component.

### `class scivianna.plotter_3d.vtk_3d_plotter.Plotter3D()  — bases: Plotter3D`

Unfinished 3D plotter to get the coupling working

#### `Plotter3D.plot(self, data: Data3D)`

Adds a new plot to the figure from a set of polygons

## Parameters

data : Data3D  
Data3D object containing the geometry and data to plot

#### `Plotter3D.update_plot(self, data: Data3D)`

Updates plot to the figure

## Parameters

data : Data3D  
Data3D object containing the geometry and data to plot

#### `Plotter3D.make_panel(self)`

Returns teh viewable displayed in the 3D panel

## Returns

pn.viewable.Viewable  
3D potter

#### `Plotter3D.update_colorbar(self, display: bool, value_range: Tuple[float, float], log_scale: bool=False)`

Displays or hide the color bar, if display, updates its range

## Parameters

display : bool  
Display or hides the color bar

value_range : Tuple\[float, float\]  
New colormap range

log_scale : bool  
Use logarithmic scale

#### `Plotter3D.set_color_map(self, color_map_name: str)`

Sets the colorbar color map name

## Parameters

color_map_name : str  
Color map name

#### `Plotter3D.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Plotter3D.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `Plotter3D.provide_on_axes_change_callback(self, callback: Callable)`

Stores a function to call everytime the user changes the axes. Functions arguments are the new axis values (u, v, origin, size_u, size_v).

## Parameters

callback : Callable  
Function to call.

#### `Plotter3D.move_slice_to(self, u: float=None, v: float=None, origin: Tuple[float, float, float]=None)`

Moves the slice to the given location

## Parameters

u : float, optional  
First axis direction vector

v : float, optional  
Second axis direction vector

origin : Tuple\[float, float, float\], optional  
Physical 3D position of the slice center (center_u\*u + center_v\*v + w\*w), by default None

#### `Plotter3D.send_event(self, callback)`

Call the mouse callback with the current hovered cell and position.

#### `Plotter3D.get_slice_normal(self)`

Returns the normal of the slice plane

## Returns

np.ndarray  
Normal of the slice plane

#### `Plotter3D.set_slice_origin(self, origin)`

Returns the normal of the slice plane

## Returns

np.ndarray  
Normal of the slice plane

#### `Plotter3D.get_slice_origin(self)`

Returns the normal of the slice plane

## Returns

np.ndarray  
Normal of the slice plane

#### `Plotter3D.compute_uv(self, event)`

Computes the u and v axes of the slice plane

## Parameters

event : param.parameterized.Event  
Event containing the normal of the slice plane

#### `Plotter3D.get_uv(self)`

Returns the u and v axes of the slice plane

## Returns

Tuple\[np.ndarray, np.ndarray\]  
u and v axes of the slice plane

#### `Plotter3D.get_mouse_location(self) -> Tuple[float, float, float]`

Returns the current mouse location (returns the panel exit location if out)

## Returns

Tuple\[float, float, float\]  
Mouse location

#### `Plotter3D.get_mouse_info(self) -> str`

Returns a human-readable string describing the hovered cell (coordinates, cell id, value).

#### `Plotter3D.set_plane_enabled(self, enabled: bool)`

Enable or disable the plane visualization overlay.

## Parameters

enabled : bool  
Whether to show the plane visualization.

#### `Plotter3D.set_clip_enabled(self, enabled: bool)`

Enable or disable the clip plane visualization.

## Parameters

enabled : bool  
Whether to enable clipping of the rendered geometry.

#### `Plotter3D.set_clip_axis(self, axis: str, sign: int=1)`

Set clip plane normal to a cardinal direction.

## Parameters

axis : {'x', 'y', 'z'}  
Axis for the normal direction.

sign : {1, -1}, optional  
Direction sign. Default is 1 (positive direction).

#### `Plotter3D.set_edges_visible(self, visible: bool)`

Enable or disable feature edges visualization.

## Parameters

visible : bool  
Whether to show feature edges.

#### `Plotter3D.set_info(self, enabled: bool)`

Enable or disable the info panel.

## Parameters

enabled : bool  
Whether to show the info panel.

#### `Plotter3D.n_cells`

Returns the number of cells in the current polydata.

## Returns

int  
Number of cells, or 0 if no data loaded.
