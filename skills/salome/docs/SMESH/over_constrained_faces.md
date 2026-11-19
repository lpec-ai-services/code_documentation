<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/over_constrained_faces.html -->

# Over-constrained faces

This mesh quality control highlights faces having all their points on the border.

Note

The highlighted faces are actually over-constrained only if, at the computation time, the boundary conditions on the borders where the nodes are located are all Dirichlet boundary conditions.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/over_constrained_faces.png)

**Over-constrained face is displayed in red**

**See Also** a sample TUI Script of a [Over-constrained faces](tui_quality_controls.md#tui-over-constrained-faces) filter.
