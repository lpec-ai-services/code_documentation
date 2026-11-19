<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/extruded_boss_operation_page.html -->

# Extruded boss

The **Extruded boss** operation allows you to easily add material on a **solid** by extruding a profile along the normal to its plane.

![extruded_boss_example.png](https://docs.salome-platform.org/latest/gui/GEOM/extruded_boss_example.png)

To produce the **extruded boss**:

1. Draw the **profile** of the extrusion. It can be:

   - a [**Sketch**](create_sketcher_page.md)  drawn on a planar face of the initial shape you want to boss.
   - any closed edge or wire of this shape (circle, ellipse ...).
2. In the **Main Menu** select **Operations - > Extruded Boss** or click on

   ![extruded_boss.png](https://docs.salome-platform.org/latest/gui/GEOM/extruded_boss.png)
3. Fill in the dialog box fields:

   ![extruded_boss_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/extruded_boss_dlg.png)

The input arguments are:

- The **initial shape** you want to add material on. It must be a solid or a compound made of a single solid.
- The **profile**. It must be a **closed** edge or wire and it must be **planar**.
- The **height** of extrusion. It is calculated from the **base profile** along the normal to its plane.

And optionally:

- A **draft angle** in degrees. Activated by clicking on

  ![draft.png](https://docs.salome-platform.org/latest/gui/GEOM/draft.png)

The direction can be reversed by pushing the  **Change direction**  button:

![change_direction.png](https://docs.salome-platform.org/latest/gui/GEOM/change_direction.png)

This functionality is available via the textual interface with the command:

**TUI Command:** *geompy.MakeExtrudedBoss(InitShape, Profile, Height, Angle),*
