# 4. TEST FACILITIES AND EXPERIMENTAL THERMAL HYDRAULICS
<!-- source PDF pages 27-35 -->

<!-- page 15 (PDF 27) -->
complicated because it will require a system in an actual reactor environment
to allow for internal heat generation. To deal with this issue, a distributed heat
source can be considered such as that in the DYNASTY loop [38]. This facility
aims to study various phenomena that may occur within a molten salt reactor by
simulating internal heat generation through an externally distributed heat source.
Efforts to model this facility are described in Benzoni et al. [39].

# 4. TEST FACILITIES AND EXPERIMENTAL THERMAL HYDRAULICS

## 4.1. INTRODUCTION TO EXPERIMENTAL METHODS

Mock-ups are widely used in the fields of research and industry to study
phenomena that are poorly understood and are therefore not yet reproducible
through simulations. They are often dedicated to studying single phenomena
(separate effect tests (SETs)) or combined phenomena (integral tests). In the
world of the nuclear industry, safety studies are based on scientific computing
tools (such as CATHARE [40]), validated on real or representative experiments
of the studied issues. When an experiment in a real configuration is not feasible,
the models of these scientific computing tools are validated through experiments
on mock-ups (experiments conducted at different scales of the actual case and,
when applicable, using fluids that simulate the real fluids).
Focusing on liquid metal fast reactor technology, experiments are generally
very complex to implement because of the nature of the coolant and the high
temperatures. For many issues, the use of a simulant fluid, such as water,
is sufficient to study specific phenomena. This is also true for sodium, which
therefore allows simulation of flow and heat transfer within a range of nondimensional
parameters similar to those of water. The experiments conducted
under isothermal conditions are mainly dedicated to studying the flow behaviour
in the various components where low thermal transfer occurs.
When it comes to thermal aspects, water can no longer act as a simulating
fluid, as its thermal conductivity is approximately 100 times lower. This is
generally true for the experiments involving heat exchange at walls, for instance,
in the heat exchanger studies. However, in certain special cases involving
a reduced scale model, the use of water better reproduces the thermal aspects
because the Péclet number is better observed.

<!-- page 16 (PDF 28) -->
Since measurements at different locations are necessary for code validation,
these experiments incorporate various types of sensors. For the experiments
using simulant fluid, the instrumentation typically consists of commercial sensors
(e.g. thermocouples, PT100, etc.) or measurement techniques (e.g. particle image
velocimetry (PIV), laser Doppler velocimetry (LDV), etc.). In the case of liquid
metal experiments, however, because of the constraints (e.g. high temperature,
opacity, chemistry, etc.), specific instrumentation is developed.
The application of the similarity theory allows studies to be carried out
on a reduced mock-up with a simulant fluid. The experimental design and
operating conditions are based on the conservation of dimensionless numbers
calculated from the phenomena involved and the geometry. However, in
general, it is impossible to guarantee conservation of all dimensionless numbers
simultaneously because of the physical phenomena they are considering. For
instance, the Reynolds number evolves linearly with the velocity, whereas the
Froude number is proportional to the square of the velocity. A researcher has to
choose which dimensionless numbers to conserve. This choice is based on expert
considerations and the analysis of the equations governing the phenomenon.
This section sums up the state of the art presented during the technical
meeting regarding the isothermal and thermal hydraulic experiments as well as
the measurement techniques.

## 4.2. ISOTHERMAL/HYDRAULIC EXPERIMENTS

The isothermal experiments are generally conducted using a simulant fluid
to study different kinds of issues.

### 4. 2. 1. Surface flow and gas entrainment

The free surface flow was studied with the aim of reducing gas entrainment
and thermal fatigue of the immersed components. Gas entrainment is due
to vortices and disturbances at the free surface [41]. For the first case, gas is
entrained through the core of the vortex; for the second case, it leads to the
entrapment of gas bubbles. Experiments are performed in analytical mock-ups
with the aim of characterizing the processes involved in the creation of the vortex
as well as in integral mock-ups to obtain validation data for the code and test
devices to smooth the surface. The Indira Gandhi Centre for Atomic Research
(IGCAR) and the French Alternative Energies and Atomic Energy Commission
(CEA) presented the latest advancements related to the study of the free surface
of liquid metal pool type reactors.

<!-- page 17 (PDF 29) -->
IGCAR based this work on the Froude and Weber numbers with water as
a simulant fluid [42]. From this consideration, a unique working point exists
to fulfil the conservation of both the Froude and Weber numbers. It leads to a
mock-up scale of 5/8, which is quite close to the full size case [43]. In the case
of studying the free surface or gas entrainment, the tension forces seem to be
negligible compared with the inertia or buoyancy forces. The authors could have
based the size calculation solely on the Froude number to achieve a smaller scale.
However, the authors’ decision to design a large mock-up to better capture the
phenomenon is understandable and justified. Because flow fluctuations at the
argon–sodium interface may induce thermal fatigue, IGCAR studied the effect
of devices developed to reduce gas entrainment at variations of the surface.
Comparative studies without and with the addition of mitigation devices show
a reduction of the velocity at the free surface and thus of the disturbances [44].
From a physical point of view, the baffle plates at the wall deviate the flow in the
inner vessel and prevent high velocity at the free surface. However, the effect
of the porous skirt on reducing gas entrainment is not well understood. These
conclusions were mainly based on the analysis of the velocity at the free surface.
The authors claimed they performed some visualizations of the bubbles with
submerged Perspex windows. A priori, they did not characterize the size and flow
of the bubbles, which is important for building models.
At CEA, experiments were conducted on the MICAS1 mock-up at 1/6 scale
of the ASTRID2 reactor [45, 46]. The studies were conducted with the same
Froude number for both the reactor and the model to achieve similar surface flow
behaviour. As numerical simulations cannot be performed in big geometries with
such complex phenomena because of the high computational costs, the use of
a gas entrainment criterion is a way to address the gas entrainment issue [47].
The Burger vortex model is used to build a gas entrainment criterion, and the
theoretical value was determined by assuming that a vortex carries gas when its
depth exceeds the distance between the outlet and the water surface. The PIV
imaging technique was employed to measure the surface flow velocity around
the vortex with different behaviours regarding gas entrainment. The parameters
of the Burger model versus the vortex state were calculated using their velocity
results. An experimental criterion was determined and compared with the
theoretical one; the experimental value is much lower than both the theoretical
value and the values determined in the analytical models. It may be due to the
specific MICAS geometry or to the fact that turbulence is neglected in the model.
Studies will need to be carried out to understand the cause of this difference.
1	 Maquette d’Intérêt du Cœur pour l’Analyse de la Structure.
2	 Advanced Sodium Technological Reactor for Industrial Demonstration.

<!-- page 18 (PDF 30) -->
It is important to describe the vortex in terms of depth and diameter versus the
operating conditions to understand its formation process.

### 4. 2. 2. Pressure drop measurements

Because of the lack of data in the handbooks, the Institute of Physics and
Power Engineering (IPPE) performed some experiments with liquid metal to
determine the hydraulic resistance in channels and structures of nuclear power
plants [48]. They ended up with the hydraulic characteristic of heat exchangers
and steam generators and were able to optimize their geometry in order to
increase their yield.

### 4. 2. 3. Cavitation

To study the primary pump hydraulic performance in transient and
accident conditions, an experimental facility called PULSAR was erected at
the Belgian Nuclear Research Centre (SCK CEN) at a scaling factor of 1:2.4,
as shown in Fig. 1. Cavitation testing will be performed using lead bismuth as
a fluid. Additional experimental investigation of the cavitation phenomenon
and its impact on structural materials under representative conditions of the
MYRRHA reactor will be carried out using the CARAT (Cavitation Ultrasonic
Test) facility [49].
Cavitation tests were also performed at CEA in the pump diagrid pipes. In
this case, water was used as a simulant fluid, and the cavitation was detected with
both pressure and accelerometer sensors. The transposition of those results to the
sodium case is possible since sodium and water behave similarly regarding the
cavitation [50].

## 4.3. THERMAL HYDRAULICS EXPERIMENTS

Downscaling in water models makes distortion of the Péclet number
acceptable for studying flow with thermal stratification. This makes it possible to
investigate the thermal flow in the upper plenum. However, when heat exchange
occurs at walls and the kinematic viscosity is much lower than the coefficient of
thermal diffusivity, water models are no longer representative. Experiments with
liquid metal are necessary.

<!-- page 19 (PDF 31) -->
### 4. 3. 1. Thermal flow behaviour in the vessel

The study of the characteristics of the flow in the upper plenum is in general
carried out with a simulant fluid at a reduced scale [51]. This makes it possible
to measure velocity using common techniques. However, it is impossible to
simultaneously observe the most important similarity criteria (Reynolds number,
Péclet number and Froude number). To ensure the retention of buoyancy effects,
different dimensionless numbers must be considered. Research at CEA on the
behaviour of the jet emerging from the core has shown that the densiometric
Froude number has to be maintained in the case of thermally stratified flow.
For studies of natural convection, IPPE demonstrated that experiments have to
be based on the Euler number [52]. The studies conducted at IPPE have shown
that when the Reynolds number > 104, the sizes of stagnant and recirculation
formations do not change at equal values of the Froude number for the model
and the reactor [53]. It is not necessary to observe the same Reynolds number;
however, the type of flow (turbulent or laminar) needs to be considered.
Booster
Primary
Throttle
valve
Vortex
flowmeter
Heat
exchanger
FIG. 1. PULSAR (Pump Facility for Scaled Experiment) test facility (courtesy of J. Pacio,
SCK CEN, Belgium). Adapted from Ref. [49] with permission.

<!-- page 20 (PDF 32) -->
The flow fluctuations in the upper plenum induce thermal oscillations in
the immerged components that lead to thermal fatigue [42] and a decrease in
reactor lifetime. At IPPE, experiments were conducted in the model at a scale of
1/10 in nominal mode and natural convection number [52]. The studies showed
that the effect of buoyancy forces leads to thermal stratification and temperature
fluctuations characterized by the Brunt–Väisälä frequency.
At CEA, the 1/6 model of the ASTRID reactor mentioned previously was
also used to study thermal stratification [46]. They studied the behaviour of the
jet going out of the core depending on the operating conditions. They showed
that the jet bends upward at the threshold value of the densiometric Froude
number. Additional work has demonstrated that this result can be transposed to
a higher scale.
Figure 2 shows a schematic and an image of the E-SCAPE (European Scaled
Pool Experiment) facility, which is a thermal hydraulic 1/6 scale model of the
primary system of the MYRRHA reactor, with a 100 kW electrical core simulator
that is cooled by LBE [49, 54]. It aims to study different operating conditions,
ranging from nominal to incidental (e.g. pump or heat sink failure, etc.). It is
equipped with thermocouples along vertical lines to measure the temperature
stratification. Results are in quite good accordance with numerical calculations.
FIG. 2.  Schematic (left) and an image (right) of the E-SCAPE facility (courtesy of J. Pacio,
SCK CEN, Belgium). Reproduced from Ref. [49] with permission.

<!-- page 21 (PDF 33) -->
### 4. 3. 2. Fuel elements

At IPPE, experimental campaigns over the years have provided extensive
data on the heat transfer and the temperature fields in the fuel elements for
both nominal and various non-nominal conditions and operating modes of the
core [52]. These data have been used for selecting spacer grid spacing and
geometries for lead cooled reactor cores.
For the MYRRHA reactor, the pressure drop measurements of a fuel
assembly were performed in the COMPLOT facility at SCK CEN at 200 and
350°C [55]. Regarding the heat exchange, tests were carried out at ENEA and
KIT. The ENEA tests were performed using the NACIE facility, a 19 pin natural
circulation driven loop, and the CIRCE facility with a 37 pin configuration.
The results from experimentation at these facilities show agreement with
empirical correlations and CFD analysis [56]. At the same time, some corrosion
tests were carried out in the MEXICO facility at SCK CEN for one year at a
temperature of 400°C [57].

### 4. 3. 3. Steam generator or heat exchanger

At IPPE, the SPRUT facility aims to study a steam generator in which
the processes of evaporation and superheating of steam are combined [52]. The
experimental results with sodium as a fluid are in agreement with the correlations
for the critical heat flux in pipes.
For the primary heat exchanger of the MYRRHA reactor, a range of
experiments is being performed or planned by SCK CEN [49]. A facility
designed to demonstrate the feasibility of leak detection in the double walled
bayonet tubes of the MYRRHA primary heat exchangers showed leak detection
rates of up to 5 × 10–4 mbar·l/s, surpassing MYRRHA’s design specifications. At
the time of writing, a tabletop steam–water natural circulation open loop system
is being commissioned to evaluate the thermal resistance of the MYRRHA heat
exchanger. Additionally, the Heat Exchanger at the COMPLOT (HEXACOM)
facility is being finalized to test a full scale MYRRHA heat exchanger with
forced convection using LBE and a steam–water mixture on the primary and
secondary sides, respectively.
Whereas previous experiments have focused on steam generators with
water as the working fluid of the secondary loop, CEA’s DANAH mockup
facility was used to investigate a sodium–gas heat exchanger for Brayton
cycle applications [46]. PIV and LDV techniques were used to study the flow
distribution in the inlet and outlet plena of the primary side. Initial tests to validate
CFD calculations showed good results, allowing additional CFD calculations to

<!-- page 22 (PDF 34) -->
be performed to optimize the geometry for a reduction in maldistributed flow
through channels.

### 4. 3. 4. Incidental and accidental experiments

Sodium boiling in a model of a fuel assembly was investigated at
IPPE [52]. From these experiments, a cartogram of a two-phase flow of liquid
metal coolants was developed, which was helpful for safety studies. IPPE also
studied the uncontrolled loss of coolant flow behaviour of the corium in sodium
reactors. The results make it possible to improve the high temperature part of
the COREMELT code.
At ENEA, SIRIO was designed to demonstrate the operation of a passive
decay power removal system utilizing non-condensable gases to prevent
overcooling, which was planned for ALFRED, on a small scale but with the same
power density [58]. The results showed the capability of the system, although
more experiments are needed to address its performance and support code
validation. It was also shown that the SIRIO facility, with some modifications,
can be used to demonstrate the effectiveness of non-condensable gases in
preventing overcooling in the MYRRHA reactor.
Regarding sodium fire, the MINA (Mini Sodium Experimental) facility
at IGCAR aims to study the sodium aerosol characteristics and temperature
distribution in the large chamber in a spatiotemporal way [59]. This experimental
study provides significant insights into understanding the heterogeneous
distribution of aerosols along with the temperature distribution in closed
containment. CEA also investigated parameters impacting the potential intensity
of a sodium fire resulting from a pipe leak by using shadowgraphy to measure the
shape and droplet size of a water jet [46]. The results show good agreement with
empirical models and CFD, indicating the potential for these techniques to be
used to predict sodium droplet size under similar conditions.
At IGCAR, two mock-ups at respective scales of 5/8 and 1/4 were
implemented to optimize the design of the surge tank with the purpose of
reducing gas entrainment and dampening pressure surges [43, 60]. Regarding the
pressure surge caused by the release of gas during a sodium–water reaction, the
overpressure generated by a rupture disc in this experiment seems sufficient for
conducting a design study, but it is not suited to code validation, since the values
of the pressures are not within the same range.
Although lead and water do not chemically interact with the same intensity
as sodium, a steam generator tube break will still result in water flashing and
fast pressure transients. The LIFUS5 SET facility has been utilized through
three major modifications to study this and other phenomena related to steam

<!-- page 23 (PDF 35) -->
generators in heavy liquid metal reactors, resulting in a database of experimental
results used to assess system codes and inform steam generator design [61].

## 4.4. MEASUREMENT TECHNIQUES AND INSTRUMENTATION

The instrumentation highly depends on the fluid used in the experiments.
For instance, since lead and sodium are opaque, no optical techniques can be
implemented. In general, it is easier to instrument a water experiment than a
liquid metal one.
Measurements are necessary for the operation of the facility, but they
are also needed for the code validation. In the following, the focus will
be on this issue.

### 4. 4. 1. Temperature

In general, the temperature of the fluid or the material is measured using a
thermocouple or a PT100 sensor. The latter is more accurate (±0.1°C) but bigger
and has a lower time resolution. The mapping of the domain of interest is carried
out using moving probes. Other techniques were tested at CEA to measure the
temperature over a large area. The laser induced fluorescence method allows
for the determination of temperature in a large field. A laser is used to excite a
fluorescent species within the flow. This tracer, an organic fluorescent dye such as
fluorescein or rhodamine, absorbs part of the excitation energy and spontaneously
re-emits, depending on the temperature, some of the absorbed energy in the
form of fluorescence. The tests concluded that this method is feasible for small
experiments but not suited to large mock-ups. On the other hand, optical fibres
were used to measure temperature profiles in a water experiment. The temperature
calculation was based on the measurement of the elongation of the Bragg grating.
The tests showed high resolution over time, and this type of sensor seems as
accurate as a thermocouple. However, the great advantage is the ability to obtain
many measurement locations using one sensor. This measurement technique may
be used with liquid metal by employing encapsulation.

### 4. 4. 2. Velocity

At IGCAR, the velocity is investigated using an ultrasonic velocity profiler
and a propeller anemometer, since the mock-up is mainly built from metal and
has only a few optical access points.
Regarding the propeller anemometer, this technique is simple to implement
but is rather intrusive and may influence both the flow and the results. However,
