<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/glue_faces_operation_page.html -->

# Glue Faces

To **Glue Faces** in the **Main Menu** select **Repair - > Glue Faces**.

This operation glues faces that are coincident with respect to the given tolerance value.

**Arguments:** Name + Shapes + Tolerance value.   
**Advanced option:** [Set presentation parameters and sub-shapes from arguments](restore_presentation_parameters_page.md).   
The **Result** will be a **GEOM_Object**.

![glue1.png](https://docs.salome-platform.org/latest/gui/GEOM/glue1.png)

**TUI Commands:**

*geompy.MakeGlueFaces( theShapes, theTolerance, doKeepNonSolids )*,   
where *theShapes* is either a list or compound of shapes to be glued, *theTolerance* is a maximum distance between two faces, which can be considered as coincident. The *doKeepNonSolids* flag allows to throw away non-solids from the result, if false. The **Result** will be a new **GEOM_Object**.

It is also possible to manually select the faces that will be glued - select the shape, specify the tolerance and press **Detect** button.

![glue2.png](https://docs.salome-platform.org/latest/gui/GEOM/glue2.png)

**Geometry** module detects the faces where gluing can be performed and displays a notification.

![glue3.png](https://docs.salome-platform.org/latest/gui/GEOM/glue3.png)

The faces that can be glued are colored in red. It is possible to select the faces for gluing in the 3D viewer. The selected faces will be marked in white.

When the faces are glued their edges are glued as well. By default, other edges are not glued. To force gluing of all edges, check **Glue all coincident edges** check-box.

**TUI Commands:**

*geompy.GetGlueFaces( theShapes, theTolerance )*,   
where *theShapes* is a list or compound of shapes to be glued, *theTolerance* is a maximum distance between two faces, which can be considered as coincident. The **Result** will be a list of **GEOM_Objects** (faces), containing one sub-shape per each detected set of coincident sub-shapes. For example if there are two coincident faces in selected shapes, the result list contains one of the two coincident faces.

*geompy.MakeGlueFacesByList( theShapes, theTolerance, theFaces, doKeepNonSolids, doGlueAllEdges )*,   
where *theShapes* is either a list or compound of shapes to be glued, *theTolerance* is a maximum distance between two faces, which can be considered as coincident, *theFaces* is a list of sub-shapes to be glued. The *doKeepNonSolids* flag allows to throw away non-solids from the result, if false. The *doGlueAllEdges* allows to glue all edges, not only owned by glued faces. The **Result** will be a new **GEOM_Object**.

**Example:**

![glue_faces1.png](https://docs.salome-platform.org/latest/gui/GEOM/glue_faces1.png)

*Object that needs gluing*

![glue_faces2.png](https://docs.salome-platform.org/latest/gui/GEOM/glue_faces2.png)

*Glued object*

![glue_faces3.png](https://docs.salome-platform.org/latest/gui/GEOM/glue_faces3.png)

*Manual selection of faces for gluing*

Our **TUI Scripts** provide you with useful examples of the use of **Repairing Operations** [Glue Faces](tui_repairing_operations_page.md#tui_glue_faces).
