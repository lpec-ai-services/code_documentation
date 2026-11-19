<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_dividedcylinder_page.html -->

# DividedCylinder

The **Divided cylinder** object is a cylinder divided into **blocks** for easy hexahedral meshing. Two division patterns are available :

- A square pattern, which is frequently used;
- A hexagonal pattern, which ensures a better mesh quality and especially less acute or obtuse angles.

![dividedcylinder.png](https://docs.salome-platform.org/latest/gui/GEOM/dividedcylinder.png)

To create a **DividedCylinder** in the **Main Menu** select **New Entity - > Advanced - > DividedCylinder**

Specify the parameters of the DividedCylinder object creation in the opened dialog box and press "Apply" or "Apply & Close" button. Result of each operation will be a GEOM_Object.

**TUI Command:** *geompy.MakeDividedCylinder(R, H, Pattern)*

**Arguments:**

- **R** - Radius of the cylinder
- **H** - Height of the cylinder
- **Pattern** - Division pattern

![dividedcylinder_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/dividedcylinder_dlg.png)

Our **TUI Scripts** provide you with useful examples of creation of [Advanced objects](tui_advanced_geom_objs_page.md#tui_creation_dividedcylinder).
