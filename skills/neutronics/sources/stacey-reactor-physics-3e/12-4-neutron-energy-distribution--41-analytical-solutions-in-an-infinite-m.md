# 4 Neutron Energy Distribution — 4.1 Analytical Solutions in an Infinite Medium … 4.2 Multigroup Calculation of Neutron Energy Distribution in an Infinite Medium
<!-- source PDF pages 125-141 -->

<!-- page 101 (PDF 125) -->
# 4 Neutron Energy Distribution

Because the cross sections for neutron–nucleus reactions depend on energy, it is
necessary to determine the energy distribution of neutrons in order to determine
the rate of interactions of neutrons with matter, which in turn determines the
transport of neutrons. We first address this problem by considering the neutron
energy distribution in an infinite homogeneous medium, for which some analytical
results can be obtained to provide physical insight. Then the important
multigroup method for calculating an approximate neutron energy distribution is
described. Methods for dealing with the rapidly varying neutron energy distribution
in the energy range of cross-section resonances are described. Then the
multigroup calculation of the neutron energy distribution is combined with the
diffusion theory calculation of the spatial neutron distribution to obtain a
powerful method for calculating the space- and energy-dependent neutron
flux distribution in a nuclear reactor.

## 4.1 Analytical Solutions in an Infinite Medium

We start our investigation of the neutron energy distribution in a nuclear reactor
by considering an infinite homogeneous medium in which spatial effects may be
ignored. The neutron flux within a differential energy interval dE is determined by
a balance between the source of fission neutrons being created within dE plus
neutrons being scattered into dE from some other energy interval dE´ and the loss
of neutrons from within dE due to absorption and scattering from dE – into all
other energy intervals dE´´:
[Σa(E) + Σs(E)]ϕ(E)dE
=
∫
dE´Σs(E´ ! E)ϕ(E´) + χ(E)
k1 ∫
dE´vΣf (E´)ϕ(E´)

d E
(4.1)
where we have included the infinite medium multiplication constant that may be
adjusted to ensure that a steady-state solution exists.
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 102 (PDF 126) -->
### Fission Source Energy Range

At very high energies, the direct source of fission neutrons into dE is much larger
than the source of fission neutrons that have been created at higher energies and
are slowing down into dE, in which case the first term on the right in Eq. (4.1) can
be neglected in comparison to the second term, leading to
ϕ(0)(E) '
χ(E)
k1Σt(E) ∫
dE´vΣf (E´)ϕ(E´) = χ(E)
Σt(E) □ const:
(4.2)
where Σt = Σa + Σs. Thus, the neutron flux distribution at the higher energies,
where direct fission neutrons are the principal source, is proportional to the
fission spectrum divided by the total cross section.
This solution can be improved by using Eq. (4.2) as a first iterate on the right
side of Eq. (4.1) to evaluate
ϕ(1)(E) =
Σt(E) ∫
E
dE´Σs(E´ ! E)ϕ(0)(E´) + χ(E) □ const:

=
Σt(E) ∫
E
dE´Σs(E´ ! E) χ(E´)
Σt(E´) + χ(E)

□ const:
= χ(E)
Σt(E) □ const: 1+ 1
χ(E) ∫
E
dE´Σs(E´ ! E) χ(E´)
χt(E´)

(4.3)
where we have taken advantage of the fact that scattering of very energetic
neutrons with much less energetic nuclei will result in an energy loss for the
neutron to place a lower limit of E on the energies from which a neutron can
scatter into dE. At the higher energies, where the fission source is important,
inelastic scattering is also important and must be included in calculation of the
correction factor. The improved energy distribution is also of the form of the
fission spectrum divided by the total cross section times 1 plus a correction factor
that obviously becomes large at lower energies where χ(E) becomes small.
Numerical evaluation of the correction factor for typical compositions indicates
that ϕ(E) = χ(E)/Σt (E) represents the energy distribution rather well for energies
E>0.5 MeV.

### Slowing-Down Energy Range

Very few fission neutrons are produced with energy less than about 50 keV. There
is very little inelastic scattering in this energy range, so the elastic scattering
transfer function
Σs(E´ ! E) =
Σs(E´)
E´(1 	 α) ;
0;
E ≤ E´ ≤ E
α
otherwise
<
:
(4.4)

<!-- page 103 (PDF 127) -->
can be used, where α [(A 	 1)/(A + 1)]2 and A is the mass of the scattering nucleus
in amu. If we limit our attention further to neutron energies greater than only
about 1 eV, the neutrons will lose energy in a scattering collision, and we can write
the slowing-down equation for the neutron energy distribution
Σt(E)ϕ(E) =
X
j ∫
E=αj
E
dE´ Σj
s(E´)ϕ(E´)
E´(1 	 αj)
(4.5)
where the sum is over the various nuclear species present.

### Moderation by Hydrogen Only

Consider a mixture of hydrogen αH ≡ [(AH 	 1)/(AH + 1)]2 = 0 and very heavy
mass nuclei α ≡ [(A 	 1)/(A + 1)]2 ≈ 1, for which Eq. (4.5) becomes
Σt(E)ϕ(E) = ∫
E
ΣH
s ϕ(E´) dE´
E´ +
X
j ≠H ∫
E=αj
E
dE´ Σj
s(E´)ϕ(E´)
E´(1 	 αj)
' ∫
E
ΣH
s ϕ(E´) dE´
E´ +
X
j ≠H
αj
Σj
s(E)ϕ(E)
(4.6)
where the range of integration E < E´ < E/αj is so small for the heavy mass nuclei
that the approximation Σj
s(E´)ϕ(E´)/E´ ≈ Σj
s(E)ϕ(E)/E can be made. This equation
can be rearranged:
Σa(E) + ΣH
s

ϕ(E) = ∫
E
ΣH
s
ϕ(E´)
E´
dE´
(4.7)
Differentiating Eq. (4.7), dividing both sides by (Σa + ΣH
s )ϕ and integrating from E
to some arbitrary upper energy E1 leads to
ϕ(E) = [Σa(E1) + ΣH
s ]E1ϕ(E1)
[Σa(E) + ΣH
s ]E
exp 	∫
E1
E
Σa(E´)dE´
[Σa(E´) + ΣH
s ]E´

(4.8)
The neutron energy distribution varies with energy as ϕ(E) ∼1/(Σa(E) + ΣH
s ) E
and is exponentially attenuated in magnitude relative to the value at E1 by any
absorption that occurs over the interval E1 > E´ > E. The overall 1/E energy
dependence of the flux is modified by the energy dependence of Σa(E).

### Energy Self-Shielding

In particular, if a large narrow resonance is present, Σa(E) will increase sharply
over the range of the resonance, causing ϕ(E) ∼1/(Σa(E) + ΣH
s ) to dip sharply over

<!-- page 104 (PDF 128) -->
this range where the resonance cross section is large, as indicated in Fig. 4.1. At
energies just below the resonance, where Σa(E) becomes small again, the flux
recovers almost to the value just above the resonance, the difference being due to
the absorption in the resonance. Physically, only those neutrons that are scattered
into the energy range of the resonance will be absorbed, but those neutrons that are
scattered from energies above the resonance to energies below the resonance will
not be affected by the presence of the resonance. This reduction in the neutron flux
in the energy range of the resonance reduces the resonance absorption relative to
what it would be if the effect of the resonance on the flux was not present, a
phenomenon known as energy self-shielding.
We can obtain a rough estimate of the importance of energy self-shielding by
calculating the exponential attenuation due to the resonance under the simplifying
assumption that the resonance is very large over an energy width ΔE. Then the
attenuation factor can be approximated:
exp 	∫
E1
E
Σa(E´)dE´
[Σa(E´) + ΣH
s ]E´

' exp 	∫
E+ΔE
E
dE´
E´

=
E
E + ΔE
(4.9)
For the first large absorption resonance in 238U at E = 6.67 eV, the width of the
resonance is about ΔE = 0.027 eV, which would absorb only about 0.4% of the
neutrons slowing down past the resonance energy according to Eq. (4.9).

### Slowing Down by Nonhydrogenic Moderators with No Absorption

The case of slowing down by only hydrogen provides valuable physical insight
into features of the neutron energy distribution in the slowing-down energy
Φ(E)
Φ(E)
σ(E)
σ(E)
E
Fig. 4.1 Energy self-shielding of the neutron flux in a large absorption resonance. (With
permission from Ref. [1]. Copyright 1975, MIT Press.)

<!-- page 105 (PDF 129) -->
range, most notably ϕ ∼1/E and energy self-shielding of resonances, which
remains valid under other moderating conditions. To gain some insight into
the effect of various moderators on the neutron energy distribution, we now
consider the case of moderation by nonhydrogen isotopes, first in the absence of
absorption. The slowing-down balance equation is
Σs(E)ϕ(E) ≡
X
j
Σj
s(E)ϕ(E) =
X
j ∫
E=αj
E
dE´ Σj
s(E´)ϕ(E´)
(1 	 αj)E´
(4.10)
Guided by the result for slowing down from hydrogen, we look for a solution of
the form
ϕ(E) =
C
EΣs(E) =
C
EP
jΣj
s(E)
(4.11)
Substituting this into Eq. (4.10) leads to the identity
C
E =
X
j
C∫
E=αj
E
Σj
s(E´)
Σs(E´)
dE´
(1 	 αj)(E´)2 ' C
X
j
Σj
s
Σs
E = C
E
(4.12)
when it is assumed that the energy dependence of the scattering cross section is
the same for all isotopes present, establishing that a solution of the form of Eq.
(4.11) satisfies Eq. (4.10) under this assumption.

### Slowing-Down Density

The slowing-down density at energy E, q(E), is defined as the rate at which
neutrons are scattered from energies E´ above E to energies E´´ below E. With
reference to Fig. 4.2, this may be written as
q(E) ≡
X
j ∫
E=αj
E
dE´
∫
E
αjE´dE´´ Σj
s(E´)ϕ(E´)
E´(1 	 αj)
(4.13)
E/αj
dEʹ
dEʺ
E
Fig. 4.2 Energy intervals for neutron slowing-down density.

<!-- page 106 (PDF 130) -->
The maximum energy E´ from which a neutron may scatter elastically below E
is E/α, and the minimum energy E´´ of a neutron that scatters from an energy
E´ > E to an energy E´´ < E is E´´ = E´α. Without absorption, the slowing-down
density is obviously constant in energy.
Substituting Eq. (4.11) into Eq. (4.13) leads to
q(E) = P
j ∫
E=αj
E
dE´
∫
E
αjE´dE´´
CΣj
s(E´)
Σs(E´)(1 	 αj)(E´)2
= C P
j
1 + αj ln αj
1 	 αj

 Σj
s
Σs
≡ C
X
j
ξj
Σj
s(E)
Σs(E) ≡ Cξ(E)
(4.14)
where the assumption of a common energy dependence of all scattering cross
sections has been used again. The quantity ξj is the average logarithmic energy
loss in a collision with a nucleus of species j that was discussed in Chapter 1, and ξ
is the effective logarithmic energy loss for the mixture of moderators. Using this
result with Eq. (4.11) leads to the very important relationship between neutral
slowing-down density and neutron flux:
q(E) = ξ Σs(E)Eϕ(E)
(4.15)
where ξ is the scattering parameter defined by Eq. (1.24) and discussed in
Section 1.6.

### Slowing Down with Weak Absorption

Absorption removes neutrons from the slowing-down process and, thereby
reduces the slowing-down density as the energy decreases. Noting that decreasing
energy corresponds to 	dE, the change in slowing-down density due to absorption
is described by
dq(E)
dE
= Σa(E)ϕ(E)
(4.16)
Assuming weak absorption or localized (resonance) absorption near energy E,
so that the flux given by Eq. (4.15) can be used to evaluate the scattering-in
integral, the neutron balance equation yields a generalization of Eq. (4.15) for the
case of weak or resonance absorption
[Σa(E) + Σs(E)]ϕ(E) = P
j ∫
E=αj
E
dE´ Σj
s(E´)ϕ(E´)
E´(1 	 αj)
' q P
j ∫
E=αj
E
ξ(1 	 αj)
Σj
s(E´)
Σs(E´)
dE´
(E´)2 = q
ξE
(4.17)

<!-- page 107 (PDF 131) -->
where again the assumption of similar energy dependence of the scattering cross
sections for all species present has been used. Combining Eqs. (4.16) and (4.17) yields
dq(E)
dE
=
Σa(E)q(E)
Eξ[Σa(E) + Σs(E)]
(4.18)
which may be integrated from energy E up to some energy E1 to obtain
q(E) = q(E1)exp 	∫
E1
E
Σa(E´)dE´
ξ Σa(E´) + Σs(E´)
[
]E´

(4.19)
which describes the attenuation of the neutron slowing-down density due to
absorption. Making use of Eq. (4.17) yields an expression for the energy dependence
of the neutron flux
ϕ(E) = [Σa(E1) + Σs(E1)]ξ(E1)E1ϕ(E1)
[Σa(E) + Σs(E)]ξ(E)E
□ exp 	∫
E1
E
Σa(E´)dE´
ξ(E´)[Σa(E´) + Σs(E´)]E´

(4.20)
The neutron flux with nonhydrogenic moderators and weak or resonant absorptionhasanenergy
dependenceϕ ∼1/ξΣt(E)E and isexponentially attenuated,a result
very similar to that obtained for moderation by hydrogen only (Eq. (4.8) – note that
ξ = 1 for hydrogen). In particular, the energy self-shielding of resonances discussed
previously is contained in the 1/Σt (E) dependence of the neutron flux.

### Fermi Age Neutron Slowing Down

The assumption that the scattering cross sections of all moderating isotopes had
the same energy dependence, which was made to obtain a relatively simple
solution for slowing down by nonhydrogenic moderators, can be avoided in the
case of heavy moderators. The neutron balance equation for slowing down by a
mixture of moderators is
Σt(E)ϕ(E) =
X
j ∫
E=αj
E
dE´ Σj
s(E´)ϕ(E´)
E´(1 	 αj)
(4.21)
Based on the previous results, we expect that ξΣt(E)Eϕ is a slowly varying
function of E. Thus, we make a Taylor’s series expansion of Σj
s(E´)E´ϕ(E´) about
Σj
s(E)Eϕ(E):
E´Σj
s(E´)ϕ(E´) = EΣj
s(E)ϕ(E) +
d
d lnE EΣj
s(E)ϕ(E)

ln E´
E + ∙∙∙
(4.22)

<!-- page 108 (PDF 132) -->
in the scattering-in integrals on the right of Eq. (4.21). If the scattering-in
interval E/αj to E is small (i.e., if αj ≡ [(Aj 	 1)/(Aj + 1)]2 ≈ 1), it should be
sufficient to retain only the first two terms in the Taylor’s series expansion,
leading to
Σt(E)ϕ(E) = P
j ∫
E=αj
E
dE´
(E´)2(1 	 αj)
□
EΣj
s(E)ϕ(E) + ln E´
E
d
d lnE EΣj
s(E)ϕ(E)

+ ∙∙∙

= P
j
Σj
s(E)ϕ(E) + 1
E
1 + αjlnαj
1 	 αj

d
d ln E [EΣj
s(E)ϕ(E) + ∙∙∙

=
Σs(E)ϕ(E) + d
dE Eξ(E)Σs(E)ϕ(E)

+ ∙∙∙

(4.23)
which can be integrated to obtain
ϕ(E) = E1ξ(E1)Σs(E1)ϕ(E1)
Eξ(E)Σs(E)
exp 	∫
E1
E
Σa(E´)d E´
E´ξ(E´)Σs(E´)

(4.24)
This result for the energy distribution of the neutron flux is identical to the
result obtained in Eq. (4.20) when Σa ≪Σs, but obtained under quite different
assumptions. The assumptions in deriving Eq. (4.20) were that the absorption was
weak, so that the no-absorption relationship between the slowing-down density
and the flux could be used and that the energy dependence of the scattering cross
sections was the same for all moderators in the mixture, in order to evaluate the
scattering-in integrals. The only assumption in deriving Eq. (4.24) was that Σj
s(E´)
E´ϕ(E´) varied slowly over the scattering-in interval E to E/αj.
The important results we have obtained about the neutron energy distribution
in the slowing-down region are ϕ(E) ∼1/ξ(E)Σt(E)E, q ≈ ξ(E)Σt(E)Eϕ(E) and that
both the neutron slowing-down density q and the neutron flux ϕ are attenuated
exponentially by absorption during the slowing-down process. The expressions
that we have developed for this exponential attenuation are qualitatively correct,
but need to be refined to explicitly treat the resonance absorption that dominates
in the slowing-down region. We return to this in Section 4.3.

### Neutron Energy Distribution in the Thermal Range

Determination of the neutron energy distribution in the “thermal” range (E less
than 1 eV or so) is complicated by a number of factors. The thermal motion of
the nuclei is comparable to the neutron motion, with the consequences that the
cross sections must be averaged over the nuclear motion and that a scattering

<!-- page 109 (PDF 133) -->
event can increase, as well as decrease, the energy of the neutron. Since the
thermal neutron energy is comparable to the binding energy of nuclei in
material lattices, the recoil of the nucleus will be affected by the binding of
the nucleus in the lattice, and the neutron scattering kinematics is more
complex. Inelastic scattering in which the molecular rotational or vibrational
states or the crystal lattice vibration state is changed also affects the scattering
kinematics. At very low energies the neutron wavelength is comparable to the
interatomic spacing of the scattering nuclei, and diffraction effects become
important. Accurate calculation of thermal reaction rates requires both the
calculation of appropriate cross sections characterizing thermal neutron scattering
and calculation of the energy distribution of neutrons in the thermal
range. Fortunately, most of the complex details of thermal neutron cross
sections are not of great importance in nuclear reactor calculations, and
reasonable accuracy can be obtained with relatively simple models. In this
section we characterize the thermal neutron distribution and reaction rates
from relatively simple physical considerations. We return to a more detailed
discussion of thermal neutron cross sections and distributions in Chapter 12.
The neutron balance equation in the thermal energy range is
[Σa(E) + Σs(E)]ϕ(E) = ∫
Eth
d E´Σs(E´ ! E)ϕ(E´) + S(E)
(4.25)
where the scattering-in integral is from all energies in the thermal range E < Eth,
and S(E) is the source of neutrons scattered into the thermal energy range from
E > Eth. An equilibrium solution requires that the total number of neutrons downscattered
into the thermal energy range be absorbed, assuming for the moment no
leakage and no upscatter above Eth:
∫
Eth
d E Σs(E)ϕ(E) = q(Eth)
(4.26)
where q(Eth) is the neutron slowing-down density past Eth.
Consider the situation that would obtain if there were no absorption and
slowing-down source; that is, the neutron flux balance is
Σs(E)ϕ(E) = ∫
dE´ Σs(E´ ! E)ϕ(E´)
(4.27)
where we have extended the upper limit on the integral to infinity under the
assumption that the scattering to energies greater than Eth is zero. The principle
of detailed balance places the following constraint on the scattering transfer cross
section for a neutron distribution that is in equilibrium, regardless of the physical
details of the scattering event:
v´Σs(E´ ! E)M(E´; T) = vΣs(E ! E´)M(E; T)
(4.28)

<!-- page 110 (PDF 134) -->
where M(E, T) is the Maxwellian neutron distribution
M(E; T) =
2π
(πkT)3=2
ffiffiffi
E
p
exp 	 E
kT

(4.29)
It can be shown that the Maxwellian neutron flux distribution,
ϕM(E; T) = nv(E)M(E) =
2πn
(πkT)3=2
m

1=2
E exp 	 E
kT

≡ ϕT
E
(kT)2 exp 	 E
kT

(4.30)
satisfies Eq. (4.27). Thus, the principal of detailed balance is sufficient to
ensure that the equilibrium neutron distribution, in the absence of absorption,
leakage, or sources, is a Maxwellian distribution characterized by the temperature
T of the medium (i.e., the neutrons will come into thermal equilibrium
with the moderator nuclei). The most probable energy of neutrons in a
Maxwellian distribution is kT, and the corresponding neutron speed is
vT = (2kT/m)1/2.
However, absorption, leakage, and a slowing-down source will distort the
actual neutron distribution from a Maxwellian. Since most absorption cross
sections vary as 1/v = 1/(E)1/2, absorption preferentially removes lower energy
neutrons, effectively shifting the neutron distribution to higher energies than a
Maxwellian at the moderator temperature T. A shift to higher energies can be
represented approximately by a Maxwellian distribution with an effective “neutron
temperature”
Tn = T
1 + CΣa
ξ Σs

(4.31)
where C must be determined experimentally. Leakage can be represented by
modifying the absorption cross section to Σa →Σa + DB2. Since D = 1/3Σtr,
leakage will preferentially remove higher energy neutrons, offsetting the effect
of absorption to some extent.
In the slowing-down region E > Eth, the neutron flux distribution is 1/E, and the
slowing-down source into the upper part of the thermal energy range will tend to
make the flux 1/E. Thus, the hardened Maxwellian must be corrected by the
addition of a joining term Δ that is about unity for values of E/kTn > 10 and
vanishes for values of E/kTn < 5:
ϕ(E) = ϕM(E; Tn) + λ Δ(E=kTn)
E
(4.32)

<!-- page 111 (PDF 135) -->
where λ is a normalization factor
λ = ϕT
ffiffiffi
π
p
=2)
1 	 ξ Σs=Σa
(4.33)
The Maxwellian distribution has some useful properties insofar as calculation
of the neutron absorption rate in the thermal energy range is concerned. Most
absorption cross sections are 1/v; that is,
Σa(E; T) = Σ0
a
v = Σa(E0)v0
v
(4.34)
where E0 = kT = 0.025 eV and v0 = (2kT/mn)1/2 = 2200 m/s. The total absorption
rate integrated over the thermal energy range is
Ra = ∫
Eth
d EΣa(E; T)vnM(E; Tn) = Σa(E0)v0n0 ≡ Σa(E0)ϕ0
(4.35)
The quantity ϕ0 = nv0 is the 2200 m/s flux, which when multiplied by the cross
section evaluated at E = 0.025 eV yields the total absorption rate integrated over
the thermal energy range. Most thermal data compilations include the 2200 m/s
value of the cross section (see Appendix A). From the definitions of ϕT = (2/π1/2)
nv (Eq. (4.30)) and of ϕ0 = nv0, the appropriate thermal group absorption cross
section (the quantity that is multiplied by the integral of the neutron flux over the
thermal energy range to recover Ra) for a 1/v absorber in a Maxwellian neutron
distribution at neutron temperature Tn is
Σth
a =
ffiffiffi
π
p
T0
Tn

1=2
Σa(E0)
(4.36)
Non-1/v correction factors have been developed to correct this expression for
absorbers that are not 1/v.

### Summary

The fission spectrum divided by the total cross section, ϕ(E) = χ(E)/Σt(E), represents
the energy distribution rather well for energies E > 0.5 MeV. In the slowingdown
range below the fission spectrum, E < 50 keV, and above the thermal range,
E > 1 eV, ϕ(E) ∼1/ξ(E)Σt(E)E represents the neutron energy distribution. In
the thermal range, E < 1 eV, a hardened Maxwellian plus a 1/E correction at
higher energies, ϕ(E) = ϕM(E, Tn) + λΔ(E/kTn)/E, represents the neutron energy
distribution.

<!-- page 112 (PDF 136) -->
## 4.2 Multigroup Calculation of Neutron Energy Distribution in an Infinite Medium

### Derivation of Multigroup Equations

While the neutron energy dependences derived in Section 4.1 provide a qualitative
, even semiquantitative description of the neutron energy distribution in
nuclear reactors, the multigroup method is widely used for the quantitative
calculation of the neutron energy distribution. As we will see, the qualitative
results of Section 4.1 will provide valuable insight as to the choice of weighting
functions to be used in the preparation of multigroup constants.
To develop a multigroup calculational method for the energy distribution, we
divide the energy interval of interest, say 10 MeV down to zero, into G intervals, or
groups, as indicated in Fig. 4.3. The equation describing the neutron energy
distribution in a very large homogeneous region of a nuclear reactor (where
spatial and leakage effects may be neglected) is
[Σa(E) + Σs(E)]ϕ(E)
= ∫
dE´Σs(E´ ! E)ϕ(E´) + χ(E)
k1 ∫
dE´ vΣf (E´)ϕ(E´)
(4.37)
This equation can be integrated over the energy interval Eg < E < Eg	1 of group g
to obtain
∫
Eg	1
Eg
dE[Σa(E) + Σs(E)]ϕ(E)
= ∫
Eg	1
Eg
dE
X
G
g´=1∫
Eg´	1
Eg´
dE´Σs(E´ ! E)ϕ(E´)
+ 1
k1 ∫
Eg	1
Eg
dEχ(E)
X
G
g´=1∫
Eg´	1
Eg´
dE´vΣf (E´)ϕ(E´)
(4.38)
E0 = 10 MeV
E1
Eg-1
E9+1
EG-1
EG = 0
Eg
Fig. 4.3 Multigroup energy structure.

<!-- page 113 (PDF 137) -->
where we have made use of the fact that the sum of integrals over the groups is
equal to the integral over 0 < E < 1. Defining the integral terms in Eq. (4.38) in a
natural way,
ϕg ≡ ∫
Eg	1
Eg
dE ϕ(E);
χg ≡ ∫
Eg	1
Eg
dEχ(E)
Σg
a ≡
∫
Eg	1
Eg
dE Σa(E)ϕ(E)
ϕg
;
vΣg
f ≡
∫
Eg	1
Eg
dE vΣf (E)
ϕg
Σg´!g
s
≡
∫
Eg	1
Eg
dE∫
Eg´	1
Eg´
dE´Σs(E´ ! E)ϕ(E´)
ϕg´
;
Σg
s ≡
X
G
g´=1
Σg!g´
s
(4.39)
Eq. (4.38) can be written as
(Σg
a + Σg
s)ϕg =
X
G
g´=1
Σg´!g
s
ϕg´ + χg
k1
X
G
g´=1
vΣg´
f ϕg´;
g = 1; ∙∙∙; G
(4.40)
Equations (4.40) are the multigroup neutron spectrum equations for an infinite
medium, one in which spatial and leakage effects are unimportant. There are G
equations and G unknowns, the group fluxes ϕg, so the problem is well posed.
This overlooks the fact that the group constants Σg depend on the neutron flux
and hence are also unknown. Actually, the group constants depend only on the
energy dependence of the neutron flux within the group, not on the magnitude of
the neutron flux, which appears in both the numerator and denominator of the
definition of the group constants. In practice, some assumption is made about this
energy dependence, so that the group constants are known. From the results of
the preceding section, we have a pretty good idea about the energy dependence of
the neutron flux in the fission, slowing down, and thermal energy ranges, which
can be used to evaluate group constants.
Summing Eqs. (4.40) over groups yields
k1 =
ΣG
g=1vΣg
f ϕg
ΣG
g=1Σg
aϕg
(4.41)
which identifies k1 as the ratio of the total neutron production rate by fission to
the total neutron absorption rate, in accord with our previous discussion of the
multiplication constant.

<!-- page 114 (PDF 138) -->
### Mathematical Properties of the Multigroup Equations

The set of equations (4.40) may be written in matrix notation as
Aϕ 	 1
k1
Fϕ =
A 	 1
k1
F

ϕ = 0
(4.42)
where A and F are G × G matrices and ϕ is a G-element column vector:
A =
Σ1
a + Σ1
s 	 Σ1!1
s
	Σ2!1
s
	Σ3!1
s
. . .
	ΣG!1
s
	Σ1!2
s
Σ2
s + Σ2
s 	 Σ2!2
s
	Σ3!2
s
. . .
	ΣG!2
s
..
.
..
.
..
.
..
.
..
.
	Σ1!G
s
	Σ2!G
s
	Σ3!G
s
. . .
ΣG
a + ΣG
s 	 ΣG!G
s
F =
χ1vΣ1
f
χ1vΣ2
f
χ1vΣ3
f
. . .
χ1vΣG
f
χ2vΣ1
f
χ2vΣ2
f
χ2vΣ3
f
. . .
χ2vΣG
f
..
.
..
.
..
.
..
.
..
.
χGvΣ1
f
χGvΣ2
f
χGvΣ3
f
. . .
χgvΣG
f
;
ϕ =
ϕ1
ϕ2
..
.
ϕG
(4.43)
Note that the scattering terms on the diagonal are of the form Σg
s 	 Σg!g
s
,
leading to the concept of a removal cross section Σg
r ≡ Σg
a + Σg
s 	 Σg!g
s
to represent
the net loss of neutrons from group g by absorption plus scattering.
Equations (4.40) or (4.42) are homogeneous equations and thus, by Cramer’s
rule, have nontrivial solutions only if the determinant of the coefficient matrix
vanishes:
det A 	 1
k1
F

= 0
(4.44)
This condition defines an eigenvalue problem for the determination of k1 –
there are only a certain set of G discrete values of k1 for which a nontrivial
solution exists. (Note that we have included k1 in the formulation for just this
reason. If we had not included k1, Eq. (4.44) would be a requirement on the
composition of the reactor for criticality, and we would be faced with the
cumbersome requirement to adjust the composition by trial and error until
Eq. (4.44) was satisfied.)

<!-- page 115 (PDF 139) -->
It is possible to prove that the inverse of the matrix A exists for any physically
real set of cross sections and number densities. Multiplying Eq. (4.42) by k1A	1
yields
k1ϕ = A	1Fϕ
(4.45)
which is the standard form for a matrix eigenvalue problem. It is possible to prove
(e.g., Refs. [2, 3, and 4]) for this equation that (1) there is a unique real, positive
eigenvalue greater in magnitude than any other eigenvalue; (2) all of the elements –
the group fluxes – of the eigenvector corresponding to this largest eigenvalue are
real and positive; and (3) the eigenvectors corresponding to all other eigenvalues
have zero or negative elements. Thus, the largest value of k1 for which Eq. (4.44) is
satisfied is real and positive and the associated group fluxes given by Eq. (4.45) are
real and positive (i.e., physical).

### Solution of Multigroup Equations

The multigroup equations have been written in their full generality, allowing
upscatter (the terms above the diagonal in A) as well as downscatter (the terms
below the diagonal in A) and a fission spectrum contribution in every group. In
fact, upscatter takes place only for those groups that are in the thermal energy
range E ≲1 eV, and the fission spectrum contributes only to the higher energy
groups E ≳50 keV. Taking these physical considerations into account greatly
simplifies solution of the multigroup equations.
Consider, as the simplest example of a multigroup description, the representation
of the neutrons in a nuclear reactor as being either in a thermal group
(E ≲1 eV) or in a fast group (E ≳1 eV). All of the fission neutrons are deposited in
the fast group, and there is no upscatter from the thermal to the fast group. The
two-group equations are
(Σ1
a + Σ1!2
s
)ϕ1 = 1
k1
(vΣ1
f ϕ1 + vΣ2
f ϕ2)
Σ2
aϕ2 = Σ1!2
s
ϕ1
(4.46)
which may readily be solved for
ϕ1 = Σ2
a
Σ1!2
s
ϕ2;
k1 =
vΣ1
f + (Σ1!2
s
=Σ2
a)vΣ2
f
Σ1
a + Σ1!2
a
(4.47)
Note that a critical reactor may operate at many power levels, so the absolute
magnitude of the group fluxes quite properly cannot be determined by the set of
homogeneous multigroup equations, but the relative magnitudes of the different
group fluxes can be determined.
A somewhat better multigroup description results from representing the
fission interval (E > 50 keV) as a fast group into which all fission neutrons are

<!-- page 116 (PDF 140) -->
introduced, the slowing-down interval (50 keV > E > 1 eV) as an intermediate
group, and the thermal region (E < 1 eV) as a thermal group. There would be no
upscattering in such a group structure, allowing the three-group equations to be
written
(Σ1
a + Σ1!2
s
+ Σ1!3
s
)ϕ1 = 1
k1
(vΣ1
f ϕ1 + vΣ2
f ϕ2 + vΣ3
f ϕ3)
(Σ2
a + Σ2!3
s
)ϕ2 = Σ1!2
s
ϕ1
Σ3
aϕ3 = Σ1!3
s
ϕ1 + Σ2!3
s
ϕ2
(4.48)
with solutions
ϕ2 = [Σ1!2
s
=(Σ2
a + Σ2!3
s
)]ϕ1;
ϕ3 =
Σ1!3
s
+
Σ2!3
s
Σ2
a + Σ2!3
s
Σ1!2
s

Σ2
a

ϕ1
k1 =
vΣ1
f + vΣ2
f
Σ1!2
s
Σ2
a + Σ2!3
s

+vΣ3
f
Σ1!3
s
+
Σ2!3
s
Σ2
a + Σ2!3
s
Σ1!2
s

(Σ1
a + Σ1!2
s
+ Σ1!3
s
)
(4.49)
Example 4.1 Two-Group Fluxes and k1
A representative set of two-group
cross sections for a PWR fuel assembly are (Σ1!2
s
= 0.0241 cm	1, Σ1
a = 0.0121 cm	1,
vΣ1
f = 0.0085) and (Σ2
a = 0.121 cm	1, vΣ2
f = 0.185). From Eq. (4.47,) the fast/thermal
flux
ratio
is
ϕ1/ϕ2 = 0.121/0.241 = 5.02,
and
k1 = (0.0085 + 0.185/5.02)/
(0.0121 + 0.0241) = 1.253. The spectrum-averaged one-group absorption cross
section is Σa = (Σ1
aϕ1 + Σ2
aϕ2)/(ϕ1 + ϕ2) = 0.0302 cm	1.

### Preparation of Multigroup Cross-Section Sets

There exist in the world several sets of evaluated nuclear data (e.g., Refs [5 and 6]),
which have been both checked for consistency and benchmarked extensively in
the calculation of experiments designed for data testing. Representation of the
cross-section data in such data files is generally as follows:
1) σ(Ei) are tabulated pointwise in energy at low energies below the resonance
region.
2) Resolved resonance parameters and background cross sections in the resolved
resonance region.
3) Unresolved resonance statistical parameters and background cross section in
the unresolved resonance region.

<!-- page 117 (PDF 141) -->
4) σ(Ei) are tabulated pointwise in energy at energies above the resonance region.
5) Scattering transfer functions p(Ei, μs) are tabulated pointwise in energy and
either pointwise in angle (μsj) or as Legendre coefficients.
The resonance parameters and the construction of multigroup cross sections
from them are discussed in Section 4.3 and in Chapter 11.
The scattering transfer function – the probability that a neutron will undergo a
scattering event which changes its direction from direction Ω to direction Ω´
(μs = Ω □ Ω´) and its energy from E to E´ – is represented as
σs(μs; E ! E´) = m(E)σs(E)p(E; μs) g(μs; E ! E´)
(4.50)
where m(E) = 1 for elastic and inelastic scattering, 2 for (n, 2n), ν for fission; p(E,
μs) is the angular distribution for scattering of a neutron of energy E; and g(μs,
E →E´) is the final energy distribution of a neutron at energy E that has scattered
through μs. When the scattering angle and energy loss are correlated, as they are
for elastic scattering, E´/E = [(1 + α) + (1 	 α) cos θ]/2 and g(μs, E →E´) = δ(μs
μ(E, E´)). Otherwise, g(μsi; Ej ! E´k) is tabulated. The angular distribution may be
tabulated as p(Ei, μsj), or the Legendre components may be tabulated pointwise in
energy
pn(Ei) = ∫
dμsPn(μs)p(Ei; μs)
(4.51)
where Pn is the Legendre polynomial.
There are a number of codes (e.g., Refs [7, 8, and 9]) that directly process the
evaluated nuclear data files to prepare multigroup cross sections. These codes
numerically calculate integrals of the type
σg
=
∫
Eg	1
Eg
dEσ(E)W(E)
∫
Eg	1
Eg
dE W(E)
σg!g´
n
= ∫
Eg!1
Eg
dEσs(E)W(E)∫
Eg´	1
Eg´
dE´ pn(E´)=∫
Eg!1
Eg
dEW(E)
(4.52)
for a specified weighting function, W(E), which may be a constant, 1/E, χ(E), and
so on. These codes are used to calculate fine-group cross sections in a few hundred
groups for thermal reactors or ultrafine-group cross sections in a few thousand
groups for fast reactors. These fine- or ultrafine-group structures are chosen such
that the results of calculations using the fine- or ultrafine-group cross sections are
essentially independent of the choice of weighting function, W(E), used in the
cross-section preparation.
