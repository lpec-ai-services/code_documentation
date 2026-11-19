# 9 Neutron Transport Theory — 9.1 Neutron Transport Equation … 9.3 Collision Probability Methods
<!-- source PDF pages 328-347 -->

<!-- page 307 (PDF 328) -->
# 9 Neutron Transport Theory

Calculation of the transport ofneutronsand theirinteraction with matterareperhaps
the fundamental topics of reactor physics. In this chapter, the major computational
methods used for the transport of neutrons in nuclear reactors are described.

## 9.1 Neutron Transport Equation

The distribution of neutrons in space and angle is defined by the particle
distribution function N(r, Ω, t), such that N(r, Ω, t)dr dΩ is the number of
neutrons in volume element dr at position r moving in the cone of directions dΩ
about direction Ω, as depicted in Fig. 9.1. An equation for N(r, Ω, t) can be derived
by considering a balance on the differential cylindrical volume element of length
dl = v dt, where v is the neutron speed, and cross-section area dA surrounding the
direction of neutron motion, as shown in Fig. 9.2. The rate of change of N(r, Ω, t)
within this differential volume is equal to the rate at which neutrons with
direction Ω are flowing into the volume element (e.g., across the left face in
Fig. 9.2) and less the rate at which they are flowing out of the volume element (e.g.,
across the right face), plus the rate at which neutrons traveling in direction Ω are
being introduced into the volume element by scattering of neutrons within the
volume element from different directions Ω´ and by fission, plus the rate at which
neutrons are being introduced into the volume element by an external source Sex,
minus the rate at which neutrons within the volume element traveling in direction
Ω are being absorbed or being scattered into a different direction Ω´:
@N
@t (r; Ω; t)dr dΩ
= v N(r; Ω; t) □ N(r + Ω dl; Ω; t)
)dA dΩ
+ ∫
4π
dΩ´Σs(r; Ω´ ! Ω)vN(r; Ω´; t)dr dΩ
+ 1
4π ∫
4π
dΩ´v Σf (r)vN(r; Ω´; t)dr dΩ
+ Sex(r; Ω)dr dΩ □ Σa(r) + Σs(r)
)vN(r; Ω; t)dr dΩ
(9.1)
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 308 (PDF 329) -->
z
y
x
dr
r
→
dΩ
Ω
Fig. 9.1 Particles in dr at location r moving in the cone dΩ about the direction Ω. (With
permission from Ref. [1]. Copyright 1984, Wiley.)
z
y
x
dA
r→
Ω
dl
Fig. 9.2 Incremental volume element for particles at location r moving in the direction Ω.
(With permission from Ref. [1]. Copyright 1984, Wiley.)

<!-- page 309 (PDF 330) -->
Making a Taylor’s series expansion
N(r + Ω dl; Ω; t) = N(r; Ω; t) + @N(r; Ω; t)
@l
dl + ∙∙∙
= N(r; Ω; t) + Ω ? ∇N(r; Ω; t) + ∙∙∙
(9.2)
to evaluate the streaming term, denning the directional flux distribution,
ψ(r; Ω; t) ≡ vN(r; Ω; t)
(9.3)
and taking note of the fact that the scattering from Ω´ to Ω depends only on
Ω □ Ω ≡ μ0, so that
Σs(r; Ω´ ! Ω) = 1
2π Σs(r; Ω ? Ω´) ≡ 1
2π Σs(r; μ0)
(9.4)
and writing Σt = Σa + Σs, leads to the neutron transport equation
v
@ψ
@t (r; Ω; t) + Ω ? ∇ψ(r; Ω; t) + Σt(r)ψ(r; Ω; t)
= ∫
□1
dμ0Σs(r; μ0)ψ(r; Ω´; t)
+ 1
4π ∫
4π
dΩ´vΣf (r)ψ(r; Ω; t) + Sex(r; Ω) ≡ S(r; Ω)
(9.5)
The representation of the neutron streaming operator Ω □ ∇ψ in the common
geometries is given in Table 9.1, and the respective coordinate systems are defined
in Figs. 9.3–9.5.

### Boundary Conditions

Boundary conditions for Eq. (9.5) are generally specified by the physical situation.
For a left boundary at rL with inward normal vector n, such that n □ Ω > 0 indicates
inward, one of the following boundary conditions is usually appropriate:
Vacuum :
ψ(rL; Ω) = 0;
Ω ? n > 0
Incident flux known : ψ(rL; Ω) = ψin(rL; Ω);
Ω ? n > 0
Reflection :
ψ(rL; Ω) = ∫
4π
α(Ω´ ! Ω)ψ(rL; Ω´)dΩ´
(9.6)
where α is a reflection or albedo function.

<!-- page 310 (PDF 331) -->
### Scalar Flux and Current

The scalar flux is the product of the total number of neutrons in a differential
volume, which is the integral over direction of the number of neutrons with
direction within dΩ about Ω, times the speed:
ϕ(r) ≡ ∫
4π
dΩψ(r; Ω)
(9.7)
Table 9.1 Neutron Streaming Operator in Conservative Form
Spatial
Variables
Angular
Variables
Ω □ ∇ψ
Streaming Operator in Rectangular Coordinates
x (one
dimension)
μ
μ @ψ
@x
x, y (two
dimensions)
μ, η
μ @ψ
@x + η @ψ
@y
x, y, z (three
dimensions)
μ, η, ξ
μ @ψ
@x + η @ψ
@y + ξ @ψ
@z
Streaming Operator in Cylindrical Coordinates in Conservation Form
ρ (one
dimension)
ω, ξ
μ
ρ
@
@ρ (ρψ) □ 1
ρ
@
@ω (ηψ)
ρ, θ (two
dimensions)
ω, ξ
μ
ρ
@
@ρ (ρψ) □ η
ρ
@ψ
@θ □ 1
ρ
@
@ω (ηψ)
ρ, z (three
dimensions)
ω, ξ
μ
ρ
@
@ρ (ρψ) + ξ @ψ
@z □ 1
ρ
@
@ω (ηψ)
ρ, θ, z
ω, ξ
μ
ρ
@
@ρ (ρψ) □ η
ρ
@ψ
@θ + ξ @ψ
@z □ 1
ρ
@
@ω (ηψ);μ = (1 □ ξ2)1=2cos ω; η = (1 □ ξ2)1=2sin ω
Streaming Operator in Spherical Coordinates in Conservation Form
ρ
μ
μ
ρ2
@
@ρ (ρ2ψ) + 1
ρ
@
@μ (1 □ μ2)ψ

ρ, θ
μ, ω
μ
ρ2
@
@ρ (ρ2ψ) +
η
ρ sin θ
@
@θ (sin θψ) + 1
ρ
@
@μ (1 □ μ2)ψ

□ cot θ
ρ
@
@ω (ξψ)
ρ, θ, φ
μ, ω
μ
ρ2
@
@ρ (ρ2ψ) +
η
ρ sin θ
@
@θ (sin θψ) +
ξ
ρ sin θ
@ψ
@φ + 1
ρ
@
@μ (1 □ μ2)ψ

□ cot θ
ρ
@
@ω (ξψ) η = (1 □ μ2)1=2cos ω; ξ = (1 □ μ2)1=2sin ω
Source: Data from Ref. [1]; used with permission of Wiley.

<!-- page 311 (PDF 332) -->
and the current with respect to the ξ-coordinate is the net flow of neutrons in the
positive ξ-direction:
Jξ(r) ≡ nξ∫
4π
dΩ(nξ ? Ω)ψ(r; Ω)
(9.8)

### Partial Currents

The positive and negative partial currents, with respect to the ξ-direction, are the
total neutron flows in the positive and negative ξ-directions, respectively:
J+
ξ (r) ≡ nξ∫
2π
dϕ∫
dμ(nξ ? Ω)ψ(r; Ω)
J□
ξ (r) ≡ nξ∫
2π
dϕ∫
□1
dμ(nξ ? Ω)ψ(r; Ω)
(9.9)
z
y
x
r⇀
Ω
ey
^
ex
^
ez
^
μ
η
ξ
ε
Fig. 9.3 Cartesian space–angle coordinate system. (With permission from Ref. [1]. Copyright
1984, Wiley.)

<!-- page 312 (PDF 333) -->
## 9.2 Integral Transport Theory

The steady-state version of Eq. (9.5) may be written as
d
dR ψ(r; Ω)dr dΩ + Σt(r)ψ(r; Ω)dr dΩ = S(r; Ω)dr dΩ
(9.10)
where dR is the differential length along the direction Ω (i.e., Ω □ ∇= d/dR). This
equation may be integrated along the direction Ω from r0 to r, to obtain
ψ(r; Ω)dr = e□α(r0;r)ψ(r0; Ω)dr0 + ∫
r
r0
e□α(r´;r) S(r´; Ω)dr´
(9.11)
z
y
x
r→
Ω
eθ
^
–eφ
^
er^
μ
η
ξ
ε
χ
θ
φ
Fig. 9.4 Spherical space–angle coordinate system. (With permission from Ref. [1]. Copyright
1984, Wiley.)

<!-- page 313 (PDF 334) -->
where α(r´, r) is the optical path length along the direction Ω between r´ and r:
α(r´; r) ≡ ∫
r
r´Σt(R)dR

(9.12)

### Isotropic Point Source

For an isotropic point source of strength S0(n/s) located at r0, the directional flux
outward through the cone dΩ about direction Ω is S0(dΩ/4π). The volume
element dr subtended by this cone at distance R = |r □ r´| away is 4πdΩR2dR, as
depicted in Fig. 9.6. From Eq. (9.11), the directional flux at r of uncollided
neutrons from an isotropic point source at r´ (such that the direction from r´ to r
is Ω) is given by
ψpt(R) = ψ(j(r □ r´)j; Ω) = S0e□α(r;r´)
4πjr □ r´j
2 = S0e□α(R;0)
4πR2
(9.13)

### Isotropic Plane Source

The scalar flux of uncollided neutrons at a distance x from a uniform planar
isotropic source can be constructed by treating each point in the plane as an
z
z
y
x
r
⇀
Ω
ez
^
eρ
^
–eθ
^
μ
η
ξ
ε
ρ
θ
Fig. 9.5 Cylindrical space–angle coordinate system. (With permission from Ref. [1]. Copyright
1984, Wiley.)

<!-- page 314 (PDF 335) -->
isotropic point source and integrating over the plane, as indicated in Fig. 9.7, to
obtain
ϕpl(x; 0) = ∫
2πρψpt(R)dρ = ∫
x
2πRψpt(R)dR
= S0
2 ∫
x
e□α(R;0) dR
R = 1
2 S0E1(α(x; 0))
(9.14)
dR1 = 4πdΩdRʹ Rʹ2
Ω
dΩ
rʹ
Rʹ
r
O
Fig. 9.6 Incremental volume subtended by cone dΩ at distance R = |r □ r´| from point r. (With
permission from Ref. [1]. Copyright 1984, Wiley.)
z
dA
+y
R
x
x
O
θ
ρ
–y
Fig. 9.7 Coordinate system for
plane isotropic source calculation.
(With permission from Ref. [2].
Copyright 1960, McGraw-Hill.)

<!-- page 315 (PDF 336) -->
where the exponential integral function is defined as
En(y) ≡ ∫
dμ e□yuμ□n = ∫
dμ e□y=μμn□2
(9.15)
The x-direction current of uncollided neutrons at a distance x from a uniform
planar isotropic source can be constructed in a similar manner by noting that for a
neutron originating on the plane with direction Ω, the quantity μ = Ω □ nx = x/R:
Jpl;x(x; 0) = ∫
2πρ x
R ψpt(R)dρ = x∫
x
2πRψpt(R) d R
R
= S0
2 ∫
x
e□α(R;0) d R
R2 = 1
2 S0 E2(α(x; 0))
(9.16)
A one-dimensional isotropic source distribution S0(x) in a slab of thickness a
can be considered as a distribution of isotropic planar sources, and the uncollided
scalar flux distribution can be constructed by integrating over the contributions
from each planar source:
ϕ(x) = ∫
a
S0(x´)ϕpl(x; x´)dx´ = 1
2 ∫
a
S0(x´)E1(α(x; x´))dx´
(9.17)

### Anisotropic Plane Source

Using the relations μ = cos θ = x/R and R2 = x2 + ρ2 and noting that all source
neutrons in the annular region 2πρ dρ on the source plane will pass through a
point at a distance x above the center of the annular region within dμ about the
same value of μ, the directional flux of uncollided neutrons that results from an
anisotropic planar source S(μ) can be constructed:
ψ(x; μ)dμ = ψpt(R(ρ))2πρ dρ = S(μ)e□α(x;0)=μ
μ
dμ
(9.18)
The scalar flux and current of uncollided neutrons at a distance x from a uniform
anisotropic planar source S(μ) are
ϕ(x) ≡ ∫
□1
ψ(x; μ) dμ = ∫
S(μ)e□α(x;0)=μ dμ
μ
(9.19)
Jx(x) ≡ ∫
□1
μψ(x; μ)dμ = ∫
S(μ)e□α(x;0)=μ dμ
(9.20)

<!-- page 316 (PDF 337) -->
It is convenient to expand the directional dependence of the source
S(μ) =
X
n=0
(2n + 1)p+
n(μ)Sn
(9.21)
in half-range Legendre polynomials,
p+
n(μ) = Pn(2μ □ 1)
p+
0 (μ) = 1;
p+
1 (μ) = 2μ □ 1;
p+
2 (μ) = 6μ2 □ 6μ + 1;
p+
3 (μ) = 20μ3 □ 30μ2 + 12μ □ 1;
and so on:
(9.22)
which have the orthogonality properties
∫
p+
n(μ)p+
m(μ)dμ =
δnm
2n + 1
(9.23)
With
these
orthogonality
properties,
it
follows
immediately
that
Sn =
∫
p+
n(μ) □ S(μ)dμ
Using this expansion in Eq. (9.19), the flux of uncollided neutrons at a distance
x from a uniform anisotropic planar source is
ϕ(x) =
X
n=0
(2n + 1)SnB+
n(α(x; 0))
(9.24)
where
B+
n(α(x; 0)) ≡ ∫
p+
n(μ)e
□α(x;0)=μ dμ
μ
B+
0 (α(x; 0)) = E1(α(x; 0))
B+
1 (α(x; 0)) = 2E2(α(x; 0)) □ E1(α(x; 0));
and so on
(9.25)
Similarly, the x-directed current of uncollided neutrons at a distance x from a
uniform anisotropic planar source is
Jx(x) =
X
n=0
(2n + 1)SnL+
n(α(x; 0))
(9.26)

<!-- page 317 (PDF 338) -->
where
L+
n(α(x; 0)) = ∫
p+
n(μ)e□α(x;0)=μdμ
L+
0 (α(x; 0)) = E2(α(x; 0))
L+
1 (α(x; 0)) = 2E3(α(x; 0)) □ E2(α(x; 0));
and so on:
(9.27)

### Transmission and Absorption Probabilities

As an example of an application of the formalism above, consider a purely
absorbing slab of thickness a with an isotropic plane source of neutrons on one
surface. The transmission probability for the slab is just the ratio of the exiting
current on the opposite surface to the incident partial current on the other
surface:
T = J(a)
Jin(0) = S0L+
0 (α(a; 0))
S0
= E2(α(a; 0))
(9.28)
and the absorption probability is A = 1 □ T = 1 □ E2(α(a, 0)).

### Escape Probability

As another example, consider a uniform, purely absorbing slab of thickness a with
an isotropic neutron source S0 distributed uniformly throughout. Representing
the source of neutrons at x within the slab as a plane isotropic source of strength
S0/2 to the right and S0/2 to the left, the current of neutrons produced by the
source at x = x´ that exit through the surface at x = a is
Jout(a : x´) = 1
2 S0L+
0 (α(a; x´)) = 1
2 S0E2(α(a; x´))
(9.29)
The total current of neutrons out through the surface at x = a is found by
integrating this expression over the slab:
Jout(a) = ∫
a
dx´ Jout(a : x´) = 1
2 S0∫
a
dx´E2(α(a; x´))
(9.30)
Using the differentiation property of the exponential integral function
dEn
dy = □En□1(y);
n = 1; 2; 3; . . .
(9.31)

<!-- page 318 (PDF 339) -->
Eq. (9.30) may be evaluated:
Jout(a) = □ 1
2 S0∫
a
dE3(α)
dα
dx´ = □ 1
S0
Σt ∫
α(a;0)
d E3
dα dα
= 1
S0
Σt
E3(0) □ E3(α(a; 0))
[
] = 1
S0
Σt
2 □ E3(α(a; 0))

(9.32)
By symmetry, the current out through the surface at x = 0 must be the same. The
escape probability from the slab is the ratio of the total current out of the slab
through both surfaces to the total neutron source rate aS0 in the slab:
P0 = Jout(a) + Jout(0)
aS0
= 1
aΣt
2 □ E3(aΣt)

(9.33)

### First-Collision Source for Diffusion Theory

As a further application, consider a medium with a surface source of neutrons,
which is highly forward directed but almost isotropic within the forwarddirectional
hemisphere, incident on one surface of a diffusing medium; that is,
the forward-directed neutrons incident on the medium are nearly isotropic within
the forward-directional hemisphere, but many more neutrons are moving forward
into the medium than are moving backward out of it. Diffusion theory will
not be accurate for treating these source neutrons, because diffusion theory is
based on an implicit assumption that the neutron flux is nearly isotropic over the
full angle (this is discussed in Section 9.6), even though diffusion theory may
otherwise be sufficient for the analysis of neutrons once their direction is
randomized by a scattering event within the medium. The first collision of the
incident source neutrons can be calculated with integral transport theory and
used as a distributed first-collision source for the diffusion theory calculation:
Sfc(x) = Σs(x)ϕ(x) = S0Σs(x)E1(α(x; 0))
(9.34)
If the distribution of incident source neutrons is more highly forward
directed, so that it is anisotropic even over the forward-directional hemisphere,
it may be represented by an anisotropic plane source and the first-collision
source becomes
Sfc(x) = Σs(x)
X
n=0
(2n + 1)SnB+
n (α(x; 0))
(9.35)

### Inclusion of Isotropic Scattering and Fission

Consider again the slab with a distributed isotropic source of neutrons, but now
with isotropic elastic scattering and fission, as well as absorption represented

<!-- page 319 (PDF 340) -->
explicitly. The flux of uncollided source neutrons is
ϕ0(x) = 1
2 ∫
a
S0(x´)E1(α(x; x´))dx´
(9.36)
If the first-collision rate at x = x´ is considered as a plane isotropic source of oncecollided
neutrons at x´, the flux of once-collided neutrons due to the once-collided
source at x´ is
ϕ1(x : x´) = 1
2 (Σs(x´) + vΣf (x´))ϕ0(x´)E1(α(x; x´))
(9.37)
and the total flux of once-collided neutrons at x is found by integrating over the
distribution of first-collision sources:
ϕ1(x) = ∫
a
ϕ1(x : x´)dx´
= ∫
a
2 (Σs(x´) + vΣf (x´))ϕ0(x´)

E1(α(x; x´))dx´
(9.38)
Continuing in this vein, the flux of n-collided neutrons is given by
ϕn(x) = ∫
a
2 (Σs(x´) + vΣf (x´))ϕn□1(x´)

? E1(α(x; x´))dx´;
n = 1; 2; 3; . . . ; 1
(9.39)
The total neutron flux is the sum of the uncollided, once-collided, twicecollided
, and so on, fluxes:
ϕ(x) ≡ ϕ0(x) +
X
n=1
ϕn(x)
= ∫
a
2 Σs(x´) + vΣf (x´)

X
n=1
ϕn□1(x´)E1(α(x; x´))dx´
+ 1
2 ∫
a
(S0(x´)E1(α(x; x´)))dx´
∫
a
2 (Σs(x´) + vΣf (x´))ϕ(x´)E1(α(x; x´))dx´
+ 1
2 ∫
a
S0(x´)E1(α(x; x´))dx´
(9.40)

<!-- page 320 (PDF 341) -->
Thus, we have found an integral equation for the neutron flux in a slab with
isotropic scattering and fission, with a kernel 1
2 Σs(x´) + vΣf (x´)

E1(α(x; x´)) and a
first-collision source 1
2 S0E1(α(x; 0)).

### Distributed Volumetric Sources in Arbitrary Geometry

The scalar flux of uncollided neutrons resulting from an arbitrary neutron source
distribution can be constructed by treating each spatial location as a point source
with strength given by the source distribution for that location. The uncollided
directional flux at r arising from a point source at r´ is given by Eq. (9.13). The total
uncollided directional flux at r is obtained by integrating over all source points r´,
and the total uncollided scalar flux is then calculated by integrating over Ω:
ϕun(r) = ∫dr´ S0(r´)e□α(r;r´)
4πjr´ □ rj
(9.41)
Following the same development as that leading to Eq. (9.40), an integral
equation for the total neutron flux can be developed for the case of isotropic
scattering:
ϕ(r) = ∫dr´ [Σs(r´) + vΣf (r´)]ϕ(r´)e□α(r;r´)
4πjr´ □ rj
+ ϕun(r´)
= ∫dr´f Σs(r´) + vΣf (r´)

ϕ(r´) + S0(r´)g
e□α(r;r´)
4πjr´ □ rj
(9.42)
where exp[□α(r, r´)]/4π|r □ r´|2 is the isotropic point source kernel and ϕun given
by Eq. (9.41) is the uncollided flux contribution.
The derivations leading to Eqs. (9.40) and (9.42) did not explicitly take
boundary conditions into account. Since scattering source rates integrated
over the volume of the reactor were used to derive successive n-collided fluxes,
the implicit assumption was that neutrons that escaped from the reactor did not
return. Thus, these equations are valid with vacuum boundary conditions, but not
with reflective boundary conditions.

### Flux from a Line Isotropic Source of Neutrons

Consider the situation illustrated in Fig. 9.8 of a line isotropic source of neutrons
of strength S0(n/cm □ s). The point source kernel can be used to construct the
differential scalar flux at a point P located a distance t from the line source due to
the differential element dz of the line source located at z:
dϕ (t) = S0 dz e□α(t;z)
4π R2
(9.43)

<!-- page 321 (PDF 342) -->
where α(t, z) denotes the optical thickness along the path of length R from the
source point at coordinate z to the point P a perpendicular distance t from the line
source at z = 0. Noting that R = t/cos θ and dz = R dθ/cos θ = t dθ/cos2 θ, the total
flux at a point at a distance t can be found by integrating the differential flux
contribution from all such differential elements dz:
ϕ(t) = ∫
□1
S0 dz e□α(t;z)
4πR2
= S0∫
dz e□α(t;0)=cosθ
2πt2=cos2θ ≡ Ki1[α(t; 0)]
2πt
S0
(9.44)
where Ki1(x) is the Bickley function of order 1.

### Bickley Functions

The general Bickley function is defined as
Kin(x) ≡ ∫
π=2
cosn□1 θe□x=cosθdθ = ∫
e□x cosh(u)
coshn(u) du
(9.45)
Rdθ
dz
Line
source
dθ
t, τ
R and t in cm,
ρ and τ in mfp.
P
R, ρ
θ
Fig. 9.8 Geometry for calculating
flux at P from a line isotropic
neutron source (t = x, τ = α(x, 0)).
(With permission from Ref. [3].
Copyright 1983, Academic Press.)

<!-- page 322 (PDF 343) -->
These functions satisfy the following differential and integral laws:
dK in(x)
dx
= □K in□1(x)
(9.46)
K in(x) = K in(0) □ ∫
x
K in□1(x´)dx´ = ∫
x
K in□1(x´)dx´
(9.47)
and the recurrence relation
n K in+1(x) = (n □ 1)K in□1(x) + x[K in□2(x) □ K in(x)]
(9.48)
The Bickley functions must be evaluated numerically (e.g., Ref. [3]).

### Probability of Reaching a Distance t from a Line Isotropic Source without a Collision

With reference to Fig. 9.9, the probability P that a neutron emitted isotropically
from point P on the line source is able to get a perpendicular distance t away from
the line source without having a collision depends on the direction in which the
neutron is traveling relative to the perpendicular to the line source. The
Line
source
R, ρ
dz
Rdθ
dz
P
tdφ
dφ
dθ
t, τ
θ
Fig. 9.9 Geometry for calculating probability that a neutron from an isotropic line source
does not have a collision within perpendicular distance t from the line source (t = x,
τ = α(x, 0)). (With permission from Ref. [3]. Copyright 1983, Academic Press.)

<!-- page 323 (PDF 344) -->
uncollided differential neutron current arising from a point on the line source and
passing through a differential surface area dA = R dθt dφ = t2 dθ dφ/cos θ normal
to the R-direction at a perpendicular distance t from the line source is
dJ(t; θ) = e□α(t;z)
4πR2 d A = e□α(t;0)=cos θ
4π(t=cos θ)2
t2dθ dφ
cos θ
(9.49)
where the optical thickness α(t, z) is taken along the path length R. Integrating
over all possible values of the angles, the probability of a neutron emitted
isotropically from a line source crossing the cylindrical surface at a distance t
from the line source is
P(t) = ∫
2π
dφ∫
π=2
□π=2
dθ e□α(t;0)=cosθ(t2=cos θ)
4π(t=cos θ)2
= K i2(α(t; 0))
(9.50)
where now α(t, 0) is the optical path length perpendicular to the line source out to
the cylindrical surface at distance t.
The Bickley and exponential integral functions arise because of the assumption
of spatial symmetry. They take into account that the neutron flight path is always
in three spatial dimensions, even though symmetry otherwise allows reduction in
the dimensionality of the problem.

## 9.3 Collision Probability Methods

Ifthe volume of the problem ofinterest ispartitioned intodiscretevolumes, Vi,within
each of which uniform average cross sections and a flat flux are assumed, Eq. (9.42)
can be integrated over Vi, and the resulting equation can be divided by Vi to obtain
ϕi =
X
j
Tj!i[(Σsj + vΣf j)ϕj + S0j]
(9.51)
which relates the fluxes in the various volumes by the first-flight transmission
probabilities Tj→i:
Tj!i ≡ 1
V i ∫V i
dri∫V j
drj
e□α(ri;rj)
4πjri □ rjj
(9.52)

### Reciprocity Among Transmission and Collision Probabilities

Since α(ri, rj) = α(rj, ri) (i.e., the optical path is the same no matter which way the
neutron traverses the straight-line distance between ri and r), there is a reciprocity

<!-- page 324 (PDF 345) -->
relation between the transmission probabilities:
V iTj!i = V jTi!j
(9.53)
Upon multiplication by Σti Vi, Eq. (9.51) can be written as
ΣtiViϕi =
X
j
Pji (Σsj + vΣf j)ϕj + S0j
Σtj
(9.54)
where the collision rate in cell i is related to the neutrons introduced by scattering,
fission, and an external source in all cells j by the collision probabilities
Pji ≡ ΣtjΣtiV iTj!i = ΣtjΣti∫V i
dri∫V j
drj
e□α(ri;rj)
4πjri □ rjj
(9.55)
Because α(ri, rj) = α(rj, ri), there is reciprocity between the collision probabilities;
that is,
Pij = Pji
(9.56)

### Collision Probabilities for Slab Geometry

For a slab lattice, the volumes Vi become the widths Δi ≡ xi+1/2 □ xi□1/2 of the slab
regions centered at xi, and the slab kernel E1(α(x´, x))/2 replaces the point source
kernel in Eq. (9.55), which becomes
Pji = ΣtiΣtj∫Δi
dx´
∫Δj
dx 1
2 E1(α(x´; x))
(9.57)
For j ≠i, the probability that a neutron introduced in cell j has its next collision in
cell i is
Pji = 1
2 E3(αi+1=2;j+1=2) □ E3(αi□1=2;j+1=2) □ E3(αi+1=2;j□1=2) + E3(αi□1=2;j□1=2)

ΣtiΣtj
(9.58)
where αi,j ≡ α(xi, xj). For j = i, a similar development leads to an expression for the
probability that a neutron introduced in cell j has its next collision in cell i is
Pii = ΣtiΔi 1 □
2ΣtiΔi
(1 □ 2E3(ΣtiΔi))

(9.59)

<!-- page 325 (PDF 346) -->
### Collision Probabilities in Two-Dimensional Geometry

Consider the two-dimensional cross section shown in Fig. 9.10, in which the
volumes Vi and Vj extend indefinitely in the direction perpendicular to the
page. With respect to Fig. 9.9, a neutron emitted at point t defined by the
angle φ and coordinate y in volume Vi in Fig. 9.10 and traveling in the
direction defined by the angle φ that passes through volume Vj may be
traveling at any angle □π/2 ≤ θ ≤ π/2 with respect to the horizontal cross
section shown in Fig. 9.10.
The probability that a neutron emitted at point t will reach some point on the
line perpendicular to the page that passes through the page at point t´ in volume Vj
is, from Eq. (9.50), given by Ki2(α(t´, t)), where α(t´, t) is the optical path length in
the horizontal plane of Fig. 9.10. With respect to Fig. 9.10, identify ti and tj as the
points along the horizontal line between t and t´ at which the line passes through
the surfaces of volumes Vi and Vj, respectively. Thus, Ki2(Σti(ti □ t) + α(tj, ti)) is the
probability that a neutron emitted from point t in volume Vi in direction φ reaches
volume Vj, and Ki2(Σti(ti □ t) + α(tj, ti) + α(tj + Δtj, tj)), with Δtj being the distance
in the horizontal plane across volume Vj, is the probability that the neutron not
only reaches volume Vj but continues through volume Vj and emerges from the
opposite side without a collision, both probabilities being averaged over an
isotropic distribution of neutron directions with respect to the horizontal, as
measured by the angle θ. The probability that neutrons emitted from point t
in volume Vi with direction φ have their first collision in volume Vj is then
pij(t, φ, y) = □Ki2(Σti(ti □ t) + α(tj, ti) + α(tj + Δtj, tj)) + Ki2(Σti(ti □ t) + α(tj, ti)).
Averaging this probability over all source points along the line defined by angle
φ within volume Vi and using the differential property of the Bickley functions
COLLISION PROBABILITY METHOD
(mfp)
(cm)
ymin(φ)
y(φ)
ymax(φ)
t
t
ti
τi
τij
τj
vj
vi
φ
Fig. 9.10 Geometry for calculating collision probabilities in two-dimensional geometry (τ is
the optical path length α over the indicated path). (With permission from Ref. [3]. Copyright
1983, Academic Press.)

<!-- page 326 (PDF 347) -->
given by Eq. (9.45) leads to
pij(φ; y) = 1
ti ∫
ti
pij(t; φ; y)dt
=
Σtiti
K i3(α(tj; ti)) □ K i3(α(tj; ti) + α(tj + Δtj; tj)) □ K i3(α(tj; ti)

+ α(ti; 0)) + K i3(α(tj; ti) + α(tj + Δtj; ti) + α(ti; 0))]
(9.60)
To obtain the average probability Pij that a neutron introduced by an isotropic
source uniformly distributed over volume Vi will have its first collision in volume
Vj, this expression must be multiplied by the probability that an isotropically
emitted neutron source will emit a neutron in the differential direction dφ about
φ, which is dφ/2π, and the probability that for a uniform source within Vi the
neutron will be emitted from along the chord of length ti(y) at coordinate y, which
is ti(y)dy/Vi, and integrated over all relevant values of φ and y. Note that the
volumes Vi and Vj are actually the respective areas within the planar cross section
of Fig. 9.10. The result for the collision probability is
pij = 1
2π ∫
φmax
φmin
dφ∫
ymax(φ)
ymin(φ)
dy K i3 α(tj; ti)

□ K i3 α(tj; ti) + α(tj + Δtj; tj)

□ K i3 α(tj; ti) + α(ti; 0)

+ K i3 α(tj; ti) + α(tj + Δtj; tj) + α(ti; 0)

(9.61)
A similar development leads to an expression for the probability that the next
collision for a neutron introduced in volume Vi is within that same volume Vi:
Pii = Σti V i □ 1
2π ∫
φmax
φmin
dφ ∫
ymax(φ)
ymin(φ)
dy[K i3(0) □ K i3(α(ti; 0))]
(9.62)

### Collision Probabilities for Annular Geometry

The annular geometry of a fuel pin, its clad, and the surrounding moderator is of
particular interest. For the annular geometry of Fig. 9.11, Eq. (9.61) specializes to
Pij = δijΣtj V j + 2(Si□1;j□1 □ Si□1;j □ Si;j□1 + Si;j)
(9.63)
where
Si;j ≡ ∫
Ri
[K i3(τ+
ij) □ K i3(τ□
ij)]dy
(9.64)
