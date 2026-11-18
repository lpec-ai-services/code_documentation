# Special components
<!-- source PDF pages 25-39 -->

<!-- page 619 (PDF 25) -->
For side break, there are two expressions depending on the location of the level with
respect to the break. They are as follows:
X = X
1 + C
h
hb
□
□
1□0:5
h
hb
□
□
1 + h
hb
□
□
X
1□ h
hb
0:5
where,
C =1.09 for vapor pull through
=1.0 for liquid entrainment
X0=
1:15
1 +
ρl
ρg
!0:5
10.3
Special components
Reactorsystemcontainsmanycomponentsthatareimportantforreactorperformanceduringnormalandaccidentconditions
,suchaspumps,steamseparators,advanceaccumulator,
and jet pumps. These components in the reactor system have very complicated flow and
cannotbemodeledbytheformulationsofthecurrentsystemcodesandrequireseparateanalyses
both empirical and analytical. Some of these special components are described here.

## 10.3.1 Pumps

Reactor coolant pumps provide head to meet frictional losses in the loop. In addition,
the torque generated also makes up for energy supplied to the coolant and any frictional
losses in the pump. If there is a loss of power, the pump motor will not provide
the torque and the rotating element will start to coast down depending on pump inertia
and frictional losses. The pump head also decreases. In the case of reduction in pressure
, the coolant may flash and a two-phase mixture flows through the pump, leading
to degradation of the pump performance.
The head and torque characteristic functions have to be known in the four quadrants.
The head flow curve for the pump for single-phase flow is governed by specific
speed as defined below
Ns = ωq1=2=H3=4
The flow direction in the pump changes from radial flow pump to axial flow pump as
the specific speed increases as shown in Fig. 10.12. Here the specific speed is given in
metric units.

<!-- page 620 (PDF 26) -->
There are many pumps in operation as shown in Table 10.2.
Pumps are generally modeled as a point (or 0-D) module. A pump is located in a
node or a mesh and it adds source and/or sink terms to the momentum and energy
balance equations. The model also includes angular momentum equation that predicts
the rotation speed of the pump. The pump head and hydraulic torque are modeled
through user-defined characteristic functions of fluid flow rate and rotational speed.
The hydraulic torque is a sink term for the angular momentum equation and is multiplied
by the rotation speed in a source term for the fluid energy equations. The pump
head is also modeled through the user-defined characteristic functions of fluid flow
rate and rotational speed. The pump head appears as a source term in the fluid momentum
equations. If pump is free to rotate in reverse direction, the flow reversal can
do that.
Normally, the pump performance is reported in terms of homologous curves. The
parameters representing the performance are obtained from nondimensional analyses
such as Buckingham π Theorem. There are five independent variables, namely pressure
increase (ΔP), rotation (ω), flow rate (Q), diameter (D), and density (ρ) leading to
two nondimensional groups.
π1 =
ΔP
ρω2D2
π2 = ωD3
Q
FrIBo
2Nμ
−0.5(rI/Δr)
0.5
Frg(rg/Δr)
0.5
Onset of liquid entrainment
T/S: IB-SD
KfK Air-water data
INEL data
Data fit
correlation
Steam/water
Air/water
Incipient pull through data
Present
T/S:IB-SD
INEL
KfK
hb/(s/Δrg)0.5
hb/d
Fig. 10.12 Vapor pull through data for side oriented break.

<!-- page 621 (PDF 27) -->
Table 10.2 Available data for centrifugal pumps
Westinghouse
Bingham-Willamette
primary coolant
pump
Byron-Jackson primary coolant pump
RS111
Parameter
PWR
AP
W. small
pump
PWR
B & W
pump
PWR
primary
coolant
pump
C-E
pump
Creare
pump
KWU
pump
Scale
1/1
1/1
1/3
1/1
1/3
1/1
1/3
1/20
1/5, RS111
Rated volumetric
flow rate (gpm)
94,600
78,750
104,200
11,200
87,000
181 (219)
Rated total
head (ft)
64.4
293.7
Rated speed (rpm)
18,000
Specific speed rpm
(gpm)0.5/(ft)0.75
Fluid
S/W
S/W
A/W & S/W
S/W
A/W
S/W
S/W
A/W & S/W
S/W
Pressure (psia)
15–2250
15–420
15–2250
20–120
15–2250
15–1250
A/W at 90
S/W at 400
435–1305

<!-- page 622 (PDF 28) -->
H = ΔP
ρ
We can create alternate groups that can be transformed into homologous groups by
eliminating angular speed from π1. In addition, the parameters can be normalized with
design values so that groups remain with 1.0 and □1.0 as much as possible. The
geometric parameter, D will normalize to 1.0.
H*
Q*2 = F Ω*
Q*
□
□
We can get another set from π groups
H*
Ω*2 = F
Q*
Ω*2
□
□
This provides a general format for presenting any pump performance curves based on
nondimensional analyses and normalization with design values. There are four
possible flow combinations of flow and rotational speed (Choi et al., 2003).
Here, see Fig. 10.13,
a = Ω
Ωref
; v = Q
Qref
C -E/EPRI pump
RS 111 pumps
Semiscale pump
Flow
Head, power,
efficiency
Head, power,
efficiency
Head, power,
efficiency
Flow
Flow
Radial impeller
100 120
Francis impeller
Mixed - flow
Axial
Axis of rotation
Specific speed nq= n0×Q0
0.5× H0
−0.75 based on rated conditions
with nq, n0(min–1), Q0(m3/s), H0(m)
Impeller
Head
Efficiency
Power
Fig. 10.13 Design characteristics for centrifugal pumps.

<!-- page 623 (PDF 29) -->
Normal operation
HAN and HVN,
a>0, v>0; h/a2 vs v/a and h/v2 vs a/v
Reverse flow
HAR and HVR
a>0, v<0
Energy dissipation
HAD and HVD
a<0, v>0
Turbine operation
HAT and HVT
a<0, v<0
Some pumps have protection against reverse rotation and therefore third and fourth
quadrant flow and rotation combination (HAD, HVT, HAT, HVT) will not occur.
However, pump may become resistance device due to locked rotor (Fig. 10.14).
Single-phase pump performance is either available from manufacturer or can be
obtained easily.
A study by Schneider and Winkler (1988) indicated that two-phase performance of
the pumps depends on specific speed, void fraction, flow, pressure, and size. They
provided some nondimensional groups to account for flow stratification, slip in
phases, and flow coefficient effect on pump head degradation. An analytic study
by Furuya (1985) indicated that the performance degradation occurred due to increase
in liquid velocity, slip between the phases, and void fraction change. It should be noted
that this study does not include vapor compressibility, and increase in void fraction is
due to relative velocity of two phases.
The pump performance degrades based on three possible phenomena in the pump
channels: slip between vapor and liquid, phase separation, and vapor compressibility.
0.0
a/v or v/a
–0.5
0.0
0.5
HVD
HAR
HVR
h/a2 or h/v2
HVT
HAT
HAN
HAD
HVN
1.0
1.5
2.0
–1.2 –1.0 –0.8 –0.6 –0.4 –0.2
0.2
0.4
0.6
0.8
1.0
1.2
Fig. 10.14 Parameters for centrifugal pump modeling in system codes.

<!-- page 624 (PDF 30) -->
The separation leads to decrease in the component of absolute velocity in the direction
of rotating velocity as shown in Fig. 10.15 (Schneider and Winkler, 1988).
From Euler equation for pump head.
Pump Head = uoutincu,out □uincu,in
Here u is the azimuthal velocity of impeller, c is the actual fluid velocity, and cu is the
component of fluid velocity in direction of pump speed. As seen in the figure cu
decrease due to flow separation.
Tests with full size (Chan et al., 1999) indicated that pump performance degraded
rapidly around inlet void fraction of 0.35 for different inlet flows and inlet fluid temperature
, as shown in Fig. 10.16.
The current model uses inlet void fraction-based interpolating function between
single-phase and two-phase fully degraded (α>0.9) performance. The phase separation
could also depend on the flow field upstream of the pump. The study reported in
CSAU indicated that pump size, pressure, and specific speed have impact on performance
degradation (Fig. 10.17).
Most models only account for inlet void fraction effect on pump performance.
CSAU study (USNRC, 1989a) reviewed five sets of data from small-scale pumps
to 1/3 size Westinghouse pump as shown in Table 10.3. The analyses are described
in Appendix I of USNRC (1989a). It was shown that pump with larger specific speed
degraded less, larger pump with same specific speed degraded less, and data at higher
pressure degraded less.
The AP1000 pump is a large pump with a specific speed of 6050 in units of gpm, ft,
and rpm. As shown in Table 10.2, it will have larger specific speed than any other
pump. Based on CSAU analyses, it will have smaller effect of void fraction on performance
. Currently, Westinghouse 1/3 scale is the largest data that is widely used. As
the prototype pump (both AP1000 and regular PWR) will degrade less than Westinghouse
1/3 scale pump with same specific speed, the Westinghouse Test data may be
du3, sep = ωR sep
du3, sep
u3
C3
C3, sep
Fig. 10.15 Flow separation in
blade channel.

<!-- page 625 (PDF 31) -->
conservative for some transients as it will lead to stagnation and flow reversal sooner
during the blowdown phase of LBLOCA.

### 10.3.1.1 Model in system codes

The framework of pump models in TRACE and RELAP5 is based on homologous
curves that are supplied through input.
Usually pump vendors give only single-phase characteristic functions in the first
quadrant. It may be necessary to do experimental tests to get the pump characteristic
functions in the other quadrants. Moreover, two-phase characteristic functions have
also been given as user-defined functions since pump performance (head and torque)
is degraded in two-phase flow conditions. Usually two-phase characteristic functions
are also function of inlet void fraction. The single- and two-phase characteristics are
obtained empirically along with degradation functions M(α) and N(α).
Hhyd = H1ϕ □M α
ð Þ □ H1ϕ □H2ϕ
□
□
Thyd = T1ϕ □N α
ð Þ □ T1ϕ □T2ϕ
□
□
The pumps are generally modeled as a point (or 0-D) module. Turbine also adds
source and/or sink terms to the momentum and energy balance equations. The sink
and source terms are also modeled as user-defined functions. The degradation
0.00
0.10
0.20
0.30
0.40
0.50
0.60
0.70
0.80
0.90
1.00
1.10
1.20
1.30
1.40
0.1
0.2
0.3
0.4
Average pump suction void fraction
Normalized pump head, H/Hr
0.5
0.6
0.7
0.8
0.9
260 C / v=0.8 (D191)
260 C / v=1.0 (D184)
260 C / v=1.2 (D189)
Fig. 10.16 Pump head degradation as a function of void fraction at the inlet.

<!-- page 626 (PDF 32) -->
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Void fraction aF
CREARE/CE (NS 4200)
CREARE air/water (4200)
B&W air/water (4300)
Semiscale (926)
CANDU (2700)
KWU steam/water (6700)
Homologous pump head ratio
(H2f/Href)/ (W/ Wref)2
0.8
0.9
1.0
0.5
1.0
1.5
1.2
1.1
1.0
1.9
−150
±50
±50
±50
+60
0.8
1200 psia
1000 psia
850 psia
480 psia
0.7
0.6
0.5
0.4
Homologous pump head ratio
(H2f/Href) / (W /Wref)2
0.3
0.2
0.1
−0.1
0.1
0.2
0.3
Upstreamvoid fraction, aF, Homogeneous per orif.
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Fig. 10.17 Centrifugal pump performance, head versus entrance void relationship. Top: effect
of size. Bottom: effect of pressure.

<!-- page 627 (PDF 33) -->
function is shown in Table 10.3, derived from RELAP5 []. This function can also be
provided through input, see also Fig. 10.18.
The pump angular momentum balance is given as follows:
IdΩ
dt = □ Thyd □Tfrict
□
□
Here, I is the moment of inertia of moving parts; Thyd and Tfrict are hydraulic and
frictional torque, respectively; and Tfric is the function of impeller rotational speed.
Table 10.3 Degradation function for pump
head based on Semiscale pump
A
M(α)
0.00
0.0
0.07
0.0
0.08
0.74
0.165
1.0
0.90
1.0
1.00
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
0.1
0.2
0.3
0.4
0.5
0.000
0.00
0.00
0.74
1.00
1.00
0.00
0.070
0.080
0.165
0.900
1.000
Void fraction (a)
M2 (a)
M3 (a)
MM (a)
MM (a)
M (a)
(a)
Hand fit
Test S – 01– 4A
Points
Test S – 01– 5
Test S – 01– 1B
Multiplier M (a)
0.6
0.7
0.8
0.9
ANC – A – 6078
1.0
Fig. 10.18 Experimental data and modeling for the multiplier of two-phase pump performance.

<!-- page 628 (PDF 34) -->
## 10.3.2 Separators and dryers

Separators are used to separate steam and liquid water at core exit of BWRs or at the
top of PWR steam generators. These components are needed as wet steam has an
adverse effect on the life of turbines. In the case of BWRs, a two-phase mixture enters
the separator barrel, passing through a set of stationary swirl vanes. These vanes produce
a high rotational velocity in the fluid flowing through the separator barrel. The
resultant centrifugal force separates the steam-water mixture into a water vortex on the
inner wall of the separator barrel and a steam vortex in the core. The process is shown
in Fig. 10.19. The separated liquid film is picked from the wall as shown in the figure.
There are multiple stages of separator, each with a pick-up ring.
This separation process cannot be simulated by using the 1-D two-fluid model.
Special empirical models are used for the separators. The separator model determines
the low void fraction mixture that goes to downcomer and high void fraction mixture
Vent
Steam outlet nozzle
Water level
Measurement taps
Separator assembly
hold down bolt
Core spray nozzle
Core spray sparger
Upper core grid
In-core flux monitor
assembly
Core shroud
Fuel support piece
Control rod drive
housing
Two-phase
Mixture Inlet
(i) Standpipe
(iii) Discharge
(ii) Barrel
Bulk
Water
Level
Steam
Outlet
Pick-off
Ring
Liquid
Layer
Vapor
Core
Swirl
Vanes
Liquid
Discharge
DIS
IN
EX
Vessel support skirt
Core differential
pressure tap
Recirculating water
outlet nozzle
Feedwater inlet nozzle
Steam separator
Steam
separator
assembly
Steam pressure
measurement tap
Vessel head stud
Vessel head nut
Vessel flange
Steam separator
Standpipe
Steam plenum head
Diffuser
Control rod
Fuel assembly
Core plate
Lower core grid
Vessel wall
Control rod guide tube
Recirculating water
inlet nozzle
In-core monitor
sleeve
Feedwater sparger
Reactor vessel head
Steam dryer assembly
Fig. 10.19 Sketch of a BWR with detail for a single stage of steam separator.

<!-- page 629 (PDF 35) -->
going out of top outlet junction. In general, two options might be available: (i) a simple
separator model in which a steam-water inflowing mixture is separated by defining the
quality of the outflow streams using input specification and (ii) a mechanistic separator
model, which is intended to model the centrifugal separators by solving phasic
continuity equation, angular momentum equation, and axial momentum equation with
some simplifying assumptions. These are discussed in next section.
A sketch of a BWR with some details of the separators can be found in Fig. 10.19.
Dryer steam
Returning
water
Turning
vanes
Wet steam
Core discharge
plenum
Standpipe
Water level
operating
range
Fig. 10.19 Continued.

<!-- page 630 (PDF 36) -->
The steam dryer uses Chevron vanes to remove the moisture, which is discharged
from the steam separators. The vanes provide a curved path, which the liquid droplets
must follow if they are to flow through the dryer. The liquid droplets, flowing along
the curved path, hit the vanes due to their inertia and are de-entrained. The resultant
liquid film flows down the vanes under the force of gravity and then back to the liquid
pool surrounding the separators. The dryer efficiency depends on the steam velocity
and the moisture content of the steam flow entering the dryer. Since this process cannot
be simulated by using a 1-D two-fluid model, special models, which are either
simple or mechanistic, are used for dryers.

### 10.3.2.1 Model in system codes

System codes such as RELAP5 and TRACE used supplied values for carry over quality
(Xco) and carry under quality (Xcu). Carry over quality determines amount of liquid
that is carried by the vapor. Carry under quality determines the amount of vapor that is
carried by the discharged liquid. The purpose of this model is to predict the liquid flow
rate going out with vapor and vapor going down in the downcomer.
_ml,in = _ml,ex + _ml,dis
_mg,in = _mg,ex + _mg,dis
Xco =
_ml,ex
_ml,ex + _mg,ex
Xcu =
_mg,dis
_ml,edis + _mg,dis
This set of equation is solved for each stage of separator and will predict the mixture
going into downcomer. The inlet liquid and vapor flow from the core exit are known
and Xco and Xcu are specified. This is an important parameter as it will influence the
core inlet subcooling and therefore, the core power.
General Electric, EPRI, and USNRC (Cheung et al., 1983) also developed a mechanistic
model to predict the carry over and carry under. The model includes angular
momentum conservation that leads to redistribution of liquid and vapor with liquid
migrating toward the wall where it is picked up and discharged to downcomer.
However some of the vapor also picked up leading to carry under. Fig. 10.19 shows
the configuration of separator that is modeled. The two-phase mixture enters the separators
from stand pipes. Separator has swirl vanes that create a vortex that separates
the liquid toward wall and vapor in the center.
The model assumes that the axial velocity is uniform, tangential velocity is based
on vortex strength, void fraction distribution is based on measurements and is related
to inlet quality, Xi, pressure in gas core is uniform and in the liquid film is based on
centrifugal force. The velocity and void fraction distribution are as given here.

<!-- page 631 (PDF 37) -->
∝=
1□b r
rw
0 ≡ r ≡ rf
a rw
r □1
rf ≡ r ≡ rw
<
:
where
a = AA
ffiffiffiffiffiffiffi
gr2
w
p
C
!0:5
X2
i
For Xi < 0:15
a = AA
ffiffiffiffiffiffiffi
gr2
w
p
C
!0:5
0:09335
ð
ÞX2
i
For Xi > 0:15
b = BB
ffiffiffiffiffiffiffi
gr2
w
p
C
!0:5
1□X1
ð
Þ3 For Xi < 0:15
AA and BB are based on data as given in Table 10.4.
In addition to this distribution, there are conservation equations for mass and
momentum that can be solved for gas and liquid velocities. The carry under flow rate
of liquid and gas is given as follows.
For liquid film thicker than pick-off ring and barrel wall,
Wg,cu = πρgvaf a rw □rr
ð
Þ3:
Wl = πρlvaf
r2
w □r2
r
□
□
□a rw □rr
ð
Þ2
h
i
For liquid film thinner than the pick-off ring, one gets:
Wg,cu = XiWi □2πρgvag
2□ brr
3rw
□
□
r2
r
Wl,cu = 1□Xi
ð
ÞWi □2πρlvagr2
r
□ □
b rr
rw
Table 10.4 Design data for steam separator
Parameter
2-Stage separator
3-Stage separator
1st Stage
2nd Stage
1st Stage
2nd Stage
3rd Stage
AA
BB
0.5
0.25
0.5
0.25
0.55

<!-- page 632 (PDF 38) -->
From mass balance carry over can be calculated,
Wg,co = Wg,in □Wg,cu
Wl,co = Wl,in □Wl,cu
Liquid and vapor mass balances are given as,
1□Xi
ð
ÞWi = 2πρlvagr2
r
□ □
b rr
rw
r2
f + 2πρlvag
1 + a
□
□
r2
w □r2
f
□arw rw □rf
□
□
XiWi = 2πρgvag
2□ brr
3rw
□
□
r2
r + 2πρgvag
a rw □rf
□
□2
Angular momentum equation provides pressure drop radial film.
ðrw
rh
vtnr 2πrρmvan
ð
Þdr =
ðrw
vtr 2πrρva
ð
Þdr + Ftrw
Ft = 0:5ρlCf v2
w 2πrw
ð
ÞHD
□
□vtw
vw
Here vtw and vw are tangential and total velocity at the wall and rh is hub radius.
Axial momentum balance is given as
πr2
hP0 + 2π
ðrw
ρmiv2
an + Pn
□
□
rdr = 2π
ðrw
ρv2
a + P
□
□
rdr + Fa
Fa = 0:5ρlCf v2
w 2πrw
ð
ÞHD
□
□vaf
vw
The details of this model are given in RELAP5 and TRACE manuals ().

## 10.3.3 Accumulators

Accumulators store coolant and inject when system pressure is sufficiently low to
open the valve in accumulator line. Accumulators may be modeled either using standard
modules (0-D, 1-D, valves, tee, walls) of the codes or by a specific accumulator
model. The specific module must predict:
l
Accumulator pressure as function of remaining mass and of heat released from accumulator
walls (from isentropic depressurization for rapid discharge to quasi-isothermal for slow
discharge).
l
Flow rate delivered to the circuit as function of valve opening, accumulator pressure,
primary circuit pressure, pressure losses, etc.

<!-- page 633 (PDF 39) -->
l
Mass momentum and energy source terms in both phases in the injection mesh.
l
If some specific options are actuated, the accumulator-specific module should also predict
the amount of dissolved nitrogen in liquid water and the source term of nitrogen in gas mixture
in the case of transport of noncondensable gas.
Recently, MHI provided model for advanced US PWR (Fig. 10.20). The advanced
accumulator has a vortex device at the bottom of the tank that replaces a valve in
surge line and controls the flow rate. Similar design is used in new Korean PWR.
Initially there is flow through central pipe into vortex chamber leading to radial flow
in the vortex chamber exiting in surge line. After certain amount of flow has been
released, there is no flow through the central pipe and only tangential flow at the
bottom of the tank into the vortex chamber. This leads to vortex flow, increase in
friction, and reduction in flow. MHI had a full length, half size test facility and
developed a model to connect pressure difference between top of the accumulator
and cold leg, liquid level for early flow and later vortex flow case. As the vortex
chamber was only half size, there was some scale distortion that was estimated using
computational fluid dynamics (CFD) analyses of prototype and the test facility.
Scale distortion was very small. However, CFD procedure contributed additional
biases.
The data were plotted in the form of flow coefficient and cavitation number.
Cv =
Q
Ad
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
2 pa □pdT
ð
Þ=ρ
p
σv = pd □pv
pa □pdT
Small flow rate (later stage)
Large flow rate (initial stage)
Small flow pipe
Small flow pipe
Large
flow pipe
Large flow pipe
Vortex
chamber
Vortex
chamber
Vortex
chamber
Outlet
port
Throat
Diffuser
Throat
Diffuser
Standpipe
Standpipe
Injection pipe
Low water level
High water level
Accumulator tank
N2
Standpipe
Outlet
port
Water-level change
Fig. 10.20 Advanced accumulator with “vortex” device to control delivered flow rate.
