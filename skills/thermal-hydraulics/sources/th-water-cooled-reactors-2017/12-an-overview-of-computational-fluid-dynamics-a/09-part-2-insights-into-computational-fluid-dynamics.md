# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD applications to nuclear thermal fluids problems — Phenomenological issues
<!-- source PDF pages 57-72 -->

<!-- page 785 (PDF 57) -->
### 12.9.4 Phenomenological issues

#### 12.9.4.1 Stratification and buoyancy effects

Buoyancy forces develop in the case of heterogeneous density distributions in the
flow. Most of the events concern thermally stratified flows, which result from differential
heating (e.g., in heat exchangers), or from incomplete mixing of flows of
different temperatures (e.g., thermal stratification). Other contributions to this report
have underlined the possible occurrence of stratification and buoyancy forces. For
single-phase flows, one can recall stratified flow developing in the case of pressurized
thermal shock, hot leg heterogeneities, thermal shock, induced break, and for natural
convection in many relevant safety situations for GFR and LMFBRs and within the
context of the design of PAHR (post accident heat removal). For two-phase flow problems
, the reader may also refer to Mahaffy et al. (2007a,b).
Stratification may be one of the significant phenomena in the case of thermal
shock, under some small break LOCA conditions (e.g., performance of AP-600)
and for water-hammer condensation. Stratification and buoyancy effects may lead
to thermal fatigue, to modification of condensation rates, and to difficulties in
predicting the associated mixing processes.

### 12.9.5 Turbulence

#### 12.9.5.1 Steady RANS turbulence modeling

From the very early days of industrial CFD practice to the present time, the treatment
of turbulence has been based on statistical closure models of the Reynolds-averaged
Navier-Stokes (RANS) equations. The limitations of computing power available have
rendered this the only feasible option, although the complexity and sophistication of
the closure models employed have increased in line with advancing power. Although a
large amount of research capability has been invested in steady RANS models over the
past few decades, to date, no practicable model has emerged that is competent across a
broad range of flows featuring diverse states of strain. Over one hundred RANS
models or model variants have now been published. Many of these variants have been
devised to fix a problem in a preceding model, but few are widely successful beyond
that class of flows against which they are calibrated.
Here, we consider RANS turbulence closure models under the three categories:

##### l Linear eddy viscosity models (LEVM)

l
Nonlinear eddy viscosity models (NLEVM)
l
Reynolds stress models (RSM)
Linear eddy viscosity models (LEVM)
Among the various RANS turbulence models, the k-ε is currently the most popular
together with its variants (e.g., realizable, RNG) and similar linear approaches such

<!-- page 786 (PDF 58) -->
as the k-ω and shear stress transport (SST) models. However, it is well known that
the usual formulations of these models assume isotropic eddy diffusivity in modeling
the Reynolds stress tensor, and therefore anisotropic effects are not accounted
for. A consistent overview of selected Turbulence model is provided below:
Spalart-Allmaras (SA) model
Overview
The SA model (Spalart and Allmaras, 1992) solves a single transport
equation that determines the turbulent eddy viscosity. This is in contrast to
many of the early one-equation LEVMs that solve an equation for the
transport of turbulent kinetic energy and require an algebraic prescription
of a length scale.
The original model was developed primarily for the aerospace industry. It
has been widely used in the aerodynamic field because it has the advantage
of being readily implemented in an unstructured CFD solver.
Advantages
It showed reasonable prediction of the results for attached boundary layers
and flows with mild separation, such as flow past a wing, and acceptable
results for wake, mixing layer, and radial jet flows.
Limitations
However, for jet-like free shear regions, such as plane and round jets, it
showed inaccurate results (Wilcox, 1998). It is also likely to be less suited
to flows involving complex recirculation and body forces, such as
buoyancy, than higher level of RANS turbulence closure models.
Standard k-ε model
Overview
A significant proportion of industrial applications deployed the standard
k-ε model two-equation.
Advantages
It is relatively simple to implement, leads to stable calculations that
converge relatively easily and above all provides reasonable prediction for
many flows.
General
limitations
However, it is known that it shows poor predictions for:
l
swirling and rotating flows,
l
flows with strong separation,
l
axisymmetric jets,
l
certain unconfined flows, and
l
fully developed flows in noncircular duct flows, etc.
Also, it is valid only for fully turbulent flows and has too simplistic
an ε-equation.
Realizable k-ε model
Overview
The realizable k-ε model, derived from the realizability condition, shares
the same k-equation as the standard k-ε model but has an improved
ε-equation.
A coefficient (Cμ) in eddy viscosity becomes a variable instead of a
constant.
Advantages
It shows improved performance for flows involving planar and round jets
(it can predict round jet spreading correctly), boundary layer under strong
adverse pressure gradients or separation, rotation and recirculation, and
strong streamline curvature.

<!-- page 787 (PDF 59) -->
RNG k–ε model
Overview
The Renormalization Group (RNG) k-ε model, which is derived from the
rigorous statistical technique (so-called Renormalization Group method)
to the instantaneous NS equation, has a form similar to the standard k-ε
equations, but includes an additional term in ε-equation for interaction
between turbulence dissipation and mean shear, the effect of swirl on
turbulence, analytical formula for turbulence Prandtl number, and
differential formula for effective viscosity.
Advantages
Thus, it provides improved predictions for high streamline curvature and
strain rate, transitional flows and wall heat and mass transfer. The model still
does not predict the spreading of a round jet correctly (FLUENT, 2006).
Caution
Aside from the time per iteration, the choice of turbulence model can affect
the ability to obtain a converged solution. The standard k-ε model is known
to be slightly overdiffusive in certain situations, while the RNG k-ε model
is designed such that the turbulent viscosity is reduced in response to high
rates of strain. Since diffusion has a stabilizing effect on the numerics, the
RNG model is more likely to be susceptible to instability in steady-state
solutions. However, this should not necessarily be seen as a disadvantage
of the RNG model since these characteristics make it more responsive to
important physical instabilities such as time-dependent turbulent vortex
shedding (FLUENT, 2006).
k-ω model
Overview
The standard k-ω model, e.g., Wilcox (1998), is a widely used
two-equation model that is an alternative to the k-ε model.
The transport equations solved are for the turbulent kinetic energy and a
quantity called ω, which is defined as the specific dissipation rate, that is,
the dissipation rate per unit turbulent kinetic energy.
Advantages
This model offers a much more robust and accurate viscous sublayer
formulation and also has proven more accurate for boundary layers in
adverse pressure gradients.
Limitations
However, the standard k-ω model also had crucial weaknesses. It was a
severe sensitivity of the results to the freestream values specified for
omega outside boundary and shear layers (Menter, 1992; Wilcox, 1998).
This freestream sensitivity introduced a strong dependency of the solution
on relatively arbitrary values specified for k and ω at the inlet, as well as on
their decay upstream of the device of interest.
The effects of freestream dependency have also not been eliminated by
even the new version of the k-ω model (Wilcox, 2007).
SST k-ω model
Overview
The SST k-ω model has a transformed equation, which looks very similar
to the one in the standard k-ω model, but adds an additional
nonconservative cross-diffusion term containing the dot product.
Advantages
Inclusion of this term in the transport equation will potentially make the
k-ω model give identical results to the k-ε model. Menter (1994) suggested
using a blending function (which includes functions of wall distance) that

<!-- page 788 (PDF 60) -->
would include the cross-diffusion term far from walls, but not near the
wall. This approach effectively blends a k-ε model in the far field with a
k-ω model near the wall. The SST model is usually recommended for high
accuracy boundary layer simulations. For free shear flows, the SST model
is identical to the k-ε model.
Disadvantages
Since the zonal k-ω models, i.e., SST (or BSL k-ω) models, include
blending functions in the near-wall region that are a function of wall
distance, an additional equation is solved to compute the wall distance at
the start of simulations (the first few iterations).

##### Comments on LEVM

Adopting an isotropic eddy diffusivity in modeling the Reynolds stress tensor means
that since the viscosity is a scalar, each component of the stress affects its strain to the
same extent. For this reason, flows, where turbulent intensity gradients and hence the
augmentation effects of secondary strain rates are important, cannot be accurately
predicted. The most evident example is the secondary flow that originates in noncircular
ducts due to the gradients of turbulent shear stresses (Baglietto and
Ninokata, 2004).
An important weakness of the standard two-equation models is that they are insensitive
to streamline curvature and system rotation. Particularly, for swirling flows, this
can lead to an overprediction of turbulence mixing, i.e., overly dissipative, and to a
strong decay of the core vortex. There are curvature correction models available,
but they have not been generally validated for complex flows (ANSYS, 2010).

##### Nonlinear eddy viscosity models (NLEVM)

It is well known that a significant development in the turbulence modeling theory
since the 1990s is the nonlinear eddy viscosity turbulence model (NLEVM), which
is essentially equivalent to the explicit algebraic stress model (EASM).
Theoretical background The NLEVM describes the Reynolds stresses explicitly
in an algebraic expression in terms of the mean strain and rotation (spin) tensors as:
u0
iu0
j = ·νtSij + 2
3kδij + nonlinear terms
(12.11)
Many EARSMs and NLEVMs are used in combination with different k-ε models, but
several authors have also proposed combinations with k-ω models and other types of
two-equation models. Specifically, in Eq. (12.11), nonlinear terms consist of
second-order (quadratic) terms and third-order (cubic) terms, which reflect the normal
stress anisotropy of the turbulence structure and the effect of the streamline curvature
and the rotation, respectively (Xu and Ma, 2009). Several NLEVMs have been developed
according to flow characteristics by selecting appropriate nonlinear terms.
Advantages The advantage of NLEVM lies in that, with a well-developed robust
CFD code for the conventional two-equation turbulence models, it can be readily
implemented to simulate complex turbulent flows by merely adding the nonlinear

<!-- page 789 (PDF 61) -->
terms into the expression for the Reynolds stress (In et al., 2003) without significantly
consuming the CPU (about 10% increase) and losing the computational robustness
(Xu and Ma, 2009). Thus, for the problem of flow in a rod bundle with mixing vanes,
it needs to be validated.
Notes However, it should be emphasized that a careful calibration is needed for the
scale-determining part of the model when it is coupled with a nonlinear stress-strain
relationship, either NLEVM or EARSM (Hellsten and Wallin, 2009).
EARSMs or NLEVMs that are simply combined with an existing two-equation
model developed originally in the context of linear eddy-viscosity modeling may
show unexpected problems if insufficient attention is paid to the recalibration of
the scale-determining model. Both EARSMs and NLEVMs need the turbulent kinetic
energy k and timescale (τ=k/ε), which must be obtained from a scale-determining
model. As an example, strongly unphysical velocity profiles were obtained around
outer edges of turbulent layers using the Wallin and Johansson EARSM (Wallin,
2000; Wallin and Johansson, 2000), the Wallin model in combination with the k-ω
TNT model (Kok, 2000), or the k-ω BSL model (Menter, 1994), without any
recalibration (Hellsten and Bezard, 2005; Hellsten, 2005).

##### Reynolds stress models

Overview The Reynolds stress model (RSM) is the most elaborate turbulence model
in (U)RANS turbulence models. Abandoning the isotropic eddy-viscosity hypothesis,
the RSM closes the Reynolds-averaged Navier-Stokes equations by solving transport
equations for the Reynolds stresses, together with an equation for the dissipation rate.
This means that five additional transport equations are required in 2D flows and seven
additional transport equations must be solved in 3D.
Advantages Specifically, RSM can show better performance involving the following
types of flows:
l
Free shear flows with strong anisotropy, like a strong swirl component, including flows in
rotating fluids,
l
Flows with sudden changes in the mean strain rate,
l
Flows where the strain fields are complex and reproduce the anisotropic nature of turbulence
itself,
l
Flows with strong streamline curvature, secondary flows, and
l
Buoyancy flows.
All of these are based on a higher degree of universality by considering each Reynolds
stress tensor.
Disadvantages However, the penalty for this flexibility is a high degree of complexity
in the resulting mathematical system, thus leading to reduced numerical
robustness, requires increased computational resources. Thus, people typically start
with a more stable turbulence closure model, such as k-ε model, and then run the
RSM. The RSM may require more iterations to converge than the k-ε and the k-ω
models due to the strong coupling between the Reynolds stresses and the mean flow.

<!-- page 790 (PDF 62) -->
Notes The fidelity of RSM predictions is still limited by the closure assumptions
employed to model various terms in the exact transport equations for the Reynolds
stresses. The modeling of the pressure-strain and dissipation-rate terms is particularly
challenging and often considered to be responsible for compromising the accuracy of
RSM predictions.
In addition, the RSM might not always yield results that are clearly superior to the
simpler models in all classes of flows to warrant the additional computational expense.

##### Variants of RSM

Some variants exist in RSM. These vary depending on modeling of the pressure-strain
term. Examples are provided in the following:
l
The LRR RSM (Launder, Reece, Rodi) (Launder et al., 1975), with a linear pressure-strain
term, and SSG RSM (Speziale, Sarkar, Gatski), (Speziale et al., 1991), with a quadratic
pressure-strain term, are used well.
l
The SSG RSM has been demonstrated to give superior performance in a range of basic shear
flows, including plane strain, rotating plane shear, and axisymmetric expansion/contraction.
This improved accuracy should be beneficial for a wider class of complex engineering flows,
particularly those with streamline curvature.
l
The quadratic pressure-strain model, i.e., the SSG RSM, does not require a correction to
account for the wall-reflection effect in order to obtain a satisfactory solution in the logarithmic
region of a turbulent boundary layer.
l
However, the SSG RSM can be only used with wall-modeled near-wall treatment, while the
linear pressure-strain model can be used with wall-resolved treatment or a two-layer model.
Thus, if it is important to resolve the viscous sublayer, only the linear pressure-strain model
(LRR RSM)can be chosen.
l
The CFX code also provides ω-based RSMs, such as the SMC-ω (underlying the Wilcox k-ω
model, Wilcox, 1998) and the baseline RSM (BSL RSM, underlying the BSL k-ω model)
because the ω-equation allows a more accurate near-wall treatment.

#### 12.9.5.2 Unsteady RANS (URANS) turbulence modeling

When the flow is not statistically stationary, Reynolds averaging is not same as
time-averaging and thus, the simulation must be time-dependent (Ramesh et al.,
2006) (see also Diwan et al., 2006). In fact, it has become common to call RANS
modeling URANS whenever the computed solution is time dependent. The approach
then is to apply an existing RANS model and to aim at resolving some of the unsteady
features of the flow without recalibration of model coefficients (Fr€ohlich and von
Terzi, 2008). Although the URANS is still theoretically disputable, it has been proven
to be successful in numerous real applications.

##### Theoretical background

The URANS is based on the following triple decomposition:
ui xi, t
ð
Þ = ⟩ui xi
ð Þ + u_
i xi, t
ð
Þ + u00
i xi, t
ð
Þ
(12.12)

<!-- page 791 (PDF 63) -->
where u¯i(xi) is the mean value defined as ui xi
ð Þ = lim
T⃗∞
T
ðT
ui xi, t
ð
Þdt, ȗi(xi,t) is
deterministic or coherent contribution, and ui
00(xi,t) is random, turbulent fluctuation.
In the actual calculation, the mean and the coherent component in Eq. (12.12) are
lumped together and thus,
ui xi, t
ð
Þ = ui
h i xi, t
ð
Þ + u00
i xi, t
ð
Þ
(12.13)
Using the above decomposition, the URANS equations can be derived as (Johnson,
2008) (see also Labois and Lakehal, 2011):
∂ ui
h i
∂t
+ ∂ ui
h i uj
∂xj
= ·∂ p
h i
∂xi
· ∂
∂xj
·ν ∂ ui
h i
∂xj
+ ∂ uj
∂xi
+ u00
i u00
j
D
E
|fflfflffl{zfflfflffl}
□τURANS
ij
(12.14)
It should be noted that
τURANS
ij
xi, t
ð
Þ 6= τRANS
ij
xi
ð Þ and τURANS
ij
xi, t
ð
Þ 6= τRANS
ij
xi
ð Þ
(12.15)
where τURANS
ij
xi, t
ð
Þ 6= τRANS
ij
xi
ð Þ is Reynolds stress.
Since it is practically impossible to attain ensemble average in an experiment, we
cannot directly compare τij
URANS(xi,t) results, i.e.:
τRANS
ij
= u0
iu0
j = u_
iu_
j + u00
i u00
j
D
E
=
ui
h i· ui
h iÞð uj
· uj
□
(
+ u00
i u00
j
D
E
=
ui
h i· ui
h iÞð uj
· uj
□
(
+ τURANS
ij
(12.16)
Turbulent kinetic energy is also evaluated as:
k = kc + knc
(12.17)
where
kc = 1
2 u_2
i = 1
ui
h i· ui
h i
□
(2
and knc = 1
2 u002
i
(12.18)
Since the URANS model in usual CFD code typically calculates huii and τij
URANS and
their average and RMS values, to compare Reynolds stress τRANS or turbulent kinetic
energy with experimental ones, additional calculations need to be performed using
Eqs. (12.16)–(12.18). For example, the coherent part of kinetic energy is obtained
by time averaging the sum of the squares of the resolved velocity component

<!-- page 792 (PDF 64) -->
fluctuations and the noncoherent part of kinetic energy is obtained by time-averaging
the URANS computed instantaneous turbulent kinetic energy.

##### Theoretical issues

One theoretical issue is that the triple decomposition (Eq. 12.12) is valid under the
assumption that there is a clear spectral gap between deterministic (coherent) and
turbulent fluctuation. In other words, the deterministic component should have larger
timescale than the maximum timescale of turbulent fluctuation.
Modeling of τURANS
ij
xi, t
ð
Þ = u00
i u00
j
D
E
xi, t
ð
Þ, i.e., in terms of steady RANS turbulence
closure models without modification, may cause another problem. This is
because coefficients in steady RANS turbulent transport equations were determined
by statistically stationary experiments or DNS results. In general, most previous
RANS turbulence models are basically adjusted to reproduce the spreading rate of
mixing layers in steady RANS simulations, i.e., the Reynolds stress predicted by
the models implicitly contains contributions not only from the turbulent or random
motions but also from the coherent motions of the flow (Spalart, 2000), and thus the
models are, in general, overly dissipative (Menter et al., 2003a,b) when used in
URANS simulations.
Especially, using an isotropic linear eddy viscosity model makes the overly
dissipative characteristics more clear. This is because the Boussinesq approximation
adopted in linear eddy viscosity model assumes that anisotropy and strain are aligned.
The production term in the transport equation of kinetic energy continuously changes
with the maximum and the minimum when anisotropy and strain are aligned and perpendicular
, respectively. However, unsteady flow with large-scale fluctuations strain
is generally not aligned with the anisotropy tensor. Thus, the linear eddy viscosity
model always has the maximum production term, thereby showing overly dissipative
characteristics in unsteady flows.
Also, URANS can often capture the instability, but the difference from DES or LES
is that grid refinement does not extend the energy cascade. The solution converges to
the smooth solution of the modeled equations, instead of generating smaller and
smaller eddies. Typically, both the three-dimensionality and the shedding modulations
are suppressed by the smoothing effect of the RANS model (Travin et al., 1999).

#### 12.9.5.3 Near-wall treatment of (U)RANS

#####  Wall-modeled (U)RANS (wall function methods)

In this treatment, standard wall function is based on the assumption that the first grid
point of the wall is located in the universal law of the wall or logarithmic layer. The
wall function eliminates the need to resolve the very thin viscous sublayer, thus
leading to reduction in the number of cells and to a more moderate (and desirable)
aspect ratio of the cells (ratio of the longest to the smallest side in a structured grid).
On the other hand, standard wall function formulations are difficult to handle
because it should be ensured that the computational grid resolution near the wall
satisfies the wall function requirements. If the grid becomes too coarse the resolution

<!-- page 793 (PDF 65) -->
of the boundary layer is no longer ensured. If the resolution becomes too fine, the first
grid spacing can be too small to bridge the viscous sublayer. In this case, the logarithmic
assumptions are no longer satisfied. The user should ensure that both limits are not
overstepped in the grid generation step. Also, high aspect ratios can result in numerical
problems due to round-off errors.
The lower limit on the grid resolution for standard wall functions is a severe
detriment to a systemic grid refinement process, as required by the best practice
approach. In other words, instead of an improved accuracy of the solution with grid
refinement, the solution will deteriorate from a certain level on, leading eventually to a
singularity of the numerical method. Standard wall functions are therefore not recommended
for systematic grid refinement studies. Recently, alternative formulations
like scalable wall functions (Menter and Esch, 2001) have become available, which
allow for systematic grid refinement when using wall functions (ANSYS, 2010).
The wall function approach for the near-wall region is simple but becomes less reliable
when the flow conditions depart too much from the ideal conditions underlying
the wall functions. Examples are as follows (FLUENT, 2006):
l
Pervasive low-Re number or near-wall effects (e.g., flow through a small gap or highly
viscous, low-velocity fluid flow);
l
Massive transpiration through the wall (blowing/suction);
l
Severe pressure gradients leading to boundary layer separations;
l
Strong body forces (e.g., flow near rotating disks, buoyancy-driven flows);
l
High three-dimensionality in the near-wall region (e.g., Ekman spiral flow (Ekman, 1905)
strongly skewed 3D boundary layers).

##### Wall-resolved (U)RANS

The use of low-Reynolds number formulations of turbulence models for the integration
of the equations through the viscous sublayer is generally more accurate because
no additional assumptions are required regarding the variation of the variables near the
wall. On the other hand, most low-Reynolds number turbulent models are quite
complex and can reduce the numerical performance or even destabilize the numerical
method. In addition, classical low-Re models require a very fine near-wall resolution
of y+ around 1 at all wall nodes. This is quite difficult to ensure for all walls of a
complex industrial application. In the case that significantly coarser grids are used,
the wall shear stress and the wall heat transfer could be reduced significantly below
their correct values (ANSYS, 2010).

##### Low Reynolds number model

The low-Reynolds number approach employs a turbulence model that is valid
throughout the boundary layer including the viscous sublayer. Turbulence models
need to be modified to resolve the viscous layer by using a damping function.
The mesh must be sufficiently fine to resolve the viscous sublayer, and there is little
or no need for rmodeling to obtain the wall boundary conditions. The computational
expense associated with this approach can be significant, particularly for large Reynolds
numbers (FLUENT, 2006).

<!-- page 794 (PDF 66) -->
Two-layer model (for ε-based RANS models)
The two-layer model is an alternative to the low-Reynolds number model, allowing
the k-ε model to be applied in the viscous sublayer.
In this model, the computation is divided into two layers. In the layer adjacent to the
wall, the turbulent dissipation rate (ε) and the eddy viscosity are specified as functions
of wall distance. The values of ε specified in the near-wall layer are blended smoothly
with the values computed from solving the transport equation far from the wall. In
contrast, the k-equation is solved in the entire flow region.
This explicit specification of ε and eddy viscosity is arguably no less empirical than
the damping function approach in low Reynolds number models and the results are
often as good or better (CD-adapco, 2006).

##### Enhanced near-wall treatment

Most commercial codes have the enhanced near-wall treatment method so that low Re
number (mainly ω-based models but also ε-based models in STAR-CCM+) or
two-layer models (ε-based models) may not be deteriorated by coarse mesh.

#### 12.9.5.4 Large eddy simulations

Large eddy simulation (LES) was pioneered in the 1960s and much progress has been
achieved over the last few decades. Although important subgrid scale models were
already developed in the 1990s, the main applications of such models are mainly
confined to building-block flows. Actual applications to engineering problems have
not been performed prevalently. This is mainly because LES simulations still require
enormous amount of computational cost for engineering application.
This fact can also be confirmed by viewing the LES models in commercial CFD
codes. Most CFD codes only contain very simple SGS models, Smagorinsky model, or
WALE model (although the FLUENT code contains a dynamic Smagorinsky model
and a dynamic kinetic energy equation model).
However, since the LES still requires a large computational cost compared to (U)
RANS simulations, its applications have been mainly simple flows rather than
complex engineering flows. Furthermore, in wall-bounded flows, demanded grid
resolution near the wall become enormous, comparable to DNS.
Thus, for practical applications, one can employ several wall models, such as the
wall stress model similar to wall function methods as in RANS model, zonal models,
or hybrid methods, where the near-wall region is solved by a (U)RANS equation and
far from the wall LES is performed.

##### Wall-modeled LES

Large eddy simulations (LES) of wall-bounded flows become prohibitively expensive
at high Reynolds numbers if one attempts to resolve the small but dynamically important
vertical structures in the near-wall region. The Reynolds number scaling of the
required number of grid point is nearly the same as for DNS.

<!-- page 795 (PDF 67) -->
An attractive alternative to compute high-Reynolds number flows is using
wall-layer models (wall-modeled LES), in which only the outer layer is resolved,
while the near-wall region is modeled.
Three broad classes of approaches are presently used (Piomelli, 2008): (1)
bypassing this region altogether using wall function (equilibrium stress model), (2)
solving a separate set of equations in the near-wall region, weakly coupled to the outer
flow (zonal approaches), and (3) simulating the near-wall region in a global,
Reynolds-averaged, sense (hybrid RANS-LES method).
Zonal methods can also be included in hybrid methods (layering RANS-LES
method) (Fr€ohlich and von Terzi, 2008).

##### Wall stress model

To circumvent the severe near-wall resolution requirement, LES can be combined
with a wall (-layer) model. In this approach, LES is conducted on a relatively coarse
grid designed to resolve the desired outer flow scales. The dynamic effects of the
energy-containing eddies in the wall layer (viscous and buffer regions) are determined
from a wall model calculation, which provides to the outer flow LES a set of approximate
boundary conditions, often in the form of wall shear stresses. Wall models,
which supply wall stresses to the LES, are called wall stress models (Wang and
Moin, 2002) or equilibrium stress models (Piomelli, 2008).
The simplest wall stress models are analogous to the wall functions commonly used
in RANS approaches except that they are applied in the instantaneous sense in
unsteady calculations. The wall function provides an algebraic relationship between
the local wall stresses and tangential velocities at the first off-wall velocity nodes.
This approach was first employed in a channel flow simulation by Schumann
(1975) who assumed that streamwise and spanwise velocity fluctuations are in phase
with the respective surface shear stress components.
A number of modifications to Schumann’s model have been made by, for example,
Groetzbach (1987) and Werner and Wengle (1991) (whose power law model was
adopted in commercial CFD code like STAR-CCM+) to eliminate the need for a priori
prescription of the mean wall shear stress and to simplify computations, and by
Piomelli et al. (1989) to empirically account for the phase shift between the wall stress
and near-wall tangential velocity due to the tilting of near-wall eddies.

##### Comments and recommendations

The wall stress approach can give reasonably accurate results in attached flows, with
mild pressure gradient and curvature (Piomelli, 2008). However, since the assumption
underlying the approximate boundary condition (i.e., turbulence is in equilibrium) is
quite strong, it may fail catastrophically in the following flows:
l
Rotating flows where turbulence is damped on one side and amplified on the other.
l
Flow with shallow separation, e.g., flow over a contoured ramp.
l
Flow with strong pressure gradient.
l
In attached flows, even in the presence of fluid-dynamical nonequilibrium, the logarithmic
law approximate boundary condition can give more accurate results.
l
Oscillating freestream (where fluid is dynamically nonequilibrium, but the boundary layer is
still attached)

<!-- page 796 (PDF 68) -->
##### Zonal model

The “algebraic” wall stress models mentioned above all imply the logarithmic law or
law of the wall for the mean velocity, which is not valid in many complex flows.
To incorporate more physics into the model, wall stress models based on
boundary-layer approximations have been proposed, e.g., Cabot and Moin (2000),
Balaras et al. (1996), Cabot (1996), Wang and Moin (2002), and Gungor and
Menon (1996).
In this method, turbulent boundary-layer (TBL) equations are solved numerically
on an embedded near-wall mesh to compute the wall stress. These equations are forced
at the outer boundary by the instantaneous tangential velocities from LES, while
no-slip conditions are applied at the wall. The turbulent viscosity is modeled by a
RANS type model, such as the mixing length model with wall damping.

##### Comments and recommendations

Zonal models have had success in flow in which the outer layer drives the inner layer.
However, they have been less successful when the perturbation is propagated from the
wall outward.

##### Hybrid RANS-LES models (as wall models)

In hybrid RANS-LES methods, the RANS equations are solved in the inner layer,
while the filtered LES equations are solved away from the wall. The main issue is
the disparity of scales between the LES and RANS regions.
In the wall stress and zonal models, the outer layer imposes its scales on the inner
one, which therefore contains eddies as small as the filter size.
In hybrid methods, on the other hand, the inner layer has its own time scale and
length scale (determined by the URANS equations applied there), which are generally
much larger than those of the outer-layer eddies.
The lack of resolved eddies in the interface region results in the logarithmic law
mismatch (LLM). Since the total stress is determined by the global momentum
balance, the decrease in the eddy viscosity that occurs beyond the RANS/LES nominal
interface, if not accompanied by a corresponding increase of the resolved Reynolds
stress, must result in an increase in the mean velocity gradient.
To reduce or remove the LLM, various methods have been developed, e.g.:
l
Introducing artificial fluctuation (e.g., stochastic forcing) at the interface (Piomelli et al.,
2003; Keating and Piomelli, 2006).
l
Introducing additional filtering at the interface (Hamba, 2003, 2006).

##### Comments and recommendations

Hybrid RANS-LES methods seem to be the most effective in flow conditions that
facilitate the rapid amplification of any instability, whether due to numerical or natural
causes, such as separation, concave curvature, and adverse pressure gradients. In such
cases, the eddy generation at the interface is greatly increased, and accurate results can
be obtained.
Hybrid RANS-LES methods are the least accurate in attached, thin shear layers,
where the instability mechanisms are comparatively weak (due to logarithmic law
mismatch).

<!-- page 797 (PDF 69) -->
##### Summary of wall-modeled LES

It is unreasonable to expect that wall-modeled LES, which bypasses the inner layer,
could ever be as accurate as wall-resolved LES because even in equilibrium flows, the
inner layer is the region where most of the production occurs and the eddies are created
that grow and advect into the outer layer, affecting the momentum transfer too.
Despite this intrinsic shortcoming, wall-modeled LES is able to predict with
reasonable accuracy a wide variety of flows.
In many cases, the physics of the outer layer is reproduced well, despite the fact that
the inner layer is bypassed, as long as the grid is fine enough to resolve the outer-flow
integral scale.
Unless the integral scale in the outer layer is resolved well, Δ>δ/15, uniformly
accurate results cannot be obtained.

#### 12.9.5.5 Very large eddy simulation

#####  Overview

Based on the initial successes of LES in predicting prototypical flows, attempts have
been made to apply traditional LES to complex flows of industrial relevance.
However, due to computational affordability, the resulting computational grids
necessarily had to be coarse, too coarse to resolve the desired amount (about 80%)
of kinetic energy (Fr€ohlich and von Terzi, 2008). This was called very large eddy
simulation (VLES) by some researchers (e.g., Ferziger, 1996). Within the framework
of this chapter, we restrict the VLES to its original intent, i.e., LES with traditional
SGS models on coarse grids.

##### Notes

The VLES has two fundamental problems. First, the LES cutoff is now located within
or even below the wavenumber range of the most energetic modes. Modeling the
interaction between resolved motion and unresolved motion is very delicate in this
case, and there is little hope for success. Second, the numerical discretization scheme,
mostly disregarded in the classical (explicit) LES model development, impacts the
scales near the grid scale, which are the physically relevant ones with VLES
(Fr€ohlich and von Terzi, 2008).

##### Comments and recommendations

Despite the failure of the naive approach, the idea to predict the large-scale unsteadiness
of the flow at minimum cost (e.g., Smagorinsky, 1963) remains attractive and
such coherent structure capturing, as it was called by Ferziger (1996), is the aim of
many hybrid LES/RANS methods. This, however, requires a substantially more
sophisticated modeling approach. In the literature, the acronym VLES has occasionally
been used synonymously for a wide range of methods (e.g., Drikakis, 2002) such
that this term is no longer descriptive.
However, the VLES can be used to generate inflow conditions for LES, e.g., Meri
et al., 1999; Meri and Wengle (2002), and Howard and Pourquie (2002).

<!-- page 798 (PDF 70) -->
#### 12.9.5.6 Hybrid RANS-LES method

URANS turbulence models are overly dissipative, thus rendering only a single mode
of unsteady structures. Also, VLES turbulence models do not resolve turbulence
production fully, whereas dissipation is largely overpredicted. Despite the failure
of such approaches, the idea of predicting the large-scale unsteadiness of the flow
at minimum cost remains attractive and such coherent structure capturing is the main
motivation of many hybrid RANS-LES methods. This however requires a substantially
more sophisticated modeling approach than URANS or VLES.
Numerous hybrid methods have been developed. These are
l
based on (U)RANS closure models, by adding the characteristics of resolved turbulence
scales mainly related to grid size, which is a main property of LES SGS model, or
l
based on LES SGS models, by adding the characteristics of broad turbulence scales coverage
, which is a main property of a (U)RANS closure model.
These approaches are possible because the governing equations (momentum and
energy equations) have the same form, except that Reynolds averaging and filtering
operations were applied in URANS and LES, respectively. Although Reynolds
averaging and filtering has quite different physical meaning, the difference is not revealed
explicitly in the actual calculation process except in the turbulence stress term.

##### Classifications

In the hybrid RANS-LES method, the calculation for a node can be performed (i) by
selecting (switching) either RANS turbulence models or LES SGS models, or (ii) by
blending two model effects (in turbulence stresses or some physical values). This kind
of hybrid method is often called a global or unified approach.
On the other hand, one can simulate pure LES calculations in one domain region
and pure RANS calculations in the remaining parts of the domain and then match
values in the interfaces. This kind of hybrid method is called a zonal (or segregated)
approach.
It should be noted that in global (or unified) models without using blending
concepts, usually RANS and LES regions separately exist as in zonal model.
However, they are different from zonal models in the following ways.
l
Interfaces in global (or unified) models are determined by wall distance and grid size or
additionally in a solution-dependent manner for each time calculation, not by predetermined
separate domains as in zonal methods.
l
Communication at interfaces in global (or unified) models is achieved in a turbulence stress
level (i.e., unresolved turbulence values), such as turbulence kinetic energy and turbulence
dissipation, in contrast to a governing equation level (i.e., resolved scales) in zonal (or
segregated) models.
Also, it should be pointed out that: (i) if the interface is determined only by wall
distance and grid size, it will not change (hard interface) over time, once grid is
generated, whereas, (ii) if it is determined by solution-dependent values in addition,
it may change with time (soft interface) (Fr€ohlich and von Terzi, 2008).

<!-- page 799 (PDF 71) -->
On the other hand, zonal approaches in the wall-modeled LES can be regarded as a
global (or unified) hybrid RANS-LES method with hard interface because they solve
the near-wall flow region using RANS and the flow region from the outer layer using
LES, and they communicate unresolved turbulence scales with each other. Thus, the
zonal approach can be called layering RANS-LES models (Fr€ohlich and von Terzi,
2008). It also needs to be mentioned that layering RANS-LES models can have soft
interface by specifying the wall distance in a solution-dependent coordinate system
(e.g., Breuer et al., 2008a; Breuer et al., 2008b) or by using the ratio of kinetic energy
to total turbulent kinetic energy (Kniesner et al., 2007).

#### 12.9.5.7 Detached eddy simulation

Although most hybrid methods were developed for general purposes, some hybrid
models can be used as wall layer models for LES simulation. Among them, detached
eddy simulation (DES) has been the most widely used in CFD society and also
included in
many
commercial CFD
codes, such
as
CFX,
FLUENT,
and
STAR-CCM+ because of its simplicity to implement in previous RANS turbulence
models through simple modification.
Original SA-DES can be classified into a global (or unified) hybrid RANS-LES
method with hard interface because the interface is determined by wall distance
and grid size.
One advantage of DES is that it uses the same transport equation for RANS and
LES turbulence stress and instead chooses the length scale in the dissipation term
of the equation from either wall distance (originally for RANS turbulence closure
models) or grid size-related length scale.

##### Use of DES

The DES was originally developed for massively separated flows in the aerodynamic
field to apply RANS calculations in an attached boundary layer region and LES calculations
in separated flows. This use of DES can be called Natural DES. DES can
also be used as a wall layer model for LES. Hereafter, this use of DES will be called
wall-modeled DES. The difference between the natural and wall-modeled DES is that
in wall-modeled DES applied to wall-attached flows, the RANS region is usually limited
to a region in the outer layer as in wall-modeled LES, while in natural DES mainly
applied to massively separated flows, such as airfoil, the RANS region is desired to
cover all boundary layers, which is because intermediately resolved wall grids may
cause the early transition to LES, thus inducing the early separation (which is called
grid-induced separation (GIS) due to modeled stress depletion (MSD) (Spalart, 2009).

##### Variants of DES

Subsequent enhancements, such as delayed (SA-) DES (DDES), zonal (SA-) DES
(ZDES), and shielding SST-DES, were mainly for the prevention of the GIS in terms
of natural DES. In contrast, improved DDES (IDDES) was developed to relieve the
LLM by changing the length scale.

<!-- page 800 (PDF 72) -->
##### Comments and recommendations

If a hybrid RANS-LES method like DES is used as a wall-layer model, grids in the
LES region should be finely resolved enough to satisfy the LES SGS model
conditions.
If one wants to use entirely coarse grids (finer than URANS but coarser than LES),
one should not use DES methods because the DES becomes VLES outside the boundary
layer region. Alternatively, one can use blending hybrid RANS-LES methods like
flow simulation methodology (FSM), e.g., Zhang et al. (2000), Fasel et al. (2002), and
Hussaini et al. (2006), or hybrid methods using weighted sum (Xiao et al., 2004), see
also Fu et al. (2010) and Xiao et al. (2003) because these methods consider a RANS
correction of LES in coarser regions.

#### 12.9.5.8 Scale-adaptive simulation

The scale-adaptive simulation (SAS) is regarded as an improved URANS. The
improved URANS aimed at resolving a substantial part of the turbulent fluctuations
but do not contain an explicit dependency on the computational grid like LES. RANS
models involve only physical length scales, while LES models contain explicitly or
implicitly a length scale related to the numerical grid, which determines the size of
resolved fluctuations.
The SAS modeling is based on the use of a second mechanical scale in the source/
sink terms of the underlying turbulence model. In addition to the standard input from
the momentum equations in the form of first velocity gradient (such as strain rate tensor
and vorticity tensor), SAS models rely on a second scale, in the form of higher
velocity derivatives (second derivatives).
SAS models satisfy the following requirements (Menter and Egorov, 2005):
(a) Provide proper RANS performance in stable flow regions.
(b) Allow the breakup of large unsteady structures into a turbulent spectrum.
(c) Provide proper damping of resolved turbulence at the high wave number end of the
spectrum (resolution limit of the grid).
Functions (a) and (b) are achieved without explicit grid or time step dependency in the
model. Naturally, function (c) must be based on information on the grid spacing, other
information concerning the resolution limit (dynamic LES model, etc.), or numerical
method (MILES) damping.

##### Characteristics

Flows or flow conditions where SAS mode is active are:
l
Flows where steady-state solution cannot be obtained;
l
Flows where the use of smaller time steps results in unsteady solutions.
One could argue that the occurrence of unsteady regions in URANS simulation is the
result of a nonlocal interaction which cannot be covered by the single-point RANS
closure. Flows where SAS mode is not active, i.e., they return to URANS mode, are
l
Attached or mildly separated boundary layers, and
l
Undisturbed channel/pipe flows.
