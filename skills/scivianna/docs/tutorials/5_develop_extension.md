<!-- source: 5_develop_extension.ipynb -->

# Tutorial 5: Developing an Extension (Dev)

This tutorial shows how to create custom extensions for scivianna panels, adding new functionality and UI elements.

## Introduction

**Extensions** in scivianna are modular components that add new functionality to panels. They can:

- Add custom UI widgets (buttons, sliders, text inputs)
- Receive callbacks from the panel (mouse events, data changes, viewport updates)
- Modify panel rendering behavior
- Access and manipulate slave data

## Extension Architecture

Extensions are built on a single base class:

- **`Extension`**: Base class providing event callbacks, GUI creation, and serialization hooks

## Extension Lifecycle

1.  **Initialization**: Extension is created with references to slave, plotter, and panel
2.  **GUI Creation**: `make_gui()` returns the widget to display in the extension tab
3.  **Event Handling**: Extension callback methods are called when events occur:
    - File loading (`on_file_load`)
    - Field changes (`on_field_change`)
    - Data updates (`on_updated_data`)
    - Viewport changes (`on_range_change`, `on_frame_change`)
    - Mouse events (`on_mouse_move`, `on_mouse_clic`)
4.  **Options Providing**: `provide_options()` sends options to the slave
5.  **Serialization**: `to_json()`/`from_json()` for saving/restoring state

## Complete Example: DummyTestExtension

Here's a complete example of a simple extension that displays a title and receives mouse events. This is the same extension used in the test suite.

### How It Works

1.  **`__init__`**: Calls parent constructor with name, icon, and references; initializes event history lists
2.  **`make_gui`**: Returns a Panel Material UI Column with a title and description text
3.  **`on_mouse_move`**: Called when mouse moves over the plot - logs the event with coordinates and cell ID
4.  **`on_mouse_clic`**: Called when user clicks on the plot - logs the click event

``` python
from typing import Tuple, Union, List
import panel as pn
import panel_material_ui as pmui

from scivianna.extension.extension import Extension
from scivianna.plotter_2d.generic_plotter import Plotter2D
from scivianna.panel.panel_2d import Panel2D
from scivianna.slave import ComputeSlave
from scivianna.data.data2d import Data2D

# SVG icon for the extension (optional)
ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" fill="#4CAF50"/>
</svg>
"""

class DummyTestExtension(Extension):
    """A simple extension that displays a title and tracks mouse events.
    
    This is a minimal example showing how to:
    - Create an extension with a custom GUI
    - Receive mouse move and click callbacks
    - Track event history for debugging or display
    """
    
    def __init__(
        self,
        slave: "ComputeSlave",
        plotter: "Plotter2D",
        panel: "Panel2D"
    ):
        """Initialize the extension.
        
        Parameters
        ----------
        slave : ComputeSlave
            Slave computing the displayed data
        plotter : Plotter2D
            Figure plotter
        panel : Panel2D
            Panel to which the extension is attached
        """
        # Call parent constructor with required parameters
        super().__init__(
            title="TestExtension",
            icon=ICON_SVG,
            slave=slave,
            plotter=plotter,
            panel=panel,
        )

        self.description = """
        This is a simple test extension that displays a title
        and tracks mouse events.
        """

        self.iconsize = "1.5em"

        # Event history for tracking
        self._mouse_move_history: List[Tuple] = []
        self._mouse_click_history: List[Tuple] = []

    def make_gui(self) -> pn.viewable.Viewable:
        """Create the GUI widget for this extension.
        
        Returns
        -------
        pn.viewable.Viewable
            Panel component to display in the extension tab
        """
        return pmui.Column(
            pmui.Typography("Test Extension"),
            pmui.Text("Move or click on the plot to see events."),
            margin=10
        )

    def on_mouse_move(
        self,
        screen_location: Tuple[float, float],
        space_location: Tuple[float, float, float],
        cell_id: Union[str, int],
    ):
        """Called when the mouse moves over the plot.
        
        This callback is triggered continuously as the user moves their cursor
        over the visualization area. Use it for tooltips, highlighting,
        or real-time coordinate display.
        
        Parameters
        ----------
        screen_location : Tuple[float, float]
            Mouse position in screen coordinates (pixels from top-left)
        space_location : Tuple[float, float, float]
            Mouse position in 3D world coordinates (x, y, z)
        cell_id : Union[str, int]
            ID of the cell currently under the mouse cursor
        """
        event = (screen_location, space_location, cell_id)
        self._mouse_move_history.append(event)
        print(f"Mouse moved: screen={screen_location}, space={space_location}, cell={cell_id}")

    def on_mouse_clic(
        self,
        screen_location: Tuple[float, float],
        space_location: Tuple[float, float, float],
        cell_id: Union[str, int],
    ):
        """Called when the mouse clicks on the plot.
        
        This callback is triggered when the user clicks (taps) on the
        visualization area. Use it for selection, annotations, or
        triggering actions on specific cells.
        
        Parameters
        ----------
        screen_location : Tuple[float, float]
            Click position in screen coordinates (pixels from top-left)
        space_location : Tuple[float, float, float]
            Click position in 3D world coordinates (x, y, z)
        cell_id : Union[str, int]
            ID of the cell that was clicked
        """
        event = (screen_location, space_location, cell_id)
        self._mouse_click_history.append(event)
        print(f"Mouse clicked: screen={screen_location}, space={space_location}, cell={cell_id}")

# Test the extension
if __name__ == "__main__":
    from scivianna.slave import ComputeSlave
    from scivianna.panel.panel_2d import Panel2D
    
    # First, you need an interface (see Tutorial 4)
    from test_interface import DummyTestInterface
    
    # Create slave and panel
    slave = ComputeSlave(DummyTestInterface)
    panel = Panel2D(slave, name="My View")
    
    # Extensions are automatically created from the interface's extensions list
    print(f"Extensions: {[e.title for e in panel.extensions]}")
```

## Linking an Extension to an Interface

To automatically include your extension when using a specific interface, add it to the `extensions` class attribute:

``` python
from scivianna.interface.generic_interface import Geometry2DPolygon

class MyInterfaceWithExtension(Geometry2DPolygon):
    """An interface that includes a custom extension."""
    
    # List your extensions here - they will be automatically instantiated
    # when a Panel2D is created with this interface
    extensions = [DummyTestExtension]
    
    # ... implement other required methods ...

# When you create a panel with this interface:
# from scivianna.slave import ComputeSlave
# from scivianna.panel.panel_2d import Panel2D
#
# slave = ComputeSlave(MyInterfaceWithExtension)
# panel = Panel2D(slave)
# 
# Your extension will automatically appear in the panel's extension tab.
```

## API Reference: Methods Table

| Method                                                    | Description                                                            |
|-----------------------------------------------------------|------------------------------------------------------------------------|
| `__init__(title, icon, slave, plotter, panel)`            | Initialize extension with title, icon, and panel references. Required. |
| `make_gui()`                                              | Return Panel widget for the extension tab. Default: None.              |
| `on_file_load(file_path, file_label)`                     | Called when a file is loaded. Default: no-op.                          |
| `on_field_change(field_name)`                             | Called when displayed field changes. Default: no-op.                   |
| `on_updated_data(data)`                                   | Called when displayed data updates. Can modify data. Default: no-op.   |
| `on_range_change(u_bounds, v_bounds, w_value)`            | Called when viewport bounds change (zoom/pan). Default: no-op.         |
| `on_frame_change(u_vector, v_vector)`                     | Called when viewport orientation changes (rotation). Default: no-op.   |
| `on_mouse_move(screen_location, space_location, cell_id)` | Called on mouse hover over plot. Default: no-op.                       |
| `on_mouse_clic(screen_location, space_location, cell_id)` | Called on mouse click on plot. Default: no-op.                         |
| `provide_options()`                                       | Return options dict to send to slave. Default: {}.                     |
| `to_json()`                                               | Return state dict for serialization. Default: {}.                      |
| `from_json(extension, info_dict)`                         | Restore extension from state dict. Default: unchanged.                 |

### Mouse Event Parameters

| Parameter         | Type                         | Description                                                 |
|-------------------|------------------------------|-------------------------------------------------------------|
| `screen_location` | `Tuple[float, float]`        | Mouse position in screen coordinates (pixels from top-left) |
| `space_location`  | `Tuple[float, float, float]` | Mouse position in 3D world coordinates (x, y, z)            |
| `cell_id`         | `str` or `int`               | ID of the cell currently under the mouse / clicked          |

### Class Attributes

| Attribute     | Type                  | Description                                 |
|---------------|-----------------------|---------------------------------------------|
| `title`       | str                   | Extension title displayed at top of sidebar |
| `description` | str                   | Short description of the extension          |
| `icon`        | str                   | SVG icon string or file path for tabs       |
| `slave`       | ComputeSlave          | Reference to computing slave                |
| `plotter`     | Plotter2D / Plotter3D | Reference to figure plotter                 |
| `panel`       | VisualizationPanel    | Reference to parent panel                   |
| `iconsize`    | str                   | Icon size CSS (default: "6em")              |

## Summary

To create a custom extension:

1.  **Inherit from `Extension`**

2.  **Implement `__init__`**:

    - Call `super().__init__(title, icon, slave, plotter, panel)`
    - Set `description` and `iconsize`

3.  **Implement `make_gui()`**:

    - Return a Panel component (e.g., `pmui.Column`, `pn.Row`)
    - Add widgets like sliders, buttons, text inputs

4.  **(Optional) Implement event callbacks**:

    - `on_file_load(file_path, file_key)` - React to file loading
    - `on_field_change(field_name)` - React to field changes
    - `on_updated_data(data)` - Modify data before plotting
    - `on_range_change(u_bounds, v_bounds, w_value)` - React to zoom/pan
    - `on_frame_change(u_vector, v_vector)` - React to rotation
    - `on_mouse_move(screen_location, space_location, cell_id)` - Hover effects
    - `on_mouse_clic(screen_location, space_location, cell_id)` - Click actions

5.  **(Optional) Implement utility methods**:

    - `provide_options()` - Send options to slave
    - `to_json()` / `from_json()` - Save/restore state

6.  **Link to an interface** by adding it to the `extensions` class attribute:

    ``` python
    class MyInterface(Geometry2DPolygon):
        extensions = [MyCustomExtension]
    ```
