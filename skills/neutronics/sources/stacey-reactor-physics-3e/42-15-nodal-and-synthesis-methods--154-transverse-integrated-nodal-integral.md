# 15 Nodal and Synthesis Methods — 15.4 Transverse Integrated Nodal Integral Transport Theory Models … 15.6 Finite-Element Coarse-Mesh Methods
<!-- source PDF pages 595-612 -->

<!-- page 577 (PDF 595) -->
equations. In a variant known as the analytical nodal method, the onedimensional
transverse integrated equation is integrated analytically to relate
the nodal leakage in that dimension to the nodal average fluxes in the node and in
the adjacent nodes in that dimension. In another variant known as the nodal
Green’s function method, the one-dimensional transverse integrated equation is
formally solved by the method of Green’s functions, resulting in expressions that
can be used together with the polynomial expansion to evaluate coefficients.
These are discussed more fully in Ref. [1].

### Heterogeneous Flux Reconstruction

The results of the nodal calculation are global node-averaged fluxes, ϕ
n
g flux
distributions consisting of the polynomial flux distributions ϕn
g(x; y; z) within each
node or assembly n [e.g., as constructed from Eqs. (15.34) for each direction], and
nodal interface currents. These global fluxes and flux distributions are normalized
to the reactor power level. To obtain a more detailed heterogeneous intraassembly
flux distribution, it is necessary to superimpose on these nodal average
or smoothly varying polynomial flux distributions a detailed intranodal flux
shape, An
g(x; y), usually taken from a planar assembly transport calculation:
Φn
g(x; y; z) = ϕn
g(x; y; z)An
g(x; y)
(15.59)
The simplest such procedures use an assembly calculation with symmetry
boundary conditions to determine An
g(x; y) and Eq. (15.59). Improved accuracy
has been obtained by using the first of Eqs. (15.59) to construct a gross intranodal
flux distribution that approximates the gross intranodal flux shape from the
global calculation. Use of the same intranodal flux shape for the nodal homogenization
and flux reconstruction is necessary for consistency, but this is difficult to
achieve in practice without an iteration among the homogenization, nodal
solution, and flux reconstruction steps.

## 15.4 Transverse Integrated Nodal Integral Transport Theory Models

### Transverse Integrated Integral Transport Equations

The concepts and procedures introduced in Section 15.3 can be extended to
develop nodal methods based on integral transport theory. To limit the notational
complexity, we discuss the development of integral transport nodal methods in
two-dimensional rectangular geometry, although we note that three-dimensional
models are in use for nuclear reactor analysis. Assuming that a detailed heterogeneous
assembly transport calculation has been performed to produce homogenized
multigroup constants that are uniform over the domain of node n (□Δx/
2 ≤ x ≤ Δx/2, □Δy/2 ≤ y ≤ Δy/2), the transport equation for the multigroup
neutron flux within node n in two-dimensional Cartesian geometry may be

<!-- page 578 (PDF 596) -->
written as
μ @
@x ψn
g(x; y; μ; ϕ) +
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cosϕ @
@y ψn
g(x; y; μ; ϕ) + Σg
tnψn
g(x; y; μ; ϕ)
= 1
4π Sn
g(x; y);
g = 1; . . . ; G
(15.60)
where, for notational convenience, the group in-scatter and fission terms have
been written as a source term:
Sn
g(x; y) = χg
k
X
G
g´=1
vΣg´
f ∫
□1
dμ∫
2π
dϕψn
g´(x; y; μ; ϕ)
+
X
G
g´=1
vΣg´!g
n
∫
□1
dμ∫
2π
dϕψn
g´(x; y; μ; ϕ)
(15.61)
isotropic scattering has been assumed, and the coordinate system is defined such
that
Ωx ≡ Ω ⋅nx = μ;
Ωy ≡ Ω ⋅ny =
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cosϕ
(15.62)
The coordinate system and spatial domain of node n are depicted in Figs. 15.2 and
15.3.
θ
X
Z
Y
Ωx = cos θ = μ
Ω
→
Ωy = sin θcos ϕ =  1–μ2 cos ϕ
ϕ
Ωyz = sin θ =  1–μ2
Fig. 15.2 Coordinate system for two-dimensional nodal transport model.

<!-- page 579 (PDF 597) -->
ΔY
Y
X
ΔX
–ΔX
–ΔY
Fig. 15.3 Spatial domain for two-dimensional nodal model.
Integrating Eq. (15.60) over □Δy/2 ≤ y ≤ Δy/2 yields the one-dimensional
x-direction transverse integrated transport equation for node n:
μ @
@x ψn
gx(x; μ; ϕ) + Σg
tnψn
gx(x; μ; ϕ) + Lg
ny(x; μ; ϕ)
= 1
4π ∫
Δy=2
□Δy=2
dySn
g(x; y) ≡ 1
4π Sn
g(x)
(15.63)
where the x-direction angular flux is
ψn
gx(x; μ; ϕ) ≡ 1
Δy ∫
Δy=2
□Δy=2
dyψn
g(x; y; μ; ϕ)
(15.64)
and the transverse leakage term defining the average net neutron loss rate across
the node boundaries at y = □Δy/2 and y = Δy/2 is
Lg
ny(x; μ; ϕ)
≡ 1
Δy
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cos ϕ ψn
g
x; + Δy
2 ; μ; ϕ

□ ψn
g
x; □ Δy
2 ; μ; ϕ

(15.65)
Equation (15.63) can be integrated if the scattering, fission, and leakage are
treated as a known source:
ψn
gx(x; μ > 0; ϕ) =
∫
x
□(Δx=2)
dx´e□Σg
tn(x□x´)=μ 1
μ
4π Sn
g(x´) □ Lg
ny(x´; μ; ϕ)

+ψn;in
gx□(μ; ϕ)e□Σg
tn(x+(Δx=2))=μ;
μ > 0
(15.66a)

<!-- page 580 (PDF 598) -->
ψn
gx(x; μ < 0; ϕ) = □∫
(Δx=2)
x
dx´e□Σg
tn(x□x´)=μ
□ 1
μ
4π Sn
g(x´) □ Lg
ny(x´; μ; ϕ)

+ψn;in
gx+(μ; ϕ)e□Σg
tn(x□(Δx=2))=μ;
μ < 0
(15.66b)
where the inward-directed average angular fluxes at x = Δx/2 and x = □Δx/2 are
ψn;in
gx−(μ; ϕ) ≡ ψn
gx − Δx
2 ; μ£0; ϕ

(15.67)
and the outward-directed average angular fluxes at x = Δx/2 and x = □Δx/2 are
ψn;out
gx− (μ; ϕ) ≡ ψn
gx − Δx
2 ; μ≷0; ϕ

(15.68)
The average scalar flux in the x-direction problem is
ϕn
gx(x) = ∫
2π
dϕ ∫
dμψn
gx(x; μ > 0; ϕ) + ∫
□1
dμψn
gx(x; μ < 0; ϕ)

= 1
2 ∫
Δx=2
□Δx=2
dx´E1(Σg
tnjx □ x´j) Sn
g(x´) □ Lg;iso
ny (x´)
h
i
□ ∫
Δx=2
□Δx=2
dx´
∫
dμ
μ e□Σg
tnjx□x´jμ
∫
2π
Lg;anis
ny
(x´; jμj; ϕ)dϕ
+ ∫
dμe□Σg
tn(x+(Δx=2))=μ
∫
2π
ψn;in
gx□(μ; ϕ)dϕ
+ ∫
□1
dμe□Σg
tn(x□(Δx=2))=μ
∫
2π
ψn;in
gx+(μ; ϕ)dϕ
(15.69)
where the exponential integral function is
En(ξ) ≡ ∫
dμμn□2exp □ ξ
μ

(15.70)
and the transverse leakage has been split into an isotropic and an anisotropic
component:
Lg
ny(x´; μ; ϕ) = 1
4π Lg;iso
ny (x´) + Lg;anis
ny
(x´; μ; ϕ)
(15.71)

<!-- page 581 (PDF 599) -->
### Polynomial Expansion of Scalar Flux

Following the same general procedure used to develop the diffusion theory nodal
model, the scalar flux for the x-direction problem is expanded:
ϕn
gx(x) =
X
I
i=1
aiϕn
gxif i(x);
I ≤ 2
(15.72)
The expansion coefficients are normalized such that
ai
≡ 1
Δx ∫
Δx=2
□Δx=2
dx[f i(x)]2
(15.73)
and the polynomials
f 0 = 1;
f 1(x) = x
Δx ;
f 2(x) = 3
x
Δx
□ 1
(15.74)
are used. The moments of the scalar flux are
ϕn
gxi ≡ ∫
Δx=2
□Δx=2
dxϕn
gx(x)f i(x)
(15.75)
so that ϕn
gx0 is the node-averaged scalar flux.

### Isotropic Component of Transverse Leakage

The surface average of the isotropic component of the transverse leakage is
L
g;iso
ny
≡ 1
Δx ∫
Δx=2
□Δx=2
dxLg;iso
ny (x)
= [(Jn
gy+)out □ (Jn
gy+)in] □ [(Jn
gy□)in □ (Jn
gy□)out]
(15.76)
where the surface average of the outward and inward partial currents at +Δy/2
and □Δy/2 are
(Jn
gy+)out ≡ ∫
2π
dϕ∫
dμμψn;out
gy+ (μ; ϕ)
(Jn
gy□)out ≡ ∫
2π
dϕ∫
□1
dμμψn;out
gy□ (μ; ϕ)
(15.77)

<!-- page 582 (PDF 600) -->
and
(Jn
gy+)in ≡ ∫
2π
dϕ∫
□1
dμμψn;in
gy+(μ; ϕ)
(Jn
gy□)in ≡ ∫
2π
dϕ∫
dμμψn;in
gy□(μ; ϕ)
(15.78)
respectively, with the directional neutron fluxes at +Δy/2 and □Δy/2, ψn;in
gy− and
ψn;out
gy−
defined by equations similar to Eqs. (15.67) and (15.68).

### Double-Pn Expansion of Surface Fluxes

The angular dependence of the neutron flux on the surfaces of the node is
approximated by a double-P1 approximation, which allows independent linearly
anisotropic distributions for the incident and exiting fluxes on a surface. In terms
of the half-space polynomials, which are related to the Legendre polynomials by
p+
n(ξ) = Pn(2ξ □ 1) for 1 □ ξ □ 0 and p□
n(ξ) = Pn(2ξ + 1) for 0 □ ξ □ □1, the surfaceaveraged
inward neutron fluxes at ±Δx/2 are expanded:
ψn;in
gx−(μ; ϕ) ≡ ψn
gx − Δx
2 ; μ£0; ϕ

≈ 1
2π
2 a−
0 p□
0 + 3
2 a−
1xp□
1 (Ωx) + 3
2 a−
1yp□
1 (Ωy)

≈ 1
2π
2 C−
0 + 3
2 C−
1xμ + 3
2 C−
1y
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cosϕ

= 1
2π
4ϕ
n;in
gx− − 6Jn;in
gx−
+ 1
2π
12J
n;in
gx− − 6ψn;in
gx−
μ
+ 1
2π (3J
n;in
gx−)
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cosϕ
(15.79)
The angular moments of the surface-averaged inward fluxes that appear in
Eq. (15.79) are
ψn;in
gx□ ≡ ∫
2π
dϕ∫
dμψn;in
gx□(μ; ϕ)
ψn;in
gx+ ≡ ∫
2π
dϕ∫
□1
dμψn;in
gx□(μ; ϕ)
J
n;in
gx□ ≡ ∫
2π
dϕ∫
dμμψn;in
gx□(μ; ϕ)
J
n;in
gx+ ≡ ∫
2π
dϕ∫
□1
dμμψn;in
gx+(μ; ϕ)
J
n;in
gy□ ≡ ∫
2π
dϕ∫
dμ
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cosϕψn;in
gy□(μ; ϕ)
J
n;in
gy+ ≡ ∫
2π
dϕ∫
□1
dμ
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cosϕψn;in
gy+(μ; ϕ)
(15.80)

<!-- page 583 (PDF 601) -->
Using Eq. (15.79) to evaluate the integrals involving the incident fluxes in
Eq. (15.69) yields
ϕn
gx(x) = ∫
Δx=2
□Δx=2
dx´E1(Σg
tnjx □ x´j) 1
2 Sn
g(x´) □ Lg;iso
ny (x´)
h
i
□ ∫
Δx=2
□Δx=2
dx´
∫
dμ
μ e□Σg
tnjx´□x´j=μ
∫
2π
dϕLg;anis
ny
(x´; jμj; ϕ)
+ ψn;in
gx□ 4E2 Σg
tn x + Δx

□ 6E3 Σg
tn x + Δx

+ J
n;in
gx□ 12E3 Σg
tn x + Δx

□ 6E2 Σg
tn x + Δx

+ ψn;in
gx+ 4E2 Σg
tn
Δx
2 □ x

□ 6E3 Σg
tn
Δx
2 □ x

+ J
n;in
gx+ 6E2 Σg
tn
Δx
2 □ x

□ 12E3 Σg
tn
Δx
2 □ x

(15.81)

### Angular Moments of Outgoing Surface Fluxes

The angular moments of the surface-averaged outgoing flux and current at Δx/2
can be constructed from Eq. (15.66a), using Eq. (15.79) to expand the angular
dependence of the incoming flux at □Δx/2:
ψn;out
gx+ ≡ ∫
2π
dϕ∫
dμψn
gx
Δx
2 ; μ > 0; ϕ

= ∫
Δx=2
□Δx=2
dx´E1 Σg
tn
Δx
2 □ x´

2 Sn
g(x´) □ Lg;iso
ny (x´)
h
i
□∫
Δx=2
□Δx=2
dx´
∫
dμ
μ e□Σg
tn((Δx=2)□x´)=μ
∫
2π
Lg;anis
ny
(x´; μ; ϕ)dϕ
+ ψn;in
gx□[4E2(Σg
tnΔx) □ 6E3(Σg
tnΔx)]
+ J
n;in
gx□[12E3(Σg
tnΔx) □ 6E2(Σg
tnΔx)]
(15.82)
J
n;out
gx+ ≡ ∫
2π
dϕ∫
dμμψn
gx
Δx
2 ; μ > 0; ϕ

= ∫
Δx=2
□Δx=2
dx´E2 Σg
tn
Δx
2 □ x´

2 Sn
g(x´) □ Lg;iso
ny (x´)
h
i
□∫
Δx=2
□Δx=2
dx´
∫
dμe□Σg
tn((Δx=2)□x´)=μ
∫
2π
Lg;anis
ny
(x´; μ; ϕ)dϕ
+ ψn;in
gx□[4E3(Σg
tnΔx) □ 6E4(Σg
tnΔx)]
+ J
n;in
gx□[12E4(Σg
tnΔx) □ 6E3(Σg
tnΔx)]
(15.83)

<!-- page 584 (PDF 602) -->
The angular moments of the surface-averaged outgoing flux and current at
□Δx/2 can be constructed from Eq. (15.66b), using Eq. (15.79) to expand the
angular dependence of the incoming flux at +Δx/2:
ψn;out
gx□ ≡ ∫
2π
dϕ∫
□1
dμψn
gx □ Δx
2 ; μ < 0; ϕ

= ∫
Δx=2
□Δx=2
dx´E1 Σg
tn
Δx
2 + x´

2 Sn
g(x´) □ Lg;iso
ny (x´)
h
i
□ ∫
Δx=2
□Δx=2
dx´
∫
□1
dμ
μ eΣg
tn(Δx=2+x´)=μ
∫
2π
dϕLg;anis
ny
(x´; μ; ϕ)
+ ψn;in
gx+[4E2(Σg
tnΔx) + 6E3(Σg
tnΔx)]
+ J
n;in
gx+[12E3(Σg
tnΔx) + 6E2(Σg
tnΔx)]
(15.84)
J
n;out
gx□ ≡ ∫
2π
dϕ∫
□1
dμμψn
gx □ Δx
2 ; μ < 0; ϕ

= ∫
Δx=2
□Δx=2
dx´E2 Σg
tn
Δx
2 + x´

2 Sn
g(x´) □ Lg;iso
ny (x´)
h
i
+ ∫
Δx=2
□Δx=2
dx´
∫
□1
dμeΣg
tn((Δx=2)+x´)=μ
∫
2π
dϕLg;anis
ny
(x´; μ; ϕ)
+ ψn;in
gx+[4E3(Σg
tnΔ) + 6E4(Σg
tnΔx)]
+ J
n;in
gx+[12E4(Σg
tnΔx) + 6E3(Σg
tnΔx)]
(15.85)

### Nodal Transport Equations

These equations can be written, in terms of matrices and column vectors, in a
form analogous to the diffusion theory relation of Eq. (15.58):
ψn;out
g
= ~P
n
g[Qn
g □ Ln
g] + ~R
n
gψn;in
g
(15.86)
The column vectors Qn
g and Ln
g are defined as for diffusion theory and represent
the fission plus in-scatter source and the transverse leakage, respectively. The
column vector ψn;out
g
contains outgoing surface-averaged partial currents
[Eqs. (15.83) and (15.85)] and half-angle integrated fluxes [Eqs. (15.82) and
(15.84)]; and the column vector ψn;in
g
contains incoming surface-averaged partial
currents and half-angle integrated fluxes [Eqs. (15.80)] for each of the six (in three
dimensions) nodal surfaces. The matrices Pn
g and Rn
g contain the nodal coupling
coefficients.
The transverse integrated formulation allows for direct transmission of neutrons
entering node n over the x-surface at □Δx/2 across the node to exit over the

<!-- page 585 (PDF 603) -->
x-surface at +Δx/2 [e.g., the ψn;in
gx+ and Jn;in
gx+ terms in Eqs. (15.82) and (15.83)], but
does not allow for the direct transmission of neutrons entering node n over an
x-surface across the node to exit over a y- or z-surface.

## 15.5 Transverse Integrated Nodal Discrete Ordinates Method

A nodal transport equation can also be formulated in terms of the discrete
ordinates approximation. The development is similar to that of Sections 15.3 and
15.4 and we will only briefly examine how the nodal coupling equations
are formulated in terms of discrete ordinates. In two-dimensional Cartesian
geometry, the multigroup discrete ordinates equations with isotropic scattering
within a node of constant homogenized cross section may be written as
μm @ψm
g
@x (x; y) + μm @ψm
g
@y (x; y) + Σg
t ψm
g (x; y) = Σg
s
2π ϕg(x; y) + Qg(x; y)
2π
(15.87)
where ψm
g (x; y) = ψg(x; y; Ωm) is the group flux in the ordinate direction Ωm,
μm = nx □ Ωm, and ηm = ny □ Ωm. Letting the node extend over □Δx/2 < x < Δx/2,
□Δy/2 < y Δy/2, and integrating Eq. (15.87) over □Δy/2 < y < Δy/2 leads to the
transverse integrated one-dimensional discrete ordinates equation
μm @ψm
gx(x)
@x
+ Σg
t ψm
gx(x) = Σg
sϕg(x)
2π
+ Qg
x(x)
2π
□
Lg
mg(x)
Δy
≡ Sm
g (x)
(15.88)
where the y-direction transverse leakage is
Lg
my(x) ≡ ∫
(Δy=2)
□(Δy=2)
dyηm @ψm
g (x; y)
@y
= ηm ψm
gy+(x) □ ψm
gy□(x)
h
i
(15.89)
and ψm
gy−(x) = ψm
gy(x; y = −Δy=2).
We now make a polynomial expansion of Sm
g (x) within the node in the
polynomials
f 0(x) = 1;
f 1(x) = x;
f 2(x) = x2 □ 1
12 ;
f 3(x) = x3 □ 3
20 x
f 4(x) = x4 □ 3
14 x2 + 3
560 ;
f 5(x) = x5 □ 5
18 x3 + 5
336 x
f 6(x) = x6 □ 15
44 x4 + 5
176 x2 □
14; 784
(15.90)

<!-- page 586 (PDF 604) -->
integrate Eq. (15.88) over □Δx/2 < x < Δx/2 in the direction of neutron flow (i.e.,
from □Δx/2 to +Δx/2 for μm > 0 and in the opposite direction for μm < 0), and
make use of the orthogonality property
∫
Δx=2
□Δx=2
f i(x)f j(x)dx =
∫
Δx=2
□Δx=2
dxf 2
i (x)
"
δij
(15.91)
to obtain a relation among the outward-directed fluxes at one boundary, the inwarddirected
fluxes at the other boundary, and the group sources within the node
ψm;out
gx−
= 1
μm
X
i=0
Sm
gi∫
Δx=2
□Δx=2
f i(−x)e(Σg
t (x□Δx=2))=μmdx
+ψm;in
gx□ e□(Σg
t Δx=jμmj)
(15.92)
where the Sm
gi are the coefficients of the polynomial expansion of Sm
g (x).
Equation (15.88) can be integrated over □Δx/2 < x´ < x for μm > 0 and in the
opposite direction for μm < 0 to obtain an expression for the flux ψm
gx(x) similar to
that given by Eq. (15.92) but with the upper limit of the integral replaced by x. This
expression can expanded in polynomials, multiplied by fi, and integrated over
□Δx/2 < x < Δx/2 to obtain an expression for the ith node-averaged flux expansion
coefficient in terms of the inward flux at ±Δx/2 and the group sources within
the node:
ψm
gi =
μmDi
X
j=0
Sm
gj∫
Δx=2
□Δx=2
dxf i(−x)∫
x
□Δx=2
dx´f j(−x´)e(Σt(x´□x)=jμmj)
+ 1
Di
ψm;in
gx□ ∫
Δx=2
□Δx=2
f i(−x)eΣg
t (x□Δx=2)=jμmj;
i = 0; . . . ; 6
(15.93)
The fluxes at the interface between nodes n □ 1 and n are coupled by
(ψm;out
gx+ )n□1 = (ψm;in
gx□ )n;
μm > 0
(ψm;in
gx+ )n□1 = (ψm;out
gx□ )n;
μm < 0
(15.94)
which enables the development of equations for solving the x-direction transverse
integrated equations. A similar procedure is then applied to develop and solve the
y-direction transverse integrated equations.

## 15.6 Finite-Element Coarse-Mesh Methods

The finite-element methodology provides a systematic procedure for developing
coarse-mesh equations with higher order accuracy than the conventional
finite-difference equations. In the finite-element method, the spatial (or other)

<!-- page 587 (PDF 605) -->
dependence of the neutron flux and current are represented by a supposition of
trial functions that are nonzero only within a limited range of the spatial variables.
These trial functions are continuous within volumes Vi, but may be discontinuous
across the interfaces between adjacent volumes. The finite-element approximation
will be developed from a variational principle that admits discontinuous trial
functions, but it could also be derived from a weighted residuals development.
The development of finite-element approximations will be discussed for onegroup
P1 and diffusion theory. The results can formally be extended to multigroup
theory by replacing the total and fission cross sections with diagonal cross section
matrices, replacing the scattering cross section with the multigroup scattering
matrix, and replacing fluxes and currents with column vectors of multigroup
fluxes and currents.

### Variational Functional for the P1 Equations

The volume of the reactor core may be subdivided into volumes Vi within which
the trial functions for the neutron flux and current are continuous. These regions
are bounded by interfaces Sk across which the trial functions may be discontinuous
. A variational functional for the one-group P1 equations is
F1fJ∗; ϕ∗; J; ϕg
= P
i ∫V i
ϕ∗
Σt □ Σs □ vΣf
k

ϕ + ∇⋅J

dr
+ P
i ∫V i
J∗⋅[D□1J + ∇ϕ]dr + P
k ∫Sk
nk⋅ϕ∗
k[Jk+ □ Jk□]ds
+ P
k ∫sk
J∗⋅nk[ϕk+ □ ϕk□]ds
(15.95)
where the first two terms are sums over the volumes within which the admissible
trial functions are continuous and the last two terms are surface integrals over the
interfaces between these volumes. The subscripts k+ and k□ refer to limiting values
as the surface k is approached from the positive and negative sides, respectively.
The stationarity of this variational functional with respect to independent and
arbitrary variations of the adjoint flux (ϕ∗) and current (J∗) within the different
volumes Vi requires that
δF1
δϕi
δϕ∗
i = ∫V i
δϕ∗
Σt □ ΣS □ vΣf
k

ϕ + ∇⋅J

dr = 0
)
∇⋅J +
Σt □ ΣS □ vΣf
k

ϕ = 0;
r ∈V i
(15.96)
δF1
δJ∗
i
δJ∗
i = ∫δJ∗⋅D□J + ∇ϕ
[
]dr = 0
)
J = □D∇ϕ;
r ∈V i
(15.97)
(i.e., that the P1 equations are satisfied within the different volumes Vi).

<!-- page 588 (PDF 606) -->
The stationarity of this variational functional with respect to independent and
arbitrary variations of the adjoint flux (ϕ∗
k) and current (J∗
k) on the interfaces
between volumes Vi requires that
δF1
δϕ∗
k
δϕ∗
k = ∫Sk
δϕ∗
knk⋅Jk+ □ Jk□
= 0
)
nk⋅Jk+ = nk⋅Jk□
(15.98)
δF1
δJ∗
k
δJ∗
k = ∫Sk
δJ∗
knk ϕk+ □ ϕk□
= 0
)
ϕk+ = ϕk□
(15.99)
(i.e., that the normal component of the current and the flux are continuous across
each interface).
Thus, the requirements that the variational functional of Eq. (15.95) is
stationary with respect to arbitrary and independent variations of the adjoint
flux and current in each volume Vi and on each interface Sk is equivalent to the
requirements that the Pl equations are satisfied within each volume Vi and that
the normal component of the current and the flux are continuous across the
interfaces bounding these volumes. This equivalence will now be exploited to
develop finite-element approximations for the neutron flux distribution.

### One-Dimensional Finite-Difference Approximation

Although it is not a finite-element approximation per se, it is instructive to derive
variationally the conventional finite-difference approximation for a slab extending
from 0 < x < a with zero flux boundary conditions. The slab is partitioned into
N mesh intervals and the flux and current are expanded in piecewise constant
functions:
ϕ(x) =
X
N□1
n=1
ϕnHn(x);
ϕ∗(x) =
X
N□1
n=1
ϕ∗
nHn(x)
(15.100)
J(x) =
X
N□1
n=0
JnKn(x);
J∗(x) =
X
N□1
n=0
J∗
nKn(x)
(15.101)
where the Hn and Kn are Heaviside functions:
Hn(x) =
1;
xn □ 1
2 hn□1 < x < xn + 1
2 hn
0;
otherwise
>
<
>
:
K n(x) =
1;
xn < x < xn+1
0;
otherwise
<
:
(15.102)

<!-- page 589 (PDF 607) -->
Jn
Xn-1
Xn
Xn+1
hn
hn-1
ϕn, ϕn*
Fig. 15.4 Trial functions for finite-difference approximation.
the domain of which is illustrated in Fig. 15.4. The volumes Vi over which the flux
and adjoint flux trial functions are continuous are the mesh intervals xn □ hn□1/
2 < x < xn + hn/2, and the surfaces bounding these regions are at xn □ hn□1/2 and
xn + hn/2. The volumes Vi over which the current and adjoint current trial
functions are continuous are the mesh intervals xn < x < xn+1, and the surfaces
bounding these regions are at xn and xn+1.
For the piecewise constant adjoint flux trial functions of Eq. (15.100), the
variations on the surfaces are not independent of the variations in the volumes;
that is, instead of having separate Eqs. (15.96) and (15.98), these two equations
must be combined, leading in this case to
δF1
δϕ∗δϕ∗=
X
N□1
n=1
δϕ∗
n
∫
xn+1
2hn
xn□1
2hn□1
dx
Σt □ ΣS □ vΣf
k

ϕ + dJ
dx

(
+(Jn □ Jn□1)
)
=
X
N□1
n=1
δϕ∗
n
2 hn□1 Σtn□1 □ Σsn□1 □ vΣf n□1
k

+ 1
2 hn Σtn □ Σsn □ vΣf n
k

ϕn + (Jn □ Jn□1)

= 0
(15.103)
where the materials properties denoted by the subscript n have been taken to be
uniform in the interval xn ≤ x ≤ xn+1. Similarly, the variations of the adjoint
current trial functions in the volumes and on the surfaces are not independent,
requiring that Eqs. (15.97) and (15.99) be combined to yield
δF1
δJ∗δJ∗=
X
N□1
n=0
δJ∗
n
∫
xn+1
xn
dx D□1J + dϕ
dx

+ (ϕn+1 □ ϕn)

=
X
N□1
n=0
δJ∗
n[hnD□1
n Jn + (ϕn+1 □ ϕn)] = 0
(15.104)

<!-- page 590 (PDF 608) -->
Requiring that the variational functional be stationary with respect to arbitrary
and independent variations δϕ∗
n and f mn
ijk (x; y) in each mesh interval yields
2 hn□1 Σtn□1 + Σsn□1 □ vΣf n□1
k

+ 1
2 hn Σtn □ Σsn □ vΣf n
k

ϕn
+ (Jn □ Jn□1) = 0
Jn = □Dn
ϕn+1 □ ϕn
hn
(15.105)
which may be combined to obtain the standard form of the finite-difference
diffusion equation:
2 hn□1 Σtn□1 □ Σsn□1 □ vΣf n□1
k

+ 1
2 hn Σtn □ Σsn □ vΣf n
k

+ Dn□1
hn□1
+ Dn
hn

ϕn □ Dn□1
hn□1
ϕn□1 □ Dn+1
hn
ϕn+1 = 0
(15.106)
The volumes Vi over which the flux and adjoint flux trial functions are continuous
are the mesh intervals xn □ hn□1/2 < x < xn + hn/2, and the surfaces bounding
these regions are at xn □ hn□1/2 and xn + hn/2.

### Diffusion Theory Variational Functional

We shall restrict our attention to trial functions that are continuous over the
volume of the reactor, which means that the last term in the variational functional
of Eq. (15.95) is identically zero. We further restrict ourselves to current and
adjoint current trial functions that satisfy Fick’s law, so that the second term in
Eq. (15.95) is identically zero and the current in the first and third terms may be
replaced by □D∇ϕ to obtain the diffusion theory variational functional:
Fdfϕ∗; ϕg = P
i ∫V i
ϕ∗
Σt □ Σs □ vΣf
k

ϕ □ ∇⋅D∇ϕ

dr
+ P
k ∫Sk
ϕ∗ns[(□D∇ϕ)k+ □ (□D∇ϕ)k□]dS
= P
i ∫V i
ϕ∗Σt □ Σs □ vΣf
k

ϕ + ∇ϕ∗⋅D∇ϕ

dr
(15.107)
The second form of this functional resulted from integrating the divergence in the
first term by parts over the various volumes to obtain terms that cancel identically
with the interior surface terms in the second term and vanish on the outer

<!-- page 591 (PDF 609) -->
boundary because of the physical boundary condition. Note that this second form
of the functional admits trial functions that do not identically satisfy continuity of
□D∇ϕ □ ns across interior surfaces.

### Linear Finite-Element Diffusion Approximation in One Dimension

We consider the same problem as above, a slab reactor with zero flux boundary
conditions in one-group diffusion theory. The neutron flux is expanded
ϕ(x) =
X
N□1
n=1
ϕnHn(x);
ϕ∗(x) =
X
N□1
n=1
ϕ∗
nHn(x)
(15.108)
in tent function trial functions
Hn(x) =
xn+1 □ x
hn
;
xn < x < xn+1
x □ xn□1
hn□1
;
xn□1 < x < xn
0;
otherwise
>
>
>
>
<
>
>
>
>
:
(15.109)
depicted in Fig. 15.5. The volumes Vi over which the trial functions ϕ and ϕ∗of
Eq. (15.108) and the vectors D∇ϕ and D∇ϕ∗are continuous are just the mesh
intervals xn□1 < x < xn, and the surfaces are the xn. Requiring that the variational
functional of Eq. (15.107) be stationary with respect to arbitrary and independent
variations in all the adjoint trial functions yields
Hn(x)
Hn+1(x)
Xn-1
Xn
Xn+1
Xn+2
hn+1
hn
hn-1
ϕn+1
ϕn
Fig. 15.5 Trial functions for linear finite-element approximation.

<!-- page 592 (PDF 610) -->
δFd
δϕ∗
n
δϕ∗
n = δϕ∗
n
"
∫
xn
xn□1
(
x □ xn
hn□1
Σtn□1 □ Σsn□1 □ vΣf n□1
k

□
X
n+1
n´=n□1
ϕn´Hn´(x) + Dn□1
hn□1
X
n+1
n´=n□1
d
dx ϕn´Hn´(x)
)
dx
+∫
xn+1
xn
(
xn+1 □ x
hn
Σtn □ Σsn □ vΣf n
k

□
X
n+1
n´=n□1
ϕn´Hn´(x) □ Dn
hn
X
n+1
n´=n□1
d
dx ϕn´Hn´(x)
)
dx
= 0
(15.110)
Carrying out the integration results in a three-point coarse-mesh equation for
each mesh point:
hn□1 Σtn□1 □ Σsn□1 □ vΣf n□1
k

3 ϕn + 1
6 ϕn□1

+ hn Σtn □ Σsn □ vΣf n
k

3 ϕn + 1
6 ϕn+1

+ Dn□1
hn□1
(ϕn □ ϕn□1) □ Dn
hn
(ϕn+1 □ ϕn) = 0
(15.111)
which are similar to the finite-difference Eq. (15.106), but with more coupling
among mesh points.
Numerical studies reveal that Eqs. (15.111) can achieve the same accuracy as
Eqs. (15.106) with much larger mesh spacing, hn. This result is physically
intuitive because the piecewise linear representation of the flux allowed by the
trial functions of Eqs. (15.109) is more realistic than the step function representation
allowed by the trial functions of Eqs. (15.100) and (15.101), as
illustrated in Fig. 15.6. It stands to reason that higher order polynomial trial
Xn-2
Xn-1
Xn
Xn+1
Xn+2
Fig. 15.6 Finite-difference (solid lines) and linear finite-element (dashed lines) representation
of flux solution.

<!-- page 593 (PDF 611) -->
functions should provide an even better representation of the flux and hence be
more accurate.

### Higher Order Cubic Hermite Coarse-Mesh Diffusion Approximation

The cubic Hermite interpolating polynomials
H0
n(x) =
3 x □ xn□1
hn□1

□ 2 x □ xn□1
hn□1

;
xn□1 ≤ x ≤ xn
3 xn+1 □ x
hn

□ 2 xn+1 □ x
hn

;
xn ≤ x ≤ xn+1
0;
otherwise
>
>
>
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
>
>
>
:
H□
n(x) =
□ x □ xn□1
hn□1

+
x □ xn□1
hn□1

"
hn□1;
xn□1 ≤ x
_
xn
0;
otherwise
>
>
>
<
>
>
>
:
H+
n(x) =
xn+1 □ x
hn

□
xn+1 □ x
hn

"
hn;
xn ≤ x ≤ xn+1
0;
otherwise
>
>
>
<
>
>
>
:
(15.112)
are frequently used for the development of coarse-mesh finite-element approximations
. These polynomials have the properties
H0
n(xn) = dH□
n
dx (xn) = dH+
n
dx (xn) = 1
H□
n(xn) = H+
n(xn) = 0
(15.113)
These polynomials are used to construct trial functions:
ϕ(x) =
X
N□1
n=1
[ϕ0
nH0
n(x) + ϕ□
n (x)H□
n(x) + ϕ+
nH+
n(x)]
ϕ∗(x) =
X
N□1
n=1
[ϕ∗0
n H0
n(x) + ϕ∗□
n H□
n (x) + ϕ∗+
n H+
n(x)]
(15.114)
The second property of Eq. (15.113) ensures that this trial function is continuous
at the xn. Thus, the variational functional of Eq. (15.107) admits these trial
functions.

<!-- page 594 (PDF 612) -->
Requiring stationarity of the variational functional with respect to arbitrary and
independent variations of all the adjoint trial functions in all interior mesh
intervals, that is, requiring (δFd=δϕ∗0
n )δϕ∗0
n = 0, (δFd=δϕ∗□
n )δϕ∗□
n = 0, and
(δFd=δϕ∗+
n )δϕ∗+
n = 0 for n = 1, . . . , N □ 1, yields three equations for each
mesh point:
□ Dn
hn
(ϕ0
n+1 □ ϕ0
n) + Dn□1
hn□1
(ϕ0
n □ ϕ0
n□1)
+ hn Σtn □ Σsn□1 □ vΣf n
k

20 ϕ0
n + 3
20 ϕ0
n+1 □ 1
30 hnϕ□
n+1 + 1
20 hnϕ+
n

+ hn□1 Σtn□1 □ Σsn□1 □ vΣf n□1
k

□
20 ϕ0
n + 3
20 ϕ0
n□1 + 1
30 hn□1ϕ+
n□1 □ 1
20 hn□1ϕ□
n

= 0
hn Σtn □ Σsn □ vΣf n
k

□ 3
140 (ϕ0
n+1 □ ϕ0
n) + hn
420 (ϕ□
n+1 + ϕ+
n )

+ Dn
hn
□ 1
5 (ϕ0
n+1 □ ϕ0
n) + hn
10 (ϕ□
n+1 + ϕ+
n)

= 0
hn Σtn □ Σsn □ vΣf n
k

□ 1
2 (ϕ0
n+1 □ ϕ0
n) + hn
60 (ϕ□
n+1 □ ϕ+
n)

+ Dn
6 (ϕ□
n+1 + ϕ+
n) = 0
(15.115)
These equations are for the interior mesh intervals. The zero flux boundary
condition requires ϕ0
0 and ϕ0
N to vanish (or a symmetry boundary condition
would require, for example, ϕ0
0 = ϕ0
1). However, additional constraints must be
imposed to evaluate ϕ−
0 and ϕ−
N. Requiring stationarity of the variational
functional
at
the
external
boundaries
[i.e.,
(δFd=δϕ∗−
N )δϕ∗−
N = 0
and
(δFd=δϕ∗−
0 )δϕ∗−
= 0] provides the additional equations that are necessary to
specify the problem completely.
The use of cubic Hermite polynomials is found to increase the accuracy of the
finite-element approximation relative to use of the linear polynomial of Eq.
(15.109), but, of course, to increase the computing time because three equations
per mesh point are involved instead of only one. The accuracy of which we are
speaking is the error with respect to an exact solution of the homogenized
problem, not with respect to an exact solution of the true heterogeneous problem.
Although it seems plausible that a more accurate solution to the global homogeneous
problem, when combined with a local heterogeneous solution, will yield a
more accurate solution of the actual global heterogeneous problem, this is not
obvious.
