# 11 Resonance Absorption — 11.1 Resonance Cross Sections … 11.4 Unresolved Resonances
<!-- source PDF pages 448-467 -->

<!-- page 429 (PDF 448) -->
# 11 Resonance Absorption

## 11.1 Resonance Cross Sections

When the relative (center-of-mass) energy of an incident neutron and a
nucleus plus the neutron binding energy match an energy level of the
compound nucleus that would be formed upon neutron capture, the probability
of neutron absorption is quite large. For the odd-mass fissionable fuel
isotopes, resonances occur from a fraction of 1 eV up to a few thousand
electron volts, and for the even-mass fuel isotopes, resonances occur from a
few electron volts to about 10,000 eV, as shown in Figs. 11.1–11.4. At the lower
energies the resonances are well separated, but at the higher energies the
resonances overlap and become unresolvable experimentally. We first examine
the widely spaced resonances at lower energy, where spatial self-shielding,
as well as energy self-shielding, is important. At higher energies, spatial selfshielding
becomes less important, but resonance overlap interference effects
become important.

## 11.2 Widely Spaced Single-Level Resonances in a Heterogeneous Fuel–Moderator Lattice

### Neutron Balance in Heterogeneous Fuel–Moderator Cell

At lower energies in the 10-eV range, the neutron mean free path becomes
comparable to the fuel and moderator dimensions, and it is important to take
into account the spatial heterogeneity of the fuel–moderator cell. The fuel
assembly in a nuclear reactor generally consists of a repeating array of unit cells
consisting of fuel, moderator/coolant, clad, and so on. For simplicity, we
consider a two-region unit cell of fuel (F) and a separate moderator (M). We
allow further for a moderator admixed with the fuel (e.g., the oxygen in UO2
fuel). We return to the problem of calculating the absorption of neutrons in
widely spaced resonances that was treated for a homogeneous mixture in
Section 4.3, but now take into account the important spatial self-shielding
effects that are present in a heterogeneous fuel–moderator lattice. Consider a
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 430 (PDF 449) -->
U235 Capture Cross Section MT = 27
Cross Section (barns)
10–1
10–2
10–3
10–1
Neutron Energy (eV)
Fig. 11.2 235U capture cross section. (From www.nndc.bnl.gov/.)
U235 Fission Cross Section MT = 18
Cross Section (barns)
10–1
10–1
Neutron Energy (eV)
Fig. 11.1 235U fission cross section. (From www.nndc.bnl.gov/.)

<!-- page 431 (PDF 450) -->
U238 Capture Cross Section MT = 27
10–1
10–2
10–3
10–1
Cross Section (barns)
Neutron Energy (eV)
Fig. 11.3 238U capture cross section. (From www.nndc.bnl.gov/.)
U238 Elastic Scattering Cross Section MT = 2
10–2
10–1
10–1
Cross Section (barns)
Neutron Energy (eV)
Fig. 11.4 238U elastic scattering cross section. (From www.nndc.bnl.gov/.)

<!-- page 432 (PDF 451) -->
repeating array of fuel–moderator cells with fuel volume VF and moderator
volume VM. Define the first-flight escape probabilities:
PF0(E) = probability that a neutron that slows down to energy E in the fuel will
make its next collision in the moderator
PM0(E) = probability that a neutron that slows down to energy E in the moderator
will make its next collision in the fuel
We assume that these probabilities are uniform over the fuel and moderator,
respectively.
The neutron balance equation in the fuel can be written as
[ΣF
m + ΣF
t (E)]ϕF(E)VF
= VF 1 □ PF0(E)
[
] ∫
E=αF
E
dE´ ΣF
S(E´)ϕF(E´)
(1 □ αF)E
+ ∫
E=αm
E
dE´ ΣF
mϕF(E´)
(1 □ αm)E
"
+ VMPM0(E)∫
E=αM
E
dE´ ΣM
S (E´)ϕM(E´)
(1 □ αM)E
(11.1)
The left side of the equation is the total reaction rate of the fuel plus admixed
moderator in the fuel volume. The first term on the right side is the source of
neutrons scattering to energy E in the fuel (from scattering collisions with fuel and
with admixed moderator nuclei) times the probability (1 □ PF0) that their next
collision is in the fuel, and the second term is the source of neutrons scattering
into energy E in the moderator times the probability PM0 that their next collision
is in the fuel.
The practical width of an absorption resonance will generally be much smaller
than the scattering-in interval of the moderator, Γp ≪(1 □ αM) E0, or of the
admixed moderator, Γp ≪(1 □ αm) E0, which allows us to use the asymptotic form
of the neutron flux above the resonance energy in the moderator and the fuel,
ϕasy(E) ∼1/E, to evaluate the moderator and admixed moderator scattering
integrals in Eq. (11.1), leading to
[ΣF
m + ΣF
t (E)]ϕF(E)V F
= V F 1 □ PF0(E)
[
] ∫
E=αF
E
dE´ ΣF
S(E´)ϕF(E´)
(1 □ αF)E
+ ΣF
m
E
"
+ V MPM0(E) ΣM
S (E)
E
(11.2)

### Reciprocity Relation

Define G(rF; rM) as the probability that a neutron isotropically scattered to energy
E at location rF in the fuel travels without collision to location rM in the

<!-- page 433 (PDF 452) -->
moderator, and G(rM; rF) as the probability that a neutron isotropically scattered
to energy E at location rM in the moderator travels without collision to location rF
in the fuel. For a uniformly distributed source of neutrons scattering to energy E in
each region, the following identities must obtain:
VFPF0(E)
≡ ΣM
t (E)∫V F
drF∫V M
G(rF; rM)drM
VMPM0(E) ≡ (ΣF
m + ΣF
t (E))∫V M
drM∫V F
G(rM; rF)drF
(11.3)
Since G(rF; rM) and G(rM; rF) depend only on the collision probability along
the path between rF and rM, and this probability is independent of the
direction in which the neutron travels, G(rM; rF) = G(rF; rM), Eq. (11.3) may
be combined to obtain the reciprocity relation between the two first-flight
collision probabilities:
PF0(E)[ΣF
m + ΣF
t (E)]VF = PM0(E)ΣM
t (E)VM
(11.4)
If we make the assumption that absorption is very small relative to scattering in
the moderator, the reciprocity relation may be used to write Eq. (11.2) as
[ΣF
m + ΣF
t (E)]ϕF(E)
= 1 □ PF0(E)
[
] ∫
E=αF
E
dE´ ΣF
S(E´)ϕF(E´)
(1 □ αF)E´ + ΣF
m
E
"
+ PF0(E) ΣF
m + ΣF
t (E)
E
(11.5)

### Narrow Resonance Approximation

If the practical width of the resonance is much smaller than the scattering-in
interval of the resonance nucleus, Γp ≪(1 □ αF) E0, the contribution of the
resonance to the scattering-in integral in Eq. (11.5) can be neglected and the
asymptotic flux in the fuel ϕ(E) ∼1/E can be used to evaluate the integral to
obtain
ϕNR
F (E) =
[1 □ PF0(E)]ΣF
p + PF0(E)ΣF
t (E) + ΣF
m
[ΣF
m + ΣF
t (E)]E
(11.6)
Using this form for the neutron flux to evaluate the capture resonance integral
Iγ ≡ ∫dEσγ(E)ϕ(E)
(11.7)

<!-- page 434 (PDF 453) -->
leads to the narrow resonance approximation for the heterogeneous resonance
integral:
Iγ
NR = ∫
dE
E σγ(E)
σF
p + σF
m + PF0(E)[σF
t (E) □ σF
p]
σF
m + σF
t (E)
= ∫
dE
E σγ(E)
σF
p + σF
m + σe(E)
σF
t (E) + σF
m + σe(E)
(11.8)
where we have defined an escape cross section:
PF0(E) ≡
σe(E)
σe(E) + σF
t (E) + σF
m
)
σe(E) = PF0(E) σF
t (E) + σF
m
1 □ PF0(E)
(11.9)
and used the notation σF
t (E) and σF
p for the total and potential scattering
microscopic cross sections of the resonance absorber, and σF
m for the cross
section of the admixed moderator per fuel nucleus.

### Wide Resonance Approximation

If the practical width of the resonance is much larger than the scattering-in
interval of the resonance nuclei, Γp ≫(1 □ αF) E0, the term Pres
s (E´)ϕ(E´)=E´ ≈
Pres
s (E)ϕ(E)=E in the integrand of Eq. (11.5), leading to the wide resonance
approximation for the flux in the fuel region
ϕWR
F
(E) =
PF0(E)ΣF
t (E) + ΣF
m
[ΣF
t (E) + ΣF
m □ (1 □ PF0(E))ΣF
S(E)]E
(11.10)
Using this result to evaluate the resonance integral of Eq. (11.7) leads to
Iγ
WR = ∫
dE
E σγ(E)
PF0(E)σF
t (E) + σF
m
σF
t (E) + σF
m □ [1 □ PF0(E)]σF
S(E)
= ∫
dE
E σγ(E)
σF
m + σe(E)
σF
a(E) + σF
m + σe(E)
(11.11)
where σF
a = σF
γ + σF
f is the microscopic absorption cross section of the resonance
absorber.

### Evaluation of Resonance Integrals

Recalling from Section 4.3 the form of the single-level resonance cross section
averaged over the thermal motion of the nuclei, the (n, γ) capture cross section or

<!-- page 435 (PDF 454) -->
fission cross section averaged over the motion of the nucleus can be written as
σq(E; T) = σ0
Γq
Γ
E0
E

1=2
ψ(ξ; x);
q = γ; f
(11.12)
and the total scattering cross section, including resonance and potential scattering
and interference between the two, can be written as
σs(E; T) = σ0
Γn
Γ ψ(ξ; x) + σ0R
λ0
χ(ξ; x) + 4πR2
(11.13)
where R is the nuclear radius, λ0 is the neutron De Broglie wavelength, and the
functions
ψ(ξ; x) =
ξ
ffiffiffi
π
p ∫
□1
e□(1=4)(x□y)2ξ2
dy
1 + y2
(11.14)
χ(ξ; x) = ξffiffiffi
π
p ∫
□1
e□(1=4)(x□y)2ξ2 ydy
1 + y2
(11.15)
are integrals over the relative motion of the neutron and nucleus, x = 2(Ecm □ E0)/
Γ, assuming that the nuclear motion can be characterized by a Maxwellian
distribution with temperature T, and Ecm is the energy of the neutron in the
neutron–nucleus center-of-mass system. The parameters characterizing the
resonance are σ0, the peak value of the cross section; E0, the neutron energy
in the center-of-mass system at which it occurs; Γ, the resonance width; Γγ, the
partial width for neutron capture; Γf, the partial width for fission; and Γn, the
partial width for scattering. The resonance absorption cross section is symmetric
about E0, but the scattering cross section is asymmetric because the potential and
resonance scattering interfere constructively for E > E0 and destructively for
E < E0, as indicated in Fig. 11.4.
The temperature characterizing the nuclear motion is contained in the resonance
parameter
ξ =
Γ
(4E0kT=A)1=2
(11.16)
where A is the atomic mass (amu) and k is the Boltzmann constant.
Using these forms for the resonance cross sections in Eqs. (11.8) and (11.11),
the resonance integrals become in the narrow resonance approximation (neglecting
interference scattering)
Iγ
NR = Γγ
2E0
(σF
p + σF
m + σe)∫
□1
ψ(ξ; x)dx
ψ(ξ; x) + β
≡ Γγ
E0
(σF
p + σF
m + σe)J(ξ; β)
(11.17)

<!-- page 436 (PDF 455) -->
and in the wide resonance approximation,
Iγ
WR = Γγ
2E0
(σF
m + σe)∫
□1
ψ(ξ; x)dx
ψ(ξ; x) + β´ ≡ Γγ
E0
(σF
m + σe)J(ξ; β´)
(11.18)
where
β ≡
σF
p + σF
m + σe
σ0
;
β´ ≡ σF
m + σe
σ0
Γ
Γγ
(11.19)
The J(ξ, β) function is tabulated in Table 4.3. The properties of the moderator
region do not appear explicitly in these expressions for the resonance integral
because we have assumed that a neutron that escapes the fuel will have its next
collision in the moderator and because we assumed that absorption in the
moderator could be ignored in using the reciprocity relation.

### Infinite Dilution Resonance Integral

In the infinite dilution limit σ F
m + σe □ σ0, all forms for the resonance integral
approach the infinite dilution value:
Iγ
1 = π
2 σ0
Γγ
E0
;
If
1 = π
2 σ0
Γf
E0
(11.20)
Infinite dilution resonance integrals for a number of fuel isotopes are given in
Table 11.1. Actual resonance integrals will be smaller because of self-shielding
effects.

### Equivalence Relations

For a given resonance absorbing species, assemblies with the same values of σF
m +
σe have the same resonance integral. Furthermore, the heterogeneous assemblies
with a given value of σF
m + σe have the same resonance integrals as homogeneous
assemblies that have moderator scattering cross section per resonance absorber
nucleus σM
s = σF
m + σe. Equations (11.17) and (11.18) reduce to the homogeneous
resonance integrals of Eqs. (4.68) and (4.71) when σe ∼PF0 = 0 (i.e., in the case of a
resonance absorber with a homogeneously admixed moderator).

### Heterogeneous Resonance Escape Probability

The resonance capture rate in a fuel–moderator cell with fuel volume VF and
moderator volume VM is
Rγ = V FNF∫σF
γ (E)ϕF(E) = V FNFIγ
(11.21)

<!-- page 437 (PDF 456) -->
We have evaluated the resonance integral for an asymptotic flux above the
resonance ϕasy = 1/E, assumed uniform over the fuel and moderator. Using the
asymptotic relationship between the slowing-down density, q, and the flux
q = ξ ΣsEϕasy
(11.22)
where ξ is the average logarithmic energy loss defined by Eq. (1.24) and the
average asymptotic moderating power of the cell is
ξ Σs =
V MξMΣM
s + V F(ξFΣF
p + ξmΣF
m)
V M + V F
(11.23)
indicates that an asymptotic flux of 1/E implies an asymptotic slowing-down
density of q = ξ Σs. The resonance escape probability for the cell is unity minus the
resonance absorption probability, and the latter is the resonance absorption rate
divided by the total number of neutrons slowing down q(VF + VM):
p = 1 □
Rγ
q(V F + V M) = 1 □
V FNFIγ
ξΣs(V F + V M) = 1 □ Iγ
ξσs
(11.24)
Table 11.1 Infinite Dilution Total Resonance Integrals for Some Heavy
Elements∗
Isotope
RI(n, γ) (barns)
RI(n, f) (barns)
232Th
–
233U
233Pa
–
234U
235U
236U
237Np
239Np
–
239Pu
241Pu
241Am
238U
240Pu
242Pu
242Am
∗Calculated with ORIGEN (see Ref. [1]).

<!-- page 438 (PDF 457) -->
where ξσs is the cell moderating power per fuel nucleus. The total resonance
escape probability over an energy group g containing several resonances is
P = ∏
i ∈g
pi = ∏
i ∈g
1 □ Iγ
i
ξσs

' exp □ 1
ξσs
X
i ∈g
Iγ
i
!
(11.25)
where i ∈g indicates all of the resonances within energy group g extending from
Eg to Eg□1.
By lumping the fuel, the neutron flux in the fuel is reduced relative to the flux in
the separate moderator – spatial self-shielding – and it is possible to decrease the
resonance integral without decreasing the slowing-down power, thus increasing
the resonance escape probability relative to the value for the same fuel and
moderator distributed homogeneously. In fact, lumping the natural uranium fuel
in the early graphite-moderated reactors was essential to achieving criticality –
the resonance escape probability increased from about 0.7 in a homogeneous
graphite–natural uranium assembly to about 0.88 in a heterogeneous assembly.

### Homogenized Multigroup Resonance Cross Section

An effective multigroup cross section for the resonance absorber can be constructed
by summing the resonance absorption rates over all of the resonances in
the group, dividing by the fuel number density, NF, dividing by the volume of the
fuel–moderator cell, and dividing by the integral of the asymptotic flux over the
energy interval of the group:
σres
g
=
P
i ∈gRi
γ=NF
(V F + V M)∫
Eg□1
Eg
ϕasydE
=
V F
P
i ∈gIγ
i
(V F + V M)ln(Eg□1=Eg)
(11.26)

### Improved and Intermediate Resonance Approximations

The narrow [Γp ≪(1 □ αF)E0] and wide [Γp ≫(1 □ αF)E0] resonance approximations
are limiting cases. For many resonances, the actual situation is intermediate
to these extremes. It is possible to improve upon the narrow resonance and wide
resonance approximations using the neutron balance equation to improve the
flux solution iteratively:
[σF
m + σF
t (E)]ϕ(n)
F (E)
= 1 □ PF0(E)
[
] ∫
E=αF
E
dE´ σF
s (E´)ϕ(n□1)
F
(E´)
(1 □ αF)E´
+ σF
m
E
"
+ PF0(E) σF
m + σF
t (E)
E
(11.27)

<!-- page 439 (PDF 458) -->
The initial flux guess can be the narrow or wide resonance approximation, or an
intermediate resonance approximation that is suggested by comparison of the
two:
ϕ(1)
NR =
σF
m + σF
p + σe
σF
m + σF
t + σe
E
ϕ(1)
WR =
σF
m + σe
σF
m + σF
a + σe
E
ϕ(1)
IR
=
σF
m + λσF
p + σe
σF
m + λσF
s + σF
a + σe
E
(11.28)
where λ, which is in the range 0 < λ < 1, is a parameter to be determined separately
(Chapter 13). In practice, it is not practical to extend this procedure beyond a
single iteration.

## 11.3 Calculation of First-Flight Escape Probabilities

To evaluate the resonance integrals of Section 11.2, it is first necessary to calculate
the probability PF0 that a neutron reaching energy E in the fuel will have its next
collision in the moderator. Although this can be done exactly with a Monte Carlo
calculation, a large number of such calculations would be necessary, and a
number of analytical approximations have been developed.

### Escape Probability for an Isolated Fuel Rod

For an isolated fuel rod surrounded by moderator, the probability PF0 that a
neutron reaching energy E in the fuel will have its next collision in the moderator
is just the probability that the neutron will escape from the fuel rod without a
collision, P0. For a uniform fuel rod, the probability that a neutron created
isotropically at location r0 within a fuel rod of arbitrary shape (Fig. 11.5) escapes
ni
ns
r0
Fig. 11.5 Geometry notation for
escape probability calculation.

<!-- page 440 (PDF 459) -->
from the fuel rod is
P´
0(r0) = ∫
e□l=λ
4πl2 (Ω ? ns)ds
(11.29)
where λ = P□1
t
is the total mean free path, l(r0, Ω) is the distance from r0 to the
surface of the rod in the direction Ω, ns is the outward normal vector to the surface
of the fuel rod, (Ω□ns)ds/4πl2(r0, Ω) is the solid angle that the surface element ds in
the direction ω subtends, and exp(□l/λ) is the probability that the neutron will
reach the surface without collision.
If the neutrons are created isotropically, the average escape probability is
P0 = 1
V ∫P´
0(r0)dr0 = 1
V ∫dV∫dΩ e□l=λ
4π
(11.30)
If we represent the volume as tubular elements oriented in the Ω direction with
cross-sectional area ds(ni□Ω) where ni is the inward normal unit vector on the rod
surface, the volume element is dV = dlds(ni□Ω), and Eq. (11.30) can be integrated
over length l to obtain
P0 =
λ
4πV ∫∫dsdΩ(Ω ? ni)(1 □ e□ls(Ω)=λ)
(11.31)
where ls(Ω) is the chord length from surface to surface of the rod in direction Ω.
For a long fuel plate of thickness a, this may be evaluated exactly:
P0 = λ
a
2 □ E3
a
λ

(11.32)
where E3 is the exponential integral function. An approximate evaluation is
possible for a sphere of radius a:
P0 = λ
R0
1 □
9(R0=λ)2 +
3(R0=λ)
1 +
3(R0=λ)

e□(3=2)(R0=λ)

;
R0 ≡ 4a
(11.33)
and for a long cylindrical fuel rod of radius a,
P0 = λ
R0
1 □ 4
π ∫
π=2
dβcosβKi3
R0
λ cosβ

"
;
Kin(X) ≡ ∫
e□Xcoshudu
(coshu)n ;
R0 = 2a
(11.34)

<!-- page 441 (PDF 460) -->
A more general evaluation may be made by invoking the theory of chord
distributions. The probability that the length of a chord lies between ls and
ls + dls is
ϕ(ls) =
∫∫l´
s=ls
(Ω ? ni)dΩ

(Ω ? ni)>0
ds
∫∫(Ω ? ni)dΩds
(11.35)
where the integral over Ω in the numerator includes only those values of Ω for
which l´
s = ls (i.e., is a chord length of the fuel rod). The denominator is readily
evaluated:
∫∫(Ω ? ni)dΩds = 2πS∫
μdμ = πS
(11.36)
where S is the surface area of the fuel rod.
In this representation, the volume of the fuel rod is
V = ∫l(Ω ? ni)ds;
(Ω ? ni) > 0
(11.37)
and the mean chord length is
ls ≡ ∫lsϕ(ls)dls = 1
πS ∫ls ∫∫l´
s=ls
(Ω ? ni)dΩds

(Ω ? ni)>0
dls
= 1
πS ∫∫ls(Ω ? ni)dΩds = 4V
S ;
(Ω ? ni) > 0
(11.38)
Hence
4πV
ls
ϕ(ls)dls = ∫∫l´
s=ls
(Ω ? ni)dΩ

(Ω ? ni)>0
ds
(11.39)
Using these results in Eq. (11.31) yields
P0 = λ
ls ∫(1 □ e□ls=λ)ϕ(ls)dls = λ
ls
□ ∫e□ls=λϕ(ls)dls
(11.40)

<!-- page 442 (PDF 461) -->
When the dimensions of the fuel rod are small compared with the mean free path,
ls ≪λ, this reduces to
P0 ' 1 □ 1
(l
s )
lsλ
' 1
(11.41)
and when the dimensions are large compared with the mean free path, ls ≫λ,
P0 ' λ
ls
(11.42)
which suggests the rational approximation:
P0 =
1 + (ls=λ) =
1 + (4V=λS)
(11.43)
The rational approximation is known to underestimate the escape probability.
An improved approximation for a long cylindrical rod has been obtained by
integrating an empirical fit for the chord length distribution function:
P0 = λ
ls
1 □
1 + (ls=4:58λ)4:58

(11.44)
An improved rational approximation of the form
P0 =
4V=λs 1 □
1 + 4V=λs
c

□c

(11.45)
with c = 2.09 has been determined empirically to be more accurate than the
Wigner approximation and more accurate than the Sauer approximation for all
geometries other than cylindrical. Note that the approximation of Eq. (11.45)
reduces to the Wigner approximation for c = 1 and to the Sauer approximation
for c = 4.58.

### Closely Packed Lattices

In a lattice of closely packed fuel elements interspersed in moderating material a
neutron escaping from a fuel element without collision may traverse a distance in
moderator without collision and enter another fuel element, where it may have a
collision with a fuel atom or may pass through uncollided to enter moderator

<!-- page 443 (PDF 462) -->
again, and so on. In this situation, the probability of a neutron escaping from the
fuel element in which it is scattered to energy E(P0) is not the same as the
probability that the neutron will have its next collision in moderator (PF0), but
the two are related. Let G(1)
m be the probability that a neutron escaping from the
original fuel element will traverse the line-of-sight distance of moderator
separating the original fuel element from other fuel elements without a collision,
G(2)
f
be the probability that the neutron will traverse the second fuel element
without collision to reenter moderator, and so on. Then we can write
PF0 = P0[(1 □ G(1)
m ) + G(1)
m G(2)
f (1 □ G(2)
m )
+ G(1)
m G(2)
f G(2)
m G(3)
f (1 □ G(3)
m ) + ∙∙∙]
(11.46)
The various G(n)
x
depend on the lattice geometry and are not the same for
successive flights in moderator or fuel (i.e., not equal for n = 1 and n = 2 or
n = 4 and n = 5). However, if we make the approximation that the individual
flight probabilities can be replaced by an average value, Eq. (11.46) can be
summed:
PF0 = P0(1 □ Gf )(1 □ Gm)
1 □ Gf Gm
(11.47)
Gm,f can be estimated by analogy with Eq. (11.43) or heuristically as
Gm;f =
1 + lm;f =λm;f
or
Gm;f = e□lm;f =λm;f
(11.48)
when lm and λm are the mean chord length through the moderator between
fuel elements and the mean free path of neutrons in the moderator, and so on.
Such corrections to P0 are known as Dancoff corrections and allow PF0 to be
written as
PF0 = P0(1 □ γ)
(11.49)
where the factor γ accounts for the decrease in the probability that a neutron
escaping a fuel element will first collide with a moderator nucleus because of the
presence of other fuel elements. For fuel rods arranged in a square or hexagonal
lattice structure,
γ =
exp(□τlsNFσM
S )
1 + (1 □ τ)lsNFσM
s
(11.50)

<!-- page 444 (PDF 463) -->
where
τ =
ffiffiffi
π
p
1 + V F
V M

1=2
□ 1
"
V F
V M
□ 0:08
square
π
ffiffi
p
!1=2
1 + V F
V M

1=2
□ 1
5 V F
V M
□ 0:12 hexagonal
>
>
>
>
>
>
<
>
>
>
>
>
>
:
(11.51)

## 11.4 Unresolved Resonances

Unlike the case of the resonances in the resolved energy region (up to a few
hundred eV or less) where parameters for each individual resonance can be
evaluated explicitly from the high-resolution data, the evaluations of such
parameters become increasingly more difficult as the Doppler and instrument
resolution widths become much greater than the corresponding natural width in
the relatively high-energy range. Under such circumstances, it is not possible to
deal with the physical quantities of interest as a function of energy in great detail.
Instead, it is necessary to estimate the expectation values of these quantities on
the basis of statistical theory. Two types of expectation values of particular
interest in reactor applications are the reaction rate of a given process, denoted by
hσxϕi, and the average flux, denoted by h0i, in the energy interval where many
resonances are present.
Since the NR approximation described earlier is usually applicable in the
unresolved energy range at relatively high energy, the extension of the J-integral
approach is quite natural. The expectation values of interest can be expressed in
terms of the population averages of an ensemble of resonance integrals with their
resonance parameters determined by the known distribution functions from the
statistical theory of spectra. In principle, these averages can be determined once
the average resonance parameters are specified.
Two types of distributions are needed to characterize the statistical behavior of
the resonance parameters. According to Porter–Thomas, the partial widths are
theoretically expected to exhibit a chi-squared distribution with v degrees of
freedom about their mean value hTxi:
Pv(y)dy =
v
2Γ(v=2)
vy

(ν=2)□1
e□(vy=2)dy
(11.52)
where y = Γx/hΓxi and F(v/2) is the gamma function of argument v/2. The degree of
freedom v is identifiable with the number of open channels for reaction process x.
The level spacing between two adjacent levels for a given spin state, D = |Ek □
Ek+1|, is characterized by the Wigner distribution of the form:
W(y)dy = π
2 yexp □ π
4 y2

dy
(11.53)

<!-- page 445 (PDF 464) -->
where y = D/hDi. Physically, it signifies the tendency of repulsion between the
adjacent levels of the same spin sequence. For the integral approach to be
described, a level correlation function that specifies the probability of finding
any level Ek´ at a distance | Ek´ □ Ek | away from a given level Ek is also required. It is
related to the Wigner distribution via the convolution integral equation, defined
as follows:
Ω(y) = W(y) + ∫
y
W(t)Ω(y □ t)dt
(11.54)
For Ek´ belonging to a different spin sequence with respect to Ek, the levels are
statistically independent, and consequently, the correlation function becomes
unity.
With the specification of distributions, the averages can be determined once
the average parameters are provided. For elastic scattering, in which the neutron
width is explicitly energy dependent, one convenient average parameter usually
used is the strength junction. For neutrons with orbital angular momentum l, the
strength function is
Sl =
P
JgJhΓ(0)
nlki
hDki
;
k ∈J; l
(11.55)
where
Γ(0)
nlk
is the average reduced neutron width for given l and k, which is
energy independent, and hDki is the average level spacing for the sequence in
which level k occurs, with
gJ =
2J + 1
2(2I + 1)
(11.56)
where J is the total spin of the neutron–nuclide system and I is the spin of the
target nucleus. Statistical resonance parameters for some of the principal nuclides
are given in Table 11.2.
The single-level Breit–Wigner formula, now generalized to include spin
effects, is
σxk =
πλ2
0gJΓxkΓnk
(E □ Ek)2 + (Γk=2)2
(11.57)
where Fxk,Γnk and Γk are the capture (x = γ) or fission (x = f) width, the neutron
width, and the total width, respectively, for a resonance at Ek, and λ0 is the De
Broglie neutron wavelength.

<!-- page 446 (PDF 465) -->
### Multigroup Cross Sections for Isolated Resonances

Using a narrow resonance approximation for the neutron flux, ϕ ∼1/Σt, the
effective multigroup cross section is
σg
xk =
∫
Eg□1
Eg
dEσxk(E)=Σt(E)
∫
Eg□1
Eg
dE=Σt(E)
= ΣpΓxkJk
f ΔEgNres
(11.58)
Table 11.2 Statistical Resonance Parameters for 235U, 238U, and 239Pu
235U
238U
239Pu
S0 = (0.915 ± 0.5) × 10□4
S0 = (0.90 ± 0.10) × 10□4
S0 = (1.07 ± 0.1) × 10□4
(0 < E < 50 eV);
SJ=3
≈ SJ=4
≈ S0
S1 = (2.5 ± 0.5) × 10□4
S1 = (2.5 ± 0.5) × 10□4
S1 = (2.5 ± 0.5) × 10□4
D
l=0
obs = 0:53 − 0:05 eV
D
l=0
obs = Dl=0;1
J=1=2 = 20:8 − 2:0 eV
D
l=0
obs = 2:3 − 0:2 eV
D
l=1
J=2 = 1:23 eV
D
l=1
J=1=2 = 11:4 − 1:1 eV
D
l=0;1
J=0
= 8:78 eV
D
l=0;1
J=3
= Dl=0;1
J=4
= 1:06 eV
Γ
l=0
γ
= 24:8 − 5:6 meV
D
l=0;1
J=0
= 3:12 eV
D
l=1
J=5 = 1:18 eV
νγ = 39
D
l=1
J=2 = 2:12 eV
Γ
l=0
γ
= 47:9 meV
σpot = 10.6 ± 0.2 barns
Γ
l=0
γ
= 38:7 meV
Γl=0 = 65.1 meV
(0 < E < 50 eV)
R = (9.18 ± 0.13) × 10□13 cm
Γ
l=0
f J=0 = 2800 meV
νf = 4
Γ
l=0
f J=1 = 57 meV
(0 < E < 100 eV)
νf = 27
νf = 2 for (1, J) = (0, 0)
σpot = 11.7 ± 0.1 barns
νf = 1 for (1, J) = (0, 0)
R = (9.65 ± 0.05) × 10□13 cm
νγ = 24
σpot = 10.3 ± 0.15 barns
R = (9.05 ± 0.11) × 10□13 cm
Source: Data from Ref. [2]; used with permission of American Nuclear Society.

<!-- page 447 (PDF 466) -->
where
f = Σp
ΔEg ∫
Eg□1
Eg
dE
Σt(E)
(11.59)
In the unresolved resonance region, statistical averages over the distribution
functions of Eqs. (11.52)–(11.54) are used to construct an effective multigroup
cross section for process x:
hσg
xki = σp
f
X
spin
states
hΓxkJki
hDki
(11.60)
where σp = Σp/Nres is the potential scattering cross section per resonance nucleus
and h□i indicates averages over statistical distributions of both widths and level
spacings.

### Self-Overlap Effects

The large Doppler width for high-energy neutrons and the small level spacing
produce a high degree of self-overlap among the resonances for fissile isotopes,
and significant but less self-overlap for the fertile isotopes. In fast reactor spectra,
the self-overlap effect is not important for the fertile isotopes at operating
temperatures, but does affect the temperature dependence of the Doppler effect
above about 10 keV. The effect of the presence of other resonances on the
effective cross section of resonance k arises from their effect on the flux, ϕ ∼1/Σt,
and gives rise to a generalization of the J function:
J∗(ξk; βk) = 1
2 ∫
□1
ψkdxk
ψk + βk + P
k´ ≠k(σ0k´=σ0k)ψk´ = 1
2 ∫
□1
ψkdxk
ψk + βk
□ 1
2 ∫
□1
ψk
P
k´ ≠k(σ0k´=σ0k)ψk´dxk
(βk + ψk)[βk + ψk + P
k´ ≠k(σ0k´=σ0k)ψk´]
≡ Jk(ξk; βk) +
X
k´ ≠k
Hkk´
(11.61)
where ξk is the resonance parameter of Eq. (11.16) and ψk and ψk´ are evaluated for
the respective resonance parameters of the resonances at Ek and Ek´. The
evaluation of the second, overlap, term is quite complicated because of the
statistical average over resonance parameters and level spacings, and useful
approximations have been developed (Refs. [2,3]).

<!-- page 448 (PDF 467) -->
The multigroup cross section then consists of a term like Eq. (11.58) plus a
negative overlap correction term:
hσg
xki = σp
f
X
spin
states
hΓxkJki
hDki + σp
f
X
k´
X
spin
states
hΓxkHkk´i
hDki
(11.62)

### Overlap Effects for Different Sequences

The spacings of resonances belonging to different J-spin states in the same isotope
or to two different isotopes are not correlated. The most important case is the
overlap of resonances in a fissile isotope by resonances in a fertile isotope.
Neglecting self-overlap, for the moment, the generalized J function for a fissile
isotope with a resonance sequence at energies Ek overlapped by a fertile isotope
with a resonance sequence at energies Ei is
J∗
k(ξk; βk) = 1
2 ∫
□1
ψkdxk
βk + ψk + (σ0i=σ0k)ψi
(11.63)
Separating the generalized J function into the normal J function and an overlap
term, as in Eq. (11.61), and making some further approximations, it is possible to
write the effective multigroup resonance cross section as
hσg
xki = σp
f
X
spin
states
hΓxkJki
hDki
1 □ hΓiJii
hDii

(11.64)
It can be shown that for a single spin state in the fissile isotope, the flux correction
factor f of Eq. (11.59) can be written as
f '
1 □ hΓkJki
hDki

1 □ hΓiJii
hDii

(11.65)
so that the effective multigroup cross section for a fissile isotope overlapped by a
fertile isotope can be written as
hσg
xki = σp
hΓxkJki
hDki
,
1 □ hΓkJki
hDki

(11.66)
In this approximation, the effect of the resonance overlap is compensated
by the corresponding change in flux that it produces, and the parameters of
