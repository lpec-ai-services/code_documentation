<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/fuse_operation_page.html -->

# Fuse

**Fuse** operation creates one shape from a list of shapes.

To produce it, select in the Main Menu **Operations - > Boolean - > Fuse**.

![bool1.png](https://docs.salome-platform.org/latest/gui/GEOM/bool1.png)

Fuse dialog

In this dialog:

- Input or accept the default **Name** of the resulting shape.
- Click the arrow button and select in the Object Browser or in the Viewer the **Objects** to be fused.
- Activate the corresponding check-box if you wish to  **Detect Self-intersections** .
- Activate the corresponding check-box if you wish to  **remove extra edges** .
- Activate the corresponding check-box if you wish to use a  **fuzzy parameter** .   
  If activated, you can define the fuzzy tolerance in the  **fuzzy parameter**  input box.
- Activate [Advanced options](restore_presentation_parameters_page.md) if required.
- Press "Apply" or "Apply & Close" button to get the result (GEOM_Object).

Note
:   This algorithm does not find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections use [Detect Self-intersection tool](check_self_intersections_page.md).

This operation can be performed using a **TUI Command:**

*geompy.MakeFuseList(theShapesList, checkSelfInte, rmExtraEdges, name, fuzzyParam)*

**Arguments:** a list of shapes + an optional flag for self-intersection check + an optional flag to remove extra edges + an optional name + an optional fuzzy parameter.

There is also a special **TUI Command** for **Fuse** operation on two shapes :

*geompy.MakeFuse(s1, s2, checkSelfInte, rmExtraEdges, name, fuzzyParam)*

**Arguments:** 2 shapes + an optional flag for self-intersection check + an optional flag to remove extra edges + an optional name + an optional fuzzy parameter.

**Example:**

![fusesn1.png](https://docs.salome-platform.org/latest/gui/GEOM/fusesn1.png)

The initial shapes

![fusesn2.png](https://docs.salome-platform.org/latest/gui/GEOM/fusesn2.png)

The resulting fuse

Our **TUI Scripts** provide you with useful examples of the use of [Boolean Operations](tui_boolean_operations_page.md#tui_fuse).

**More details**

Please, refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf) for a detailed description of Boolean operations.

It provides a general review of the Partition and Boolean operations algorithms, describes the usage methodology and highlights major limitations of these operations.

Perhaps you also ask yourself : [What is the difference between partition, compounds and fuse operation ?](partition_explanation.md)
