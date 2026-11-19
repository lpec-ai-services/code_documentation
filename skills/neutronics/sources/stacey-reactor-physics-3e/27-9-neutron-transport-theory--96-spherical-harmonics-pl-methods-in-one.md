# 9 Neutron Transport Theory — 9.6 Spherical Harmonics (PL) Methods in One-Dimensional Geometries … 9.7 Multidimensional Spherical Harmonics (PL) Transport Theory
<!-- source PDF pages 365-382 -->

<!-- page 344 (PDF 365) -->
proposed by Wigner and with which his name is associated, is
P0 =
1 + hli=λ =
1 + 4V=Sλ =
4V=Sλ 1 □
1 + (4V=Sλ)

(9.116)
This Wigner rational approximation is known to underpredict the first-flight
escape probability. However, extensive Monte Carlo calculations have confirmed
that the first-flight escape probability depends only on the parameter 4V/Sλ, and
improved rational approximations of the form
P0 =
(4V=Sλ)
1 □
[1 + (4V=Sλ)=c]C
(
)
(9.117)
have been proposed. The Sauer approximation, developed from theoretical
considerations for cylindrical geometry, corresponds to c = 4.58. The best fit
to Monte Carlo calculations of first-flight escape probabilities for a uniform
neutron source distribution in volumes with a wide range of geometries and
values of the parameter 4V/Sλ was found by using c = 2.09.

## 9.6 Spherical Harmonics (PL) Methods in One-Dimensional Geometries

The spherical harmonics, or PL, approximation is developed by expansion of the
angular flux and the differential scattering cross section in Legendre polynomials.

### Legendre Polynomials

The first few Legendre polynomials are
P0(μ) = 1; P2(μ) = 1
2 (3μ2 □ 1)
P1(μ) = μ; P3(μ) = 1
2 (5μ3 □ 3μ)
(9.118)
and higher order polynomials can be generated from the recursion relation
(2n + 1)μ Pn(μ) = (n + 1)Pn+1(μ) + nPn□1(μ)
(9.119)
The Legendre polynomials satisfy the orthogonality relation
∫
□1
dμ Pm(μ)Pn(μ) = 2δmn
2n + 1
(9.120)

<!-- page 345 (PDF 366) -->
With reference to Fig. 9.17, the Legendre polynomials of μ0 = cos θ0, the cosine
of the angle, between μ´ and μ, can be expressed in terms of the Legendre
polynomials of μ´ and μ by the addition theorem
Pn(μ0) = Pn(μ)Pn(μ´)
+ 2
X
n
m=1
(n □ m)!
(n + m)! Pm
n (μ´)Pm
n (μ)cos m(ϕ □ ϕ´)
(9.121)
where the associated Legendre functions are defined by
Pm
n (μ) ≡ (1 □ μ2)m=2 dmPn(μ)
dμm
(9.122)

### Neutron Transport Equation in Slab Geometry

Consider a situation in which there is symmetry in the y- and z-coordinate
directions but a variation in properties in the x-coordinate direction. The
θ
θʹ
θ0
Ωʹ
Ω
φʹ
φ
Z
Y
X
Fig. 9.17 Scattering from Ω´ to Ω.

<!-- page 346 (PDF 367) -->
steady-state neutron transport eq. (9.5) in this case becomes
μ @ψ(x; μ)
@x
+ Σt(x; μ)ψ(x; μ)
= ∫
□1
Σs(x; μ´ ! μ)ψ(x; μ´)dμ´ + S(x; μ)
= ∫
□1
Σs(x; μ0)ψ(x; μ´)dμ´ + S(x; μ)
(9.123)
where, with reference to Fig. 9.17, we take advantage of the fact that the scattering
from a cone of directions μ´ = cos θ´ to a cone of directions μ = cos θ only depends
on μ0 = cos θ0, the cosine of the angle between μ´ and μ, and not on the incident
and exiting directions for the scattering event.

### PL Equations

The PL equations are based on the approximation that the angular dependence
of the neutron flux can be expanded in the first L + 1 Legendre
polynomials:
ψ(x; μ) =
X
L
l=0
2l + 1
ϕl(x)Pl(μ)
(9.124)
The angular dependence of the differential scattering cross section is also
expanded in Legendre polynomials:
Σs(x; μ0) =
X
M
m=0
2m + 1
Σsm(x)Pm(μ0)
(9.125)
When these expansions are used in Eq. (9.123), the addition theorem of Eq.
(9.121) is used to replace Pm(μ0) with Pm(μ) and Pm(μ´), the recursion relation of
Eq. (9.119) is used to replace μPn(μ) terms with Pn±1(μ) terms, the resulting
equation is multiplied in turn by Pk(μ) (k = 0 to L) and integrated over □ 1 ≤
μ ≤ 1, and the orthogonality relation of Eq. (9.120) is used, the L + 1 PL
equations
dϕ1(x)
dx
+ (Σt □ Σso)ϕ0(x) = S0(x);
n = 0
n + 1
2n + 1
dϕn+1(x)
dx
+
n
2n + 1
dϕn□1
dx
+ (Σt □ Σsn)ϕn(x) = Sn(x);
n = 1; . . . ; L
(9.126)

<!-- page 347 (PDF 368) -->
are obtained. The n subscript indicates the nth Legendre moment of the angular
dependent quantity:
ϕn(x)
≡ ∫
□1
dμPn(μ)ψ(x; μ)
Sn(x)
≡ ∫
□1
dμPn(μ)S(x; μ)
Σsn(X) ≡ ∫
□1
dμ0Pn(μ0)Σs(x; μ0)
(9.127)
This set of L + 1 equations has a closure problem – they involve L + 2 unknowns.
This problem is usually resolved by ignoring the term dϕL+1/dx, which appears in
the n = L equation.

### Boundary and Interface Conditions

The true boundary condition at the left boundary xL,
ψ(xL; μ) = ψin(xL; μ);
μ > 0
(9.128)
where ψin(xL, μ > 0) is a known incident flux (ψin(xL, μ > 0) = 0 is the vacuum
boundary condition), cannot be satisfied exactly by the angular flux approximation
of Eq. (9.124), for finite L. The most obvious way to develop approximate
boundary conditions that are consistent with the flux approximation is to
substitute Eq. (9.124) into the exact boundary condition of (9.128), multiply
by Pm(μ), and integrate over 0 ≤ μ ≤ 1. Since it is the odd Legendre polynomials
that represent directionality (i.e., are different for μ and □μ), this procedure is
repeated for all the odd Legendre polynomials m = 1, 3, . . . , L (or L □ 1) as
weighting functions to obtain, with the use of the orthogonality relation of
Eq. (9.120), the Marshak boundary conditions
∫
dμ Pm(μ)
X
N
n=0
2n + 1
ϕn(xL)Pn(μ) ≡ ϕm(xL) = ∫
dμ Pm(μ)ψin(xL; μ);
m = 1; 3; . . . ; L (or L □ 1)
(9.129)
Equations (9.129) constitute a set of (L + 1)/2 boundary conditions. An additional
(L + 1)/2 boundary conditions are obtained similarly for the right boundary. The
Marshak boundary conditions ensure that the exact inward partial current at the
boundary is incorporated into the solution; that is,
J+(xL) ≡ ∫
dμ P1(μ)
X
N
n=0
2n + 1
ϕn(xL)Pn(μ)
≡ ∫
dμ P1(μ)ψin(xL; μ) ≡ J+
in(xL)
(9.130)

<!-- page 348 (PDF 369) -->
A less intuitive set of Mark boundary conditions arises from requiring that the
flux expansion of Eq. (9.124) satisfy the boundary condition
X
N
n=0
2n + 1
ϕn(xL)Pn(μi) = ψin(xL; μi);
μi > 0
(9.131)
for the (L + 1)/2 discrete values of μi in the inward direction that are the positive
roots of PL+1(μi) = 0. Another (L + 1)/2 approximate boundary conditions are
obtained at the other boundary by requiring that the flux expansion satisfy the
true boundary condition for the (L + 1)/2 discrete values of μi in the inward
direction that are the negative roots of PL+1(μi) = 0. These Mark boundary
conditions are justified by the fact that analytical solution of the PL equations
for a source-free, purely absorbing problem in a infinite half-space leads to these
conditions. However, experience has shown that results obtained with the Mark
boundary conditions are generally less accurate than results obtained with the
Marshak boundary conditions.
A symmetry, or reflective, boundary condition ψ(xL, μ) = ψ(xL, □ μ) obviously
requiresthatalloddmomentsofthefluxvanish(i.e.,ϕn(xL) = 0forn = 1,3, . . . ,odd).
The exact interface condition of continuity of angular flux
ψ(xs □ ε; μ) = ψ(xs + ε; μ)
(9.132)
where ϵ is a vanishingly small distance, cannot, of course, be satisfied exactly by
the flux approximation of Eq. (9.124), for finite L. Following the same procedure
as for Marshak boundary conditions, we replace the exact flux with the expansion
of Eq. (9.124) and require that the first L + 1 Legendre moments of this relation be
satisfied (i.e., multiply by Pm and integrate over □1 ≤ μ ≤ 1, for m = 0, . . . , L).
Using the orthogonality relation of Eq. (9.120) then leads to the interface
conditions of continuity of the moments:
ϕn(x □ ε) = ϕn(xs + ε);
n = 0; 1; 2; . . . ; L
(9.133)
There are some subtle reasons why this approximation is not appropriate for
even-L approximations (see Ref. [4]), but since odd-L approximations are almost
always used, we will only raise a caution.

### P1 Equations and Diffusion Theory

Neglecting the dϕ2/dx term, the first two of Eqs. (9.126) constitute the P1 equations
dϕ1
dx + (Σt □ Σs0)ϕ0 = S0
dϕ0
dx + (Σt □ Σs1)ϕ1 = S1
(9.134)

<!-- page 349 (PDF 370) -->
Noting that Σs0= Σs, the total scattering cross section, and that Σs1 = μ0Σs, where μ0
is the average cosine of the scattering angle, and assuming that the source is isotropic
(i.e., S1= 0), the second of the P1 equations yields a Fick’s law for neutron diffusion
ϕ1(x) = ∫
□1
μψ(x; μ)dμ ≡ J(x) = □
3(Σt □ μ0Σs)
dϕ0
dx
(9.135)
which, when used in the first of the P1 equations, yields the neutron diffusion
equation
□ d
dx D0(x) dϕ0(x)
dx

+ (Σt □ Σs)ϕ0(x) = S0(x)
(9.136)
where the diffusion coefficient and the transport cross section are defined by
D0 ≡
3(Σt □ μ0Σs) ≡
3Σtr
(9.137)
The basic assumptions made in this derivation of diffusion theory are that the
angular dependence of the neutron flux is linearly anisotropic
ψ(x; μ) ' 1
2 ϕ0(x) + 3
2 μϕ1(x)
(9.138)
and that the neutron source is isotropic, or at least has no linearly anisotropic
component (S1 = 0). Diffusion theory should be a good approximation when these
assumptions are valid (i.e., in media for which the distribution is almost isotropic
because of the preponderance of randomizing scattering collisions, away from
interfaces with dissimilar media, and in the absence of anisotropic sources).
The boundary conditions for diffusion theory follow directly from the Marshak
condition (9.130):
J+
in(xL) = ∫
dμ P1(μ) 1
2 ϕ0(xL) + 3
2 μϕ1(xL)

= 1
4 ϕ0(xL) □ 1
2 D dϕ0(xL)
dx
(9.139)
When the prescribed incident current J+
in = 0, the vacuum boundary condition for
diffusion theory can be constructed from a geometrical interpretation of the ratio
of the flux gradient to the flux in this equation to obtain the condition that the
extrapolated flux vanishes a distance λex outside the boundary:
ϕ(xL □ λex) = 0;
λex =
3Σtr
≡ 2
3 λtr
(9.140)

<!-- page 350 (PDF 371) -->
The interface conditions of Eq. (9.133) become in the diffusion approximation
ϕ0(xs + ε) = ϕ0(xs □ ε)
□D0(xs + ε) dϕ0(xs + ε)
dx
= □D0(xs □ ε) dϕ0(xs □ ε)
dx
(9.141)

### Simplified PL or Extended Diffusion Theory

The same procedure used to derive diffusion theory from the P1 equations – solve
the odd-order equation for the odd-order moment of the flux in terms of a
gradient of the even-order flux moment and use the result to eliminate the oddorder
flux – can be used to simplify odd-L PL approximations of higher order. For
example, in the P3 approximation with an isotropic source and isotropic scattering
, the following change of variables is made
F0 = 2ϕ2 + ϕ0
F
= ϕ2
(9.142)
to facilitate the reduction of the four coupled P3 equations to the two coupled
diffusion equations
□ d
dx
D0
dF0
dx
+ (Σt □ Σs0)F0 = S0 + 2(Σt □ Σs0)F1
□ d
dx
D1
dF1
dx
+ 5
3 (Σt □ Σs2) + 4
3 (Σt □ Σs0)

F1
= □ 2
3 S0 + 2
3 (Σt □ Σs0)F0
(9.143)
where
D1 ≡
7(Σt □ Σs3)
(9.144)
The Marshak vacuum (J+
in = 0) boundary conditions of Eq. (9.129) become
2 F0(xL) □ 3
8 F1(xL) = D0
dF0(xL)
dx
□ 1
8 F0(xL) + 7
8 F1(xL) = D1
dF1(xL)
dx
(9.145)
This formulation of the PL equations allows the powerful numerical solution
techniques for diffusion theory to be used to solve a higher order transport
approximation.

<!-- page 351 (PDF 372) -->
### PL Equations in Spherical and Cylindrical Geometries

In the case of spherical symmetry, the neutron transport equation becomes
μ @ψ(r; μ)
@r
+ 1 □ μ2
r
@ψ(r; μ)
@μ
+ Σt(r)ψ(r; μ)
= ∫
□1
dμ´Σs(r; μ´ ! μ)ψ(r; μ´) + S(r; μ)
(9.146)
where r is the magnitude of the radius vector r from the center of the spherical
geometry and μ = Ω □ r. Following the same procedure as of expanding the angular
dependence of the flux and differential scattering cross section according to Eqs.
(9.124) and (9.125) and making use of the addition theorem, orthogonality
relations, and the recursion relation
(1 □ μ2) d Pm
dμ (μ) = (m + 1) μ Pm(μ) □ Pm+1(μ)
[
]
(9.147)
yields the PL equations in spherical geometry:
dϕ1
dr + 2
r ϕ1 + (Σt □ Σs0)ϕ0 = S0;
n = 0
n + 1
2n + 1
dϕn+1
dr
+ n + 2
r
ϕn+1
+
n
2n + 1
dϕn□1
dr
□ n □ 1
r
ϕn□1
+ (Σt □ Σsn)ϕn = Sn;
n = 1; . . . ; L
(9.148)
For cylindrical symmetry, the formalism becomes more complex because the
angular flux depends on two components of the neutron direction vector Ω, instead
of one as in the case of slab and spherical symmetry. With reference to Fig. 9.18, μ is
definedwithrespecttotheangleθ betweenΩ andthecylindricalaxis,which istaken
in the z-direction, and φ is defined as the angle in the x–y plane between the x–y
projection of Ω and the radius vector r, noting that Ωp/sin θ is a unit vector:
μ = cos θ = Ω ? nz;
φ = cos□1 r ? Ωp
sin θ
(9.149)
The neutron transport equation in systems with cylindrical symmetry becomes
sin θ cos φ @ψ(r; μ; φ)
@r
□ sin θ
@ψ(r; μ; φ)
@φ

+ Σt(r)ψ(r; μ; φ)
= ∫
4π
dΩΣs(r; Ω ? Ω´)ψ(r; μ´; φ´) + S(r; μ; φ)
(9.150)

<!-- page 352 (PDF 373) -->
The expansion of the angular dependence of the differential scattering cross
section is written in this coordinate system as
Σs(r; Ω ? Ω´)
= Σs(r; μ0)
2π
= 1
2π
X
L
l´=0
2l´ + 1
Σsl´(r)Pl´(μ0)
= 1
2π
X
L
l´=0
2l´ + 1
Σsl´(r)
□ Pl´(μ)Pl´(μ´) + 2
X
l´
m=0
(l´ □ m)!
(l´ + m)! Pm
l´ (μ)Pm
l´ (μ´)cosm(φ □ φ´)
"
(9.151)
where the addition theorem for Legendre polynomials has been used in the last
step. Using this expansion in Eq. (9.150) and multiplying, in turn, by all functions
Ω
Ωp
φ
θ
Z
Y
Z
Y
X
X
r
Fig. 9.18 Nomenclature for cylindrical geometry PL equations.

<!-- page 353 (PDF 374) -->
Pm
l (μ)cos(mφ) for which l ≤ L, and making use of the recursion relations
(l + m □ 1)(l + m)Pm□1
l□1 (μ) □ (l □ m + 1)(l □ m + 2)Pm□1
l+1 (μ)
= (2l + 1)
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
Pm
l (μ);
m ≠0
Pm+1
l+1 (μ) □ Pm+1
l□1 (μ) = (2l + 1)
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
Pm
l (μ)
(9.152)
(where it is understood here and further that terms with negative super- or
subscripts are to be omitted) and the orthogonality relations
∫
2π
dφ∫
□1
dμ Pm
l (μ)Pm´
l´ (μ) cos mφ cos m´φ
=
π 2(l + m)!δll´δmm´
(2l + 1)(l □ m)! ; m ≠0
2π
2l + 1 δll´δmm´;
m = 0
>
>
>
<
>
>
>
:
(9.153)
leads to the PL equations with an isotropic source in systems with cylindrical
symmetry:
Jm+1
l
+ Jm□1
l
+ (Σt □ Σsl)ϕm
l = Sδl0;
l = 0; . . . ; L □ 1;
m = 1; . . . ; l
(1 □ δm0)(L + m □ 1)(L + m)
2(2L + 1)
d
dr ϕm□1
L□1 □ (m □ 1) ϕm□1
L□1
r

□ 1 + δm0
2(2L + 1)
d
dr ϕm+1
L□1 + (m + 1) ϕm+1
L□1
r

+ (Σt □ ΣsL)ϕm
L = 0;
l = L;
m = 1; . . . ; L
(9.154)
where
Jm+1
l
≡ 1
2 (1 + δm0)
dϕm+1
l+1
dr
+ (m + 1) ϕm+1
l+1
r

□ dϕm+1
l□1
dr
+ (m + 1) ϕm+1
l□1
r

(2l + 1)
Jm□1
l
≡ 1
2 (1 □ δm0) (l + m □ 1)(l + m) dϕm□1
l□1
dr
□ (m □ 1) ϕm□1
l□1
r

□ (l □ m + 1)(l □ m + 2)
□ dϕm□1
l+1
dr
□ (m □ 1) ϕm□1
l+1
r

(2l + 1)
(9.155)

<!-- page 354 (PDF 375) -->
The PL equations are equations for the L + 1 flux moments
ϕm
l (r) ≡ ∫
□1
dμ Pm
l (μ)∫
2π
dφ cos mφψ(r; μ; φ)
(9.156)
in terms of which the angular flux distribution is given by
ψ(r; μ; φ) =
X
L
l=0
2l + 1
4π
X
l
m=□l
(l □ m)!
(l + m)! ϕm
l (r)Pm
l (μ)cos mφ
(9.157)
Either the Mark or Marshak boundary conditions are applicable in spherical or
cylindrical geometry, on the exterior boundary, but these provide only (L + 1)/2
conditions. The other (L + 1)/2 conditions are provided by the requirement for
symmetry about the origin, which requires the odd flux moments to vanish at the
origin. The Marshak form of the interface continuity conditions are also applicable
in these geometries.

### Diffusion Equations in One-Dimensional Geometry

The P1 equations may be reduced to a diffusion theory form for spherical and
cylindrical geometries. In general, letting r be the spatial coordinate upon which
the flux distribution depends, the P1 equations may be reduced to
□ 1
rn
d
dr rnD0
dϕ(r)
dr

+ Σt(r) □ Σs0
[
]ϕ(r) = S0(r)
(9.158)
where n = 0 for planar geometry, 1 for cylindrical geometry, and 2 for spherical
geometry.
The reduction of the PL equations to coupled diffusion equations that was
discussed for slab geometry is not possible in spherical and cylindrical geometries
because it is not possible to eliminate coupling terms containing spatial derivatives
of the Legendre flux moments. Thus, the efficient diffusion theory solution
procedures cannot be employed with the spherical and cylindrical PL equations,
and other, generally less efficient iterative methods must be used (e.g., Ref. [4]).

### Half-Angle Legendre Polynomials

The efficacy of the PL method depends on the validity of representing the angular
dependence of the neutron flux as a low-order continuous polynomial expansion
over □1 ≤ μ ≤ 1. There are situations in which the flux may be highly directional
and thus not well represented by a continuous polynomial expansion over both
forward and backward directions, but in which the flux may be well represented
by separate low-order polynomial expansions over the forward and backward
directions. The half-angle Legendre polynomials have been developed for this
purpose. The forward (μ > 0) and backward (μ < 0) half-angle Legendre

<!-- page 355 (PDF 376) -->
polynomials are defined as
p+
l (μ) ≡ Pl(2μ □ 1);
μ > 0
p□
l (μ) ≡ Pl(2μ + 1);
μ < 0
(9.159)
These polynomials clearly satisfy
p+
l (0) ≡ p□
l (□1) = Pl(□1)
p+
l (1) = p□
l (0) = Pl(+1)
(9.160)
and may be shown from the orthogonality and recursion relations for the fullrange
Legendre polynomials to satisfy the orthogonality conditions
∫
p+
l (μ)p+
m(μ)dμ = ∫
□1
dμ p□
l (μ)p□
m(μ) =
δlm
2l + 1
(9.161)
and to have the recursion relations
(l + 1)p+
l+1(μ) + (2l + 1)p+
l (μ) + lp+
l□1(μ) = 2(2l + 1)μp+
l (μ)
(l + 1)p□
l+1(μ) □ (2l + 1)p□
l (μ) + lp□
l□1(μ) = 2(2l + 1)μp□
l (μ)
(9.162)

### Double-PL Theory

Expanding the flux separately in each half-space 0 ≤ μ ≤ 1 and □1 ≤ μ ≤ 0,
ψ(x; μ) '
PL
l´=0(2l´ + 1)ϕ+
l´ (x)p+
l´ (μ);
μ > 0
PL
l´=0(2l´ + 1)ϕ□
l´ (x)p□
l´ (μ);
μ < 0
(
(9.163)
substituting into Eq. (9.123), weighting in turn by each p+
l (l ≤ L) and integrating
over 0 ≤ μ ≤ 1 and by each p□
l (l ≤ L) and integrating over □1 ≤ μ ≤ 0, and making
use of the orthogonality and recursion relations above yield a coupled set of
2(L + 1) double-PL, or D-PL, equations:
l + 1
2(2l + 1)
dϕ+
l+1
dx
+ 2l + 1
2(2l + 1)
dϕ+
l
dx +
l
2(2l + 1)
dϕ+
l□1
dx
+ Σtϕ+
l
=
X
2L+1
l´=l
2l´ + 1
C+
ll´Σsl´ϕl´ + S+
l
l + 1
2(2l + 1)
dϕ□
l+1
dx
□ 2l + 1
2(2l + 1)
dϕ□
l
dx +
l
2(2l + 1)
dϕ□
l□1
dx
+ Σtϕ□
l
=
X
2L+1
l´=l
2l´ + 1
C□
ll´Σsl´ϕl´ + S□
l ;
l = 0; 1; . . . ; L
(9.164)

<!-- page 356 (PDF 377) -->
where
c+
ll´ ≡ ∫
p+
l (μ)Pl´(μ)dμ; c□
ll´ ≡ ∫
□1
dμ p□
l (μ)Pl´(μ)
S+
l ≡ ∫
p+
l (μ)S(x; μ)dμ; S□
l ≡ ∫
□1
dμ p□
l (μ)S(x; μ)
(9.165)
The coupling between the forward (+) and backward (□) flux moment equations
comes about because of the possibility of scattering from the interval □1 ≤ μ ≤ 0 to
the interval 0 ≤ μ ≤ 1, and vice versa, as indicated by the scattering sums on the right
in Eqs. (9.164). The upper limits on these summations arise because the expansion
of thedifferentialscatteringcrosssectionwasterminatedat2L + 1.Thesescattering
terms contain full-range Legendre flux moments that must be represented in terms
of the half-range moments by using the approximate representation of the fullrange
Legendre polynomials in terms of the half-range polynomials:
Pl(μ) '
PL;l
l´=0(2l´ + 1)C+
l´lp+
l´ (μ);
μ > 0
PL;l
l´=0(2l´ + 1)C□
l´lp□
l´ (μ);
μ < 0
<
:
(9.166)
where the summation extends to l or L, whichever is smaller. This representation
leads to
ϕl(x) ≡ ∫
□1
dμP(μ)ψ(x; μ)dx
'
X
L;l
l´=0
(2l´ + 1) [C+
l´lϕ+
l´ (x) + C□
l´lϕ□
l´ (x)]
(9.167)
The final form of the D-PL equations is
l + 1
2(2l + 1)
dϕ+
l+1
dx
+ 2l + 1
2(2l + 1)
dϕ+
l
dx +
l
2(2l + 1)
dϕ+
l□1
dx
+ Σtϕ+
l
= S+
l +
X
2L+l
l´=1
(2l´ + 1)
C+
ll´Σsl´
X
L;l´
l´´=0
[C+
ll´´l´ϕ+
l´´ + C□
ll´´l´ϕ□
l´´]
l + 1
2(2l + 1)
dϕ□
l+1
dx
□ 2l + 1
2(2l + 1)
dϕ□
l
dx +
l
2(2l + 1)
dϕ□
l□1
dx
+ Σtϕ□
l
= S□
l +
X
2L+l
l´=1
(2l´ + 1)
C□
ll´Σsl´
X
L;l´
l´´=0
[C+
ll´´l´ϕ+
l´´ + C□
ll´´l´ϕ□
l´´];
l = 0; 1; . . . ; L
(9.168)
Interface and boundary conditions for the D-PL equations are straightforward
extensions of the conditions derived for the PL equations. All of the ϕ+
l and ϕ□
l are

<!-- page 357 (PDF 378) -->
continuous at interfaces. A vacuum boundary condition requires that the incoming
flux moments be zero at that boundary (e.g., a vacuum condition on the left boundary
requires that all ϕ+
l (xL) = 0, and a vacuum condition on the right boundary requires
that all ϕ□
l (xL) = 0). A symmetry, or reflective, boundary condition requires that
ϕ+
l (xL) = ϕ□
l (xL). Known incident flux conditions at the left boundary, ψin(xL, μ > 0),
or at the right boundary, ψin(xR, μ < 0), lead to boundary conditions
ϕ+
l (xL) = ∫
dμp+
l (μ)ψin(xL; μ > 0)
ϕ□
l (xR) = ∫
□1
dμp□
l (μ)ψin(xR; μ < 0)
(9.169)
The D-PL approximation results in 2(L + 1) first-order ordinary differential
equations to be solved for 2(L + 1) unknowns, the flux moments ϕ+
l and ϕ□
l . The
same number of first-order ordinary differential equations and unknown flux
moments ϕl are obtained in the P2L approximation. In problems in which the
difference in the number of neutrons moving in the forward and backward
directional half-spaces is more important than the angular distribution per se, the
D-PL approximation is more accurate than the P2L approximation with the same
number of unknowns. Thus, the D-PL approximation is to be preferred for
interface and boundary problems, whereas the P2L approximation is to be
preferred for deep penetration problems.

### D-P0 Equations

This simplest and most widely used of the D-PL methods is obtained by setting
L = 0 in the equations above and noting that C−
00 = 1 and C−
01 = 1
2:
dϕ+
dx + Σt □ 1
2 Σs0 1 + 3
4 μ0

ϕ+
0 = 1
2 Σs0 1 + 3
4 μ0
ϕ□
0 + S+
□ 1
dϕ□
dx + Σt □ 1
2 Σs0 1 + 3
4 μ0

ϕ□
0 = 1
2 Σs0 1 + 3
4 μ0
ϕ+
0 + S□
(9.170)

## 9.7 Multidimensional Spherical Harmonics (PL) Transport Theory

### Spherical Harmonics

The spherical harmonics are defined as (note that there are several normalizations
in use)
Y lm(μ; φ) =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l □ m)!
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l + m)!
p
Pm
l (μ)exp(imφ)
(9.171)

<!-- page 358 (PDF 379) -->
in terms of the previously discussed associated Legendre functions. Denoting the
complex conjugate by an asterisk, it follows that
Y l;□m(μ; φ) = (□1)mY ∗
lm(μ; φ)
(9.172)
The first few such functions are
Y 00(μ; φ)
= P0
0(μ) = P0(μ) = 1
Y 10(μ; φ)
= P0
1(μ) = P1(μ) = μ
Y 11(μ; φ)
= □ 1ffiffi
p
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
(cos φ + i sin φ)
Y 1;□1(μ; φ) = 1ffiffi
p
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
(cos φ □ i sin φ)
(9.173)
and the remaining spherical harmonics can be generated using the recursion
relation for the associated Legendre functions defined by Eq. (9.122):
(2l + 1)μPm
l (μ) = (l □ m + 1)Pm
l+1(μ) + (l + m)Pm
l□1(μ)
(9.174)
With respect to Fig. 9.19, the directional cosines along Cartesian coordinate
axes are given in terms of the spherical harmonics by
Ωz ≡ Ω ? nz = μ
Ωx ≡ Ω ? nx =
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cos φ = □ 1ffiffi
p (Y 11 □ Y 1;□1) = 1ffiffi
p (Y ∗
11 □ Y ∗
1;□1)
Ωy ≡ Ω ? ny =
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
sin φ =
iffiffi
p (Y 11 + Y 1;□1) = □iffiffi
p (Y ∗
11 + Y ∗
1;□1)
(9.175)
The spherical harmonics satisfy the orthogonality relationship
∫
□1
dμ∫
2π
dφ Y ∗
l´m´(μ; φ)Y lm(μ; φ) =
4π
2l + 1 δll´δmm´
(9.176)
and in terms of the spherical harmonics the addition theorem for Legendre
polynomials can be written
Pl(μ0) =
X
l
m=□l
Y lm(μ; φ)Y ∗
lm(μ´; φ´)
(9.177)

<!-- page 359 (PDF 380) -->
### Spherical Harmonics Transport Equations in Cartesian Coordinates

Expanding the angular dependence of the neutron flux
ψ(r; Ω) =
X
L
l=0
2l + 1
4π
X
l
m=□l
ϕlm(r)Y lm(μ; φ)
(9.178)
and the differential scattering cross section
Σs(r; μ0) =
X
L´
l´=0
2l´ + 1
4π
Σsl´(r)Pl´(μ0)
(9.179)
in spherical harmonics, substituting the expansions into the neutron transport
equation
Ω ? ∇ψ(r; Ω) + Σt(r; Ω)ψ(r; Ω)
= 1
4π ∫4π
dΩ´vΣf (r)ψ(r; Ω´) + ∫4π
dΩ´Σs(r)(r; Ω ? Ω´)ψ(r; Ω´) + S(r; Ω)
(9.180)
φ
Ω
θ
Z
Y
X
Fig. 9.19 Nomenclature for spherical harmonics.

<!-- page 360 (PDF 381) -->
multiplying by each Y ∗
lm in turn, integrating over dΩ, and making use of the
orthogonality and recursion relations and the addition theorem yields the
spherical harmonics equations for the flux moments ϕlm
2l + 1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l + m + 2)(l + m + 1)
p
□ @
@x □ i @
@y
ϕl+1;m+1
+ 1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l □ m + 2)(l □ m + 1)
p
@
@x □ i @
@y
ϕl+1;m□1
+ 1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l □ m □ 1)(l □ m)
p
@
@x + i @
@y
ϕl□1;m+1
+ 1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l + m □ 1)(l + m)
p
□ @
@x + i @
@y
ϕl□1;m□1
+
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l + m + 1)(l + m □ 1)
p
@
@z ϕl+1;m
+
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
(l + m)(l □ m)
p
@
@z ϕl□1;m
+ Σtϕlm
= Σslϕlm + δl0vΣf ϕ00 + Qlm;
l = 0; . . . ; L;
m = □l; . . . ; l
(9.181)
where Qlm is the Y ∗
lm moment of the external source and the other quantities have
been discussed previously.
This formidable set of equations is rarely solved as is; however, it provides the
basis for the development of a number of useful approximations. Note that the
equation for each flux moment ϕlm contains scattering terms involving only that
same flux moment, so that the coupling among equations for different flux
moments is entirely through the streaming terms arising from the Ω □ ∇ψ term.

### Pl Equations in Cartesian Geometry

As was the case in one dimension, the spherical harmonics equations lack closure.
When the spatial derivatives involving ϕL+1 in the l = L equation are set to zero,
the three-dimensional PL approximation is obtained. We consider the lowestorder
P1 approximation in more detail. Using Eqs. (9.173) and (9.175), it can be
shown that the flux moments are related to the scalar flux and to the currents
along the various coordinate axes:
ϕ(r) ≡ ∫ψ(r; Ω)dΩ = ϕ00
Jx(r) ≡ ∫(^nx ? Ω)ψ(r; Ω)dΩ = 1ffiffi
p (ϕ1;□1 □ ϕ11)
Jy(r) ≡ ∫(ny ? Ω)ψ(r; Ω)dΩ = □iffiffi
p (ϕ1;□1 + ϕ11)
Jz(r) ≡ ∫(nz ? Ω)ψ(r; Ω)dΩ = ϕ10
(9.182)

<!-- page 361 (PDF 382) -->
Using these relations to express the flux moments in terms of the scalar flux and
the currents, Eq. (9.178) becomes (for L = 1)
ψ(r; Ω) = 1
4π ϕ(r) + 3Ω ? J(r)
[
]
(9.183)
Using the flux moments calculated from Eqs. (9.182) in the (l = 0, m = 0),
equation (9.181) yields the exact equation (i.e., it was not necessary to discard a
derivative of a higher moment in this equation)
∇? J(r) + Σt(r)ϕ(r) = Σs0(r)ϕ(r) + vΣf (r)ϕ(r) + Q00(r)
(9.184)
Adding and subtracting the (l = 1, m = 1) and (l = 1, m = □1), Eqs. (9.181) yields
the approximate (i.e., it was necessary to discard a derivative of a higher moment
in these equations) equations
@ϕ(r)
@x
+ Σt(r)Jx(r) □ Σs1(r)Jx(r) = ∫(Ω ? nx)Q dΩ ≡ Q1x
@ϕ(r)
@y
+ Σt(r)Jy(r) □ Σs1(r)Jy(r) = ∫(Ω ? ny)Q dΩ ≡ Q1y
(9.185)
and the (l = 1, m = 0) equation yields the approximate equation
@ϕ(r)
@z
+ Σt(r)Jz(r) □ Σs1(r)Jz(r) = ∫(Ω ? nz)Q dΩ ≡ Q1z
(9.186)
Equations (9.184)–(9.186) are the three-dimensional P1 equations in Cartesian
geometry.

### Diffusion Theory

The one-dimensional P1 equations led to diffusion theory, and it is of some
interest to see if the same is true in three dimensions. Equations (9.185) and
(9.186) can be written as a Fick’s law,
J(r) = □
3[Σt(r) □ μ0Σs(r)] ∇ϕ(r) ≡ □D∇ϕ(r)
(9.187)
if the anisotropic source terms Q1 vanish. Equation (9.187) can be used in
Eq. (9.184) to obtain the three-dimensional diffusion equation in Cartesian
coordinates
□∇? D(r)∇ϕ(r) + [Σt(r) □ Σs0(r)]ϕ(r) = vΣf (r)ϕ(r) + Q00(r)
(9.188)
