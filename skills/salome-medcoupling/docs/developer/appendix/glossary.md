<!-- source: appendix/glossary.dox -->

# Glossary, concepts and definitions

- **Mesh:** representation of a domain by a set of **cells** and **nodes.** Cells and nodes are named **entities.** There is no notion of edges or faces.
- The **dimension** **of** **a** **mesh** is characterized by two parameters: the size of the space wherein the mesh is immersed, and the (maximum) size of the mesh cells.
Examples: 3D surface mesh (3D space, 2D cells), 3D mesh (3D space, 3D cells), curved 2D mesh (2D space, 1D cells)...

- **Field:** physical quantity whose value varies in space and time. Represented by a result vector V obtained from one or more tables of values A, at any point of space covered by a mesh and in time defined by its temporal resolution. The size of V is called the number of **components** (equal to the number of components of A).
A <b>P1 field</b> is a field where values are stored at node level, a <b>P0 field</b> is a field where values are stored
at cell level.
- **Intensive** **field:** represents intensive physical data (i.e. which do not depend on the amount of material).
Examples: density, power density, temperature, pressure.
- **Extensive** **field:** represents extensive physical data (i.e. proportional to the size of the physical system represented).
Examples: mass, volume, time, power.
- The **mesh** **support** identifies both the mesh and the entity on which it is defined.

- **Family:** partition of a mesh (nodes and cells with the same identifier). Every node or cell can only belong to one family, i.e. the intersection of two families is zero.
- **Group:** a set of families; two groups may share elements.
- **Profile:** subset of the entities of a mesh.
- **Field** **profile:** indicates on which mesh entities field values are located (a field being defined on a part of a mesh).

- The **connectivity** of a mesh represents the kind of connections between its vertices.
- The **nodal** **connectivity** is the description of a mesh entity by the ordered list of its nodes.
- The **descending** **connectivity** is the description of N-dimensional mesh entities by the ordered list of (N-1)-dimensional geometrical entities.

- **Intersector:** algorithm that calculates the intersection of two cells from their position and geometry.
- **Maximum** **principle:** a property of solutions to certain partial differential equations, of the elliptic and parabolic types; it says that the maximum of a function in a domain is to be found on the boundary of that domain.
- **Conservativity:** preservation of conservation laws governing physical quantities during their discretization or their interpolation.
- **Projection:** modification (by interpolation) of the entity on which a field is defined. The projection is called **conservative** if the interpolation uses intersection detection. The projection is said **not** **conservative** if the interpolation localizes a cloud of points in a mesh.
- The **Gauss** **integration** **points** are the geometrical points where the numerical integration of a given quantity is performed. Precise location of these nodes and a sufficient number (related to the approximation order of the integration term) allow for an exact integration in the case of polynomial functions integration.
- **Kriging:** a linear estimation method guaranteeing minimum variance. The estimate at a given point P is obtained locally from the point values on a neighborhood of P.
- **Code** **coupling:** run of two numerical codes (or two instances of the same code) in such a way that information
is passed from one instance to the other.
