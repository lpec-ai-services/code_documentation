<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/fillet2d_operation_page.html -->

# Fillet 2D

This operation creates fillets on the corners of a **2D Planar Face** or a **Shell, made of 2D Planar Faces**.

![fillet2d_2.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet2d_2.png)

To produce a **Fillet 2D** in the **Main Menu** select **Operations - > Fillet 2D**

Define the **Planar Face** or the **Shell** to create a fillet on, select the necessary vertexes on this shape in the OCC Viewer and define the **Radius** of the Fillet.

**Note:** This operation works only for **Planar 2D Faces** and shells, made of such faces. For shells, only corner vertexes are available for fillet building, i.e. the vertexes that belong to only one face of this shell.

**TUI Command:** *geompy.MakeFillet2D(Shape, R, ListVertexes)*   
**Arguments:** Name + 1 shape + one or several vertexes + 1 value (Fillet radius).   
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

**Examples:**

![fillet2d_1.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet2d_1.png)

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_fillet2d).
