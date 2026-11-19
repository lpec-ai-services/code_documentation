# 9 Neutron Transport Theory — 9.4 Interface Current Methods in Slab Geometry … 9.5 Multidimensional Interface Current Methods
<!-- source PDF pages 348-364 -->

<!-- page 327 (PDF 348) -->
with the τ being optical path lengths α over the indicated chords in the horizontal
plane in Fig. 9.11:
τ−
ij ≡
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
R2
j □ y2
q
□
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
R2
i □ y2
q
(9.65)
Methods for the numerical evaluation of these expressions are given in Ref. [3].

## 9.4 Interface Current Methods in Slab Geometry

### Emergent Currents and Reaction Rates Due to Incident Currents

Consider the slab geometry configuration depicted in Fig. 9.12, in which a slab
region i is bounded by surfaces i and i + 1 with incident currents J+
i and J□
i+1 and
vi
vj
Ri
y
Rj
τij
–
τij
+
τij
± =
Rj
2-y2  ±    Ri
2-y2
mfp
Fig. 9.11 Annular geometry notation for calculation of collision probabilities (τ is the optical
path length α over the indicated path). (With permission from Ref. [3]. Copyright 1983,
Academic Press.)

<!-- page 328 (PDF 349) -->
emergent currents J□
i and J+
i+1. The angular flux of particles at x arising from an
angular flux of neutrons at x´ is
ψ(x; μ) = e□Σti(x□x´)=μψ(x´μ)
(9.66)
where it is assumed that the total cross section, Σt, is uniform over Δi, and μ is the
cosine of the angle that the particle direction makes with the x-axis. Further
assuming that the incident fluxes, ψ+
i and ψ□
i+1, are isotropically distributed in
angle over the incident hemisphere (i.e., a double P0 approximation), the
uncollided currents emergent from the opposite surface are given in terms of
the incident partial currents (J+
i = 1
2 ψ+
i ; J□
i+1 = 1
2 ψ□
i+1) by
^J
+
un(xi+1) = 2J+
i ∫
μ(e□ΣtiΔi=μ)dμ = 2E3(ΔiΣti)J+
i
^J
□
un(xi)
= 2J□
i+1∫
□1
μ(e+ΣtiΔi=μ)dμ = 2E3(ΔiΣti)J□
i+1
(9.67)
where En is the exponential integral function given by
En(z) ≡ ∫
μn□2e□z=μdμ
(9.68)
Jj
-
Jj+
-
Ji+
+
Ji
+
Xi
Xi+1
X
θ
Δi
ψ(Xi, µ)
ψ(Xi+1, µ)
Fig. 9.12 Nomenclature for slab geometry interface current method.

<!-- page 329 (PDF 350) -->
The first-collision rate for incident particles within Δi is given by
^Ri1 = Σti 2J+
i ∫
dμ∫
xi+1
xi
dx(e□Σti(x□xi)=μ)

+ 2J□
i+1∫
□1
dμ∫
xi+1
xi
dx(e□Σti(x□xi+1)=μ)

(J+
i + J□
i+1)[1 □ 2E3(ΔiΣti)]
(9.69)
The fraction ci of the collision rate that is due to scattering (i.e., to events that do
not remove the particle) from the cohort under consideration (i.e., ci = (Σsi + vΣfi)/
Σti) constitutes a source of once-collided particles, which we assume to be
isotropic (1
2 emerge going to the right and 1
2 to the left) and distributed uniformly
over Δi. Treating these “scattered” neutrons as a distribution of plane isotropic
sources, with the source at x´ producing exiting uncollided fluxes
2 ci
^Ri1
Δi
 exp(□Σti(xi+1 □ x´)=μ)
μ
and
2 ci
^Ri1
Δi
 exp(□Σti(xi □ x´)=μ)
μ
at xi+1 and xi, respectively, the emergent currents of once-collided particles are
^J
+
1 (xi+1) = ∫
xi+1
xi
dx∫
μ 1
2 ci
^Ri1
Δi
 e□Σti(xi+1□x)=μ
μ
dμ
= 1
ci^Ri1
ΔiΣti
2 □ E3(Δi Σti)

= 1
2 ci P0i ^Ri1
^J
□
1 (xi) = 1
2 ci P0i ^Ri1 = 1
2 ciP0i(J+
i + J□
i+1) 1 □ 2E2(ΔiΣti)
[
]
(9.70)
where the average first-flight escape probability for source particles distributed
uniformly over Δi has been defined as
P0i ≡
Δi ∫
xi+1
xi
dx∫
dμ μ e□Σti(xi+1□x)=μ
μ
+
Δi ∫
xi+1
xi
dx∫
□1
dμ μ e□Σti(xi□x)=μ
μ
=
ΔiΣti
2 □ E3(ΔiΣti)

(9.71)

<!-- page 330 (PDF 351) -->
The collision rate for incident particles undergoing a second collision in Δi is
^Ri2 = Σti
2 ci
^Ri1
Δi
□
∫
dμ∫
xi+1
xi
dx´
∫
xi+1
xi
dx e□Σti(x□x´)=μ
μ
+ ∫
□1
dμ∫
xi+1
xi
dx´
∫
x´
xi
dx e□Σti(x□x´)=μ
μ
= ci^Ri1(1 □ P0i) = ci(J+
i + J□
i+1) 1 □ 2E3(ΔiΣti)
[
](1 □ P0i)
!
(9.72)
As before, the fraction ci of this collision rate constitutes a source of twice-collided
particles that are assumed to be isotropic. The emergent currents of twicecollided
particles are given by Eqs. (9.70) but with ^Ri1 replaced by ^Ri2:
^J
+
2 (xi+1) = ^J
□
2 (xi) = 1
2 ci^Ri2P0i
= 1
2 c2
i (J+
i + J□
i+1) 1 □ 2E3(ΔiΣti)
[
](1 □ P0i)P0i
(9.73)
Continuing this line of argument, we derive general expressions for the rate at
which incident particles undergo their nth collision in Δi
^Rin = cn□1
i
(J+
i + J□
i+1)[1 □ 2E3(ΔiΣti)](1 □ P0i)n□1
(9.74)
and for the emergent currents of n-collided incident particles,
^J
+
n(xi+1) = ^J
□
n(xi)
= 1
2 cn
i (J+
i + J□
i+1) 1 □ 2E3(ΔiΣti)
[
](1 □ P0i)n□1P0i
(9.75)
The total collision rate in Δi due to incident currents is obtained by summing
Eq. (9.74):
^Ri =
X
n=1
^Rin = (J+
i + J□
i+1)[1 □ 2E3(ΔiΣti)]
X
n=0
[ci(1 □ P0i)]n
= (J+
i + J□
i+1)[1 □ 2E3(ΔiΣti)]
1 □ ci(1 □ P0i)
(9.76)

<!-- page 331 (PDF 352) -->
and the total emergent currents due to incident currents are obtained by
summing Eq. (9.75) and adding the uncollided contributions of Eqs. (9.67):
^J
+(xi+1) =
2 ciP0i 1 □ 2E3(ΔiΣti)
[
]
1 □ ci(1 □ P0i)
+ 2E3(ΔiΣti)
75J+
i
+
2 ciP0i 1 □ 2E3(ΔiΣti)
[
]
1 □ ci(1 □ P0i)
J□
i+1
^J
□(xj)
=
2 ciP0i 1 □ 2E3(ΔiΣti)
[
]
1 □ ci(1 □ P0i)
+ 2E3(ΔiΣti)
75J□
i+1
+
2 ciP0i 1 □ 2E3(ΔiΣti)
[
]
1 □ ci(1 □ P0i)
J+
i
(9.77)

### Emergent Currents and Reaction Rates Due to Internal Sources

We consider a uniform distribution of particle sources within Δi of strength si/Δi
per unit length. This source is allowed to be anisotropic, with a number s+
i emitted
to the right and s□
i emitted to the left. The emergent currents of uncollided source
particles are
J+
un;s(xi+1) = s+
i
Δi ∫
xi+1
xi
dx∫
dμ μ e□Σti(xi+1□x)=μ
μ
= s+
i P0i
J□
un;s(xi)
= s□
i
Δi ∫
xi+1
xi
dx∫
□1
dμ μ e□Σti(xi□x)=μ
μ
= s□
i P0i
(9.78)
The first-collision rate of source particles within Δi is given by
^Ri1;s = s+
i
Δ Σti∫
xi+1
xi
dx´
∫
xi+1
x´ dx∫
dμ e□Σti(x□x´)=μ
μ
+ s□
i
4i
Σti∫
xi+1
xi
dx´
∫
x´
xi
dx∫
□1
dμ e□Σti(x□x´)=μ
μ
= (s+
i + s□
i ) 1 □
ΔiΣti
2 □ E3(ΣtiΔi)

= si(1 □ P0i)
(9.79)
As before, treating the fraction ci of these particles that undergo scattering
collisions as an isotropic plane source of once-collided particles, the emergent

<!-- page 332 (PDF 353) -->
currents of once-collided source particles are given by
J+
1s(xi+1) = ∫
dμ μ∫
xi+1
xi
dx 1
2 ci
^Ri1;s
Δi
e□Σti(xi+1□x)=μ
μ
= 1
2 ci^Ri1;sP0i = 1
2 cisi(1 □ P0i)P0i
J□
1s(xi)
= ∫
□1
dμ μ∫
xi+1
xi
dx 1
2 ci
^Ri1;s
Δi
e□Σti(xi□x)=μ
μ
= 1
2 ciRi1;sP0i = 1
2 cisi(1 □ P0i)P0i
(9.80)
Continuing in this fashion, the general expression for the nth collision rate of
source particles in Δi is
^Rin;s = cn□1
i
si(1 □ P0i)n
(9.81)
and the general expressions for the emergent currents of n-collided source
particles are
J+
ns(xi+1) = J□
ns(xi) = 1
2 siP0icn
i (1 □ P0i)n
(9.82)
The total collision rate of source particles within Δi is
^Ri;s =
X
n=1
^Rin;s =
si(1 □ P0i)
1 □ ci(1 □ P0i)
(9.83)
and the total emergent currents due to an anisotropic particle source within Δi are
obtained by summing Eqs. (9.82) and adding Eqs. (9.78):
J+
s (xi+1) =
s+
i □ 1
2 si
P0i +
2 si P0i
1 □ ci(1 □ P0i)
J□
s (xi)
=
s□
i □ 1
2 si
P0i +
2 siP0i
1 □ ci(1 □ P0i)
(9.84)

<!-- page 333 (PDF 354) -->
### Total Reaction Rates and Emergent Currents

The total reaction rate in Δi due to incident currents and to internal sources is
obtained by adding Eqs. (9.76) and (9.83):
Ri = (J+
i + J□
i+1)(1 □ T0i) + si(1 □ P0i)
1 □ ci(1 □ P0i)
(9.85)
where the first-flight, or uncollided, transmission probability has been identified:
T0i ≡ 2E3 ΔiΣti
)
(9.86)
Further identifying the total escape probability,
Pi ≡ P0i
X
n=0
[ci(1 □ P0i)]n =
P0i
1 □ ci(1 □ P0i)
(9.87)
the total reflection probability,
Ri ≡
2 ci P0i 1 □ 2E3(ΔiΣti)
[
]
1 □ ci(1 □ P0i)
= 1
2 ci Pi(1 □ T0i)
(9.88)
and the total transmission probability,
Ti = T0i + Ri = T0i + 1
2 ciPi(1 □ T0i)
(9.89)
Eqs. (9.77) and (9.84) can be summed to obtain expressions for the total emergent
currents due to incident currents and internal particle sources:
J+
i+1 = TiJ+
i + RiJ□
i+1 + 1
2 siPi + (s+
i □ 1
2 si)P0i
J□
i
= TiJ□
i+1 + RiJ+
i + 1
2 siPi + (s□
i □ 1
2 si)P0i
(9.90)
The inherent advantage of an interface current formulation of integral transport
theory is evident from Eqs. (9.90). To solve for the currents across interface i,
one needs only the currents at interface i + 1 and the source in the intervening
region. This leads, in essence, to a “four-point” coupling of the unknowns, the
partial currents at i and i + 1, and the evaluation of only one E3 function for each
region. By contrast, in the standard collision probabilities formulation of the
preceding section, the fluxes in all other regions in the problem and the transition
probabilities from all of these regions to the region in question are needed in order

<!-- page 334 (PDF 355) -->
to solve for the flux in a given region, in essence coupling all regions in the
problem. In both formulations, an iterative solution is needed.
As formulated already, the interface current method is based on the D-P0
assumption of an isotropic angular flux distribution within the incident hemisphere
at each interface, for the purpose of calculating the uncollided transmission across
theregion.Thisassumptionisphysicallyplausibleforproblemswithscattering(and
fission) rates comparable to or larger than absorption rates, because this tends to
isotropize the flux exiting from a region. However, for problems with an incident
neutron source on one boundary of an almost purely absorbing medium, the flux
will become increasingly forward directed with distance into the region. In the limit
of a purely absorbing region with an incident isotropic neutron source at x = 0, the
current attenuation at a distance x from the source plane is exactly E2(Σx). If this
problem is modeled in the interface current formulation and the distance x is
subdivided into N intervals Δ, the calculated current attenuation at x is
∏N
n=1E2(ΣΔ), which differs from the exact answer E2 (ΣnΔ). Thus, inaccuracies
might be expected in highly absorbing multiregion problems.
It is informative to sum Eqs. (9.90) to obtain an intuitively obvious balance
between incident and emergent currents and internal sources:
J+
i+1 + J□
i = (Ti + Ri)(J+
i + J□
i+1) + siPi
or
Jout = (T0i + (1 □ T0i)ciPi)Jin + siPi
(9.91)
Solving the first of Eqs. (9.90) for J+
i and using the result in the second equation
leads to a matrix relation among the partial currents at adjacent surfaces:
J+
i
J□
i
5 =
T□1
i
□T□1
i Ri
RiT□1
i
Ti □ RiT□1
i Rj
J+
i+1
J□
i+1
+ 1
2 si
Pi
□T□1
i
1 □ RiT□1
i
@
A+P0i
□T□1
i
s+
i □ 1
2 si
s□
i □ 1
2 si
□ RiT□1
i
s+
i □ 1
2 si
>
>
>
>
=
>
>
>
>
;
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
(9.92)
Equation (9.92) is well suited for numerical evaluation simply by marching from
one boundary of the problem to the other.

### Boundary Conditions

Boundary conditions take on a particularly simple form for an interface current
formulation of integral transport. Let x = 0, i = 0 represent the leftmost surface of
the transport medium. If a vacuum or nonscattering medium with no particle

<!-- page 335 (PDF 356) -->
source exists for x < 0, then J+
0 = 0 is the appropriate boundary condition. If, on
the other hand, a source-free scattering medium exists for x < 0, an albedo or
reflection condition of the form J+
0 = βJ□
0 , where β is the reflection coefficient or
albedo, is appropriate. Finally, if a known current of particles Jin is incident upon
the medium from the left at x = 0, the appropriate boundary condition is J+
0 = Jin.

### Response Matrix

Suppressing internal sources, the matrix Eq. (9.92) may be written in more
compact notation
J −
i = RiJ −
i+1
(9.93)
(where J indicates a column vector and R indicates a matrix) and applied
successively to relate the incident and exiting currents on the left boundary,
J −
0 , to the incident and exiting currents on the right boundary, J−
I :
J −
0 = [R0 ? R1 ? R2 ∙∙∙RI□2 ? RI□1]J−
I ≡ RJ−
I
(9.94)
where the matrix R is the matrix product of the matrices Ri for each slab Δi and
has the form
R =
R11 R12
R21 R22
"
(9.95)
in terms of which Eq. (9.94) may be written as the two equations
J+
0 = R11J+
I + R12J□
I
J□
0 = R21J+
I + R22J□
I
(9.96)
which may be solved to obtain the response matrix relationship between the
incident currents, J+
0 and J□
I , and the exiting currents, J□
0 and J+
I .
J□
J+
I
5 =
R22 □ R21(R11)□1R12
R21(R11)□1
□R21(R11)□1R12
R21(R11)□1
J□
I
J+
or
J out = RMJ in
(9.97)
Once the response matrix, RM, is evaluated, the exiting currents can be computed
rapidly for a given set of incident currents. This formalism can be extended in an
obvious way to treat internal sources.

<!-- page 336 (PDF 357) -->
## 9.5 Multidimensional Interface Current Methods

### Extension to Multidimension

The interface current formulation of integral transport theory can be extended to
two and, in principle, three dimensions. First, for conceptual purposes, we rewrite
Eqs. (9.90) by making the identification J+
i = Jin
i ; J□
i = Jout
i
; J+
i+1 = Jout
i+1; J□
i+1 = Jin
i+1,
and
Λs
i+1siPi ≡ 1
2 siPi + (s+
i □ 1
2 si)P0i
Λs
isiPi
≡ 1
2 siPi + (s□
i □ 1
2 si)P0i
(9.98)
where Λs
i is the fraction of escaping source neutrons that escapes to the left across
surface i and Λs
i+1 is the fraction escaping to the right across surface i + 1. Then,
using Eqs. (9.85)–(9.89), Eqs. (9.90) may be written as
Jout
i+1 = T0iJin
i+1 + (1 □ T0i)(Jin
i + Jin
i+1)ciPi Λi+1 + Λs
i+1si Pi
Jout
i
= T0iJin
i+1 + (1 □ T0i)(Jin
i + Jin
i+1)ciPi Λi + Λs
isi Pi
(9.99)
where Λi = Λi+1 = 1
2 is the fraction of escaping scattered incident neutrons that
escape across surfaces i and i + 1, respectively.
In this form, the terms in Eqs. (9.99) for the emergent currents have a direct
physical interpretation that leads immediately to a generalization to multidimensions
. The outward current across surface i + 1 consists of three terms:
(1) the inward current across surface i times the probability T0i that it is
transmitted across region i without collision to surface i + 1; (2) the inward
currents across all surfaces times the probability (1 □ T0i) that these currents are
not transmitted across region i without collision, times the probability ci that
the first collision is a “scattering” event, times the probability Pi that the
scattered neutrons subsequently escape from region i, times the probability
Λi+1 that escaping neutrons escape across surface i + 1; and (3) the total particle
source si in region i times the probability Pi that these neutrons will escape from
region i, times the probability Λs
i+1 that escaping source neutrons escape across
surface i + 1. Note that Λi+1 and Λs
i+1 can in principle differ because an
anisotropic source is allowed (i.e., Λi+1 = 1
2 and Λs
i+1 is given by Eq. (9.98)
for slab geometry).
Generalization to multidimensions is straightforward, in principle. Consider
the two-dimensional configuration in Fig. 9.13. The current from region k into
region i is denoted Jki (Γk→i in the figure), the probability that the current
entering region i from region k is transmitted across region i without collision
to contribute to the current from region i into region j is denoted Tkj
0i, and the
probability that a collided or source neutron escaping from region i escapes
into region j is denoted Λij. The generalization of Eqs. (9.99) to two dimensions

<!-- page 337 (PDF 358) -->
is then
Jij =
X
i
k
Tkj
0iJki +
X
i
k
1 □
X
i
l
Tkl
0i
!
JkiciPiΛij + Λs
ijsi Pi
(9.100)
where the summation Pi
k is over all regions k that are contiguous to region i. The
three terms in Eq. (9.100) correspond physically to (1) the sum of the currents
incident into region i from all contiguous regions times the probability that each is
transmitted across region i without collision to exit into region j (note that the
possibility of concave surfaces is allowed by including uncollided transmission
from region j across region i back into region j); (2) the sum of the currents
incident into region i from all contiguous regions times the probability that each is
not transmitted without collision across region i to any of the contiguous regions,
times the probability that the first collision is a “scattering” event, times the
probability that the scattered neutron eventually escapes from region i into region
j; and (3) the source of neutrons in region i times the probability that a source
neutron in region i eventually escapes into region j.
Uncollided flux
Γk-iTi
k+j
CiPiʌi-jΓk-i
Ti
k-l
i
l
1-
Γout
Γin
Collided flux

### Region j Region i Region k

Σ
Fig. 9.13 Planar projection of geometry for multidimensional interface current methods.

<!-- page 338 (PDF 359) -->
### Evaluation of Transmission and Escape Probabilities

The general form for the evaluation of transmission and escape probabilities can
be developed using the point kernel discussed previously. We treat the case of
incident fluxes that are distributed isotropically in the incident hemisphere of
directions and volumetric neutron sources (scattering, fission, external) that are
uniformly distributed over volume and emitted isotropically in direction. These
results can be extended to anisotropic incident fluxes and nonuniform and
anisotropic volumetric source distributions by extending the procedures indicated
below.
The probability that a neutron introduced isotropically at location ri within
volume Vi escapes without collision across the surface Ski that defines the
interface between volume Vi and contiguous volume Vk is the probability
dΩ=4πjrSki □ rij
2 that the neutron is traveling within a cone of directions dΩ,
which intersects that surface, times the probability exp[□α(rSki; ri)] that the
neutron reaches the surface at location rSki along the direction Ω from ri without
a collision, integrated over all Ω that intersect the surface Ski from point ri. This
probability is then averaged over all points ri within volume Vi to obtain
P0iΛk =
4π V i ∫V i
dri∫Ski
dS e□α(rSki;ri)
jrSki □ rij
(9.101)
Extension of this expression to treat anisotropic neutron emission would be
accomplished by including a function f (rSki; ri) under the integral to represent any
directional dependence of neutron emission. Extension to include a spatial
distribution g(ri) of neutron sources would be accomplished by including this
function in the integrand.
The probability that an incident unit neutron flux that is isotropically distributed
over the inward hemisphere of directions entering volume Vi from volume
Vk across surface Ski is transmitted without collision across volume Vi to the
surface Sji that forms the interface with contiguous volume Vj is the product of the
probability nSki ? dΩ=2πjrSki □ rSjij
2 = (nSki ? Ω)dΩ=2πjrSki □ rSjij
2 that a neutron
incident across Ski is traveling within a cone of directions dΩ, which intersects
the surface Sji, times the probability exp[□α(rSji; rSki)] that the neutron reaches the
surface at location rSji along the direction Ω from rSki without a collision,
integrated over all Ω that intersect the surface Sji from point rSki. The quantity
nSki is the unit vector normal to the surface Ski in the direction from volume Vk
into volume Vi. This probability is then averaged over all points rSki on Ski, to
obtain
Tkj
0i =
∫Ski
d S∫Sji
d S[e□α(rSji;rSki)(nSki ? Ω)=jrSji □ rSkij
2]
∫nSki ? Ω>0
dΩ∫Ski
dS
(9.102)

<!-- page 339 (PDF 360) -->
Extension of this expression to include an anisotropic incident neutron flux
would be accomplished by including a function f (rSki; rSji) in the integrand.

### Transmission Probabilities in Two-Dimensional Geometries

To develop computational algorithms, we consider geometries with symmetry in
onedirection, which are conventionally known as two-dimensional geometries. It is
important to keep in mind, however, that neutron flight paths take place in three
dimensions. Consider a volume Vi that is symmetric in the axial direction and
bounded by flat vertical surfaces, so that a horizontal (x □ y) planar slice is as shown
inFig.9.14,withtheverticaldimensionnormaltothepage.Wewanttocalculate the
transmission coefficient from volume 1 through the volume into volume 3. A threedimensional
projection and a vertical projection are shown in Fig. 9.15. The points
ξ1 and ξ3 in Fig. 9.14 are the projection onto the horizontal plane of the vertical axes
shown in Fig. 9.15. The differential solid angle in this coordinate system is
dΩ = 1
4π sin θ´ dθ´ dϕ = □ 1
4π cos θ dθ dϕ
(9.103)
ξ3
max
ξ3
min
ξ1
max
ϕ
ℓ
ξ1
min
ξ3
ξ1
Fig. 9.14 Planar projection of geometry for transmission probability calculation in two
dimensions.

<!-- page 340 (PDF 361) -->
The incident directional flux from volume 1 at point ξ1, ψ(r □ RΩ, Ω) is
attenuated when it traverses the distance R to reach the point ξ3 and enter
volume 3:
ψ(r; Ω) = ψ(r □ RΩ; Ω)e□ΣR
(9.104)
The incident partial current density (n/cm2 □ s) from volume 1 at point ξ1 is
jin(ξ1) = ∫nin ? Ω>0
dΩ(nin ? Ω)ψ(r □ RΩ; Ω)dΩ
= □ 1
4π ∫
π
dϕ∫
π=2
□π=2
dθ cos2 θ sin ϕψ(r □ RΩ; Ω)
(9.105)
where nin □ Ω = cos θ sin ϕ has been used. When the incident flux is isotropic in
the incident hemisphere (double-P0 approximation), this becomes
jiso
in (ξ1) = 1
4 ψ(r □ RΩ)
(9.106)
The incident partial current (n/s) is obtained by multiplying by the (arbitrary)
axial dimension H and integrating over ξmin
≤ ξ1 ≤ ξmax
Jin = H∫
ξmax
ξmin
dξ1 jin(ξ1)
(9.107)
Z, ξ1
Z, ξ1
ξ3
ξ3
r
R
Y
X
R
r-RΩ
Ω
Ω
θ
θ
θʹ
ϕ
ℓ
Fig. 9.15 Three-dimensional and axial projection of geometry for transmission probability
calculation in two dimensions.

<!-- page 341 (PDF 362) -->
The incident neutrons from volume 1 that enter volume Vi at ξ1 within the solid
angle subtended by volume 3 and traverse volume i without collision to enter
volume 3 constitute an uncollided neutron current out of volume Vi into volume
3, and hence a contribution to the incident current into volume 3 from volume i.
For the moment we write this contribution to the current into volume 3 as
Jout = H∫
ξmax
ξmin
dξ1∫Ω ? nout > 0
ϕ(ξ1) 3 3
dΩ(Ω ? nout)ψ(r □ RΩ; Ω)e□ΣR
= H∫
ξmax
ξmin
dξ1∫
ϕmax(ξ1)
ϕmin(ξ1)
dϕ∫
π=2
□π=2
dθ cos2θ sin ϕe(□Σl(ϕ(ξ1))=cosθ)
□ ψ(r □ RΩ; Ω)
(9.108)
where nout □ Ω = cos θ sin ϕout may differ from nin □ Ω = cos θ sin ϕ if the interfaces
with volumes 1 and 3 are not parallel, and ϕ(ξ1) 3 3 indicates angles ϕ from a
point ξ1 that intersect the interface with region 3. When the incident flux from
volume 1 is isotropic in the incident directional hemisphere, this becomes
Jiso
out = H
2π ∫
ξmax
ξmin
dξ1∫
ϕmax(ξ1)
ϕmin(ξ1)
dϕ sin ϕoutK i3[Σl(ϕ(ξ1))]ψ(r □ RΩ)
(9.109)
The transmission probability for an isotropic incident flux distribution from
volume 1 that is uniform over ξmin
≤ ξ1 ≤ ξmax
can be written in a form that
couples the contribution to the incident current into volume 3 with the incident
current into volume i:
T13
0i ≡ Jiso
out
Jiso
in
= 2
π
∫
ξmax
ξmin
dξ1∫
ϕmax(ξ1)
ϕmin(ξ1)
dϕsinϕoutK i3[Σl(ϕ(ξ1))]
ξmax
□ ξmin
(9.110)
When the incident and exiting surfaces (the interfaces of volumes 1 and i and of
volumes 3 and i in this example) are not parallel, there is a subtlety about the
direction to take for nout in the equations above. The incident current into volume
i from volume 1 was calculated on the basis of a DP-0 angular flux approximation
with respect to the orientation of the incident surface. The transport of the
uncollided incident DP-0 angular flux across region i is properly calculated, and
by using nout = nin, the exiting uncollided partial current in the direction normal
to the incident surface is properly calculated. So the neutron flow into volume 3 is
properly calculated, although the direction of this current exiting volume i is not
normal to the exit surface. In constructing the incident current for region 3 from
region i, this uncollided contribution from region 1 is added to the uncollided
contribution from regions 2 and 4 and to the collided contribution, and the
combination is assumed to have a DP-0 incident angular distribution into volume

<!-- page 342 (PDF 363) -->
3 with respect to the orientation of this incident interface of volume 3 (the exiting
interface of volume i). Thus, in the discussed equations, nout = nin should be used.

### Escape Probabilities in Two-Dimensional Geometries

The neutron flux per unit surface area dA normal to the direction of neutron flight
at a distance R away from an isotropic point source is exp(□ ΣR)/4π R2, and with
reference to Fig. 9.15, the surface area normal to the direction Ω of neutron travel
is dA = R dθl dϕ = l2 dθ dϕ/cos θ. Thus, with reference to Fig. 9.16, an isotropic
neutron source of unit strength per axial length located at ri within volume Vi
produces an outward current of uncollided neutrons over the surface labeled ξ3
into volume 3 that is described by
J3
out(ri) = ∫A□S3
(nout ? Ω) e□ΣRdA
4πR2
= ∫ϕ□S3
dϕ∫
π=2
□π=2
dθ(cos θ sin ϕout) e□Σl(ϕ)=cosθ(l2=cos θ)
4π(l=cos θ)2
= ∫ϕ□S3
dϕ sin ϕout
2π ∫
π=2
dθ cos2θe□Σl(ϕ)=cosθ
= ∫ϕ□S3
dϕ sin ϕout
K i3(Σl(ϕ))
2π
(9.111)
where ϕ □ S3 indicates the range of ϕmin < ϕ < ϕmax subtended by side S3 at
location ri within volume Vi.
ϕmin
ϕmax
ϕ
ϕout
ℓ
(x, y)
nout
Fig. 9.16 Planar projection of geometry for escape probability calculation in two dimensions.

<!-- page 343 (PDF 364) -->
The average value of J3
out(x; y) over the planar two-dimensional area Ai of
volume Vi is just the probability that an isotropic, uniform neutron source si will
produce an uncollided current siΛs
i3P0i from volume Vi into volume V3:
Λi3P0i = 1
Ai ∫Ai
dx dy J3
out(x; y)
= 1
Ai ∫Ai
dx dy∫ϕ□S3
dϕ sin ϕout
K i3(Σl(ϕ))
2π
(9.112)
The proper value of nout is the outward normal to the surface in question, and
ϕout is measured with respect to the orientation of that surface, whereas ϕ may
be measured with respect to a fixed coordinate system, so that in general
ϕout = ϕ, although it is convenient to orient the coordinate system so that
ϕout = ϕ.
The total uncollided escape probability is obtained by summing Eq. (9.112)
over all volumes Vk that are contiguous to volume Vi:
P0i =
X
k
ΛikP0i
(9.113)
and the directional escape fractions are calculated from
Λij = ΛijP0i
P0i
=
ΛijP0i
P
kΛikP0i
(9.114)
Using the same arguments as were made for the one-dimensional case in the
preceding section, the total escape probability, including escape after zero, one,
two, . . . collisions can be calculated from
Pi =
P0i
1 □ ci(1 □ P0i)
(9.115)
where ci = (Σsi + vΣfi)/Σti is the number of secondary neutrons produced per
collision.

### Simple Approximations for the Escape Probability

Physical considerations lead to a simple approximation for the first-flight escape
probability. In the limit that the average neutron path length hli in a volume V is
much less than the mean free path X for a collision, the escape probability tends to
unity. In the limit when hli ≫λ, a simple approximation for the first-flight escape
probability is 1 □ exp(□λ/hli) ≈ λhli. If we associate the average neutron path
length in the volume with the mean chord length 4V/S, where S is the surface area
of the volume V, a simple rational approximation for the escape probability, first
