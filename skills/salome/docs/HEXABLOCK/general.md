<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/general.html -->

# Introduction to HEXABLOCK

With SALOME framework, a CAD component (GEOM) and a meshing component (SMESH) are developed.
These tools enable to construct hexahedral meshes:

- by means of a CAD cutting in blocks topologically equivalent to hexahedra with GEOM component,
- and generate a hexahedral mesh with SMESH component.

The HEXABLOCK component of SALOME is designed to help users to build hexahedral meshes:

- with also the block method,
- but without modify the geometry.

Like other SALOME components, HEXABLOCK can also be used in two ways:

- by using Graphic User Interface,
- by writing Python Script.

## Stages to obtain hexahedral mesh

HEXABLOCK component enables to define a mesh with hexahedra in 5 stages:

- [Import or build a geometry without constraint](cad.md)
- [Build a model of blocks](block_method.md)
- [Associate this model of blocks with the geometry](intro_association.md)
- [Define the groups on the model of blocks](intro_groups.md)
- [Generate the hexahedral mesh](intro_mesh.md)

- [Example: Python script for a connecting rod](intro_python.md)
- [Appendix: naming rule to find elements in an hexahedron](annexe.md)
