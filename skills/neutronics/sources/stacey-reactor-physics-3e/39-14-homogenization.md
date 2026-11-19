# 14 Homogenization — 14 Homogenization … 14.5 Homogenization Theory
<!-- source PDF pages 553-570 -->

<!-- page 535 (PDF 553) -->
# 14 Homogenization

Nuclear reactor cores are composed of a large number of fuel assemblies, each
containing a large number of discrete fuel elements of differing composition and
consisting of separate fuel and cladding regions, coolant, structural elements,
burnable poisons, water channels, control rods, and so on – tens to hundreds of
thousands of discrete, heterogeneous regions. On the other hand, most of the
methods for calculating criticality and global flux distributions that are in use (in
particular diffusion theory) are predicated on the existence of large (with respect
to a mean free path) homogeneous regions. The methods employed to replace a
heterogeneous lattice of materials of differing properties with an equivalent
homogeneous mixture of these materials to which the previously discussed
methods for the calculation of ultrafine-group spectra, calculation of the diffusion
of neutrons during the slowing-down process, and so on are referred to as
homogenization theory. Homogenization of a heterogeneous assembly usually
proceeds in two steps: a lattice transport calculation to obtain the detailed
heterogeneous flux distribution within a unit cell or fuel assembly, followed
by the use of this detailed flux distribution to calculate average homogeneous
cross sections for the unit cell or assembly.
The general procedure that is followed in nuclear reactor analysis is to perform
very detailed energy and spatial calculations on a local basis to obtain cross
sections averaged over energy and spatial detail that can be used in few-group
global core calculations. For example, for a thermal reactor, a pin-cell transport
calculation of a cell consisting of the fuel, clad, coolant, and structural in a local
region may be carried out in 20–100 fine groups to obtain homogenized 6–20
intermediate-group cross sections averaged over the pin-cell geometry and the
20–100 fine-group spectrum. Several such pin-cell calculations may be needed for
a fuel assembly and the adjacent water gaps and control rods. Intermediate-group
assembly transport calculations are then performed for models that represent all
fuel pins, control rods, water channels, can walls, and so on, associated with a
given fuel assembly. It is important that the intermediate-group assembly
transport calculation uses enough groups to represent the spectral interactions
among fuel pins of different composition, control rods, water channels, and so on,
at the intermediate-group level. Several such intermediate-group assembly calculations
may be needed for the reactor core, and a large number of such
calculations may be needed to represent different operating temperatures,
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 536 (PDF 554) -->
depletion steps, void fractions, and so on. The results of the intermediate-group
assembly transport calculations are next averaged over the assembly spatial detail
and the intermediate-group spectra to obtain two to six few-group homogenized
assembly cross sections which can be used in few-group global core calculations
of criticality and flux distribution.
We have discussed the procedure of group collapsing to obtain few-group cross
sections from fine- or intermediate-group spectra in previous chapters. Here we
are interested in the spatial-averaging procedures used to obtain homogenized
cross sections appropriately averaged over spatial detail, and in the procedures
used to construct effective diffusion theory cross sections for regions such as
control rods in which the basic assumptions of diffusion theory are not satisfied.

## 14.1 Equivalent Homogenized Cross Sections

The general problem of homogenization can be illustrated by considering a
symmetric, repeating array of fuel and moderator elements of volumes VF and VM.
The average absorption cross section for the fuel–moderator unit cell is
hΣaicell = ΣF
aϕFV F + ΣM
a ϕMV M
ϕFV F + ϕMV M
= ΣF
a + ΣM
a (V M=V F)ζ
1 + (V M=V F)ζ
(14.1)
where
ζ ≡ ϕM
ϕF
(14.2)
is referred to as the flux disadvantage factor, and φF and φM are the average
neutron fluxes in the fuel and moderator, respectively. The homogenized cell
average cross section of Eq. (14.1) is equivalent in the sense that if it is multiplied
by the exact average cell flux
ϕcell = ϕFV F + ϕMV M
V F + V M
≡ ϕFV F + ϕMV M
V cell
(14.3)
and the cell volume, the result will be the exact absorption rate in the cell:
hΣaicellϕcellV cell ≡ ΣF
aϕFV F + ΣM
a ϕMV M
(14.4)
This type of definition can obviously be extended to a multiregion heterogeneous
assembly by defining
hΣaicell = Σ1
a + PI
i=2 Σi
a(V i=V 1)ζi
1 + PI
i=2(V i=V 1)ζi
; ζi ≡ ϕi
ϕ1
ϕcell
≡
PI
i=1 ϕiV i
PI
i=1 V i
≡
PI
i=1 ϕiV i
V ce11
(14.5)

<!-- page 537 (PDF 555) -->
The same type of definition defines equivalent cell average fission and
scattering cross sections. The appropriate definition of the cell average diffusion
coefficient is less straightforward. An equivalent cell average diffusion
coefficient must represent the net leakage from the cell, but that depends
on the calculational method that will be employed for that purpose. We will
return to this subject when we consider the detailed homogenization
procedures.
Thus, the problem of cell homogenization reduces to the problem of determining
the flux disadvantage factors, ξi, which will enable the homogenized
model to predict the correct intracell reaction rates, and of determining the
equivalent diffusion coefficients (or other leakage representation) that will enable
the homogenized model to predict correct intercell leakage. Note that it is only
necessary to know the relative value of the neutron flux in the different regions of
the problem, not the absolute values, in order to calculate homogenized cross
sections, which enables calculation of homogenized cross sections for local
regions in a reactor before the absolute value of the flux is determined from a
global calculation (which utilizes the homogenized cross sections). Calculation of
the flux disadvantage factors from diffusion theory was discussed in Chapter 4.
We turn now to methods that can be used when diffusion theory does not provide
an adequate treatment of the heterogeneous problem, which is the usual case in a
nuclear reactor.

## 14.2 ABH Collision Probability Method

The ABH collision probability method (named after its originators – Ref. [1])
found widespread use for calculation of thermal disadvantage factors before the
availability of assembly transport codes (discussed in Section 14.4) and provides
physical insight into the unit cell transport problem. A unit cell of fuel (F) and
moderator (M) with zero net current on the cell boundary is assumed. It is further
assumed that the neutron slowing-down source is uniform in the moderator and
zero in the fuel. We define
PFM = average probability that a neutron born uniformly and isotropically in
region F will eventually be absorbed in region M
PF = average probability that a neutron born uniformly and isotropically in region
F escapes from the fuel before being absorbed
βM = conditional probability that a neutron, having escaped from F into M, will
then be absorbed in M
A similar probability PMF can be defined for region M. As discussed in
Chapter 11, there exists a reciprocity relation:
V FΣF
aPFM = V MΣM
a PMF
(14.6)
Since neutrons are only slowing down to thermal in the moderator, the
reciprocity relation can be used to write the thermal utilization factor in terms

<!-- page 538 (PDF 556) -->
of PFM:
f ≡ PFM = V F
V M
ΣF
a
ΣM
a
PFM =
ΣF
aV FϕF
ΣF
aV FϕF + ΣM
a V MϕM
(14.7)
and to write the thermal disadvantage factor:
ζ ≡ ϕM
ϕF
= ΣF
a
ΣM
a
V F
V M
f □ 1

=
PFM
□ ΣF
a
ΣM
a
V F
V M
(14.8)
The probability that a neutron born uniformly and isotropically in the fuel
escapes into the moderator without making a collision was discussed in
Chapter 11 and is given approximately by
PF0 '
1 + 4(V FΣF
t =SF)
(14.9)
where SF is the surface area of the fuel. If the neutron does not escape but has a
scattering event [probability (1 □ PF0)ΣF
S=ΣF
t ], it also has a probability PF0 of escaping
without a second collision. Continuing this line of argument, the total probability that
the neutron escapes from the fuel into the moderator may be written as
PF = PF0 1 + (1 □ PF0) ΣF
s
ΣF
t
+ (1 □ PF0)2 ΣF
s
ΣF
t

+ ∙∙∙
"
=
PF0
1 □ (1 □ PF0)(ΣF
S=ΣF
t ) =
1 + ΣF
a(1 □ PF0)=ΣF
t PF0
(14.10)
A somewhat more accurate expression, which takes into account the nonuniform
distribution of the first collisions for a cylindrical fuel rod of radius a, is
PF =
1 + ΣF
a
ΣP
t
1 □ PF0
PF0
+a

1 + α ΣF
s
ΣF
t
+ β ΣF
s
ΣF
t

"
+ aΣF
a
(
)□1
(14.11)
where the parameters α and β are as given in Fig. 14.1.
It is apparent from the definitions that
PFM = PFβM
(14.12)
Equation (14.7) can be rearranged to
f □ 1 = ΣM
a
ΣF
a
V M
V F
PF
+ 1 □ f □ βM
f
= ΣM
a
ΣF
a
V M
V F
PF
+ 1 □ PMF
PMF
□ βM
PMF
(14.13)

<!-- page 539 (PDF 557) -->
Using the reciprocity relation of Eq. (14.6) and, for the purpose of estimating βM
only, approximating PF ≈ FF0 ≈ SF=4V FΣF
a yield an approximation for the
conditional probability:
βM ' 4ΣM
a V M
SM
PMF
(14.14)
We approximate PMF ≈ PM (probability that a neutron born in the moderator
escapes from the moderator before being absorbed). We calculate PM by solving
the diffusion equation in the moderator:
□DM∇2ϕM(r) + ΣM
a ϕM(r) = qM
(14.15)
where qM is the uniform slowing-down density in the moderator. The boundary
conditions for Eq. (14.15) are symmetry at the cell boundary and a transport
boundary condition at the fuel–moderator interface:
Cell boundary :
ns?∇ϕM = 0
Fuel−moderator interface: ns?
ϕM
∇ϕM

a
= 1
d
(14.16)
where ns is the unit vector normal to the surface and d is a transport parameter
related to the transport mean free path in the moderator and is given in
0.05
0.1
0.15
0.2
α
α, β
β
a
F
t
Fig. 14.1 Parameters α and β for use in calculation of ABH cylindrical escape probability.
(With permission from Ref. [2]. Copyright 1976, Wiley.)

<!-- page 540 (PDF 558) -->
Fig. 14.2 for a cylindrical unit cell. Assuming that all neutrons diffusing from
the moderator into the fuel are absorbed, PM is just the total neutron flow into
the fuel from the moderator divided by the total neutron source in the
moderator:
PM = JM
outSF
qMV M
=
SF
qMV M
ns ? DM∇ϕMja =
adV M
2V FL2
M
+ E
a
LM
; b
LM

□1
(14.17)
where a is the thickness or radius of the fuel region, b is the thickness of the
moderator region associated with a fuel element, L2
M = DM=ΣM
a , and E(a/LM, b/
LM) is the lattice function given in Table 3.6.
With these approximations for βM and PMF given by Eqs. (14.14) and (14.17),
respectively, and the expression for PF given by Eq. (14.11), Eq. (14.13) can be
evaluated:
f □ 1 = ΣM
a V F
ΣF
aV F
1 + ΣF
a
ΣF
t
1 □ PF0
PF0
□ aΣF
t

1 + α ΣF
s
ΣF
t
+ β ΣF
s
ΣF
t

"
(
)
+
ad
2L2
M
□ aΣM
a

 V M
V F
+ E
a
LM
; b
LM

□ 1
(14.18)
0.6
0.8
1.0
1.2
Small black cylinder
Probable shape of dependence for a
cylinder of finite radius
Large black cylinder
1.4
Radius of black cylinder R
M
tr
Linear extrapolation distance d
M
tr
Fig. 14.2 Transport boundary condition for cylinders. (With permission from Ref. [2].
Copyright 1976, Wiley.)

<!-- page 541 (PDF 559) -->
the disadvantage factor can be calculated from
ζ = ΣF
a
ΣM
a
V F
V M
f □ 1

(14.19)
and the homogenized cross section can be calculated from Eq. (14.1).
Although we have developed the ABH method in the context of thermal
neutrons, the same general procedure can be applied to homogenize cross
sections for any group of a multigroup scheme.

## 14.3 Blackness Theory

Blackness theory refers to a class of methods for matching an approximate (e.g.,
diffusion theory) solution in one region to a very accurate solution of the
transport equation in an adjacent region in order to obtain an effective diffusion
theory cross section that will preserve the transport theory accuracy in the
calculation of reaction rate. Such a procedure is required in order to treat control
rods, lumped burnable poisons, and so on, within the context of multigroup
diffusion theory.
Consider a purely absorbing slab occupying the region xi ≤ x ≤ xi+1. The onespeed
transport equation within the absorbing slab is
μ @
@x ψ(x; μ) + Σaψ(x; μ) = 0
(14.20)
This equation may be solved for the exiting neutron fluxes ψ+(xi+1, μ) to the right
and ψ□(xi, μ) to the left in terms of the entering fluxes from the left ψ+(xi, μ) and
from the right ψ□(xi, μ), where the +/□ denotes μ > 0/μ< 0:
ψ+(xi+1; μ) = ψ+(xi; μ)exp □Σa
Δ
μ

; 1 > μ > 0
ψ□(xi; μ)
= ψ□(xi+1; μ)exp Σa
Δ
μ

; □1 < μ < 0
(14.21)
where Δ = xi+1 □ xi. The incident fluxes into the purely absorbing region are
assumed to have the Pl form that is consistent with a diffusion theory solution in
the adjacent fuel-moderating region:
ψ+(xi; μ)
= ϕ(xi) + 3μJ(xi);
1 > μ > 0
ψ□(xi+1; μ) = ϕ(xi+1) + 3μJ(xi+1); □1 < μ < 0
(14.22)

<!-- page 542 (PDF 560) -->
The currents at the surfaces of the absorbing region can be written as
J(xi)
≡ ∫
□1
dμ
2 μψ(xi; μ)
= ∫
□1
dμ
2 μψ□(xi; μ) + ∫
dμ
2 μ ϕ(xi) + 3μJ(xi)
[
]
J(xi+1) ≡ ∫
□1
dμ
2 μψ(xi+1; μ)
□∫
□1
dμ
2 μ ϕ(xi+1) + 3μJ(xi+1)
[
] + ∫
dμ
2 μψ(xi+1; μ)
(14.23)
Using Eqs. (14.21) to evaluate the exiting fluxes, these equations become
2 J(xi)
= 1
4 ϕ(xi) □ 1
2 E3(ΣaΔ)ϕ(xi+1) + 3
2 E4(ΣaΔ)J(xi+1)
□ 1
2 J(xi+1) = 1
4 ϕ(xi+1) □ 1
2 E3(ΣaΔ)ϕ(xi) □ 3
2 E4(ΣaΔ)J(xi)
(14.24)
where E3 and E4 are the exponential integral functions,
En+2(ξ) ≡ ∫
μnexp □ ΣaΔ
μ

dμ
(14.25)
Equations (14.24) can be rearranged to define the blackness parameters
α(ΣaΔ) ≡ J(xi) □ J(xi+1)
ϕ(xi) + ϕ(xi+1) =
1 □ 2E3(ΣaΔ)
2[1 + 3E4(ΣaΔ)]
β(ΣaΔ) ≡ J(xi) + J(xi+1)
ϕ(xi) □ ϕ(xi+1) =
1 + 2E3(ΣaΔ)
2[1 □ 3E4(ΣaΔ)]
(14.26)
The parameter α is the ratio of the average inward current to the average flux at
the surface of the absorbing slab. This quantity is used as a boundary condition for
the diffusion theory calculation in the adjacent region,
JM
ϕM
= □ DM∇ϕM
ϕM
= α
(14.27)
(e.g., the transport parameter d of the ABH method is d/λtr = 1/3α). This transport
boundary condition was used in Chapter 3 to derive an effective diffusion theory
cross section for the control rod:
Σc
a =
ΣM
a
a[(ΣM
a =α) + (1=LM)coth(a=LM)] □ 1
(14.28)

<!-- page 543 (PDF 561) -->
where a is the half-thickness of the fuel–moderator region denoted by M. Since
this development was for a purely absorbing slab, the results are valid at any
energy, provided that the cross sections for that energy are used.
For a purely absorbing slab with a spatially dependent absorption cross section,
the results above are valid if the following replacement is made:
ΣaΔ ! ∫
xi+1
xi
Σa(x)dx
(14.29)

## 14.4 Fuel Assembly Transport Calculations

### Pin Cells

A fuel assembly consists of a large number of fuel pins of differing fuel loading,
enrichment, burnup, and so on, each of which is clad and surrounded by
moderator and perhaps other elements, such as structure and burnable poisons,
as depicted in Fig. 14.3. At this most detailed level of heterogeneity, the assembly
can be considered to be made up of a large number of units cells, or pin cells,
consisting of a fuel pin, cladding, surrounding moderator, and perhaps structure
and burnable poison. The first step in homogenizing the fuel assembly is to
homogenize each of the pin cells, by calculating the multigroup flux distribution
across the fuel, clad, moderator, and so on, and using it to calculate volumeaveraged
cross sections for the pin cell.
If the pin cell can be considered to be one of a large number of identical pin
cells, reflective symmetry boundary conditions can be used. However, this
assumption becomes questionable in the vicinity of gaps, control pins, burnable
poisons, or fuel pins of very different composition (e.g., MOX pins near UO2
pins). The influence of the surrounding environment can be introduced into the
pin-cell calculation by specifying the partial inward current J□ (and a zero
reflection, or black boundary conditions) or the net current J = J+ □ J□ (and a
perfectly reflecting boundary condition) on the cell boundary.

### Wigner–Seitz Approximation

If the cell associated with each pin is defined symmetrically and such that the cells
fill the volume of the assembly, the pin-cell boundary will have a noncylindrical
shape depending on the lattice geometry, generally square or hexagonal. Since the
pin geometry is cylindrical, it is convenient to approximate the actual pin-cell
geometry by an equivalent cylindrical cell that preserves moderator volume. The
approximate Wigner–Seitz cell has a radius R that depends on the pin-to-pin
distance p as R = p/π1/2 for a square pitch fuel lattice and R = p(31/2/2π)1/2 for a
hexagonal pitch lattice.
The change in geometry can lead to an anomalously high flux in the moderator of
a cell with reflective boundaryconditionsbecause a neutron introducedinto thecell

<!-- page 544 (PDF 562) -->
traveling in the direction of a chord that does not pass through the innermost n
shells before intersecting the reflecting cell boundary will never pass through these
innermost n shells since spectral reflection from the cylindrical wall will result in
motion along a similar chord. On the other hand, as shown in Fig. 14.4, correct
reflection from a square or hexagonal boundary will cause motion into the innermost
shells. This problem can be corrected by “white reflection” in a cosine
distribution with respect to the inward normal.

### Collision Probability Pin-Cell Model

The collision probability methodology of Section 9.3 can be extended to handle
the albedo (partial reflection) and incident current conditions that enable the
environment to influence the pin-cell calculations. With reference to Fig. 14.5,
consider a cylindrical pin cell consisting of i annular regions. Using the notation of
Section 9.3, define the probability, γ0i, that an uniformly distributed isotropic flux
Fig. 14.3 Representative fuel assembly. (With permission from Ref. [3]. Copyright 1993,
American Nuclear Society.)

<!-- page 545 (PDF 563) -->
of neutrons at the external surface (SB) of the pin cell will suffer a first collision in
region i before exiting across surface SB:
γ0i ≡
Σti∫V i
dri∫SB
drB∫Ω□V i
dΩ(n ? Ω)(1=4π)e□α(ri;rB)
∫SB∫Ω ? n<0
dΩ(n ? Ω)(1=4π)
(14.30)
where Ω □ Vi indicates those values of Ω that intersect the volume Vi, n is the
outward unit vector to the surface SB, α(ri, rB) is the optical distance (e.g., distance
Fig. 14.4 Reflection misrepresentation in Wigner–Seitz approximation. (With permission from
Ref. [3]. Copyright 1993, American Nuclear Society.)
Fig. 14.5 Cylindrical pin-cell
model.

<!-- page 546 (PDF 564) -->
measured in mean free paths) along the chord from rB to ri, and n □ Ω/4π is the
rate at which neutrons in an isotropic flux of unit strength will cross the surface at
SB into the pin cell. This probability is related to the first-flight escape probability,
P0i, that a neutron introduced in volume Vi will exit the pin cell across surface SB
without a collision:
P0i ≡ ∫V i
dri∫SB
drB∫Ω□V i
dΩ(n ? Ω)(1=4π)e□α(rB;ri)
∫4π
dΩ∫V i
dri(1=4π)
(14.31)
where 1/4π is the isotropic angular flux corresponding to unit scalar flux in Vi and
Ω □ Vi indicates those values of Ω for which a neutron could have reached rB on a
first flight from within volume Vi. Except for the Σti, the numerators are identical,
reflecting the fact that the probabilities for neutrons traveling from the surface
into volume Vi without collision and traveling in the opposite direction from
within Vi to the surface are identical. This allows Eq. (14.30) to be written as
γ0i =
ΣtiV iP0i
SB∫
□1
dμ∫
2π
dϕ(n ? Ω=4π)
= ΣtiV iP0i
4SB
(14.32)
In terms of the probability Pij/ΣtiVi that neutrons introduced uniformly and
isotropically within volume Vi have their first collision in volume Vj, this may be
written as
γ0i = ΣtiV i
4SB
1 □
X
I
j=1
Pij
ΣtiV i
!
= 4
SB
ΣtiV i □
X
I
j=1
Pij
!
(14.33)
A similar line of argument leads to the result that the probability, Ri, that a
uniformly distributed isotropic flux of neutrons crossing the external surface (SB)
of the pin cell will be removed (absorbed or scattered to another group) by a
collision in region i before exiting across surface SB is related to the total escape
probability, Pi, that a neutron introduced in volume Vi will escape (perhaps after
multiple collisions) out of the pin cell across surface SB:
Ri = ΣriV iPi
4SB
(14.34)
We now wish to construct source and current flux response functions in terms of
which the flux in any one of the annular regions of the pin cell can be constructed:
ϕi =
X
I
k=1
QkXki(β) + j□
exY i(β)
(14.35)

<!-- page 547 (PDF 565) -->
where Qk is the neutron source density in annular region k, Xki(β) is the neutron
flux produced in region i by a unit neutron source density in region k, taking into
account possible multiple reflections at the cell boundary with albedo β, and Yi(β)
is the neutron flux produced in annular region i by unit neutron inward current
across the cell boundary. The quantities Xki(0) and Yi(0) refer to the response
functions above when the albedo of the region surrounding the pin cell is zero
(i.e., when there is no reflection of neutrons exiting the pin cell back across surface
SB). The response functions Xki(β) and Yi(β) can be calculated in terms of Xki(0)
and Yi (0) and the albedo, β.
For a neutron incident into the pin cell across the boundary SB, the cell has an
effective albedo (1 □ R), where
R =
X
I
j=1
Ri =
X
I
i=1
ΣriV iY i(0)
(14.36)
is the total removal (Σr is the cross section for absorption plus scatter to another
group) probability for a neutron incident on the cell from outside. For a cohort of
incident neutrons, a fraction R is removed and a fraction (1 □ R) is returned to the
boundary SB. Of the (1 □ R) returned to the boundary, a fraction β (the albedo of the
surrounding assembly for neutrons exiting the pin cell) is reflected back into the pin
cell. Of the fraction (1 □ R)β that enters the cell for a second time, a fraction R is
removed and a fraction (1 □ R) return to the surface SB a second time, and so on.
Thus, an inward partial current of neutrons incident across SB is effectively
amplified by the factor 1+ 1 □ R
)β + [(1 □ R)β]2 + ∙∙∙= 1=[1 □ 1 □ R
)β]. If
Yi(0) is the neutron flux produced in annular region i by unit neutron inward
current across the cell boundary, without taking into account reflection of exiting
neutrons back into the pin cell, the neutron flux due to a unit inward, current
taking reflection into account, is
Y i(β) =
Y i(0)
1 □ β(1 □ R)
(14.37)
The flux Xki(β) in volume Vi due to a unit neutron source density in volume Vk is
made up of two components: the flux Xki(0) due to source neutrons from volume
Vk which have not been reflected from the boundary SB, and the flux due to the
number of source neutrons PkVk from volume Vk which do reach the boundary
and are reflected with albedo β. These reflected neutrons can be treated as an
incoming flux, and the flux produced by it in volume Vi is found by multiplying by
Yi(β). The resulting expression is
Xki(β) = Xki(0) + βPkV k
Y i(0)
1 □ β(1 □ R)
(14.38)
The collision probability Equations (9.54) were derived under the implicit
assumption of no reflection from the external boundary (i.e., β = 0) and no

<!-- page 548 (PDF 566) -->
incident current. Thus, these equations are suitable for calculating the basic
response functions Xki(0) and Yi(0) when a first collision source term to account
for incident partial current density j□
ex is included:
ΣtiV iϕi =
X
I
j=1
Pji (Σsj + vΣf j)ϕj
Σtj
+ Qj
Σtj

+ γi0j□
ex
≡
X
I
j=1
Pji cjϕj + Qj
Σtj

+ γi0j□
ex
(14.39)
The collision probabilities Pji for a cylindrical cell are given by Eqs. (9.63–9.65). In
some applications it may be more convenient to treat the fission neutron source
as a fixed source and include it in the Qj term.
The quantities Xki(0) satisfy this equation with a unit source density in volume
Vk only and no incident current density:
ΣtiV iXki(0) =
X
I
j=1
PjicjXkj(0) + Pki
Σk
;
i = 1; . . . ; I;
k = 1; . . . ; I
(14.40)
This constitutes a set of I2 equations to be solved for the Xki(0). The quantities
Yi(0) satisfy Eq. (14.39) with no volumetric source but with a unit external current
density:
ΣiV iY i(0) =
X
I
j=1
PjicjY j(0) + γi0;
i = 1; . . . ; I
(14.41)
– a set of I equations to be solved for the Yi(0).
In summary, the pin-cell calculation consists of (1) solving Eqs. (14.40) and (14.41)
for the isolated pin-cell flux response functions Xki(0) and Yi(0); (2) constructing the
flux response functions Xki(β) and Yi(β) that take into account reflection from the
surroundingmediumbythealbedoβ fromEqs.(14.37)and(14.38);(3)calculatingthe
flux in each annular region of the pin cell using Eq. (14.35); and (4) constructing
homogenized cross sections for the cell using Eq. (14.5).

### Interface Current Formulation

The outward partial current density from the pin cell across surface SB consists of
two components: (1) the source neutrons that are introduced within the pin cell
and that are crossing SB for the first time (ΣI
i=1PiV iQi), and (2) the incident
neutrons (j□
ex) that traverse the pin cell without being removed with probability
(1 □ R) – both components are reflected with probability β and constitute an
inward current that may traverse the cell without removal and so on. The total
outward partial current density due to neutron sources within the pin cell and

<!-- page 549 (PDF 567) -->
neutrons incident on the pin cell from the surrounding medium is
j+
out(β) =
PI
i=1 V iPiQi + (1 □ R)j□
ex
1 □ β(1 □ R)
(14.42)
The inward partial current density across surface SB also has two components:
(1) the source neutrons that escape from the pin cell to reach SB for the first time
(ΣI
i=1PiV iQi) and are reflected with probability β, and (2) the incident neutrons
(j□
ex), both of which may traverse the pin cell without removal with probability
(1 □ R) to reach surface SB and be reflected with probability β and so on. The total
incident partial current density is
J□
in(β) = β PI
i=1 V iPiQi + j□
ex
1 □ β(1 □ R)
(14.43)
The net current density (in the outward direction) across the surface of the pin
cell is
j(β) ≡ j+
out(β) □ j□
in(β) = (1 □ β) PI
i=1 V iPiQi □ Rj□
ex
1 □ β(1 □ R)
(14.44)

### Multigroup Pin-Cell Collision Probabilities Model

The pin-cell model above extends immediately to multigroup by making the
replacements Σti ! Σg
ti, Σri ! Σg
ti □ Σg!g
si
(i.e., group removal cross section),
γ0i ! γg
0i, Pji ! Pji
g, and Ri ! Rg
i , and extending certain equations to multigroup.
Equations (14.40) become
Σg
tiV iXki
g (0) =
X
I
j=1
Pji
g
PG
g´=1(Σg´!g
sj
+ χgvΣg´
f )Xji
g´(0) + δjk
Σg
tj
;
g = 1; . . . ; G;
i; k = 1; . . . ; I
(14.45)
which can be written in matrix notation as
ViΣtiXki(0) =
X
I
j=1
[Pji
SFXji(0) + Pji];
i; j = 1; . . . ; I
(14.46)
and Eqs. (14.41) become
Σg
tiV iY g
i (0) =
X
I
j=1
Pji
g
PG
g´=1(Σg´!g
sj
+ χgvΣg´
f j)Y g´
j (0)
Σg
tj
+ γg
0i;
g = 1; . . . ; G;
i; j = 1; . . . ; I
(14.47)

<!-- page 550 (PDF 568) -->
which can be written in matrix notation as
ViΣtiY i(0) =
X
I
j=1
Pji
SFY j(0) + γ0i;
i = 1; . . . ; I
(14.48)
Equations (14.37) and (14.38), with the appropriate group cross probabilities,
can be used to correct the basic flux response functions Xki
g (0) and Y g
i (0) to
account for reflection from the surface SB, and the multigroup fluxes in each
region of the pin cell can be calculated from the multigroup version of
Eq. (14.35):
ϕg
i =
X
I
k=1
Qg
kXki
g (β) + j□g
ex Y g
i (β);
i = 1; . . . ; I
(14.49)

### Resonance Cross Sections

Homogenized resonance cross sections are calculated at the pin-cell level using
the methods discussed in Chapter 11.

### Full Assembly Transport Calculation

Once the finest level of heterogeneity has been homogenized with a series of pincell
calculations, the assembly is made up of a large number of homogeneous
regions (e.g., the square pin cells of Fig. 14.3), surrounded by structure, water
gaps, control rods, other dissimilar assemblies, and so on (i.e., the assembly is still
a heterogeneous medium embedded in a larger-scale heterogeneous medium, the
reactor core). The next step in the homogenization process is to perform a
multigroup transport calculation on the pin-cell homogenized assembly for the
purpose of obtaining average group fluxes for each homogenized pin cell that can
be used to calculate homogenized cross sections that will allow the entire
assembly to be represented as a homogenized region.
Any of the transport methods discussed in Chapter 9 (collision probabilities,
discrete ordinates, Monte Carlo) or even diffusion theory in some cases can be
used for the full assembly transport calculation. Such calculations are normally
performed using reflective conditions on the assembly boundary, or more
correctly on the boundary defined by the centerline of the water gap or other
medium separating adjacent assemblies, thus implicitly assuming an infinite array
of identical assemblies. The fact that different assemblies have different homogenized
properties is taken into account in the global core calculation based on a
homogenized assembly model that follows assembly homogenization. However,
the fact that the adjacent assembly is dissimilar or that there is a control rod
nearby or that there is significant leakage out of or into an assembly affects the
assembly calculation and hence the homogenized properties of the assembly.
Stratagems such as extending the boundaries for an assembly calculation into
adjacent assemblies or over a larger planar region have evolved for dealing with
this problem.

<!-- page 551 (PDF 569) -->
## 14.5 Homogenization Theory

When used in the calculation for which they were intended, homogenized cross
sections should yield a result that is equivalent, in some sense, to the result that
would have been obtained if the calculation could be performed with all the
spatial detail without the need for homogenization. It is useful, in this regard, to
develop homogenization procedures that would preserve the essential integral
properties of a global heterogeneous transport calculation, the result of which is
assumed known for the purpose of development of homogenization procedures,
and then to evaluate the homogenized cross sections using an approximation to
the global heterogeneous transport solution.

### Homogenization Considerations

The neutron flux distribution and effective multiplication constant, k, can be
described exactly by multigroup transport theory, which we write in the general
form:
∇?Jg(r) + Σg
t (r)ϕg(r)
= χg
k
X
G
g=1
vΣg´
f (r)ϕg´(r) +
X
G
g´=1
Σg´!g(r)ϕg´;
g = 1; . . . ; G
(14.50)
Imagine that we know the solution to Eq. (14.50) and wish to use it to define
homogenized cross sections that when used in the solution of the homogenized
transport equation
∇?^Jg(r) + ^Σ
g
t (r)^ϕg(r)
= χg^k
X
G
g´=1
v^Σ
g´
f (r)^ϕg´(r) +
X
G
g´=1
^Σ
g´!g ^ϕg´;
g = 1; . . . ; G
(14.51)
yield the same result for certain important quantities as would be obtained if the
detailed cross sections and the exact solution of Eq. (14.50) were used in their
evaluation (i.e., preserves certain properties of the exact solution). The most
important quantities to be preserved are the multiplication constant, k, the group
reaction rates averaged over the homogenization region, and the group currents
averaged over the surface of the homogenization region. Preservation of the last
two quantities requires that
∫V i
^Σ
g
x(r)^ϕg(r)dr = ∫V i
Σg
x(r)ϕg(r)dr
(14.52)
∫Sk
i
^Jg(r)?dS = ∫Sk
i
Jg(r)?dS
(14.53)

<!-- page 552 (PDF 570) -->
where Vi is the volume of the homogenization region i and Sk
i is the kth surface of
the homogenization region i. Satisfaction of Eqs. (14.52) and (14.53) would also
ensure preservation of k.
If the homogenized cross sections are uniform over the homogenization region,
an exact definition is
^Σ
g
xi ≡ ∫V i
Σg
X(r)ϕg(r)dr
∫V i
^ϕg(r)dr
(14.54)
and when diffusion theory is to be used in the homogenized calculation,
^D
g
ik ≡
□∫Sk
i
Jg(r) ? dS
∫Sk
i
∇^ϕg(r) ? dS
(14.55)
The practical difficulty in using Eqs. (14.54) and (14.55), of course, is that the
exact solution of the global transport equation is not known (and never will be,
or we would not be bothering with homogenization) and the homogenized
solution of the global diffusion equation is not known prior to solving
Eq. (14.51), which requires the homogenized group constants as input. Another
conceptual problem is that the integrals in Eq. (14.55) will generally be different
for each surface, k, so that it is not possible to define a constant value of the
homogenized diffusion coefficient which preserves the surface-averaged currents
over all the surfaces.

### Conventional Homogenization Theory

The conventional pin-cell or assembly homogenization procedure approximates
the solution to the global core transport equation, ϕg(r) and Jg(r), with the
solutions, ϕg
A(r) and Jg
A(r), to a pin-cell or assembly transport calculation, usually
with symmetry boundary conditions, n ? Jg
A(r) = 0. The numerator of Eq. (14.54) is
then evaluated using ϕg
A(r) instead of the (unavailable) exact global transport
solution ϕg(r). This assembly transport solution, ϕg
A(r), is also used to evaluate the
flux integral in the denominator of Eq. (14.54). A possible choice of the
homogenized diffusion coefficient is
^D
g
iA ≡ ∫V i
Dg(r)ϕg
A(r)dr
∫V i
ϕg
A(r)dr
(14.56)
