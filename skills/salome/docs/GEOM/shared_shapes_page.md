<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/shared_shapes_page.html -->

# Get Shared Shapes

This operation is a special case of **Explode** operation. It produces sub-shapes of the exploded shape (the first shape in the list of argument shapes), which are shared with other shapes in the arguments. The argument shapes can also be contained in a compound or group.

To use this operation, select in the Main Menu **Operations -> Get Shared Shapes.** The following dialog box will appear.

![shared_shapes.png](https://docs.salome-platform.org/latest/gui/GEOM/shared_shapes.png)

In this dialog:

- **Name** is the base name of the resulting shapes.
- **Shapes** are the shapes whose shared sub-shapes should be found.
- **Sub-shapes Type** is the type of required sub-shapes.
- **Shared by all** option specifies what type of shared sub-shapes should be checked:
  - **On:** searches for sub-shapes from the first input shape shared with all other input shapes;
  - **Off:** searches for sub-shapes shared between couples of input shapes.

Note
:   For the case when "Shared by all" option is switched off - if an input list of shapes contains a single compound, the sub-shapes shared between all possible couples of its top-level shapes are searched for; otherwise, only sub-shapes that are shared between the first input shape and all other input shapes are searched.

**Advanced options:** [Preview](restore_presentation_parameters_page.md#preview_anchor)

**TUI Command:**  *geompy.GetSharedShapesMulti( Shapes, Type ),*   
where *Shapes* is a list or compound of shapes, whose shared sub- shapes should be found and *Type* is the type of required sub-shapes.

Our **TUI Scripts** provide you with useful examples of the use of Get Shared Shapes functionality:

- [Example 1](tui_basic_operations_page.md#tui_shared_shapes)
- [Example 2](tui_test_others_page.md#swig_GetSharedShapes)
