<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/fillet_operation_page.html -->

# Fillet 3D

To produce a **Fillet** in the **Main Menu** select **Operations - > Fillet**

This operation creates fillets on the edges of a shape.   
The **Result** will be a **GEOM_Object**.

To create fillets on all edges of the given shape, you need to select the **Main Object** to create a fillet on and to define the **Radius** of the Fillet.   
**TUI Command:** *geompy.MakeFilletAll(Shape, R)*   
**Arguments:** Name + 1 shape + 1 value (fillet radius).   
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![fillet1.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet1.png)

To create fillets on the specified edges or faces of the given shape, you need to define the **Main Object** to create a fillet on, select the necessary edges or faces in the OCC Viewer and define the **Radius** of the Fillet.   
**TUI Command:** *geompy.MakeFillet(Shape, R, ShapeType, ListShapes)*   
**Arguments:** Name + 1 shape + one or several edges (or faces)

- 1 value (Fillet radius).   
  **Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

Alternatively, there is a possibility to create a fillet with a variable radius. For this, toggle the lower radio button and define **R1** (the radius at the start of the selected edge(s)) and **R2** (the radius at the end of the selected edge(s))

![fillet2.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet2.png)

![fillet3.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet3.png)

**Examples:**

![fillet_all.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet_all.png)

*Fillet on all*

![fillet_edge.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet_edge.png)

*Fillet on an edge*

![fillet_prism.png](https://docs.salome-platform.org/latest/gui/GEOM/fillet_prism.png)

*Fillet on a Face*

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_fillet).
