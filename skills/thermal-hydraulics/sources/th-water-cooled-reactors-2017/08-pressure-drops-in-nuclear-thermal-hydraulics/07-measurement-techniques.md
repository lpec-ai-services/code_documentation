# Measurement techniques
<!-- source PDF pages 43-46 -->

<!-- page 535 (PDF 43) -->
at the location of pressure drop transducer terminals (i.e., the port connecting the
measurement pipeline and the concerned “high” pressure system).
□
The distance between the location of pressure drop transducers and the terminals (or
taps) is typically of the order of several tens meters. A small (typically 5–10 mm internal
diameter) measurement pipeline (hereafter called pipeline) connects the terminals with
the pressure transducers. Usually bends and U-configurations cannot be avoided. Filling
of the pipeline by incompressible fluid must be ensured by proper actions before the start
of the transient (e.g., experiment in ITF).
□
Very small leakages in the pipelines, gas liberated from liquid inside the pipelines
when the absolute value of the system pressure decreases, initially undetected gas bubbles
, regions of high fluid temperature in the pipe such that liquid flashing may occur
when the absolute value of the system pressure decreases, may produce unqualified pressure
drop signals with very few possibilities to detect the failure or to recover the right
signal.
The provided overview confirms the role and stresses the importance of pressure drops
in nominal and transient operation of water cooled reactors: pressure drops are not
measured in all cases in NPP; however, predictive capabilities for pressure drops must
be ensured in all cases and, in all cases, pressure drops are measured in ITF.
8.6
Measurement techniques
The measurement of pressure drops constitutes the focus for this chapter. Here one
may state:
(a) measurable quantities exist which are derived from pressure drop type of measurement
(e.g., liquid levels);
(b) quantities can be measured which are directly connected with pressure drops (e.g., fluid
velocities and mass flow rates).
Techniques are considered hereafter dealing with quantities in categories
(a) and (b), in addition to direct measurement of pressure drop. Furthermore,
measurements in experimental loops (or test facilities) are distinguished from
measurement adopted in NPP. Namely key measured quantities connected with
pressure drops are:
l
In test facilities: local pressure drop; collapsed level/swell level; void fraction; density;
mass flow;
l
In NPP systems: RPV level/loop level; Δp over MCP; mass flow.
Hereafter some comments are provided to the current state of the art in performing
pressure drop measurement rather than discussing (important) details of experimental
techniques including techniques for interpreting raw data from transducers. When
considering the issues (or measurement drawbacks) in forthcoming sections the complexity
of measurement should be considered (high temperature, high pressure, and
presence in the case of NPP of radiation fields).

<!-- page 536 (PDF 44) -->
## 8.6.1 Direct measurement of pressure drops

Reference is made to direct measurements for pressure drops in ITF and in NPP. The
typical configuration of interest below is constituted by two pressure taps connected
by two hydraulic lines to two terminals of a pressure transducer. Pressure transmission
lines have a diameter of 6–8 mm and are filled by incompressible fluid, typically liquid
water. It must be ensured that liquid does not vaporize at the contact with the high
temperature fluid and that (reasonably) noncondensable gases are not present to form
bubbles or even are not dissolved in the fluid. Dissolved gas in the fluid (as well as
steam produced at the interface between measuring liquid and hot process fluid, and
gas produced during a depressurization process) may heavily affect the measured
values.

### 8.6.1.1 Distributed (friction and acceleration)

The presence of gas or vapor in the transmission line is one reason of concern for the
quality of measurement: this is also connected with the length of pressure lines (up to
several tens meters) and to the many elbows and curves necessarily part of the construction
of those lines. The main additional issues which may cause measurement
errors for distributed friction pressure drops (acceleration pressure drops issues can
be inferred as a consequence) are:
l
Static pressure target. The goal of the measurement is the static pressure in the majority of
cases; problems may arise because of possible influence of dynamic pressure, e.g., caused by
imperfectly aligned pressure taps.
l
Elevation pressure drops. It is necessary to separate the contribution of elevation pressure
drops: this is not straightforward (see also below) when two-phase flows are involved.
l
Compressible fluids including two phase. It is necessary to separate the contribution of
(spatial) acceleration pressure drop: this is not straightforward (see also below) when
two-phase flows are involved.
l
Two-phase conditions. An interpretation model is needed to estimate the average void
fraction between the two taps. The model is necessarily imperfect and its quality depends
upon the flow regime experienced by the process fluid.
l
Long piping for transmitting pressure drop signal may generate errors in measurement in
very fast transients in addition to errors possibly originated by the presence of gas or steam.

### 8.6.1.2 Local or at geometric discontinuities

The issues described for distributed friction pressure drops also apply to the measurement
of local pressure drops at geometric discontinuities, e.g., signals used to characterize
the K factors. In addition, the following issues are specific for local pressure
drop measurements:
l
Irreversible portion-1. Any local pressure drop implies the occurrence of a total pressure
drop which is formed by a reversible and an irreversible portion. Only the irreversible portion
is of technological interest and contributes to the K factor. Typically, the total pressure
drop occurs immediately downstream the geometric discontinuity: the reversible portion
brings to a recovery in pressure at some distance downstream. The value of the “distance

<!-- page 537 (PDF 45) -->
downstream” causes the issue: the distance is not known and depends upon the geometric
configuration and the flow conditions.
l
Irreversible portion-2. The measurement of the “distance downstream” is troublesome and is
possible only in selected reference situations. Hence unavoidable error must be expected
from measurements.
l
Special geometry. Local pressure drops also occur inside plena, e.g., lower plenum or UP in
case of PWR RPV. In those situations it is impractical to install transducers along the actual
flow path of the fluid. This gives origin to a hidden error when attempting to simulate fluid
flow behavior in those conditions.

## 8.6.2 Quantities connected with pressure drops

Pressure is a scalable physical variable, which describes the force on a unit of area.
Together with the measurement of temperature, the measurement of pressure is one
of the first and most used measurements in science. Pressure measurement, which is
one of the so-called “conventional measurements,” continues to play a central role in
the detection and recording of flow processes in thermohydraulic systems. In nuclear
engineering this not only applies to detection and recording of the processes in the
nuclear plants themselves but also to the test facilities used for analysis and modeling
important thermohydraulic processes.
In practice the pressure at certain measuring points in the system to be investigated
is forwarded to a sensor via pressure tapping points and so-called pressure sensing
lines. The sensor responds to the pressure exerted on it or pressure difference with
a displacement or deformation (e.g., a diaphragm). The deformation is converted
via appropriate sensors (capacitive, inductive, etc.) into electrical signals proportional
to the differential pressure.
Due to this measurement principal, pressure measurements generally give a
pressure difference between two points or the difference in pressure between a measurement
point and a reference pressure.
If the reference pressure is zero (i.e., complete vacuum) the measured value corresponds
to the so-called absolute pressure, if the reference pressure equals the atmospheric
pressure, the measured pressure difference corresponds to the so-called
overpressure (aka positive or gauge pressure) at the measuring point concerned. However
, if both measuring points are located within the system, the measurement registers
the pressure difference between these two points, i.e., the pressure drop along the
flow path which is mainly of interest later.
As described in Section 8.2, the total measured pressure drop is made up of several
components including gravity, acceleration, and pressure losses.
Δp = Δpe + Δpa + Δpf + Δp‘
(8.18)
where Δpe is the pressure drop due to static head. Δpa is the acceleration pressure drop
due to change in flow velocity along the flow path as a result of change in cross-sectional
area or change in density. In nonsteady-state processes another term is added to this
convective acceleration, which expresses the local acceleration over time.

<!-- page 538 (PDF 46) -->
Under certain conditions or if certain influencing factors are ignored, the differential
pressure measurement can be used not only to determine the permanent pressure
loss, but other important physical variables can also be derived, such as
–
Level (swell level/collapsed level)
–
Mean fluid density
–
Mean void fraction.
In steady-state flows of incompressible fluids in flow paths with constant
cross-section, the acceleration term is omitted completely. For horizontal flows the
head component of Eq. (8.18) is also omitted and the measured differential pressure
in fully developed flow is the remaining pressure loss in the flow path (Δpf+Δpe).

### 8.6.2.1 Filling level

Using the static pressure of water columns to take differential pressure measurements
of the water filling level or water reserves is a common method used both in nuclear
plant and also associated testing systems. If tanks are filled with water and steam (idle
system) and the two phases exist in a separated form, the differential pressure measurement
is a simple and very precise method for determining the filling level; this
method requires knowledge of the densities of the two phases (e.g., by means of additional
absolute pressure and temperature measurements). The water filling level can
be determined via the following designation.
Wherever there are high pressure levels, the static pressure of the steam can no longer
be neglected and should be taken into account when determining the water
filling level.

### 8.6.2.2 Collapsed level

It is not possible to directly determine the swell level (separation between two-phase
mixes with a predominant steam proportion) by measuring the differential pressure
alone; additional measuring information is required. However, conducting several differential
pressure measurements in succession can pinpoint the position of the swell
level to at least a segment of the corresponding differential pressure measurement.
Also, if the mix level changes (increase/decrease), it is possible to at least trace the
trend of the temporal progression of the mix level. For instance, usually information
can be derived from the Δp measuring signal curve about the passing of the swell level
at a pressure removal point and therefore the transition to a predominant steam proportion
within the associated Δp measurement (when the swell level decreases).
If a measuring range section is completely filled with a two-phase mix and if the
water and steam density is known, it is possible to derive from the measured differential
pressure a constant assumed mean density of the mix or the mean void fraction.
Strictly speaking, these considerations only apply to states or processes in which
the pressure drop can be neglected due to dynamic effects (e.g., wall friction,
two-phase friction).
This usually also applies to flow conditions in which a specific steam quantity
flows from bottom to top through standing water in tanks or vertical pipes.
