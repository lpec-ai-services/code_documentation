# Modeling of pressure drops and applications in TH system codes
<!-- source PDF pages 38-42 -->

<!-- page 530 (PDF 38) -->
8.5
Modeling of pressure drops and applications
in TH system codes

## 8.5.1 SYS TH code modeling

SYS TH codes constitute the tip of the pyramid of knowledge in nuclear
thermal-hydraulics as discussed in different chapters of the book. Insight into the code
modeling can be found in Chapters 5, 10, and 11), including the modeling for pressure
drops (i.e., the momentum equations). A few comments about modeling features are
provided hereafter rather than insights into the features (noticeably including numerical
aspects) of the pressure drop models.

### 8.5.1.1 Wall friction

Making reference to the Relap5 code, the wall friction model consists of two main
parts:
–
Computing the overall two-phase friction pressure drop,
–
Apportioning the total wall friction into liquid and vapor components.
The wall friction model is based on a two-phase multiplier approach calculated from
the HTFS-modified Baroczy correlation, which is independent of flow regime. The
individual phasic wall friction components are calculated by apportioning the
two-phase friction between the phases using a technique derived by Chisholm from
the Lockhart-Martinelli model. The calculated phasic factors depend on flow regimes.
Comments are as follows.
Plot from a time series of 22,000 s after
neglecting initial transients
−30
−0.2
−0.1
0.0
Flow rate (kg/s)
0.1
0.2
−20
−10
ΔP (Pa)
Fig. 8.20 Characterization of an instability event: pressure drop versus mass flow rate
(Vijayan and Nayak, 2012).

<!-- page 531 (PDF 39) -->
l
Notwithstanding highly (or relatively) sophisticate mass, momentum, and energy balance
equations,
i.e.,
the
so
called
unequal
velocities,
unequal
temperatures
or,
six
partial-derivative set of equations, single-phase and two-phase pressure drops are based
upon empirical correlations (basically those discussed in Section 8.3) developed during
the 60s.
l
The process “of apportioning” mentioned above implies that one overall data (typical the
total friction pressure drop available from experiments) is split into two or more components,
according to the structure of the balance equations. In the majority of the conditions of interest
there is no possibility to estimate the correctness of, i.e., to validate, the apportioning
process.
l
Pressure drops are highly dependent upon flow regimes: flow regimes are highly dependent
upon geometry and upon the condition of fully developed flow. In the case of large diameter
pipes (up to around 1 m) like those constituting the hot legs and the cold legs of RCS in PWR,
experiments in two-phase conditions have not been performed. Necessarily simplified flow
regimes are considered in modeling which are derived from small scale experiment (scaling
issue occurs as discussed in Chapter 13 of the book).
From the view point of the code user (or analyst) one may add what follows:
l
Roughness: the related value must be supplied by the analyst and may not constitute an available
data for the system to be simulated by the code; furthermore, roughness may vary during
the lifetime of the system, e.g., due to corrosion, erosion oxide formation, and crud deposit.
l
Equivalent diameter: the related value must be supplied by the user; an engineering formulation
is available which is directly connected with simple geometry without possible
three-dimensional effects; the value of equivalent diameter is therefore used to adapt results
of code prediction, noticeably pressure drops, to measured data if available; the process is
prone to some arbitrariness from the side of the code user: the fixed value for equivalent
diameters also impact the calculation of heat transfer coefficient in the concerned region.
One may summarize that modeling for distributed friction pressure drops is part of the
code and user effect is restricted to the (sometimes unknown) values of roughness and
equivalent diameter.

### 8.5.1.2 Form losses

Losses due to abrupt area change are calculated using form loss models and are
originated by geometric discontinuities already discussed in this chapter. Noticeably,
connection between pipes (relatively small diameter) and plena (relatively large diameters
), changes of direction of flow in plena and entrance-exit of a plate (e.g., the core
support plate) are characterized by form loss coefficients which constitute input for
the code.
Dependency of K factor upon Re (or fluid velocity) is typically allowed in
correlations to be supplied by the code user; however no dependence for K factor
is envisaged in available models upon void fraction. Comments are as follows.
l
The first two bullet items in the previous paragraph, i.e., current sophistication level of
modeling and apportioning procedure, also apply here.
l
K factor values (very) strongly depend upon details, e.g., rounded or sharp edge, which are
not available in all locations of a RCS in water cooled nuclear reactors.

<!-- page 532 (PDF 40) -->
l
At every discontinuity, whatever is its geometric complexity, different flow situations may
occur, namely in two-phase conditions: cocurrent flow of steam and liquid (with steam and
liquid flow configurations affected by flow pattern determined by upstream conditions),
countercurrent flow of steam and liquid and flow reversal (i.e., liquid and steam flowing
together in a direction opposite to the direction which characterizes the nominal operating
conditions of the RCS).
l
With the partial exception of core region in all water cooled reactors and the SG tube region
in PWR, local pressure drops constitute the largest part of total pressure drops in RCS at any
time during a transient. (Note: partial exception in core region is introduced because of the
importance of bottom, top, and spacer grids as far as the total pressure drops in the core are
concerned.)
From the view point of the code user (or analyst) one may add what follows:
l
It is responsibility of code user to supply suitable data for K factors as calculation input
parameters: unavailability of data (typical situation) should correspond to the execution
of proper sensitivity and uncertainty analyses (this is not always possible).
l
The user must consider the existence of possible large differences between direct and reverse
K factors values.
l
CFD codes may provide a valid support o the analysts for a systematic estimation of K factors
at any geometric discontinuity (Chapter 12 of the book) although the related results are not
immune by errors.
So, one may expect highly approximate calculation results: the degree of approximation
changes with void fraction. Even larger impact of K factors upon calculation
results may be expected if one considers the combination of fluid velocities and void
fraction.
One may summarize that modeling for local pressure drops is not part of the code
and user effect is decisive for attaining reasonable results from code applications.

## 8.5.2 Pressure drops and steady-state qualification of computational model

Establishment by code user of a correct steady-state conditions in terms of pressure
(based on pressure drops) along the loop constitutes a mandatory prerequisite for
the prediction of any transient scenario and of NPP performance. Acceptable errors
are proposed by Bonuccelli et al. (1993). An example of current situation is discussed
in the following, based upon a code application activity performed within an international
framework in 2006 (Petruzzi et al., 2006).
The calculated normalized (respect to the hot leg inlet position) pressure distribution
curve versus loop length related to the LOFT nuclear facility, are shown in
Fig. 8.21. The activity was performed by a dozen groups of analysts using different
SYS TH codes; it constitutes the second phase (of six) of the OECD/NEA/CSNI
BEMUSE project, see also Glaeser et al. (2011). The following considerations
apply:
l
Almost all calculated values are inside the uncertainty experimental bands in correspondence
of the hot leg outlet position and of the LS;

<!-- page 533 (PDF 41) -->
l
In correspondence of the cold leg inlet and outlet positions, the major part of the calculations
fall outside the uncertainty bands;
l
The positions characterized by a large discrepancy among the calculated results of the participants
are: (a) the SG U-tubes top elevation, (b) the pump inlet and outlet, and (c) the lower
plenum. No experimental value was available for those locations.
Not surprisingly large differences where observed in the comparison among various
calculated data (as well as in the comparison between experimental data and code calculation
) for the concerned LB-LOCA. Full documentation available by Petruzzi et al.
(2006) (see also de De Cr□ecy et al., 2008).
8.5.3
Pressure drops and pressure drop predictions/
measurements during transients
In nuclear thermal-hydraulics pressure drops during a transient do not necessarily
imply transient pressure drops or time-acceleration pressure drops. Namely, quasi
steady conditions and related assumptions can be used to predict and to characterize
pressure drops during most of the design basis accident (DBA) scenarios in NPPs as
discussed in Chapter 15 of the book. Fast changing conditions which require consideration
of time acceleration pressure drop occur, for instance, in the initial tenths of
seconds of LOCA, or in case of control rod ejection (CRE) event part of reactivity
initiated accident (RIA).
A sample list of items connecting pressure drops and pressure drop predictions with
transient conditions in NPP is provided below not in an order of importance. In this
case the word transient refers to accident scenarios in water cooled nuclear reactors
within the DBA category and to simulated accident scenarios in ITF.
0.994
0.996
0.998
1.000
1.002
1.004
Loop length (m)
Normalized pressure (-)
HL IN
CL IN
PUMP OUT
SG OUT
OUT SG NOZZLE
UT TOP
SG IN
HL OUT
PUMP IN
LOOP SEAL
TAF
BAF
LP
CL OUT
HL IN
Fig. 8.21 Comparison of normalized pressure curves along the loop, BEMUSE phase II.

<!-- page 534 (PDF 42) -->
l
LS. The LS is the U-shaped part of the cold leg in PWR upstream the main coolant pumps
(MCPs). The elevation of the horizontal axis of the LS is lower than the elevation of the top
of active fuel (TAF) for the core. This induces the possibility of formation of a plug of liquid
in the LS during accident scenarios. The plug formation constitutes a seal for the coolant
flowing in the loop, hence the name LS. The depth of the LS vertical part is close to
1 m. LSC may induce level recovery in the core and in some case quenching of a previous
dry-out condition. Measurement of pressure drop across the vertical part provides the
information about the LS status and possible clearing occurrence.
l
Bypass. Several bypass flow-paths inside the vessel of a PWR play a role primarily in case of
SB-LOCA. Pressure drop measurements indicate the direction of the flow and may contribute
to determine bypass flow rate.
l
Flow reversal. Direct flow at any location in the primary system of either a PWR or a BWR is
connected with nominal operating conditions. However, flow reversal may occur almost
anywhere in the circuit during transient conditions. The predictability of flow reversal
(i.e., very important to calculate system performance in case of transients) is connected with
the knowledge of related loss coefficient at abrupt discontinuities. Those coefficients may be
different from “direct” coefficients at the same location and their value may reveal (much)
more uncertain than the value characterizing the direct flow.
l
Stability of single-phase and two-phase or boiling condensing systems. In addition to BWR
stability mentioned in Section 8.4.2.5, flow oscillations, thus stability issues, are expected in
one- and two-phase NC conditions in PWR (see also Chapter 15 of the book). Namely it is
well established that selected groups of U-tubes in SGs may experience flow oscillations
including flow reversal, thus reducing the overall transit flow area for the coolant in the core.
Pressure drops are the key indicator of this phenomenon.
l
Emptying and filling and DC level (SG and RPV in PWR and RPV in BWR). Change
of level, namely in the PRZ of a PWR, implies changes in the dynamic response characteristics
of the overall system. Empty or overfill PRZ signifies loss of control capacity for the
pressure in the system. The knowledge of narrow range and wide range level in SG and in
RPV of BWR allows the control of the core power. Pressure drop signal is used for
detecting level.
l
Advancement of quench front. Specifically in case of LOCA in either PWR or BWR, core
uncovery is expected which must be followed by proper recovery mainly governed by level
rise in the DC of the vessel. Then quench front advancement is detectable by pressure drop
measurement.
l
MCPs. Values of head of MCP as well as of head during MCP rundown (coast-down) and of
head in locked or free rotor conditions constitute essential parameters affecting the coolant
flow in the core. Related pressure drop measurements are essential for determining the
system response in case of transients.
l
Sump recirculation and core pressure drops. Long-term cooling implies containment sump
(PWR) or pressure suppression pool recirculation (BWR). In both cases “small” debris accumulated
in the bottom of the containment may pass through filters and recirculation pumps
and may produce partial core blockage. Ballooning of fuel rods may also cause partial core
blockage. Cross-correlating pressure drop signals in different regions of the vessel may
allow detection of core blockage. Related techniques may need to be developed.
l
Measurement issue. At least three issues must be carefully addressed for a qualified transient
pressure drop measurement:
□
The absolute value for the range of variation expected for pressure drop measurement
may be several orders of magnitude lower than the absolute pressure acting in the system
