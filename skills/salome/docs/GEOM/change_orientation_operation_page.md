<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/change_orientation_operation_page.html -->

# Change Orientation

To **Change Orientation** in the **Main Menu** select **Repair - > Change Orientation**.   
This operation reverses the normals of selected faces or the normal of faces composing the selected opened shell. For edge or wire the operation reverses its direction.

**TUI Command:** *geompy.ChangeOrientation(shape)*   
**Arguments:** Name + one or several objects (edge(s), wire(s), face(s), opened shell(s)).   
Uncheck **Create a copy** checkbox if you don't wish to leave the initial object in the project (**Result name** field will be locked).

![changeorientation.png](https://docs.salome-platform.org/latest/gui/GEOM/changeorientation.png)

**Example:**

![image38.png](https://docs.salome-platform.org/latest/gui/GEOM/image38.png)

*Inward orientation*

![image40.png](https://docs.salome-platform.org/latest/gui/GEOM/image40.png)

*Outward orientation*
