# 3 Neutron Diffusion and Transport Theory — 3.11 Nodal Approximation … Problems
<!-- source PDF pages 106-124 -->

<!-- page 82 (PDF 106) -->
Thus, the solution of the finite-difference equations has a two-level iteration
hierarchy. There is an outer power iteration on the fission source and the
eigenvalue, described by Eqs. (3.122)–(3.124). Then for each of the outer iterations
, there is a series of inner relaxation iterations – described by Eq. (3.129) or
(3.131) and (3.130) – to converge the flux solution for that outer iterate of the
fission source.

### Limitations on Mesh Spacing

We can obtain some insight as to limitations on mesh spacing by considering the
source-free diffusion equation in one dimension:
d2ϕ
dx2 − ϕ
L2 = 0
(3.132)
which can be solved exactly over the mesh interval Δ = xi+1/2 − xi−1/2 centered
on xi:
ϕ(xi+1=2) = e−Δ=2Lϕ(xi) = e−Δ=Lϕ(xi−1=2)
(3.133)
The central difference finite-difference approximation (which we have been
using) of Eq. (3.132) on this interval can be written as
ϕ(xi+1=2) + ϕ(xi−1=2) =
2 +
Δ
L
"
ϕ(xi)
(3.134)
Comparing the right side of Eq. (3.134) with the exact expression for the left side
constructed from Eq. (3.133) allows us to define the difference as a measure of the
error in the finite-difference approximation:
error = 3
Δ
L
+ ∙∙∙
(3.135)
Clearly, the mesh spacing should be less than the diffusion length.

## 3.11 Nodal Approximation

In principle, once the local fuel cell heterogeneity in each fuel assembly is
replaced by effective homogenized cross sections and effective cross sections
are constructed for the control rods, the three-dimensional finite-difference
diffusion equations can be solved for the effective multiplication constant and
the neutron flux distribution everywhere in a reactor. In practice, it is seldom
practical to do so because of the large number of simultaneous equations that
must be solved. As we have seen, accuracy in the finite-difference solution
requires that the mesh spacing be smaller than the diffusion length, and a
typical LWR core is about 200 thermal diffusion lengths in each of the three
dimensions, which results in several million mesh points, hence several million
simultaneous equations.

<!-- page 83 (PDF 107) -->
One means to deal with this situation is to divide the flux solution into two
parts. The reactor core (and reflector, etc.) is divided into a relatively small
number (on the order of 100 or less) large regions, or nodes, as depicted in Fig. 3.8.
The detailed flux distribution within each node is determined from a finitedifference
calculation just within the node (or set of contiguous nodes); such
calculations need to be performed only for every different type of node, since the
solution for different nodes that have the same internal material distribution and
the same boundary conditions will be identical. The global flux distribution (i.e.,
the average value of the flux in the different nodes) and the effective multiplication
factor are then determined from a nodal calculation.
The general derivation of nodal diffusion theory methods may be illustrated by
integrating the diffusion equation
−∇? D∇ϕ + Σaϕ = v
k Σf ϕ
(3.136)
over the spatial domain of each node n to obtain
−∫Sn
d~s ? D∇ϕ + ∫V n
Σaϕdr = 1
k ∫V n
vΣf ϕdr;
n = 1; . . . ; N
(3.137)
where Gauss’s law has been used to replace the volume integral over node n, Vn, of
the divergence with the surface integral over the surface Sn bounding node n of
the normal component of the current. In general, the surface Sn bounding node n
consists of the several interfaces Snn´ between node n and the contiguous nodes n´.
Defining the average nodal flux as
ϕn ≡ 1
V n ∫V n
ϕ(r)dr
(3.138)
Node cell n’
Node cell n
Fig. 3.8 Division of a reactor into nodes. (With permission from Ref. [2].
Copyright 1976, Wiley.)

<!-- page 84 (PDF 108) -->
the definition of average nodal cross section follows immediately:
Σan ≡
ϕnV n
∫V n
Σa(r)ϕ(r)dr;
vΣf n ≡
ϕnV n ∫V n
vΣf (r)ϕ(r)dr
(3.139)
The treatment of the surface integral term, which represents node-to-node
leakage, is not so obvious. However, it is plausible that the gradient of the flux
across the surface between two adjacent nodes is proportional to the difference in
the two average nodal fluxes:
−αnn´(ϕn − ϕn´) ≡ ∫Snn´
d~s ? D∇ϕ
(3.140)
The accuracy of the nodal methods depends to a large extent on the actual
evaluation of the nodal coupling coefficients αnn´, which is discussed in some
detail in Chapter 15. A simple approximation results from using an average value
2(Dn + Dn´) for the diffusion coefficient on the interface between nodes n and n´,
and assuming the average diffusion coefficient and the flux gradient are both
constant over the interface, which yields
αnn´ ' Snn´ ? 1
2(Dn + Dn´)
lnn´
(3.141)
where lnn´ is the distance between the centers of contiguous nodes n and n´.
Collecting these results leads to the set of N nodal equations for the nodal
average fluxes and the effective multiplication constant:
−
X
n´ ∈n αnn´ϕn´ +
X
n´ ∈n
αnn´ + ΣanV n
!
ϕn = 1
k vΣf nV nϕn; n = 1; . . . ; N
(3.142)
where n´∈n indicates that the sum is over nodes n´ that are contiguous to node n.
For those nodes n located adjacent to the exterior boundary of the reactor, the
nodal equations contain the flux ϕn´ for a nonexistent node on the other side of
the boundary. For vacuum boundary conditions, this flux ϕn´ would be set to zero
in the equation for node n. For symmetry boundary conditions, ϕn´ = ϕn would be
used in the equation for node n.

## 3.12 Transport Methods

For many situations of interest (e.g., a strongly absorbing control rod), the
conditions for the validity of neutron diffusion theory are not satisfied, and a
more rigorous approximation for the transport of neutrons than the diffusion
approximation developed in Section 3.1 is required. Limiting consideration to a
“one-dimensional” medium, that is, one that is uniform in two dimensions (y and
z in Fig. 3.9), the number of uncollided neutrons arising from an isotropic source,
S0, in the differential area dA = ρdθdρ in the y–z plane at x = 0 that passes through

<!-- page 85 (PDF 109) -->
unit area at a point on the x-axis per unit time is (S0e−ΣtRdA)=4πR2. Defining the
cosine of the angle between R and x, μ ≡ nx□nR, we can write R = x/μ and make
use of ρ2 + x2 = R2 to write the total flux of uncollided neutrons arising from
a ring of a uniform plane isotropic source that passes through a point on the
x-axis as
ψ(x; μ : 0) = 1
2 S0e−ΣtR dR
R = 1
2 S0e−Σt(x=μ) d(x
μ)
(x
μ) = − 1
2 S0e−Σt(x=μ) dμ
μ
(3.143)
This expression can be used to construct the total flux of uncollided neutrons
passing through unit area at a point on the x-axis by integrating over all such rings
to obtain
ϕ(x : 0) = 1
2 S0∫
x
e−ΣtR dR
R = 1
2 S0∫
e−Σtx=μ dμ
μ ≡ 1
2 S0E1(Σtx)
(3.144)
and a similar expression for the total current of uncollided neutrons
J(x : 0) = 1
2 S0∫
x
μe−ΣtR dR
R = 1
2 S0∫
e−Σtx=μdμ = 1
2 S0E2(Σtx)
(3.145)
where
En(y) ≡ ∫
μn−2e−y=μdμ
(3.146)
z
dA
+y
O
-y
x
x
R
θ
ρ
Fig. 3.9 Coordinate system for
plane isotropic source calculation.
(With permission from Ref. [1].
Copyright 1960, McGraw-Hill.)

<!-- page 86 (PDF 110) -->
is the exponential integral function, which has the useful differentiation property:
dEn(y)
dy
= −En−1(y);
n = 1; 2; 3; . . .
(3.147)

### Transmission and Absorption in a Purely Absorbing Slab Control Plate

Consider a purely absorbing slab of thickness a inserted in a diffusing medium;
that is, a medium in which diffusion theory is appropriate, such as a homogenized
fuel–moderator lattice. Assuming that the scattering source external to
the slab is isotropic, the probability that a neutron incident on the slab is
transmitted across the absorbing slab is T ≡ J(a: 0)/J (0: 0) = E2(Σta), and the
probability that an incident neutron is absorbed in the slab is A ≡ 1 − T = 1 − E2
(Σta). Such an approximation was used in deriving the effective control cross
section in Section 3.9.

### Escape Probability in a Slab

The probability that a neutron that enters a slab region of thickness a from a
diffusing medium and suffers an isotropic scattering event at a location 0 ≤ x´ ≤ a
and then escapes from the slab across the surface at x = a without another
collision can be calculated by treating the scattering event as an isotropic source;
that is, the escaping current at x = a of “uncollided” neutrons arising from the
isotropic scattering at x = x´ is J(a: x´) = (1/2)S0E2 (Σt(a − x´)). If the scattering
source of incident neutrons is uniform over the slab, then the total current of
scattered neutrons that escapes across the surface at x = a without another
collision is
Jout(a) = ∫
a
J(a : x´)dx´ = 1
2 S0∫
a
E2 Σt(a − x´)
)dx´
= 1
S0
Σt
E3(0) − E3(Σta)
[
]
(3.148)
Noting that E3(0) = 1/2 and that the current of neutrons that escapes across the
surface at x = 0 without another collision must be the same as escape across the
surface at x = a, the “first-flight” escape probability is the sum of these two
escaping currents divided by the total scattering source aS0:
P0 ≡ Jout(a) + Jout(0)
aS0
= 1
aΣt
2 − E3(Σta)

(3.149)

### Integral Transport Formulation

Consider again the slab with a distributed isotropic source of neutrons, but now
with isotropic elastic scattering and fission, as well as absorption, represented

<!-- page 87 (PDF 111) -->
explicitly. The flux of uncollided source neutrons is
ϕ0(x) = 1
2 ∫
a
S0(x´)E1 Σt(jx − x´j)
dx´
(3.150)
If the first-collision rate at x = x´ is considered as a plane isotropic source of oncecollided
neutrons at x´, then the flux of once-collided neutrons at x due to the
once-collided source at x´ is
ϕ1(x : x´) = 1
2 Σs(x´) + vΣf (x´)
ϕ0(x´)E1 Σt(jx − x´j)
(3.151)
and the total flux of once-collided neutrons at x is found by integrating over the
distribution of first-collision sources
ϕ1(x) = ∫
a
ϕ1(x : x´)dx´
= ∫
a
2 Σs(x´) + vΣf (x´)
ϕ0(x´)

E1 Σt(jx − x´j)
dx´
(3.152)
Continuing in this vein, the flux of n-collided neutrons is given by
ϕn(x) = ∫
a
2 Σs(x´) + vΣf (x´)
ϕn−1(x´)

E1 Et(jx − x´j)
dx´
n
= 1; 2; 3; . . .
(3.153)
The total neutron flux is the sum of the uncollided, once-collided, twice-collided,
and so on fluxes
ϕ(x) ≡ ϕ0(x) +
X
n=1
ϕn(x)
= ∫
a
2 Σs(x´) + vΣf (x´)
X
n=0
ϕn+1(x´)E1 Σt(jx − x´j)
dx´
+ 1
2 ∫
a
S0(x´)E1 Σt(jx − x´j)
dx´
= ∫
a
2 Σs(x´) + vΣf (x´)
ϕ(x´)E1 Σt(jx − x´j)
dx´
+ 1
2 ∫
a
S0(x´)E1 Σt(jx − x´j)
dx´
(3.154)
Thus, we have found an integral equation for the neutron flux in a slab with
isotropic scattering and fission, with a kernel (1/2)(Σs(x´) + νΣf(x´))E1(Σt(|x − x´|))
and a first collision or external source S0E1(Σtx´).

<!-- page 88 (PDF 112) -->
### Collision Probability Method

If the volume of the slab is partitioned into discrete slab regions centered at xi with
widths Δi ≡ xi+1/2 − xi−1/2 within each of which uniform average cross sections
and a flat flux is assumed, Eq. (3.154) can be integrated over the volume of each
region, Vi = const. × Δi, and the resulting equation can be divided by Vi to obtain
ϕi =
X
j
Tj!i (Σsj + vΣf j)ϕj + S0j
h
i
(3.155)
which relates the fluxes in the various volumes by the “first-flight transmission
probabilities” T j→i:
Tj!i ≡ 1
Δj ∫Δi
dx´
∫Δj
dx 1
2 E1 α(x´; x)
)
(3.156)
where the “optical thickness” is defined
α(x´; x) ≡ ∫
x
x´Σt(x´´)dx´´

(3.157)
Since α(xj, xi) = α(xi, xj) – that is, the optical path is the same no matter which
way the neutron traverses the straight-line distance between xi and xj – there is a
reciprocity relation between the transmission probabilities
ΔiTj!i = ΔjTi!j
(3.158)
Upon multiplication by ΣtiΔi, Eq. (3.155) can be written as
ΣtiΔiϕi =
X
j
Pji [(Σsj + vΣf j)ϕj + S0j]
Σtj
(3.159)
where the collision rate in cell i is related to the neutrons introduced by scattering,
fission, and an external source in all cells j by the “collision probabilities”
Pji = ΣtiΣtj∫Δi
dx´
∫Δj
dx 1
2 E1 α(x´; x)
)
(3.160)
Because α(xi, xj) = α(xj, xi), there is also reciprocity between the collision probabilities
; that is,
Pij = Pji
(3.161)
For j ≠i, the probability that a neutron introduced in cell j has its next collision in
cell i is
Pji = 1
2 E3(αi+1=2;j+1=2) − E3(αi−1=2;j+1=2) − E3(αi+1=2;j−1=2)

+E3(αi−1=2;j−1=2)

ΣtiΣtj
(3.162)

<!-- page 89 (PDF 113) -->
where αi,j ≡ α(xi, xj).
For j = i, a similar development leads to an expression for the probability that a
neutron introduced in cell i has its next collision in cell i
Pii = ΣtiΔi 1 −
2ΣtiΔi
1 − 2E3(ΣtiΔi)
)

(3.163)
The set of Eqs. (3.159) can be solved for the neutron flux in all the cells.

### Differential Transport Formulation

Another formulation of neutron transport theory follows an approach similar to
that used in Section 3.1 to derive diffusion theory, but without some of the
limiting assumptions. Referring to Fig. 3.9, the change in the flux of particles
moving along the cone of radius vectors R making the same angle (μ is the
cosine of the angle made by the line R with respect to the normal to the y–z
plane in Fig. 3.9) with respect to a point on the x-axis within the differential
distance ΔR can be written as
ψ(R + ΔR; μ) = ψ(R; μ) + ΔR∫
−1
P
s(R; μ´ ! μ)ψ(R; μ´)dμ´
+ 1
2 ΔR∫
−1
v
X
f (R)ψ(R; μ´)dμ´
− ΔR P
s(R) + P
a(R)

ψ(R; μ)
(3.164)
The second term on the right is the source of neutrons within ΔR with direction μ
due to scattering within ΔR by neutrons with other directions μ´ (including μ).
The third term on the right is the number of source neutrons within ΔR
with direction μ due to isotropic fission produced by neutrons with other
directions μ´ (including μ). The last term on the right represents the rate at
which neutrons within ΔR with direction μ are being lost by scattering to some
other direction μ´ (including μ) and by absorption. The first assumption made is
that the directional flux can be represented by the first two terms of a Taylor’s
series, ψ(R + ΔR, μ) ' ψ(R, μ) + ΔR[dψ(R, μ)/dR]. Noting that the spatial nonuniformity
depends on the variable x and that μ = x/R, Eq. (3.164) becomes in the
differential limit ΔR →dR the one-dimensional slab version of the Boltzmann
transport equation
μ dψ(R; μ)
dx
+ Σs(R) + Σa(R)
[
]ψ(R; μ)
= ∫
−1
Σs(R; μ´ ! μ)ψ(R; μ´)dμ´ + 1
2 ∫
−1
vΣf (R)ψ(R; μ´)dμ´
(3.165)

### Spherical Harmonics Methods

The spherical harmonics, or PL, approximation is developed by expansion of the
angular dependence of the angular flux and of the differential scattering cross

<!-- page 90 (PDF 114) -->
section in Legendre polynomials. The first few Legendre polynomials are
P0(μ) = 1;
P2(μ) = 1
2 (3μ2 − 1)
P1(μ) = μ;
P3(μ) = 1
2 (5μ3 − 3μ)
(3.166)
and higher order polynomials can be generated from the recursion relation
(2n + 1)μPn(μ) = (n + 1)Pn(μ) + nPn−1(μ)
(3.167)
The Legendre polynomials satisfy the orthogonality relation
∫
−1
dμPm(μ)Pn(μ) = 2δmn
2n + 1
(3.168)
The cosine of the scattering angle between μ´ and μ, can be expressed in terms of
the Legendre polynomials of μ´ and μ by the addition theorem in one-dimension
Pn(μ0) = Pn(μ)Pn(μ´)
(3.169)
The PL equations are based on the approximation that the angular dependence
of the neutron flux can be expanded in the first L + 1 Legendre polynomials
ψ(x; μ) =
X
L
l=0
2l + 1
ϕl(x)Pl(μ)
(3.170)
The angular dependence of the differential scattering cross section is also
expanded in Legendre polynomials
Σs(x; μ0) =
X
M
m=0
2m + 1
Σsm(x)Pm(μ0)
(3.171)
When these expansions are used in Eq. (3.165), the addition theorem of
Eq. (3.169) is used to replace Pm(μ0) with Pm(μ)Pm(μ´), the recursion relation
of Eq. (3.167) is used to replace μPn(μ) terms with Pn±1(μ) terms, the resulting
equation is multiplied in turn by Pk(μ) (k = 0 to L) and integrated over −1 ≤ μ ≤ 1,
and the orthogonality relation of Eq. (3.168) is used, the L + 1 PL equations
dϕ1(x)
dx
+ (Σt − Σs0)ϕ0(x) = S0(x);
n = 0
(n + 1)
(2n + 1)
dϕn+1(x)
dx
+
n
(2n + 1)
dϕn−1
dx
+ (Σt − Σsn)ϕn(x) = Sn(x);
n = 1; . . . ; L
(3.172)

<!-- page 91 (PDF 115) -->
are obtained. The n subscript indicates the nth Legendre moment of the direction
flux, source and scattering cross section
ϕn(x) ≡ ∫
−1
dμPn(μ)ψ(x; μ)
Sn(x) ≡ ∫
−1
dμPn(μ)S(x; μ)
Σsn(x) ≡ ∫
−1
dμ0Pn(μ0)Σs(x; μ0)
(3.173)
This set of L + 1 equations has a closure problem – they involve L + 2 unknowns.
This problem is usually resolved by ignoring the term dϕL+1/dx that appears in
the n = L equation.

### Boundary and Interface Conditions

The true boundary condition at the left boundary xL
ψ(xL; μ) = ψin(xL; μ);
μ > 0
(3.174)
where ψin(xL, μ > 0) is a known incident flux (ψin (xL, μ > 0) = 0 is the vacuum
boundary condition), cannot be satisfied exactly by the angular flux approximation
of Eq. (3.170), for finite L.
The most obvious way to develop approximate boundary conditions that are
consistent with the flux approximation is to substitute Eq. (3.170) into the exact
boundary condition of (3.174), multiply by Pm(μ), and integrate over 0 ≤ μ ≤ 1.
Since it is the odd Legendre polynomials that represent directionality (i.e., are
different for μ and −μ), this procedure is repeated for all the odd Legendre
polynomials m = 1, 3, . . . , L (or L − 1) as weighting functions to obtain, with the
use of the orthogonality relation of Eq. (3.168), the Marshak boundary conditions
∫
dμPm(μ)
X
N
n=0
2n + 1

ϕn(xL)Pn(μ) ≡ ϕm(xL)
= ∫
dμPm(μ)ψin(xL;μ);
m = 1; 3; ∙∙∙; L(or L − 1)
(3.175)
Equations (3.175) constitute a set of (L + 1)/2 boundary conditions. An additional
(L + 1)/2 boundary conditions are similarly obtain for the right boundary.
The Marshak boundary conditions insure that the exact inward partial current
at the boundary is incorporated into the solution; that is,
J+(xL) ≡ ∫
dμP1(μ)
X
N
n=0
2n + 1

ϕn(xL)Pn(μ)
= ∫
dμP1(μ)ψin(xL;μ) ≡ J+
in(xL)
(3.176)

<!-- page 92 (PDF 116) -->
A symmetry, or reflective, boundary condition ψ(xL, μ) = ψ(xL, −μ) obviously
requires that all odd moments of the flux vanish; that is, ϕn(xL) = 0 for n = 1,
3, . . . , odd.
The exact interface condition of continuity of angular flux
ψ xs − ε; μ
) = ψ(xs + ε; μ)
(3.177)
where ε is a vanishingly small distance, cannot, of course, be satisfied exactly by
the flux approximation of Eq. (3.170), for finite L. Following the same procedure
as for Marshak boundary conditions, we replace the exact flux with the expansion
of Eq. (3.170) and require that the first L + 1 Legendre moments of this relation be
satisfied (i.e., multiply by Pm and integrate over −1 ≤ μ ≤ 1, for m = 0, . . . , L).
Using the orthogonality relation of Eq. (3.168) then leads to the interface
conditions of continuity of the moments
ϕn(x − ε) = ϕn(x + ε);
n = 0; 1; 2; . . . ; L
(3.178)

### P1 Equations and Diffusion Theory

Neglecting the dϕ2/dx term, the first two of Eqs. (3.172) constitute the P1 equations
dϕ1
dx + (Σt − Σs0)ϕ0 = S0
dϕ0
dx + (Σt − Σs1)ϕ1 = S1
(3.179)
Noting that Σs0 = Σs, the total scattering cross section, and that Σs1 = μΣs, where
μ0 is the average cosine of the scattering angle, and assuming that the source is
isotropic (i.e., S1 = 0), the second of these P1 equations yields a Fick’s law for
neutron diffusion
ϕ1(x) = ∫
−1
μψ(x; μ)dμ ≡ J(x) = −
3(Σt − μ0Σs)
dϕ0
dx
(3.180)
which, when used in the first of the P1 equations, yields the neutron diffusion
equation
− d
dx
D0(x) dϕ0(x)
dx

+ (Σt − Σs)ϕ0(x) = S0(x)
(3.181)
where the diffusion coefficient and the transport cross section are defined by
D0 ≡
3(Σt − μ0Σs) ≡
3Σtr
(3.182)
The basic assumptions made in this derivation of diffusion theory are that the
angular dependence of the neutron flux is linearly anisotropic:
ψ(x; μ) ' 1
2 ϕ0(x) + 3
2 μϕ1(x)
(3.183)

<!-- page 93 (PDF 117) -->
and that the neutron source is isotropic, or at least has no linearly anisotropic
component (S1 = 0). Diffusion theory should be a good approximation when
these assumptions are valid; that is, in media for which the distribution is
almost isotropic because of the preponderance of randomizing scattering
collisions, away from interfaces with dissimilar media, and in the absence of
anisotropic sources.
The boundary conditions for diffusion theory follow directly from the Marshak
condition (3.176)
J+
in(xL) = ∫
dμP1(μ) 1
2 ϕ0(xL) + 3
2 μϕ1(xL)

= 1
4 ϕ0(xL) − 1
2 D dϕ0(xL)
dx
(3.184)
When the prescribed incident current, J+
in = 0, the vacuum boundary condition
for diffusion theory can be constructed from a geometrical interpretation
of the ratio of the flux gradient to the flux in this equation to obtain the
condition that the extrapolated flux vanishes a distance λtr = 1/Σtr outside the
boundary
ϕ(xL − λex) = 0;
λex =
3Σtr
(3.185)
The interface conditions of Eq. (3.178) become in the diffusion approximation:
ϕ0(xs + ε) = ϕ0(xs − ε)
−D(xs + ε) dϕ0(xs + ε)
dx
= −D(xs − ε) dϕ0(xs − ε)
dx
(3.186)

### Discrete Ordinates Method

The discrete ordinates method is based on a conceptually straightforward
evaluation of the transport equation at a few discrete angular directions, or
ordinates, and the use of quadrature relationships to replace scattering and
fission neutron source integrals over angle with summations over ordinates.
The essence of the method is the choice of ordinates, quadrature weights,
differencing schemes, and iterative solution procedures. In one dimension, the
ordinates can be chosen such that the discrete ordinates methods are completely
equivalent to the PL method discussed above, and in fact the use of
discrete ordinates is probably the most effective way to solve the PL and D − PL
equations in one dimension.
Making use of the spherical harmonics expansion of the differential scattering
cross section of Eq. (3.171) and the addition theorem for Legendre polynomials of
Eq. (3.169), the one dimensional neutron transport equation (3.165) in slab

<!-- page 94 (PDF 118) -->
geometry becomes
μ dψ
dx (x; μ) + Σt(x)ψ(x; μ)
=
X
l´=0
2l´ + 1

Σsl´(x)Pl´(μ)∫
−1
dμ´Pl´(μ´)ψ(x; μ´) + S(x; μ)
(3.187)
where the source term includes an external source and, in the case of a multiplying
medium such as a reactor core, a fission source. We will first discuss the
solution of the fixed external source problem (which implicitly assumes a
subcritical reactor) and then return to the solution of the critical reactor problem,
in which the solution of the fixed source problem constitutes part of the iteration
strategy.
Defining N ordinate directions, μn, and corresponding quadrature weights, wn,
the integral over angle in Eq. (3.187) can be replaced by
ϕl(x) ≡ ∫
−1
dμPl(μ)ψ(x; μ) ≈
X
n
wnPl(μn)ψn(x)
(3.188)
where ψn ≡ ψ(μn). The quadrature weights are normalized by
X
N
n=1
wn = 2
(3.189)
It is convenient to choose ordinates and quadrature weights that are symmetric
about μ = 0, hence providing equal detail in the description of forward and
backward neutron fluxes. This can be accomplished by choosing
μN+1−n = −μn;
μn > 0;
n = 1; 2; . . . ; N=2
wN+1−n = wn;
wn > 0;
n = 1; 2; . . . ; N=2
(3.190)
With such even ordinates, reflective boundary conditions are simply prescribed
ψn = ψN+1−n;
n = 1; 2; . . . ; N=2
(3.191)
Known incident flux, ψin(μ), boundary conditions, including vacuum conditions
when ψin(μ) = 0, are
ψn = ψin(μn);
n = 1; 2; . . . ; N=2
(3.192)
Normally, an even number of ordinates is used (N = even) because this results
in the correct number of boundary conditions and avoids certain other problems
encountered with N = odd. Even with these restrictions, there remains considerable
freedom in the choice of ordinates and weights.
If the ordinates are chosen to be the L roots of the Legendre polynomial of
order N
PN(μi) = 0
(3.193)

<!-- page 95 (PDF 119) -->
and the weights are chosen to correctly integrate all Legendre polynomials up to
PN−1
∫
−1
Pl(μ)dμ =
X
N
n=1
wnPl(μn) = 2δl0;
l = 0; 1; . . . ; N − 1
(3.194)
then the discrete ordinates equations with N ordinates are entirely equivalent to
the PN−1 equations. To establish this, we multiply Eq. (3.187) by wnPl(μn) for
0 ≤ l ≤ N − 1, in turn, and use the recursion relation of Eq. (3.167) to obtain
wn
l + 1
2l + 1

Pl+1(μn) +
l
2l + 1

Pl−1(μn)

 dψn
dx + wnΣtψn
=
X
N−1
l´=0
2l´ + 1

Σsl´wnPl´(μn)Pl(μn)ϕl´ + wnPl(μn)S(μn);
l = 0; . . . ; N − 1;
n = 1; . . . ; N
(3.195)
Summing these equations over 1 ≤ n ≤ N yields
l + 1
2l + 1

 dϕl+1
dx
+
l
2l + 1

 dϕl−1
dx
+ Σtϕl
=
X
N−1
l´=0
2l´ + 1

Σsl´ϕl´
X
N
n=0
wnPl´(μn)Pl(μn)
"
+
X
N
n=1
wnPl(μn)S(μn);
l = 0; . . . ; N − 1
(3.196)
Weights chosen to satisfy Eqs. (3.194) obviously correctly integrate all polynomials
through order N (any polynomial of order n can be written as a sum of
Legendre polynomials through order n), but fortuitously they also integrate
correctly all polynomials through order less than 2N. Thus, the term in the
scattering integral becomes
X
N
n=1
wnPl´(μn)Pl(μn) = ∫
−1
Pl´(μ)Pl(μ)dμ = 2δll´
2l + 1
(3.197)
and assuming that the angular dependence of the source term can be represented
by a polynomial of order < 2N
X
N
n=1
wnPl(μn)S(μn) = ∫
−1
Pl(μ)S(μ)dμ =
2Sl
2l + 1
(3.198)

<!-- page 96 (PDF 120) -->
where Sl is the Legendre moment of the source given by Eq. (3.173).
Using Eqs. (3.197) and (3.198), Eqs. (3.196) become
l + 1
2l + 1

 dϕl+1
dx
+
l
2l + 1

 dϕl−1
dx
+ (Σt − Σsl)ϕl = Sl
l = 0; . . . ; N − 2
N − 1
2(N − 1) + 1
dϕ(N−1)−1
dx
+ (Σt − Σs;N−1)ϕN−1 = SN−1
l = N − 1
(3.199)
which, when ϕ−1 is set to zero, are identically the PL equations (3.172) for
L = N − 1.

## References

1 R. V. MEGHREBLIAN and D. K. HOLMES, Reactor Analysis, McGraw-Hill, New York
(1960), pp. 160–267 and 626–747.
2 J. J. DUDERSTADT and L. J. HAMILTON, Nuclear Reactor Analysis, Wiley, New York
(1976), pp. 149–232 and 537–556.
3 A. M. WEINBERG and E. P. WIGNER, The Physical Theory of Neutron Chain
Reactors, University of Chicago Press, Chicago (1958), pp. 181–218, 495–500,
and 615–655.
4 E. L. WACHSPRESS, Iterative Solution of Elliptic Systems, Prentice Hall, Englewood
Cliffs, NJ (1966). Another widely used method for solving the two-dimensional
diffusion equations is the alternating direction implicit iteration scheme
described in Section 14.3.

## Further Readings

BELL G. I. and GLASSTONE S., Nuclear Reactor Theory, Van Nostrand Reinhold, New
York (1970), pp. 89–91, 104–105, and 151–157.
BUTLER M. K. and COOK J. M., “One Dimensional Diffusion Theory,” and A. HASSITT,
“Diffusion Theory in Two and Three Dimensions,” in H. Greenspan, C. N. Kelber,
and D. Okrent, eds., Computing Methods in Reactor Physics, Gordon and Breach,
New York (1968).
CLARKE M. and HANSEN K. F., Numerical Methods of Reactor Analysis, Academic
Press, New York (1964).
GLASSTONE S. and EDLUND M. C., Nuclear Reactor Theory, D. Van Nostrand,
Princeton, NJ (1952), pp. 90–136, 236–272, and 279–289.
HENRY A. F., Nuclear-Reactor Analysis, MIT Press, Cambridge, MA (1975),
pp. 115–199.

<!-- page 97 (PDF 121) -->
LAMARSH J. R., Introduction to Nuclear Reactor Theory, 2nd ed., Addison-Wesley,
Reading, MA (1983), Chaps. 5, 6, 8, 9, and 10.
STAMM’LER R. J. J. and ABBATE M. J., Methods of Steady-State Reactor Physics in
Nuclear Design, Academic Press, London (1983), Chap. 5.
VONDY D. R., “Diffusion Theory,” in Y. Ronen, ed., CRC Handbook of Nuclear
Reactor Calculations I, CRC Press, Boca Raton, FL (1986).

## Problems

### 3.1

Plot the neutron flux distribution given by Eq. (3.24) from r = 0 to r = 25 cm
away from a point thermal neutron source in an infinite medium of (a) H2O
(L = 2.9 cm, D = 0.16 cm); (b) D2O (L = 170 cm, D = 0.9 cm); and (c) graphite
(L = 60 cm, D = 0.8 cm).

### 3.2

Plot the neutron flux distribution in a finite slab of width 2a = 10 cm with
an incident thermal neutron beam from the left, as given by Eq. (3.36), for
an iron slab (Σt = 1.15 cm−1, D = 0.36 cm, L = 1.3 cm).

### 3.3

Derive the albedo boundary condition of Eq. (3.38) from the definition of
the albedo, α ≡ j−/j+, and the diffusion theory expressions for partial
currents, Eqs. (3.4) and (3.5).

### 3.4

A thermal diffusion-length experiment is performed by placing a block of
diffusing medium with aex = bex = 175.7 cm adjacent to a reactor thermal
column port and irradiating a series of indium foils placed along the z-axis
of the block. The saturation activity (disintegrations/min) of foils at various
locations is (40,000 at z = 28 cm), (29,000 at z = 40 cm), (20,000 at z =
45 cm), (17,000 at z = 56 cm), (10,000 at z = 70 cm), (8500 at z = 76 cm),
(5800 at 90 cm), and (3500 at 100 cm). The experimental error is ±10%.
Determine the thermal neutron diffusion length.

### 3.5

Derive the criticality condition for a bare rectangular parallelepiped core of
x-dimension a, y-dimension b, and z-dimension c.

### 3.6

A typical composition for a PWR core is: H, 2.75 × 1022 cm−3; O,
2.76 × 1022 cm−3;
Zr,
3.69 × 1021 cm−3;
Fe,
1.71 × 1021 cm−3;
235U
1.91 × 1020 cm−3; 238U, 6.59 × 1021 cm−3; and 10B, 1 × 1019 cm−3. Appropriate
spectrum-averaged microscopic cross sections (barns) for these
isotopes are σtr/σa/νσf = 0.65/0.29/0.0 for H, 0.26/0.0002/0.0 for O,
0.79/0.19/0.0 for Zr, 0.55/2.33/0.0 for Fe, 1.62/484.0/758.0 for
235U,
1.06/2.11/1.82 for 238U, and 0.89/3410.0/0.0 for 10B. Calculate the critical
radius for a right circular cylindrical bare core of fixed height H = 375 cm.

### 3.7

Calculate the critical radius for the right circular cylindrical core of
Problem 3.6 with a 20-cm-thick side reflector with DR = 1 cm and
ΣaR = 0.01 cm−1.

<!-- page 98 (PDF 122) -->
### 3.8

Calculate the thermal flux disadvantage factor for UO2 rods varying from
0.5 to 2.0 cm in diameter in an H2O moderator for VM/VF varying from 1.0
to 4.0. Calculate the corresponding effective homogeneous absorption
cross sections and thermal utilization. Plot the results.

### 3.9

Derive an expression analogous to Eq. (3.100) for the power peaking factor
in a fuel–moderator assembly with cylindrical fuel elements.

### 3.10

Derive an expression for the effective diffusion theory absorption cross
section for a cylindrical control rod of radius a surrounded by an annular
region of fuel–moderator extending from r = a to r = R. The transport
parameter for this geometry is given by (1/3α) = 0.7104 + 0.2524/aΣaC +
0.0949/(aΣaC)2+ ∙∙∙.

### 3.11

∗Jezebel is a bare, critical, spherical fast reactor assembly with radius
6.3 cm constructed of 239Pu metal (density 15.4 g/cm3). Using the onegroup
constants ν = 2.98, σf = 1.85 barns (1 barn = 10−24 cm2), σa =
2.11 barns, and σtr = 6.8 barns and the finite-difference numerical method,
calculate the effective multiplication constant, λ = keff, predicted by diffusion
theory. λ − 1 is a measure of the accuracy of diffusion theory for this
assembly. Should diffusion theory be valid for this assembly?

### 3.12

∗Solve numerically for the eigenvalue and neutron flux distribution in a
slab reactor consisting of two adjacent core regions each of thickness
50 cm, with a 25-cm-thick reflector on each side. The nuclear parameters
of the two core regions are (D = 0.65 cm, Σa = 0.12 cm−1, and νΣf =
0.125 cm−1) and (D = 0.75 cm, Σa = 0.11 cm−1, and νΣf = 0.12 cm−1), and
the parameters of the reflector are (D = 1.15 cm, Σa = 0.01 cm−1, and
νΣf = 0.0 cm−1). Solve this problem analytically and compare the answers.

### 3.13

∗Calculate numerically the effective multiplication constant and the flux
distribution in a reactor with rectangular (x, y) cross section which is
sufficiently tall that axial (z) leakage can be neglected. The core cross
section in the x–y plane consists of four symmetric quadrants. The upper
right quadrant consists of core region 1, rectangular (0 < x < 50 cm, 60 <
y < 100 cm); core region 2, rectangular (0 < x < 50 cm, 0 < y < 60 cm); and
reflector region 3, also rectangular (50 < x < 100 cm, 0 < y < 100 cm). The
nuclear parameters are: core region 1 (D = 0.65 cm, Σa = 0.12 cm−1,
νΣf = 0.185); core region 2 (D = 0.75 cm, Σa = 0.10 cm−1, νΣf = 0.15); and
reflector region 3 (D = 1.15 cm, Σa = 0.01 cm−1, νΣf = 0.0 cm−1). Use vacuum
boundary conditions except on the boundaries (x = 0, 0 < y < 100 cm)
and (0 < x < 100 cm, y = 0), where a symmetry condition should be used.
(This is a model for one-half of the symmetric reactor cross section.) Plot
the x-direction flux distribution at y = 30 and 80 cm.
∗Problems 11 to 13 are longer problems suitable for take-home projects.

<!-- page 99 (PDF 123) -->
### 3.14

Calculate thethermalextrapolationdistanceλextrapforH2O andfora 1:1 wt%
homogeneous mixture of H2O and 4% enriched uranium.

### 3.15

Estimate the maximum size of the mesh spacing that can be used in a finitedifference
solution for the thermal neutron flux distribution in an H2O
medium and in a 1:1 wt% homogeneous mixture of H2O and 4% enriched
uranium.

### 3.16

Calculate and plot the thermal neutron flux distribution arising from a
plane neutron source in an H2O medium and in a 1:1 wt% homogeneous
mixture of H2O and 4% enriched uranium.

### 3.17

Repeat the calculation of Problem 3.16 in a carbon medium and in a 1:1 wt%
homogeneous mixture of carbon and 4% enriched uranium.

### 3.18

Calculate the albedo boundary condition for the thermal neutron flux in a
1-m-thick slab medium with a 1:1 wt% homogeneous mixture of H2O and
4% enriched uranium that is bounded on both sides by very thick graphite
slabs.

### 3.19

Using the microscopic cross sections and number densities (except for
235U) of Table 3.4, determine the critical 235U enrichment for a bare
cylindrical core of height H = 350 cm and radius R = 110 cm. Repeat the
calculation for R = 100 and 120 cm.

### 3.20

Repeat the calculation in Section 3.8 (Example 3.4) of flux disadvantage
factor and effective homogenized fuel absorption cross section for a water
thickness of 2 and 5 cm between fuel plates.

### 3.21

Calculate the power peaking factor in the slab lattices of Problem 3.20.

### 3.22

Repeat the calculation of the effective control slab cross section given in
Section 3.9 (Example 3.5) for a control blade that contains only 2% natural
boron.

### 3.23

Solve Problem 3.12 using a four-node model, one node for each reflector
and core region. Compare the result with the results of Problem 3.12.

### 3.24

Discuss the approximations made in the derivation of neutron diffusion
theory and how these approximations limit the validity of diffusion theory
in reactor calculations. Explain why diffusion theory is not directly valid for
the calculation of the flux distribution within the highly heterogeneous
assembly of fuel, moderator, structure and control elements that make up a
typical LWR fuel region. Describe how an effective homogeneous model of
this heterogeneous assembly can be constructed for which diffusion theory
is valid.

<!-- page 100 (PDF 124) -->
### 3.25

Calculate the critical (k = 1) dimension of a bare cube of multiplying
medium with average macroscopic cross sections νΣf = 0.115 cm−1,
Σa = 0.113 cm−1, Σtr = 0.3 cm−1.

### 3.26

A single rod containing a spontaneous fission source is placed in a large
volume of moderating material and surrounded at different radial distances
with foils containing a material with a large 1/υ capture cross
section. The foil activation is measured. Explain how the radial distribution
of the foil activation rate could be used to determine the migration length
of neutrons in the moderating material.
