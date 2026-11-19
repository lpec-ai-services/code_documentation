<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/get_non_blocks_page.html -->

# Get Non Blocks

This operation retrieves all non-block solids and non-quadrangular faces from the selected shape.

A block solid is a solid that has 6 quadrangular faces.

A quadrangular face is a face that has 1 wire with 4 edges. If there are more than 4 edges in a single wire and C1 continuity mode is switched on, a face is quadrangular if it has 4 bounds of C1 continuity.

All solids and faces from a shape that do not satisfy these conditions are returned by this operation.

![measures2.png](https://docs.salome-platform.org/latest/gui/GEOM/measures2.png)

It is possible to select an **Object** to be explored, to check or uncheck **Use C1 criterion** option and to set the **Angular Tolerance** to check C1 continuity between neighbor edges in a wire.

**Preview** option shows non-block solids and non-quadrangular faces in the viewer.

Press **Apply** or **Apply and Close** button to publish non-block solids and non-quadrangular faces in the Object Browser under the processed object. Solids and faces are published separately in two groups.

If no bad sub-shapes have been found, the corresponding warning is shown.

![measures2a.png](https://docs.salome-platform.org/latest/gui/GEOM/measures2a.png)

**TUI Command:** *geompy.GetNonBlocks(theShape, theIsUseC1 = False, theAngTolerance = 1.e-12).*   
where   
*theShape* is the shape to explore,   
*theIsUseC1* is the flag to check if there are 4 bounds on a face taking into account C1 continuity,   
*theAngTolerance* the angular tolerance to check if two neighbor edges are codirectional in the common vertex with this tolerance. This parameter is used only if *theIsUseC1* is set to True.

This command returns a tuple of two GEOM_Objects.

The first object is a group of all non-block solids; the second object is a group of all non-quadrangular faces.

See also a [TUI example](tui_get_non_blocks_page.md).
