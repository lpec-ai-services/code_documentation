<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/check_compound_of_blocks_page.html -->

# Check Compound of Blocks

This operation checks whether a shape is a compound of glued blocks and improves the shape to include only valid blocks.

![measures10.png](https://docs.salome-platform.org/latest/gui/GEOM/measures10.png)

To be considered as a compound of blocks, the given shape must satisfy the following conditions:

- Each element of the compound should be a Block, i.e. have 6 quadrangle faces;
- Each quadrangle face should have one wire with four edges. If there are more than four edges in a single wire and C1 continuity mode is switched on, a face is quadrangular if it has four bounds with C1 continuity.
- Blocks can be connected only via an entire quadrangle face or an entire edge;
- The compound should be connected;
- Each couple of connecting quadrangle faces should be glued.

In this dialog:

- **Object** - the checked object. **Selection** button allows picking it in the viewer or in the object browser.
- **Use C1 criterion** - option switches on/off the C1 continuity mode.
- **Angular Tolerance** - angular tolerance to check C1 continuity between neighbor edges in a wire.
- **Errors** list informs of possible errors, for example:
  - Not a block;
  - Not glued;
  - Not connected;
  - Extra or degenerated edge.
- **Incriminated Sub-shapes** field outputs the list of sub-shapes that cause problem.
- **Apply** and **Apply and Close** buttons launch the improvement process and publish the result shape, which includes valid blocks only. The algorithm tries to:
  - remove seam and degenerated edges from surfaces of revolution;
  - re-approximate surfaces to exclude singularities on boundaries;
  - unite edges and faces;
  - glue faces.

**TUI Command:** *geompy.CheckCompoundOfBlocks(Compound, theIsUseC1 = False, theAngTolerance = 1.e-12).* Checks if the shape is a valid compound of blocks. If it is true, then the validity flag is returned, and encountered errors are printed in the python console.

See also a [TUI example](tui_check_compound_of_blocks_page.md).
