# 11 Resonance Absorption — 11.5 Multiband Treatment of Spatially Dependent Self-Shielding … References
<!-- source PDF pages 468-487 -->

<!-- page 449 (PDF 468) -->
the overlapping fertile isotope sequence do not appear. With respect to
Eq. (11.64), the effect of the overlapping sequence i enters via the 1/Σt in
both the numerator and denominator and, to first order, these two effects
cancel.
Combining the self-overlap and different sequence overlap results, the effective
multigroup cross section for a fissile resonance sequence k with self-overlap and
with overlap by a fertile isotope resonance sequence i is
hσg
xki =
σp
P
spin
states
[(hΓxkJki=hDki) + P
k´hΓxkHkk´i=hDki]
1 □ P
spin
states
hΓkJki=hDki
(11.67)

## 11.5 Multiband Treatment of Spatially Dependent Self-Shielding

### Spatially Dependent Self-Shielding

Approximate methods for calculating effective multigroup cross sections for
resonance absorbing isotopes have been discussed in Sections 4.3 and 11.2. It
was found that the approximate flux to be used in evaluating the resonance
integral was of the form ϕ(E) ∼fss(Σt(E)) × M(E), where M(E) is a spectral
function with an energy dependence that would exist even in the absence of
the resonance absorber and fss is a self-shielding factor that depends on the
energy via the dependence of the total cross section on energy [e.g.,
f ss∼1=(Pres
t (E) + PM
s ) and M(E) ∼1/E in the narrow resonance approximation
for a homogeneous mixture given by Eq. (4.65)]. This same general form
persists in approximate treatments of heterogeneous resonance absorbers, as
may be seen from Eqs. (11.6) and (11.10).
In the approximate treatment of heterogeneous resonance absorbers discussed
in Section 11.2, the self-shielding factor, fss, and hence also the resulting
multigroup cross section, was implicitly assumed to be spatially independent
within the resonance absorber. However, simple physical considerations suggest
that the self-shielding will be much more pronounced deep within a
resonance absorber than on its surface, where the neutron spectrum is
dominated by neutrons entering from the adjacent moderator and, furthermore
, that the self-shielding near the surface will be different for neutrons
entering from the moderator than for neutrons coming from deeper within the
resonance absorber. Thus, even if accurate spatially constant multigroup cross
sections that preserve volume-averaged reaction rates are obtained for a
heterogeneous resonance absorber (e.g., a fuel pin), the spatial dependence
of reaction rates within the resonance absorber will not be calculated properly,
which will introduce an error into calculations of fuel depletion, fission heating
distribution, and so on. Even if the spatial multigroup flux distributions within

<!-- page 450 (PDF 469) -->
the resonance absorber are calculated with multigroup transport theory, there
will remain an inaccuracy in calculating the spatial distribution of reaction rates
because these spatially independent volume-averaged multigroup cross sections
were used instead of spatially dependent cross sections that take into
account the spatial dependence of the self-shielding.
The most straightforward way to solve this problem of spatially dependent
within-group self-shielding might seem to be to further subdivide the normal
multigroup structure (e.g., 20–50 groups) that would be used in a pin-cell
transport calculation (see Section 14.4) into ultrafine groups in the resonance
energy region. If the ultrafine groups could be sufficiently numerous that
the within-group self-shielding term was almost unity (i.e., such that the
variation of the cross section within any ultrafine group was small), the
ultrafine-group cross sections could be accurately calculated as previously
described, and the spatial self-shielding effect on the normal multigroup level
would be calculated on the ultrafine-group level. However, this procedure is
impractical except for special cases because each ultrafine-group width would
have to be narrow compared with the width of the resonances at that energy,
resulting in an enormous number of ultrafine groups to span the resonance
energy region. This approach would not work at all for the unresolved
resonances, of course.

### Multiband Theory

In the multiband method, each normal group is further subdivided, not into finer
energy intervals as in the ultrafine-group method discussed above, but into
intervals of the total cross section magnitude that span the variation in the total
cross section within the normal group. The multiband equations are derived by an
extension to the derivation of the multigroup equations. Starting with the energydependent
transport equation (with scattering and fission included in a general
transfer function),
Ω ? ∇Ψ(r; E; Ω) + Σt(r; E)Ψ(r; E; Ω)
= ∫
dE´
∫
4π
dΩ´Σs(r; E´ ! E; Ω´ ! Ω)Ψ(r; E´; Ω´)
(11.68)
the normal multigroup equations are formally derived by integrating over the
energy interval Eg < E < Eg□1:
Ω ? ∇Ψg(r; Ω) + Σg
t (r; Ω)Ψg(r; Ω)
=
X
G
g´=1∫
4π
dΩ´Σg´!g
s
(r; Ω´ ! Ω)Ψg´(r; Ω);
g = 1; . . . ; G
(11.69)

<!-- page 451 (PDF 470) -->
where
Ψg(r; Ω) ≡ ∫
Eg□1
Eg
dEΨg(r; E; Ω)
Σg
t (r; Ω) ≡ ∫
Eg□1
Eg
dEΣt(r; E)Ψ(r; E; Ω)=Ψg(r; Ω)
Σg´!g
s
(r; Ω´ ! Ω)
= ∫
Eg□1
Eg
dE∫
Eg´□1
Eg´
dE´Σs(r; E´ ! E; Ω´ ! Ω)Ψ(r; E´; Ω´)=Ψg´(r; Ω´);
g; g´ = 1; . . . ; G
(11.70)
The multiband equations are formally derived by a similar process, but now
with each group (g) energy interval subdivided into B cross section bands (g, b),
which span the range of total cross section in group g, as depicted in Fig. 11.6.
Defining a Heaviside function Hgb(E) that is unity for those energy intervals for
which the total cross section is within the band Σtb+1 □ Σt(E) □ Σtb and zero
elsewhere, the multiband equations are derived by first multiplying Eq. (11.68) by
ΣT5
ΣT4
ΣT3
ΣT (E)
ΣT2
ΣT1
Eg
E
Eg–1
Fig. 11.6 The Heaviside function Hgb=3 for the third band in a four-band representation of
the total cross section (Hsb=3 = 1.0 in dark energy intervals and = 0.0 elsewhere). (With
permission from Ref. [4]. Copyright 1986, CRC Press.)

<!-- page 452 (PDF 471) -->
Hgb(E) and then integrating over both the energy interval Eg ≤ E ≤ Eg□1 of group g
and over the total cross section range Σtb+1 □ Σt(E) □ Etb of band b:
Ω ? ∇Ψgb(r; Ω) + Σgb
t (r; Ω)Ψgb(r; Ω)
=
X
G
g´=1
X
B
b´=1∫
4π
dΩ´Σg´b´!gb
s
(r; Ω´ ! Ω)Ψg´b´(r; Ω´);
g; g´ = 1; . . . ; G;
b; b´ = 1; . . . ; B
(11.71)
where the multiband parameters are given by
Ψgb(r; Ω) ≡ ∫
Eg□1
Eg
dE∫
Σtgb+1
Σtgb
dΣ∗
t (E)Hgb(E)Ψ(r; E; Ω)
Σgb
t (r; Ω) ≡ ∫
Eg□1
Eg
dE∫
Σtgb+1
Σtgb
dΣ∗
t (E)Hgb(E)Σt(r; E)Ψ(r; E; Ω)=Ψgb(r; Ω)
Σg´b´!gb
s
(r; Ω´ ! Ω) ≡ ∫
Eg□1
Eg
dE∫
Eg´□1
Eg´
dE´
∫
Σtb+1
Σtb
dΣ∗
t (E)
□ ∫
Σtb´+1
Σtb´
dΣ∗
t (E´)Hgb(E)Hg´b´(E´)
□ Σs(r; E´ ! E; Ω´ ! Ω)Ψ(r; E´; Ω´)=Ψg´b´(r; Ω´)
(11.72)
with the quantity Σ∗
t normalized such that
X
B
b=1 ∫
Etb+1
Etb
dΣ∗
t (E) = 1
(11.73)
The normal multigroup quantities are related to the multiband quantities
within the different groups as
Ψg(r; Ω) =
X
B
b=1
Ψgb(r; Ω)
Σg
t (r; Ω) =
X
B
b=1
Σgb
t (r)Ψgb(r; Ω)
,X
B
b=1
Ψgb(r; Ω)
(11.74)

<!-- page 453 (PDF 472) -->
### Evaluation of Multiband Parameters

Directevaluationofthemultibandparametersfromtherelationshipsabove(actually
from the relationships that result when some discrete representation of the angular
dependence is invoked) is possible in principle, but these relationships may be recast
into a form that can make use of existing self-shielded multigroup libraries. The
definition of the normal multigroup cross section for process x as an integral over
energy can be exactly transformed into an integral over total cross section:
Σg
x ≡
∫
Eg□1
Eg
dEΣx(E)Ψ(E)
∫
Eg□1
Eg
dEΨ(E)
=
∫
Eg□1
Eg
dEΣx(E)M(E)f ss(E)
∫
Eg□1
Eg
dEM(E)f ss(E)
=
∫
Eg□1
Eg
dE PB
b=1 ∫
Σtb+1
Σtb
dΣ∗
t (E)Hgb(E)Σx(E)M(E)f ss(E)
∫
Eg□1
Eg
dE PB
b=1 ∫
Σtb+1
Σtb
dΣ∗
t (E)Hgb(E)M(E)f ss(E)
(11.75)
where use has been made of the approximate relationship ϕ(E) ∼M(E) fss(E)
discussed previously. Performing the integration over energy first and defining
P(Σ∗
t ) ≡
∫
Eg□1
Eg
dEHgb(E)M(E)
∫
Eg□1
Eg
dEM(E)
(11.76)
Σx(Σ∗
t ) ≡
∫
Eg□1
Eg
dEHgb(E)M(E)
∫
Eg□1
Eg
dEM(E)Hgb(E)
(11.77)
leads to the equivalent definition of the normal multigroup cross section:
Σg
x =
PB
b=1 ∫
Σtb+1
Σtb
dΣ∗
t Σx(Σ∗
t )f ss(Σ∗
t )p(Σ∗
t )
PB
b=1 ∫
Σtb+1
Σtb
dΣ∗
t f ss(Σ∗
t )p(Σ∗
t )
(11.78)
in terms of the total cross section probability distribution function p(Σ∗
t ), defined
such that p(Σ∗
t )dΣ∗
t is just the normalized probability of the total cross section
being within dΣ∗
t of Σ∗
t within the energy interval Eg ≤ E ≤ Eg□1.

<!-- page 454 (PDF 473) -->
For the practical evaluation of Eq. (11.78), average values of the cross sections
Σxb for process x in each band b are used to replace the integrals with quadratures:
Σg
x =
PB
b=1 Σgb
x f ss(Σ∗
tb)Pb
PB
b=1 f ss(Σ∗
tb)Pb
(11.79)
where
Pb ≡ ∫
Σtb+1
Σtb
p(Σ∗
t )dΣ∗
t
(11.80)
is the band weight. The computational advantage of this approach relative to a
direct quadrature approximation of the second form of Eq. (11.75) is that Σx(Σ∗
t ) is
generally a much smoother function than is Σx(E) over the resonance energy
range, so it is much easier to define an appropriate quadrature. Once the total
cross section probability distribution is evaluated, integrals involving this distribution
may be performed quite accurately and efficiently.

### Calculation of Multiband Parameters

Although it would be most straightforward to choose the band structure (Σt) a
priori and just evaluate the Pb and the various Σtb, it is more common to use a
moments method to calculate these multiband parameters to reproduce the
results obtained using certain limiting forms for the self-shielding. Using a
generalized self-shielding factor of the form
f ss(E) =
[Σt(E) + Σ0]n
(11.81)
the band parameters can be calculated by requiring that the multiband expression
agrees with the known results for various values of Σ0 and n. As an example, for two
bands, there are two weighting parameters (P1, P2) and for each reaction process x
two group-band cross sections (Σg1
x ; Σg2
x ) in each group. A normal multigroup
processing code will provide the unshielded [fss = 1 = 1/(Σt + Σ0)0], the totally selfshielded
flux-weighted [fss = 1/(Σt + Σ0)1], and sometimes the totally self-shielded
current-weighted [fss = 1/(Σt + Σ0)2] values of the various cross sections in group g,
(Σg
x)0, (Σg
x)1, and (Σg
x)2, respectively. Requiring that Eq. (11.79) yields these three
values of the total cross section and realizing that P1 + P2 = 1 yields four equations
from which the band parameters can be calculated. It is necessary to introduce the
ordering Σt1 < Σt2 in order to obtain a unique solution, since the two bands are
otherwise indistinguishable. The solutions are
P1=2 = 1
2 − δ;
Σt1=2 =
A − B
(11.82)

<!-- page 455 (PDF 474) -->
where
δ
≡ 1 □ A(Σg
t )1
2B(Σg
t )1
A
≡
2(Σg
t )2
(Σg
t )0 □ (Σg
t )2
(Σg
t )0 □ (Σg
t )1
B2 ≡
(Σg
t )0(Σg
t )1
1 □ 2A(Σg
t )1 + (Σg
t )0(Σg
t )1A2
(11.83)
Having thus determined (P1, P2, Σg1
t , and Σg2
t ), the group-band cross sections for
the individual processes x, (Σg1
x ; Σg2
x ) can then be determined by requiring that Eq.
(11.79) yields the unshielded [fss = 1 = 1/(Σt + Σ0)0] and the totally shielded fluxweighted
[fss = 1/(Σt + Σ0)1] cross sections (Σx)0 and (Σg
x)1, respectively, which
yields
Σg2=1
x
= (Σg
x)0 − C
P1
;
C = (Σg
x)0 □ (Σg
x)1
 P1=Σg1
t + P2=Σg2
t
1=Σg1
t □ 1=Σg2
t
(11.84)
This general procedure may be extended to more bands. In practice, it has been
found that two to four bands are sufficient.
The scattering transfer rate from group g´ to group g in the normal multigroup
theory depends on the scattering cross section in group g´, Σg´
s , and on the transfer
probability, Tg´→g, that a neutron scattered in group g´ will have final energy in
group g (i.e., Σg´!g
s
= Σg´
s Tg´!g). The transfer probability does not depend on the
scattering cross section in either group g´ or group g. The usual procedure for
constructing the group band g´b´ to group band gb scattering transfer rate is to
replace Σg´
s with Σg´b´
s
and to assume that the transfer probability from group band
g´b´ to group band gb is just the group g´ to group g transfer probability times the
weight Pg
b of band b in group g (i.e., Σg´b´!gb
s
= Σg´b´
s
Tg´!gPg
b). Various extensions of
this definition of the group-band scattering transfer probability have been
suggested, but its calculation remains heuristic.

### Interface Conditions

The interface–boundary conditions for multiband transport theory remain
somewhat heuristic as well. Clearly, the continuity of directional group-flux
condition requires that
X
B
b=1
Ψgb(□s; Ω) ≡ Ψg(□s; Ω) = Ψg(s; Ω) ≡
X
B
b=1
Ψgb(s; Ω)
(11.85)
where ±s refers to the + and □ sides of the interface at r = s. The argument that the
cross sections are not correlated across an interface between dissimilar media is

<!-- page 456 (PDF 475) -->
used to justify the distribution of directional group fluxes crossing an interface
from □ to + side according to the weights on the + side:
Ψgb(+s; Ω) = Pg+
b Ψg(□s; Ω) = Pg+
b
X
B
b´=1
Ψgb´(□s; Ω)
(11.86)

## 11.6 Resonance Cross Section Representations∗

### R-Matrix Representation

The quantum mechanical representation of reaction cross sections is given
most generally by R-matrix theory, in which the reaction cross section for any
incident channel c and exit channel c´ is generally expressed in terms of the
collision matrix Ucc´:
σcc´ = πλ2gcjδcc´ □ Ucc´j
(11.87)
where gc and Scc´ are the statistical factor and the Kronecker delta, respectively.
The unitary property of Ucc´ leads to the expression of the total cross section as a
linear function of Ucc´:
σt =
X
c´
σcc´ = 2πλ2gc(l □ RefUccg)
(11.88)
The collision matrix, in turn, can be expressed in terms of the resonance
parameter matrix R according to Wigner and Eisenbud:
Ucc´ = exp[□i(ϕc + ϕc´)]fδcc´ + iP1=2
c
[(I □ RL0)□1R]cc´P1=2
c´ g
(11.89)
where
Rcc´ =
X
λ
γλcγλc´
Eλ □ E
(11.90)
is a real symmetric matrix and
L0
cc´ = (Sc □ Bc + iPc)δcc´
(11.91)
The energy-independent parameters Eλ, γλc, and Bc denote the R-matrix state,
reduced width amplitude and arbitrary boundary parameters, respectively. Of all
parameters given above, ϕc, Sc, and Pc are momentum dependent for the elastic
scattering channels only. ϕc, the hard-sphere phase shift factor, is related directly
∗This section was prepared with the extensive collaboration of R. N. Hwang.

<!-- page 457 (PDF 476) -->
to the argument of the outgoing wavefunction at the channel radius, whereas Sc,
the shift factor, and Pc, the penetration factor, reflect the real and imaginary parts
of its logarithmic derivative, respectively, as defined in Table 11.3. These
quantities, along with the matrix R, specify the explicit energy dependence of
the cross section. It should be noted that the matrix R is primarily responsible for
the sharp rise in cross section at the energy near the resonance energy, Eλ, while
the other energy-dependent quantities are relatively smooth by comparison. All
energy-independent quantities given above are, in principle, determined by the
fitting of the experimental data.
An alternative expression for the collision matrix is the equivalent level matrix
representation derived by Wigner, which can provide more analytical insight for
the discussions to follow. It is given as
Ucc´ = e□i(ϕc+ϕc´)
δcc´ + i
X
λ;μ
Γ1=2
λc AλμΓ1=2
μc´
!
(11.92)
where the level matrix A is defined as
(A□1)λc = (Eλ □ E)δλμ □
X
c
γλcL0
cγμc;
Γ1=2
λc =
ffiffiffiffiffiffiffi
2Pc
p
γλc
(11.93)
This expression provides a clearer picture of the explicit energy dependence of the
collision matrix.

### Practical Formulations

Although the formal R-matrix representation is rigorous on theoretical grounds,
it is quite obvious that simplifications are required before its deployment as the
basis for nuclear data evaluations and subsequent use in reactor applications. In
Table 11.3 Momentum-Dependent Factors for Various l-States Defined at Channel Radius rc
(ρ = krc)
Factors
l = 0
l = 1
l = 2
l = 3
Pl
ρ
ρ3
1 + ρ2
ρ5
9 + 3ρ2 + ρ4
ρ7
225 + 45ρ2 + 6ρ4 + ρ6
Sl
□1
1 + ρ2
□(18 + 3ρ2)
9 + 3ρ2 + ρ4
□(675 + 91ρ2 + 6ρ4)
225 + 45ρ2 + 6ρ4 + ρ6
ϕl
ρ
ρ □ tan□1 ρ
ρ □ tan□1
3ρ
3 □ ρ2
ρ □ tan□1 ρ(15 □ ρ2)
15 □ 6ρ2
Source: Data from Ref. [5]; used with permission of Institute for Nuclear Research and Nuclear Energy,
Sofia.

<!-- page 458 (PDF 477) -->
the current ENDF/B format, four major formalisms pertinent to the treatment of
the resonance absorption are allowed: the single-level Breit–Wigner (SLBW),
multilevel Breit–Wigner (MLBW), Adler–Adler (AA), and Reich–Moore (RM)
formalisms. These formalisms are based on approximations of the formal R-
matrix theory to various degrees of sophistication.
With exception of the Reich–Moore formalism, all these formalisms exhibit a
similar form as a function of energy and can be considered as the consequences of
various approximations of the Wigner level matrix. It is convenient to cast them
into the pole expansion form in either the energy or momentum domain (kplane
). A simple generic form that is widely used in reactor physics is
σx = 1
E
X
l;J
X
λ
Re
ρ(x)
l;J;λ
□i
ffiffiffi
E
p
dλ □ E
(
)
(energy domain)
= 1
E
X
l;J
X
λ
Re
ρ(x)
l;J;λ
□i
ffiffiffiffiffi
dλ
p
□
ffiffiffi
E
p
□
□i
ffiffiffiffi
dλ
p
+
ffiffiffi
E
p
!
(
)
(momentum domain)
(11.94)
where the superscript x denotes the type of reaction under consideration. The
superscripts f, γ, and R will be used to denote fission, capture, and compound
nucleus (or total resonance) cross sections, respectively. Physically, each term
retains the general features of a Breit–Wigner resonance upon which the
traditional resonance integral concept was based. The relationships between
these pole and residue parameters and the traditional resonance parameters for
three of the major formalism are tabulated in Table 11.4. The use of complex
arithmetic here makes possible a direct comparison of these traditional
Table 11.4 Poles and Residues for Traditional Formalism
Formalism
Poles, dλ
Residues, ρ(x)
l;j;λ
SLBW
E0λ □ iΓlλ
cgJ
ΓxλΓnλ
Γtλ=2
1ffiffiffi
E
p ;
x ∈
(
f ; γg CgJ2Γnλ
1ffiffiffi
E
p exp(□i2ϕl);
x ∈R
MLBW
Same as
above
Same as above if x ∈{f, γ}
CgJ2Γnλ
1ffiffiffi
E
p
exp(□i2ϕl) + W λ´
;
x ∈R
where W λ´ = P
λ´ ≠λ
iΓnλ´
(Eλ □ Eλ´) + i[Γtλ + Γtλ´)=2]
Adler–
Adler
μλ □ ivλ
CgJ[G(x)
λ + iH(x)
λ ]; x ∈ff ; γg
CgJexp(□i2ϕl)[G(x)
λ + iH(x)]; x ∈R
Source: Data from Ref. [5]; used with permission of Institute for Nuclear Research and Nuclear Energy,
Sofia.

<!-- page 459 (PDF 478) -->
formalisms to the rigorous pole representation to be discussed later. ρ(x)
l;J;λ
however, are different and depend on the approximations assumed.
Single-Level Breit–Wigner Approximation (SLBW)
The SLBW approximation represents the limiting case when the resonances are
well separated from each other. Thus, the level matrix A at a given E can be viewed
as a matrix with only one element. In much of the previous discussion, the
resonance integrals were also treated in this approximation. In reality, the
resonance cross sections clearly cannot be taken as a disjoint set of isolated
resonances in a rigorous treatment. Ambiguity can arise as to what constitutes the
macroscopic cross sections in a detailed treatment of the neutron slowing-down
problem over an energy span consisting of many resonances of more than one
nuclide. For this reason, the single-level description used in practical applications
such as that specified in the ENDF/B manual is often given in the context of
Eq. (11.92) as a linear combination of Breit–Wigner terms supplemented by the
tabulated pointwise smooth data so that the continuous nature of the cross
sections, and thus the flux, can be preserved.
Multilevel Breit–Wigner Approximation (MLBW)
The MLBW approximation corresponds to the situation in which the inverse of
the level matrix is taken to be diagonal. One constraint for SLBW and MLBW
approximations of practical interest is that all parameters must be positive. It is
worth noting that poles and residues are energy dependent, although in many
applications they are taken to be energy independent. Otherwise, additional terms
in the
ffiffiffi
E
p
-domain would result in all l>0 sequences using SLBW and MLBW
formalism.
It should be noted that, strictly speaking, the amplitude ρ(x)
l;J;λ and the pole dλ are
also energy dependent for the single-level Breit–Wigner and multilevel Breit–
Wigner approximations if the explicit energy dependence of the penetration factor
andthelevel-shift factorare considered forall l > 1 states.In reference totheENDF/
B manual, the amplitude of an individual resonance is proportional to the
penetration factor, while the real part of dλ is identifiable as
dλ = E´
λ = Eλ + Sl(jEλj) □ Sl(E)
2Pl(jEλj)
Γnλ(jEλj)
The latter is equivalent to assuming that the boundary parameter is set to be
Bl = Sl(|Eλ|). Thus, the rational function nature of Pl(ρ) and Sl(ρ) defined in
Table 11.3 can lead to 2(l + 1) pole terms for each resonance in the momentum
domain, instead of two terms. The absolute values of the additional 2l poles are
generally large compared with those two, resulting from the line shape function
directly, so as to reflect the relatively smooth nature of the energy dependence of
the penetration factor and the level shift factor. The inclusion of these secondary
energy effects can readily be added within the context of the generalized pole
representation to be described (Ref. [6]).

<!-- page 460 (PDF 479) -->
Adler–Adler Approximation (A–A)
The diagonalization of the inverse level matrix A□1 leads directly to the pole
expansion defined by Eq. (11.92). The Adler–Adler approximation is equivalent to
theKapur–Peierlsrepresentation,inwhichthepolesandresiduesare assumedtobe
energy independent. In the context of the forgoing discussion, it is equivalent to
assuming the energy independence of L0 of Eq. (11.91) when the inverse of A□1 is
considered. The approximation is usually restricted to the s-wave sequences of the
fissionable isotopes in the low-energy region, where the assumption is valid.
Reich–Moore Formalism
For practical applications, the formal R-matrix representation is obviously
difficult to use when many levels and channels are present. The problem has
been simplified significantly by the method proposed by Reich and Moore. The
only significant assumption required, in principle, is
X
c ∈γ
γλcL0
cc´γμc´ = δλμ
X
c ∈γ
γ2
λcL0
c
(11.95)
which utilizes thepresence of the large numberof capture channels andthe random
sign of γλc. It is consistent with the observed fact that the total capture width
distribution is generally very narrow. If one partitions the collision matrix into a
2 × 2blockmatrixarrangedsuchthattheupperandlowerdiagonalblocksconsistof
only noncapture and capture channels, respectively, and utilizes Eq. (11.95) as well
as Wigner’s identity between the channel matrix and the level matrix, the collision
matrix can be reduced to the order of m × m where m is the total number of
noncapture channels. The reduced collision matrix remains in the same form
except that the real matrix R is replaced by a complex matrix R´ with elements
R´
cc´ =
X
λ
γλcγλc´
Eλ □ E □ iΓλγ=2
(11.96)
The substitution of the reduced R-matrix into the original equation leads to the
following general form of collision matrix expression for the Reich–Moore
approximation in terms of the familiar notations commonly used in applications:
U(E) = e□iφ(I + 2Y)e□iφ
(11.97)
where
Y = iP1=2(I □ R^L)□1RP1=2 = F□1[(I □ iFK)□1 □ I]
(11.98)
K = (L0)1=2R(L0)1=2;
F = I □ i^SP□1
(11.99)
and ^S = S(E) □ B.

<!-- page 461 (PDF 480) -->
It should be noted that the traditional Reich–Moore representation currently
specified by the ENDF/B manual was originally developed for applications in the
relatively low-energy regions. It is different from the general form given above
because two additional assumptions were introduced. First, ^S is taken to be zero.
The rationale is based on the fact that lim St(E) = □l, implied by the rational
functions listed in Table 11.3. Thus, by taking limE→0 Bc = □l, the quantity ^Sl = 0
and the level shift factor will not play a role in the low-energy region. Second, one
elastic scattering channel is allowed in the channel matrix K. Although the
assumption simplifies the computation required, the issue may still arise for
nuclides with odd atomic weight, for which the multiple elastic channels still may
play a role. All evaluated resonance data given in the ENDF/B-VI to date are based
on these assumptions.
One consequence of the Reich–Moore approximation is that the reduced
collision matrix is no longer unitary because Rl
cc´ is complex. For practical
applications, this presents no problem since the total cross section can be preserved
if the capture cross section is defined as
σγ = σt □
X
c´γ
σcc´
(11.100)
All parameters retain the physical as well as the statistical properties specified
by the formal R-matrix theory. The order of the channel matrix is usually no
greater than 3 × 3. Hence the method is attractive for data evaluations, and in
fact, Reich–Moore parameters have become widely available in the new ENDF/
B-VI data.
However, unlike the other three formalisms, resonances defined by the Reich–
Moore formalism can no longer be perceived in the context upon which the
traditional resonance theory in reactor physics was based. The direct application
of this formalism to reactor calculations not only requires the entry of excessive
files of precomputed, numerically Doppler-broadened pointwise cross sections at
various temperatures, but also renders useless many well-established methods
based on the resonance integral concept. Hence there is strong motivation to seek
remedies so that the newly released Reich–Moore parameters can be fully utilized
within the framework of the existing methodologies.

### Generalization of the Pole Representation

Although any given set of R-matrix parameters, including those in the Reich–
Moore form, can be numerically converted into parameters of the Kapur–
Peierls type, the parameters so obtained are implicitly energy dependent. With
the exception of low-lying resonances of a few fissionable isotopes, such
dependence is generally not negligible. Thus, from the practical point of
view, the traditional pole expansion is not useful for most nuclides of interest.
However, a desirable representation directly compatible with the traditional
forms given by Eq. (11.94) can be derived if the pole expansion is cast into a
somewhat different form.

<!-- page 462 (PDF 481) -->
Rigorous Pole Representation
One attractive means to preserve the rigor of the R-matrix description of cross
sections is to perform the pole expansion in the k-plane (or momentum domain).
Such a representation is natural for the SLBW, MLBW, and Adler–Adler
approximations. The theoretical justification of such a representation is based
on the rationale that the collision matrix must be single valued and meromorphic
in the momentum domain. Any function that exhibits such properties must be a
rational function according to a well-known theorem in complex analysis. The
rational function characteristics are quite apparent if one examines the explicit
ffiffiffi
E
p
-dependence of the collision matrix Ucc´ defined by Eq. (11.89), if the level
matrix is expressed as the ratio of the cofactor and the determinant of its inverse.
By substituting Sl and Pl into Eq. (11.89) or (11.92), the quantity Ucc´ is expressible
in terms of a rational function of order 2(N + l), where N is the total number of
resonances. This reflects the polynomial nature of the cofactor and the determinant
of the inverse level matrix. Thus, one obtains via partial fractions the similar
pole representation for other approximations. A general expression that can be
used with all cross section representations is
σt = σp + 1
E
X
l;J
X
M
λ=1
X
jj
j=1
Re
R(t)
l;J;j;λe□i2ϕ1
h
i
?
□i
p(j)∗
λ
□
ffiffiffi
E
p
(
)
(11.101)
and similarly,
σx = 1
E
X
l;J
X
M
λ=1
X
jj
j=1
Re
R(x)
l;J;j;λ
□i
p(j)∗
λ
□
ffiffiffi
E
p
(
)
(11.102)
for the reaction cross section of process x, where R(x)
l;J;j;λand p(j)
λ
are pole and
residue, respectively. Note that the complex conjugate p(j)∗
λ
is used here in order to
cast the expressions into the form defined by Eq. (11.92). These equations can be
viewed as the generalized pole expansion in which all parameters are truly energy
independent and the energy dependence of the cross sections is specified
explicitly by the rational terms alone.
The indices M and jj depend on the type of resonance parameters and
assumptions used to generate these pole parameters:

## □ Adler–Adler: M = N (total number of resonance); jj = 2. All pole parameters can

be deduced directly via partial fractions.

## □ SLBW and MLBW: M = N; jj = 2 if penetration factor and level shift factor are

taken to be energy independent, an assumption used in the traditional resonance
integral approach. Otherwise, M = N; jj = 2(l + 1) if all energy-dependent
features are included.

## □ Reich–Moore: M = N + l; jj = 2 for both scenarios with ^Sl(E) = 0 and ^Sl(E) ≠0 if

Eq. (11.98) is used. Another possible scenario is to keep the traditional
expression specified by the ENDF/B manual intact; that is, let F = I in

<!-- page 463 (PDF 482) -->
Eq. (11.98), but to introduce the level shift factor via replacing the resonance
energy Eλ with
E´
λ = Eλ + Sl(jEλj) □ Sl(E)
2Pl(jEλj)
Γnλ(jEλj)
the same as for the SLBW and MLBW approximations. The resulting number of
poles becomes M = N; jj = 2(l + 1).
By comparing Eqs. (11.94) and (11.101), one is led to the following observations: (1)
For the s-wave, both the rigorous pole representation and the traditional formalism
consist of an identical number of terms with the same functional form in the
momentum domain. In particular, the Adler–Adler formalism for the s-wave can
be considered as the special case of the former when p(1)
λ
= □p(2)
λ and R(x)
l;J;1;λ = R(x)
l;J;2;λ.
(2)Forhigherangularmomentumstates,Eq.(11.101) consistsofeither2lor2lNmore
terms than those defined by Eq. (11.94). The difference, however, is only superficial.
The same number of terms would have resulted if the detailed energy dependence of
the penetration factor and the shift factor had been included in Eq. (11.94).
Equations (11.101) and (11.102) provide the basis whereby any given set of R-
matrix parameters, in principle, can be converted into pole parameters, although
it may not be an easy task in practice. The recent availability of R-matrix
parameters in the Reich–Moore form greatly alleviates the numerical difficulties
for such a conversion process. One obvious disadvantage of this method is that
two to as many as 2(l + 1) terms must be considered for each resonance if the
cross section is to be evaluated in the momentum domain. This is obviously
undesirable for computing efficiency, storage requirement, and its amenability to
the existing codes for reactor calculations.
Simplified Pole Representation
The Mxjj poles for a given l and J defined in Eqs. (11.101) and (11.102) can be
divided into two distinct classes. There are 2N s-wavelike poles with sharp peaks
and distinct spacings, while the remaining 2l or 2lN poles are closely spaced and
are characterized by their extremely large imaginary components (or widths). In
fact, the contributions of the latter to the sums are practically without any
resonance-like fluctuations, as if they were a smooth constituent. On the other
hand, the s-wavelike poles always appear in pairs with opposite signs but not
necessarily with the same magnitude. These characteristics provide a valuable
basis for simplification.
Let q(x)
l (
ffiffiffi
E
p
) denote the contributions from those additional 2l or 2lN terms
involving poles with giant width. Equation (11.102) can be cast into the same form
as that of Humblet–Rosenfeld:
σx = 1
E
X
l
Re
X
J
X
n
λ=1
R(x)
l;J;j;λ
2(□i)
ffiffiffi
E
p
(p(1)∗
λ
)2 □ E
"
+ s(x)
l (
ffiffiffi
E
p
)
(
+ q(x)
l (
ffiffiffi
E
p
) ? δl
)
;
ffiffiffi
E
p
> 0
(11.103)

<!-- page 464 (PDF 483) -->
where
s(x)
l (
ffiffiffi
E
p
) =
X
J
X
N
λ=1
R(x)
l;J;2;λ(□i)
p(2)∗
λ
□
ffiffiffi
E
p
□
R(x)
l;J;1;λ(□i)
p(1)∗
λ
□
ffiffiffi
E
p
"
(11.104)
and δ0 = 0 and δl = 1 for l > 0. The quantity s(x)
l (
ffiffiffi
E
p
), physically signifying a
measure of deviation from the Adler–Adler limit of p(2)∗
λ
= □p(1)∗
λ
, is usually not
only small in magnitude but also smooth as a function of energy in the region
where the calculations take place. Thus, s(x)
l (
ffiffiffi
E
p
) and q(x)
l (
ffiffiffi
E
p
) can be construed
as the energy-dependent smooth term in the Humblet–Rosenfeld representation
with its energy dependence explicitly specified.
Hence, for a given range of practical interest, the rigorous pole representation
can be viewed as a combination of fluctuating terms, consisting of N poles with
Refp(1)
λ g > 0 expressed in the energy domain consistent with the traditional
formalism and two nonfluctuating (or background) terms attributed to the tails of
outlying poles (in reference to the domain
ffiffiffi
E
p
> 0, where calculations are to take
place) with negative real component and the poles with extremely large width (or
jImfp(j)
λ gj) for l>0 states, respectively. The striking behavior of the fluctuating and
nonfluctuating components has been confirmed in recent calculations for all
major nuclei specified by the Reich–Moore parameters in the ENDF/B VI files.
The smooth behavior of these terms clearly suggests that their energy dependence
can be reproduced by other, simpler functions within the finite interval of
practical interest. It is well known in numerical analysis that the rational functions
are best suited to approximate a well-behaved function within a finite range.
Hence, the obvious choice is to set the approximate functions ^s(x)
l (
ffiffiffi
E
p
) and
^q(x)
l (
ffiffiffi
E
p
) to be rational functions of arbitrary order. Mathematically, they can be
viewed as the analytic continuations of the original functions ^s(x)
l (
ffiffiffi
E
p
) and
^q(x)
l (
ffiffiffi
E
p
) within domain
ffiffiffi
E
p
> 0. One attractive feature of the method proposed
is that the rational functions so obtained can be again expressed in the form of a
pole expansion via partial fraction, that is,
^s(x)
l (
ffiffiffi
E
p
) = PMM(
ffiffiffi
E
p
)
QNN(
ffiffiffi
E
p
)
=
X
NN
λ=1
r(x)
λ (□i)
α∗
λ □
ffiffiffi
E
p
(11.105)
^q(x)
l (
ffiffiffi
E
p
) =
X
NN
λ=1
b(x)
λ (□i)
ξ∗
λ □
ffiffiffi
E
p
(11.106)
if N N > M M:α∗
λ and ξ∗
λ are the poles of the fitted rational functions (i.e., the ratio
of the two low-order polynomials) for ^s(x)
l (
ffiffiffi
E
p
) and ^q(x)
l (
ffiffiffi
E
p
), respectively, while
r(x)
λ
and ξ(x)
λ
are their corresponding residues.

### Doppler Broadening of the Generalized Pole Representation

Either one of two approaches are usually taken, depending on the accuracy
required. The rigorous broadening must be carried out in the momentum

<!-- page 465 (PDF 484) -->
domain, whereas the simplified broadening is based on the approximate kernel in
the energy domain. In the following discussions, the Doppler-broadened cross
section based on the traditional formalism and the generalized pole representation
are compared.
Exact Doppler Broadening
The Maxwell–Boltzmann kernel can be expressed rigorously as
S(
ffiffiffi
E
p
;
ffiffiffiffi
E´
p
) =
ffiffiffiffi
E´
p
(πE)1=2Δm
exp □ (
ffiffiffi
E
p
□
ffiffiffiffi
E´
p
)2
Δ2
m
"
(
□ exp □ (
ffiffiffi
E
p
+
ffiffiffiffi
E´
p
)2
Δ2
m
"
#)
(11.107)
where
Δm =
ffiffiffiffiffiffi
kT
A
r
= Doppler width in momentum space
(11.108)
The Doppler broadening of
ffiffiffiffi
E´
p
σx(
ffiffiffiffi
E´
p
) defined by Eq. (11.94) in momentum
space and that defined by Eq. (11.102) lead immediately to:

## □ Traditional representation:

σx(
ffiffiffi
E
p
; τ) = 1
E
X
l;J
X
N
λ=1
Re
ρ(x)
l;J;λ
ffiffiffi
π
p
Δm
W
ffiffiffi
E
p
□ ζλ
Δ2
m
!
"
(
□ W ∗
ffiffiffi
E
p
+ ζ∗
λ
Δm
!#)
(11.109)

## □ Generalized pole representation:

σx(
ffiffiffi
E
p
; T) = 1
E
X
l
Re
X
J
X
N
λ=1
X
j=1
R(x)
l;J;λ;j
ffiffiffi
π
p
Δm
W
ffiffiffi
E
p
□ p(j)∗
λ
Δm
!
"
(
+^s(x)
l (
ffiffiffi
E
p
; τ) + q(x)
l (
ffiffiffi
E
p
)δl
)
(11.110)
where ^q(x)
l (
ffiffiffi
E
p
) is insensitive to Doppler broadening and
^s(x)
l (
ffiffiffi
E
p
; τ) =
X
NN
k=1
r(x)
k
ffiffiffi
π
p
Δm
W
ffiffiffi
E
p
□ α∗
k
Δm
!
"
(11.111)

<!-- page 466 (PDF 485) -->
and W(z) is the complex probability integral and is directly related to the usual
Doppler-broadened line shape functions via the relation
W(z) = i
π ∫
□1
e□t2
z □ t dt
(11.112)
ψ(x; y) + iχ(x; y) =
ffiffiffi
π
p
yW(z)
(11.113)
and z = x + iy.
In the single-level limit, Eq. (11.109) is equivalent to the generalized form of
the exact Doppler broadening defined by Ishiguro. Thus, except for the
superficial difference leading to the smooth term ^q(x)
l (
ffiffiffi
E
p
)δl, Eqs. (11.109)
and (11.110) have the same functional form but are characterized by different
parameters. From a practical point of view, the computational requirements for
these equations are expected to be comparable if the smooth term is replaced
by the approximation defined by Eqs. (11.100) and (11.101).
Approximate Doppler Broadening
For most of the existing codes based on the traditional formalism, the Doppler
broadening is generally based on the approximate Gauss kernel defined in the
energy domain
M(Eλ □ E) =
1ffiffiffi
π
p
ΔE
exp (Eλ □ E)2
ΔE

(11.114)
where ΔE =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
4kTE=A
p
is the Doppler width in the energy domain.
The validity of such an approximation requires the criterion E ⋙Δm. It has been
well established that the use of the Gauss kernel in the energy domain is generally
satisfactory for E > 1 eV. The Doppler-broadened cross sections become:

## □ Traditional formalism:

σx(E; T) = 1
E
X
l:J
X
N
λ=1
Re
ffiffiffi
E
p
ρ(x)
l;J;λ
ffiffiffi
π
p
ΔE
W
E □ dλ
ΔE

(
)
(11.115)

## □ Generalized pole representation after simplification:

σx(E; T) = 1
E
X
l
Re
X
J
X
N
λ=1
ffiffiffi
E
p
R(x)
l;J;1;λ
ffiffiffi
π
p
ΔE
W
E □ ελ
ΔE

(
+ ^s(x)
l (
ffiffiffi
E
p
; T) + ^q(x)
l (
ffiffiffi
E
p
)δl
)
(11.116)
where
ελ = [p(1)∗
λ
]2
(11.117)

<!-- page 467 (PDF 486) -->
## References

1 A. G. CROFF, ORIGEN2: A Revised and Updated Version of the Oak Ridge Isotope
Generation and Depletion Code, ORNL-5621, Oak Ridge National Laboratory,
Oak Ridge, TN (1980).
2 H. H. HUMMEL and D. OKRENT, Reactivity Coefficients in Large Fast Power
Reactors, American Nuclear Society, La Grange Park, IL (1970).
3 R. B. NICHOLSON and E. A. FISCHER, “The Doppler Effect in Fast Reactors,” in
Advances in Nuclear Science and Technology, Academic Press, New York (1968).
4 D. E. CULLEN, “Nuclear Cross Section Preparation,” in Y. RONEN, ed., CRC
Handbook of Nuclear Reactor Calculations I, CRC Press, Boca Raton, FL (1986).
5 R. N. HWANG, “An Overview of the Current Status of Resonance Theory in
Reactor Physics Applications,” in W. AUDREJTSCHEFF and D. ELENKOV, eds., Proc.
11th Int. School Nuclear Physics, Neutron Physics, and Nuclear Energy, Institute
for Nuclear Research and Nuclear Energy, Sofia, Bulgaria (1993).
6 C. JAMMES and R. N. HWANG, “Conversion of Single- and Multi-Level Breit–
Wigner Resonance Parameters to Pole Representation Parameters,” Nucl. Sci.
Eng. 134, 37 (2000).

## Further Reading

BELL G. I., Nuclear Reactor Theory, Van Nostrand Reinhold, New York (1970),
Chap. 8.
DRESNER L., Resonance Absorption in Nuclear Reactors, Pergamon Press, Elmsford,
NY (1960).
DUDERSTADT J. J. and HAMILTON L. J., Nuclear Reactor Analysis, Wiley, New York
(1976), Chaps. 2 and 8.
HENRY A. F., Nuclear-Reactor Analysis, MIT Press, Cambridge, MA (1975), Chap. 5.
HWANG R. N., “Doppler Effect Calculations with Interference Corrections,” Nucl. Sci.
Eng. 21, 523 (1965).
NORDHEIM L. W., “The Doppler Coefficient,” in THOMPSON T. J. and BECKERLEY J. G.,
eds., The Technology of Nuclear Reactor Safety, MIT Press, Cambridge, MA
(1964).
ROTHENSTEIN W. and SEGEV M., “Unit Cell Calculations,” in RONEN Y., ed., CRC
Handbook of Nuclear Reactor Calculations I, CRC Press, Boca Raton, FL (1986).
SAUER A., “Approximate Escape Probabilities,” Nucl. Sci. Eng. 16, 329 (1963).

## Problems

11.1 Carry through the steps indicated to derive the narrow resonance
approximation flux of Eq. (11.6) and the wide resonance approximation
flux of Eq. (11.10).
11.2 A fuel assembly in a reactor consists of a uniform array of fuel pins 1 cm in
diameter set in parallel rows such that the center-to-center separation

<!-- page 468 (PDF 487) -->
between adjacent rows is 3 cm in both ways. The fuel is 2.8% enriched
UO2 operating at 800 °C. The moderator is H2O at 0.85 g/cm3. Calculate
the heterogeneous resonance integral in the narrow resonance and the
wide resonance approximations for the 238U resonance at 36.8 eV, in the
isolated fuel rod approximation.
11.3 Repeat Problem 11.2 taking into account the Dancoff correction for a
closely packed square lattice.
11.4 Assume that the fuel and moderator in Problem 11.2 are mixed homogeneously
together. Calculate the homogeneous resonance integral for the
238U resonance at 36.8 eV at 800 °C.
11.5 Calculate the contribution of the 238U resonance at 36.8 eV to the
multigroup cross section of a group with Eg = 10 eV and Eg□1 = 100 eV,
for Problems 11.2–11.4.
11.6 Repeat Problem 11.2 for D2O moderator. Calculate the contribution to
the multigroup cross section over Eg = 10 eV to Eg□1 = 100 eV.
11.7 Compare the calculated escape probability for a fuel plate immersed in
water for values of λ/ls in the range 0.1 ≤ λ/ls ≤ 10.0, using the exact
expression of Eq. (11.32) and the rational approximation of Eq. (11.43).
11.8 Derive the first-flight escape probability for neutrons created uniformly
over a slab of thickness a given by Eq. (11.32).
11.9 Write a code to calculate the unresolved 238U multigroup capture cross
section of Eq. (11.62) for a group extending from Eg = 1 keV to
Eg□1 = 10 keV.
11.10 Evaluate the two-band group absorption cross section for a group
extending from Eg = 10 eV to Eg□1 = 100 eV for a nuclide for which the
absorption and total cross sections are Σa1 = 0.4 cm□1 and Σt1 = 0.5 cm□1
from 10 ≤ E ≤ 50 eV and are Σa2 = 0. 6 cm□1 and Σt2 = 0. 8 cm□1 from
50 eV ≤ E ≤ 100 eV.
