# 16 Space–Time Neutron Kinetics — □ Fission event: … Problems
<!-- source PDF pages 700-711 -->

<!-- page 683 (PDF 700) -->
## □ Fission event:

@P
@t
f
= P
ig Λf ig (nig + 1)Pig(nig + 1) P
vp pg(vp)
h
□
(1 □ β´vp) P
g´ χg´
p Pig(nig´ □ vp) ∏´Pi´´g´´

∏^Pi´m´

n
+ P
m β´
mvp
P
g´ χg´
p Pig´(nig´ □ vp) ? ^Pim(cim □ 1)
□ ∏´Pi´´g´´

∏´^Pi´m´

□ nigPig(nig) ∏´Pi´g´

∏^Pi´m´

@G
@t
f
= P
ig Λf ig
P
g´ f gχg´
p □ β´ □ P
m βm´υim
 P
g´ uig´ @f g
@uig´ χg´
p □ uig

□ @G
@uig
The quantity Λ□ig represents a reaction frequency per neutron, in space cell i and
energy cell g, and the subscripts c, s, and f refer to capture, scattering, and fission,
respectively.7 Kgg´ is the probability that a scattering event which occurred in energy
cell g transfers a neutron to energy cell g´, while χg
p and χg
m are the probabilities that a
neutron produced by fission and m-type precursor decay, respectively, has energy
within energy cell g. The decay constant for precursor type m is λm, and β´
m is the
average ratio of the number of m-type precursors to the number of prompt
neutrons produced in a fission (β´ = Σmβm´). Sig is the neutron source rate in space
cell i and energy cell g. The quantity lg
ii´ represents the frequency per neutron at
which neutrons in space cell i and energy cell g will diffuse into space cell i´ (without
a change in energy). The prime on the product operator, Π, indicates that the
product is taken over all i, g, and m except those explicitly shown in the same term.
The quantity fg is the probability generating function for pg(vp), which is the
probability distribution function for the number of prompt neutrons emitted in
a fission that was caused by a neutron in energy cell g:
f g(uig´) =
X
nig´
u
nig´
ig´ pg(vp)
(16.251)
A single fissionable species is assumed for simplicity.
Appropriate balance equations for the transition probability, P, and its probability
generating function, G, may be constructed from these terms:
@P
@t (N´t´jNt) = @P
@t
S
+ @P
@t
c
+ @P
@t
T
+ @P
@t
s
+ @P
@t
d
+ @P
@t
f
(16.252)
@G
@t (N´t´jUt) = @G
@t
S
+ @G
@t
c
@G
@t
T
+ @G
@t
s
+ @G
@t
d
+ @G
@t
f
(16.253)
7 For example, Λf ig = vgΣg
f , vg = neutron speed; Σg
f = fission cross section.

<!-- page 684 (PDF 701) -->
### Means, Variances, and Covariances

By differentiating Eq. (16.253) with respect to uig and vim and evaluating the
resulting expressions for U = 1, equations for the mean value of the neutron and
precursor distribution, respectively, are obtained (see Eqs. (16.246) and
(16.247)):
@nig(t)
@t
= Sig(t) □ [Λcig(t) + Λsig(t) + Λf ig(t)]nig(t)
+
X
G
g´=1
Λsig(t)Kg´g
i nig´(t) + χg
p
X
G
g´=1
vg´
p Λf ig´(t)nig´(t)
+
X
M
m=1
χg
mλmcim(t) +
X
I
i´=1
lg
i´i(t)[ni´g(t) □ nig(t)]
(16.254)
@cim(t)
@t
= □λmcim(t) + βm´
X
G
g=1
vg´
p Λf ig(t)nig(t)
g = 1; . . . ; G; i = 1; . . . ; I; m = 1; . . . ; M
(16.255)
Making use of the identities vg
p ≡ (1 □ β)vg, where vg is the average number of
neutrons (prompt and delayed) per fission induced by a neutron in energy cell g,
and β´ = β/(1 □ β), it is apparent that these are the conventional space- and
energy-dependent neutron and precursor kinetics equations in the finite-difference
multigroup approximation.
By taking second partial derivatives of Eq. (16.253) with respect to uig and vim,
and evaluating the result for U = 1, equations for the quantities defined by Eqs.
(16.248)–(16.250) are derived:
@W ig;i´g´
@t
= Signi´g´ + Si´g´nig´ □ (Λcig + Λci´g´)W ig;i´g´
+ P
j lg
ji(W jg;i´g´ □ W ig;i´g´) + P
j lg´
ji´(W jg´;ig □ W jg;ig)
+ P
g´´(Λsig´´K g´´g
i
W i´g;ig + Λsi´g´´Kg´´g´
i´
W i´g´´;ig)
□ (Λsig + Λsi´g´)W ig;i´g´ + P
m λm(χg
mY im;i´g´ + χg´
mY i´m;ig)
+ χg
p
P
g vg´´
p Λf ig´´W i´g´;ig´´
+ χg´
p
P
g´´ vg´´
p Λf i´g´´W ig;i´g´´(Λf ig + Λf i´g´)W ig;i´g´
+ χg
p
P
g´´ Λf ig´´vg´´
p
vg´´
p □ 1

nig´δig;i´;g´
i; i´ = 1; . . . ; I; g;
g´ = 1; . . . ; G
(16.256)

<!-- page 685 (PDF 702) -->
@Y im;i´g´
@t
= Si´g´cim □ Λci´g´Y im;i´g´ + P
j lg´
ji´(Y im;jg´ □ Y im;i´g´)
+ P
g´´ Λsi´g´´K g´´g´
i´
Y im;i´g´ □ Λsi´g´Y im;i´g´ □ λmY im;i´g´
+ P
m´ λm´χg´
m´Zim;i´m´ + β´
m
P
g´´ vg´´
p Λf i´g´W i´g´;ig´´
+ χg´
p
P
g´´ vg´´
p Λf i´g´´Y im;i´g´´ □ Λf i´g´Y im;i´g´
+ βm
P
g´´ (vg´´
p )2Λf i´g´´ni´g´´δi;i´
i; i´ = 1; . . . ; I;
m = 1; . . . ; M;
g´ = 1; . . . ; G
(16.257)
@Zim;i´m´
@t
= □ λmZim;i´m´ □ λm´Zim;i´m´ + β´
m
P
g vg
pΛf i´gY im;i´g
+ β´
m´ P
g vg
pΛf igY i´m´;ig;
i; i´ = 1; . . . ; I;
m; m´ = 1; . . . ; M
(16.258)
Equations (16.256)–(16.258) are coupled.
From Eqs. (16.248)–(16.250), it is apparent that the solutions of Eqs. (16.256)–
(16.258) are related to the variances and covariances of the neutron and precursor
distributions; for example,
σ2
ig ≡ (nig □ nig)2 = W ig;ig □ nig(nig □ 1)
(16.259)
σ2
im ≡ (cim □ cim)2 = Zim;im □ cim(cim □ 1)
(16.260)
σ2
igm ≡ (nig □ nig)(cim □ cim) = Y im;ig □ nigcim
(16.261)

### Correlation Functions

Define the correlation functions
nig(t)ni´g´(t´) ≡
X
N
X
N´
nigni´g´P(N´t´jNt)
(16.262)
cim(t)ni´g´(t´) ≡
X
N
X
N´
cimni´g´P(N´t´jNt)
(16.263)
nig(t)ci´m´(t´) ≡
X
N
X
N´
nigci´m´P(N´t´jNt)
(16.264)
cim(t)ci´m´(t´) ≡
X
N
X
N´
cimci´m´P(N´t´jNt)
(16.265)
By differentiating Eqs. (16.262)–(16.265) with respect to t, and using
Eqs. (16.245)–(16.248), (16.254), and (16.255), equations satisfied by the

<!-- page 686 (PDF 703) -->
correlation functions may be obtained.
@
@t nig(t)ni´g´(t´) = Sig(t)ni´g´(t) □ [Λcig(t) + Tig(t) + Λsig(t)
+ Λf ig(t)]nig(t)ni´g´(t) +
X
M
m=1
λmχg
mcim(t)ni´m´(t´)
+
X
G
g´´=1
Λsig´´(t)Kg´´g
i
(t) + χg
pvg´´
p Λf ig´´(t)
h
i
□ nig´´(t)ni´g´(t´)
(16.266)
@
@t cim(t)ni´g´(t´) = β´
m
X
G
g=1
vg
pΛf ig(t)nig(t)ni´g´(t´) □ λmcim(t)ni´g´(t´)
(16.267)
@
@t nig(t)ci´m´(t´) = Sig(t)ci´m´(t´) +
X
G
g´´=1
Λsig´´(t)Kg´´g
i
(t) + χg
pvg´´
p Λf ig´´(t)
h
i
□ nig´´(t)ci´m´(t) □ [Λcig(t) + Tig(t) + Λsig(t)
+ Λf ig(t)]nig(t)ci´m´(t´) +
X
M
m=1
λmχg
mcim(t)ci´m´(t´)
(16.268)
@
@t cim(t)ci´m´(t´) = β´
m
X
G
g=1
vg
pΛf ig(t)nig(t)ci´m´(t´) □ λmcim(t)ci´m´(t´)
i; i´ = 1; . . . ; I;
m; m´ = 1; . . . ; M
(16.269)
Equations (16.266) and (16.267) are coupled, as are Eqs. (16.268) and (16.269).
The operator Tig is defined by the operation
Tignigni´g´ =
X
I
i´´=1
lg
i´´i(ni´´gni´g´ □ nigni´g´)

### Physical Interpretation, Applications, and Initial and Boundary Conditions

If all members of a large ensemble of identical reactors are known to be in an
identical state, N´, at time t´, if all reactors are operated identically subsequent to
time t´, and if the state, N, of each reactor could be determined at a later time t, the
number of reactors in the ensemble that would be found to have a given state, N,
would approach the distribution P(N´t´|Nt). Thus, nig(t) is the ensemble average
for the number of neutrons in space cell i and energy cell g at time t, and similarly,
cim(t) is the ensemble average for the number of m-type precursors in space cell i
at time t.

<!-- page 687 (PDF 704) -->
Alternatively, consider a single reactor that is brought to a known state N´ at a
reference time t´, and subsequently operated in a given manner until a reference
time t. If this procedure is repeated a large number of times, the distribution of
the number of times the reactor is in a given state N at reference time t
approaches
P(N´t´|Nt). Consequently, nig(t) and cim(t) are mean values of the neutron and
precursor populations, and σ2
ig(t) and σ2
im(t) are the mean-squared deviations in
these populations. These deviations are an indication of the uncertainty
associated with the usual assumption that the actual population is equal to
the mean value, the latter being predicted by conventional kinetics equations.
Such considerations are important in analyzing weak-source startup problems.
A set of initial conditions for Eqs. (16.254)–(16.258) may be obtained from the
identity
P(N0t0jNt0) = δNN0
(16.270)
where the zero superscript indicates the known state at t0. From Eqs. (16.243) and
(16.245)–(16.250), the following initial conditions may be deduced:
G(N0t0jUt0) = ∏
igm
u
n0
ig
ig u
c0
im
im
(16.271)
nig(t0) = @G
@uig
(N0t0jUt0)
U=1
= n0
ig
(16.272)
cim(t0) = @G
@vim
(N0t0jUt0)
U=1
= c0
im
(16.273)
W ig;i´g´(t0) =
n0
ig n0
ig □ 1

; i´g´ = ig
n0
ign0
i´g´;
i´g´ ≠ig
<
:
(16.274)
Y im;i´g´(t0) = n0
i´g´c0
im
(16.275)
Zi´m´;im(t0) =
c0
im c0
im □ 1

; i´m´ = im
c0
imc0
i´m´´;
i´m; ≠im
(
(16.276)
In practice, it is not possible to ascertain the “known” initial conditions. This
difficulty may be circumvented by using homogeneous initial conditions and, in a
subcritical system, taking the asymptotic solution of Eqs. (16.254)–(16.258) as
the initial conditions for further calculations involving changes in operating
conditions. Alternatively, the time-independent versions of Eqs. (16.254)–
(16.258) may be solved to provide initial conditions.
External boundary conditions may be treated by assuming that the space cells
on the exterior of the reactor are contiguous to a fictitious external space cell in

<!-- page 688 (PDF 705) -->
which the mean value, variance, or covariance is zero, for the purpose of
evaluating the net leakage operator. This is equivalent to the familiar extrapolated
boundary condition of neutron diffusion theory.
The interpretation of P(N´t´|Nt) just discussed leads to an interpretation of the
correlation functions. For example, nig(t)ni´g´(t´) is the expectation (mean) value of
the product of the number of neutrons in space cell i´ and energy cell g´ at t´, and
the number of neutrons in space cell i and energy cell g at t. When the reactor
properties are time independent, the ensemble average may be replaced by an
average over time in a single reactor (the ergodic theory).8 In this case,
nig(t´ + τ)ni´g´(t´) is amenable to experimental measurement if the energy and
space cells are chosen to conform with the detector resolution. The corresponding
theoretical quantity is obtained by solving the time-independent versions of
Eqs. (16.266) using the same type of external boundary treatment discussed
before, and employing corrections for the detection process and counting circuit
statistics.

### Numerical Studies

Equations (16.254)–(16.258) have been solved numerically for the special case of
one energy cell, one delayed neutron precursor type, and one spatial dimension, to
study the characteristics of the neutron and precursor distributions under a
variety of static and transient conditions. The results of these studies may be
characterized in terms of the mean value of the neutron (ni) and precursor (ci)
distributions in region i and in terms of the relative variances in the neutron and
precursor distributions in region i, which are defined by the relations
μi ≡ (ni □ ni)2
n2
i
= W i;i □ ni(ni □ 1)
n2
i
(16.277)
εi ≡ (ci □ ci)2
c2
i
= Zi;i □ ci(ci □ 1)
c2
i
(16.278)
The quantities μi and εi are measurements of the relative dispersion in the
neutron and precursor statistical distributions in region i.
Certain general trends emerge from the numerical studies that have been
performed:
1) When the reactor is subcritical, the asymptotic values of μi and εi vary from
region to region, and within a given region εi < μi.
2) When the reactor is subcritical, the asymptotic values of μi and εi depend on
the source level and distribution and the degree of subcriticality. In general,
increasing the source level or the multiplication factor reduces μi and εi.
3) When the reactor is supercritical, μi and εi attain asymptotic values that are
identical in all regions, and μi = εi.
8 For a subcritical reactor.

<!-- page 689 (PDF 706) -->
4) When the reactor is brought from a subcritical to a supercritical configuration,
μi generally decreases and εi generally increases.
5) The asymptotic value of μi and εi in a supercritical reactor is sensitive to the
manner in which the reactor is brought supercritical.
a) For the withdrawal of a single rod (or group of rods) between fixed limits,
the more rapid the withdrawal the larger the asymptotic value of μi and εi.
b) When a number of rods are to be withdrawn, each rod at the same rate,
withdrawing the rods on one side of the reactor and then withdrawing the
rods on the other side of the reactor results in a larger asymptotic value for
μi and εi than if all the rods are withdrawn simultaneously.
c) Withdrawing a rod (group of rods) from position a to position c, then
reinserting it (them) to position b (a>b>c) results in a larger asymptotic
value of μi and εi than if the rod (group of rods) was withdrawn at the same
rate from position a to position b.
6) The time at which μi and εi obtain an asymptotic value may differ from region
to region, particularly if flux tilting is significant.
7) When the reactor is brought from a subcritical to a supercritical configuration,
the asymptotic value of μi and εi depends on the source level and the initial
subcritical multiplication factor.
8) The more supercritical the configuration obtained before μi and εi attain their
asymptotic value, the larger this asymptotic value is.
9) For a supercritical reactor, μi and εi generally attain their asymptotic value
when ni is of the order of 105 n/cm3.
In a subcritical reactor, the neutron fluctuations are governed by fluctuations in
the neutron sources, which are the instantaneous natural and neutron-induced
fission rates and delayed neutron precursor decay rates, as well as by the
fluctuations of the fission, capture, and diffusion processes. The precursor
fluctuations are governed by an integral of the fission fluctuations over several
mean lifetimes for the precursors (τmean = λ□1). This integral dependence of the
precursor fluctuations on the fluctuations in the fission process tends to smooth
out the fluctuations in the former relative to fluctuations in the latter:
Cm(r; t) = ∫
t
t□nτ
dt´e□λ(t□t´)β Σf (t; t´)n(r; t´)v;
n∼10
In a supercritical reactor, the precursor fluctuations still depend on an integral of
the fission fluctuations over the last few mean precursor lifetimes. However, the
major contribution to the integral now comes from times close to the upper limit of
the integral. Thus, the precursor fluctuations tend to depend on the instantaneous
fission fluctuations. In a supercritical reactor the major source of prompt neutrons
very quickly becomes the neutron-induced fission rate. Thus, the neutron and
precursor fluctuations are governed by fluctuations in the instantaneous fission
rates, and it is plausible that these fluctuations are statistically identical.9
9 Have the same relative variances.

<!-- page 690 (PDF 707) -->
In a subcritical reactor in which the relative fission and the capture and
diffusion probabilities vary from region to region, it is reasonable to expect
the fluctuations in the neutron population to exhibit different statistical characteristics
from region to region. Similarly, when the relative absorption and
scattering probabilities and the fission spectrum differ for the various energy
groups in a subcritical reactor, the fluctuations in the neutron populations in the
different energy groups plausibly exhibit different statistical characteristics. It is
interesting that in a supercritical reactor the fluctuations in the neutron population
exhibit asymptotically the same statistical characteristics at all spatial
positions and in all energy groups.
From the numerical results, the behavior of the stochastic distribution of the
neutron and precursor populations within a reactor can be deduced. In subcritical
reactors, the stochastic neutron distribution is spatially and energy dependent,
and the stochastic precursor distribution is spatially dependent. In general, in a
subcritical reactor, the stochastic neutron distribution is more disperse than the
stochastic precursor distribution at the same spatial location.
In a supercritical reactor, the asymptotic stochastic neutron distribution is
space and energy independent and is identical to the asymptotic stochastic
precursor distribution. As a reactor is brought from a subcritical to a supercritical
configuration, the stochastic neutron distribution generally becomes less disperse
, whereas the stochastic precursor distribution becomes more disperse. The
dispersion of the asymptotic distribution in a supercritical reactor depends on the
manner in which the reactor attains its final configuration as well as on the
multiplicative properties of the initial and final configurations and the source
level. The dispersion of the asymptotic distribution is more sensitive to changes
that are made to the reactor configuration when the mean neutron and precursor
densities are small than to later changes made in the presence of larger mean
neutron and precursor densities.

### Startup Analysis

The essential problem of the analysis of a reactor startup is determination of the
probability that the actual neutron population is within a prescribed band about
the mean neutron population predicted by the deterministic kinetics equations.
As a specific example, consider a startup excursion that is terminated by a
power level trip actuating the scram mechanism. The scram is initiated at a
finite time after the trip point is reached, during which time interval the neutron
density continues to increase. If the startup procedure consists of shimming out
control rods, the principal concern is that the actual neutron population is less
than the mean population, in which case the neutron density at which the trip
point is reached occurs later, with the reactor being more supercritical and thus
on a shorter period than is predicted by the deterministic kinetics equations.
Consequently, the power excursion is more severe than would be predicted
deterministically.
Startup analyses may be separated into two phases, stochastic and deterministic
. The first phase is analyzed with stochastic kinetics, and the results are used as
initial conditions, with associated probabilities, for the second phase, which is

<!-- page 691 (PDF 708) -->
analyzed with deterministic kinetics. Feedback effects generally may be ignored
during the stochastic phase. A reasonable time to switch from the stochastic to
the deterministic phase is the time at which the neutron and precursor distributions
obtain their asymptotic shape. This time may probably be approximated by
the time at which μi and εi of Eqs. (16.277) and (16.278) attain their asymptotic
value. If the neutron and precursor distributions (i.e., P(N´t´|N ts)) were known at
the switchover time ts, the probability that the actual neutron and precursor
densities are less than some specified values could be calculated.
The asymptotic neutron and precursor distributions in a reactor with large
multiplication and no feedback can be approximated by the gamma distribution,
which is completely characterized by the mean and variance of the distribution
(i.e., by ni and μi and ci, and εi). Use of the gamma distribution is suggested
theoretically by the fact that the stationary probability distribution of a variate in a
stationary multiplicative process approaches a gamma distribution as the multiplication
increases without limit, and is justified empirically by the fact that its use
in conjunction with a point reactor kinetics model leads to results that are in
reasonable agreement with the GODIVA weak-source transient data.
The gamma distribution is
F(x)dx = rr
Γ(r) xr□1e□rxdx
(16.279)
where Γ is the gamma function, x the ratio of the actual value of the variate to the
mean value of the variate, and r the ratio of the mean value of the variate to the
square root of the variance. For example,
x = ni
ni
;
r = μ□1
i
(16.280)
for the monoenergetic model.
From Eq. (16.279), the probability that x < Δ can be computed.
Prob x < Δ
f
g = ∫
Δ
F(x)dx = 1 □ Γin(r; Δr)
Γ(r)
(16.281)
where Γin is the incomplete gamma function. This can be written entirely in terms
of tabulated functions by using certain identities,
Prob x < Δ
f
g = (Δr)re□ΔrM(1; r + 1; Δr)
rΓ(r)
(16.282)
where M is the confluent hypergeometric function.
Based on the results of the stochastic phase, initial conditions for the deterministic
phase can be assigned from
n0
i = Δni(ts);
c0
i = Δci(ts)
(16.283)

<!-- page 692 (PDF 709) -->
where ni and ci are the mean values of the neutron and precursor densities at the
switchover time, ts. For a given value of Δ, Eq. (16.282) yields the probability that
ni(ts) < Δni(ts); ci(ts) < Δci(ts).

## References

1 P. KAPS and P. RENTROP, “Generalized Runge–Kutta Methods of Order Four with
Step-Size Control for Stiff Ordinary Differential Equations,” Numer. Math. 33, 55
(1979); W. H. PRESS, S. A. TEUKOLSKY, W. T. VETTERLING, and B. P. FLANNERY,
Numerical Recipes in Fortran: The Art of Scientific Computing, 2nd Ed.,
Cambridge University Press, Cambridge (1992).
2 J. LASALLE and S. LEFSCHETZ, Stability by Lyapunov’s Direct Method, Academic
Press, New York (1961).
3 W. M. STACEY, Space-Time Nuclear Reactor Kinetics, Academic Press, New York
(1969).

## Further Readings

BELLMAN R., Dynamic Programming, Princeton University Press, Princeton, NJ (1957).
DODDS H. L., “Accuracy of the Quasistatic Method for Two-Dimensional Thermal
Reactor Transients with Feedback,” Nucl. Sci. Eng. 59, 271 (1976).
FAVORITE J. A. and STACEY W. M., “Variational Estimates of Point Kinetics
Parameters,” Nucl. Sci. Eng. 121, 353 (1995); “Variational Estimates for Use with
the Improved Quasistatic Method for Reactor Dynamics,” Nucl. Sci. Eng. 126, 282
(1997).
FEL’DBAUM A. A., Optimal Control Systems, Academic Press, New York (1965).
FERGUSON D. R.,“Multidimensional Reactor Dynamics: An Overview,” Proc. Conf.
Computation Methods in Nuclear Engineering, CONF-750413, VI, 49 (1975).
GRACE J. N., ed., “Reactor Kinetics” in Naval Reactors Physics Handbook, A.
RADKOWSKY, ed., USAEC, Washington (1964).
HENRY A. F., Nuclear Reactor Analysis, MIT Press, Cambridge, MA (1975), Chap. 7.
LEWINS J. and BABB A. L., “Optimum Nuclear Reactor Control Theory,” Adv. Nucl.
Sci. Technol. 4, 252 (1968).
MENELEY D. A. et al., “A Kinetics Model for Fast Reactor Analysis in Two
Dimensions,” in D. L. HETRICK, ed., Dynamics of Nuclear Systems, University of
Arizona Press, Tuscon, AZ (1972).
OTT K. O. and MENELEY D. A., “Accuracy of the Quasistatic Treatment of Spatial
Reactor Kinetics,” Nucl. Sci. Eng. 36, 402 (1969).
PONTRYAGIN L. S., BOLTYANSKII V. G., GAMKNELIDZE R. V., and MISHCHENKO E. F., The
Mathematical Theory of Optimum Processes, Wiley-Interscience, New York
(1962).
STACEY W. M., “Space- and Energy-Dependent Neutronics in Reactor Transient
Analysis,” Reactor Technol. 14, 169 (1971); “Xenon-Induced Spatial Power
Oscillations,” Reactor Technol. 13, 252 (1970).

<!-- page 693 (PDF 710) -->
SUTTON T. M. and AVILES B. N., “Diffusion Theory Methods for Spatial Kinetics
Calculations,” Prog. Nucl. Energy 30, 119 (1996).
WADE D. C. and RYDIN R. A., “An Experimentally Measurable Relationship between
Asymptotic Flux Tilts and Eigenvalue Separation,” in D. L. HETRICK, ed., Dynamics
of Nuclear Systems, University of Arizona Press, Tuscon, AZ (1972) p. 335.
WERNER W., “Solution Methods for the Space–Time Dependent Neutron Diffusion
Equation,” Adv. Nucl. Sci. Technol. 10, 313 (1977).

## Problems

### 16.1

Estimate the relative “tiltiness” of graphite- and H2O-moderated thermal
reactors by estimating 1 □ k1 as a function of slab reactor thickness over
the range 1 ≤ a ≤ 5 m. Calculate the associated time constant for the tilt to
take place due to delayed neutron holdback.

### 16.2

Derive the orthogonality property given by Eq. (16.11) and the relationship
of Eq. (16.12).

### 16.3

Calculate and plot the delayed neutron holdback time constant τtilt as a
function of the ratio of reactor thickness to migration area for a uniform
slab reactor.

### 16.4

Derive the point kinetics equations from the multigroup diffusion equations
. Discuss the physical significance of the point kinetics parameters.

### 16.5

Consider a uniform bare slab reactor in one group diffusion theory
(D = 1.2 cm, Σa = 0.12 cm□1, νΣf = 0.14 cm□1) that is perturbed over
the left one-half of the slab by a 1% increase in absorption cross section.
Calculate the critical slab thickness and the unperturbed flux distribution.
Calculate the generalized adjoint function of Eq. (16.36). Calculate the
first-order perturbation theory estimate, the variational estimate, and the
exact value of the reactivity worth of the perturbation.

### 16.6

Numerically integrate the point kinetics equations for the transient
ensuing from the perturbation in Problem 16.5, using the three different
reactivity estimates. Use the prompt jump approximation and one group
of delayed neutrons (λ = 0.08 s□1, β = 0.0075).

### 16.7

Derive a two-node kinetics model for the slab reactor of Problem 16.5.
Numerically integrate the kinetics equations for the transient ensuing from
the perturbation. Use the time-integrated method for the integration of one
group of delayed neutron precursors and a prompt-jump approximation.

### 16.8

Repeat Problem 16.7, but retaining the time derivative in the neutron
equations and approximating it by the θ-method. Solve the problem with
θ = 0, 0.5, and 1.

<!-- page 694 (PDF 711) -->
### 16.9

Assume that the absorption and fission cross sections in each node of
Problem 16.7 have power temperature feedback coefficients and that the
temperature in each node is determined by a balance between fission
heating and conductive cooling. Analyze the linear stability of the twonode
model as a function of the feedback coefficient values.

### 16.10

It is wished to linearly increase the power in node 1 of the reactor of
Problems 16.5 and 16.7 by 25% and in node 2 by 50% over 10 s, by
withdrawing separate control rods in nodes 1 and 2, and then to maintain
constant power. Determine the time history of the change in control rod
cross section in each node that will best approximate this desired power
trajectory. Use the prompt-jump approximation and assume one group of
delayed neutrons.

### 16.11

Construct a Lyapunov functional for the point kinetics equations with one
delayed neutron precursor group. What can you say about the stability of
these equations?

### 16.12

Consider a reactor described by the point kinetics equation with one
group of delayed neutron precursors, a conductive heat removal equation,
and a temperature coefficient of reactivity αT. Analyze the linear stability
of this reactor model.

### 16.13

Construct a Lyapunov function for the reactor model of Problem 16.12
and analyze the stability.

### 16.14

Carry through the derivation of the λ-mode linear stability criterion for
xenon spatial oscillations discussed in Section 16.6.

### 16.15

Analyze the stability with respect to xenon spatial oscillations of the
reactor of Problem 16.5 as a function of equilibrium flux level and power
feedback coefficient. Use the λ-mode stability criterion.

### 16.16

Write a two-node dynamics code for one neutron energy group and one
delayed neutron precursor group to solve for the time dependences of the
means and variances in the neutron and precursor populations in a lowsource
startup problem. Use the properties (D = 1.5 cm, Σf = 0.008 cm□1,
Σac = 0.0125 cm□1) and (D = 0.1 cm, Σf = 0.008 cm□1, Σc = 0.005 cm□1) for
two adjacent slab regions of thickness 150 cm each, the delayed neutron
parameters β = 0.0075, λ = 0.088 s□1, and the prompt neutron parameters
νp = 2:41, vp(νp □ 1) = 3:84. Calculate the startup of the reactor with a
source of S = 5 × 102 s□1 in the first regions.

### 16.17

Calculate the probability that the actual value of the neutron flux is less
than 110% of the mean value as a function of μi, the mean-squared
variance in the density to the square of the mean value of the density.
