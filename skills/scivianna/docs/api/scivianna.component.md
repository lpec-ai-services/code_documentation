<!-- source: api/scivianna.component.rst -->

# scivianna.component package

# Scivianna Component Module

The `component` module provides custom UI components for building interactive Scivianna dashboards using Panel.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `gridstack_component.py` | GridStack layout component for resizable, draggable panels |
| `overlay_component.py` | Overlay component for layering UI elements over plots with keyboard event support |
| `server_file_browser.py` | File browser component for server-side file navigation |
| `splitjs_component.py` | Split-pane component using Split.js for resizable divisions |
| `dist/` | Compiled JavaScript bundles for custom components |

## Components Overview

### GridStack Component
Implements a grid-based layout system where panels can be:
- Resized dynamically
- Dragged to new positions
- Added or removed interactively

### Overlay Component
Provides a container for overlaying buttons, titles, and controls on top of visualization plots. Features:
- **Hover detection**: Buttons only visible when mouse is over the figure area
- **Keyboard events**: Captures keyboard input when mouse is inside the figure area (via the `key` parameter)
- **Configurable elements**: Title, buttons, and custom HTML content can be overlaid

### SplitJS Component
Creates split-pane layouts with draggable dividers for flexible horizontal or vertical divisions.

### Server File Browser
Enables browsing and loading files from the server filesystem directly within the Panel application. Submodules ----------

## scivianna.component.gridstack_component module

Custom GridStack panel layout component for scivianna.

### `class scivianna.component.gridstack_component.CustomGridStack  — bases: GridStack`

Custom version of the panel.layout.gridstack.GridStack to allow clearing the objects properly.

#### `CustomGridStack.clear_objects(self)`

Clears the objects list and the object dictionnary.

#### `CustomGridStack.print_stored_items(self)`

Prints the information of the objects stored

#### `CustomGridStack.print_state(self)`

Prints the current gridstack state (viewable id to coordinates in the grid).

#### `CustomGridStack.add_object(self, obj: pn.viewable.Viewable, x_range: Tuple[int, int], y_range: Tuple[int, int])`

Adds an object to the gridstack objects dict

## Parameters

obj : pn.viewable.Viewable  
Panel added

x_range : Tuple\[int, int\]  
Horizontal range used to update the number of rows and columns

y_range : Tuple\[int, int\]  
Vertical range used to update the number of rows and columns scivianna.component.overlay_component module ---------------------------------------------

Panel component overlaying a button and a title on top of a figure.

### `class scivianna.component.overlay_component.Overlay  — bases: ReactiveHTML`

This component allow displaying buttons over a figure only when the mouse is in the area.

It also tracks keyboard events while the mouse is inside the figure and stores the last pressed key in the `key` parameter.

#### `Overlay.hide_buttons(self, *args, **kwargs)`

Hide all element on top of the figure

#### `Overlay.show_buttons(self, *args, **kwargs)`

Show all element on top of the figure if the mouse is in the frame scivianna.component.server_file_browser module ------------------------------------------------

Server-side file browser component based on a Select widget.

### `class scivianna.component.server_file_browser.ServerFileBrowser(folder_path: Union[str, Path]=None, width: int=300, *args, **kwargs)  — bases: Viewer`

The ServerFileBrowser is a file explorer based on a Select widget that lets browse on the server side.

#### `ServerFileBrowser.on_value_change(self, event: param.Event)`

Event triggered by a dropdown open change, it updates the content of the select if a value was selected:  
- If a folder is selected, the select updates its content to the folder content, and the folder path is saved;
- If a file is selected, its path is saved in selected_file.

## Parameters

event : param.Event  
Change event scivianna.component.splitjs_component module ---------------------------------------------

SplitJS-based split layout components for scivianna. Module contents ---------------

Custom Panel components used to build the scivianna GUI.
