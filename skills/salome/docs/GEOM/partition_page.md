<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/partition_page.html -->

# Partition

For a detailed description of the Partition operation please refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf). It provides a general review of the Partition and Boolean operations algorithms, describes the usage methodology and highlights major limitations of these operations.

Perhaps you also ask yourself : [What's the difference between partition, compounds and fuse operation?](partition_explanation.md)

To produce a **Partition** in the **Main Menu** select **Operations -> Partition**

This operation builds a compound by partitioning a set of input objects by a set of tool objects.

The **Result** of the operation is a **GEOM_Object**.

![partition1.png](https://docs.salome-platform.org/latest/gui/GEOM/partition1.png)

**Arguments:** Name + 2 lists of shapes (the shapes from the first list will be intersected with the shapes from the second list) + Resulting Type of shape.

As far as the partition of two objects can produce any type of geometrical objects, **Resulting type** box allows choosing the preferable result, i.e. a solid, a shell, a list of faces, etc.

The **Resulting type** has to be equal or lower than the type of the *Objects*. In other words, if the *Objects* don't contain any shape of this type, Partition fails.

**Keep shapes of lower type** checkbox manages standalone shapes of type other than the *Limit*. If it is checked, lower dimension objects will be preserved, else they will be lost.

For example, you partition a box (Solid) and a face (Face) without any tool (the box is split in two parts by the shape). If you choose the Resulting Type "Solid", you will obtain a compound of two solids, but if you also check **Keep shapes of lower type** checkbox, you will obtain a compound of two solids and one face (there will be a hole in the resulting face, where the original face intersects with the box, see the corresponding [picture](partition_page.md#partition_picture_3) below).

**No sub-shapes intersection (Compounds only)** check box affects only input shapes of the Compound type.

- If this option is switched off (default behavior) each input compound will be automatically exploded into sub-shapes and the partition between these shapes will be also computed.
- If this option is switched on, the partition between sub-shapes will not be performed. In this case the Partition algorithm will work faster, but the result might differ from the default behavior.

**Detect Self-intersections** check box is used to check self-intersection of arguments. It is enabled only if **No sub-shapes intersection (Compounds only)** is checked.

- If this option is switched off (by default), the partition algorithm is performed without self-intersection checks.
- If this option is switched on, each input shape is checked for self-intersection. If self-intersection is detected, the operation is aborted.

Note
:   This algorithm does not find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face interferences. Face/face interference detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [Detect Self-intersection tool](check_self_intersections_page.md).

**Use Fuzzy Parameter** check box is used to enable the usage of the fuzzy tolerance inside the partition algorithm. The fuzzy tolerance itself can be given in the Fuzzy Parameter input box.

- Activate [Advanced options](restore_presentation_parameters_page.md) if required.

Note
:   Partition is a complex operation, so its result of it depends on the quality of the initial shapes. Sometimes, if partition fails, such healing operations as **Shape Processing** and **Limit Tolerance** can help to attune source shapes to obtain correct result of the Partition. See also [TUI example](tui_repairing_operations_page.md#tui_limit_tolerance) of shape healing.

**TUI Command (with sub-shapes intersection):**

*geompy.MakePartition(ListOfShapes, ListOfTools, ListOfKeepInside, ListOfRemoveInside, Limit, RemoveWebs, ListOfMaterials, KeepNonlimitShapes, fuzzyParam)*

**TUI Command (without sub-shapes intersection):**

*geompy.MakePartitionNonSelfIntersectedShape(ListOfShapes, ListOfTools, ListOfKeepInside, ListOfRemoveInside, Limit, RemoveWebs, ListOfMaterials, KeepNonlimitShapes, checkSelfInte, fuzzyParam)*

Here,

- *ListOfShapes* is a list of shapes to be intersected
- *ListOfTools* is a list of shapes to intersect the shapes from *ListOfShapes*
- *Limit* is a Type of resulting shapes
- *KeepNonlimitShapes* is a flag that allows to preserve standalone shapes of low dimension (than *Limit*) in the result.
- *checkSelfInte* is a flag that indicates if the arguments should be checked for self-intersection prior to the operation.
- *fuzzyParam* is the used fuzzy tolerance inside the partition algorithm. This tolerance is ignored, if this parameter is omitted or not positive.
- Other parameters are obsolete and kept only for compatibility with previous versions of SALOME.

**Examples:**

![partitionsn1.png](https://docs.salome-platform.org/latest/gui/GEOM/partitionsn1.png)

Input data: box intersected by plane

![partitionsn2.png](https://docs.salome-platform.org/latest/gui/GEOM/partitionsn2.png)

Result: box partitioned by plane

![partitionsn3.png](https://docs.salome-platform.org/latest/gui/GEOM/partitionsn3.png)

Result: partitioned box and plane (both as *Objects*); resulting type is *Solid*; option 'Keep shapes of lower type' is on

Our **TUI Scripts** provide you with useful examples of [Basic Operations](tui_basic_operations_page.md#tui_partition).
