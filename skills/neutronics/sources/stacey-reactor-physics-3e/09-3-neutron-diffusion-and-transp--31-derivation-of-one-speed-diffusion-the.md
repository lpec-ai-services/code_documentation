# 3 Neutron Diffusion and Transport Theory — 3.1 Derivation of One-Speed Diffusion Theory … 3.6 Bare Homogeneous Reactor
<!-- source PDF pages 67-85 -->

<!-- page 43 (PDF 67) -->
# 3 Neutron Diffusion and Transport Theory

In this chapter we develop a one-speed diffusion theory mathematical description
of nuclear reactors. Such a relatively simple description has the great advantage of
illustrating many of the important features of nuclear reactors without the
complexity that is introduced by the treatment of important effects associated
with the neutron energy spectrum and with highly directional neutron transport,
which are the subjects of subsequent chapters. Moreover, diffusion theory is
sufficiently accurate to provide a quantitative understanding of many physics
features of nuclear reactors and is, in fact, the workhorse computational method
of nuclear reactor physics.

## 3.1 Derivation of One-Speed Diffusion Theory

Calculation of the rates of the different reactions of neutrons with the materials in
the various parts of a nuclear reactor is the fundamental task of nuclear reactor
physics. This calculation requires a knowledge of nuclear cross sections and their
energy dependence (Chapter 1) and of the distribution of neutrons in space and
energy throughout the reactor. The neutron distribution depends on the neutron
source distribution, which in the case of the fission source depends on the neutron
distribution itself, and on the interactions with atomic nuclei experienced by the
neutrons as they move away from the source. The simplest and most widely used
mathematical description of the neutron distribution in nuclear reactors is
provided by neutron diffusion theory. For simplicity of explication, the neutrons
are treated as if they are all of one effective speed, and effects associated with
changes in neutron energy are suppressed. Such a simplification would be
justified in practice if the cross sections were averaged over the appropriate
neutron energy distribution. As a further simplification, the medium is initially
assumed to be uniform.

### Partial and Net Currents

With respect to Fig. 3.1, the rate at which neutrons are scattering in the
differential volume element dr = r2drdμdψ is Σsϕdr, where μ ≡ cos θ, the macroscopic
cross section Σ ≡ Nσ is the product of the number density of atomic nuclei
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 44 (PDF 68) -->
and the microscopic cross section discussed previously, and the neutron scalar
flux ϕ ≡ nυ is the product of the neutron density and the neutron speed. The
fraction of the isotropically scattered neutrons leaving dr headed toward the
differential area dA at the origin is −(r/r)□dA/4πr2 = μdA/4πr2. Not all of these
neutrons reach dA, however; some are absorbed and others are scattered again so
that they do not cross dA. The probability that a neutron leaving dr in the
direction of dA actually reaches dA is e−Σr. The differential current j−(0: r, μ, ψ)
drdA of neutrons passing downward through dA that had their last scattering
collision in dr is thus
j−(0 : r; μ; ψ)drdA = μe−ΣrΣsϕ(r; μ; ψ)drdA
4πr2
(3.1)
The total current passing downward through dA is found by integrating this
expression over the entire upper half-plane (x > 0):
j−(0)dA = Σ∫
dr∫
2π
dψ∫
dμμe−Σrϕ(r; μ; ψ) dA
4π
(3.2)
ψy
ψ
𝛁ϕ
θx
θ
y
z
dr
dA
x
r(r,θ,ψ)
β
Fig. 3.1 Definition of coordinate system. (With permission from Ref. [1]. Copyright 1960,
McGraw-Hill.)

<!-- page 45 (PDF 69) -->
Now, the first major approximation leading to diffusion theory is made – for
the purpose of evaluating the integral in Eq. (3.2), the flux is assumed to be
sufficiently slowly varying in space that it can be approximated by expansion in a
Taylor series about the origin:
ϕ(r) = ϕ(0) + r ? ∇ϕ(0) + 1
2 r2∇2ϕ(0)

+ ∙∙∙
(3.3)
in which only the first two terms are retained. Using this approximation and the
trigonometric identity cos β = cos θx cos θ + sin θx sin θ cos(ψy − ψ), and making
the second major approximation – that absorption is small relative to scattering
(e.g., Σ ∼Σs) – Eq. (3.2) can be integrated to obtain the diffusion theory expression
for the partial downward current density:
j−(0) = 1
4 ϕ(0) + 1
6Σs
j∇ϕ(0)jcosθx = 1
4 ϕ(0) + 1
6Σs
dϕ(0)
dx
≡ 1
4 ϕ(0) + 1
2 D dϕ(0)
dx
(3.4)
A similar derivation leads to an expression for the partial upward current
density,
j+(0) = 1
4 ϕ(0) − 1
2 D dϕ(0)
dx
(3.5)
where D is known as the diffusion coefficient.
The diffusion theory expression for the net current at the origin (positive sign
up) is
Jx(0) = j+(0) − j−(0) = − 1
3Σs
dϕ(0)
dx
= −D dϕ(0)
dx
(3.6)
Carrying out a similar derivation for dA in the x–y and x–z planes leads
immediately to the three-dimensional generalization:
J(0) = − 1
3Σs
∇ϕ(0) ≡ −D∇ϕ(0)
(3.7)
A third assumption – that the neutrons are scattered isotropically – was used in
the derivation above. The last form of Eq. (3.7) is known as Fick’s law, which
governs the diffusion of many other quantities as well as neutrons. A more
accurate derivation of diffusion theory from transport theory (Section 3.12)
reveals that a better approximation for the diffusion coefficient that takes into
account anisotropy in scattering is given by
D =
3(Σt − μ0Σs) ≡
3Σtr
(3.8)
where Σt and Σs are the total and scattering cross sections and μ0 ≈ 2
3A is the
average cosine of the scattering angle (A is the atomic mass number of the
scattering nuclei).

<!-- page 46 (PDF 70) -->
### Diffusion Theory

The mathematical formulation of neutron diffusion theory is then obtained by
using the diffusion theory expression for the neutron current in the neutron
balance equation on a differential volume element:
@n
@t = S + vΣf ϕ − Σaϕ − ∇? J
= S + vΣf ϕ − Σaϕ + ∇? D∇ϕ
(3.9)
which states that the time rate of change of the neutron density within a
differential volume is equal to the external rate at which neutrons are produced
in the volume by an external source (S) and by fission (νΣfϕ) minus the rate at
which neutrons are lost by absorption (Σaϕ) and minus the net leakage of
neutrons out of the volume (∇□J). Proof that the net leakage out of a differential
volume element is ∇□J follows from considering the difference of outward and
inward currents in a cube of dimensions ΔxΔyΔz. The net transport of particles
out of the cube is
Jx(x + Δx) − Jx(x)
[
]ΔyΔz + Jy(y + Δy) − Jy(y)

ΔxΔz + Jz(z + Δz)
[
−Jz(z)]ΔxΔy '
@Jx
@x Δx

ΔyΔz +
@Jy
@y Δy

ΔxΔz +
@Jz
@z Δy

ΔxΔy
≡ ∇?~JΔxΔyΔz
where a Taylor’s series expansion of the current has been made.

### Interface Conditions

At an interface between regions 1 and 2 at which there is an isotropic source S0,
the partial currents on both sides of the interface must be related by
j(2)
+ (0) = 1
2 S0 + j(1)
+ (0)
j(1)
− (0) = 1
2 S0 + j(2)
− (0)
(3.10)
Subtracting these two equations and using Eqs. (3.4) and (3.5) yields an interface
condition of continuity of neutron flux:
ϕ2(0) = ϕ1(0)
(3.11)
Adding the two equations yields
J2(0) = J1(0) + S0
(3.12)
which, in the absence of an interface source, is a continuity of neutron net current
condition.

### Boundary Conditions

At an external boundary, the appropriate boundary condition is found by
equating the expression for the inward partial current to the known incident

<!-- page 47 (PDF 71) -->
current, jin, for example, from the right at xb,
jin
− = 1
4 ϕ(xb) + 1
2 D dϕ(xb)
dx
(3.13)
When the diffusing medium is surrounded by a vacuum or nonreflecting region,
jin = 0 and Eq. (3.13) may be written as
ϕ
dϕ
dx

xb
= − 1
2D = − 3Σtr
(3.14)
A widely used but more approximate vacuum boundary condition is obtained
by noting that this expression relates the flux and the flux slope at the boundary. If
the slope of the flux versus x at the boundary (xb) is used to extrapolate the flux
outside the boundary, the extrapolated flux will vanish at a distance λextrap =
3 λtr = 2
3 Σ−1
tr outside the external boundary. A more accurate result from neutron
transport theory is λextrap = 0.7104λtr. This result gives rise to the approximate
vacuum boundary condition of zero neutron flux at a distance λextrap outside the
physical boundary at x = a, or ϕ(a + λextrap) ≡ ϕ(aex) = 0, where we have defined
the extrapolated boundary
aex ≡ a + λextrap
(3.15)
Since λextrap is usually very small compared with the typical dimensions of a
diffusing medium encountered in reactor physics, it is common to use the even
more approximate vacuum boundary condition of zero flux at the physical
external boundary.

### Example 3.1 Typical Values of Thermal Extrapolation Distance

The thermal
neutron extrapolation distance λextrap = 0.7104/Σtr = 0.7104/[Σa + (1 − μ0)Σs] for
some typical diffusing media is 0.30 cm for H2O, 1.79 cm for D2O, 1.95 cm for C,
and 6.34 cm for Na. The approximation that the neutron flux vanishes at the
boundary of the diffusing medium is valid when the dimension L of the diffusing
medium is much larger than the extrapolation distance, L ≫λextrap.

### Applicability of Diffusion Theory

Diffusion theory provides a strictly valid mathematical description of the neutron
flux when the assumptions made in its derivation – absorption much less likely
than scattering, linear spatial variation of the neutron distribution, isotropic
scattering – are satisfied. The first condition is satisfied for most of the moderating
(e.g., water, graphite) and structural materials found in a nuclear reactor, but
not for the fuel and control elements. The second condition is satisfied for a few
mean free paths away from the boundary of large (relative to the mean free path)
homogeneous media with relatively uniform source distributions. The third
condition is satisfied for scattering from heavy atomic mass nuclei. One might
well ask at this point how diffusion theory can be used in reactor physics when a

<!-- page 48 (PDF 72) -->
modern nuclear reactor consists of thousands of small elements, many of them
highly absorbing, with dimensions on the order of a few mean free paths or less.
Yet diffusion theory is widely used in nuclear reactor analysis and makes accurate
predictions. The secret is that a more accurate transport theory is used to “make
diffusion theory work” where it would be expected to fail. The many small
elements in a large region are replaced by a homogenized mixture with effective
averaged cross sections and diffusion coefficients, thus creating a computational
model for which diffusion theory is valid. Highly absorbing control elements are
represented by effective diffusion theory cross sections that reproduce transport
theory absorption rates.

## 3.2 Solutions of the Neutron Diffusion Equation in Nonmultiplying Media

### Plane Isotropic Source in an Infinite Homogeneous Medium

Consider an infinite homogeneous nonmultiplying (Σf = 0) medium in which a
plane isotropic source (infinite in the y–z plane) with strength S0 is located at
x = 0. Everywhere except at x = 0 the time-independent diffusion equation can be
written as
d2ϕ(x)
dx2
− 1
L2 ϕ(x) = 0
(3.16)
where L2 ≡ D/Σa is the neutron diffusion length squared. This equation has a
general solution ϕ = A exp(x/L) + B exp(−x/L). For x > 0, the physical requirement
for a finite solution at large x requires that A = 0, and the physical
requirement that the net current must approach 1
2 S0 as x approaches 0 requires
that B = LS0/2D. Following a similar procedure for x < 0 leads to similar results, so
that the solution may be written as
ϕ(x) = S0Le−jxj=L
2D
(3.17)

### Plane Isotropic Source in a Finite Homogeneous Medium

Consider next a finite-slab medium extending from x = 0 to x = +a with an
isotropic plane source at x = 0. In this case, the general solution of Eq. (3.16) is
more conveniently written as ϕ = A sinh(x/L) + B cosh(x/L). The appropriate
boundary conditions are that the inward partial current vanishes at x = a [i.e.,
j−(a) = 0] and that the outward partial current equals ( the isotropic source
strength as x →0 [i.e., j+(0) = 1
2 S0]. The resulting solution is
ϕ(x) = 4S0
sinh[(a − x)=L] + (2D=L)cosh[(a − x)=L]
[2(D=L) + 1]2ea=L − [2(D=L) − 1]2e−a=L
(3.18)

<!-- page 49 (PDF 73) -->
If instead of j−(a) = 0, the extrapolated boundary condition ϕ(aex) = 0 is used,
the resulting solution is
ϕ(x) = 2S0
sinh[(aex − x)=L]
sinh(aex=L) + (2D=L)cosh(aex=L)
(3.19)
When 0.71λtr/a ≪1 and 2(Σa/3Σtr)1/2 ≪1 (i.e., when the transport mean free path
is small compared with the dimension of the medium and the absorption cross
section is small relative to the scattering cross section), these two solutions agree.
These conditions must also be satisfied in order for diffusion theory to be valid, so
we conclude that use of the extrapolated zero flux boundary condition instead of
the zero inward current boundary condition is acceptable.

### Line Source in an Infinite Homogeneous Medium

Consider an isotropic line source (e.g., infinite along the z-axis) of strength S0 (per
centimeter per second) located at r = 0. The general solution of
r
d
dr r dϕ(r)
dr

− 1
L2 ϕ(r) = 0
(3.20)
is ϕ = AI0(r/L) + BK0(r/L), where I0 and K0 are the modified Bessel functions of
order zero of the first and second kind, respectively. The physical requirement for
a finite solution at large r requires that A = 0. The source condition is limr→0
2πrJ = S0. The resulting solution for an isotropic line source in an infinite
homogeneous nonmultiplying medium is
ϕ(r) = S0K0(r=L)
2πD
(3.21)

### Homogeneous Cylinder of Infinite Axial Extent with Axial Line Source

Consider an infinitely long cylinder of radius a with an isotropic source on axis.
The source condition limr→0 2πrJ = S0 still obtains, but now A = 0 no longer holds
and the other boundary condition is a zero incident current condition at r = a or a
zero flux condition at r = a + λextrap. The latter vacuum boundary condition leads
to the solution for the neutron flux distribution in an infinite homogeneous
nonmultiplying cylinder with an isotropic axial line source:
ϕ(r) = S0[I0(aex=L)K 0(r=L) − K 0(aex=L)I0(r=L)]
2πDI0(aex=L)
(3.22)

### Point Source in an Infinite Homogeneous Medium

The neutron diffusion equation in spherical coordinates is
r2
d
dr r2 dϕ(r)
dr

− 1
L2 ϕ(r) = 0
(3.23)

<!-- page 50 (PDF 74) -->
This equation has the general solution ϕ = (Aer/L + Be−r/L)/r. The source condition
is limr→0 4πr2J = S0, and the physical requirement for a finite solution at large
r requires that A = 0, yielding
ϕ(r) = S0e−r=L
4πrD
(3.24)

### Point Source at the Center of a Finite Homogeneous Sphere

Consider a finite sphere of radius a with a point source at the center. The same
general solution ϕ = (Aer/L + Be−r/L)/r of Eq. (3.23) is applicable, but the A = 0
condition must be replaced by a vacuum boundary condition at r = a. Using an
extrapolated zero flux condition yields
ϕ(r) = S0sinh[(aex − r)=L]
4πrDsinh(aex − L)
(3.25)
for the neutron distribution in a finite sphere of homogeneous nonmultiplying
material with a point source at the center.

## 3.3 Diffusion Kernels and Distributed Sources in a Homogeneous Medium

### Infinite-Medium Diffusion Kernels

The previous solutions for plane, line, and point sources at the origin of slab,
cylindrical, and spherical coordinate systems in an infinite medium can be
generalized immediately to slab, line, and point sources located away from the
origin (i.e., the location of the coordinate axis in an infinite medium can be offset
without changing the functional form of the result). The resulting solutions for
the neutron flux at location x or r due to a unit isotropic source at x´ and r´ may be
thought of as kernels. The infinite-medium kernels for a plane isotropic source of
one neutron per unit area per second, a point isotropic source of one neutron per
second, a line isotropic source of one neutron per unit length, a cylindrical shell
source of one neutron per shell per unit length per second, and a spherical shell
source of one neutron per shell per second are
Plane : ϕpl(x : x´)
= L
2D e−jx−x´j=L
Line : ϕl(r : r´)
= K 0(jr − r´j=L)
2πD
Point : ϕpt(r : r´)
=
e−jr−r´j=L
4πjr − r´jD
Cylindrical shell : ϕcyl(r : r´) =
2πD □
K0(r=L)I0(r´=L);
r > r´
K0(r´=L)I0(r=L);
r < r´
(
Spherical shell : ϕsph(r : r´)
=
L
8πrr´D (e−jr−r´j=L − e−jr+r´j=L)
(3.26)

<!-- page 51 (PDF 75) -->
These kernels may be used to construct the neutron flux in an infinite
homogeneous nonmultiplying medium due to an arbitrary source distribution
S0:
ϕ(r) = ∫ϕ(r : r´)S0(r´)dr´
(3.27)
For a planar source distribution, this takes the form
ϕ(x) = ∫
−1
S0(x´)L
2D
e−jx−x´j=Ldx´
(3.28)
and for the more general point source,
ϕ(r) = ∫
S0(r´) e−jr−r´j=L
4πjr − r´jD dr´
(3.29)

### Finite-Slab Diffusion Kernel

Consider a slab infinite in the y- and z-directions extending from x = −a to x = +a
with a unit isotropic source at x´. The neutron diffusion equation
d2ϕ(x)
dx2
− 1
L2 ϕ(x) = 0
(3.30)
holds everywhere in −a < x < + a except at x = x´, the source plane. The interface
conditions at the source plane, x = x´, are from Eqs. (3.11) and (3.12),
ϕ(x´ + ε) = ϕ(x´ − ε)
J(x´ + ε) = J(x´ − ε) + 1
(3.31)
where x´ + ε indicates an infinitesimal distance to the right of x´, and so on. For the
vacuum boundary conditions at x = −a and x = a, we use the approximate zero
flux conditions
ϕ(−a) = ϕ(a) = 0
(3.32)
Solving Eq. (3.30) as before and using these source and boundary conditions
yields the following expressions for the flux at x due to a unit isotropic source at x´,
or the finite-slab diffusion kernel:
ϕ+(x : x´) = sinh[(a + x´)=L]sinh[(a − x)=L]
(D=L)sinh(2a=L)
;
x > x´
ϕ−(x : x´) = sinh[(a − x´)=L]sinh[(a + x)=L]
(D=L)sinh(2a=L)
;
x < x´
(3.33)

<!-- page 52 (PDF 76) -->
These kernels may be used to calculate the neutron flux distribution in the slab
due to a distributed source, S0(x´):
ϕ(x) = ∫
x
−a
S0(x´)ϕ+(x : x´)dx´ + ∫
a
x
S0(x´)ϕ−(x : x´)dx´
(3.34)

### Finite Slab with Incident Neutron Beam

As a further relevant example, consider the first-collision source distribution in a
slab due to a beam incident from the left at x = −a:
S0(x) = q0Σse−Σt(x+a)
(3.35)
Using this source in Eq. (3.34) yields the neutron flux distribution within the
slab:
ϕ(x) =
q0Σse−Σta
D(Σ2
t − (1=L2))sinh(2a=L)
□ eΣtasinh a − x
L
+ e−Σtasinh a + x
L
− e−Σtxsinh 2a
L

 (3.36)
By using a first-collision source, the highly anisotropic incident beam neutrons
are treated by first-flight transport theory until they have had a scattering collision
that (at least partially) converts the beam to a nearly isotropic neutron distribution
that is amenable to treatment by diffusion theory. The solution for the nearly
isotropic neutron distribution given by Eq. (3.36) has a maximum some distance
into the slab at 0 >x > − a.

## 3.4 Albedo Boundary Condition

Consider a slab that is infinite in the y- and z-directions located between x = 0 and
x = a with a known inward partial current j+(0) = j+
in. Upon solving for the
neutron flux distribution for an extrapolated zero flux vacuum boundary condition
ϕ(a + λextrap) ≡ ϕ(aex) = 0, it is possible to evaluate the reflection coefficient,
or albedo, for neutrons entering the slab from the left at x = 0.
α ≡ j−(0)
j+(0) = 1 − (2D=L)coth(aex=L)
1 + (2D=L)coth(aex=L)
(3.37)
As a/L becomes large, coth[(a + λextrap)/L] →1 and α →(1 − 2D/L)/(1+2D/L), the
infinite-medium value.
Now consider two adjacent slabs, one denoted B and located in the range
−b ≤ x ≤ 0 and the other denoted A and located in the range 0 ≤ x ≤ a. If we are not
interested in the neutron flux distribution in slab A but only in the effect of slab A
on the neutron flux distribution in slab B, the albedo of slab A can be used as an
albedo boundary condition for the neutron flux solution in slab B. From Eqs. (3.4)
and (3.5),

<!-- page 53 (PDF 77) -->
ϕB
DB
dϕB
dx

x=0
= − j+(0) − j−(0)
2[j+(0) + j−(0)] = − 1
1 − αA
1 + αA

(3.38)
This albedo boundary condition can also be simplified by a geometric interpretation
. If the flux in slab B at the interface between slabs A and B (x = 0)
is extrapolated (into slab A) to zero using the slope at the interface given by
Eq. (3.38), an approximate albedo boundary condition for the flux solution in slab
B (−b < x < 0) becomes ϕB(λalbedo) = 0, where
λalbedo ≡ 0:71λB
tr
1 + αA
1 − αA

(3.39)

## 3.5 Neutron Diffusion and Migration Lengths

The distribution of neutrons within a finite or infinite medium is determined by
the source distribution, the geometry (in a finite medium), and the neutron
diffusion length, L = (D/Σa)1/2. The (thermal) diffusion length is related to the
mean-squared distance that a thermal neutron travels from the source point to
the point at which it is absorbed, as may be seen by computing the mean-squared
distance to capture for (thermal) neutrons emitted by a point source in an infinite
medium:
r2 ≡ ∫
r2(4πr2Σaϕ)dr
∫
(4πr2Σaϕ)dr
= ∫
r3e−r=Ldr
∫
re−r=Ldr
= 6L2
(3.40)
where Eq. (3.24) has been used for the neutron flux due to a point source at r = 0.
It is also apparent from the exp(±x/L) nature of many of the solutions above that L
is the physical distance over which the neutron flux can change by a significant
amount (i.e., e−1).

### Thermal Diffusion-Length Experiment

The thermal neutron diffusion length can be determined experimentally by
measuring the axial neutron flux distribution in a long (with respect to mean
free path) block of material with an isotropic thermal neutron flux incident
on one end (e.g., from the thermal column of a reactor). With reference to
Fig. 3.2, consider a rectangular parallelepiped of length c and cross section
2a × 2b with an incident isotropic thermal neutron source S0(x, y) at z = 0 that
is symmetric in x and y about x = 0 and y = 0. The neutron flux in the block
satisfies
@2ϕ
@x2 + @2ϕ
@y2 + @2ϕ
@z2 − ϕ
L2 = 0
(3.41)

<!-- page 54 (PDF 78) -->
and the boundary conditions
j+(x; y; 0) = 1
2 S0(x; y)
(3.42a)
ϕ(−aex; y; z) = 0
(3.42b)
ϕ(x; −bex; z) = 0
(3.42c)
ϕ(x; y; cex) = 0
(3.42d)
We seek a separable solution to Eq. (3.41) of the form ϕ(x, y, z) = X(x)Y(y)Z(z).
Substitution of this form into Eq. (3.41) and division by XYZ yields
X´´(x)
X(x) + Y ´´(y)
Y(y) + Z´´(z)
Z(z) = 1
L2
(3.43)
where the double prime indicates a second derivative with respect to the
respective spatial variables. In general, this equation can only be satisfied if
each of the terms on the left is separately equal to a constant:
X´´(x)
X(x) = −k2
1;
Y ´(y)
Y(y) = −k2
2;
Z´´(z)
Z(z) = k2
(3.44)
in which case Eq. (3.43) becomes
k2
3 = 1
L2 + k2
1 + k2
(3.45)
Fig. 3.2 Geometry for diffusion-length experiment. (From Ref. [1].)

<!-- page 55 (PDF 79) -->
The general solutions to Eqs. (3.44) are
X(x) = A1sink1x + C1cosk1x
Y(y) = A2sink2y + C2cosk2y
Z(z) = A3e−k3z + C3ek3z
(3.46)
The x–y symmetry requirement determines that A1 = A2 = 0. The end condition
of Eq. (3.42d) may be used to eliminate C3 to obtain
Z(z) = A3e−k3z[1 − e−2k3(cex−z)]
(3.47)
The extrapolated boundary conditions of Eqs. (3.42b) and (3.42c) require that cos
k1aex = cos k2bex = 0, which can only be satisfied if k1 and k2 have the discrete
values
k1n =
π
2aex
(2n + 1);
n = 0; 1; . . .
k2m =
π
2bex
(2m + 1);
m = 0; 1; . . .
(3.48)
This result, together with Eq. (3.45), requires that k3 can only take on discrete
values
k2
3 ! k2
3nm = k2
1n + k2
2m + 1
L2
(3.49)
Thus, the most general solution of the neutron diffusion equation that satisfies the
extrapolated boundary conditions of Eqs. (3.42b)–(3.42d) is
ϕ(x; y; z) =
X
n;m=0
Amncosk1nxcosk2mye−k3nmz[1 − e−2k3nm(cex−z)]
(3.50)
where Amn is a constant that can be determined from Eq. (3.42a), but that is not
necessary for our purposes.
Noting that k3nm increases with m and n, the asymptotic form of the
neutron flux distribution along the z-axis that persists at large distances from
z = 0 is
ϕ(0; 0; z) ' A00e−k300z[1 − e−2k300(cex−z)]
(3.51)
For very long blocks (large cex), the term in brackets is unimportant except near
the end, and the flux decreases exponentially, so that a measurement of the axial
flux distribution far away from both the source at z = 0 and the end at z = cex
should provide for experimental determination of k300. The diffusion length then
is determined from
l
L2 = k2
300 −
π
2aex

−
π
2bex

(3.52)

<!-- page 56 (PDF 80) -->
The measured diffusion lengths L for thermal neutrons in H2O, D2O, and
graphite are about 2.9, 170, and 60 cm, respectively. The implication of these
measurements is that thermal neutrons would diffuse a root-mean-square
distance from the point at which they appear (are thermalized) to the point at
which they are absorbed of 7.1, 416, and 147 cm, respectively, in these three
moderators.

### Migration Length

In a water- or graphite-moderated reactor, the fission neutrons are born fast
(average energy about 1.0 MeV) and diffuse as fast neutrons while they are in the
process of slowing down to become thermal neutrons. In fast reactors, the
neutrons are absorbed before thermalizing. In a later chapter we return to
calculation of the diffusion of these fast neutrons, but for now we simply indicate
that there is an equivalent for fast neutrons of the thermal diffusion length, which
for historical reasons is identified as the square root of the “age to thermal,” τth.
For intermediate-to-heavy-mass moderators, this quantity can be shown to be
equal to one-sixth of the mean-squared distance a fast neutron diffuses before it
thermalizes (for hydrogenous moderators, this is the definition of the quantity).
The mean-squared distance that a neutron travels from birth as a fast fission
neutron until capture as a thermal neutron is given by
r2 = 6(τth + L2) ≡ 6M2
(3.53)
where M = (τth + L2)1/2 is known as the migration length.

### Example 3.2 Characteristic Diffusion Parameters

Diffusion characteristics
for some common moderators are given in Table 3.1. The values of D, Σa, and L
are for thermal neutrons. Diffusion characteristics for compositions representative
of pressurized water (H2O) reactors (PWRs), boiling water (H2O) reactors
(BWRs), high-temperature graphite thermal reactors (HTGRs), sodium-cooled
fast reactors (LMFRs), and gas-cooled fast reactors (GCFRs) are given in
Table 3.2. Typical core diameters, measured in thermal diffusion lengths
and in migration lengths for the thermal reactors and measured in fast diffusion
lengths for the fast reactors, are also given. It is clear from these numbers that
most of the diffusion displacement undergone by a fission neutron occurs
during the slowing-down process.
Table 3.1 Diffusion Parameters for Common Moderators
Moderator
Density (g/cm3)
D (cm)
Σa (cm −1)
L (cm)
τ1=2
th (cm)
M (cm)
H2O
1.00
0.16
2.0 × 10−2
2.9
5.1
5.8
D2O
1.10
0.87
2.9 × 10−5
11.4
Graphite
1.60
0.84
2.4 × 10−4
Source: Data from Ref. [2]; used with permission of Wiley.

<!-- page 57 (PDF 81) -->
## 3.6 Bare Homogeneous Reactor

In a fission chain reacting medium (i.e., a medium in which neutron absorption
can lead to fission and the production of more neutrons), the diffusion equation
may or may not have an equilibrium steady-state solution, depending on the
precise amount of multiplication. Thus, we must consider the time-dependent
diffusion equation
v
@ϕ(r; t)
@t
− D∇2ϕ(r; t) + Σaϕ(r; t) = vΣf ϕ(r; t)
(3.54)
In a finite homogeneous medium (i.e., a bare reactor), the appropriate boundary
condition is the extrapolated zero flux condition
ϕ(aex; t) = 0
(3.55)
where aex denotes the external boundaries. We further specify an initial condition
ϕ(r; 0) = ϕ0(r)
(3.56)
where ϕ0 denotes the initial spatial flux distribution at t = 0.
We use the separation-of-variables technique and look for a solution of the
form
ϕ(r; t) = ψ(r)T(t)
(3.57)
Substituting Eq. (3.57) into Eq. (3.54) and dividing by ϕ = ψT yields
v
ψ D∇2ψ + (vΣf − Σa)ψ

= 1
T
@T
@t = −λ
(3.58)
where we have indicated that an expression that depends only on the spatial
variable and an expression that depends only on the time variable can be equal at
Table 3.2 Diffusion Parameters for Representative Reactor Core Types
Reactor
L (cm)
τ1=2
th (cm)
M (cm)
Diameter (L)
Diameter (M)
PWR
1.8
6.3
6.6
BWR
2.2
7.1
7.3
HTGR
LMFR
5.0∗
5.0
GCFR
6.6∗
6.6
Source: Data from Ref. [2]; used with permission of Wiley.
∗Fast neutron diffusion length.

<!-- page 58 (PDF 82) -->
all spatial locations and times only if both expressions are equal to the same
constant, −λ. The second form of Eq. (3.58) has the solution
T(t) = T(0)e−λt
(3.59)
We look for spatial solutions ψ that satisfy
∇2ψ(r) = −B2
gψ(r)
(3.60)
and the extrapolated spatial boundary conditions of Eq. (3.55). The constant Bg,
known as geometric buckling, depends only on the geometry.

### Slab Reactor

For example, in a slab reactor extending from x = −a/2 to x = +a/2 and infinite in
the y- and z-directions, Eqs. (3.60) and (3.55) become
d2ψ
dx2 (x) = −B2
gψ(x);
ψ aex
= ψ −aex
= 0
(3.61)
which have solutions ψ = ψn only for the (infinite) set of discrete spatial eigenvalues
of Bg = Bn:
ψn(x) = cosBnx;
B2
n =
nπ
aex

;
n = 1; 3; 5; . . .
(3.62)
Using this result in Eq. (3.58) implies that solutions of that equation exist only for
discrete-time eigenvalues λn given by
λn = v Σa + DB2
n − vΣf
(3.63)
Thus, the solution of Eq. (3.54) for a slab reactor is
ϕ(x; t) =
X
n=odd
AnTn(t)cos nπx
aex
(3.64)
where Tn is given by Eq. (3.59) with λ = λn and An is a constant that may be
determined from the initial condition of Eq. (3.56) and orthogonality:
An(x) = 2
aex ∫
aex=2
−aex=2
dxϕ0(x)cos nπx
aex
(3.65)
Since B2
1 < B2
3 < ∙∙∙< B2
n = (nπ=aex)2, the time eigenvalues are ordered
λ1 < λ3 < ∙∙∙< λn = v(Σa + DB2
n − νΣf ). Thus, after a sufficiently long time
(t ≫1/λ3), the solution becomes
ϕ(x; t) ! A1e−λ1tcosB1x = A1e−λ1tcos πx
aex
(3.66)
This result implies that, independent of the initial distribution (as long as A1 ≠0),
the asymptotic shape will be the fundamental mode solution corresponding to the
smallest spatial and time eigenvalues. The asymptotic solution is steady state only
if λ1 = 0. If λ1 > 0, the asymptotic solution is decaying in time, and if λ1 < 0, it is

<!-- page 59 (PDF 83) -->
increasing in time. When the neutron population is sustained precisely in steady
state by the fission chain reaction, the reactor is said to be critical; when the
neutron population is increasing in time, the reactor is said to be supercritical; and
when the neutron population is dying away in time, the reactor is said to be
subcritical. Defining the material buckling, Bm,
B2
m ≡ vΣf − Σa
D
= vΣf =Σa − 1
L2
(3.67)
the criticality condition for a bare homogeneous reactor may be written as
Supercritical : λ1 < 0; B2
m > B2
Critical :
λ1 = 0; B2
m = B2
Subcritical :
λ1 > 0; B2
m < B2
(3.68)

### Right Circular Cylinder Reactor

The slab reactor results can be extended immediately to more general geometries
by replacing Eqs. (3.61) and (3.62) with the corresponding equations for
the other geometries. For example, for the more realistic core geometry of a
right circular cylinder of radius a and height H, the equation corresponding to
Eq. (3.60) is
r
@
@r r @ψ(r; z)
@r

+ @2ψ(r; z)
@z2
= −B2
gψ(r; z)
(3.69)
and the extrapolated boundary conditions are
ψ(aex; z) = ψ
r; − Hex

= 0
(3.70)
We make further use of the separation-of-variables technique to write
ψ(r; z) = R(r)Z(z)
(3.71)
Substituting Eq. (3.71) into Eq. (3.69) and dividing by RZ yields
R(r)
r
@
@r r @R(r)
@r

+
Z(z)
@2Z(z)
@z2
= −v2 − κ2 = −B2
g
(3.72)
where the second form of the equation indicates that the only way in which the
sum of an expression that depends only on the r-variable plus an expression
that depends only on the z-variable can everywhere equal a constant is if the two
expressions separately are equal to constants. Solutions of these two equations
– the first expression equal to the first constant and the second expression equal
to the second constant – that satisfy the corresponding boundary condition of
Eqs. (3.70) exist only for discrete values of the constants νm (the roots of
J0(νm) = 0, m = 1, 2, . . . ) and κn (κn = nπ/Hex, n = 1, 3, . . . ). Since the roots of J0
are ordered, ν1 < ν2 < ∙∙∙< νn, the smallest of the corresponding discrete

<!-- page 60 (PDF 84) -->
eigenvalues B2
mn =
 vm
Rex
2 + (nπ=Hex)2 is B2
11 =
 v1
Rex
2 + (π=Hex)2, and the smallest
time eigenvalue is
λ1 = v
Σa + D
v1
Rex

+
π
Hex

"
− vΣf
(
)
= v B2
11 − B2
m
D
= v B2
g − B2
m
D
(3.73)
The corresponding asymptotic solution is
ϕ(r; z; t) ! A11J0
v1r
aex

cos
πz
Hex

e−λ1t
(3.74)
The criticality condition, λ1 = 0, corresponds to B2
m = B2
g = B2
11. The first zerocrossing
for the Bessel function J0(ν) occurs at ν = ν1 = 2.405.
The geometric bucklings and asymptotic flux solutions are given for the
common geometries in Table 3.3.
Table 3.3 Geometric Bucklings and Critical Flux Profiles Characterizing Some Common Core
Geometries
Geometry
Geometric Buckling B2
g
Flux Profile
Slab
a
π
aex

cos
πx
aex

Infinite
cylinder
R
v1
Rex

J0
v1r
Rex

Sphere
R
π
Rex

r−1sin
πr
Rex

Rectangular
parallelepiped
c
b
a
π
aex

+
π
bex

+
π
cex

cos
πx
aex

cos
πy
bex

cos
πz
cex

Finite cylinder
H
R
v1
Rex

+
π
Hex

J0
v1r
Rex

cos
πz
Hex

Source: Adapted from Ref. [2]; used with permission of Wiley.

<!-- page 61 (PDF 85) -->
### Interpretation of Criticality Condition

The criticality condition λ1 = 0, or B2
m = B2
g, can be rearranged to yield
1 = vΣf =Σa
1 + L2B2
g
≡
k1
1 + L2B2
g
= k1PNL
(3.75)
where k1 is the infinite-medium multiplication constant and PNL = (1 + L2B2
g)−1
is interpreted as the nonleakage probability.
If λ1 ≠0, the reactor is not critical and the asymptotic solution will either grow
indefinitely or decay away in time because the multiplication of neutrons (the
ratio of the neutron population in successive generations) is greater or less than,
respectively, unity. Since Eq. (3.75) applies only when k = 1, we can more generally
write
k = vΣf =Σa
1 + L2B2
g
≡ k1PNL
(3.76)
The situation λ1 < 0, in which the asymptotic solution increases in time,
corresponds to k > 1, and the situation λ1 > 0, in which the asymptotic solution
decays in time, corresponds to k < 1. From Eqs. (3.63) and (3.76),
λ1 = v B2
1 − B2
m
D = vΣa 1 + L2B2
1 − vΣf =Σa
1 + L2B2

(3.77)
Since the mean free path to absorption is 1/Σa, the lifetime of a neutron that
remains in the reactor until absorption is 1/vΣa. Defining an effective lifetime of a
neutron in the reactor that takes into account the possibility of leakage before
absorption
l =
vΣa(1 + L2B2
1) = PNL
vΣa
(3.78)
enables Eq. (3.77) to be written as
λ1 = 1 − k
l
(3.79)
Thus, the asymptotic solution of Eq. (3.54) that satisfies the extrapolated
boundary conditions of Eq. (3.55) can be written as
ϕasy(r; t) ! A1ψ1(r)e[(k−1)=l]t
(3.80)
where ψ is the fundamental mode spatial distribution for the specific geometry
given in Table 3.3.

### Optimum Geometries

The minimum size for a bare reactor of a given composition that will be critical
depends on the leakage, hence on the surface-to-volume ratio. The minimum
critical volume for a rectangular parallelepiped bare reactor occurs for a cube and
