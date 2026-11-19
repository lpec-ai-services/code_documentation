<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/over_constrained_volumes.html -->

# Over-constrained volumes

This mesh quality control highlights volumes having all their points on the border.

Note

The highlighted volumes are actually over-constrained only if, at the computation time, the boundary conditions on the borders where the nodes are located are all Dirichlet boundary conditions.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/over_constrained_volumes.png)

**Over-constrained volume is displayed in red.**

**See Also** a sample TUI Script of a [Over-constrained volumes](tui_quality_controls.md#tui-over-constrained-volumes) filter.
