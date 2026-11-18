<!-- source: api/scivianna.plotter_graph.rst -->

# scivianna.plotter_graph package

# Scivianna Graph Plotter Module

The `plotter_graph` module provides the rendering backend for graph panels: it
displays a set of 2D plots (nodes) connected by directed links, typically used
to visualize the topology of coupled simulations.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `generic_plotter.py` | Abstract base class `PlotterGraph` defining the graph rendering interface |
| `reactflow_plotter.py` | ReactFlow-based plotter (via the `scivianna-graph` module) used by the graph panel: one Bokeh figure per node, hover-only, fitted to its content; supports 4-side plugs, node rotation (with an optional fixed pivot) and drag-select | Submodules ----------

## scivianna.plotter_graph.generic_plotter module

Abstract interface for graph plotters (nodes + directed links).

### `class scivianna.plotter_graph.generic_plotter.PlotterGraph`

Abstract base class for plotting a `DataGraph`.

A graph plotter renders a set of 2D plots (nodes) connected by directed links, typically used to visualize the topology of coupled simulations. Concrete implementations provide the rendering backend and implement the methods below; they are consumed by `PanelGraph` in the same way that `Plotter2D`/ `Plotter3D` backends are consumed by their panels.

#### `PlotterGraph.plot(self, data: DataGraph)`

Adds a new graph to the figure from a set of nodes and links

## Parameters

data : DataGraph  
DataGraph object containing the node geometries and links to plot

#### `PlotterGraph.update_plot(self, data: DataGraph)`

Updates the displayed graph in place

## Parameters

data : DataGraph  
DataGraph object with updated node geometries and links

#### `PlotterGraph.make_panel(self)`

Returns the viewable displayed in the graph panel

## Returns

pn.viewable.Viewable  
Graph plotter widget

#### `PlotterGraph.update_colorbar(self, display: bool, value_range: Tuple[float, float])`

Displays or hide the color bar, if display, updates its range

## Parameters

display : bool  
Display or hides the color bar

value_range : Tuple\[float, float\]  
New colormap range

#### `PlotterGraph.set_color_map(self, color_map_name: str)`

Sets the colorbar color map name

## Parameters

color_map_name : str  
Color map name

#### `PlotterGraph.provide_on_mouse_move_callback(self, callback: Callable)`

Stores a function to call everytime the user moves the mouse on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `PlotterGraph.provide_on_clic_callback(self, callback: Callable)`

Stores a function to call everytime the user clics on the plot. Functions arguments are location, cell_id.

## Parameters

callback : Callable  
Function to call.

#### `PlotterGraph.provide_on_node_selection_change_callback(self, callback: Callable)`

Stores a function to call everytime the selection of nodes changes. Functions arguments are the ids of the selected nodes (empty list when nothing is selected).

## Parameters

callback : Callable  
Function to call.

#### `PlotterGraph.provide_on_nodes_moved_callback(self, callback: Callable)`

Stores a function to call everytime one or several nodes are moved on the canvas. Functions arguments are a list of {"id", "x", "y"} dicts, one per moved node.

## Parameters

callback : Callable  
Function to call.

#### `PlotterGraph.get_mouse_info(self) -> str`

Returns a human-readable string describing the hovered cell in the graph (node key, coordinates, cell id, value).

## Returns

str  
Information on mouse hovered location Module contents ---------------

Graph plot backends for scivianna: abstract interface and the ReactFlow renderer.
