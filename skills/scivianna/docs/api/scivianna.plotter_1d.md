<!-- source: api/scivianna.plotter_1d.rst -->

# scivianna.plotter_1d package

# Scivianna 1D Plotter Module

The `plotter_1d` module provides plotting backends for rendering one-dimensional data such as line charts, time series, and XY plots in Scivianna.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `generic_plotter.py` | Base class `Plotter1D` defining the 1D plotting API |
| `bokeh_1d_plotter.py` | Bokeh-based implementation `BokehPlotter1D` for interactive 1D plots |

## Plotter1D (Base Class)

Defines the interface for all 1D plotters in `generic_plotter.py`:

### Key Methods

| Method | Purpose |
|--------|---------|
| `make_panel()` | Create and return the Panel display object |
| `plot(name, serie)` | Add a new plot with given name and pandas Series data |
| `update_plot(name, serie)` | Update existing plot or create if not exists |
| `set_visible(names)` | Set which plots are visible (list of names) |
| `set_x_scale(scale)` | Set X axis scale to "log" or "lin" |
| `set_y_scale(scale)` | Set Y axis scale to "log" or "lin" |
| `get_mouse_location()` | Returns current mouse position in 3D world coordinates as `(x, y, z)` |

## BokehPlotter1D

Implementation using Bokeh for interactive 1D visualization in `bokeh_1d_plotter.py`:

### Features
- Interactive hover tools
- Multiple line overlays
- Zoom and pan controls
- Legend management
- Responsive sizing
- Color palette based on plot visibility order

### Supported Plot Types
- Line charts (single or multi-line)
- Time series with time navigation
- Variable comparisons

## Customization

Bokeh plot properties can be customized via the underlying Bokeh figure:

- Line colors and styles (automatically set based on visibility order)
- Axis ranges
- Grid visibility
- Toolbar configuration

## Additional Methods

| Method | Purpose |
|--------|---------|
| `get_x_bounds()` | Returns (min, max) of displayed data on X axis |
| `get_y_bounds()` | Returns (min, max) of displayed data on Y axis |
| `_disable_interactions(val)` | Enable/disable plot interactions | Submodules ----------

## scivianna.plotter_1d.bokeh_1d_plotter module

Bokeh implementation of the 1D line plotter.

### `class scivianna.plotter_1d.bokeh_1d_plotter.BokehPlotter1D()  — bases: Plotter1D`

1D Bokeh plotter.

#### `BokehPlotter1D.plot(self, name: str, serie: pd.Series)`

Adds a new plot to the figure from a set of polygons

## Parameters

name : str  
Plot name

serie : pd.Series  
Sata to plot

#### `BokehPlotter1D.update_plot(self, name: str, serie: pd.Series)`

Updates plot to the figure

## Parameters

name : str  
Plot name

serie : pd.Series  
Sata to plot

#### `BokehPlotter1D.set_visible(self, names: List[str])`

Updates the visible plots in the figure

## Parameters

names : List\[str\]  
List of displayed plots

#### `BokehPlotter1D.make_panel(self)`

Returns the panel to display in the layout

## Returns

pn.viewable.Viewable  
Panel to display

#### `BokehPlotter1D.get_y_bounds(self) -> Tuple[float, float]`

Returns the bounds of the displayed data along the Y axis

## Returns

Tuple\[float, float\]  
Displayed data Y bounds

#### `BokehPlotter1D.get_x_bounds(self) -> Tuple[float, float]`

Returns the bounds of the displayed data along the X axis

## Returns

Tuple\[float, float\]  
Displayed data X bounds

#### `BokehPlotter1D.set_x_scale(self, scale: str)`

Sets the X axis scale to either log or lin

## Parameters

scale : str  
Scale to set

#### `BokehPlotter1D.set_y_scale(self, scale: str)`

Sets the Y axis scale to either log or lin

## Parameters

scale : str  
Scale to set

#### `BokehPlotter1D.get_mouse_location(self) -> Tuple[float, float, float]`

Returns the current mouse location (returns the panel exit location if out)

## Returns

Tuple\[float, float, float\]  
Mouse location scivianna.plotter_1d.generic_plotter module ---------------------------------------------

Abstract interface for 1D line plotters.

### `class scivianna.plotter_1d.generic_plotter.Plotter1D()`

Unfinished 1D plotter to get the coupling working

#### `Plotter1D.plot(self, name: str, serie: pd.Series)`

Adds a new plot to the figure from a set of polygons

## Parameters

name : str  
Plot name

serie : pd.Series  
Sata to plot

#### `Plotter1D.update_plot(self, name: str, serie: pd.Series)`

Updates plot to the figure

## Parameters

name : str  
Plot name

serie : pd.Series  
Sata to plot

#### `Plotter1D.set_visible(self, names: List[str])`

Updates the visible plots in the figure

## Parameters

names : List\[str\]  
List of displayed plots

#### `Plotter1D.make_panel(self)`

Return the Panel viewable displaying the 1D figure.

#### `Plotter1D.set_x_scale(self, scale: str)`

Sets the X axis scale to either log or lin

## Parameters

scale : str  
Scale to set

#### `Plotter1D.set_y_scale(self, scale: str)`

Sets the Y axis scale to either log or lin

## Parameters

scale : str  
Scale to set

#### `Plotter1D.get_mouse_location(self) -> Tuple[float, float, float]`

Returns the current mouse location (returns the panel exit location if out)

## Returns

Tuple\[float, float, float\]  
Mouse location Module contents ---------------

1D line plot backends for scivianna (abstract interface and Bokeh implementation).
