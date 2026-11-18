# The various approaches to single-phase modeling
<!-- source PDF pages 14-17 -->

<!-- page 180 (PDF 14) -->
One may choose (p, h, Yk=2,n) as independent variables, and the necessary equations
of state are then functions of 2+n−1 state variables:
ρ p,h, Yk=2,n
ð
Þ;T p,h, Yk=2,n
ð
Þ ;μ p,h, Yk=2,n
ð
Þ ;λ p,h, Yk=2,n
ð
Þ

## 5.2.2 Some properties of the local instantaneous equations

It is not yet proven that this set of equations is a well-posed problem as defined by
Jacques Hadamard, which requires three conditions:
1. A solution exists
2. The solution is unique
3. The solution’s behavior changes continuously with the initial conditions
The third condition is directly linked to the predictability of fluid flows since it is
related to the sensitivity to initial conditions. An exponential sensitivity would result
in an ill-posed problem and a high sensitivity may give at least an ill-conditioned
problem.
It is simply “believed” that fluid equations are exact and correspond to a well-posed
problem—even if the demonstration is still open to mathematicians—but it is
observed that turbulence may result in a rather high sensitivity to initial conditions.
It is also observed that macroscopic quantities (time averaged, space averaged, or
space-time averaged quantities) have a lower sensitivity to initial conditions. This
opens the possibility to predict macroscopic fluid flow parameters using averaged
balance equations.
Fluid flow equations are strongly nonlinear, which may explain the rather high sensitivity
to initial conditions. The main source of nonlinearity is the advection term in
momentum equations.
The turbulent nature of many flows induces a chaotic or stochastic character and a
large spectrum of flow fluctuations including very small scales. This makes it practically
impossible to solving the local instantaneous equations. Analytical exact solutions
are not known in (almost) all cases of interest and numerical solutions are and
will remain for a long time beyond the capabilities of current computers.
Since exact equations cannot be solved, simplified, and/or averaged equations must
be used to predict fluid flows. The main difficulty of industrial thermal-hydraulic studies
is to apply the right simplification to exact equations to give an approximate solution
with a sufficient degree of confidence. The next sections will present some of the
simplified set of equations used in nuclear thermalhydraulics.
5.3
The various approaches to single-phase modeling
One can classify single-phase modeling approaches (Bestion et al., 2011) first with
regard to the space dimension of the model, considering 0-D, 1-D, 2-D, and 3-D
models. Then, to be more specific on may consider the type of time and/or space averaging
which is used. 3-D models are often called CFD models. They can be split first
into 3-D for porous body and 3-D CFD in an open medium approach.

<!-- page 181 (PDF 15) -->
RANS-type models, LES-type models, and direct numerical solution (DNS) are the
three main categories of single-phase CFD models in open medium, see Table 5.2.
RANS models are the most commonly used in nuclear reactor applications, and they
include a large variety of turbulence models. Some recommendations were made by
the Writing Group of OECD-WGAMA for selection of the model according to the
application for reactor safety analysis (Mahaffy 2007).

## 5.3.1 RANS-type models

Time or ensemble averaging of local instantaneous equations (mass momentum and
energy) is a common way to derive equations for the so-called Reynolds average
Navier-Stokes (RANS) approach. Although time averaging and ensemble averaging
are different, they can reasonably be considered as equivalent (ergodicity) in steady or
quasi-steady flows where the RANS approach is applied. Since closure laws (e.g., for
Reynolds stress) are almost systematically validated against time averaged measured
flow parameters, one may consider that practical validated RANS model are
time-averaged models. Time-averaged equations are supposed to filter all turbulent
eddies and to predict only a mean velocity field. The time averaging affects both time
and space resolution in an Eulerian approach since eddies are transported by the mean
flow. The most popular RANS model (k−ε) uses a two-equation turbulence model
with the Boussinesq approximation and a turbulent viscosity. Many variations of
two-equation turbulence modeling exist such as k-l, k-ω, SST, RNG-k ε, k-ε-V2,
nonlinear k-ε. RANS was initially devoted to steady flow but may be also applied
to some unsteady or transient flow (U-RANS or T-RANS) if the time scale of the mean
flow is larger than the time scale of the largest eddies. It has been shown that a RANS
approach could predict the large-scale Von Karman alleys in the wake of the cylinder
provided that the numerical scheme does not induce artificial numerical viscosity.
RANS-type models require closure models for Reynolds stress tensor and turbulent
diffusion of heat. Wall functions are required for both momentum and energy to avoid
too fine meshes close to the walls. The modeling effort is rather heavy since models
for Reynolds stress require additional equations with several closure laws.

## 5.3.2 Scale/eddy-resolving-type models

When the computational grid is not sufficient to resolve the entire spectrum of scale
(from integral to Kolmogorov ones), a space filter is applied to the basic balance equations
. This allows predicting large eddies (or sometimes called super-grid scale),
whereas the effects of smaller eddy have to be modeled in a statistical way. This is
the basis of the large eddy simulation (LES). The detached eddy simulation (DES)
and very large eddy simulation (VLES) belong to the same class of scale/
eddy-resolving models. Some hybrid methods between U-RANS and LES exist such
as scale adaptive simulation (SAS). LES requires a transient calculation with rather
fine 3-D space nodalization; high-order space discretization scheme and high-order
time integration method are needed, which make the method much more CPU time
demanding than RANS methods. Statistical models are required to mimic the diffusive
effects of the unresolved subgrid scales (called simply “subscale” in the VLES

<!-- page 182 (PDF 16) -->
Table 5.2 Characteristics and modeling needs of the various types of single-phase CFD
Type of model
3D Open medium
3D porous
2D
1D
0D
DNS
LES (DES,
VLES,
SAS,…)
RANS (U-RANS,
T-RANS)
Time or
ensemble
averaging
No
LES (No)
DES, VLES,
SAS
(partially)
Yes
Yes
Yes
Yes
Yes
Space filtering
averaging
No
Yes
No
Filtering or
averaging
Averaging
Averaging
Averaging
Treatment of
eddies
All eddies
simulated
Large eddies
simulated
Effects of
small eddies
modeled
No eddy simulated
(largest scale
fluctuations—e.g.,
vortex shedding—
may be simulated in
U-RANS)
Effects of all
eddies modeled
Effects of all
eddies modeled
Effects of all
eddies modeled
Effects of
all eddies
modeled
Required
closure models
No model
Subgrid
turbulent
diffusion of
momentum
and scalars
Wall functions
Reynolds stress tensor
Turbulent diffusion of
scalars
Wall functions
3D-Diffusion-
Dispersion
Wall friction
Wall HT
2D-Diffusion-
Dispersion
Wall friction
Wall HT
axial-Diffusion-
Dispersion
Wall friction
Wall HT
Wall HT
Required
modeling
effort
X
XX
XXX
XXX
XXX
XX
Locality &
universality of
the modeling
*****
****
***
*
**
*
-

<!-- page 183 (PDF 17) -->
context) on momentum and energy transfers. Very often turbulent viscosity and diffusivity
models are used. Wall functions are also required for both momentum and
energy to avoid fine meshes near the walls. However the modeling effort is much lighter
than for RANS.

## 5.3.3 Direct numerical solution (DNS)

Direct numerical simulation just solves exact local instantaneous equations without
any averaging or filtering. In turbulent flow this requires that the nodalization is
extremely fine to be able to capture the smallest eddies at the Kolmogorov scale. This
approach being extremely CPU costly is limited to some investigations of simple
problems to create reference solutions or “numerical experiments” in view of
assessing other approaches.

## 5.3.4 Locality and universality of the modeling

Both RANS- and LES-type methods require some closure laws for additional
terms of equations coming from the averaging of filtering procedure. The modeling
of these terms most often assumes a kind of “principle of locality” where the
physics of the process to model depends only on local flow variables (i.e., velocity
, density, internal energy) and their time and space local derivatives. This is the
case for the treatment of Reynolds stresses and turbulent heat fluxes in both
RANS- and LES-type methods. The only exceptions to this principle of locality
are the so-called wall functions where some closure terms depend on the distance
to a wall. This allows using rather coarse nodalization in high shear regions close
to a wall.
It must be stressed that the principle of locality is much more relevant in a LES-type
method than in a RANS approach. The subgrid local turbulent viscosity at a given
point P(x, y, z, t) of a flow in a LES approach models only effects of small eddies
which are close to point P. In a RANS approach the effects of the largest eddies
on local physics have also to be modeled, and such large eddies depend on flow conditions
far from the point P. This is a reason why different RANS model options are
recommended for different flows like a boundary layer, wake, mixing layer, or jet,
whereas LES best models tend to be more universal. In RANS approach, local models
are much more geometry dependent than in LES. One may also consider that only
DNS provides a full application of the principle of locality since the only transfers
that are present are molecular transfers, which are expressed as functions of the first
derivatives (Fourier law, Newtonian fluid law).
One may define a figure of merit to quantify the degree of locality and then the
degree of universality of a model which would give five stars to the DNS *****, four
stars **** to the LES, three stars *** to the RANS, two stars ** to the 2D, only one
star* to porous-3D and to 1D, and no star to 0D.
