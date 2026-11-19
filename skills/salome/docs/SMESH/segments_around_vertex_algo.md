<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/segments_around_vertex_algo.html -->

# Segments around Vertex

**Segments around Vertex** algorithm is considered to be a 0D meshing
algorithm, but, of course, it doesn’t mesh vertices. It allows to define
the local size of the segments in the neighborhood of a certain
vertex. If we assign this algorithm to a geometrical object of higher
dimension, it applies to all its vertices.

Length of segments near vertex is defined by **Length Near Vertex** hypothesis.
This hypothesis is used by [Wire Discretization](basic_meshing_algos.md#a1d-algos-anchor) or
[Composite Side Discretization](basic_meshing_algos.md#a1d-algos-anchor) algorithms as
follows: a geometrical edge is discretized according to a 1D
hypotheses and then nodes near vertices are modified to assure the
segment length required by **Length Near Vertex** hypothesis.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/lengthnearvertex.png)

**See also** a sample [TUI Script](tui_defining_hypotheses.md#tui-segments-around-vertex).
