# 9 Neutron Transport Theory — 9.8 Discrete Ordinates Methods in One-Dimensional Slab Geometry … 9.11 Even-Parity Transport Formulation
<!-- source PDF pages 383-400 -->

<!-- page 362 (PDF 383) -->
Equation (9.187) and hence also the diffusion equation are thus based on two
major assumptions: (1) spatial derivatives of higher flux moments ϕ2 can be
neglected and (2) anisotropic neutron sources can be neglected. Had we carried
out the development from the time-dependent transport equation, it would have
also been necessary to assume that the time derivatives of the current could be
neglected to obtain a Fick’s law.

## 9.8 Discrete Ordinates Methods in One-Dimensional Slab Geometry

The discrete ordinate methods are based on a conceptually straightforward
evaluation of the transport equation at a few discrete angular directions, or
ordinates, and the use of quadrature relationships to replace scattering and fission
neutron source integrals over angle with summations over ordinates. The essence
of the methods are the choice of ordinates, quadrature weights, differencing
schemes, and iterative solution procedures. In one dimension, the ordinates can
be chosen such that the discrete ordinates methods are completely equivalent to
the PL and D-PL methods discussed in Section 9.6, and in fact the use of discrete
ordinates is probably the most effective way to solve the PL and D-PL equations in
one dimension. This equivalence does not carry over into multidimensional
geometries.
Making use of the spherical harmonics expansion of the differential scattering
cross section of Eq. (9.125) and the addition theorem for Legendre polynomials of
Eq. (9.121), the one-dimensional neutron transport Eq. (9.123) in slab geometry
becomes
μ dψ
dx (x; μ) + Σt(x)ψ(x; μ)
= P
l´=0
2l´ + 1
Σsl´(x)Pl´(μ)∫
□1
dμ´Pl´(μ´)ψ(x; μ´) + S(x; μ)
(9.189)
where the source term includes an external source and, in the case of a multiplying
medium such as a reactor core, a fission source. We first discuss the
solution of the fixed external source problem (which implicitly assumes a
subcritical reactor) and then return to the solution of the critical reactor problem,
in which the solution of the fixed source problem constitutes part of the iteration
strategy.
Defining N ordinate directions μn and corresponding quadrature weights wn,
the integral over the angle in Eq. (9.189) can be replaced by
ϕl(x) ≡ ∫
□1
dμ Pl(μ)ψ(x; μ) '
X
n
wnPl(μn)ψn(x)
(9.190)

<!-- page 363 (PDF 384) -->
where ψn ≡ ψ(μn). The quadrature weights are normalized by
X
N
n=1
wn = 2
(9.191)
It is convenient to choose ordinates and quadrature weights that are symmetric
about μ = 0, hence providing equal detail in the description of forward and
backward neutron fluxes. This can be accomplished by choosing
μN+1□n = □μn;
μn > 0;
n = 1; 2; . . . ; N=2
wN+1□n = wn;
wn > 0;
n = 1; 2; . . . ; N=2
(9.192)
With such even ordinates, reflective boundary conditions are simply prescribed
:
ψn = ψN+1□n;
n = 1; 2; . . . ; N=2
(9.193)
Known incident flux, ψin(μ), boundary conditions, including vacuum conditions
when ψin(μ) = 0, are
ψn = ψin(μn);
n = 1; 2; . . . ; N=2
(9.194)
Normally, an even number of ordinates is used (N = even), because this results
in the correct number of boundary conditions and avoids certain other problems
encountered with N = odd. Even with these restrictions, there remains considerable
freedom in the choice of ordinates and weights.

### PL and D-PL Ordinates

If the ordinates are chosen to be the N roots of the Legendre polynomial of
order N,
PN(μi) = 0
(9.195)
and the weights are chosen to integrate all Legendre polynomials correctly up
to PN□1
∫
□1
Pl(μ)dμ =
X
N
n=1
wnPl(μn) = 2δl0;
l = 0; 1; . . . ; N □ 1
(9.196)
then the discrete ordinates equations with N ordinates are entirely equivalent to
the PN□1 equations. To establish this, we multiply Eq. (9.189) by wnPl(μn) for

<!-- page 364 (PDF 385) -->
0 ≤ l ≤ N □ 1, in turn, and use the recursion relation of Eq. (9.119) to obtain
wn
l + 1
2l + 1 Pl+1(μn) +
l
2l + 1 Pl□1(μn)

 dψn
dx + wnΣtψn Pl μn
)
=
X
N□1
l´=0
2l´ + 1
Σsl´wnPl´(μn)Pl(μn)ϕl´ + wnPl(μn)S(μn);
l = 0; . . . ; N □ 1;
n = 1; . . . ; N
(9.197)
Summing these equations over 1 ≤ n ≤ N yields
l + 1
2l + 1
dϕl+1
dx
+
l
2l + 1
dϕl□1
dx
+ Σtϕl
=
X
N□1
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
l = 0; . . . ; N □ 1
(9.198)
Weights chosen to satisfy Eqs. (9.196) obviously correctly integrate all polynomials
through order N (any polynomial of order n can be written as a sum of
Legendre polynomials through order n), but fortuitously they also integrate
correctly all polynomials through order less than 2N. Thus, the term in the
scattering integral becomes
X
N
n=1
wnPl´(μn)Pl(μn) = ∫
□1
Pl´(μ)Pl(μ)dμ = 2δll´
2l + 1
(9.199)
and assuming that the angular dependence of the source term can be represented
by a polynomial of order <2N:
X
N
n=1
wnPl(μn)S(μn) = ∫
□1
Pl(μ)S(μ)dμ =
2Sl
2l + 1
(9.200)
where Sl is the Legendre moment of the source given by Eq. (9.127).
Using Eqs. (9.199) and (9.200), Eqs. (9.198) become
l + 1
2l + 1
dϕl+1
dx
+
l
2l + 1
dϕl□1
dx
+ (Σt □ Σsl)ϕl = Sl;
l = 0; . . . ; N □ 2
N □ 1
2(N □ 1) + 1
dϕ(N□1)□1
dx
+ (Σt □ Σs;N□1)ϕN□1 = SN□1; l = N □ 1
(9.201)
which, when ϕ□1 is set to zero, are identically the PL Eqs. (9.126) for L = N □ 1.
These PL ordinates and weights are given in Table 9.2.

<!-- page 365 (PDF 386) -->
The D-PL ordinates are the roots of the half-angle Legendre polynomials for
L = N/2 □ 1:
PN=2(2μn + 1) = 0;
n = 1; 2; . . . ; N
PN=2(2μn □ 1) = 0;
n = N
2 + 1; . . . ; N
(9.202)
Table 9.2 PN□1 Ordinates and Weights
±μn
wn
N = 2
0.57735
1.00000
N = 4
0.33998
0.65215
0.86114
0.34785
N = 6
0.23862
0.46791
0.66121
0.36076
0.93247
0.17132
N = 8
0.18343
0.36268
0.52553
0.31371
0.79667
0.22238
0.96029
0.10123
N = 10
0.14887
0.29552
0.43340
0.26927
0.67941
0.21909
0.86506
0.14945
0.97391
0.06667
N = 12
0.12523
0.24915
0.36783
0.23349
0.58732
0.20317
0.76990
0.16008
0.90412
0.10694
0.98156
0.04718
Source: Data from Ref. [1]; used with permission of Wiley.

<!-- page 366 (PDF 387) -->
and the corresponding weights are determined from
X
N=2
n=1
wnPl(2μn + 1) = δl0;
l = 0; . . . ; N □ 2
X
N
n=(N+2)=2
wnPl(2μn □ 1) = δl0; l = 0; . . . ; N □ 2
(9.203)
These ordinates and weights may be evaluated from the data in Table 9.2.
The PL ordinates and weights are preferable to the D-PL ordinates and weights
for deep penetration problems in heterogeneous media and for problems in which
anisotropic scattering is important, for both of which the correct calculation of a
large number of Legendre moments of the flux are required. Conversely, for the
calculation of highly anisotropic neutron fluxes near boundaries, the D-PL
ordinates and weights are preferable. With either set of ordinates and weights,
the discrete ordinates method in one dimension is essentially a numerical method
for solving the PL or D-PL equations. Other choices of weights and ordinates can
be made to specialize the discrete ordinates method to the problem to be solved
(e.g., bunching ordinates to emphasize an accurate calculation of the neutron flux
in a certain direction). However, care must be exercised when choosing ordinates
and weights that do not correctly integrate the low-order angular polynomials,
because surprising results sometimes turn up.

### Spatial Differencing and Iterative Solution

Defining cross sections to be constant over xi□1/2 < x < xi+1/2, Eq. (9.189), for
each ordinate, can be integrated over xi□1/2 < x < xi+1/2 to obtain
μn(ψi+1=2
n
□ ψi□1=2
n
) + Σi
tψi
nΔi
= ΔiQi
n ≡ Δi
X
L
l´=0
2l´ + 1
Σi
sl´Pl´(μn)ϕi
l´ + Si(μn)
"
(9.204)
where ψi
n ≡ ψ(xi; μn), and so on, and Δi = xi+1/2 □ xi□1/2. Using the diamond
difference relation
ψi
n = 1
2 (ψi+1=2
n
+ ψi□1=2
n
)
(9.205)
algorithms for sweeping to the right in the direction of neutrons traveling with
μn > 0,
ψi
n
=
1 + Σi
tΔi
2jμnj
□1
ψi□1=2
n
+ Δi Qi
n
2jμnj
ψi+1=2
n
= 2ψi
n □ ψi□1=2
n
(9.206)

<!-- page 367 (PDF 388) -->
and for sweeping to the left in the direction of neutrons traveling with μn < 0,
ψi
n
=
1 + Σi
tΔi
2jμnj
□1
ψi+1=2
n
+ ΔiQi
n
2jμnj
ψi□1=2
n
= 2ψi
n □ ψi+1=2
n
(9.207)
are specified.
The boundary conditions at the left boundary (for incident flux or vacuum
conditions) are specified for the positive-direction ordinates by Eqs. (9.194) (e.g.,
ψ1=2
n
= 0, μn > 0 for a vacuum condition). Note that the physical boundaries are
located at x1/2 and xI+1/2. Equations (9.206) are then used to sweep the solutions
for ordinates μn > 0 to the right boundary, where conditions similar to Eqs. (9.194)
specify the boundary conditions (e.g., ψI+1=2
n
= 0, μn < 0 for a vacuum condition)
for the ordinates with μn < 0, and Eqs. (9.207) are used to sweep the solutions for
μn < 0 from the right to the left boundary. If there were no scattering or fission
sources in Qi
n, the solution would be complete. However, there are, and this iterate
of the fluxes must be used to update the Qi
n and the double sweep repeated until
convergence. If there is a reflective boundary, say on the right, the condition
ψI+1=2
N+1□n = ψI+1=2
n
is used for the return sweep (the problem should be stated so
that the reflective boundary is on the right). If there are reflective conditions on
both boundaries, the boundary conditions on the left must be initially guessed,
then updated following a double sweep, and so on, which, of course, slows
convergence.

### Limitations on Spatial Mesh Size

Truncation error determines the allowable spatial mesh size. Consider
Eq. (9.189), for a given ordinate, but without the source term:
μn
dψn(x)
dx
+ Σt(x)ψn(x) = 0
(9.208)
The exact solution for the flux at xi+1/2 in terms of the flux at xi□1/2 is
ψi+1=2
n
= exp □Σi
tΔi
jμnj
ψi□1=2
n
(9.209)
The finite difference solution is found by using Eq. (9.205) to eliminate ψi
n in
Eq. (9.204) with Qi
n = 0:
ψi+1=2
n
= 1 □ Σi
tΔi=2jμnj
1 + Σi
tΔi=2jμnj ψi□1=2
n
(9.210)

<!-- page 368 (PDF 389) -->
The error in the approximate solution is O((Σi
tΔi=2jμnj)2). The allowable
mesh spacing is determined by the accuracy required and the smallest value
of |μn|.
Negative fluxes will occur if Δi > 2jμnj=Σi
t. Negative flux fix-up schemes have
been developed, which amount to setting negative fluxes to zero when they occur
in the iteration, but this introduces difficulties. This problem is sufficiently serious
to have motivated the development of a number of alternative difference schemes,
but variants of the diamond differencing scheme remain the most commonly
used.

## 9.9 Discrete Ordinates Methods in One-Dimensional Spherical Geometry

The angles that specify the neutron direction in curvilinear geometry change as
the neutron moves, as shown in Fig. 9.20. This leads to angular derivatives in the
neutron streaming operator, making curvilinear geometries qualitatively different
from slab geometry. The conservative form of the neutron transport equation in
spherical geometry is
μ
ρ2
@
@ρ ρ2ψ(ρ; μ)

+ 1
ρ
@
@μ (1 □ μ2)ψ(ρ; μ)

+ Σt(ρ)ψ(ρ; μ) = Q(ρ; μ)
(9.211)

### Representation of Angular Derivative

The difference scheme for the angular derivative is determined by the
requirement that the sum of the angular and radial streaming terms (the first
two terms in the equation above) satisfy the physical constraint of vanishing
for a uniform, isotropic flux in an infinite medium. Approximating the angular
ρ1
θ1 = cos-1 µ1
ρ2
θ2 = cos-1 µ2
Ω
Fig. 9.20 Change in angular coordinate μ = cos θ as the neutron moves. (With permission
from Ref. [1]. Copyright 1984, Wiley.)

<!-- page 369 (PDF 390) -->
derivative as
ρ
@
@μ (1 □ μ2)ψ(ρ; μ)

'
ρwn
(αn+1=2ψn+1=2 □ αn□1=2ψn□1=2)
(9.212)
and noting that for a uniform medium and an isotropic flux that ψn = ψn±1 = ϕn/2,
the scalar flux, the requirement that the spatial plus angular derivative terms
vanish is
αn+1=2 = αn□1=2 □ μnwn
(9.213)
which is an algorithm for determining the αn+1/2 once α1/2 is known. By choosing
α1/2 = 0 and N even, Eq. (9.213) yields αN+1/2 = 0, which leads to closure in the
angular differencing algorithm.
Using this form for the angular derivative and an angular diamond difference
relation
ψn = 1
2 (ψn+1=2 + ψn□1=2)
(9.214)
in Eq. (9.211) yields
μn
ρ2
@
@ρ (ρ2ψn) + 2
ρwn
2αn+1=2ψn □ (αn+1=2 + αn□1=2)ψn□1=2
h
i
+ Σtψn = Qn
(9.215)
The spatial differencing proceeds as for the slab case, but taking into account the
variation of differential area and volume with radius.

### Iterative Solution Procedure

The equations are solved by sweeping in the direction of neutron travel. With
reference to Fig. 9.21, for an S4 (N = 4) calculation, the calculation is started on the
outer surface of the sphere for the direction n = 1
2.
A known incident flux (including vacuum) boundary condition
ψI+1=2
n
= ψin(μn);
n = 1; . . . ; N=2
(9.216)
provides a starting value for ψI+1=2
1=2 . The calculation sweeps inward (decreasing i)
for n = 1/2 (μ = □1) using
ψi□1=2
n
= 2ψi
n □ ψi+1=2
n
(9.217)
ψi
1=2 =
2ψi+1=2
1=2
+ (ρi+1=2 □ ρi□1=2)Qi
1=2
2 + Σi
t(ρi+1=2 □ ρi□1=2)
;
μ < 0
(9.218)

<!-- page 370 (PDF 391) -->
Next, the ψi
1 row is calculated using the starting value from Eq. (9.216) and using
Eq. (9.217) and
ψi
n =
2jμnjAi□1=2 + 2
wn
(Ai+1=2 □ Ai□1=2)αn+1=2 + V iΣi
t

□1
□ jμnj(Ai+1=2 + Ai□1=2)ψi+1=2
n
+ 1
wn
(Ai+1=2 □ Ai□1=2)(αn+1=2 + αn□1=2)ψi
n□1=2 + V iQi
n

(9.219)
to sweep the solution inward. Then the ψi
3=2 are calculated from the angular
diamond difference relation
ψi
n+1=2 = 2ψi
n □ ψi
n□1=2
(9.220)
These inward sweeps are continued, using, alternatively, Eqs. (9.217) and (9.219)
for the ψi
n and Eqs. (9.220) for the ψi
n+1=2 until all the inward (μn < 0, n ≤ N/2)
fluxes are calculated.
The starting fluxes at the center of the sphere (l = 1/2) for the outward (μn > 0,
n > N/2) calculation are determined from the symmetry condition at the center of
the sphere:
ψ1=2
N+1□n = ψ1=2
n ;
n = 1; 2; . . . ; N=2
(9.221)
µ4 = µN
µ2 = µN/2
µ5/2 = 0
µ1/2 = -1
ρ1/2 = 0
ρi-1/2
ρi+1/2
ρi+1/2
µ7/2
µ3/2
µ3
µ1
ρ1
ρi
ρI
Fig. 9.21 Sweep of the space–angle mesh for one-dimensional spherical geometry. (With
permission from Ref. [1]. Copyright 1984, Wiley.)

<!-- page 371 (PDF 392) -->
Then the calculation is swept outward (increasing i) using for ψi
n
ψi+1=2
n
= 2ψi
n □ ψi□1=2
n
(9.222)
ψi
n =
2jμnjAi+1=2 + 2
wn
(Ai+1=2 □ Ai□1=2)αn+1=2 + V i Σi
t

□1
□ jμnj(Ai+1=2 + Ai□1=2)ψi□1=2
n
+ 1
wn
(Ai+1=2 □ Ai□1=2)(αn+1=2 + αn□1=2)ψi
n□1=2 + V iQi
n

(9.223)
and the angular diamond difference relation for ψi
n+1=2:
ψi
n+1=2 = 2ψi
n □ ψi
n□1=2
(9.224)
The A’s and V ’s in the equations above are the shell areas and differential
volume elements at the radii indicated:
Ai+1=2 = 4πρ2
i+1=2;
V i = 4π
3 (ρ3
i+1=2 □ ρ3
i□1=2)
(9.225)
From these directional fluxes the scalar flux is calculated and the scattering and
fission source terms in Q are updated for the next iteration.

### Acceleration of Convergence

The numerical solution for the fluxes ψi
n on each double sweep is exact for the
given scattering and fission source guess Q. The rate of convergence of
the solution depends on the rate of convergence of these sources. Note
from Eq. (9.204) that these sources depend only on the Legendre flux moments
defined by Eq. (9.190) as a weighted sum over the ordinates of the ψi
n. This
suggests that the iterative solution for the ψi
n can be accelerated by advancing
the solution for the ϕi
l in a low-order (e.g., diffusion theory) approximation at
intermittent steps during the iteration, which is the basis of the synthetic
method.
Another acceleration technique – coarse mesh rebalance – makes use of the
fact that the converged solution for the ψi
n must satisfy neutron balance.
Imposing this condition on the unconverged solution over coarse mesh regions
that include a number of spatial mesh points at intermittent steps in the
iteration provides a means for accelerating the solution. Both acceleration
methods, which are discussed in detail in Ref. [1], may become unstable if the
spatial mesh spacing is not sufficiently small. The synthetic method may even
become unstable with small mesh spacing. Other acceleration methods, such as
Chebychev acceleration, may also be applied to accelerate the discrete ordinates
solution.

<!-- page 372 (PDF 393) -->
### Calculation of Criticality

Up to this point, we have discussed solving the discreteordinatesequations for a fixed
external source. We now consider the critical reactor problem, in which there is no
external source. In this case, the equations above would be modified by the inclusion
of an effective multiplication constant, k□1, as an eigenvalue in the fission term. A
value k0 and an initial flux guess ψ(0) would be used to evaluate the fission S(0)
f
and
scattering S(0)
s
sources, and the solution above would be carried out to obtain a first
iterate flux solution ψ(1). An improved fission source S(1)
f (ψ(1)=k1), an improved
eigenvalue guess k1 = k0S(1)
f =S(0)
f , and an improved scattering source S(1)
s (ψ(1)=k1)
would be constructed, and the solution would be repeated to obtain ψ(2), and so on,
until the eigenvalues obtained on successive iterates converged to within a specified
tolerance. There are also techniques for accelerating this power iteration procedure.

## 9.10 Multidimensional Discrete Ordinates Methods

### Ordinates and Quadrature Sets

Two angular coordinates are required to specify the direction of motion in
multidimensional geometries. With reference to Fig. 9.22, denote the direction
µ = cos θ
θ
Ω
η = (1-µ2)1/2 cos ω
η
ξ = (1-µ2)1/2 sin ω
ξ
ω
X2
x1
µ
X3
Fig. 9.22 Coordinate system for multidimensional discrete ordinates. (With permission from
Ref. [1]. Copyright 1984, Wiley.)

<!-- page 373 (PDF 394) -->
cosines of the neutron direction Ω with respect to the x1-, x2-, and x3-coordinate
axes as μ, η, and ξ, respectively. Only two of these direction cosines are
independent, and since Ω is a unit vector, μ2 + η2 + ξ2 = 1.
In three-dimensional problems, the flux must be determined in all eight octants
of the unit sphere over which Ω varies. In two-dimensional geometries, there is an
assumption of symmetry in one of the coordinate directions, which reduces to four
thenumberofoctantsoverwhichthefluxmustbedetermined.(Inone-dimensional
geometries, there is an assumption of symmetry in two of the coordinate directions,
and the flux must be determined only within two of the octants.) It is convenient to
use a set of ordinates that are symmetric in the eight octants (i.e., can satisfy
reflective conditions across surfaces in the x1–x2 plane, the x2–x3 plane, and the x3–
x1 plane). Then, if the ordinates and weights are constructed for a set of direction
cosines satisfying μ2
n + η2
n + ξ2
n = 1 in one octant, the ordinates and weights for the
other octants with direction cosine sets (□μn, ηn, ξn), (μn, □ηn, ξn), (μn, ηn, □ξn), (□μn,
□ηn, ξn), (□μn, ηn, □ξn), (μn, □ηn, □ξn), and (□μn, □ηn, □ξn) are obtained simply by
changing the signs of one or more direction cosines.
The level symmetric quadratures shown in Fig. 9.23 use the same set of N/2
positive values of the direction cosines with respect to each of the three axes (i.e.,
ξ4
ξ3
ξ2
ξ1
μ1
η1
η2
η3
η4
η
μ3
μ2
μ4
μ
ξ
Fig. 9.23 Level symmetric S8 discrete ordinates quadrature set. (With permission from
Ref. [1]. Copyright 1984, Wiley.)

<!-- page 374 (PDF 395) -->
μn = ηn = ξn, n = 1, . . . , N/2). Use of such a quadrature set strictly defines the SN
method, although the term SN is loosely used more widely as a synonym for
discrete ordinates. The rotational symmetry of the level symmetric quadrature set
and the requirement μ2
n + η2
n + ξ2
n = 1 determines all the direction cosines except
one. Once μ1 is chosen, the other μn are calculated from
μ2
n = μ2
1 + 2(n □ 1) 1 □ 3μ2
N □ 2
(9.226)
and the ηn = ξn = μn. For the S2 approximation, with only one direction cosine,
satisfaction of μ2
1 + η2
1 + ξ2
1 = 1 uniquely specifies η1 = ξ1 = μ1 =
ffiffiffiffiffiffiffi
1=3
p
, and there
are no degrees of freedom in the choice of ordinates.
The weights in each octant are normalized by
X
N(N+2)=8
n=1
wn = 1
(9.227)
where the index n runs over all the (μi, ηj, ηk), i, j, k = 1, . . . , N/2 ordinate
combinations in the octant. For the S2 approximation, with only one ordinate per
octant, w1 = 1. For other SN approximations, the level symmetry condition
μn = ηn = ξn requires that the weights be equal for ordinates obtained by permuting
the direction cosines, as shown in Fig. 9.24, where the same value of wn is
assigned to all the ordinates indicated by the same number.
Note that unlike the situation in one dimension, this level symmetric quadrature
set does not integrate Legendre polynomials to any given order accurately.
However, even within the restrictions discussed already, there remain a few
S2
S4
1 1
S6
2 2
1 2
S8
2 2
2 3
1 2 2 1
S12
2 2
3 4
5 4
3 5
2 4
3 3
1 2
5 3
S16
2 2
3 5
8 7
4 6
4 7
8 8
3 6
6 4
2 1
6 7
2 5
3 4
1 2
Fig. 9.24 Equal-weighted ordinates for one octant in the SN quadrature. (With permission
from Ref. [1]. Copyright 1984, Wiley.)

<!-- page 375 (PDF 396) -->
degrees of freedom, and these may be chosen for the purpose of correctly
integrating the maximum number of Legendre polynomials in each of the angular
variables consistent with the number of degrees of freedom. A quadrature set so
constructed is given in Table 9.3.

### SN Method in Two-Dimensional x–y Geometry

The discrete ordinates equations in two-dimensional x–y geometry are
μn
@ψ(Ωn)
@x
+ ηn
@ψ(Ωn)
@y
+ Σtψ(Ωn) = Q(Ωn)
(9.228)
where the spatial dependence has been suppressed, Ωn = Ω(μn, ηn), and the source
Q includes a spherical harmonics representation of the scattering source plus a
fission and external source S:
Q(Ωn) =
X
L
l=0
X
l
m=0
(2 □ δm0)Y lm(Ωn)Σslϕm
l + S(Ωn)
(9.229)
Table 9.3 Level Symmetric SN Quadrature Set
SN
n
μn
wn
S4
0.35002
0.33333
0.86889
–
S6
0.26664
0.17613
0.68150
0.15721
0.92618
–
S8
0.21822
0.12099
0.57735
0.09074
0.78680
0.09259
0.95119
–
S12
0.16721
0.07076
0.45955
0.05588
0.62802
0.03734
0.76002
0.05028
0.87227
0.02585
0.97164
–
Source: Data from Ref. [1]; used with permission of Wiley.

<!-- page 376 (PDF 397) -->
and the discrete ordinates approximation for the flux moments are
ϕm
l = 1
X
N(N+2)=2
n=1
wnY lm(Ωn)ψ(Ωn)
(9.230)
Dividing the x–y domain of the problem into mesh boxes xi□1/2 < x < xi+1/2,
yj□1/2 < y < yj+1/2 centered at (xi, yj) with constant cross sections within each
mesh box, integrating Eq. (9.228) over a mesh box, and defining volumeaveraged
quantities
ψi j
n ≡
ΔxiΔyj ∫i
dx∫j
dy ψn(x; y)
(9.231)
Qi j
n ≡
ΔxiΔyj ∫i
dx∫j
dy Qn(x; y)
(9.232)
and surface-averaged fluxes
ψi+1=2;j
n
≡ 1
Δyj ∫j
dy ψn(xi+1=2; y)
(9.233)
ψi;j+1=2
n
≡ 1
Δxi ∫i
dx ψn(x; yj+1=2)
(9.234)
yields the neutron balance equation on a mesh box:
μn
Δxi
(ψi+1=2;j
n
□ ψi□1=2;j
n
) + ηn
Δyj
(ψi;j+1=2
n
□ ψi;j□1=2
n
) + Σij
t ψij
n = Qij
n
(9.235)
It is necessary to relate the volume-averaged flux to the surface-averaged fluxes
for each mesh box. There are several methods for doing this, the most common of
which are the diamond difference method, which is used here, and the thetaweighted
method. The volume- and surface-averaged fluxes are related in the
diamond difference method by
ψi j
n = 1
2 (ψi+1=2;j
n
+ ψi□1=2;j
n
) = 1
2 (ψi;j+1=2
n
+ ψi;j□1=2
n
)
(9.236)
These equations are solved by sweeping the two-dimensional mesh grid in the
direction of neutron travel. With respect to Fig. 9.25, each iteration (on the
scattering source) consists of four sweeps through the grid corresponding to
the four octants. For the octant with (μn > 0, ηn > 0), the sweep is left to right,
bottom to top; for the octant with (μn < 0, ηn > 0), the sweep is right to left, bottom

<!-- page 377 (PDF 398) -->
to top; for the octant with (μn > 0, ηn < 0), the sweep is left to right, top to bottom;
and for the octant with (μn < 0, ηn < 0), the sweep is right to left, top to bottom.
For the octant with (μn > 0, ηn > 0), Eqs. (9.236) can be used to write Eqs. (9.235)
as
ψi j
n =
Σi j
t + 2μn
Δxi
+ 2ηn
Δyi
□1
□
2μn
Δxi
ψi□1=2;j
n
+ 2ηn
Δyj
ψi;j□1=2
n
+ Qi j
n
!
(9.237)
Starting
with
known
incident
flux
(including
vacuum)
conditions
ψ1=2;j
n
= ψin(xL; μn > 0), j = 1, . . . , J and ψi;1=2
n
= ψin(yB; ηn > 0), i = 1, . . . , I,

### 56 46 47 57 49 48 58 51 50 52 54 59 60 41 42 43 44 45 31

yj+ ½
yj–½
Ωm
xi–½
xi+½
xi
yj

### 33 35 37 39 26 27 28 29 30 16 18 20 22 24 11 12 13 14 15 1 3

Known boundary flux
Calculated flux at cell interface
Calculated flux at cell center

### 5 7 9 53 55 32 34 36 38 40 17 19 21 23 25 2 4 6 8 10

Fig. 9.25 Order of sweeping the two-dimensional (x–y) mesh grid for the octant with (μn > 0,
ηn > 0). (With permission from Ref. [1]. Copyright 1984, Wiley.)

<!-- page 378 (PDF 399) -->
where xL refers to the left boundary and yB refers to the bottom boundary, the flux
ψ11
n can be calculated with Eq. (9.237). The solution is then swept to the right
using, alternatively, Eqs. (9.235) and (9.236) to calculate ψ3=2;1
n
, ψ2;1
n ; . . . ; ψI+1=2;1
n
.
Then Eq. (9.236) is used to calculate ψ1;3=2
n
, ψ2;3=2
n
; . . . ; ψI;3=2
n
. Using the boundary
conditions ψ1=2;2
n
= ψin(xL; μn > 0), Eqs. (9.235) and (9.236) can be used alternatively
to sweep to the right across the j = 2 row, and then Eq. (9.236) can be used to
sweep to the right across the j = 2 1
2 row, and so on, until all the outgoing fluxes are
calculated. Sweeps through the other three octants are carried out in a similar
manner but in the order indicated above and with Eqs. (9.235) and (9.236)
combined in such a way as to obtain an algorithm like Eq. (9.237) appropriate for
that octant. The scalar flux
ϕi j = 1
X
N(N+2)=2
n=1
wnψi j
n
(9.238)
and the Legendre moments
ϕi j
lm = 1
X
N(N+2)=2
n=1
wnY lm(Ωn)ψij
n
(9.239)
are then constructed and used to evaluate the scattering and fission source terms.
The process is repeated until source convergence on successive iterations is
within a specified tolerance.

### Further Discussion

The discrete ordinates method in multidimensional geometries is highly geometry
dependent. Because of the coupling of spatial and angular mesh intervals, the
methodology was initially limited to the regular geometries: parallelepipeds,
cylinders, and spheres. However, the development of triangular spatial mesh
techniques enables a variety of geometries to be approximated. A number of other
ordinate and weight quadrature sets have been devised for special purposes (e.g.,
to emphasize a given direction in a deep penetration problem). The acceleration
methods discussed for the one-dimensional discrete ordinates methods are also
used for multidimensional discrete ordinates solutions, but the higher dimensionality
introduces complications that diminish their efficacy. In problems with
optically thick regions in which the scattering cross section (within-group
scattering cross section in multigroup applications) is much larger than the
absorption cross section, the source convergence can become intolerably slow. In
problems with very little scattering and localized neutron sources, unphysical
oscillations in the angular distribution, known as ray effects, arise because of
discrete directions in which the solution is calculated. There are special remedies
for these ray effects, such as a semianalytical calculation of a first collision source
to be used in a subsequent discrete ordinates calculation. These difficulties

<!-- page 379 (PDF 400) -->
notwithstanding, the discrete ordinates method provides a powerful means for
calculating the neutron flux distribution in a nuclear reactor core and the
surrounding shield and structure, and is widely used for problems in which
diffusion theory is inadequate. Detailed discussions of discrete ordinates methods
can be found in Refs. [1,5].

## 9.11 Even-Parity Transport Formulation

The one-group, or within-group, transport equation can be written in the case of
isotropic sources and isotropic scattering:
Ω ? ∇ψ(r; Ω) + Σt(r; Ω)ψ(r; Ω) = Σs(r)ϕ(r) + S(r)
(9.240)
Defining the (+) even- and (□ □) odd-parity components of the angular flux
ψ−(r; Ω) = 1
2 ψ(r; Ω) − ψ(r; □Ω)
[
]
(9.241)
results in the following identities
ψ(r; Ω)
= [ψ+(r; Ω) + ψ□(r; Ω)]
ψ+(r; Ω) = ψ+(r; □Ω)
ψ□(r; Ω) = □ψ□(r; □Ω)
(9.242)
which can be used to demonstrate that the scalar flux and current can be written
in terms of the even and odd, respectively, components
ψ(r) ≡ ∫dΩ(ψ+(r; Ω) + ψ□(r; Ω)) = ∫dΩψ+(r; Ω)
J(r) ≡ ∫dΩ Ω(ψ+(r; Ω) + ψ□(r; Ω)) = ∫dΩ Ωψ□(r; Ω)
(9.243)
Adding Eq. (9.240) written for □Ω to the same equation written for Ω and using
Eq. (9.241) yields
Ω ? ∇ψ□(r; Ω) + Σt(r)ψ+(r; Ω) = Σs(r)ϕ(r) + S(r)
(9.244)
and subtracting the same two equations yields
Ω ? ∇ψ+(r; Ω) + Σt(r)ψ□(r; Ω) = 0
(9.245)
