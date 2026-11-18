# Part 2: Boiling Heat Transfer — Unstable boiling modes
<!-- source PDF pages 119-121 -->

<!-- page 475 (PDF 119) -->
This calculation Tw is possible, but its results should be treated with caution, i.e., it is
possible to predict the value of δ on the basis of experimental data, as well as the values
of λ on the basis of analysis of the composition and characteristics of the sediments.
Apparently, this approach can only serve to estimates, and almost the same has to be
based on an experiment or industrial experience.

## 7.10 Unstable boiling modes

### 7.10.1 Types of instabilities

1. Unstable pool boiling occurs in the process of surface cooling in a large volume of fluid,
which may be followed by a transition from the liquid-phase convection to the nucleate boiling
regime and again to the convection. The nucleate boiling can be replaced by the film
boiling and return to the nucleate boiling regime. All of these transitions at a constant heat
flux lead to unstable regimes—temperature fluctuations/oscillations at the cooled surface,
which adversely affect the structural integrity.
2. Instability of boiling in a single channel has a different (thermohydraulic or thermal fluid
dynamic) nature. If boiling occurs in a separate part of the channel, its pressure drop is
changed. As a result it may cause a change of flow rate. Under the certain circumstances
fluctuations in flow rate and pressure can be the periodic (pulsating mode).
To avoid the unstable regimes under operation of the steam generating channel, its
hydraulic characteristic should be known. The latter reflects the dependence of the total pressure
drop in the channel on a flow rate (or a mass flux) at the steady-state regime:
Δp = f G
ð Þ = f ρw
ð
Þ.
For stable operation of the channel, it is necessary that this characteristic was unambiguous
(Fig. 7.63). The characteristics, which shows the same value of pressure drop associated
with the different flow rate in a certain range of Δp, is considered as unstable (Habensky
and Gerliga, 1994). Furthermore, it is necessary to know the enthalpy distribution along a
channel length. The pulsations of the flow rate occur when the ratio Δhec/Δh is below
ΔP
rw
Fig. 7.63 Typical hydraulic characteristics. 1—single-valued, stable; 2—multiple-valued,
unstable: l—points of extremum.

<!-- page 476 (PDF 120) -->
the certain value (here Δhec is the enthalpy growth within the economizer section; Δh is the
total increase in enthalpy.)
3. Boiling instabilities in parallel channels. In the case of flow boiling in the separate-parallel
tubes each of which has different pressure drop characteristics and is under different heating
conditions. Assume these parallel flow channels are connected at an inlet plenum and at an
outlet plenum, i.e., share the inlet and outlet in common. In this parallel channel system, the
flow and temperature re-distributions take place showing a different enthalpy increase in
different channels. It is characterized by the ratio of the enthalpy increase in ith single tube
(Δhi) to the mean value of enthalpy for the whole tube bundle (Δ⟨h), i.e., Ki = Δhi=Δ⟨h and a
hydraulic nonuniformity factor ηi = ζi=ζB a ratio of the hydraulic resistance (drag) coefficient
of the ith channel ζi = Δpi · 2ρi
ρiwi
ð
Þ2 to that of the whole bundle ζB = Δ⟨p · 2ρ
ρw
ð
Þ2 ; ρi is the coolant
density in a tube; ρ is the mean density in the bundle. Large values of these ratios in a bundle
of parallel tubes result in unstable modes.

### 7.10.2 Unstable pool boiling

At the low reduced pressures p/pcr<2□10−3 and the good wettability of surface cavities
(centers of vapor generation) there is the significant liquid superheating as regard
to the saturation temperature. At low pressures, the critical radius of the vapor nucleus
reaches the high values (Rcr□1/ρg), boiling is appeared to be complicated, and the
natural convection is delayed. This phenomenon is also due to the decrease in the
number of vapor generation centers (Avsentuk and Kutateladze, 1977). In some cases,
a transition from the natural convection to the film boiling is possible bypassing nucleate
boiling (Fig. 7.64).
The S-shaped form of the boiling curve, when the q is the independent variable (for
example, electric heating), determines the number of vapor generation centers per the
area unit (N/A) and the surface superheating relative to the saturation temperature
(ΔT), with all other factors being equal:
ΔT
q
Zone of stable
nucleate boiling
Zone of unstable
boiling
qB
qA
Fig. 7.64 Boiling curves at different pressures (p1>p2>p3). 1—High pressures; 2, 3—low
pressures; 4—transition from natural convection to the film boiling.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 477 (PDF 121) -->
q □ N=A
ð
Þn ΔT
ð
Þm:
The values of (N/A) and (ΔT) are related to each other. So the increase in (q>qA) also
causes an increase of (N/A), which causes the ΔT decrease (curves 2, 3 in Fig. 7.64).
Usually n□0.5–0.7 and m□3.
The mechanism of the film boiling bypassing the nucleate boiling has cavitational
character—i.e., an explosive emergence of vapor bubbles is observed on the surface
and the formation of a vapor film (curve 4).

### 7.10.3 Instability of channel boiling

In a single channel the boiling instability is primarily associated with the hydrodynamic
instability, especially in circuits with natural circulation. Despite to the constant
power applied to the channel, the oscillations of flow rate can be observed after onset
of boiling. There are the following explanations of the reasons for this phenomenon.
Let us suppose that as a result of some disturbance, the flow rate through the channel
will increase slightly. This causes at all factors to be equal the decrease of vapor generation
, which will reduce the value of lifting force and as well as the flow rate. However
, the flow rate decrease will cause an increase in quality and lifting forces,
therefore it should be resulted in further increase of flow rate. The sequence of each
process will take place with some delay and causes the flow rate pulsation. If the ratio
of two successive amplitudes D=A1/A2<1, then damping of oscillations is occurred,
at D>1 pulsation gain will be observed.
All these processes have to a large extent by nonlinear relationships. Since the
hydraulic resistance is a nonlinear function of water and vapor velocities, and, moreover
, the nonlinear function of void fraction, which, in its turn, depends on the applied
power and flow rate.
The hydrodynamic characteristic of a single steam generating pipe with the certain
diameter and length is described by function Δp=f(ρw). Here Δp is the full hydraulic
resistance of channel, which consists of two components: Δp1 is the resistance of the
economizer
section;
Δp2
is
the
resistance
of
the
evaporator
section
and
Δp=Δp1+Δp2.
Δp1 = ξl1
d
ρw
ð
Þ2
2ρf
; Δp2 = ξl−l1
d
ρw
ð
Þ2
2ρf
1 + ⟨x ρf =ρg −1
□
□
h
i
ψ:
(7.181)
The thermal balance equation for the economizer and the evaporation sections is as
follows:
πdl1⟨q = πd2
4 ρw hf,sat −hin
□
□
;
πd l−l1
ð
Þ⟨q = πd2
4 ρw hout −hf,sat
□
□
;
