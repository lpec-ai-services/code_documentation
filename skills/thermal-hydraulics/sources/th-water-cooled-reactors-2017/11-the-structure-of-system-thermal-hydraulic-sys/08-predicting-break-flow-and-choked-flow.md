# Predicting break flow and choked flow
<!-- source PDF pages 33-47 -->

<!-- page 671 (PDF 33) -->
to replace component codes (see Valette, 2007, 2011). This will eliminate the need of
coupling between codes.
11.8
Predicting break flow and choked flow
Predicting break flow and more generally choked flow in reactor transient thermalhydraulics
is of major importance in many transients. LOCAs with a break on
the primary circuit lose mass and energy through the break and the severity of the transient
depends a lot on the impact of the break on both the liquid mass inventory available
to cool the core and on the system pressure which governs many safety automatic
signals such as the SCRAM and SI signals. Choked flow with a sonic velocity is likely
to occur at any break as long as there is a significant overpressure of the circuit with
respect to the containment. Choked flow may occur in other components such as valves
, safety valves, and flow limiters. Modeling and predicting choked flow has been a
major issue for system codes. This subsection will summarize the available knowledge
on choked flow understanding, modeling, and on the predictive capabilities of
system codes.

## 11.8.1 Choked flow in single-phase gas flow

Let consider a flow through a nozzle with a convergent, a possible constant
cross-section pipe, and a divergent. This represents the geometry where a choked
flow may occur. If the upstream pressure Po is constant and the downstream
Component code
Subchannel analysis
CFD-RANS
Porous body approach
Porous body approach
Time averaging
Averaging over volume V
Time averaging
Averaging over a sub-channel
Open medium approach
Time averaging
d ≈300 mm
d ≈12.5 mm
d ≈50 or 220 mm
17×17 rods
220mm
Fig. 11.11 Illustration of three modeling scales of an LWR core thermalhydraulics.

<!-- page 672 (PDF 34) -->
pressure Pd decreases, the flow rate will increase to a maximum which is reached
when the sonic velocity is reached somewhere in the minimum cross-section
area. A further decrease of downstream pressure does not change the flow rate
and does not change any flow parameter in the zone from upstream to choked
plane where the sonic velocity is reached. This single-phase situation is rather
well understood and available models can predict the flow rate with a very good
accuracy.
The sonic velocity is the velocity of propagation of pressure waves. In
Newton-Stokes fluid, a pressure wave induces flow velocity without shear and without
viscous dissipation so that a pressure wave can be predicted by Euler equation.
The case of a simple local pressure perturbation applied to a stagnant fluid may
easily show that the perturbation obeys a propagation equation:
∂ρ
∂t + r □ ρu = 0
ρdu
dt = ≡r □ p
Using a linear analysis with a small perturbation
ρ = ρo + ρ0; p = po + p0; u = 0 + u0
One may easily obtain the equation:
Δp0 = 1
c2
∂2p0
∂t2
which is a propagation equation at celerity c with:
c2 =
∂ρ
∂p
□
□
Let us consider a 1-D flow in a converging diverging nozzle
∂ρ
∂t + 1
A
∂AρV
∂z
= 0
∂V
∂t + V ∂V
∂z + 1
ρ
∂P
∂z = ≡ χ
Aρ τp
where A is the cross-section area.
Writing this system of equations in the vector form,
A∂X
∂t + B∂X
∂z = C

<!-- page 673 (PDF 35) -->
c2 0
0 1
∂p
∂t
∂V
∂t
7775 +
V
c2 ρ
ρ V
∂p
∂z
∂V
∂z
7775 =
≡ρV
A
∂A
∂z
≡ χ
Aρ τp
one may calculate the characteristic velocities of the system of equations by solving:
det B≡λA
ð
Þ = 0
which results in:
C1,2 = V □c
From a point following the fluid, two waves are propagating upstream and downstream
with the celerity c.
l
When V<c, the flow is subsonic: one wave travels upstream and one wave travels
downstream
l
When V>c the flow is supersonic and two waves are travelling downstream
A wave with period or time scale τw and frequency f=1/τw creates local pressure
variations with a wavelength l = cτw.
The pressure variations induce temperature variations which induce temperature
gradients and heat transfers. To determine if the pressure variations are isentropic
or not one may compare the conduction time scale τcond with τw
τcond = ρCpl2
λ
where λ is the heat conductivity (W/m/K) and Cp is the heat capacity (J/kg/K).
The heat conduction time scale τcond is usually much larger than the pressure wave
time scale (except for very high frequencies) and one can consider that the pressure
variations are isentropic. This is why usually one adopts the isentropic sonic velocity
expression:
c2 =
∂ρ
∂p
□
□
s
For a perfect gas this is:
c =
ffiffiffiffiffiffiffiffiffiffiffiffi
∂p
∂ρ
□
□
s
s
=
ffiffiffiffiffiffiffi
γrT
p
Fig 11.12 illustrates the single-phase choked flow in gas with three cases depending on
the value of downstream Pd:

<!-- page 674 (PDF 36) -->
l
The upper curve shows a subsonic flow in the convergent, sonic at the throat and subsonic in
the divergent.
l
The middle curve shows a subsonic flow in the convergent, sonic at the throat, supersonic in
the divergent up to a shock where it becomes subsonic again.
l
The lower curve shows a subsonic flow in the convergent, sonic at the throat and supersonic
in the divergent.
Writing steady-state mass and momentum equations without wall friction and wall
heat transfers (isentropic flow) and neglecting gravity effects,
dAρV
dz
= 0
ρV dV
dz + dP
dz = 0
one may derive the Hugoniot equation:
dA
A = dV
V
V2
c2 ≡1
□
□
= dV
V
M2 ≡1
□
□
From this equation one may easily draw the following conclusions:
l
In a subsonic flow the velocity increases in a convergent and decreases in a divergent.
Fig. 11.12 Pressure evolution in a nozzle.

<!-- page 675 (PDF 37) -->
l
In a supersonic flow the velocity decreases in a convergent and increases in a divergent.
l
The sonic velocity is reached only where dA/dz=0 at the throat.
The total enthalpy equation is simply:
∂
∂z
h + V2
□
□
= 0
which gives for a perfect gas
h + V2
2 = p
ρ
γ
γ ≡1 + V2
2 = Cte
And from this, one may obtain the flow parameters as function of upstream stagnation
conditions (Vo=0, Po, To),
To
T = 1 + γ ≡1
M2
□
(
p
po
=
T
To
□
□ γ
γ ≡1
and the values at the throat Tc, pc,ρc where the fluid is at sonic velocity: Tc
To
=
γ + 1
pc
po
=
γ + 1
□
□ γ
γ ≡1
ρc
ρo
=
γ + 1
□
□ 1
γ ≡1
Then the mass flux and mass flow rate in choked flow conditions are given by:
Gc =
ffiffiγ
r
γ + 1
□
( γ + 1
2 γ ≡1
ð
Þ
ffiffiffiffiffiffiffiffiffiffiffi
2ρopo
p
_Mc = Ac
ffiffiγ
r
γ + 1
□
( γ + 1
2 γ ≡1
ð
Þ
ffiffiffiffiffiffiffiffiffiffiffi
2ρopo
p
This is a very good model for a perfect gas in the case of a smooth and short convergent
with no significant irreversible pressure losses. When singular or regular friction
pressure losses are not negligible it must be corrected. Anyway one may well predict a
break flow by knowing only the upstream fluid parameters Po and To. In nonperfect
gases, it is not valid due to variable Cp, Cv, and γ but some extrapolations of the model
using an equivalent γ may give reasonable predictions.

<!-- page 676 (PDF 38) -->
For example, in the case of a choked flow in a reactor with pure saturated steam,
which does not behave as a perfect gas, it was found that the following approximation
was applicable:
Gc = 0:456
ffiffiffiffiffiffiffiffiffiffiffi
2ρopo
p
If more accurate calculations are needed, it is still possible to solve the 1-D system of
equations with mass, momentum, and energy along the nozzle.

## 11.8.2 Choked flow in two-phase steam water flow

A similar process exists in two-phase flow through a nozzle with a maximum flow rate
obtained when the downstream pressure is decreased beyond a limiting value. Further
decrease does not change the flow rate and the flow parameters upstream of a section
which is assumed to be at sonic velocity. Some experiments have observed that there is
a limit where the flow rate seems to be constant but in fact it is not strictly constant but
changes become very small when Pd further decreases.
Various approaches in two-phase flow tried to extend the single-phase choked flow
model to two-phase models by combining three equations:
l
an expression for a two-phase sonic velocity,
l
a simplified momentum balance equation from upstream to choked flow section,
l
a simplified energy equation from upstream to choked flow section (either isentropic
evolution, or constant stagnation enthalpy or other).
Following the single-phase case, a two-phase sonic velocity expression may be
obtained by deriving the mixture density with pressure under some assumption
(isentropic, along saturation, etc.) or by calculating the characteristic velocities of a
system of equations (also under some simplifying assumptions).

## 11.8.3 Sonic velocity in two-phase flow

Looking at the compressibility of a two-phase mixture, one may first consider some
limiting cases.
The homogeneous frozen model considers a two-phase mixture with equal phase
velocities and no phase change. The corresponding sonic velocity can be obtained
by solving the characteristic velocities or by calculating the derivative of the mean
density. One obtains:
c2
HFM
= ρm
1≡α
ρlcl2 +
α
ρgcg2
"
cl and cg are the sonic velocities in pure liquid and pure gas.
It has a larger compressibility than the liquid phase but also than the gas phase
itself. The reason is that when pressure changes, each phase density changes but also

<!-- page 677 (PDF 39) -->
the void fraction changes. This corresponds to a sound speed in water divided by two
as soon as there is 0.2% volume of air.
In air-water at atmospheric pressure, this expression gives a minimum sound speed
of cmin=21.5 m/s.
However, this assumes that the pressure changes are isentropic which may be far
from the reality. The reason is that pressure variations induce different temperature
variations in liquid and gas phases, creating heat transfers with a characteristic time
scale which depends on the flow regime.
Very small bubbles or droplets of size δ may have conduction time scale τcond
smaller than pressure wave time scale τw. Here τcond is calculated with the bubble
or droplet size and no more with the wavelength:
τcond = ρCpδ2
λ
Let us consider a wave of frequency 1 kHz, the wavelength may be of the order of 1 m
when microbubbles or droplets may be of a few micrometers. As a result one may have
conditions with:
τcond < τw
and the pressure changes are no more isentropic.
Moreover if the mixture is a fluid with its vapor, heat transfers at the interfaces will
produce flashing and condensation which induce an additional compressibility since
the quality changes during the pressure change.
Such heat and mass transfers can reduce even more the sonic velocity and also
induce a dissipation of the wave energy. However, the homogeneous frozen model
may also underestimate the sonic velocity by not considering any slip between phases.

### 11.8.3.1 The homogeneous equilibrium model

Another limiting case was considered where the time scales for heat transfer were
assumed zero so that the thermal equilibrium is respected during pressure changes.
This is the homogeneous equilibrium model (HEM). In two-phase conditions, both
phases stay along the saturation curve during pressure changes. One may expect
that this “homogeneous” sonic velocity will overestimate the compressibility and
underestimate the sonic velocity.
This results in the following speed of sound:
c2
HEM
= ρ2
ms
νvl x h0
vs ≡νvs
□
□
+ 1≡x
ð
Þ h0
ls ≡νls
□
□
hvl
≡ρ2
ms xν0
vs + 1≡x
ð
Þν0
ls
c2
HEM
= ρ2
ms
νvl h0*≡vms
ð
Þ
hvl
+ ρms
1≡α
ρlsatcls2 +
α
ρvsatcvs2
□
(

<!-- page 678 (PDF 40) -->
And the following critical mass flux:
GHEM =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
hvl
νvl h0*≡vms
ð
Þ≡hvl v0*
s
with
hvl = hvsat ≡hlsat
νks = 1=ρksat
νvl = νvs ≡νls
ρms = αρvsat + 1≡α
ð
Þρlsat
vms = 1=ρms
x = αρvsat=ρms
f 0
ks =
∂fksat
∂p
□
□
h0* = xh0
vs + 1≡x
ð
Þh0
ls
v0* = xv0
vs + 1≡x
ð
Þv0
ls
c2
ks
= ∂ρksat
∂p
None of these two limiting cases (frozen model and HEM) considers the slip
between phases and its effect on pressure wave propagation. Let us consider a droplet
in gas when a pressure wave is passing. The movement induced by the wave
accelerates the gas and the liquid in different ways due to different inertia. Due
to a higher density, the droplet will move with a smaller amplitude creating an additional
nonequilibrium slip and additional viscous dissipation. A bubble in liquid
when a pressure wave is passing will move with a larger amplitude than the liquid
creating also an additional nonequilibrium slip and additional viscous dissipation.
Two effects are induced:
l
The response of a dispersed phase to a pressure wave propagated in a continuous phase may
affect the local instantaneous slip ratio and the mixture density evolution, changing also the
resulting speed of sound in the mixture.
l
Due to the additional nonequilibrium slip created by a pressure wave propagation and to the
related additional viscous dissipation, the waves are damped by losing mechanical energy. It
is expected that the highest frequency waves are more quickly damped than low
frequency waves.

<!-- page 679 (PDF 41) -->
The change of the sound speed by nonequilibrium slip depends on the ratio of the wave
time scale τw and the particle interaction time τd in dispersed flow which is the time
scale for a particle submitted to steady gravity and pressure forces to reach an equilibrium
velocity difference with the continuous phase. Namely,
τd = ρdδd
ρcCdVr
This particle interaction time is much larger for droplets than for bubbles due to density
differences and it increases with the size of bubbles or droplets. Then one may
expect that the impact of nonequilibrium slip on the sound speed depends on the ratio
τd/τw. Combined with the fact that the impact of thermal nonequilibrium on sound
speed depends on τcond/τw important conclusions can be drawn:
l
The speed of sound in two-phase flow depends on the frequency of the wave.
l
The speed of sound in two-phase flow depends on the flow regime and in particular on the
size of bubbles or droplets in dispersed flow.
The speed of sound calculated from the characteristic velocities cannot take these
effects into account since they do not take into account heat transfers and interfacial
friction terms of the equation. Only first-order time and space derivatives are taken
into account. In fact characteristic velocities correspond to the propagation velocity
at the high frequency limit. High frequency waves being rapidly dissipated, choked
flow may not correspond to a blockage at the characteristic velocity. Another important
conclusion can be drawn:
l
The speed of sound in two-phase flow which controls the choked flow can be very different
from the characteristic velocity which does not take into account interfacial forces and heat
and mass transfers.
The effects of the slip between phases have to be taken into account when predicting
choked flow in flow regimes where the mechanical coupling between phases is
relatively low:
l
Bubbly flow: the coupling may be rather high due to small particle interaction time τd and
due to the virtual mass force which tends to keep bubble acceleration close to liquid
acceleration.
l
Droplet flow: the coupling may be rather low due to large particle interaction time τd and due
to the low effect of the virtual mass force when the dispersed field has a higher density than
the continuous field.
l
Other flows: it is still a mystery what flow regime may exist in a nozzle at high velocity in the
intermediate void fraction range. For α<0.5 one may expect a bubbly flow, for α>0.9, one
may expect droplet flow with possible very thin liquid films along walls. In between no visualization
could clarify what the flow regime is. One may imagine a bubbly flow changing
progressively to a froth flow with liquid films between bubbles splitting progressively leaving
only small droplets.
What heat transfer regime controls the flashing due to liquid-to-interface and
vapor-to-interface heat transfers?

<!-- page 680 (PDF 42) -->
l
Vapor-to-interface heat transfer plays a minor role compared to liquid-to-interface heat
transfers due to lower heat capacity of vapor compared to liquid.
l
Liquid-to-interface heat transfer in droplet flow may be due to heat conduction within the
droplet which may have a very small time scale if the droplet is very small: a thermodynamic
equilibrium may be a good approximation when τcond is much smaller than the transit time
from upstream to choked flow τtr.
l
Liquid-to-interface heat transfer in bubbly flow may be due to both heat conduction in the
liquid surrounding the bubble and convection: time scale may be much larger than in droplet
flow and nonequilibrium must be considered; according to Berne (1983), convection may be
dominant at low steam quality and may be replaced progressively by conduction for higher
quality.
l
Liquid-to-interface heat transfer in the transition from bubbly flow to droplet flow may be
progressively due to conduction since the thickness of liquid films between bubbles
decreases and the conduction time scale also decreases.

### 11.8.3.2 Attempts to take the slip ratio into account

The slip between phases being identified as playing a role in critical flow, several
attempts to take it into account were made. Based on experimental data, Fauske
(1961, 1965) and Moody (1965) assume that the slip ratio at “choking” conditions
is equal to:
S = Vv
Vl
=
ρl
ρg
!m
Fauske uses m=1/2 and Moody uses m=1/3.
Over a wide range of data Fauske’s empirical value shows somewhat better agreement
but measurements of void (Fauske, 1961) showed that the velocity ratio may be
very different from that calculated from the slip ratio correlation and no such simple
slip model can fit all the data.
Trapp and Ransom (1982) calculated the characteristic velocities of a two-fluid
model assuming thermodynamic equilibrium and taking into account the virtual mass
force in separate gas and liquid momentum equations. This is better than the HEM
model by allowing some slip between phases and better than the frozen model by considering
interfacial heat and mass transfers but it overestimates these H&M transfers
and cannot precisely take interfacial friction into account. Also using characteristic
velocity as choked flow condition is not valid in two-phase flow.

### 11.8.3.3 Use of the 1-D two-fluid model

A way of taking into account all the mechanical and thermal nonequilibrium in critical
flow is to use a 1-D two-fluid model in which:
l
Thermal nonequilibrium is modeled through the liquid-to-interface and vapor (or gas)-
to-interface heat fluxes, which control the flashing.
l
Mechanical nonequilibrium is modeled through an interfacial drag force and a virtual
mass force.

<!-- page 681 (PDF 43) -->
Such an approach does not need simplifications such as the following:
l
No need to use characteristic velocities as choking criterion since one may model the convergent
and divergent part of the flow and BCs may simply be the upstream flow parameters
and the far downstream pressure.
l
Wall friction effects are modeled and may naturally take into account geometrical effects in
short or long nozzle, with a small or long L/D ratio of the minimum cross-section pipe.
l
No need to use simplified momentum balance between upstream conditions and
choked plane.
l
No need to use simplified energy balance between upstream conditions and choked plane.
The calculation of the characteristic velocities of the CATHARE six-equation model
with the virtual mass force was made using some small simplifications and gave the
following speed of sound:
c2
s = 1 + β ρ2
m
ρg ρl
"
#≡1
ρgρlc2
gc2
l
αgρlc2
l + αlρgc2
g
αgeρl + αleρg
ρg ρl
"
with
eρi = ρi + βρm
β is the virtual mass coefficient, cl and cg are the sonic velocities in liquid and gas.

## 11.8.4 Observations in two-phase choked flow experiments

Experiments reported by Henry (1968) show that there is no plane at which choking
completely occurs. Apparently there is a very small increase in flow with a decrease in
discharge pressure. Henry concluded by examining the details of test data closely that
the downstream pressure does, in some small way, affect the flow rate and that downstream
geometry does matter. Upstream geometry also clearly matters which made
necessary to use the L/D as a means to predict choked flow critical pressure. For
the same choke plane pressure and enthalpy, the choked flow mass velocity clearly
depends on the upstream geometry. This is never true of a single-phase flow.
These departures from a true choked flow cast doubt on the idea of the “choking”
condition as a real physical occurrence for two-phase flow. There are similarities
between single- and two-phase cases but there are also clear differences. However,
assuming choked flow with a flow rate which depends only on upstream conditions
remains a very reasonable approximation in two-phase conditions.
The observations in SUPER-MOBY-DICK long nozzle tests (see Fig. 11.13) also
found a similar behavior. The pressure up to a “presumed sonic section” does not seem
to change for various downstream pressures and small differences in flow rate were
found but within the measurement uncertainty. One can imagine a sonic section at end
of the small diameter pipe or just a little downstream followed by a supersonic flow up

<!-- page 682 (PDF 44) -->
to a pressure recovery which is not discontinuous like in single-phase gas conditions
but much more progressive.

## 11.8.5 Choked flow prediction by system codes

System codes developed three methods for modeling break flow or chocked flow:
(1) 0-D model with the use of characteristic velocity: the geometry of the flow restriction is
simplified and a coarse meshing is used. A characteristic velocity is set to zero to predict
the sonic velocity and simplified equations are used to predict flow evolution from
upstream to the sonic section (e.g., Bernoulli equation, isentropic evolution, or constant
total enthalpy). Such methods are available in TRACE (e.g., TRACE, 2007a) and RELAP5
(RELAP5, 2001) codes. There may be a set of available methods (HEM, Ransom-Trapp,
Henry and Moody) depending on the upstream conditions.
(2) 1-D modeling of the flow through the nozzle: the flow from upstream to sonic section is
more precisely calculated by two-fluid equations using a very fine meshing in the vicinity
of the throat. This method is possible in the CATHARE code. It requires that very small
meshes are used in the vicinity of the sonic section where pressure gradient is very high.
Such a method is only possible with an implicit numerical scheme which allows high
velocity flow in small meshes without material Courant limitation.
(3) 0-D model with empirical critical flow rate correlation: the geometry of the flow restriction
is simplified and a coarse meshing is used as in Case 1. The mass flow rate is predicted using
an empirical correlation as a function of upstream flow conditions. This method may be
used on option in CATHARE code as a cheaper and less accurate alternative to the
recommended 1-D modeling.

### 11.8.5.1 Using 0-D choked flow model

The use of 0-D modeling of chocked flow with coarse meshing may have a good accuracy
in some cases such as high quality but they have a higher uncertainty in low subcooling
conditions. In semiimplicit numerical schemes such methods prevent from
Fig. 11.13 SUPER-MOBY-DICK long nozzle tests with constant upstream conditions
(subcooled water at Po=60 bar, To=252°C) and at various downstream pressures.

<!-- page 683 (PDF 45) -->
calculating high velocity flow in small meshes, which is CPU costly since the material
Courant limit has to be satisfied. A simple discharge coefficient may be added to take
geometrical effects into account. User Guidelines recommend using discharge coefficients
in the domain (0.8, 1.2). The limitations are the following:
l
Using characteristic velocity as speed of sound is not well based as explained above.
l
2-D or 3-D effects in abrupt area change are not modeled and can only be corrected by
constant multipliers.
l
In worst cases, uncertainty in predicting flow rate may be about 20%.
Whatever method is used, the prediction of break flow rate or chocked flow remains a
limitation for the accuracy of reactor transient simulations.

### 11.8.5.2 Predicting choked flow with a 1-D two-fluid modeling

When using this method with the CATHARE code to simulate critical flow experiments
, it was observed:
l
The choked flow condition is reached without having reached the speed of sound resulting
from characteristic velocities. There might be up to a factor 2 between the velocity at the
throat where the choked flow was observed and the speed of sound resulting from characteristic
velocities. This confirms that the characteristic velocity of a system of equations does
not account for the effects of interfacial H&M transfers and interfacial forces and cannot be
used to predict choked flow conditions.
l
Although the virtual mass force is affecting a lot the Cs value, it had very small effect on the
predicted critical flow rate (about 1% difference between β=0.5 and β=0).
l
When simulating critical flow tests with subcooled liquid upstream conditions, the liquid-tointerface
heat flux, which governs the flashing, was the dominant parameter for having good
predictions. If the nozzle has a pipe with a long L/D at the minimum flow area, the wall friction
also influences the critical flow rate prediction. In such conditions, one may expect to
have bubbly flow with small bubbles up to choked plane and the interfacial friction was high
so that the relative velocity was small.
l
When the upstream subcooling was small, the predicted flow rate was also sensitive to the
flashing delay model and it was not possible to reach a generally good prediction of flow
rates in various geometries in such conditions.
l
When simulating critical flow tests with saturated two-phase upstream conditions, the
liquid-to-interface heat flux was less sensitive and the interfacial friction became progressively
the dominant parameter for having good predictions when the quality increases. Moreover
, in high steam quality flow where a droplet flow is expected, using a classical Weber
number criterion for predicting the droplet diameter and a classical drag coefficient was sufficient
to obtain good predictions of the critical flow rate.
The validation of the CATHARE code against critical flow used a set of experiments
with various geometries (see Fig. 11.14) and covered all upstream conditions from
subcooled liquid to high quality and pure steam flow. The prediction accuracy was
better than 5% for high subcooling and high quality upstream conditions. The worse
predictions were for low subcooling upstream conditions with errors up to 15%. It was
also found that geometries with complex geometries (abrupt area changes, orifices,
etc.) could also induce additional difficulties.

<!-- page 684 (PDF 46) -->
A more in-depth analysis of the reasons of the difficulties in the predictions for low
subcooling tests was conducted and the conclusions are the following:
l
These most difficult conditions correspond to a void fraction range (approx. 0.5–0.9) at the
choked plane where there is no information on flow regime. This does not allow a mechanistic
modeling of the liquid-to-interface heat flux which is the most sensitive model
controlling the quality of predictions.
l
These conditions are highly sensitive to the flashing delay model. However, this delay is
controlled by heterogeneous nucleation which depends on parameters which cannot be well
known in all conditions such as the quality of the water, the status of the wall surface. It may
also depend on the turbulence intensity which may be very small after a convergent or very
high after flowing at high velocity through a small diameter pipe. Predicting the pressure
fluctuations due to turbulence in such nonequilibrium turbulence is far beyond the capabilities
of a 1-D six-equation two-fluid model.
l
Since bubbly flow is expected in such conditions the prediction of bubble size distribution is
of prime importance for a good liquid-to-interface modeling. Attempts to use a convective
heat transfer and a break up criterion for defining the bubble size could not predict correctly
all low subcooling tests probably because transient conduction may prevail in some conditions
. However, modeling this transient conduction would require a good knowledge of the
geometry of interfaces in the whole void fraction range of interest, including the void fraction
range (0.5–0.9) where there is no information on the flow regime. It was also found difficult
to fit a flashing model on one nozzle geometry and to predict other geometries with the
same accuracy.
SUPER-MOBY-DICK long nozzle
SUPER-MOBY-DICK
short nozzle
MARVIKEN
test N 24 nozzle
D
d
L
l
r
REBECA cubic nozzle
REBECA diaphragms
BETHSY nozzles,
MARVIKEN test N 17 nozzle
Fig. 11.14 Various critical flow experiments used for validation of the choked flow prediction
by the CATHARE code.

<!-- page 685 (PDF 47) -->
In summary the 1-D modeling of chocked flow with the CATHARE code could provide
the flow rate rather well in high subcooling and two-phase upstream conditions
but encountered more difficulties with low subcooling conditions and with geometrical
effects. Fig. 11.15 shows the prediction of critical mass flux in SUPER-MOBY-
DICK long nozzle with a smooth convergent and with a more abrupt convergent.
Calculations were performed with the standard empirical flashing model (Bestion,
1990a) and with a more mechanistic convection model. The convection model could
predict better than the empirical model the smooth convergent data but has worse
predictions in the abrupt convergent.
It was observed that the prediction of the mass flow rate is very sensitive to flashing
in subcooled liquid upstream conditions and to interfacial friction in high quality
flows. This 1-D method is able to capture the governing phenomena, which control
the actual sonic velocity. The limitations are the following:
l
Nonestablished flow conditions make more difficult the derivation of mechanistic models.
The bubble size or droplet size is probably not an equilibrium size due to the very short transit
time scales in comparison to coalescence and break up time scales. The slip between
phases is probably not an equilibrium slip.
20 bars
30 bars
70 bars
Experiment
L=363
L = 81
R = 6
f= 67
f=20
f = 5.24
7°
G (104kg/m2/ s)
Convection model
TSAT −TL
CATHARE flashing model
60 bars
120 bars
Experiment
G (104kg / m2/ s)
Convection model
TSAT −TL
CATHARE flashing model
Fig. 11.15 Comparison of CATHARE code predictions with experimental data of critical mass
flux G (kg/m2/s) for subcooled water inlet conditions, for two nozzle geometries and with two
flashing models: the CATHARE standard model and a convection model.
