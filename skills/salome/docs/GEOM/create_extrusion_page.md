<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_extrusion_page.html -->

# Extrusion

**Extrusion** is propagation of the selected base shape in a certain direction and by a certain distance.   
The **Result** of the operation will be a GEOM_Object (edge, face, shell solid or compsolid).

**Examples:**

![prisms_basessn.png](https://docs.salome-platform.org/latest/gui/GEOM/prisms_basessn.png)

Base Shape

![prismssn.png](https://docs.salome-platform.org/latest/gui/GEOM/prismssn.png)

Resulting Prisms

To generate an **Extrusion** on an object in the **Main Menu** select **New Entity - > Generation - > Extrusion**

![extrusion1.png](https://docs.salome-platform.org/latest/gui/GEOM/extrusion1.png)

The following parameters and options can be defined in this dialog

- **Result name** of the created resulting shape.
- **Base** - the extruded object. It is possible to select in GUI several Base Shapes to make several extrusions (using Shift button).
- Direction and distance can be defined in three different ways selectable with the radio buttons on top of the dialog box :

  - By the **Vector** and the **Height** of extrusion. **TUI Command:** *geompy.MakePrismVecH(Base, Vector, Height, theScaleFactor = -1.0)*
  - By the **Start** and **End Point** of the **Vector** (in this way you don't need to create it in advance). **TUI Command:** *geompy.MakePrism(Base, Point1, Point2, theScaleFactor = -1.0)*

    ![extrusion2.png](https://docs.salome-platform.org/latest/gui/GEOM/extrusion2.png)
  - By **DX**, **DY**, and **DZ** coordinates of the Vector. **TUI Command:** *geompy.MakePrismDXDYDZ(Base, dx, dy, dz, theScaleFactor = -1.0)*

    ![extrusion3.png](https://docs.salome-platform.org/latest/gui/GEOM/extrusion3.png)
- **Both Directions**  checkbox allows extruding the base shape both forward and backward. With this option scaling is not possible.
- **Reverse** checkbox reverts the direction of the scaling vector. It is usable only if the direction and distance are set via a **Vector** and a **Height**.
- **Scale the face opposite to the base** checkbox and **Scale Factor** field allow building the extrusion with scaled opposite base. Scaling is possible only for 1D and 2D bases.
- **Add thickness** checkbox and **Thickess** field allow adding thickness to the created prism (only when extruding an edge or wire). By default the material is added on the outside of the generated pipe, but it is possible to **Thicken towards the inside** using the corresponding checkbox. **TUI Command:** *geompy.Thicken(Shape, Thickness)*

  ![prism_with_thickness.png](https://docs.salome-platform.org/latest/gui/GEOM/prism_with_thickness.png)
- **Advanced options:** [Preview](restore_presentation_parameters_page.md#preview_anchor) - displays the resulting shape in the viewer before **Apply** command.

Our **TUI Scripts** provide you with useful examples of creation of [Complex Geometric Objects](tui_complex_objs_page.md#tui_creation_prism).
