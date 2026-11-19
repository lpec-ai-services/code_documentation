<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/using_boolean_operations_page.html -->

# Boolean Operations

For a detailed description of Boolean operations refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf). It provides a general review of the Partition and Boolean operations algorithms, describes the usage methodology and highlights major limitations of these operations.

You can use the following boolean operations for construction of more complex geometrical objects (2D & 3D elements):

- [Fuse](fuse_operation_page.md) - creates a shape from a list of shapes.
- [Common](common_operation_page.md) - transforms the common part of a list of objects into an independent object.
- [Cut](cut_operation_page.md) - cuts one shape with a list of others.
- [Intersection](section_operation_page.md) - performs an intersection between two shapes.

You can use advanced TUI commands performing these operations independently from each other:

:   *geompy.MakeFuseList(theShapesList, checkSelfInte, rmExtraEdges)*, where *theShapesList* is the list of shapes for Fuse operation;

:   *geompy.MakeCommonList(theShapesList, checkSelfInte)*, where *theShapesList* is the list of shapes for Common operation;

:   *geompy.MakeCutList(theMainShape, theShapesList, checkSelfInte)*, where *theMainShape* is the object of the operation and *theShapesList* is the list of tools for Cut operation;

:   *geompy.MakeSection(Shape1, Shape2, checkSelfInte)*, where *Shape1* is the first argument and *Shape2* is the second argument of Intersection operation;

There are several TUI commands that can be used to perform boolean operations with only two arguments. There is a general TUI command covering these operations, which can be used alongside with separate commands for each operation.

:   *geompy.MakeBoolean(Shape1, Shape2, Operation, checkSelfInte),* where *Shape1* is the first argument and *Shape2* is the second argument of a Boolean operation, *Operation* is the type of a Boolean operation (1 — Common, 2 — Cut, 3 — Fuse, 4 — Intersection).

Besides, you can use advanced TUI commands performing these operations independently from each other:

:   *geompy.MakeFuse(Shape1, Shape2, checkSelfInte, rmExtraEdges)*, where *Shape1* is the first argument and *Shape2* is the second argument of Fuse operation;

:   *geompy.MakeCommon(Shape1, Shape2, checkSelfInte)*, where *Shape1* is the first argument and *Shape2* is the second argument of Common operation;

:   *geompy.MakeCut(Shape1, Shape2, checkSelfInte)*, where *Shape1* is the first argument and *Shape2* is the second argument of Cut operation;

The flag *checkSelfInte* indicates whether the arguments should be checked for self-intersection prior to an operation. Its default value is *False*, which means that there is no need to check it. This option is provided to ensure that an operation is performed on not self-intersected shapes as they are not valid for boolean operations.

Note
:   This algorithm does not find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections use [Detect Self-intersection tool](check_self_intersections_page.md).

The flag *rmExtraEdges* is used for *MakeFuseList* and *MakeFuse* operations only. It indicates if Remove Extra Edges operation should be performed during the operation. Its default value is *False*, which means that there is no need to do it.

Note
:   *rmExtraEdges* is not available for *MakeBoolean* call with operation type 3 (Fuse). *MakeBoolean* operation doesn't perform Remove Extra Edges. So the call *geompy.MakeBoolean(Shape1, Shape2, 3, checkSelfInte)* is equivalent to *geompy.MakeFuse(Shape1, Shape2, checkSelfInte, False)*.

Our **TUI Scripts** provide you with useful examples of the use of [Boolean Operations](tui_boolean_operations_page.md).
