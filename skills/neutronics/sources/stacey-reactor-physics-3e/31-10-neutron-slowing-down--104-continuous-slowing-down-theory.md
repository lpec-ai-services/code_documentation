# 10 Neutron Slowing Down — 10.4 Continuous Slowing-Down Theory … Problems
<!-- source PDF pages 431-447 -->

<!-- page 411 (PDF 431) -->
extrapolation distance is typically very small relative to the physical dimensions,
the approximate boundary condition of vanishing flux on the physical boundary is
appropriate as an approximation to Eq. (10.65):
ϕ(rb; u) = 0;
ϕg(rb) = 0
(10.68)
As an approximation to the interface condition of Eq. (10.66), we require that
the first two Legendre moments of this equation be satisfied:
∫ψ(ri − ε; Ω; u)dΩ = ∫ψ(ri + ε; Ω; u)dΩ
∫ni ? Ωψ(ri − ε; Ω; u)dΩ = ∫ni ? Ωψ(ri + ε; Ω; u)dΩ
(10.69)
Using the definitions of scalar flux and current as the first two Legendre moments
of the angular flux, this may be written as
ϕ(ri − ε; u) = ϕ(ri + ε; u)
ni ? J(ri − ε; u) = ni ? J(ri + ε; u)
(10.70)
and for multigroup diffusion theory,
ϕg(ri − ε) = ϕg(ri + ε)
ni ? Jg(ri − ε) = ni ? Jg(ri + ε)
(10.71)

## 10.4 Continuous Slowing-Down Theory

Over much of the slowing-down range above (in lethargy) the fission spectrum and
below the thermal range, neutron slowing down is due primarily to elastic scattering.
Since there is no lethargy decrease in a scattering event below (in lethargy) the
thermal range, the scatter-in integral is over lower lethargies only. It has been found
convenient forcomputationalpurposes to replace the elastic scatter-in integralwitha
lethargy derivative of the associated elastic slowing-down density, which is computed
in a coupled calculation, rather than evaluating the scatter-in integral directly. The
variouscomputational methods that have been developed for this purpose are known
collectively as continuous slowing-down theory.

### P1 Equations in Slowing-Down Density Formulation

Generalizing the definition of slowing-down density introduced in Chapter 4 to
include anisotropic scattering, the isotropic slowing-down density is defined as the
number of neutrons slowing down past energy E, or lethargy u, by isotropic (in the

<!-- page 412 (PDF 432) -->
lab system) elastic scattering:
qi
0(x; u) ≡ ∫
u
du´
∫
u
du´´Σi
s0(x; u´ ! u´´)ϕ(x; u´)
(10.72)
and the linearly anisotropic slowing-down density is defined as the number of
neutrons slowing down past lethargy u by linearly anisotropic scattering:
qi
1(x; u) ≡ ∫
u
du´
∫
u
du´´Σi
s1(x; u´ ! u´´)J(x; u´)
(10.73)
These two slowing-down densities are the zeroth and first Legendre components
of the angular-dependent neutron slowing-down density.
Making use of Eq. (10.20), the first of these equations can be written explicitly as
qi
0(x; u) ≡ ∫
u
u−ln1=αi
du´
∫
u+ln1=αi
u
Σi
s(u´) eu´−u´´
1 − αi
ϕ(x; u´)du´´
= ∫
u
u−ln1=αi
du´Σi
s(u´) eu´−u − αi
1 − αi
ϕ(x; u´)
(10.74)
and making use of Eq. (10.23), the second of these equations can be written
explicitly as
qi
1(x; u) = ∫
u
u−ln1=αi
du´
∫
u+ln1=αi
u
du´´ Σi
s(u´)eu´−u´´
1 − αi
□ 1 + 3μc(u´) 1 − 2(1 − eu´−u´´)
1 − αi

J(x; u´)du´´
(10.75)
where Ai is the atomic mass in amu of the scattering nuclei and αi = [(Ai − i)/
(Ai + 1)]2.
These slowing-down densities can be related to the scatter-in integrals in the P1
equations given by Eqs. (10.36) and (10.37):
@qi
@u = ∫
u
du´´Σi
s0(x; u ! u´´)ϕ(x; u) − ∫
u
du´Σi
s0(x; u´ ! u)ϕ(x; u´)
= Σi
s(x; u)ϕ(x; u) − ∫
u
du´Σi
s0(x; u´ ! u)ϕ(x; u´)
(10.76)
@qi
@u = ∫
u
du´´Σi
s1(x; u ! u´´)J(x; u) − ∫
u
du´Σi
s1(x; u´ ! u)J(x; u´)
= μi
0Σi
s(x; u)J(x; u) − ∫
u
du´Σi
s1(x; u´ ! u)J(x; u´)
(10.77)

<!-- page 413 (PDF 433) -->
Using Eqs. (10.76) and (10.77) to eliminate the scatter-in integrals in
Eqs. (10.36) and (10.37) yields an equivalent form of the P1 equations (written
for one-dimensional slab geometry):
@J(x; u)
@x
+ Σne(x; u)ϕ(x; u) = −
X
I
i=1
@qi
@u (x; u) + S0(x; u)
(10.78)
@ϕ(x; u)
@x
+ Σtr(x; u)J(x; u) = −
X
I
i=1
@qi
1(x; u)
@u
+ S1(x; u)
(10.79)
where the nonelastic cross section
Σne(x; u) ≡ Σt(x; u) −
X
I
i=1
Σi
s(x; u)
(10.80)
and the transport cross section
Σtr(x; u) ≡ Σt(x; u) −
X
l
i=1
μi
0Σi
s(x; u)
(10.81)
have been defined in a natural way.
Integrating these equations over Δug = ug+1 − ug leads to the multigroup P1
equations in the slowing-down density formulation of elastic scattering:
@Jg(x)
@x
+ Σg
ne(x)ϕg(x) = −
X
I
i=1
[qi
0(x; ug+1) − qi
0(x; ug)] + Sg
0(x)
(10.82)
@ϕg(x)
@x
+ Σg
tr(x)Jg(x) = −
X
I
i=1
[qi
1(x; ug+1) − qi
1(x; ug)] + Sg
1(x)
g = 1; . . . ; G
(10.83)
where the multigroup quantities are defined as
ϕg(x) ≡ ∫
ug+1
ug
duϕ(x; u);
Jg(x) ≡ ∫
ug+1
ug
duJ(x; u)
Sg
n(x) ≡ ∫
ug+1
ug
duSn(x; u)
Σg
ne(x) ≡ ∫
ug+1
ug
duΣne(x; u) ϕ(x; u)
ϕg(x)
Σg
tr(x) ≡ ∫
ug+1
ug
duΣtr(x; u) J(x; u)
Jg(x)
(10.84)

<!-- page 414 (PDF 434) -->
In this formulation, the natural definition of the group-averaged transport
equation is as a current-averaged quantity.
The same type of difficulty encountered previously in reducing the energydependent
P1 equations to diffusion theory is present in Eq. (10.83); to obtain a
Fick’s law type of relationship J = −Ddϕ/dx, it is necessary to require that the
anisotropic source Sg
1 vanishes and that the anisotropic slowing-down density
does not change over the group, which would be the case if it was assumed to be
identically zero. Making these assumptions, the multigroup diffusion equation in
the slowing-down density formulation is
− @
@x
3Σg
tr(x)
@ϕg(x)
@x

+ Σg
ne(x)ϕg(x)
=
X
I
i=1
[qi
0(x; ug) − qi
0(x; ug + 1)] + Sg
0(x)
(10.85)
with the diffusion coefficient being unambiguously defined in terms of a current
spectrum-weighted group-averaged transport cross section, which contains some
anisotropic effects – the average cosines of the scattering angle of the various
nuclear species are embedded in the definition of the transport coefficient given
by Eq. (10.81).
Making the approximation that the spatial dependence can be represented by a
simple buckling [i.e., ϕ(x, u) = ϕ(u) exp(iBx), J(x, u) = J(u) exp(iBx)] in Eqs. (10.82)
and (10.83) reduces these equations to the forms that are found in various
multigroup spectrum codes:
iBJg + Σg
neϕg
=
X
J
i=1
[qi
0(ug) − qi
0(ug+1)] + Sg
3 iBϕg + Σg
trϕg =
X
J
i=1
[qi
1(ug) − qi
1(ug+1)] + Sg
1;
g = 1; . . . ; G
(10.86)
The asymptotic forms ϕasy(u) ∼1 and J(u)asy ∼1 are used in Eq. (10.84) to define
fine- or ultrafine-group constants. The few-group constants are then constructed
from the solutions ϕg and Jg of the fine- or ultrafine-group calculation:
Σk
ne(X) =
P
g∈kΣg
ne(x)ϕg(x)
P
g∈kϕg(x)
Σk
tr(X) =
P
g∈kΣg
tr(x)Jg(x)
P
g∈kJg(x)
(10.87)
where g ∈k indicates that the sum is over fine groups g within few group k.

<!-- page 415 (PDF 435) -->
### Slowing-Down Density in Hydrogen

The evaluation of the slowing-down densities in hydrogen is quite straightforward
because a neutron can scatter from any lethargy to any greater lethargy in a single
collision, which is implicit in the fact that αH = 0. This fact allows Eqs. (10.72) and
(10.73) to be written as
qH
0 (x; u) = ∫
u
du´ΣH
s (u´)eu´−uϕ(x; u´)
(10.88)
q1(x; u) = 2
3 ∫
u
du´ΣH
s (u´)e3(u´−u)=2J(x; u´)
(10.89)
These equations may be differentiated to obtain
@qH
@u + qH
0 (x; u) = ΣH
s (u)ϕ(x; u)
(10.90)
@qH
@u + 3
2 qH
1 (x; u) = 2
3 ΣH
s (u)J(x; u)
(10.91)
which may be put in multigroup form, to be used with Eq. (10.86), by integration
over Δug:
qH
0 (ug+1) − qH
0 (ug)

+ 1
2 qH
0 (ug+1) + qH
0 (ug)

Δug = Σ
Hg
S ϕg
qH
1 (ug+1) − qH
1 (ug)

+ 3
4 qH
1 (ug+1) + qH
1 (ug)

Δug = 2
3Σ
Hg
S Jg
(10.92)

### Heavy Mass Scatterers

For moderators other than hydrogen, this procedure does not lead to such a simple
differential equation for the slowing-down density, precisely because it is not
possible for a neutron to lose all of its energy in a single collision, which means that
the lower limits on the first integral in Eqs. (10.72) and (10.73) are u − ln(1/αi), not
zero. At the other extreme from hydrogen are heavy mass nuclei for which the
maximum lethargy gain in a scattering collision is quite small and it is reasonable to
expand the integrands in Eqs. (10.72) and (10.73) in Taylor’s series:
Σi
s(u´)ϕ(u´) ' Σi
s(u)ϕ(u) + (u´ − u) @
@u Σi
s(u)ϕ(u)

+ ∙∙∙
(10.93)
Σi
s(u´)J(u´) ' Σi
s(u)J(u) + (u´ − u) @
@u Σi
s(u)J(u)

+ ∙∙∙
(10.94)
Various approximations result from keeping different terms in these expansions.

<!-- page 416 (PDF 436) -->
### Age Approximation

The simplest such approximation, resulting from retaining only the first term in
Eq. (10.93) and setting qi
1 = 0, is known as the age approximation:
qi
0(x; u) ' ξiΣi
s(x; u)ϕ(x; u)
(10.95)
where ξi = ξiso
i
given by Eq. (10.21). With these approximations for qi
0 and qI
1,
Eqs. (10.78) and (10.79) become the inconsistent (because of the neglect of qi
1) P1
equations:
@J
@x (x; u) + Σne(x; u)ϕ(x; u)
= −
X
I
i=1
@
@u ξiΣi
s(x; u)ϕ(x; u)

+ S0(x; u)
@ϕ(x; u)
@x
+ Σtr(x; u)J(x; u) = S1(x; u)
(10.96)
which, with the additional assumption of zero anisotropic source (S1 = 0), can be
reduced to the age-diffusion equation:
− @
@x
3Σtr(x; u)
@ϕ(x; u)
@x

+ Σne(x; u)ϕ(x; u)
= −
X
l
i=1
@
@u ξiΣi
s(x; u)ϕ(x; u)

+ S0(x; u)
(10.97)

### Selengut–Goertzel Approximation

The age approximation for the slowing-down density, and hence the inconsistent
P1 and age-diffusion equations are restricted to heavy mass moderators for which
the interval of the scatter-in integral, ln(1/αi), is quite small, and certainly would not
be appropriate for hydrogen. For a mixture of hydrogen and heavy mass moderators
, the hydrogen can be treated exactly and the age approximation can be used for
the remaining nuclei, resulting in the Selengut–Goertzel approximation
X
l
i=1
@qi
@u = @qH
@u +
X
l
i≠H
@
@u (ξiΣi
sϕ)
(10.98)

### Consistent P1 Approximation

If, instead of setting qi
1 = 0, Eq. (10.73) is evaluated retaining the first term of the
Taylor’s series expansion of Eq. (10.94), to obtain
qi
1(x; u) ' ξ1
i Σi
s(x; u)J(x; u)
(10.99)

<!-- page 417 (PDF 437) -->
where the first Legendre moment of the mean lethargy gain is defined as
ξ1
i = (Ai + 1)2
1 + 1=Ai
1 − α3=2
i
2 ln 1
αi
+ 1

− (1 − 1=Ai) 1 − α1=2
i
2 ln 1
αi
+ 1

(10.100)
the consistent P1 equations (with the Selengut–Goertzel approximation) are
obtained:
@J(x; u)
@x
+ Σne(x; u)ϕ(x; u)
= −
X
l
i≠H
@
@u ξiΣi
s(x; u)ϕ(x; u)

− @qH
@u (x; u) + S0(x; u)
(10.101)
@ϕ(x; u)
@x
+ Σtr(x; u) + ξ1
i Σi
s(x; u)

J(x; u) = S1(x; u)
(10.102)

### Extended Age Approximation

If the first two terms in the Taylor’s series expansion of Eq. (10.93) are retained in
evaluating Eq. (10.72), the result is
qi
0(x; u) ' ξiΣi
s(x; u)ϕ(x; u) + ai
ξi
@q0(x; u)
@u
(10.103)
where
ai = ∫
u
u−ln1=αi
du´ eu´−u − αi
1 − αi
(u´ − u) = αi[ln(1=αi)]2
2(1 − αi)
− ξi
(10.104)
Using the balance equation for the elastic slowing-down density in a very large
region (neglecting leakage)
@q0(u)
@u
= −Σne(u)ϕ(u)
(10.105)
allows Eq. (10.103) to be written as
q0(x; u) '
X
i
ξiΣi
s(x; u) − ai
ξi
Σne(x; u)

ϕ(x; u)
' ξΣt(x; u)ϕ(x; u)
(10.106)
With this extended age approximation, the summation on the right in the first
of Eq. (10.101) is replaced by −d(ξΣtϕ)/du in the age-diffusion equations.

<!-- page 418 (PDF 438) -->
### Grueling–Goertzel Approximation

The slowing-down density for hydrogen can be calculated exactly, and the
slowing-down density for heavy mass nuclei can be well approximated by one
of the variants of the age approximation given above. However, light nonhydrogen
moderators are not well approximated by any of the age approximations above.
Greater accuracy can obviously be obtained by retaining more terms in the
Taylor’s series expansions of Eqs. (10.93) and (10.94). In addition, it is possible to
construct an approximate equation for the isotopic slowing-down densities that
has the same form as the simple differential equation that describes the hydrogen
slowing-down density and that reduces to the hydrogen equation when Ai = 1.
Retaining three terms in the Taylor series expansion of Eq. (10.93) when used with
Eq. (10.72) to evaluate λi
0dqi
0=du + qi
0 yields
λi
@qi
@u + qi
0 ' λi
0 ξi
@
@u (Σi
sϕ) + ai
@2(Σi
sϕ)
@u2

+ ξiΣi
sϕ + ai
@(Σi
sϕ)
@u

(10.107)
The objective is to develop an equation for qi
0 that is like Eq. (10.90) for hydrogen.
Neglecting @2ϕ/@u2 and choosing λi
0 to make the @ϕ/@u term vanish leads to
λi
@qi
@u (x; u) + qi
0(x; u) = ξiΣi
s(x; u)ϕ(x; u)
(10.108)
which is of the same form as Eq. (10.90) for the hydrogen slowing-down density
where
λi
0 = 1 − αi 1 + ln(1=αi) + 1
2[ln(1=αi)]2
1 − αi[1 + ln(1=αi)]
(10.109)
Retaining the first three terms in the Taylor series expansion of Eq. (10.94)
when used with Eq. (10.73) in a similar calculation leads to an equation similar to
the hydrogen Eq. (10.91):
λi
@qi
@u (x; u) + qi
1(x; u) = ξ1
i Σi
s(x; u)J(x; u)
(10.110)
where
λi
1 = − (1 + 1=Ai)2
4=Ai
1 + 1=Ai
9 − α3=2
i
ln 1

− 4
3 ln 1
αi
+ 8
"
(
)
!
"
−
1 − 1
Ai

8 − α1=2
i
ln 1
αi

− 4 ln 1
αi
+ 8
"
(
)#,
ξ1
i
(10.111)
again has been chosen to make @ϕ/@u terms vanish.

<!-- page 419 (PDF 439) -->
### Summary of Pl Continuous Slowing-Down Theory

The Pl equations
@J(x; u)
@x
+ Σne(x; u)ϕ(x; u)
= − @qH
0 (x; u)
@u
−
X
i≠H
@qi
0(x; u)
@u
+ S0(x; u)
@ϕ(x; u)
@x
+ Σtr(x; u)J(x; u)
= − @qH
1 (x; u)
@u
−
X
i≠H
@qi
1(x; u)
@u
+ S1(x; u)
(10.112)
and the equations for the elastic slowing-down density, using the exact equations
for hydrogen and the Grueling–Goertzel approximation for nonhydrogen nuclei,
@qH
@u (x; u) + qH
0 (x; u)
= ΣH
s (x; u)ϕ(x; u)
@qH
@u (x; u) + qH
1 (x; u) = 4
9 ΣH
s (x; u)J(x; u)
λi
@qi
@u (x; u) + qi
0(x; u) = ξiΣi
s(x; u)ϕ(x; u)
λi
@qi
@u (x; u) + qi
1(x; u) = ξ1
i Σi
s(x; u)J(x; u)
(10.113)
represent the formulation usually referred to as Pl continuous slowing-down
theory.

### Inclusion of Anisotropic Scattering

In an ultrafine-group calculation for which the group width is less than ln(1/αi) for
some of the nuclei that contribute strongly to neutron moderation, it is necessary
to retain a large number of Legendre moments to accurately represent the group
transfer cross sections, which actually represent the probabilities for scattering to
within relatively small angular intervals. (This situation is more likely to be found
in a fast than in a thermal reactor.) The concept of slowing-down density can be
extended to a higher order of anisotropy by defining the Legendre moments of the
slowing-down density as the number of neutrons slowing down past lethargy u by
the lth Legendre moment of the elastic scattering transfer function:
qi
l(u) ≡ ∫
u
du´
∫
u
du´´Σi
sl(u´ ! u´´)ϕl(u´)
(10.114)

<!-- page 420 (PDF 440) -->
where, recalling Eq. (10.38), we have
Σi
sl(u´ ! u) = Niσi
s(u´)
X
l´=0
Ti
ll´(U) bc
l´i(u´)
bc
0i(u) ≡
X
l´=0
Ti
ll´(U)Σi
sl´(u´)
(10.115)
Making a general Taylor series expansion about u in the integrand in
Eq. (10.114),
Σi
sl´(u´)ϕl´(u´) =
X
n=0
(u´ − u)n
n!
dn
dun Σi
sl´(u)ϕl´(u)

(10.116)
and using Eq. (10.115) yields
qi
l(u) = −
X
n=0
dn
dun Gi
l;n+1(u)ϕl(u)
h
i
(10.117)
where
Gi
l;n(u) =
X
l´=0
Σi
sl´(u) 2l´ + 1
2n!
∫
u
u−ln1=αi
du´
∫
u+ln1=αi
u
du´´Pl μ0(u´ − u´´)

□Pl μc(u´ − u´´)

(u´ − u)n 2eu´−u´´
1 − αi
≡
X
l´=0
Σi
sl´(u)Ti
ll´;n(u)
(10.118)
Extending the calculation that was described for the Grueling–Goertzel approximation
yields an equation for each Legendre moment of the slowing-down density
λl(u) dql
du (u) + ql(u)
= −
X
I
i
(
Gi
l;1(u)ϕl(u) 1 − dλl(u)
du

+
X
n=2
dn[Gi
l;n+1(u)ϕl(u)]
dun
+ λl(u) dn[Gi
l;n(u)ϕl(u)
dun
"
#)
(10.119)
where
λl(u)
P
i
P1
l´=0 Ti
ll´;2(u)Σi
sl´(u)
P
i
P1
l´=0 Ti
ll´;1(u)Σi
sl´(u) =
P
iGi
l;2(u)
P
iGi
l;1(u)
(10.120)
are chosen to eliminate first derivative terms involving ϕl.

<!-- page 421 (PDF 441) -->
The conventional Grueling–Goertzel theory is recovered by retaining only the
l = 0, 1 slowing-down moments, neglecting terms n □ 2 in Eq. (10.119) and
identifying
ξl
i(u) = −Gi
l;1(u)
Σs(u)
ai
l(u) =
−Gi
l;2(u)
Σs(u)
(10.121)

### Inclusion of Scattering Resonances

An impractically large number of terms may have to be retained in the Taylor’s
series expansion to obtain an accurate approximation for the slowing-down
density when resonance scattering nuclei are present in the mixture because
resonance scattering in nuclei j may cause ϕ, hence Σi
sϕ for another nuclear
species i, to be a rapidly varying quantity. In this case, a better approximation may
be developed by expanding the total collision density in a Taylor’s series:
Σt(u´)ϕl(u´) =
X
n=0
(u´ − u)n
n!
dn[Σt(u)ϕl(u)]
dun
(10.122)
Using this expansion to evaluate Eq. (10.114) yields
ql(u) = −
X
i
X
n=0
Hi
l;n(u) dn[Σt(u)ϕl(u)]
dun
(10.123)
where
Hi
l;n(u) ≡ 1
n!
X
l´=0
2 (2l´ + 1)∫
u
u−ln1=αi
du´
∫
u+ln1=αi
n
du´´Pl μ0(u´ − u´´)

□ Pl´ μc(u´ − u´´)

 2eu´−u´´
1 − αi
Σi
sl´(u´)
Σt(u) (u´ − u)n
(10.124)
Differentiating Eq. (10.123),
dql(u)
du
= −
X
i
X
n=0
Hi
l;n(u) dn+1[Σt(u)ϕl(u)
dun+1
"
+
X
n=0
dHi
l;n(u)
du
? dn[Σt(u)ϕl(u)]
dun
(10.125)
and carrying out a calculation similar to those described previously results in a
hydrogen-like equation for the lth Legendre component of the slowing-down

<!-- page 422 (PDF 442) -->
density:
^λl(u) dql(u)
du
+ ql(u) = −
X
i
Hi
l;0(u) + ^λl(u) dHi
l;0(u)
du
"
Σt(u)ϕl(u)
(
+
X
n=2
Hi
l;n(u) dn[Σt(u)ϕl(u)]
dun

+ ^λl(u)Hi
l;n−1(u) dn[Σt(u)ϕl(u)]
dun
+ ^λl(u)
dHi
l;n(u)
du
dn[Σt(u)ξl(u)]
dun
#)
(10.126)
where
^λl(u) = −
P
iHi
l;1(u)
P
i[Hi
l;0(u) + dhi
l;1(u)=du]
(10.127)
has been chosen to eliminate first derivative terms involving ϕl.

### Pl Continuous Slowing-Down Equations

The lethargy-dependent Pl equations are generalized from the one-speed Pl
equations of Chapter 9 by including a scattering loss term and a scatter-in source
of neutrons:
l + 1
2l + 1
@ϕl+1(x; u)
@x
+
l
2l + 1
@ϕl−1(x; u)
@x
+ Σt(x; u)ϕl(x; u)
= ∫
u
du´Σs;l(x; u´ ! u)ϕl(x; u´) + Sl(x; u);
l = 1; . . . ; L
(10.128)
The Legendre moments of the slowing-down density are related to the
Legendre moments of the scatter-in integral. Differentiating Eq. (10.114) yields
@ql(u)
@u
= Σs;l(u)ϕl(u) − ∫
u
du´Σs;l(u´ ! u)ϕl(u´)
(10.129)
Using this result to eliminate the elastic scatter-in integral in Eq. (10.128) leads to
the Pl continuous slowing-down equations:
l + 1
2l + 1
@ϕl+1(x; u)
@x
+
l
2l + 1
@ϕl−1(x; u)
@x
+ Σl
ne(x; u)ϕl(x; u)
= − @ql(x; u)
@u
+ Sl(x; u);
l = 1; . . . ; L
(10.130)

<!-- page 423 (PDF 443) -->
where the nonelastic cross section is
Σl
ne(x; u) ≡ Σt(x; u) − Σs;l(x; u)
(10.131)
and the Legendre moments of the slowing-down density are calculated from
Eq. (10.126) for nonhydrogenic nuclei and Eqs. (10.90) and (10.91) and similarly
derived higher Legendre moment equations for hydrogen.

## 10.5 Multigroup Discrete Ordinates Transport Theory

In situations in which a high degree of angular anisotropy in the neutron flux
could be expected, the low-order P1 and diffusion theory approximations might
be inadequate to treat the combined slowing down and transport of neutrons.
Such situations might arise in the treatment of slowing down in a highly
heterogeneous lattice consisting of materials of very different properties or in
the treatment of problems in which there is a highly directional flow of fast
neutrons from one region to another. For such situations, the discrete ordinates
methods of Chapter 9, extended to treat the neutron slowing down, are well
suited. Generalizing the expansion of the differential (over scattering angle)
elastic scattering cross section of Eq. (9.179) to an expansion of the double
differential (over scattering angle and lethargy change) scattering cross section,
and using the addition theorem for Legendre polynomials of Eq. (9.177) to relate
the cosine of the scattering angle, μ0, to the cosines of the incident, μ´, and exiting,
μ, directions for the scattering event, yields
Σs(r; Ω´ ? Ω; u´ ! u)
=
X
L
l´=0
2l´ + 1
4π
Σsl´(r; u´ ! u)Pl(μ0)
=
X
L
l´=0
2l´ + 1
4π
Σsl´(r; u´ ! u)
X
l´
m=−l´
Y l´m(μ; φ)Y ∗
l´m(μ´; φ´)
=
X
L
l´=0
2l´ + 1
4π
Σsl´(r; u´ ! u)
□ Pl´(μ)Pl´(μ´) + 2
X
l´
m=1
(l´ − m)!
(l´ + m)! Pm
l´ (μ)Pm
l´ (μ´)cosm(φ − φ´)
"
(10.132)
Using this representation of the double differential scattering cross section in the
neutron transport equation (10.26) yields
Ω ? ∇ψ(r; Ω; u) + Σt(r; u)ψ(r; Ω; u)
= Sex(r; Ω; u) + ∫
du´X
L
l´=0
Y l´m(Ω)Σsl´(r; u´ ! u)ϕl´m(r; u´)
+ χ(u)
4π ∫
du´vΣf (r; u´)ϕ(r; u´)
(10.133)

<!-- page 424 (PDF 444) -->
where the Legendre moments of the angular flux, ϕlm, and the scalar flux, ϕ, are
defined as
ϕlm(r; u´) ≡ ∫4π
dΩ´Y ∗
lm(Ω´)ψ(r; Ω´; u´)
ϕ(r; u´) = ϕ00(r; u´) ≡ ∫4π
dΩ´ψ(r; Ω´; u´)
(10.134)
These equations may be reduced to a set of multigroup equations by integrating
over the lethargy width Δug = ug+1 − ug of group g:
Ω ? ∇ψg(r; Ω) + Σg
t (r)ψg(r; Ω)
= Sg
ex(r; Ω) +
X
G
g´=1
X
L
l´=0
Y l´m(Ω)Σg´!g
sl´
(r)ϕg´
l´m(r)
+ χg
4π
X
G
g´=1
vΣg´
f (r)ϕg´(r);
g = 1; . . . ; G
(10.135)
where multigroup quantities have been defined
ψg(r; Ω) ≡ ∫Δug
duψ(r; Ω; u)
ϕg
lm(r)
≡ ∫Δug
duϕlm(r; u)
ϕg(r)
≡ ∫Δug
duϕ(r; u)
χg
≡ ∫Δug
duχ(u);
Sg
ex(r; Ω) ≡ ∫Δug
duSg
ex(r; Ω; u)
Σg
t (r)
≡
∫
4π
dΩ∫Δug
duΣt(r; u)ψ(r; Ω; u)
∫
4π
dΩ∫Δug
duψ(r; Ω; u)
=
∫Δug
duΣt(r; u)ϕ(r; u)
∫Δug
duϕ(r; u)
vΣg
f (r)
≡
∫Δug
duvΣf (r; u)ϕ(r; u)
∫Δug
duϕ(r; u)
Σg´!g
sl
(r) ≡
∫Δug
du∫Δug´
du´Σsl(r; u´ ! u)ϕlm(r; u´)
∫Δug´
du´ϕlm(r; u´)
(10.136)

<!-- page 425 (PDF 445) -->
Writing Eq. (10.135) for each discrete ordinate, Ωn, results in the set of multigroup
discrete ordinates equations
Ωn:∇ψg(r; Ωn) + Σg
t ψg(r; Ωn) = Qg(r; Ωn)
g = 1; . . . ; G
(10.137)
where the group scattering plus fission plus external source term is
Qg(r; Ωn) ≡
X
G
g´=1
X
L
l´=0
Y l´m(Ωn)Σg´!g
sl´
(r)ϕg´
l´m(r)
+ χg
4π
X
G
g´=1
vΣg´
f (r)ϕg´(r) + Sg
ex(r; Ωn)
(10.138)
Equation (10.137), for each group, is of the same form as the discrete
ordinates equation discussed in Chapter 9. Thus, the methods used to solve
the discrete ordinates equations in Chapter 9 can be applied to solve the
multigroup discrete ordinates equations, on a group-by-group basis. For a given
fission and scattering source, the multigroup discrete ordinates equations are
solved group by group using the methods of Chapter 9. Then on the source
iteration, the new scattering and fission source for each group are constructed
by summing over contributions from all groups, and the solution for the
multigroup fluxes on a group-by-group basis is repeated until convergence.
The power iteration procedure for criticality eigenvalue calculations is the same
as discussed in Chapter 9, but now the fission source is summed over the
contributions from all groups.

## References

1 A. F. HENRY, Nuclear Reactor Analysis, MIT Press, Cambridge, MA (1975),
pp. 359–367 and 386–423.
2 B. J. TOPPEL, A. L. RAGO, and D. M. O’SHEA, MC2: A Code to Calculate
Multigroup Cross Sections, ANL-7318, Argonne National Laboratory, Argonne,
IL (1967).
3 H. BOHL, JR., E. M. GELBARD, and G. H. RYAN, MUFT-4: A Fast Neutron
Spectrum Code, WAPD-TM-22, Bettis Atomic Power Laboratory, West Miflin,
PA (1957).
4 R. A. KNIEF, Nuclear Engineering, 2nd ed., Taylor & Francis, Washington, DC
(1992).

## Further Reading

AMSTER H. J., “Heavy Moderator Approximations in Neutron Transport Theory,”
J. Appl. Phys. 29, 623 (1958).

<!-- page 426 (PDF 446) -->
DUDERSTADT J. J. and HAMILTON L. J., Nuclear Reactor Analysis, Wiley, New York
(1976), pp. 347–369.
FERZIGER J. H. and ZWEIFEL P. F., The Theory of Neutron Slowing Down in Nuclear
Reactors, MIT Press, Cambridge, MA (1966).
GOERTZEL G. and GRUELING E., “Approximate Method for Treating Neutron Slowing
Down,” Nucl. Sci. Eng. 7, 69 (1960).
SELENGUT D. S. et al., “The Neutron Slowing Down Problem,” in A. RADKOWSKY, ed.,
Naval Reactors Physics Handbook, U.S. Atomic Energy Commission, Washington,
DC (1964).
STACEY W. M., “The Effect of Wide Scattering Resonances on Neutron Multigroup
Cross Sections,” Nucl. Sci. Eng. 47 29 (1972); “The Effect of Anisotropic
Scattering upon the Elastic Moderation of Fast Neutrons,” Nucl. Sci. Eng. 44, 194
(1971); “Continuous Slowing Down Theory for Anisotropic Elastic Moderation in
the Pn and Bn Representations,” Nucl. Sci. Eng. 41, 457 (1970).
WILLIAMS M. M. R., The Slowing Down and Thermalization of Neutrons, North-
Holland, Amsterdam (1966), pp. 317–516.

## Problems

### 10.1

Calculate the average cosine of the scattering angle in the CM system for
neutrons at 1 MeV, 100 keV, and 1 keV colliding with uranium, iron,
carbon, and hydrogen.

### 10.2

Calculate the values of the average lethargy increase, ξ, and the average
cosine of the scattering angle in the lab system, μ0, for the neutron energies
and nuclei of Problem 10.1, for isotropic scattering and for linearly
anisotropic scattering.

### 10.3

Carry through the steps in the derivation of the lethargy-dependent P1
equations given by Eqs. (10.36) and (10.37).

### 10.4

Carry through the derivation of the isotropic and linearly anisotropic
lethargy transfer functions of Eqs. (10.39) and (10.40).

### 10.5

Divide the energy interval 10 MeV > E > 1 eV into 54 equal-lethargy
intervals. Evaluate the multigroup scattering transfer functions Σg´!g
s0
for carbon for g´ = 1, 10, and 50.

### 10.6

Carry through the steps in the derivation of the lethargy-dependent B1
equations given by Eqs. (10.50).

### 10.7

Solve for the lethargy-dependent neutron flux and current in an infinite
medium, using the age approximation of Eq. (10.96).

### 10.8

Derive a differential equation similar to Eqs. (10.90) and (10.91) for the
higher Legendre moments of the slowing-down density in hydrogen.

<!-- page 427 (PDF 447) -->
### 10.9

Derive the multigroup approximation for the P1 continuous slowing-down
equations, Eqs. (10.112) and (10.113).
10.10 Write a computer code to solve the multigroup P1 continuous slowingdown
equations of Problem 10.9 for an assembly consisting of 3%
enriched, zircalloy-clad UO2 and water. The fuel pins are 1 cm in
diameter with clad thickness of 0.05 cm in a square array with fuel
pin center-to-center distance of 2.0 cm. Assume that spatial gradients
can be neglected.
