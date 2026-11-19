# 16 Space–Time Neutron Kinetics — 16.5 Xenon Spatial Oscillations … □ Source neutron emission:
<!-- source PDF pages 684-699 -->

<!-- page 667 (PDF 684) -->
This is the extension of Pontryagin’s maximum principle to the partial differential
equation description of the reactor dynamics.
When the optimal u∗(t) is chosen, variational derivatives of the quantity within
the square brackets must vanish. This leads to the boundary conditions
Pi(ψi(R; t)) = 0
(16.182)
where Pi is the bilinear concomitant defined in Eq. (16.170), and to the equations
dψj
dt = □L+
j ψj □
X
N
i=1
ψi
@f i
@yj
+ @F
@yj
+
X
N
i=1
@F
@ _yi
@
@yj
(Liyi + f i)
"
;
j = 1; . . . ; N
(16.183)
dψN+1
dt
= □
X
N
i=1
ψi
@
@t (Liyi + f i)
(16.184)
Identities similar to those just before Eq. (16.162) have been used in arriving at
these equations. Appropriate final conditions for the ψi and ψN+1 are
ψ1(tf ) = ∙∙∙= ψN(tf ) = ψN+1(tf ) = 0
(16.185)
Theoptimalcontrol functions must be found bysolvingEqs. (16.166)and(16.182)–
(16.184). The initial conditions associated with the yi and the final conditions
associatedwith theψi andψN+1 produce a system of equationsthat must,ingeneral,
be solved iteratively. This formulation allows discontinuous control functions and
can incorporate constraints on the control functions readily, which are its principle
advantages with respect to the calculus-of-variations formulation.

## 16.5 Xenon Spatial Oscillations

Xenon-135, with a thermal absorption cross section of 2.6 × 106 barns and a halflife
against β-decay of 9.2 h, is produced by the fission product decay chain
fission(235U)
6.1%
135Te
135Xe
135I
< 1 min
β –
β –
β –
0.2%
6.7 h
9.2 h
(n,γ)
The instantaneous production rate of 135Xe depends on the 135I concentration
and hence on the local neutron flux history over the past 50 h or so. On the other

<!-- page 668 (PDF 685) -->
hand, the destruction rate of 135Xe depends on the instantaneous flux through the
neutron absorption process and on the flux history through the 135Xe decay
process. When the flux is suddenly reduced in a reactor that has been operating at
a thermal flux level >1013 n/cm2 □ s, the xenon destruction rate decreases
dramatically while the xenon production rate is initially unchanged, thus increasing
the xenon concentration. The xenon concentration passes through a maximum
and decreases to a new equilibrium value as the iodine concentration decays
away to a new equilibrium value (see Section 6.2).
When a flux tilt is introduced into a reactor, the xenon concentration will
initially increase in the region in which the flux is reduced, and initially decrease in
the region of increased flux, for similar reasons. This shift in the xenon
distribution is such as to increase (decrease) the multiplication properties of
the region in which the flux has increased (decreased), thus enhancing the flux tilt.
After a few hours the increased xenon production due to the increasing iodine
concentration in the high-flux region causes the high-flux region to have reduced
multiplicative properties, and the multiplicative properties of the low-flux region
increase due to the decreased xenon production associated with a decreasing
iodine concentration. This decreases, and may reverse, the flux tilt. In this manner
it is possible, under certain conditions, for the delayed xenon production effects to
induce growing oscillations in the spatial flux distribution. Such oscillations were
common in the large production reactors at Hanford and Savannah River, and
measures are required to control them in most thermal power reactors.
Because of the time scale of the iodine and xenon dynamics, prompt and
delayed neutron dynamics may be neglected (i.e., changes in the neutron flux are
assumed to occur instantaneously, and the delayed neutron precursors are
assumed to be always in equilibrium). Moreover, 135I can be assumed to be
formed directly from fission. The appropriate equations are
∇? Dg(r; t)∇ϕg(r; t) □ [Σg
a(r; t) + Σg
s(r; t) + σG
x X(r; t)δg;G]ϕg(r; t)
+
X
G
g´=1
Σg´!g
s
(r; t)ϕg´(r; t) + χg
p
X
G
g´=1
vΣg´
f (r; t)ϕg(r; t) = 0;
g = 1; . . . ; G
(16.186)
γi
X
G
g=1
Σg
f (r; t)ϕg(r; t) □ λiI(r; t) = _I(r; t)
(16.187)
γx
X
G
g=1
Σg
f (r; t)ϕg(r; t) + λiI(r; t) □ λxX(r; t) □ σG
x X(r; t)ϕG(r; t) = _X(r; t)
(16.188)
In writing these equations, it is assumed that the xenon absorption cross section is
zero except in the thermal group (g = G). The absorption cross section, Σg
a, does not
include xenon. The quantity σG
x is the microscopic absorption cross section of xenon

<!-- page 669 (PDF 686) -->
for thermal neutrons, γ and λ denote yields and decay constants, and I and X are the
iodine and xenon concentrations. Changes in the macroscopic cross sections and
diffusion coefficients are due to control rod motion or temperature feedback.

### Linear Stability Analysis

One of the features of Eqs. (16.186)–(16.188) that makes their solution by
analytical methods difficult is the nonlinearity introduced by the xenon absorption
term (implicit nonlinearities are also introduced by the dependence of the
cross sections on the flux via the temperature feedback). Linearizing Eqs.
(16.186)–(16.188) reduces their complexity but also reduces their applicability
to a small region about the equilibrium point. The linearized equations are used
principally for investigations of stability; that is, if a small flux tilt is introduced,
will this flux tilt oscillate spatially with an amplitude that diminishes or grows in
time?
The linearized equations are obtained by expanding about the equilibrium
point, denoted by a zero subscript
ϕg(r; t) = ϕg
0(r) + δϕg(r; t)
I(r; t)
= I0(r) + δI(r; t)
X(r; t) = X0(r) + δX(r; t)
making use of the fact that the equilibrium solutions satisfy the time-independent
version of Eqs. (16.186)–(16.188), and neglecting terms that are nonlinear in δϕg
and δX:
∇? Dg(r)∇δϕg(r; t) □ [Σg
a(r) + Σg
s(r) + σG
x (r)X0(r)δg;G]δϕg(r; t)
+
X
G
g´=1
Σg´!g
s
(r)δϕg´(r; t) □ σG
x (r)ϕG
0 (r)δX(r; t)δg;G
+ χg
p
X
G
g´=1
vΣg´
f (r)δϕg´(r; t) = 0;
g = 1; . . . ; G
(16.189)
γi
X
G
g=1
Σg
f (r)δϕg(r; t) □ λiδI(r; t) = δ _I(r; t)
(16.190)
γx
X
G
g=1
Σg
f (r)δϕg(r; t) + λiδI(r; t) □ λxδX(r; t)
□ σG
x (r)X0(r)δϕG(r; t) □ σG
x (r)ϕG
0 (r)δX(r; t) = δ _X(r; t)
(16.191)
The effect of temperature feedback has been neglected momentarily in writing
Eqs. (16.189)–(16.191), in that the time dependence of the cross sections has been
suppressed. Feedback effects will be reintroduced later.

<!-- page 670 (PDF 687) -->
Upon Laplace transforming the time dependence, Eqs. (16.189)–(16.191) become
∇? Dg(r)∇δϕg(r; p) □ [Σg
a(r) + Σg
s(r) + σG
x (r)X0(r)δg;G]δϕg(r; p)
+
X
G
g´=1
Σg´!g
s
(r)δϕg´(r; p) □ σG
x (r)ϕG
0 (r)δX(r; p)δg;G
+ χg
p
X
G
g´=1
vΣg´
f (r)δϕg´(r; p) = 0;
g = 1; . . . ; G
(16.192)
γi
X
G
g=1
Σg
f (r)δϕg(r; p) □ (p + λi)δI(r; p) = □δI(r; t = 0)
(16.193)
γx
X
G
g=1
Σg
f (r)δϕg(r; p) + λiδI(r; p) □ (p + λx + σG
x (r)ϕG
0 (r))δX(r; p)
□ σG
x (r)X0(r)δϕG(r; p) = □δX(r; t = 0)
(16.194)
Equations (16.192)–(16.194) may be written as
Hδy = δy0
(16.195)
where
δy(r; p) ≡
δϕ1(r; p)
...
δϕG(r; p)
δI(r; p)
δX(r; p)
;
δy0 ≡
..
.
□δI(r; t = 0)
□δX(r; t = 0)
and H is composed of the coefficient terms on the left side of Eqs. (16.192)–
(16.194).
The solution of Eq. (16.195) is formally
δy(r; p) = H□1(r; p)δy0(r; t = 0)
(16.196)
Thus, the solutions of Eqs. (16.192)–(16.194) are related to the initiating
perturbations by a transfer function matrix, H□1. The condition that the solutions
diminish6 in time is equivalent to the condition that the poles of the transfer
function (thus the roots of H) lie in the left-half complex plane. The roots of H are
6 The solutions of Eqs. (16.192) to (16.194) have an oscillatory time dependence if the roots of H
have an imaginary component. The requirement that these roots lie in the left-half complex plane
ensures that these solutions oscillate with a diminishing amplitude.

<!-- page 671 (PDF 688) -->
the eigenvalues, p, of Eqs. (16.192) to (16.194), with a homogeneous right-hand
side. These homogeneous equations are known as the p-mode equations. The pmode
equations generally have complex eigenfunctions and eigenvalues and must
be calculated numerically except for the simplest geometries. Numerical determination
of the p-eigenvalues requires special codes and has been successful only
for slab geometries. For practical reactor models, it is necessary to resort to
approximate methods to evaluate the p-eigenvalues. Two methods that have been
employed successfully are the μ- and λ-mode approximations.

### μ-Mode Approximation

The μ-mode approximation is motivated by recognition that the only manner in
whichEq.(16.192)differsfroma standardstaticdiffusiontheoryproblemisthrough
the additional term □σG
x ϕG
0 δX in the thermal group balance equation. Using the
homogeneous versions of Eqs. (16.193) and (16.194), this term may be written as
σG
x (r)ϕG
0 (r)δϕX(r; p) = N(r; p)ΣG
f (r)δϕG(r; p)
(16.197)
where
N(r; p) = [1 + η(r)][γxp + λi(γx + γi)]δf (r; p) □ η(r)(γx + γi)(p + λi)f 0(r)
[1 + (p=λx) + η(r)][p + λi)(1 + 1=η(r)]
(16.198)
with
η(r) ≡ σG
x (r)ϕG
0 (r)
λx
(16.199)
δf (r; p) ≡
X
G
g=1
Σg
f (r)
ΣG
f (r)
δϕg(r; p)
δϕG(r; p)
(16.200)
f 0(r) ≡
X
G
g=1
Σg
f (r)
ΣG
f (r)
ϕg
0(r)
ϕG
0 (r)
(16.201)
In applications, the quantity δf(r, p) is usually assumed equal to f0(r).
Using these definitions, the p-mode equations (homogeneous versions of
Eq. (16.192)–(16.194)) may be written in the equivalent form
∇? Dg(r)∇δϕg(r; p) □ [Σg
a(r) + Σg
s(r) + σG
x (r)X0(r)δg;G]δϕg(r; p)
+
X
G
g´=1
Σg´!g
s
(r)δϕg´(r; p) + χg
p
X
G
g´=1
vΣg´
f (r)δϕg´(r; p)
= N(r; p)ΣG
f (r)δϕg´(r; p)δg;G;
g = 1; . . . ; G
(16.202)

<!-- page 672 (PDF 689) -->
If N(r, p) is real, the term NΣG
f in Eq. (16.202) is formally like a distributed
poison, and Eq. (16.202) can be solved with standard multigroup diffusion
theory codes. In general, N(r, p) is complex because the p-eigenvalues are
complex. The essential assumption of the μ-mode approximation is that N(r, p)
is real.
There are two types of μ-mode approximations and they differ in the treatment
of the spatial dependence of N(r, p). In the first approximation, the spatial
dependence is retained explicitly and N(r; p)ΣG
f (r) is treated as a distributed
poison, in which case Eqs. (16.202) become the standard multigroup criticality
equations. A value of p is guessed, N(r, p) is evaluated, and Eqs. (16.202) are solved
for the eigenvalue k (1/k multiplies the fission term in the eigenvalue problem).
This procedure is repeated until the calculated eigenvalue agrees with the known
critical eigenvalue; the corresponding value of p is an approximation to the
p-eigenvalue with the largest real part.
An alternative μ-mode approximation (and the one that gives rise to the name
μ-mode) results when N(r, p) is assumed to be spatially independent:
N(r; p) = μ(p)
(16.203)
In this case, Eqs. (16.202) define an eigenvalue problem for the μ-eigenvalues,
which can be solved, with a slight modification to the coding, by conventional
multigroup diffusion theory codes. To obtain an estimate of the p-eigenvalue
from the calculated μ-eigenvalue requires definitions of effective values of η and f 0
that account for the spatial dependence of these quantities. In practice, an
effective η is usually defined as
η ≡ ∫dr ϕG∗
0 (r)ΣG
f (r)η(r)ϕG
0 (r)
∫dr ϕG∗
0 (r)ΣG
f (r)ϕG
0 (r)
(16.204)
an expression that can be motivated by perturbation theory. The asterisk denotes
adjoint. Temperature feedback effects are included in the calculation of
μ-eigenvalues by perturbation theory.

### λ-Mode Approximation

The λ-mode approximation begins with Eqs. (16.192)–(16.194) and expands the
spatial dependence in the eigenfunctions of the neutron balance operator at the
equilibrium point (i.e., λ-modes):
∇? Dg(r)∇ψg
n(r) □ [Σg
a(r) + Σg
s(r) + σG
x (r)X0(r)δg;G]ψg
n(r)
+
X
G
g´=1
Σg´!g
s
(r)ψg´
n (r) + 1
kn
χg
p
X
G
g´=1
vΣg´
f (r)ψg´
n (r) = 0;
g = 1; . . . ; G
(16.205)

<!-- page 673 (PDF 690) -->
normalized such that
∫dr
X
G
g´=1
χg´
p ψg´∗
m (r)
"
# X
G
g=1
vΣg
f (r)ψg
m(r)
"
= δm;n
(16.206)
where ψg∗
m satisfy equations adjoint to Eq. (16.205) with appropriate adjoint
boundary conditions. It is convenient to treat thermal feedback explicitly in this
approximation by including a power feedback term
+αδf (r)ΣG
f (r)δϕG(r; p)ϕG
0 (r)
on the left side of Eq. (16.192) for group G.
When the iodine is eliminated between Eqs. (16.193) and (16.194), and the flux
and xenon are expanded in λ-modes,
δϕg(r; p) =
X
N
n=1
An(p)ψg
n(r);
g = 1; . . . ; G
(16.207)
δX(r; p) =
X
N
n=1
Bn(p)ΣG
f (r)ψG
n (r)
(16.208)
the biorthogonality relation of Eq. (16.206) may be used to reduce Eqs. (16.192)–
(16.194) to a set of 2N algebraic equations in the unknowns An and Bn, with
inhomogeneous terms involving spatial integrals containing δX(r, t = 0) and
δI(r, t = 0). These equations may be written as a transfer function relation
between the inhomogeneous terms R and the column vector A(p) containing
the An and Bn:
A(p) = ^H(p) ? R
(16.209)
Again, the condition for stability is that the poles of ^H lie in the left-half
complex p-plane. When N = 1 in the expansion of Eqs. (16.207) and (16.208),
Eq. (16.209) may be reduced to the scalar relation
A1(p) = ^H
´(p) ? R
(16.210)
where
^H
´(p) = [(p □ p1)(p □ p2)]□1
(16.211)

<!-- page 674 (PDF 691) -->
and
p1 = □pr + i(c □ p2
r)1=2
p2 = □pr □ i(c □ p2
r)1=2
(16.212)
with
pr = λx
1 + λi
λx
+ η

□ η
Ω
(γi + γx)η
1 + β
□ γx

c = λiλx (1 + η) + η(γi + γx)
Ω
1 □
η
1 + β

The parameters η, Ω, and β, which characterize the reactor in this formulation,
are defined as
η ≡ 1
λx
∫dr ψG−
1 (r)σG
x (r)ΣG
f (r)ϕG
0 (r)ψG
1 (r)
∫dr ψG−
1 (r)ΣG
f (r)ψG
1 (r)
(16.213)
Ω ≡
1=k1 □ 1=k0
δf ∫dr ψG−
1 (r)ΣG
f (r)ψG
1 (r)
□ ∫dr ψG−
1 (r)α(r)ΣG
f (r)ϕG
0 (r)ψG
1 (r)
∫dr ψG−
1 (r)ΣG
f (r)ψG
1 (r)
(16.214)
β ≡
δf (γi + γx)∫dr ψG−
f (r)ΣG
f (r)ϕG
0 (r)ψG
1 (r)
∫dr ψG∗
1 (r)λxX0(r)ψG
1 (r)
□ 1
(16.215)
The quantity δf was defined previously as the ratio of the total fission rate to the
thermal group fission rate and an effective spatially independent value has been
assumed. The fundamental and first harmonic λ-eigenvalues are denoted by k0
and k1, respectively.
The requirement that the poles of ^H
´(p) lie in the left-half complex p-plane (i.e.,
that pr > 0) defines a relationship among η, Ω, and β. In practice, β ' η has been
found to be a good approximation, so that the stability requirement defines a
curve in the η–Ω phase plane, as shown in Fig. 16.1.
The effect of physical parameters upon xenon spatial stability can be traced
through Eqs. (16.213) and (16.214) and Fig. 16.1. The quantity Ω is primarily
determined by the eigenvalue separation 1/k1 □ 1/k0. A reactor becomes less
stable when the eigenvalue separation decreases, which occurs when the dimensions
are increased, when the migration length is decreased, or when the power
distribution is flattened. A negative power coefficient (α < 0) increases Ω, thus

<!-- page 675 (PDF 692) -->
making a reactor more stable. The quantity η is proportional to the thermal flux
level, ϕG
0 . An increase in thermal flux level is generally destabilizing (increasing η),
but may be stabilizing if α < 0 (increasing Ω); that is, for α < 0, an increase in
thermal flux moves the point characterizing a given reactor in Fig. 16.1 to the right
and up. It is interesting that an increase in thermal flux level can, under some
circumstances, be stabilizing, although this is not generally the case.
If Ω > γi, Fig. 16.1 predicts stability independent of the value of η. Physically, Ω is a
measure of the reactivity required to excite the first harmonic λ-mode in the
presence of power feedback, and γi is a measure of the maximum reactivity that can
be introduced by iodine decay into xenon. The parameters η and Ω can be evaluated
using standard multigroup diffusion theory codes. A fundamental λ-mode flux and
first harmonic λ-mode flux and adjoint calculations are required. The integrals in
Eqs. (16.213) and (16.214) may be performed with any code that computes
perturbation theory-type integrals. Computation of first harmonic flux and adjoint
requires that either the problem is symmetric so that zero flux boundary conditions
may be located on node lines or that the Wielandt iteration scheme be employed.
Several comparisons with experiment and numerical simulation are indicated in
Fig. 16.1. The location of the symbol indicates the prediction of the stability
criterion, and the type symbol indicates the experimental or numerical result.
At 900 effective full power hours (EFPH), Core 1 Seed 1 of the Shippingport
reactor experienced planar xenon oscillations with a doubling time of 30 h. Using
this doubling time and the calculated value for η, an experimental Ω may be
inferred that agrees with the calculated Ω to within 3%. Core 1 Seed 4 of the
Shippingport reactor was observed to be quite unstable at 893 EFPH, and to be
slightly unstable at 1397 EFPH. These observations are consistent with the
predictions of the stability criterion at 1050 EFPH.
0.05
0.04
0.03
0.02
0.01
Core 1,
Speed 4,
1050 EFPH
Core 1, Seed 1, 900 EFPH
Unstable
Stable
x
x
x
x
Ω
η
Fig. 16.1 λ-mode linear xenon stability criterion. PWR results: open square: calculated with
feedback; solid square: calculated, no feedback; open triangle: inferred from experiment.
Calculated transients: open circle: decaying oscillation; cross: neutral oscillation; solid circle:
growing oscillation. (With permission from Ref. [3]. Copyright 1969, Academic Press.)

<!-- page 676 (PDF 693) -->
The finite-difference approximations to Eqs. (16.186)–(16.188) were solved
numerically for a variety of two-dimensional three-group reactor models. These
same reactor models were evaluated for stability with the λ-mode stability
criterion. The results depicted in Fig. 16.1 indicate that the predictions of the
stability criterion were generally reliable.
Intheanalysisofthissection,thetotalpowerwasassumedtobeheldconstantand
the effects of nonlinearities and control rod motion on the stability were neglected.
Although the effects of xenon dynamics upon the total power in an uncontrolled
reactor can be evaluated, most reactors can be controlled to yield a constant power
output. The treatment of nonlinearities and control rod motion is discussed next.

### Nonlinear Stability Criterion

The extended methods of Lyapunov, which were discussed in Section 16.4, are
applied to derive a stability criterion that includes the nonlinear terms that were
neglected in the preceding section. Employing a one-group neutronics model and
retaining the prompt neutron dynamics and expanding the flux, iodine, and
xenon about their equilibrium states, the equations governing the reactor
dynamics may be written in matrix form as
_y(r; t) = L(r)y(r; t) + g(r; t)
(16.216)
where
y(r; t) ≡
δϕ(r; t)
δX(r; t)
δI(r; t)
7775;
g(r; t) ≡ □
vσxδXδϕ + αvΣf (δϕ)2
σxδXδϕ
L(r)
≡
(v∇? D∇□ vΣa + +vvΣf □ vσxX0 □ αvΣf ϕ0)
□vσxϕ0
γxΣf □ σxX0
□(λx + σxϕ0)
λi
γiΣf
□λi
(16.217)
where v is the neutron speed, α is the power feedback coefficient, and the other
notation is as defined previously.
A Lyapunov functional may be chosen as
V y[ ] = 1
2 ∫R
dr yT(r; t)y(r; t)
(16.218)
The condition for stability (asymptotic stability) in the sense of Lyapunov is that _V
evaluated along the system trajectory defined by Eq. (16.216) is negative semidefinite
(definite).

<!-- page 677 (PDF 694) -->
V_ = 1
2 ∫R
dr _yTy + yT _y

= 1
2 ∫R
dr yT(L∗+ L)y + ∫R
dr gTy
≤ □μ∫R
dr yTy +
∫R
dr gTg

1=2
∫R
dr yTy

1=2
(16.219)
where μ is the smallest eigenvalue of
2 (L∗+ L)φn = □μnφn
(16.220)
Thus, the condition for stability is
μ □
∫R
dr gTg

1=2
∫R
dr yTy

1=2
(16.221)
For a given reactor model and equilibrium state, characterized by μ, relation
(16.221) defines the domain of perturbations for which a stable response will be
obtained. For asymptotic stability, the inequality must obtain in relation (16.221).
The linear eigenvalue problem, Eq. (16.220), which must be solved for μ,
involves the matrix L of Eq. (16.217) and its Hermitean adjoint L∗. The matrix
operator 1
2 (L∗+ L) is self-adjoint with a spectrum of real eigenvalues and a
complete set of orthogonal eigenfunctions.
The foregoing choice of Lyapunov functional is not unique. As a consequence,
this type of analysis provides sufficient, but not necessary, conditions for stability.

### Control of Xenon Spatial Power Oscillations

Inclusion of the control system in a stability analysis is difficult primarily because of
the difficulty encountered in analytically representing the motion of discrete control
rods required to maintain criticality. Control rod motion has a profound effect on the
transient response to a perturbation in the equilibrium state in many cases, however,
and neglect of this effect may invalidate the stability analysis completely.

### Variational Control Theory of Xenon Spatial Oscillations

When the spatial dependence is represented by the nodal approximation, a
general optimality functional may be written (for a M-node model)
J[ϕ1; . . . ; ϕM; u1; . . . ; uM] =
X
M
m=1 ∫
tf
t0
dtf[ϕm(t) □ Nm(t)]2 + Ku2
m(t)g
(16.222)

<!-- page 678 (PDF 695) -->
where ϕm and Nm represent the actual and the desired, respectively, timedependent
fluxes in node m, um is the control in node m, and K is a constant
that can be varied to influence the relative importance of the two types of terms in
the optimality functional. The purpose of the control program is to find the um(t)
that minimizes the optimality functional, subject to the constraints that the
reactor remain critical,
0 =
X
M
m´ ≠m
Imm´[ϕm´(t) □ ϕm(t)] + [vΣf m □ Σam □ σxXm(t) □ um(t)]ϕm(t)
= f 1m
(16.223)
and the iodine and xenon dynamics equations are satisfied,
_Im(t) = γiΣf mϕm(t) □ λiIm(t) = f 2m;
Im(0) = Im0
(16.224)
_Xm(t) = γxΣf mϕm(t) + λmIm(t) □ [λx + σxϕm(t)]Xm(t) = f 3m
Xm(0) = Xm0;
m = 1; . . . ; M
(16.225)
The m subscript denotes node m and Imm´ is the internodal coupling coefficient of
the type discussed in Sections 15.2 and 15.3.
Equations (16.148) become
0 = 2[ϕm(t) □ Nm(t)] □ [vΣf m □ Σam □ σxXm(t) □ um(t)]ω1m(t)
+
X
M
m´ ≠m
Imm´[ω1m(t) □ ω1m´(t)] □ γiΣf m(t)ω2m(t)
□[γxΣf m □ σxXm(t)]ω3m(t)
(16.226)
_ω2m(t) = λi[ω2m(t) □ ω3m(t)]
(16.227)
_ω3m(t) = σxϕm(t)ω1m(t) + [λx + σxϕm(t)]ω3m(t);
m = 1; . . . ; M
(16.228)
(The symbol ω has been used to denote the Lagrange multipliers, since λ is
conventionally used to represent the decay constants.) The final conditions
corresponding to Eqs. (16.150) are
ω2m(tf ) = 0;
ω3m(tf ) = 0;
m = 1; . . . ; M
(16.229)
Equations (16.149) are modified somewhat in this case because the optimality
functional depends on the control. The more general relation is
@F
@ur
+
X
N
i=1
λi(t) @f i
@ur
(y; u) = 0;
r = 1; . . . ; R
(16.230)

<!-- page 679 (PDF 696) -->
that becomes
2Kum(t) + ω1m(t)ϕm(t) = 0;
m = 1; . . . ; M
(16.231)
Equations (16.231) can be used to eliminate the um from Eqs. (16.223) and
(16.226). The modified equations, plus Eqs. (16.224), (16.225), (16.227), and
(16.228), constitute a set of 6M equations which, together with the initial and final
conditions specified above, can be solved for the optimal flux, iodine, xenon, and
Lagrange multiplier trajectories. The optimal control can then be determined
from Eqs. (16.231).
If no approximation is made for the spatial dependence, an equivalent
optimality functional is
J[ϕ; u] = ∫V
dr∫
tf
t0
dt[(ϕ(r; t) □ N(r; t))2 + Ku2(r; t)]
(16.232)
and the constraints are
0 = ∇? D(r)∇ϕ(r; t) + [vΣf (r) □ Σa(r) □ σxX(r; t) □ u(r; t)]ϕ(r; t) = f 1
(16.233)
_I(r; t) = γiΣf (r)ϕ(r; t) □ λiI(r; t) = f 2;
I(r; 0) = I0(r)
(16.234)
_X(r; t) = γxΣf (r)ϕ(r; t) + λiI(r; t) □ [λx + σxϕ(r; t)]X(r; t) = f 3
X(r; 0) = X0(r)
(16.235)
Equations (16.171) become
0 = 2[ϕ(r; t) □ N(r; t)] □ ∇? D(r)∇ω1(r; t)
□[vΣf (r) □ Σa(r) □ σxX(r; t) □ u(r; t)]ω1(r; t)
□γiΣf (r)ω2(r; t) □ [γxΣf (r) □ σxX(r; t)]ω3(r; t)
(16.236)
_ω2(r; t) = λi[ω2(r; t) □ ω3(r; t)]
(16.237)
_ω3(r; t) = σxϕ(r; t)ω1(r; t) + [λx + σxϕ(r; t)]ω3(r; t)
(16.238)
The final conditions of Eqs. (16.172) are
_ω2(r; tf ) = ω3(r; tf ) = 0
(16.239)
and the boundary condition of Eq. (16.173) is
ω1(R; t) = 0
(16.240)

<!-- page 680 (PDF 697) -->
Because the optimality functional contains the control functions, Eqs. (16.174)
must be modified to
@F
@ur
+
X
N
i=1
λi(r; t) @f i
@ur
(y; u) = 0
(16.241)
that becomes
2Ku(r; t) + ω1(r; t)ϕ(r; t) = 0
(16.242)

## 16.6 Stochastic Kinetics

The evolution of the state of a nuclear reactor is essentially a stochastic process
and should, in general, be described mathematically by a set of stochastic kinetics
equations. For most problems in reactor physics it suffices to describe the mean
value of the state variables in a deterministic manner and to ignore the stochastic
aspects. However, the stochastic features of the state variables are important in
the analysis of reactor startups in the presence of a weak source and underlie some
experimental techniques, such as the measurement of the dispersion of the
number of neutrons born in fission, the Rossi-α measurement, and the measurement
and interpretation of reactor noise. The purpose of this section is to present
a computationally tractable formalism for the calculation of stochastic phenomena
in a space- and energy-dependent time-varying zero-power reactor
model.

### Forward Stochastic Model

The spatial domain of a reactor may be partitioned into I space cells, and the
energy range of interest may be partitioned into G energy cells. Subject to this
partitioning, the state of the reactor is defined by the set of numbers
N ≡ fnigcimg;
i = 1; . . . ; I; g = 1; . . . ; G; m = 1; . . . ; M
where nig is the number of neutrons in space cell i and energy cell g, and cim is the
number of m-type delayed neutron precursors in space cell i.
Define the transition probability P(N´t´|Nt) that a reactor that was in state N´ at
time t´ will be in state N at time t. The probability generating function for this
transition probability is defined by the relation
G(N´t´jUt) ≡
X
N
P(N´t´jNt) ∏
igm
u
nig
ig υcim
im
(16.243)
The summation over N implies a summation over all values of nig and cim for all i,
g, and m. The quantities uig and vim play the role of transform variables.

<!-- page 681 (PDF 698) -->
The transition probability will be written as
P(N´t´jNt) =
∏
ig
Pig(N´t´jnigt)
"
∏
im
^Pim(N´t´jCimt)

(16.244)
for mnemonic reasons. This formalism does not denote product probabilities and
is used only to facilitate the distinction between states that differ only by the
number of neutrons in one space-energy cell or the number of m-type precursors
in one space cell.
Some properties of the probability generating function that will be needed in
the subsequent analysis are:
G(N´t´jUt)U=1 =
X
N
P(N´t´jNt) ≡ 1
(16.245)
@G
@uig
(N´t´jUt)jU=1 =
X
N
nigP(N´t´jNt) ≡ nig(t)
(16.246)
@G
@υim
(N´t´jUt)jU=1 =
X
N
cimP(N´t´jNt) ≡ cim(t)
(16.247)
W ig;i´g´(t) ≡ @2G(N´t´jUt)
@uig@ui´g´
U=1
=
nig(t)(nig(t) □ 1); ig = i´g´
nig(t)ni´g´(t);
ig ≠i´g
<
:
(16.248)
Y im;i´g´(t) ≡ @2G(N´t´jUt)
@υim@ui´g´
U=1
= ni´g´(t)cim(t)
(16.249)
Zim;i´m´(t) ≡ @2G(N´t´jUt)
@υim@υi´m´
U=1
=
cim(t)(cim(t) □ 1); im = i´m´
cim(t)ci´m´(t);
im ≠i´m´
<
:
(16.250)
The notation U = 1 indicates that the expression is evaluated for all uig and uim
equal to unity. The overbar denotes an expectation value, as defined explicitly in
Eqs. (16.246) and (16.247). In the foregoing equations and in the subsequent
development, the dependence of the expectation values at time t on the state of
the reactor at time t´ is implicit. By considering the events that could alter the state
of the reactor during the time interval t →t + Δt, balance equations for the
transition probability and the probability generating function may be derived. In
the limit Δt →0, the probability of more than one event occurring during Δt
becomes negligible, and the balance equations can be constructed by summing
over all single event probabilities.

<!-- page 682 (PDF 699) -->
## □ Source neutron emission:

@P
@t
s
= P
ig Sig[Pig(nig □ 1) □ Pig(nig)] ∏´Pi´g´

∏^Pi´m´

@G
@t
s
= P
ig Sig[uig □ 1]G

## □ Capture event (includes capture by detectors):

@P
@t
c
= P
ig Λcig[(nig + 1)Pig(nig + 1) □ nigPig(nig)] ∏´Pi´g´

∏^Pi´m´

@G
@t
c
= P
ig Λcig 1 □ uig

 @G
@uig

## □ Transport event:

@P
@t
T
= P
ig
P
i´ lg
ii´[(nig + 1)Pig(nig + 1)Pi´g(ni´g □ 1)
□ nigPig(nig)Pi´g(ni´g)] ∏´Pi´´g´´

∏^Pi´´m

@G
@t
T
= P
ig
P
i´ lg
ii´ ui´g □ uig

 @G
@uig

## □ Scattering event:

@P
@t
s
= P
ig Λsig (nig + 1)Pig(nig + 1) P
g´ Kgg´
i Pig(nig´ □ 1) ∏´Pi´´g´´

h
□ nigPig(nig) ∏´Pi´g´

∏^Pi´m´

@G
@t
s
= P
ig Λsig
P
g´ K gg´
i uig´ □ uig
h
i @G
@uig

## □ Delayed neutron emission:

@P
@t
d
= P
im λm (cim + 1)^Pim(cim + 1) P
g χg
mPig(nig □ 1) ∏´Pi´g´

h
□ cim^Pim(cim) ∏´Pi´g´

∏^Pi´m´

@G
@t
d
= P
im λm
P
g χg
muig □ υim
h
i @G
@υim
