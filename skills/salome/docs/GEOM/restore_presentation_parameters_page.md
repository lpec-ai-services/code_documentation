<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/restore_presentation_parameters_page.html -->

# Advanced Transformation Options

**Set presentation parameters and sub-shapes from arguments**

This option allows the operation result to inherit color and sub-shapes from its arguments.

To activate this functionality, check in "Set
presentation parameters and sub-shapes from arguments" checkbox in the corresponding dialog.

For example, there exist two objects: Box_1 with two published faces and Cylinder_1 with free published edges.

![restore-ss-viewer-before.png](https://docs.salome-platform.org/latest/gui/GEOM/restore-ss-viewer-before.png)

The initial box and cylinder

First, we examine the case when the resulting shape corresponds to one argument (after transformation, after the Boolean operation Cut, or after the partition with one object shape).

We create a Cut of Box_1 with Cylinder_1.

![restore-ss-cut.png](https://docs.salome-platform.org/latest/gui/GEOM/restore-ss-cut.png)

The resulting shape inherits the sub-shapes and the colour of Box_1.

![restore-ss-viewer-cut.png](https://docs.salome-platform.org/latest/gui/GEOM/restore-ss-viewer-cut.png)

The resulting shape

Second, we examine the case when the resulting shape is composed from multiple arguments (after all Boolean operations, except for Cut, or after the partition with several object shapes, or if the resulting shape is a compound).

We create a Common of Box_1 and Cylinder_1.

![restore-ss-dialog.png](https://docs.salome-platform.org/latest/gui/GEOM/restore-ss-dialog.png)

The resulting object is created with several sub-shapes that correspond to the operation arguments and their published sub-shapes. The resulting shape has a default color, but its sub-shapes inherit colors corresponding to arguments and their sub-shapes.

![restore-ss-viewer-after.png](https://docs.salome-platform.org/latest/gui/GEOM/restore-ss-viewer-after.png)

The resulting shape

Please, note that when the resulting shape corresponds to one argument, the inherited sub-shapes depend directly on the resulting shape.

![restore-ss-OB-cut.png](https://docs.salome-platform.org/latest/gui/GEOM/restore-ss-OB-cut.png)

When the resulting shape is composed from multiple arguments, the inherited sub-shapes depend on the arguments.

![restore-ss-OB.png](https://docs.salome-platform.org/latest/gui/GEOM/restore-ss-OB.png)

You can also call this functionality from your python scripts. See our **TUI Scripts** for [example](tui_basic_operations_page.md#tui_restore_prs_params).

**Add prefix to names of restored sub-shapes**

This option allows adding the prefix "from_" to the names of restored sub-shapes, and the prefix "from_subshapes_of_" to the names of partially restored sub-shapes. By default this option is On.

**Preview**

**Preview** checkbox allows displaying/erasing simulation of the **Result** in the viewer.
