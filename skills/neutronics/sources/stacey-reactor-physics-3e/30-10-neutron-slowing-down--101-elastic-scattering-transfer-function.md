# 10 Neutron Slowing Down — 10.1 Elastic Scattering Transfer Function … 10.3 Diffusion Theory
<!-- source PDF pages 415-430 -->

<!-- page 395 (PDF 415) -->
# 10 Neutron Slowing Down

The methods used to calculate the slowing down of fast neutrons above the
thermal energy range are treated in this chapter. We also introduce the lethargy as
an alternative to the energy variable and develop the formalism in terms of
lethargy.

## 10.1 Elastic Scattering Transfer Function

### Lethargy

It is convenient in treating neutron slowing down to replace the energy variable
with the neutron lethargy:
u = ln E0
E
(10.1)
where E0 is the maximum energy that a neutron might have in a nuclear reactor,
say 10 MeV. The incremental lethargy interval, du, corresponding to the incremental
energy interval, dE, is
du = du
dE dE = − dE
E
(10.2)
with the minus sign indicating that as the neutron energy decreases, its lethargy
increases – hence the name.
The fact that the total neutron flux in an incremental lethargy interval
physically is the same as the neutron flux in the corresponding incremental
energy interval provides a correspondence between the flux per unit energy, ϕ(E),
and the flux per unit lethargy, ϕ(u):
ϕ(u)du = −ϕ(E)dE ) ϕ(u) = Eϕ(E)
(10.3)

### Elastic Scattering Kinematics

The principal results obtained in Chapter 2 from the conservation of energy and
momentum in an elastic scattering event were the correlation between the energy
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 396 (PDF 416) -->
change E´ →E and the cosine of the scattering angle in the center-of-mass (CM)
system μC = cos θC:
E
E´ = A2 + 1 + 2Aμc
(A + 1)2
= eu´−u ≡ e−U
(10.4)
and the relation between the cosine of the scattering angle in the lab system,
μ0 = cos θ0, and the cosine of the scattering angle in the CM system,
μ0 =
1 + Aμc
(1 + 2Aμc + A2)1=2
(10.5)
which may be combined to express the correlation between the scattering angle in
the lab system and the change in lethargy U = u − u´:
μ0(U) = 1
2 (A + 1)e−(1=2)U − (A − 1)e(1=2)U
h
i
(10.6)

### Elastic Scattering Kernel

The general lethargy-angle scattering transfer function can be written as
σs(μ0; u´ ! u) = σs(u´)p0(u´; μ0)g(μ0; u´ ! u)
(10.7)
where μ0 = Ω´□Ω is the cosine of the angle in the lab system between the incident
and exit directions of a neutron in a scattering collision, as shown in Fig. 10.1,
p0(u´, μ0) is the probability that a neutron of lethargy u´ will scatter through an
angle θ0 = cos−1 μ0, and g(μ0, u´ →u) is the probability that a neutron of lethargy u´
that scatters through an angle θ0 = cos−1 μ0 will have a final lethargy u. With the
normalization
∫g(μ0; u´ ! u)du = 1
(10.8)
the angular transfer function for scattering through an angle θ0 = cos−1 μ0 is
σs(μ0; u´) ≡ ∫σs(μ0; u´ ! u)du = σs(u´)p0(u´; μ0)
(10.9)
Writing the lethargy-angle transfer function as a function of (u´, U = u − u´, μ0)
and expanding in Legendre polynomials yields
σs(μ0; U; u´) =
X
l´=0
2 (2l´ + 1)b0
l´(u´; U)Pl´(μ0)
(10.10)

<!-- page 397 (PDF 417) -->
where Pl(μ0) is the lth Legendre polynomial of the argument of the cosine of the
scattering angle in the lab system, and the orthogonality properties of the Legendre
polynomials can be used to identify the Legendre coefficients of the scattering
transfer function:
b0
l (u´; U) = ∫
−1
dμ0Pl(μ0)σs(μ0; U; u´)
(10.11)
For elastic scattering, there is a strict lethargy-angle correlation given by
Eq. (10.6), which means that the probability for a scattering collision that
produces a lethargy gain within dU about U is equal to the probability for
scattering with a cosine of the scattering angle within dμ0 about μ0 when U and μ0
are related by Eq. (10.6) and is zero otherwise:
σs(μ0; U; u´)dU = −σs(μ0; u´)δ(μ0 − μ0(U))dμ0(U)
(10.12)
where the minus sign reflects the fact that an increase in the cosine of the
scattering angle corresponds to a decrease in the lethargy gain. Using Eq. (10.12)
in Eq. (10.11) yields
b0
l (u´; U) = σs(μ0; u´)Pl(μ0(U)) − dμ0(U)
dU

(10.13)
Z
Y
X
θ
θ0
θʹ
Ωʹ
Ω
φʹ
φ
Fig. 10.1 Angles involved in a scattering event. (With permission from Ref. [1]. Copyright
1975, MIT Press.)

<!-- page 398 (PDF 418) -->
Making use of the physical fact that the probabilities for scattering through a
given scattering angle in the lab system to within dμ0 about μ0 and for scattering
through the corresponding [via Eq. (10.5)] scattering angle in the CM system to
within dμC about μC must be equal:
σs(μ0; u´)dμ0 = σc
s(μc; u´)dμc
(10.14)
and making use of the observation that the experimental scattering data are well
represented by a Legendre expansion in the cosine of the CM scattering angle
θC = cos−1 μC:
σ(μ0; u´) = σc
s(μc; u´) dμc
dμ0
=
X
l´=0
2 (2l´ + 1)bc
l´(u´)Pl´(μc) dμc
dμ0
(10.15)
allows the Legendre moments of the lethargy gain, b0
l (u´; U), to be related to the
Legendre moments of the angular scattering distribution in the CM system,
bc
l´(u´), which are tabulated in the nuclear data files:
b0
l (u´; U) =
X
l´=0
2 (2l´ + 1)bc
l´(u´)Pl´(μc) dμc
dμ0
Pl(μ0(U)) − dμ0(U)
dU

=
X
l´=0
2 (2l´ + 1)bc
l´(u´)Pl´(μc(U))Pl(μ0(U)) − dμc(U)
dU

≡
X
l´=0
Tll´(U)bc
l´(u´)
(10.16)
Using this result in Eq. (10.10) leads to
σs(μ0; U; u´) =
X
l;l´
2 (2l + 1)Tll´(U)Pl(μ0)bc
l´(u´)
(10.17)
for the elastic scattering lethargy-angle transfer function. Integrating this result
over angle yields the total probability for an elastic scattering event to cause a
lethargy increase from u´ to u:
σs(u´ ! u) = ∫
−1
dμ0σs(μ0; U; u´) =
X
l´=0
T0l´(U)bc
l´(u´)
(10.18)

### Isotropic Scattering in Center-of-Mass System

The angular distribution of elastic scattering in the CM system may be
represented by an average value of the cosine of the CM scattering angle

<!-- page 399 (PDF 419) -->
given by μc = 0.07A2/3E (MeV), except near scattering resonances. Hence the
elastic scattering distribution is essentially isotropic in the CM system, except
for high-energy neutrons scattering from heavy mass nuclei. When the
scattering is taken as spherically symmetric in the CM system, the Legendre
moments of the angular scattering distribution in the CM system are
bc
l(u´) = σs(u´)δl0
(10.19)
In this case, Eq. (10.18) becomes
σiso
s (u´ ! u) = σs(u´)T00(U) = σs(u´)eu´−u
1 − α
(10.20)
The average lethargy increase with isotropic scattering is
ξiso = ∫
ln1=α
σs(u´ ! u)UdU
σs(u´)
= ∫
ln1=α
T00(U)Udu = 1 + α ln α
1 − α
(10.21)
and the average cosine of the scattering angle in the lab system is
(μiso
0 ) = ∫
ln1=α
σs(u´ ! u)μ0(U)dU
σs(u´)
= ∫
ln1=α
T10(U)dU = 2
3A
(10.22)
where A is the atomic mass in amu of the scattering nuclei and α = [(A − 1)/
(A + 1)]2. Both of these quantities are independent of lethargy for a given species
of scattering nuclei. However, the composite values for a mixture, ξ = Σjσsj(u)ξi/
Σjσsj(u) and μ0 = Σjσsj(u)μ0j/Σjσsj(u), may be lethargy dependent. The parameter ξ
used in this section is the scattering parameter of Section 1.6.

### Linearly Anisotropic Scattering in Center-of-Mass System

When only the first two Legendre components of the scattering transfer function
in the center-of-mass system are nonzero, Eq. (10.18) becomes
σanis
s
(u´ ! u) = T(U)
00 bc
0(u´) + T01(U)bc
1(u´)
= σs(u´)eu´−u
1 − α
1 + μc(u´) 3 −
1 − α (1 − e−u´−u)

(10.23)

<!-- page 400 (PDF 420) -->
In this case, the mean lethargy increase in an elastic scattering event,
ξ(u´) = bc
0(u´)
σs(u) ∫
ln1=α
dUUT00(U) + bc
1(u´)
σs(u) ∫
ln1=α
dUUT01(U)
= ξiso − 3 bc
1(u´)
bc
0(u´)
A2 + 1
A
+ 1
(A2 − 1)2
A2
ln A − 1
A + 1

−!
large A ξiso − 2
A
bc
1(u´)
bc
0(u) = ξiso 1 − μc(u´)

(10.24)
is reduced by anisotropic scattering (i.e., the moderation in energy is reduced),
and the average cosine of the scattering angle in the lab system
μ0(u´) = bc
0(u´)
σs(u´) ∫
ln1=α
dUμ0(U) T00(U) + bc
1(u´)
bc
0(u´) T01(U)

= [μ0(u´)]iso + μc(u´) 1 − 3
5A2

(10.25)
is increased by anisotropic scattering (i.e., the scattering is more forward
directed). Both ξ and μ0 become lethargy dependent with anisotropic scattering.

## 10.2 P1 and B1 Slowing-Down Equations

### Derivation

The transport equation of Chapter 9 can immediately be generalized to include
lethargy dependence by allowing for the scattering removal of neutrons from
incremental interval du and for a scattering source of neutrons into du from other
incremental intervals du´ (in the slowing-down region above 1 eV, the in-scatter
would only be from u´ ≤ u):
Ω ? ∇ψ(r; Ω; u) + Σt(r; u)ψ(r; Ω; u)
= ∫
u
du´
∫
4π
dΩ´ Σs(r; μ0; U; u´)
2π
ψ(r; Ω´; u´)
+ 1
k χ(u)∫
du´
∫
4π
dΩ´ vΣf (r; u´)
4π
ψ(r; Ω´; u´)
≡ ∫
u
u−ln1=α
du´
∫
4π
dΩ´ Σse1(r; μ0; U; u´)
2π
ψ(r; Ω´; u´) + S(r; Ω; u)
(10.26)
where μ0 = Ω´□Ω is the cosine of the angle in the lab system between the incident
and exit directions of a neutron in a scattering collision. In the last step,

<!-- page 401 (PDF 421) -->
inelastically scattered and fission neutrons are grouped into a source term and the
remaining scattering term includes only elastic scattering. The macroscopic
elastic scattering transfer function is a sum over nuclear species of the density
times the microscopic transfer function of Eq. (10.17):
Σse1(r; μ0; U; u´) =
X
j
Nj(r)σsj(μ0; U; u´)
=
X
j
Nj(r)
X
l;l´
2 (2l + 1)Tll´(U)Pl(μ0)bc
l´(u´)
(10.27)
and the lower limit of the scatter-in integral for each species is 1 − ln(1/αj), but
this is represented symbolically for notational convenience as a single 1 − ln
(1/α).
The Pn equations were derived in Chapter 9 for one-dimensional geometry and
one-speed neutrons by expanding the directional flux in a Legendre polynomial
series, and this can immediately be generalized to the lethargy-dependent neutron
flux:
ψ(z; μ; u) ' 1
2 ϕ0(z; u)P0(μ) + 3
2 ϕ1(z; μ)P1(μ)
=
2 ϕ0(z; u) + 3
2 μJz(z; u)
=
2 ϕ0(z; u) + 3
2 ΩzJz(z; u)
(10.28)
where μ = Ω□nz = Ωz = cos θ is the cosine of the angle made by the direction of
neutron motion with the z-coordinate axis, as indicated in Fig. 10.2, and the
current Jz has been associated with the n = 1 component of the flux expansion by
using the orthogonality properties of the Legendre polynomials:
Jz(z; u) ≡ ϕ1(z; u) ≡ ∫
−1
P1(μ)ψ(z; μ; u)dμ
(10.29)
Further defining Ωx = Ω□nx = sin θ cos φ, Ωy = Ω□ny = sin θ sin φ, and dΩ = sin θ
dθdφ/4π, the P1 expansion of the directional neutron flux in three-dimensional
geometry is
ψ(r; Ω; u) ' 1
2 ϕ0(r; u) + 3
2 Ω ? J(r; u)
(10.30)
In developing the P1 equations in one dimension (Chapter 9), the expansion
of Eq. (10.28) was substituted into the transport equation, and the resulting
equation was weighted with P0 = 1 and integrated over μ, and then weighted
with P1(μ = Ωz) = μ and integrated over μ, to obtain the two P1 equations. We
generalize this procedure to three dimensions by substituting Eq. (10.30)
into Eq. (10.26) and weighting with 1, Ωx = μx, Ωy = μy, and Ωz = μz, that is,
weight with 1 and Ω, and integrating over Ω to obtain the P1 equations in

<!-- page 402 (PDF 422) -->
three-dimensional geometry:
∫
4π
dΩ Ω ? ∇1
2 ϕ0 + 3
2 Ω ? J

+ Σt
2 ϕ0 + 3
2 Ω ? J

= ∫
4π
dΩ∫
u
du´
∫
4π
dΩ´ Σse1(r; μ0; U; u´)
2π
2 ϕ0(u´) + 3
2 Ω´ ? J(u´)

+ S0(r; u)
(10.31)
∫
4π
dΩΩ Ω ? ∇1
2 ϕ0 + 3
2 Ω ? J

+ Σt
2 ϕ0 + 3
2 Ω ? J

= ∫
4π
dΩ∫
u
du´
∫
4π
dΩ´Ω Σse1(r; μ0; U; u´)
2π
2 ϕ0(u´) + 3
2 Ω ? J(u´)

+ S1(r; u)
(10.32)
where
S0(r; u) ≡ ∫
4π
dΩS(r; Ω; u)
S1(r; u) ≡ ∫
4π
dΩΩS(r; Ω; u)
(10.33)
θ
Z
Zʹ
Yʹ
Xʹ
Y
X
φ
Ω
ρ
Fig. 10.2 Specification of the directional vector Ω in a Cartesian coordinate system. (With
permission from Ref. [1]. Copyright 1975, MIT Press.)

<!-- page 403 (PDF 423) -->
To simplify these P1 equations, Eq. (10.27) is used for the scattering transfer
function, and the addition theorem for Legendre polynomials,
Pn(μ0) = Pn(μ´)Pn(μ) + 2
X
n
m=1
(n − m)!
(n + m)! Pm
n (μ´)Pm
n (μ)cosm(φ´ − φ)
(10.34)
is used to relate the cosine of the scattering angle μ0 = cos θ0 to the cosines of the
angles that the incident and exiting neutron directions make with the z-axis,
μ´ = cos θ´ and μ = cos θ, respectively, as depicted in Fig. 10.1, where Pm
n is the
associated Legendre function. Using the identities
∫dΩ = 1;
∫ΩξΩχdΩ = 1
3 δξχ
∫ΩξdΩ = ∫Ω3
ξdΩ = 0;
ξ = x; y; z
(10.35)
Eqs. (10.32) and (10.33) then can be reduced to
∇? J(r; u) + Σt(r; u)ϕ(r; u) = ∫
u
u−ln1=α
du´Σs0(r; U; u´)ϕ(r; u´) + S0(r; u)
(10.36)
3 ∇ϕ(r; u) + Σt(r; u)J(r; u) = ∫
u
u−ln1=α
du´Σs1(r; U; u´)J(r; u´) + S1(r; u)
(10.37)
where the zero subscript on the flux has been dropped and the Legendre moments
of the elastic scattering transfer functions are defined:
Σsn(r; U; u´) ≡ ∫
−1
dμ0Σsel(r; μ0; U; u´)Pn(μ0)
=
X
j
Nj(r)
X
l´=0
Tnl´(U)bc
l´(u´)
≡ P
j Nj(r)σj
sn(u´ ! u)
(10.38)
In particular, the isotropic and linearly anisotropic lethargy change transfer
functions are
σj
s0(u´ ! u) =
σj
s(u´) eu´−u
1 − αj
u − ln 1
αj
< u´ < u
0;
otherwise
>
<
>
:
(10.39)

<!-- page 404 (PDF 424) -->
σj
s1(u´ ! u)
=
σj
s(u´)eu´−u
1 − αj
A + 1
e(1=2)(u´−u) − A − 1
e−(1=2)(u´−u)

; u − ln 1
αj
< u´ < u
0;
otherwise
>
<
>
:
(10.40)
The essential approximation that has been made in deriving Eqs. (10.36) and
(10.37) is that the angular dependence of the neutron flux can be represented
by only a linearly anisotropic dependence on the angular variable, as given by
Eq. (10.30). This approximation should be good at more than a few mean free
paths away from an interface between very dissimilar media (i.e., in the interior of
large homogeneous regions) and more than a few mean free paths away from an
anisotropic source.

### Solution in Finite Uniform Medium

To solve Eqs. (10.36) and (10.37), it is assumed that the medium is uniform and
that the spatial dependence of the flux and the current can both be represented by
a simple buckling mode [i.e., ϕ(z, u) = ϕ(u) exp(iBz), J(z, u) = J(u) exp(iBz)], so that
these equations become
iBJ(u) + Σt(u)ϕ(u) = ∫
u
u−ln1=α
du´Σs0(U; u´)ϕ(u´) + S0(u)
(10.41)
3 iBϕ(u) + Σt(u)J(u) = ∫
u
u−ln1=α
du´Σs1(U; u´)J(u´) + S1(u)
(10.42)
The parameter B may be considered to characterize the leakage from or into the
medium. Note that this procedure is formally equivalent to Fourier transforming
Eqs. (10.36) and (10.37).
These equations may be put in multigroup form by integrating over Δug =
ug − ug−1 and defining
ϕg
= ∫
ug
ug−1
duϕ(u);
Jg ≡ ∫
ug
ug−1
duJ(u)
Σg
t
≡
Δug ∫
ug
ug−1
duΣt;
Sg
n ≡ ∫
ug
ug−1
duSn(u)
Σg´!g
sn
≡
Δug´ ∫
ug´
ug´−1
du´
∫
ug
ug−1
duΣsn(u´ ! u);
n = 0; 1
(10.43)
Here we have used the asymptotic flux solution ϕ(u) ∼1, corresponding to
ϕ(E) ∼1/E, and assumed that J(u) ∼1, also, in evaluating the total and scattering

<!-- page 405 (PDF 425) -->
cross sections. The multigroup form of the P1 equations is
iBJg + Σg
t ϕg =
X
g´≤g
Σg´!g
s0
ϕg´ + Sg
0;
g = 1; . . . ; G
(10.44)
3 iBϕg + Σg
t Jg =
X
g´≤g
Σg´!g
s1
Jg´ + Sg
1;
g = 1; . . . ; G
(10.45)

### B1 Equations

The principal approximation involved in derivation of the P1 equations is the
assumption of linear anisotropy in the angular dependence of the neutron flux
made in Eq. (10.28) or (10.30). There is an alternative formulation that avoids this
approximation but instead makes the approximation that the angular dependence
of the scattering can be represented by an isotropic plus a linearly anisotropic
scattering transfer function. Returning to Eq. (10.26), but simplified to onedimensional
geometry,
μ @ψ(z; μ; u)
@z
+ Σt(z; u)ψ(z; μ; u)
= ∫
−1
dμ´
∫
u
u−ln1=α
du´Σs(z; μ0; U; u´)ψ(z; μ´; u´) + S(z; μ; u)
(10.46)
and making the same type of assumption about the spatial dependence [i.e., ψ(z, μ,
u) = ψ(μ, u) exp(iBz)] in a uniform medium leads to
[Σt(u) + iBμ]ψ(μ; u)
= ∫
−1
du´
∫
u
u−ln1=α
du´Σs(μ0; U; u´)ψ(μ´; u´) + S(μ; u)
(10.47)
Dividing by (Σt + iBμ) and assuming linearly anisotropic scattering yields
ψ(μ; u) = (Σt(u) + iBμ)−1 1
2 ∫
u
u−ln1=α
du´Σs0(u´ ! u)ϕ(u´)
"
+ 3
2 μ∫
u
u−ln1=α
du´Σs1(u´ ! u)J(u´) + S(μ; u)
(10.48)
The approximation of Eq. (10.28) has not been made in deriving this result; the
quantities ϕ and J have been identified from the definitions
ϕ(u) ≡ ∫
−1
dμψ(μ; u);
J(u) ≡ ∫
−1
dμμψ(μ; u)
(10.49)

<!-- page 406 (PDF 426) -->
Now, Eq. (10.48) is multiplied by 1 and by μ and integrated over μ to obtain the
two B1 equations:
iBJ(u) + Σt(u)ϕ(u) = ∫
u
u−ln1=α
du´Σs0(u´ ! u)ϕ(u´) + S0(u)
3 iBϕ(u) + γ(u)Σt(u)J(u) = ∫
u
u−ln1=α
du´Σs1(u´ ! u)J(u´) + S1(u)
(10.50)
where
γ(u) =
[B=Σt(u)]2tan−1[B=Σt(u)]
3fB=Σt(u) − tan−1[B=Σt(u)]g ' 1 + 4
B
Σt(u)
(10.51)
The B1 equations differ from the P1 equations [Eqs. (10.44) and (10.45)] only by
the factor γ. The essential B1 approximation is a linearly anisotropic scattering
transfer function; the essential P1 approximation is linearly anisotropic neutron
flux. The B1 equations have been found to be somewhat more accurate for slab
geometries, but clearly the two approximations will differ only when B is
significant. The multigroup P1 and B1 equations are the basis of most multigroup
fast spectrum codes (e.g., Refs. [2] and [3]). Typical neutron energy distributions
calculated for thermal (PWR) and fast (LMFBR) reactors are shown in Fig. 10.3.
10–3
FLUX, n/cm2 · s
10–2
10–1
ENERGY, ev
1 keV
LWR
LMFBR
1 MeV
0.025 eV
Fig. 10.3 Representative neutron energy distributions in a PWR and a LMFBR. (With
permission from Ref. [4]. Copyright 1992, Taylor & Francis.)

<!-- page 407 (PDF 427) -->
### Few-Group Constants

The usual procedure in reactor analysis is to solve the multigroup equations (with
a large number of groups varying from 50 to 100 for thermal reactors to a few
1000 for fast reactors) for one or more large homogenized regions and then to
develop few-group (2–4 for water-moderated thermal reactors, 5–10 for graphitemoderated
thermal reactors, 20–30 for fast reactors) constants that can be used
in a few-group diffusion theory calculation of the neutron diffusion during the
slowing-down process. The few-group constants are constructed by using the
fine-group fluxes to weight the fine-group constants over the fine groups
contained within a few group. Denoting the fine groups with a g and the few
groups with a k, the prescriptions for the few-group capture and fission cross
sections
σk =
P
g∈kσgϕg
P
g∈kϕg
(10.52)
and scattering transfer cross sections
σk´!k
sn
=
P
g´∈k´P
g∈k´σg´!g
sn
ϕg´
P
g´∈k´ϕg´
(10.53)
follow directly, where g ∈k indicates a sum over fine groups g within the lethargy
interval of few group k.
There is ambiguity about the definition of the few-group diffusion coefficient,
as discussed in the following section. An appropriate definition is in terms of a
few-group directional transport coefficient, defined as
σk
tr;ξ =
P
g∈k(σg
t Jgξ − P
g´σg´!g
s1
Jg´ξ)
P
g∈kJgξ
;
ξ = x; y; z
(10.54)
where Jgξ is the fine-group current in the ξ-direction. The diffusion coefficient is
related to the transport coefficient by Dg = 1=3Σg
tr. Many other prescriptions for
the diffusion coefficient are found in practice.

## 10.3 Diffusion Theory

### Lethargy-Dependent Diffusion Theory

It was shown in Chapter 9 that the one-speed P1 equations led naturally to
diffusion theory. Unfortunately, this is not the case for the lethargy-dependent P1
equations of Eqs. (10.36) and (10.37). To derive from Eq. (10.37), a relationship of
the form J(r, E) = −D(r, E)∇ϕ(r, E), it is necessary to require further (1) that

<!-- page 408 (PDF 428) -->
Σs1(u´ →u) ∼Σs(u´)δ(u´ − u) or zero; and (2) that J(r, E) and ∇ϕ(r, E) are parallel.
Neither of these relations is satisfied in general, which gives rise to a number of
ambiguities in defining the multigroup diffusion constants, in particular the
diffusion coefficient. A common way to treat the anisotropic scattering difficulty
is to make use of the one-speed results to approximate
∫
u
u−ln1=α
du´Σs1(r; U; u´)J(r; u´) ' Σs(r; u)μ0J(r; μ)
(10.55)
which is equivalent to assuming no lethargy change in anisotropic elastic
scattering. If, in addition, the anisotropic source that would arise from anisotropic
inelastic scattering is assumed to vanish, then
J(r; u) = −
3(P
t(r; u) − P
s(r; u)μ0) ∇ϕ(r; u)
= −
3Σtr(r; u) ∇ϕ(r; u) = −D(r; u)∇ϕ(r; u)
(10.56)
is obtained from Eq. (10.37). This relation, a Fick’s law, can be substituted into
Eq. (10.36) to obtain lethargy-dependent diffusion theory:
−∇? D(r; u)∇ϕ(r; u) + Σt(r; u)
= ∫
u
u−ln1=α
du´Σs0(r; U; u´)ϕ(r; u´) + S0(r; u)
= ∫
u
u−ln1=α
du´Σs0(r; U; u´)ϕ(r; u´) + ∫
u
du´Σ0
in(r; u´ ! u)ϕ(r; u´)
+ 1
k χ(u)∫
du´vΣf (r; u´)ϕ(r; u´)
(10.57)
where the inelastic and fission contributions to the isotropic source are shown
explicitly in the last form.

### Directional Diffusion Theory

In this derivation of lethargy-dependent diffusion theory from neutron transport
theory, the lethargy change (energy change) in anisotropic scattering was neglected
entirely. It is possible to formally include anisotropic lethargy change effects
by defining
Σtr;ξ(r; u) ≡ Σt(r; u) −
∫
u
u−ln1=α
du´Σs1(r; U; u´)Jξ(r; u´)
Jξ(r; u)
(10.58)

<!-- page 409 (PDF 429) -->
whereJξ isthecurrentintheξ-direction.Sincethelethargy dependenceofthecurrent
could well be different for different ξ-directions, a different Σtr,ξ could be defined by
Eq. (10.58) for each coordinate direction ξ = x, y, and z, giving rise to directional
diffusion coefficients Dξ = 1/3Σtr,ξ and to a directional diffusion equation:
− @
@x Dx(r; u) @
@x + @
@y Dy(r; u) @
@y + @
@z Dz(r; u) @
@z

□ ϕ(r; u) + Σt(r; u)ϕ(r; u)
= ∫
u
u−ln1=α
du´Σs0(r; U; u´)ϕ(r; u´) + ∫
u
du´Σ0
in(r; u´ ! u)ϕ(r; u´)
+ 1
k χ(u)∫
du´vΣf (r; u´)ϕ(r; u´)
(10.59)

### Multigroup Diffusion Theory

Multigroup diffusion theory can be formally derived from the lethargy-dependent
diffusion equations [Eqs. (10.57) or (10.59)] or directly from the lethargydependent
P1 equations [Eqs. (10.36) and (10.37)] by integrating over the lethargy
interval of the group Δug = ug − ug−1. The definition of most of the group
quantities is the same for all three procedures and is given by Eq. (10.43),
with fission and absorption cross sections evaluated similarly to the total cross
section. However, the definition of the diffusion coefficient is different for the
various derivations. In the derivation proceeding from Eq. (10.57), the multigroup
diffusion term is formally defined by the replacement
−∇? Dg(r)∇ϕg(r) ≡ −∫
ug
ug−1
du∇? D(r; u)∇ϕ(r; u)
(10.60)
but this leaves open how to define Dg. Since it is unlikely that lethargy-dependent
flux gradients will be available, various heuristic definitions suggest themselves;
for example,
Dg(r) =
∫
ug
ug−1
duD(r; u)
Δug
(10.61)
or
Dg(r) =
3Σg
tr
=
3(Σg
t − μg
0Σg
s)
(10.62)
A similar ambiguity plagues the development of multigroup diffusion equations
from Eq. (10.59).

<!-- page 410 (PDF 430) -->
The formal definition of ξ-direction diffusion coefficient that arises from the
integration of Eq. (10.37) over Δug is
Dg
ξ(r) =
Jξ;g(r)
3∫
ug
ug−1
du[Σt(r; u)Jξ(r; u) − P
g´≤g∫
ug´
ug´−1
du´Σs1(r; u´ ! u)Jξ(r; u´)]
(10.63)
The multigroup diffusion equations have the same form for all derivations:
− @
@x Dg
x(r) @ϕg(r)
@x
− @
@y Dg(r) @ϕg(r)
@y
− @
@z Dg
z(r) @ϕg(r)
@z
+ Σg
t (r)ϕg(r)
=
X
g´≤g
Σg´!g
s
(r)ϕg´(r) + χg
k
X
G
g´=1
vΣg´
f (r)ϕg´(r);
g = 1; . . . ; G
(10.64)
where the elastic and inelastic scattering terms have been combined into a single
scattering term.

### Boundary and Interface Conditions

The appropriate transport theory boundary conditions are zero return current at
external boundaries (unless there is an external beam source):
ϕ(rb; Ω; u) = 0;
^nb ? Ω < 0
(10.65)
where nb is the outward unit vector to the external boundary at rb, and the
appropriate interface condition is continuity of directional flux:
ψ(ri − ε; Ω; u) = ψ(ri + ε; Ω; u)
(10.66)
where ε is a small quantity. These conditions obviously cannot be satisfied exactly
by the diffusion theory approximation to the neutron flux.
The Marshak boundary conditions discussed in Chapter 9 generalize to
Jin = −nb ? J(rb; u) = −nb ? ∫Ωψ(rb; Ω; u)dΩ = 0
(10.67)
Making use of the partial currents and geometric interpretation discussed in
Section 3.1, this condition can be interpreted as the vanishing of the flux at an
extrapolated distance 0.71/Σtr(u) outside the physical boundary. Given the
ambiguity in defining Σtr(u), the computational difficulties that would ensue
from an extrapolated boundary that varied with lethargy and the fact that the
