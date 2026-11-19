<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/union_faces_operation_page.html -->

# Union Faces

This operation unites on a given shape all faces sharing the same surface.

To **Union Faces** in the **Main Menu** select **Repair - > Union Faces**.

![union_faces.png](https://docs.salome-platform.org/latest/gui/GEOM/union_faces.png)

In this dialog:

- Click on the "Arrow" button and select in the Object Browser or in the viewer one or more **Shapes** (compounds or single solids).
- If necessary, activate [Advanced Transformation Options](restore_presentation_parameters_page.md).
- Click **Apply** or **Apply and Close** button.

This operation can be also launched using a **TUI Command:** *geompy.UnionFaces(theShape)*, where *theShape* is a compound or a single solid.

**Example:**

![union_faces1.png](https://docs.salome-platform.org/latest/gui/GEOM/union_faces1.png)

*Shape with not united faces*

![union_faces2.png](https://docs.salome-platform.org/latest/gui/GEOM/union_faces2.png)

*Improved shape*

Our **TUI Scripts** provide you with useful examples of the [Union Faces](tui_test_others_page.md#swig_UnionFaces) functionality usage.
