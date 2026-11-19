<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/extruded_cut_operation_page.html -->

# Extruded cut

The **Extruded cut** operation allows you to easily remove material from a **solid** by extruding a profile along the normal to its plane.

![extruded_cut_example.png](https://docs.salome-platform.org/latest/gui/GEOM/extruded_cut_example.png)

To produce the **extruded cut**:

1. Draw the **profile** of the extrusion. It can be:

   - a [**Sketch**](create_sketcher_page.md)  drawn on a planar face of the object you want to cut.
   - any closed edge or wire of the desired shape (circle, ellipse ...).
2. In the **Main Menu** select **Operations - > Extruded Cut** or click on

   ![extruded_cut.png](https://docs.salome-platform.org/latest/gui/GEOM/extruded_cut.png)
3. Fill in the dialog box fields:

   ![extruded_cut_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/extruded_cut_dlg.png)

The input arguments are:

- The **initial shape** you want to cut. It must be a solid or a compound made of a single solid.
- The **profile**. It must be a **closed** edge or wire and it must be **planar**.
- The **height** of extrusion. It's calculated from the **base profile** along the normal to its plane.

And optionally:

- A **draft angle** in degrees. Activated by clicking on

  ![draft.png](https://docs.salome-platform.org/latest/gui/GEOM/draft.png)

The direction can be reversed by pushing the  **Change direction**  button:

![change_direction.png](https://docs.salome-platform.org/latest/gui/GEOM/change_direction.png)

This functionality is available via the textual interface with the command:

**TUI Command:** *geompy.MakeExtrudedCut(InitShape, Profile, Height,Angle),*
