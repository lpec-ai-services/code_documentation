# The thermal-hydraulics aspects of the nuclear events
<!-- source PDF pages 32-46 -->

<!-- page 1130 (PDF 32) -->
It would be difficult for any NPP unit in the world to ensure core integrity when a
longer than 10 days loss of off-site power occurs. On the other hand, the multiple
Fukushima events impacted the whole world industry and technology as well as
the energy policies in individual Countries owing (not least) to financial implications
associated with the accident consequences, e.g., D’Auria et al. (2015).
16.4
The thermal-hydraulics aspects of the nuclear events
The idea is to connect the time evolutions of NPP accident scenarios with the
thermal-hydraulics phenomena discussed in the book (e.g., Chapter 6).
Two main goals can be associated with this chapter:
(1) To confirm that information derived from NPP events is valuable for the assessment of
numerical computational tools including nodalizations and codes, as suggested by IAEA
(2016d), see also D’Auria et al. (2012b);
(2) To confirm that NPP data do not contradict the findings from scaling studies, see, e.g.,
D’Auria and Galassi (2010), Mascari et al. (2015), and D’Auria et al. (2016).
In relation to the first goal the following shall be observed: (a) the creation of a database
for validation implies collecting design data (e.g., RCS geometry, operating conditions
values, and material data), boundary conditions data (e.g., pump operation
information), and recorded instrument data; (b) there is no attempt (here) to create
a database, rather to confirm that a suitable database can be gathered; (c) the level
of information detail to be expected from NPP data is not comparable with what
achieved from scaled-down test facilities; nevertheless NPP data are of high value
for code validation.
Furthermore, thermal-hydraulics (support) analysis can be essential for the understanding
of accident scenarios at any time during the events. So the question arises
“why we stop the thermal-hydraulics accident analysis at the conditions before core
melt?” The answer is based upon there consequential statements:
l
Thermal-hydraulics is a complex subject characterized by incomplete fundamental knowledge
(turbulence, bubble movements, two-phase flow regimes).
l
Experiments-based qualification is essential to prove the validity of any application.
l
A step change in qualification occurs between the situations “before core loss of geometric
integrity” and “after core loss of geometric integrity.”
In order to link phenomena and NPP scenarios, phenomenological windows (PHW)
are introduced, i.e., time spans during the accidents where one or a few key phenomena
occur. Arbitrariness in the selection of time duration for PHW is unavoidable.
In each section below at least one publication is cited dealing with the
thermal-hydraulics of the concerned event.
In all cases below “time 0” is 0.0 s and corresponds to time 00:00:00 in
Tables 16.1–16.7. An attempt is made to use the same wording as in Chapter 6 of
the book: in order to provide specific details different words are used in some cases.
Acronyms adopted in the list below and not yet used in this chapter are counter-current

<!-- page 1131 (PDF 33) -->
flow limitation (CCFL), core damage (CD), critical heat flux (CHF), instrumentation
and control (I & C), natural circulation (NC), neutron kinetics (NK), primary side
(PS), thermal-hydraulics (TH), two phase critical flow (TPCF) and can be found in
the list of acronyms. The star indicates that the concerned phenomenon also occurs
during other listed PHW during the same event.

## 16.4.1 TMI-2 LOFW-SBLOCA

The thermal-hydraulics of the TMI-2 accident has been widely studied by the scientific
community as already mentioned, for instance, see Broughton et al. (1989), and
more recently Bandini and De Rosa (2014). The TMI-2 phenomenological windows
are identified (time duration) and characterized (key phenomenon or phenomena) as
follows:
TM-PHW-1:
0.0–60.0 s (10)
«» RCS pressure rise
Other key phenomena:
l
Heat transfer across OTSG in nominal operation (e.g., including steam superheating in SS)
l
Critical flow through valves (TPCF through PORV)*
l
Heat transfer across SG with SS loosing mass inventory
TM-PHW-2:
10–60
«» RCS pressure decrease/PRZ level rise
Other key phenomena:
l
Condensation due to HPIS actuation
l
Degradation of SG heat transfer due to SG SS dry
l
CCFL at surge-line connection with HL*
l
Condensation in PORV drain tank
l
Pressurization of PORV drain tank
TM-PHW-3
60–850
«» PRZ full/CCFL in surge-line
Other key phenomena:
l
Mixture level formation in the core
l
Centrifugal pump behavior in single and two-phase conditions*
TM-PHW-4
850–1100
«» Restoration of SG heat sink
Other key phenomena:
l
Stop of circulation in loop B
l
SG-B depressurization (due to steam condensation and reduced heat transfer from PS)
l
SG-A heat transfer with increasing PS void fraction
TM-PHW-5
1100–CD
«» RCS mixture level collapse
Other key phenomena:
l
MCP performance during coast-down
l
NC performance in RCS

<!-- page 1132 (PDF 34) -->
(A)
(B)
(C)
(D)
Level (m)
Pressure (MPa)
Time (min)
Series5
RPV pressure
SGA pressure
SGB pressure
PHW3
PHW4
PHW5
PHW2
PHW1
Accident start: 04:00:57
of Mar. 28, 1979
CD: 01:51:27
from accident
start
Pressure (MPa)
Time (s)
RPV pressure
PHW1
PORV  stuck open
Letdown stopped by operatos
PRZ minimum
level
PRZ level
rising
SCRAM
Trip of condensate pumps (1A and 1B)
Trip of FW pumps
Turbine trip
EFW pumps started—valves did not open
PRZ PORV opens
EFW pumps cleared
Make-up pump
started (1A & 1B)
Level (m)
Pressure (MPa)
Time (min)
RPV pressure
SGA pressure
SGB pressure
PRZ level
PHW3
PHW4
PHW5
CD
EFW valves opened
EFW 2B shut down
MCP 2B stopped
MCP 1A stopped
MCP 2A stopped
SGB SS isolated
Level (m)
Pressure (MPa)
Time (min)
RPV pressure
PRZ level
PHW2
HPIS actuated
Make-up pump 1C started
Make-up pump 1B tripped
Both SG dry
PRZ high level
alarm
PRZ level off scale
HPIS pump 1C stopped
Valves of lines 1A and 1B throttled
HPIS bypassed manually
Fig. 16.1 (A) TMI-2 accident, pressure in RPV, SG-A, and SG-B and level in PRZ.
Identification of PHW. (B) TMI-2 accident, pressure in RPV, PHW1. (C) TMI-2 accident,
pressure in RPV and level in PRZ, PHW-2. (D) TMI-2 accident, pressure in RPV, SG-A, and
SG-B and level in PRZ, PHW3, PHW4, and PHW5.

<!-- page 1133 (PDF 35) -->
l
Core level and dry-out occurrence
l
Core film boiling
l
H2 production
l
H2 distribution in RCS
PHW 1–5 during the TMI-2 accident can be found in Fig. 16.1A–D (Fig. 16.1A: RPV,
SG-A, and SG-B pressure & PRZ level, 0 to CD with identification of all PHW;
Fig. 16.1B: RPV pressure during PHW-1; Fig 16.1C: RPV pressure and PRZ level
during PHW-2; Fig. 16.1D: RPV, SG-A, and SG-B pressure & PRZ level, during
PHW-3, PHW-4, and PHW-5).

## 16.4.2 Chernobyl-4 reactivity excursion

Athermal-hydraulicanalysisoftheChernobylRBMKreactorpriortheaccidenthasbeen
performed by Mokizuki (2007). The Chernobyl-4 phenomenological windows are identified
(time duration) and characterized (key phenomenon or phenomena) as follows:
CH-PHW-1:
0.0–23:28 (h)
«» Controlled power reduction
Other key phenomena:
l
Three-dimensional core performance (TH & NK)
l
CR performance*
l
System I & C
CH-PHW-2:
23:28–24:03
«» Uncontrolledpowerreduction&powerrise
Other key phenomena:
l
Neutron poisons (Xenon) concentration growth
CH-PHW-3:
24:03–24:23:48
«» Establishing system TH conditions
Other key phenomena:
l
Core heat transfer in high-flow low-power conditions
CH-PHW-4:
24:23:48—CD
«» Fission power excursion
Other key phenomena:
l
Subcooled nucleate boiling transient heat transfer in core
PHW 1–4 during the Chernobyl-4 accident can be found in Fig. 16.2A and B
(Fig. 16.2A: core power, core inlet flowrate, 0 to CD with identification of all
PHW; Fig. 16.2B: core power, core inlet flowrate, and core inlet subcooling during
PHW-3 and PHW-4).

<!-- page 1134 (PDF 36) -->
## 16.4.3 La Salle-2 and Oskarshamn-2 boiling stability

From a thermal-hydraulics viewpoint a similar event occurred in La Salle-2 and
Oskarshamn-2 reactors as it results from Table 16.8. Thermal-hydraulic analyses
for both event have been published in the literature, e.g., Wulff et al. (1990) and
Kozlowski et al. (2014), respectively, related to La Salle and Oskarshamn.
Power (MW)
Flow (%)
Time (h)
Power
Core flow
PHW2
PHW3
PHW4
Time 01:00:00
of Apr. 25, 1979
Core power at
1600 MWth
Time 01:23:49
of Apr. 26, 1979: CD
ECCS
isolated
Core power at
30 MWth
–5
–4
–3
–2
–1
Temperature (°C)
Power (%)
Flow (%)
Time (s)
Power
Core flow
Core inlet subcooling (upper value)
Core inlet subcooling (lower value)
PHW3
PHW4
CD
Time 24:03:00 from
sequence initiation
Core power: 200MWth
Planned coast-down
experiment starts
First MCP in
standby starts
Second MCP in
standby starts
AZ-5 bottom
pressing
MCPs
restoed
(A)
(B)
Fig. 16.2 (A) Chernobyl-4 accident, core power and core inlet flowrate. Identification of PHW.
(B) Chernobyl-4 accident, core power, core inlet flowrate, and (reasonable) boundaries for core
inlet subcooling, PHW3 and PHW4.

<!-- page 1135 (PDF 37) -->
Table 16.8 Summary of core performance in the case of La Salle-2
and Oskarshamn-2 events
La Salle event
Time (s)
Consequences
84% power—75% flow
0.0
Nominal operation
MCP trip
49.0
Entering the recognized “unstable” region of
power-flow map
(APRM) Core power to
45%
72.0
Small amplitude oscillations appear
(APRM) Core power to
54%
240.0
Oscillations start
Modulated limit cycle
oscillations
330.0
(APRM) Core power
118%
445.0
Automatic reactor trip
End of transient
540.0
Recorded by STARTREC, see Table 16.3
Oskarshamn event
Time (s)
Consequences or notes
100% power—100%
flow
0.0
Nominal operation
APRM core power to
117%
·35.0
Short peak
APRM core power to
108% (E5 limit)
48.0
MCP 1st rundown: flow reduced and signal
“canceled”
Core flow to 90%
52.0
Following previous rundown
APRM core power to
108% (E5 limit)
75.0
MCP 2nd rundown: flow reduced and signal
“canceled”
Core flow to 82%
82.0
Following previous rundown
APRM core power to
108% (E5 limit)
107.0
MCP 3rd rundown: flow reduced and signal
“canceled”
Core flow to 70%
111.0
Following previous rundown
Core power increases
again (E4 limit)
118.0
Operator triggers the partial scram (at 126 s) &
fixes minimum MCP flow
APRM core power to
64%
132.0
Core flow to 50%
135.0
Entering the recognized “unstable” region of
power-flow map
Oscillations start
160.0
DR about 1.36
APRM core power to
132% (SS9 limit)
181.0
Automatic reactor trip
End of event
300.0
End of recording

<!-- page 1136 (PDF 38) -->
### 16.4.3.1 La Salle-2

The review performed after the event revealed APRM peak-to-peak oscillations ranging
from 20% to about 75% power during the event. The oscillation amplitude was at
least 100% peak-to-peak when the scram occurred. The peaking factor for axial
power distribution in the core increased from 2.11 before the event to 2.65 at the time
of the local power range monitor (LPRM) alarm. The phenomenological windows are
identified (time duration) and characterized (key phenomenon or phenomena) as
follows:
LS-PHW-1:
0.0–40
«» Controlled power reduction
Other key phenomena:
l
Three-dimensional core performance (TH & NK)*
l
Reduction of core inlet flow and subcooling
l
MCP coast-down
LS-PHW-2:
40–Scram
«» Stability event
Other key phenomena:
l
Natural circulation in the RPV
l
Margin to CHF
l
Core power oscillation characteristics (frequency and amplitude)

### 16.4.3.2 Oskarshamn-2

The Oskarshamn-2 phenomenological windows are identified (time duration) and
characterized (key phenomenon or phenomena) as follows:
OS-PHW-1:
0.0–118. s
«» Step-changes in core power
Other key phenomena:
l
Three-dimensional core performance (TH & NK)*
l
Positive drift in core power
l
Reduction of core inlet flow and subcooling
l
MCP coast-down
l
Reduction in FW flow and temperature
l
Controlled power reduction
OS-PHW-2:
118. s—Scram
«» Stability event
Other key phenomena:
l
Natural circulation in the RPV
l
Margin to CHF
l
Core power oscillation characteristics (frequency and amplitude)
PHW 1 and 2 during the La Salle-2 and the Oskarshamn-2 events can be found in
Fig. 16.3A–C (Fig. 16.3A: trajectories of La Salle-2 and Oskarshamn-2 in the

<!-- page 1137 (PDF 39) -->
(A)
(B)
(C)
Power (%)
Flow (%)
Locus of OS event
Locus of LS event
LS measured data
LS 105% rod line
OS rod line
SS9
E25
Flow (%)
Power (%)
Time (min)
Power
Core flow
FW flow
PHW2
CR entered
APRM oscillations
PHW1
Time 17:32 of
Mar. 9, 1988
Valving error
Both recirculation
pumps trip
SCRAM
APRM 118 %
FW heater
isolation
Flow (%)
Power (%)
Time (s)
Power (APRM1)
FW flow
Core flow
PHW1
PHW2
Time 14:58:00 of
Feb. 25, 1999
Turbine and
MCP stop
Partial SCRAM
actuated by operator
APRM above E4 limit
APRM above SS9 limit
SCRAM
Fig. 16.3 (A) La Salle-2 and Oskarshamn-2, trajectories of the events in the BWR flow map.
(B) La Salle-2 core power and inlet flowrate and Feed-water flowrate, identification of PHW.
(C) Oskarshamn-2 core power and inlet flowrate and Feed-water flowrate, identification
of PHW.

<!-- page 1138 (PDF 40) -->
BWR flow map [core power versus flow]; Fig. 16.3B: La Salle-2 core power, core,
and FW flow 0 to end; Fig. 16.3C: Oskarshamn-2 core power, core, and FW flow
0 to end).

## 16.4.4 Fukushima-1 to -4, SBO and LOOSP

The thermal-hydraulics of the Fukushima accident has already been the topic of published
papers, see for instance Sevo´n (2015) and Ozdemir et al. (2015) related to
Fukushima-1, Kim et al. (2016) related to Fukushima-2, and Fernandez-Moguel
and Birchley (2015) related to Fukushima-3. The Fukushima Units 1–3 phenomenological
windows are identified (time duration) and characterized (key phenomenon or
phenomena) in the following.
F1-PHW-1:
0.0–480
«» SBO evolution
Key phenomena:
l
Natural circulation through IC
l
RPV pressure drop caused by IC cooling
F1-PHW-2:
480—CD
«» LOOSP evolution
Key phenomena:
l
RPV pressure increase following IC isolation & SRV operation
l
RPV level decrease (due to coolant loss through SRV)
l
Core dry-out
PHW 1 and 2 during the Fukushima Unit 1 event can be found in Fig. 16.4A
(Fig. 16.4A: RPV pressure and level).
F2-PHW-1:
0.0–4 h
«» SBO/LOOSP evolutions (SRV cycling controlled)
Key phenomenon:
l
Core cooling ensured by RCIC and SRV operation
F2-PHW-2:
4–15 h
«» LOOSP-RCIC overcooling
Key phenomena:
l
RPV pressure undershoot and recovery
l
Containment (PSP) temperature rise (caused by RCIC turbine discharge)
F2-PHW-3:
15–70 h
«» LOOSP-RCIC “stable” cooling
Key phenomena:
l
RPV pressure (below SRV set-point)
l
Core cooling ensured (level above TAF)
l
Containment pressure and temperature rise*
F2-PHW-4:
70–CD
«» LOOSP-RCIC out of operation

<!-- page 1139 (PDF 41) -->
Time (hr)
–10
–8
–6
–4
–2
Level (m)
Pressure (MPa)
RPV pressure measured (A)
RPV pressure (analysis)
RPV level
PHW1
PHW2
Time 00:00:00  is 14:47:00
of Mar. 11, 2011
SBO event including SCRAM
MSIV closure
TAF
BAF
Time 04:03:00 from
accident starts
CD
IC
started
IC isolated
IC manually
started
IC manually
isolated
–6
–4
–2
Level (m)
Pressure (MPa)
Time (h)
RPV pressure
RPV level
PHW1
PHW2
PHW3
PHW4
Time 00:00:00 is 14:47:00 of
Mar. 11, 2011
SCRAM
MSIV closure
RCIC manually
started
CD
RCIC out of operation
(assumption)
Hunting due to running out of
instrumentation battery
TAF
BAF
SRV actuated
manually
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Temperature (°C)
Pressure (MPa)
Time (h)
DW pressure
DW temperature
SP temperature
PHW2
PHW1
PHW3
PHW4
PCIS and SGTS active
Containment
venting valve open
25% (DW side)
Containment venting
valve open 25% (PSP side)
Containment
venting valve
closed
CD
(A)
(B)
(C)
Fig. 16.4 (A) Fukushima-1, RPV pressure and level (core side), identification of PHW.
(B) Fukushima-2, RPV pressure and level (core side), identification of PHW. (C) Fukushima-2,
pressure and temperature in the containment.
(Continued)

<!-- page 1140 (PDF 42) -->
Key phenomena:
l
RPV pressure rise
l
SRV manual actuation and RPV pressure fall
l
RPV level fall
l
Core dry-out
PHW 1–4 during the Fukushima Unit 2 event can be found in Fig. 16.4B and C
(Fig. 16.4B: RPV pressure and level all PHW; Fig. 16.4C: containment pressure
and temperatures all PHW). An explanation of the negative peak at about 42 h is provided
in Table 16.6.
F3-PHW-1:
0.0–22 h
«» SBO/LOOSP evolutions (SRV cycling controlled)
–6
–4
–2
Level (m)
Pressure (MPa)
Time (h)
RPV pressure
RPV level
TAF
BAF
PHW2
PHW3
Time 00:00:00 is 14:47:00
of Mar. 11, 2011
SCRAM
Pressure controlled
by SRV
PHW1
MSIV
closed
RCIC started
(manually)
HPCI
active
HPCI stopped
Fire water injection started
SRV
opened
CD
RPV level
indication lost
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Pressure (MPa)
Time (h)
DW pressure
PHW2
PHW3
CD
PCIS and
SGTS  active
PSP spray
initiated
Containment
venting
(D)
(E)
Fig. 16.4 Continued. (D) Fukushima-3, RPV pressure and level (core side), identification of
PHW. (E) Fukushima-3, RPV pressure in the containment.

<!-- page 1141 (PDF 43) -->
Key phenomenon:
l
Core cooling ensured by RCIC and SRV operation
l
Containment pressure and temperature rise*
F3-PHW-2:
22–36 h
«» LOOSP evolution-HPCI actuated
Key phenomena:
l
RPV pressure decrease
l
Core cooling ensured by HPCI
F3-PHW-3:
36-CD
«» LOOSP evolutions—Lack of core cooling
Key phenomena:
l
RPV pressure increase
l
Core dry-out
PHW 1–3 during the Fukushima Unit 3 event can be found in Fig. 16.4D and E
(Fig. 16.4D: RPV pressure and level all PHW; Fig. 16.4E: containment pressure
and temperatures all PHW).

## 16.4.5 Final remarks

The exploitation of the listed phenomena and of concerned database needs a follow-up
analysis (see also the “caution statement” in the Foreword) including the steps below:
(1) Identification of physical quantities which characterize the phenomena: i.e., typically, the
unknowns of balance equations discussed in Chapter 5 of the Book, but also connected
quantities, like pressure, void fraction, level in various components of RCS, mass inventory
, rod surface temperature, heat flux, mass flow, superficial velocities.
(2) Identification of ranges of variations for those quantities in the concerned PHW, e.g., pressure
change between 15.0 and 8.0 MPa.
(3) Combining the ranges of variations of selected key quantities, e.g., related to PHW-xx and
PHW-yy (two examples given), respectively,
l
Ranges in core region: pressure 6.0–8.0 MPa, void fraction 0–0.4, liquid velocity
5.0–6.0 m/s, linear heat flux 2.0–3.0 kW/m
l
Ranges in HL-PRZ connection: HL diameter 0.8 m, surge-line diameter and mutual
position related to HL 0.2 m and vertical angle, pressure 10.0–9.0 MPa, liquid velocity
in HL 1.0–2.0 m/s, void fraction in HL 0.7–0.8.
(4) Confirm scaling: demonstrate that experimental database gathered in ITF or SETF having,
as far as possible, the same ranges of variations of parameters in NPP exist & demonstrate
“no-contradiction” between data relationships from scaled experiments and NPP.
(5) Confirm code capabilities: demonstrate that code calculations performed without adjusting
input parameters (but considering related uncertainties or errors) produce results which are
in qualitative and quantitative agreement with NPP data according to established procedures
and acceptability thresholds as discussed in Chapters 6, 13, and 14 of the book
and according, e.g., to Petruzzi et al. (2006).

<!-- page 1142 (PDF 44) -->
The following summary notes are derived from the thermal-hydraulic investigation of
the concerned NPP events.

### 16.4.5.1 TMI-2

All phenomena occur quicker in TMI-2 related to UTSG equipped NPP. In this case
“quicker” means whatever is expected in a UTSG PWR in a time scale of the order of
ten seconds occurs in TMI-2 (OTSG PWR) in a time scale of the order of one second.
Definitely the quick progression of the accident (e.g., PORV opening and
“undetected” stuck open condition occurring in a few seconds since the start of the
transient) might have contributed to mislead the operators.
The understanding of CCFL, namely, CCFL at the connection between HL and
PRZ surge-line, was clear to the scientific community at the time of the accident. Nevertheless
the knowledge was not of “textbook” type: i.e., this was not spread necessarily
to the industry and countermeasures were not necessarily planned in the
emergency procedures.
The natural circulation performance of OTSG equipped PWR is definitely not the
same as UTSG equipped PWR, i.e., in terms of NC mass flux in the core at an assigned
decay power value and with a decreasing mass inventory in PS. This is a conceivable
motivation for keeping the MCP in operation during the TMI-2 event. This is true
although advantages and disadvantages of the conditions MCP-on and MCP-off were
not well established at the time of the transient as well as the connected EOP. In the
case of TMI-2 one may conclude that MCP in operation delayed the occurrence of core
failure related to the condition of MCP stopped. In the case of UTSG PWR undergoing
the same TMI-2 LOFW+undetected SBLOCA event, the condition MCP stopped
appears more reasonable to prevent or to delay an irreversible core cooling degradation.

### 16.4.5.2 Chernobyl-4

As well clear the Chernobyl event was a normal operation situation (i.e., not even an
“event”) till the time when the fission power fell to “zero” owing to an operator error,
e.g., about 1 h before the uncontrolled reactivity excursion (see Table 16.2). At this
moment the reactor was pushed toward a beyond design condition with core keeping
its geometric integrity till the explosion. Such a time period (i.e., “about 1 h”) is of
interest for the notes below.
The thermal-hydraulic situation of the RCS (including core and piping till the steam
drums) can be depicted by the following statements applicable to the whole period:
(a) Core power was much lower than nominal full power value.
(b) Pressure was at (or close to) the nominal full power value.
(c) Core flow was varied by operators and lower or equal to nominal value (i.e., corresponding
to full power).
(d) The ratio [core flow]/[core power] was for all time higher or much higher than the value
corresponding to nominal or full power condition.
(e) The core inlet subcooling was apparently lower than the value corresponding to nominal
full power.
(f ) The FW flow was higher than the value corresponding to the actual core power.

<!-- page 1143 (PDF 45) -->
(g) The level in the steam drums was lower (on average in the period) than the value
corresponding to nominal full power condition.
The thermal-hydraulic situation can be depicted as “coolant forced circulation through
the core,” i.e., low-temperature difference between core inlet and outlet and, therefore,
low subcooling at core inlet. Under these circumstances key questions for
thermal-hydraulics are, i.e., related to the time a few seconds before the explosion:
l
What was the quality at core outlet?
l
What was the margin to DNB in the core?
The answer to both questions is not straightforward because of the possibility that the
MCP (or some of those) were in a cavitation conditions. Furthermore, a comprehensive
answer requires further investigations which are beyond the purpose for the present
effort. So, rather than answering the questions a few thermal-hydraulics related
statements addressing the questions are provided below (i.e., making reference to a
few seconds before the explosion):
(1) In case there was no pump cavitation and all MCP were pumping the (slight) subcooled
liquid into the core according to the best information gathered so far (see, e.g.,
Table 16.2), the sudden boiling of the coolant, i.e., a phenomenon taken to explain the positive
reactivity insertion at the origin of the explosion, cannot be justified.
(2) The margin to DNB (again in case of no steam at core entrance) considering the items (a),
(c), and (d) was well above a reasonable value acceptable for safety.
(3) The RBMK core is very large, i.e., 14 m diameter and about 8 m distance between bottom of
the active fuel (BAF) and TAF (and includes more than 1500 pressure channels):
thermal-hydraulics conditions, i.e., coolant and fuel temperatures, are necessarily different
frombottom totopand fromcentertoperiphery: so,theassumptionof uniform-simultaneous
vaporization of the entire coolant mass in the core is not easily defendable and application of
three-dimensional thermal-hydraulics is needed, see, e.g., Parisi (2008).
(4) Time constants for the evolution of thermal-hydraulic phenomena, including flashing or
fast-sudden vaporization, are much longer (i.e., order of magnitude of seconds) than time
constants associated with neutron flux changes if a prompt-critical situation is created (i.e.,
order of magnitude of milliseconds or less): the assumption of a (relatively slow, possible)
reactivity insertion due to thermal-hydraulic phenomena only, like flashing, appears inconsistent
with a reactivity impulse (or, better, a fast reactivity increase) lasting fractions of 1 s
needed to justify the neutron flux power peak.
(5) The formation of local super-critical regions involving parts of the core is possible, e.g.,
according to Malko (2002). The propagation of local disturbance in neutron flux to the
entire core is expected to be much faster than the evolution of any phenomenon connected
with thermal-hydraulics, e.g., including the depressurization caused by the eventual rupture
of one or a few pressure channels. This makes difficult the explanation of a spatial nonsymmetric
neutron flux spike as the origin of a nonsymmetric explosion.

### 16.4.5.3 La Salle-2 and Oskarshamn-2

Data after scram (time of accident end for the concerned cases), or RCS recovery by
suited EOP, can also be of interest for the purposes of the present chapter although
these are not considered.

<!-- page 1144 (PDF 46) -->
Stability constitutes a complex issue in nuclear thermal-hydraulics (as already
mentioned) and full predictive capabilities (e.g., by SYS TH codes) are not available.
However capabilities to analytically reproduce detected events do exist (Bousbia
Salah et al., 2010) (see also Chapters 1, 2, and 10 of the book). Four main origins
for the complexity can be distinguished:
l
the large number of different physical mechanisms which may trigger the instability occurrence
(D’Auria et al., 2014)
l
the possible interaction among various physical mechanisms during a stability event
l
the influence upon instability of parameters known with some approximation (or affected by
errors) like the local material properties of nuclear fuel (e.g., gap conductance) also affected
by burn-up, see also Lombardi-Costa et al. (2008)
l
the influence of a variety of systems, the so-called BoP, e.g., located several hundred meters
away from the core (upon the instability scenario in the core)
It seems worth noting at this point, not necessarily connected with the events in La
Salle and Oskarshamn: (a) the distinction between static and dynamic instabilities,
as well as between “Type I” and “Type II” instabilities (Van der Hagen et al.,
2000); (b) the relevance of the density wave oscillation (DWO, dynamic) stability
mechanism (Lahey and Moody, 1993); (c) the detection of local instability in a prototype
full height simulator of BWR which are static at the center of the core and may
not detectable at the core boundaries (D’Auria and Pellicoro, 1996; see also D’Auria
(Ed.) et al., 1997).

### 16.4.5.4 Fukushima-1 to -3 events

The evolution of the SBO and, later on of the LOOSP transients in Fukushima Daiichi
Units 1–3 is fully consistent with the thermal-hydraulics knowledge at the time of the
events. Definitely no flaw in the thermal-hydraulics knowledge can be connected with
the Fukushima scenarios or, in other words, no better destiny for the Units 1–3 cores
could be expected under the assigned events and circumstances. This statement is substantiated
by the issues below.
l
IC in Fukushima-1. The IC is a passive system without moving parts during its design operation
. IC was adopted in early BWR and reconsidered for future NPP including Simplified
BWR, SBWR. The IC correctly entered into operation in the Fukushima-1 NPP following
the SBO occurrence. After the LOOSP event and some nonoptimized operator actions the IC
went out of operation. The IC heat sink in Fukushima-1 NPP could have been sufficient for
about 10 h, i.e., a time period less than the actual duration of the LOOSP condition. Furthermore
, the SBWR IC has been the target system for a reliability study (D’Auria and Galassi,
2000) where it was found that was the reliability of the thermal-hydraulic performance (i.e.,
independent of the actuation of any mechanical system) is below unity, see also Jafari et al.
(2003). This implies that the integrity of the Fukushima-1 core was not ensured even in the
case of an IC fully operative.
l
RCIC in Fukushima-2 and -3. The RCIC is a passive system with moving parts (i.e., the turbine
) during its design operation. Turbine-driven RCIC is adopted in most of the existing
BWR. The RCIC correctly entered into operation in the Fukushima-2 and -3 NPP following
