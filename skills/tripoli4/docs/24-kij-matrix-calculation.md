# KIJ MATRIX CALCULATION
<!-- source PDF pages 336-337 -->

<!-- page 336 -->
Chapter 24
KIJ MATRIX CALCULATION
The Kij matrix gives the number of neutrons produced by fission in the volume i from a neutron emitted in
the volume j.
His highest eigenvalue is equal to the Keffective of the system and the corresponding eigenvector represents
the neutron sources in the volumes.
Only volumes containing a fissile material are taken into consideration, therefore the size of the matrix is
equal to the number of these volumes.
The calculation is also possible with an EXTENDED_MESH. In this case the size of the matrix is equal to the
number of cells (all cells are taken into consideration even if some of them do not contain any fissile material).
Change warning: Since version 11, an additionnal keyword KIJ_MATRIX must be included in the simulation
block if the Kij matrix is to be calculated. This allows for having multiple simulations, not all having Kij
calculations.

## 24.1 SYNTAX

The general syntax used to define Kij matrix is as follows :
MATRIX
KIJ_MATRIX
EXTENDED_MESH
VTK
Extended mesh definition
END_MATRIX
For the optional definition of an extended mesh, see section 15.8.
The optional keyword VTK allows to get 3D PARAVIEW outputs of the fundamental mode.

<!-- page 337 -->
## 24.2 OUTPUT

A Keffective sensibility matrix is also given in mono-processor mode. The standard deviation of each matrix
coefficient is given in a matrix. Each cell represents by how much the Keffective would be changed if this
cell in the kij matrix were shifted by one standard deviation.
