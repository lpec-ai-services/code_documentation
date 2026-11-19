# 5 Nuclear Reactor Dynamics — 5.10 Measurement of Reactor Transfer Functions … Further Reading
<!-- source PDF pages 203-220 -->

<!-- page 179 (PDF 203) -->
where @ρ/@Tj are the reactivity temperature coefficients corresponding to a
change in local temperature Tj. The quantities @ρ/@Tj´ are reactivity temperature
gradient coefficients denoting the change in reactivity due to a change in
temperature gradient (e.g., as would produce bowing of a fuel element). These
reactivity coefficients can be calculated as discussed in the two preceding sections.
The quantities @Tj/@P and @Tj´/@P are the time-dependent changes in local
temperature and temperature gradients resulting from a change in reactor power
and must be calculated from models of the distributed temperature response to a
change in reactor power.
The time constants that determine the time delays in the various local temperature
responses to a power increase depend on the specific reactor design. Some
simpleestimatessufficetoestablishordersofmagnitude.The timeconstantforheat
transfer out of a fuel pin of radius r or plate of thickness r, density ρ, heat capacity
C, andthermalconductivity κ isτf = ρCr2/κ,whichgenerallyvariesfrom a fewtenths
to a few tens of seconds. The effect of cladding and the surface film drop is to
increase the time constant for the fuel element. The lumped time constant for the
coolant temperature is τc = Cc/h + (Z/2v)(1 + Cf/Cc), where Cc and Cf are the
heat capacities per unit length of the coolant and fuel, respectively, h is the heat
transfer coefficient between fuel and coolant, Z is the core height, and v is the
coolant flow speed. Typical values of τc vary from a few tenths to a few seconds.

## 5.10 Measurement of Reactor Transfer Functions

Measurement of the reactor transfer function provides useful information about a
reactor. A measurement at low power can identify incipient instabilities that
produce peaks in the transfer function. Provided that the feedback mechanisms
do not change abruptly with power, the low-power transfer function measurements
can identify conditions that would be hazardous at high power, thus
Table 5.5 Sufficient Conditions for Unconditional Stability of Two-Temperature Feedback
Models
Reactivity Coefficients
F(iω)
Stability Criterion
Coupled prompt Xf,
conduction Xs
Xf +
Xs
1 + iω=ωs
Xf ≤ 0 and Xf + Xs < 0
Uncoupled conduction
Xf and Xs
Xf
1 + iω=ωf
+
Xs
1 + iω=ωs
Xf + Xs ≤ 0, Xfωf + Xsωs < 0,
and Xfω2
f + Xsω2
s ≤ 0
Coupled conduction
Xf and Xs
Xf
1 + iω=ωf
+
Xs
(1 + iω=ωf )(1 + iω=ωs)
Xf < 0, Xf + Xs ≤ 0, and
Xfωf − Xsωs ≤ 0
Coupled prompt Xf,
convection Xs
Xf + Xse−iω/ωs
Xf < 0 and −Xf □ |Xs|
Coupled conduction
Xf, convection Xs
Xf
1 + iω=ωf
+ Xse−iω=ωs
1 + iω=ωs
Never unconditionally stable

<!-- page 180 (PDF 204) -->
allowing for their correction. Information about the feedback mechanisms can be
extracted from measurement of the amplitude and phase of the transfer function.
Any component malfunction that altered the heat removal characteristics of the
reactor would affect the transfer function, so periodic transfer function measurements
provide a means to monitor for component malfunction.

### Rod Oscillator Method

The sinusoidal oscillation of a control rod over a range of frequencies can be
used to measure the transfer function, as described in Section 5.6. The results
of Eqs. (5.60)–(5.64) apply to a reactor with feedback when n0Z(iω) is replaced
by P0H(iω). There are some practical problems in measuring the transfer
function with rod oscillation. There will be noise in the detector response,
which will require a sufficiently large reactivity oscillation for the detector
response to be separable from the noise, and nonlinear effects [i.e., the term
ρn1 that was neglected in Eq. (5.42)] may invalidate the interpretation.
Furthermore, the oscillation will not be perfectly sinusoidal, and it will be
necessary to Fourier analyze the detector response to isolate the fundamental
sinusoidal component.

### Correlation Methods

It is possible to measure the reactor transfer function with a nonperiodic rod
oscillation. Consider the inverse Laplace transform of Eq. (5.102):
P1(t) = ∫
t
−1
ρex(τ)h(t − τ)dτ = ∫
ρex(t − τ)h(τ)dτ
(5.119)
which relates the relative power variation from equilibrium [P1/P0 = (P − P0)/P0]
to the time history of the external reactivity – the rod oscillation in this case –
including the effect of feedback. The kernel h(t) is the inverse Laplace transform
of the transfer function, H(s). The cross correlation between the external
reactivity and the power variation is defined as
ϕρP ≡ 1
2T ∫
T
−T
ρex(t)P1(t + τ)dt = 1
2T ∫
T
−T
ρex(t − τ)P1(t)dt
(5.120)
where T is the period if ρex and P1 are periodic and T goes to infinity if not.
Using Eq. (5.119) in Eq. (5.120) yields
ϕρP = 1
2T ∫
T
−T
ρex(t − τ) ∫
ρex t − t´
)h t´
( )dt´

dt
= ∫
h(t´)
2T ∫
T
−T
ρex(t − τ)ρex(t − t´)dt

dt´
≡ ∫
h(t´)ϕρρ(τ − t´)dt´
(5.121)

<!-- page 181 (PDF 205) -->
where ϕρρ is the reactivity autocorrelation function. Taking the Fourier transform
of Eq. (5.121) yields an expression for the transfer function
H(−iω) = □ Ffϕρ P(τ)g
Ffϕρρ(τ)g
(5.122)
where the transforms
FfϕρP(τ)g ≡ ∫
−1
eiωτϕρρ(τ)dτ
Ffϕρρ(τ)g ≡ ∫
−1
eiωτϕρρ(τ)dτ
(5.123)
are known as the cross spectral density and the input or reactivity spectral density,
respectively.
If the control rod (or other neutron absorber) position is varied randomly over
a narrow range and a neutron detector response is recorded, the reactivity
autocorrelation function, ϕρρ, and the reactivity power cross correlation function,
ϕρP, can be constructed by numerically evaluating the defining integrals over a
period of about 5 min using a series of delay intervals, τ, increasing in discrete
steps of about Δτ = 0.01 s. The cross spectral density and reactivity spectral
density can then be calculated by numerically evaluating the defining Fourier
transform; for example,
FfϕρP(τ)g '
X
n
ϕρP(nΔτ)(cosnωΔτ + i sin nωΔτ)Δτ
(5.124)
where n varies from a large negative integer to a large positive integer. There are
sophisticated fast Fourier transform methods that are used in practice for
evaluation of the cross and reactivity spectral densities.
Experimentally, it is convenient to use a reactivity variation that changes from
positive to negative at definite times, so that the reactivity autocorrelation function
is nearly a delta function. For such a pseudorandom binary reactivity variation,
ϕρρ(τ − t´) ' const δ(t − t´)
(5.125)
In this case, it follows from Eq. (5.121) that
ϕρP(τ)
' const h(τ)
FfϕρP(τ)g ' const H(−iω)
(5.126)
and that the amplitude and phase of the transfer function can be extracted from
the computation of only the cross correlation function. By repeating the Fourier

<!-- page 182 (PDF 206) -->
transforms of Eq. (5.123) for different values of ω, the frequency dependence of
H(−iω) can be determined.

### Reactor Noise Method

Minor and essentially random variations in temperature and density within a
nuclear reactor, such as bubble formation in boiling water reactors, produce small
and essentially random reactivity variations. Autocorrelation of the response of a
neutron detector, which is proportional to the reactor neutron population or
power, provides a means of determining the amplitude of the reactor transfer
function from this noise. Writing the power autocorrelation function
ϕPP(τ) ≡ 1
2T ∫
T
−T
P1(t)P1(t + τ)dt
(5.127)
and using Eq. (5.119) yields
ϕPP(τ) = 1
2T ∫
T
−T
dt∫
h t´
( )ρex t − t´
)dt´
∫
h t´´
( )ρex(t + τ − t´´)dt´´
= ∫
h t´
( )∫
h t´´
( )
2T ∫
T
−T
ρex t − t´
)ρex t + τ − t´´
)dt

dt´dt´´
= ∫
h t´
( )dt´
∫
h t´´
( )[ϕρρ(τ + t´ − t´´)]dt´´
(5.128)
Fourier transformation then gives
H(−iω)H(iω) = jH(iω)j
2 = FfϕPP(τ)g
Ffϕρρ(τ)g ' FfϕPP(τ)g
const
(5.129)
where the fact that the autocorrelation function of a random reactivity input is a
delta function, the Fourier transform of which is a constant, has been used in
writing the final form. Thus, the amplitude, but not the phase, of the reactor
transfer function can be determined from autocorrelation of the reactor noise.
Again, the frequency dependence is determined by taking the Fourier transform
with respect to various frequencies, ω. This provides a powerful technique for
online, nonintrusive monitoring of an operating reactor for component malfunction
and incipient problems.

### Example 5.9 Reactor Transfer Function Measurement in EBR-I

The reactor
transfer function measurement on the early EBR-I sodium-cooled, metal fuel fast
reactor provides a good example of the physical insight provided by transfer

<!-- page 183 (PDF 207) -->
function measurements. The Mark II core was stable at lower power levels, but at
moderate power levels an oscillatory power was observed. The measured transfer
function is shown in Fig. 5.6: in part (a) for several values of the coolant flow rate
(gallons per minute), and in parts (b) and (c) for several values of the reactor power
level. At the lower coolant flow rates and the higher power levels there is a
(a)
(b)
(c)
1100 kW
gpm
95 gpm
1100 kw, 195 gpm
ZERO POWER
PHASE
PHASE
AMPLITUDE
AMPLITUDE
AMPLITUDE
0.01
0.01
0.1
FREQUENCY, cycles/s
-10
PHASE, (°)
-20
-30
-40
-50
0.1
kW
Fig. 5.6 Reactor transfer function EBR-1: (a) as a function of coolant flow rate; (b, c) as a function
of reactor power. (With permission from Ref. [3]. Copyright 1970, American Nuclear Society.)

<!-- page 184 (PDF 208) -->
pronounced resonance in the transfer function, suggesting an incipient instability,
which is not present at the higher flow rates and lower power levels.
The Mark II core was known to have a prompt reactivity feedback that added
reactivity with an increase in power or a decrease in coolant flow. However, when
steady state was achieved following an increase in power at constant flow, the net
change in reactivity was negative, indicating an overall asymptotic power
coefficient that was negative. Calculations indicated that the Doppler effect
was negligible, that bowing of the fuel rods toward the center of the core
contributed significant positive reactivity, and that the outward expansion of
the structural plates supporting the fuel rods led to a delayed outward movement
of the fuel rods that contributed negative reactivity.
A three-temperature model was used to explain the phenomena observed. The
fast positive reactivity was modeled as due to the fuel bowing, and the delayed
negative reactivity was modeled as the fuel motion due to the delayed outward
motion of the fuel rods upon expansion of the structural plates. Heat conduction
plus convection for the two separate structural effects led to a three-term
representation of the power feedback. After correcting for the frequency dependence
of the oscillatory heat flow, the model achieved very good agreement with
the transfer function measurements.

## 5.11 Reactor Transients with Feedback

The dynamics equations are intrinsically nonlinear when feedback effects are
included. The calculation of reactor transients is carried out with very sophisticated
computer codes that model in detail the coupled dynamics of the neutrons,
temperature, flow, structural motion, change of state, and so on. However, some
physical insight as to the effects of feedback can be obtained by considering the
simple model of Section 5.4 in the presence of feedback.
The point kinetics equations with feedback may be written in the one-delayed
neutron group approximation as
dn(t)
dt
=
ρex + αFT(t) − β
Λ

n(t) + λC(t)
dC(t)
dt
= β
Λ n(t) − λC(t)
(5.130)
where a feedback reactivity ρf(t) = αfT(t) has been added to the step reactivity
insertion ρex. We will treat the temperature, T, as either a fuel temperature or a
lumped fuel–moderator temperature that satisfies
ρCP
dT(t)
dt
= Ef Σf vn(t) − θT(t)
(5.131)

<!-- page 185 (PDF 209) -->
where ρ is the density, Ef is the deposited energy per fission, and θ ≈ κ/(heat
transfer distance) account for conductive heat removal. In Section 5.4 we found
that the response to a step subprompt-critical (ρex < β) reactivity insertion into a
critical reactor was a prompt jump that changed the neutron density from n0 to
n0/(1 − ρex/β) in a time on the order of the neutron generation time, Λ, followed
by a slow rise (ρex > 0) or decay (ρex < 0) of the neutron density on the delayed
neutron decay constant timescale. We examine these two phases of the transient
separately in the presence of feedback.
Step Reactivity Insertion (ρex < β): Prompt Jump
During the initial phase of the transient for a few Λ following the reactivity
insertion, the delayed neutron precursor decay source is constant at the critical
equilibrium value λC0 = (β/Λ)n0. In the absence of feedback, the solution of
Eq. (5.130) in this case is
n(t) = n0 exp ρex − β
Λ
t

1 + β
Λ ∫
t
exp − ρex − β
Λ
t´

dt´

'
n0
1 − ρex=β
(5.132)
Assuming that the feedback is on the fuel temperature, which responds instantaneously
to an increase in the fission rate, the corresponding solution with
feedback reactivity is
n(t) = n0 exp ρex + αf T(t) − β
Λ
t

□ 1 + β
Λ ∫
t
exp − ρex + αf T(t´) − β
Λ
t´

dt´

(5.133)
On this short timescale t ∼Λ ≪ρCp/θ, the solution of Eq. (5.131) is
T(t) ' Ef vΣf
ρCp ∫
t
n t´
( )dt´
(5.134)
If the feedback is negative (αf < 0), the effect of the feedback is to reduce the
magnitude of the input reactivity step. If ρex > 0, n and T increase in time and
ρf = αfT < 0; if ρex < 0, n and T decrease in time and ρf = αfT > 0; (T0 = 0). If the
feedback is positive (αf > 0), the effect of the feedback is to enhance the magnitude
of the input reactivity step. If ρex > 0, n and T increase in time and ρf = αfT > 0;
if ρex < 0, n and T decrease in time and ρf = αf T < 0. Thus, negative feedback
reactivity would reduce the magnitude of the prompt jump and perhaps reverse

<!-- page 186 (PDF 210) -->
the sign if the feedback reactivity exceeds the input reactivity; positive feedback
reactivity would enhance the magnitude of the prompt jump.
Step Reactivity Insertion (ρex < β): Post-Prompt-Jump Transient
We saw in Section 5.4 that in the absence of feedback, after the initial prompt
jump in the neutron density on the prompt neutron timescale, the subsequent
transient evolves on the slower timescale of the delayed neutron precursor decay:
n(t) = n0 expf(λρex=β)t=(1 − ρex=β)g
1 − ρex=β
(5.135)
For the problem with feedback, we make use of the prompt-jump approximation
(set dn/dt = 0) and solve Eqs. (5.130) to obtain
n(t) '
n0 exp −λ t − ∫
t
dt´
1 − [ρex + αf T(t´)=β]

1 − [ρex + αf T(t)]=β
(5.136)
which reduces to Eq. (5.135) when αf = 0. Note that Eq. (5.136) is valid only for the
time after the prompt jump in neutron density between t = 0 and t = tpj ≈ Λ. This
equation evaluated at tpj implies an effective prompt jump from n0 →n0/[1 −
(ρex + αfT(tpj))/β], to be compared with the effective prompt jump from n0 →
n0/(1 − ρex/β) in the case without feedback implied by Eq. (5.135). Equation (5.131)
can be solved formally for the temperature
T(t) =
Ef vP
f
ρCp
∫
t
n t´
( ) exp − (θ=ρCp) t − t´
)dt´
(5.137)
The presence of feedback can have a dramatic effect on the course of the transient.
Consider a positive step reactivity insertion, 0 < ρex < β, which without feedback
would result in an exponentially increasing neutron density with period
(β/ρex − 1)/λ. With negative reactivity feedback (αf < 0), the period becomes
longer (the rate of increase is slower), or even becomes negative (the neutron
density decreases in time) if |αf |T(t) becomes greater than ρex. For a negative step
reactivity insertion, ρex < 0, and negative reactivity feedback, the presence of
feedback with the decreasing temperature causes the decay in the neutron density
to become slower and even reverse and start increasing if |αf T(t)| becomes greater
than |ρex|. Thus, a reactor with a negative temperature coefficient of reactivity will
adjust automatically to a step reactivity insertion by seeking a new critical
condition. For example, when a cold reactor is started up by withdrawing the
control rods to produce an increasing neutron population and increasing fission
heating, the negative reactivity will also increase, until the reactor reaches a new
temperature and neutron population at which it is just critical. A negative
temperature coefficient of reactivity also allows a reactor to automatically load

<!-- page 187 (PDF 211) -->
follow (an increase in power output demand will result in a decrease in coolant
inlet temperature, which produces a positive reactivity that causes the neutron
population and the fission rate to increase until a new critical condition is reached
at higher power).

## 5.12 Reactor Fast Excursions

The examination of hypothetical accidents requires the analysis of fast, supercritical
excursions in the neutron population in a reactor. Although this analysis is
done with sophisticated computer codes, which solve the coupled neutron–
thermodynamics–hydrodynamics equation of state equations, there are several
analytical models that provide physical insight into the phenomena of fast,
supercritical reactor excursions. Delayed neutron precursors respond too slowly
to be important in such transients and may be neglected.

### Step Reactivity Input: Feedback Proportional to Fission Energy

The prompt neutron kinetics equation for a step reactivity input Δk0 > kβ and a
feedback negative reactivity proportional to the cumulative fission energy release
is described by
P
dP(t)
dt
= k − 1
Λ
= Δk0 − αEE(t)
Λ
= Δk0
Λ − αE
Λ ∫
t
P t´
( )dt´
(5.138)
where Δk0 is measured relative to prompt critical and
E(t) ≡ ∫
t
P t´
( )dt´;
αE ≡ @k
@E
(5.139)
The solution of Eq. (5.139) is
E(t) = (Δk0=Λ) + R
αE=Λ
1 − e−Rt
[(R + Δk0=Λ)]
[(R − Δk0=Λ)] e−Rt + 1
(5.140)
where
R ≡
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
Δk0
Λ

+ 2 αE
Λ

P0
s
(5.141)
For transients initiated from low initial power level, P0, R ≈ Δk0/Λ and
E(t) '
2(Δk0=αE)(1 − e−(Δk0=Λ)t)
 2(Δk0=Λ)2
(αE=Λ)P0
e−(Δk0=Λ)t + 1

(5.142)

<!-- page 188 (PDF 212) -->
The instantaneous power is
P(t) =
_E(t) = 2R2
αE=Λ
R + (Δk0=Λ)
R − (Δk0=Λ)

e−Rt

R + (Δk0=Λ)
R − (Δk0=Λ)

e−Rt + 1

' 4(Δk0=Λ)4
(αE=Λ)2P0
e−(Δk0=Λ)t

2 (Δk0=Λ)2
(αE=Λ)P0
e−(Δk0=Λ)t + 1

(5.143)
where the second form is valid only for low initial power.
Equation (5.143) describes a symmetrical power excursion that increases to a
maximum power Pmax = (Δk0/Λ)2/2(αE/Λ) at t ≈ 1.3/(Δk0/Λ) and then decreases
to zero. The width of the power burst at half maximum is ≈3.52/(Δk0/Λ), and the
total fission energy produced in the burst is 2Δk0/αE.

### Ramp Reactivity Input: Feedback Proportional to Fission Energy

If, instead of a step reactivity input, the external reactivity input is a ramp (e.g., as
might occur in rod withdrawal), Eq. (5.138) becomes
P
dP(t)
dt
= at − αEE(t)
Λ
= at
Λ − αE
Λ ∫
t
P t´
( )dt´
(5.144)
which has a solution of the form
E(t) = a
αE
t + periodic function
(5.145)
The power level has a background (a/αE) upon which is superimposed a series of
oscillations as the net external plus feedback reactivity oscillates about prompt
critical (ρ = β). We now examine one of the power oscillations. Differentiating
Eq. (5.144) yields an equation for the instantaneous period θ ≡ (dP/dt)/P:
dθ(t)
dt
= a
Λ − αE
Λ P(t)
(5.146)
which may be combined with Eq. (5.144) to obtain
dP
dθ =
θP
a=Λ − (αE=Λ)P
(5.147)
This equation has the solution
2 θ2(t) = a
Λ ln P(t)
P0
− αE
Λ P(t) − P0
[
]
(5.148)

<!-- page 189 (PDF 213) -->
The maximum power at the peak of the oscillation occurs when θ = 0 and thus
satisfies
Pmax = P0 + a
αE
ln Pmax
P0
' a
αE
ln Pmax
P0
(5.149)
where the second form is only valid for P0 ≪Pmax, where P0 = a/αE now refers to
the background power at the beginning of the oscillation.

### Step Reactivity Input: Nonlinear Feedback Proportional to Cumulative Energy Release

The Doppler feedback coefficient in large fast power reactors is not constant
but is calculated to vary approximately inversely with fuel temperature, and
theoretical considerations suggest that it varies inversely with fuel temperature
to the
2 power. If we assume no heat loss from the fuel and constant specific
heat to relate the fuel temperature increase during a transient to the cumulative
fission energy release, we can represent a broad class of temperaturedependent
feedback reactivities as αEEn, where αE now refers to the value of the
feedback coefficient at the temperature at which the transient is initiated. In
this case, the prompt neutron dynamics equation for a step external reactivity
input Δk0 is
P
dP(t)
dt
= Δk0
Λ − α´E
Λ [E(t)]n
(5.150)
This equation has the solution for the cumulative fission energy release
E(t) = (n + 1) Δk0
α´E

1=n
1 + ne−(nΔk0=Λ)t
h
i1=n
(5.151)
which can be differentiated to obtain the instantaneous power
P(t) = _E(t)
=
(n + 1) Δk0
α´E

1=n
n2 Δk0
Λ

e−(nΔk0=Λ)t

1 + ne−(nΔk0=Λ)t
1=(n+1)
(5.152)
Once again, the power increases to a maximum value, in this case
Pmax =
n
1 + n
(Δk0=Λ)n+1
α´E=Λ

1=n

<!-- page 190 (PDF 214) -->
and then decreases to zero. The total energy release in the burst is Etot =
[(1 + n)Δk0/α´
E]1/n.

### Bethe–Tait Model

It is clear that the course of a reactor excursion produced by a given external
reactivity insertion is very sensitive to the feedback reactivity, hence to the
evolution of the thermodynamic, hydrodynamic, and geometric condition of
the reactor. The coupled evolution of these variables is calculated numerically in
modern analyses. However, we can gain valuable physical insight by considering
an early semianalytical model developed for fast metal fuel reactors. The prompt
neutron dynamics are determined by
P
dP(t)
dt
= k − 1 − β
Λ
= Δk
Λ
= Δk0 + Δkinput(t) + Δkdispl(t) + Δkother(t)
(5.153)
where Δk0 is the initiating step reactivity (relative to prompt critical), Δkinput is
any control rod input, Δkdispl is the reactivity associated with a displacement of
core material due to pressure buildup, and Δkother includes the Doppler effect and
other nonhydrodynamic reactivity changes.
The displacement reactivity is given by
Δkdispl(t) = ∫ρ(r; t)u(r; t) ? ∇w+(r)dr
(5.154)
where ρ is the material density, u(r, t) represents a material displacement from r to
r + Δr, and w+(r, t) is the importance of a unit mass of material at location r to
producing subsequent fission events. (The importance function is discussed in
Chapter 13.)
The displacement is related to the pressure by the hydrodynamic equations
ρ @2u(r; t)
@t2
= −∇p(r; t)
(5.155)
and
@ρ(r; t)
@t
+ ∇? ρ(r; t) @u(r; t)
@t

= 0
(5.156)
An equation of state, represented symbolically as
p(r; t) = p(e(r; t); ρ(r; t))
(5.157)

<!-- page 191 (PDF 215) -->
relates the pressure to the energy density, e(r, t), and to the density. We neglect
changes in density and work done in expansion or compression. Differentiating
Eq. (5.154) twice and using Eq. (5.155) yields
@2Δkdispl
@t2
= −∫∇p(r; t) ? ∇ω+(r)dr
(5.158)
The analysis proceeds by postulating that there is no feedback, except the
Doppler effect, until the total energy generated in the core reaches a threshold
value, E∗, at which point the core material begins to vaporize, thereby building up
pressure, which causes the core to expand until the negative reactivity associated
with expansion eventually terminates the excursion. Rather than carrying through
the involved derivation (see Ref. [3]), we summarize the main results for a
spherical core. When the energy, E, exceeds the threshold value, it subsequently
increases as
E − E∗= E∗e(Δk=Λ)(t−t∗) − 1

(5.159)
The pressure near the center of the core is proportional to E − E∗≈ E, so that
once it becomes large the pressure varies as
p ∼ENe(Δk=Λ)t
(5.160)
The pressure gradient that tends to blow the core apart is proportional to p/R.
Thus, the radial acceleration produced by the pressure gradient goes as
€R ∼j∇pj = C1
R e(Δk=Λ)t
(5.161)
Integrating this expression twice yields an expression for the instantaneous
core radius
R´(t) ' R 1 + C1Λ2
(Δk)2R2 e(Δk=Λ)t

(5.162)
The excursion terminates when the expansion increases the negative reactivity
sufficiently to offset the initiating reactivity less any negative Doppler or rod input
reactivity:
Δkdispl R´ − R
) = Δk0 − Δkother − Δkinput = Δk´
(5.163)
which occurs at time t given by
e(Δk´=Λ)t =
(Δk´)3R2
C1ΔkdisplΛ2
(5.164)

<!-- page 192 (PDF 216) -->
The energy generated up to the time of termination is
E ∼(Δk´)3R2
Λ2
(5.165)
Numerical calculations indicate that the approximate relationships above
represent quite well excursions resulting from large initial reactivity insertions.
For modest initiating reactivities, the expression
E
E∗− 1

∼(Δk´)3R2
Λ2

2=9
(5.166)
is in better qualitative agreement with numerical results.

## 5.13 Numerical Methods

In practice, numerical methods are used to solve the neutron dynamics equations.
The solution is made difficult by the difference in timescales involved. The prompt
neutron timescale is on the order of Λ = 10−4 to 10−5 s for thermal reactors or 10−6
to 10−7 s for fast reactors, while the delayed neutron timescales vary from tenths of
seconds to tens of seconds. When ρ is significantly less than β, making the promptjump
approximation remove the prompt neutron timescale from the problem, and
straightforward time-differencing schemes are satisfactory. When it is necessary to
retain the prompt neutron dynamics (i.e., for transients near or above prompt
critical), the usual numerical methods for solving ordinary differential equations
(e.g., Runge–Kutta) are limited by solution stability to extremely small time steps
over which there is little change in the neutron population. However, a class of
methods for solving stiff sets of ordinary differential equations (sets with very
different time constants) have been developed (Refs. [5] and [6]) and are now widely
used for solution of the neutron dynamics equations.

## References

1 A. F. HENRY, Nuclear-Reactor Analysis, MIT Press, Cambridge, MA (1975),
Chap. 7.
2 J. L. DUDERSTADT and L. J. HAMILTON, Nuclear Reactor Analysis, Wiley, New York
(1976), Chap. 6 and pp. 556–565.
3 H. H. HUMMEL and D. OKRENT, Reactivity Coefficients in Large Fast Power
Reactors, American Nuclear Society, La Grange Park, IL (1970).
4 G. I. BELL and S. GLASSTONE, Nuclear Reactor Theory, Wiley (Van Nostrand
Reinhold), New York (1970), Chap. 9.
5 G. HALL and J. M. WATTS, Modern Numerical Methods for Ordinary Differential
Equations, Clarendon Press, Oxford (1976).

<!-- page 193 (PDF 217) -->
6 C. W. GEAR, Numerical Initial Value Problems in Ordinary Differential Equations,
Prentice Hall, Englewood Cliffs, NJ (1971).

## Further Reading

AKCASU A. Z., LELLOUCHE G. S., and SHOTKIN M. L., Mathematical Methods in
Nuclear Reactor Dynamics, Academic Press, New York (1971).
ASH M., Nuclear Reactor Kinetics, McGraw-Hill, New York (1965).
FLATT H. P., “Reactor Kinetics Calculations,” in GREENSPAN H., KELBER C. N., and
OKRENT D., eds., Computational Methods in Reactor Physics, Gordon and Breach,
New York (1968).
HETRICK D. L., ed., Dynamics of Nuclear Systems, University of Arizona Press,
Tucson, AZ (1972).
HETRICK D. L. and WEAVER L. E., eds., Neutron Dynamics and Control, USAEC-
CONF-650413, U.S. Atomic Energy Commission, Washington, DC (1966).
KEEPIN G. R., Physics of Nuclear Kinetics, Addison-Wesley, Reading, MA (1965).
LASALLE J. and LEFSCHETZ S., Stability by Liapunov’s Direct Methods and Applications,
Academic Press, New York (1961).
MEGHREBLIAN R. V. and HOLMES D. K., Reactor Analysis, McGraw-Hill, New York
(1960), Chap. 9.
RADKOWSKY A., ed., Naval Reactors Physics Handbook, U.S. Atomic Energy
Commission, Washington, DC (1964), Chap. 5.
SAPHIER D., “Reactor Dynamics,” in RONEN Y., ed., CRC Handbook of Nuclear Reactor
Calculations II, CRC Press, Boca Raton, FL (1986).
THIE J. A., Reactor Noise, Rowman & Littlefield, Totowa, NJ (1963).
THOMPSON T. J. and BECKERLY J. G., eds., The Technology of Nuclear Reactor Safety,
MIT Press, Cambridge, MA (1964).
WEAVER L. E., ed., Reactor Kinetics and Control, USAEC-TID-7662, U.S. Atomic
Energy Commission, Washington, DC (1964).
WEAVER L. E., Reactor Dynamics and Control, Elsevier, New York (1968).

## Problems

### 5.1

The absorption cross section in a bare, critical thermal reactor is decreased
by 0.5% by removing a purely absorbing material. Calculate the associated
reactivity.

### 5.2

A bare metal sphere of essentially pure 235U is assembled, and the output of a
neutron detector is observed, after an initial transient, to be increasing exponentially
with a period T = 1s. The neutron effectiveness values for the six
delayed neutron groups are calculated to be γi = 1.10, 1.03, 1.05,1.03, 1.01, and
1.01. What is the effective multiplication constant, k, for the assembly?

### 5.3

Using the one-delayed precursor group approximation, prompt-jump
approximation, and the reactor parameters β = 0.0075, λ = 0.08 s−1, Λ =

<!-- page 194 (PDF 218) -->
6 × 10−5 s, solve for the time dependence of the neutron population over
the interval 0 < t < 10 s following the introduction of a ramp reactivity
ρ(t) = 0.1βt into a critical reactor for 0 < t < 5 s. Such a reactivity insertion
might result from partial withdrawal of a control rod bank.

### 5.4

A pulsed neutron measurement was performed in an assembly with
β = 0.0075 and Λ = 6 × 10−5. An exponential prompt neutron decay constant
α0 = −200 s−1 was measured. What are the reactivity and effective
multiplication constant of the assembly?

### 5.5

A control rod was partially withdrawn from a critical nuclear reactor for 5 s,
then reinserted to bring the reactor back to critical. The reactivity worth of
the partial rod withdrawal was ρ = 0.0025. Use the prompt-jump approximation
and a one-delayed neutron group approximation to calculate the
neutron and precursor populations, relative to the initial critical populations
, for times 0 < t < 10 s. Use the neutron kinetic parameters β = 0.0075,
λ = 0.08 s−1, and Λ = 6 × 10−5 s.

### 5.6

A control rod bank is scrammed in an initially critical reactor. The
signal of a neutron detector drops instantaneously to one-third of its
prescram level, then decays exponentially. Assume one group of delayed
neutrons with β = 0.0075 and λ = 0.08 s, and use Λ = 10−4 s for the reactor
lifetime. What is the reactivity worth of the control rod bank? How
long is needed for the power level to reach 1% of the initial prescram
level?

### 5.7

Plot the real and imaginary parts of the zero-power transfer function versus
ω(s = iω) for a 235U reactor using a one-delayed neutron group model with
β = 0.0075, λ = 0.08 s−1, and Λ = 6 × 10−5 s.

### 5.8

Calculate the Doppler reactivity temperature coefficient for a UO2-fueled,
H2O-cooled thermal reactor with long fuel rods 1 cm in diameter operating
with a fuel temperature of 450 K. The moderator macroscopic scattering
cross section per atom of 238U is 100. Take the resonance integral at 300 K
as I = 10 barns.

### 5.9

Derive an expression for the calculation of a void temperature coefficient of
reactivity for a pressurized water reactor (i.e., the temperature coefficient
associated with a small fraction of the moderator being replaced with void).
Repeat the calculation for when the water contains 1000 ppm 10B as a
“chemical shim.”

### 5.10

Calculate the nonleakage reactivity temperature coefficient for a bare
cylindrical graphite reactor with height-to-diameter ratio H/D = 1.0,
k1 = 1.10, migration area M2 = 400 cm2, and moderator linear expansion
coefficient θM = 1 × 10−5 °C−1.

<!-- page 195 (PDF 219) -->
### 5.11

Calculate the reactivity defect in a PWR with fuel and moderator temperature
coefficients of αF = −1.0 × 10−5 Δk/k/°F and αM = −2.0 × 10−4 Δk/k/°F
when the reactor goes from hot zero power (TF = TM = 530 °F) to hot full
power (TF = 1200 °F and TM = 572 °F).

### 5.12

A critical reactor is operating at steady state when there is a step reactivity
insertion ρ = Δk/k = 0.0025. Use one group of delayed neutrons, the
parameters β = 0.0075, λ = 0.08 s−1, and Λ = 6 × 10−5 s, and a temperature
coefficient of reactivity αT = −2.5 × 10−4 °C−1. Assume that the heat
removal is proportional to the temperature. Write the coupled set of
equations that describe the dynamics of the prompt and delayed neutrons
and the temperature. Linearize and solve these equations (e.g., by Laplace
transform).

### 5.13

Calculate the power threshold for linear stability (in units of P0XF/β) from
Eq. (5.111) for XF/XM = −0.25 and −0.50 and for ωM = 0.1, 0.25, and 0.5.

### 5.14

Analyze the linear stability of a one-temperature model for a nuclear
reactor in which the heat is removed by conduction with time constant ω−1
R
and in which there is an overall negative steady-state power coefficient,
XR < 0. Is the reactor stable at all power levels?

### 5.15

Repeat Problem 5.14 for convective heat removal.

### 5.16

Calculate and plot the power burst described by Eq. (5.143) for a fast
reactor with generation time Λ = 1 × 10−6 s and negative energy feedback
coefficient αE = −0.5 × 10−6 Δk/k/MJ into which a step reactivity insertion
of Δk0 = +0.02 takes place at t = 0. Use P0 = 100 MW.

### 5.17

A control rod is partially withdrawn (assume instantaneously) from a
235U-fueled nuclear reactor that is critical and at low power at room
temperature. The signal measured by a neutron detector is observed to
increase immediately to 125% of its value prior to rod withdrawal, and
then to increase approximately exponentially. What is the reactivity
worth of the control rod? What is the value of the exponent that governs
the long-time exponential increase of the signal measured by the neutron
detector?

### 5.18

In a cold critical PWR fueled with 4% enriched UO2, the control rod bank is
withdrawn a fraction of a centimeter, introducing a positive reactivity of
ρ = 0.0005. The neutron flux begins to increase, increasing the fission rate.
Discuss the feedback reactivity effects that occur as a result of the
increasing fission heating.

### 5.19

Use the temperature coefficients of reactivity given in Table 5.3 to calculate
the change in reactivity when the core temperature in an oxide-fueled fast

<!-- page 196 (PDF 220) -->
reactor increases from 300 to 500 °C. Assume uniform temperatures in
fuel, coolant, and structure. Repeat the calculation for a fuel temperature
increase to 800 °C and a coolant and structure temperature increase to
350 °C.

### 5.20

∗Solve Eqs. (5.133) and (5.134) to calculate the response of the neutron
population in a UO2-fueled PWR to step rod withdrawal with reactivity
worth ρ = 0.002, taking into account a negative fuel Doppler feedback
coefficient of −2 × 10−6 Δk/k/K. The reactor has neutronics properties
(β = 0.0065, λ = 0.08 s−1, Λ = 1.0 × 10−4), fission heat deposition in the fuel
vnΣfEf = 250 W/cm3, and fuel properties ρ = 10.0 g/cm3 and Cp = 220 J/kg.
(Hint: It is probably easiest to do this numerically.)

### 5.21

Evaluate
the
resonance
escape probability
moderator temperature
coefficient of reactivity of Eq. (5.87) for a UO2 reactor consisting of
assemblies of 1-cm-diameter fuel pins of height H in a water lattice
with Σp/NF = 100 and fuel density ρ = 10 g/cm3. Use θM = 1 × 10−4/K for
the linear coefficient of expansion for water.

### 5.22

Derive an explicit expression for the thermal utilization temperature
coefficient of reactivity of Eq. (5.89) by using Eqs. (3.90) and (3.92) to
evaluate the @PF
a/@ξ and @ξ/@TF terms and equivalent relations to
evaluate the dΣM
a =dξ and dξ/dTM terms.

### 5.23

In a “rod-drop” experiment, a control rod is dropped into a cold, critical
reactor. The neutron flux is observed to immediately drop to one-half of its
value prior to the rod drop and then decay slowly. Using a one-delayed
group model with delayed neutron fraction β = 0.0065 and decay constant
λ = 0.08/s, determine the reactivity worth of the control rod.
∗Problem 5.20 is a longer problem suitable for a take-home project.
