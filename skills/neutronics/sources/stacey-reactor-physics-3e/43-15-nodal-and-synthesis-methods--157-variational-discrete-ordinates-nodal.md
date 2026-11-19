# 15 Nodal and Synthesis Methods — 15.7 Variational Discrete Ordinates Nodal Method … 15.9 Single-Channel Spatial Synthesis
<!-- source PDF pages 613-631 -->

<!-- page 595 (PDF 613) -->
### Multidimensional Finite-Element Coarse-Mesh Methods

In two dimensions, the volume of a core can be partitioned into region volumes
Vi, which we refer to as elements. These elements can have a variety of shapes:
triangles, quadrilaterals, tetrahedral, and so on. A finite-element approximation
for the solution is represented by a linear combination of shape functions
associated with each element, normally polynomials in the local coordinates
within the element. A shape function has the value unity at its associated coarsemesh
point and goes to zero at the surface of the volumes Vi associated with that
element. For example, a quadratic polynomial
ϕ(x; y) = a1 + azy + a3y + a4x2 + a5xy + a6y2
(15.116)
might be used to represent the flux within a triangular element. Usually, the
polynomial is redefined so that the coefficients have the values of the flux at
various support points throughout the element. A quadratic approximation
clearly requires six support points, a linear approximation would require three
support points and so on. The value of the flux at each support point is unknown
in the resulting equations.

## 15.7 Variational Discrete Ordinates Nodal Method

The nodal and coarse-mesh calculations described in Sections 15.2–15.4 proceed
in three distinct steps: (1) the performance of local assembly two-dimensional
transport calculation and the preparation of homogenized cross sections for each
node, (2) the global solution of the nodal equations for the average flux in each
node, and (3) reconstruction of the detailed heterogeneous intranode fluxes. We
found in considering the coarse-mesh methods that the higher order polynomials
that better represented the overall flux distribution within the coarse-mesh region
led to more accurate solutions of the homogenized problem, which is solved with
nodal or coarse-mesh equations in step 2.
It is possible to combine the three steps – homogenization, flux solution, and
detailed flux reconstruction – into a single, self-consistent procedure that uses the
detailed heterogeneous assembly transport flux directly, instead of a polynomial
approximation, to represent the flux distribution within the node or coarse-mesh
region. Since a relatively high-order transport solution is needed for the heterogeneous
assembly calculation, but a relatively low-order transport calculation will
usually suffice for the global nodal calculation, we illustrate the development of a
methodology that can make use of high-order discrete ordinates heterogeneous
two-dimensional assembly calculations as trial functions to develop a low-order
discrete ordinates nodal calculational model.

<!-- page 596 (PDF 614) -->
### Variational Principle

A variational principle for the neutron transport equation is
F[ψ(r; Ω); ψ∗(r; Ω)]
=
X
Λ
λ=1
∫∫∫V λ
dV∫∫4π
dΩψ∗(r; Ω) □ Ω⋅∇ψ(r; Ω) □ Σt(r)ψ(r; Ω)

+ ∫∫4π
dΩ´ΣS(r; Ω´ ! Ω)ψ(r; Ω´) + 1
4π ∫∫4π
dΩ´vΣf (r)ψ(r; Ω´)

+ P
v(λ) ∫∫σλ;ν(λ)
dS∫∫4π
dΩH(□Ω⋅n)(Ω⋅n)ψ∗(rλ;v(λ); Ω)
□ [ψ(rλ;ν(λ); Ω) □ ψ(rν(λ);λ; Ω)]
+ ∫∫Sλ
dS∫∫4π
dΩH(□Ω⋅n)(Ω⋅n)ψ∗(rex; Ω)ψ(rex; Ω)

(15.117)
The functional F is a sum over Λ volumetric reactor regions (or nodes). The
first term of the sum is an integration over the nodal volume Vλ and the entire
solid angle (4π). The second term of the sum is a sum over all the interior surfaces
v(λ) of node λ; this term is included to allow trial functions that are discontinuous
across any surface. The notation rλ,v(λ) refers to the limit of all the points on
the surface v(λ) as approached from within node λ; similarly, rv(λ),λ refers to those
same points as approached from the node adjacent to node λ [the node on
the other side of surface v(λ)]. Each of the terms in this sum is an integral over the
surface σλ,v(λ) (formed by the points rλ,v(λ) and the solid angle 4π). The final term in
the sum is an integral over the exterior surface Sλ of node λ (formed by the points
rex). This term is included to allow trial functions that do not satisfy vacuum
boundary conditions. In the functional F, n refers to the outward unit normal
vector from node λ across an interior or exterior surface, and H is the Heaviside
step function. In addition, Σt(r), ΣS(r, Ω´ →Ω), and vΣf(r) are the usual cross
sections for removal, scattering from angle Ω´ to Ω, and neutron production from
fission, respectively. Although the functional F has been presented in a oneenergy
-group (or energy-independent) form, the extension of the results below to
the multigroup case is straightforward.
The condition (δF/δψ∗)δψ∗= 0 requires that the stationary value of the trial
function ψ(r, Ω) be identified as the forward angular flux satisfying the Boltzmann
transport equation,
Ω ⋅∇ψ(r; Ω) + Σt(r)ψ(r; Ω)
= ∫∫4π
dΩ´ΣS(r; Ω´ ! Ω)ψ(r; Ω´) + 1
4π ∫∫4π
dΩ´vΣf (r)ψ(r; Ω´)
(15.118)

<!-- page 597 (PDF 615) -->
as well as the interface continuity and vacuum boundary conditions, respectively:
ψ(rλ;v(λ); Ω) □ ψ(rv(λ);λ; Ω) = 0
(15.119)
and
ψ(rex; Ω) = 0;
Ω⋅n < 0
(15.120)
The condition (δF/δψ)δψ = 0 requires that the stationary value of the trial
function ψ∗(r, Ω) be identified as the adjoint angular flux satisfying the adjoint
transport equation,
□Ω ⋅∇ψ∗(r; Ω) + Σt(r)ψ∗(r; Ω)
= ∫∫4π
dΩ´ΣS(r; Ω ! Ω´)ψ∗(r; Ω´) + 1
4π ∫∫4π
dΩ´vΣf (r)ψ∗(r; Ω´)
(15.121)
as well as the interface continuity and vacuum boundary conditions, respectively:
ψ∗(rλ;v(λ); Ω) □ ψ∗(rv(λ);λ; Ω) = 0
(15.122)
and
ψ∗(rex; Ω) = 0;
Ω ⋅n > 0
(15.123)
To apply the functional F to develop a nodal method, the reactor volume is first
partitioned into I × J × K regions, where I, J, and K are the number of partitions
along the x, y, and z coordinates, respectively, and I × J × K is equal to the Λ of the
overall sum in F. Node ijk is bounded by the surfaces xi, xi+1, yj, yj+1, zk, and zk+1 as
illustrated in Fig. 15.7. The nodal or volumetric domain function, designated
yj+1
(behind)
xi+1
(right)
zk(below)
z
x
y
zk+1
xi
yj
Fig. 15.7 Bounding surface notation.

<!-- page 598 (PDF 616) -->
Δijk(x, y, z), is defined as
Δijk(x; y; z) =
1;
xi < x < xi+1;yj < y < yj; zk < z < zk+1
0;
otherwise
(
(15.124)
The I × J regions in the radial (x□y) plane are called channels. The angular flux
ψ(x, y, z, Ω) is represented in each channel ij as the product of a one-dimensional
axial function gijk(z, Ω) and a precomputed two-dimensional planar function fijk(x,
y, Ω) that is used over the axial domain k.
The angular dependence of the axial functions gijk(z, Ω) is discretized into eight
functions gn
ijk(z), one for each octant of the unit sphere, and the octant domain
function is designated Δn(Ω), defined as
Δn(Ω) =
1;
Ω within octantn
0;
otherwise
(
(15.125)
The angular geometry is illustrated in Fig. 15.8 with a hypothetical arrangement
of the 10Δmn(Ω) in octant 1 (μ > 0, η > 0, and ξ > 0) for a scheme with M = 80
(corresponding to an S8 quadrature set). Note that the boundaries between
adjacent domains are arbitrary.
The surface area of that part of the unit sphere corresponding to region m
within octant n is designated wmn, defined as
wmn ≡ 1
4π ∫∫4π
dΩΔn(Ω)Δmn(Ω) = 1
4π ∫∫π=2
dΩΔmn(Ω)
(15.126)
η
μ
Δ21(Ω)
ˆ
Δ11(Ω)
ˆ
Δ31(Ω)
ˆ
Δ61(Ω)
ˆ
Δ10,1(Ω)
ˆ
Δ91(Ω)
ˆ
Δ81(Ω)
ˆ
Δ71(Ω)
ˆ
Δ41(Ω)
ˆ
Δ51(Ω)
ˆ
ξ
Fig. 15.8 Angular geometry notation for domain functions Δmn(Ω) in an S8 quadrature.

<!-- page 599 (PDF 617) -->
where Δmn is unity within region m in octant n and otherwise zero. Thus, the wmn
have the same interpretation as standard discrete ordinates weights, and
P8
n=1
PM=8
m=1 wmn = 1. Note that the notation mn is shortened for “m within n”
and that this notation scheme requires that the M/8 subregions of octant n be
ordered symmetrically with respect to those of each of the other octants, thus
effectively specifying the use of a standard level-symmetric quadrature set. This
requirement may be eliminated with a suitable, though possibly more confusing
change of notation and is in no way limiting.
As indicated in Fig. 15.9, the angle Ω is decomposed into its three direction
cosines as follows (i, j, and k are the unit vectors along the x, y, and z axes,
respectively):
μ = Ω ⋅i;
η = Ω ⋅j;
ξ = Ω ⋅k
(15.127)
In addition, the azimuthal angle ω is defined (see Fig. 15.9) to be the angle between
the z-axis and the projection of Ω onto the y□z plane; thus,
η =
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
sinω
ξ =
ffiffiffiffiffiffiffiffiffiffiffiffi
1 □ μ2
p
cosω
(15.128)
μ
ξ
ω
Ωˆ
ˆ
η
x
y
z
j
ˆi
ˆk
Fig. 15.9 Definition of angles.

<!-- page 600 (PDF 618) -->
Consistent averages of the Ω direction cosines may be defined as follows:
μmn ≡
4πwmn ∫∫octantn
dΩΔmn(Ω)μ
ηmn ≡
4πwmn ∫∫octantn
dΩΔmn(Ω)η
ξmn ≡
4πwmn ∫∫octantn
dΩΔmn(Ω)ξ
(15.129)
Using the domain functions defined in Eqs. (15.124) and (15.125), the trial
function used for the forward angular flux in the functional F is
ψ(x; y; z; Ω) ≈ g(z; Ω)f (x; y; Ω)
=
X
I□J□K
i;j;k=1
Δijk(x; y; z)[gijk(z; Ω)f ijk(x; y; Ω)]
=
X
I□J□K
i;j;k=1
Δijk(x; y; z)
X
n=1
Δn(Ω)gn
ijk(z)
X
M=8
m=1
Δmn(Ω)f mn
ijk (x; y)
(15.130)
The adjoint angular flux ψ∗(x, y, z, Ω) is expanded analogously.
Using the trial function of Eq. (15.130) and the analogous expansion for the
adjoint flux in F and requiring stationarity of the functional with respect to each of
the adjoint axial functions g∗n
ijk(z) yields reduced equations for the forward axial
functions gn
ijk(z), with homogenized parameters defined in terms of the precomputed
nodal basis functions f mn
ijk (x; y) and f ∗mn
ijk (x; y). The equation for each of the
eight axial functions gn
ijk(z) is
ξ
n
ijk
dgn
ijk(z)
dz
+ B
n
ijkgn
ijk(z) + Σijk(z)gn
ijk(z)
=
X
n´=1
vΣ
nn´
f ;ijk(z)gn´
ijk(z) +
X
n´=1
Σ
nn´
s;ijk(z)gn´
ijk(z)
□ (1 □ δi1)H(μn)[μn
ijk(xi)gn
ijk(z) □ μn
(i;i□1)jk(xi)gn
(i□1)jk(z)]
+ (1 □ δi1)H(□μn)[μn
ijk(xi+1)gn
ijk(z) □ μn
(i;i+1)jk(xi+1)gn
(i+1)jk(z)]
□ δi1H(μn)μn
1jk(xi)gn
1jk(z) + δiIH(□μn)μn
Ijk(xI+1)gn
Ijk(z)
□ (1 □ δj1)H(ηn)[ηn
ijk(yj)gn
ijk(z) □ ηn
i(j;j+1)k(yj)gn
i(j+1)k(z)]
+ (1 □ δjJ)H(□ηn)[ηn
ijk(yj+1)gn
ijk(z) □ ηn
i(j;j+1)k(yj+1)gn
i(j+1)k(z)]
□ δj1H(ηn)ηn
i1k(yi)gn
i1k(z) + δjJH(□ηn)ηn
iJk(yJ+1)gn
iJk(z)
(15.131)

<!-- page 601 (PDF 619) -->
In Eq. (15.131), the homogenized total, fission, and scattering cross sections in
channel ij and axial region k for octant n are defined consistently as
Σ
n
ijk(z) =
∫
xi+1
xi
dx∫
yj+1
yj
dyΣ(x; y; z) PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.132)
Σ
nn´
f ;ijk(z)
=
∫
xi+1
xi
dx∫
yj+1
yj
dyΣf (x; y; z)[PM=8
m=1 wmnf ∗mn
ijk (x; y)][PM=8
m´=1 wm´n´f m´n´
ijk (x; y)]
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.133)
and
Σ
mn´
s;ijk(z) =
∫
xi+1
xi
dx∫
yj+1
yj
dy
X
L
l=0
(2l + 1)Σl
s(x; y; z)
□
X
M=8
m=1
wmnPl(μmn)f ∗mn
ijk (x; y)
"
(
□
X
M=8
m´=1
wm´n´Pl(μm´n´)f m´n´
ijk (x; y)
"
+ 2
X
l
k=1
(l □ k)!
(l + k)!
X
M=8
m=1
wmnPk
l (μmn)cos(kωmn)f ∗mn
ijk (x; y)
"
□
X
M=8
m´=1
wm´n´Pk
l (μm´n´)cos(kωm´n´)f m´n´
ijk (x; y)
"
+ 2
X
l
k=1
(l □ k)!
(l + k)!
X
M=8
m=1
wmnPk
l (μmn)sin(kωmn)f ∗mn
ijk (x; y)
"
□
X
M=8
m´=1
wm´n´Pk
l (μm´n´)sin(kωm´n´)f m´n´
ijk (x; y)
"
#)!
∫
xi+1
xi
dx∫
yj+1
yj
dy
X
M=8
m=1
wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.134)
respectively. Note that in deriving Eq. (15.134), the scattering cross section Σs(r,
Ω´ →Ω) has been expanded in a Legendre polynomial of order L, and the addition

<!-- page 602 (PDF 620) -->
theorem for spherical harmonics has been applied in the usual way. The isotropic
portion of the homogenized scattering cross section has the same form as that of
the fission cross section above.
The transverse leakage from node ijk (i.e., the leakage in the x- and y-directions)
is defined consistently as
B
n
ijk =
∫
xi+1
xi
dx∫
yj+1
yj
dy
X
M=8
m=1
wmnμmnf ∗mn
ijk (x; y)
@f mn
ijk (x; y)
@x
"
+∫
xi+1
xi
dx∫
yj+1
yj
dy
X
M=8
m=1
wmnηmnf ∗mn
ijk (x; y)
@f mn
ijk (x; y)
@y
#,
∫
xi+1
xi
dx∫
yj+1
yj
dy
X
M=8
m=1
wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.135)
The homogenized discrete ordinate for octant n is defined consistently as
ξ
n
ijk =
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnξmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.136)
The four parameters required (for each octant) for coupling node ijk to its
x-direction neighbors, nodes (i □ 1)jk and (i + 1)jk, are
μn
ijk(xi) =
∫
yj+1
yj
dy PM=8
m=1 wmnμmnf ∗mn
ijk (xi; y)f mn
ijk (xi; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
μn
(i;i□1)jk(xi) =
∫
yj+1
yj
dy PM=8
m=1 wmnμmnf ∗mn
ijk (xi; y)f mn
(i□1)jk(xi; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
μn
ijk(xi+1) =
∫
yj+1
yj
dy PM=8
m=1 wmnμmnf ∗mn
ijk (xi+1; y)f mn
ijk (xi+1; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
μn
(i;i□1)jk(xi+1) =
∫
yj+1
yj
dy PM=8
m=1 wmnμmnf ∗mn
ijk (xi+1; y)f mn
(i+1)jk(xi+1; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.137)

<!-- page 603 (PDF 621) -->
The four parameters required (for each octant) for coupling node ijk to its
y-direction neighbors, nodes i(j □ 1)k and i(j + 1)k, are
ηn
ijk(yj) = ∫
xi+1
xi
dy PM=8
m=1 wmnηmnf ∗mn
ijk (x; yj)f mn
ijk (xi; yj)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
ηn
i(j;j□1)k(yj) = ∫
xi+1
xi
dx PM=8
m=1 wmnηmnf ∗mn
ijk (x; yj)f mn
i(j□1)k(x; yj)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
ηn
ijk(yj+1) = ∫
xi+1
xi
dx PM=8
m=1 wmnηmnf ∗mn
ijk (x; yj+1)f mn
ijk (x; yj+1)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
ηn
i(j;j+1)k(yi+1) = ∫
xi+1
xi
dx PM=8
m=1 wmnηmnf ∗mn
ijk (x; yj+1)f mn
i(j+1)k(x; yj+1)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.138)
Note that the arguments of the Heaviside step functions H in Eq. (15.131) are the
direction cosines μmn and ημv of Eq. (15.129), but with the single superscript n
because only the octant needs to be identified.
The interface conditions that couple node ijk to its axially adjacent neighbors,
nodes ij(k □ 1) and ij(k + 1), are
ξ
n
ijkgn
ijk(zk) = ξ
n
ij(k;k□1)gn
ij(k□1)(zk);
ξ
n
ijk > 0
ξ
n
ijkgn
ijk(zk+1) = ξ
n
ij(k;k+1)gn
ij(k+1)(zk+1);
ξ
n
ijk < 0
(15.139)
where the coupling parameters are defined as
ξ
n
ij(k;k□1) =
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnξmnf ∗mn
ijk (x; y)f mn
ij(k□1)(x; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
ξ
n
ij(k;k+1) =
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnξmnf ∗mn
ijk (x; y)f mn
ij(k+1)(x; y)
∫
xi+1
xi
dx∫
yj+1
yj
dy PM=8
m=1 wmnf ∗mn
ijk (x; y)f mn
ijk (x; y)
(15.140)

<!-- page 604 (PDF 622) -->
Finally, the boundary conditions on Eqs. (15.131) are
gn
ij1(Z1) = 0;
ξ
n
ij1 > 0
gn
ijK(ZK+1) = 0;
ξ
n
ijK < 0
(15.141)
Using the angular flux trial function of Eq. (15.130) in the usual definition of the
isotropic flux specifies the heterogeneous flux reconstruction equation:
ϕ(x; y; z) ≡ ∫∫4π
dΩψ(x; y; x; Ω)
≈ ∫∫4π
dΩ
X
n=1
Δn(Ω)gn
ijk(z)
X
M=8
m=1
Δmn(Ω)f mn
ijk (x; y)
=
X
n=1
gn
ijk(z)
X
M=8
m=1
f mn
ijk (x; y)∫∫4π
dΩΔn(Ω)Δmn(Ω)
= 4π
X
m=1
gn
ijk(z)
X
M=8
m=1
wmnf mn
ijk (x; y)
(15.142)

### Application of the Method

The stepsrequiredforapplicationofthe variationalnodaldiscreteordinatesmethod
are the same as those required for standard nodal methods. First, a set of fine-mesh
high-order two-dimensional calculations is performed for small heterogeneous
local regions in the x□y plane, such as assemblies or extended assemblies, for the
purposes of homogenizing the nodes. (It is also possible to use full two-dimensional
planar calculations to provide nodal trial functions.) In standard nodal methods,
even for full three-dimensional global calculations, only two-dimensional local
calculations are performed, but the manner of axial coupling required for the nodes
is rarely specified. In the variational nodal discrete ordinates method, the local
calculations are performed using the discrete ordinates (SN) method. The fine-mesh
SN calculations yield the angular fluxes f mn
ijk (x; y), and M = N(N + 2) for a threedimensional
problem. For this method it is also necessary to calculate the adjoint
angular SN fluxes f ∗mn
ijk (x; y) in each node. There is a different homogenized cross
section defined for each of the eight S2 directions; however, because of the axial
symmetry obtained by the use of two-dimensional basis functions, only four are
required. The basis functions f mn
ijk (x; y) and f ∗mn
ijk (x; y) are used with standard SN
ordinates and weights to compute homogenized parameters in accordance with the
definitions of Eqs. (15.132)–(15.138) and (15.140).
The second step in standard nodal methodology is a global diffusion theory
calculation, which involves (in general, for the transverse integrated methods) three
one-dimensional equations for the transverse integrated x-, y-, and z-direction
fluxes. Usually, the problem is reduced to that of finding coefficients of fourth-order
polynomials. In the variational nodal method, the global equations are onedimensional
(z-direction) S2 first-order differential equations, which are equivalent
in accuracy to the diffusion equations. The spatial discretization to use on the z-axis

<!-- page 605 (PDF 623) -->
is not specified; thus any method may be used, including coarse-mesh, finitedifference
, high-order polynomial expansion, or other standard method.
The final step in the nodal calculation for the standard and variational nodal
methods is the reconstruction of heterogeneous fluxes or reaction rates from the
homogeneous (global) calculation results. In the variational nodal method, the
flux reconstruction is completely specified by Eq. (15.142).

## 15.8 Variational Principle for Multigroup Diffusion Theory

A complete mathematical description of the neutron distribution, within the
context of multigroup diffusion theory, is provided by a coupled set of partial
differential equations for the direct and adjoint flux (and current) with associated
boundary, initial, final, and continuity conditions. An equivalent variational formulation
must not only have the original equations as Euler equations, but must
also embody the associated boundary, initial, final, and continuity conditions, either
directly or indirectly through limitations on the admissible class of trial functions.
The following variational principle embodies all these conditions:
J =
"
∫
tf
t0
dt∫V
dr
ϕ∗T[Σ □ (1 □ β)χFT]ϕ + ϕ∗T∇⋅j + ϕ∗Tτ _ϕ

□ ϕ∗TX
M
m=1
λmχ mCm □ j∗T⋅3Σtrj □ j∗T⋅∇ϕ
□
X
M
m=1
C∗
mβmFTϕ +
X
M
m=1
C∗
mλmCm
+
X
M
m=1
C∗
m _Cm □ ϕ∗TS + S∗Tϕ
)#
+ ∫
tf
t0
dt∫Sin
dsn⋅f(γϕ∗T
+ + (1 □ γ)ϕ∗T
□ )(j+ □ j□)

□(ηj∗T
+ + (1 □ η)j∗T
□ )(ϕ+ □ ϕ□)g

+ ∫V
dr
aϕ∗T(+) + (1 □ a)ϕ∗T(□))τ(ϕ(+) □ ϕ
(
"
(□)

+
X
M
m=1
(bC∗
m(+) + (1 □ b)C∗
m(□))(Cm(+) □ Cm(□))
)#
+ ∫V
dr
ϕ∗T(t0)τ(ϕ(t0) □ g0) □ g∗T
f τϕ(tf )
(
"
+
X
M
m=1
(C∗
m(t0)(Cm(t0) □ hm0) □ h∗
mf Cm(tf )]
)#
+ ∫
tf
t0
dt∫s0
dsf(j∗T
s0 ? n)(ϕs0 + ℓjs0 ? ng

≡ J1 + J2 + J3 + J4 + J5
(15.143)

<!-- page 606 (PDF 624) -->
where
ϕ∗, ϕ
= G × 1 column matrices of group adjoint and direct flux, respectively
j∗, j
= G × 1 column matrices of group adjoint and direct current, respectively – vector
quantities
S∗, S
= G × 1 column matrices of group adjoint and direct source, respectively
C∗
m; Cm = scalar adjoint and direct delayed neutron precursor densities, respectively
Σ
= G × G matrix of group removal and scattering cross sections
Σtr
= G × G diagonal matrix of group transport cross section
τ
= G × G diagonal matrix of inverse group neutron speeds
F
= G × 1 column matrix of group nu-fission cross sections
χ, χ m
= G× 1 column matrices of prompt- and delayed-fission neutron spectra, respectively
λm, βm = delayed neutron precursor decay rate and precursor yield per fission, respectively
The term in the first set of brackets is an integral over the time of interest,
t0 ≤ t ≤ tf, and the volume of the reactor. The Euler equations for this term are the
direct and adjoint flux, current, and precursor equations, which result from the
requirement that the first variations of J1 with respect to each of the argument
functions (ϕ∗, ϕ, j∗, j, C∗
m, Cm) vanishes. In taking the first variation of J1,
integration by parts is required, which introduces certain additional terms.
The requirement that these additional terms vanish, and hence that stationarity
of J1 implies satisfaction of the Euler equations, imposes restrictions on the
admissible class of trial functions. The purpose of the additional terms, J2 □ J5, is to
remove these restrictions.
If direct and adjoint flux and current trial functions that are discontinuous
across an internal interface, Sin, are admitted, a term of the general form of J2 must
be added to J1 in order that stationarity of the functional J12 J1 + J2 implies
satisfaction of the Euler equations and flux and current continuity conditions.
The subscripts indicate limiting values on the + and □ sides, with respect to the
unit normal vector n, of the surface Sin. γ and η are arbitrary constants.
Terms of the general form of J2 have given rise to an overdetermination of interface
conditions in synthesis applications. Consider, for example, the variation of J12 with
respect to ϕ∗(by a variation with respect to the column vector we intend separate and
independent variations with respect to each element of the column matrix):
δJ 12
δϕ∗T δϕ∗T = 0 =
∫
tf
t0
dt∫V
drδϕ∗T
[Σ □ (1 □ β)χFT]ϕ + ∇⋅j + τ _ϕ

"
□
X
M
m=1
λmχ mCm □ S
)#
+ ∫
tf
t0
dt∫Sin
dsn⋅
(h
γδϕ∗T
+ + (1 □ γ)δϕ∗T
□
i
"
□ (j + □j□)
)#
(15.144)

<!-- page 607 (PDF 625) -->
For completely arbitrary δϕ∗T, the first term vanishes only if the expression within
the first set of braces is identically zero, which is just the condition that the neutron
balance equation is satisfied. Vanishing of the second term for arbitrary δϕ∗T
+ and
δϕ∗T
□ appears to lead to two current continuity conditions. However, continuity of
adjoint flux requires that δϕ∗T
+ = δϕ∗T
□ , and in fact there is only one current
continuity condition. The difficulty in synthesis applications results from the failure
to impose the condition δϕ∗T
+ = δϕ∗T
□ on trial functions that are partially specified.
If direct and adjoint flux and precursor trial functions that are discontinuous in
time at tin are admitted, a term of the general form of J3 must be added to J1 in
order that stationarity of the functional J13 = J1 + J3 implies the satisfaction of the
Euler equations and flux and precursor time continuity conditions. The + and □
arguments refer to times just after and just before, respectively, tin. a and b are
arbitrary constants. An overdetermination problem, analogous to that discussed
for J2, has also arisen in synthesis applications of J3.
If direct flux and precursor trial functions that do not satisfy the known initial
conditions g0 and hm0, and adjoint flux and precursor trial functions that do not
satisfy known final conditions g∗
f and h∗
mf , are admitted, J4 must be added to J1 in
order that stationarity of the resulting variational principle implies satisfaction of
the Euler equations and the appropriate initial and final conditions. Similarly,
stationarity of J15 = J1 + J5 implies satisfaction of the Euler equations and the
external boundary conditions ϕs0 + ℓjs0 ? n = 0; ϕ∗
s0 + ℓj∗
s0 ? n = 0, even if the flux
and current trial functions do not satisfy these boundary conditions identically.
A general second-order variational principle for multigroup diffusion theory
can also be written that admits the same extended class of trial functions as J of
Eq. (15.143), and that leads to the same apparent interface overdetermination
problem in synthesis applications. Using Fick’s law to relate flux and current, and
integrating by parts in Eq. (15.143), leads to
F =
∫
tf
t0
dt∫V
dr
ϕ∗T[Σ □ (1 □ β)χFT]ϕ + ∇ϕ∗T⋅D∇ϕ + ϕ∗Tτϕ

□ ϕ∗TX
M
m=1
λmχ mCm □
X
M
m=1
C∗
mβmFTϕ
+
X
M
m=1
C∗
mλmCm +
X
M
m=1
C∗
m _C □ ϕ∗TS + S∗Tϕ
)#
+ ∫
tf
t0
dt∫Sin
dsn⋅f(ϕ∗T
+ □ ϕ∗T
□ )((1 □ γ)D+∇ϕ+ + γD□∇ϕ□)

+ (η∇ϕ∗T
+ D+ + (1 □ η)∇ϕ∗T
□ D□)(ϕ+ □ ϕ□)g

+ ∫V
dr
(aϕ∗T(+) + (1 □ a)ϕ∗T(□))τ(ϕ(+) □ ϕ(□))
(
"
+
X
M
m=1
(bC∗
m(+) + (1 □ b)C∗
m(□))(Cm(+) □ Cm(□))
)#

<!-- page 608 (PDF 626) -->
+ ∫V
dr
ϕ∗T(t0)τ(ϕ(t0) □ g0) □ g∗T
f τϕ(tf )
(
"
+
X
M
m=1
[C∗
m(t0)(Cm(t0) □ hm0) □ h∗
mf Cm(tf )]
)#
+ □∫
tf
t0
dt∫s0
dsfn ⋅∇ϕ∗T
s0 D(ϕs0 □ ℓD∇ϕs0⋅n) □ ϕ∗T
s0 D∇ϕs0⋅ng

≡
F1 + F2 + F3 + F4 + F5
(15.145)
The diffusion coefficient matrix, D = 1
3Σ□1
tr , has been introduced in Eq. (15.145).

## 15.9 Single-Channel Spatial Synthesis

The basic idea of single-channel synthesis is illustrated by the example of a
uniform reactor with a rod (or bank of rods) partially inserted, as illustrated in
Fig. 15.10. A few diffusion lengths above and below the rod tip, the flux solution is
essentially a one-dimensional radial flux shape ϕrod and ϕunrod, respectively. In the
ϕ Rod
ϕ unrod
ϕ (r,z) = arod (z)ϕrod(r) + aunrod (z)ϕunrod(r)
Control Rod
a
a
Fig. 15.10 Single-channel synthesis example.

<!-- page 609 (PDF 627) -->
vicinity of the rod tip, it is plausible that some mixture of the two flux shapes will
describe the actual radial flux distribution. The synthesis approximation is
developed by using trial functions of the form
ϕ(x; y; z; t) =
X
N
n=1
ψn(x; y)ρn(z; t)
(15.146)
j(x; y; z; t) =
X
N
n=1
J nx(x; y)bn(z; t)i + Jny(x; y)gn(z; t)j
+ J nz(x; y)dn(z; t)k
(15.147)
with similar expansions for the adjoint flux and current. ψn and the Jn are G × G
diagonal matrices with elements given by the known group expansion functions
ψg
n(x; y) and Jg
n(x; y), while ρn, bn, gn, and dn are G × 1 column matrices with
elements given by the corresponding unknown group expansion coefficients.
(Direct and adjoint expansion functions must each be linearly independent, but
similar functions may be used for direct and adjoint expansion functions.)
Precursor trial functions of the form
Cm(x; y; z; t) = βm
λm
FT(x; y; z; t)
X
N
n=1
ψn(x; y)πCm;n(z; t)
(15.148)
C∗
m(x; y; z; t) = χ T
m
X
N
n=1
ψ∗
n(x; y)πC∗
m;n(z; t)
(15.149)
are used, where π is a G × 1 column matrix with unit elements (i.e., a sum vector).
When the variational principle J of Eq. (15.143) is required to be stationary with
respect to arbitrary variations in the trial functions, which are limited to variations
in the expansion coefficients because the expansion functions are fixed, equations
that must be satisfied by the expansion coefficients are obtained.
If the trial functions above are used throughout the reactor and at all times,
then J2 and J3 are identically zero. In this case, equations valid for 0 < z < L and
t > t0 are obtained from J1 and that part of J5 contributed by the vertical (side)
external surface.
δJ
δρ∗T
n´
= 0;
n´ = 1; . . . ; N
δJ
δb∗T
n´
= 0;
n´ = 1; . . . ; N
δJ
δg∗T
n´
= 0;
n´ = 1; . . . ; N
δJ
δd∗T
n´
= 0;
n´ = 1; . . . ; N
δJ
δC∗
m;n´
= 0;
m = 1; . . . ; M;
n´ = 1; . . . ; N
(15.150)

<!-- page 610 (PDF 628) -->
Equations (15.150) can be combined to eliminate bn, gn, and dn, leaving NG
scalar equations, which can be written in matrix form as
M + R □ @
@z A @
@z

ρ + T _ρ =
X
M
m=1
βmFmCm + S
(15.151)
where A, M, and R are NG × NG matrices, and Fm is an NG × N matrix. R and A
are radial and axial leakage matrices resulting from the elimination of bn, gn, and
dn. ρ and S are NG × 1 column matrices and Cm is an N × 1 column matrix. Thus,
G three-dimensional time-dependent second-order PDEs (the multigroup diffusion
equations) are replaced by NG one-dimensional, time-dependent secondorder
PDEs [Eq. (15.151)]. The M three-dimensional first-order ODEs (precursor
equations) are replaced by NM one-dimensional first-order ODEs [last of
Eqs. (15.150)].
Boundary conditions at the top (z = L) and bottom (z = 0) of the model are
obtained by requiring stationarity of J with respect to arbitrary variations δd∗T
n on
the top and bottom surfaces:
δJ
δd∗T
n´ (z = 0; L) = 0;
n´ = 1; . . . ; N
(15.152)
Initial conditions are derived by requiring stationarity of J with respect to
arbitrary variations δρ∗T
N and δC∗
m;n at t = t0:
δJ
δρ∗T
n´ (t0) = 0;
n´ = 1; . . . ; N
(15.153)
δJ
δC∗T
m;n´(t0) = 0;
m = 1; . . . ; M;
n´ = 1; . . . ; N
(15.154)
A formally identical result could be obtained by deriving the synthesis equations
from the second-order variational principle F, the only difference arising in the
definition of the elements of the leakage matrices R and A in Eq. (15.151). Under
certain restrictive conditions the two formulations are exactly identical.
Two-dimensional static flux solutions for x □ y slices through the reactor at
various axial locations and/or for various conditions are normally chosen as
expansion functions. For some problems different sets of expansion functions are
appropriate for different axial regions, and it is convenient to use a discontinuous
trial function formulation. In this case a term of the form of J2 would be included
in the variational principle for each x □ y planar surface at which the set of
expansion functions changed. Equation (15.151) would again obtain within each
axial zone, with the coefficients defined in terms of the expansion functions
appropriate to that zone. Interface conditions result from the requirement that

<!-- page 611 (PDF 629) -->
the variational principle be stationary with respect to arbitrary variations δj∗T□n
and δϕ∗T on the interface, which results in
∫
tf
t0
dt∫Sin
dx dy n ⋅k
X
zn
n´=1
(ηδd∗T
n´+J ∗T
n´z+ + (1 □ η)δd∗T
n□J ∗T
nz□)
(
□
X
N
n=1
(ψn+ρn+ □ ψn□ρn□)
)
= 0
(15.155)
∫
tf
t0
dt∫Sin
dx dy n ⋅k
X
N
n´=1
(γδρ∗T
n´+ψ∗T
n´+ + (1 □ γ)δρ∗T
n□ψ∗T
n□)
(
□
X
N
n=1
(Jnz+dn+ □ Jnz□dn□)
)
= 0
(15.156)
If every δρ∗T
n´+ and δρ∗T
n´□ is assumed independent, 2N equations relating the Ndn
are obtained, and similarly the assumption that every δρ∗T
n´+ and δρ∗T
n´□ is independent
leads to 2 N equations relating the Nρn. Hence the system is overdetermined
by a factor of 2. Several stratagems have evolved for avoiding this difficulty.
By requiring that the flux (direct and adjoint) and current (direct and adjoint)
trial functions not be discontinuous at the same interface, the overdetermination
problem disappears. In this case J∗T
nz+ ≡ J ∗T
nz□ and δd∗T
n+ ≡ δd∗T
n□ and so on. This
technique of staggering the interfaces at which flux and current expansion
functions are changed, which has been widely employed, has the disadvantage
that Sin frequently corresponds to a physical interface in the reactor and it is
desirable to change current and flux expansion functions at the same point. This
may be accomplished, for all practical purposes, by allowing the two interfaces at
which the current and flux trial functions are discontinuous to approach each
other arbitrarily closely. A second strategy is to select γ and η = 0, 1. This is
essentially what is done when a Lagrange multiplier principle is used in deriving
the synthesis equations and the Lagrange multipliers are expanded in terms of the
flux or current expansion functions on either the + or □ side of the interface. Such
interface conditions are not symmetric with respect to the arbitrary choice of the
+ and □ sides of the interface. A third strategy consists of requiring that δρ∗T
n+ =
δd∗T
n□ and δd∗T
n+ = δd∗T
n□. With γ = η = 1
2, the interface conditions are independent
of the arbitrary choice of the + and □ sides of the interface. Thus, all of these
stratagems for removing the overdetermination of interface conditions have
certain unsatisfactory features.
As mentioned in Section 15.8, overdetermined interface conditions result
because of failure to impose the restrictions δϕ∗
+ = δϕ∗
□ and δj∗
+ = δj∗
□, which
must be satisfied if the adjoint flux and current are continuous, upon the trial
functions. Although these restrictions cannot be imposed exactly, because the
trial functions are partly specified, they can be imposed in an approximate manner
to obtain relations among the variations δρ∗T
n+ and δρ∗T
n□ among δd∗T
n+ and δd∗T
n+.

<!-- page 612 (PDF 630) -->
The requirement δϕ∗
+ = δϕ∗
□ becomes
X
N
n=1
ψ∗
n+δρ∗
n+ =
X
N
n=1
ψ∗
n□δρ∗
n□
which cannot, in general, be satisfied exactly. However, this relation can be
satisfied approximately. Multiplying by an arbitrary diagonal G × G matrix
ωn´(x; y) and integrating over the surface Sin yields one condition relating the
Nδρ∗
n□ to the Nδρ∗
n+
X
N
n=1
∫Sin
dxdyωn´ψ∗
n+

δρ∗
n+ =
X
N
n=1
∫Sin
dxdyωn´ψ∗
n□

δp∗
n□
If this is repeated for N different matrix functions ωn´, the resulting set of
equations may be written as
A+δρ∗
+ = A□δρ∗
□
where A+ is an NG × NG matrix and δρ+ is an NG × 1 column matrix. This
equation may be solved:
δρ∗
+ = (A+)□1A□δρ∗
□ ≡ Qδρ∗
□
The NG × NG matrix Q may be partitioned into N2 diagonal G × G matrices Qn´;n
in terms of which the equation above may be written as
δρ∗
n+ =
X
N
n´=1
Qnn´δρn´□;
n = 1; . . . ; N
(15.157)
δd∗
n+ =
X
N
n´=1
Pnn´δd∗
n´□;
n = 1; . . . ; N
(15.158)
where Pnn´ is one of the N2 diagonal G × G matrices analogous to the Qnn´.
Making use of Eqs. (15.157) and (15.158), Eqs. (15.155) and (15.156) each yield
N interface conditions. These interface conditions have several advantages
relative to those described previously. The theoretical derivation is consistent
and the problem of overdetermination never arises. Flux and current trial
function discontinuities are allowed at the same interface. Unfortunately, these
interface conditions are not, in general, symmetric with respect to the arbitrary
choice of the + and □ directions.
When the physical configuration of the reactor changes significantly during a
transient, it may be plausible to use different sets of expansion functions over

<!-- page 613 (PDF 631) -->
different intervals of time. For this situation a term of the form J3 would be
included in the variational principle for each time interface at which the set of
expansion functions are changed. Requiring stationarity of the variational principle
again results in Eqs. (15.150) and (15.151) within each time interval, with the
coefficients defined in terms of the expansion functions appropriate to the time
interval. Similarly, the boundary conditions of Eq. (15.152) and the spatial
interface conditions of Eqs. (15.155) and (15.156), with the coefficients defined
in terms of the expansion functions appropriate to the time interval, and the initial
conditions of Eqs. (15.153) and (15.154) are obtained again. In addition, temporal
interface conditions arise from the J3 term, the variation of which is
X
N
n´=1
∫V
dr[aδρ∗T
n´ (+)ψ∗T
n´ (+) + (1 □ a)δρ∗T
n´ (□)ψ∗T
n (□)]τ
(
□
X
N
n=1
[ψn(+)ρn(+) □ ψn(□)ρn(□)]
+ πTX
M
m=1∫V
dr[bδC∗
m;n´(+)ψ∗T
n´ (+) + (1 □ b)δC∗T
m;n´(□)ψ∗T
n´ (□)]
□ χ m
βm
λm
FTX
N
n=1
"
ψn(+)πCm;n(+) □ ψn(□)πCm;n(□)
#)
= 0
(15.159)
The same type of overdetermination, for the same reason [failure to impose the
restrictions δϕ∗(+) = δϕ∗(□) and δC∗
m(+) = δC∗
m(□)], has arisen in connection
with the temporal interface conditions. If each variation δρ∗
n´(+) and δρ∗
n´(□) is
(incorrectly) assumed to be independent, the 2N conditions are obtained relating
the Nρn(+) to the Nρn(□), and similarly for the δC∗
m;n(+) = δC∗
m;n(□). The
stratagems that have been used to remove this apparent overdetermination
parallel those employed for the spatial interface problem. Staggered discontinuities
in which the direct and adjoint flux (and precursor densities) are
discontinuous at alternative times have been suggested, and the inconvenience
of changing expansion functions at different times has been essentially eliminated
by allowing alternative times to approach each other arbitrarily closely. As in the
case of the spatial interface, the overdetermination never arises if the restrictions
δϕ∗(+) = δϕ∗(□) and δC∗
m(+) = δC∗
m(□) are imposed in an approximate manner.
Adjoint synthesis equations may be derived by an analogous development, in
this case by requiring stationarity of the functional with respect to the direct
expansion coefficients. Similar results are obtained except that final conditions,
rather than initial conditions, are obtained. It is necessary to impose approximately
the conditions δϕ+ = δϕ□, δj+ = δj□ to obtain restrictions on the variations
in the flux and current expansion coefficients at spatial interfaces, and to impose
approximately the conditions δϕ(+) = δϕ(□) and δCm(+) = δCm(□) at temporal
interfaces, to avoid an overdetermination difficulty.
