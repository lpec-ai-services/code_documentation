<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_isoline_page.html -->

# Isoline

**Isoline** is a 3D curve built on a bounded face limited by  *[Umin, Umax]*  and  *[Vmin, Vmax]*  values of U and V parameters. For all points of the isoline U or V parameter value is constant.

Result of this operation is either a single edge or a compound of edges.

To create an **Isoline** of a face in the **Main Menu** select **New Entity - > Basic - > Isoline**.

![isoline1.png](https://docs.salome-platform.org/latest/gui/GEOM/isoline1.png)

In this dialog:

- Input or accept the default **Name** of the resulting shape.
- Click the arrow button and select in the Object Browser or in the Viewer the **Face**, for which the Isoline is built.
- Select along which coordinate: **U-Isoline** or **V-Isoline** the Isoline is built;
- Set **Parameter** (ranging from 0 to 1), which defines the proportion, at which a face is divided by the isoline. If Parameter=0.5, the isoline is a median.
- Press "Apply" or "Apply & Close" button to get the result (an edge or a compound of several edges).

This operation can be performed using a **TUI Command:**

*geompy.MakeIsoline(theFace, IsUIsoline, theParameter)*

**Arguments:** Name + Face + Type (True for U-Isoline; False for V-Isoline) + Parameter.

**Example:**

![isoline2.png](https://docs.salome-platform.org/latest/gui/GEOM/isoline2.png)

Isoline on a rectangle face

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_curve).
