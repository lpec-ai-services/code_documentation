<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/inspect_object_operation_page.html -->

# Inspect Object

This operation allows browsing the contents of the selected shape.

To **Inspect Object**, in the **Main Menu** select **Measures - > Inspect Object**.

The dialog can be used in two modes. The first one is a tree view mode:

![inspect_object.png](https://docs.salome-platform.org/latest/gui/GEOM/inspect_object.png)

Dialog in the tree view mode

This is a default mode that allows to inspect an object in the form of tree starting from the shape itself. Its children are its direct sub-shapes that have they own children as sub-shapes etc. till most very base sub-shapes, i.e. vertices.

The second mode is a filtering one. It is activated when the user selects **Tolerance filter** check box:

![inspect_object2.png](https://docs.salome-platform.org/latest/gui/GEOM/inspect_object2.png)

Dialog in the filtering mode

In this mode the user can check the type of sub-shapes to work with using the radio-buttons. The type can be either **Vertex**, **Edge** or **Face**. Then the user choses a tolerance criterion to be applied to filter out sub-shapes. It is possible to chose one of the following values:

- **>** - greater than (default value)
- **>=** - greater than or equal to
- **<** - lower than
- **<=** - lower than or equal to

The last parameter to be chosen is the tolerance value. The result is the shapes of a certain type that satisfy the defined tolerance criterion. E.g. if the user chooses **Face**, criterion **>** and tolerance value equal to **1.e-6** the faces with the tolerance greater than **1.e-6** are displayed.

It is possible to set maximal and minimal value of the tolerance using the buttons **Max value** and **Min value**. These values are displayed in the labels **Max :** and **Min :**

In this dialog never mind of its mode it is possible to:

- Click on the "selection" button and select an object to inspect in the Object Browser or in the viewer.
- Show/hide sub-shape(s) in the 3D viewer, by pressing "eye" icon in the first column of the tree view.
- Show/hide all sub-shapes in the tree, by pressing "eye" icon in the first column of the tree view header or by pressing **Show all**/**Hide all** buttons.
- Rename the selected sub-shape by double-clicking on the item or pressing <F2> key.
- Show the selected sub-shape(s) in the 3D viewer by pressing **Show Selected** button.
- Show the selected sub-shape(s) in the 3D viewer and erase all currently shown objects by pressing **Show Only Selected** button.
- Hide the selected sub-shape(s) from the 3D viewer by pressing **Hide Selected** button.
- Publish the selected sub-shapes in the study, by pressing **Publish Selected** button.
- Close dialog box, by pressing **Close** button.

**TUI Command:**

A command to filter sub-shapes is defined:

*geompy.GetSubShapesWithTolerance(theShape, theShapeType, theCondition, theTolerance),*   
where   
*theShape* is the shape to be exploded.   
*theShapeType* is the type of sub-shapes to be returned. Can have the values **[GEOM.FACE](../GEOM/geompy_doc/namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5a5cfae78048cf95359061c2e812e7d691)**, **[GEOM.EDGE](../GEOM/geompy_doc/namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5aa622cbc12b78e3e883dd7b3217088a66)** and **[GEOM.VERTEX](../GEOM/geompy_doc/namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5a2e4d5495bd9d476f78962cebe074ebbd)** only.  
*theCondition* is the condition type (the value of [GEOM.comparison_condition](../GEOM/geompy_doc/namespaceGEOM.md#a52c7cde4c3a1dbddbfbae07edcd7072d) emuneration).  
*theTolerance* is the tolerance filter.

See also a [TUI example](tui_test_all_page.md#swig_GetSubShapesWithTolerance).
