# 9 Neutron Transport Theory — 9.12 Monte Carlo Methods … References
<!-- source PDF pages 401-414 -->

<!-- page 380 (PDF 401) -->
The second of these equations may be used in the first to eliminate the odd-parity
flux component, resulting in an equation for the even-parity flux,
□Ω ? ∇
Σt(r) Ω ? ∇ψ+(r; Ω)

+ Σ(r)ψ+(r; Ω) = Σs(r)ϕ(r) + S(r)
(9.246)
andEq.(9.245)maybeusedtowritethecurrentintermsoftheeven-paritycomponent:
J(r) = □∫dΩ Ω
Σt(r) Ω ? ∇ψ+(r; Ω)
(9.247)
The vacuum boundary condition becomes (from Eqs. (9.242) and (9.245))
0 = ψ(rs; Ω) = Ω ? ∇ψ+(rs; Ω) − Σt(rs)ψ+(rs; Ω);
Ω ? ns≷0
(9.248)
and the reflection boundary condition is
ψ+(rs; Ω) = ψ+(rs; Ω´)
(9.249)
where Ω is the direction of spectral reflection relative to incident direction Ω.

## 9.12 Monte Carlo Methods

At a fundamental level, neutron transport through matter is formulated as an
essentially stochastic process. The total cross section is a probability (per unit
path length and unit atom density), but not a certainty, that a neutron will have a
collision while traversing a certain spatial interval. If the neutron does have a
collision, the cross sections for the various processes are probabilities, but not
certainties, that the collision will be a scattering, radiative capture, fission, and so
on, event. The neutron flux that we have discussed earlier in the chapter is actually
the mean, or expectation, value of the neutron distribution function. The Monte
Carlo method directly simulates neutron transport as a stochastic process.

### Probability Distribution Functions

Let us postulate that variable x may take on various values over the interval
a ≤ x ≤ b and that there exists a probability distribution function (pdf), f(x), such
that f(x)dx is the probability that a variable takes on a value within dx about x. The
normalization is chosen such that
∫
b
a
f (x)dx = 1
(9.250)

<!-- page 381 (PDF 402) -->
In general, f(x) □ 0 will not be a monotonically increasing function of x, which
means that a given value for f does not correspond to a unique value of x.
A more useful quantity is the cumulative probability distribution function (cdf),
F(x), defined as the probability that the variable x takes on a value less than or
equal to x
F(x) = ∫
x
a
f (x´)dx´
(9.251)
which is a monotonically increasing function of x. Thus, the probability of a
neutron having a value of x between x and x + dx is F(x + dx) □ F(x) = f(x)dx. If κ is
a random number distributed between 0 and 1, the values of x determined from
F(x) = κ will be distributed as f(x). In some cases, it is possible to solve directly for
x = F□1(κ). In other cases, the cumulative distribution function may be known as a
large table of F(xi) and the value of x determined by interpolation, for example, if
F(xj) < κ < F (xj□1) linear interpolation yields
x = xj □
F(xj) □ κ
F(xj) □ F(xj□1) (xj □ xj□1)
(9.252)
There are also methods of selection from the pdf, but it is generally preferable to
select from the cdf.

### Analog Simulation of Neutron Transport

By tracing the path of an individual neutron as it traverses matter and considering
the various processes that may determine its history, we can understand how a
Monte Carlo calculation simulates the stochastic nature of neutron transport
through matter. We begin with the source of neutrons in a nuclear reactor, which
is predominantly if not entirely the fission source. The fission source has a
distribution in space (we discuss calculation of the fission source distribution in
Monte Carlo later), a distribution in energy given by the fission spectrum, and a
distribution in direction that is isotropic. Each of these distributions may be
characterized by a pdf and a cdf. Generating a random number and selecting from
the cdf for the spatial fission distribution defines a location in space for the source
particle. Generating another random number and selecting from the cdf for the
fission spectrum determines the energy of the source particle. Generating third
and fourth random numbers and selecting from the cdf’s for the two independent
angular variables (say μ = cos θ and φ) defines the direction of the source neutron.
Once launched, the source neutron will travel in a straight line until it has a
collision. The probability that a neutron has a collision at a distance s along the
flight path is
T(s) = Σt(s)exp □∫
s
Σt(s´)ds´

(9.253)

<!-- page 382 (PDF 403) -->
which is the pdf for the collision distance s. Generating a random number λ and
selecting s from the cdf
□ln λ = ∫
s
Σt(s´)ds´
(9.254)
locates the position of the first collision, in principle. In fact, the process is
considerably complicated by the nonuniform geometry. It is necessary to know
the composition at the point of the first collision. We treat the medium as
piecewise homogeneous and define the lengths of each uniform segment of the
straight-line flight path as sj. If
X
n□1
j=1
Σt jsj ≤ □ln λ <
X
n
j=1
Σt jsj
(9.255)
the collision occurs in the nth region at a distance
s´
n = 1
Σtn
□ln λ □
X
n
j=1
Σt jsj
!
(9.256)
beyond the entrance of the flight path into region n. The actual procedures for
treating flight paths in complex geometries are quite involved but highly developed
. Modern Monte Carlo codes can essentially model any geometry exactly,
which is a great strength of the method.
Having determined that a collision occurred at a distance sn into region n on the
original flight path, it is now necessary to determine what type of nuclide and what
type of reaction are involved. The probability for a reaction of type x with a
nuclide of species i is
pi x =
Niσi x
P
i;xNiσi x
(9.257)
where Ni is the number density of nuclide i in region n, σix is the microscopic cross
section for reaction x for nuclide i at the energy of the neutron. Constructing a pdf
and a cdf, generating a random number η, and selecting the nuclide and reaction
type by equating η and the cdf (probably involving table interpolation per
Eq. (9.252)), the nuclide and reaction type can be determined.
If the reaction type is absorption, the neutron history is terminated, the energy
and location of the absorbed neutron are recorded, and another history is started.
If the reaction type is elastic scattering, another random number is generated and
equated to the cdf for the cosine of the scattering angle in the center of mass (CM)
to obtain μcm (it is convenient to work in the CM because the scattering is
isotropic except for high-energy neutrons scattering from heavy mass nuclei, and

<!-- page 383 (PDF 404) -->
the pdf and cdf are simple) and by transformation to obtain the scattering angle in
the lab. For energies above thermal, the energy of the scattered neutron is
uniquely correlated to μcm from the scattering kinematics:
E´ = E(A2 + 2Aμcm + 1)
(A + 1)2
(9.258)
Knowing E´, the cosine of the scattering angle in the lab can be determined from
μ = cos θ = 1
2 (A + 1)
ffiffiffiffi
E
E´
r
+ 1
2 (A □ 1)
ffiffiffiffi
E´
E
r
(9.259)
When inelastic scattering or elastic scattering of thermal neutrons from bound
lattice atoms is involved, the cdf’s are more complicated. Generating another
random number and equating it to the cdf for the azimuthal angle φ, the direction
of the scattered neutron can be determined. The scattered neutron is treated as
described already for a fission source neutron, and the calculation is repeated until
the neutron either leaks from the system or is absorbed.

### Statistical Estimation

The mean, or expectation, value of a function h(x) of x is defined in terms of the
pdf for x by
hhi = ∫
b
a
dxh(x) f (x)
(9.260)
and the standard deviation σ and the variance V are defined:
σ(h) =
ffiffiffiffiffiffiffiffiffiffi
V(h)
p
=
∫
b
a
dx[h(x) □ hhi]2f (x)
(
)1=2
= [hh2i □ hhi2]1=2
(9.261)
If N random values of the variable x are chosen from the cdf, as discussed, a
statistical estimate of the mean value hhi is
h = 1
N
X
N
n=1
h(X)
(9.262)
A bound for the error in an estimate of this type is given by the central limit
theorem, which states that if many estimates h of hhi are obtained, each estimate
involving N trials, the variable h is normally distributed about hhi to terms of

<!-- page 384 (PDF 405) -->
accuracy O(1/N1/2). In the limit N →infinity, this theorem takes the form
Prob
hhi □ Mσ(h)
ffiffiffiffi
N
p
≤ h ≤ hhi + Mσ(h)
ffiffiffiffi
N
p
(
)
=
0:6826; M = 1
0:954;
M = 2
0:997;
M = 3
>
>
<
>
>
:
(9.263)
(i.e., the probability that the statistical estimate of the mean value of Eq. (9.262) is
within ±Mσ/N1/2 of the exact value hhi is 68.3% for M = 1, 95.4% for M = 2, 99.7%
for M = 3, etc.).
In general, the first and second moments of h(x) are unknown. The statistical
data can be used to construct approximations to these moments. The expectation
value of h is
hhi = 1
N
X
N
n=1
hh(xn)i = 1
N
X
N
n=1∫
b
a
dxn f (xn)h(xn)
= 1
N
X
N
n=1 ∫
b
a
dx f (x)h(x) = 1
N
X
N
n=1
hhi = hhi
(9.264)
(i.e., the statistical estimate h is an unbiased estimate of hhi since h^hi = hhi. The
expected value of h
2 is
hh
2i = 1
N2
X
N
n=1
h(xn)
X
N
m=1
h(xm)
*
+
= 1
N2
X
N
n=1
h2(xn) +
X
N
n=1
h(xm)
X
N
m≠n
h(xm)
*
+
= 1
N2 Nhh2i + N(N □ 1)hhi2

= hh2i
N □ N □ 1
N
hhi2
(9.265)
(i.e., the statistical estimate h2 is a biased estimate of hh2i since hh
2i ≠hh2i.
Since hh
2i = hh2i, the variance in the statistical estimate of h (h-bar) can be
approximated:
V(h) =
N hh2i □ hhi2

= V(h)
N
'
N □ 1 h2 □ h

(9.266)
and the mean squared fractional error associated with the statistical estimate
of h is
ε2 = 1
N
hh2i
hhi2 □ 1
'
N □ 1
h2
h
2 □ 1
!
(9.267)

<!-- page 385 (PDF 406) -->
### Variance Reduction

It is clearly important to reduce the mean-squared error in order to increase
confidence in the Monte Carlo calculation of the mean value of a quantity h(x)
based on a random sampling of the variable x. From Eq. (9.267), this can be
accomplished by just running more histories, but that involves longer computational
times. There are other methods of reducing the mean-squared error, or the
related variance.
We now discuss a number of such variance reduction methods.
The basic idea of importance sampling is to select from a modified distribution
function that yields the same mean value but a smaller variance. Suppose that
instead of evaluating hhi and the statistical estimate from Eqs. (9.260) and (9.262),
we evaluate them from
hh2i = ∫
b
a
dx h(x) f (x)
f ∗(x) f ∗(x)
(9.268)
h2 = 1
N
X
N
n=1
h(xn) f (xn)
f ∗(xn) ≡ 1
N
X
N
n=1
h(xn)w(xn)
(9.269)
where the values of xn are now selected from the distribution f ∗(x) according to
the procedures described previously. The quantity w(xn) ≡ f (xn)/f ∗(xn) is known
as a weight function. Obviously, the mean value hh1i computed from Eq. (9.260)
and the mean value hh2i computed from Eq. (9.268) are the same. The statistical
estimate h2 of Eq. (9.269) and the statistical estimate h1 of Eq. (9.262) both have
the expectation value hhi. However, the variances are different, and this is the
point. The variances computed by the two sampling procedures are
V 1(h1) = 1
N ∫
b
a
dx h(x) □ hhi
)2f (x)
= 1
N
∫
b
a
d x h2(x)f (x) □ hhi2
"
(9.270)
V 2(h2) = 1
N ∫
b
a
dx h(x)f (x)
f ∗(x)
□ hhi
f ∗(x)
= 1
N
∫
b
a
dx h2(x)f 2(x)
f ∗(x)
□ hhi2
"
(9.271)
The objective is to choose f ∗(x) so that V2 < V1. If the distribution h(x) and its
expectation value were known, the optimum choice of f ∗(x) would be
f ∗(x) = h(x)f (x)
hhi
(9.272)

<!-- page 386 (PDF 407) -->
for which V2 = 0. This suggests that a good estimate of f ∗(x) could reduce the
variance significantly. The function f ∗(x) should be chosen to emphasize those
neutrons that in some sense are the most important to the quantity that is being
estimated, hhi, which suggests that it is an importance or adjoint function
(Chapter 13). However, the variance reduction techniques that are in common
use are schemes for emphasizing neutrons that are most likely to contribute to the
tally for the quantity of interest, hhi, based on experience and intuition. Nonanalog
variance reduction schemes are implemented by adjusting the neutron
weight at each event in its history. An event may be a collision, crossing a
boundary into a different region, and so on.
An exponential transformation is useful in penetration problems to increase
the number of neutron histories that penetrate deeply to contribute to the event
of interest (e.g., penetration of a shield, penetration into a control rod). If
the event of interest depends primarily on neutrons moving in the positive
x-direction, the cross section can be artificially reduced in the x-direction to
enhance penetration:
Σex
t = Σt(1 □ pΩ ? nx)
(9.273)
where 0 ≤ p ≤ 1. At a collision, the particle weight must be multiplied by a weight
wex to preserve the expected weight of the collided neutron; that is,
Σte□Σtsds = wexΣex
t e□Σex
t sds
(9.274)
must be satisfied, which defines the weight
wex = exp[□p(Ω ? nx)s]
1 □ p(Ω ? nx)
(9.275)
When a reaction rate is to be calculated over a small volume in which the
collision probability is small, the artifice of forced collisions is useful. A neutron
entering the volume with weight w that would have to travel a distance l to cross
the volume is split into two neutrons, the first of which passes through the
volume without collision and the second of which is forced to collide within the
volume. Since the actual probability for the particle to cross the region without
collision is exp(□Σtl), the collided and uncollided neutrons must be given
weights wc = w[1 □ exp(□ Σtl)] and wun = w exp(□Σtl), respectively. The history
of the uncollided particle with weight wun is restarted on the exiting surface of
the volume. A new history is started for the collided particle. The pdf for
collision of this second particle within the volume is
f (s) = Σte□Σts
1 □ e□Σtl
(9.276)

<!-- page 387 (PDF 408) -->
Generating a random number ξ(0 ≤ ξ ≤ 1), the distance into the volume at which
the collision takes place is selected:
s = □ 1
Σt
ln 1 □ ξ(1 □ e□Σtl)

(9.277)
and the subsequent history of the collided particle with weight wc is followed.
In some problems, the penetration of a neutron to a particular region may be of
interest, and absorption in other regions may unduly reduce the number of
neutrons that survive to do so. Absorption weighting can be used as an alternative
to terminating a history by an absorption event. In a collision, all outcomes are
treated as scattering events, but the emerging neutron is given a weight
wa = w 1 □ Σa
Σt
(9.278)
to preserve the survival probability.
Since continuing the computation of histories of neutrons with small weights is
inefficient, Russian roulette can be used to either increase the neutron weight or
terminate the history. A random number ξ (0 ≤ ξ ≤ 1) is generated and compared
with an input number v typically between 2 and 10. If ξ > 1/v, the history is
terminated; if ξ < 1/v, the history is continued with original neutron weight w
increased to wRR = wv.
Splitting can be used to increase the number of histories that penetrate in deep
penetration problems. When a neutron with weight w crosses a fixed surface in
the direction of penetration from a region with importance Ii into a region with
importance Ii+1, the history is terminated and Ii+1/Ii new histories are started for
neutrons with the same energy and direction and weights ws = wIi/Ii+1. Here,
importance refers to importance with respect to the quantity of interest hhi.
Russian roulette can be used in conjunction with splitting to terminate histories of
particles with low weights moving across the surfaces away from the direction of
penetration.

### Tallying

The calculation of reaction rates in various regions, over various energies, and by
various nuclides is accomplished straightforwardly by tallying each collision
event. Neutron fluxes and currents can also be constructed by tallying events
and surface crossings. By definition, the collision rate in a region is equal to the
product of the cross section times the flux times the volume. Thus, by tallying the
collision rate (CR), the flux can be calculated from
ϕ = CR
Σt V
(9.279)

<!-- page 388 (PDF 409) -->
A shortcoming of this algorithm is that only particles that collide within the
volume V will contribute to CR, hence to ϕ. Another definition of the scalar flux is
the path length traversed by all particles passing through a volume per unit
volume per unit time,
ϕ = l
V = 1
V
N
X
N
n=1
ln
(9.280)
where l is the track length per unit time in the volume in question of the nth
history. Taking into account the weights of neutrons at various stages of their
histories, this definition of flux becomes
ϕ = 1
V
N
X
N
n
wnln
(9.281)
where wn is the weight the neutron on the nth history had when it traversed the
volume (note that a neutron history may traverse a given volume more than once,
and it should be tallied each time). The variance in the flux estimate is given by
V ar =
N
N □ 1
V 2N
X
N
n=1
(wnln)2 □
V 2N2
X
N
n=1
wnln
!2
"
(9.282)
Currents across surfaces are also of interest. It is straightforward to tally the
rate at which particles are passing through a given surface in the positive and
negative directions, p−
n for history n. The total number of particles per unit time
passing through the surface in the positive and negative directions can then be
estimated from
p− = 1
N
X
N
n=1
wnp−
n
(9.283)
Here wn is the weight that the neutron in the nth history had when it crossed
through the surface to contribute to the tally (note that a neutron in a given
history may cross through a surface more than once, and it should be tallied each
time). The partial currents are obtained by dividing by the surface area A, and the
net current is obtained by subtracting the partial currents:
J = J+ □ J□ = p+ □ p□
A
= 1
AN
X
N
n=1
wn(p+
n □ p□
n)
(9.284)
If the Monte Carlo calculation is to be used to determine small differences, such
as reactivity worths of perturbations, or reactivity coefficients, special methods

<!-- page 389 (PDF 410) -->
must be used to avoid the small difference in two calculations being masked by
statistical errors. The method of correlated sampling addresses this problem by
using the same sequence of random numbers to generate the sequence of events
that describes the histories in the two problems. If the system is unchanged, the
two calculations must yield identical results. So any difference in results is due to
the perturbation.

### Criticality Problems

Monte Carlo can be used to calculate the multiplication constant and associated
eigensolution for the flux distribution. The problem is started with an arbitrary
spatial distribution of neutrons distributed in the fission energy spectrum and
isotropically in direction. This initial spatial distribution can be uniform or a
spatial distribution that is the result of a previous Monte Carlo calculation for a
similar problem or of a deterministic transport (e.g., discrete ordinates) solution
for the problem at hand. The history of a large number of neutrons in a given
generation is followed in parallel to termination, thus obtaining a new fission
distribution for the next generation of neutrons, and the process is repeated
until the fission neutron spatial source distribution has settled down. The total
number of neutrons in successive generations may be increased during the
settling down period to obtain greater detail only after the solution has settled.
Once the spatial fission neutron source distribution has settled down, the ratio
of the total number of fission neutrons on successive generations is the
statistical estimate of the multiplication constant. The computational effort
in the period before the distribution settles down can be reduced by a number of
techniques.
The fission source distribution is determined from generation to generation as
follows. If wn is the weight of the nth history neutron when it has an absorption
event that terminates the history, then either In or In + 1 fission neutrons are
produced at that location in the next generation. The selection is made by writing
wn
vΣf
Σa
= In + Rn
(9.285)
where In is an integer and 0 < Rn < 1. A random number ξ (0 ≤ ξ ≤ 1) is generated.
If Rn > ξ, then In + 1 neutrons are launched in the next generation; otherwise, In
neutrons are launched. Track lengths can provide a second estimate of the total
number of fission neutrons produced by history n:
X
i
wniln
vΣf i
Σai
= total number of secondaries produced by history n
(9.286)
where wni is the neutron weight as it crosses region i and lni is the total track
length across region i.

<!-- page 390 (PDF 411) -->
One of the problems in criticality calculations is to prevent the total neutron
population from increasing or decreasing too much, which it will do if the
assembly is supercritical or subcritical, respectively. One technique is to change
the neutron weight at each collision by multiplying the previous weight by the
expected number of secondary neutrons. A second method is simply to start off
each generation with the same number of neutrons by eliminating some of the
next-generation neutrons if there are more neutrons than in the previous
generation or using some of the neutrons twice if there are less neutrons than
in the previous generation.

### Source Problems

A number of reactor physics problems can be formulated as source problems.
The most obvious is the shielding problem, where the reactor core can be
considered as a fixed neutron source. The calculation of resonance absorption
of neutrons from a slowing-down source in a heterogeneous lattice, the
thermalization of neutrons from a slowing-down source into the thermal range,
and the calculation of temperature coefficients of reactivity from a fixed fission
source in a heterogeneous lattice are other problems that are treated as source
problems.
The resonance cross sections in the resolved region can be represented by
values at a very large number of energy points or calculated from the Dopplerbroadened
Breit–Wigner formula, and the resonance cross sections in the
unresolved region can be selected from a pdf based on the statistics of the
nuclear level spacing and width (Chapter 11). The neutron slowing down through
the resonance region is then treated by sampling the uniform distribution of
neutrons scattered at energy E over the interval E to αE, sampling the path length
distribution to determine the point of collision, sampling the reaction-type
distribution to determine whether the collision is absorption or scattering,
and so on. Effective Doppler-broadened cross sections at different temperatures
can be used in conjunction with correlated sampling to compute temperature
coefficients of reactivity.
A source distribution in energy of neutrons slowing down into the thermal
range in the moderator can be used to launch neutrons isotropically in the
thermal energy region. The distribution of rotational–vibrational levels (Chapter
12) that affect inelastic scattering of neutrons from bound atoms and molecules
can be used to construct pdf’s for inelastic scattering. Then the histories of
thermal neutrons can be traced until termination by absorption. Path length
estimators at different energies can be used to estimate the thermal flux spectrum.

### Random Numbers

Generation of random numbers is essential to a Monte Carlo calculation. There
exist a number of random number generators – algorithms for generating
random numbers – and there is a great deal of controversy about just how
random they are. A discussion of random number generators and several
FORTRAN routines for generating random numbers are given in Ref. [6].

<!-- page 391 (PDF 412) -->
## References

1 E. E. LEWIS and W. F. MILLER, Computational Methods of Neutron Transport,
Wiley -Interscience, New York (1984); reprinted by American Nuclear Society,
La Grange Park, IL (1993).
2 R. V. MEGHREBLIAN and D. K. HOLMES, Reactor Analysis, McGraw-Hill, New York,
(1960), pp. 160–267 and 626-747.
3 R. J. J. STAMM’LER AND M. J. ABBATE, Methods of Steady-State Reactor Physics in
Nuclear Design, Academic Press, London (1983), Chaps. IV and V.
4 E. M. GELBARD, “Spherical Harmonics Methods: PL and Double PL
Approximations,” in H. GREENSPAN, C. N. KELBER, and D. OKRENT, eds., Computing
Methods in Reactor Physics, Gordon and Breach, New York (1968).
5 B. G. CARLSON and K. D. LATHROP, “Transport Theory: The Method of Discrete
Ordinates,” in H. GREENSPAN, C. N. KELBER, and D. OKRENT, eds., Computing
Methods in Reactor Physics, Gordon and Breach, New York (1968).
6 W. H. PRESS et al., Numerical Recipes, Cambridge University Press, Cambridge
(1989), Chap. 7.

## Further Readings

CASE K. M., DE HOFFMANN F., and PLACZEK G., Introduction to the Theory of Neutron
Diffusion, Los Alamos National Laboratory, Los Alamos, NM (1953).
CLARK M. and HANSEN K. F., Numerical Methods of Reactor Analysis, Academic
Press, New York (1964).
DAVISON B., Neutron Transport Theory, Oxford University Press, London (1957).
HENRY A. F., Nuclear Reactor Analysis, MIT Press, Cambridge, MA (1975), Chap. 6.
KALOS M. H., NAKACHE F. R., and CELNIK J., “Monte Carlo Methods in Reactor
Computations,” in H. GREENSPAN, C. N. KELBER, and D. OKRENT, eds., Computing
Methods in Reactor Physics, Gordon and Breach, New York (1968).
LINDAHL S. O. and WEISS Z., “The Response Matrix Method,” in J. LEWINS and M.
BECKER, eds., Adv. Nucl. Sci. Technol. 13 (1981).
SANCHEZ R., “Approximate Solution of the Two-Dimensional Integral Transport
Equation by Collision Probabilities Methods,” Nucl. Sci. Eng. 64, 384 (1977);
“A Transport Multicell Method for Two-Dimensional Lattices of Hexagonal
Cells,” Nucl. Sci. Eng. 92, 247 (1986).
SPANIER J. and GELBARD E. M., Monte Carlo Principles and Neutron Transport
Problems, Addison-Wesley, Reading, MA (1964).

## Problems

### 9.1

Rederive the transmission and absorption probabilities for a purely absorbing
slab given by Eq. (9.28) for the situation in which the incident flux is
linearly anisotropic (i.e., ∼μ).

### 9.2

Use the orthogonality relation for Legendre polynomials to derive the
orthogonality relation for half-angle polynomials given by Eq. (9.23).

<!-- page 392 (PDF 413) -->
### 9.3

Carry through the indicated steps to derive the integral Eq. (9.42).

### 9.4

Develop analytical expressions for the two-dimensional transmission and
escape probabilities of Eqs. (9.110) and (9.112) for rectangular geometry
with dimension ax and ay on a side. Evaluate these transmission and
first-flight escape probabilities for X = 4V/Sλ varying over the range
0.1 < X < 10.0.

### 9.5

Evaluate the first-flight escape probabilities given by Eq. (9.117) with
c = 2.09 for X = 4V/Sλ varying over the range 0.1 < X < 10.0 and compare
with the results of Problem 9.4.

### 9.6

Carry through the indicated steps to derive the PL Eqs. (9.126).

### 9.7

Derive the simplified P3 Eqs. (9.143) from the P3 equations and derive the
boundary conditions of Eqs. (9.145).

### 9.8

Demonstrate that when the ordinates and weights given by Eqs. (9.202) and
(9.203) are used, the discrete ordinates equations with N ordinates reduce
identically to the D-PN□1 equations.

### 9.9

Write a code to solve the one-dimensional discrete ordinates equations in
slab geometry. Solve for the flux in the S2 approximation in a uniform slab
100 cm thick with vacuum boundary conditions, with Σt = 0.25 cm□1,
Σs0 = 0.15 cm□1, and an isotropic source S0 = 1014 n/cm□s distributed
over 0 < x < 25 cm. Repeat for the S4, S8, and S12 approximations.

### 9.10

Repeat Problem 9.9 including anisotropic scattering Σs1 = 0.01 and
Σs2 = 0.0025.

### 9.11

Derive the spatial difference equations for the one-dimensional discrete
ordinates equations in spherical geometry. Reconcile your results with the
algorithms of Eqs. (9.219) and (9.223).

### 9.12

Write a code to solve the SN equations in two-dimensional x□y geometry.
Solve for the flux in the S2 approximation in a uniform square 100 cm on
a side with vacuum boundary conditions, with Σt = 0.25 cm□1, Σs0 =
0.15 cm□1, Σs1 = 0.01, and Σs2 = 0.0025, and an isotropic source S0 =
1014 n/cm2 □ s distributed over 0 < x < 25 cm, 25 < y < 50 cm. Repeat for
the S4, S8, and S12 approximations.

### 9.13

The pdf for variable x is f (x) = 4/π(1 + x2) with 0 ≤ x ≤ 1. Show that if a
random number ξ (0 ≤ ξ ≤ 1) is generated, the corresponding value of
x = tan(ξπ/4).

<!-- page 393 (PDF 414) -->
### 9.14

Derive the simplified P5 diffusion equations and associated Marshak
boundary conditions from the P5 equations. (Hint: Use F0 = 2ϕ2 + ϕ0,
F1 = 4
3 ϕ4 + ϕ2, F2 = ϕ4.)

### 9.15

Derive the diffusion theory Eq. (9.158) from the one-dimensional Pl
equations in cylindrical and spherical geometries.

### 9.16

Derive the spherical harmonics approximation to the neutron transport
equation in three-dimensional x□y□z geometry given by Eqs. (9.181).

### 9.17

Plot the cumulative distribution function corresponding to the fission
spectrum given approximately by χ(E) = 0:453exp(□1:036E)sinh
ffiffiffiffiffiffiffiffiffiffiffi
2:29E
p
over the energy range 104 eV ≤ E ≤ 107 eV.

### 9.18

Calculate the maximum spatial mesh size that could be used in a onedimensional
S2 calculation for a problem with Σt = 0.3 cm□1. Repeat for the
S4 and S8 approximations.

### 9.19

Plot the pdf and cdf for the cross-section distribution in a region with
Σa = 0.15 cm□1, Σs = 0.08 cm□1, and Σf = 0.08 cm□1.

### 9.20

Write a Monte Carlo code to calculate the multiplication constant and flux
distribution for one-speed neutrons in a slab reactor of thickness a = 1.0 m
with isotropic scattering for which (Σa = 0.12 cm□1, Σs = 0.05 cm□1,
vΣf = 0.15 cm□1) over 0 < x < 50 cm and (Σa = 0.10 cm□1, Σs = 0.05 cm□1,
vΣf = 0.12) over 50 < x < 100 cm.

### 9.21

A S(μ) ∼μ2 neutron source is present on the left face of a slab of thickness a
with absorption cross section Σa and isotropic scattering cross section Σs.
Derive expressions for the uncollided and total neutron currents exiting
from the right surface of the slab.

### 9.22

Derive the Boltzmann transport equation from particle balance considerations
on a differential element of space–angle–energy phase space. Justify
any assumptions.
