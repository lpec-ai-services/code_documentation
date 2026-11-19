<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/glue_edges_operation_page.html -->

# Glue Edges

To **Glue Edges** in the **Main Menu** select **Repair - > Glue Edges**.

This operation glues edges that are coincident with respect to the given tolerance value.

**Arguments:** Name + Shapes + Tolerance value.   
**Advanced option:** [Set presentation parameters and sub-shapes from arguments](restore_presentation_parameters_page.md).   
The **Result** will be a **GEOM_Object**.

![glue4.png](https://docs.salome-platform.org/latest/gui/GEOM/glue4.png)

**TUI Command:**

*geompy.MakeGlueEdges( theShapes, theTolerance )*,   
where *theShapes* is a list or compound of shapes to be glued, and *theTolerance* is a maximum distance between two edges, which can be considered as coincident.

It is also possible to manually select the edges that will be glued - select the shape, specify the tolerance and press **Detect** button.

![glue5.png](https://docs.salome-platform.org/latest/gui/GEOM/glue5.png)

**Geometry** module detects the edges where gluing can be performed and displays a notification.

![glue7.png](https://docs.salome-platform.org/latest/gui/GEOM/glue7.png)

The edges that can be glued are colored in red. It is possible to select the edges for gluing in the 3D viewer. The selected edges will be marked in white.

**TUI Command:**

*geompy.GetGlueEdges( theShapes, theTolerance )*,   
where *theShape* is either a list or compound of shapes to be glued, *theTolerance* is a maximum distance between two edges, which can be considered as coincident. The **Result** will be a list of **GEOM_Objects** (edges), containing one sub-shape per each detected set of coincident sub-shapes. For example, if there are two coincident edges in the selected shapes, the result list contains one of the two coincident edges.

*geompy.MakeGlueEdgesByList( theShapes, theTolerance, theEdges )*,   
where *theShape* is a list or compound of shapes to be glued, *theTolerance* is a maximum distance between two edges, which can be considered as coincident, *theEdges* is a list of edges to be glued.

**Example:**

![glue8.png](https://docs.salome-platform.org/latest/gui/GEOM/glue8.png)

*Two boxes with an edge that can be glued*

Our **TUI Scripts** provide you with useful examples of the use of **Repairing Operations** [Glue Edges](tui_repairing_operations_page.md#tui_glue_edges).
