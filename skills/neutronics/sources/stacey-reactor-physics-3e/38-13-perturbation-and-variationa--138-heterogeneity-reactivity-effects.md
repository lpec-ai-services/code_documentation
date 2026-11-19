# 13 Perturbation and Variational Methods — 13.8 Heterogeneity Reactivity Effects … Problems
<!-- source PDF pages 539-552 -->

<!-- page 521 (PDF 539) -->
which contain arbitrary constants λ and κ that are determined by using Eq. (13.72)
in the variational functional of Eq. (13.63) and requiring stationarity with respect
to arbitrary and independent variations δλ and δκ, which leads to the transcendental
equations
λ =
χ2
κλ
1 + χ2
κλ
;
βκ = βλ
1 + 2σp(1 □ Y κλ)
σm
(13.73)
which must be solved for χκλ and Yκλ, where
β2
i = 1 +
σ0
σm + iσp
Γγ + iΓn
Γ
;
i = λ; κ; 0; 1
χκλ = 2E0(1 □ α)
Γ(βκ + βλ)
Y κλ = arctanχκλ=χκλ
(13.74)
where the Γ’s are the resonance widths, and σ0 and E0 are the peak resonance
cross section and the energy at which it occurs.
The variational estimate of the resonance integral is
Jfϕλ; ϕ+
κ g
=
πσ0Γγ=2E0
βλ + ((σm + σp)(β2
1 □ β2
0)=(σm + λσp)(βκ + βλ))(1 □ λ □ Y κλ)
(13.75)
which has been shown to provide a more accurate estimate than either the
narrow-resonance or wide-resonance approximations to the resonance integral
for resonances of “intermediate” width.

## 13.8 Heterogeneity Reactivity Effects

As an application of the Raleigh quotient, consider a heterogeneous lattice described
by collision probability integral transport theory. Equations (12.100) become
μng
t ϕg
n = P
g´n´ Pg
n´n(μn´g´!g
s
+ λvμn´g´
f
χg)ϕg´
n ;
n; n´ = 1; . . . ; N; g; g´ = 1; . . . ; G
and the corresponding adjoint equations are
μng
t ϕ+g
n = P
g´n´ Pg´
nn´(μng!g´
s
+ λvμng
f χg´)ϕ+g´
n ;
n; n´ = 1; . . . ; N; g; g´ = 1; . . . ; G
(13.76)

<!-- page 522 (PDF 540) -->
where n and g refer to spatial region and group, Pg
n´n is the probability that a
neutron in group g and region n´ has its next collision in region n, and μng is the
cross section in group g and region n times the volume of region n divided by the
total volume of all regions.
The Rayleigh quotient of Eq. (13.63) becomes
λ ϕ+; ϕ
f
g =
P
gnϕ+g
n (μtϕg
n □ P
g´n´Pg
n´nμn´g´!g
s
ϕg´
n´)
P
gnϕ+g
n χgP
g´n´Pg
n´nvμn´g´
f
ϕg´
n´
(13.77)
This expression can be used in a number of ways. For example, approximate flux
and adjoint distributions (even one based on a homogenized model) can be used
as trial functions in Eq. (13.77) to obtain a more accurate estimate of the infinite
multiplication factor in a heterogeneous lattice.

## 13.9 Variational Derivation of Approximate Equations

The requirement that a variational functional be stationary about the function ϕs
that causes the first variation of the functional to vanish is entirely equivalent to
requiring that the function ϕs satisfy the governing equation for ϕ if the
variational functional is constructed so that satisfaction of this governing equation
is the stationarity condition. Thus, the equations of reactor physics can be
stated equivalently as stationary variational functionals, just as the equations of
particle dynamics can be equivalently stated in terms of a Hamiltonian. For
example, the statement that ϕ+
s and ϕs make the Raleigh quotient of Eq. (13.63)
stationary is entirely equivalent to the statement that ϕs and ϕ+
s satisfy Eq. (13.62)
and the associated boundary conditions. This equivalence provides a basis for the
variational derivation of approximate equations.
As an example, consider a reactor described by one-speed diffusion theory in
two dimensions:
□ @
@x D(x; y) @ϕ(x; y)
@x

□ @
@y D(x; y) @ϕ(x; y)
@y

+ Σa(x; y) □ vΣf (x; y)
k

ϕ(x; y) = 0
(13.78)
An equivalent variational description is the stationarity requirement for the
variational functional:
Ffϕ+; ϕg = ∫dx dy ϕ+(x; y)
□ □ @
@x D @ϕ
@x □ @
@y D @ϕ
@y +
Σa □ vΣf
k

ϕ

(13.79)

<!-- page 523 (PDF 541) -->
Recalling that the one-speed diffusion equation is self-adjoint, we look for a
separable solution
ϕ+(x; y) = ϕ(x; y) = ϕx(x)ϕy(y)
(13.80)
consisting of a known function ϕy(y), perhaps obtained from a one-dimensional
calculation, and an unknown function ϕx(x). Substituting Eq. (13.80) into
Eq. (13.79) and requiring stationarity with respect to arbitrary variations δϕx
(ϕy is specified and hence does not allow arbitrary variations) leads to a onedimensional
equation for the unknown ϕx(x),
□ d
dx Dx(x) dϕx(x)
dx

+ ΣRx(x) + Dx(x)B2
g(x) □ vΣf x
k

ϕx(x) = 0
(13.81)
where the effective y-independent constants are defined as weighted integrals over y:
Dx(x) ≡ ∫dy ϕ2
y(y)D(x; y)
Dx(x)B2
g(x) ≡ □∫dy ϕy(y) @
@y D(x; y) @ϕy(y)
@y

Σx(x) ≡ ∫dy ϕ2
y(y)Σ(x; y)
(13.82)
This procedure is referred to as variational synthesis and is described more fully
in Chapter 15.

### Inclusion of Interface and Boundary Terms

In deriving Eqs. (13.81) and (13.82), it was implicitly assumed that the known
function ϕy(y) is continuous over all y, which limits the approximation to trial
functions ≡ ϕy that are continuous in y. This limitation can be removed if the
variational functional is modified so that stationarity requires not only satisfaction
of Eq. (13.78) but also continuity of flux and current across an interface at y = yi.
Stationarity of the modified functional
Fdisfϕ+; ϕg = ∫dx dy ϕ+(x; y)
□ □ @
@x
D @ϕ
@x

□ @
@y
D @ϕ
@y

+
Σa □ vΣf
k

ϕ

+ ∫dx ϕ+
i (x; yi)[ϕ(x; yi + ε) □ ϕ(x; yi □ ε)]
+ ∫dx J+
i (x; yi) □D(x; yj + ε) @ϕ(x; yi + ε)
@y

+ D(x; yi □ ε) @ϕ(x; yi □ ε)
@y

(13.83)

<!-- page 524 (PDF 542) -->
with respect to arbitrary and independent variations δϕx over the volume and
variations δϕ+
i and δJ+
i on the interface at y = yi requires both that Eq. (13.78) be
satisfied everywhere in the reactor except on the interface and that continuity of
flux and current be satisfied at the interface:
ϕ(x; yi + ε) = ϕ(x; yi □ ε)
□ D(x; yi + ε) @ϕ(x; yi + ε)
@y
= □D(x; yi □ ε) @ϕ(x; yi □ ε)
@y
(13.84)
Boundary terms can be included in a similar fashion, leading to variational functionals
which admit trial functions that do not satisfy the boundary conditions.
Inclusion of interface and boundary terms is important for the development of
synthesis and nodal approximations and is discussed in greater detail in Chapter 15
as well as in Section 13.11.

## 13.10 Variational Even-Parity Transport Approximations

### Variational Principle for the Even-Parity Transport Equation

The even-parity form of the transport equation introduced in Section 9.11 is
convenient for the development of approximate transport equations when the
scattering and source are isotropic. A variational functional for the even-parity
component of the angular flux, which is self-adjoint, may be written,
J
(
ψ+; ϕ
)
= ∫V
dr ∫dΩ 1
Σ (Ω ? ∇ψ+)2 + Σt(ψ+)2

□ Σsϕ2 □ 2ϕS
+ ∫S
ds∫dΩjn ? Ωj[ψ+(rs)]2
(13.85)
where the dependence on (r, Ω) has been suppressed, and the two integrals are
over the volume V and the bounding surface S, with n being the outward normal
to the surface. Note that here ψ+ refers to the even component of the angular flux,
not an adjoint function. Taking the variation of the functional J with respect to
arbitrary but dependent (since ϕ depends on ψ+) variations δψ+ and δϕ about
some reference functions ψ+
0 and ϕ0 yields
δJ ≡ Jfψ+
0 + δψ+; ϕ + δϕg □ Jfψ+
0 ; ϕg
= 2∫V
dr∫dΩ
Σ(r) (Ω ? ∇δψ+)(Ω ? ∇ψ+
0 )

+ Σtψ+
0 δψ+ □ δϕ(Σsϕ0 + S)
+ 2∫S
ds∫dΩjns ? Ωjψ+
0 δψ+ + O((δψ+)2; (δϕ)2)
= 2∫V
dr∫dΩδψ+ □Ω ? ∇
Σt
Ω ? ∇ψ+

+ Σtψ+
0 □ Σsϕ0 □ S

+ 2∫S
ds∫dΩδψ+ jn ? Ωjψ+
0 + n ? Ω
Σt
Ω ? ∇ψ+

+ O((δψ+)2)
(13.86)

<!-- page 525 (PDF 543) -->
where integration by parts and the divergence theorem have been used to obtain
the final form. The requirements that the volume and surface integrals vanish for
arbitrary and independent variations δψ+ in the volume and on the surface are
just the transport equation for the one-speed (or within-group) even-parity
transport equation
□Ω ? ∇
Σt(r) Ω ? ∇ψ+
0 (r; Ω)

+ Σt(r)ψ+
0 (r; Ω) □ Σs(r)ϕ0(r) □ S(r) = 0
(13.87)
and the vacuum boundary condition satisfied by the even-parity flux component:
Ω ? ∇ψ+(rs; Ω) − Σt(rs)ψ+(rs; Ω) = 0;
Ω ? ns≷0
(13.88)

### Ritz Procedure

This is a procedure for constructing an improved approximate solution by
combining several plausible approximate solutions, each of which perhaps
represents some feature expected in the exact solution, that is, by approximating
the even-parity flux by an expansion in known functions χi (r, Ω):
ψ+(r; Ω) '
X
i
aiχi(r; Ω)
(13.89)
The general Ritz method proceeds by substituting this expansion into the
variational functional describing the system of interest, Eq. (13.85) in our case,
and requiring stationarity (vanishing of first variations) for arbitrary and independent
variations of the combining coefficients, ai,
δJfag = 0 = 2δaT[Aa □ S]
(13.90)
where a is a column vector of the ai, aT is the transposed row vector, A is a matrix
with elements
Aij = ∫V
dr ∫dΩ 1
Σt
(Ω ? ∇χi)(Ω ? ∇χj) □ Σtχiχj

□ Σs∫dΩ´χi∫dΩχj
)
+ ∫S
ds∫dΩjns ? Ωjχiχj
(13.91)
and
Si = ∫V
dr∫dΩ χiS(r)
(13.92)

<!-- page 526 (PDF 544) -->
Thus, the requirement for stationarity of the variational principle defines the ai as
the solution of
Aa = S
(13.93)

### Diffusion Approximation

The diffusion approximation was shown in Chapter 9 to follow from a representation
of the angular flux of the form
ψ(r; Ω) ' ϕ(r) + 3Ω ? J(r)
(13.94)
With this representation, the even-parity component of the angular flux is just the
scalar flux,
ψ+(r; Ω) ≡ 1
2 ψ(r; Ω) + ψ(r; □Ω)
[
] = ϕ(r)
(13.95)
Using this representation for the even-parity flux in the variational principle of Eq.
(13.85) leads to
J ϕ
f g = ∫V
dr∫dΩ 1
Σt
(Ω ? ∇ϕ)2 + Σtϕ2 □ Σsϕ2 □ 2ϕS

+ ∫S
ds ϕ2
∫dΩjΩ ? nsj
= ∫V
dr
3Σt
(∇ϕ)2 + (Σt □ Σs)ϕ2 □ 2ϕS

+ 1
2 ∫s
ds ϕ2
(13.96)
Requiring stationarity with respect to arbitrary and independent variations δϕ in
the volume and on the surface leads to the equation
□∇?
3Σt(r) ∇ϕ0(r)

+ Σt(r) □ Σs(r)
[
]ϕ0(r) = S(r)
(13.97)
and the boundary condition
□
3Σt(rs) ns ? ∇ϕ0(rs) + ϕ0(rs) = 0
(13.98)
Equation (13.97) differs from the previous diffusion equation only by the Σ□1
t
rather than (Σt □ μ0Σs)□1 in the first term, and had we neglected anisotropic
scattering (→μ0 = 0) in Chapter 9 as we have here, the two would be identical.
Equation (13.98) specifies that the flux extrapolate to zero a distance 2/3Σt outside

<!-- page 527 (PDF 545) -->
the boundary, which is the same result (for isotropic scattering) that was obtained
from P1 theory in Chapter 9.

### One-Dimensional Slab Transport Equation

In a slab varying from x = 0 to x = a, the variational principle of Eq. (13.85)
becomes
J ψ+
f
g = ∫
a
dx
∫
□1
dμ
μ2
Σt
@ψ+
@x

+ Σt(ψ+)2
"
□ Σsϕ2 □ 2ϕS
(
)
+ ∫
□1
dμ
2 jμj(ψ+)2jx=0 + ∫
□1
dμ
2 jμj(ψ+)2jx=a
(13.99)
Requiring stationarity with respect to arbitrary and independent variations δψ+
within 0 < x < a and at x = 0 and x = a yields a one-dimensional transport
equation for the even-parity flux component
□μ2 @
@x
Σt(x)
@
@x ψ+(x; μ)

+ Σt(x)ψ+(x; μ)
= Σs(x)ϕ(x) + S(x)
(13.100)
and a pair of extrapolated vacuum boundary conditions
ψ+(a; μ) +
Σt(a)
@
@x ψ+(a; μ) = 0
ψ+(0; μ) □
Σt(a)
@
@x ψ+(0; μ) = 0
(13.101)

## 13.11 Boundary Perturbation Theory

Consider a reactor described by the multigroup diffusion equations, which are
written in operator notation as
A0(r)ϕ0(r) = λ0F0(r)ϕ0(r)
(13.102)
with general boundary conditions given by
a0n ? ∇ϕ0(rs) + b0ϕ0(rs) = 0
(13.103)
where a0 and b0 are group-dependent operators that may vary with position on
the surface rs.

<!-- page 528 (PDF 546) -->
The adjoint equation is
A+
0 (r)ϕ+
0 (r) = λ0F+
0 (r)ϕ+
0 (r)
(13.104)
where the definition (13.11) or (13.14) of adjoint operator has been used. The double
integration by parts of the spatial derivative term in the diffusion operator yields
□∫V
drϕ2
0(∇? D0∇ϕ0)
= □∫V
drϕ0(∇?D0∇ϕ+
0 ) □ ∫s
ds n?(ϕ+
0 D0∇ϕ0 □ ϕ0D0∇ϕ+
0 )
(13.105)
Using the boundary condition of Eq. (13.103) to evaluate the n □ ∇ϕ0 term in the
surface integral reveals that the natural adjoint boundary condition (the condition
that leads to vanishing of the surface integral) is
a0n ? ∇ϕ+
0 (rs) + b0ϕ+
0 (rs) = 0
(13.106)
Now, let the boundary condition be changed by perturbing b0 to b0 + b1:
a0n ? ∇ϕ+(rs) + (b0 + b1)ϕ+(rs) = 0
and
a0n ? ∇ϕ(rs) + (b0 + b1)ϕ(rs) = 0
(13.107)
where |b1/b0| ≡ε ≪1. The perturbed flux, which must satisfy a different boundary
condition and is associated with a different eigenvalue as a consequence, now
satisfies
A0(r)ϕ(r) = λF0(r)ϕ(r)
(13.108)
Expanding the perturbed flux and eigenvalue
ϕ = ϕ0 + ϕ1 + ϕ2 + ∙∙∙
(13.109)
λ = λ0 + λ1 + λ2 + ∙∙∙
(13.110)
where the subscript indicates the order of the term with respect to the small
parameter |b1/b0| ≡ ε ≪1, and substituting into Eqs. (13.107) and (13.108) results
in the following hierarchy of perturbation equations and boundary conditions:

## □ Order ε0:

A0(r)ϕ0(r) = λ0F0(r)ϕ0(r)
(13.111)
a0n ? ∇ϕ0(rs) + b0ϕ0(rs) = 0
(13.112)

<!-- page 529 (PDF 547) -->
## □ Order ε1:

[A0(r) □ λ0F0(r)]ϕ1(r) = λ1F0(r)ϕ0(r)
(13.113)
a0n ? ∇ϕ1(rs) + b0ϕ1(rs) + b1ϕ0(rs) = 0
(13.114)

## □ Order ε2:

(A0(r) □ λ0F0(r))ϕ2(r) = λ1F0(r)ϕ1(r) + λ2F0(r)ϕ0(r)
(13.115)
a0n ? ∇ϕ2(rs) + b0ϕ2(rs) + b1ϕ1(rs) = 0
(13.116)
The leading order estimate of the eigenvalue is obtained by multiplying Eq. (13.111)
by ϕ+
0 and integrating over space and summing over groups (indicated by h□i):
λ0 = hϕ+
0 ; A0ϕ0i
hϕ+
0 ; F0ϕ0i
(13.117)
The first-order correction to the eigenvalue is obtained by multiplying Eq.
(13.113) by ϕ+
0 and integrating over space and summing over groups, integrating
the derivative term by parts twice, and using the boundary conditions of Eqs.
(13.106) and (13.114):
λ1 = hϕ+
0 ; D0a□1
0 b1ϕ0iS
hϕ+
0 ; F0ϕ0i
(13.118)
where h□iS indicates an integral over the surface and a sum over groups. The
second-order correction to the eigenvalue is obtained by multiplying Eq. (13.115)
by ϕ+
0 and integrating over space and summing over groups, integrating the
derivative term by parts twice and using the boundary conditions of Eqs. (13.106)
and (13.114):
λ2 = □λ1
hϕ+
0 ; F0ϕ1i
hϕ+
0 ; F0ϕ0i + hϕ+
0 ; D0a□1
0 b1ϕ1iS
hϕ+
0 ; F0ϕ0i
(13.119)
The perturbation theory estimate, through second order, is
λ ' λ0 + λ1 + λ2
= hϕ+
0 ; A0ϕ0i + (1 □ hϕ+
0 ; F0ϕ1i=hϕ+
0 ; F0ϕ0i)hϕ+
0 ; D0a□1
0 b1ϕ0iS + hϕ+
0 ; D0a□1
0 b1ϕ1iS
hϕ+
0 ; F0ϕ0i
(13.120)
To evaluate this second-order estimate, it is necessary to solve Eqs. (13.104),
(13.111), and (13.113), with the associated boundary conditions. The first two

<!-- page 530 (PDF 548) -->
equations, for ϕ+
0 and ϕ0, and their boundary conditions are independent of the
boundary perturbation b1. Upon using Eq. (13.118), Eq. (13.113) for ϕ1 can be
written
A0(r) □ λ0F0(r)
[
]ϕ1(r) = hϕ+
0 ; D0a□1
0 b1ϕ0iSF0(r)ϕ0(r)
hϕ+
0 ; F0ϕ0i
(13.121)
showing that the amplitude of ϕ1 depends on the magnitude of the perturbation
in boundary condition b1. The first-order perturbation theory estimate is λ = λ0
+ λ1 and corresponds to omitting the ϕ1 terms in Eq. (13.120), which obviates the
necessity of calculating ϕ1.

## References

1 W. M. STACEY, Variational Methods in Nuclear Reactor Physics, Academic Press,
New York (1974).
2 W. M. STACEY and J. A. FAVORITE, “Variational Reactivity Estimates,” Joint Int.
Conf. Mathematical Methods and Supercomputing for Nuclear Applications I,
American Nuclear Society, La Grange Park, IL (1997), pp. 900–909.
3 J. DEVOOGHT, “Higher-Order Variational Principles and Iterative Processes,” Nucl.
Sci. Eng. 41, 399 (1970).
4 G. C. POMRANING,“Generalized Variational Principles for Reactor Analysis,” Proc.
Int. Conf. Utilization of Research Reactors and Mathematics and Computation,
Mexico, D.F. (1966), p. 250.

## Further Reading

BELL G. I. and GLASSTONE S., Nuclear Reactor Theory, Van Nostrand Reinhold, New
York (1970), Chap. 6.
CACUCI D. G., “Sensitivity Theory for Nonlinear Systems,” J. Math. Phys. 22 2794
and 2803 (1981).
CACUCI D. G., WEBER C. F., OBLOW E. M., and MARABLE J. H., “Sensitivity Theory for
General Systems of Nonlinear Equations,” Nucl. Sci. Eng. 75, 88 (1980).
FRANCIS N. C., STEWART J. C., BOHL L. S., and KRIEGER T. J., “Variational Solutions of
the Transport Equation,” Prog. Nucl. Energy Ser. I 3, 360 (1958).
GANDINI A., “A Generalized Perturbation Method for Bilinear Functionals of the
Real and Adjoint Neutron Fluxes,” J. Nucl. Energy Part A/B 21, 755 (1967).
GANDINI A., “Generalized Perturbation Theory (GPT) Methods: A Heuristic
Approach,” in J. LEWINS and M. BECKER, eds., Advances in Nuclear Science and
Technology, Vol. 19, Plenum Press, New York (1987).
GREENSPAN E., “Developments in Perturbation Theory,” in J. LEWINS and M. BECKER,
eds., Advances in Nuclear Science and Technology, Vol. 9, Plenum Press, New
York (1976).

<!-- page 531 (PDF 549) -->
KOMATA M., “Generalized Perturbation Theory Applicable to Reactor Boundary
Changes,” Nucl. Sci. Eng. 64, 811 (1977).
LARSEN E. W. and POMRANING G. C., “Boundary Perturbation Theory,” Nucl. Sci. Eng.
77, 415 (1981).
LAURIN-KOVITZ K. F. and LEWIS E. E., “Solution of the Mathematical Adjoint
Equations for an Interface Current Nodal Formulation,” Nucl. Sci. Eng. 123, 369
(1996).
LEWINS J., Importance: The Adjoint Function, Pergamon Press, Oxford (1965).
LEWINS J., “A Variational Principle for Ratios in Critical Systems,” J. Nucl. Energy
Part A/B 20, 141 (1966).
POMRANING G. C., “A Variational Description of Dissipative Processes,” J. Nucl.
Energy Part A/B 20, 617 (1966).
POMRANING G. C., “The Calculation of Ratios in Critical Systems,” J. Nucl. Energy
Part A/B 21, 285 (1967).
POMRANING G. C., “Variational Principles for Eigenvalue Equations,” J. Math. Phys. 8,
149 (1967).
POMRANING G. C., “A Derivation of Variational Principles for Inhomogeneous
Equations,” Nucl. Sci. Eng. 29, 220 (1967).
RAHNEMA F. and POMRANING G. C., “Boundary Perturbation Theory for
Inhomogeneous Transport Equations,” Nucl. Sci. Eng. 84, 313 (1983).
RONEN Y., ed., Uncertainty Analysis, CRC Press, Boca Raton, FL (1988).
SELENGUT D. S., Variational Analysis of Multidimensional Systems, Hanford
Engineering Laboratory report HW-59126 (1959).
STACEY W. M., “Variational Estimates of Reactivity Worths and Reaction Rate Ratios
in Critical Systems,” Nucl. Sci. Eng. 48, 444 (1972).
STACEY W. M., “Variational Estimates and Generalized Perturbation Theory for
Ratios of Linear and Bilinear Functionals,” J. Math. Phys. 13, 1119 (1972).
TAIWO T. A. and HENRY A. F., “Perturbation Theory Based on a Nodal Model,” Nucl.
Sci. Eng. 92, 34 (1986).
USACHEV L. N., “Perturbation Theory for the Breeding Ratio and Other Number
Ratios Pertaining to Various Reactor Processes,” J. Nucl. Energy Part A/B 18, 571
(1964).
WILLIAMS M. L., “Perturbation Theory for Nuclear Reactor Analysis,” in Y. RONEN,
ed., CRC Handbook of Nuclear Reactor Calculations I, CRC Press, Boca Raton, FL
(1986).

## Problems

### 13.1

Use one-speed diffusion theory and perturbation theory to estimate the
reactivity worth of a 0.25% increase in the fission cross section over the left
half of a critical slab reactor of 1-m thickness.

### 13.2

Use two-group diffusion theory and perturbation theory to estimate the
reactivity worth of a 0.5% change in the thermal absorption cross section
of a very large core described by: group 1–D = 1.2 cm, Σa = 0.012 cm□1,

<!-- page 532 (PDF 550) -->
Σ1→2 = 0.018 cm□1, νΣf = 0.006 cm□1; group 2–D = 0.40 cm, Σa = 0.120
cm□1, νΣf = 0.150 cm□1.

### 13.3

Prove that each term in the importance equation (Eq. (13.17)) is mathematically
adjoint to the corresponding term in the neutron transport
equation (Eq. (13.19)).

### 13.4

Derive the multigroup discrete ordinates adjoint equation for a critical
reactor (a) directly from the discrete ordinates equations and (b) by making
the discrete ordinates approximation of the adjoint transport equation.

### 13.5

Derive an explicit expression for the perturbation theory reactivity estimate
in the multigroup discrete ordinates representation of neutron
transport.

### 13.6

Solve for the infinite medium neutron flux and adjoint energy distributions
in a three-group representation: group 1 – Σa = 0.030 cm□1, Σ1→2
= 0.060 cm□1, νΣf = 0.004 cm□1; group 2 – Σa = 0.031 cm□1, Σ2→3 = 0.088
cm□1, νΣf = 0.018 cm□1; group 3–Σa = 0.120 cm□1, νΣf = 0.180 cm□1.

### 13.7

Carry through the derivation to show that ρvarfϕ+
0 ; ϕ; Γ+
0 g = ρexfϕ+
0 ; ϕexg
+ O(δϕ2; δϕδΓ), where Γ+
ex = Γ+
0 + δΓ+ and Γ+
0 is obtained by solving
Eq. (13.32).

### 13.8

Consider a critical slab reactor with one-speed diffusion theory constants
D = 1.0 cm, Σa = 0.15 cm□1, and νΣf = 0.16 cm□1. Calculate the flux correction
function, Γ+
0 , from Eq. (13.32) for a 1% change in the absorption
cross section in the left one-fourth of the critical slab. (Hint: Note that Γ+
is orthogonal to ϕ+
0 = ϕ0 and expand Γ+
0 in the higher harmonics of the
critical reactor eigenfunctions.)

### 13.9

Evaluate the variational/generalized perturbation reactivity estimate of
Eq. (13.36) for Problem 13.8.

### 13.10

Carry out the missing steps of the derivation in Section 13.4 to show that
RRvarfϕ0; Γ+
R0g □ RRexfϕexg = OfδΓ+
Rδϕg.

### 13.11

Consider a critical bare slab reactor described by one-speed diffusion
theory with D = 1.0 cm, Σa = 0.15 cm□1, and νΣf = 0.16 cm□1. Use Eq.
(13.47) to evaluate the variational estimate for a 1% increase in absorption
cross section on the absorption-to-fission rate ratio in the right one-tenth
of the slab core.

### 13.12

Use the Rayleigh quotient to estimate the effective multiplication constant
for a bare cylindrical core with H/D = 1, H = 2 m and one-speed diffusion
theory parameters D = 1.0 cm, Σa = 0.15 cm□1, and νΣf = 0.16 cm□1.

<!-- page 533 (PDF 551) -->
### 13.13

In the window shade model, a control rod bank can be represented by a
10% increase in Σa for Problem 13.11. Use the Rayleigh quotient to
estimate the effective multiplication constant when the control rod
bank is inserted halfway, using the flux and adjoint distributions
calculated in Problem 13.11. Recalculate the effective multiplication
constant directly (i.e., solve the two-region diffusion theory problem)
for the control rod bank inserted halfway and compare with the
variational estimate.

### 13.14

Consider a uniform slab nonfissioning assembly of width 50 cm in
which there is a uniform source Sf of fast neutrons in the left half.
Calculate the thermal absorption rate in the right half (a) directly and
(b) using the Schwinger variational estimate evaluated trial functions,
obtain from an infinite medium calculation with a source 1/2Sf. Use
the two-group representation: fast group – D = 2.0 cm, Σa = 0.006
cm□1, and Σ1→2 = 0.018 cm□1; thermal group – D = 0.40 cm and
Σa = 0.120 cm□1.

### 13.15

Repeat the derivation of Section 13.3 for multigroup diffusion theory.

### 13.16

Discuss how the result of Eq. (13.55) could be employed to calculate the
response of a localized detector to a point neutron source some
distance away if the adjoint function is known in the vicinity of the
source.

### 13.17

Carry through the steps in deriving the variational synthesis approximation
of Eq. (13.81).

### 13.18

Demonstrate that stationarity of the variational functional of Eq. (13.83)
requires that the diffusion equation be satisfied and that the flux and
current be continuous at the interface y = yi. (Hint: Consider arbitrary and
independent variations of the adjoint flux and current within the volume
and on the interface.)

### 13.19

Derive the transport Eq. (13.100) and the associated boundary conditions
of Eq. (13.101) from the stationarity of the functional of Eq. (13.99).

### 13.20

Consider a uniform slab reactor of thickness 2a with zero flux conditions
at each boundary, which may be represented as a slab with a zero flux
condition at x = 0 and a symmetry ^n ? ∇ϕ = 0 condition at x = a. Use
boundary perturbation theory to derive an estimate for the change in
eigenvalue, λ1, that would result from replacing the symmetry condition at
x = a with the condition ^n ? ∇ϕ + b1ϕ = 0.

### 13.21

In a critical uniform slab reactor in one-group theory, 10% of the neutrons
leak from the reactor and the other 90% are absorbed. Use perturbation

<!-- page 534 (PDF 552) -->
theory to calculate the reactivity worth of a 5% increase in absorption
cross section over the right half of the reactor. Discuss the error in this
estimate due to the failure to take into account the change in flux
distribution caused by the increase in absorption cross section. Would
the perturbation theory estimate be expected to underpredict or overpredict
the reactivity worth because of this error? Discuss how the effect
of this flux change on the reactivity worth could be taken into account
without actually calculating the flux change.
