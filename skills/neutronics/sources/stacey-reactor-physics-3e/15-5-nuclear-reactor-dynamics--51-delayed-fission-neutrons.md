# 5 Nuclear Reactor Dynamics — 5.1 Delayed Fission Neutrons … 5.6 Experimental Determination of Neutron Kinetics Parameters
<!-- source PDF pages 165-183 -->

<!-- page 141 (PDF 165) -->
# 5 Nuclear Reactor Dynamics

An understanding of the time-dependent behavior of the neutron population in a
nuclear reactor in response to either a planned change in the reactor conditions or
to unplanned and abnormal conditions is of the utmost importance to the safe
and reliable operation of nuclear reactors. We saw in Chapter 2 that the response
of the prompt neutrons is very rapid indeed. However, unless the reactor is
supercritical on prompt neutrons alone, the delayed emission of a small fraction
of the fission neutrons can slow the increase in neutron population to the delayed
neutron precursor decay timescale of seconds, providing time for corrective
control measures to be taken. If a change in conditions makes a reactor
supercritical on prompt neutrons alone, only intrinsic negative feedback mechanisms
that automatically provide a compensating change in reactor conditions in
response to an increase in the neutron population can prevent a runaway increase
in neutron population (and fission power level). However, some of the intrinsic
changes in reactor conditions in response to a change in power level may enhance
the power excursion (positive feedback), and others may be negative but delayed
sufficiently long that the compensatory reactivity feedback is out of phase with the
actual condition of the neutron population in the reactor, leading to power-level
instabilities. These reactor dynamics phenomena, the methods used for their
analysis, and the experimental techniques for determining the basic kinetics
parameters that govern them are discussed in this chapter.

## 5.1 Delayed Fission Neutrons

### Neutrons Emitted in Fission Product Decay

The dynamics of a nuclear reactor or any other fission chain-reacting system
under normal operation is determined primarily by the characteristics of the
delayed emission of neutrons from the decay of fission products. The total yield of
delayed neutrons per fission, νd, depends on the fissioning isotope and generally
increases with the energy of the neutron causing fission. Although there are a
relatively large number of fission products that subsequently decay via neutron
emission, the observed composite emission characteristics can be well represented
by defining six effective groups of delayed neutron precursor fission
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 142 (PDF 166) -->
products. Each group can be characterized by a decay constant, λi, and a relative
yield fraction, βi/β. The fraction of the total fission neutrons that are delayed is
β = νd/ν. The parameters of delayed neutrons emitted by fission product decay of
several relevant isotopes are given in Table 5.1.
Table 5.1 Delayed Neutron Parameters
Fast Neutrons
Thermal Neutrons
Group
Decay
Constant λi (s−1)
Relative
Yield βi/β
Decay
Constant λi (s−1)
Relative
Yield βi/β
233U
νd = 0.00 731
νd = 0.00 667
β = 0.0026
β = 0.0026
0.0125
0.096
0.0126
0.086
0.0360
0.208
0.0337
0.299
0.138
0.242
0.139
0.252
0.318
0.327
0.325
0.278
1.22
0.087
1.13
0.051
3.15
0.041
2.50
0.034
235U
νd = 0.01 673
νd = 0.01 668
β = 0.0064
β = 0.0067
0.0127
0.038
0.0124
0.033
0.0317
0.213
0.0305
0.219
0.115
0.188
0.111
0.196
0.311
0.407
0.301
0.395
1.40
0.128
1.14
0.115
3.87
0.026
3.01
0.042
239Pu
νd = 0.0063
νd = 0.00 645
β = 0.0020
β = 0.0022
0.0129
0.038
0.0128
0.035
0.0311
0.280
0.0301
0.298
0.134
0.216
0.124
0.211
0.331
0.328
0.325
0.326
1.26
0.103
1.12
0.086
3.21
0.035
2.69
0.044
241Pu
νd = 0.0152
νd = 0.0157
β = 0.0054
–
–
0.0128
0.010
–
–
0.0297
0.229
–
–
0.124
0.173

<!-- page 143 (PDF 167) -->
### Effective Delayed Neutron Parameters for Composite Mixtures

The delayed neutrons emitted by the decay of fission products are generally less
energetic (average energy about 0.5 MeV) than the prompt neutrons (average
energy about 1 MeV) released directly in the fission event. Thus, these delayed
neutrons will slow down quicker than the prompt neutrons and experience less
probability for absorption and leakage in the process (i.e., the delayed and prompt
Table 5.1
(Continued )
Fast Neutrons
Thermal Neutrons
Group
Decay
Constant λi (s−1)
Relative
Yield βi/β
Decay
Constant λi (s−1)
Relative
Yield βi/β
–
–
0.352
0.390
–
–
1.61
0.182
–
–
3.47
0.016
232Th
νd = 0.0531
β = 0.0203
0.0124
0.034
0.0334
0.150
0.121
0.155
0.321
0.446
1.21
0.172
3.29
0.043
238U
νd = 0.0460
β = 0.0164
0.0132
0.013
0.0321
0.137
0.139
0.162
0.358
0.388
1.41
0.225
4.02
0.075
240Pu
νd = 0.0090
β = 0.0029
0.0129
0.028
0.0313
0.273
0.135
0.192
0.333
0.350
1.36
0.128
4.04
0.029

<!-- page 144 (PDF 168) -->
neutrons have a difference in their effectiveness in producing a subsequent fission
event). Since the energy distribution of the delayed neutrons differs from group to
group, the different groups of delayed neutrons will also have a different
effectiveness. Furthermore, a nuclear reactor will, of course, contain a mixture
of fissionable isotopes (e.g., a uranium-fueled reactor will initially contain 235U
and 238U, and after operation for some time will also contain some admixture of
239Pu, 240Pu, and so on; see Chapter 6).
To deal with this situation, it is necessary to define an importance function,
ϕ+(r, E), which is the probability that a neutron introduced at position r and
energy E will ultimately result in a fission (Chapter 13). Then the relative
importance (to the production of a subsequent fission) of delayed neutrons in
group i emitted with energy distribution χq
di(E) and prompt neutrons from the
fission of isotope q emitted with energy distribution χq
p(E) are
Iq
di = ∫dV∫
dEχq
di(E)ϕ+(r; E)∫
dE´νσq
f (E´)Nq(r)ϕ(r; E´)
(5.1)
Iq
p = ∫dV∫
dEχq
p(E)ϕ+(r; E)∫
dE´νσq
f (E´)Nq(r)ϕ(r; E´)
(5.2)
The relative effective delayed neutron yield of group i delayed neutrons for
fissionable isotope q is Iq
diβq
i , where βq
i is the group i delayed neutron yield of
fissionable isotope q given in Table 5.1. The effective group i delayed neutron
fraction for isotope q in a mixture of fissionable isotopes is then
γiβq
i = Iq
diβq
i
 X
q
Iq
p
1 −
X
i=1
βq
i
!
+
X
i=1
Iq
diβq
i
"
(5.3)
The effectiveness of delayed neutron group i of fissionable isotope q in a specific
admixture of fissionable isotopes and reactor geometry is then γq
i = γq
i βq
i =βq
i . In
the remainder of the book, except when specifically stated otherwise, it is assumed
that the delayed neutron effectiveness is included in the evaluation of βi and β, and
the effectiveness parameter will be suppressed.

### Photoneutrons

Fission products also emit gamma rays when they undergo β-decay. A photon can
eject a neutron from a nucleus when its energy exceeds the neutron binding
energy. Although most nuclei have neutron binding energies in excess of 6 MeV,
which is above the energy of most gamma rays from fission, there are four nuclei
that have sufficiently low neutron binding energy, En, to be of practical interest:
2D (En = 2.2 MeV),
9Be (En = 1.7 MeV),
6Li (En = 5.4 MeV), and
13C (En =
4.9 MeV). The photoneutrons can be considered as additional groups of delayed
neutrons. Since the β-decay of fission products is generally much slower than the
direct neutron decay, the photoneutron precursor decay constants are much

<!-- page 145 (PDF 169) -->
smaller than the delayed neutron precursor decay constants, as shown in
Table 5.1. The only reactors in which photoneutrons are of practical importance
are D2O-moderated reactors. As we shall see, the dynamic response time of a
reactor under normal operation is largely determined by the inverse decay
constants, and consequently, D2O reactors are quite sluggish compared with
other reactor types.

## 5.2 Point Kinetics Equations

The delayed neutron precursors satisfy an equation of the form
@ ^Ci
@t (r; t) = βiνΣf (r; t)ϕ(r; t) − λi ^Ci(r; t);
i = 1; . . . ; 6
(5.4)
The one-speed neutron diffusion equation is now written as
v
@ϕ(r; t)
@t
− D(r; t)∇2ϕ(r; t) + Σa(r; t)ϕ(r; t)
= (1 − β)νΣf (r; t)ϕ(r; t) +
X
i=1
λi ^Ci(r; t)
(5.5)
where we have taken into account that a fraction β of the fission neutrons is
delayed and that there is a source of neutrons due to the decay of the delayed
neutron precursors.
Based on the results of Chapter 3, we assume a separation-of-variables solution
ϕ(r; t) = vn(t)ψ1(r);
^Ci(r; t) = Ci(t)ψ1(r)
(5.6)
where ψ1 is the fundamental mode solution of
∇2ψn + B2
gψn = 0
(5.7)
and Bg is the geometric buckling appropriate for the reactor geometry, as
discussed in Chapter 3. Using this in Eqs. (5.4) and (5.5) leads to the point
kinetics equations
dn(t)
dt
= ρ(t) − β
Λ
n(t) +
X
i=1
λiCi(t)
dCi(t)
dt
= βi
Λ n(t) − λiCi(t);
i = 1; . . . ; 6
(5.8)

<!-- page 146 (PDF 170) -->
where
Λ ≡ vνΣF
) − 1
(5.9)
is the mean generation time between the birth of a fission neutron and the
subsequent absorption leading to another fission, and
ρ(t) ≡
νΣF − Σa(1 + L2B2
g)
νΣF
≡ k(t) − 1
k(t)
(5.10)
is the reactivity. The quantity k is the effective multiplication constant, given by
k ≡ νΣF=Σa
1 + L2B2
g
(5.11)
For predominantly thermal reactors, νΣf and Σa are thermal cross sections,
and L2 should be replaced by M2 = L2 + τth to include the fast diffusion while
the neutron is slowing down, τth, as well as the thermal diffusion length, L2.
For fast reactors, all cross sections are averaged over the appropriate fast
spectrum.
The limiting assumption for the validity of the point kinetics equations is the
assumption of a constant spatial shape. As we will see, this assumption is
reasonable for transients caused by uniform changes in reactor properties or
for reactors with dimensions that are only a few migration lengths, M (or diffusion
lengths, L), but is poor for reactors with dimensions that are very large compared
with M in which the transient is caused by localized changes in reactor properties
(e.g., a nonsymmetric control rod withdrawal). However, as we will see in
Chapter 16, such spatial shape changes can be taken into account in computation
of the reactivity and the mean generation time, and the point kinetics equations
can be extended to have a much wider range of validity.

## 5.3 Period–Reactivity Relations

Equations (5.8) may be solved for the case of an initially critical reactor in which
the properties are changed at t = 0 in such a way as to introduce a reactivity ρ0
which is then constant over time, by Laplace transforming, or equivalently
assuming an exponential time dependence e−st. The equations for the timedependent
parts of n and Ci are
sn(s)
= ρ0 − β
Λ
n(s) +
X
i=1
λiCi(s) + n0
sCi(s) = βi
Λ n(s) − λiCi(s) + Ci0;
i = 1; . . . ; 6
(5.12)

<!-- page 147 (PDF 171) -->
which can be reduced to
n(s) = f (s; n0; Ci0)
Y(s)
(5.13)
where
Y(s) ≡ ρ0 − s Λ +
X
i=1
βi
s + λi
!
(5.14)
The poles of the right side – the roots of Y(s) = 0 – determine the time
dependence of the neutron and precursor populations. Y(s) = 0 is a seventhorder
equation, known as the inverse hour, or more succinctly, the inhour,
equation, the solutions of which are best visualized graphically, as indicated in
Fig. 5.1, where the right-hand side of
ρ0 = s Λ +
X
i=1
βi
s + λi
!
(5.15)
is plotted. The left-hand side, ρ0, would plot as a straight horizontal line, of course,
and the points at which it crosses the right-hand side are the solutions (roots of the
equation). For ρ0 < 0, indicated by the circles in Fig. 5.1, all the solutions sj < 0. For
ρ0 > 0, indicated by the crosses, there are one positive and six negative solutions.
The solution for the time-dependent neutron flux is of the form
n(t) =
X
j=0
Ajesjt
(5.16)
+
+
+
+
+
+
+
-λ6
-λ5
-λ4
-λ3
-λ2
-λ1
Λ
-β
ω
f(ω)
Fig. 5.1 Plot of the function R(ω) = ω[Λ + Σβi/(ω + λi)], which appears in the inhour equation.
(With permission from Ref. [1]. Copyright 1975, MIT Press.)

<!-- page 148 (PDF 172) -->
where the sj are the roots of Y(s) = 0 and the Aj are given by
Aj =
Λ +
X
i=1
βi
sj + λi
!,
1 + k
X
i=1
βiλi
(sj + λi)2
"
(5.17)
After a sufficient time, the solution will be dominated by the largest root s0 (s0 > 0
when ρ0 > 0, s0 is the least negative root when ρ0 < 0):
n(t) ' A0es0t ≡ A0et=T
(5.18)
where T ≡ s−1
is referred to as the asymptotic period. Measurement of the
asymptotic period then provides a means for the experimental determination
of the reactivity
ρ0 = 1
T
Λ +
X
i=1
βi
(1=T) + λi
"
(5.19)

## 5.4 Approximate Solutions of the Point Neutron Kinetics Equations

### One-Delayed Neutron Group Approximation

To simplify the problem so that we can gain insight into the nature of the solution
of the point kinetics equations, we assume that the six groups of delayed neutrons
can be replaced by one-delayed neutron group with an effective yield fraction
β = Σiγiβi and an effective decay constant λ = Σiβiλi/β, so that the point kinetics
equations become
dn
dt = ρ − β
Λ
n + λC;
dC
dt = β
Λ n − λC
(5.20)
Proceeding as in Section 5.3 by Laplace transforming or assuming an est form of
the solution, the equivalent of Eq. (5.13) for the determination of the roots of the
reduced inhour equation is
s2 −
ρ − β
Λ
− λ

s − λρ
Λ = 0
(5.21)
which has the solution
s1;2 = 1
ρ − β
Λ
− λ

−
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ρ − β
Λ
+ λ

+ βλ
Λ
s
= 1
ρ − β
Λ
− λ

−
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ρ − β
Λ
− λ

+ λρ
Λ
s
(5.22)

<!-- page 149 (PDF 173) -->
For ρ > 0, one root is positive and the other is negative; for ρ = 0, one root is zero
and the other is negative; and for ρ < 0, both roots are negative.
The assumed est time dependence, when used in Eqs. (5.20), requires that for
each of the two roots, s1 and s2, there is a fixed relation between the precursor and
the neutron populations:
C(t)
n(t) =
β
Λ(s1;2 + λ) = − ρ − β
Λ
− s1;2

λ
(5.23)
which means that the solution of Eqs. (5.20) is of the form
n(t) = A1es1t + A2es2t;
C(t) = A1
β
Λ(s1 + λ) es1t + A2
β
Λ(s2 + λ) es2t
(5.24)
Now, let us take some parameters typical of a light water reactor: β = 0.0075,
λ = 0.08 s−1, Λ = 6 × 10−5 s. Except for |ρ − β| ≈ 0, one root of Eq. (5.21) will be of
very large magnitude, and the other will be of very small magnitude. For the larger
root, s2
1 □ λρ=Λ and λρ/Λ can be neglected in Eq. (5.21); and for the smaller root,
s2
2 □ λρ=Λ and s2
2 can be neglected. Assuming that |ρ − β|/Λ ≫λ, the solutions of
Eq. (5.21) are
s1 = ρ − β
Λ
;
s2 = − λρ
ρ − β
(5.25)
The constants A1 and A2 can be evaluated by requiring that the solution satisfies the
initial condition at t = 0 that is determined by setting ρ = 0 in Eqs. (5.24), which
identifies A1≈ n0ρ/(ρ − β) and A2≈ −n0β/(ρ − β), where n0 is the initial neutron
population before the reactivity insertion, so that the solutions of Eqs. (5.24) become
n(t) = n0
ρ
ρ − β exp ρ − β
Λ
t

−
β
ρ − β exp − λρ
ρ − β t

c(t) = n0
ρβ
(ρ − β)2 exp ρ − β
Λ
t

− β
Λλ exp − λρ
ρ − β t

(5.26)
At t = 0, before the reactivity insertion, C0 = βn0/Λλ ≈ 1600n0. Thus, the population
of delayed neutron precursors, hence the latent source of neutrons, is about
1600 times greater than the neutron population in a critical reactor. It is not
surprising that this large latent neutron source controls the dynamics of the
neutron population under normal conditions, as we shall now see.

### Example 5.1 Step Negative Reactivity Insertion, ρ < 0

Equations (5.26) enable
ustoinvestigate the neutron kinetics ofa nuclear reactor. We firstconsider the case
of a large negative reactivity insertion ρ = −0.05 into a critical reactor at t = 0, such
as might be produced by scramming (rapid insertion) of a control rod bank. With

<!-- page 150 (PDF 174) -->
the representative light water reactor parameters (β = 0.0075, λ = 0.08 s−1, Λ =
6 × 10−5 s), Eqs. (5.26) become
n(t) = n0(0:87e−958t + 0:13e−0:068t)
C(t) = n0(0:0113e−958t + 1563e−0:068t)
(5.27)
which is plotted in Fig. 5.2, with T ≡ n. The first term goes promptly to zero on a
timescale Δt ≈ Λ, corresponding physically to readjustment of the prompt
neutron population to the subcritical condition of the reactor on the neutron
generation timescale. The second term decays slowly, corresponding to the slow
decay of the delayed neutron precursor source of neutrons. The neutron
population drops promptly from n0 to n0/(1 − ρ/β) – the prompt jump – then
slowly decays as e−[λ/(1−β/ρ)]t. Thus, scramming a control rod bank cannot
immediately shut down (reduce the neutron population or the fission rate to
near zero) a nuclear reactor or other fission chain-reacting medium. The delayed
neutron precursors decay as e−[λ/(1−β/ρ)]t.

### Example 5.2 Subprompt-Critical (Delayed Critical) Step Positive Reactivity Insertion, 0 < ρ < β

Next, consider a positive reactivity insertion ρ = 0.0015 < β,
such as might occur as a result of control rod withdrawal. Equations (5.26) now
become
n(t) = n0(−0:25e−100t + 1:25e0:02t)
C(t) = n0(0:3125e−100t + 1562:5e0:02t)
(5.28)
which is plotted in Fig. 5.3. The neutron population increases promptly, on the
neutron generation timescale – the prompt jump – from n0 to n0/(1 − ρ/β), as the
prompt neutron population adjusts to the supercritical condition of the reactor,
1.0
0.5
C(t)
T0
C(t)
T0
T(t)
t(s)
T0
T(t)
T0
Fig. 5.2 Neutron and delayed neutron precursor decay following negative reactivity insertion
ρ = −0.05 into a critical nuclear reactor. (With permission from Ref. [1]. Copyright 1975, MIT Press.)

<!-- page 151 (PDF 175) -->
then increases as e−[λ/(1−β/ρ)]t, governed by the rate of increase in the delayed
neutron source. The relatively slow rate of increase of the neutron population,
following the prompt jump, allows time for corrective control action to be taken
before the fission rate becomes excessive.

### Example 5.3 Superprompt-Critical Step Positive Reactivity Insertion, ρ > β

Now considera step increase ofreactivityρ = 0.0115 > β,suchas mightoccurasthe
result of the ejection of a bank of control rods from a reactor. Equations (5.26) now
become
n(t) = n0(2:9e66:7t − 1:9e−0:23t)
C(t) = n0(5:4e66:7t + 1563e−0:23t)
(5.29)
The neutron population in the reactor grows exponentially on the neutron
generation timescale, n ∼e[(ρ−β)/Λ]t, because the reactor is supercritical on prompt
neutrons alone [i.e., k(1 − β) > 1]. In this example, the neutron population would
increase by almost a factor of 800 in a tenth of a second, and it would be impossible
to take corrective action quickly enough to prevent excessive fission heating and
destruction of the reactor. Fortunately, there are inherent feedback mechanisms
that introduce negative reactivity instantaneously in response to an increase in the
fission heating (e.g., the Doppler effect discussed in Sections 5.7 and 5.8), and the
neutron population will first increase rapidly, then decrease. However, conditions
that would lead to superprompt-critical reactivity insertion are to be avoided for
reasons of safety. Since β = 0.0026 for 233U, 0.0067 for 235U, and 0.0022 for 239Pu,
the safe operating range for positive reactivity insertions, 0 < ρ < β, is much larger
for reactors fueled with 235U than for reactors fueled with 233U or 239Pu.

### Prompt-Jump Approximation

We found that with a reactivity insertion for which the reactor condition is less
than prompt critical (ρ < β) the neutron population changed sharply on the
C(t)
t(s)
1.0
1.25
1.50
1.75
2.00
2.25
2.5
T0
C(t)
T0
T(t)
T0
T(t)
T0
Fig. 5.3 Neutron and delayed neutron precursor increase following subprompt-critical
positive reactivity insertion ρ = 0.0015 < β into a critical nuclear reactor. (With permission
from Ref. [1]. Copyright 1975, MIT Press.)

<!-- page 152 (PDF 176) -->
neutron generation timescale, then changed slowly on the delayed neutron
inverse decay constant timescale. If we are not interested in the details of the
prompt neutron kinetics during the prompt jump, we can simplify the equations
by assuming that the prompt jump takes place instantaneously in response to any
reactivity change, and afterward the neutron population changes instantaneously
in response to changes in the delayed neutron source (i.e., we set the time
derivative to zero in the neutron equation).
0 = [ρ(t) − β]n(t) + Λ
X
i=1
λiCi(t)
(5.30)
Since the delayed neutron precursor population does not respond instantaneously
to a change in reactivity, Eq. (5.30) is valid with the same delayed precursor
population both before and just after a change in reactivity from ρ0 to ρ1 < β, from
which we conclude that the ratio of the neutron populations just after and before
the reactivity change is
n1
n0
= β − ρ0
β − ρ1
(5.31)
Use of Eq. (5.30) to eliminate n(t) in the second of Eqs. (5.8) yields a coupled set of
equations for the time dependence of the precursor density:
dCi
dt =
βi
ρ(t) − βi
X
j=1
λjCj(t) − λiCi(t)
(5.32)
which in the one-delayed precursor group approximation takes on the simple
form
dC(t)
dt
=
−λC(t)
1 − β=ρ(t)
(5.33)
The prompt-jump approximation is convenient for numerical solutions
because it eliminates the fast timescale due to Λ, which introduces difficulties
in time-differencing methods. Numerical solutions of the point kinetics equations
with and without the prompt-jump approximation for a variety of reactivity
insertions indicate that the prompt-jump approximation is accurate to within
about 1% for reactivities ρ < 0.5 β.
Using the one-delayed precursor group approximation, the equivalent of
Eq. (5.30) can be solved for C(t) and used in the second of Eqs. (5.20) to obtain
ρ(t) − β
[
] dn(t)
dt
+ dp(t)
dt
+ λρ(t)

n(t) = 0
(5.34)
which for a given reactivity variation ρ(t) can be solved for the neutron population:
n(t) = n0exp ∫
t
_ρ(t´) + λρ(t´)
β − ρ(t´)
dt´

(5.35)

<!-- page 153 (PDF 177) -->
### Example 5.4 Reactivity Worth of Rod Insertion

The neutron flux measured
by a detector is observed to drop instantaneously from n0 to 0.5 n0 when a
control rod is dropped into a cold highly enriched critical nuclear reactor, in
which ρ0 = 0. Using the one-delayed group model with β = 0.0065, Eq. (5.31)
yields ρ1 = β(1 − n0/n1) = 0.0065(1 − 2) = −0.0065Δk/k.

### Reactor Shutdown

We mentioned that the large step negative reactivity insertion considered
previously might be representative of the situation encountered in a reactor
shutdown, or scram. However, the time required to fully insert control rods is very
long compared with the prompt neutron generation time that governs the
timescale of the prompt jump. We can improve on the representation of the
control rod insertion by considering a ramp reactivity insertion ρ(t) = −εt. If we
are only interested in calculating the initial rapid decrease in the neutron
population, we can make the assumption that the initial precursor concentration
remains constant; hence the precursor source of delayed neutrons remains
constant at its preinsertion value:
X
i=1
λiCi(0) = β
Λ n0
(5.36)
Using this approximation, the equation governing the prompt neutron response
to the reactivity insertion – the first of Eqs. (5.8) – can be integrated to obtain
n(t) = n0 exp − 1
Λ
2 εt2 + βt

+ β
Λ ∫
t
exp − 1
Λ
ε
2 (t2 − (t´)2) + β(t − t´)
h
i

dt´

(5.37)
This provides a somewhat better description of the initial reduction in the
neutron population than do Eqs. (5.27), which, however, would still govern
the long-time decay after completion of the rod insertion.

## 5.5 Delayed Neutron Kernel and Zero-Power Transfer Function

### Delayed Neutron Kernel

The delayed neutron precursor equations, the second of Eqs. (5.8), can be
formally integrated to obtain (assuming that Ci = 0 at −∝)
Ci(t) = ∫
t
−1
βi
Λ n(t´)e−λi(t−t´)dt´ = ∫
βi
Λ e−λiτn(t − τ)dτ:
(5.38)

<!-- page 154 (PDF 178) -->
Using this result in the neutron kinetics equation, the first of Eqs. (5.8), yields
dn(t)
dt
=
ρ(t) − β
Λ

n(t) + ∫
β
Λ D(τ)n(t − τ)dτ
(5.39)
where we have defined the delayed neutron kernel
D(τ) ≡
X
i=1
λiβi
β e−λiτ
(5.40)

### Zero-Power Transfer Function

If the neutron population is expanded about the initial neutron population in the
critical reactor at t = 0,
n(t) = n0 + n1(t)
(5.41)
Eq. (5.39) may be rewritten as
dn1(t)
dt
= ρ(t)n0
Λ
+ ρ(t)n1(t)
Λ
+ ∫
β
Λ D(τ) n1(t − τ) − n1(t)
[
]dτ
(5.42)
The Laplace transform of a function of time A(t) is defined as
A(s) = ∫
A(t)e−st dt
(5.43)
Laplace transforming Eq. (5.42) and using the convolution theorem
L ∫
A(t)B(τ − t)dt

= A(s)B(s)
(5.44)
yield, upon assuming that the term ρ(t)n1(t) is a product of two small terms and
can be neglected relative to ρ(t)n0,
n1(s) = n0Z(s)ρ(s)
(5.45)
where
Z(s) ≡ 1
s
Λ +
X
i=1
βi
s + λi
!−1
(5.46)

<!-- page 155 (PDF 179) -->
is the zero-power transfer function, which defines the response of the density n1 to
the reactivity.
The inverse Laplace transformation of Eq. (5.45) and the convolution theorem
yield the solution for the time dependence of the neutron population as a function
of the time dependence of the reactivity:
n1(t) = n0∫
t
dτ Z(t − τ)ρ(τ)
(5.47)
where the inverse Laplace transform of the zero-power transfer function is
Z(t − τ) = 1
Λ +
X
j=2
esj(t−τ)
sj Λ + P6
i=1[βiλi=(sj + λi)2]
n
o
(5.48)
and the sj are the roots of the inhour equation, Y(s) = 0, with Y(s) given by
Eq. (5.14).

## 5.6 Experimental Determination of Neutron Kinetics Parameters

### Asymptotic Period Measurement

When a critical reactor is perturbed by a step change in properties, the asymptotic
period may be determined from the response R(t) of neutron detectors by T−1 =
d(lnR)/dt; then the period–reactivity relation of Eq. (5.19) can be used to infer the
reactivity. For negative reactivities, the asymptotic period, the largest root of the
inhour equation, is dominated by the largest delayed neutron period and is
relatively insensitive to the value of the reactivity, so this method is limited
practically to supercritical reactivity (0 < ρ) measurements, for which Eq. (5.19)
may be written as
ρ
β = Λ
βT +
X
i=1
βi=β
1 + λiT '
X
i=1
βi=β
1 + λiT
(5.49)
where the fact that safety considerations further limit the practical applicability of
this method to the delayed critical regime (0 < ρ < β) has been taken into account
in writing the second form of the equation.

### Rod Drop Method

The responses of a neutron detector immediately before (R0 ∼n0) and after
(R1 ∼n1) a control rod is dropped into a critical reactor (ρ0 = 0) are related by

<!-- page 156 (PDF 180) -->
Eq. (5.31), which allows determination of the reactivity worth of the rod
ρ1
β = 1 − R0
R1
(5.50)

### Source Jerk Method

Consider a subcritical system that is maintained at equilibrium neutron, n0, and
precursor, Ci0, populations by an extraneous neutron source rate, S. The neutron
balance equation is
ρ − β
Λ

n0 +
X
i=1
λiCi0 + S = 0
(5.51)
If the source is jerked, the prompt-jump approximation for the neutron density
immediately after the source jerk is
ρ − β
Λ

n1 +
X
i=1
λiCi0 = 0
(5.52)
because the delayed neutron precursor population will not change immediately.
These equations and the equilibrium precursor concentrations Ci0 = βin0/λiΛ
may be used to relate the responses of a neutron detector immediately before
(R0 ∼n0) and after (R1 ∼n1) the source jerk to the reactivity of the system:
ρ
β = 1 − R0
R1
(5.53)

### Pulsed Neutron Methods

The time dependence of the prompt neutron population in a subcritical fission
chain-reacting medium following the introduction of a burst of neutrons is
described by
v
@ϕ(r; t)
@t
= D∇2ϕ(r; t) −
X
a − (1 − β)v
X
f
h
i
ϕ(r; t)
(5.54)
since the delayed neutrons will not contribute until later. As discussed in Section
3.6, the asymptotic solution that remains after higher order spatial transients
decay is the fundamental mode, which decays exponentially:
n(r; t) ' A1ψ1(r)e−v[Σa−(1−β)vΣf +DB2
g]t
(5.55)

<!-- page 157 (PDF 181) -->
where Bg is the fundamental mode geometric buckling for the geometry of the
system.
If the neutron detector response, R(r, t) ∼n(r, t), is measured as a function of
time, then
α0 = 1
R
dR
dt = v v
X
f (1 − β) −
X
a − DB2
g
h
i
= ρ − β
Λ
(5.56)
Thus, the pulsed neutron method can be used to determine ∼ρ/Λ, assuming that
β/Λ is known. If the experiment is performed in a critical system (ρ = 0), the
measurement yields a value for β/Λ. In practice, a correction must be made to
account for transport- and energy-dependent effects that have been neglected in
this analysis, so that
α0 = v v
X
f (1 − β) −
X
a − DB2
g − CB4
g + ∙∙∙
h
i
(5.57)

### Rod Oscillator Measurements

The response of the neutron population, as measured by a neutron detector
R(t) ∼n(t), to a sinusoidal oscillation of a control rod that produces a sinusoidal
reactivity perturbation
ρ(t) = ρ0 sin ωt
(5.58)
can be used to determine a number of neutron kinetics parameters. The
response of the neutron population to a sinusoidal reactivity perturbation
can be calculated from Eq. (5.45) by first computing the Laplace transform of
Eq. (5.58):
ρ(s) =
ρ0ω
s2 + ω2 =
ρ0ω
(s + iω)(s − iω)
(5.59)
and then Laplace inverting Eq. (5.45), or equivalently, by using Eq. (5.58) in
Eq. (5.47), to obtain
n1(t) = n0ρ0 jZ(iω)jsin(ωt + ϕ)
+ ω
X
j=0
esjt
(ω2 + s2
j )(dY=ds)sj
(5.60)
where ϕ is the phase angle, defined by
tan ϕ ≡ ImfZ(iω)g
RefZ(iω)g
(5.61)

<!-- page 158 (PDF 182) -->
The first term in Eq. (5.60) arises from the poles of the reactivity [Eq. (5.59)] at
s = ±iω, and the remaining terms arise from the poles of the zero-power transfer
function Z(s) [i.e., the roots of the inhour equation Y(s) = 0 given by Eq. (5.13)].
For a critical system, the largest root of the inhour equation is s = 0, so that after
sufficient time the solution given by Eq. (5.60) approaches
n1(t) ' n0ρ0 jZ(iω)jsin(ωt + ϕ) + 1
ωΛ

(5.62)
The average neutron detector response will be (ρ0/ωΛ)R0, where R0 is the
average detector response before the oscillation began. At high oscillation
frequency, the contribution of the first term in Eq. (5.62) to the detector response
will average to zero and the detector response will reflect the second term. In both
cases, this provides a means for the experimental determination of ρ0/Λ in terms
of the average detector response hRi:
ρ0
Λ = ω R
h i − R0
R0
(5.63)

### Zero-Power Transfer Function Measurements

By varying the frequency of rod oscillation, ω, the zero-power transfer function,
Z(iω), can be measured for a reactor or other critical fission chain-reacting system
by interpreting the detector reading R(t) as
R(t) − R0 = R0ρ0 jZ(iω)jsin(ωt + ϕ) + 1
ωΛ

(5.64)
Such measurements, when compared with calculation of the transfer function,
provide an indirect means of determining or confirming the parameters Λ, βi, and
λi. At low frequencies the amplitude of the transfer function approaches
jZ(iω)j ! ω
X
i=1
βi=β
λ2
i
(5.65)
for ω ≪λi, and the phase angle ϕ approaches
tan ϕ ! −
X
i=1
βi=β
λi
=ω
X
i=1
βi=β
λ2
i
(5.66)

### Rossi-α Measurement

The prompt neutron decay constant
α ≡ 1
n
dn
dt = k(1 − β) − 1
l
(5.67)

<!-- page 159 (PDF 183) -->
can be measured by observing the decay of individual fission reaction chains in
succession if the process is continued long enough to observe a statistically
significant number of decay chains. Assume that a neutron count from a decay
chain is observed at t = 0. The probability of another neutron count being
observed at a later time t is the sum of the probability of a count from a
chain-related neutron, Q exp(αt)Δt, plus the probability of a neutron from
another chain, CΔt, where C is the average counting rate:
P(t)dt = Cdt + Qeαtdt
(5.68)
We use a statistical argument to determine Q. The probability of a count
occurring at t0 is Fdt0, where F is just the average fission rate in the system. The
probability of another detector count at t1 > t0 that is chain related to the count at
t0 is
P(t1)dt1 = εvpv
X
f eα(t1−t0) dt1
(5.69)
where νp is the number of prompt neutrons per fission and ε is the detector
efficiency. The probability of a second chain-related count at t2 > t1 is
P(t2)dt2 = ε(vp − 1)v
X
f eα(t2−t0) dt2
(5.70)
where (νp − 1) takes account of the chain-related fission required to produce the
count at t1. The three probabilities Fdt0, P(t1)dt1, and P(t2)dt2 are treated as
independent probabilities. Hence, the probability for a count in dt1 followed by a
count in dt2, both in the chain that produced the count in dt0, is obtained by
multiplying the three probabilities and integrating over −1 < t < t1:
P(t1; t2)dt1dt2 = ∫
t1
−1
Fε2 v2
p − vp

v
X
f
eα(t1+t2−2t0)dt0dt1dt2
= Fε2 v2
p − vp
 vP
f
−2α
eα(t2−t1)dt1dt2
(5.71)
where an overbar indicates an average over the prompt neutron emission
distribution function.
Noting that νp = kpΣa/Σf = kp/(vlΣf) and including the probability F2ε2dt1dt2
of a random pair of counts, this becomes
P(t1; t2)dt1dt2 = F2ε2dt1dt2 + Fε2
v2
p − vp

k2
peα(t2−t1)dt1dt2
2v2
p(1 − kp)l
(5.72)
Since the overall probability of a count in dt1 is Fεdt1, we need to normalize this
conditional probability by division by Fεdt1, which yields, upon rescaling time
