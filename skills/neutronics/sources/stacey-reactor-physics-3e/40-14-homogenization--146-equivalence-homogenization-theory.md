# 14 Homogenization — 14.6 Equivalence Homogenization Theory … Further Readings
<!-- source PDF pages 571-580 -->

<!-- page 553 (PDF 571) -->
Rather large errors have been found in calculations that employed these
conventional homogenization methods when compared with exact solutions
for benchmark problems. The major source of error is in the treatment of the
homogenized diffusion coefficients and the imposition of continuity of flux and
current continuity boundary conditions at interfaces between homogenization
regions. The source of the problem is that the homogenized diffusion equation,
with continuity of current and flux imposed at interfaces, lacks sufficient degrees
of freedom to preserve both surface currents and reaction rates.

## 14.6 Equivalence Homogenization Theory

Itispossiblethatboththevolume-integratedreactionratesandthesurface-integrated
currents from the heterogeneous problem be required to preserve in the homogenized
problem [i.e., that Eqs. (14.52) and (14.53) be satisfied] if the continuity of flux
condition is relaxed. Instead of continuity of flux, the flux interface condition
^ϕ
+
i (xi+1)f +
i (xi+1) = ^ϕ
□
i+1(xi+1)f □
i+1(xi+1)
(14.57)
is imposed at the interface at xi+1 between homogenization regions i and i + 1,
where ϕ+
i (xi+1) and ϕ□
i+1(xi+1) are the homogenized fluxes in homogenization
regions xi ≤ x ≤ xi+1 and xi+1 ≤ x ≤ xi+2, respectively, both evaluated at the interface
xi+1 between the two, as indicated in Fig. 14.6. Similarly, f □
i+1(xi) refers to the
flux discontinuity factor at the lower (minus) interface xi+1 of the region xi+1 ≤
x ≤ xi+2, and f +
i (xi+1) refers to the flux discontinuity factor at the upper (plus)
interface xi+1 of the region xi ≤ x ≤ xi+1. The flux discontinuity factors on each side
of the interface at xi+1 are defined by the ratios of the heterogeneous to
homogeneous fluxes at this interface:
f +
i (xi+1) = ϕ+
i (xi+1)
^ϕ
+
i (xi+1)
;
f □
i+1(xi+1) = ϕ□
i+1(xi+1)
^ϕ
□
i+1(xi+1)
(14.58)
fi
+(xi +1)
fi
–
+1(xi +1)
ϕi
–
+1(xi +1)
xi +2
xi +1
xi
i
i +1
ϕi
+(xi +1)
Fig. 14.6 Equivalence theory
notation.

<!-- page 554 (PDF 572) -->
Equations (14.57) and (14.58) express the requirement that the heterogeneous
flux is continuous at the interface and relate the homogeneous to heterogeneous
fluxes at the interface. The discontinuity factors introduce additional degrees of
freedom into the homogenization procedure, which permits the satisfaction of
Eqs. (14.52) and (14.53).
Let us now consider the implementation of equivalence theory. For the
moment, we continue to assume the existence of an exact heterogeneous
solution for the entire core. The evaluation of homogenized cross sections
from Eq. (14.54) is straightforward. We examine implementation of the
requirement of Eq. (14.53) for the homogenized multigroup diffusion equation
in two dimensions:
□∇?^D
g
ij∇^ϕ
g
ij(x; y) + ^Σ
g
tij^ϕ
g
ij(x; y)
=
X
G
g´=1
^Σ
g´!g
ij
^ϕ
g´
ij (x; y) + χg
k
X
G
g´=1
v^Σ
g´
f ij^ϕ
g´
ij (x; y);
g = 1; . . . ; G
(14.59)
where the homogenized cross sections for homogenization region (i, j) have been
calculated from Eq. (14.54) and both homogenized cross sections and diffusion
coefficients are constant within region (i, j). Integrating this equation over the ydimension
of the homogenization region (i, j), which is defined by xi ≤ x ≤ xt+1 and
yj ≤ y ≤ yj+1, yields
(14.60)
Since the heterogeneous solution is assumed to be known, the heterogeneous ydirection
leakage (Lg
ijy) is known, in principle, and may be used to evaluate the ydirection
leakage term in Eq. (14.60); that is,
^L
g
ijy(x) ≡ □^D
g
ij∫
yj+1
yj
dy d2
dy2 ^ϕ
g
ij(x; y) = Lg
ijy(x)
≡ ∫
yj+1
yi
dy d
dy Jg(x; y) = Jg(x; yj+1) □ Jg(x; yj)
(14.61)
Furthermore, the known values of the heterogeneous currents (Jg) at xi+1 and xi
can be used as boundary conditions for the solution of Eq. (14.60) in the
homogenization region (i, j):
□^D
g
ij
d
dx ∫
yj+1
yj
dy^ϕ
g
ij(xi+1; y) = ∫
yj+1
yj
Jg(xi+1; y)dy
□^D
g
ij
d
dx ∫
yj+1
yj
dy^ϕ
g
ij(xi; y) = ∫
yj+1
yj
Jg(xi; y)dy
(14.62)

<!-- page 555 (PDF 573) -->
With the (assumed) known values of the heterogeneous fluxes at the interfaces
and the calculated values of the homogeneous flux integrals, the discontinuity
factors for region (i, j) at the surfaces at xi+1 and at xi can be calculated as the ratio
of heterogeneous-to-homogeneous flux integrals:
f +
ig = Φg
i (xi+1)
^Φ
g
i (xi+1)
;
f □
ig = Φg
i (xi)
^Φ
g
i (xi)
(14.63)
where
^Φ
g
i (x) ≡ ∫
yj+1
yj
dy^ϕ
g
ij(x; y);
Φg
i (x) = ∫
yj+1
yj
dyϕ(x; y)
(14.64)
The global heterogeneous solution will not be known, of course, so the practical
implementation of the prescriptions above requires their approximation using a
local heterogeneous solution for an assembly or set of assemblies, usually
performed with a zero current boundary condition. It is important that the
same approximate heterogeneous solution be used to evaluate the leakage term of
Eq. (14.61) in Eq. (14.60), to evaluate the boundary conditions of Eq. (14.62) for
Eq. (14.60), and to evaluate the numerators of the flux discontinuity factors. A
similar procedure yields the flux discontinuity factors f +
j and f □
j+1 for region (i, j) at
the surfaces at y = yj and y = yj+1. The four different flux discontinuity factors for
region (i, j) will in general be different.
Note that this procedure can be implemented for any arbitrary definition of the
homogenized diffusion coefficient. The choice of diffusion coefficient will, of
course, affect the solution for the homogeneous flux in the calculation above,
hence affect the value of the computed flux discontinuity factor. A common
choice for the homogenized diffusion coefficient is the simple heterogeneous fluxweighted
value:
^D
g
ij =
∫
xi+1
xi
dx∫
yj+1
yj
dyDg(x; y)ϕg(x; y)
∫
xi+1
xi
dx∫
yj+1
yj
dyϕg(x; y)
(14.65)
The calculation of flux discontinuity factors. can be implemented by using
assembly calculations of both the heterogeneous and homogeneous fluxes and
currents. The volume integral of flux over the assembly can be normalized to be
the same in both calculations. If the homogeneous assembly calculation is carried
out with zero current symmetry boundary conditions, the homogeneous flux
distribution is uniform within the homogenization region. Under these approximations
, the flux discontinuity factor can be calculated entirely from the results of
the heterogeneous assembly calculation as the ratio of the surface integral of the
heterogeneous assembly flux to the volume integral of the heterogeneous flux, as

<!-- page 556 (PDF 574) -->
may be seen by considering
∫
yj+1
yj
dyϕg
A(xi+1; y)
∫
xi+1
xi
dx∫
yj+1
yj
dyϕg
A(x; y)
=
Φg
i+1(xi+1)
∫
xi+1
xi
dx ∫
yj+1
yj
dy ^ϕ
g
ij(x; y)
= Φg
i+1(xi+1)
Δxi ^Φ
g
ij
≡
f +
ig
Δx
(14.66)
where ϕg
A(x; y) is the heterogeneous flux from the assembly calculation, the
common normalization of the heterogeneous and homogeneous fluxes has been
used in the second step, and the uniformity of the homogeneous assembly flux
with symmetry boundary conditions has been used in the third step. The
discontinuity factors calculated from Eq. (14.66), referred to as assembly discontinuity
factors, will be accurate for assemblies in which the net current almost
vanishes over the boundaries, but will be inaccurate for conditions in which there
is significant leakage across assembly interfaces; this is an area of active research.
This formulation of equivalence theory is appropriate for any nodal method
that uses surface-averaged fluxes [e.g., the quantities defined by Eq. (14.64)] in
evaluating node-to-node coupling. The expression for the nodal interface current
on the interface at xi+1 between nodes (i, j) and (i + 1, j) is
J+
g(i;j) =
2Dg
ijDg
i+1j
ΔxiΔxi+1
f +
giΦg
i □ f □
gi+1Φg
i+1
f □
gi+1Dg
ij=Δxi + f +
giDg
i+1j=Δxi+1
(14.67)
Similar expressions obtains for the other nodal interfaces.

## 14.7 Multiscale Expansion Homogenization Theory

A more formal development of homogenization theory builds on the spatial
structure typical of a nuclear reactor, a repeating array of highly heterogeneous
fuel assemblies within an almost periodic (symmetric) configuration with
assembly-averaged properties that vary slowly from assembly to assembly.
This suggests the introduction of two spatial scales – the fine scale of the
intra-assembly heterogeneity (rf) and the coarse scale of the global interassembly
variation (rc) – that are treated as independent spatial variables.
The multiscale homogenization theory will be illustrated with one-group diffusion
theory, the governing equation for which is written with rf and rc as formally
independent spatial variables:
□
@
@rc
+ @
@rf

?D(rc; rf )
@
@rc
+ @
@rf

Φ(rc; rf )
+ Σa(rc; rf )Φ(rc; rf ) □ 1
k vΣf (rc; rf )Φ(rc; rf ) = 0
(14.68)

<!-- page 557 (PDF 575) -->
Normalized to a core average diffusion length, L, the spatial gradients are of
different order: O(Ld/drc) ∼O(Lrf/rcd/drf) ∼εO(Ld/drf), where ε ≡rf/rc is a small
parameter on the order of the ratio of the scale lengths of the intra-assembly
heterogeneity to the assembly dimensions. Making flux and eigenvalue expansions
in powers of the small parameter ε,
Φ(rc; rf ) =
X
n=0
εnΦn(rc; rf );
k =
X
n=0
εn
kn
(14.69)
and substituting in Eq. (14.68) yields to leading order O(ε0):
Lrf Φ(rc; rf ) ≡ □ @
@rf
?D(rc; rf ) @Φ0(rc; rf )
@rf
+ Σa(rc; rf )Φ0(rc; rf )
□ 1
k0
vΣf (rc; rf )Φ0(rc; rf ) = 0
(14.70)
Equation (14.70) plus the periodic (symmetry) boundary conditions on an
assembly defines the detailed heterogeneous intra-assembly flux for an assembly
k; there will be K such heterogeneous assembly problems, corresponding to
the K different fuel assembly types in the reactor core. The dependence on rc
indicated in Eq. (14.70) is a dependence on the assembly for which the
calculation is made; all intra-assembly spatial dependence is represented by
the rf dependence. Since no spatial gradients with respect to rc occur in
Eq. (14.70), the general solution is
Φ0(rc; rf ) = A0(rc)ϕ0(rc; rf )
(14.71)
where A0(rc) is an arbitrary function of the global spatial scale parameter which
will be determined from a higher order equation.
The first-order O(ε1) equation is
Lrf Φ1(rc; rf ) = @
@rc
?D(rc; rf ) @
@rf
ϕ0(rc; rf )A0(rc)
+ @
@rf
?D(rc; rf ) @ϕ0(rc; rf )
@rc
A0(rc)
+ 1
k1
vΣf (rc; rf )ϕ0(rc; rf )A0(rc)
(14.72)
which is an inhomogeneous equation of the same form as the homogeneous
Eq. (14.70). By the Fredholm alternative theorem, Eq. (14.72) has a solution only if
the right side is orthogonal to the solutions of the equation that is adjoint to
Eq. (14.70). Since this equation is self-adjoint for one-group diffusion theory (it is

<!-- page 558 (PDF 576) -->
not for multigroup diffusion theory or transport theory) with periodic boundary
conditions, a solvability condition for Eq. (14.72) is
k1
= hϕ0; vΣf ϕ0iA0 +
ϕ0;
@
@rf
D + D @
@rf

ϕ0

? @A0
@rc
+
ϕ0; @ϕ0
@rf
? @D
@rc
+ D @
@rf
? @ϕ0
@rc

A0
(14.73)
where h□i indicates a spatial integral over rf within node k. Equation (14.73)
provides a calculation for k1. The solution of Eq. (14.72) consists of a solution to
the homogeneous equation, which is ϕ0, with an arbitrary multiplier A1(rc), and
particular solutions corresponding to the terms on the right side:
Φ1(rc; rf ) = A1(rc)ϕ0(rc; rf ) + P
ξ gξ(rc; rf )nξ? @A0(r0)
@rc
+ q(rc; rf )A0(rc)
(14.74)
where the particular solutions satisfy
Lrf gξ(rc; rf ) = nξ?
@
@rf
∇ϕ0(rc; rf ) + D(rc; rf ) @
@rf
ϕ0(rc; rf )

Lrf q(rc; rf )
= 1
k1
vΣf (rc; rf )ϕ0(rc; rf )
(14.75)
with periodic assembly boundary conditions. There is an equation of the form of
the first of Eqs. (14.75) for each coordinate direction.
The second-order O(ε2) equation is
Lrf ϕ2 = @
@rc
?D @
@rc
Φ0 +
@
@rf
?D @
@rc
+ @
@rc
?D @
@rf

Φ1
+ 1
k1
vΣf Φ1 + 1
k2
vΣf Φ0
(14.76)
which has a solvability condition
ϕ0;
k1
vΣf Φ1 + 1
k2
vΣf Φ0

+
ϕ0; @
@rc
?D @
@rc
Φ0

+
ϕ0;
@
@rf
?D @
@rc
+ @
@rc
?D @
@rf

Φ1

= 0
(14.77)

<!-- page 559 (PDF 577) -->
that provides a solution for k2. Integrating Eq. (14.76) over the rf intra-assembly
heterogeneous spatial scale yields the global diffusion equation with parameters
averaged over the fuel assembly:
@
@rc
?hDi @
@rc
A0(rc) + 1
ε2
k hvΣf i □ hΣai

A0(rc)
+ h~Γi? @
@rc
A0(rc) + hSiA0(rc) = 0
(14.78)
where, defining the normalization N ≡hϕ0, ϕ0i, the appropriate assembly-averaged
homogenized nu-fission and absorption cross section are flux-adjoint
weighted with the detailed intra-assembly solutions
hvΣf i = hϕ0; vΣf ϕ0i
N
hΣai
= hϕ0; Σaϕ0i
N
(14.79)
the elements of the diffusion tensor for a two-dimensional problem are
hD11i =
hϕ0; Dϕ0i +
ϕ0; D @
@rf 1
g2 + @
@rf 1
Dg2

N
hD12i =
ϕ0;
@
@rf 1
D + D @
@rf 1

g1

N
hD21i =
ϕ0;
@
@rf 2
D + D @
@rf 2

g2

N
hD22i =
hϕ0; Dϕ0i +
ϕ0;
D @g1
@rf 2
+ @
@rf 2
Dg1

N
hD33i = hϕ0; Dϕ0i
N
hD13i = hD23i = hD31i = hD32i = 0
(14.80)
there is a source that acts like an effective fission or absorption cross section,
hSi =
ϕ0;
@
@rc
?D @
@rf
+ @
@rf
?D @
@rc

q

+ 1
k hϕ0; vΣf qi
□ 1
k hϕ0; vΣf ϕ0i □
@
@rc
ϕ0; D @
@rc
ϕ0

(14.81)

<!-- page 560 (PDF 578) -->
and there is a convection term (defined in Ref. [4]). The source and convection
terms arise because of the assembly-to-assembly variation of cross sections and
diffusion coefficient. These terms, which vanish for a reactor with exactly periodic
conditions associated with each assembly, account for the effect of inter-assembly
leakage between adjacent assemblies, which is not accounted for in the calculation
of ϕ0.
Thus, the solution of Eqs. (14.70) and (14.75), with periodic boundary conditions
, for the detailed intra-assembly flux distribution ϕ0 and supplementary
intranodal functions gξ and q can be used to calculate flux-adjoint-weighted
homogenized assembly parameters for a consistently formulated global diffusion
equation (14.78). This type of multiscale procedure can also be employed to
develop a global diffusion equation based on assembly homogenization with
transport lattice calculations replacing Eq. (14.70).

## 14.8 Flux Detail Reconstruction

The homogenization procedure results in homogenized cross sections that
can be used for an entire fuel assembly or collections of fuel assemblies (e.g.,
modules) in a full core calculation. The resulting flux distribution from the full
core calculation reflects the global flux distribution, but not the local detailed
flux distribution. The detailed assembly or module flux calculations that were
used in the homogenization process must be superimposed on the global flux
distribution, and the detailed pin-cell flux distributions must be further
superimposed on the assembly or module flux distributions. It is important
that the assumptions used in reconstructing the detailed flux distribution be
consistent, if not identical, with the assumptions made in the homogenization
process.

## References

1 A. AMOUYAL, P. BENOIST, and J. HOROWITZ, “New Method of Determining the
Thermal Utilization Factor in a Unit Cell,” J. Nucl. Energy 6, 79 (1957).
2 J. J. DUDERSTADT and L. J. HAMILTON, Nuclear Reactor Analysis, Wiley, New York
(1976), Chap. 10.
3 E. E. LEWIS and W. F. MILLER, Computational Methods of Neutron Transport,
American Nuclear Society, La Grange Park, IL (1993).
4 H. ZHANG, RIZWAN-UDDIN, and J. J. DORNING, “Systematic Homogenization and
Self-Consistent Flux and Pin Power Reconstruction for Nodal Diffusion Methods,
Part I: Diffusion Theory Based Theory,” Nucl. Sci. Eng. 121, 226 (1995);
“Transport-Equation-Based Systematic Homogenization Theory for Nodal
Diffusion Methods with Self-Consistent Flux and Pin Power Reconstruction,”
J. Transport Theory Stat. Phys. 26, 433 (1997); “A Multiple-Scales Systematic
Theory for the Simultaneous Homogenization of Lattice Cells and Fuel
Assemblies,” J. Transport Theory Stat. Phys. 26, 765 (1997).

<!-- page 561 (PDF 579) -->
## Further Readings

ASKEW J. R., FAYERS F. J., and KEMSHELL F. B., “A General Description of the Lattice
Code WIMS,” J. Br. Nucl. Energy Soc. 5, 564 (1966).
CHIANG R. T. and DORNING J.,“A Homogenization Theory for Lattices with Burnup and
Non-uniform Loadings,” Proc. Top. Mtg. Advances in Reactor Physics and Core
Thermal-Hydraulics, American Nuclear Society, La Grange Park, IL (1980), p. 240.
DENIZ V. C., “The Theory of Neutron Leakage in Reactor Calculations,” in Y. RONEN,
ed., CRC Handbook of Nuclear Reactor Calculations II, CRC Press, Boca Raton,
FL (1986), p. 409.
HEBERT A. et al., “A Consistent Technique for the Global Homogenization of a
Pressurized Water Reactor Assembly,” Nucl. Sci. Eng. 109, 360 (1991);
“Development of a Third Generation SPH Method for the Homogenization of a
PWR Assembly,” Proc. Conf. Mathematical Methods and Supercomputing in
Nuclear Applications, Karlsruhe, Germany (1993), p. 558; “A Consistent
Technique for the Pin-by-Pin Homogenization of a Pressurized Water Assembly,”
Nucl. Sci. Eng. 113, 227 (1993).
HENRY A. F., Nuclear-Reactor Analysis, MIT Press, Cambridge, MA (1975), Chap. 10.
JONSSON A., “Control Rods and Burnable Absorber Calculations,” in Y. RONEN, ed.,
CRC Handbook of Nuclear Reactor Calculations III, CRC Press, Boca Raton, FL
(1986).
KAVENOKY A.,“The SPH Homogenization Method,” Proc. Specialist’s Mtg.
Homogenization Methods in Reactor Physics, Lugano, Switzerland, 1978, IAEA-
TECDOC-231, International Atomic Energy Agency, Vienna (1980).
KOEBKE K.,“A New Approach to Homogenization and Group Condensation,” Proc.
Specialist’s Mtg. Homogenization Methods in Reactor Physics, Lugano,
Switzerland, 1978, IAEA-TECDOC-231, International Atomic Energy Agency,
Vienna (1980).
LARSEN E. W., “Neutron Transport and Diffusion in Inhomogeneous Media, I,”
J. Math. Phys. 16, 1421 (1975); “Neutron Transport and Diffusion in
Inhomogeneous Media, II,” Nucl. Sci. Eng. 60, 357 (1976); “Neutron Drift in
Heterogeneous Media,” Nucl. Sci. Eng. 65, 290 (1978).
MAYNARD C. W., “Blackness Theory for Slabs,” in A. RADKOWSKY, ed., Naval Reactors
Physics Handbook, U.S. Atomic Energy Commission, Washington, DC (1964),
pp. 409–448.
SMITH K. S., “Assembly Homogenization Techniques for Light Water Reactor
Analysis,” Prog. Nucl. Energy 14, 303 (1986).
STAMM’LER R. J. J. and ABBATE M. J., Methods of Steady State Reactor Physics in
Nuclear Design, Academic Press, London (1983), Chap. VII.

## Problems

### 14.1

Carry through the detailed derivation of the ABH method.

### 14.2

Consider a two-region slab geometry model of a unit cell consisting of a fuel
plate of thickness a = 1cm with a moderator region of thickness b = 2 cm on

<!-- page 562 (PDF 580) -->
each side, with zero current cell boundary conditions and a uniform slowingdown
source in the moderator. The fuel is UO2, with thermal cross sections
Σa= 0.169cm□1, Σs= 0.372cm□1, and 1□ μ0= 0.9887. The moderator is
H2O, with thermal cross sections Σa= 0.022cm□1, Σs= 3.45cm□1, and
1□ μ0= 0.676. Use the ABH method to calculate the thermal disadvantage
factor, thermal utilization and homogenized scattering, and absorption cross
sections for the cell.

### 14.3

Carry through the detailed derivation of blackness theory.

### 14.4

A reactor assembly consists of repeating arrays of three fuel–moderator
unit cells of the type described in Problem 14.2, then a 0.1-cm-thick boron
plate with thermal cross sections Σa = 25 cm□1, Σs = 0.346 cm□1, and
(1 □ μ0) = 0.9394, and then another three fuel–moderator unit cells. Use
blackness theory to calculate an effective diffusion theory cross section to
represent the boron slabs in the fuel–moderator plus boron plate array.

### 14.5

A reactor fuel assembly consists of five of the fuel–moderator boron
arrays described in Problem 14.4. Use one-group diffusion theory to
calculate the assembly detailed heterogeneous flux distribution. Calculate
the homogenized assembly absorption and scattering cross sections and
diffusion coefficient and the assembly flux discontinuity factors using
equivalence theory.

### 14.6

Construct the Wigner–Seitz cell model for a fuel pin 1 cm in diameter
within a 2-cm square of moderator.

### 14.7

Set up and solve the collision probability equations for Problem 14.6, in onegroup
theory. Use the fuel and moderator parameters given in Problem 14.2.

### 14.8

Calculate the homogenized cross sections for the pin-cell model of
Problem 14.7, using conventional homogenization theory.

### 14.9

Consider a lattice made up of a repeating array of 1-cm-thick fuel plates
separated by 2 cm of H2O, as described in Problem 14.2, but with different
fuel enrichments in different plates. Taking a fuel plate and 1 cm of H2O on
each side as an assembly, use diffusion theory to solve for the assembly
heterogeneous flux, with zero current assembly boundary conditions.
Calculate the homogenized assembly cross sections and diffusion
coefficient and the assembly flux discontinuity factor, using equivalence
homogenized theory.
14.10∗Write a one-dimensional S4 code in slab geometry and repeat Problem 14.9
using an S4 assembly heterogeneous flux.
∗Problem 14.10 is a longer problem suitable for a take-home project.
