# DEFINING VOLUME-COMPOSITION ASSOCIATIONS
<!-- source PDF pages 137-138 -->

<!-- page 137 -->
Chapter 11
DEFINING VOLUME-COMPOSITION
ASSOCIATIONS
Volume-composition associations are defined using the keyword GEOMCOMP.
This stage of the definition is very simple, but two rules must be followed:
• all the volumes must be associated with a composition, except for virtual (fictive) and lattice volumes;
• no volume must be associated with more than one composition.
Volume-composition associations are defined as follows:
GEOMCOMP
name-compo(1)
nb-volu(1)
volu(1)...volu[nb-volu(1)]
...
name-compo(n)
nb-volu(n)
volu(1)...volu[nb-volu(n)]
END_GEOMCOMP
It is also possible to associate one composition to all the volumes of the geometry. In this case, the volumecomposition
association is defined as follows:
GEOMCOMP
name-compo
ALL_VOLUMES
END_GEOMCOMP

<!-- page 138 -->
Defining volume-composition associations for the criticality calculation example
GEOMCOMP
INOX_STEEL 2 3 6
SOLUTION_U 2 5 8
CONCRETE
1 2
AIR
3 1 4 7
END_GEOMCOMP
