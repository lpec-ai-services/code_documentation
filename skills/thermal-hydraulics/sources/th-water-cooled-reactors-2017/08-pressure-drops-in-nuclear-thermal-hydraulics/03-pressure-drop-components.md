# Pressure drop components
<!-- source PDF pages 4-11 -->

<!-- page 496 (PDF 4) -->
8.2
Pressure drop components
The starting point for the pressure drops equations is the theorem of the conservation
of momentum. Accordingly, the total static pressure drop, which a fluid is exposed to
flowing through a flow path in steady-state conditions, is made up of the following
components:
Δp = Δpe + Δpa + Δpf + Δp‘
(8.1)
where Δpe is the pressure drop due to static head—reversible component caused
by different heights. Δpa is the acceleration pressure drop—reversible (or partly
reversible, or reversible in principle) component caused by change in the
cross-section area or the density of the fluid. Δpf is the friction pressure
drop—irreversible component caused by shear stress on the walls. Δp‘ is the local
pressure drop—irreversible component caused by change in flow geometry and
the flow direction.
The total pressure drop is therefore made up of the reversible components of the
height (head) and (partly of ) acceleration and a permanent pressure drop (referred
to as pressure loss in the following), which in turn is made up of friction pressure loss
and local form (shape) loss. When the fluid conditions change with time the acceleration
pressure drop also includes a transient term. This term, although part of the equations
at the basis of system thermal-hydraulic codes (see Chapters 5 and 11 of the
book) has negligible impact upon the prediction of system performance in the majority
of situations of interest.
The permanent pressure drop caused by the dissipation of kinetic or mechanical
energy cannot only arise due to friction on walls and structures but also, especially
in two-phase water/steam mixtures, due to irreversible momentum exchange between
the phases.
Eq. (8.1) derived from the theorem of the conservation of momentum, also
expresses the conservation of mechanical energy along a flow path including the
reduction in energy due to dissipation.
8.3
Overview on pressure drop models
and related phenomena

## 8.3.1 Friction pressure drop

### 8.3.1.1 Single-phase flow

Modeling of friction pressure drops in single-phase flows is based on empirical
approach widely validated by experiments and theoretical data, see e.g.,
Nikuradse (1932). The irreversible pressure drop caused by sheer stress at the wall,
sometimes also called distributed pressure drop, because it occurs all along the
lengths of the flow channel, is determined by:

<!-- page 497 (PDF 5) -->
Δp = f L
Dh
□ W2
2ρA2
(8.2)
where f is the friction factor and Dh is the hydraulic diameter (equal to four times flow
area/wetted perimeter). Pressure drops across tubes, rectangular channels, and bare
rod bundles (without spacers) are typical examples for this pressure drop component.
The friction factor depends on the Reynolds number within the flow channel.
Commonly used correlations some of which are discussed in the following are applicable
to steady state fully developed flow.

#### Adiabatic single-phase flow

For fully developed laminar flow, the friction factor can be expressed as follows:
f = 64
Re
(8.3)
This is valid for Re numbers <2320.
For turbulent flow in smooth pipes a large number of friction factor correlations are
available in the literature. A few commonly used are mentioned in the following:
According to Blasius (1913), the following simple formula applies in the range:
3000<Re<105
f = 0:3164□Re·0:25
(8.4)
The Herman equation is appropriate for the higher range from Re □ 2≡104to2≡106
f = 0:0054 + 0:33964□Re·0:3
(8.5)
Colebrook and White (1937) (see also Colebrook, 1939) proposed an implicit
equation, valid for smooth and rough pipes (considering the pipe roughness e) for
the whole range of Re number above 3000:
1ffiffif
p = 0:86 ln
e=D
3:7 + 2:5L
Re
ffiffif
p
□
□
(8.6)
The explicit equation provided by Filonenko (1948):
1ffiffif
p = 1:82□ log Re
ð
Þ·1:64
(8.7)
is a good approximation of the Colebrook-White equation for smooth tubes in the
range 4≡103 < Re < 1012.
Correlations for circular pipes are normally used also for the calculation of
single-phase pressure drops in rectangular channels, in annuli and without existence of

<!-- page 498 (PDF 6) -->
experimental data also in bare rod bundles applying the hydraulic diameter concept. One
of the commonly used correlations for bare rod bundles is proposed by Kays (1975):
f = fcir □K1
(8.8)
where K1 is a function of pt/D (pitch to diameter) based on the work by Diessler and
Taylor (1956), and fcir can be calculated using correlations for circular pipes.

### 8.3.1.2 Two-phase flow

While the pressure drop in single-phase flow is characterized by the level of turbulence
, the two-phase pressure drop is connected with the momentum exchange
between the two phases and is characterized by the two-phase flow pattern.
A large number of methods for the prediction of two-phase pressure drop can be found
in the literature. The two-phase multiplier approach which is the basis for most of the
citied methods, is the generally accepted engineering model to account for the effect
of a two-phase mixture in a flow channel. The fundamental idea behind this is to calculate
the pressure drop of one phase (gas or liquid) ΔpL first. To determine the
two-phase pressure drop ΔpTP, the single-phase pressure drop is multiplied with a
two-phase multiplier ∅2
L, G to consider the influence of the second phase. The following
four basis methods to define the two-phase multiplier are commonly used:
–
two methods that assume the liquid or gas phase flowing alone in the flow channel
–
two methods that assume the entire mixture flowing as liquid or gas only.
Applying these basis definitions of the two-phase multipliers, the two-phase friction
pressure gradients can be expressed as follows:
Δp
Δz
□
□
TPF
=
Δp
Δz
□
□
Φ2
L for the liquid alone case
Δp
Δz
□
□
TPF
=
Δp
Δz
□
□
Φ2
G for the gas alone case
Δp
Δz
□
□
TPF
=
Δp
Δz
□
□
Φ2
LO for the entire mixture flowing as liquid only and
Δp
Δz
□
□
TPF
=
Δp
Δz
□
□
Φ2
GO for the entire mixture flowing as gas only
(8.9)
The ΦL
2, ΦG
2, ΦLO
2, ΦGO
2 terms constitute the two-phase pressure drop multiplier to be
determined. The numerous approaches found in the literature on the calculation of
two-phase pressure drop can be categorized into two general groups:
–
Modifications of the single-phase friction factor based on the homogeneous model
–
Empiricalcalculationsapplyingthetwo-phasemultiplierconceptbasedonseparatedflowmodel.
In addition, there are also some direct empirical models (e.g., Lombardi and
Pedrocchi, 1972). According to this approach, the two-phase pressure drop is directly

<!-- page 499 (PDF 7) -->
determined as function of mass flux, mixture density, geometry of the flow channel,
etc. without reference to a single-phase pressure drop. Furthermore flow pattern
specific models have been developed to provide flow pattern specific correlations.
Finally, it has to be mentioned that modern computer codes based on two fluid
models require additional correlations for the partitioning of the wall friction between
the two phases (wall-to-phase for each phase) and interfacial friction models. Some of
the widely used and often citied correlations are summarized in IAEA (2001), a few
typical examples are outlined in the following.

#### Homogeneous model

Applying the homogeneous model, the two-phase flow is treated as pseudo-fluid characterized
by suitable averaged properties of the liquid and gas phases. First approaches
to determine the frictional pressure drops of two-phase flow were based on modifications
of the friction factor for single-phase flow. For this approach, the two-phase
pressure drop caused by shear stress at the wall can be expressed as:
ΔpTP = fTP
L
Dh
□ W2
2ρA2
(8.10)
where fTP is the friction factor for two-phase flow and ρ is the density of the mixture.
The friction factor is calculated applying one of the equations for single-phase flow,
Eqs. (8.3)–(8.7), with the use of the mixture viscosity for the determination of the Re
number. Several two-phase flow viscosity models are available; the most common
ones have been introduced by:
McAdams et al. (1942):
μ = x
μG
+ 1·x
ð
Þ
μL
(8.11)
and Cicchitti et al. (1960):
μ = xμG + 1·x
ð
ÞμL
(8.12)
Additionalexamplesfortwo-phaseviscositymodelsfor use inthehomogeneousapproach
are givenin IAEA(2001).Manyofthesemodelsdonotleadtosignificantdifferentresults.
Homogeneous models are expected to provide good results for high mass flux flows. All
homogeneous models can also be formulated in terms of two-phase friction multipliers.

#### Two-phase multiplier for separated flow model

The frictional pressure drop in two-phase flow is typically predicted by use of
separated flow models. In the separated flow model the phases are considered to flow
separately in the flow channel each with a given velocity and capturing a certain
fraction of the channel cross-section area.
The study of two-phase pressure drop has been subject to numerous investigations
over the last six decades. Most of the developed methods are based on empirical

<!-- page 500 (PDF 8) -->
calculations applying the two-phase multiplier approach. The methods by Martinelli
and Nelson (1948) and Lockhart and Martinelli (1949) can be considered as origin of
the two-phase friction multiplier approach. Lockhart and Martinelli (1949) defined a
parameter X, known as Martinelli parameter:
X2 = ∅2
G
∅2
L
= dp=dz
ð
ÞL
dp=dz
ð
ÞG
Based on the idea of Lockhart-Martinelli other researchers have then developed
further correlations to account for specific geometry or flow conditions, e.g., see
Fitzsimmons (1964) and Friedel (1980). The Martinelli-Lockhart-Nelson approach
does not consider the interaction between the phases and does also not consider the
influence of the mass flux on the two-phase multiplier.
While the correlations developed by Baroczy (1966) and Friedel (1979) consider
the effect of the mass flux on the two-phase multiplier, the method introduced by
Chisholm (1973), see also Chisholm (1968) and Chisholm and Sutherland (1969)
accounts for the interaction between the phases.

### 8.3.1.3 Conclusive remarks

A not comprehensive (as already mentioned) overview of friction pressure drops has
been given in this section. Additional snapshot like information which may be useful
for the reader for connecting friction pressure drop with different topics in the book or
in applications of nuclear thermal-hydraulics are listed in the following.
l
All textbooks in nuclear thermal-hydraulics (see references in Chapters 1 and 2 of the
book) provide key information about pressure drops. A pioneering, still valid and applicable
document, mostly focusing upon local pressure drops, is by Idel’Chik (1960) (see
also Idel’chik, 1979), and a more recent effort to summarize current technological
understanding in the area of water cooled nuclear reactors has been performed
within the framework of the International Atomic Energy Agency (IAEA) activities
(IAEA, 2001).
l
The principle approach to the calculation of friction pressure drops is based upon the definition
of “τw” as mentioned in Chapters 5 and 11 of the book (see also Chapter 9 of the
book). The approach suffers from the difficulty in determining the derivative of fluid velocity
in the direction perpendicular to the wall where the friction is acing. The difficulty occurs
for Newtonian fluids and may reveal higher in the case of non-Newtonian fluids. Computational
fluid dynamics (CFD) codes or approaches (see Chapter 12 of the book) did not
get rid of the problem so far. The engineering approach, widely used is based upon the definition
of “f” (friction coefficient) and the computation of hydraulic diameter and Re number
(also function of the hydraulic diameter).
l
The concepts equivalent diameter, and the situations “fully developed flow” and “laminar or
turbulent velocity profile” in the cross sections, largely affect the computation of friction
pressure drops. The related evaluations are not immune by errors and approximations
(Del Frate et al., 2016) (see also the Ph.D. Thesis, Del Frate, 2016). Furthermore, the condition
fully developed flow is needed to establish any meaningful/qualified correlation (e.g.,
for the friction coefficient); however, in no region of a water cooled reactor [either

<!-- page 501 (PDF 9) -->
pressurized water reactor (PWR) or boiling water reactor (BWR), with the exception of the
primary side of vertical parts of tubes in steam generators (SGs)] fully developed conditions
occur. So errors are expected in any calculation of practical interest: this is an issue which
generates the need for uncertainty quantification (Chapter 13 of the book).
l
Experimental data are definitely needed to circumvent the limitations and deficiencies outlined
in the previous bullet items. However experimental data are not immune of problems:
measurement errors, reproducibility of test conditions, and of measured data and lack or
insufficient knowledge of boundary conditions are reasons which give rise to the scatter
of data; this requires an interpretation by the analysts. Powerful statistics based methods
are available which do not reduce to zero the arbitrariness, e.g., when formulating a correlation
(for instance, the exclusion of singular points which do not fall into a selected category
may not be based upon fundamental principles of physics).
l
The validity range for a correlation is at the origin of an additional problem for any empirical
model based upon the analysis of experimental data. A strict interpretation of the information
from a correlation would imply the use of the assigned correlation only within the ranges of
parameters which are used to develop or to qualify the correlations. However, if one
considers the following:
–
combinations of the ranges of parameters (typically, many more than three parameters
appear explicitly or implicitly, including boundary and initial condition values) used for
development or available to demonstrate the qualification level of the correlation,
–
expected ranges of interest in water cooled reactors, namely high pressure and large
geometry,
the only applicable conclusion is that the concerned correlation is no applicable for
predictions in water cooled reactor conditions. This constitutes the subject for scaling
analysis and contributes to the uncertainty expected for any calculation (see
Chapter 13 of the book).

## 8.3.2 Local pressure drop

When local obstacles, connected with flow area and/or flow direction changes occur in
the flow channel, additional irreversible pressure losses, so called local or form losses,
have to be considered.
Pressure drop across area changes (abrupt or continuously), bends, valves, elbows,
tees, etc. are typical examples. In case of NPPs, the geometries of main interest for
local pressure drop are the spacer grids, tie plates and any transition zones between
individual components which are connected with change in flow area (e.g., SG
U-tube inlet/exit or various bypasses in the PWR RPV) or change in flow direction
[e.g., hot leg to SG inlet chamber, loop seal (LS) bends].
The local pressure drop is generally given by:
Δp = K W2
2ρA2
(8.13)
where K is the local loss coefficient which is different for single-phase and two-phase
flows and depending on geometrical details of the obstacle.

<!-- page 502 (PDF 10) -->
### 8.3.2.1 Area changes

####  Single-phase flow

One of the common flow obstacles is a sudden cross-sectional area change. Fig. 8.1
shows the flow structure for a single phase flow through a sudden expansion.
Turbulent recirculation flow zones with mechanical energy losses are formed
behind the opening of the cross-sectional area. After a transition lengths (8 to 10 times
the larger tube diameter) behind the enlargement, the flow is again fully developed
(VDI Heat Atlas, 2010). Based on a balance of mass, momentum, and kinetic energy
and applying the Bourda-Carnot assumption, the irreversible local pressure loss can be
expressed as follows:
Δp =
1·A1
A2
□
□2 ρu2
(8.14)
and according to Eq. (8.13) the local loss coefficient is as follows:
K =
1·A1
A2
□
□2
(8.15)
Eq. (8.15) is valid for turbulent flow. Loss coefficients for the pressure drop in laminar
flow have been presented by Kays, 1950.
The flow process at a sudden contraction can be treated in a similar way with the
exception that an additional effect has to be considered. Behind the point of area
reduction, the flow continues to contract and forms a so called vena contracta at
location C in Fig. 8.2.
Fig. 8.1 Flow through sudden expansion.
Fig. 8.2 Flow through sudden contraction.

<!-- page 503 (PDF 11) -->
The local pressure loss and the loss coefficient can be expressed as follows:
Δp =
1·A2
Ac
□
□2 ρu2
(8.16)
K =
A2
Ac
·1
□
□2
(8.17)
The smallest flow cross-section area Ac is not exactly known and is an empirical function
of A2/A1.

#### Two-phase flow

The “K” factor in two-phase flow is a function primarily of geometric characteristics
of the system (this is at the origin of the definition of form loss factor for “K”) and of
void fraction, other than fluid velocity or Re number. Related correlations have necessarily
an empirical nature (see, e.g., Van Rooyen and Thome, 2013). The following
should be considered before application:
(1) range of validity, part 1: range of void fraction used in the experiment is important together
with the number of boundary values used for void fraction: in other terms, extrapolation of
“K” between two void fraction measurement is not appropriate when the distance between
two points is greater than 0.05;
(2) range of validity, part 2: the way to measure void fraction and the experimental error in the
measurement should be documented;
(3) flow reversal condition in the same geometrical configuration may give rise to a dramatically
different dependence of “K” upon void fraction and Re than measured for direct flow;
(4) use of the correlation shall be connected with a suitable model to predict void fraction (i.e.,
consistent with the model used to generate the correlation).

### 8.3.2.2 Conclusive remarks

Pressure drops at geometric discontinuities either in single- or two-phase conditions
are currently modeled by the application of empirically based coefficients. Assumptions
are needed to determine those coefficients from experiments and, usually, no
dependence is available from Reynolds number and void fractions: the impact
of assumptions and of the lack of specification of dependencies upon results of prediction
is unknown. This may largely contribute to the uncertainty of system
thermal-hydraulics (SYS TH) code predictions, as already discussed in Chapter 1
of the book.

## 8.3.3 Acceleration pressure drop

The following topics are relevant for acceleration pressure drops (see also
IAEA, 2001):
l
Acceleration pressure drops may occur in steady-state flow conditions.
l
Acceleration pressure drops are zero in case of steady flow of incompressible fluid.
