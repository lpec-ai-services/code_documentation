<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/view_geom_obj_page.html -->

# Viewing geometrical objects

Newly created or imported geometrical objects are added as items in the Object Browser and displayed in the **OCC 3D Viewer**.

See the corresponding topic about the [Operations available in the Object Browser for Geometry module](arranging_study_objects_page.md).

**OCC 3D Viewer** is described in the documentation on **GUI module**.

After the object has appeared in the Viewer, you can select it with left mouse click to change its presentation parameters and access to other useful options by right-clicking on the selected object.

![dialog.png](https://docs.salome-platform.org/latest/gui/GEOM/dialog.png)

- **Rename** - allows to change the name of the geometric object.
- **Delete** - irreversibly deletes the selected object from the viewer and from the Object Browser.
- **Create Group** - allows to create group.
- [Display Mode](display_mode_page.md) - allows to select between Wireframe and Shading presentation.
- [Bring To Front](bring_to_front_page.md) - allows to bring to front of the viewer the selected geometrical object.
- **Clear Top Level State** - allows to remove from the viewer foreground geometrical objects that have been placed there via **Bring To Front** command.
- [Color](color_page.md) - allows to change the filling color in the standard **Select Color** menu.
- [Transparency](transparency_page.md) - allows to change the transparency of geometrical objects.
- [Isos](isolines_page.md) - allows to change the number of isolines displayed within a shape.
- [Deflection](deflection_page.md) - allows to change the deflection coefficient of a shape.
- [Material](material_page.md) - allows to change the material properties of a shape.
- [Point Marker](point_marker_page.md) - allows to change the representation of geometrical vertices.
- [Line Width](line_width_page.md) - allows to change the width of edges and isolines.
- **Auto color** / **Disable auto color** - activates the auto color mode. When the auto color mode is enabled, the groups created on the sub-shapes of the selected geometrical object are automatically coloured by the unique colors. TUI Commands : *go.SetAutoColor(enable)*, *enabled = go.GetAutoColor()*
- **Hide** - allows to hide the selected geometrical object from the viewer. TUI Command : *sg.EraseOnly(ID)*

  ![image18.png](https://docs.salome-platform.org/latest/gui/GEOM/image18.png)
- **Hide all** - hides all objects from the viewer. TUI Command: *sg.EraseAll()*

  ![image26.png](https://docs.salome-platform.org/latest/gui/GEOM/image26.png)
- **Show Only** - displays only the selected geometrical object. TUI Command: *sg.DisplayOnly(ID)*

  ![image33.png](https://docs.salome-platform.org/latest/gui/GEOM/image33.png)
- **Show all dimensions** - shows all of the persistent dimensions created for the selected geometrical object.
- **Hide all dimensions** - hides all of the persistent dimensions created for the selected geometrical object.
- [Show dependency tree](dependency_tree_page.md) - shows the dependency tree with parents and children of the selected object in a new 2D View Window.
- [Reduce study](reduce_study_page.md) - allows reducing the study by removing objects from it.
- **Dump view** - exports an object from the viewer in bmp, png, jpg or jpeg image format.
- **Change background** - allows to redefine the background color. By default it is black.

Some of these functionalities are available through right-clicking on the viewer background:

![image22.png](https://docs.salome-platform.org/latest/gui/GEOM/image22.png)

- **Select Only** provides a filter for exclusive selection of objects of a certain type.
