# 3 Neutron Diffusion and Transport Theory — 3.7 Reflected Reactor … 3.10 Numerical Solution of Diffusion Equation
<!-- source PDF pages 86-105 -->

<!-- page 62 (PDF 86) -->
is V ≈ 161.11/B3
m. For a right circular cylinder, the minimum critical volume bare
reactor occurs for a diameter d = 21/2 × 2.405H/π ≈ 1.08H and is V ≈ 148:31=B3
m.
The minimum critical volume for a spherical bare reactor is 129:88=B3
m.
It is generally desirable for the neutron flux to be distributed as uniformly as
possible over the reactor core. A measure of nonuniformity is the peak-to-volume
average value. For a homogeneous bare core, the peak value occurs at the center,
and the peak-to-volume average is (π/2)3 = 3.88 for a rectangular parallelepiped,
−2.405πν1/4J1(ν1) = 3.65 for a right circular cylinder, and π2/3 = 3.29 for a sphere.

### Example 3.3 Critical Size of a Bare Cylindrical Reactor

Although the above
formalism has been developed for a one-speed description of neutron diffusion, it
can be generalized to energy-dependent diffusion by using cross sections that are
averaged over the neutron energy distribution. A typical composition and set of
spectrum-averaged crosssectionsforaPWRaregiveninTable3.4.Fromthetablea
number of important materials parameters can be determined: D =
3Σtr = 9:21 cm,
L2= D/Σa = 60.1 cm2,B2
m = νΣf − Σa
=D = 4.13× 10−4 cm−2,k1 = νΣf/Σa = 1.025,
and λextrap = 19.6cm. The criticality condition is B2
m = B2
g = (π=Hex)2 + (2.405/Rex)2.
Fixing the height at 370 cm, the criticality condition requires that Rex = 127.6cm or
R = 108 cm.

## 3.7 Reflected Reactor

Since the dimensions of a critical core of a given composition depend on the
fraction of the neutrons that leak out, these dimensions can be reduced if some of
the leaking neutrons are reflected back into the core. A reflector has the added
benefit of making the neutron flux distribution in the core more uniform by
increasing the neutron population in the outer region due to reflected neutrons
Table 3.4 Typical PWR Core Composition and Spectrum-Averaged Cross Sections
Isotope
n (1024 cm −3)
σtr
(10 −24
cm2)
σa
(10 −24
cm2)
σf
(10 −24
cm2)
ν
Σtr (cm −1)
Σa (cm −1)
νΣf (cm −1)
H
2.748 × 10−2
0.650
0.294
1.79 × 10−2 8.08 × 10−3 0
O
2.757 × 10−2
0.260
1.78 × 10−4 0
7.16 × 10−3 4.90 × 10−6 0
Zr
3.694 × 10−3
0.787
0.190
2.91 × 10−3 7.01 × 10−4 0
Fe
1.710 × 10−3
0.554
2.33
9.46 × 10−4 3.99 × 10−3 0
235U
1.909 × 10−4
1.62
484.0
312.0
2.43 3.08 × 10−4 9.24 × 10−2 0.145
238U
6.592 × 10−3
1.06
2.11
0.638
2.84 6.93 × 10−3 1.39 × 10−2 1.20 × 10−2
10B
1.001 × 10−5
0.877
3.41 × 103
8.77 × 10−6 3.41 × 10−2 0
Sum
3.62 × 10−2 0.1532
0.1570
Source: Data from Ref. [2]; used with permission of Wiley.

<!-- page 63 (PDF 87) -->
that otherwise would have escaped. Figure 3.3 illustrates the neutron flux
distributions in bare and reflected cores of the same composition and dimension.

### Reflected Slab Reactor

The mathematical treatment of a reflected reactor can be illustrated most simply
by considering a slab core of thickness a extending from x = −a/2 to x = +a/2
reflected on both sides by a nonmultiplying slab of thickness b. If we were to solve
the time-dependent equations in both the core and reflector as we did for the bare
core, but now also requiring that the solutions satisfied continuity of flux and
current conditions at x = +a/2, we would find a similar but more complicated
result as before – that the solution consists of a sum of spatial eigenfunctions
corresponding to discrete geometrical eigenvalues, and at long times the dominant
component is the fundamental mode. Rather than carry through the entire
calculation, we examine the fundamental mode that obtains at long times.
The neutron diffusion equations in the core and reflector are
Core :
−DC
d2ϕC
dx2 + (ΣaC − vΣf C)ϕC = 0
Reflector : −DR
d2ϕR
dx2 + ΣaRϕR = 0
(3.81)
The appropriate interface and boundary conditions are symmetry at x = 0,
continuity of flux and current at x = a/2, and zero flux at the extrapolated
boundary a/2 + bex:
dϕC
dx

x=0
= 0
(3.82a)
ϕC
a
= ϕR
a
(3.82b)
REFLECTOR
REFLECTOR
SLOW-NEUTRON FLUX
WITHOUT REFLECTOR
SLOW-NEUTRON FLUX
WITH REFLECTOR
DISTANCE FROM CENTER (cm)
-48
-36
-24
-12
REACTOR
Fig. 3.3 Thermal neutron flux in a spherical 235U water-moderated reactor with and without
a beryllium oxide reflector. (With permission from Ref. [3]. Copyright 1958, University of
Chicago Press.)

<!-- page 64 (PDF 88) -->
JC
a
= JR
a
(3.82c)
ϕR
a
2 + bex
= 0
(3.82d)
The solution in the core satisfying the symmetry boundary condition Eq. (3.82a)
is
ϕC(x) = AC cos BmCx
(3.83)
and the solution in the reflector satisfying the extrapolated boundary condition
Eq. (3.82d) is
ϕR = AR sinh (a=2) + bex − x
LR
(3.84)
where B2
mC = (νΣfC − ΣaC)/DC and L2
R = DR=ΣaR. Using these general solutions in
the interface conditions of Eqs. (3.82b) and (3.82c), dividing the two equations,
and rearranging leads to the criticality condition that must be satisfied in order for
a steady-state solution to exist:
BmCa
tan BmCa
=
DRa
2DCLR
coth bex
LR
(3.85)
The smallest value of a for which a solution of this equation exists is less than
π/BmC, as can be seen by plotting both sides of Eq. (3.85), in Fig. 3.4. Since the
criticality condition for the bare slab was BmC = π/aex, this result confirms that the
addition of a reflector reduces the dimension necessary for criticality.
RHS
LHS
π
3π
Bc a
Fig. 3.4 Plot of criticality equation for reflected reactor. (With permission from Ref. [1].
Copyright 1960, McGraw-Hill.)

<!-- page 65 (PDF 89) -->
### Reflector Savings

The difference in the reflected and unreflected critical dimensions is known as the
reflector savings, δ:
δ ≡ a(bare) − a(reflected) =
BmC
tan−1 DCBmC
DR
LRtanh bex
LR

(3.86)
In the limit of a reflector that is thick in comparison to the neutron diffusion
length (b ≫LR), this reduces to δ ≈ DCLR/DR.

### Reflected Spherical, Cylindrical, and Rectangular Parallelepiped Cores

A similar calculation can be performed for other core geometries, but with
reflection in only one direction. The resulting criticality conditions are given in
Table 3.5.

## 3.8 Homogenization of a Heterogeneous Fuel–Moderator Assembly

In our previous treatment of a homogeneous core, we have implicitly assumed
that the actual core – consisting of thousands of fuel and control elements,
coolant, and structure (Fig. 3.5) – can be represented by some effective homogeneous
mixture.

### Spatial Self-Shielding and Thermal Disadvantage Factor

We might be tempted to construct this homogeneous mixture by simply volumeweighting
the number densities of the various fuel, control, moderator, coolant, and
structuralmaterials,butthisprocedure wouldfailtotakeintoaccount thereduction
of the neutron population in the region of strong absorbers, a phenomenon known
as spatial self-shielding. We illustrate this phenomenon by considering the thermal
neutron flux distribution in a large fuel–moderator assembly consisting of a
repeating array of slab fuel elements of width 2a interspersed with moderating
regions of thickness 2(b − a). Since the moderator is much more effective than the
fuel at slowing-down neutrons, we specify a uniform source SM of thermal neutrons
in the moderator and no thermal neutron source in the fuel. We take as a
calculational model one-half of the slab fuel element, extending from x = 0 to
x = a, and one-half of the moderating region, extending from x = a to x = b. The
neutron diffusion equations in the fuel and moderator are
Fuel :
−DF
d2ϕF(x)
dx2
+ ΣaFϕF(x) = 0
Moderator : −DM
d2ϕM(x)
dx2
+ ΣaMϕM(x) = SM
(3.87)

<!-- page 66 (PDF 90) -->
The appropriate boundary conditions are symmetry at the fuel and moderator
midplanes at x = 0 and x = b, respectively. The other two conditions that must be
satisfied are continuity of flux and current at the fuel–moderator interface at
x = a:
dϕF(0)
dx
= 0
(3.88a)
Table 3.5 Criticality Condition for Reflected Reactors
Geometry
Sphere
R0
R1
Dc(BR0cotBR0 − 1) = −DR
R0
LR
coth(R1ex − R0
LR
) + 1

B2 = (vΣf − Σa)
D
Cylinder: sidereflected

2h
ρ0
ρ1
DcJ´0(κcρ0)
J0(κcρ0)
= DRL´0(ρ0)
L0(ρ0)
L0(ρ) = I0(κRρ1ex)K 0(κRρ) − I0(κRρ)K0(κRρ1ex)
B2
mC = κ2
c +
π
2hex

κ2
R = 1
L2
R
+
π
2hex

; κ2
c = vΣf − Σa
D
−
π
2hex

Cylinder: endreflected

2a
2h
ρ1
Dcμctanμch = DRcothμR(aex − h)
μ2
R = 1
L2
R +
v1
ρ1ex

; B2
mC = μ2
C +
v1
ρ1ex

v1 = 2:405
μ2
c =
vΣf − Σn
D

−
v1
ρ1ex

Block: endreflected

2d
2c
2b
2a
DCκ1tanκ1a = DRμ1cothμ1(dex − a)
μ2
1 = 1
L2
R
+
π
2bex

+
π
2cex

B2
mC = κ2
1 +
π
2bex

+
π
2cex

κ2
1 = vΣf − Σa
D
−
π
2bex

−
π
2cex

<!-- page 67 (PDF 91) -->
dϕM(b)
dx
= 0
(3.88b)
ϕF(a) = ϕM(a)
(3.88c)
DF
dϕF(a)
dx
= DM
dϕM(a)
dx
(3.88d)
Fig. 3.5 Heterogeneous nuclear reactor fuel assemblies. (With permission from Ref. [2].
Copyright 1976, Wiley.)

<!-- page 68 (PDF 92) -->
The solutions to Eqs. (3.87) that satisfy the conditions of Eqs. (3.88) are
ϕF(x) =
SM cosh(x=LF)
f(LF=DF)coth(a=LF) + (LM=DM)coth[(b − a)=LM]g(DF=LF)ΣaMsinh(a=LF)
ϕM(x) = SM
ΣaM
1 −
cosh[(b − x)=LM]
f(LF=DF)coth(a=LF) + (LM=DM)coth[(b − a)=LM]g(DM=LM)sinh[(b − a)=LM]

(3.89)
The thermal flux disadvantage factor is defined as the ratio of the average flux
in the moderator to the average flux in the fuel:
ζ ≡ ϕM
ϕF
=
a∫
b
a
ϕM(x)dx
(b − a)∫
a
ϕF(x)dx
= V FΣaF
V MΣaM
V MΣaM
V FΣaF
F + E − 1

(3.90)
where VF = a, VM = b − a, and
F = a
LF
coth a
LF
;
E = b − a
LM
coth b − a
LM

(3.91)
for slab geometry.
Thermal flux disadvantage factors for repeating arrays formed by other simple
geometries can be calculated in the same manner and represented by the
second form of Eq. (3.90). The results for the lattice functions E and F in other
geometries are given in Table 3.6. The volumes are V F = πρ2
Fh and 4=3πr3
f and
V M = π ρ2
M − ρ2
F
h, for the cylinder and sphere, respectively.

### Effective Homogeneous Cross Sections

An effective homogeneous fuel cross section averaged over the fuel–moderator
lattice can be constructed by using the thermal disadvantage factor of Eq. (3.90) in
the definition
Σeff
aF ≡
ΣaFϕFV F
ϕFV F + ϕMV M
=
ΣaV F
V F + V M
V F + V M
V F + ζV M
= Σhom
aF
1 + V M=V F
1 + ζV M=V F

(3.92)
An effective homogeneous absorption cross section for the moderator can
obviously be constructed by exchanging the F and M subscripts and replacing ζ by
ζ−1. These fuel and moderator effective cross sections can then be combined
(Σeff
a = Σeff
aF + Σeff
aM) to obtain an effective homogeneous cross section for the fuel–
moderator assembly to be used in one of the previous homogeneous core
calculations. Effective homogeneous scattering and transport cross sections
can be constructed in a similar manner.

<!-- page 69 (PDF 93) -->
### Example 3.4 Flux Disadvantage Factor and Effective Homogenized Cross Section in a Slab Lattice

Consider a lattice consisting of a large number of
1-cm-thick slab fuel plates separated by 1 cm of water at room temperature.
The fuel is 10% enriched uranium. The fuel and water number densities
are n235 = 0.004 78 × 1024 cm−3, n238 = 0.0430 × 1024 cm−3, and nH2O = 0.0334
× 1024 cm−3. Using the spectrum-averaged cross sections of Table 3.4 (and constructing
effective H2O σ values as two times the H σ values plus the O σ) yields the
following material properties for the uranium fuel: Σtr = 0.0534 cm−1, Σa = 3.220
cm−1, D = 6.17 cm, and L = 1.38 cm, and for water: Σtr = 0.0521 cm−1, Σa = 0.0196
cm−1, D = 6.40 cm, and L = 18.06 cm. The geometric parameters in Eqs. (3.90) and
(3.91) are VF = VM = a = b − a = 0.5 cm.
Evaluating Eq. (3.90) yields ζ = 1.04 for the thermal disadvantage factor. The
effective homogenized fuel absorption and transport cross sections calculated
from Eq. (3.92) are Σeff
aF = 1.575 cm−1 and Σeff
trF = 0.0264 cm−1. A simple homogenization
(implicitly assuming that ζ = 1) yields Σhom
aF
= 1.610 cm−1 and Σhom
trF =
0.0267 cm−1, so the effect of the spatial self-shielding (ζ) is significant.
Table 3.6 Functions E and F for Various Cell Geometries
Geometry
E and F Functions
Slab
a
b
C
F = a
LF
coth a
LF
E = b − a
LM
coth b − a
LM
Cylindrical
ρM
ρF
F = (ρF=LF)I0(ρF=LF)
2I1(ρF=LF)
E = (1=LM)(ρ2
M − ρ2
F)
2ρF
I0(ρF=LM)K1(ρM=LM) + K 0(ρF=LM)I1(ρM=LM)
I1(ρM=LM)K1(ρF=LM) − K 1(ρM=LM)I1(ρF=LM)

Spherical
rM
rF
F =
rF=LF
)2tanh(rL=LF)
3[(rF=LF) − tanh(rF=LF)]
E = r3
M − r3
F
3rFL3
M
1 − (rM=LM)coth[(rM − rF)=LM]
1 − rMrF=L2
M − [(rM − rF)=LM]coth[(rM − rF)=LM]
Source: Adapted from Ref. [1]: used with permission of McGraw-Hill.

<!-- page 70 (PDF 94) -->
The effective homogenized cross section for the water (moderator) is derived
by a procedure similar to that in Eq. (3.92) and results in an expression similar to
Eq. (3.92) but with the M and F subscripts interchanged and ζ replaced by ζ−1.
The effective homogenized water absorption and transport cross sections are
Σeff
aM = 0.010 cm−1 and Σeff
trM = 0.0266 cm−1, so that the total effective absorption
and transport cross sections for the lattice are Σeff
a = Σeff
aF + Σeff
aM = 1.575 + 0.010 =
1.585 cm−1 and Σeff
tr = Σeff
trF + Σeff
trM = 0.0264 + 0.0266 = 0.053 cm−1.
Note that diffusion theory is not really suitable for calculating the diffusion of
neutrons in such a lattice because λtr = 1/Σtr≫0.5cm, the dimension of the diffusing
medium, in both the fuel and the water, and that this example serves more to illustrate
the application of the methodology than to provide accurate quantitative results. The
transport methods introduced in Section 3.12 and described more fully in Chapter 9
must be used to calculate flux disadvantage factors, in general.

### Thermal Utilization

Another use of the thermal disadvantage factor is to calculate the thermal
utilization for the fuel–moderator lattice:
f het ≡
ΣaFϕFV F
ΣaFϕFV F + ΣaMϕMV M
=
ΣaFV F
ΣaFV F + ΣaMV M
ΣaFV F + ΣaMV M
ΣaFV F + ζΣaMV M
= f hom
ΣaFV F + ΣaMV M
ΣaFV F + ζΣaMV M
(3.93)
In both Eqs. (3.92) and (3.93), the first term is the result that would be obtained
with simple volume-weighted homogenization of the fuel and moderator number
densities, and the second term is a correction that accounts for the flux selfshielding
in the fuel.

### Measurement of Thermal Utilization

In a finite fuel–moderator assembly with geometry characterized by the geometric
buckling Bg and neutrons becoming thermal at a rate qM (per second per cubic
centimeter) in the moderator, the thermal neutron balance is
qMV M = (ΣaMϕMV M + ΣaFϕFV F) 1 + L2B2
g
(3.94)
and the thermal utilization is just the fraction of those thermal neutrons that are
absorbed by the fuel:
f =
ΣaFϕFV F
ΣaFϕFV F + ΣaMϕMV M
(3.95)
The ratio of the slowing-down source to the thermal flux at some point in the
moderator qM/ϕM(x) can be determined by irradiating an indium foil (indium
has an absorption resonance just above thermal) at that point and then
measuring the total foil activation Atot. Then another indium foil clad in a

<!-- page 71 (PDF 95) -->
cadmium jacket, which will absorb all the thermal neutrons before they can
reach the foil but will pass the epithermal neutrons, is irradiated at the same
location to determine the epithermal activation Aepi. The thermal component of
the total activation, Ath = Atot − Aepi, is proportional to the thermal flux at the
location of the foil, Ath = cthϕM(x). The epithermal activation is proportional to
the slowing-down source, Aepi = cepiqM. Thus, qM/ϕM(x) = (cepi/cth)(Aepi/Ath).
The quantity CR = Aepi/Ath is determined by the foil measurements and is
known as the cadmium ratio.
The ratio of constants (cepi/cth) can be determined by irradiating many clad and
unclad indium foils in a large block of pure moderator that has a source emitting
Q neutrons per second. The neutron balance is
ΣaM∫ϕ(x)dx ' ∫q(x)dx = Q
(3.96)
and the ratio of integrated thermal and epithermal activities is
ρ ≡ ∫Ath(x)dx
∫Aepi(x)dx
=
cepi∫ϕ(x)dx
cth∫q(x)dx
= cepi
cth
ΣaM
(3.97)
These results can be combined to write an expression for the thermal utilization,
f = 1 − ΣaMϕM(1 + L2B2)
qM
= 1 − 1 + L2B2
ρCR
ϕM
ϕM(x)
(3.98)
in terms of the experimentally determined quantities CR and ρ and the local-toaverage
moderator flux ratio, which can be calculated using the foregoing
formalism.

### Local Power Peaking Factor

Once effective homogenized cross sections are constructed, the fuel–moderator
assembly may be treated as a homogeneous region, and the average flux
distribution in the assembly may be calculated using one of the other techniques
discussed in this chapter. The average power density in the fuel–moderator
assembly is then Σeff
f Fϕav, where Σeff
f F is given by an expression such as Eq. (3.92)
and ϕav is the average flux in the fuel–moderator assembly:
ϕav = ϕFV F + ϕMV M
V F + V M
= ϕF
1 + ζ(V M + V F)
1 + (V M + V F)
(3.99)
The peak power density will occur at the location of the maximum neutron
flux in the fuel element, which is at x = a, as may be seen from Eq. (3.89). The
power peaking factor – the ratio of the peak to average power densities in the

<!-- page 72 (PDF 96) -->
assembly – is given by
Fpp ≡ Σf FϕF(a)
Σeff
f Fϕav
=
1 + V M
V F

 ϕF(a)
ϕF
=
1 + V M
V F

 a
LF
coth a
LF
=
1 + V M
V F

1 + 1
a
LF

− 1
a
LF

+ ∙∙∙
"
;
a
LF
< π
(3.100)
where the form of ϕF(a)/ϕF for a slab fuel–moderator lattice has been used to
arrive at the second form of the equation. The power peaking is minimized by
minimizing a/LF and VM/VF.

## 3.9 Control Rods

### Effective Diffusion Theory Cross Sections for Control Rods

Localized highly absorbing control elements such as control rods cannot be
calculated directly using diffusion theory. However, transport theory can be used
to determine effective diffusion theory cross sections for use with diffusion theory.
We illustrate this by considering the BWR example, shown in Fig. 3.5, of a core
consisting of a repeating array of four fuel–moderator assemblies surrounding a
cruciform control rod. First, the fuel–moderator assemblies must be homogenized,
using the procedure of Section 3.8 or some more sophisticated procedure based on
transport theory, yielding a model of a cruciform control rod embedded in a square
cell of homogeneous fuel–moderator, as shown in Fig. 3.6. If the span, l, of the
control blade is large compared with the neutron diffusion length in the fuel–
moderator region, the diffusion of neutrons into the rod is essentially one-dimensional
. We take advantage of this fact to replace the two-dimensional problem by an
equivalent one-dimensional problem that preserves both the ratio of the control rod
surface to the fuel–moderator volume and the thickness of the control blade. We
construct an equivalent model consisting of a repeating array of fuel–moderator
slabs of thickness 2a and control rod slabs of thickness 2t, where a = (m2 − 2tl + t2)/
2l, as shown in Fig. 3.6. Our calculational model then is a fuel–moderator (half) slab
from x = 0 to x = a and a control (half) slab from x = a to x = a + t, with symmetry
boundary conditions at x = 0 and x = a + t. The neutron diffusion equation
−D d2ϕ(x)
dx2
+ Σaϕ(x) = S0
(3.101)
is valid in the fuel–moderator slab, where S0 is a uniform source of neutrons
slowing down in the fuel–moderator region. The symmetry boundary condition
for the diffusion theory calculation is
dϕ(0)
dx
= 0
(3.102)

<!-- page 73 (PDF 97) -->
and a transport boundary condition
J(a)
ϕ(a) = α
(3.103)
is used at the fuel–moderator interface with the control rod. The parameter α
must be determined from a transport theory calculation of the control rod region
(Section 3.12). For a slab of width 2t, such a calculation yields
α =
1 − 2E3(2Σact)
2[1 + 3E4(2Σact)]
(3.104)
where Σac is the control rod absorption cross section and En is the exponential
integral function:
En(g) = ∫
e−guu−ndu
(3.105)
The solution to Eq. (3.101) that satisfies Eqs. (3.102) and (3.103) is
ϕ(x) = S0
Σa
1 −
αcosh(x=L)
αcosh(a=L) + (D=L)sinh(a=L)

(3.106)
We now define an effective diffusion theory cross section for the control rod by
requiring that the diffusion theory and transport theory calculations of the
2/
2t
2t
a
x
2m
Control
Control
Fuel
+
moderator
Fuel
+
moderator
Fig. 3.6 One-dimensional model of a cruciform control blade cell. (With permission from
Ref. [2]. Copyright 1976, Wiley.)

<!-- page 74 (PDF 98) -->
neutron absorption rate in the control rod agree:
Σeff
c ϕavAcell = PcJc
(3.107)
where ϕav is the average diffusion theory flux in the fuel–moderator region,
Acell = (a + t)b is the area of the fuel–moderator plus control rod cell of arbitrary
transverse direction b, Pc = b is the perimeter of the control rod interface with the
fuel–moderator region, and Jc is the neutron current from the fuel–moderator
region at the surface of the control rod. It is assumed that all neutrons that enter
the control rod are absorbed. Combining the results above yields
Σeff
c
= Pc
Acell
Jc
ϕ = 1
a α ϕ(a)
ϕ
=
Σa
a[Σa=α + (1=L)coth(a=L)] − 1
(3.108)
for the effective homogeneous control rod cross section to be used in a diffusion
theory calculation. Note that the Σa in this equation is the effective fuel–
moderator homogenized cross section, and the control rod cross section is
hidden in the parameter α.

### Example 3.5 Slab Control Plate Effective Cross Section

Consider again the
lattice of alternating 10% enriched uranium fuel and water slabs, each 1 cm thick,
discussed in Section 3.8. The effective homogenized lattice cross sections
are Σeff
a = 0.4144 cm−1 and Σeff
tr = 0.0525 cm−1, leading to Deff = 6.35 cm and Leff =
3.91 cm in the fuel–water lattice. Now consider the placement of 1-cm-thick slab
naturalboronplates(19.9% 10B)every10.5 cminthelattice.WithrespecttoFig.3.6,
t = 0.5 cm and a = 5 cm. The 10B density in the control slab is nB10 = 0.199(2.45/
10.8)(0.6022 × 1024) = 0.0271 × 1024 cm−3, the absorption cross section from
Table 3.4 is σB10 = 3.41 × 10−21 cm2, and the macroscopic control slab absorption
cross section is Σac = 92.411 cm−1. For such large values of 2tΣac, the exponential
integrals approach zero and the transport boundary condition parameter α →0.5.
Evaluation of Eq. (3.108) with these parameters yields for the effective homogenized
control cross section Σeff
c = 0.0894 cm−1.Thus, in the homogenized representation
of the lattice, the effective macroscopic absorption cross section is
0.414 cm−1 with the control plates removed and 0.493 cm−1 with the control
plates inserted. The effective transport cross section is 0.0525 cm−1 and is assumed
to be the same with or without the control plates.

### Windowshade Treatment of Control Rods

Now that we know how to obtain effective homogenized cross sections for the
fuel–moderator assemblies, and for control rods we can represent the partial
insertion of a bank of control rods (from the top) into a bare cylindrical core as a
two-region core diffusion problem, as indicated in Fig. 3.7. The lower, unrodded
region is represented by the homogenized fuel–moderator cross sections, and the
upper rodded region is represented by the homogenized fuel–moderator cross
sections plus the effective control rod cross section.
The neutron diffusion equation in both the rodded and unrodded regions is of
the form of Eq. (3.69), and we can anticipate from the development of Section 3.6

<!-- page 75 (PDF 99) -->
that a separation of variables solution that satisfies a zero flux boundary condition
at r = R (we assume that the reactor is sufficiently large that the zero flux condition
at the external boundary is equivalent to the zero flux condition at the extrapolated
boundary) will be of the form
ψ(r; z) = Z(z)J0
v1r
R
(3.109)
and the function Z(z) will satisfy
d2Z
dz2 + B2
z(Z)(z) = 0
(3.110)
where
B2
z ≡ vΣf =Σa − 1
L2
−
v1
Rex

(3.111)
and ν1 = 2.405 is the smallest root of J0(ν) = 0.
Solving the diffusion equation separately in the rodded and unrodded regions
and requiring that the solutions vanish at z = 0 and z = H yields
Zun(z) = Aunsin Bun
z z
;
0 ≤ z ≤ h
Zrod(z) = Arodsinh Brod
z (H − z)

; h ≤ z ≤ H
(3.112)
Rod bank
z
H
(z)
h = H
h = 0.6 H
h = 0.4 H
No control
h
Fig. 3.7 Insertion of a control rod bank into a bare cylindrical core. (With permission from
Ref. [2]. Copyright 1976, Wiley.)

<!-- page 76 (PDF 100) -->
We require continuity of flux and current at z = h, the interface between the
rodded and unrodded regions,
Zun(h) = Zrod(h)
Dun
dZun(h)
dz
= Drod
dZrod(h)
dz
(3.113)
The first condition leads to the relationship
Arod
Aun
=
sin(Bun
z h)
sinh[Brod
z (H − h)]
(3.114)
and dividing the two conditions leads to the criticality condition,
DunBun
z
tanBun
z h = −
DrodBrod
z
tanh Brod
z (H − h)

(3.115)
which may be solved for the rod insertion distance (H − h), for which the reactor is
just critical.
The axial neutron flux solution is sketched in Fig. 3.7 for several rod insertions.
As might be expected, the axial flux distribution is symmetric when the rod bank
is fully withdrawn and becomes progressively more peaked toward the bottom of
the core as the rod bank is inserted farther downward. Note that in case of rod
insertion from the bottom, the situation is just reversed.

## 3.10 Numerical Solution of Diffusion Equation

Although the semianalytical techniques for solving the neutron diffusion equation
that we have developed can be extended to treat reactor models consisting of
a larger number of different homogeneous regions than we have considered,
realistic reactor models may consist of hundreds or thousands of different
homogenized regions, even after the local fuel–moderator homogenization has
taken place. The fuel concentration may vary from assembly to assembly and
within an assembly in order to make the power distribution more uniform, and
even within initially uniform assemblies the composition will change differently
from location to location with fuel burnup. The standard practice today is to use
numerical techniques to solve the neutron diffusion equation.

### Finite-Difference Equations in One Dimension

The neutron diffusion equation in a one-dimensional slab reactor model is
− d
dx D(x) dϕ(x)
dx
+ Σa(x)ϕ(x) = 1
λ vΣf (x)ϕ(x)
(3.116)

<!-- page 77 (PDF 101) -->
The first step in developing a numerical solution procedure is to replace the
continuous spatial dependence of the flux, ϕ(x), with the values of the flux at a
number of discrete spatial locations, ϕi ≡ ϕ(xi), the solution for which will be the
objective of the numerical technique. There are many ways to do this, and we will
use a simple finite-difference approximation. We subdivide the interval 0 ≤ x ≤ a of
interest into I subintervals of length Δ = a/I. (A more general development would
use nonuniform subintervals.) A general rule of thumb is that Δ < L (the neutron
diffusion length) sets an upper limit on the subinterval length (or mesh spacing).
j
x0
j Δ !
x1
j
x2 . . .
j
xi−1
j
xi
j
xi+1 . . .
j
xI−1
j
xI
j
xi−1=2
j
xi+1=2
Next, the terms in Eq. (3.116) are each integrated from xi−1/2 to xi+1/2, using the
following approximations:
∫
xi+(1=2)Δ
xi−(1=2)Δ
dxΣa(x)ϕ(x)
' ΣaiϕiΔ
∫
xi+(1=2)Δ
xi−(1=2)Δ
dx
d
dx D(x) dϕ
dx

' Ddϕ
dx

xi+1=2Δ
− Ddϕ
dx

xi+1=2Δ
' 1
2 (Di + Di+1) ϕi+1 − ϕi
Δ
− 1
2 (Di−1 + Di) ϕi − ϕi−1
Δ
(3.117)
where we have associated Σai, Di, and so on, with the subinterval xi−1/2 ≤ x ≤ xi+1/2.
The discrete equation associated with xi may be written as
ai;i−1ϕi−1 + ai;iϕi + ai;i+1ϕi+1 = 1
λ f iϕi ≡ Si;
i = 1; . . . ; I − 1
(3.118)
where
ai;i−1 = − 1
Di + Di−1
Δ2

1 −
c
2i − 1
ai;i
= Σai + 1
Di−1 + 2Di + Di+1
Δ2

ai;i+1 = − 1
Di+1 + Di
Δ2

1 +
c
2i − 1
f i
= vΣf i
(3.119)
We have generalized to other one-dimensional geometries, where c = 0, 1, and 2
for slab, cylindrical, and spherical, respectively. The significant feature of the set of
Eqs. (3.118) is nearest-neighbor coupling – the flux at any xi is only directly

<!-- page 78 (PDF 102) -->
coupled to the flux at the adjacent points xi−1 and xi+1, which greatly facilitates
their solution.
Note that the difference equations are formulated only for the I − 1 interior
mesh points at x1, x2, . . . , xI−1. The boundary conditions determine the exterior
mesh points. A zero flux boundary condition at the left boundary corresponds to
ϕ0 = 0, for example. A zero current or symmetry boundary condition at the left
boundary corresponds to ϕ0 = ϕ1 and would be implemented by setting a1,0 = 0
and a1,1 = Σa1 + (D1 + D2)/Δ2.

### Forward Elimination/Backward Substitution Spatial Solution Procedure

The set of I − 1 in Eqs. (3.118) can readily be solved by Gaussian elimination, or
forward elimination backward substitution, for a known fission source Si. The
Gaussian elimination solution is implemented by subtracting ai,i−1/ai−1,i−1 times
the (i − 1)th equation from the ith equation to eliminate the ai,i−1 element in the
ith equation. The modified ith equation is then divided by ai,i. This process is
repeated successively for i = 1 through i = I − 1. Then the manipulated equations
can be solved successively from i = I − 1 to i = 1 using the algorithms
ϕI−1 = αI−1
ϕI−2 = −AI−2ϕI−1 + αI−2
..
.
..
. ..
.
ϕi
= −Aiϕi+1 + αi
(3.120)
for the backward substitution, where
A1 = a1;2
a1;1
; Ai =
ai;i+1
ai;i − ai;i−1Ai−1
α1 = S1
a1;1
; αi = Si − ai;i−1αi−1
ai;i − ai;i−1Ai−1
(3.121)
had previously been constructed on the forward elimination.

### Power Iteration on Fission Source

Thefissionsourceisnotknowna priori,ofcourse,sotheGaussianeliminationmust
beembeddedinaniterationonthefission source term,as follows. Aninitial guessof
the flux ϕ(0)
i
at each point and of the eigenvalue λ(0) is made and an initial fission
sourceateach pointisconstructedSi(0) = vΣf iϕ(0)
i =λ(0). TheGaussianeliminationis
performed to determine ϕ(1)
i . A new estimate of the eigenvalue is made from
λ(1) =
ΣI−1
i=1vΣf iϕ(1)
i Δ
ΣI−1
i=1Δ[ai;i−1ϕ(0)
i−1 + ai;iϕ(0)
i
+ ai;i+1ϕ(0)
i+1]
'
ΣI−1
i=1vΣf iϕ(1)
i Δ
ΣI−1
i=1vΣf iϕ(0)
i Δ=λ(0)
(3.122)

<!-- page 79 (PDF 103) -->
and a new fission source is constructed from
S(1)
i
= 1
λ(1) vΣf iϕ(1)
i
(3.123)
This iteration process is continued [using Eqs. (3.122) and (3.123) with 0 →n − 1
and 1 →n] until the eigenvalues obtained on two successive iterates differ by less
than some convergence criterion, say ε = 10−5:
λ(n) − λ(n−1)
λ(n−1)

 < ε
(3.124)

### Finite-Difference Equations in Two Dimensions

In rectangular geometry, the neutron diffusion equation is
− @
@x D(x; y) @ϕ(x; y)
@x
− @
@y D(x; y) @ϕ(x; y)
@y
+ Σa(x; y)ϕ(x; y)
= 1
λ vΣf (x; y)ϕ(x; y)
(3.125)
To extend the procedure for developing finite-difference equations that was
discussed for the one-dimensional case, we consider a rectangle with x-dimension
a and y-dimension b. We subdivide a into I intervals of length Δx = a/I and
subdivide b into J intervals of length Δy = b/J.
□
□
□
□
□
□
□
□
□
□
yJ
□
□
□
□
□
□
□
□
□
□
yJ−1
□
□
□
□
□
□
□
□
□
□
..
.
□
□
□
□
□
□
□
□
□
□
yJ+1
□
□
□
□
□
□
□
□
□
□
yj
(i; j)
□
□
□
□
□
□
□
□
□
□
yj−1
□
□
□
□
□
□
□
□
□
□
..
.
□
□
□
□
□
□
□
□
□
□
y2
□
□
□
□
□
□
□
□
□
□
y1
□
□
□
□
□
□
□
□
□
□
y0
x0
x1
x2
. . .
xi−1
xi
xi+1
. . .
xI−1
x1

<!-- page 80 (PDF 104) -->
The diffusion equation is integrated over the mesh box (xi−1/2 ≤ x ≤ xi+1/2, yj−1/2/≤
y ≤ yj+1/2), and the approximations of Eqs. (3.117) are extended to two dimensions
to obtain the finite-difference equations:
− 1
Di−1;j + Di;j
Δ2
y
!
ϕi−1;j − 1
Di;j + Di+1;j
Δ2
x

ϕi+1;j
− 1
Di;j−1 + Di;j
Δ2
y
!
ϕi;j−1 − 1
Di;j + Di;j+1
Δ2
y
!
ϕi;j+1
+
Σaij +
2 Di−1;j + Di;j + 1
2Di+1;j
Δ2
x
+
2 Di;j−1 + Di;j + 1
2Di;j+1
Δ2
y
!
ϕi;j
= 1
λ vΣf i;jϕi;j;
i = 1; . . . ; I − 1;
j = 1; . . . ; J − 1
(3.126)
The significant feature of these equations is, once again, nearest-neighbor
coupling – the flux at (i, j) is only directly coupled to the fluxes at (i, j + 1),
(i, j − 1), (i + 1, j), and (i − 1, j).
The boundary conditions are used to specify ϕ0,j, ϕI,j, ϕi,0, and ϕi,J, as discussed
for the one-dimensional case.
In order to simplify the notation somewhat, we replace the (i, j) identification of
a spatial location with a (p) identification. The total number of spatial locations is
P = (I − 1) × (J − 1). We will choose p = 1 for (i = 1, j = 1), p = 2 for (i = 2, j = 1), . . . ,
p = I − 1 for (i = I − 1, j = 1), p = I for (i = 1, j = 2), . . . , p = 2(I − 1) for (i = I − 1,
j = 2), and so on. Then the set of finite-difference equations may be written as
a1;1ϕ1 + a1;2ϕ2 + a1;3ϕ3 + ∙∙∙+ a1;pϕp + ∙∙∙+ a1;PϕP = Sf 1
a2;1ϕ1 + a2;2ϕ2 + a2;3ϕ3 + ∙∙∙+ a2;pϕp + ∙∙∙+ a2;PϕP = Sf 2
a3;1ϕ1 + a3;2ϕ2 + a3;3ϕ3 + ∙∙∙+ a3;pϕp + ∙∙∙+ a3;PϕP = Sf 3
..
.
..
. ..
.
aP;1ϕ1 + aP;2ϕ2 + aP;3ϕ3 + ∙∙∙+ aP;pϕp + ∙∙∙+ aP;PϕP = Sf P
(3.127)
where
ap;p
= Σap +
2 Dp−1 + Dp + 1
2Dp+1
Δ2
x
+
2 Dp−I + Dp + 1
2Dp+I
Δ2
y
ap;p−1 = − 1
Dp−1 + Dp
Δ2
x

;
ap;p+1 = − 1
Dp + Dp+1
Δ2
y
!
ap;p−I = − 1
Dp + Dp−I
Δ2
y
!
;
ap;p+I = − 1
Dp+I + Dp
Δ2
y
!
ap;q
= 0;
q ≠p − 1;
p + 1;
p − I;
p + I
Sf p
= 1
λ vΣf pϕp
(3.128)

<!-- page 81 (PDF 105) -->
### Successive Relaxation Solution of Two-Dimensional Finite-Difference Equations

There are a number of possible ways to solve the set of Eqs. (3.127). We describe
here the widely used Gauss–Seidel or successive relaxation method. This is an
iterative method that proceeds by solving the first equation for ϕ1, assuming S1 is
known and guessing a value for ϕ2, . . . , ϕP; then solving the second equation for
ϕ2, assuming that S2 is known, using the value just calculated for ϕ1, and using the
same guessed values for ϕ3, . . . , ϕP; then solving the third equation for ϕ3,
assuming that S3 is known, using the just calculated values for ϕ1 and ϕ2, and
using the same guessed values for ϕ4, . . . , ϕP; and continuing thusly until the last
equation is solved for ϕP, assuming that SP is known, and using the just calculated
values for ϕ1, . . . , ϕP−1. The set of new values of ϕ1, . . . , ϕP thus calculated
provides a new guess to be used in a repeated iteration. The general algorithm for
the solution at each step is
ϕ(m+1)
p
= 1
ap;p
Sf p −
X
p−1
q=1
ap;qϕ(m+1)
q
−
X
P
q=p+1
ap;qϕ(m)
q
"
(3.129)
where m is the iteration index. This inner iteration is continued until the flux
solution at each location has converged to within a specified tolerance, ε ≈ 10−2,
which may be chosen smaller in regions where exact knowledge of the neutron
flux is more important than in, for example, reflector regions:
ϕ(m+1)
p
− ϕ(m)
p
ϕ(m)
p

 < εp
(3.130)
It is possible to accelerate the convergence of the relaxation iteration by using
as a new flux guess a mixture of the previous flux and the relaxation result of
Eq. (3.129):
ϕ(m+1)
p
= (1 − ω)ϕ(m)
p
+ ω
ap;p
Sf p −
X
p−1
q=1
ap;qϕ(m+1)
q
−
X
P
q=p+1
ap;qϕ(m)
q
"
(3.131)
The acceleration parameter ω may be chosen in a number of ways (see Ref. [4]),
but generally varies between 1 and 2. The algorithm of Eq. (3.131) is known as
successive overrelaxation (SOR).
Another widely used method for solving the two-dimensional diffusion equations
is the alternating direction implicit iteration scheme described in
Section 16.3.

### Power Outer Iteration on Fission Source

The power iteration on the fission source proceeds as described above [i.e., in
Eqs. (3.122)–(3.124)] but with i replaced by p in the notation of this section, and
with Δ replaced by Δx, Δy.
