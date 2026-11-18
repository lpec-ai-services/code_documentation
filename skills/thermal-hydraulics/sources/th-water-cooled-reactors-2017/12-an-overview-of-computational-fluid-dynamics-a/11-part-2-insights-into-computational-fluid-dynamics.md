# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD coupling
<!-- source PDF pages 78-78 -->

<!-- page 806 (PDF 78) -->
## 12.10 CFD coupling

The following CFD couplings are considered below:
l
Coupling of CFD code with neutron physics codes
l
Coupling of CFD code with structural mechanics codes
l
Coupling CFD with System (SYS TH) codes: porous medium approach
Validation of CFD-type computer codes on separate-effect experiments is discussed
thoroughly in Mahaffy et al. (2007a,b) as already mentioned. The processes of validation
in the context of nuclear reactor simulations are, in majority of cases,
beyond the possibilities of present hardware capabilities if a CFD code is used
alone. Use of a less detailed, less demanding system analysis code to produce initial
and boundary conditions for the CFD code is a practical alternative. Such multiscale
coupling is indispensable in the case of demonstration simulations and, of course,
application of a CFD code to real industrial problems. Moreover, in such problems
it is very frequently necessary to simulate not only thermal hydraulics, but also phenomena
belonging to different fields of physics or even to chemistry. Furthermore,
in this type of multiphysics coupling, problems with different spatial and temporal
scales appear.
General methods of coupling are treated in several books and papers, e.g.,
Zienkiewicz (1984), Hackbush and Wittum (1995), Cadinu et al. (2007), and
Ibrahimbegovic and Markovic (2003). Most generally, couplings are distinguished
between those taking place on the same domain, by changing the differential equations
describing the corresponding physical phenomena (this approach is frequently realized
by means of a single computer code), or coupling on adjacent domains by
matching boundary conditions at their interfaces. In this case, either the models are
combined to produce a comprehensive model for the coupled problem (joint, or simultaneous
solution strategy), or there are modules solving the individual problems, and
Table 12.5 CPU time required by various
SGS models
Model
CPU time
No model
0.93
Smagorinsky
1.00
Dynamic eddy viscosity
1.07
Dynamic mixed
1.11
Lagrangian eddy viscosity
1.21
Lagrangian mixed (one coefficient)
1.28
Lagrangian mixed (two coefficients)
1.31
The CPU time is normalized by that of an LES that used the Smagorinsky
model (Piomelli, 1999).
