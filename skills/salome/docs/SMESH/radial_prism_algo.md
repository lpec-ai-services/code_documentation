<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/radial_prism_algo.html -->

# Radial Prism

This algorithm applies to the meshing of a hollow 3D shape,
i.e. such shape should be composed of two meshed shells: an outer
shell and an internal shell without intersection with the outer
shell. One of the shells should be a [2D Projection](projection_algos.md#projection-2d) of the other
shell. The meshes of the shells can consist both of triangles and
quadrangles.

The Radial Prism algorithm would fill the space between the two shells
with prisms.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/radial_prism_mesh.png)

**Cut-view of a hollow sphere meshed by Radial Prism algorithm**

This algorithm also needs the information concerning the number and
distribution of mesh layers between the inner and the outer shapes.
This information can be defined using either of two hypotheses:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/number_of_layers.png)

***“Number of layers”* hypothesis**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/distribution_of_layers.png)

***“Distribution of layers”* hypothesis**

*Distribution of layers* hypothesis allows using most of
[1D Hypotheses](1d_meshing_hypo.md#a1d-meshing-hypo-page) to define
the distribution of mesh layers.

**See also** a sample [TUI script](tui_defining_hypotheses.md#tui-radial-prism).
