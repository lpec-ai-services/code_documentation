<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_polyline_page.html -->

# 2D Polyline

The 2D Polyline allows drawing arbitrary 2D shapes.

To create a **2D Polyline** select in the main menu **New Entity -> Basic -> 2D Polyline**.

![polyline_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/polyline_dlg.png)

A polyline represents a section or a set of sections. Each section is constructed from a sequence of 2D points connected by either linear segments or an interpolation curve. Every section has its own attributes:

- **Name**,
- **Type** (Polyline or Spline),
- **Closed** flag.

A created Polyline represents a shape that lies on the XOY plane. Its type can be one of the following:

- **Vertex** for a single section with only 1 point.
- **Wire** for a single section with 2 or more points. A Wire can have multiple edges for more then 2 points if the section type is Polyline. A single edge in the resulting wire is obtained for a Spline or Polyline with 2 points.
- **Compound** of Wires and/or Vertices if there are several sections.

For the moment only one reference coordinate system for polyline creation is supported, which is the XOY plane of the **Global coordinate system**. **Restore** button orientates the viewer correspondingly to the chosen working plane and fits the scene to show all objects. For the moment this button works with only one plane.

It is possible to import a shape in this dialog using **Import polyline** selection button. An imported object should meet the conditions for polyline shapes mentioned above. If a valid shape is selected, when the dialog is opened, it is initialized by this shape. Though the shape can be on any plane, the imported polyline will be defined on XOY plane only due to the limitation.

The group **Sections** in this dialog represents the Polyline construction framework.

The buttons **Undo** and **Redo** allow to undo or redo the changes of the polyline.

**Insert new section** button opens the corresponding dialog:

![polyline_dlg_add_section.png](https://docs.salome-platform.org/latest/gui/GEOM/polyline_dlg_add_section.png)

In this dialog it is possible to choose:

- **Name** of section;
- **Type** of section;
- Set **Closed** flag.

To create a new section, click **Add** button. **Cancel** button is used to cancel this operation. After clicking **Add** button a new section appears in the list. Its name is generated automatically depending on its type, closed or opened state and the number of points (equal to 0 after creation).

To modify section parameters, double-click on a section in the list. In this case the following dialog appears:

![polyline_dlg_edit_section.png](https://docs.salome-platform.org/latest/gui/GEOM/polyline_dlg_edit_section.png)

To apply the modifications, click **Ok** button.

**Addition mode** allows adding points to a section. Select a particular section in the list of sections and left-click in the viewer to add new nodes to the section. A section preview is recomputed after each click.

**Modification mode** and **Detection mode** are not implemented for the moment.

**Remove** button allows removing a section. It is available if all modes are deactivated and one section is selected.

**Join selected sections** button is available in modification mode if two or more sections are selected. It is used to merge several sections into the first one from the selection list. The points of the merged sections are appended at the end of the list of points of the first section.

Some actions are available via the context menu activated by right mouse button click.

- **Join all sections** - joins all defined sections into the first one.
- **Join** - joins two or more selected sections.
- **Clear all** - removes all selected sections.
- **Set closed** - sets **Closed** flag for all selected section.
- **Set open** - unset **Closed** flag for all selected sections.
- **Set polyline** - sets the type of all selected sections to Polyline.
- **Set spline** - set the type of all selected sections to Spline.

Different actions are available depending on the mode and selection.

## TUI Commands

To create the 2D polyline in TUI Polyline2D interface is used.

*pl = geompy.Polyline2D()* - returns an instance of Polyline2D interface *pl*.

See the [Polyline2D](../GEOM/geompy_doc/classgsketcher_1_1Polyline2D.md) interface documentation for more information.

Our **TUI Scripts** provide you with useful examples of the use of [2D Polyline](tui_basic_geom_objs_page.md#tui_creation_polyline).
