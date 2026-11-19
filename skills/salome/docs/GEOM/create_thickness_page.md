<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_thickness_page.html -->

# Thickness Construction

To add **Thickness** to a shape in the **Main Menu** select **New Entity - > Generation - > Thickness**.

Switch between adding thickness to a Face (Shell) or a Solid using radio buttons.

Firstly, **Thickness** can be applied to a Face or a Shell to create a Solid.

![thickness.png](https://docs.salome-platform.org/latest/gui/GEOM/thickness.png)

It is necessary to define an **Object** (Face or Shell) and the value of **Thickness**. **Thicken towards the inside** check box allows changing the thickness direction.

**Example:**

![thickness_result.png](https://docs.salome-platform.org/latest/gui/GEOM/thickness_result.png)

Thickness of Shell

Secondly, the **Thickness** can be applied to a Solid to create a hollowed Solid.

![thicksolid.png](https://docs.salome-platform.org/latest/gui/GEOM/thicksolid.png)

It is necessary to define a Solid **Object** **Faces** to be removed from the result and **Thickness**. **Thicken towards the inside** check box allows changing the thickness direction.

**Example:**

![thicksolid_result.png](https://docs.salome-platform.org/latest/gui/GEOM/thicksolid_result.png)

Thickness of Solid

**TUI Commands:**   
*geompy.MakeThickSolid(theShape, theThickness, theFacesIDs=[])* - Makes a thick solid from a shape;   
*geompy.Thicken(theShape, theThickness, theFacesIDs=[])* - Modifies a shape to make it a thick solid.

**Arguments:** Name + 1 shape (face, shell or solid) + thickness + the list of face IDs.   
If the shape is a face or a shell the list of face IDs is not used. The thickness can be positive or negative for thickening towards the inside.   
  
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

Our **TUI Scripts** provide you with useful examples of creation of [Complex Geometric Objects](tui_complex_objs_page.md#tui_creation_thickness).
