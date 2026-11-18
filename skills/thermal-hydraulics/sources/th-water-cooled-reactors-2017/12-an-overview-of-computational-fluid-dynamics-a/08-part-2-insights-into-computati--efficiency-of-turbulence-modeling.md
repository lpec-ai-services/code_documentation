# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD applications to nuclear thermal fluids problems — Efficiency of turbulence modeling
<!-- source PDF pages 73-77 -->

<!-- page 801 (PDF 73) -->
This behavior of SAS is ideal for many technical applications, as flows for which the
model produces steady solutions are typically those where a well-calibrated RANS
model can produce accurate results.
Contrary to DES, SAS cannot be forced to go unsteady by grid refinement.
SAS has the advantage of being relatively “safe” as it has a RANS fall-back
position in case of overly coarse grids/time steps or insufficient flow instability.
This is not the case with the DES model, which introduces a grid dependency into
the RANS portion of the model to ensure an LES mode under certain conditions.
On the other hand, DES models can more easily be forced into unsteady mode
which can be of significant advantage for otherwise stable flows.

##### Note

However, it has been shown in many simulations, such as the backstep simulation, that
enforcing unsteadiness by grid refinement requires an in-depth understanding of the
flow, the turbulence model, and its interaction with the grid in order to produce
reliable results. Nevertheless, there will be cases where the grid sensitivity of DES
will be advantageous, as it allows unsteady simulations where SAS might produce
a steady-state flow field.

##### Variants of SAS

Several SAS models were developed:
l
Original SAS model.
l
SST-SAS model.
l
k-epsilon SAS model.

### 12.9.6 Efficiency of turbulence modeling

Computational power has dramatically increased over the last few decades.
A consequence of this is the rapid increase in the size of subsequent datasets, with
unsteady 50–100 million point grid simulations now being conducted with increasing
regularity (Sagaut and Deck, 2009).
General estimation of the computational cost of each turbulence model for a given
Reynolds number is impossible because it depends on the problem (especially geometry
). However, approximate estimation may be possible. Regarding computational
efficiency, the following issues are evident:
l
High-level turbulence models are more expensive than low-level ones because they contain
more equations to be solved and more parameters to be evaluated. In other words, computational
cost increases with RANS, Hybrid RANS-LES, and LES in that order.
l
In the same context, unsteady turbulence simulation is more expensive than steady turbulence
simulation. This is only valid for RANS-related turbulence models.
l
Wall-resolved near-wall treatments are more expensive than wall-modeled ones.
In addition to turbulence models, the following also affect computational cost:
l
Thermal simulation is more expensive than isothermal simulation because additional energy
equations need to be included.

<!-- page 802 (PDF 74) -->
l
Simulations with lower order schemes are faster than those with higher order schemes.
l
Calculations in structured mesh are faster than those in unstructured mesh.
Table 12.4 shows a comparison of computational cost of turbulence modeling
strategies for flows over an airliner or a car (Spalart, 2000).

#### 12.9.6.1 (U)RANS turbulence modeling

#####  Linear eddy viscosity models (LEVM)

In RANS turbulence closure models, the number of transport equations is a dominant
factor affecting computational cost for the same near-wall treatment. The standard
k-ε model clearly requires more computational effort than the Spalart-Allmaras model
since an additional transport equation is solved. The realizable k-ε model requires only
slightlymorecomputationaleffortthandoesthestandardk-εmodel.However,duetothe
extratermsandfunctionsinthegoverningequationsandagreaterdegreeofnonlinearity,
computations with the RNG k-ε model tend to take 10%–15% more CPU time than with
the standard k-ε model. Like the k-ε models, the k-ω models are also two-equation
models, thus requiring about the same computational effort as k-ε models.

##### LEVM versus NLEVM

The advantage of nonlinear eddy-viscosity model (NLEVM) lies in that, with a
well-developed robust CFD code for the conventional two-equation turbulence
models, it can be readily implemented to simulate complex turbulent flows by merely
adding the nonlinear terms into the expression for the Reynolds stress, without significantly
consuming the CPU (about 10% increase) and losing the computational robustness
(Xu and Ma, 2009).

##### LEVM versus RSM

Compared to k-ε and RNG k-ε models, the Reynolds stress model (RSM) requires
additional memory and CPU time due to an increased number of transport equations.
On average, a calculation using the RSM requires 50%–60% CPU time and 15%–20%
per iteration more than that using the k-ε model (FLUENT, 2006).
Table 12.4 Comparison of turbulence modeling strategies for flows
over an airliner or car (Spalart, 2000)
Strategy
Grid
Steps
Readiness
2D URANS
103.5
3D RANS
3D URANS
103.5
DES
LES
1011.5
106.7
QDNS
107.3
DNS
107.7

<!-- page 803 (PDF 75) -->
##### Near-wall treatment (wall-modeled) versus wall-resolved RANS

Wall-resolved RANS requires much more stringent grid resolution especially for the
wall-normal direction. The viscosity-affected sublayer is a region where effective
transport properties change at a rate typically two or more orders of magnitude faster
than elsewhere in the flow. So, if one adopts the same numerical strategy, a much finer
mesh is required. Consequently, while the viscous-affected sublayer typically
occupies only around 1% of the flow, resolving that region can require between 3
and 300 times as much computational time (depending on the flow problem, the
mathematical model of turbulence, and the type of CFD solver adopted) as would
be required if the mesh density could be kept comparable with that in the fully turbulent
part of the flow (Craft et al., 2006).

##### RANS versus URANS

For the same grids, i.e., the same wall treatment, URANS needs slightly more
computational time because of time advancement, but it is not so critical. For example,
in computational cost estimations for flows over an airliner or car (e.g., see Spalart,
2000), 3D URANS requires more computational steps by 100.5 for the same grids.

##### LES and hybrid RANS-LES

Cost estimates for LES can be found in various references available from the
literature, e.g., Chapman (1979), Reynolds (1990), Spalart (2000), Piomelli and
Balaras (2002), and Piomelli (2008).

##### Core flow region in LES

The cost estimate is based on the consideration that in LES the integral scales of
motion must be accurately resolved. The classical picture of turbulence starts from
a sequence of bifurcations in a laminar flow, each of which renders more eddies of
smaller and smaller scales. The kinetic energy is found to be of the form
E k
ð Þ = Ckε2=3k·5=3f klk
ð
Þ, where length scale 1/k corresponds to the wave number
k, f is a damping function (for high k), and lK is the Kolmogorov length scale, at which
the smallest turbulent eddies dissipate into heat. Most of the kinetic energy is
contained within the (large) integral scales, lI, from which energy is transported by
the cascade process down to the Kolmogorov scales. In most flows, the large-scale
flow forms coherent structures, containing most of the energy, typically spanning a
range of scales from lI to lT where lT is the (intermediate) Taylor scale. These coherent
structures consist of relatively closely bounded vortex filaments that move collectively
in the flow, being responsible for most of the large-scale mixing and dynamics.
Dimensional analysis suggests that lK □ ν3=ε
ð
Þ1=4 and lI=lT □ Re1=2
I
, where ε is the
dissipation; by assuming equilibrium between production, P∝v3
I =lI and dissipation,
it follows that lI=lK = Re3=4
I
. These relations suggest that a DNS will require NDNS □
lI=lK
ð
Þ3 □ Re9=4
I
cells, whereas an LES would only require NLES □ lI=lT
ð
Þ3 □ Re3=2
I
cells. Hence, LES is cheaper than DNS, although still expensive compared to RANS
(Fureby et al., 2008; Fureby, 2009).

<!-- page 804 (PDF 76) -->
##### Region far away from wall in wall-bounded flows

In wall-bounded flows, the integral scale, away from the walls, is proportional to the
boundary layer thickness, δ; a reasonable estimate of the grid spacing in each direction
is then Δxi □ δ=25 □ δ=15. For boundary layer flows, the boundary layer thickness is
represented by δ∝Re·0:2. Thus, the number of grid points required to resolve the
outer layer is proportional to Re0.4 (Piomelli, 2008).

##### Computational cost of outer and inner layers in LES

The cost estimate in LES is shown in Fig. 12.14, in which the CPU time required to
compute a turbulent boundary layer is estimated for three different codes: (1) a
Cartesian code with a staggered, second-order discretization; (2) a colocated
finite-volume code suited for body-fitted grids, also second order in space and time;
and (3) an unstructured, second-order accurate, finite-volume code. The cost per time
step and grid point was measured on an AMD Opteron processor for calculation at a
given Re, and the scaling laws derived above were used to extend the cost estimate to
higher Re. From this figure, one can observe that even at moderate Reynolds numbers
(Re about 104), over 50% of the resources are used to resolve only 10% of the flow. For
Re>5≡104 a vanishing fraction of the grid points is used in the outer layer.
As a consequence of this unfavorable scaling, wall-resolved LES are limited to
very moderate Reynolds numbers. Only if massive computational resources (clusters
with thousands of processors) are available, calculations at Reynolds numbers of
marginal engineering interest (Re around 105) are possible. Resolved LES is clearly
not suitable for designs in which substantially more rapid computation is required, or
to evaluate and compare possible designs within strict time limits, or to study aerodynamic
or geophysical flows at Re=106·109 (Piomelli, 2008).
1 day
10 days
100 days
1000 days
Outer layer, staggered code
Outer layer, finite-volume code
Outer layer, unstructured code
Inner layer, staggered code
Inner layer, finite-volume code
Inner layer, unstructured code
Total, staggered code
Total, finite-volume code
Total, unstructured code
CPU (s)
Re
Fig. 12.14 Cost, in CPU seconds, of the LES of flat-plate boundary layer flow. Calculations
were performed on an AMD Opteron, using two in-house codes and an open source unstructured
one. Actual mileage may vary (Piomelli, 2008).

<!-- page 805 (PDF 77) -->
##### Wall-resolved LES

Assuming that a nested grid system is used, with mesh spacing that increases in all
directions as one moves away from the wall, Chapman (1979) estimates that the
number of points required to resolve the inner layer is proportional to Re1.8
(Piomelli, 2008).

##### Wall-modeled LES

Wall stress models are the least expensive models, in terms of computational requirements
. The cost of this kind scales like the cost of the outer layer, Re0.6. Zonal models
require between 10% and 20% more CPU time for the solution of the boundary-layer
equations, and significantly more memory. The cost of hybrid RANS/LES methods is
higher, since the wall-normal direction must be well resolved (the SA model, for
instance, requires that the first point be at y+□1), so that the number of grid points
in the wall-normal direction is proportional to log(Re), resulting in a cost that scales
approximately like Re0.6 log (Re) (Piomelli, 2008).
In WMLES, the resolution of the outer layer is, in fact, an often overlooked issue.
Bypassing the wall layer is sometimes viewed as justification to use excessively
coarse grids everywhere; however, many of the simulations demonstrate that unless
the integral scale in the outer layer is resolved well, uniformly accurate results cannot
be
obtained.
Several
calculations
(see
e.g.,
Keating
and
Piomelli,
2006;
Radhakrishnan et al., 2006, 2008; Radhakrishnan and Piomelli, 2008) show how grid
sizes greater than δ/15 do not result in grid-dependent results, and often give incorrect
predictions of the Reynolds stresses (Piomelli, 2008).

##### DES

Hutton (2009), after consultation with colleagues who are experienced practitioners of
DES, estimates that a hybrid solution to a problem is of the order of 103–104 times more
expensive than a steady RANS solution. It is difficult to be more precise because the
computational effort depends strongly upon the complexity of the problem, the quality
of the solution sought, and indeed the expertise of the person running the solution.

##### Subgrid-scale (SGS) models

There are many kinds of subgrid-scale models in explicit LES. According to SGS
models selected, computation cost varies. Table 12.5 shows the CPU time used by
various models in a pseudo-spectral channel code, compared to that required by
the Smagorinsky model and by a simulation with no model. The calculation of the
SGS model, for the dynamic eddy viscosity model, requires a small amount of total
CPU time, only 7% more than the Smagorinsky model. As more complex models are
used, however, the calculation of the SGS stresses may require a substantial amount of
CPU time. Two-coefficient models require over 30% of the CPU time only for the
model evaluation. It is not clear whether the benefits gained by such models outweigh
their additional cost.
