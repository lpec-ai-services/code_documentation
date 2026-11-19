# 12 Neutron Thermalization — 12.1 Double Differential Scattering Cross Section for Thermal Neutrons … 12.3 Thermal Neutron Scattering from Bound Nuclei
<!-- source PDF pages 488-496 -->

<!-- page 469 (PDF 488) -->
# 12 Neutron Thermalization

The thermalization of neutrons is complicated, relative to neutron slowing down,
by the fact that the thermal energies of the target nuclei are comparable to the
neutron energies, so that a neutron may gain or lose energy in a scattering
collision, and by the fact that the nuclei are generally bound in a lattice or
molecular structure, which considerably complicates both the calculation of a
scattering cross section and the scattering kinematics. The objectives of neutron
thermalization theory are first to calculate cross sections that characterize the
thermal neutron scattering and energy transfer and then to use these cross
sections in calculation of the thermal neutron spectrum. In this chapter, we
consider some approximate models of neutron thermalization that provide useful
physical insights, discuss the construction of thermal neutron scattering kernels,
and then discuss the analytical and numerical calculation of the neutron thermal
energy spectrum in homogeneous media and heterogeneous reactor lattices.

## 12.1 Double Differential Scattering Cross Section for Thermal Neutrons

A quantum mechanical analysis of the scattering event in which an incident
neutron interacts with an assembly of target nuclei of atomic mass A leads to an
expression of the differential scattering cross section for scattering from energy E´
to energy E and from direction Ω´ to direction Ω:
Σs(E´ ! E; μ0) =
Σb
4πkT
E
E´

1=2
exp □ β

S(α; β)
(12.1)
where μ0 = Ω´ ∙∙∙Ω, σb is the scattering cross section for a neutron incident on a
bound nucleus,
α ≡ E´ + E □ 2μ0
ffiffiffiffiffiffiffi
E´E
p
AkT
;
β ≡ E □ E´
kT
(12.2)
and S(α, β) is a scattering function that depends in a complicated way on the
detailed dynamics and structure of the scattering material. Hence,
Σb = Nσb = N
A + 1
A

σf =
A + 1
A

Σf
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 470 (PDF 489) -->
is the bound atom cross section, given in terms of the free atom cross section, P
f,
and the ratio of scattering to neutron masses, A.

## 12.2 Neutron Scattering from a Monatomic Maxwellian Gas

### Differential Scattering Cross Section

The simplest, but by no means simple, model of neutron thermalization is for
neutrons scattering from a monatomic gas of unbound nuclei distributed in energy
according to a Maxwellian distribution, for which the scattering function is
S(α; β) =
2(πα)1=2 exp □ α2 + β2
4α

(12.3)
which yields for the differential scattering cross section
Σs(E´ ! E; μ0) =
1 + 1
A

2 Σf
4π
E
E´

1=2
A
2πkTħ2κ2

1=2
□ exp □
A
2kTħ2κ2
ε □ ħ2κ2
2A

"
(12.4)
where A is the atomic mass (amu) of the target nuclei, σf is the total scattering
cross section for a neutron incident on a free nucleus, and
ε ≡ E´ □ E;
ħ2κ2 = 2m(E´ + E □ 2μ0
ffiffiffiffiffiffiffi
E´E
p
)
(12.5)
Integrating Eq. (12.4) over □1 ≤ μ0 ≤ 1 and using the relationship between μ0 and
(E, E´) for elastic scattering,
μ0 = 1
2 (A + 1)
ffiffiffiffi
E
E´
r
□ (A □ 1)
ffiffiffiffi
E´
E
r
"
(12.6)
yields for the zeroth Legendre moment of the scattering transfer function,
Σs0(E´ ! E) = Σf θ2
2E´
exp
E´
kT □ E
kT

□ erf
θ
ffiffiffiffiffiffi
E´
kT
r
□ η
ffiffiffiffiffiffi
E
kT
r
!
− erf
θ
ffiffiffiffiffiffi
E´
kT
r
+ η
ffiffiffiffiffiffi
E
kT
r
!
"
+ erf
θ
ffiffiffiffiffiffi
E
kT
r
□ η
ffiffiffiffiffiffi
E´
kT
r
!
□ erf
θ
ffiffiffiffiffiffi
E
kT
r
+ η
ffiffiffiffiffiffi
E´
kT
r
!)
(12.7)

<!-- page 471 (PDF 490) -->
where erf(x) is the error function and
θ ≡ A + 1
ffiffiffi
A
p
;
η ≡ A □ 1
ffiffiffi
A
p
(12.8)
The upper signs are used when E´ < E, and the lower signs are used when
E´ > E.

### Cold Target Limit

In the limit T →0, Eq. (12.7) reduces to the scattering transfer function for elastic
scattering from a stationary target,
Σs0(E´ ! E) =
Σf (E´)
E´
(A + 1)2
4A
; E < E´ < E
α
0;
otherwise
<
:
(12.9)
which was used in Chapter 10 for the treatment of neutron slowing down in the
energy range well above thermal where the nuclear motion is negligible compared
to the neutron motion.

### Free-Hydrogen (Proton) Gas Model

Hydrogen, in the form of water molecules, is a dominant nuclear species for
neutron thermalization in water-cooled nuclear reactors. The free-hydrogen gas
model neglects the fact that hydrogen is present in molecular form and treats the
thermalization of neutrons by a gas of free protons (hydrogen nuclei). For
scattering from hydrogen nuclei (A = 1), the zeroth Legendre moment of the
scattering energy transfer function of Eq. (12.7) simplifies to
Σs0(E´ ! E) =
ΣH
f (E´)
E´
exp E´ □ E
kT

erf
ffiffiffiffiffiffi
E´
kT
r
!
"
;
E´ < E
ΣH
f (E´)
E´
erf
ffiffiffiffiffiffi
E
kT
r
!
;
E´ > E
>
>
>
>
>
<
>
>
>
>
>
:
(12.10)

### Radkowsky Model for Scattering from H2O

The Radkowsky model uses the hydrogen gas model of Eq. (12.10) to describe the
zeroth Legendre moment of the scattering transfer function, and uses
Σs1(E´ ! E) = Σs(E)μ0(E)δ(E □ E´)
(12.11)

<!-- page 472 (PDF 491) -->
to describe the first Legendre moment. The bound-state cross section P
b is
related to the free-state cross section P
f by
Σs = Σb = Σf
[(A + 1)=A]2
(1 + 1=Amol)2 = 4Σf
Amol
Amol + 1

(12.12)
where A is the mass of an atom bound in a molecule of mass Amol and has been
set to unity in the last step to represent the hydrogen bound in water
molecules.
Application of this model is implemented by adjustment of Amol until P
b
agrees with an experimentally measured scattering cross section, as a
function of energy. Then μ0 = 2/(3Amol) is used to calculate P
tr(E) =
P
b(E)[1 □ μ0(E)].

### Heavy Gas Model

In the limit of large A, the scattering transfer function of Eq. (12.7) can be
expanded in powers of A□1. When only the leading term is retained, the
result is
Σs0(E´ ! E) = Σf
δ(E □E´)+
E
E´

1=2 E +E´
A
□ □δ´(E □E´)+kTδ´´(E □E´)
[
]
(
)
(12.13)
where δ´ and δ´´ are the first and second derivatives of the delta function with
respect to x. Integrating this expression over E defines the total scattering cross
section in this model:
Σs0(E) = Σf
1 + kT
2AE

(12.14)
Using Eq. (12.13) to evaluate the scatter-in integral yields
∫
dE´Σs0(E´ ! E)ϕ(E´) = 2Σf
A
kTEd2ϕ(E)
dE2
+Edϕ(E)
dE
+ϕ(E)

+Σs0(E)ϕ(E)
(12.15)
when the property of the derivatives of the delta functions
∫dx f (x) dn
dxn δ(x □ a) = (□1)n dnf (x = a)
dxn
(12.16)
is taken into account. Substituting this expression for the scatter-in integral into
the neutron balance equation
Σt(E)ϕ(E) = ∫
Σs0(E´ ! E)ϕ(E´)dE´
(12.17)

<!-- page 473 (PDF 492) -->
yields
Σa(E)ϕ(E) = 2 Σf
A
EkT d2ϕ(E)
dE2
+ E dϕ(E)
dE
+ ϕ(E)

(12.18)
which is the heavy gas model for the thermal neutron spectrum, ϕ(E).

## 12.3 Thermal Neutron Scattering from Bound Nuclei

The quantum mechanical theory for neutron scattering from a system of
bound nuclei leads to an expression for the double differential scattering
function for scattering from energy E´ to energy E and from direction Ω´ to
direction Ω:
Σs(E´ ! E; Ω´ ! Ω) = Σcoh
4πħ
ffiffiffiffi
E
E´
r
2π ∫
□1∫ei(κ ? r□εt=ħ)G(r; t)dr dt
+ Σinc
4πħ
ffiffiffiffi
E
E´
r
2π ∫
□1∫ei(κ ? r□εt=ħ)Gs(r; t)dr dt
(12.19)
where h̵ is the reduced Planck’s constant, h̵κ = m(ν´ □ ν) is the neutron momentum
exchange vector, ϵ = E´ □ E is the neutron energy change, and P
coh and P
inc
are the bound coherent and incoherent macroscopic cross sections. The coherent
scattering takes into account the interference of neutrons scattering from
different nuclei, which is important when the neutron wavelength λ (cm) = 2.86
× 10□9/(E(eV))1/2 is comparable with the spacing between atoms in a crystal or
molecule, and the incoherent scattering takes into account the scattering of
neutrons from isolated nuclei.

### Pair Distribution Functions and Scattering Functions

The functions G(r, t) and Gs(r, t) are pair distribution functions. If a scattering
target atom is at the origin r = 0 at time t = 0, then G(r, t) is the probability that
an atom will be present within unit volume dr about r at time t. G(r, t) = Gs
(r, t) + Gd (r, t), where Gs (r, t) is the probability that the atom present in dr about r
at time t is the same atom that was present at r = 0 at time t = 0, and Gd (r, t) is the
probability that a different atom is present in dr about r at time t. The integrals
involving the pair distribution functions in Eq. (12.19) are defined as the
scattering functions
S(κ; G) = 1
2π ∫
□1∫ei(κ ? r□εt=ħ)G(r; t)dr dt
(12.20)
with a similar definition for Ss in terms of Gs.

<!-- page 474 (PDF 493) -->
The principle of detailed balance requires that
M(E;T)
ffiffiffiffi
E´
E
r
[ΣcohS(□κ;□ε)+ΣincSs(□κ;□ε)] = M(E´;T)
ffiffiffiffi
E
E´
r
[ΣcohS(κ;ε)
+ΣincSs(κ;ε)]
(12.21)
be satisfied separately for the incoherent and coherent contributions. Recalling
that
M(E; T) = 2π
ffiffiffi
E
p
(πkT)3=2 exp □ E
kT

(12.22)
this detailed balance requirement may be written as
e□ε=2kTS(κ; ε) = eε=2kTS(□κ; □ε)
(12.23)
with a similar requirement for Ss, which requires that both S(κ, ϵ) and Ss(κ, ϵ) be
even functions of ϵ.
In many scattering models, S(κ, ϵ) is a function of κ2, and an equivalent
scattering function can be defined:
S(α; β) = kTeβ=2S(κ; ε) =
2(πα)1=2 exp □ α2 + β2
4α

(12.24)
where α and β are defined by Eq. (12.2). Using this scattering function, the double
differential scattering transfer function can be represented as
Σs(E´ ! E; Ω´ ! Ω) =
4πħkT
ffiffiffiffi
E
E´
r
e□β=2 ΣcohS(α; β) + ΣincSs(α; β)
[
]
(12.25)

### Intermediate Scattering Functions

An equivalent representation of the double differential scattering transfer
function is
Σs(E´ ! E; Ω´ ! Ω) = 1
4πħ
ffiffiffiffi
E
E´
r
2π ∫
□1
e□iεt=ħ χcoh(κ; t) + χinc(κ; t)

dt
(12.26)
where the intermediate scattering functions are defined:
χcoh(κ; t) ≡ ∫eiκ ? rG(r; t)dr
χinc(κ; t) ≡ ∫eiκ ? rGs(r; t)dr
(12.27)

<!-- page 475 (PDF 494) -->
### Incoherent Approximation

The interference effects, which are contained entirely in the pair distribution
function Gd, are important in elastic scattering, but are less important in inelastic
scattering, particularly in liquids and polycrystalline solids. This observation leads
to the incoherent approximation, obtained by setting Gd = 0 in Eq. (12.19):
Σs(E´ ! E; Ω´ ! Ω) = Σcoh + Σinc
4πħ
ffiffiffiffi
E
E´
r
2π ∫
□1
ei(κ ? r□εt=ħ)Gs(r; t)dr dt
(12.28)
Note that this approximation retains the coherent scattering cross section, P
coh.
With the incoherent approximation, S(α, β) = Ss(α, β) in Eq. (12.25) and χcoh = χinc
in Eq. (12.26).

### Gaussian Representation of Scattering

In the incoherent approximation, the intermediate scattering function has a
Gaussian form in many important cases:
χs(κ; t) = exp □ 1
2 κ2Λ(t)

(12.29)
where
Λ t + i
2T

= ∫
g(ω) coth ω
2kT □
cos ωt
sinh(ω=2kT)

 dω
ω
(12.30)
The properties of a particular moderator are represented in the frequency
distribution function, g(ω). For crystals, g(ω) is a true phonon frequency spectrum.
For liquids and molecules, g(ω) contains the diffusive and vibrational characteristics
and may be temperature dependent. Representative frequency distribution
functions are:
Perfect gas:
g(ω) = 1
A δ(ω)
Debye crystal:
g(ω) = 3ω2
Aθ3
Einstein crystal:
g(ω) = 1
A δ(ω □ θ)
Molecular liquid:
g(ω) = 1
A fd(ω) +
X
i
γiδ(ω □ ωi)
(12.31)
where θ = hνm/2πk h̵νm/k, νm is the maximum allowed frequency, fd(ω) describes
the frequency distribution associated with diffusive motion of the molecule, and
the γi δ(ω □ ωi) describe the internal vibrations with frequency ωi of the individual

<!-- page 476 (PDF 495) -->
atoms of which the molecular fluid is composed.
The corresponding scattering functions in the Gaussian representation are
Ss(α; β) = 1
2π ∫
□1
dt eiβtexp □αW 2(t)

(12.32)
where
W 2(t) = ∫
□1
g(β)[cosh(β=2) □ cos(kTβt=ħ)]dβ
β sinh(β=2)
(12.33)

### Measurement of the Scattering Function

The scattering transfer function can be determined from Eq. (12.25), in the
incoherent approximation, by measuring P
s(E´ →E, Ω´ →Ω). For small values of
neutron momentum transfer κ2 and energy transfer, the exponential in Eq. (12.32)
can be expanded to obtain a relation between the frequency distribution function
and the measured Ss(α, β)
f (β) = 2βsinh β
2 lim
α!0
Ss(α; β)
α
(12.34)
and noting that hω/2π = E´ □ E = βkT. Thus, by measuring the scattering double
differential cross section for small momentum and energy transfer events, the
scattering function Ss can be inferred and related to the frequency distribution.
This enables the experimental determination of g(ω), which can then be extrapolated
and used to calculate scattering transfer functions for larger energy and
momentum transfers.

### Applications to Neutron Moderating Media

The double differential scattering transfer function for water has been calculated
with a molecular liquid model in which the frequency distribution function is
given by
g(ω) = 1
18 +
X
i=2
Ai
δ(ω □ ωi)
(12.35)
where the first term represents the translational (diffusive) motion of free gas
molecules, the second term represents hindered rotation (A2 = 2.32, hω/2π =
0.06 eV), and the third and fourth terms represent vibrational modes with
(A3 = 5.84, hω/2π = 0.205 eV) and (A4 = 2.92, hω/2π = 0.481 eV), respectively.
This Nelkin distribution function was used to evaluate the scattering function
of Eq. (12.32), which was then used to evaluate the double differential scattering
transfer function of Eq. (12.1). The results are compared with experimental
measurements of the double differential scattering transfer function, for different

<!-- page 477 (PDF 496) -->
incident neutron energies, in Fig. 12.1. Also shown are results calculated with the
free-hydrogen gas model of Eq. (12.4).
The phonon frequency spectrum for graphite, based on two slightly different
models, is shown in Fig. 12.2. Specializing the incoherent approximation for the
double differential scattering transfer function of Eq. (12.28) to a crystal lattice
with cubic symmetry and harmonic interatomic forces yields
Σs(E´ ! E; Ω´ ! Ω) = Σb
4πħ
ffiffiffiffi
E
E´
r
2 ∫
□1
e□iεt=ħ
□ exp
ħκ2
2Am ∫
□1
f (ω)e□ħω=2κT
2ω sinh(ħω=2κT) (e□iωt □ 1)dω

dt
(12.36)
Using the Young–Koppel frequency distribution shown in Fig. 12.2 to evaluate
Eq. (12.36,) yields the inelastic cross section shown in Fig. 12.3. Adding to this, the
absorption cross section of graphite and an elastic scattering cross section
calculated without making the incoherent approximation, the total calculated
cross section for graphite is compared to measured values in Fig. 12.3. Here m is
the neutron mass.
100.0
0.212 eV
0.462 eV
1.0 eV
1.60 eV
(× 0.149)
(× 0.35)
(× 0.848)
(× 2.26)
2.20 eV
EXPERIMENTAL
NELKIN MODEL
GAS MODEL
10.0
1.0
0.1
σ f(Eʹ, Ωʹ→ Ω), BARNS/STERADIAN
SCATTERING ANGLE, θ
100 120 140 160 180
(× 5.95)
Fig. 12.1 Calculated and measured double differential scattering transfer functions in liquid
water at various incident neutron energies. (With permission from Ref. [1]. Copyright 1970,
Wiley.)
