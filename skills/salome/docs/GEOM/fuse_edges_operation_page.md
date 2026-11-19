<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/fuse_edges_operation_page.html -->

# Fuse Collinear Edges within a Wire

To **Fuse Collinear Edges within a Wire** in the **Main Menu** select **Repair - > Fuse Collinear Edges within a Wire**.   
This operation removes the selected vertices from a given wire, provided that the junction of two adjacent edges is C1 continuous (i.e. the edges have equal tangents at the junction).   
The function takes a list of vertices to suppress as a parameter. If the list is empty, all vertices in a wire are taken into account.

**Example:**

Wire with 2 colinear edges:

![wire_before_fuse.png](https://docs.salome-platform.org/latest/gui/GEOM/wire_before_fuse.png)

Fused wire (only one edge):

![fused_wire.png](https://docs.salome-platform.org/latest/gui/GEOM/fused_wire.png)

**Arguments:** Name + a wire + a list of vertices (can be empty).

![fuse_collinear_edges.png](https://docs.salome-platform.org/latest/gui/GEOM/fuse_collinear_edges.png)

**TUI Command:** *geompy.FuseCollinearEdgesWithinWire(wire, vertices)*, where *wire* is a wire and *vertices* is a list of vertices to be suppressed.

Our **TUI Scripts** provide you with useful examples of the [Fuse Collinear Edges](tui_repairing_operations_page.md#tui_fuse_collinear_edges) functionality usage.
