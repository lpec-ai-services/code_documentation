# 16 Space–Time Neutron Kinetics — 16.1 Flux Tilts and Delayed Neutron Holdback … 16.2 Spatially Dependent Point Kinetics
<!-- source PDF pages 640-651 -->

<!-- page 623 (PDF 640) -->
# 16 Space–Time Neutron Kinetics

The discussion of reactor dynamics in Chapter 5 was based on the implicit
assumption that the spatial neutron distribution remained fixed and only the total
neutron population changed in time. However, when a critical reactor is perturbed
locally, the spatial neutron flux distribution, as well as the total neutron population,
willchange,andthechange inthespatialfluxdistributionwillaffectthe changeinthe
total neutron population. A very local perturbation (e.g., the withdrawal of a control
rod) will obviously affect the neutron flux in the immediate vicinity of the perturbation
. However, a local or regional perturbation can also affect the global neutron flux
distribution (i.e., produce a flux tilt), which will, in turn, alter the reactivity and affect
the global neutron population. Moreover, for a transient below prompt critical, the
largest part of the neutron source is due to the decay of delayed neutron precursors,
which tends to hold back a flux tilt until the delayed neutron precursor distribution
also tilts. The point kinetics equations discussed in Chapter 5 can be extended to
treat flux tilts and delayedneutronholdback effectsbyrecomputing the point kinetic
parameters during the course of a transient. The various methods that have been
discussed for calculating the spatial distribution of the neutron flux can also be
extended to calculate the space- and time-varying neutron flux distribution by
adding neutron density time derivative and delayed neutron precursor source terms
and appending a set of equations to calculate local delayed neutron precursor
densities. The methods of stability analysis and control can also be extended to
include spatial dependence, as illustrated by an analysis of xenon spatial oscillations.

## 16.1 Flux Tilts and Delayed Neutron Holdback

Physical insight into the flux tilting and delayed neutron holdback phenomena
can be obtained by considering a step local perturbation in the material composition
of an initially critical reactor. In multigroup diffusion theory, the initial
critical state of the reactor is described by
□∇? Dg(r; t)∇ϕg(r; t) + Σg
t (r; t)ϕg(r; t) □
X
G
g´=1
Σg´!g(r; t)ϕg´(r; t)
= χgX
G
g´=1
vΣg´
f (r; t)ϕg0(r; t);
g = 1; . . . ; G
(16.1)
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 624 (PDF 641) -->
which will be written in operator notation as
A0ϕ0 = M0ϕ0
(16.2)
where the zero subscript is used to indicate the initial critical state.
Now we consider a spatially nonuniform change in materials properties which
is represented by the changes ΔA in the destruction operator and ΔM in the
fission operator so that A0 →A = A0 + ΔA and M0 →M = M0 + ΔM. For changes
producing reactivities well below prompt critical, the prompt jump approximation
may be used to describe the neutron kinetics. Making the further approximation
of a single delayed neutron precursor group, the neutron kinetics is
described by
0 = (□A + f1 □ β)M)ϕ + λC
(16.3)
_C = βMϕ □ λC
(16.4)
Expanding about the initial critical distributions
ϕ(r; t) = ϕ0(r) + Δϕ(r; t)
(16.5)
C(r; t) = C0(r) + ΔC(r; t) ≡ βM0ϕ0
λ
+ ΔC
(16.6)
linearizing (i.e., ignoring quadratic terms ΔM Δϕ, etc.), Laplace transforming, and
combining the two equations results in an equation for the time dependence of
the neutron flux Δϕ in the frequency domain:
0 =
□A0 +
1 □ sβ
s + λ

M0

Δ ~ϕ(r; s) + 1
s □ΔA +
1 □ sβ
s + λ

ΔM

ϕ0
(16.7)

### Modal Eigenfunction Expansion

We now expand the time-dependent flux,
Δϕ(r; t) =
X
n=0
an(t)ψn(r)
(16.8)
where the ψn are the spatial eigenfunctions of the initial critical reactor and satisfy
A0ψn = 1
kn
M0ψn
(16.9)

<!-- page 625 (PDF 642) -->
(e.g., in a uniform slab reactor of width a, ψn = sin(nπ x/a)). The corresponding
adjoint eigenfunctions of the initial critical reactor are defined by
A∗
0ψ∗
n = 1
kn
M∗
0ψ∗
n
(16.10)
From the definition of the adjoint operator discussed in Chapter 13, the
orthogonality property
hψ∗
m; M0ψni = δmn
(16.11)
the relationship
hψ∗
m; A0ψni = 1
kn
hψ∗
m; M0; ψni
(16.12)
can be established, where hXXi indicates integration over space and summation
over groups.
Using the eigenfunction expansion of Eq. (16.8) in Eq. (16.7), multiplying the
resulting equation by ψ∗
m, integrating over space and summing over groups, and
using Eqs. (16.11) and (16.12) yields
~am(s) =
(s + λ)hψ∗
m; (□ΔA + (1 □ sβ
s + λ)ΔM)ϕ0i
s (s + λ)
1 □ km
1 □ (1 □ β)km
!
"
1 □ (1 □ β)km
km

hψ∗
m; M0ψmi
(16.13)
which may be inverse Laplace transformed to obtain
am(t) = ρmkm
1 □ km
1 □
βkm
1 □ (1 □ β)km
exp
□λ(1 □ km)t
1 □ (1 □ β)km

□
βkmhψ∗
m; ΔMϕ0i
[1 □ (1 □ β)km]hψ∗
m; M0ψmi exp
□λ(1 □ km)t
1 □ (1 □ β)km

(16.14)
where
ρm ≡ hψ∗
m; (□ΔA + M)ϕ0i
hψ∗
m; M0ψmi
(16.15)
is the mth-mode reactivity.

### Flux Tilts

If ρm ≠0, a nonuniform perturbation in materials properties in a critical reactor
will introduce higher harmonic eigenfunctions into the flux distribution, which

<!-- page 626 (PDF 643) -->
becomes after the transient terms in Eq. (16.14) have died out becomes
ϕ(r; 1) = 1 + a0(1)
[
]ϕ0(r) +
X
n=1
ρnkn
1 □ kn
ψn(r)
(16.16)
For a uniform slab reactor in 1 1
2-group diffusion theory, the results of Chapter 3
can be used to write the nth-mode eigenvalue:
kn =
k1
1 + M2B2
n
=
k1
1 + M2[(n + 1)π=a]2 =
1 + M2(π=a)2
1 + M2[(n + 1)π=a]2
(16.17)
where M2 is now the migration area and we have taken advantage of the fact that
k0 = 1 to write the last form of the equation.
The amplitude of the first harmonic eigenfunction, which would be the main
component of a flux tilt, depends on the magnitude of the first harmonic
reactivity, ρ1, and on the first harmonic eigenvalue separation, 1 □ k1 (note that
k0 = 1). Using Eq. (16.17), the 1 1
2-group diffusion theory estimate for the first
harmonic eigenvalue separation of a uniform slab reactor is
1 □ k1 =
3(Mπ=a)2
1 + (2Mπ=a)2 ≈ 3 Mπ
a

(16.18)
Thus, reactors that are very large in units of migration length (a/M ≫1) will have
a small first harmonic eigenvalue separation and will be very “tilty.”

### Delayed Neutron Holdback

As indicated by Eq. (16.14), a tilt will not occur instantaneously upon the
introduction of a nonuniform step change in materials properties into a critical
reactor, but will gradually build in over a time t ≈ 2 to 3τtilt, where
τtilt = 1 □ (1 □ β)k1
λ(1 □ k1)
> λ□1
(16.19)
Physically, the prompt neutrons respond essentially instantaneously (on the
neutron lifetime scale) to the change in materials properties, but the delayed
neutron source only gradually changes from the initial fundamental mode
distribution into the asymptotic distribution.

## 16.2 Spatially Dependent Point Kinetics

The multigroup diffusion theory approximation for the space and time
dependence of the neutron flux within a nuclear reactor is described by the

<!-- page 627 (PDF 644) -->
set of G equations
vg
@ϕg(r; t)
@t
= ∇? Dg(r; t)∇ϕg(r; t) □ Σg
t (r; t)ϕg(r; t)
+
X
G
g´=1
Σg´!g(r; t)ϕg´(r; t)
+ λ0(1 □ β) χg
p
X
G
g´=1
vΣg´
f (r; t)ϕg´(r; t)
+
X
M
m=1
λmχg
mCm(r; t);
g = 1; . . . ; G
(16.20a)
which for notational convenience we shall write in operator notation as
v
@ϕ(r; t)
@t
= □ A(r; t)ϕ(r; t) + λ0(1 □ β)Fp(r; t)ϕ(r; t)
+
X
M
m=1
λmCm(r; t)
(16.20b)
The space and time dependence of the M groups of delayed neutron precursors
are described by
@Cm(r; t)
@t
= λ0βm
X
G
g=1
vΣg
f (r; t)ϕg(r; t) □ λmCm(r; t)
(16.21a)
which in operator notation becomes
@Cm(r; t)
@t
= λ0βmF(r; t)ϕ(r; t) □ λmCm(r; t);
m = 1; . . . ; M
(16.21b)
where
A, F = loss and production operator, respectively
ϕ(r, t) = neutron flux
Cm (r, t) = precursor density of type m
v = neutron speed
χm, λm, βm = fission spectrum, decay constant, and delayed neutron fraction,
respectively, for precursor type m
Fp ≡ χpF = fission source for prompt neutrons (χp is the fission spectrum
for prompt neutrons; Fm ≡ χmF will be the fission source for
delayed neutrons from precursor group m in subsequent
equations)
λ0 = eigenvalue adjusted to render the system critical at time t = 0.

<!-- page 628 (PDF 645) -->
In the development of the formalism of reactor physics over the years by
many different people it is inevitable that the same symbol has been used by
different people for different quantities. This presents the quandary of whether
to introduce new and unfamiliar symbols or to stick with the familiar symbols
even though it sometimes results in the confusing situation of the same symbol
being used for different quantities on the same page. I have opted for using the
familiar symbols. This is particularly a problem for spatially dependent kinetics
in which the symbol λ is used for the radioactive decay constant (e.g., in
Table 5.1, Eqs. (6.1), (16.4), and (16.19) and following equations), for the inverse
eigenvalue λ = 1=k of the spatial neutron balance equation (e.g., in Eqs. (13.23)
and (16.22) and following equations), and as a Lagrange multiplier in Eq.
(16.168) and following equations. Hopefully, the meaning of the symbol is clear
from the context.
In the multigroup form of Eqs. (16.20a) and (16.21a), ϕ(r, t) represents a
column vector of group fluxes, and A and F are matrices.
For the initial, static configuration, these equations reduce to
(A0 □ λ0F0)ϕ0 = 0
(16.22)
For the perturbed static configuration (i.e., after the delayed neutrons reach
equilibrium), these equations reduce to
(Ae □ λeFe)ϕe = 0
(16.23)
and the quantity □Δλ = λ0 □ λe = (ke □ k0)/kek0 is called the static reactivity worth
of the perturbation (k = λ□1). (Note that because Eq. (16.23) is an eigenvalue
problem, the word static here refers only to the flux distribution, not the
amplitude.) The static reactivity worth of the perturbation is
ρe ≡ □Δλ = hϕ∗
0; (λ0Δ F □ Δ A)ϕei
hϕ∗
0; Fϕei
(16.24)
where the static flux adjoint function ϕ∗
0 satisfies
(A∗
0 □ λ0F∗
0)ϕ∗
0 = 0
(16.25)
(The inner product notation h,i indicates an integration over volume and a sum
over energy groups.)

### Derivation of Point Kinetics Equations

The exact space–time equations are reduced to the point reactor kinetics model
by writing the flux as a product of a shape function and an amplitude function;
that is,
ϕ(r; t) = ψ(r; t)n(t)
(16.26)

<!-- page 629 (PDF 646) -->
The point kinetics equations are derived by weighting Eqs. (16.20) and (16.21)
with the static adjoint flux and integrating over volume and summing over energy:
_n(t) = ρ(t) □ β(t)
Λ(t)
n(t) +
X
M
m=1
λm Pm(t)
(16.27)
_Pm(t) = βmγm(t)
Λ(t)
n(t) □ λmPm(t);
m = 1; . . . ; M
(16.28)
where the dynamic reactivity, prompt neutron generation time, and delayed
neutron effectiveness are defined as
ρ(t) = hϕ∗
0; (λ0ΔF □ ΔAiψ(r; t)i
hϕ∗
0; Fψ(r; t)i
= ∫dr
X
G
g=1
ϕg∗
0 (r)χg
p
λ0 □
X
G
g´=1
∇(vΣg´
f (r; t)ψg´(r; t)
(
)
"
□
(
□ ∇? ΔDg(r; t)∇ψg(r; t) + Δ Σg
t (r; t)ψg(r; t)
□
X
G
g´=1
∇Σg´!g(r; t)ψg´(r; t)
)#,
∫dr
X
G
g=1
ϕg∗
0 (r)χg
p
X
G
g´=1
vΣg´
f (r; t)ψg´(r; t)
(16.29)
Λ□1(t) = hϕ∗
0; Fψ(r; t)i
hϕ∗
0; v□1ψ(r; t)i
= ∫dr PG
g=1 ϕg∗
0 (r)χg
p
PG
g´=1 vΣg´
f (r; t)ψg´(r; t)
∫dr PG
g=1 ϕg∗
0 (r)(1=vg)ψg(r; t)
(16.30)
and
γm(t) = hϕ∗
0; Fmψ(r; t)i
hϕ∗
0; Fψ(r; t)i = ∫dr PG
g=1 ϕg∗
0 (r)χg
m
PG
g´=1 vΣg´
f (r; t)ψg´(r; t)
∫dr PG
g=1 ϕg∗
0 (r)χg
p
PG
g=1 Σg´
f (r; t)ψg´(r; t)
(16.31)
respectively (β = γ1β1 + ∙∙∙+ γMβM; ΔA = A □ A0; and ΔF = F □ F0). In principle
, the point kinetics equations can be used to calculate the exact space–time
neutron flux, if the correct spatial flux shape is used at all times to evaluate the
parameters defined by Eqs. (16.29)–(16.31). Note that these parameters do not
depend on the amplitude of the flux, only the flux distribution.

<!-- page 630 (PDF 647) -->
In a large LWR core, the flux is slow to reach equilibrium in its perturbed static
distribution, due to the holdback effect of the delayed neutrons. Thus, for the first
few seconds after a perturbation, the time-dependent flux shape ψ(r, t) differs
from the static perturbed flux shape ϕe, and the dynamic reactivity of Eq. (16.29)
differs from the static reactivity of Eq. (16.24).
In the standard implementation of the point kinetics method, the parameters
are estimated using the initial static flux distribution ϕ0. This approximation
corresponds to first-order perturbation theory, and for the reactivity, it is
denoted
ρ0 = hϕ∗
0; (λ0ΔF □ ΔA)ϕ0i
hϕ∗
0; Fϕ0i
(16.32)
This expression can be shown (Chapter 13) to be a first-order approximation of
the static reactivity (i.e., ρ0 is an estimate of the difference (□Δλ = λ0 □ λe) of
reciprocal eigenvalues for the initial and perturbed core static configurations
that is accurate to first order in the flux perturbation Δϕ = ϕe □ ϕ0 (i.e., error ∼
Δϕ)).

### Adiabatic and Quasistatic Methods

If parameters of Eqs. (16.29)–(16.31) calculated with the initial spatial flux shape
are used throughout the transient calculation, the result is the standard point
kinetics approximation of Chapter 5. If the parameters are recomputed at selected
times during the transient, using a static neutron flux solution corresponding to
the instantaneous conditions of the reactor, the result is an improvement to the
standard point kinetics known as the adiabatic method.
In the quasistatic (QS) method, the point kinetics equations are used for the
flux amplitude, but the flux shape is recomputed (at time steps t = tn) using
A□λ0(1□β)Fp +1
v
_n
n+ 1
Δtn

tn
Sn =
vΔtn
Sn□1 +
n(tn)
X
M
m=1
χmλmCm(r;tn)
(16.33)
where Δtn = tn □ tn□1 is the shape time step. (The precursor density is computed
directly from the flux history.) When the flux shape from the nth such
recalculation Sn is used directly to estimate the reactivity using the inner product
definition (Eq. (16.29)), the result is
ρn(t) ≡ hϕ∗
0; (λ0ΔF □ ΔA)Sni
hϕ∗
0; FSni
(16.34)
a potentially accurate estimate of the dynamic reactivity, depending, of course, on
the accuracy of the flux calculation. It is more accurate to use a flux shape
interpolated from the most recent known shape Sn□1 and the best guess for the

<!-- page 631 (PDF 648) -->
next shape Sℓ
n, where ℓrepresents the most recent (the ℓth) calculation of Sn using
Eq. (16.33). (The Sℓ
n are considered converged when the last one satisfies a
normalization constraint.) Regardless of the approximate shape that is used, ρn(t)
is a first-order estimate of the static reactivity corresponding to the reactor
conditions at time t, and it will be referred to as such.

### Variational Principle for Static Reactivity

A variational estimate, accurate to second order [error ∼(Δϕ)2], for the static
reactivity worth of a perturbation to an altered system (i.e., a system other than the
one for which ϕ0 and ϕ∗
0 were calculated) is
ρv;e = hϕ∗
0; (λΔF □ ΔA)Si
hϕ∗
0; F´Si
□ 1 □ hϕ∗
0; (A □ λF)Γi □ hΓ∗; (A´ □ λ´F´)Si

(16.35)
where the generalized adjoint function Γ∗is calculated using
(A∗
0 □ λ0F∗
0)Γ∗=
(ΔA∗□ λ0ΔF∗)ϕ∗
hϕ∗
0; (ΔA □ λ0ΔF)ϕ0i □
F∗
0ϕ∗
hϕ∗
0; F0ϕ0i
(16.36)
and the function Γ is calculated using
(A0 □ λ0F0)Γ =
(Δ A □ λ0Δ F)ϕ0
hϕ∗
0; (ΔA □ λ0ΔF)ϕ0i □
F0ϕ0
hϕ∗
0; F0ϕ0i
(16.37)
In Eq. (16.35), the unprimed operators and eigenvalue refer to the altered system
at time tn and the primed operators and eigenvalue refer to the altered (by
previous changes from the initial) system plus a perturbation (i.e., ΔA = A´ □ A
and ΔF = F´ □ F) at time t>tn. The variational functional ρv,e provides an estimate
of the static reactivity worth of the perturbation, □Δλ = λ □ λ´, in the altered
system. The functional ρv,e is stationary about the altered and static perturbed
altered adjoint and direct eigenvalue equations, respectively (as well as being
stationary about the equations for Γ∗and Γ, for which Eqs. (16.36) and (16.37) are
approximations).
When ρv,e is used to estimate the reactivity for the point kinetics method
without updating the flux shapes, the initial configuration described by Eqs.
(16.22) and (16.25) is considered the altered system and ϕ0 is used for S. In this
case, ρv,e provides a second-order estimate of the static reactivity of Eq. (16.24),
rather than the dynamic reactivity of Eq. (16.29). In so doing, it ignores the
delayed neutron holdback effect, an omission that leads to errors in reactivity
estimates and consequent errors in power calculations.
When ρv,e is used to estimate the reactivity for the QS method, the configuration
at the time tn of the most recent shape calculation is considered the altered
system, and the Sn is used for S. In this case, ρv,e provides an estimate accurate to

<!-- page 632 (PDF 649) -->
second order of the static reactivity worth of perturbations made since time tn.
This estimate ignores the delayed neutron holdback effect. The total reactivity
worth of all perturbations (and alterations) is found by adding this perturbed
reactivity worth in the altered system to the best available estimate of the dynamic
reactivity worth of the alteration, which is ρn[Sn(r, tn)]. Because it is necessary to
use the flux shape corresponding to the altered system, it is not appropriate to use
the variational static reactivity estimate with interpolated flux shapes.

### Variational Principle for Dynamic Reactivity

To account for the delayed neutron holdback effect on the reactivity, a variational
principle should be stationary about the solutions of the time-dependent diffusion
and precursor equations, rather than stationary about the solution of the
perturbed static diffusion equation. To this end, the following functional was
constructed:
ρv ψ;ψ∗;ξm;ξ∗
m;Γ;Γ∗

=hψ∗;(λ0ΔF □ΔA)ψi
hψ∗;Fψi
□
1□hψ∗;(A0□λ0F0)Γi□
Γ∗; A□λ0(1□β)Fp+1
v
@
@t

ψ
(
+
Γ∗;
X
M
m=1
λmχmξm
*
+
□
X
M
m=1
ξ∗
m; λm+ @
@t

ξm
*
+
+
X
M
m=1
ξ∗
m;λ0βmFψ
*
+)
(16.38)
The usual procedure is to require that the functional be stationary with respect
to arbitrary and independent variations of the trial functions over all the
independent variables. However, in order to retain the time dependence of
the dynamic reactivity, the integrals in ρv (indicated by h,i), are only over space
and energy, not time. Thus, the stationarity conditions for the functional are
established by requiring that it be stationary with respect to arbitrary and
independent variations of only the space and energy dependencies of the
functions Γ∗, ξ∗
m Γ, ψ∗, ψ, and ξm. The following equations result
Aψs □ λ0(1 □ β)Fpψs □
X
M
m=1
λmχmξm;s + 1
v
@ψs
@t = 0
(16.39)
@ξm;s
@t
= λ0βmFψs □ λmξm;s
(16.40)
A∗
0ψ∗
s □ λ0F∗
0ψ∗
s = 0
(16.41)
(A0 □ λ0F0)Γs =
(ΔA □ λ0ΔF)ψs
hψ∗
s ; (ΔA □ λ0ΔF)ψsi □
Fψs
hψ∗
s ; Fψsi
(16.42)

<!-- page 633 (PDF 650) -->
A∗Γ∗
s □ λ0(1 □ β)F∗
pΓ∗
s □
X
M
m=1
λ0βmFξ∗
m;s
=
(ΔA∗□ λ0ΔF∗)ψ∗
s
hψ∗
s ; (ΔA □ λ0ΔF)ψsi □
F∗ψ∗
s
hψ∗
s ; Fψsi
(16.43)
and
λmξ∗
m;s □ λχT
mΓ∗
s = 0
(16.44)
respectively. Comparing Eqs. (16.39) and (16.20), (16.40) and (16.21), and
(16.41) and (16.25), it is clear that ψs and ξm,s can be identified as the solutions
ϕ(r, t) and Cm(r, t) of the exact time-dependent diffusion and precursor
equations and that ξ∗
m can be identified as the unperturbed static adjoint
flux ϕ∗
m.
The stationary value of ρv is
ρv;s = hϕ∗
0; (λ0ΔF □ ΔA)ϕ(r; t)i
hϕ∗
0; Fϕ(r; t)i
(16.45)
the exact, dynamic reactivity worth of a perturbation. To adapt the functional ρv
for use with the QS method, we introduce as a trial function
ψ(r; t) ≈ S(r; t)n(t)
(16.46)
and note that the best available approximation for the time derivative of the
precursor density is
@Cm(r; t)
@t
≈ βmF S(r; t)n(t) □ λmCm(r; t)
(16.47)
Under these conditions (and noting that ψ∗= ϕ∗
0 is available from Eq. (16.25)), the
functional becomes
ρv = hϕ∗
0; (λ0ΔF □ ΔA)Si
hϕ∗
0; FSi
1 □ hG∗; A □ λ0(1 □ β)Fp

Si □
G∗; 1
v
@S
@t
(
□ _n
n
G∗; 1
v S
+ 1
n
G∗;
X
M
m=1
λmχmCm
*
+)
(16.48)
where the quantity Γ∗(r, t)n(t) has been replaced by a trial function G∗(r, t). Note
that ΔA and ΔF here refer to the total perturbation, not the perturbation since the
most recent shape calculation, and that A = A0 + ΔA, F = F0 + ΔF.

<!-- page 634 (PDF 651) -->
Using Eqs. (16.44) and (16.46) in Eq. (16.43) results in the following equation
for G∗(r, t):
(A∗□ λ0F∗)G∗(r; t) =
(ΔA∗□ λ0ΔF∗)ϕ∗
hϕ∗
0; (ΔA □ λ0ΔF)S(r; t)i □
F∗ϕ∗
hϕ∗
0; FS(r; t)i
(16.49)
It is computationally economical to compute the generalized adjoint function G∗
only once for a particular core configuration. In this case, the initial static
configuration is used, resulting in the following approximation:
(A∗
0 □ λ0F∗
0)G∗=
(ΔA∗□ λ0ΔF∗)ϕ∗
hϕ∗
0; (ΔA □ λ0ΔF)S0i □
F∗
0ϕ∗
hϕ∗
0; F0S0i
(16.50)
(any magnitude perturbation ΔA and/or ΔF can be used since these operators
appear in both the numerator and denominator of the same term). Thus, G∗(r)
differs only in amplitude from Γ∗(r) of Eq. (16.36).
The form of the functional represented by Eq. (16.48) is well suited for use
with the QS method. In the QS method, the point kinetics equations are used
for the flux amplitude n(t), the precursor concentration densities Cm(r, t) are
updated at each time step and are therefore available for use in the variational
estimate, and the flux shape S(r, t) is recomputed periodically using Eq. (16.33).
The variational dynamic reactivity estimate can be used with or without flux
shape interpolations.
It should be noted that the G∗of Eq. (16.50) satisfies the orthogonality
condition
hG∗; F0S0i = 0
(16.51)
As a consequence, when the initial flux shape S0 is used in ρv and if the
precursor density functions Cm(r, t) have the same shape as S0, the variational
estimate for dynamic reactivity reduces to the variational estimate for static
reactivity, ρv, e of Eq. (16.35) (in which the second term in the square brackets
disappears because of Eq. (16.25)). The effect of this reduction is that until the
flux shape is recomputed or until some other approximation is made to replace
S0, the new variational functional still ignores the delayed neutron holdback
effect.
Numerical tests on a large LWR model indicate that the flux shape computational
effort required with the QS method can be reduced by a factor of 3–4 by
using the variational estimate of dynamic reactivity. In addition, use of a
variational reactivity estimate rather than the standard first-order estimate of
static reactivity can improve the accuracy of the QS method enough that the timeconsuming
flux shape interpolation/recomputation procedure may not be
necessary.
