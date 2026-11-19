<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/multi_transformation_operation_page.html -->

# Block Multi Transformation

To produce a **Multi Transformation** operation in the **Main Menu** select **Operations - > Blocks - > Multi Transformation**

This operation makes several translations of a block (solid) in one or two directions depending on the arguments specified by the user.   
The **Result** in both cases will be a **GEOM_Object**.

## Simple Multi Transformation (in one direction)

**TUI Command:**  *geompy. MakeMultiTransformation1D(Block, DirFaceID1, DirFaceID2, NbTimes),* where *Block* is a block to be transformed, *DirFaceID1* is an ID of the face which defines the first direction of transformation, *DirFaceID2* is an ID of the face which defines the second direction of transformation, *NbTimes* is a number of transformations.   
**Arguments:** Name + 1 hexahedral solid + 1 or 2 faces + 1 integer (number of blocks).   
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![mtransf1.png](https://docs.salome-platform.org/latest/gui/GEOM/mtransf1.png)

![multi_transformationsn1d.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_transformationsn1d.png)

Single Multi-transformation on a box

## Double Multi Transformation (in two directions)

**TUI Command:** *geompy. MakeMultiTransformation2D(Block, DirFaceID1U, DirFaceID2U, NbTimesU, DirFaceID1V, DirFaceID2V, NbTimesV),* where *Block* is a block to be transformed, *DirFaceID1U* and *DirFaceID2U* are IDs of the faces, which define directions of the first transformation, *DirFaceID1V* and *DirFaceID2V* are ID's of the faces which define directions of the second transformation, *NbTimesU* and *NbTimesV* are numbers of transformations.   
**Arguments:** Name + 1 hexahedral solid + 2, 3 or 4 faces + 2 integers (number of blocks).   
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![mtransf2.png](https://docs.salome-platform.org/latest/gui/GEOM/mtransf2.png)

![multi_transformationsn2d.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_transformationsn2d.png)

Double Multi-transformation on a box

Our **TUI Scripts** provide you with useful examples of the use of [Blocks Operations](tui_blocks_operations_page.md#tui_multi_transformation).
