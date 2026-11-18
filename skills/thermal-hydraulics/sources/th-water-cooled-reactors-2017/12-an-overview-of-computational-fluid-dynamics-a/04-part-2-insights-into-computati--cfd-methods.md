# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD methods
<!-- source PDF pages 22-35 -->

<!-- page 750 (PDF 22) -->
(4) Collaboration (understanding) is needed among experts of different physics:
neutronics, fuel performance analysis, reactor kinetics, chemistry, system code,
structural mechanics, etc.
(5) Collaboration is needed among CFD users and analysts: the round robin benchmark
exercise is recommended.
(6) Goal set 2: Active (CFD main solver) and passive applications (CFD parts) are
concerned: for instance, without considering 3D effect and local effects, the results
can never be accurate.
(7) An “open system” should be designed and constructed where the accumulation of
experiences, the collaboration among CFD players, and the accessibility of data are
possible. This should imply not only the form (e.g., web-based, hypertext) but also
the contents (e.g., provide a common methodology and share results of interest).
Furthermore, it may be impossible to explain all the reasons of respective selections
, but selected experiments should be shared as well as experienced in considering
those experiments within the model development and validation processes.
The assumptions at the basis of the methodologies should be made known. The
reasons for good results with main factors to produce them should be explained.
The question “Bad results, why?” should be asked frequently; what was not considered
should be revealed. Great courage is required to do these!
(8) Implicit knowledge should be changed into explicit one.
(9) The importance of experts should be increased as well as their impact upon the
conduct of activities: suggestions by senior experts may save years of failing
attempts to get solutions for given problems.
(10) More understanding in physics is definitely needed (e.g., turbulence dissipation,
pressure drops at geometric discontinuities).
(11) More understanding of CFD methods including numerical solution methods and
the interaction between those methods and the computer features is needed.

## 12.7 CFD methods

### 12.7.1 CFD procedure

A typical procedure for performing CFD analysis is given in Fig. 12.3.
l
Procedure of CFD NTF applications (NRS issues). The topics for performing CFD applications
indicated in Fig. 12.3 are further discussed in this paragraph. When a problem (rather,
an issue) for CFD application is assigned, related phenomena identification (PIRT) should be
performed. The problem definition requires the identification of the CFD role. Then CFD
methodologies (physical models) should be selected and related assessment should be
planned: this may require the availability of CFD-grade benchmark experiments and suitable
/applicable V&V and UQ procedures. Review of results should be planned. Implications
of results should be considered. Problem-specific BPG should be used and experience from
their application should be documented. However, V&V and UQ procedures are not so
simple: phenomena are mixed and occur simultaneously in the reality; some phenomena
may simply be unknown, especially for emerging issues or new applications; CFD needs,
e.g., boundary and initial condition values may not be consistent with available information;
few CFD-grade experiments are available; no efficient CFD-level V&V and UQ procedures

<!-- page 751 (PDF 23) -->
exist, so far; BPG application is resource and time consuming, i.e., beyond what is available;
scaling issues should be identified and addressed. In addition, according to Boyd (2016), a
general procedure for the CFD applications to the nuclear thermal fluids problems can be
summarized as follows: First, the key phenomena should be clarified because this step
critically affects the selection of the CFD models. Especially for an emerging issue, this step
is very important. Next, the selected CFD methods or models become a CFD methodology
for the problem. A thorough assessment for the selected CFD methodologies should be
performed. The verification and validation and uncertainty quantification are key parts in
the assessment step. Feedback by trial and error and the multitude of V&V can establish best
practice guideline specific for the problem.

### 12.7.2 Problem definition and identification of CFD role

The following additional items should be considered when a coupled CFD/SYS TH
code application is planned (Bestion, 2012).
l
Identification of important flow process. The following steps are undertaken when a coupled
CFD/SYS TH code application is performed: (1) Identification of the target basic process of
interest in the reactor system, (e.g.,) fluid temperature field in a component, clad temperature
, local heat transfer, mechanical load on some structure, velocity field in a component,
system peak pressure, etc.; (2) Identification of the other basic processes expected in the
process of interest; (3) Identification of the main nondimensional numbers, which characterize
the important flow process; (4) Identification of space and time domain of interest
for the concerned; (5) Identification of two-phase flow characteristics and kind of
two-phase flow regime likely to occur in the domain of interest; this should also include
1: Understand the problem and formulate the simulation strategy
2: Create the geometry
3: Generate the mesh
4: Establish the boundary and initial conditions
5: Run the solver, and monitor for convergence
6: Postprocess and interpret the results
7: Refine the mesh
8: Perform a sensitivity analysis
9: Document the analysis
Fig. 12.3 Typical CFD analysis procedure, Faragher, 2004.

<!-- page 752 (PDF 24) -->
the number and the kind of expected separate fields; (6) Identification of the fluid motion
nature, i.e., steady or transient; in case of transient, the minimum timescale of interest should
be identified; (7) Fixing the minimum space scale of interest in the process.
l
Isolation of CFD issues. First, the CFD computational domain and the boundary conditions
(also initial conditions) are defined: examples of computational domain in RCS: RPV lower
plenum, RPV downcomer, cold leg (e.g., to solve PTS problems), and SG tube. Second, the
issue of Boundary and Initial Condition (BIC) needs to be addressed: this may be a complex
step and different solutions are possible, e.g., one-way/two-ways coupling. Third, the
sources of uncertainty should be identified. Any of the steps above may have large effect
on the CFD results.
l
Features of Nuclear Thermal Fluids (NTF) problems: All problems in nuclear field involve
fluid and/or heat transfer. Therefore the following issues should be addressed:
−
Geometry: this is typically “large,” “complex,” and “multiscale” (i.e., with phenomena
expected in the range from mm to m).
−
Flows: complex three-dimensional flows are expected. The flow nature can be steady
(time independent) and/or unsteady (time dependent). Multiple flow physics are
concerned: in relation to heat transfer, natural, mixed and forced convection; in relation
to flow motion, laminar, turbulent, and transition flows; in relation to the number of
phases, single-phase and multiphase (having a variety of flow regimes); in relation to
the number of components, single and multicomponent flows (e.g., various gases moving
in the same space region); in relation to fluid properties, incompressible and compressible
flows. One difficulty comes from observing that all the listed conditions may
occur simultaneously for the simulation of a unique phenomenon.
−
Multiple physics: the following areas are involved: chemistry (corrosion), neutron
physics, and structural mechanics (e.g., fluid-structure interaction, fatigue).
l
CFD Boundary/Interface conditions. Related to CFD analysis within a coupled CFD/SYS
TH computational framework, the following problems occur: (1) lack of data: more details
are needed for a 2D analysis than for a 1D; (2) 2D and 3D situations imply more difficulties
in gathering experimental data suitable for validation than in the case of 1D; (3) sensitivity
analysis and uncertainty evaluation techniques and approaches; (4) when the governing
equations change (case of CFD analyses), problems at the interface can occur: e.g., in open
and porous medium approach, the interface between REV-averaged equation and RANS
equation may reveal inconsistent; in Zonal Hybrid RANS-LES models problems are
expected at the interface between RANS and LES regions.
l
Multiphase interface. In multiphase modeling, large difference in results may occur,
depending on whether the interface is treated statistically or deterministically: the statistical
approach requires a large modeling effort; the deterministic approach typically requires
enormous CPU resources.
l
Simplification. The simpler is the model and the approach, the easier is the validation
process. However, basic assumptions (simplifications) need justification, e.g., that the
simplification would not affect the main physics. Then we have to know what the key
phenomena are and what mechanism is important a priori (i.e., before performing the
analysis). Furthermore, the effect of simplification should be traceable during the entire code
application.

### 12.7.3 Selection of physical models

l
Selecting basic model options for two-phase flow CFD application. In the case of two-phase
flow application, Bestion (2012) proposes the following steps: specify (1) the time and space

<!-- page 753 (PDF 25) -->
resolution of the simulation; (2) the choice of a number of fields; (3) the list of wall transfers
(mass, momentum, and energy), which may play a significant role in the whole process; (4)
the list of interfacial and interfield transfers (mass, momentum, and energy) which may play
a significant role in the whole process; and (5) the list of turbulent transfers (mass, momentum
, and energy) which may play a significant role in the whole process;
l
Selection of physical models in CFD NTF applications. The following items should be
considered:
−
Understanding of physical phenomena involved and understanding of CFD models and
capabilities: the phenomena should be consistent with the capabilities of the models.
−
Physical models that are expected (i.e., known) to capture the main physical phenomena
must be available.
l
Single-Phase CFD: The most important methodological factors in the single-phase CFD are
turbulence model and computational grid. We may consider the following unavoidable steps
or options in relation to turbulence modeling.
If we start from Navier-Stokes equations we have (standard symbols are used, see also
Chapter 5):
∂ui
∂t + ∂uiuj
∂xj
= ·1
ρ
∂p
∂xi
+ ν∂2ui
∂x2
i
(12.1)
Filtered or time-averaged Navier-Stokes equation:
∂⟩ui
∂t + ∂uiuj
∂xj
= ·1
ρ
∂⟩p
∂xi
+ ν∂2⟩ui
∂x2
j
(12.2)
Putting uiuj = uiuj + ⟩ui⟩uj · ⟩ui⟩uj and rewriting:
∂⟩ui
∂t + ∂⟩ui⟩uj
∂xj
= ·1
ρ
∂⟩p
∂xi
+ ∂
∂xj
ν∂⟩ui
∂xj
· uiuj · ⟩ui⟩uj
□
□
□
□
(12.3a)
∂⟩ui
∂t + ∂⟩ui⟩uj
∂xj
= ·1
ρ
∂⟩p
∂xi
+ ∂
∂xj
ν∂⟩ui
∂xj
·τRS
ij
□
□
(12.3b)
or
∂⟩ui
∂t + ∂⟩ui⟩uj
∂xj
= ·1
ρ
∂⟩p
∂xi
+ ν ∂⟩ui
∂x2
j
·
∂τRS
ij
∂xj
(12.3c)
where
τRS
ij □
uiuj · ⟩ui⟩uj = u0
iu0
j Reynolds stress
ð
Þ for time·averaging
uiuj · ⟩ui⟩uj Subgrid·scale stress
ð
Þ for filtering
□
Note:
Reynolds decomposition (for time-averaging only) gives:

<!-- page 754 (PDF 26) -->
uiuj = ⟩ui + u0
i
□
□
⟩uj + u0
j
□
(
= ⟩ui⟩uj + u0
i⟩uj + u0
j⟩ui + u0
iu0
j
= ⟩ui⟩uj + u0
i⟩uj + u0
j⟩ui + u0
iu0
j
= ⟩ui⟩uj + u0
iu0
j u0
i = u0
j = 0; ui or uj = const; ⟩c = c
□
(
(12.4)
Decomposition of variables:
fi = ⟩f i + f 0
i
=
Average component + fluctuation component for Reynolds decomposition
Resolved component + Unresolved component for LES decomposition
□
If we start from momentum equation:
∂tρui + ∂jρuiuj = ·∂ip + ∂jτij
(12.5)
Filtered or time-averaged Navier-Stokes equation:
∂tρ⟩ui + ∂jρuiuj = ·∂i⟩p + ∂jτij
(12.6)
Rewriting, we get:
∂tρ⟩ui + ∂jρ uiuj · ⟩ui⟩uj + ⟩ui⟩uj
□
□
= ·∂i⟩p + ∂jτij
(12.7)
For RANS, overbar means time averaging. Introducing the Reynolds decomposition:
fi = ⟩f i + f 0
i
∂tρ⟩ui + ∂jρ ⟩ui⟩uj + u0
iu0
j
□
(
= ·∂i⟩p + ∂jτij
(12.8)
RANS equation:
∂tρ⟩ui + ∂jρ⟩ui⟩uj = ·∂i⟩p + ∂jðτij · ρu0
iu0
j
|ffl{zffl}
Reynolds
stress
Þ
(12.9)
For LES, overbar means filtered integration.
Filtered equation:
∂tρ⟩ui + ∂jρ⟩ui⟩uj = ·∂i⟩p + ∂jðτij ·ρ uiuj · ⟩ui⟩uj
□
□
|fflfflfflfflfflfflfflfflffl{zfflfflfflfflfflfflfflfflffl}
subgrid-scalestress
Þ
(12.10)

<!-- page 755 (PDF 27) -->
Some of the possible (multiple and theoretically based) directions for CFD
solutions-calculations-applications can be understood by comparing Eqs. (12.3c),
(12.6), (12.9), and (12.10).

### 12.7.4 Turbulence models

The following statements provide a picture in relation to turbulence models, e.g., see
mainly Smith et al. (2015), then, Rotta (1972), and Roelofs et al. (2013).
−
CFD simulations of NRS problems almost always involve turbulent flow conditions. However
, laminar situations may occur (even for short time) during the simulation of a “turbulent
scenario” (e.g., flow reversal conditions in RCS).
−
The turbulence community has assembled and classified a large selection of generic flow
situations (jets, plumes, flow through tee junctions, swirling flow, etc.), and made recommendations
of which turbulence models are most appropriate. Care is needed to ensure that
in NRS applications the turbulence model has been chosen appropriately.
−
CFD is not capable, for the time being, of modeling entire reactor systems, which means that
sections of the system must be isolated for CFD treatment. The range of scales can be large
(e.g., in containments), and/or the flow phenomena rather special (e.g., ECC injection). It is
necessary to extend the database of recognized flow configurations to include those particular
conditions and build a suitable validation database.
−
In most industrial applications of CFD, RANS models are employed. However, due to the
averaging procedure, information is lost, which has to be fed back into the equations via an
appropriate turbulence model. The lowest level of turbulence models offering sufficient
generality and flexibility are two-equation models. They are based on the description of
the dominant length and timescale by two independent variables. More complex models
have been developed, and offer more general platforms for the inclusion of physical effects.
The most complex are second moment closure (SMC) models. Here, instead of two equations
for the two main turbulent scales, the solution of seven transport equations for the independent
Reynolds stresses and one length (or related) scale is required.
−
The challenge for the user of a CFD method is to select the optimal model for the application
at hand from the models available in the CFD method. It is not trivial to provide general
rules and recommendations for the selection and use of turbulence models for complex applications
. Two equation models offer a good compromise between complexity, accuracy, and
robustness. The most popular models are the standard k-ε model and different versions of the
k-ω model. However, the latter shows a severe free-stream dependency, and is therefore not
recommended for general flow simulations, as the results are strongly dependent on the
user input.
−
An important weakness of standard two-equation models is that they are insensitive to
streamline curvature and system rotation. Particularly for swirling flows, this can lead to
an overprediction of turbulent mixing and to a strong decay of the core vortex. There are
curvature correction models available, but they have not been generally validated for complex
flows. On the other hand, SMC models are much less robust; they are often recommended
to perform a first simulation based on the k-ε model and use this as a starting
point for the SMC approach. However, such an approach is hardly feasible for transient simulations
, which are usually required for NRS applications.
−
The first alternative to RANS is URANS (Unsteady RANS) or VLES (very large eddy simulation
). The former is more descriptive of the actual technique of application: i.e., to carry

<!-- page 756 (PDF 28) -->
out an unsteady RANS analysis, even if the boundary conditions are steady. Thus, if
steady-state RANS calculation does not converge, it may be that some unsteady behavior
is present in the flow, such as periodic behavior, plume or jet meandering, and vortex shedding
. A URANS calculation can often identify the unsteady component, but it has to be
remembered that averaging over all turbulence scales remains implicit in the method, and
may not be appropriate to reliably capture the nonsteady phenomena.
−
The amount of information to be provided by the turbulence model can be reduced if the
large time and length scales of the turbulent motion are resolved explicitly. In LES, the equations
are filtered over the grid size of the computational cells. All scales smaller than that
provided by the resolution of the mesh are modeled using a suitable subgrid scale (SGS)
model, and all scales larger than the cells are computed explicitly. Away from boundaries,
LES appears trustworthy, even with very simplistic SGS models, such as Smagorinsky. In
the wall regions, pure LES becomes very inefficient due to the need to scale the lateral
dimensions in the same way as in the normal direction to capture the smaller scale eddies.
This is not necessary in RANS because the mean flow parallel to the wall changes much less
abruptly than in the normal direction. Also, lack of sophistication of the SGS models may be
tolerated in the bulk flow, but near walls the SGS stresses become much more important, and
need to be accounted for accurately.
−
An alternative to a full LES application is to entrust the entire boundary layer treatment to a
RANS model for the “attached” eddies and only use LES away from the walls where the
eddies are “detached.” This approach has become known as detached eddy simulation
(DES) and leads to considerable savings in CPU time. The case for continued use of LES
in near-wall regions, probably in combination with a more complex SGS model, has to
be judged in terms of possible information lost using DES versus the extra computational
effort. This remains an active research area, particularly in the aerospace industry.
−
The scale-adaptive simulation (SAS) model is a hybrid approach similar to DES, but
operates without an explicit grid dependency. The controlling parameter is the ratio of
the turbulent length scale L, for example, derived from the two-equation k-kL RANS model
of Rotta (Rotta, 1972) and the von-Karman length scale LvK, which is determined in the
usual way from the first and second velocity gradients. In regions where the flow tends
to be unstable, LvK is reduced, increasing the length scale ratio, L/LvK. This leads to a
reduction in the eddy viscosity. The flow will become more unstable, and hence transient
in these regions, with vortices down to the scale of the local grid size being resolved,
resulting in a LES-like behavior. In stable flow regions, LvK remains large, which leads
to high values for the eddy viscosity. In these areas, the model acts like a RANS model.
Due to the model’s ability to resolve the turbulent spectrum, it is termed a
“scale-adaptive simulation” model. It has similarities to the DES model, but has the advantage
that it is not based on the local grid size and therefore avoids grid sensitivity problems.
−
As way of illustration, the picture in Fig. 12.4 shows how each approach to turbulence
modeling is expected to capture an instantaneous velocity signal, produced experimentally
or using direct numerical simulation (DNS).
−
As a general observation, LES simulations do not easily lend themselves to the application of
grid refinement studies, for either the time or space domains. The main reason is that the
turbulence model adjusts itself to the resolution of the grid. Two simulations on different
grids may not be compared by asymptotic expansion, as they are based on different levels
of the eddy viscosity and therefore on a different resolution of the turbulent scales. From a
theoretical standpoint, the problem can be avoided if the LES model is not based on the grid
spacing but on a prespecified filter width. This would allow grid-independent LES solutions
to be obtained. However, LES remains a very expensive approach to turbulence modeling,

<!-- page 757 (PDF 29) -->
and systematic grid and time step studies too prohibitive, even for a prespecified filter. It is
one of the disturbing facts that LES does not lend itself naturally to the application of BPGs.
−
Note: when the laminar and turbulence transitions exist, large-scale unsteady flow conditions
occur (e.g., flows in a tight rod bundle), causing specific problems in modeling.

### 12.7.5 Characterization of turbulent situations

Various turbulent situations may occur. An attempt is made below to characterize
some situations.
l
Turbulent flow types/classifications (1): Depending on turbulent flow types, suitable turbulence
models are different. The model may depend on whether the flow is stable or unstable
and whether the unstable flow is local or global (see e.g., Menter, 1992; Menter, 1994;
Menter and Esch, 2001; Menter et al., 2003a; Menter et al., 2003b; and Menter and
Egorov, 2005). However, it is not easy to categorize turbulent flows in many NTF problems;
coexistence of several types of turbulence situations affecting one another may occur. Steady
RANS can be used to scale or to resolve different turbulent situations.
−
Example: difficulties in classifying the turbulent flow type in NTF problems, the
T-junction mixing problem.
The flow condition in the case of T-Junction is not easily categorized into one of the
three recognized groups: stable, globally unstable, and locally stable. In principle, it
can be computed with SAS and DDES models in SRS mode. This means that the instability
in the interaction zone between the two streams is sufficiently strong to generate
unsteady resolved turbulence. However, it was also observed that these simulations are
extremely sensitive to the details of the numerical method employed or the shielding
function used. The SAS model provided “proper” solutions only when a pure Central
Difference scheme was selected, but went into URANS mode in the case of the Bounded
Central Difference scheme. The DDES model provided correct solutions when a nonconservative
shielding function is used but produces only weak unsteadiness in the case
of a conservative shielding function. It is therefore recommended to apply the ELES
model, where modeled turbulence is converted into synthetic resolved turbulence in both
pipes upstream of the interaction zone at predefined RANS-LES interfaces. In addition,
the turbulence model is switched from SST to WMLES at these interfaces. This then
Reynolds number
Physics
Computational cost
DNS
LES
E (k)
Wave number
Hybrid: RANS/LES
RANS
Modeled
Resolved
DNS computed
LES computed
LES computed
RANS modeled
LES
DNS
LES
Hybrid
RANS
RANS
Fig. 12.4 CFD modeling approaches (Roelofs et al., 2013).

<!-- page 758 (PDF 30) -->
avoids the need for the flow instability of the interacting streams to generate resolved
scales (Menter, 1994).
l
Turbulent flow types/classifications (2): One choice may be to consider the issue both for
single and global effects. Indeed, the rather complex configurations arising in industrial
situations have led people to consider canonical situations that may be identified in industrial
flows.
(1) The first level of complexity consists of flows dominated by a single and identified
phenomenon and a single and identified regime for a given identified geometry. Usual
isolated effects lead to the consideration of: simple shear flows (attached shear flows
(boundary layer, wall jet); free shear flows (mixing layers; wake; plume, plane or round
jets); impinging flows. The related regimes may be stably (unstably) stratified flows,
flows dominated by buoyancy leading to mixed or natural convection, or forced convection
. Geometries are rather simple ones and may refer to canonical configurations
including plane wall; round tube; plane or round jets; the related flows are driven by
a nearly two-dimensional strain.
(2) The second level of complexity includes configurations with secondary flows, and
configurations with a strong coupling between turbulence and another key physical
phenomenon such as rotation or chemical processes (e.g., combustion). This also
includes flows with strong turbulence state variation (transition between laminar and
turbulence state or occurrence of unsteadiness that cannot be considered as fully developed
turbulence).
(3) Strong Unsteady Flows: The two previous items mainly refer to steady flows. More
complex flows involve strongly unsteady flows for which the timescale of variations
is of the order of turbulence time. Unsteadiness may originate from unsteady boundary
conditions; from flow separations, from coupling between turbulence, and from other
phenomenon (e.g., acoustics or material vibrations). These circumstances are seldom
compatible with the hypotheses of turbulence modeling and the predictive capacity
of this latter will be very difficult to access, see e.g., Mahaffy et al. (2007a,b) and
OECD/NEA/CSNI/R(2014)3 (2014).
l
Coexistence of turbulent and laminar flows and turbulence-laminar transitions. T-junction
mixing problems with low ratio of branch to main pipe flow rate may occur when branch
flow is due to the leak from the valve. In these conditions the flow in branch pipe is laminar
and the main pipe flow is turbulent. Laminar to turbulent transition occurs around the mixing
zone. For modeling purposes, turbulence model should cover laminar, turbulent, and
transition regions. In such situation: (a) if one applies the Smagorinsky SGS model, even
if the flow is laminar, the second invariant of the strain rate tensor is large near the wall
and the eddy viscosity exists; (b) in WALE model, in pure pipe shear flows, the eddy
viscosity vanishes (this situation is ensured only in the simple pipe-like flows: for laminar
flows with complex 3D velocity gradient this is not ensured; in this case, dynamic turbulence
model should be considered).
l
Wall function. Wall function is based on the streamwise flows in attached boundary layer
parallel to the channel wall; thus, when flow separation or impinging occurs we cannot
ensure the accuracy of the results. For these cases, strict evaluation should be performed.
Note that it does not necessarily mean that the wall function does not work for these cases
(e.g., for the rod bundle problem the pressure loss across the grid can be predicted accurately
using the wall function). Definitely, the important point when we evaluate the wall function
is to use right condition for the first y+.
l
Statistically steady (stable) vs. unsteady (unstable): Although turbulent flow is unsteady,
steady RANS model can be successfully applied to problems with statistically steady

<!-- page 759 (PDF 31) -->
turbulent flows (or stable flows). However, there is a region where large-scale unsteady flow
is dominant and is related to target region and variables. In these cases, we should consider
unsteady turbulence models. For globally unstable flows, even unsteady RANS can capture
the physics, but shows large errors. For locally unstable flows RANS cannot capture the
unstable flows, thus requiring the use of scale-resolving simulation models (SAS, Hybrid
RANS-LES, LES);
l
3D CFD models (Bestion, 2008):
The question marks arising for identifying and classifying CFD models can be derived from
Fig. 12.5.
l
Two-phase CFD. According to Bestion (2012), two-phase CFD is a promising way for
extending the simulation capabilities for many nuclear reactor thermal-hydraulic issues.
However, this is a rather new technology and a long effort is still required before reaching
a good maturity and reliability of the tools and application methods. Various methods exist
and many modeling options are offered to users but only some combinations of options
constitute physically consistent approaches, see e.g., Fig. 12.6. Scientists who wish to
develop new applications of two-phase CFD and analysts who must evaluate these applications
should consider the classification of various modeling approaches. Clear identification
of the simplifying assumptions and range of applicability of each approach and consistency
checks are needed. Specific checklists for applications of two-phase CFD to nuclear reactor
thermal-hydraulic issues are needed (e.g., considering Fig. 12.6).

### 12.7.6 Coupling

In many nuclear thermal hydraulics application the CFD codes and models are applied
(and are applicable only) in combination with other numerical tools including primarily
SYS TH codes. This originates the issue of “coupling” discussed below. Multiphysics
and/or multiscale coupling can be considered.
−
Multiphysics coupling. Examples are (i) neutron physics and CFD in core analysis; (ii) crud
deposition and growth: CFD, chemistry, and (possibly) neutron physics are needed;
One phase for porous body
Single-phase
C
F
D
?
C
M
F
D
?
Two-phase
Two-fluid for porous body
Two-fluid for open medium
Two-fluid+LES+LIS+ITM??
Two-phase pseudo-DNS with ITM
LES+ITM
One phase RANS models
One phase LES models
One phase DNS models
Fig. 12.5 Classification of 3D CFD models (Bestion, 2008).

<!-- page 760 (PDF 32) -->
(iii) T-junction mixing: CFD and structural analyses should be connected. What is needed in
those situations is a clear understanding of the CFD roles (as already mentioned in the
text above).
−
Multiscale coupling. CFD codes’ capabilities in predicting mesoscale phenomena may be
linked to SYS TH codes capabilities in predicting macroscale phenomena. As already
discussed above in this chapter, this needs: (i) identification of space region in RCS or
RPV for CFD application; (ii) identification of CFD computational domain and/or CFD isolation
; (iii) identification and characterization of BIC. The characterization of BIC may
reveal a problem because information needed for CFD running is not available for the space
outside the CFD computational domain (BIC affects noticeably the CFD results into the CFD
domain).
−
Multiscale and multiphysics coupling. This is the combination of the above two.
l
Example-1, notes in multiphysics coupling – CFD application range. In crud modeling
problem, CFD plays a role in providing rod surface temperature. The typical assumptions
used are that flow is single-phase and the geometry change due to crud deposit growth is
negligible. However, the surface roughness and the equivalent diameter of the region
may change with the presence of crud. This may affect flow pattern, pressure drops, and local
heat transfer coefficient, and thus local temperature field. All of this may also generate secondary
flows (the circumferential gradient of axial velocity generates the secondary flows)
which may not be considered by the application.
l
Example-2, nuclear reactor core behavior. The following areas are concerned: neutron
physics, thermal fluids (CFD part), fuel performance, chemistry, crud formation and induced
Corrosion, CILC, structural mechanics, materials, and reactor physics (including core
control). A synthetic outline of the concerned topics can be derived from Figs. 12.7 and
12.8 (Kothe et al., 2010; Kothe, 2011; Kothe, 2015).
Multiphase CFD methods with turbulence
Fluid-fluid interface & exclusion of porousmedium
approach
(Quasi-or pseudo-)DNS
LES
RANS
No averaging / filtering;
1 fluid
Deterministic
interface
Deterministic
interface
(all interface)
Filtered and
statistical
(interface)
Statistical interface
(small bubbles or
droplets)
Statistical
interface
(all interfaces)
ITM
Fronttracking

ITM
DNS: Direct numerical simulation
LES: Large eddy simulation
ITM: Interfacial tracking method
ICM: Interfacial capturing method
ALE: Arbitrary Eulerian-Lagrangian
VOF: Volume-of-fluid
ICM
ALE
(moving
mesh)
Level set
VOF
Phase-field
model
ICM
(marker-field)
Filtering/space-averaging;
1 or 2 fluid
Ensemble or time-averaging;
2 fluid
Fig. 12.6 A view of multiphase CFD methods (Bestion, 2012).

<!-- page 761 (PDF 33) -->
### 12.7.7 CFD assessment: V&V and UQ

l
V&V
International or National institutions (in the latter case, looking at an international
consensus) deal with V&V and UQ, see e.g., the three elements diagram in Fig. 12.9
(AIAA, 1998).
Neutronics
Thermal
hydraulics
Structural
mechanics
Reactor system
Fuel performance
(diffusion,
transport)
(thermo-mechanics,
materials models)
Chemistry
(crud formation,
corrosion)
Multiresolution
geometry
Mesh motion/
quality
improvement
Multiphysics
integrator
Multimesh
management
(thermal fluids)
– Not a single
   executable
– Both legacy
   and new capability
– Both proprietary
   and distributable
Flexible coupling
of physics
components
•
• Toolkit of components
– Diversity of models,
   approximations,
   algorithms
– Architecture-aware
   implementaions
• Scalable from high-end
   workstation
   to existing and future
   HPC platforms
• Development guided
   by relevant challenge
   problems
• Broad applicability
• Attention to usability
• Rigorous software
   processes
• Fundamental focus
  on V&V and UQ
Fig. 12.7 The CASL virtual reactor: a code system for scalable simulation of nuclear reactor
core behavior (e.g., Kothe, 2015).
Lattice physics + nodal diffusion:
Current workhorse (Westinghouse)
Deterministic transport: PARTISn (LANL),
Denovo (ORNL), DeCART (UMichigan)
VIPRE-W: Current subchannel
flow workhorse (Westinghouse)
ARIA (SNL), NPHASE (RPI):
Initial 3D flow capability
SIERRA (SNL)
RELAP5 (INL)
CASL developers have delivered code for production (not just research)
–  ORNL and LANL codes account for almost 80% of RSICC distributions since 2005
Monte Carlo transport: MCNP5 (LANL),
SCALE/KENO (ORNL)
Fuel performance
(thermo-mechanics,
materials models)
Thermal
hydraulics
(thermal fluids)
Neutronics
(diffusion,
transport)
Reactor system
Structural
mechanics
Chemistry
(crud formation,
corrosion)
Multiresolution
geometry
Mesh motion/
quality
improvement
Multimesh
managemant
LIME
multiphysics
integrator
FALCON: Current 1D/2D
workhorse (EPRI)
BISON: Advanced 2D/3D
capability (INL)
AMP FY10: Initial 3D
capability (NEAMS)
BOA: Current
CRUD and
corrosion
workhorse
(EPRI)
•
•
•
•
•
•
•
•
•
•
•
•
Fig. 12.8 The CASL virtual reactor (VR) builds on a foundation of mature validated and widely
used software (e.g., Kothe, 2015).

<!-- page 762 (PDF 34) -->
Performance-based V&V capability. It is infeasible to apply system code level V&V
strategies to CFD. New methodologies are required. When planning a “new” V&V methodology
, for any code prediction, the first question one might ask is whether or not we can trust
the prediction for the intended purpose. The issues outlined above provide some of the areas
where legitimate questions regarding the validity of the solution must be explored. When
dealing with problem-specific models with a history of benchmarking and analysis, other
concerns can be outlined. If compromises or simplifications are needed for a practical
solution and assumptions are made to fill gaps in one’s knowledge about boundary conditions
or modeling approaches, what is the impact on the final results? All of these concerns,
as well as concerns related to verification, such as ASME standard V&V 20 (ASME, 2009)
provide methods for estimating uncertainties but are very expensive to follow for large and
complex scenarios. In some cases, the test data sufficient for the task of validation are not
available and it is common for compromises to be made in the area of verification and
validation. Estimates of uncertainty are commonly limited in scope and based on only a
subset of potential uncertainties. It can be difficult to determine whether or not the predictions
are adequate if the uncertainty is not quantified. Methods to determine whether or not a
code is adequate for a given analysis and the methods for determining the uncertainty are
common considerations for nuclear safety analysts (e.g., see Theofanous et al. (1984),
Nourbakhsh and Banerjee (2013), and Banerjee (2013)). When discussing these methods
for CFD applications, additional practical concerns come into play. Many analyses are
completed using large computer systems and significant amounts of CPU time. Methods
to propagate uncertainties with systematic approaches such as Monte Carlo methods or even
Real
world
(experiment)
Mathematical
model
Code
Code
V & V
of
CFD code
Model
qualification
Discrete numerical
approximation
Empirical &
theoretical
approximation
Analysis
or
simulation
validation
verification
Computer
code
V & V
of
CFD code
Fig. 12.9 Verification and validation (V&V) in CFD (AIAA, 1998).

<!-- page 763 (PDF 35) -->
the more efficient Latin Hypercube sampling approaches can become impractical for many
CFD models due to the large computational requirements. Efficient techniques to estimate
uncertainty for nuclear safety CFD analyses need to be demonstrated (Boyd, 2016).
l
UQ
Discussion about UQ for CFD calculation started more recently within the international
community. Elements and descriptions of activities in progress can be derived from
Bestion et al. (2016).

### 12.7.8 CFD experiments

l
Overview of experimental data for validation. The following checklist applies (Bestion,
2012).
(1) Check whether available experimental data cover all basic flow processes identified in
phenomena-identification process. If required, plan and design new experiments to
cover all processes.
(2) For two-phase flows, check that the available experimental data cover all important wall
transfers, interfacial transfers, and turbulent transfers identified in phenomenaidentification
process. Check that they can be used to validate all important transfer
models in a separate effect way. If required, plan and design new experimental programs
in order to be more exhaustive.
(3) Check that the instrumentation and the experimental tests provide enough information to
get initial conditions and boundary conditions for the simulation.
(4) Check that the instrumentation and the experimental test provide sufficient local information
on flow parameters of interest to validate closure laws for wall, interfacial, and
turbulent transfers identified in the phenomena-identification process.
l
Identification/definition of CFD-grade experiments. CFD grade experiments are performed
having in mind the CFD validation. Those experiments should be discriminated from other
purpose experiments like those aiming at physics developing correlations and system code
validation (1D model). CFD-grade experiments must use nonintrusive techniques: LDV,
PIV, and PTV techniques and instruments are assumed to be available.
−
Geometry is a key issue. Specific issues are: (1) test section size; (2) boundary condition
measurements (e.g., 2D field data, mean and turbulence information needed); (3) measuring
regions and variables (target region and variables; figure of merits); (4) field data
may be needed; (5) test conditions (real vs. measurable).
−
Note-1: Simplification in designing experiments may not be simple: oversimplification
can sometimes make problem more challenging to the CFD method (see the discussion
below in relation to EPRI-NESTOR benchmark. Wall effect may become important in a
reduced size test section, e.g., wall effect in a rod bundle with mixing vane grids. (3)
A stepwise approach (bottom to top) for design of experiments is desirable, but sometimes
top-to-bottom approach can be efficient. Scaling issue must be addressed in
both cases.
−
Note-2: Different from system code scaling, local phenomenon is at the center of the
attention of CFD experiments.

### 12.7.9 Best practice guidelines (CFD application)

The use of approved/endorsed BPG is essential in NRS applications of CFD. Additional
notes are reported below.
