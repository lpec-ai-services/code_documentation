<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/connectivity.html -->

# Nodal connectivity of elements

The following images show order of nodes in correctly defined elements.

|  |
| --- |
| Edge (segment): linear and quadratic  figure |
| Triangle: linear, quadratic and bi-quadratic  figure |
| Quadrangle: linear, quadratic and bi-quadratic  figure |
| Polygon: linear and quadratic  figure |
| Tetrahedron: linear and quadratic  figure |
| Hexahedron: linear, quadratic and tri-quadratic  figure |
| Pentahedron: linear and quadratic  figure |
| Pyramid: linear and quadratic  figure |
| Hexagonal prism  figure |
| Polyhedron is defined by  - a sequence of nodes defining all facets - a sequence of number of nodes per facet  **Nodes**: Node1_of_Facet1, Node2_of_Facet1, …, NodeN_of_Facet1, Node1_of_Facet2, Node2_of_Facet2, …, NodeN_of_Facet2, Node1_of_FacetM, Node2_of_FacetM, …, NodeN_of_FacetM  **Quantity** of nodes per facet: NbNodes_in_Facet1, NbNodes_in_Facet2, …, NbNodes_in_FacetM  For example the polyhedron shown in the image below is defined by nodes [ 1,2,3, 1,4,5,2, 2,5,6,3, 3,6,4,1, 4,7,9,5, 5,9,8,6, 6,8,7,4, 7,8,9 ] and quantities [ 3, 4, 4, 4, 4, 4, 4, 3 ]  figure  Order of nodes of a facet must assure outward direction of its normal. |
