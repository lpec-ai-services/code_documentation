# EXAMPLE OF GEOMETRY
<!-- source PDF pages 512-524 -->

<!-- page 512 -->
Appendix A
EXAMPLE OF GEOMETRY

## A.1 INTRODUCTION

This appendix presents a case with geometry developed using the available lattice functionality: a hexagonal
lattice with modification of the cells, included in a parallelepipedic lattice cell, in order to illustrate calculations
relating to a lattice of lattices. The construction is described step-by-step to show the different stages
involved.
Two other examples of relatively complex geometry are described in this appendix:
• a homogenizer:
– surface-based geometry,
– combinatorial geometry.
• an eighth of a transport cask cylinder:
– surface-based geometry,
– combinatorial geometry.

## A.2 A HEXAGONAL AND PARALLELEPIPEDIC LATTICE, A LATTICE OF LATTICES

The geometry is shown on the following page.

<!-- page 513 -->
Figure A.1: Geometry of Case 2

<!-- page 514 -->
The first step consists in constructing the basic parallelepipedic cell:
TYPE 100 BOX 15 15 3
// Basic cell of the
parallelepipedic lattice
VOLU 100 COMBI 100 0 0 0 ENDV
Then two concentric cylinders are created
TYPE 101 CYLZ 7 1
TYPE 102 CYLZ 6 1
// Cylinders
VOLU 101 COMBI 101 0 0 0 SMASH 1
100 ENDV
VOLU 102 COMBI 102 0 0 0 SMASH 1
101 ENDV
Then the hexagonal cell is created
TYPE 1 HEXAZ 1 1 0
// Hexagonal cell
VOLU 1 COMBI 1 0 0 0 SMASH 1 102
ENDV
This cell itself contains a hexagonal prism

<!-- page 515 -->
TYPE 2 HEXAZ 0.4 0.4 0
// Volume included in the
hexagonal cell
VOLU 2 COMBI 2 0 0 0 SMASH 1 1
ENDV
It is now possible to create the hexagonal lattice. Since it is to be centered on (0,0,0), it is sufficient to declare
that the basic cell is the cell (6,6,1)
VOLU 3 RESH VOLU 1 6 1
BASIS 6 6 1
ENDV
It is only the complete cells that are actually wanted; therefore, option MATCH needs to be used. It should be
noted that the lattice cannot override volume 102 (incompatible with option MATCH).
VOLU 3 RESH VOLU 1 6 1
BASIS 6 6 1
MATCH
ENDV
It is necessary to individualize the cell (3,2,1) using option CELL. It has to be declared that the cell overrides
102, as we want to create a lattice of lattices.

<!-- page 516 -->
VOLU 4 CELL 3 2 1
LATTICE 3 REPLACE 1
SMASH 1 102
ENDV
The lattice of lattices is now created. The basic cell is the central cell (2,2,1).
VOLU 1000 RESC
VOLU 100 3 3 1
BASIS 2 2 1
ENDV
Cell (4,3,1) is then excluded from the hexagonal lattice in cell (3,1,1) of the square lattice using the option
LOWER_CELL.
VOLU 40 LOWER_CELL DEPTH 2
LATTICE 3 VOLU 1 CELL 4 3 1
LATTICE 1000 VOLU 100 CELL 3 1 1
ENDV
Display and creation of a captionless encapsulated PostScript file is obtained by:
GRAPH
-25 -25 0
1 0 0
0 1 0
50 50
4

<!-- page 517 -->
## A.3 HOMOGENIZER

### A.3.1 DEFINING THE COMBINATORIAL GEOMETRY OF A HOMOGENIZER

-9
-6
-5
10
2.5
9
6
5
-2.5
-5.5
-7.5
1
1
2
3
4
8
9
7
7
4
3
2
-10
Figure A.2: Homogenizer described using a combinatorial geometry

<!-- page 518 -->
TITLE TEST-GEOM
TYPE 1 CYLZ 10 2.5
TYPE 2 CYLZ 9 2.5
TYPE 3 CYLZ 6 2.5
TYPE 4 CYLZ 5 2.5
TYPE 5 BOX 10 10 10
TYPE 6 CONE 26.565 0 0 1
// Cylinders
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
VOLU 3 COMBI 3 0 0 0 SMASH 2 1 2 ENDV
VOLU 4 COMBI 4 0 0 0 SMASH 3 1 2 3 ENDV
VOLU 5 COMBI 5 0 0 -7.5 FICTIVE ENDV
VOLU 6 COMBI 5 0 0 -7.
FICTIVE ENDV
// Cones
VOLU 7 COMBI 6 0 0 -7.5 10
SMASH 4 1 2 3 4 VMINUS 1 5
ENDV
VOLU 8 COMBI 6 0 0 -5.5 7.5
SMASH 5 1 2 3 4 7 VMINUS 1 6
ENDV
VOLU 9 COMBI 6 0 0 -5.5 6
SMASH 6 1 2 3 4 7 8 VMINUS 1 6
ENDV
GRAPH
-15 1 -3
1 0 0
0 0 1
30 4
0
ENDGEOM

<!-- page 519 -->
-9
-6
-5
10
2.5
9
6
5
-2.5
-5.5
-7.5
1
1
2
3
4
4
3
2
-10
5
5
9
8
6
7
Figure A.3: Homogenizer described using a surface-based geometry

### A.3.2 DEFINING THE SURFACE-BASED GEOMETRY OF A HOMOGENIZER

GEOMETRY
TITLE TEST-GEOM
/*
* homogenizer
*/
SURF 1 CYLZ 0 0 10
SURF 2 PLANEZ 2.5
SURF 3 PLANEZ -2.5
SURF 4 CYLZ 0 0 9
SURF 5 CYLZ 0 0 6
SURF 6 CYLZ 0 0 5
SURF 7 PLANEZ -2
SURF 8 PLANEZ 0.5

<!-- page 520 -->
SURF 9 PLANEZ 2
SURF 10 QUAD 1 1 -0.25 0 0 0 0 0 -3.75 -14.0625
SURF 11 QUAD 1 1 -0.25 0 0 0 0 0 -2.75 -7.5625
VOLU 1 EQUA MINUS 2 1 2 PLUS 2 3 4
ENDV
VOLU 2 EQUA MINUS 2 2 4 PLUS 2 3 5
ENDV
VOLU 3 EQUA MINUS 2 2 5 PLUS 2 3 6
ENDV
VOLU 4 EQUA MINUS 2 2 6 PLUS 2 3 10
ENDV
VOLU 5 EQUA MINUS 2 10 2 PLUS 2 3 11
ENDV
VOLU 6 EQUA MINUS 2 11 2 PLUS 1 9
ENDV
VOLU 7 EQUA MINUS 2 11 7 PLUS 1 3
ENDV
VOLU 8 EQUA MINUS 2 11 8 PLUS 1 7
ENDV
VOLU 9 EQUA MINUS 2 11 9 PLUS 1 8
ENDV
ENDGEOM

## A.4 TRANSPORT CASK

The cask exhibits symmetry, and it is, therefore, possible to only describe one eighth of it.
Note: Although the current geometry makes it possible to construct 1/8 of a cask using combinatorial geometry
, it is not yet possible to associate reflective boundary conditions with it. This is because the surfaces of
the volume thus created result from truncation by operators.

### A.4.1 DEFINING THE COMBINATORIAL GEOMETRY OF A TRANSPORT CASK

GEOMETRY
TITLE TEST-GEOM
COMMENT
transport cask
COMMENT
TYPE 1 BOX 1000 1000 1000
TYPE 2 CYLZ 12 2.5

<!-- page 521 -->
X
Y
3.5
1.5
0.5
6.5
5
9.5
7.5
3.5
14
11
12
8
9
13
10
Figure A.4: Cask described using a combinatorial geometry
TYPE 3 BOX 24 12 5
TYPE 4 CYLZ 1 2.5
TYPE 5 CYLZ 0.5 2.5
TYPE 6 CYLZ 0.3 2.5
TYPE 7 BOX 2 2 5
TYPE 8 BOX 12 1.4 5
TYPE 9 BOX 12 24 5
TYPE 10 BOX 12 12 5
VOLU 1 COMBI 1 0 0 0
ENDV
VOLU 2 COMBI 3 0 -6 0
FICTIVE
ENDV

<!-- page 522 -->
VOLU 3 COMBI 9 -6 0 0
FICTIVE
ENDV
VOLU 4 COMBI 2 0 0 0
VMINUS 2 2 3
FICTIVE
ENDV
VOLU 5 COMBI 8 6 0.25 0
FICTIVE
ENDV
VOLU 6 COMBI 10 6 6 0
FICTIVE
ENDV
VOLU 7 ROTATION VOLU 6 0 0 1 45 0 0 0
FICTIVE
ENDV
VOLU 8 COMBI 8 6 0.25 0
VMINUS 1 7 INTE 2 4 5 SMASH 1 1
ENDV
VOLU 9 COMBI 2 0 0 0
VMINUS 4 2 3 7 8 SMASH 1 1
ENDV
VOLU 10 COMBI 5 9.5 5 0
SMASH 2 1 9
ENDV
VOLU 11 COMBI 7 8.5 2.5 0
SMASH 2 1 9
ENDV
VOLU 12 COMBI 7 2.5 2.5 0
VMINUS 1 7 SMASH 2 1 9
ENDV
VOLU 13 COMBI 4 6.5 6.5 0
VMINUS 1 7 SMASH 2 1 9
ENDV
VOLU 14 COMBI 6 6.5 6.5 0
VMINUS 1 7 SMASH 3 1 9 13
ENDV
ENDGEOM

### A.4.2 DEFINING THE SURFACE-BASED GEOMETRY OF A TRANSPORT CASK

GEOMETRY

<!-- page 523 -->
X
Y
3.5
1.5
0.5
6.5
5
9.5
7.5
3.5
3
4
5
6
2
8
10
7
9
1
Figure A.5: Cask in surface-based form
TITLE TEST-GEOM
// transport cask
SURF 1 CYLZ 0 0 12
SURF 2 PLANY 0
SURF 3 PLAN 1 -1 0 0
SURF 4 PLANY 0.5
SURF 5 PLANY 1.5
SURF 6 PLANY 3.5
SURF 7 PLANX 9.5
SURF 8 PLANX 7.5
SURF 9 PLANX 3.5
SURF 10 CYLZ 9.5 5 0.5
SURF 11 CYLZ 6.5 6.5 1

<!-- page 524 -->
SURF 12 CYLZ 6.5 6.5 0.3
SURF 13 PLANEZ -5
SURF 14 PLANEZ 5
VOLU 1 EQUA MINUS 3 1 4 14 PLUS 3 2 3 13
ENDV
VOLU 2 EQUA MINUS 3 1 5 14 PLUS 3 3 4 13
ENDV
VOLU 3 EQUA MINUS 2 9 14 PLUS 3 3 5 13
ENDV
VOLU 4 EQUA MINUS 3 6 8 14 PLUS 3 5 9 13
ENDV
VOLU 5 EQUA MINUS 3 7 6 14 PLUS 3 5 8 13
ENDV
VOLU 6 EQUA MINUS 3 1 6 14 PLUS 3 7 5 13
ENDV VOLU 7 EQUA MINUS 2 1 14 PLUS 5 6 3 10 11 13
ENDV
VOLU 8 EQUA MINUS 2 10 14 PLUS 1 13
ENDV
VOLU 9 EQUA MINUS 2 12 14 PLUS 2 3 13
ENDV
VOLU 10 EQUA MINUS 2 14 11 PLUS 3 3 12 13
ENDV
ENDGEOM
