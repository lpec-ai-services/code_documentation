# 12 Neutron Thermalization — 12.4 Calculation of the Thermal Neutron Spectra in Homogeneous Media … References
<!-- source PDF pages 497-516 -->

<!-- page 478 (PDF 497) -->
## 12.4 Calculation of the Thermal Neutron Spectra in Homogeneous Media

Turning now to the calculation of the neutron energy spectrum, the neutron
balance equation for thermal neutrons, neglecting leakage, is
[Σa(E) + Σs(E)]v(E)n(E) = ∫
dE´Σs0(E´ !E)v(E´)n(E´)
(12.37)
The principle of detailed balance for a neutron distribution in equilibrium,
M(E´; T)Σs0(E´ ! E) = M(E; T)Σs0(E ! E´)
(12.38)
where M(E, T) is the Maxwellian neutron particle distribution at temperature T,
M(E; T) =
2π
(πkT)3=2
ffiffiffi
E
p
exp □ E
kT

(12.39)
is quite important in developing solutions for the thermal neutron distribution.
10.0
YOUNG-KOPPEL
FREQUENCY SPECTRUM
YOSHIMORI-KITANO
FREQUENCY SPECTRUM
8.0
6.0
4.0
2.0
0.04
0.08
0.12
0.16
0.20
0.24
ω, eV
f (ω), SEC (× 1015)
Fig. 12.2 Phonon frequency distribution functions for graphite derived from two different
models. (With permission from Ref. [1]. Copyright 1970, Wiley.)

<!-- page 479 (PDF 498) -->
7.0
[σel + σinel(GASKET) + σa] = σt
6.0
5.0
4.0
3.0
2.0
1.0
EXPERIMENTAL
0.001
0.01
NEUTRON ENERGY, eV
CROSS SECTION, BARNS
0.1
1.0
σel
σinel
(GASKET)
σinel
(SUMMIT)
Fig. 12.3 Calculated and measured cross sections in graphite (GASKET and SUMMIT refer to
codes). (With permission from Ref. [1]. Copyright 1970, Wiley.)

<!-- page 480 (PDF 499) -->
### Wigner–Wilkins Proton Gas Model

The zeroth Legendre moment of the scattering energy transfer function for
neutron scattering from a free gas of hydrogen nuclei with a Maxwellian
distribution is given by Eq. (12.10). It is convenient to define the dimensionless
variable x = (E/kT)1/2 and to symmetrize the scattering transfer function:
S(x´ ! x) ≡ 1
ΣH
f
ffiffiffiffiffiffiffiffiffiffiffi
M(x´)
M(x)
s
x´Σs0(x´ ! x)
(12.40)
In terms of the reduced density,
χ(x) ≡
n(x)
ffiffiffiffiffiffiffiffiffiffi
M(x)
p
(12.41)
Equation (12.37) can be written as
xΣs(x)
Σf
+ Σa0
Σf

χ(x) = ∫
S(x´ ! x)χ(x´)dx´
(12.42)
or more explicitly,
x+ 1
2x

erf(x)+exp(□x2)
ffiffi
π
p
+Σa0
Σf
"
χ(x)
=2exp □1
2x2

∫
x
χ(x´)exp □1
2(x´)2

erf(x´)dx´
+2exp 1
2x2
erf(x)∫
x
exp □1
2(x´)2

χ(x´)dx´
(12.43)
where erf(x) is the error function of argument x, 1/v absorption has been assumed,
and P
a0 = P
a(v0 = 2200 m/s) is the 2200-m/s macroscopic absorption cross
section.
Equation (12.42) can be transformed into a second-order differential equation
by defining a second-order differential operator that when applied to either erf(x)
exp(x2/2) or exp(□x2/2) yields zero. Such an operator is
L = d2
dx2 + a(x) d
dx + b(x)
(12.44)
with
a(x) =
□
ffiffi
π
p
erf(x)
exp(□x2) + x
ffiffi
π
p
erf(x) ;
b(x) =
exp(□x2)
exp(□x2) +
ffiffi
π
p
x erf(x) □ x2
(12.45)

<!-- page 481 (PDF 500) -->
When this operator is divided by
P(x) = exp(□x2) +
ffiffi
π
p
x erf(x)
(12.46)
and then applied to Eq. (12.42), the Wigner–Wilkins equation results:
□ d
dx
(
P(x)
d
dx V(x) + Σa0
Σf

χ(x)
)
+
W(x) V(x) + Σa0
Σf

□ 4ffiffi
π
p
(
)
χ(x) = 0
(12.47)
where
W(x) = x2
P(x) □ exp(□x2)
P2(x)
;
V(x) = xΣs(x)
(12.48)
Appropriate low-energy boundary conditions can be deduced from setting x = 0
in Eq. (12.43), which leads to the low-energy boundary condition χ(0) = 0. The
two solutions of Eq. (12.43) near x = 0 are a constant and a solution that varies like
x; and only the latter can satisfy the boundary condition χ(0) = 0. The other
boundary condition follows from the requirement that the flux take on the
asymptotic 1/E ∼1/x2 form from the slowing-down region at high energies in the
thermal range.
Defining
μ(x) ≡ V(x) + Σa0
Σf

χ(x);
y(x) ≡
μ(x)P(x)
dμ(x)
dx
(12.49)
Eq. (12.47) can be reduced to a Riccati equation:
dy(x)
dx
= W(x) □ 4ffiffi
π
p
V(x) + Σa0
Σf

□1
□ P(x)y2(x)
(12.50)
At low energies (small x), Eq. (12.50) has a power series solution
y(x) ' a1
x + a2x + a3x3 + a4x4 + ∙∙∙
(12.51)
Defining
δ ≡
ffiffi
π
p
Σa(x)
Σf
'
ffiffi
π
p
Σa0
Σf
(12.52)

<!-- page 482 (PDF 501) -->
the coefficients are
a1 = 1;
a2 = □ 4
1 + δ
1 + 2δ

;
a3 = 103 + 380δ + 364δ2
90(1 + 2δ)2
(12.53)
The solution can be extended numerically to higher energies (larger x) by fitting a
polynomial to values for which the power series is valid, say up to xn, to define the
polynomials
W(x) = ∏
K
k=1
(x □ xk);
q(x) =
X
K
k=1
W(x)
x □ xk
dV(xk)=dx
dW(xk)=dx
(12.54)
which can be used to extrapolate the solution to higher x > xn:
y(xn+1) = y(yn) + ∫
xn+1
xn
q(x)dx
(12.55)
These algorithms can be used as a predictor coupled with Eq. (12.50) in a
predictor–corrector type of solution.
The boundary condition μ(0) = 0, together with μ(x) ≠0, implies that
lim
x!0
y(x) □ 1
x

= 0
(12.56)
which in turn implies that
μ(x) = xdμ(0)
dx
exp ∫
x
P(x´)y(x´) □ 1
x´

dx´

(12.57)
Numerical integration of the exponent then allows the density to be constructed
from
n(x) =
π3=4
x
ffiffiffiffiffiffiffiffiffiffi
M(x)
p
V(x) + Σa0
)=Σf
exp ∫
x
y(x´)P(x´) □ 1
x´

dx´

(12.58)
The development can be extended to include non-1/v absorbers and leakage by
the replacement
Σa0 ! Σa(E) +
B2
3[Σa(E) + Σs(E)(1 □ μ0)]
(12.59)
where B characterizes a simple buckling mode.
A thermal spectrum calculated for a 1/v absorber and with a thermal resonance
, and matched to a 1/E slowing-down source upper boundary condition, is
compared with a Maxwellian in Fig. 12.4. The spectrum hardening effects of the

<!-- page 483 (PDF 502) -->
1/v absorber in preferentially absorbing the lower-energy neutrons and of the 1/E
slowing-down source in increasing the higher energy neutron population are
apparent, as is the flux depression in the vicinity of the resonance.

### Heavy Gas Model

The heavy gas model given by Eq. (12.18) is a second-order differential equation
for the thermal neutron flux. It is instructive to rederive that result before looking
for a solution. We take advantage of the fact that the thermal neutron spectrum is
expected to be similar to a Maxwellian for small absorption to look for a solution
of Eq. (12.37) of the form
ϕ(E) = M(E)ψ(E)
(12.60)
and then make use of the detailed balanced condition of Eq. (12.38) to rewrite
Eq. (12.37):
Σt(E)M(E)ψ(E) = M(E)∫
Σs0(E ! E´)ψ(E´)dE´
(12.61)
Assuming that ψ is a slowly varying function of E, we make a Taylor’s series
expansion
ψ(E´) = ψ(E) + (E´ □ E) dψ(E)
dE
+ 1
2! (E´ □ E)2 d2ψ(E)
dE2
+ ∙∙∙
(12.62)
of ψ(E´) in the scatter-in integral, to obtain
Σa(E)M(E)ψ(E) = M(E)
X
n=1
n! An(E) dnψ(E)
dEn
(12.63)
Relative flux
0.001
0.01
Neutron energy, eV
Wigner–Wilkins
Maxwellian
0.1
Fig. 12.4 Comparison of Wigner–Wilkins and Maxwellian thermal neutron spectra for a
typical PWR composition. (With permission from Ref. [2]. Copyright 1976, Wiley.)

<!-- page 484 (PDF 503) -->
where the energy moments of the scattering energy transfer function are
An(E) = ∫
(E´ □ E)nΣs0(E ! E´)dE´
(12.64)
and where the first term in the expansion has canceled with the scattering
contribution to the total cross section on the left side of the equation. This
expansion is valid for any scattering transfer function, but its utility depends on
rapid convergence of the Taylor series, which requires that P
s0(E →E´) is strongly
peaked about E´ = E (i.e., for heavy mass moderators that cannot produce a large
energy change). Making a 1/A expansion of the gas scattering transfer function of
Eq. (12.7) and using the result to evaluate Eq. (12.64) yields
A1(E) =
A
A + 1

2 2Σf
A (2kT □ E) + O
A2

A2(E) =
A
A + 1

2 4Σf
A EkT + O
A2

An(E) = O
A2

; n □ 3
(12.65)
If only terms through n = 2 are retained in Eq. (12.63), the resulting equation is
identical to Eq. (12.18) to within a factor [A/(1 + A)]2, which approaches unity for
large A.
It is convenient to rewrite Eq. (12.63) in terms of the variable x = (E/kT)1/2:
x d2n x
( )
dx2
+ 2x2 □ 1
 dn x
( )
dx
+ 4x □ Δ
)n x( ) = 0
(12.66)
where 1/v absorption has been assumed and the absorption parameter is
Δ ≡ 2AΣa
Σf
(12.67)
This equation can be solved exactly in the case of zero absorption (Δ = 0):
n x( ) = a1x2e□x2 + a2 x2e□x2E1 x2
□ 1
h
i
(12.68)
where E1 is the exponential integral function. Since the second term is negative at
x = 0 and positive for large x, a2 must be zero.
When absorption is present, Eq. (12.66) can be integrated once to obtain
x dx x
( )
dx + 2 x2 □ 1
n x
( ) = Δ∫
x
n x´
( )dx´ = 2A
Σf
q x
( )
(12.69)
where we have used the fact that all of the neutrons slowing down below x – the
slowing-down density q(x) – must be absorbed in the interval x < x´ < 0.

<!-- page 485 (PDF 504) -->
Integrating a second time yields an integral equation:
n x
( ) = x2e□x2
4ffiffi
π
p + Δ∫
x
eu2
u3 ∫
u
n u´
( )du´du
"
(12.70)
that is well suited to solution by iteration. The asymptotic form for the neutron
flux ϕ = nv at large values of x is
ϕ E
( ) =
A
2Σf E 1 □ 1
2 Δ kT
E

1=2
+ 1
8 Δ2 + 16
 kT
E + ∙∙∙
"
(12.71)
Equation (12.70) can be solved numerically to obtain the thermal neutron
spectrum, ϕ(E). The solution is shown in Fig. 12.5 for different values of the
parameter Γ = P
a0/P
f.
10-1
10-2
0.025
0.25
Eϕ (E)
1.25
Γ = 2.5
√E
kT
Fig. 12.5 Neutron spectrum predicted by the heavy gas model for a 1/v absorber and
different values of Γ = P
a0/P
f. (With permission from Ref. [2]. Copyright 1976, Wiley.)

<!-- page 486 (PDF 505) -->
### Numerical Solution

Neutron scattering kernels are frequently so complicated that analytical or even
semianalytical solutions are impractical, in which case direct numerical solution
of the governing equation is the method of choice. A general numerical solution
method, applicable to any scattering kernel, is illustrated for the proton gas
model, for which Eq. (12.37) may be rewritten
V x
( ) + Γ
[
]N x
( ) = ∫
x
dx´G x´ ! x
)N x´
( ) + ∫
xc
dx´G x´ ! x
)Nasym x´
( )
(12.72)
where
V x
( ) = xΣs x
( )
Σf
;
Γ = Σao
Σf
;
G x´ ! x
) = x´Σ x´ ! x
)
(12.73)
and xc has been chosen so that the asymptotic form Nasym from the slowing-down
range may be used for x´ > xc. In this case, the last term in Eq. (12.72) may be
written cx erf(x)/(xc + Γ)2, where erf(x) is the error function.
Dividing the thermal energy range (0 ≤ x ≤ xc) into I intervals and using the
trapezoidal rule, the right side of Eq. (12.72) may be approximated:
X
i□1
j=1
G xj ! xi
N xj
Δj + G xi ! xi
)N xi
( )Δi + 2cxierf xi
( )
xc + Γ
)2
(12.74)
Equation (12.72) now may be solved directly by matrix inversion or by iteration.
For the iterative solution, the equations are rearranged to obtain
N xi
( ) =
V xi
( ) + Γ
)
X
I
j=1
G xj ! xi
N xj
Δj + 2cxierf xi
( )
xc + Γ
)2
"
i = 1; . . . ; I
(12.75)
The iterative solution of Eqs. (12.75) proceeds by guessing N(0)(xj), evaluating the
right-hand side, calculating N(1)(xi), and so on. A convenient starting guess is
N(0)(xi) = Nasym(xi). It is important to enforce neutron conservation during the
iteration, which is done by adjusting c.

### Moments Expansion Solution

The continuous slowing-down, or moments expansion, methodology that was
applied in Chapter 11 to the neutron slowing-down problem is also applicable to
the neutron thermalization problem. For heavy elements, the development is
similar to that of age theory. Defining
u ≡ ln T
E
(12.76)

<!-- page 487 (PDF 506) -->
and changing to the lethargy variable, Eq. (12.37) may be written as
Σa + Σs
)ϕ u
( ) ≡ ∫
□1
Σ u´ ! u
)ϕ u´
( )du´
(12.77)
where
ϕ u
( ) ≡ En E
( )v E
( );
Σ u´ ! u
) ≡ EΣ E´ ! E
)
Since ϕ(u) is approximately constant in the slowing-down range above thermal,
ϕ(u´) is expanded in a Taylor’s series about u to obtain
Σa u
( ) + Σs u
( ) □ ξ0Σ

ϕ u
( ) = □ ξ Σ
h
i dϕ u
( )
du
+ 1
2! ξ2Σ
 d2ϕ u
( )
du2
+ ∙∙∙+ □1
)n
n!
ξnΣ
h
i dnϕ u
( )
dun
+ ∙∙∙
(12.78)
where
ξ nΣ

≡ □1
)n
∫
□1
u´ □ u
)n Σ u´ ! u
)du´
(12.79)
Noting that for energies above thermal (no upscattering), the nth term in Eq.
(12.78) is of order (ξ0)n□1 relative to hξ nPidϕ/du, where ξ0 is the average
logarithmic energy loss for scattering by free atoms at rest [ξ0 ≡ ξiso = 1 + α ln
α/(1 □ α)]. Hence, for scattering from atoms other than hydrogen and
deuterium, Eq. (12.38) can be truncated after a few terms with little loss
in accuracy.
Differentiating Eq. (12.38), truncating terms higher than d2ϕ/du2, solving for
hξPid2ϕ/du2, using this result in Eq. (12.38), and neglecting terms of order (ξ3
0)
and higher yields
Σa u
( ) + Σs u
( ) □ ξ0Σ

ϕ u
( ) =
□
Σs u
( )ξ u
( ) + γ u
( ) Σa u
( ) + Σs u
( ) □ ξ0Σs

+ γ u
( ) d
du ξ Σ
h
i

 dϕ u
( )
du
(12.80)
which can be integrated to obtain
ϕ u
( ) =
K u
( )exp □∫
u
□1
^Σa u´
( )= ξ u´
( )Σs u´
( )Σs u´
( ) + γ u´
( )^Σa u´
( )

du´

ξ u
( )Σs u
( ) + γ u
( )^Σa u
( )
(12.81)

<!-- page 488 (PDF 507) -->
where
K u
( ) ≡ exp
(
∫
u
□1
^Σa(u´) dγ(u´)=du´
) + d ξ u´
( )Σs(u´)
[
]=du´
)
ξ u´
( )Σs(u´) + γ(u´)^Σa u´
( )

□ g(u´) Σa u´
( ) + γ u´
( ) d^Σa u´
( )=du´

ξ u´
( )Σs u´
( ) + γ u´
( )^Σa u´
( )
du´
)
g u
( ) ≡
ξ u
( )Σs u
( ) + γ u
( )^Σa u
( )
Σs u
( )ξ u
( ) + γ u
( )^Σa u
( ) + γ u
( ) d ξ Σ
h
i=du
)
□ 1
^Σa u
( ) ≡ Σa u
( ) + Σs u
( ) □ ξ0 Σ

ξ u
( ) ≡ ξ Σ u
( )
h
i
Σs u
( )
γ u
( ) ≡ 1
ξ2Σ u
( )

ξΣ u
( )
h
i
(12.82)
The moments of the scattering kernel are given by
ξn Σ
h
i = (□1)n+1Σf
(
α
1 □ α
lnα
)n □ n lnα
)n□1 + n n □ 1
) lnα
)n□2

+ ∙∙∙+ □1
)nn!] + □1
)n+1n!
1 □ α
□ 1 + μ
)2
4μ
2μ
1 + μ □ 1
2 μ 1 □ α
) □ 1 □ μ
1 + μ

α lnα
)n

□ 1 □ α
)α ln 2
)n□1 2 ln α + n
)
 T
E
)
+ O
μ
E2

(12.83)
where μ m/M, the ratio of the masses of the neutron and the scattering atom.
For scattering by unbound atoms at rest, K(u) →1 and Eq. (12.81) is identical to
the Grueling–Goertzel approximation of Chapter 10. For γ = 0, Eq. (12.81)
reduces to Fermi age theory. The presence of γ ≠0 accounts for upscattering in
the thermal range of energies. It is the decrease in ^Σa = P
a + P
s □ hξ0 Pi,
rather than the decrease in ξP
s, that is the dominant effect of the chemical
binding.
For neutron thermalization by graphite, an explicit expression for the thermal
spectrum is given by

<!-- page 489 (PDF 508) -->
ξ Σf Eϕ(E) = 1 □ 1:1138 1
2 Δ

z + 0:6526 1
2 Δ

+ 1:913 T
T

z2
□ 0:2673 1
Δ

+ 3:313 T
T
"
z3
+ 0:08569 1
Δ

+ 2:752 1
Δ

2 T
T + 4:935 T
T
"
+ 0:201 (K 2)av
T2
□ 0:6204 Bav
T2
z4 + O(z5)
(12.84)
where z (T/E)1/2, Δ ≡ 2P
a(T)/μP
f, and the other parameters are defined in terms
of the crystal vibration spectra for perpendicular, ρ1(ω), and parallel, ρ2(ω),
vibrations:
T ≡ 1
3 T1 + 2
3T2
Ti ≡ 1
2 ∫
θi
ωρi(ω) coth ω
2T dω
(K 2)av ≡ 3
4 T2
1 + T1T2 + 2T2
Bav ≡ 1
3 ∫
θ1
ω2ρ1(ω)dω + 2
3 ∫
θ2
ω2ρ2(ω)dω
(12.85)
where the θi are the cutoff frequencies for the respective crystal vibration modes.
These parameters are given for graphite and a free carbon gas in a Maxwellian
distribution in Table 12.1.
For hydrogenous atoms, it is not possible to truncate Eq. (12.78) as described
already for heavy mass scattering atoms. However, noting that
ξnΣ
h
i = (□1)nn!Σf + O
E2

(12.86)
Table 12.1 Thermalization Parameters for Carbon
Graphite
Free Gas
T (K)
T=T
(K2)av/T2
Bav/T2
T=T
(K2)av/T2
Bav/T2
2.363
21.63
15/4
1.432
7.794
25/4
15/4

<!-- page 490 (PDF 509) -->
for hydrogen, it is possible to obtain a solution ϕ(u) accurate to O(1/E2) by
neglecting terms of order 1/E2 and higher in Eq. (12.78), which enables this
equation to be written as
^Σa(u)
Σf
ϕ(u) = □ dϕ(u)
du
+ d2ϕ(u)
du2
□ ∙∙∙+ (□1)n dϕn(u)
dun
+ ∙∙∙
(12.87)
Operating on Eq. (12.87) with 1 + d/du and integrating then yields
ϕ(u) =
^Σa(u) + Σf
exp □∫
E
^Σa(E´)
^Σa(E´) + Σf
dE´
E´
"
(12.88)
Expanding Eq. (12.88) in inverse powers of (E/T)1/2 yields
EϕE = 1 □ 3 1
2 Δ

z + 6 1
Δ

+ T
T
"
z2
□ 10 1
Δ

+ 25
2 Δ

 T
T
"
z3
+ 15 1
Δ

+ 43
Δ

2 T
T

+ 3
T
T
+ 4
(K 2)av
T2
"
□ 1
Bav
T2
z4 + O(z5)
(12.89)
For hydrogen bound in water molecules at 293 K, the thermalization parameters
are T=T = 4.345, Bav/T2 = 126.90, and (K2)av/T2 = 53.63.

### Multigroup Calculation

The thermal neutron scattering transfer function discussed in the preceding
sections can be used in a multigroup calculation of the thermal neutron energy
spectrum. The group-to-group scattering transfer term is defined as
Σg´!g =
∫
Eg□1
Eg
dE∫
Eg´□1
g´
dE´Σs0(E´ ! E)ϕ(E´)
∫
Eg´□1
Eg´
dE´ϕ(E´)
(12.90)
Evaluation of Eq. (12.90) requires an approximation for the energy dependence of
the thermal neutron flux over the energy interval Eg < E < Eg□1. One of the
approximate thermal neutron spectra above can be used for this purpose, or if

<!-- page 491 (PDF 510) -->
the interval is sufficiently small, ϕ = constant can be used.
The multigroup thermal neutron flux balance equation, neglecting leakage, is
Σg
aϕg =
X
G
g´ ≠g
Σg´!g
s
ϕg´ + Sg;
g = 1; . . . ; G
(12.91)
where Sg is the slowing-down source to the upper groups in the thermal energy range.

### Applications to Moderators

The thermal neutron flux distribution has been calculated numerically for water
with various amounts of admixed cadmium absorber, using both the free gas and
Nelkin models to calculate the scattering transfer cross section. Results of the
calculations are compared with experiment in Fig. 12.6.
The thermal neutron flux distribution has also been calculated numerically for
a large graphite block poisoned with boron, using both the crystal model of
EXPERIMENTAL (Cd POISON)
BOUND HYDROGEN CALCULATION
FREE HYDROGEN CALCULATION
15.4 BARNS/H ATOM
9.6
5.4
2.67
0.001
0.01
0.1
NEUTRON ENERGY, eV
RELATIVE NEUTRON FLUX
1.0
Fig. 12.6 Experimental and calculated neutron energy spectrum in water with cadmium
poisons. (With permission from Ref. [1]. Copyright 1970, Wiley.)

<!-- page 492 (PDF 511) -->
Eq. (12.36) and the heavy gas model of Eq. (12.13) to evaluate the scattering
transfer cross section. The results are compared with experiment in Fig. 12.7.

## 12.5 Calculation of Thermal Neutron Energy Spectra in Heterogeneous Lattices

The transport equation for neutrons in the thermal energy region E < Eth ∼1 eV is
Ω ? ∇ψ(r; E; Ω) = ∫
Eth
dE´
∫
4π
dΩ´Σs(r; Ω´ ! Ω; E´ ! E)ψ(r; E´; Ω´)
+ S(r; E)
4π
;
0 < E < Eth
(12.92)
where
S(r; E) = ∫
Eth
dE´Σs(r; E´ ! E)ϕ(r; E´)
(12.93)
is the source of neutron scattering into the thermal region from the slowing-down
region. With reference to Section 9.2, this equation can be converted into an
integral equation for the scalar neutron flux, which for the case of isotropic
scattering may be written as
ϕ(r; E) = ∫dr´
e□α(r;r´)
4πjr □ r´j
2 ∫
Eth
dE´Σs0(r; E´ ! E)ϕ(r; E´) + S(r; E´)

(12.94)
RELATIVE NEUTRON FLUX
0.001
0.01
323°K
CRYSTAL
GAS
EXPERIMENTAL
0.1
NEUTRON ENERGY, eV
1.0
Fig. 12.7 Experimental and calculated neutron energy spectrum in graphite at 323 K. (With
permission from Ref. [1]. Copyright 1970, Wiley.)

<!-- page 493 (PDF 512) -->
Dividing the problem of interest (e.g., a fuel assembly) up into I spatial regions,
integrating Eq. (12.94) over the volume Vi of region i, and defining (by analogy
with Eq. (9.52))
Tj!i(E) ≡ 1
V i ∫V i
dri∫V j
drj
e□α(ri;rj)
4πjri □ rjj
(12.95)
leads to a coupled set of equations for the group fluxes ϕi in each region:
ϕi(E) =
X
I
j=1
Tj!i(E) ∫
Eth
dE´Σsj(r´; E´ ! E)ϕj(E´) + Sj(E´)

(12.96)
Dividing the thermal energy range into G groups and using an appropriate
differential scattering cross section and weighting spectrum to calculate
Σg´!g
sj
≡
∫
Eg□1
g
∫
Eg´□1
g´
Σsj(E´ ! E)w(E´)dE´dE
∫
Eg□1
g
w(E´)dE´
(12.97)
Eq. (12.96) can be integrated over Eg < E < Eg□1 to obtain the set of multigroup
equations
ϕg
i
X
N
j=1
Tj!i
g
X
G
g´=1
Σg´!g
sj
ϕg´
j + Sg
j
!
;
g = 1; . . . ; G
(12.98)
Following Section 9.3, define the collision probability
P ji
g ≡ V iΣg
tiΣg
tjTj!i
g
(12.99)
in terms of which Eqs. (12.98) can be written as
Σg
tiV iϕg
i =
X
N
j=1
Pji
g
PG
g´=1 Σg´!g
sj
ϕg´
i + Sg
j
Σg
tj
;
g = 1; . . . ; G;
i = 1; . . . ; I
(12.100)
The collision probabilities can be calculated by the methods of Section 9.3. The
multigroup scattering transfer cross sections can be calculated using one of the
differential scattering cross sections and a plausible weighting function, as
discussed in this chapter. Then the set of I × G Eqs. (12.100) can be solved for
the group fluxes in each region. Such methods are widely employed for practical
calculations of the thermal spectra in heterogeneous reactor fuel assemblies.

<!-- page 494 (PDF 513) -->
## 12.6 Pulsed Neutron Thermalization

### Spatial Eigenfunction Expansion

The time-dependent diffusion equation that describes the neutron flux distribution
following the introduction of a pulse Q of neutrons with energy E0 at time
t = 0 into a uniform but finite nonmultiplying medium is
ν
@ϕ
@t (r; E; t) □ D(E)∇2ϕ(r; E; t) + Σa(E)ϕ(r; E; t) =
∫
Σ(E´ ! E)ϕ(r; E´; t)dE´ □ Σs(E)ϕ(r; E; t) + δ(t)Q(r)δ(E □ E0)
(12.101)
Assuming that the spatial eigenfunctions satisfying
∇2Gn(r) + B2
nGn(r) = 0
(12.102)
and the physical boundary conditions form a complete set, the solution of Eq.
(12.101) can be expanded:
ϕ(r; E; t) =
X
n
ϕn(E; t)Gn(r)
(12.103)
and the general orthogonality property
∫Gn(r)Gm(r)dr = δnm
(12.104)
can be used to reduce Eq. (12.101) to a coupled set of equations for the ϕn(E, t):
v
@ϕn
@t (E; t) + D(E)B2
nϕn(E; t) + Σa(E)ϕn(E; t)
= ∫
Σ(E´ ! E)ϕn(E´; t)dE´ + δ(E □ E0)δ(t)Qn
(12.105)
where Qn ≡ ∫dr Gn(r)Q(r):

### Energy Eigenfunctions of the Scattering Operator

The scattering operator S0 defined by
S0ϕ(E) ≡ ∫
Σ(E´ ! E)ϕ(E´)dE´ □ Σs(E)ϕ(E)
(12.106)
possesses an eigenvalue spectrum and a set of eigenfunctions in terms of which
the energy dependence of the neutron spectrum may be expanded. The general

<!-- page 495 (PDF 514) -->
eigenvalue problem is
κχ(E) = Σs(E)χ(E) □ ∫
Σ(E´ ! E)χ(E´)dE´
(12.107a)
or
κχ(E) = □S0χ(E)
(12.107b)
The adjoint operator S+
0 defined (see Chapter 13) by
∫χ+(E)S0χ(E)dE ≡ ∫χ(E)S+
0 χ+(E)dE
(12.108)
is
S+
0 χ+(E) = ∫
dE´Σ(E ! E´)χ+(E´) □ Σs(E)χ+(E)
(12.109)
The principle of detailed balance,
Σ(E´ ! E)M(E´) = Σ(E ! E´)M(E)
(12.110)
requires that
χ(E) = M(E)χ+(E)
(12.111)
where M(E) is the Maxwellian distribution. Thus, the principle of detailed balance
ensures that the lowest eigenvalue κ0 = 0 and eigenfunction χ0(E) = M(E), independent
of scattering model.
As an example, consider the heavy gas model of Section 12.2. From Eq. (12.15),
S0χ(E) = 2Σf
A
kTE d2χ(E)
dE2
+ E dχ(E)
dE
+ χ(E)

(12.112)
and from Eq. (12.108),
S+
0 χ+(E) = 2Σf
A
kTE d2χ+(E)
dE2
+ (2kT □ E) dχ+(E)
dE

(12.113)
The eigenvalues of the direct and adjoint eigenvalue problems of Eqs. (12.107) and
(12.109) are identical (Chapter 13). Substitution of
χ+(E) =
X
n=0
anEn
(12.114)
into the adjoint eigenvalue problem
S+
0 χ+(E) + κχ+(E) = 0
(12.115)

<!-- page 496 (PDF 515) -->
and working use of Eq. (12.113) reveals that the eigenvalue spectrum is discrete:
κn = 2Σf
A n;
n = 0; 1; 2; . . .
(12.116)
The associated eigenfunctions are the Laguerre polynomials of order unity
χ+
n(E) = L(1)
n (E)
ffiffiffiffiffiffiffiffiffiffi
n + 1
p
(12.117)
where
L(1)
0 (E) = 1;
L(1)
1 (E) = 2 □ E;
L(1)
2 (E) = 3 □ 3E + 1
2E2; . . .
(12.118)
These polynomials constitute a complete set, so any arbitrary function can be
expanded in them.

### Expansion in Energy Eigenfunctions of the Scattering Operator

Assuming that the function ϕn(E, t) can be represented as
ϕn(E; t)∼ϕn(E)e□λnt
(12.119)
the homogeneous part of Eq. (12.105) reduces to the eigenvalue problem
□ λn
v + D(E)B2
n

ϕn(E) = S0ϕn(E)
(12.120)
Expanding each ϕn(E) in the eigenfunctions of the scattering operator χm(E),
ϕn(E) =
X
m
Cmnχm(E)
(12.121)
substituting into Eq. (12.120), multiplying by χ+
p (E), and integrating over energy
yields
X
m
(□λnV mp + DmpB2
n + κmδmp)Cmn = 0
(12.122)
where
V mp = ∫
v χ(E)
m χ+
p (E)dE
Dmp = ∫
D(E)χm(E)χ+
p (E)dE
(12.123)

<!-- page 497 (PDF 516) -->
The set of Eqs. (12.122) formed by multiplying by each χ+
p (E) must simultaneously
vanish, which by Cramer’s rule requires that
det(□λnVmp + DmpB2
n + κmδmp) = 0
(12.124)
This is the eigenvalue condition from which the κm are determined.
The spatial harmonics n > 0 will decay more rapidly than the n = 0 modes,
because λn>0 > λ0, due to the larger B2
n. When all the higher spatial harmonics
have become negligible, the neutron pulse will decay as a series of energy
harmonics of the fundamental spatial mode:
ϕ(r; E; t) = G0(r)
X
p
Apϕp;0(E)e□λp;0t
(12.125)
At long times,
ϕ(r; E; t) ! G0(r)ϕ0;0(E)e□λ0;0t
(12.126)
since λp,0 < λp,n for n > 0. If Eq. (12.121) is truncated at one term (i.e., only the
fundamental energy eigenfunction is retained), then Eq. (12.124) yields
λ0;0 = D00
V 00
B2
0 ≡ D0B2
(12.127)
If the first two terms are retained in Eq. (12.121), then
λ0;0 = D0B2
0 □
V 00κ1
(D01 □ D0V 01)2B4
(12.128)
Thus, measurement of the time decay of the neutron pulse yields information
about the Maxwellian average diffusion coefficient, D00. The second term in Eq.
(12.128), which is known as the diffusion cooling term, depends explicitly on the
thermalizing properties of the medium.

## References

1 G. I. BELL and S. GLASSTONE, Nuclear Reactor Theory, Wiley (Van Nostrand
Reinhold), New York (1970), Chap. 7.
2 J. J. DUDERSTADT and L. J. HAMILTON, Nuclear Reactor Analysis, Wiley, New York
(1976), Chap. 9.

## Further Readings

BECKHURTS K. H. and WIRTZ K., Neutron Physics, Springer-Verlag, Berlin (1964).
