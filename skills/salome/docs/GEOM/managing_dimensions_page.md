<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/managing_dimensions_page.html -->

# Manage Dimensions

**Manage Dimensions**  functionality allows showing in the viewer the measured dimensions of sub-elements of a geometrical object (shape).

![dimensions_preview.png](https://docs.salome-platform.org/latest/gui/GEOM/dimensions_preview.png)

It can be accessed from the main menu via **Measures -> Dimensions -> Manage Dimensions**

![manage_dimensions.png](https://docs.salome-platform.org/latest/gui/GEOM/manage_dimensions.png)

**List of Dimensions**

This dialog provides the list of dimensions shown in the view for the selected geometrical **Object**. The list items are sorted by dimension type: **Distance**, **Diameter** and **Angle**.

It is possible to show/hide a dimension in the view by checking on/off the box to the left of its name.

The buttons to the right of the list provide the following operations:

- "Add" - opens "Add Dimension" dialog to define a new fly-out.
- "Remove" - removes the selected item from the list.
- "Show All" / "Hide All" - shows/hides all dimensions existing in the list.

**Add a Dimension**

To add a new dimension to the object presentation, click **Add** button in the **Manage Dimensions** dialog.

![add_dimension.png](https://docs.salome-platform.org/latest/gui/GEOM/add_dimension.png)

The following dimensions can be shown:

- **Length.** There are three possible types of length dimensions:

  - **Edge length** - shows the length of the edge selected in the viewer. Only line edges, i.e. line segments built on two points are accepted.
  - **Two points**  - shows the distance between two points selected in the viewer.
  - **Parallel edges** - shows the distance between two parallel line edges.
- **Diameter**  of an an arc, a circular edge or face, a sphere, a cylinder, a cone or a torus.
- **Angle.** The angle dimension can be defined in one of two possible ways :

  - By selecting **Two edges** located in the same plane.
  - By selecting **Three points**. The second point is in the corner of the angle.

**Modification of Dimension properties**

The default properties of dimension text and line, such as font color, line width, measurement units, etc. can be defined from the [Geometry preferences](geometry_preferences_page.md).

It is also possible to change the geometrical properties of the selected dimension interactively in the viewer.

When hovering with mouse, the text and line become highlighted, which means that the dimension is ready for interactive operations.

![interact_with_dimensions.png](https://docs.salome-platform.org/latest/gui/GEOM/interact_with_dimensions.png)

The following operations are possible:

- To change the fly-out of a dimension text without changing its plane (direction), drag it by mouse with left mouse button pressed.
- To change both the fly-out and the plane (direction) of a dimension text, drag the flyout by mouse with both *ctrl* key and additionally enables modification of the flyout plane.
- To modify the location of the dimension text correspondingly to the dimension line, drag it by mouse. The text can be aligned horizontally or vertically and located on the line, under it or in its center.

All modifications of the dimensions are temporary. The "Apply" and "Apply and Close" buttons save the changes.
