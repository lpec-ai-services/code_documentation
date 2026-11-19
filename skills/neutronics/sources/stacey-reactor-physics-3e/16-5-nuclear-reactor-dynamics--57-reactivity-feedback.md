# 5 Nuclear Reactor Dynamics — 5.7 Reactivity Feedback … 5.9 Reactor Stability
<!-- source PDF pages 184-202 -->

<!-- page 160 (PDF 184) -->
from t1 = 0,
P(t1; t2)dt1dt2 =
ε v2
p − vp

v2
p
k2
p
2(1 − kp)l eαtdt
(5.73)
This is the Q exp(αt)dt term in Eq. (5.68), so
Q =
ε v2
p − vp

v2
p
k2
p
2(1 − kp)l
(5.74)
In a Rossi-α experiment, the function P(t) of Eq. (5.68) is measured by a time
analyzer and the random count rate Cdt is subtracted. The parameter α is then
determined from the remaining Q exp(αt)dt term.

## 5.7 Reactivity Feedback

Up to this point, we have discussed neutron kinetics – the response of the neutron
population in a nuclear reactor or other fission chain-reacting system to an
external reactivity input – under the implicit assumption that the level of the
neutron population does not affect the properties of the system that determine
the neutron kinetics, most notably the reactivity. This is the situation when the
neutron population is sufficiently small that the fission heat does not affect the
temperature of the system (i.e., at zero power). However, in an operating nuclear
reactor the neutron population is large enough that any change in fission heating
resulting from a change in neutron population will produce changes in temperature
, which, in turn, will produce changes in reactivity, or reactivity feedback. The
combined and coupled response of the neutron population and of the temperatures
, densities, and displacements of the various materials in a nuclear reactor is
properly the subject of reactor dynamics, but the term is commonly used to also
include neutron kinetics.
When the neutron population increases, the fission heating increases. Since
this heating is deposited in the fuel element, the fuel temperature will increase
immediately. An increase in fuel temperature will broaden the effective resonance
absorption (and fission) cross section, generally resulting in an increase in
neutron absorption and a corresponding reduction in reactivity – the Doppler
effect. The fuel element will also expand and, depending on the constraints, bend
or bow slightly, thus changing the local fuel–moderator geometry and flux
disadvantage factor (the ratio of the flux in the fuel to the flux in the moderator),
thereby producing a change in reactivity. If the increase in fission heating is large
enough to raise the fuel temperature above the melting point, fuel slumping will
occur, resulting in a large change in the local fuel–moderator geometry and a
corresponding change in flux disadvantage factor and fuel absorption, producing
a further change in reactivity.

<!-- page 161 (PDF 185) -->
Some of the increased fission heat will be transported out of the fuel element
(time constant of tenths of seconds to seconds) into the surrounding moderator/
coolant and structure, causing a delayed increase in moderator/coolant and
structure temperature. An increase in moderator/coolant temperature will produce
a decrease in moderator/coolant density, which causes a change in the local
fuel–moderator properties and a corresponding change in both the moderator
absorption and the flux disadvantage factor. In addition, a decrease in moderator
density will reduce the moderating effectiveness and produce a hardening (shift to
higher energies) in the neutron energy distribution, which will change the
effective energy-averaged absorption cross sections for the fuel, control elements,
and so on. An increase in structure temperature will cause expansion and
deformation, producing a change in the local geometry that will further affect
the flux disadvantage factor. These various moderator/coolant changes all
produce changes in reactivity.
The reduction in moderator/coolant density increases the diffusion of
neutrons, and the increase in temperature causes an expansion of the reactor.
The effect of increased diffusion is to increase the leakage, and the effect of
increased size is to reduce the leakage, producing offsetting negative and
positive reactivity effects. In addition to these internal (to the core) reactivity
feedback effects, there are external feedback effects caused by changes in the
coolant outlet temperature that will produce changes in the coolant inlet
temperature.

### Temperature Coefficients of Reactivity

The temperature coefficient of reactivity is defined as
αT ≡ @ρ
@T = @
@T
k − 1
k

= 1
k2
@k
@T ' 1
k
@k
@T
(5.75)
To gain physical insight into the various physical phenomena that contribute to
the reactivity feedback, we first use the one-speed diffusion theory expression for
the effective multiplication constant for a bare reactor, but extend it to account
for fast fission by including the ratio ε = total fission/thermal fission, to account
for the resonance absorption of neutrons during the slowing down to thermal
energies by including the resonance escape probability p, and to account for the
leakage of fast as well as thermal neutrons by replacing the diffusion length with
the migration length M:
k = k1PNL =
vP
f
P
a
1 + L2B2 =
vP
f
PF
a
PF
a
P
a
(1 + L2B2)
= ηf PNL ! ηf εpPNL
(5.76)

<!-- page 162 (PDF 186) -->
which allows us to write
αT = 1
η
@η
@T + 1
ε
@ε
@T + 1
f
@f
@T + 1
p
@p
@T + 1
PNL
@PNL
@T
(5.77)
This formalism lends itself to physical interpretation and can provide quantitative
estimates of reactivity coefficients for thermal reactors, but it is not directly
applicable to fast reactors. We discuss fast reactor reactivity coefficients in the
next section, where a perturbation theory formalism that is more appropriate for
the quantitative evaluation of reactivity coefficients in both fast and thermal
reactors is introduced. We now discuss reactivity feedback effects on p, f, and PNL;
there are also smaller reactivity effects associated with η due to shifts in the
thermal neutron energy distribution and associated with ε, which latter are similar
to the effects associated with the thermal utilization factor.

### Doppler Effect

The resonance capture cross section (one-level Breit–Wigner) is
σγ = σ0
ffiffiffiffiffi
E0
E
r
Γγ
Γ ψ(x; ξ)
(5.78)
where ψ is the Doppler broadening shape function, which takes into account the
averaging of the neutron–nucleus interaction cross section over the thermal
motion of the nucleus,
ψ(x; ξ) =
ξffiffiffiffiffi
4π
p
∫
−1
e−[(x−y)2ξ2=4]
dy
1 + y2
(5.79)
σ0 is the peak resonance cross section, Γγ and Γ are the capture and total widths of
the resonance, x = (E − E0)/Γ, ξ = Γ/(4E0kT/A)1/2, E and E0 are the energies of the
neutron and of the resonance peak, and A is the mass of the nucleus in amu. The
total capture in the resonance is given by the resonance integral
Iγ ≡ ∫σγ(E)ϕ(E)dE
(5.80)
The function ψ broadens with increasing temperature, T, characterizing the
motion of the nucleus. A broadening of the ψ function reduces the energy selfshielding
in the resonance and increases the resonance integral. Thus, an increase
in fuel temperature due to an increase in fission heating will cause an increase in
the effective capture cross section hσγi ∼Iγ. A similar result is found for the fission
resonances.
In thermal reactors, the Doppler effect is due primarily to epithermal capture
resonances in the nonfissionable fuel isotopes (232Th, 238U, 240Pu) and can be

<!-- page 163 (PDF 187) -->
estimated by considering the change in resonance escape probability
p = e−(NFIγ=ξΣp)
(5.81)
where ξ Σp=NF is the average moderating power per fuel atom, with a sum over
resonance integrals for all fuel resonances implied; the function
J(ξ; β´) ≡ ∫
ψ(x; ξ)
ψ(x; ξ) + β´ dx
(5.82)
is tabulated in Table 4.3, and β´ = (Σp/NF)(Γ/σ0Γγ). Note here the double usage
of the symbol ξ. The resonance parameter definition following Eq. (5.79) is
used in Eqs. (5.78), (5.79), and (5.82), but the scattering definition of Eq. (1.24)
is used in Eq. (5.81).
The Doppler temperature coefficient of reactivity for a thermal reactor can
then be calculated as
αD
TF = @ρ
@TF
' 1
k
@k
@TF
= 1
p
@p
@TF
= ln p 1
I
@I
@TF

(5.83)
Since the additional fission heating is deposited in the fuel, the fuel temperature,
TF, increases immediately, and the Doppler effect immediately reduces the
reactivity. The Doppler effect is a very strong contributor to the safety and
operational stability of thermal reactors.
There are useful fits to the total resonance integrals for 238UO2 and 232ThO2:
I(300 K) = 11:6 + 22:8
SF
MF

I(TF) = I(300 K) 1 + β´´
ffiffiffiffiffiffiffiffiffiffi
T(K)
p
−
ffiffiffiffiffiffiffi
p

h
i
238U O2 : β´´ = 61 □ 10−4 + 47 □ 10−4
SF
MF

232ThO2 : β´´ = 97 □ 10−4 + 120 □ 10−4
SF
MF

(5.84)
where SF and MF are surface area and mass of the fuel element. Using this fit,
Eq. (5.83) becomes
αD
TF = −ln
p(300 K)

β´´
ffiffiffiffiffiffiffiffiffiffiffiffi
TF(K)
p
(5.85)

<!-- page 164 (PDF 188) -->
### Fuel and Moderator Expansion Effect on Resonance Escape Probability

When the fuel temperature increases, the fuel will expand, causing among
other things a decrease in the fuel density, which affects the resonance
escape probability and contributes an immediate temperature coefficient of
reactivity:
αp
TF = 1
p
@p
@NF
@Nf
@TF
= ln p
NF
@NF
@TF

= −3θF ln p
(5.86)
where (dN/dT)/N = −3(dl/dT)/l = −3θ, with θ being the linear coefficient of
expansion of the material. Since the fuel density decreases upon expansion,
the resonance absorption decreases, and this reactivity coefficient contribution is
positive (note that since p < 1, ln p < 0).
After the increase in fission heating has been transported out of the fuel
element into the coolant/moderator, the moderator temperature, TM, will
increase, which causes the moderator to expand and contributes a delayed
temperature coefficient of reactivity:
αp
TM = 1
p
@p
@NM
@NM
@TM
= −ln p
NM
@NM
@TM

= 3θM ln p
(5.87)
The decreased moderator density reduces the moderating power, reducing the
probability that the neutrons will be scattered to energies beneath the resonance,
hence increasing the resonance absorption and contributing a negative reactivity
coefficient.

### Example 5.5 Resonance Escape Probability Fuel Temperature Coefficient for UO2

The prompt feedback resulting immediately from an increase in power
is associated with the increase in fuel temperature, the most significant part of
which is due to the change in the resonance escape probability due to the Doppler
broadening of resonances, as given by Eq. (5.85), and due to the fuel expansion, as
given by Eq. (5.86). For a UO2 reactor consisting of assemblies of 1-cm-diameter
fuel pins of height H in a water lattice with Σp/NF = 100 and fuel density ρ =
10 g/cm3, SF/MF = πdH/π(d/2)2Hρ = 0.4, I(300 K) = 11.6 + 22.8 × 0.4 = 20.72, and
β´´ = 61 + 47(SF/MF) × 10−4 = 79.8 × 10−4. The resonance escape probability at
300 K
is
p = exp(−NF
I/ξΣp) = exp[−20.72/(100 × 0.948)] = 0.8036,
and
ln
(p) = −0.2186. The Doppler temperature coefficient of reactivity at 300 K is
αD
TF = ln(p)β´´/2T1/2 = (−0.2186)(79.8 × 10−4)/(2)(17.32) = −5.036× 10−5Δk/k. The
linear thermal expansion coefficient for UO2 is θF= 1.75× 10−5K−1, and the fuel
expansion contribution to the resonance escape probability temperature coefficient of
reactivity is αp
TF = −3θFln(p)= −3(1.75× 10−5)□(−0.2186) = 1.148× 10−5Δk/k. Thus,
the total prompt fuel temperature coefficient of reactivity due to the resonance escape
probability is αD
TF + αp
TF = −3.888× 10−5Δk/k.

<!-- page 165 (PDF 189) -->
### Thermal Utilization

The thermal utilization can be written simply in terms of the effective cellaveraged
fuel and moderator absorption cross sections discussed in Section 3.8:
f =
Peff
aF
Peff
aF + Peff
aM
!
PF
a
PF
a + PM
a
(5.88)
Recalling that Σ ≡ Nσ, the reactivity coefficient associated with the thermal utilization
has an immediate negative component associated with the fuel temperature
increase and a delayed positive contribution associated with the moderator density
decrease:
f
@f
@T = (1 − f )
σF
a
@σF
a
@TF
+ 1
PF
a
@ PF
a
@ξ
@ξ
@TF
+ 1
NF
@NF
@TF
!
"
−
σM
a
@σM
a
@TM
+
PM
a
@ PM
a
@ξ
@ξ
@TM
+ 1
NM
@NM
@TM
!#
' −(1 − f )
2TF
− 1
PF
a
@ PF
a
@ξ
@ξ
@TF
+ 3θF
!
"
− −
PM
a
@ PM
a
@ξ
@ξ
@TM
+ 3θM
!#
≡ α f
TF + α f
TM
(5.89)
Account has been taken in writing Eq. (5.89) of the fact that the thermal
disadvantage factor, ξ, which is used in the definition of effective homogenized
fuel and moderator cross sections, will also be affected by a change in temperature.
An increase in fuel temperature hardens (makes more energetic) the thermal
neutron energy distribution, which reduces the spectrumaverageof the 1/vthermal
fuel cross section and thus reduces the thermal utilization. An increase in the fuel
temperature also reduces the fuel density, further reducing the thermal utilization.
An increase in moderator temperature has little effect on the moderator cross
section but reduces the moderator density, which increases the thermal utilization.

### Nonleakage Probability

The nonleakage probability can be represented by
PNL '
1 + M2B2
g
(5.90)

<!-- page 166 (PDF 190) -->
Temperature increases can affect the nonleakage probability by changing the characteristic
neutron migration length, or the mean distance that a neutron is
displaced before absorption, and by changing the size of the reactor. Assuming
that both of these effects are associated primarily with changes in the moderator
temperature, we write
PNL
@PNL
@TM
= −
M2B2
g
1 + M2B2
g
M2
@M2
@TM
+ 1
B2
g
@B2
g
@TM
!
(5.91)
An increase in moderator temperature causes a decrease in moderator density,
which affects the migration area as
M2
@M2
@TM
= 1
DM
@DM
@TM
− 1 − f
)
ΣM
a
@ ΣM
a = 1 − f
)
@TM
= 6θM +
2TM
−
1 − f
@f
@TM
(5.92)
where we have used P
a = PM
a + PF
a = PM
a (1 − f ):
The geometric buckling Bg = G/lR, where G is a constant depending on geometry
(Table 3.3) and lR is a characteristic physical dimension of the reactor. Thus,
B2
g
@B2
g
@TM
=
lR
G
 2 @(G=lR)2
@TM
= −2
lR
@lR
@TM

(5.93)
and Eq. (5.91) becomes
αPNL
TM =
PNL
@PNL
@TM
=
M2B2
g
1 + M2B2
g
lR
@lR
@TM
− 6θM −
2TM
+
1 − f
@f
@TM

(5.94)
A decrease in moderator density allows neutrons to travel farther before absorption
, which increases the leakage and contributes a negative reactivity coefficient
component. Expansion of the reactor means that a neutron must travel farther to
escape, which contributes a positive reactivity coefficient component.

### Representative Thermal Reactor Reactivity Coefficients

Reactivity coefficients calculated for representative thermal reactors are given in
Table 5.2.

<!-- page 167 (PDF 191) -->
### Example 5.6 UO2 Fuel Heat Removal Time Constant

It is important to
emphasize that the temperature reactivity feedback associated with the various
mechanisms that have been discussed take place at different times. The feedback
associated with changes in the fuel temperature take place essentially instantaneously
, since an increase in fission rate produces an immediate increase in fuel
temperature. However, the increase in moderator/coolant temperature occurs
later,aftersomeoftheadditionalheatisconductedoutofthefuelelement.Theheat
balance equation in the fuel element,
ρC @T
@t

= r−1 @
@r
rκ @T
@r

+ q´´´
(5.95)
where ρ is the fuel density, κ is the heat conductivity, C is the heat capacity, and q´´´
is the volumetric fission heat source, can be used to estimate a time constant
characterizing the conduction of heat out of the fuel element to the interface with
the coolant/moderator for a fuel pin of radius a, τ ≈ ρCa2/κ.
Typical parameters for a UO2 fuel element in a thermal reactor are a = 0.5 cm,
κ = 0.024 W/cm□K, ρ = 10.0 g/cm3, and C = 220 J/kg□K. The heat conduction time
constant for heat removal from the fuel into the coolant is τ = ρCa2/κ = (10 g/cm3)
(220 J/kg□K)/(0.024 J/s□cm□K)(103 g/kg) = 22.9 s. For a smaller fuel pin characteristic
of a fast reactor with a = 0.25 cm, the UO2 fuel time constant would be about
6 s. With a metal fuel instead of UO2, the heat conductivity is much larger, and the
heat removal time constants are on the order of 0.1 to 1.0 s.

### Startup Temperature Defect

A reactor is initially started up from a cold condition by withdrawing control rods
until the reactor is slightly supercritical, thus producing an exponentially increasing
neutron population on a very long period. As the neutron population
increases, the fission heating and thus the reactor temperature increase. This
increase in temperature produces a decrease in reactivity (almost all reactors are
designed to have a negative temperature coefficient) that would cause the neutron
population to decrease and the reactor to shut down if the control rods were not
withdrawn further to maintain an increasing neutron population. The total
Table 5.2 Representative Reactivity Temperature Coefficients in Thermal Reactors
BWR
PWR
HTGR
Doppler (Δk/k × 10−6 K−1)
−4 to −1
−4 to −1
−7
Coolant void (Δk/k × 10−6/% void)
−200 to −100
–
–
Moderator (Δk/k × 10−6 K−1)
−50 to −8
−50 to −8
+1
Expansion (Δk/k × 10−6 K−1)
≈ 0
≈ 0
≈ 0
Source: Data from Ref. [2]; used with permission of Wiley.

<!-- page 168 (PDF 192) -->
amount of feedback reactivity that must be offset by control rod withdrawal
during the course of the startup to operating power level is known as the
temperature defect. The temperature defects for water-moderated reactors,
graphite-moderated reactors, and sodium-cooled fast reactors are about
Δk/k = 2–3 × 10−2, 0.7 × 10−2, and 0.5 × 10−2, respectively.

## 5.8 Perturbation Theory Evaluation of Reactivity Temperature Coefficients

### Perturbation Theory

The multigroup diffusion equations (Chapter 4) are
−∇? Dg∇ϕg + P
rgϕg =
X
G
g´≠g
X
g´!gϕg´ + 1
k χg
X
G
g´=1
v
X
f g´ϕg´
g = 1; . . . ; G
(5.96)
where Σg´!g is the cross section for scattering a neutron from group g´ to group g,
Σrg is the removal cross section for group g, which is equal to the absorption cross
section plus the cross section for scattering to all other groups, χg is the fraction of
the fission neutrons in group g, Dg and νΣfg are the diffusion coefficient and the
nu-fission cross section in group g, and ϕg is the neutron flux in group g.
We now consider a perturbation in materials properties (e.g., as would be
caused by a change in local temperature) such that the reactor is described by an
equation like Eq. (5.96), but with Dg →Dg + ΔDg, Σg →Σg + ΔΣg, where the Δ
terms include changes in densities, changes in the energy averaging of the cross
section data and energy self-shielding, changes in spatial self-shielding, and
changes in geometry. If we assume that the perturbation in materials properties
is sufficiently small that it does not significantly alter the group fluxes, we can
multiply the unperturbed and perturbed equations by ϕ+
g , subtract the two,
integrate over the volume of the reactor, and sum the resulting equations for all
groups to obtain the perturbation theory estimate for the change in reactivity
associated with the perturbation in material properties:
Δk
k
'
X
G
g=1∫dr ϕ+
g ∇? (ΔDg∇ϕg) − ϕ+
g Δ
X
rgϕg + ϕ+
g
X
G
g´≠g
Δ
X
g´!gϕg´
"
+ϕ+
g χg
X
G
g´=1
Δ(v
X
f g´)ϕg´
□
X
G
g=1∫dr
ϕ+
g χg
X
G
g´=1
v
X
f g´ϕg´
!
(5.97)

<!-- page 169 (PDF 193) -->
The quantity ϕ+
g , the importance of neutrons in group g in producing a subsequent
fission event, is discussed in Chapter 13. This expression, together with the
subsidiary calculation of the ΔΣg and ΔDg terms, including all the effects
mentioned above, provides a practical means for the quantitative evaluation of
reactivity coefficients in nuclear reactors.

### Example 5.7 Reactivity Worth of Uniform Change in Thermal Absorption Cross Section

With the assumption that all of the fission occurs in the thermal
group, the reactivity worth of a uniform change in thermal absorption cross section
in a uniform thermal reactor is Δk=k = Δ Pth
a Ith=v Pth
j Ith ≈ Δ Pth
a = Pth
a
because Ith, the integral over the reactor of the product of the thermal group
importance function and flux, appears in both the numerator and denominator,
and because in a critical reactor Pth
a ≈ v Pth
f .
We now discuss some fast reactor reactivity coefficients that could not be
treated by the more approximate method of the preceding section, although we
emphasize that this perturbation theory calculation is also used for thermal
reactor reactivity coefficient evaluation.

### Sodium Void Effect in Fast Reactors

The reactivity change that occurs when sodium is voided from a fast reactor
can be separated into leakage, absorption, and spectral components. The
leakage and spectral components correspond to the first (ΔDg) and third
(ΔΣg´!g) terms, respectively, in Eq. (5.97). The absorption component corresponds
to the second (ΔΣrg) and fourth (ΔνΣf) terms in Eq. (5.97), although the
change in fission cross section is usually small and therefore neglected, and this
component is usually referred to as the capture component. The spectral and
capture components are normally largest in the center of the core, where the
neutron flux and importance function are largest, and the leakage component
is normally largest in the outer part of the core, where the flux gradient is
largest.
The magnitude of the sodium void coefficient varies directly with the ratio
of the number of sodium atoms removed to the number of fuel atoms present.
The spectral component of the sodium void coefficient is generally positive,
is more positive for 239Pu than for 235U, and becomes increasingly positive as
fissile material concentration decreases relative to sodium content. The
capture component tends to become more positive with softer neutron
spectra because of the 2.85-keV resonance in
23Na, hence to become
more positive with increasing sodium concentration relative to fuel concentration
. The negative leakage component is generally smaller than the other
two components, although the leakage component can be enhanced by the
choice of geometrical configuration. As a result, the overall reactivity effect of
voiding the central part of the core is positive, and may be positive for voiding
of the entire core. This poses a serious safety concern that must be offset by
proper design to ensure that other negative reactivity coefficients are
dominant.

<!-- page 170 (PDF 194) -->
### Doppler Effect in Fast Reactors

In fast reactors, the neutron energy spectrum includes the resonance regions of
both the fissionable (235U, 233U, 239Pu, 241Pu) and nonfissionable (232Th, 238U,
240Pu) fuel isotopes. The Doppler effect in fast reactors is due almost entirely to
resonances below about 25 keV. An increase in fuel temperature will produce an
increase in both the fission and absorption cross sections, and the resulting
change in reactivity can be positive or negative, depending on the exact composition
. The temperature coefficient of reactivity can be estimated from
@k
@TF
= ∫NF ϕ+
f
@σf
@TF
− ϕ+(E)
@σγ
@TF
+ @σf
@TF

ϕ(E)dE
' NF∫
v
@σf
@TF
(v − 1 − α)ϕ(E)dE
(5.98)
where NF is the density of fuel nuclei (sum over species implied), and ϕ+(E) and
ϕ+
f are the importance of a neutron at energy E and of a fission neutron (i.e., the
number of fissions the neutron subsequently produces). Since in a critical
system each neutron will on average produce 1/ν fissions, ϕ+ ≈ ϕ+
f ≈ 1/ν is used
in the second form of the estimate, and α ≡ σγ/σf has also been used. Since α
generally decreases with increasing neutron energy (Chapter 2), the reactivity
change will tend to be more positive/less negative for metal-fueled cores with a
relatively hard spectrum. The oxygen in UO2 fuel softens (makes less energetic
) the energy spectrum and thereby making the reactivity change more
negative/less positive. Detailed design calculations, using methods benchmarked
against critical experiments, indicate that in larger reactors with a
high fertile-to-fissile ratio the Doppler coefficient is sufficiently negative to
provide a prompt shutdown mechanism in the event of excess fission heating
of the fuel.

### Fuel and Structure Motion in Fast Reactors

The increased fission heating coincident with an increase in the neutron population
causes the fuel to expand radially and axially and to distort (e.g., bow) due to
constraints. The expanding fuel first compresses, then ejects, sodium. The additional
fission heat is transferredto the structure, producinga delayed expansion and
distortion of the structure. The radial expansion, which is cumulative from the core
center outward, results in a general outward radial movement of the fuel and in an
expansion of the size of the reactor. The reactivity effect of this fuel and structure
motion is highly dependent on the details of the design. However, a few simple
estimates provide a sense of the magnitude of the effects.

### Example 5.8 Reactivity Effects of Fuel and Structure Expansion

Radial
motion of the fuel by an amount Δr from an initial radial location r causes a
reduction in local fuel density that varies as r2, leading to a local density change ΔNF/

<!-- page 171 (PDF 195) -->
NF≈ (r2− (r + Δr)2/r2≈ −2Δr/r. Axial fuel expansion leads to linear fuel density
decrease. The overall expansion reactivity coefficient is a combination of the negative
effect of reduced fuel density and the positive effect of increased core size, hence
reduced leakage. An overall expansion reactivity coefficient is of the form
αexp
TM =
a ΔR
R + b ΔNF
NF

radial
+
c ΔH
H + d ΔNF
NF

axial
(5.99)
where, for the example of a 1000-MWe UO2 reactor with H/D = 0.6, the constants
are (a = 0.143, b = 0.282, c = 0.131, d = 0.281).

### Fuel Bowing

Fuel distortion (e.g., bowing) is very much a function of how the fuel is constrained.
The calculated reactivity effect of inward bowing in the metal-fueled EBR-I was
Δk/k ≈ −0.35ΔV/V ≈ −0.7ΔR/R ≈ 0.0013. This predicted positive reactivity due to
bowing exceeded the combined negative reactivity from all other effects at full flow
and intermediate power, suggesting the possibility of a positive reactivity coefficient
over the intermediate power range, consistent with experimental observation.

### Representative Fast Reactor Reactivity Coefficients

Reactivity coefficients calculated for a representative fast reactor design are given
in Table 5.3.

## 5.9 Reactor Stability

### Reactor Transfer Function with Reactivity Feedback

Since the reactor power is related directly to the neutron population, we can
rewrite the neutron kinetics equations, in particular Eq. (5.39), in terms of the
power, P = Ef nvΣf□Vol, where Ef is the energy release per fission. If we expand the
Table 5.3 Reactivity Coefficients in a 1000-MWe Oxide-Fueled Fast Reactor
Temperature Δk/k × 10 −6 °C −1
Power Δk/k × 10 −6 MW −1
Sodium expansion core
+3.0
+0.085
Sodium expansion reflector
−1.6
−0.081
Doppler
−3.2
−0.628
Radial fuel pin expansion
+0.4
+0.117
Axial core expansion
−4.1
−0.181
Radial core expansion
−6.8
−0.182
Source: Data from Ref. [3]; used with permission of American Nuclear Society.

<!-- page 172 (PDF 196) -->
power about the equilibrium power P0 as P(t) = P0 + P1(t) and limit consideration
to the situation |P1/P0| ≪1, we find that
dP1(t)
dt
= 1
Λ
ρ(t)P0 + ∫
dτβD(τ)[P1(t − τ) − P1(t)]

(5.100)
Representing the reactivity as the sum of an external reactivity, ρex, such as may be
caused by control rod motion, and a feedback reactivity, ρf, caused by the inherent
reactivity feedback mechanisms discussed in the preceding two sections, the total
reactivity may be written as
ρ(t) = ρex(t) + ρf (t)
= ρex(t) + ∫
t
−1
f (t − τ)P1(τ) dτ
= ρex(t) + ∫
f (τ)P1(t − τ) dτ
(5.101)
where f(t − τ) is the feedback kernel that relates the power deviation P1 = P − P0 at
time t − τ to the resulting reactivity at time t.
UsingthelastformofEq.(5.101)inEq.(5.100),Laplacetransforming(equivalently,
assuming an est time dependence), and rearranging yields a transfer function, H(s),
relating the external reactivity input to the power deviation from equilibrium:
P1(s) =
Z(s)
1 − P0F(s)Z(s) P0ρex(s) ≡ H(s)P0ρex(s)
(5.102)
This new transfer function contains the zero-power transfer function, Z(s), which
relates the prompt and delayed neutron response to the external reactivity, and
the feedback transfer function, F(s), which relates the feedback reactivity to the
power deviation P1 = P − P0:
ρf (s) = F(s)P1(s)
(5.103)
Note that when P0 →0, H(s) →Z(s).
The linear stability of a nuclear reactor can be determined by locating the poles
of H(s) in the complex s-plane. This follows from noting that when Eq. (5.102) is
Laplace inverted, the solutions for P1(t) ∼exp(sjt), where the sj are the poles of
H(s). Any poles located in the right half of the complex s-plane (i.e., with a positive
real part) indicate a growing value of P1(t) – an instability. Since Z(s) appears in
the numerator and denominator of H(s), its poles (the roots of the inhour
equation) cancel in H(s), and the poles of H(s) are the roots of
1 − P0F(s)Z(s) = 0
(5.104)

<!-- page 173 (PDF 197) -->
We can anticipate from Eq. (5.104) that the poles of H(s), hence the linear stability
of the reactor, will depend on the equilibrium power level, P0.

### Stability Analysis for a Simple Feedback Model

To determine the roots of Eq. (5.104), we must first specify a feedback model in
order to determine the feedback transfer function, F(s). We consider a twotemperature
model in which the deviation in the fuel temperature from the
equilibrium value satisfies
dTF(t)
dt
= aP1(t) − ωFTF(t)
(5.105)
where a involves the heat capacity and density of the fuel and ωF is the inverse of
the heat transfer time constant of the fuel element (i.e., the time constant for
removal of heat from the fuel element into the coolant/moderator). The temperature
deviation about the equilibrium value in the coolant/moderator satisfies
dTM(t)
dt
= bTF(t − Δt) − ωMTM(t)
(5.106)
where b involves the mechanism governing the response of the coolant/moderator
temperature to a change in the fuel temperature, ωM is the inverse of the heat
removal time constant for the moderator, and for the sake of generality we assume
that the coolant mass flow rate is varied in response to the fuel temperature at an
earlier time (t − Δt). The same model could be applied to any two-temperature
representation of a reactor core. For example, we could consider TF to be the
temperature of a simultaneously heated fuel–coolant region and TM to represent
the temperature of the structure in a fast reactor model. Writing
ρ(t) = ρex(t) + αFTF(t) + αMTM(t) ≡ ρex(t) + ∫
t
f (t − τ)P1(τ)dτ
(5.107)
defines the feedback kernel, f(t − τ), where TF(t) and TM(t) are deviations from the
equilibrium temperatures.
Laplace transforming these three equations, using the convolution theorem,
and combining lead to identification of the feedback transfer function:
F(s) =
XF
1 + s=ωF
+
XMe−sΔt
(1 + s=ωF)(1 + s=ωM)
(5.108)
where XF = aαF/ωF and XM = (abαM/ωFωM) are the steady-state reactivity power
coefficient for the fuel and coolant/moderator, respectively. Using the zero-power
transfer function, Z(s), of Eq. (5.46), but in the one-delayed neutron group
approximation, and the feedback transfer function, F(s), of Eq. (5.108),

<!-- page 174 (PDF 198) -->
Eq. (5.104) for the poles of the reactor transfer function with feedback, H(s),
becomes
1 −
P0
s[Λ + β=(s + λ)]
XF
1 + s=ωF
+
XMe−sΔt
(1 + s=ωF)(1 + s=ωM)

= 0
(5.109)
There are a number of powerful mathematical techniques from the field of linear
control theory (Nyquist diagrams, root-locus plots, Routh–Hurwitz criterion,
iterative root finding methods, etc.) for finding the roots of Eq. (5.109), or of the
more complex equations that would result from more detailed reactivity feedback
models. Some simplification results from limiting attention to growth rates that
are small compared with the inverse neutron generation time (s ≪Λ−1), allowing
neglect of the Λ term. We now consider two additional approximations that allow
us to obtain valuable physical insights.
If we set XM ∼αM = 0 (i.e., neglect the coolant/moderator feedback), Eq. (5.109)
can be solved analytically to obtain
s− = 1
2 ωF
P0XF
β
− 1

1 −
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 + 4(P0XF=β)(λ=ωF)
(P0XF=β − 1)2
s
"
(5.110)
If the fuel power coefficient is positive (XF ∼αF > 0), the term under the radical
is positive and greater than unity, both roots are real, and one root is positive,
indicating an instability. If the fuel power coefficient is negative (XF ∼αF < 0), the
real parts of both roots are negative, indicating stability.

### Threshold Power Level for Reactor Stability

If we retain XM finite but restrict our consideration to instabilities with growth
rates much less than the inverse fuel heat removal time constant, s ≪ωF, and set
the time delay to zero, Δt = 0, we can again solve Eq. (5.109) analytically for the
poles of the reactor transfer function, H(s):
s− = − 1
2 ωM
1 − P0XF
β
XM
XF
+ 1 + λ
ωM

1 − P0XF
β
□
1 −
1 +
λ
ωM

 P0XF
β

1 − P0XF
β

1 − P0XF
β
XM
XF
+ 1 +
λ
ωM

>
>
>
<
>
>
>
:
>
>
>
=
>
>
>
;
1=2
(5.111)
This expression reveals the existence of a threshold equilibrium power level, P0,
above which a reactor becomes unstable. As P0 →0, the two roots approach 0 and

<!-- page 175 (PDF 199) -->
−ωM, a marginally stable condition, and do not depend on the reactivity power
coefficients XM and XF. As P0 increases, the nature of the solution depends on XM
and XF. Suppose that the fuel power coefficient is positive, XF > 0, and the
moderator power coefficient is negative, XM < 0; this situation might arise, for
example, in a fast reactor when XF represents the combined Doppler, fuel
expansion, and sodium void coefficients of the fuel–coolant mixture and XM
represents the structure expansion coefficient. Taking XF=XM = − 1
2 and ωM = 1
4,
the roots of Eq. (5.111) are plotted as a function of |XM|P0/β (denoted at P0) in
Fig. 5.4. As P0 increases from zero, the marginally stable (s = 0) root moves into
the left-half complex s-plane and the (s = −ωM) root becomes less negative,
indicating that the reactor would be stable. At |XM|P0/β = 0.0962, the roots
become complex conjugates with a real part that increases with P0. At
jXMjP0=β > 2
3, the real part of the two roots becomes positive, indicating that
the reactor would become unstable above a certain threshold operating power
level. At |XM|P0/β > 1.664, the roots become real and positive, with one increasing
and the other decreasing with increasing P0, continuing to indicate instability.
The total power coefficient at steady state is negative (F(0) = XF + XM < 0), but
the reactor in this example was unstable above a certain threshold power level.
The positive fuel power feedback was instantaneous because the fuel temperature
increases instantaneously in response to an increase in fission heating. However,
the coolant/moderator temperature does not increase instantaneously because of
moderator heat removal, but increases on a timescale governed by the moderator
heat removal time constant ω−1
M following a change in fuel temperature, as may be
seen by solving Eq. (5.106) for a step increase ΔTF at t = 0:
ΔTM =
0;
t < Δt
bΔTF
ωM
(1 − e−ωM(t+Δt))
t □ Δt
>
<
>
:
(5.112)
Im (s)
P0 = 0
P0 = 0
P0 =
P0 = 1.664
Re (s)
P0 = 0.0962
P0 =
Fig. 5.4 Characteristic roots s+ and s− of Eq. (5.111) as a function of critical power level P0
(|XM|P0/β) (XF > 0, XF=XM = − 1
2, WM = 1
4 s). (With permission from Ref. [4]. Copyright 1970, Van
Nostrand.)

<!-- page 176 (PDF 200) -->
The delay of the moderator temperature response to an increase in the temperature
of the fuel was neglected; its inclusion would contribute further to the
possibility of instabilities. It is clear that heat removal time constants play an
important role in the stability of a reactor.
The two-temperature feedback model can be generalized to investigate the
stability of a variety of different feedback models that can be characterized by a
fast (f)- and a slow (s)-responding temperature. For a fast temperature response
that was either prompt (ωf = 0) or zero (Xf = 0) plus a slow temperature response
with a finite time constant (ωs ≠0) determined either by heat conduction or heat
convection, the results are given in Table 5.4.

### More General Stability Conditions

A necessary condition for stability is
F(0) = ∫
f (t)dt < 0
(5.113)
However, this is not a sufficient condition, as the analysis above, in which
F(0) = XF + XM < 0, demonstrates. The result discussed in the preceding example
suggests a useful generalization – a reactor is on the verge of becoming unstable
when the transfer function, H(s), has a pole with purely imaginary s [i.e., when
Eq. (5.104) has a purely imaginary root s = iω]. Except for values of ω for which
Table 5.4 Instability Conditions for Some Simple Two-Temperature Feedback Models
Reactivity Coefficients
Fast (ωf = 0)
Slow (ωs ≠0)
Heat Removal
F(s)
Instability
Xf = 0
Xs < 0
Conduction
Xs
1 + s=ωs
None
Xf = 0
Xs < 0
Convection
Xse−s=ωs
P0 > Pthresh
Xf > 0
Xs < 0
Conduction
Xf +
Xs
1 + s=ωs
P0 > Pthresh
Xf < 0
Xs < 0
Conduction
Xf +
Xs
1 + s=ωs
None
Xf > 0
Xs < 0
Convection
Xf + Xse−s=ωs
P0 > Pthresh
Xf < 0
Xs < 0
Convection
Xf + Xse−s=ωs
P0 > Pthresh
Xf = 0
Xs1 < 0
Convection X
Xs1e−s=ωs1 +
Xs2
1 + s=ωs2
P0 > Pthresh
Xs2 < or > 0
Conduction
Source: Data from Ref. [3]; used with permission of American Nuclear Society.

<!-- page 177 (PDF 201) -->
Z(iω) = 0, Eq. (5.104), which determines the poles of the transfer function, can be
rewritten in the case s = iω:
G(iω) =
Z(iω) − P0F(iω) = iωΛ +
X
j=1
βjiω
iω + λj
− P0F(iω) = 0
(5.114)
If this equation has a solution, it corresponds to a condition for which the reactor
is on the verge of instability. A necessary condition for a solution is that Z−1(iω)
and F(iω) have the same ratio of real to imaginary parts (i.e., the same phase). If
Z−1(iω) and F(iω) do have the same phase at some ω = ωres, there will be some
value of P0 for which Eq. (5.114) has a solution. If this value of P0 is physically
reasonable (P0 □ 0), there is instability onset at this (P0, ωres) condition. The real
and imaginary parts of 1/Z(iω) are
Re
Z(iω)

=
X
j=1
ω2βj
ω2 + λ2
j
Im
Z(iω)

= ωΛ +
X
j=1
ωβjλj
ω2 + λ2
j
(5.115)
which are both real and positive, thus are in the upper right quadrant of the
complex plane. Therefore, a necessary condition for G(iω) = 0 to have a solution is
that the real and imaginary parts of the feedback transfer function, F(iω), also lie
in the same quadrant (i.e., both be real and positive). Hence, a necessary condition
for an instability is
RefF(iω)g > 0 and lmfF(iω)g > 0
(5.116)
We now consider the example above with the simple feedback model of
Eqs. (5.105)–(5.108), but with the delay term Δt = 0. The qualitative behavior
of the real and imaginary parts of F(iω) of Eq. (5.108) is plotted in Fig. 5.5 for three
different cases, all of which have a negative moderator power coefficient, XM < 0.
Case (a) corresponds to no reactivity feedback from the fuel (XF = 0); the
instability criterion of Eq. (5.116) is satisfied for ω > (ωMωF)1/2, even though
the steady-state power coefficient X(0) = XM < 0. For case (b), with a sufficiently
large negative value of the fuel power coefficient, XF < 0, the criterion of
Eq. (5.116) is never satisfied and the reactor is stable. In case (c), the fuel reactivity
power coefficient is positive but smaller in magnitude than the negative moderator
reactivity power coefficient, |XM| > |XF | > 0, which is the situation leading to
the solution of Eq. (5.111); the reactor can become unstable, as found above from
examination of the roots given by Eq. (5.111).
A sufficient condition for unconditional stability (i.e., no power threshold) has
been shown to be
RefF(iω)g = ∫
f (t) cos (ωt)dt ≤ 0
(5.117)

<!-- page 178 (PDF 202) -->
which is a requirement that the phase angle of the feedback transfer function,
−F(s), along the iω-axis is between −90° < ϕ < +90°; thus, the feedback response
is negative and less than 90° out of phase with the power change that produced it.
This phase constraint places constraints on the time delays. This sufficient
criterion for stability has been found to be over-restrictive, however.
The unconditional stability sufficient condition of Eq. (5.117) has been used to
determine unconditional stability criteria for a variety of feedback models that can
be characterized by a fast (f) and a slow (s) responding temperature. The fast
temperature response was either prompt (ωf = 0) or determined by heat conduction
, and the slow temperature response was with a finite time constant (ωs ≠0)
determined by either heat conduction or heat convection. The results are given in
Table 5.5.

### Power Coefficients and Feedback Delay Time Constants

It is clear from the previous discussion that the reactivity temperature coefficients
actually enter the analysis as reactor power coefficients, associated with which
there are time delays related to heat transfer and removal time constants, and that
the results of the analysis are dependent on the delay times as well as on the
temperature coefficients. We can generalize the two-temperature model to define
a general reactor power coefficient:
X(t) =
X
j
@ρ
@Tj
@Tj(t)
@P
+ @ρ
@T´
j
@T´
j(t)
@P
!
(5.118)
Fig. 5.5 Plot of R = Re{F(iω)} + iI{F(iω)} of Eq. (5.108) with Δt = 0: case (a) XF = 0, XM < 0; case
(b) XF < 0, XM < 0; case (c) |XM | > XF > 0, XM < 0. (With permission from Ref. [4]. Copyright
1970, Van Nostrand.)
