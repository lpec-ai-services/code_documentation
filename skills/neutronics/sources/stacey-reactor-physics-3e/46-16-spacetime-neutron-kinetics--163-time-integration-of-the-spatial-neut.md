# 16 Space–Time Neutron Kinetics — 16.3 Time Integration of the Spatial Neutron Flux Distribution
<!-- source PDF pages 652-667 -->

<!-- page 635 (PDF 652) -->
## 16.3 Time Integration of the Spatial Neutron Flux Distribution

The various methods that have been discussed for calculating the spatial neutron
flux distribution (finite-difference, nodal, finite-element, synthesis, etc.) can be
extended to calculate the space–time neutron flux distribution by adding a
neutron density time derivative, distinguishing between prompt and delayed
neutron sources in the neutron balance equation, and appending equations to
calculate the delayed neutron precursor densities (e.g., Eqs. (16.20) and (16.21)).
Writing the group fluxes and precursor densities at every spatial point (e.g., mesh
point, node) as a column vector ψ, and writing the terms of the multigroup
neutron and delayed neutron precursor balance equations at each spatial point as
a matrix H, the space–time neutron kinetics equations can be written as a coupled
set of ordinary differential equations
Hψ = _ψ
(16.52)

### Explicit Integration: Forward-Difference Method

The simplest approximate solution to Eq. (16.52) is obtained by a simple forwarddifference
algorithm,
ψ(p + 1) = ψ(p) + Δt H(p)ψ(p)
(16.53)
where the argument p denotes the value at time tp, and Δt = tp+1 □ tp. In terms of
the multigroup diffusion equations, this algorithm is
ϕg(p + 1) = ϕg(p) + Δtvg
∇? Dg(p)∇ϕg(p) □ [Σg
a(p) + Σg
s(p)]ϕg(p)
(
+
X
G
g´=1
Σg´!g
s
(p)ϕg´(p)
+ (1 □ β)χg
p
X
G
g´=1
vΣg´
f (p)ϕg´(p)
+
X
M
m=1
λmχg
mCm(p)
)
;
g = 1; . . . ; G
(16.54)
and for the precursors,
Cm(p + 1) = Cm(p) + Δt βm
X
G
g=1
vΣg
f (p)ϕg(p) □ λmCm(p)
"
;
m = 1; . . . ; M
(16.55)
where the spatial dependence is implicit.

<!-- page 636 (PDF 653) -->
This algorithm suffers from a problem of numerical stability, which requires
the use of such small time steps that the advantage offered by the simplicity of the
algorithm is usually more than offset by the large number of time steps required.
The nature of this problem is seen by considering an expansion of ψ(p) in the
eigenfunctions of the operator H:
ψ(p) =
X
n
anΩn
(16.56)
where
HΩn = ωnΩn
(16.57)
Substituting Eq. (16.56) into Eq. (16.53) yields
ψ(p + 1) =
X
n
an(1 + ωnΔt)Ωn
(16.58)
The condition for numerical stability is that the fundamental mode Ω1 grow
more rapidly than the harmonics Ωn, n □ 2. This requires that
j1 + ω1Δtj > j1 + ωnΔtj;
n □ 2
(16.59)
To ensure this, |ωnΔt| must be much less than unity. The eigenvalue problem of
Eq. (16.57) is a generalization to several groups and many spatial points of the inhour
equation of Section 5.3. The magnitude of the fundamental eigenvalue is on
the order of the precursor decay constant, except for highly supercritical
transients, in which case small time steps must be used in any case. Numerical
studies have shown that the smallest eigenvalues can be on the order of □(vgΣg
a),
which can be about □104 for thermal neutrons and about □107 for fast neutrons.
Thus, Δt < 10□7 may be required for stability. When the time derivative terms
for the epithermal groups are assumed to vanish (a useful approximation since
1/vG ≫1/vg, g ≠G), Δt < 10□4 may be required.

### Implicit Integration: Backward-Difference Method

The numerical stability problem associated with the preceding method can be all
but eliminated by the backward-difference algorithm:
ψ(p + 1) = [I □ Δt H(p + 1)]□1ψ(p)
(16.60)
In terms of the precursor and multigroup diffusion equations, this algorithm is
Cm(p + 1) =
Cm(p)
1 + λmΔt +
βmΔt
1 + λmΔt
X
G
g=1
vΣg
f (p + 1)ϕg(p + 1);
m = 1; . . . ; M
(16.61)

<!-- page 637 (PDF 654) -->
∇? Dg(p + 1)∇ϕg(p + 1) + [Σg
a(p + 1) + Σg
s(p + 1)]ϕg(p + 1)
+
X
G
g´=1
Σg´!g
s
(p + 1)ϕg´(p + 1) + (1 □ β)χg
p
X
G
g´=1
vΣg´
f (p + 1)ϕg´(p + 1)
+
X
M
m=1
λmχg
mβmΔt
1 + λmΔt
X
G
g´=1
vΣg´
f (p + 1)ϕg´(p + 1) □
vgΔt ϕg(p + 1)
= □
vgΔt ϕg(p) □
X
M
m=1
λmχg
mCm(p)
1 + λmΔt ;
g = 1; . . . ; G
(16.62)
An expansion of the type of Eq. (16.56) substituted into Eq. (16.60) yields
ψ(p + 1) =
X
n
an(1 □ Δtωn)□1Ωn
(16.63)
and the condition for stability is
j(1 □ Δtω1)□1j > j(1 □ Δtωn)□1j;
n □ 2
(16.64)
The method is unconditionally stable if 0 > Re{ω1} > Re{ωn}, n □ 2. For Re{ω1} > 0,
the stability requirement is determined by the requirement that ψ (p + 1) be a
positive vector, which necessitates that
□
X
G
g´=1
Σg´!g
s
(p)ϕg´(p)
(16.65)
This requirement is restrictive only for large ω1 that correspond to fast transients
where small time steps would be necessary in any case.
The difficulty with the backward-difference method arises from the necessity of
inverting a matrix at each time step. The actual matrix that must be inverted is the
coefficient matrix for the left side of Eq. (16.62); the delayed neutrons can be
determined directly. Thus, although much larger time steps can be taken with the
implicit method than with the explicit method, the computation time needed for
the matrix inversions may more than offset this advantage. The size time step
used in the backward-difference method is usually limited by the effect of
truncation error (of order Δt2) upon the accuracy of the solution rather than
by numerical stability.

### Implicit Integration: θ Method

For a constant H in the interval tp ≤ t ≤ tp+1, Eq. (16.52) has the formal solution
ψ(p + 1) = exp(ΔtH)ψ(p) =
I + ΔtH + Δt2
2! H2 + ∙∙∙

ψ(p)
(16.66)

<!-- page 638 (PDF 655) -->
The algorithms of Eqs. (16.53) and (16.60) may be considered as approximations
to Eq. (16.66). An improved algorithm results from the prescription
ψ(p + 1) □ ψ(p) = Δt[Mψ(p + 1) + (H □ M)ψ(p)]
(16.67)
with matrix elements of M and H related by
mij = θijhij
(16.68)
where the mij, thus the θij, are chosen so that ψ (p + 1) calculated from Eq. (16.67)
agrees with ψ (p + 1) calculated from Eq. (16.66). This requires that
M = 1
Δt I □ H[exp(ΔtH) □ I]□1
(16.69)
Assuming that H has distinct eigenvalues, it may be diagonalized by the
transformation
(J +)TH J = Γ
(16.70)
where J and J+ are the modal matrices corresponding to H and HT (i.e., the
columns of J and J+ are the eigenvectors of H and HT, respectively), and Γ is a
diagonal matrix composed of the eigenvalues of H. Thus
(J +)TMJ = 1
Δt I □ Γ[exp(ΔtΓ) □ I]□1 = L
(16.71)
with L diagonal. From this it follows that
M = JL(J +)T
(16.72)
and the factors θij can be determined from
θij = mij
hij
after the mij are found from Eq. (16.72).
Because solving for the θij rigorously would entail a great deal of effort, several
approximations are made in employing this method to arrive at an algorithm for
solutions of the multigroup kinetics equations. The delayed neutrons are treated
as sources, and thus are neglected in the determination of the θij. An average space
independent value of θij is calculated based on a flux square weighting procedure.
The delayed neutron precursors have a separate θij. Denoting the θij associated

<!-- page 639 (PDF 656) -->
with groups g and g´ as θgg´ and θij associated with the delayed neutrons as θd, the
following algorithm results:
Cm(p + 1) = 1 □ (1 □ θd)λmΔt
1 + θdλmΔt
Cm(p) +
Δtβm
1 + θdλmΔt
□
X
G
g=1
vΣg
f (p + 1)ϕg(p + 1)θ1g
"
+
X
G
g=1
vΣg
f (p)ϕg(p)(1 □ θ1g)
;
m = 1; . . . ; M
(16.73)
θggf∇? Dg(p + 1)∇ϕg(p + 1) □ [Σg
a(p + 1) + Σg
s(p + 1)]ϕg(p + 1)g
+
X
G
g´=1
θgg´Σg´!g
s
(p + 1)ϕg´(p + 1)
+ χg
p(1 □ β)
X
G
g´=1
θgg´vΣg´
f (p + 1)ϕg´(p + 1) □
Δtvg ϕg(p + 1)
+
X
M
m=1
χg
mλmΔtβmθd
1 + θdλmΔt
X
G
g´=1
vΣg´
f (p + 1)ϕg´(p + 1)θ1g´
= □ (1 □ θgg)f∇? Dg(p)∇ϕg(p) □ [Σg
a(p) + Σg
s(p)]ϕg(p)g
□
X
G
g´=1
(1 □ θgg´)Σg´!g
s
(p)ϕg´(p)
□ (1 □ β)χg
p
X
G
g´=1
(1 □ θgg´)vΣg´
f (p)ϕg´(p)
□
Δtvg ϕg(p) □
X
M
m=1
χg
mλmCm(p)
1 + θdλmΔt
□
X
M
m=1
χg
mθdλmΔtβm
1 + θdλmΔt
X
G
g´=1
vΣg´
f (p)ϕg´(p)(1 □ θ1g´)
g = 1; . . . ; G
(16.74)
In the limit θgg´ θd →1, Eqs. (16.73) and (16.74) reduce to the backwarddifference
algorithms of Eqs. (16.61) and (16.62), while Eqs. (16.73) and (16.74)
reduce to the forward-difference algorithms of Eqs. (16.54) and (16.55) in the limit
θgg´ θd →0. As mentioned, a number of approximations are made in arriving at
Eqs. (16.73) and (16.74), so the mathematical properties associated with Eqs.
(16.67)–(16.72) are not rigorously retained by Eqs. (16.73) and (16.74).
Insight into the stability properties of the θ-method can be gained by considering
the situation for a constant matrix H and a constant time step Δt. Expanding
the exact solutions of Eq. (16.52) in the eigenfunctions Ωn, of H given by

<!-- page 640 (PDF 657) -->
Eq. (16.57),
ψ(tp) =
X
N
n=1
anΩneωntp =
X
N
n=1
anΩneωn(pΔt)
(16.75)
where the expansion coefficients an are determined from the initial conditions
and where ω1 > ω2 > ∙∙∙> ωN. For the same eigenfunctions to satisfy Eq.
(16.67), which becomes
γnΩn = (I □ Δt M)□1(I + Δt H □ Δt M)Ωn
(16.76)
the eigenvalues must be related by
γn = 1 + (1 □ θ)ωnΔt
1 □ θωnΔt
(16.77)
The general solution for the θ-approximation of Eq. (16.67) may be written as
ψ(tp) =
X
N
n=1
anγp
nΩn
(16.78)
where tp = pΔt. Comparison with the exact solution of Eq. (16.75) indicates that
exp(ωnt) = exp(ωnpΔt) has been replaced by γp
n in the approximate solution. For a
stable θ approximation, γn > □1; otherwise, γp
n will oscillate and diverge as time
increases. Thus, Eq. (16.77) and the eigenvalues ωn can be used to determine a
maximum stable step size Δt.
Numerical experience indicates that the algorithm of Eqs. (16.73) and (16.74) is
(1) numerically stable for time steps two orders of magnitude greater than are
required for stability of Eqs. (16.54) and (16.55) and (2) somewhat more accurate
than the algorithm of Eqs. (16.61) and (16.62) for the same time steps. The
algorithm of Eqs. (16.74) requires inversion of the same type of matrix as does the
backward-difference algorithm of Eqs. (16.62), and, in addition, requires computation
of θgg´ and θd, although the latter computation is negligible with respect to
the time required for the matrix inversion. In practice, the θ’s are predetermined
based on experience or intuition.

### Implicit Integration: Time-Integrated Method

The delayed neutron precursor equations may, in principle, be integrated directly
between tp and tp+1:
Cm(p + 1) = exp(□λmΔt)Cm(p) + βmltp+1
p
dtexp[□λm(tp+1 □ t)]
X
G
g=1
vΣg
f (t)ϕg(t)
(16.79)

<!-- page 641 (PDF 658) -->
If the assumption is made that the group-fission rate at each point varies linearly
in time in the interval tp ≤ t ≤ tp+1, Eq. (16.79) yields an implicit integration
algorithm for the precursors,
Cm(p+1) = exp(□λmΔt)C(p)+βm
λm
1□exp(□λmΔt)
λmΔt
□exp(□λmΔt)

X
G
g=1
vΣg
f (p)ϕg(p)
(
□ 1□exp(□λmΔt)
λmΔt
□1

X
G
g=1
vΣg
f (p+1)ϕg(p+1)
)
(16.80)
Integration of the multigroup diffusion equation over the interval tp ≤ t ≤ tp+1,
with the assumption that all reaction rates vary linearly in that interval, results in
an implicit integration algorithm for the neutron flux,
∇? Dg(p + 1)∇ϕg(p + 1) □ [Σg
a(p + 1) + Σg
s(p + 1)]ϕg(p + 1)
+
X
G
g´=1
Σg´!g
s
(p + 1)ϕg´(p + 1)
+
χg
p □
X
M
m=1
βm(χg
p □ χg
m) +
X
M
m=1
Δt
χg
mβm
λm
1 □ exp(□λmΔt)
λmΔt
□ 1

(
)
□
X
G
g´=1
vΣg´
f (p + 1)ϕg´(p + 1) □
vgΔt ϕg(p + 1)
= □ 2
Δt
X
M
m=1
χg
m 1 □ exp(□λmΔt)
[
]Cm(p) □
vgΔt ϕg(p)
□
χg
p □
X
M
m=1
βm(χg
p □ χg
m)
(
□
X
M
m=1
Δt
χg
mβm
λm
1 □ exp(□λmΔt)
λmΔt
□ exp(□λmΔt)

)
□
X
G
g´=1
vΣg´
f (p)ϕg´(p) □ ∇? Dg(p)∇ϕg(p) + [Σg
a(p) + Σg
s(p)]ϕg(p)
□
X
G
g´=1
Σg´!g
s
(p)ϕg´(p)
(16.81)
In arriving at Eq. (16.81), integration of the precursors was treated as in Eq. (16.80)
(i.e., the group-fission rate was assumed to vary linearly).

<!-- page 642 (PDF 659) -->
Equations (16.80) and (16.81) define the time-integrated algorithm, which, like
Eqs. (16.73) and (16.74), represents an attempt to reduce the truncation error
associated with the simple implicit integration formulas of Eqs. (16.61) and (16.62)
without materially increasing the computational time required to obtain a solution.
All three implicit integration algorithms require inversion (at each time step) of
roughly the same matrix. Numerical experience indicates that the θ-method and
the time-integrated method yield essentially identical results, and that both
methods are somewhat more accurate than the backward-difference method.

### Implicit Integration: GAKIN Method

The mathematical properties of this method derive directly from the properties of
the spatial finite-difference approximation. This approximation is
_θ = Kθ
(16.82)
where
θ =
ψ1
...
ψG
d1
..
.
dM
(16.83)
with ψg and dm representing N × 1 column vectors of group fluxes and m-type
precursor densities, respectively, at each of N spatial mesh points. The matrix K
can be written in terms of N × N submatrices Kij:
K =
K 11
K 12
K 13
∙∙∙
K 1;G+M
K 21
K 22
K 23
∙∙∙
K 2;G+M
..
.
..
.
K G+M;1
K G+M;2
∙∙∙
K G+M;G+M
(16.84)
The N × N matrices Kij are split,
K i j = Γi j + viDi;
1 ≤ i ≤ G
(16.85)
where Di represents the coupling among mesh points due to the diffusion term.
By splitting K into a matrix L, which contains all the submatrices below the
diagonal block; a matrix U, which contains all the submatrices above the diagonal

<!-- page 643 (PDF 660) -->
block; and into the block diagonal matrices Γ and D,
L =
∙∙∙
K 21
∙∙∙
..
.
..
.
K G+M;1
K G+M;2
∙∙∙
(16.86)
U =
K 12
K 13
∙∙∙
K 1;G+M
K 23
∙∙∙
K 2;G+M
...
∙∙∙
(16.87)
Γ =
Γ11
∙∙∙
Γ22
∙∙∙
∙∙∙
ΓGG
∙∙∙
∙∙∙
K G+1;G+1
..
.
..
.
∙∙∙
K G+M;G+M
(16.88)
D =
v1D1
∙∙∙
v2D2
∙∙∙
∙∙∙
...
...
vGDG
∙∙∙
∙∙∙
∙∙∙
∙∙∙
...
...
∙∙∙
(16.89)
Equation (16.82) may be written as
_θ □ Γθ = (L + U)θ + Dθ
(16.90)
This equation may formally be integrated over the interval tp ≤ t ≤ tp+1:
θ(tp+1) = exp(ΔtΓ)θ(tp) + ∫
Δt
dt´exp[(Δt □ t´)Γ](L + U)θ(tp + t´)
+∫
Δt
dt´exp[(Δt □ t´)Γ]Dθ(tp + t´)
(16.91)

<!-- page 644 (PDF 661) -->
In the first integral of Eq. (16.91), the approximation
θ(tp + t´) = exp(ωt´)θ(tp)
(16.92)
is made, and the second integral is performed with the approximation
θ(tp + t´) = exp[□ω(Δt □ t´)]θ(tp+1)
(16.93)
In general, ω is a diagonal matrix. Using Eqs. (16.92) and (16.93) in Eq. (16.91)
results in
[I □ (ω □ Γ)□1(I □ exp[(Γ □ ω)Δt])D]θ(tp+1)
= [exp(Γ Δt) + (ω □ I)□1(exp(ωΔt) □ exp(Γ Δt))(L + U)]θ(tp)
(16.94)
which may be written as
θ(tp+1) = Aθ(tp)
(16.95)
If all the diagonal elements of ω are equal to ω1, which is the eigenvalue of
Kθn = ωnθn
(16.96)
with largest real part, then from Eq. (16.90),
(L + U)θ1 = (ω1I □ Γ □ D)θ1
(16.97)
From the definition of A (with ω = ω1I), it can be shown that
Aθ1 = exp(Δtω1)θ1
(16.98)
It can be shown that ω1 is real and simple, and that θ1 is positive. For all real values
of ω, hence for ω = ω1, A can be shown to be nonnegative, irreducible, and
primitive. From the Perron–Frobenius theorem it follows that A has a simple, real,
largest eigenvalue ρ1 and a corresponding positive eigenvector. The eigenvalue
ρ1 = exp(Δtω1) is seen from Eq. (16.98) to have a positive eigenvector that is the
fundamental-mode solution of the kinetics equations (16.96). If it can be shown
that ρ1 is the largest eigenvalue of A, Eq. (16.98) indicates that the asymptotic
solution of the integration algorithm of Eq. (16.95) is the asymptotic solution of
Eq. (16.82) for a step change in properties, which shows that the method is
unconditionally numerically stable.
The transpose matrix AT has the same properties and eigenvalue spectrum
as A:
ATqn = ρnqn
(16.99)

<!-- page 645 (PDF 662) -->
By the Perron–Frobenius theorem, AT has a real, simple eigenvalue, ρk, which is
larger than the real part of the other eigenvalues, and the corresponding
eigenvector is positive. Premultiplying Eq. (16.93) for n = k by θT
1 , premultiplying
Eq. (16.98) by qT
1 , and subtracting yields
0 = [exp(Δtω1) □ ρ1]θT
1 q1
(16.100)
Because θ1 and q1 are positive, Eq. (16.100) is satisfied only if
exp(Δtω1) = ρ1
is the real eigenvalue. Thus, the method is numerically unconditionally stable.
Inversion of the matrix on the left of Eq. (16.94) to obtain A can be accomplished
by the inversion of GN × N matrices. In practice, an approximation to ω1
is obtained by an expression of the form
ω1 = 1
Δt ln θi(tp)
θi(tp□1)
(16.101)
where i indicates some component or components of the θ vector, and different
values of ω1 are used in different parts of the reactor (i.e., ω ≠ω1I).

### Alternating Direction Implicit Method

The implicit integration methods of previous sections all reduced to an algorithm
for the neutron flux that required the inversion of a matrix at each time step.
When the finite-difference spatial approximation is employed, this matrix is
NG × NG, where N is the number of mesh points and G is the number of energy
groups. In one-dimensional problems, the matrix to be inverted becomes block
tridiagonal with G × G blocks, and inversion can be accomplished by the
backward-elimination/forward-substitution method and requires the inversion
of N G × G matrices. In the GAKIN method, this matrix inversion can be
accomplished by inverting G N × N matrices.
However, for multidimensional problems, the matrix inversion associated
with the implicit methods poses a formidable and time-consuming task.
Alternative formulations of the θ and GAKIN methods have been proposed
to reduce the time required for this matrix inversion. Another technique,
designed to eliminate this same problem, is the alternating direction implicit
(ADI) method. The basis of the ADI method is to make the algorithm implicit
for one space dimension at a time and to alternate the space dimension for
which the algorithm is implicit. The ideas involved are illustrated by a twodimensional
problem. The equation for the group g neutron flux can be written
in the notation of Section 16.2 as
_ψg =
vgDg
x + 1
2 Γgg

ψg +
vgDg
y + 1
2 Γgg

ψg
+
X
G
g´=1
K gg´ψg´ +
X
M
m=1
K g;G+mdm
(16.102)

<!-- page 646 (PDF 663) -->
where the N × N diffusion matrix Dg, which represents
@
@x Dg @
@x + @
@y Dg @
@y
has been separated into Dg
x, which represents
@
@x Dg @
@x
and Dg
y, which represents
@
@y Dg @
@y
For the time step tp to tp + 1, an integration algorithm that is implicit in the
x-direction and explicit in the y-direction is chosen. First define
Hg
x ≡ vgDg
x + 1
2 Γgg
Hg
y ≡ vgDg
y + 1
2 Γgg
(16.103)
then the algorithm is written as
ψg(p + 1) □ ψg(p)
= Δt Hg
x(p + 1)ψg(p + 1) + Hg
y(p)ψg(p) +
X
G
g´□1
K gg´(p)ψg´(p)
"
+
X
M
m□1
K g;G+m(p)dm(p)
;
g = 1; . . . ; G
or
[I □ ΔtHg
X(p + 1)]ψg(p + 1) = [I + ΔtHg
y(p)]ψg(p) + Δt
X
G
g´=1
K gg´(p)ψg´(p)
"
+
X
M
m=1
K g;G+m(p)dm(p)
;
g = 1 ; . . . ; G (16.104)
For the time step tp+1 to tp+2, an algorithm that is implicit in the y-direction and in
the removal, scattering, fission, and precursor terms is chosen:

<!-- page 647 (PDF 664) -->
ψg(p + 2) □ ψg(p + 1)
= Δt Hg
x(p + 1)ψg(p + 1) + Hg
y(p + 2)ψg(p + 2)
"
+
X
G
g´=1
K gg´(p + 2)ψg´(p + 2)
+
X
M
m=1
K g;G+m(p + 2)dm(p + 2)
;
d = 1; . . . ; G
(16.105)
Use, for the sake of definiteness, the implicit integration formulas of Eq. (16.61)
for the precursors,
dm(p + 2) =
1 + λmΔt dm(p + 1) +
βm
1 + λmΔt
X
G
g=1
Fg(p + 2)ψg(p + 2)
(16.106)
where FG is an N × N diagonal matrix representing vΣg
f associated with each point.
Using Eq. (16.106), Eq. (16.105) becomes
[I □ ΔtHg
y(p + 2)]ψg(p + 2)
□Δt
X
G
g´=1
K gg´(p + 2)ψg´(p + 2) +
X
M
m=1
K g;G+m(p + 2)
βm
1 + λmΔt
"
□
X
G
g´=1
Fg´(p + 2)ψg´(p + 2)
= [I + ΔtHg
x(p + 1)]ψg(p + 1)
+ Δt
X
M
m=1
1 + λmΔt K g;G+m(p + 2)dm(p + 1);
g = 1; . . . ; G
(16.107)
The solution proceeds by alternating between the algorithms of Eqs. (16.104) and
(16.107). If there are N1/2 mesh points in both the x- and y-directions, the matrices
that must be inverted in order to solve Eqs. (16.104) and (16.107) can be
partitioned so that, rather than inverting an NG × NG matrix, N1/2 N1/2G × N1/
2G matrices are inverted. This happens because the matrix to be inverted in Eqs.
(16.104) couples mesh points only in the x-direction, and the matrix to be inverted
in Eq. (16.107) couples mesh points only in the y-direction. In the case of Eq.
(16.104), each of the N1/2G × N1/2 G matrices can be further partitioned into G N1/
2 × N1/2 matrices, because the neutron source terms due to fission, scattering, and
precursor decay are treated explicitly in this step. More general algorithms treat
these source terms implicitly in both steps.

<!-- page 648 (PDF 665) -->
### Stiffness Confinement Method

The set of neutron and delayed neutron precursor equations are referred to as stiff
because of the great difference in the time constants that govern the prompt
neutron and precursor responses. The accuracy and stability of numerical integration
methods are usually determined by the shortest time constant, the prompt
neutron lifetime, which has little effect on the precursor solution. The stiffness
confinement method seeks to confine the difficulty to the neutron equations by
decoupling the precursor equations through the definition of dynamic frequencies:
ωg
ϕ(r; t) ≡ 1
ϕg
@ϕg
@t ;
ωm
c ≡ 1
Cm
@Cm
@t
(16.108)
These definitions can be used to replace the time derivatives in the multigroup
diffusionandprecursorequations,whichallowthelattertobeformallysolvedandused
to evaluate the precursor densities in the multigroup diffusion equations, resulting in
∇? Dg(r; t)ϕg(r; t) □ Σg
t +
ωg
ϕ(r; t)
vg
"
ϕg(r; t) +
X
G
g´=1
Σg´!g(r; t)ϕg´(r; t)
+
(1 □ β)χg
p +
X
M
m=1
βmλmχg
m
ωm
c (r; t) + λm
(
)X
G
g´=1
vΣg´
f (r; t)ϕg´(r; t) = 0;
g = 1; .. . ; G
(16.109)
These equations are identical to the static multigroup diffusion equations, but
with modified total and fission cross sections that include the dynamic frequencies
. Thus, to advance the solution in time, an estimate is made of the dynamic
frequencies, Eqs. (16.109) are solved for the group fluxes, the precursors are
updated, an improved guess of the dynamic frequencies is calculated using the
new flux and precursor values, and the iteration is repeated until convergence.

### Symmetric Successive Overrelaxation Method

Successive overrelaxation is combined with an exponential transformation to
decouple stiffness in the symmetric successive overrelaxation (SSOR) method.
ThematrixHisfirstdecomposedintoalowerL,adiagonalD,andanupperUmatrix:
H = L + D + U
(16.110)
The solution is then advanced iteratively over the (p + 1) time step by a forward
sweep:
ψn+1=2(p + 1) = θ[I □ Δtp+1(L + D)]□1[Δtp+1Uψn(p + 1) + ψ(p)]
+(1 □ θ)ψn(p + 1)
(16.111)

<!-- page 649 (PDF 666) -->
followed by a backward sweep
ψn+1(p + 1) = θ[I □ Δtp+1(D + U)]□1[Δtp+1Lψn+1=2(p + 1) + ψ(p)]
+(1 □ θ)ψn+1=2(p + 1)
(16.112)
where 1 ≤ θ ≤ 2 and n refers to the iteration number.
An exponential transformation of the multigroup fluxes and the precursor
densities
ψ(p + 1) = exp(Δtp+1ω)^ψ(p + 1)
(16.113)
may be made first, using dynamic frequencies calculated from local flux and
precursor values for the present and previous times:
ωg
ϕ ≡
Δtp+1
ln
ϕg(p)
ϕg(p □ 1) ;
ωm
c (p + 1) ≡
Δtp+1
ln
Cm(p)
Cm(p □ 1)
(16.114)
With the transformation of Eq. (16.113), Eq. (16.52) becomes
@
@t ^ψ = exp(□Δtp+1ω) H □ ω
[
]exp(Δtp+1ω)^ψ
(16.115)
which is integrated using the overrelaxation procedure of Eqs. (16.111) and (16.112).
The dynamic frequencies are estimated at the beginning of the time step
from Eqs. (16.114) to determine ω0. A global frequency correction factor Δωn
is computed on each iteration by considering Eqs. (16.111) and (16.112) to
each advance the solution a half time step. The dynamic frequency is then
corrected
Ωn = Ω0 + ωnI
(16.116)
where now Ω is a matrix containing the local values of the frequencies ω.

### Generalized Runge–Kutta Methods

Runge–Kutta methods have long been popular for integrating ordinary differential
equations, but the requirement for small time steps to achieve sufficient
accuracy has limited their application in solving space-discretized space–time
neutron kinetics problems. However, generalizations of these methods to allow
larger time steps and increased stability [1] have recently been applied to these
problems. The Runge–Kutta method is based on an explicit time differencing of

<!-- page 650 (PDF 667) -->
Eq. (16.52) and a linear Taylor’s series approximation:
ψ(p + 1) = ψ(p) + Δtp+1H(p + 1)ψ(p + 1)
' ψ(p) + Δtp+1 H(p)ψ(p) + Δtp+1
@
@ψ (Hψ)
p
(
"
□
Δtp+1
ψ(p + 1) □ ψ(p)

)#
(16.117)
where the term @(Hψ)/@ψ|p is the partial derivative of the left side of Eq. (16.52)
with respect to the appropriate multigroup neutron flux or delayed neutron
precursor density evaluated at the beginning of the time step, t = tp.
The generalized Runge–Kutta methods are based on the algorithm
y(p + 1) = y(p) +
X
s
i=1
ciK i(p + 1)
(16.118)
for advancing the solution from tp to tp+1, where s is the number of stages, ci are
fixed expansion coefficients, and the column vectors K(p + 1) are found by solving
a system of N (the number of energy groups times discrete spatial points plus the
number of delayed neutron precursor groups times the number of discrete spatial
points) linear equations for each of the s stages (i.e., for s different right sides for
each time step):
I □ γ Δtp+1
@
@ψ (Hψ)
p
"
K i(p + 1)
= Δtp+1Hψjp∗+ Δtp+1
@
@ψ (Hψ)
p∗
X
i□1
m=1
γimK m(p + 1)
"
;
i = 1; . . . ; I
(16.119)
where Hψ|p∗is the evaluation of the left side of Eq. (16.52) at the intermediate
points tp∗where the solution vector is given by
ψ(p∗) = ψ(p) +
X
i□1
m=1
αimK m(p + 1)
(16.120)
where γ, γm, and αim are fixed constants. The scheme is well suited for a variable
time step because it employs an embedded Runge–Kutta–Fehlberg estimate for ψ
(p + 1), which provides the capability to monitor truncation error without
increasing computational time.
