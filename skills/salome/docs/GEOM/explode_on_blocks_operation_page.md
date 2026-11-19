<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/explode_on_blocks_operation_page.html -->

# Explode on Blocks

To produce an **Explode on Blocks** operation in the **Main Menu** select **Operations - > Blocks - > Explode on Blocks**.

This operation returns blocks of the given compound. The user may define the type of blocks to be extracted by setting the minimum and maximum number of faces in the target block. By checking the corresponding box the user may also interactively choose the blocks from a compound.

The **Result** will be a **GEOM_Object**.

**TUI Command:** *geompy.MakeBlockExplode(Compound, MinNbFaces, MaxNbFaces),* where *Compound* is a compound to be exploded into the blocks, *MinNbFaces*, *MaxNbFaces* are correspondingly the minimal and the maximal number of faces of the resulting blocks.   
**Arguments:** 1 compound + 2 integers (min. and max. number of faces in the block to be extracted).

![mtransf3.png](https://docs.salome-platform.org/latest/gui/GEOM/mtransf3.png)

**Example:**

![block_explodesn.png](https://docs.salome-platform.org/latest/gui/GEOM/block_explodesn.png)

Explode on blocks operation

Our **TUI Scripts** provide you with useful examples of the use of [Blocks Operations](tui_blocks_operations_page.md#tui_explode_on_blocks).
