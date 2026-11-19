# 15 Nodal and Synthesis Methods — 15 Nodal and Synthesis Methods … 15.3 Transverse Integrated Nodal Diffusion Theory Methods
<!-- source PDF pages 581-594 -->

<!-- page 563 (PDF 581) -->
# 15 Nodal and Synthesis Methods

Even after the local fuel pin, clad, coolant, and so on, heterogeneity is replaced by a
homogenized representation; a reactor core remains a highly heterogeneous
medium because of the intra-assembly and assembly-to-assembly variation in
fuel composition, burnable poisons, control rods, water channels, structure, and
so on. The mesh spacing in a conventional few-group finite-difference model of
such a core is constrained by two requirements: (1) it must be sufficiently fine to
represent the remaining spatial heterogeneity adequately, and (2) it must be no
larger than the shortest (thermal) group diffusion length in order to avoid
numerical inaccuracy. A few-group finite-difference model that could adequately
describe such a core might well have 105–106 unknowns (the fluxes in each group
at each mesh point). The direct solution of such a problem, even in diffusion
theory, remains a formidable computation that was unthinkable until very
recently. For calculations such as fuel burnup or transient analysis, in which
many full-core spatial solutions are needed, direct few-group finite-difference
solutions remain impractical.
A large number of approximation methods have been developed to enable a
more computationally tractable solution for the effective multiplication constant
and neutron flux distribution in reactor cores. Following historical precedent,
these methods can generally be classified as nodal, coarse-mesh, or synthesis
methods, although the distinction among the categories may be largely a matter of
perspective and sequencing of calculational steps.
Nodal methods characterize the global neutron flux distribution in terms of a
small number of parameters in each of several large regions, or nodes, into which
the reactor core is subdivided for this purpose. Such methods generally require
detailed heterogeneous intranodal flux distributions to construct homogenized
parameters for each of the many nodes into which a reactor core may be divided
and to calculate coupling parameters that link the average flux solutions in
adjacent nodes. The global average nodal fluxes must then be combined with the
intranodal heterogeneous flux solutions if a heterogeneous flux distribution is
required.
Coarse-mesh methods extend the numerical accuracy of conventional finitedifference
methods by using higher order approximations for the flux variation
among mesh points. Like nodal methods, coarse-mesh methods generally require
detailed regional heterogeneous flux distributions in order to construct
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 564 (PDF 582) -->
homogenized parameters and to combine with the coarse-mesh solution to
construct a detailed heterogeneous flux solution.
Synthesis methods generally combine detailed heterogeneous two-dimensional
planar flux distributions by means of a one-dimensional axial calculation to
obtain a global heterogeneous flux solution. Such methods do not require a
previous homogenization within large regions of the core as do nodal and coarsemesh
methods, but in effect perform a homogenization in constructing the
parameters to be used in the axial synthesis calculation, thus ensuring a certain
consistency between the homogenization and the approximate model calculation.

## 15.1 General Nodal Formalism

Writing the multigroup neutron balance equations in the form
∇⋅Jg(r) + Σg
t (r)ϕg(r)
=
X
G
g´=1
Σg´!g(r)ϕg´(r) + χg
k
X
G
g´=1
v
Xg´
f (r)ϕg´(r);
g = 1; . . . ; G
(15.1)
and integrating over the volume of node n (Fig. 15.1) yields an integral balance on
node n:
X
n´
Lg
nn´ + Σg
tnϕ
n
gV n =
X
G
g´=1
Σg´!g
n
ϕ
n
g´V n + χg
k
X
G
g´=1
vΣg´
f nϕ
n
g´V n;
g = 1; . . . ; G;
n = 1; . . . ; N
(15.2)
where the nodal average total, scattering, and fission cross sections are defined by
expressions of the form
Σg
tn ≡ ∫V n
drΣg
t (r)ϕg(r)
∫V n
drϕg(r)
(15.3)
the average nodal flux is
ϕ
n
g ≡ ∫V n
ϕg(r)dr
V n
(15.4)
and the leakage between node n and adjacent node n´ is defined by a surface
integral over the common interface:
Lg
nn´ ≡ ∫rs ∈Snn´
drsn ? Jg(rs)
(15.5)

<!-- page 565 (PDF 583) -->
(nx + 1, ny, nz)
(nx ny, + 1, nz)
(nx-1, ny, nz)
(nx ny, nz)
(nx, ny-1, nz)
(nx, ny, nz-1)
(nx, ny, nz + 1)
ΔZ
(Jn
gx+)out
(Jn
gx+)in
ΔX
ΔY
–ΔZ
–ΔX
2 –ΔY
Fig. 15.1 Nodal model nomenclature.
To be more specific, in discussion of the leakage term, we consider a parallelepiped
node of dimensions Δx, Δy, and Δz, as shown in Fig. 15.1. The surface
integrals of the net x-direction current at the node boundaries at x = +Δx/2 and at
□Δx/2 are defined as
Jn
gx− ≡
∫
Δy=2
□Δy=2
dy∫
Δz=2
□Δz=2
dznx ? Jg(−Δx=2; y; z)
ΔyΔz
(15.6)
with similar definitions for the surface integrals of net y- and z-direction currents
at ±Δy/2 and ±Δz/2, respectively. Surface integrals of the outward and inward
x-directed partial currents at ±x/2 are defined in terms of the partial currents
directed to the right (J+
g ) and to the left (J□
g ), respectively:
(J
n
gx−)out ≡
∫
Δy=2
□Δy=2
dy∫
Δz=2
□Δz=2
dznx ? J−
g (−(Δx=2); y; z)
ΔyΔz
(J
n
gx−)in ≡ □
∫
Δy=2
□Δy=2
dy∫
Δz=2
□Δz=2
dznx ? J□
g (−(Δx=2); y; z)
ΔyΔz
(15.7)

<!-- page 566 (PDF 584) -->
with similar definitions for surface integrals of partial y- and z-direction currents
at ±Δy/2 and ±Δz/2, respectively. The surface integrals of the net current are
related to the surface integrals of the partial currents as the net current is related
to the partial currents:
J
n
gx− = − (J
n
gx−)out □ (J
n
gx−)in
h
i
(15.8)
Using these definitions of surface integrals of the net current over the six faces
bounding the node, the balance Eq. (15.2) can be written in the more explicit form
Δx (J
n
gx+ □ J
n
gx□) + 1
Δy (J
n
gy+ □ J
n
gy□) + 1
Δz (J
n
gz+ □ J
n
gz□) + Σg
tnϕ
n
g
=
X
G
g´=1
Σg´!g
n
ϕ
n
g´ + χg
k
X
G
g´=1
vΣg´
f nϕ
n
g´;
g = 1; . . . ; G
(15.9)
The various nodal formulations are distinguished primarily by the methods used
to evaluate the surface currents in Eq. (15.9).
In diffusion theory approximation, the x-directed partial currents and the flux
are related by
J−
gx(x) = 1
4 ϕg(x) □ 1
2 Dg dϕg(x)
dx
(15.10)
with similar relations for the y- and z-directed partial currents. Thus, the surface
integrals of the flux at ±Δx/2
ϕ
n
gx− ≡
∫
Δy=2
□Δy=2
dy∫
Δz=2
□Δz=2
dzϕ(−(Δx=2); y; z)
ΔyΔz
(15.11)
are related to the corresponding surface integrals of the partial currents:
ϕ
n
gx− = 2[(Jn
gx−)out + (Jn
gx−)in]
(15.12)
with similar relations for the y- and z-directed partial currents at ±Δy/2 and ±Δz/
2, respectively. All surface integrals with the node index n are evaluated in the
limit as the surface is approached from within the nth node.
As mentioned, the various nodal formulations are distinguished primarily by
the methods used to evaluate the surface currents in Eq. (15.9). Two rather
distinct classes of nodal methods have evolved. The first class, often referred to as
conventional or simulation models, makes use of detailed calculations or reactor
operating experience to evaluate the surface current integrals in terms of
differences in node-averaged fluxes for adjacent nodes, with empirically adjusted
coupling coefficients. The second class, sometimes referred to as consistently

<!-- page 567 (PDF 585) -->
formulated models, makes use of the concept of transverse integration and of
higher order (than ordinary finite-difference) approximations to evaluate the
surface integrals of the current and the internodal coupling terms in order to
derive nodal equations that can be expected to converge to the exact solution in
the limit of small mesh spacing.

## 15.2 Conventional Nodal Methods

The first class of nodal models to be considered is based on relatively simple
mathematical models with parameters that can be adjusted to match the results of
more detailed calculation or measurement. Such methods are widely used in threedimensional
simulators, which play a key role in guiding and interpreting the
operation of research and power reactors. The basis of such methods is
the representation of the neutron flux or neutron fission rate within each of the
many homogenized fuel assemblies by a single nodal average flux or fission rate that
is coupled to the average flux or fission rate in adjacent nodes by the internodal
diffusion of fast neutrons, which is represented by coupling coefficients. The
reflector is usually represented by an albedo. Such methods are frequently based
on 11
2-group theory. The coupling coefficients and the reflector albedo are normally
adjusted to provide agreement with more detailed calculations or measurements.
The earlier versions of this class of nodal methods imposed a continuity of net
current condition at interfaces:
J
n
gx
Δxn

= □Dg
n
dϕ
n
gx
dx
(Δxn=2) = □Dg
n;eff(αn;n+1
gx
ϕ
n+1
g
□ αn;n
gx ϕ
n
g)
(15.13)
where ϕ
n
g is the node-averaged flux, and chose the effective diffusion coefficients
and coupling parameters α to match interface net currents or nodal average fluxes
from detailed planar finite-difference calculations. The sometimes unphysical
nature of the solution or the strong sensitivity to the properties of both adjacent
fuel assemblies of the coupling coefficients obtained by such net current-matching
procedures led to the development of coupling coefficients based on matching
partial currents at node interfaces:
J
n+
gx
Δxn

≡ ∫
(Δy=2)
(□Δy=2)
dy∫
(Δz=2)
(□Δz=2)
dznx ? J+
g
Δx
2 ; y; z

= αn;n+1
g
ϕ
n
gΔxn
J
n□
gx
Δxn

≡ □∫
(Δy=2)
(□Δy=2)
dy∫
(Δz=2)
(□Δz=2)
dznx ? J□
g
Δx
2 ; y; z

= αn+1;n
g
ϕ
n+1
g
Δxn+1
(15.14)

<!-- page 568 (PDF 586) -->
The gross coupling method uses detailed finite-difference diffusion theory fluxes
from a heterogeneous planar (x, y) model to calculate interface partial currents:
nx ? J−
g
Δxn
2 ; y

= 1
4 ϕg
Δxn
2 ; y

□ 1
2 Dg
Δxn
2 ; y

 @ϕg((Δxn=2); y)
@x
(15.15)
which are used to evaluate the coupling coefficients, α. For ϕg(Δxn/2, y), ϕ
n
g and
ϕ
n+1
g
obtained from detailed planar calculations, Eqs. (15.14) and (15.6) – with the
integral over Δz suppressed – are used to evaluate αn
g and αn+1
g
. The nodal
Eq. (15.9) in two-dimensional geometry may be written as
□αnx+1;n
g
Δxnx+1
Δxn
ϕ
nx+1
g
□ α
ny+1;n
g
Δyny+1
Δyn
ϕ
ny+1
g
□ αnx□1;n
g
Δxnx□1
Δxn
ϕ
nx□1
g
□ α
ny□1;n
g
Δyny□1
Δyn
ϕ
ny□1
g
+ (αn;nx+1
g
+ α
n;ny+1
g
+ αn;nx□1
g
+ α
n;ny□1
g
+ Σg
tn)ϕ
n
g
□
X
G
g´=1
Σg´!g
n
ϕ
n
g´ □ χg
k
X
G
g´=1
vΣg´
f ϕ
n
g´ = 0
(15.16)
where the node n is designated by sub- and superscripts nx and ny so that the
adjacent node in the x- and y-directions may be indicated by nx ± 1 and ny ± 1,
respectively [e.g., n, nx + 1 refers to the coupling between node n (nx, ny) and the
adjacent node (nx + 1, ny) at x = +Δxn/2] (see Fig. 15.1).
Most of the conventional nodal models do not make use of detailed planar
calculations to evaluate the internodal coupling coefficients. Instead, the coupling
coefficients are reinterpreted in a manner that enables intranodal collision
probability methods to be used in their evaluation. The one-group version of
Eq. (15.16) may be rewritten as
□W nx+1;nSnx+1 □ W ny+1;nSny+1 □ W nx□1;nSnx□1 □ W ny□1;nSny□1
+ W n;nx+1 + W n;ny+1 + W n;nx□1 + W n;ny□1 + k
kn
□ 1

Sn = 0
(15.17)
as a balance among the fission neutron production rates in the various nodes,
where
Sn ≡ vΣf nϕnΔxnΔyn;
kn
1 ≡ vΣf n
Σan
(15.18)

<!-- page 569 (PDF 587) -->
and the coupling terms are of the form
W n;nx+1 = J
n+
x ((Δxn=2))
vΣf nϕ
n
W nx+1;n = J
n□
x ((Δxn=2))Δxn
vΣf nϕ
n+1Δxn+1
(15.19)
The new coupling coefficients W n;nx+1 may be interpreted as the probability that a
fission neutron born in node (nx, ny) escapes into node (nx+1, ny), and so on,
quantities that readily lend themselves to calculation using collision probabilities
or other methods. For example, the well-known FLARE code uses
W n;nx+1 = (1 □ g)
ffiffiffiffiffiffiffi
M2
n
p
2Δxn
+ g
M2
n
(Δxn)2
(15.20)
where M2
n is the migration area in node (nx, ny) and g is an adjustable parameter.
The two terms correspond to the one-group transport and diffusion kernels for
leakage from a slab of thickness Δxn. A reformulation of the FLARE equations in
2-group theory leads to
W n;nx+1 = M2
n
Δx2
n
? 1
kn
?
1 + Mn+1=Mn
(15.21)
Neutron conservation for an internal node requires that
Sn = kn
k
X
m=1
W m;nSm
(15.22)
where the sum is over the six adjacent nodes. Wm,n represents the probability that
a neutron created from fission in node m will be absorbed in node n, since it has
been assumed that a neutron escaping into an adjacent node is absorbed therein.
(This assumption can be removed.) For nodes on the surface of the core, an albedo
βnr is used for each surface r that faces a reflector, so that the balance equation is
Sn = kn
k
X
m ≠r
W m;nSm + (1 □ βnr)W n;rSn
"
;
n = 1; . . . ; N
(15.23)
Equations (15.22) and (15.23) are solved iteratively, with the eigenvalue guess
updated on each iteration by using the most recently calculated Sn in the neutron
balance to evaluate
k =
P
nSn[1 □ (1 □ βnr)W n;r]
P
nSn=kn
(15.24)

<!-- page 570 (PDF 588) -->
Nodal methods of the type described in this section generally require parameter
adjustment to obtain agreement with more detailed calculations or measurements
of power distribution, effective multiplication constant, and so on.
Computations based on these nodal methods run very fast and have found
widespread use in three-dimensional reactor simulators.

## 15.3 Transverse Integrated Nodal Diffusion Theory Methods

A second class of nodal methods are those that have been formulated on the basis of
integrating thethree-dimensional diffusion equation over two transverse directions
to obtain a one-dimensional diffusion equation, with transverse leakage terms,
which can be solved within a node by approximating the dependence on the
remaining spatial variable, usually with a polynomial. These methods are consistently
formulated in that they reduce in the limit of small node sizes to the
conventional finite-difference method for the homogenized reactor model.

### Transverse Integrated Equations

Integration of the three-dimensional multigroup diffusion equations over the two
transverse directions to obtain a one-dimensional equation in node n yields
d
dx J
n
gx(x) + 1
Δy Lg
ny(x) + 1
Δz Lg
nz(x) + Σg
tnϕ
n
gx(x)
=
X
G
g´=1
Σg´!g
n
ϕ
n
g´x(x) + χg
k
X
G
g´=1
vΣg´
f nϕ
n
g´x(x);
g = 1; . . . ; G
(15.25)
The x-dependent flux and current averaged over the transverse directions are
ϕ
n
gx(x) ≡
∫
Δy=2
□Δy=2
dy∫
Δz=2
□Δz=2
dzϕn
g(x; y; z)
ΔyΔz
(15.26)
J
n
gx(x) ≡
∫
Δy=2
□Δy=2
dy∫
Δz=2
□Δz=2
dzJn
g(x; y; z)
ΔyΔz
(15.27)
and leakage terms transverse to the x-direction are
Lg
ny(x) = 1
Δz ∫
Δz=2
□Δz=2
dzny ? Jg
x; Δy
2 ; z

□ Jg
x; □ Δy
2 ; z

= □1
Δz ∫
Δz=2
□Δz=2
dz Dg
n
@ϕg(x; (Δy=2); z)
@y
□ Dg
n
@ϕg(x; □(Δy=2); z)
@y

(15.28)

<!-- page 571 (PDF 589) -->
Lg
nz(x) = 1
Δy ∫
Δy=2
□Δy=2
dynz ? Jg
x; y; Δz

□ Jg
x; y; □ Δz

= □1
Δy ∫
Δy=2
□Δy=2
dy Dg
n
@ϕg(x; y; (Δz=2))
@z
□ Dg
n
@ϕg(x; y; □(Δz=2))
@z

(15.29)
Making the diffusion theory approximation
J
n
gx(x) = □Dg
n
d
dx ϕ
n
gx(x)
(15.30)
the multigroup diffusion theory x-direction transverse integrated equation for
node n is
□ d
dx Dg
n
d
dx ϕ
n
gx(x) + 1
Δy Lg
ny(x) + 1
Δz Lg
nz(x) + Σg
tnϕ
n
gx
=
X
G
g´=1
Σg´!g
n
ϕ
n
g´x(x) + χg
k
X
G
g´=1
vΣg´
f nϕ
n
g´x(x);
g = 1; . . . ; G
(15.31)
The node-averaged values of the group flux and transverse leakage terms are
ϕ
n
g ≡ 1
Δx ∫
Δx=2
□Δx=2
dxϕ
n
gx(x)
=
ΔxΔyΔz ∫
Δx=2
□Δx=2
dx∫
Δy=2
□Δy=2
dy∫
Δz=2
□Δz=2
dzϕg(x; y; z)
(15.32)
L
g
ny ≡ 1
Δx ∫
Δx=2
□Δx=2
dxLg
ny(x) = Jn
gy+ □ Jn
gy□
L
g
nz ≡ 1
Δx ∫
Δx=2
□Δx=2
dxLg
nz(x) = Jn
gz+ □ Jn
gz□
(15.33)
Integrating Eq. (15.25) over x and using Eqs. (15.32) and (15.33) yields the
nodal balance Eq. (15.19). One-dimensional transverse integrated equations in
the y- and z-directions are derived in a similar manner.

### Polynomial Expansion Methods

The coarse-mesh methods can obtain a higher order accuracy than conventional
finite-difference methods by expanding the x-dependence of the flux:
ϕ
n
gx(x) ' ϕ
n
gf 0(x) +
X
I
i=1
an
gxif i(x);
□ Δx
2 ≤ x ≤ Δx
(15.34)

<!-- page 572 (PDF 590) -->
where the polynomials
f 0(x) = 1;
f 1(x) = x
Δx ≡ ξ
f 2(x) = 3ξ2 □ 1
4 ;
f 3(x) = ξ ξ □ 1

ξ + 1

f 4(x) =
ξ2 □ 1

ξ □ 1

ξ + 1

..
.
(15.35)
are normalized so that the volume average of the polynomial representation of the
flux is the volume average of the flux defined by Eq. (15.32):
Δx ∫
Δx=2
□Δx=2
dxf n(x) =
1;
n = 0
0;
n > 0
(
(15.36)
and the surface average of the flux is equal to the surface-averaged flux defined by
Eq. (15.11) at x = ±Δx/2:
ϕ
n
gx − Δx

= ϕn
gx−
(15.37)
These requirements are satisfied by polynomial expansion coefficients,
an
gx1 = ϕn
gx+ □ ϕn
gx□
an
gx2 = ϕn
gx+ □ ϕn
gx□ □ 2ϕ
n
g
(15.38)
and the requirement that
f i − Δx

= 0;
n > 2
(15.39)
on the polynomials.
In terms of these polynomials, the outgoing x-direction surface-averaged
currents at x = ±Δx/2 are
(Jn
gx+)out = Jn
gx+ + (Jn
gx+)in = □Dg
n
d
dx ϕ
n
gx
Δx

+ (Jn
gx+)in
= □ Dg
n
Δx
an
gx1 + 3an
gx2 + 1
2 an
gx3 + 1
5 an
gx4

+ (Jn
gx+)in
(15.40)

<!-- page 573 (PDF 591) -->
(Jn
gx□)out = □Jn
gx□ + (Jn
gx□)in = Dg
n
d
dx ϕ
n
gx □ Δx

+ (Jn
gx□)in
= Dg
n
Δx
an
gx1 □ 3an
gx2 + 1
2 an
gx3 □ 1
5 an
gx4

+ (Jn
gx□)in
(15.41)
with similar expressions for the y- and z-direction surface-averaged currents at
±Δy/2 and ±Δz/2, respectively.
If the polynomial expansion of the x-direction flux in Eq. (15.34) is terminated
at I = 2, and similarly for the y- and z-direction expansions, the transverse
integrated nodal equations are well posed in terms of node-averaged fluxes
and incoming and outgoing partial currents over node boundaries (i.e., the
number of equations and the number of unknowns agree). Equations (15.38)
and (15.12) can be used to express Eqs. (15.40) and (15.41) in terms of nodeaveraged
flux and partial currents at x = ±Δx/2:
(Jn
gx+)out 1 + 8Dg
n
Δx

+ (Jn
gx□)out
4Dg
n
Δx □ 6Dg
n
Δx ϕ
n
g
= (Jn
gx+)in 1 □ 8Dg
n
Δx

+ (Jn
gx□)in □ 4Dg
n
Δx

(15.42)
(Jn
gx□)out 1 + 8Dg
n
Δx

+ (Jn
gx+)out
4Dg
n
Δx □ 6Dg
n
Δx ϕ
n
g
= (Jn
gx□)in 1 □ 8Dg
n
Δx

+ (Jn
gx+)in □ 4Dg
n
Δx

(15.43)
with similar expressions for the y- and z-direction surface-averaged currents at
±Δy/2 and ±Δz/2, respectively. Equation (15.8) can be used to replace the
currents with partial currents in the nodal balance Eq. (15.9) to obtain
Δx
(
(Jn
gx+)out + (Jn
gx□)out
h
i
□ (Jn
gx+)in + (Jn
gx□)in
h
i)
+ 1
Δy
(
(Jn
gy+)out + (Jn
gy□)out
h
i
□ (Jn
gy+)in + (Jn
gy□)in
h
i)
+ 1
Δz
(
(Jn
gz+)out + (Jn
gz□)out
h
i
□ (Jn
gz+)in + (Jn
gz□)in
h
i)
+ Σg
tnϕ
n
g =
X
G
g´=1
Σg´!g
n
ϕ
n
g´ + χg
k
X
G
g´=1
vΣg´
f nϕ
n
g´;
g = 1; . . . ; G
(15.44)
Note that this equation could be derived directly by integrating Eq. (15.1) over the
node.

<!-- page 574 (PDF 592) -->
The incoming x-direction partial currents to node n may be related to the
outgoing partial currents from the adjacent node n + 1 at Δx/2. Using the flux
discontinuity condition discussed in Chapter 14, the surface-averaged fluxes are
related by
f n
gx+ϕn
gx+ = f n+1
gx□ϕn+1
gx□
f n
gx+[(Jn
gx+)out + (Jn
gx+)in] = f n+1
gx□[(Jn+1
gx□)out + (Jn+1
gx□)in]
(15.45)
where Eq. (15.12) has been used to write the second form of the equation. For
unity flux discontinuity factors, Eq. (15.45) becomes the continuity of flux
condition. The surface-averaged current continuity condition
Jn
gx+ = Jn+1
gx□
(Jn
gx+)out □ (Jn
gx+)in = (Jn+1
gx□)in □ (Jn+1
gx□)out
(15.46)
may be combined with the flux discontinuity condition to obtain
(Jn
gx+)in =
2(Jn+1
gx□)out
1 + f n
gx+=f n+1
gx□
+
1 □ f n
gx+=f n+1
gx□
1 + f n
gx+=f n+1
gx□
(Jn
gx+)out
(15.47)
Imposition of similar conditions at the interface with adjacent node n □ 1 at □Δx/
2 yields
(Jn
gx□)in =
2(Jn□1
gx+)out
1 + f n
gx□=f n□1
gx+
+
1 □ f n
gx□=f n□1
gx+
1 + f n
gx□=f n□1
gx+
(Jn
gx□)out
(15.48)
Similar expressions are obtained relating the incoming y- and z-direction surfaceaveraged
partial currents at ±Δy/2 and ±Δz/2, respectively, to the outgoing
partial currents from the adjacent nodes in the y- and z-directions.
The equations above can be derived directly from an expansion of the form
ϕn
g(x; y; z) = ϕg +
X
i=1
αn
gxif i(x) +
X
j=1
αgyjf j(y) +
X
k=1
αn
gzkf k(z)
(15.49)
without recourse to the transverse integration stratagem. In fact, Eqs. (15.44)
follow directly from Eqs. (15.8) and (15.9), and the interface conditions of
Eqs. (15.45) and (15.46) arise from other considerations. However, this transverse
integration stratagem is essential for extending the formalism to higher order.
For polynomial expansions with I>2 in Eq. (15.34), the transverse integrated
equations are no longer well posed in the sense of having the same number of
equations and unknowns. However, weighted residuals methods can be used to

<!-- page 575 (PDF 593) -->
develop higher order approximations, but this requires the further approximation
of higher order leakage moments. Multiplying Eq. (15.25) by the spatial function
wi(x) and integrating yields
wi(x); d
dx J
n
gx(x)

+ Σn
tnϕn
gxi
=
X
G
g´=1
Σg´!g
n
ϕn
g´xi + χg
k
X
G
g´=1
vΣn
f g´ϕn
g´xi □ 1
Δy Lg
nyxi □ 1
Δz Lg
nzxi
(15.50)
where the ith spatial moment of the flux is
ϕ
n
gxi ≡ hwi(x); ϕ
n
gx(x)i ≡ 1
Δx ∫
(Δx=2)
□(Δx=2)
dxwi(x)ϕ
n
gx(x)
(15.51)
and the ith spatial moment of the transverse leakage is
Lg
nyxi ≡ hwj(x); Lg
ny(x)i ≡ 1
Δx ∫
(Δx=2)
□(Δx=2)
dxwi(x)Lg
ny(x)
(15.52)
with a similar term for the z-direction transverse leakage.
The nodal balance equation results from choosing w0 = 1 in Eq. (15.50).
Numerical comparison with detailed finite-difference solutions indicates that
the choices w1(x) = f1(x) and w2(x) = f2(x) yield good results. Using these two
functions and integrating the first term in Eq. (15.50) by parts yields the two
equations that must be solved for the higher order flux moments:
2Δx Tg
nx + Dg
n
(Δx)2 αn
gx1 + Σg
tnϕn
gx1
=
X
G
g´=1
Σg´!g
n
ϕn
g´x1 + χg
k
X
G
g´=1
vΣn
f g´ϕn
g´x1 □ 1
Δy Lg
nyx1 □ 1
Δz Lg
nzx1
(15.53)
2Δx Lg
nx + 3Dg
n
(Δx)2 αn
gx2 + Σg
tnϕn
gx2
=
X
G
g´=1
Σg´!g
n
ϕn
g´x2 + χg
k
X
G
g´=1
vΣn
f g´ϕn
g´x2 □ 1
Δy Lg
nyx2 □ 1
Δz Lg
nzx2
(15.54)
where
Tg
nx ≡ Jn
gx+ + Jn
gx□;
Lg
nx ≡ Jn
gx+ □ Jn
gx□
(15.55)

<!-- page 576 (PDF 594) -->
Using w1(x) = f1(x) and w2(x) = f2(x) and Eq. (15.49) in Eq. (15.51) then yields
the higher order expansion coefficients
αn
gx3 = □120ϕn
gx1 + 10αn
gx1;
αn
gx4 = □700ϕn
gx2 + 35αn
gx2
(15.56)
Solution of Eqs. (15.54)) requires further approximation for the x-dependence
of the x-direction transverse leakage (and similarly for the y- and z-direction
transverse leakage terms). A number of approximations have been used, but the
most successful has been the quadratic approximation
Lg
ny(x) = L
g
ny + Cn
gy1f 1(x) + Cn
gy2f 2(x)
(15.57)
which is assumed, for the purpose of evaluating moments of the transverse
leakage, to extend over node n and the two nodes adjacent to node n in
the x-direction. Use of Eq. (15.57) in Eq. (15.52) then makes it possible to
evaluate the transverse leakage moments in terms of the surface-averaged
leakages (thus surface-averaged partial currents) in the adjacent nodes.
Combining results in the three coordinate directions leads to an interface
current balance in each group of the form
J n;out
g
= Pn
g[Qn
g □ Ln
g] + Rn
gJ n;in
g
(15.58)
The column vectors J n;out
g
and Jn;in
g
contain the six outgoing and incoming,
respectively, surface-averaged partial currents for the nth node. The column
vector Qn
g contains the node-averaged scatter-in and fission sources to group g,
and Ln
g contains the higher order spatial moments of the transverse leakage
computed using the quadratic fit or some other approximation. The matrices Pn
g
and Rn
g contain nodal coupling coefficients. A variety of iterative schemes have
been devised for solving Eq. (15.58), within an outer power iteration solution
procedure. Generally, the three-dimensional geometry is subdivided into a
number of axial planes, and the nodes within each plane are solved (swept) a
few times using the most recent values for group fluxes in nodes in the adjacent
planes. The number of planar sweeps required per group generally increases with
the planar average diffusion length within the group.
The nodal procedure outlined above uses constant homogenized cross sections
over the node. In applications where the actual cross sections vary significantly
over the node, the use of constant cross sections introduces an error in calculating
effects such as space-dependent internodal burnup. An extension to include loworder
polynomial dependence of the cross sections over the node has been shown
to lead to improved accuracy in such cases.

### Analytical Methods

There are variants of the transverse integrated method in which an analytical
solution is used in some part of the derivation of the transverse integrated nodal
