<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geometry_preferences_page.html -->

# Geometry preferences

## Settings

In the **Geometry** module you can set preferences for visualization of geometrical figures, which can be used right now or in later sessions with this module according to the preferences.

![pref15.png](https://docs.salome-platform.org/latest/gui/GEOM/pref15.png)

:   To redefine any color click on the corresponding line to access to the **Select Color** dialog box.

- **General**
  - **Default display mode** - allows to choose between wireframe, shading or shading with edges.
  - **Default shading color** - allows to select default shading color.
  - **Edges in shading** - allows to select default edges color in shading mode.
  - **Default wireframe color** - allows to select default wireframe color (to be applied to any lines not being free boundaries or isolated lines).
  - **Color of free boundaries** - allows to select default color for free boundaries.
  - **Color of edges, vectors and wires** - allows to select default color for edges, vectors and wires (isolated lines).
  - **Color of points** - allows to select default color for vertices.
  - **Color of isolines** - allows to select default color for isolines.
  - **Color of labels** - allows to select default color for labels (textual fields, shape name).
  - **Top level color** - allows to select default color for objects which were brought to the viewer foreground.
  - **Top level display mode** - allows to select default top level display mode between:
    - **Show additional wireframe actor** - allows to have the shading actor at its usual place (in the back) and add the additional wireframe actor in the viewer foreground.
    - **Keep current display mode** - allows to use current display mode of object.
    - **Wireframe** - allows to switch display mode to wireframe mode after "top-level" operation.
    - **Shading** - allows to switch display mode to shading mode after "top-level" operation.
    - **Shading With Edges** - allows to switch display mode to shading with edges mode after "top-level" operation.
  - **Default transparency** - allows to define default transparency value.
  - **Default deflection coefficient** - allows to define default deflection coefficient for lines and surfaces. A smaller coefficient provides better quality of a shape in the viewer.
  - **Show predefined materials in popup menu** - allows to customize the displaying of popup menu with list of predefined materials.
  - **Default material** - allows to define default material.
  - **Subshapes color for editing a group** - allows to select default color for subshapes in a group.
  - **Default edges width** - allows to define default width of the edges.
  - **Default isolines width** - allows to define default width of the isolines.
  - **Preview edges width** - allows to define width of the edges for preview.
  - **Measures line width** - allows to define lines width of measurements tools.
  - **Step value for spin boxes** - allows to define the increment of values set in spin boxes.
  - **Automatic bring to front** - when the option is on, the objects selected by the user automatically become "top-level".

- **Dimensions (Measurements)** - a group of preferences controlling the presentation of dimensions.
  - **Color** - allows to define color for persistent dimension presentations.
  - **Line width** - allows to define pixel width of dimension lines.
  - **Font height** - allows to define height of dimension text.
  - **Length of arrows** - allows to define length of dimension arrows.
  - **Length measurement units** - allows to define units of measurement for lengths dimensions.
  - **Angle measurement units** - allows to define units of measurement for angles dimensions.
  - **Show units of measurements** - when this option is on, the measurement units are added as prefix to value label of dimension.
  - **Default flyout length** - allows to define default flyout length used when creating the dimensions. The length can be interactively changed after creation by moving the flyouts.

- **Default number of isolines** - allows to specify the default number of isolines along **Along U** and **Along V** coordinate axes. They are shown on each selected face. For example:

  ![isos.png](https://docs.salome-platform.org/latest/gui/GEOM/isos.png)

  This preference is not related with **Create Isoline** operation. By default **Along U** and **Along V** are null and isolines are not drawn.

- **Input fields precision** - a group of preferences controlling input precision for floating-point data. The semantics of the precision values is described in detail in *Using input widgets* chapter of GUI documentation (Introduction to Salome Platform / Introduction to GUI / Using input widgets). In brief: **positive** precision value is the maximum allowed number of digits after the decimal point in the fixed-point format; **nagative** precision value is the maximum allowed number of significant digits in mantissa in either the fixed-point or scientific format.
  - **Length precision** - allows to adjust input precision of coordinates and dimensions.
  - **Angular precision** - allows to adjust input precision of angles.
  - **Length tolerance precision** - allows to adjust input precision of tolerance of coordinates and dimensions.
  - **Angular tolerance precision** - allows to adjust input precision of tolerance of angles.
  - **Weight precision** - allows to adjust input precision of weight and mass.
  - **Density precision** - allows to a just input precision of density.
  - **Parametric precision** - allows to adjust input precision of parametric values.
  - **Parametric tolerance precision** - allows to adjust input precision of tolerance in parametric space.

- **Default marker of points**
  - **Type** - allows to select the default symbol for representation of points (cross, asterisk, etc.).
  - **Size** - allows to define the default size of the marker from 1 (smallest) to 7 (largest).

- **Scalar bar for field presentation**
  - **X position** - allows to define the parametric X position of the scalar bar.
  - **Y position** - allows to define the parametric Y position of the scalar bar.
  - **Width** - allows to define the parametric width of the scalar bar.
  - **Height** - allows to define the parametric height of the scalar bar.
  - **Text height** - allows to define the font height of the scalar bar labels.
  - **Number of intervals** - allows to define the number of scalar bar intervals.

- **Origin and base vectors**
  - **Length of base vectors** - allows to define the length of base vectors.
  - **Auto create** - allows to automatically create a point of origin and three base vectors of the rectangular coordinate system immediately after the module activation.

- **Operations**
  - **Preview** - allows to customize the displaying preview by default.
  - **Hide input objects from the viewer** - allows automatic hiding of input shapes from the 3D viewer (OCC and VTK) in all operations of Geometry module.

## Dependency Tree

This tab groups preferences for visualization of **Dependency Tree** in the 2D Viewer.

![pref_dep_tree.png](https://docs.salome-platform.org/latest/gui/GEOM/pref_dep_tree.png)

- **General**
  - **Hierarchy type** - allows to choose the default display mode of the dependency tree.
  - **Possibility to move nodes** - enables/disables the possibility of moving nodes by default.

- **Color**
  - **Background color** - allows to select the default background color.
  - **Default node color** - allows to select the default node color.
  - **Main node color** - allows to select the default main node color.
  - **Unpublished node color** - allows to select the default node color for unpublished objects.
  - **Selected node color** - allows to select the default selected node color.
  - **Default arrow color** - allows to select the default arrow color.
  - **Highlighted arrow color** - allows to select the default highlighted arrow color.
  - **Selected arrow color** - allows to select the default selected arrow color.
