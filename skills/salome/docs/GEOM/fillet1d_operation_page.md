<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/fillet1d_operation_page.html -->

# Fillet 1D

This operation creates fillets on the corners of a **Wire with Planar Edges**. Note that each couple of edges connected with a vertex, where 1D fillet should be constructed, have to lie in the same plane.

![fillet1d_2.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet1d_2.png)

To produce a **Fillet** 1D in the **Main Menu** select **Operations - > Fillet 1D**

Define the **Wire with planar Edges** to create a fillet on, select the necessary vertexes on this wire in the OCC Viewer and define the **Radius** of the Fillet.

**Note:** This Operation Works for the Wires with **Planar Edges** only.

**Note:** Use option **Fuse collinear edges to allow bigger radius** in order to ignore possible secant points, i.e. the joints of collinear edges, thus processing such edges as one.

**TUI Command:** *geompy.MakeFillet1D(Shape, R, ListVertexes)*   
**Arguments:** Name + 1 shape + empty list or several vertexes + 1 value (Fillet radius).   
**Advanced options:** [Preview](restore_presentation_parameters_page.md#preview_anchor)

**Examples:**

![fillet1d_1.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet1d_1.png)

Filleted Wire

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_fillet1d).
