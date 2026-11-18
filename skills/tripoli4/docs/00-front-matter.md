# Front matter
<!-- source PDF pages 1-20 -->

<!-- page 1 -->
RAPPORT
CEA-R-6599
CEA-R-6599
ISSN 0429 - 3460
C E A C E N T R E D E P A R I S - S A C L A Y / S A C L A Y
D I R E C T I O N D E S É N E R G I E S
I N S T I T U T D E S S C I E N C E S A P P L I Q U É E S E T
D E L A S I M U L A T I O N P O U R L E S
É N E R G I E S B A S C A R B O N E
D É P A R T E M E N T D E M O D É L I S A T I O N D E S S Y S T È M E S
E T S T R U C T U R E S
 S E R V I C E D ’ É T U D E S D E S R É A C T E U R S E T
D E M A T H É M A T I Q U E S A P P L I Q U É E S
D I R E C T I O N D E S S Y S T È M E S
D ’ I N F O R M A T I O N
CEA / SACLAY 91191 GIF -SUR-YVET TE CEDEX FRANCE
RAPPORT
C E A - R - 6 5 9 9
2025
2025
par
par
Equipe TRIPOLI-4®
Equipe TRIPOLI-4®
C O M M I S S A R I A T À L ’ É N E R G I E A T O M I Q U E
E T A U X É N E R G I E S A L T E R N A T I V E S
DIRECTION DES ÉNERGIES

<!-- page 2 -->
- Rapport CEA-R-6599 -

CEA Centre de Paris-Saclay/Saclay
Direction des Énergies
Institut des Sciences Appliquées et de la Simulation pour les
énergies bas carbone
Département de Modélisation des Systèmes et Structures
 Service d'Études des Réacteurs et de Mathématiques Appliquées

 par

    Equipe TRIPOLI-4®

-
Avril 2025   -

<!-- page 3 -->
RAPPORT CEA-R-6599 – Equipe TRIPOLI-4®

“Guide de l’utilisateur TRIPOLI-4® version 12”

Résumé : TRIPOLI-4® est un code de transport généraliste. Il simule le transport des neutrons,
photons, électrons et positrons par la méthode de Monte-Carlo dans des géométries
tridimensionnelles. Les domaines d'application principaux sont la radioprotection, la sûreté-
criticité, la physique des réacteurs (y compris l'évolution à partir de la version 10) et
l'instrumentation. TRIPOLI-4® est compatible avec les bibliothèques de sections efficaces
ponctuelles au format ENDF/B en provenance des évaluations JEF2, ENDF/B-VI, JEFF3,
ENDF/B-VII, JENDL3, ENDF/B-VIII, JENDL4, etc. Pour les neutrons thermiques le modèle gaz
libre comme les S(alpha, béta) sont disponibles. Des méthodes performantes et automatisées de
réduction de variance permettent de traiter des problèmes présentant de très fortes atténuations de
flux. Grâce à un mode parallèle à la fois robuste et performant, des simulations sur plusieurs
processeurs sont aisément conduites sur des machines massivement parallèles. Des outils d'aide
au diagnostic, graphiques et algorithmiques, permettent de corriger rapidement les jeux de données
erronés. TRIPOLI-4® dispose d'une base de V&V étendue, tant en comparaison calcul-calcul que
calcul-mesure. C'est un outil qualifié pour la R&D, l'enseignement et l'industrie.

RAPPORT CEA-R-6599 – Equipe TRIPOLI-4®

“TRIPOLI-4® version 12 user guide”

Abstract : TRIPOLI-4® is a general-purpose particle-transport code. It simulates the transport of
neutrons, photons, electrons, and positrons using the Monte Carlo method in three-dimensional
geometries. Its main application areas are radiation shielding, criticality safety, reactor physics
(including depletion calculations, since version 10), and nuclear instrumentation. TRIPOLI-4® is
compatible with continuous-energy cross-section libraries in ENDF/B format from several
evaluations, encompassing JEF2, ENDF/B-VI, JEFF3, ENDF/B-VII, JENDL3, ENDF/B-VIII, or
JENDL4. For thermal neutrons, both the free gas and S(alpha, beta) models are available. Powerful
and automated variance reduction methods allow handling configurations with very high flux
attenuations. Thanks to a robust and efficient parallel mode, simulations with multiple processors
can be easily run on massively parallel machines. Graphical and algorithmic diagnostic tools allow
for the fast correction of mistakes in user data files. TRIPOLI-4® has an extensive V&V database,
both for code-to-code and code-to-measurement comparisons. It is a qualified tool for R&D,
education, and industry.

2025 – Commissariat à l’Énergie Atomique et aux Énergies Alternatives – France

<!-- page 4 -->
Contents
1
GENERALITIES
20
1.1
General description of the code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
1.2
Purpose of this document . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
1.3
Execution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
1.4
Displaying physical units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
1.5
Version number . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
1.6
Verification and Validation tool VALJEAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
2
CROSS-SECTIONS
24
2.1
Nuclear data file names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
2.2
Optimizing cross-section use . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
3
DEFINING PATH AND DICTIONARY FILES
26
3.1
The path file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.1.1
Legacy format
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.1.2
New format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.2
The dictionary file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
4
GENERAL CONSIDERATIONS : DATA, CONVENTIONS, UNITS, FRAMES
31
4.1
The default units
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
4.2
Unit changes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
4.3
Conventions used in this manual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
4.4
Character style conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
4.5
Defining frames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
4.6
List layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
4.7
List of calculation commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
5
EXAMPLE
42
6
USING COMMENTS AND INSERTING FILES
44
6.1
Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
6.1.1
Comments using COMMENT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
6.1.2
C type comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
6.1.3
C++ type comments
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
6.1.4
Restrictions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
6.2
Inserting files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45

<!-- page 5 -->
7
GEOMETRY DEFINITIONS
46
7.1
Geometrical accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
7.2
Global structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
7.3
Different ways to define volumes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
7.3.1
Combinatorial geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
7.3.2
Surface-based geometry
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
7.3.3
Definition using a rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
7.3.4
Defining a lattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
7.3.5
Redefining a cell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
7.3.6
Operators, virtual volumes, and syntax for a volume
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
7.4
Defining a type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
7.4.1
Spheres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
7.4.2
Boxes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
7.4.3
Cylinders parallel to an axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
7.4.4
Generic cylinders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
7.4.5
Cones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
7.4.6
Generic parallelepipeds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
7.4.7
Hexagonal prisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
7.4.8
Tori . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
7.5
Surface data definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
58
7.5.1
Plane parallel to (OY,OZ)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
59
7.5.2
Plane parallel to (OX,OZ)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
59
7.5.3
Plane parallel to (OX,OY) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
59
7.5.4
Generic planes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
7.5.5
Spheres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
7.5.6
A cylinder that is parallel to axis OX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
7.5.7
A cylinder that is parallel to axis OY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
7.5.8
A cylinder that is parallel to axis OZ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
7.5.9
A cylinder with a generic axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
7.5.10 A cone whose axis is parallel to axis OX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
7.5.11 A cone whose axis is parallel to axis OY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.5.12 A cone whose axis is parallel to axis OZ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.5.13 A cone with a generic axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.5.14 An elliptic torus
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
7.5.15 Generic quadratic surface
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
64
7.5.16 Surface transformation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
64
7.6
Defining simple volumes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
7.6.1
Defining simple volumes using predetermined types
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
7.6.1.1
Sphere, cylinder with axis parallel to Ox, cylinder with axis parallel to Oy, cylinder with axis
parallel to Oz, box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
7.6.1.2
Cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
7.6.2
Defining simple volumes using surfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
7.7
Defining rotation type volumes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
69
7.8
Defining operators related to volumes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
7.8.1
The SMASH operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
71
7.8.1.1
Properties of SMASH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
7.8.1.2
The SMASH operator and virtual volumes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
7.8.1.3
Rotation and operator SMASH
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73
7.8.2
The VMINUS operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73

<!-- page 6 -->
7.8.2.1
Restrictions on the SMASH and VMINUS operators . . . . . . . . . . . . . . . . . . . . . . . . . .
75
7.8.2.2
Transitivity, link with the SMASH and FICTIVE operators . . . . . . . . . . . . . . . . . . . . . .
76
7.8.3
The INTE Operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
7.8.4
The UNION Operator
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
7.9
Operator priority
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
7.9.1
Prioritization of VMINUS, INTE, and UNION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
7.9.2
Prioritization of (INTE, UNION, VMINUS), and SMASH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
7.10 Defining a lattice
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
7.10.1 The concept of lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
7.10.2 Syntax
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
82
7.10.3 Lattice restrictions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
7.10.4 Lattices and the SMASH operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
84
7.10.5 Cell numbering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
84
7.10.6 Lattice of lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
86
7.10.7 Volume definitions based on cells
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
87
7.10.7.1
Replacing a volume of a cell
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
87
7.10.7.2
Replacing a cell of a lattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
87
7.10.7.3
Replacing a sub-cell of a lattice of lattices
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
89
7.10.7.4
Replacing a cell using EXCEPT and VOL_EXCEPT . . . . . . . . . . . . . . . . . . . . . . . . . .
91
7.10.8 The virtual cell trick
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
99
7.11 Copies of volumes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
7.12 2D-view display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
7.12.1 Choice of colors
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
7.12.2 2D-cross sectional graph request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
7.13 Geometry Checks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7.13.1 Combinatorial geometry checks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7.13.2
Requesting Checks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7.13.3 1D scan of geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
7.13.4 1D scan of geometry-composition association . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
7.13.5
Requesting Checks Using Tracking Routines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
7.14 Influence of data input on calculation time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.14.1 Connectivity maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.14.1.1
Usage
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.14.1.2
Map Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
7.14.2 Surface-based geometries
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
7.14.3 Combinatorial geometries
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
8
THE VOLSURF COMMAND
118
9
BOUNDARY CONDITIONS
120
9.1
Defining boundary conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
9.1.1
Leakage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
9.1.2
Reflection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
9.1.3
Albedo
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
9.1.4
Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
9.1.5
Rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
9.1.6
Cosine
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
9.2
Sequence of instructions
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
9.3
Additional boundary surfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

<!-- page 7 -->
10 DEFINING COMPOSITIONS
126
10.1 Pointwise cross-sections in ENDF format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
10.1.1 Defining compositions by supplying the number of atoms per 1e-24 cm3
. . . . . . . . . . . . . . . . . . 128
10.1.2 Defining compositions by entering the density (in g/cm3) . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
10.2 Multigroup homogenized cross-sections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
10.2.1 Self-shielded homogenized multigroup cross-sections from APOLLO2 and TRIPOLI-4®
. . . . . . . . . . 131
10.3 Multigroup Cross-Sections in GENDF Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
10.4
TRIPOLI-4®-NJOY Coupling
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
11 DEFINING VOLUME-COMPOSITION ASSOCIATIONS
136
12 DEFINING SOURCES
138
12.1 Defining a source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
12.2 Spatial distribution
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
12.2.1 Point sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
12.2.2 Distributed sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
12.2.2.1
Definition context . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
12.2.2.2
Syntax for a factorized source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
12.2.2.3
Surface, analytical and tabulated distributions
. . . . . . . . . . . . . . . . . . . . . . . . . . . 144
12.3 Angular distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
12.3.1 Dirac . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
12.3.2 Uniform distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
12.3.3 Ray distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
12.3.3.1
Discrete mu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
12.3.3.2
Discrete phi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
12.3.4 Tabulated distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
12.3.4.1
Mu tabulated distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
12.3.4.2
Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
12.3.4.3
Phi tabulated distribution
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
12.3.4.4
Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
12.3.5 2D Tabulated distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
12.3.5.1
Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
12.3.6 Analytical distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
12.4 Energy distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
12.4.1 Dirac . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
12.4.2 Line spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
12.4.3 Uniform distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
12.4.4 Gauss spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
12.4.5 Watt spectrum
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
12.4.6 Maxwell spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
12.4.7 Tabulated spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
12.4.8 Analytical distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
12.4.9 Fission spectrum from the evaluation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
12.5 Time distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
12.5.1 Dirac . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
12.5.2 Uniform distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
12.5.3 Gauss distribution
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
12.5.4 Tabulated distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
12.5.5 Analytical distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
12.6 Sources taken from source files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169

<!-- page 8 -->
12.6.1 Volume particle sources
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
12.6.2 Surface particle sources
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
12.6.2.1
Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
12.6.2.2
Zooming approach principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
12.6.2.3
Parallel mode
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
12.7 Complete source examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
12.7.1 Isotropic point source with no time dependence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
12.7.1.1
Line spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
12.7.1.2
Interpolated spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
12.7.2 Distributed isotropic source without time dependence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
12.8 External sources
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
12.8.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
12.8.2 Example
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
12.9 Multi-particle sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
12.9.1 Uncorrelated source particles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
12.9.2 Correlated source particles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
12.10Sources for activation calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
12.11GEANT4 particle sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
12.12Spontaneous fission sources with the FIFRELIN fission model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
13 DEFINING RESPONSE TYPES
189
13.1 The available responses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
13.2 Additional data for reaction rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
13.3 Sum of reaction rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
13.4 DATA additional data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
13.5 Additional data for a weighted current . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
13.6 Macroscopic reaction rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
13.7 Deposited energy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
13.7.1 Reaction Q-values for energy deposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
13.7.2 Fission energy
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
13.8 Kinematic limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
13.9 DPA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
13.10Gas production
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
13.11Fission spectrum
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
13.12Fixed source emission . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
13.13Deposited charge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
13.14Special option to except a part of the contribution for secondary particles . . . . . . . . . . . . . . . . . . . . . . . 209
14 DEFINING GRIDS
211
15 DEFINING SCORES
214
15.1 Notes regarding score definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
15.2 Standard Monte Carlo estimators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
15.2.1 Volume-based estimators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
15.2.2 Surface-based estimators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
15.3 Next-event estimators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
15.3.1 Point-based estimators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
15.3.2 Surface-based estimators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
15.3.3 Remarks
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
15.4 Variance evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

<!-- page 9 -->
15.5 Geometrical elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
15.6 Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
15.7 Defining the score . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
15.8 Extended meshes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
15.8.1 Uniform window syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
15.8.2 Nonuniform window syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
15.8.3 Variance reduction and TRACK estimators
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
15.8.4 Note on COLLISION estimator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
15.8.5 Note on mesh edition results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
15.9 Examples of score requests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
15.9.1 Example on a simple geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
15.9.2 Using the keyword ENTROPY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
16 DEFINING SCORES DECOMPOSED OVER REAL SPHERICAL HARMONICS
235
17 VARIANCE REDUCTION TECHNIQUES (BIASING)
238
17.1 The concept of a weight . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
17.2 Spatial biasing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
17.2.1 Biasing energy groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
17.2.2 Detectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
17.2.3 Calculation of spatial importance
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
17.2.3.1
For biasing with discrete detectors
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
17.2.3.2
For an analytical biasing (plane, cylindrical, or spherical) . . . . . . . . . . . . . . . . . . . . . 244
17.2.3.3
For biasing with a splitting sphere . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
17.2.4 Mesh and importance maps in TRIPOLI-4® . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
17.2.4.1
Cartesian mesh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
17.2.4.2
Cylindrical mesh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
17.2.4.3
Refining the mesh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
17.2.4.4
Uniform mesh syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
17.2.4.5
Nonuniform mesh syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
17.2.5 Bias parameter k . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
17.2.6 Smoothing option . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
17.3 Directions of interest . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
17.4 Energy biasing
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
17.5 Time biasing
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
17.6 Special biasing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
17.6.1 Splitting when entering specific volumes VOLUME_SPLITTING . . . . . . . . . . . . . . . . . . . . . . . . 253
17.6.2 Optical biasing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
17.6.3 Russian roulette control
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
17.6.4 Special source biasing
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
17.7 Variance reduction techniques for coupled neutron photon simulations . . . . . . . . . . . . . . . . . . . . . . . . 255
17.8 Graphical display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
17.9 Hints concerning biasing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
17.9.1 Hints concerning Inipond module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
17.9.1.1
The automatic case
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
17.9.1.2
Mesh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259

<!-- page 10 -->
18 THE ADAPTIVE MULTILEVEL SPLITTING VARIANCE REDUCTION TECHNIQUE
261
18.1 SYNTAX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
18.2 TARGET DEFINITON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
18.2.1 SINGLE TARGET . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
18.2.2 MULTIPLE TARGETS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
18.2.3 SCORING OUTSIDE TARGETS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
18.3 SPLITTING PROPORTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
18.4 AMS OPTIONS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
18.4.1 CROSSING POINTS SPLITTING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
18.4.2 COLLISION RESAMPLING
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
18.5 IMPORTANCE FUNCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
18.5.1 Importance maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
18.5.2 SPATIAL IMPORTANCES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
18.5.2.1
POINT
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
18.5.2.2
LINE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
18.5.2.3
PLANE
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
18.5.2.4
SPHERE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
18.5.2.5
CYLINDER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
18.5.2.6
RING
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
18.5.2.7
PATH
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
18.5.2.8
VOLUME IMPORTANCE WEIGHTING
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
18.6 RELATED OPTIONS IN OTHER COMMAND BLOCKS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
18.6.1 ANALOG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
18.6.2 MONITORING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
18.6.3 SMOOTHING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
18.7 RESTRICTIONS AND FORBIDDEN OPTIONS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
19 THE WEIGHT WINDOWS VARIANCE REDUCTION TECHNIQUE
270
19.1 SYNTAX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
19.2 WEIGHT WINDOWS FILE SYNTAX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
19.3 SPECIFIC SYNTAX WHEN DATA ARE PROVIDED BY ADVANTG CODE
. . . . . . . . . . . . . . . . . . . 273
19.4 OTHER RELATED SIMULATION OPTIONS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
20 THE CADIS VARIANCE REDUCTION TECHNIQUE
274
20.1 Principle of the CADIS method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
20.2 Modelling and approximations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
20.3 Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
20.3.1 IDT parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
20.3.1.1
TARGET keyword . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
20.3.1.2
SPECTRUM keyword
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
20.3.1.3
CONVERGENCE keyword
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
20.3.1.4
MICROSCOPIC_CROSS_SECTIONS block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
20.3.2 Other keywords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
20.4 Caveats
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
20.5 Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
21 THE HOMOGENIZATION COMMAND
284

<!-- page 11 -->
22 DEFINING NUMERICAL SIMULATION PARAMETERS
286
22.1 Simulation parameters
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
22.2 Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
22.3 Option KEEP_RESULT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
22.4 Option XML_EXPORT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
22.5 Option RANDOM
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
22.6 Computing the kinetics parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
22.7 Neutron importance (critical adjoint flux)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
22.8 Critical parameter search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
22.8.1 Albedo search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
22.8.2 Boron search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
22.9 Slowing down current . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
22.10Six factor formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
22.11Diven dispersion factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307
22.12DYNAMIC (time-dependent simulation) options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
22.12.1 Time mesh for forced precursor decay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310
22.12.2 Population control
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
22.12.2.1 Russian roulette & splitting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
22.12.2.2 Combing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
22.12.3 Time mesh for scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
22.12.4 Relative particle importance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
22.12.5 Critical source
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313
22.12.6 Adjusting the reactivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
22.12.7 Changing geometries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
22.12.8 Branchless collisions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
22.13EPITHERMAL BROADENING options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
22.13.1 SVT model with a different threshold energy E_threshold
. . . . . . . . . . . . . . . . . . . . . . . . . . 316
22.13.2 Doppler Broadening Rejection Correction (DBRC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
22.13.3 Weight Correction Method (WCM)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 318
22.14Electromagnetic shower options
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
22.15Option PHOTON_NEUTRON_RATIO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
22.16Option ALL_COLLIDED_FLUX_PT_POINTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
22.17Option SUPER_HISTORY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321
22.18Option WIELANDT_METHOD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
22.19The MULTIPLE simulation mode (neutronics-shielding coupling) . . . . . . . . . . . . . . . . . . . . . . . . . . . 323
22.19.1 Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 323
22.19.2 Principle
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 323
22.19.3 History of the multiple simulation mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 323
22.19.4 Syntax
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324
22.20Storage of particle events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
22.21Counting holes within the simulation options
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
22.21.1 Options HOLE_COUNT, HOLE_MAP, HOLE_VOLU_MAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
22.21.2 Procedure for testing geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326
23 CALCULATION VERIFICATION DEFINITIONS
329
23.1 Volume calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329
23.2 Density calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
23.3 MASS calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332

<!-- page 12 -->
24 KIJ MATRIX CALCULATION
335
24.1 Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 335
24.2 Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336
25 DISPLAY OF COLLISIONS SITES
337
25.1 Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
25.1.1 Types of particles
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338
25.1.2 Variation of the parameter height . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339
25.1.3 Display for “full” 2D-views or contour-2D-views of the geometry . . . . . . . . . . . . . . . . . . . . . . 339
25.1.4 Option DISCARD
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
25.1.5 Options SCORE and SCORE_SEGMENTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
25.1.6 Option SOURCE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
25.1.7 Option NB_COLLISION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
25.1.8 Optional definitions for an energy grid and related colors . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
25.1.8.1
Definition of an energy grid, keyword GRID : . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
25.1.8.2
Color definition, keyword COLOR :
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
25.2 Order of apparition for the display windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
25.3 Number of particles in the simulation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
25.4 Number of projected points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
26 THE OUTPUT FILE
343
26.1 Printing out the output file
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
26.2 When a variance reduction technique is used . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
26.3 Outputs relating to sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
26.4 Outputs for each batch
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346
26.5 Complete outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346
26.6 Criticality calculations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346
26.7 Sub-criticality calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
27 STORING PARTICLES
348
28 DEFINING PERTURBATIONS
351
28.1 General . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351
28.2 Data on a perturbation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351
28.3 Density and concentration perturbations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352
28.4 Partial cross-section perturbation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354
28.4.1 Syntax
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354
28.4.2 The carry-over file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 356
28.5 Covariance perturbations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 359
29 STANDARD PERTURBATION THEORY
361
29.1 Reactivity perturbations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 361
29.1.1 Iterated Fission Probability Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 362
29.1.2 Wielandt Syntax
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366
29.1.3 Super-History Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367
29.2 k-eigenvalue sensitivity coefficients
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 369
29.2.1 Iterated Fission Probability Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370
29.2.2 Wielandt Syntax
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
29.2.3 Super-History Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376
29.2.4 Comments
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377

<!-- page 13 -->
30 GENERALIZED PERTURBATION THEORY
378
30.1 Reaction rate ratio sensitivity coefficients
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 378
30.1.1 Super-History Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 379
30.2 Limitations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 381
31 SPECIAL OUTPUTS
383
31.1 XVGR plots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383
31.2 Cross-section data and plots
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 385
31.3 Information on simulated nuclei
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
31.4 T4G dedicated outputs
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
31.4.1 Mesh outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
31.4.2 Point event outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387
32 CONNECTION WITH THE DARWIN/PEPIN2 CODE
389
33 PARALLELISM
391
33.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 391
33.2 Launching tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
33.2.1 Mpirun or Srun tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
33.2.2 Lpar* tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 394
33.3 The parallelism file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 394
33.3.1 Heterogeneous clusters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
33.3.2 Calculation on a machine with a resource manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395
33.3.2.1
Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396
33.3.2.2
Advices regarding execution
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396
33.4 Differences between DISCARD processing in mono-processor and parallel calculations . . . . . . . . . . . . . . . 397
33.5 Incompatibilities
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398
34 COLLISION FILES
399
34.1 Creation of a collision file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 400
34.2 Use of a collision file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401
35 GREEN’S FUNCTION FILES
402
35.1 Objective
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402
35.2 Principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402
35.3 Limitations and hypotheses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403
35.4 Command structure for user data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404
35.4.1 Creation phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404
35.4.2 Exploitation phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 405
35.5 Use of parallelism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
35.6 Aspect of the output file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
35.6.1 Creation phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
35.6.2 Exploitation phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
35.7 Incompatibilities
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 408
36 TRIPOLI-4/ROOT COUPLING
409
36.1 Installation procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
36.2 Using a ROOT geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
36.2.1 Defining the geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 409
36.2.1.1
Defining the geometry via a file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 410

<!-- page 14 -->
36.2.1.2
Defining the geometry directly in C++ or Python code . . . . . . . . . . . . . . . . . . . . . . . 411
36.2.2 Defining boundary conditions
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412
36.2.3 Defining a score
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412
36.2.4 How to check a ROOT geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 413
36.2.5 Caveat: use of overlapping nodes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 413
36.2.6 Example
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 413
36.3 ROOT post-processing: recording particle tracks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417
37 ENERGY CUT PER VOLUME
418
38 VISUALIZER T4G
420
38.1 Introduction to T4G . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 420
38.2 How to launch T4G . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 421
38.3 2D visualization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
38.3.1 Geometry retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
38.3.1.1
"Pursuit" mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
38.3.1.2
"Position" mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
38.3.1.3
"Contours" mode
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
38.3.2 Display of the color policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423
38.3.2.1
"Volumes values" file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 424
38.3.2.2
"Colors" file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
38.3.3 Tripoli-4 scores, meshes and points plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
38.3.3.1
Scores plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426
38.3.3.2
Meshes plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 427
38.3.3.3
Points plot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 428
38.3.4 Window . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
38.3.4.1
Definition
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
38.3.4.2
Default window . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
38.3.4.3
Command line option . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
38.3.4.4
Window file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
38.3.5 Available keys in 2D mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430
38.4 3D visualization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
38.4.1 Launch 3D visualization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
38.4.2 Basic features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
38.4.2.1
Exclusion of volumes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
38.4.2.2
Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
38.4.3 Hiding a part of a Root geometry with a simple Tripoli-4 geometry
. . . . . . . . . . . . . . . . . . . . . 434
38.4.4 View and screen
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436
38.4.4.1
View . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436
38.4.4.2
Screen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436
38.4.5 Available keys in 3D mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
38.5 Configuration files
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
39 T4TOMED TOOL
440
39.1 Starting with T4toMED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
39.1.1 How to launch T4toMED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
39.1.2 T4toMED options
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440
39.1.3 Particular data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441

<!-- page 15 -->
40 DEPLETION CALCULATION
443
40.1 Depletion calculation input file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443
40.1.1 TRIPOLI-4 input file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443
40.1.2 Energy grids file
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 454
40.1.3 Initial compositions file
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 454
40.1.4 Irradiation history file
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 454
40.2 Launching independent simulations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
40.3 Restart calculation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 456
40.4 Using the source from the previous depletion step . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
40.5 Results and post-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
40.5.1 Content of the output directory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 457
40.5.2 Content of the ROOT output file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458
40.5.3 Post-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 460
40.5.3.1
Post-processing a unique ROOT output file using BurnupResults class
. . . . . . . . . . . . . . 460
40.5.3.2
Post-processing several ROOT output files using the MeanBurnupResults class . . . . . . . . . . 463
40.5.3.3
Producing TRIPOLI-4 composition files from ROOT outputs
. . . . . . . . . . . . . . . . . . . 466
41 ACTIVATION CALCULATION
468
41.1 Input for an activation calculation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
41.1.1 TRIPOLI-4 input file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
41.1.2 Homogenized cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 471
41.2 Calculation steps
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 472
41.2.1 Step 1: activation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 472
41.2.2 Step 2: photon transport
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 472
41.2.3 Parallelization of the activation calculation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474
41.2.4 Content of the ROOT output file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474
41.3 Uncertainties
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 476
42 TRIPOLI-4/GEANT4 COUPLING
478
42.1 Requirements on the GEANT4 compilation phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478
42.2 Using GEANT4 geometries in TRIPOLI-4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478
42.2.1 Wrapping a GEANT4 geometry with g42so . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479
42.2.2 Building the geometry wrapper by hand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
42.2.3 Declaring the GEANT4 geometry in the TRIPOLI-4 input file . . . . . . . . . . . . . . . . . . . . . . . . . 481
42.3 Visualizing the geometry with T4G . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482
42.4 Physics coupling
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482
42.4.1 Syntax
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 483
42.5 Using GEANT4 particle sources in TRIPOLI-4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 483
42.5.1 Wrapping a GEANT4 source with g42so
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
42.5.2 Building the source wrapper by hand
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
42.5.3 Declaring the GEANT4 source in the TRIPOLI-4 input file . . . . . . . . . . . . . . . . . . . . . . . . . . 486
42.6 Wrapping sources and geometries in the same shared library . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486
42.7 Scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486
42.8 Support for GEANT4 UI commands
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486
42.9 Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487
43 TRIPOLI-4/MORET COUPLING
489
43.1 Using a MORET geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489
43.2 Using MORET boundary conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490

<!-- page 16 -->
44 SCHEDULER
491
44.1 KIJ acceleration of critical calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492
44.2 Specialised tasks
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493
44.2.1 Cleaning of results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493
44.2.2 Initialising sources from KIJ matrix fundamental . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493
45 GENERATOR OF STOCHASTIC GEOMETRIES (CASTOR)
494
45.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 494
45.2 Construction of random geometries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
45.2.1 Type of geometries (mandatory) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
45.2.2 Number of realizations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496
45.2.3 Container . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496
45.2.4 Coloring probabilities (volume ratios) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 498
45.2.5 Geometrical specifications (tessellation density or radius distribution) . . . . . . . . . . . . . . . . . . . . 499
45.2.5.1
Poisson and Poisson-Box geometries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 499
45.2.5.2
Spherical inclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500
45.2.6 Construction algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500
45.3 Export input files for TRIPOLI-4 and T4G . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 501
45.3.1 Activation and target repository
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 501
45.3.2 Start rank and end rank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502
45.3.3 Name of mixture compositions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502
45.3.4 Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502
45.3.5 Boundary conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 503
45.3.6 Language . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 504
45.3.7 Export for the visualizer T4G
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 504
45.3.8 Connectivity map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505
45.3.9 Mesh (spherical inclusions only) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505
45.4 Export input files for VtK . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
45.4.1 Activation and target repository
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
45.4.2 Start rank and end rank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
45.4.3 Visualization option
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
45.4.4 Resolution of the spheres (spherical inclusions only) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 508
45.5 Statistical properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509
45.5.1 Activation and target repository
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509
45.5.2 Number of test lines
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 510
45.5.3 Options for pre-defined grids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 510
A EXAMPLE OF GEOMETRY
511
A.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511
A.2
A hexagonal and parallelepipedic lattice, a lattice of lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511
A.3
Homogenizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 516
A.3.1
Defining the combinatorial geometry of a homogenizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . 516
A.3.2
Defining the surface-based geometry of a homogenizer . . . . . . . . . . . . . . . . . . . . . . . . . . . . 518
A.4
Transport cask . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 519
A.4.1
Defining the combinatorial geometry of a transport cask
. . . . . . . . . . . . . . . . . . . . . . . . . . . 519
A.4.2
Defining the surface-based geometry of a transport cask
. . . . . . . . . . . . . . . . . . . . . . . . . . . 521
B
DATA ENTRY SEQUENCE
524
C TRANSLATION KEYWORDS
551

<!-- page 17 -->
D BIBLIOGRAPHY
562
E
INDEX
567

<!-- page 18 -->
TRIPOLI-4® Project Team
(in alphabetical order)
CEA : François-Xavier HUGOT, Alexis JINAPHANH, Cédric JOUANNE, Coline LARMIER,
Yi-Kang LEE, Davide MANCUSI, Odile PETIT, Thierry VISONNEAU, Andrea ZOIA

<!-- page 19 -->
MAJOR CHANGES MADE TO THE CODE
WITH RESPECT TO VERSION 11.1.
Important warning:
• The keywords used in the present manual belong to the English dictionary. However, the user must execute the code using
the specific english option (as explained in Chapter 1 of this document) in order for the code to recognize these keywords.
Otherwise, the code still uses the keywords given in the default dictionary (named old).
Generalities (see Chapter 1)
• The -a command-line option is now the default (all score values, even zeros) are printed.
• New command-line options -z and -x.
Geometry (see Chapters 7, 43 and 45)
• Matrices and origin change for surface transformations (see Subsection 7.5.16).
• MORET geometries can be read with minimal changes to data file (see Chapter 43).
• Generator of stochastic geometries (see Chapter 45).
Sources (see Chapter 12)
• New helpers for factorized source descriptions UPTO_LIN and REPEAT (see Subsubsection 12.2.2.3).
Responses and scores (see Chapters 13, 15 and 16)
• ZA distribution of fission products (see Section 13.1).
• Scores decomposed over real spherical harmonics, for needs of deterministic codes (see Chapter 16).
• Change of method for evaluating variances (see Section 15.4).
Variance Reduction Techniques (see Chapters 17, 19 and 20)
• Weight Windows (see Chapter 19).
• CADIS method (see Chapter 20).
Simulation options (see Chapter 22)
• Kinetic simulation mode (DYNAMIC option) (see Section 22.12).
• Wielandt method for criticality calculations (see Sections 22.1 and 22.18).
• Super-history method for criticality calculations (see Sections 22.1 and 22.17).
• Temperature stochastic interpolation available also with probability tables (see Section 22.1).
• Multiple mode (for subcritical or critical configurations) with AMS variance reduction technique (see Section 22.19).
• Inelastic threshold correction (see Section 22.1).

<!-- page 20 -->
• New version 2.0.5 of the external LLNL fission library as fission model, to be used when requesting the new ZA
distribution feature (see Section 22.1).
• K-th collision histories for partial contribution to the scores up to the k-th collision source (see Section 22.1).
• SUPPRESS_MESH_EDITION_TEXT option for mesh tallies edition (see Section 22.1).
Depletion (see Chapter 40)
• Allow normalization of power on a list of compositions or volumes and not only to the total.
Perturbations and sensitivities (see Chapters 29 and 30)
• Standard Perturbation Theory using history-based (Super-History or Wielandt) methods to reduce the memory occupation
(see Chapter 29).
• Creation of default keywords to compute sensitivities for all nuclides for a list of reactions (see Section 29.2.1).
• Generalized Perturbation Theory for a reaction rate ratio using the Super-History simulation mode (see Chapter 30).
Parallelism (see Chapter 33)
• Cluster mode is now by default (mandatory use of mpirun or compatible launchers, see Section 33.2)
• Launcher to simplify launch in parallel (lparm tool, see Section 33.2)
• New command-line options -S (load balancing in parallel), -E (shorten simulator output files) and -M (tune the size of
TCP packets in communications, for all options see Section 33.1)
Graphical tools (see Chapter 25 and 38)
• New T4G options mainly on meshes (see Chapter 38)
• New default in the collision sites feature: the maximum number of simulated particles for this graphical option is now
10000 (instead of 1000), unless the option for memory management MAXP_FOR_COLLISION_SITES is activated (see
Section 25.3).
Verification and validation (see Chapter 1)
• Tool for verification and validation (see Section 1.6)
