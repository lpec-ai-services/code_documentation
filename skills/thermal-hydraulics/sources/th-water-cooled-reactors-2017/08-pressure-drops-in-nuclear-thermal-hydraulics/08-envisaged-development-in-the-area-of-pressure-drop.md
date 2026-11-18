# Envisaged development in the area of pressure drops
<!-- source PDF pages 47-51 -->

<!-- page 539 (PDF 47) -->
The proportion of the pressure loss (due to friction) of the measured differential
pressure can be neglected, especially in small steam mass flows and higher pressure
levels compared to the height (head) component. Generally, the height (head) component
can be determined by also measuring the volumetric steam proportion using
special two-phase measuring equipment (see below, will be included). The pressure
loss proportion is the difference between the measured differential pressure and the
height (head) component determined by measuring the steam content.

### 8.6.2.3 Practical applications for differential pressure measurement in NPPs

Absolute pressure and differential pressure measurements are, in combination with the
temperature measurements, the main measuring methods used in nuclear plants, and
are used both as operating instruments and for incident instrumentation purposes. For
instance, differential pressure measurements taken via MCPs in the BWR not only
supply information about the number of operational pumps, but are also used to determine
the loop flow rate using the pump characteristic curve, as well as helping to protect
the aggregates. During commissioning tests, pressure loss measurements via other
plant parts are taken in some cases to obtain an overall picture of the total pressure loss
and establish the status of individual plant components; they are also used to confirm
computed values upon which the plant was designed.
8.7
Envisaged development in the area of pressure drops
The phenomena associated with the loss of pressure along with those associated to the
heat exchange gave rise to major technological problems since the advent of thermal
machines in the 18th century (the identification and the characterization of pressure
drops and heat transfer mechanisms came much earlier during the human civilization
history), as already discussed in the book, see also D’Auria (2012). Furthermore,
within the areas of pressure drops and heat transfer a tight connection exists between
theoretical modeling and the actual configuration of the systems.
Insights addressing the above statements can be found in this chapter and in other
parts of the book. Furthermore, Reynolds, Moody, Colebrook, Darcy, Idel’chik,
Martinelli, Nelson, etc. (see also Chapter 1 of the book), are eminent scientists whose
name is associated with the calculation of pressure drops.
The target for this section is to identify directions for possible improvements in the
knowledge in the area of pressure drops.
Looking at the future may take benefit from the view of the past. A few sentences
from the well-known, more-than 500 pages, Idel’chik Handbook (Idel’chik, 1960) are
reported:
There is, almost no branch of engineering which is not somehow concerned with the
necessity of moving fluids through pipes, conduits, or machinery. The degree of complexity
of a hydraulic or gas-air line can be quite varied. In some cases these are

<!-- page 540 (PDF 48) -->
largescale systems of pipes, gas mains, water conduits, steam pipes, air ducts, etc.,
while in other cases these are pipelines of relatively small length, but having a large
number of fittings and branches, various obstructions such as throttles and adjusting
devices, grids, protruding parts, etc. … Until recently only restricted data were available
on the subject, and these were scattered among various textbooks … and in scientific
papers. In many cases these data are contradictory or dated, and deal with only
a limited number of local resistances. Furthermore, the coefficients of local resistances
generally were given only for special geometric and physical characteristics.
In order to fill this gap, in 1954 the author published a book … We present here in the
same spirit this special handbook on the local fluid and friction resistances.
The writing of this handbook presented considerable difficulties, mainly due to the
range of local resistances, their geometric boundaries, and the states of flow in them,
which are much narrower than required by practice. Furthermore, much of the data
obtained is insufficiently accurate and reliable; this is particularly true of the coefficients
of local resistances. Therefore, it would have been better to delay the publication
of this handbook until all coefficients of local resistances could have been
checked and refined experimentally by some standard method, based on the contemporary
level of metrology. Unfortunately, it seems unlikely that such a series of
experiments would be completed in the near future.
Those words are perfectly true today, after more than half a century. Namely:
□ more experiments have been done, but their number is still much less than needed with reference
to the geometric and operating conditions of Water Cooled Reactors, specifically if
two-phase conditions are concerned; errors, which are not always documented, are the result
of experiments; measurement errors are expected to be larger in two-phase conditions;
□ computational fluid-dynamic codes have been made available which, at least in single-phase
conditions could be used to determine “all coefficients of local resistances,” but, errors in
computed results (a bit less than j10%j of the actual value) may reveal higher than precision
needs; and
□ precision targets from the side of nuclear plant designers or safety analysts have not been
fixed: these could be a function of Re number and void fraction and could be less than
j1%j of the actual value, i.e., 10 times below established computational capabilities, and possibly
much below attainable accuracy from experiments.
As defined above is the context in which an attempt is made to identify some lines of
development in the evaluation of pressure losses.

## 8.7.1 Extension of experimental database

A nonexhaustive list of key words connected with pressure drops (PD) includes:
l
Laminar or turbulent;
l
Fully developed flow or nondeveloped flow;
l
Transient or steady state and acceleration (in space or in time);
l
Compressible or incompressible fluid;
l
Single- or two-phase and (in case of two phase) two-fields or multiple fields;
l
Distributed (friction) or local (i.e., at geometric discontinuity);
l
Wall roughness;

<!-- page 541 (PDF 49) -->
l
Sharp or smooth edge (in case of geometric discontinuity);
l
Viscosity of fluid, Newtonian and non-Newtonian fluids;
l
Velocity profile (single-phase flow) or fluid velocities and void fraction profile
(two-phase flow).
The items above can be used for the design of new experiments and for planning
developments in the area: (a) to identify affecting variables-parameters and related
ranges; (b) to build one multidimensional table or several tables covering the identified
topics and the ranges of relevant parameters. It is also clear that the characterization
of items or conditions like “nondeveloped flow,” “viscosity,” “level of
smoothness,” etc., may require an infinite variety of situations. In this case an attempt
should be made to group the envisaged situations into a manageable number.
It is beyond the objective for the present book to pursue either the targets (a) and
(b) mentioned previously. To this aim, groups of experts from nuclear regulators,
designers, and scientific institutions involved with thermal-hydraulic programs should
be convened. Here in the book the importance for such an activity is recognized
and some guidelines are further provided in Section 8.6.2 in relation to specific topics.

## 8.7.2 Development in the area of two-phase flow modeling

It is clear from the picture given in the entire chapter and from the snapshot views of
previous sections that two-phase flows deserves or is expected to deserve the largest
attention as far as possible developments in the area of pressure drops are concerned.
Experimental and modeling researches in the 60s, even before the advent of computers
, demonstrated the existence of a situation as depicted in the sketch of Fig. 8.22.
mk
Δpl
k
ΔpT
 PUMP
ΔpT
LINE (All vapor)
ΔpT
LINE (Actual)
ΔpT
LINE (All liquid)
Fig. 8.22 Friction pressure
drop in horizontal channel as
a function of mass flow-rate
for the single-phase (liquid
and vapor) and two-phase
conditions.

<!-- page 542 (PDF 50) -->
Under the condition of equal mass flow rate (i.e., kg/s) the friction pressure drops for
liquid get a value much lower than in the case of steam (or gas) pressure drops. The
two-phase pressure drop curve is assumed to follow a trend bounded by the two curves
relating to single-phase conditions. Furthermore the two-phase curve does not show
up a monotonous trend and the well-known Ledinegg instability is expected.

### 8.7.2.1 Expected-desirable developments

Significant examples of expected-desirable developments, without having the target
of a systematic and comprehensive line of attack to the overall issue and assuming
proper support from the execution of experiments, are:
(A) Related to distributed pressure drops. Substitution of the two-phase multiplier approach
with an improved mechanistic approach where wall drag, interfacial drag, and flow
regimes play the key role. Fluid velocities, void fraction, absolute pressure, and
diameter-size (in addition to roughness and equivalent diameter) should be considered with
suitable ranges of variations. The new approach should directly account for nondeveloped
flow conditions.
(B) Related to local pressure drops. An attempt should be made first to distinguish among
groups of situations: e.g., abrupt area changes in a pipe-like configuration, bends, branches,
connection of pipes with reservoirs, changes in flow-path directions inside plena, component
related, special situations like interface between jet pump and DC region in BWR.
Then, for each group, key geometry related parameters should be identified. Then the
fluid-dynamic parameters should be identified with suitable ranges of variations. Finally
correlations, as far as possible of mechanistic type (i.e., considering balance equation)
should be developed dealing with functional relationships between local loss coefficients
and the parameters belonging to the different groups of situations.

## 8.7.3 Modeling improvements in TH system codes

System thermal-hydraulic codes, as discussed in Chapters 5, 9–11, 13, and 15 (balance
equations, constitutive equations, special models, structure, validation, and application
, respectively), constitute complex computational tools which can be imagined
as repositories for the knowledge in different areas of thermal-hydraulics. This also
applies in relation to the modeling of pressure drops.
The key issues related to pressure drop prediction within the validation process of
SYS TH codes, i.e., comparison between measured and calculated values, appear
to be:
l
Lack of or insufficient information about the experimental error (e.g., experimental values
are also needed to fix suitable steady-state conditions when transient calculations for closed
loop are performed);
l
Occurrence of nonfully developed flow conditions (within the code, these are dealt with by
correlations developed or qualified for fully developed flow conditions);
l
Lack or insufficient information about flow regimes or flow regimes changes;
l
Need for the code user to supply information related to local pressure drop coefficients.

<!-- page 543 (PDF 51) -->
The first two issues apply to single- and two-phase conditions and the third issue is
valid for two-phase conditions.

### 8.7.3.1 Envisaged developments

Traceable improvements for SYS TH codes imply resolving the listed issues even by
considering the developments in the areas of experiments and two-phase flow modeling
(Sections 8.6.1 and 8.6.2). Solution of the issue at the last bullet item (reduction of
user effect), may bring to the need of creating a database for local pressure drop coefficients
for NPP geometric conditions. In this connection, flow reversal conditions
(whose consideration is essential to determine system performance in case of transients
like LOCA) and component (MCPs, valves, separator dryers, accumulator lines,
etc.) local pressure drops should receive proper attention.

## 8.7.4 Trends for CFD applications

CFD development is driven by a context much wider than nuclear thermal-hydraulics
as also discussed in Chapter 12 of the book. CFD codes are widely used in various
areas of nuclear thermal-hydraulics including design and safety aspects. CFD codes
are also coupled with SYS TH codes and are used to support results of related calculations
in selected fields. A snapshot picture connecting CFD codes and pressure drops
in nuclear thermal-hydraulics can be given as follows:
(A) Validation studies (for CFD codes) focus upon three-dimensional phenomena like mixing
of different fluid streams and characterization of local conditions, namely velocities densities
or even void fraction when two-phase flows are involved; in a very few cases a check
is made that pressure drops along the fluid paths are close enough to experimental data: in
the majority of case are not even measured properly or available from experiments. Then,
CFD computational tools can be found qualified in computing three-dimensional phenomena
in case of some experiments without proving consistency with experimental data of
pressure drops in the same experiments.
(B) CFD computational tools have the intrinsic and unique capability to predict pressure drops
at geometric discontinuities: therefore it is also possible to predict the relationship between
local pressure drop coefficients in various situations and Re number. As already discussed,
this relationship constitutes an important input parameter for SYS TH codes.
Then, in some cases mesh convergence of CFD code results can be demonstrated as
part of the adoption of best practice guidelines.

### 8.7.4.1 Envisaged developments

Envisaged developments for CFD codes in the area of pressure drops can be derived,
as follows:
l
First: precision targets which are consistent with current numerical capabilities and, possibly
, with needs in nuclear thermal-hydraulics should be established, e.g., in relation to
pressure drops.
