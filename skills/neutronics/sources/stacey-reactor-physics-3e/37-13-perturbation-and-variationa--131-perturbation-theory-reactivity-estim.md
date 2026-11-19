# 13 Perturbation and Variational Methods — 13.1 Perturbation Theory Reactivity Estimate … 13.7 Variational Estimate of Intermediate Resonance Integral
<!-- source PDF pages 519-538 -->

<!-- page 501 (PDF 519) -->
# 13 Perturbation and Variational Methods

In many situations it is necessary to estimate the effect of numerous individual
perturbations in the materials properties of the reactor on the multiplication
constant or on a reaction rate in a reactor. Perturbation theory provides a
means for obtaining an estimate of the change in multiplication constant or
reaction rate, neglecting the effect of any change in the neutron flux distribution
caused by the perturbation. Generalized perturbation estimates and variational
estimates provide a means for taking into account the change in the neutron
flux distribution caused by the perturbation, without actually having to calculate
it, thus providing a powerful methodology for calculating reactivity
coefficients and for performing sensitivity studies. Variational methods also
have a much wider application in reactor physics in the development of
approximations, and several of these are described.

## 13.1 Perturbation Theory Reactivity Estimate

### Multigroup Diffusion Perturbation Theory

Let us return to the question of estimating the reactivity worth of a small change
made in a critical reactor described by multigroup diffusion theory:
□∇? Dg
0(r)∇ϕg
0(r) + Σg
t0(r)ϕg
0(r)
=
X
G
g´=1
Σg´!g
(r)ϕg´
0 (r) + 1
k0
χgX
G
g´=1
vΣg´
f (r)ϕg´
0 (r);
g = 1; . . . ; G
(13.1)
Assume a change in microscopic cross section, density, or geometry such that
D0 →D0 + ΔD, Σ0 →Σ0 + ΔΣ. This change will produce a change in the flux
ϕ0 →ϕ0 + δϕ and a change in effective multiplication constant k0 →k0 + Δk, such
that the perturbed system is described by
□∇? (Dg
0 + ΔDg)∇(ϕg
0 + δϕg) + (Σg
t0 + ΔΣg
t )(ϕg
0 + δϕg)
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 502 (PDF 520) -->
=
X
G
g´=1
(Σg´!g
+ ΔΣg´!g)(ϕg´
0 + δϕg´) +
χg
k0 + Δk
X
G
g´=1
(vΣg´
f 0 + Δ(vΣg´
f ))
□ (ϕg´
0 + δϕg´);
g = 1; . . . ; G
(13.2)
Equation (13.2) can, in principle, be solved to determine Δk using the methods
described previously. However, in some applications (e.g., the calculation of
reactivity coefficients associated with many different possible changes or the
evaluation of the sensitivity of the multiplication constant to cross section
uncertainties) this would be impractical because of the large number of such
calculations that would be involved. The objective of perturbation theory is to
provide an estimate of Δk without requiring a calculation of the perturbed
configuration (i.e., without calculating δϕ).
Using Eq. (13.1) to eliminate certain terms in Eq. (13.2), multiplying the
resulting equation in each group by an arbitrary (at this point) spatially dependent
function ϕ+
g , integrating over the reactor, and summing over groups, we obtain an
exact expression for Δk,
∫dr
X
G
g=1
ϕ+
g
□∇? Dg
0∇(δϕg) + Σg
t0δϕg □
X
G
g´=1
Σg´!g
δϕg´
"
(
□
χg
k0 + Δk
X
G
g´=1
vΣg´
f 0δϕg´
+ □∇? Δ Dg∇ϕg
0 + ΔΣg
t ϕg
0 □
X
G
g´=1
ΔΣg´!gϕg´
"
□
χg
k0 + Δk
X
G
g´=1
Δ(vΣg´
f )ϕg´
+ □∇? Δ Dg∇(δϕg) + ΔΣg
t δϕg □
X
G
g´=1
ΔΣg´!gδϕg´
"
□
χg
k0 + Δk
X
G
g´=1
Δ(vΣg´
f δϕg´)
#)
=
k0 + Δk □ 1
k0

∫dr
X
G
g=1
ϕ+
g χgX
G
g´=1
vΣg´
f 0ϕg´
= □
Δk
k0(Δk + k0) ∫dr
X
G
g=1
ϕ+
g χgX
G
g´=1
vΣg´
f 0ϕg´
(13.3)

<!-- page 503 (PDF 521) -->
if we were willing to calculate δϕg in order to evaluate it. However, we wish to
neglect δϕ, which appears in two of the [□] terms on the left side. We might argue
(for the moment) that since the third [□] term is the product of δϕ and ΔΣ or ΔD,
we can neglect it as being of second order in small quantities. However, we cannot
make this argument for the first [□] term, which is of first order in small quantities,
as is the second [□] term which we wish to evaluate to obtain the perturbation
estimate of Δk. Thus, are we motivated to choose the ϕ+
g to cause the first [□] term
in Eq. (13.3) to vanish for arbitrary δϕg. To determine the equation that must be
satisfied by ϕ+
g , it is necessary to twice integrate by parts the gradient part of the
first [□] term and use the divergence theorem,
□∫dr ϕ+
g ∇? Dg
0∇(δϕg) = □∫dr ∇? (ϕ+
g Dg
0∇(δϕg))
+ ∫dr Dg
0∇ϕ+
g ? ∇(δϕg) = □∫s
ds ϕ+
g Dg
0∇(δϕg) ? ns
+ ∫dr ∇? (δϕgDg
0∇ϕ+
g ) □ ∫dr δϕg∇? (Dg
0∇ϕ+
g )
= □∫s
ds ϕ+
g Dg
0∇(δϕg) ? ns + ∫s
ds δϕgDg
0∇ϕ+
g ? ns
□ ∫dr δϕg∇? (Dg
0∇ϕ+
g )
(13.4)
where ns is the outward normal unit vector to the surface of the reactor and the
integrals over s are surface integrals. δϕg, which must satisfy the same boundary
conditions as ϕg, vanishes on the surface of the reactor, which causes the second
term on the right in the final form of Eq. (13.4) to vanish. If we choose a boundary
condition ϕ+
g (rs) = 0 (i.e., ϕ+
g vanishes on the surface of the reactor), the first term
on the right in Eq. (13.4) also vanishes. Using this result in Eq. (13.3) and
interchanging the dummy g and g´ indices, the vanishing of the first [□] term
requires that
∫dr
X
G
g=1
δϕg
"
□∇? Dg
0∇ϕ+
g + Σg
t0ϕ+
g
□
X
G
g´=1
Σg!g´
ϕ+
g´ □
vΣg
f 0
k0 + Δk
X
G
g´=1
χg´ϕ+
g´
= 0
(13.5)
which is satisfied for arbitrary δϕg if ϕ+
g satisfies
□∇? Dg
0∇ϕ+
g + Σg
t0ϕ+
g =
X
G
g´=1
Σg!g´ϕ+
g´ +
vΣg
f 0
k0 + Δk
X
G
g´=1
χg´ϕ+
g ;
g = 1; . . . ; G
(13.6)

<!-- page 504 (PDF 522) -->
and vanishes on the surface of the reactor:
ϕ+
g´(rs) = 0;
g = 1; . . . ; G
(13.7)
With the function ϕ+
g which satisfies Eqs. (13.6) and (13.7), with neglect of the
third [□] term on the left, and with the approximation k0(k0 + Δk) →k0, Eq. (13.3)
reduces to the perturbation theory expression for the reactivity worth,
ρpert ≡ Δk
k0
=
∫dr
X
G
g=1
ϕ+
g
∇? ΔDg∇ϕg
0 □ ΔΣg
t ϕg
0 +
X
G
g´=1
ΔΣg´!gϕg´
"
+
χg
k0
X
G
g´=1
Δ(vΣg´
f 0)ϕg´
□
∫dr
X
G
g=1
ϕ+
g χgX
G
g´=1
vΣg´
f 0ϕg´
0 + O(δϕ)
(13.8)
where we indicate by O(δϕ) that the neglected third [□] term in Eq. (13.3)
introduces an error of order δϕ (into a term which itself is of order ΔΣ).

## 13.2 Adjoint Operators and Importance Function

### Adjoint Operators

Equation (13.6) is mathematically adjoint to Eq. (13.1), when k0 + Δk →k0, and the
function ϕ+
g is called the adjoint function. Comparing Eqs. (13.1) and (13.6) term
by term identifies the direct and adjoint operators of multigroup diffusion theory,
which are denoted symbolically as
Direct
Adjoint
[D(ϕ)]g ≡ □∇? Dg∇ϕg
[D+(ϕ+)]g ≡ □∇? Dg∇ϕ+
g
[Σ(ϕ)]g ≡ Σg
t ϕg
[Σ+(ϕ+)]g ≡ Σg
t ϕ+
g
[S(ϕ)]g ≡
X
G
g´=1
Σg´!gϕg´
[S+(ϕ+)]g ≡
X
G
g´=1
Σg!g´ϕ+
g´
[F(ϕ)]g ≡ χgX
G
g´=1
vΣg´
f ϕg´
[F+(ϕ+)]g ≡ vΣg
f
X
G
g´=1
χg´ϕ+
g´
(13.9)
The direct and adjoint operators for group diffusion and group absorption are
identical; these operators are said to be self-adjoint. On the other hand, the adjoint

<!-- page 505 (PDF 523) -->
group scattering and fission operators differ from the direct operators. Note that
there is an adjoint boundary condition (Eq. (13.7)) associated with the definition
of the adjoint group diffusion operator. In terms of these operators, Eq. (13.8) for
the perturbation theory estimate of the reactivity worth of a change in reactor
properties becomes
ρpert = ∫dr PG
g=1 ϕ+
g f□[ΔD(ϕ0)]g □ [ΔΣ(ϕ0)]g + [ΔS(ϕ0)]g + (1=k0)[ΔF(ϕ0)]gg
∫dr PG
g=1 ϕ+
g [F0(ϕ0)]g
≡ ∫dr PG
g=1 ϕ+
g f□[ΔA(ϕ0)]g + (1=k0)[ΔFϕ0]gg
∫dr PG
g=1 ϕ+
g [F0(ϕ0)]g
+ O(δϕ)
(13.10)
It is clear from the derivation above that the adjoint operators were defined by the
requirement
∫dr
X
G
g=1
ϕ+
g [B(ϕ)]g ≡ ∫dr
X
G
g=1
ϕg[B+(ϕ+)]g
(13.11)
where [B(ϕ)]g represents any one of the operators in Eq. (13.9). This definition of
adjoint group operator is quite general and provides for the immediate generalization
of perturbation theory to multigroup transport theory by replacement of
[D(ϕ)]g with the appropriate transport group operator [T(ϕ)]g.
This formalism may be generalized immediately from multigroup to energydependent
diffusion or transport theory by replacing the sum over groups by an
integral over energy. At this point, we introduce the notation
hBϕi ≡ ∫dr
X
G
g=1
[B(ϕ)]g
or
∫dr∫
dE B(ϕ)
(13.12)
which allows the compact expression of the perturbation theory estimate of
reactivity worth:
ρpert = hϕ+; (ΔF □ ΔA)ϕ0i
hϕ+; F0ϕ0i
+ O(δϕ)
(13.13)
In this notation, the definition of the adjoint operator becomes
hϕ+; Bϕi ≡ hϕ; B+ϕ+i
(13.14)

<!-- page 506 (PDF 524) -->
### Importance Interpretation of the Adjoint Function

The mathematical definition of the adjoint function (in the diffusion theory approximation
) is simply the function that satisfies Eq. (13.6). The physical interpretation is
somewhat subtle and involves the concept of neutron importance, more specifically
theimportanceofaneutronintroducedintoareactortoaspecificobservablephysical
quantity. For example, an importance may be defined as the expected number of
counts that will be produced at all subsequent times by a neutron introduced into a
reactor with a given position, energy, and direction or by the secondary, tertiary, and
so on neutrons produced at other energies and directions as a result of fission and
scattering events due to the original neutron. For a critical reactor, it is conventional
to define the neutron “importance,” ψ+(r, Ω, E), asthe asymptotic increase in neutron
population in the reactor due to a single neutron introduced into the reactor with a
given energy E, with a given direction Ω, and at a given location r. (Actually, we need
to speak of neutrons introduced within dE about E, dr about r, and dΩ about Ω, but
we will leave this cumbersome terminology to be understood.) Neutrons introduced
with a given energy and direction at a given location can (1) move to another location
r + dr where the importance is different; (2) be captured, which causes the importance
to become zero; (3) be scattered into a different energy E´ and direction Ω´
wheretheimportanceisdifferent;or(4)producefission,whichcausestheimportance
of the original neutron to become zero, but which produces v new neutrons
distributed in energy E´ and distributed isotropically in direction Ω´ with different
importances. In a critical reactor, the importance must be conserved as the N
neutrons move about and undergo these various reactions, which can be expressed as
N
"
[ψ+(r + dr; Ω; E) □ ψ+(r; Ω; E)] □ [Σa(r; E) + Σs(r; E)]ψ+(r; Ω; E)
+ ∫
dE´
∫
4π
dΩ´Σs(r; E ! E´; Ω ! Ω´)ψ+(r; Ω´; E´)
+ vΣf (r; E)
k
∫
dE´
∫
4π
dΩ´χ(E´)ψ+(r; Ω; E´)

= 0
(13.15)
Making a Taylor’s series expansion
ψ+(r + dr; Ω; E) ' ψ+(r; Ω; E) + Ω ? ∇ψ+(r; Ω; E)
(13.16)
in Eq. (13.15) leads to the transport equation satisfied by the neutron importance:
Ω ? ∇ψ+(r; Ω; E) □ Σt(r; E)ψ+(r; Ω; E)
+ ∫
dE´
∫
4π
dΩ´Σs(r; E ! E´; Ω ! Ω´)ψ+(r; Ω´; E´)
+ vΣf (r; E)
k
∫
dE´
∫
4π
dΩ´χ(E´)ψ+(r; Ω´; E´) = 0
(13.17)

<!-- page 507 (PDF 525) -->
The importance of neutrons leaving the reactor is zero, which provides a
boundary condition for the neutron importance,
ψ+(rS; Ω; E) = 0;
nS ? Ω > 0
(13.18)
where ns is the outward normal unit vector to the surface of the reactor.
Compare these equations with the neutron transport equation and surface
boundary condition derived in Chapter 9:
□Ω ? ∇ψ(r; Ω; E) □ Σt(r; E)ψ(r; Ω; E)
+ ∫
dE´
∫
4π
dΩ´Σs(r; E´ ! E; Ω´ ! Ω)ψ(r; Ω´; E´)
+ χ(E)
k
∫
dE´
∫
4π
dΩ´vΣf (r; E´)ψ(r; Ω; E´) = 0
(13.19)
and
ψ(rS; Ω; E) = 0;
nS ? Ω < 0
(13.20)
The neutron transport equation is based on a backward balance of neutrons
among those neutrons that scattered or were produced in fission or moved from a
nearby location in the immediate past (i.e., in the interval t □ Δt to t) and those
neutrons that are undergoing absorption and scattering now (i.e., at time t). The
importance equation is based on a forward balance of the importance among
those neutrons that are being absorbed or scattered now (i.e., at time t) and the
importance of those neutrons that will move to a nearby location or be scattered
into a different energy and direction or produce fission neutrons with different
energy and direction in the immediate future (i.e., in the interval t to t + Δt).

### Eigenvalues of the Adjoint Equation

In the foregoing development of Eq. (13.17) from physical arguments, the same
effective multiplication constant was used to achieve a steady-state importance
balance equation as was used to achieve a steady-state neutron balance equation.
We now establish formally that the eigenvalues of the neutron balance equation
(A □ λF)ϕ = 0
(13.21)
and of the adjoint equation
(A+ □ λ+F+)ϕ+ = 0
(13.22)
are identical when the adjoint operators are related to the direct operators by
Eq. (13.14). Multiplying Eq. (13.21) by ϕ+ and integrating over space, direction,

<!-- page 508 (PDF 526) -->
and energy, multiplying Eq. (13.22) by ϕ and integrating, and making use of
Eq. (13.14) yields
λ = hϕ+; Aϕi
hϕ+; Fϕi = hϕ; A+ϕ+i
hϕ; F+ϕ+i = λ+
(13.23)

## 13.3 Variational/Generalized Perturbation Reactivity Estimate

In many practical applications, a perturbation to the properties of the reactor
will cause a change in the neutron flux distribution that has a significant effect
on the reactivity worth of the perturbation (i.e., the neglected third [□] term in
Eq. (13.3) is important). The perturbation theory of Section 13.1 can be
extended to take into account the change in the flux distribution without
actually requiring its calculation. Such extensions can be developed within the
context of variational theory or simply as a heuristic extension of perturbation
theory; the results are the same except for minor differences. This extended
perturbation theory is widely used in reactor physics in the calculation of
reactivity worths (and reaction rate ratios – next section) and for the performance
of sensitivity studies. Since the variational theory is more systematic
and has broader applications in reactor physics, we follow the variational
development of an extended perturbation theory for estimating reactivity
worths.

### One-Speed Diffusion Theory

Consider a critical reactor described by the one-speed diffusion equation
□∇? D0∇ϕ0 + Σa0ϕ0 □ λ0vΣf 0ϕ0 = 0
(13.24)
where, for convenience of notation, we set λ ≡ k□1. Making use of the definition of
adjoint operator given by Eq. (13.11) with G = 1, the one-speed diffusion theory
adjoint equation satisfies
□∇? D0∇ϕ+
0 + Σa0ϕ+
0 □ λ0vΣf 0ϕ+
0 = 0
(13.25)
Thus, the one-speed diffusion equation is self-adjoint and ϕ+ = ϕ.
Now consider perturbations D0 →D = D0 + ΔD and Σ0 →Σ = Σ0 + ΔΣ, which
cause ϕ0 →ϕex = ϕ0 + δϕ and λ0 →λ = λ0 + Δλ. The perturbed system satisfies
□∇? D∇ϕex + Σaϕex □ λvΣf ϕex = 0
(13.26)
Multiplying Eq. (13.26) by ϕ+
0 , multiplying Eq. (13.25) by ϕex, integrating over
volume, subtracting, and rearranging yields an exact expression for the reactivity

<!-- page 509 (PDF 527) -->
worth of the perturbation:
ρexfϕ+
0 ; ϕexg = □Δλ
= hϕ+
0 ; (λ0Δ(vΣf )ϕex + ∇? ΔD∇ϕex □ ΔΣaϕex)i
hϕ+
0 ; vΣf ϕexi
(13.27)
If we used the approximation ϕex ≈ ϕ0 to evaluate Eq. (13.27), we would obtain the
perturbation theory estimate of the reactivity worth of the change, in one-speed
diffusion theory:
ρpert ϕ+
0 ; ϕ0

= hϕ+
0 ; (λ0Δ(vΣf )ϕ0 + ∇? ΔD∇ϕ0 □ ΔΣaϕ0)i
hϕ+
0 ; vΣf ϕ0i
+ O(δϕ)
(13.28)
which is accurate to first order in δϕ.
Variational or generalized perturbation theory allows us to obtain an estimate
that is accurate to second order in δϕ. Note that Eq. (13.27) defines a number that
is evaluated by performing integrals over space (more generally over space and
energy) involving the functions ϕ+
0 and ϕex. Such a function of functions is known
as a functional. The idea behind variational theory is to construct an equivalent
variational functional ρvarfϕ+; ϕ; Γ+g that has the properties: (1) ρvarfϕ+
0 ; ϕex; Γ+
exg
has the same value as the functional ρexfϕ+
0 ; ϕexg if ϕ+
0 and ϕex are used to evaluate
ρvar and (2) ρvarfϕ+
0 ; ϕ; Γ+g evaluated with functions ϕ+
0 and ϕ = ϕex + δϕ yields a
value
that
differs
from
ρexfϕ+
0 ; ϕexg
by
O(δϕ2; δϕδΓ+).
In
particular,
ρvarfϕ+
0 ; ϕ0; Γ+g = ρexfϕ+
0 ; ϕexg + O(δϕ2) when ϕex = ϕ0 + δϕ.
We construct
ρvar
(
ϕ+
0 ; ϕ; Γ+
)
= hϕ+
0 ; (λ0Δ(vΣf )ϕ + ∇? ΔD∇ϕ □ ΔΣaϕ)i
hϕ+
0 ; vΣFϕ)
□ [1 □ hΓ+; (□∇? D∇ϕ + Σaϕ □ λvΣf ϕ)i]
(13.29)
by taking the exact functional of Eq. (13.27) and multiplying it by 1 minus a
correction functional constructed by premultiplying the exact Eq. (13.26) by Γ+
and integrating over space (space and energy in general). This functional
obviously satisfies the first of the properties of the variational functional above,
because when ϕ = ϕex, the correction functional vanishes and the first term
reduces identically to ρexfϕ+
0 ; ϕexg. Subtracting yields
ρvarfϕ+
0 ; ϕex; Γ+g □ ρvarfϕ+
0 ; ϕex □ δϕ; Γ+g
= □ hϕ+
0 ; (λ0Δ(vΣf )ϕex + ∇? ΔD∇ϕex □ ΔΣaϕex)i
hϕ+
0 ; vΣf ϕexi
□
hΓ+; (□∇? D∇δϕ + Σaδϕ □ λvΣf δϕ)i + hϕ+
0 ; vΣf δϕi
hϕ+
0 ; vΣf ϕexi

+ hϕ+
0 ; (λ0Δ(vΣf )δϕ + ∇? ΔD∇δϕ □ ΔΣaδϕ)i
hϕ+
0 ; vΣf ϕexi
+ O(δϕ2)
(13.30)

<!-- page 510 (PDF 528) -->
The explicit terms on the right in this expression will vanish for arbitrary δϕ if Γ+
is chosen to satisfy
□∇? D∇Γ+
ex + ΣaΓ+
ex □ λvΣf Γ+
ex
=
□∇? ΔD∇ϕ+
0 + ΔΣaϕ+
0 □ λ0Δ(vΣf )ϕ+
hϕ+
0 ; (□∇? ΔD∇ϕex + ΔΣaϕex □ λ0Δ(vΣf )ϕex)i □
vΣf ϕ+
hϕ+
0 ; vΣϕexi
(13.31)
so that ρvarfϕ+
0 ; ϕ; Γ+
exg = ρexfϕ+
0 ; ϕexg + O(δϕ2). Thus, evaluation of the variational
functional of Eq. (13.29) using the functions ϕ+
0 given by Eq. (13.25), Γ+
ex
given by Eq. (13.31), and any function ϕ = ϕex + δϕ yields an estimate of the
reactivity worth of the change that is accurate to O(δϕ2).
Unfortunately, solving Eq. (13.31) requires a knowledge of ϕex, avoidance of the
calculation of which is the purpose of this development. If, instead of Eq. (13.31),
we use the equation obtained by changing ϕex →ϕ0
□∇? D0∇Γ+
0 + Σa0Γ+
0 □ λ0vΣf 0Γ+
=
□∇? ΔD∇ϕ+
0 □ λ0Δ(vΣf )ϕ+
0 + ΔΣaϕ+
hϕ+
0 ; (□∇? ΔD∇ϕ0 + ΔΣaϕ0 □ λ0Δ(vΣf )ϕ0)i □
vΣf ϕ+
hϕ+
0 ; vΣf ϕ0i
(13.32)
it can be shown that ρvarfϕ+
0 ; ϕ; Γ+
0 g = ρexfϕ+
0 ; ϕexg + O(δϕ2; δϕδΓ+), where
Γ+
ex = Γ+
0 + δΓ+. Thus, the variational estimate ρvarfϕ+
0 ; ϕ; Γ+
0 g is accurate to
second order in the (presumably) small quantities δϕ and δΓ.
The function Γ+ is related to the flux change, δϕ, caused by the perturbation.
The equation satisfied by δϕ is obtained by using D = D0 + ΔD, Σ = Σ0 + ΔΣ, and
ϕex = ϕ0 + δϕ in Eq. (13.26) and making use of Eq. (13.24):
□∇? D∇(δϕ) + Σa(δϕ) □ λvΣf (δϕ)
= □[□∇? ΔD∇ϕ0 + ΔΣaϕ0 □ Δ(λvΣf )ϕ0]
(13.33)
Comparing this equation with Eq. (13.31), it is apparent that Γ+ ∼□δϕ, since
ϕ0 = ϕ+
0 for one group. A similar relationship may be established for multigroup
theory.
Defining the variational flux correction factor
f varfϕ0; Γ+
0 g = hΓ+
0 ; (□∇? ΔD∇ϕ0 + ΔΣaϕ0 □ λ0Δ(vΣf )ϕ0
□ ΔλΔ(vΣf )ϕ0)i
(13.34)
the variational estimate for the reactivity worth of a change in reactor properties
may be written
ρvarfϕ+
0 ; ϕ0; Γ+
0 g = ρpertfϕ+
0 ; ϕ0g[1 □ f varfϕ0; Γ+
0 g]
(13.35)
as the perturbation theory estimate times a flux correction factor.

<!-- page 511 (PDF 529) -->
The calculations required for the variational estimate include the solution for the
threespatialfunctionsϕ+
0 ; ϕ0,andΓ+
0 fortheparametersofthecriticalreactorandthe
evaluation of the indicated spatialintegrals in Eq. (13.29). The left side of Eq. (13.32) is
identical with the homogeneous Eq. (13.24). However, the useful biorthogonality
property hΓ+
0 ; F0ϕ0i = 0 can be demonstrated (Ref. [1]), which assures the existence
ofasolution.NotethatthesourcetermontherightofEq.(13.32)willingeneralbethe
same for all perturbations taking place within a given spatial domain, since the
magnitude of the perturbations appear in the numerator and denominator, implying
that the calculation of one such Γ+
0 for each distinct spatial domain of interest will
allow the evaluation of the reactivity worths of a large number of perturbations of
different types and magnitudes within that spatial domain.
The reactivity estimate of Eq. (13.35) has been found to be quite accurate when
the change in properties is such as to produce a positive reactivity (fvar < 0) or a
small negative reactivity for which 0 < fvar ≪1. However, for large negative
reactivities such that fvar ∼1, the (1 □ fvar) term becomes inaccurate. In such
cases it is more accurate to use ρvar = ρpert[1 □ fvar/(1 + fvar)], which form can be
derived from consideration (Ref. [2]) of the exact functional of Eq. (13.27). Thus, a
better variational estimate for the reactivity worth is
ρvar ϕ+
0 ; ϕ0; Γ+

= ρpert ϕ+
0 ; ϕ0

1 □ f varfϕ0; Γ+
0 g;
ρ0 > 0
1 □
f varfϕ0; Γ+
0 g
1 + f varfϕ0; Γ+
0 g ;
ρ0 < 0
>
<
>
:
(13.36)

### Other Transport Models

This formalism can be generalized immediately to other representations of
neutron transport (e.g., multigroup diffusion or transport theory). Let the
operator A represent the transport, absorption, and scattering and the operator
F represent the fission. Then Eqs. (13.24) and (13.25) for the flux and adjoint in the
critical reactor generalize to
(A0 □ λ0F0)ϕ0 = 0
(13.37)
(A+
0 □ λ0F+
0 )ϕ+
0 = 0
(13.38)
and Eq. (13.26) for the flux in the perturbed reactor generalizes to
(A □ λF)ϕex = 0
(13.39)
The exact value and perturbation theory estimate of the reactivity worth of the
perturbation of Eqs. (13.27) and (13.28) become
ρex ϕ+
0 ; ϕex

= hϕ+
0 ; (λ0ΔF □ ΔA)ϕexi
hϕ+
0 ; Fϕexi
(13.40)

<!-- page 512 (PDF 530) -->
ρpert ϕ+
0 ; ϕ0

= hϕ+
0 ; (λ0ΔF □ ΔA)ϕ0i
hϕ+
0 ; Fϕ0i
(13.41)
Equation (13.32) for the generalized adjoint function Γ+
0 becomes
(A0 □ λ0F0)Γ+
0 =
(ΔA+ □ λ0ΔF+)ϕ+
hϕ+
0 ; (ΔA □ λ0ΔF)ϕ0i □
F+
0 ϕ+
hϕ+
0 ; F0ϕ0i
(13.42)
The variational estimate for the reactivity worth of the perturbation is still given
by Eq. (13.36), where now ρpert is given by Eq. (13.41) and the flux correction
factor is given by
f varfϕ+
0 ; ϕ0; Γ+
0 g = hΓ+
0 ; (ΔA □ λ0ΔF □ ΔλΔF)ϕ0i
(13.43)

### Reactivity Worth of Localized Perturbations in a Large PWR Core Model

Exact, perturbation theory, and variational calculations were made of the
reactivity worth of a change in the thermal group absorption cross section in
a two-group model of a large (about 40 migration lengths) slab model of a PWR
core. The perturbations were made in the left quarter of the core model. Small
cross section changes produced small reactivity changes that were well estimated
by both perturbation and variational methods because the associated flux change
was small. Larger cross section changes, which produced larger reactivity worths
and significant flux changes were poorly predicted by perturbation theory, but the
variational flux correction resulted in quite accurate predictions even for flux tilts
on the order of 100%. The reactivity predictions are shown in Fig. 13.1, and
associated flux shapes for the unperturbed core and for the core with two of the
perturbations are shown in Fig. 13.2. The unit of reactivity is pcm = 10□5.

### Higher Order Variational Estimates

A variational formalism (Refs. [3,4]) has been developed for making reactivity
estimates that are accurate to higher order in δϕ = ϕex □ ϕ0. However, the
complexity of such estimates has limited their practical application.

## 13.4 Variational/Generalized Perturbation Theory Estimates of Reaction Rate Ratios in Critical Reactors

Consider the problem of estimating the reaction rate ratio
RR ϕex
f
g = hΣiϕexi
hΣjϕexi
(13.44)

<!-- page 513 (PDF 531) -->
in a perturbed system in which the exact flux is given by Eq. (13.39), without
solving Eq. (13.39) for ϕex. The unperturbed critical reactor is described by
Eq. (13.37). As before, the operator A represents the transport, absorption, and
scattering and the operator F represents the fission, in whatever theory is chosen
to describe the neutron distribution in the reactor (e.g., multigroup diffusion,
multigroup Sn). Clearly, a perturbation theory estimate
RRpert ϕ0
f
g = hΣiϕ0i
hΣjϕ0i
(13.45)
has errors of O(δϕ = ϕex □ ϕ0).
Defining the generalized adjoint function, Γ+
R, by
(A+ □ λF+)Γ+
R =
Σi
hΣiϕexi □
Σj
hΣjϕexi
(13.46)
–1.0
–0.5
0.0
0.5
-200
exact
perturbation
variational
reactivity (pcm)
% change thermal absorption x section
-400
-600
-800
1.0
1.5
Fig. 13.1 Reactivity worth of thermal cross section changes over the left quarter of a
slab PWR model in two-group diffusion theory: comparison of exact, perturbation
theory, and variational calculations. (With permission from Ref. [2]. Copyright 1997,
American Nuclear Society.)

<!-- page 514 (PDF 532) -->
the variational estimate
RRvar ϕ0; Γ+
R0

= hΣiϕ0i
hΣjϕ0i 1 □ hΓ+
R0; (ΔA □ Δ(λF))ϕ0i

(13.47)
where Γ+
R0 is calculated from Eq. (13.46) but with A →A0, F →F0, and ϕex →ϕ0,
will have a second-order error O(δΓ+ δϕ), as may be demonstrated by
evaluating
RRexfϕexg □ RRvarfϕ0; Γ+
R0g = O(δΓ+
Rδϕ)
(13.48)
Several reaction rate ratios calculated for a multigroup diffusion theory model of
the spherical ZEBRA fast reactor critical assembly are given in Table 13.1. The
breeding ratio is the ratio of the 238U capture rate integrated over the region to the
239Pu fission rate integrated over the region. The reference assembly composition
is given in Table 13.2. It is clear that the flux correction provided by the variational
(generalized perturbation theory) calculation is important in achieving an accurate
estimate.
Perturabed
region
X (cm)
Normalized flux
Initial
+315 pcm
-120 pcm
Fig. 13.2 Thermal flux distributions for the unperturbed and two perturbed conditions in a
two-group slab PWR model. (With permission from Ref. [2]. Copyright 1997, American
Nuclear Society.)

<!-- page 515 (PDF 533) -->
## 13.5 Variational/Generalized Perturbation Theory Estimates of Reaction Rates

Many problems in reactor physics can be formulated as fixed source problems
described by
A0ϕ0 = S
(13.49)
where the operator A represents transport, absorption, scattering, and if present
in the particular problem, fission. Let us imagine that Eq. (13.49) has been solved
for ϕ0 and then the reactor is perturbed, so that the flux now satisfies
Aϕex = S
(13.50)
Table 13.1 Table Perturbed Reaction Rate Ratios
Ratio
Reference
Value
Perturbation
RRexact
RRpert
RRvar
Central σ28
c =σ49
f
0.09866
Add 0.01 at/cm3 Na
0 →9.45 cm
0.10241 0.09866 0.10225
0.09866
Increase σ49
f
10%
0.08964 0.08969 0.08964
0.09866
Add 0.0015 at/cm3 Pu
9.45 →22.95 cm
0.09887 0.09866 0.09884
Core breeding
ratio
0.80040
Add 0.01 at/cm3 Na
0 →9.45 cm
0.80554 0.80040 0.80549
Assembly
breeding ratio
2.1844
Increase σ49
f
10%
1. 9939
2.0038
1.9937
2.1844
Add 0.0015 at/cm3 Pu
9.45 →22.95 cm
1.6034
1.6446
1 .6049
Source: Data from Ref. [1]; used with permission of Academic Press.
Table 13.2 Composition of Spherical Computational Model of ZEBRA Critical Assembly
Isotope
Core (0 →22.95 cm)
Blanket (22.95 →49.95 cm)
239Pu
0.00371
0.0003
238U
0.03174
0.04099
56Fe
0.005698
0.00477
Source: Data from Ref. [1]; used with permission of Academic Press.

<!-- page 516 (PDF 534) -->
and we wish to evaluate the reaction rate
Rfϕexg = hΣϕexi
(13.51)
without calculating ϕex. The perturbation theory estimate Rpert{ϕ0} = hΣϕ0i + O
(δϕ) obviously is only accurate to zero order in the flux perturbation that is caused
by the perturbation in the reactor properties.
Defining an adjoint function, ϕ+
R0, by
A+ϕ+
R0 = Σ
(13.52)
it is easy to show that the variational estimate
Rvarfϕ0; ϕ+
R0g = hΣϕ0i □ hϕ+
R0; (S □ A0ϕ0)i
(13.53)
differs from the exact calculation of the reaction rate in the perturbed reactor by a
second-order term,
Rexfϕexg □ Rvarfϕ0; ϕ+
R0g = O(δϕδϕ+
R)
(13.54)
where ϕ+
R0 is calculated from Eq. (13.52) with A →A0.
By making use of the definition of the adjoint operator, it follows that
hΣϕi = hA+ϕ+
R; ϕi = hϕ+
R; Aϕi = hϕ+
RSi
(13.55)
implying that the reaction rate can also be calculated by integrating the product of
the source distribution S and the generalized adjoint function ϕ+
R over the volume
of the reactor. This result suggests the interpretation of ϕ+
R as an importance
function for a source neutron to produce the reaction represented by Σ.

## 13.6 Variational Theory

### Stationarity

We have constructed variational extensions of perturbation theory by establishing
functionals that when evaluated with the exact solutions of the governing
equations yielded the exact value of a quantity of interest (e.g., reactivity worth,
reaction rate) and that when evaluated with approximate solutions of the
governing equations (or exact solutions of equations that approximated the
governing equations) differed from the exact result by terms of second order
in the difference between the approximate solutions and the exact solutions. In
other words, terms involving first-order variations between the exact and

<!-- page 517 (PDF 535) -->
approximate solutions vanished when the approximate solutions were used in the
variational functionals. This property is described by stating that the variational
functionals are stationary about the exact solutions of the governing equations
(i.e., the first variations vanish), and the functions that make the variational
functional stationary (by satisfying the governing equations) are known as the
stationary functions. This means that the same value of the variational functional
will be obtained when evaluated with two different functions that differ infinitesimally
, if one of these functions exactly satisfies the governing equations (i.e., is
the stationary function of the variational functional).
Minimum principles of various sorts are usually represented by variational
functionals, and the minimum property of the variational functional is a form of
stationarity condition. However, with a minimum principle or minimum variational
functional, the value of the variational functional will increase when
evaluated with any function that differs sufficiently from the stationary function
that δϕ2 is significant, whereas the value of a stationary variational functional may
be greater or less than the stationary value when evaluated with a function that
differs sufficiently from the stationary function.

### Roussopolos Variational Functional

Consider again the variational functional of Eq. (13.53), which we now write in the
more general form known as the Roussopolos functional:
Rvarfϕ; ϕ+
Rg = hΣϕi □ hϕ+
R; Aϕ □ Si
(13.56)
The stationarity condition is
δRvar ≡ Rvarfϕ + δϕ; ϕ+
R + δϕ+
Rg □ Rvarfϕ; ϕ+
Rg
= hΣδϕi □ hδϕ+
R(Aϕ □ S)i + hA+ϕ+
R; δϕi = 0
(13.57)
For arbitrary and independent variations δϕ and δϕ+
R, this requires that
δϕ : Σ □ A+ϕ+
Rs = 0;
δϕ+ : S □ Aϕs = 0
(13.58)
where the subscript s indicates the stationary solution. When the stationary
solutions are used to evaluate the functional of Eq. (13.56), the exact value hΣϕsi is
obtained. When approximate functions – trial functions – ϕ = ϕs + δϕ and ϕ+
R =
ϕ+
Rs + δϕ+
R are used to evaluate the functional of Eq. (13.56), the value obtained
differs from the exact value by a term of order (δϕδϕ+
R).

### Schwinger Variational Functional

The estimate of the reaction rate provided by Eq. (13.56) or (13.53) is obviously
sensitive to the normalization of the trial functions. The stationarity of the

<!-- page 518 (PDF 536) -->
variational functional can be used to choose the best normalization. Write χ+ =
c+ϕ+
R and χ = cϕ. Substitute these trial functions into the variational functional of
Eq. (13.56) and require stationarity with respect to arbitrary and independent
variations δc+ and δc:
δRvar = hΣϕiδc + hϕ+
R; (S □ Acϕ)iδc+ □ hA+c+ϕ+
R; ϕiδc = 0
(13.59)
which is satisfied for arbitrary δc and δc+ only if
c+ =
hΣϕi
hϕ+
R; Aϕi ;
c =
hϕ+
RSi
hϕ+
R; Aϕi
(13.60)
Using these normalizations in Eq. (13.56) yields the equivalent Schwinger
variational principle,
J ϕ; ϕ+
R

= hΣϕihϕ+
RSi
hϕ+
R; Aϕi
(13.61)
the value of which is independent of the normalization of the trial functions.

### Rayleigh Quotient

Consider the critical reactor eigenvalue problem described by the transport and
adjoint equations
(A □ λF)ϕ = 0;
(A+ □ λF+)ϕ+ = 0
(13.62)
The Rayleigh quotient
λ ϕ+; ϕ
f
g = hϕ+; Aϕi
hϕ+; Fϕi
(13.63)
is a variational functional for the eigenvalue. The value of Eq. (13.63) when the
exact solution of the first of Eq. (13.62) is used in its evaluation is clearly the exact
eigenvalue. The requirement that the first variation of the Rayleigh quotient
vanish,
δλ = hδϕ+; Aϕi + hϕ+; Aδϕi
hϕ+; Fϕi
□ hϕ+; Aϕi
hϕ+; Fϕi
hδϕ+; Fϕi + hϕ+; Fδϕi
hϕ+; Fϕi
= 0
(13.64)
for arbitrary and independent variations δϕ+ and δϕ requires that the stationary
functions ϕs and ϕ+
s satisfy Eq. (13.62).

<!-- page 519 (PDF 537) -->
### Construction of Variational Functionals

Although the construction of variational functionals is usually done by trial and
error, there is a systematic procedure that can guide the process. The basic idea is
to add the inner product of some function ϕ+ or Γ+ with the governing equation
for ϕ to the quantity of interest and then use the stationarity requirement to
determine the equation satisfied by ϕ+ or Γ+. For example, if we want to estimate a
reaction rate hΣϕi and ϕ is determined by Aϕ = S, we construct the Roussopolos
functional Rvar{ϕ+, ϕ} = hΣϕi □ hϕ+, (S □ Aϕ)i of Eq. (13.56), and find from the
stationarity requirement that ϕ+ must satisfy A+ϕ+ = Σ. As another example, if we
want to estimate the reactivity worth ϕ+
0 ; (λ0ΔF □ ΔA)ϕ
= ϕ+
0 ; Fϕ
of changes
ΔF and ΔA leading from (A0 □ λ0F0)ϕ0 = 0 to (A □ λF)ϕ = 0, we construct
ρvarfϕ+
0 ; ϕ; Γ+g = ϕ+
0 ; (λ0ΔF □ ΔA)ϕ
= ϕ+
0 ; Fϕ
[1 □ Γ+; (A □ λF)ϕ
h
i] of Eq.
(13.29).

## 13.7 Variational Estimate of Intermediate Resonance Integral

Consider, as an application, the elastic slowing down of neutrons in the presence
of a resonance absorber and a moderator (m), which is described by
[σm + σ(u)]ϕ(u) = ∫
u
u□Δm
du´ e(u´□u)
1 □ αm
σmϕ(u´)
+ ∫
u
u□Δ
du´ e(u´□u)
1 □ α σs(u´)ϕ(u´)
' σm + ∫
u
u□Δ
du´ e(u´□u)
1 □ α σs(u´)ϕ(u´)
(13.65)
where σm, σ, and σs are moderator scattering cross section per atom of
resonance absorber and the total and scattering microscopic cross sections
of the resonance absorber, respectively. It has been assumed that the moderator
in-scatter integral can be evaluated using the asymptotic flux, which is
constant in lethargy, and the constant has been chosen as unity, in writing the
second form of the equation. This equation corresponds to the second of
Eq. (13.58).
The quantity of physical interest is the resonance integral
I = ∫σa(u)ϕ(u)du = hσaϕi
(13.66)
Using the definition of adjoint operator given by Eq. (13.14), where h□i now
indicates an integral over lethargy, the first of Eq. (13.58) – the adjoint equation –

<!-- page 520 (PDF 538) -->
for this problem is
σm + σ(u)
[
]ϕ+
R(u) □ ∫
u+Δ
u
du´ e(u□u´)
1 □ α σs(u)ϕ+
R(u´) = σa(u)
(13.67)
and the Schwinger variational functional of Eq. (13.61) becomes
Jfϕ; ϕ+
Rg = hΣϕihϕ+
RSi
hϕ+
R; Aϕi
=
[∫
du σa(u)ϕ(u)][∫
du ϕ+
R(u)σm]
∫
du ϕ+
R(u)f[σm + σ(u)]ϕ(u) □ ∫
u
u□Δ
du´[e(u´□u)=(1 □ α)]σs(u´)ϕ(u´)g
(13.68)
In choosing trial functions, we recall the narrow resonance and wide resonance
approximations of Chapter 4:
ϕNR(u) = σm + σp
σm + σ(u) ;
ϕWR(u) =
σm
σm + σa(u)
(13.69)
where σp is the background scattering cross section of the resonance absorber.
Making similar approximations in Eq. (13.67) as were made in deriving Eq.
(13.69), we can derive approximate adjoint functions. For wide resonances, σsϕ+
R
is approximately constant over the scattering interval and can be removed from
the integral in Eq. (13.67), yielding
ϕ+
WR(u) =
σa(u)
σm + σa(u)
(13.70)
In the limit of very narrow resonances, the off-resonance form for σsϕ+
R can be
used to evaluate the scattering integral to obtain
ϕ+
NR(u) = σa(u)
σm
σm + σp
σm + σ(u)
(13.71)
These results suggest the trial functions
ϕλ(u) =
σm + λσp
σm + σa(u) + λσs(u)
ϕ+
κ (u) = σm + κσp
σm
σa(u)
σm + σa(u) + κσs(u)
(13.72)
