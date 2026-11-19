# 15 Nodal and Synthesis Methods — 15.10 Multichannel Spatial Synthesis … Problems
<!-- source PDF pages 632-639 -->

<!-- page 614 (PDF 632) -->
## 15.10 Multichannel Spatial Synthesis

In Section 15.9, the idea of using different trial functions (i.e., different sets of
expansion functions) in different axial regions was discussed. It is also possible to
use different trial functions in different planar regions (channels), a procedure
referred to as multichannel synthesis. This introduces two attractive possibilities.
With expansion functions obtained from two-dimensional (x □ y) calculations
based on a model encompassing the entire cross-sectional area of the reactor, the
multichannel feature provides the additional flexibility of allowing different
expansion coefficients to be used in different channels. Thus, a greater range
of planar flux shapes can be synthesized from a given set of expansion functions
than is possible with the single-channel synthesis of Section 15.9. A second
possibility, which has not been exploited, is the use of expansion functions in each
channel obtained from two-dimensional (x □ y) calculations based on a model
encompassing only the cross-sectional area of the channel.
The basic idea of multichannel synthesis can be illustrated by the simple
example shown in Fig. 15.10. Let the radial dimension of the reactor model
be divided into two channels, 0 ≤ r ≤ a/2 and a/2 ≤ r ≤ a. Then the flux would be
constructed by separately mixing ϕrod and ϕunrod in each channel:
ϕ(r; z) = a1
rod(z)ϕrod(r) + a1
unrod(z)ϕunrod(r);
0 ≤ r ≤ a
ϕ(r; z) = a2
rod(z)ϕrod(r) + a2
unrod(z)ϕunrod(r);
a
2 < r ≤ a
The multichannel synthesis equations are derived by using separate trial
functions for each channel, denoted by a superscript c, of the form
ϕc(x; y; z; t) =
X
N
n=1
ψc
n(x; y)ρc
n(z; t)
(15.160)
jc(x; y; z; t) =
X
N
n=1
f[Jc
nx(x; y)bc
n(z; t) + ψc
n(x; y)Bc
n(z; t)]i
+ [Jc
ny(x; y)gc
n(z; t) + ψc
n(x; y)Gc
n(z; t)]j
+Jc
nz(x; y)dc
n(z; t)kg
(15.161)
with similar expansions for the adjoint flux and current. The x and y components of
the current are each expanded in two separate types of terms in anticipation of the
frequent procedure of using Jnx = □D(@ψn, @x) and so on. The second term,
proportional to ψn, is included both for added flexibility and to ensure the existence
of coupling between channels across an interface located where @ψn/@x may be zero.
Forthe sakeof illustration, the channelstructure willbe takenas concentric annuli,
so that the interface terms J2 are included for each vertical cylindrical surface, Sin, that
separates channels. Because the derivation of initial conditions and interface

<!-- page 615 (PDF 633) -->
conditions for axial and temporal trial function discontinuities, and the inclusion of
external boundary terms, are identical to the derivation given in the preceding
section,theywillbeomitted.Thus,themultichannelsynthesisequationsareobtained
from consideration of the stationarity properties of J12= J1 + J2, with J2 consisting of
the terms discussed above. These equations may be written in matrix form as
Mcρc + Tc _ρc + Λc
xbc + Λc
x+bc+1 □ Λc
x□bc□1 + Γc
xBc + Γc
x+Bc+1
□ Γc
x□Bc□1 + Λc
ygc + Λc
y+gc+1 □ Λc
y□gc□1 + Γc
yG + Γc
y+Gc+1
□ Γc
y□Gc□1 + Ac @dc
@z □
X
M
m=1
βmFc
mCc
m □ Sc = 0
(15.162)
δJ12
δ(bc∗
n´)T = 0
)
c
xbc + Lc
xBc + K c
xρc + K c
x+ρc+1 □ K c
x□ρc□1 = 0
(15.163)
δJ12
δ(gc∗
n´)T = 0
)
c
ygc + Lc
yGc + K c
yρc + K c
y+ρc+1 □ K c
y□ρc□1 = 0
(15.164)
δJ12
δ(Bc∗
n´)T = 0
)
hc
xbc + Hc
xBc + W c
xρc + W c
x+ρc+1 □ W c
x□ρc□1 = 0
(15.165)
δJ12
δ(Gc∗
n´)T = 0
)
hc
ygc + Hc
yGc + W c
yρc + W c
y+ρc+1 □ W c
y□ρc□1 = 0
(15.166)
δJ12
δ(dc∗
n´)T = 0
)
Ucdc + V c @ρc
@z = 0
(15.167)
The matrices and column matrices in Eqs. (15.162)–(15.167) are of order NG × G
and NG × 1, respectively, except for Fc
m and Cc
m, which are NG × N and N × 1,
respectively.
Equations (15.162)–(15.167) may be combined to eliminate the current
expansion coefficients, resulting in the set of one-dimensional (z) time-dependent
matrix differential equations
Mcρc + Tc _ρc + Rcρc + Rc
+ρc+1 + Rc
++ρc+2 + Rc
□ρc□1 + Rc
□□ρc□2
□ Ac @
@z (Uc)□1V c @ρc
@z

□
X
M
m=1
βmFc
mCc
m □ Sc = 0
c = 1; . . . ; number of channels
(15.168)

<!-- page 616 (PDF 634) -->
The matrices R+ and R++ in Eqs. (15.168) result from elimination of the currentcombining
coefficients and serve to couple channel c radially to channels c + 1
and c + 2, and similarly, R□ and R□ □ couple channel c to channels c □ 1 and c □ 2.
This general feature of nearest-neighbor and next-nearest-neighbor coupling is
characteristic of the multichannel formulation, independent of the particular
choice of channel structure.
Construction of the radial coupling matrices involves the evaluation of surface
integrals containing normal derivative terms and considerable matrix inversion
and matrix multiplication. The results are sensitive to the accuracy and consistency
with which the surface integrals are evaluated, a fact that has hindered
exploitation of the multichannel formalism. Moreover, the transport cross section
is embedded in the matrices that lead to R+ and so on, and a change in this
quantity requires that the matrix inversions and multiplications involved in the
construction of R+ and so on be repeated. These factors tend to mitigate the
advantages of extra flexibility and increased accuracy inherent in the multichannel
formulation. See Refs. [2] and [3] for a more detailed description.

## 15.11 Spectral Synthesis

In previous sections the emphasis has been on synthesizing the spatial dependence
of the neutron flux, and the approximations that were discussed have, in fact, found
their greatest application in problems where it was important, but uneconomical, to
represent the detailed spatial variation of the flux. Another class of problems exists
wherein it is important, but uneconomical, to represent the spectral variation of the
flux in great detail. For such problems an attempt to synthesize the detailed
spectrum from a few spectral functions is appealing. The general basis of the
method is a trial function expansion in each spatial region, or channel c, of the form
ϕc(x; y; z; t) =
X
N
n=1
ψc
nρc
n(x; y; z; t)
(15.169)
jc(x; y; z; t) =
X
N
n=1
Jc
nbc
n(x; y; z; t)
(15.170)
with similar expansions for the adjoint flux and current. Here ψn and Jn are known
G × 1 column matrices, and a single expansion coefficient ρn applies to all the G
group components of the corresponding expansion function ψn. Because the
objective of the method is to approximate the spectral dependence, it is not
necessary to make an expansion of the precursor trial function.
Requiring stationarity of the variational principle with respect to the adjoint
expansion coefficients yields the spectral synthesis equations within each channel c:
δJ1
δ(ρc∗
n´) = 0;
n´ = 1; . . . ; N
(15.171)

<!-- page 617 (PDF 635) -->
δJ1
δ(bc∗
n´) = 0;
n´ = 1; . . . ; N
(15.172)
These two sets of N equations may be written as two matrix equations, and
combined to eliminate the current combining coefficients,
Mcρc □ Λc∇⋅(ℓc)□1K c∇ρc + Tc _ρc □
X
M
m=1
βmFc
mCm □ Sc = 0
(15.173)
Mc, Λc,
c, Kc, and Tc are N × N matrices, while ρc, Fc
m, and Sc are N × 1 column
matrices.
For each spatial interface between channels a term of the form of J2 must be
added to the variational principle. The variation of such a term leads to
X
N
n´=1
X
N
n=1
n⋅f[γδρ∗
n´+ψ∗T
n´+ + (1 □ γ)δρ∗
n´□ψ∗T
n´□](Jn+bn+ □ J n□bn□)
+ [ηδb∗
n´+J ∗T
n´+ + (1 □ η)δb∗T
n´□J ∗T
n´□](ψn+ρn+ □ ψn□ρn□) = 0
(15.174)
As was the case with the spatial synthesis, it is necessary to impose some form of
restriction among the allowable variations δρ∗
n+ and δρ∗
n□, and δb∗
n+ and δb∗
n□, or to
resort to some stratagem such as staggering the interfaces at which flux and
current may be discontinuous or to set γ, η = 1, 0; otherwise, the interface
conditions appear to be overdetermined. A restriction among the variations
arises naturally from the requirement that variations δϕ∗
+ and δϕ∗
□ be equal to
ensure continuity, and similarly, that δj∗
+ = δj∗
□. This requirement must be
imposed in an approximate manner (unless N = G, in which case there is no
advantage whatsoever to using spectral synthesis), and leads to
δρ∗
n+ =
X
N
n´=1
Qnn´δρ∗
n´□;
δb∗
n+ ? n =
X
N
n´=1
Pnn´δb∗
n□ ? n
Using these relations to eliminate δρ∗
n+ and δb∗
n+, Eq. (15.174) can then be
required to be satisfied for arbitrary and independent variations δρ∗
n□ and
δb∗
n□, which yields the proper number of interface conditions.
The other strategies that have been suggested may be considered as special
cases with γ, n = 0, 1 and/or Pnn´ = Qnn´ = δnn´. Thus, in general, the spatial
interface conditions may be written in the form
X
N
n=l
n ⋅f[AT
n´J n+]bn+ □ [AT
n´Jn□]bn□g = 0;
n´ = 1; . . . ; N
(15.175)

<!-- page 618 (PDF 636) -->
X
N
n=1
f[BT
n´ψn+]ρn+ □ [BT
n´ψn□]ρn□g = 0;
n´ = 1; . . . ; N
(15.176)
Note that unless
[AT
n´J n+] = [AT
n´J n□];
n´ = 1; . . . ; N
(15.177)
[BT
n´ψn+] = [BT
n´ψn□];
n´ = 1; . . . ; N
(15.178)
Equations (15.175) and (15.176) do not reduce to continuity requirements of the
form
n ? (bn+ □ bn□) = 0
ρn+ □ ρn = 0
The conventional few-group approximation is a special case of the spectral
synthesis approximation in which an expansion function ψn or Jn has nonzero
elements only for those groups that are to be collapsed into few-group n. Thus,
the result above indicates that continuity of few-group flux and normal current is
generally not the proper interface condition, obtaining only under the special
circumstances whereby Eqs. (15.177) and (15.178) are satisfied.
If different sets of spectral expansion functions are used in different time
intervals, it is necessary to include terms of the form J3, the stationarity of which
yield temporal continuity conditions on the flux expansion coefficients at the time
when the expansion functions are changed. To avoid an apparent overdetermination
of continuity conditions, it is necessary either to resort to some stratagem
such as requiring that the adjoint and direct flux expansion functions change at
different times or setting a = 0, 1, or to impose in an approximate fashion the
continuity condition δϕ∗(+) = δϕ∗(□) to relate δρ∗
n(+) and δρ∗
n(□).
The continuity conditions resulting from this or other derivations can be
written in the form
X
N
n=1
f[DT
n´ψn(+)]ρn(+) □ [DT
n´ψn(□)]ρn(□)g;
n´ = 1; . . . ; N
(15.179)
where Dn is an N × 1 column matrix. Thus, in general, ρn(+) = ρn(□) is not the
continuity condition. Consequently, recalling that a few-group approximation is a
special case of the spectral synthesis approximation, continuity of few-group
fluxes at times when the expansion functions (within-group fine-group fluxes)
changes is generally not the proper continuity condition and obtains only when
DT
n´ψn(+) = DT
n´ψn(□);
n´ = 1; . . . ; N

<!-- page 619 (PDF 637) -->
The synthesis approximations lack, in general, the positivity properties associated
with the multigroup diffusion equations. A consequence of this is that there
is no a priori assurance that the fundamental eigenvalue (the one associated with
an everywhere nonnegative flux solution) is larger in absolute value than any of
the harmonic eigenvalues. Most numerical iteration schemes used in the solution
of the synthesis equations converge to the eigenvalue, and corresponding
eigenfunction, with the largest magnitude, but it is possible that a calculation
will not converge to the fundamental solution.

## References

1 T. M. SUTTON and B. N. AVILES, “Diffusion Theory Methods for Spatial Kinetics
Calculations,” Prog. Nucl. Energy 30, 119 (1996).
2 W. M. STACEY, “Flux Synthesis Methods in Reactor Physics,” Reactor Technol. 15,
210 (1972); “Variational Flux Synthesis Methods for Multigroup Neutron
Diffusion Theory,” Nucl. Sci. Eng. 47, 449 (1972); “Variational Flux Synthesis
Approximations,” Proc. IAEA Semin. Numerical Reactor Calculations,
International Atomic Energy Agency, Vienna (1972), p. 561; Variational Methods
in Nuclear Reactor Physics, Academic Press, New York (1974), Chap. 4.
3 E. L. WACHSPRESS ET AL. , “Multichannel Flux Synthesis,” Nucl. Sci. Eng. 12 381
(1962); “Variational Synthesis with Discontinuous Trial Functions,” Proc. Conf.
Applications of Computational Methods to Reactor Problems, USAEC report
ANL-7050, Argonne National Laboratory, Argonne, IL (1965), p. 191;
“Variational Multichannel Synthesis with Discontinuous Trial Functions,”
USAEC report KAPL-3095, Knolls Atomic Power Laboratory, Schenectady, NY
(1965).

## Further Readings

ACKROYD R. T. et al., “Foundations of Finite Element Applications to Neutron
Transport,” Prog. Nucl. Energy 29 43 (1995); “Some Recent Developments in
Finite Element Methods for Neutron Transport,” Adv. Nucl. Sci. Technol. 19, 381
(1987).
DORNING J. J.,“Modern Coarse-Mesh Methods: A Development of the 70’s,” Proc.
Conf. Computational Methods in Nuclear Engineering, Williamsburg, VA,
American Nuclear Society, La Grange Park, IL (1979), p. 3-1.
FAVORITE J. A. and STACEY W. M., “A Variational Synthesis Nodal Discrete-Ordinates
Method,” Nucl. Sci. Eng. 132, 181 (1999).
FROEHLICH R.,“A Theoretical Foundation for Coarse Mesh Variational Techniques,”
Proc. Int. Conf. Research on Reactor Utilization and Reactor Computation,
Mexico, D. F., CNM-R-2 (1967), p. 219.
GUPTA N. K., “Nodal Methods for Three-Dimensional Simulators,” Prog. Nucl.
Energy 7, 127 (1981).
HENRY A. F., Nuclear-Reactor Analysis, MIT Press, Cambridge, MA (1975), Chap.
11; “Refinements in Accuracy of Coarse-Mesh Finite-Difference Solutions of the

<!-- page 620 (PDF 638) -->
Group-Diffusion Equations,” Proc. Semin. Numerical Reactor Calculations,
International Atomic Energy Agency, Vienna (1972), p. 447.
KAPLAN S., “Synthesis Methods in Reactor Analysis,” Adv. Nucl. Sci. Technol. 3 (1966);
Kaplan, 1966 “Some New Methods of Flux Synthesis,” Nucl. Sci. Eng. 13, 22 (1962).
LAWRENCE R. D., “Progress in Nodal Methods for the Solution of the Neutron
Diffusion and Transport Equations,” Prog. Nucl. Energy 17, 271 (1986); “Three-
Dimensional Nodal Diffusion and Transport Methods for the Analysis of Fast-
Reactor Critical Experiments,” Prog. Nucl. Energy 18, 101 (1986).
STAMM’LER J. J. and ABBATE M. J., Methods of Steady-State Reactor Physics in Nuclear
Design, Academic Press, London (1983), Chap. XI.
WAGNER M. R.,“Current Trends in Multidimensional Static Reactor Calculations,”
Proc. Conf. Computational Methods in Nuclear Engineering, Charleston, SC,
CONF-750413, American Nuclear Society, La Grange Park, IL (1975), p. I-1.

## Problems

### 15.1

Derive the nodal fission rate balance equations of Eq. (15.17) from the
nodal flux balance equations of Eq. (15.16).

### 15.2

Use the rational approximation for the escape probability to calculate the
coupling terms Wn, n+1 for cubic nodes.

### 15.3

Consider a slab reactor consisting of two core regions each 50 cm thick
described by the parameters given for core 1 and core 2 in Table 15.1, with
zero flux conditions on both external boundaries. Solve for the exact
solution in two-group diffusion theory.

### 15.4

Construct a two-node conventional nodal model for the slab reactor of
Problem 15.1. Solve for the multiplication constant and compare with the
exact result of Problem 15.3.

### 15.5

Derive the transverse integrated nodal diffusion equations given by
Eq. (15.31) and similar equations in the y- and z-directions.
Table 15.1 Group Constants
Group
Core 1
Core 2
Constant
Group 1
Group 2
Group 1
Group 2
χ
1.0
0.0
1.0
0.0
νΣf (cm□1)
0.0085
0.1851
0.006
0.150
Σa (cm□1)
0.0121
0.121
0.010
0.100
Σ1!2
s
(cm□1)
0.0241
–
0.016
–
D (cm)
1.267
0.354
1.280
0.400

<!-- page 621 (PDF 639) -->
### 15.6

Construct a two-node transverse integrated model for the slab reactor of
Problem 15.3. Solve for the multiplication constant and compare with the
exact result.

### 15.7

Derive the elements of the matrices Pn
g and Rn
g in the interface current
balance of Eq. (15.58) for nodal diffusion theory.

### 15.8

Derive the nodal balance Eqs. (15.44) directly by integrating the transport
Eq. (15.1) for each group over the node.

### 15.9

Derive the elements of the matrices Pn
g and Rn
g in the interface current
balance of Eq. (15.86) for nodal GP1 transport theory.
15.10 Construct a two-coarse-mesh finite-element model for the slab reactor of
Problem 15.3. Solve for the multiplication constant and compare with the
exact result.
15.11 Prove that the two forms of the variational functional Fd of Eq. (15.107) are
equivalent in that the stationarity of both forms with respect to arbitrary
and independent variations requires that the diffusion equation is satisfied
within the volumes Vi and that the diffusion theory current is continuous
across the surfaces separating adjacent volumes.
15.12 Derive a finite-element coarse-mesh approximation, based on a quadratic
polynomial expansion, for the one-dimensional one-group diffusion equation.
15.13 Carry through the derivation to prove that stationarity of the variational
functional of Eq. (15.143) with respect to arbitrary and independent
variations in ϕ∗, j∗, and C∗
m requires that the stationary functions ϕ, j,
and Cm satisfy the time-dependent transport equation, Fick’s law relation,
and precursor balance equation.
15.14 Derive the time-dependent equations for ϕ∗, j∗, and C∗
m by requiring
stationarity of the variational function of Eq. (15.143) with respect to
arbitrary and independent variations in ϕ, j, and Cm.
15.15 Construct a single-channel synthesis model for the slab reactor of Problem
15.3, but in one-group diffusion theory. Obtain the one-group constants by
using the two-group constants of Problem 15.3 in an infinite-medium
spectrum calculation for ϕ1 and ϕ2, which can be used to construct
effective one-group cross sections. Using the trial function ϕ(x) = a cos
(πx/100) for the flux and adjoint flux, calculate the multiplication constant
and compare with the exact result of Problem 15.3.
15.16 Repeat Problem 15.15 using a two-channel synthesis model.
