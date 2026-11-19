# 4 Neutron Energy Distribution — 4.3 Resonance Absorption … References
<!-- source PDF pages 142-160 -->

<!-- page 118 (PDF 142) -->
Once the fine- or ultrafine-group cross sections are prepared, a fine- or ultrafinegroup
spectrum (ϕg) is calculated for a representative homogenized medium. The
unit cell heterogeneous structure of the region must be taken into account in
homogenizing the medium. Resonances must be treated specially, as discussed in
Chapter 11. This fine- or ultrafine-group spectrum can then be used to weight the
fine- or ultrafine-group cross sections to obtain few-group (2–10) cross sections for
thermal reactors or many-group (20–30) cross sections for fast reactors:
σk
= Σg ∈kσgϕg
Σg ∈kϕg
σk!k´
n
= Σg ∈kΣg´ ∈k´σg!g´
n
ϕg
Σg ∈kϕg
(4.53)
The notation g ∈k indicates that the sum is over all fine or ultrafine groups g
within few or many group k.
The few- or many-group cross sections may be calculated for several different
large regions in a reactor. They are then used in a few- or many-group diffusion or
transport theory calculation of the entire reactor to determine the effective
multiplication constant, power distribution, and so on. Because many such
calculations must be made, a number of parameterizations of few- and manygroup
cross sections have been developed (e.g., Ref. [10]) to avoid the necessity of
making the fine- or ultrafine-group spectrum calculation numerous times.

## 4.3 Resonance Absorption

### Resonance Cross Sections

When the relative (center-of-mass) energy of an incident neutron and a nucleus
plus the neutron binding energy match an energy level of the compound nucleus
that would be formed upon neutron capture, the probability of capture is quite
large. The lowest-energy excited states are only a fraction of 1 eV above the
ground state and extend up to about 100 keV for heavy mass fuel nuclei (fissile
and fertile), but start at about 10 eV for intermediate mass nuclei and at about
10 keV for lighter mass nuclei. The heavier mass isotopes have many relatively low
energy excited states, which give rise to resonances in the neutron absorption and
scattering cross sections (Fig. 4.4).
The neutron resonance absorption phenomena constitute one of the most
fundamental subjects in nuclear reactor physics. One of the most effective means
of treating these phenomena is in terms of the resonance integral concept, which
has a fundamental premise that the resonance cross sections are representable by
superposition of many Breit–Wigner resonances with known parameters. This
premise allows the complex resonance structure to be characterized in a
reasonably simple way by calculating the contributions of each individual resonance
. The discussion in this section concentrates on s-wave neutron cross
sections in the low-energy range.

<!-- page 119 (PDF 143) -->
As shown in Chapter 1, the (n, γ) capture cross section averaged over the
motion of the nucleus is given by
σγ(E; T) = σ0
Γγ
Γ
E0
E

1=2
ψ(ξ; x)
(4.54)
and the total scattering cross section, including resonance and potential scattering
and interference between the two, can be written
σs(E; T) = σ0
Γn
Γ ψ(ξ; x) + σ0R
λ0
χ(ξ; x) + 4πR2
(4.55)
where R is the nuclear radius, λ0 the neutron DeBroglie wavelength, the functions
ψ(ξ; x) =
ξ
ffiffiffi
π
p ∫
e	1=4(x	y)2ξ2
dy
1 + y2
(4.56)
χ(ξ; x) = ξffiffiffi
π
p ∫
e	1=4(x	y)2ξ2 y dy
1 + y2
(4.57)
are integrals over the relative motion of the neutron and nucleus, x = 2(E 	 E0)/Γ,
it has been assumed that the nuclear motion can be characterized by a Maxwellian
10-3
10-2
10-1
Cross Section (barns)
Neutron Energy (eV)
Fig. 4.4 238U capture cross section. (From www.nndc.bnl.gov/.)

<!-- page 120 (PDF 144) -->
distribution with temperature T, and E is the energy of the neutron in the lab
system. The parameters characterizing the resonance are σ0, the peak value of the
cross section; E0, the neutron energy in the center-of-mass system at which it
occurs; Γ, the resonance width; Γγ, the partial width for neutron capture; Γf, the
partial width for fission; and Γn, the partial width for scattering. The resonance
occurs when the center of mass energy Ecm = (A/(A + 1))E plus the change in
binding energy upon neutron capture equals the energy above ground state of an
excited level of the compound nucleus.

### Doppler Broadening

The temperature characterizing the nuclear motion is contained in the parameter
ξ =
Γ
(4E0kT=A)1=2
(4.58)
where A is the atomic mass (amu) and k is the Boltzmann constant. The general
dependence of the ψ-function on temperature is indicated in Fig. 4.5. As the
temperature increases, the peak magnitude of ψ at E0 decreases and the
magnitude away from peak increases. This broadening of the cross section
is known as Doppler broadening. It can be shown that the area under the curve
of the ψ-function remains constant as the temperature changes. Similar
behavior results for the χ-function. The ψ- and χ-functions are tabulated in
Tables 4.1 and 4.2.
The assumption that the nuclear motion can be characterized by a Maxwellian
is only approximately correct for atoms bound in a crystalline state. Investigation
E0
E
T3
T2
T1
T1 < T2 < T3
σ (E, T)
Fig. 4.5 Temperature broadening of the ψ-function. (With permission from Ref. [11].
Copyright 1976, Wiley.)

<!-- page 121 (PDF 145) -->
of this point indicates that a Maxwellian is a good approximation, but with a
slightly higher temperature which corresponds to the average energy per vibrational
degree of freedom of the lattice, including the zero-point energy. In
practice, the actual material temperature is widely used.
Table 4.1 ψ-Function
x
ξ
0.5
0.05 0.043 09 0.043 08 0.043 06 0.042 98 0.042 67 0.042 16 0.041 45 0.040 55 0.033 80 0.016 39
0.10 0.083 84 0.083 79 0.083 64 0.083 05 0.080 73 0.077 00 0.072 08 0.066 23 0.032 91 0.002 62
0.15 0.122 39 0.122 23 0.121 76 0.119 89 0.112 68 0.101 65 0.088 05 0.073 28 0.016 95 0.000 80
0.20 0.158 89 0.158 54 0.157 48 0.153 31 0.137 77 0.115 40 0.090 27 0.066 14 0.007 13 0.000 70
0.25 0.193 47 0.192 81 0.190 86 0.183 24 0.155 84 0.119 34 0.082 77 0.052 53 0.003 94 0.000 67
0.30 0.226 24 0.225 16 0.221 97 0.209 68 0.167 29 0.115 71 0.070 42 0.038 80 0.003 14 0.000 65
0.35 0.257 31 0.255 69 0.250 91 0.232 71 0.172 88 0.107 13 0.057 24 0.028 15 0.002 89 0.000 64
0.40 0.286 79 0.284 50 0.277 76 0.252 45 0.173 59 0.096 04 0.045 66 0.021 09 0.002 77 0.000 64
0.45 0.314 77 0.311 68 0.302 61 0.269 09 0.170 52 0.084 39 0.036 70 0.016 87 0.002 70 0.000 64
0.50 0.341 35 0.337 33 0.325 57 0.282 86 0.164 69 0.073 46 0.030 25 0.014 46 0.002 66 0.000 63
Source: Data from Ref. [11]; used with permission of Wiley.
Table 4.2 χ-Function
x
ξ
0.5
0.05
0.001 20
0.002 39
0.004 78
0.009 51
0.014 15
0.018 65
0.022 97
0.040 76
0.052 21
0.10
0.004 58
0.009 15
0.018 21
0.035 73
0.051 92
0.066 26
0.078 33
0.101 32
0.059 57
0.15
0.009 86
0.019 68
0.038 94
0.074 70
0.104 60
0.126 90
0.140 96
0.122 19
0.053 41
0.20
0.016 80
0.033 44
0.065 67
0.122 19
0.162 95
0.185 38
0.190 91
0.117 54
0.051 70
0.25
0.025 15
0.049 94
0.097 14
0.174 13
0.219 09
0.231 68
0.220 43
0.110 52
0.051 03
0.30
0.034 70
0.068 73
0.132 19
0.226 94
0.267 57
0.262 27
0.231 99
0.106 50
0.050 69
0.35
0.045 29
0.089 40
0.169 76
0.277 73
0.305 64
0.278 50
0.232 36
0.104 37
0.050 49
0.40
0.056 74
0.111 60
0.208 90
0.324 42
0.332 86
0.284 19
0.227 82
0.103 16
0.050 37
0.45
0.068 90
0.134 98
0.248 80
0.365 63
0.350 33
0.283 51
0.222 23
0.102 38
0.050 28
0.50
0.081 65
0.159 27
0.288 75
0.400 75
0.359 98
0.279 79
0.217 29
0.101 85
0.050 22
Source: Data from Ref. [11]; used with permission of Wiley.

<!-- page 122 (PDF 146) -->
### Resonance Integral

The total absorption rate per nuclei by a resonance absorber is known as the
resonance integral,
Iγ = ∫σγ(E)ϕ(E)dE
(4.59)

### Resonance Escape Probability

The absorption probability for a single resonance depends on the balance
between absorption and moderation and is given by Rabs = Nres I/q0, where
q0 = ξΣsEϕasy is the asymptotic slowing-down density above the resonance and
Nres is the number density of the resonance absorber. If we use ϕasy = 1/E to
evaluate the resonance integral, then Rabs = I/ξσs, where the denominator is the
moderating power per absorber nucleus. The resonance escape probability is
p = 1 	 Rabs = 1 	 I/ξσs ≈ exp(	I/ξσs), where Rabs is assumed small for any one
resonance. The quantity σs = (Nresσres
s
+ Nnonσnon
s
)=Nres is the effective scattering
cross section per resonance absorbing atom, including both the resonance and
nonresonance species present.
The total resonance integral for all resonances is a sum over the individual
resonance integrals, and the total resonance escape probability is
p = ∏
i
pi = exp 	 1
ξσs
X
i
Ii
!
(4.60)
where immediately above only ξ is average scattering parameter defined by Eq.
(1.24) and discussed in Section 1.6.

### Multigroup Resonance Cross Section

The resonances within a given energy group in a multigroup treatment can be
treated as a group capture cross section given by
σg
γ =
∫
Eg	1
Eg
dEσγ(E)ϕ(E)
∫
Eg	1
Eg
dEϕ(E)
=
Σi ∈gIi
ln(Eg	1=Eg)
(4.61)
where ϕ(E) ∼1/E has been used.

### Practical Width

The practical width of a resonance is defined as the energy range over which the
resonance cross section is larger than the nonresonance part of the cross section

<!-- page 123 (PDF 147) -->
of the resonance nuclide, which from the Breit–Wigner formula is
Γp '
ffiffiffiffiffiffiffiffiffiffi
σ0
4πR2
r
Γ =
ffiffiffiffiffi
σ0
σp
r
Γ
(4.62)
Typically, for low-energy resonances σ0/4πR2 ≡ σ0/σp ∼103, so the practical width
is much larger than the total width. The practical width provides a measure of the
range of influence of the resonance, which we will see is important in evaluating
the neutron flux in the resonance.

### Neutron Flux in Resonance

The resonance region is well below the fission spectrum, so the neutron balance
in the vicinity of the resonance can be written
Σres
t (E) + ΣM
s

ϕ(E) = ∫
E=αM
E
dE´
E´
ΣM
s ϕ(E´)
1 	 αm
+ ∫
E=αres
E
dE´
E´
Σres
s (E´)ϕ(E´)
1 	 αres
(4.63)
where the moderator scattering cross section is assumed to be much larger than
its absorption cross section and to be effectively constant. The practical width
of the resonance will generally be much less than the scattering-in interval of
the moderator, Γp ≪E0(1 	 αM). For widely spaced resonances, this allows the
approximate evaluation of the moderator scattering source term with the
asymptotic
form
of
the
neutron
flux
in
the
absence
of
resonances,
ϕasy∼1=ξ ΣM
s E. We choose the normalization ϕasy = 1/E above the resonance
energy to obtain
Σres
t (E) + ΣM
s

ϕ(E) = ΣM
s
E + ∫
E=αres
E
dE´
E´
Σres
s (E´)ϕ(E´)
1 	 αres
(4.64)

### Narrow Resonance Approximation

If the practical width of the resonance is also small compared to the scattering-in
interval of the resonance absorber, Γp ≪E0(1 	 αres), then the second scattering
source term can be approximated in the same fashion to obtain
ϕNR(E) =
ΣM
s + Σres
p
[Σres
t (E) + ΣM
s ]E
(4.65)

<!-- page 124 (PDF 148) -->
which can be used in Eq. (4.59) to evaluate the resonance integral:
Iγ
NR = ∫
dE
E σγ(E)
ΣM
s + Σres
p
Σres
t (E) + ΣM
s
= Γγ
2E0
(σres
p + σM
s )∫
ψ(ξ; x)dx
ψ(ξ; x) + θχ(ξ; x) + β
(4.66)
where
β =
σM
s + σres
p
σ0
;
θ =
Γn
Γ
σres
p
σ0

1=2
(4.67)
σM
s is the moderator scattering cross section per absorber nucleus and σres
p
= 4πR2
is the potential scattering cross section of the resonance absorber. If interference
between resonance and potential scattering is neglected, the resonance integral
can be written
Iγ
NR = Γγ
E0
(σres
p + σM
s )J(ξ; β)
(4.68)
where the function
J(ξ; β) ≡ ∫
ψ(ξ; x)dx
ψ(ξ; x) + β
(4.69)
is tabulated in Table 4.3. A generalization of the J-function that includes the
interference scattering term has been devised, but the form given above is more
commonly used.

### Wide Resonance Approximation

If the practical width of the resonance is large compared to the scattering-in
interval of the resonance absorber, Γp ≫E0(1 	 αres), the second scattering source
term in Eq. (4.64) can be approximated by assuming that Σres
s (E´)ϕ(E´)=E´ ≈
Σres
s (E)ϕ(E)=E; which leads to
ϕWR(E) =
ΣM
s
[Σres
t (E) 	 Σres
s (E) + ΣM
s ]E
(4.70)
Using this result to evaluate the resonance integral defined by Eq. (4.59) yields
IWR = ∫
dE
E σγ(E)
ΣM
s
Σres
s (E) 	 Σres
s (E) + ΣM
s
= Γ
E0
σM
s J(ξ; β´)
(4.71)

<!-- page 125 (PDF 149) -->
J (ξ, β)
j
ξ = 0.1
ξ = 0.2
ξ = 0.3
ξ = 0.4
ξ = 0.5
ξ = 0.6
ξ = 0.7
ξ = 0.8
ξ = 0.9
ξ = 1.0
4.979(2) 4.970(2) 4.969(2) 4.968(2) 4.968(2) 4.968(2) 4.967(2) 4.967(2) 4.967(2) 4.967(2)
3.532
3.517
3.514
3.513
3.513
3.513
3.513
3.513
3.513
3.513
2.514
2.491
2.487
2.485
2.485
2.484
2.484
2.484
2.484
2.484
1.801
1.767
1.761
1.759
1.758
1.757
1.757
1.757
1.757
1.757
1.307
1.257
1.248
1.245
1.244
1.243
1.243
1.243
1.242
1.242
9.667(1) 8.993(1) 8.872(1) 8.831(1) 8.812(1) 8.802(1) 8.796(1) 8.792(1) 8.790(1) 8.788(1)
7.355
6.501
6.335
6.278
6.252
6.238
6.230
6.225
6.221
6.218
5.773
4.777
4.562
4.485
4.450
4.430
4.419
4.412
4.407
4.403
4.647
3.589
3.328
3.230
3.183
3.158
3.143
3.133
3.126
3.121
3.781
2.759
2.471
2.354
2.297
2.265
2.245
2.232
2.223
2.217
10 3.045
2.153
1.867
1.741
1.675
1.638
1.614
1.598
1.587
1.579
11 2.367
1.676
1.423
1.301
1.235
1.194
1.168
1.151
1.138
1.129
12 1.730
1.268
1.074
9.718(0) 9.119(0) 8.739(0) 8.484(0) 8.304(0) 8.174(0) 8.077(0)
13 1.164
9.081(0) 7.815(0) 7.087
6.629
6.322
6.107
5.950
5.833
5.744
14 7.172(0) 6.014
5.342
4.914
4.624
4.419
4.268
4.154
4.066
3.997
15 4.088
3.658
3.371
3.169
3.022
2.911
2.826
2.759
2.706
2.663
16 2.204
2.067
1.966
1.889
1.829
1.781
1.743
1.712
1.687
1.666
17 1.148
1.109
1.078
1.053
1.033
1.016
1.002
9.904
(	1)
9.805
(	1)
9.722
(	1)
18 5.862
(	1)
5.757
(	1)
5.671
(	1)
5.599
(	1)
5.539
(	1)
5.488
(	1)
5.445
(	1)
5.408
5.376
5.348
19 2.963
2.936
2.913
2.894
2.877
2.863
2.851
2.840
2.831
2.823
20 1.490
1.483
1.477
1.472
1.468
1.464
1.461
1.458
1.455
1.453
21 7.468
(	2)
7.452
(	2)
7.437
(	2)
7.424
(	2)
7.413
(	2)
7.403
(	2)
7.395
(	2)
7.388
(	2)
7.381
(	2)
7.375
(	2)
22 3.739
3.735
3.732
3.728
3.726
3.723
3.721
3.719
3.718
3.716
23 1.871
1.870
1.869
1.868
1.868
1.867
1.867
1.866
1.866
1.865
24 9.358
(	3)
9.356
(	3)
9.355
(	3)
9.352
(	3)
9.350
(	3)
9.349
(	3)
9.348
(	3)
9.346
(	3)
9.345
(	3)
9.344
(	3)
25 4.680
4.680
4.679
4.679
4.678
4.678
4.678
4.677
4.677
4.677
26 2.340
2.340
2.340
2.340
2.340
2.340
2.340
2.340
2.340
2.340
27 1.170
1.170
1.170
1.170
1.170
1.170
1.170
1.170
1.170
1.170
28 5.851
(	4)
5.851
(	4)
5.851
(	4)
5.851
(	4)
5.851
(	4)
5.851
(	4)
5.851
(	4)
5.851
(	4)
5.851
(	4)
5.851
(	4)
29 2.925
2.926
2.926
2.926
2.926
2.926
2.926
2.926
2.926
2.926
30 1.463
1.463
1.463
1.463
1.463
1.463
1.463
1.463
1.463
1.463
31 7.314
(	5)
7.314
(	5)
7.315
(	5)
7.315
(	5)
7.315
(	5)
7.315
(	5)
7.314
(	5)
7.314
(	5)
7.314
(	5)
7.314
(	5)
Source: Data from Ref. [11]; used with permission of Wiley.
∗Numbers in parentheses are powers of 10, which multiply the entry next to which they stand and all unmarked
entries below it.

<!-- page 126 (PDF 150) -->
where
β´ = σM
s
σ0
Γ
Γγ
(4.72)

### Resonance Absorption Calculations

Data for several of the low-energy resonances in 238U are given in Table 4.4. Also
shown is a comparison of the absorption probabilities calculated with the narrow
and wide resonance approximations with an “exact” solution obtained numerically
, for a representative fuel-to-moderator ratio for a thermal reactor. The WR
approximation is more suitable for the lowest-energy resonances, but the narrow
resonance approximation generally is preferable for all but the lowest-energy
resonances.

### Example 4.2 Group Capture Cross Section for 6.67-eV 238U Resonance

The contribution of the 6.67-eV 238U resonance to the capture cross section of an
energy group extending from 1 to 10eV is calculated in the narrow resonance
approximation from σg
γ = Iγ
NR=ln(10=1); where Iγ
NR = (Γγ=E0)(σres
p + σM
s )J(ξ; β).
For uranium, σres
p = 8:3 barns. For a moderator cross section per fuel atom of σM
s =
ΣM
s =NF = 60
barns
and
a
temperature
T = 330°C,
ξ = (Γ/2)/(E0kT/A)1/2=
(0.0275 eV/2)/[(6.67 eV × 603 K × 0.86 × 10	4 eV/K)/238]1/2 = 0.361
and
β =
(σres
p + σM
s )/σ0 = (60 + 8.3)/2.15 × 105 = 31.8 × 10	5 = 2j × 105, or j = 4.98. Interpolating
on j and ξ in Table 4.3 yields J ≈ 88. With these values, Iγ
NR ≈ 23 and
σg
γ ≈ 10 barns.

### Temperature Dependence of Resonance Absorption

Examination of the function J(ξ, β) of Eq. (4.69) reveals that for any value of β,
the value of J increases or remains constant as ξ decreases. Since ξ ∼1/T1/2, the
resonance absorption must increase or remain unchanged when the temperature
increases. The physical reason for this is that as the temperature increases,
Table 4.4 Low-Energy 238U Resonances
(1 −αresE0)
1 −p
E0 (eV)
Γn (eV)
Γγ (eV)
σ0 (barns)
Γp (eV)
(eV)
NR
WR
Exact
6.67
0.001 52
0.026
2.15 × 105
1.26
0.110
0.2376
0.1998
0.1963
20.90
0.0087
0.025
3.19 × 104
1.95
0.348
0.074 55
0.070 59
0.067 55
36.80
0.032
0.025
3.98 × 104
3.65
0.612
0.047 39
0.061 10
0.058 20
116.85
0.030
0.022
1.30 × 104
1.32
0.966
0.009 04
0.009 50
0.009 17
208.46
0.053
0.022
8.86 × 103
2.63
1.73
0.004 44
0.007 69
0.005 02
Source: Data from Ref. [11]; used with permission of Wiley.

<!-- page 127 (PDF 151) -->
the cross section (averaged over nuclear motion) decreases in peak value and
broadens in energy in such a manner as to preserve the area under the crosssection
curve, as indicated in Fig. 4.5, but the decreasing value of the cross
section results in a decreasing depression in the neutron flux in the resonance
region. This increase in absorption cross section with increasing fuel temperature

introduces
an
important
negative-feedback
Doppler
temperature
coefficient of reactivity, which is important for reactor safety, as discussed
in Chapter 5.

## 4.4 Multigroup Diffusion Theory

### Multigroup Diffusion Equations

We consider cohorts of neutrons of different energies diffusing within a nuclear
reactor. The basic diffusion equation for each cohort, or group, of neutrons is the
same as derived in Chapter 3, but with absorption generalized to all processes that
remove the neutron from the cohort or group (i.e., absorption plus scattering to
another group) and with the source of neutrons for each group specialized to
include the in-scatter of neutrons from other groups, which are also diffusing
within the reactor:
	∇? Dg(r)∇ϕg(r) + Σg
r(r)ϕg(r)
=
X
G
g´ ≠g
Σg´!g
s
(r)ϕg´(r) + 1
k χgX
G
g´=1
vΣg´
f (r)ϕg´(r);
g = 1; . . . ; G
(4.73)
The definition of group constants given by Eqs. (4.39) is applicable. For the group
diffusion coefficient there are two plausible definitions:
Dg(r) = ∫
Eg	1
Eg
dE D(r; E)ϕ(r; E)=ϕg(r)
= 1
3 ∫
Eg	1
Eg
dE ϕ(r; E)
Σtr(r; E) =ϕg(r)
(4.74)
or
Dg(r) =
3Σg
tr(r) =
3∫
Eg	1
g
d EΣtr(r; E)ϕ(r; E)ϕg(r)
(4.75)
We return to this issue in Chapter 10, where the multigroup diffusion equations
are formally derived from energy-dependent transport theory.

<!-- page 128 (PDF 152) -->
Equations (4.73) constitute a set of homogeneous equations, the solutions of
which are nontrivial only for certain discrete values of the effective multiplication
constant, k. It has been shown (Refs. [2 and 4]) that the mathematical properties of
the multigroup diffusion equations are such that the largest such discrete
eigenvalue is real and positive. The corresponding eigenfunction is unique
and nonnegative everywhere within the reactor. In other words, mathematically,
these equations have a physically correct solution corresponding to the largest
value of the eigenvalue.

### Two-Group Theory

The simplest example of multigroup diffusion theory is two-group theory in
which the fast group contains all neutrons with E ≳1 eV and the thermal group
contains the neutrons that have slowed down into the thermal interval E ≲1 eV.
This model is described by
	∇? D1∇ϕ1 + (Σ1
a + Σ1!2
s
)ϕ1 = 1
k (vΣ1
f ϕ1 + vΣ2
f ϕ2)
	∇? D2∇ϕ2 + Σ2
aϕ2 = Σ1!2
s
ϕ1
(4.76)
and the boundary conditions of the neutron fluxes in both groups vanishing on
the boundary of the reactor.

### Two-Group Bare Reactor

For a uniform reactor, the vanishing of the neutron flux on the boundary requires
that the neutron flux in both groups satisfies
∇2ψ(r) + B2
gψ(r) = 0
(4.77)
where Bg is the geometric buckling of Table 3.3. Using this form for the group
fluxes in Eqs. (4.76) leads to a pair of homogeneous algebraic equations that can
be solved for the effective multiplication constant
k =
vΣ1
f
Σ1
a + Σ1!2
s
+ D1B2
g
+
Σ1!2
s
Σ1
a + Σ1!2
s
+ D1B2
g
?
vΣ2
f
Σ2
a + D2B2
g
(4.78)
and the flux ratio
ϕ1 =
Σ2
a + D2B2
g
Σ1!2
s
ϕ2
(4.79)

<!-- page 129 (PDF 153) -->
Extending the definition of the diffusion length for the fast group to include
removal by scattering to the thermal group
L2
1 =
D1
Σ1
a + Σ1!2
s
= D1
Σ1
r
(4.80)
Equation (4.78) for the effective multiplication constant can be rearranged into a
form from which the definition of terms in the six-factor formula are apparent:
k =
vΣ2
f
Σ2
a
!
1 +
vΣ1
f ϕ1
vΣ2
f ϕ2
!
Σ1!2
s
Σ1
a + Σ1!2
s

1 + L2
1B2
g
!
1 + L2
2B2
g
!
= (ηf )(ε)(p) P1
NL
P2
NL
(4.81)
where the fast P1
NL
and thermal P2
NL
nonleakage probabilities are identified
separately.

### One-and-One-Half-Group Theory

Because the thermal group absorption cross section is generally much larger than
the fast-group cross section, D2 ≪D1. This suggests approximating the twogroup
equations by neglecting D2 and using the resulting solution of the thermal
group equation ϕ2 = (Σ1!2
s
=Σ2
a)ϕ1 in the fast-group equation to obtain
	∇? D1∇ϕ1 + Σ1
rϕ1 = 1
k
vΣ1
f + vΣ2
f
Σ1!2
s
Σ2
a

ϕ1
(4.82)
which has the form of a one-group diffusion equation for the fast neutrons. This
method may be extended to account for the diffusion of thermal neutrons by
using an effective value of the fast diffusion coefficient,
D1
eff = D1 + Σ1
a + Σ1!2
s
Σ2
a
D2
(4.83)
which has the effect of replacing the fast diffusion length L1 by the migration
length; that is,
L2
1 ! M2 =
D1
Σ1
a + Σ1!2
s
+ D2
Σ2
a
(4.84)
The solutions discussed in Chapter 3 for the one-speed neutron diffusion
equation can be applied immediately to 1 1
2-group theory merely by replacing
vΣf ! vΣ1
f + vΣ2
f (Σ1!2
s
=Σ2
a) and D ! D1
eff:

<!-- page 130 (PDF 154) -->
### Two-Group Theory of Two-Region Reactors

Consider a rectangular parallelepiped core consisting of a uniform central region
(material 1) bounded on both ends by regions of the same composition (material 2),
as depicted in Fig. 4.6. The two-group equations in each material (subscript k) are
	D1
k∇2ϕ1k(x; y; z) + Σ1
rkϕ1k(x; y; z)
= 1
k vΣ1
f kϕ1k(x; y; z) + vΣ2
f ϕ2k(x; y; z)
h
i
	D2
k∇2ϕ2k(x; y; z) + Σ2
akϕ2k(x; y; z) = Σ1!2
sk
ϕ1(x; y; z)
(4.85)
where group 2 is assumed to be below the fission spectrum. We seek a solution by
separation of variables, and recalling the results of Chapter 3 look for a solution of
the form
ϕgk(x; y; z) = Xgk(x)cos πy
2Y 1
cos πz
2Z1
(4.86)
The y- and z-components of the gradient operators acting on the trial solutions of
Eq. (4.86) give rise to a transverse buckling term,
B2
yz =
π
2Y 1

+
π
2Z1

(4.87)
These trial solutions are substituted into Eqs. (4.85) to obtain equations for the Xgk:
	D1
k
d2
dx2 X1k(x) + (Σ1
rk + D1
kB2
yz)X1k(x) = 1
k vΣ1
f kX1k(x) + vΣ2
f kX2k(x)
h
i
	D2
k
d2X2k(x)
dx2
+ (Σ2
ak + D2
kB2
yz)X2k(x) = Σ1!2
sk
X1k(x)
(4.88)
Material (2)
Material (1)
Material (2)
2Z1
2Y1
X2
X1
X1
X2
Y
Z
X
Fig. 4.6 Three-region reactor model. (With permission from Ref. [1]. Copyright1975, MIT
Press.)

<!-- page 131 (PDF 155) -->
These equations must satisfy symmetry boundary conditions at x = 0, continuity
of flux and current interface conditions at x = x1, and zero flux at x = x1 + x2:
dXg1(0)
dx
= 0;
Xg2(x1 + x2) = 0
Xg1(x1) = Xg2(x1);
	 Dg
dXg1(x1)
dx
= 	Dg
dXg2(x1)
dx
(4.89)
The procedure for solving Eqs. (4.88) is to look for solutions of a particular form
with arbitrary constants and then to establish conditions on the arbitrary
constants by requiring the form to satisfy Eqs. (4.88). In particular, we look
for solutions that satisfy
d2Xgk(x)
dx2
+ B2
kXgk(x) = 0
(4.90)
in each region k. Note that we require that Eq. (4.90) be satisfied with the same
value of B2
k by both the fast (X1k) and thermal (X2k) fluxes in each region k.
Substituting the solution of the form that satisfies Eqs. (4.90) into Eqs. (4.88) leads
to a set of equations for each region k:
D1
kB2
k + D1
kB2
yz + Σ1
rk 	 1
k vΣ1
f k

X1k(x) 	 1
k (vΣ2
f k)X2k(x) = 0
(	Σ1!2
sk
)X1k(x) + (D2
kB2
k + D2
kB2
yz + Σ2
ak)X2k(x) = 0
(4.91)
which must be satisfied if the solution of Eqs. (4.88) within each material is to have
the form that satisfies Eqs. (4.90). These are homogeneous equations, which have
a nontrivial solution only if the determinant of the coefficient matrix vanishes,
which defines two values B2
k = μ2
k and B2
k = 	v2
k for which Eqs. (4.88) have
solutions of the form that satisfies Eqs. (4.90):
μ2
k = 	B2
yz 	 1
Σ2
ak
D2
k
+
Σ1
rk 	 k	1vΣ1
f k
D1
k
!
+
Σ2
ak
2D2
k
Σ1
rk + k	1vΣ1
f k
2D1
k
!2
+
k	1vΣ2
f kΣ1!2
sk
D1
kD2
k
"
#1=2
v2
k = B2
yz + 1
Σ2
ak
D2
k
+
Σ1
rk 	 k	1vΣ1
f k
D1
k
!
+
Σ2
ak
2D2
k
Σ1
rk 	 k	1vΣ1
f k
D1
k
!2
+
k	1vΣ2
f kΣ1!2
sk
D1
kD2
k
"
#1=2
(4.92)

<!-- page 132 (PDF 156) -->
The quantity 	v2
k is always negative, but μ2
k can be positive or negative, depending
on the value of the two-group constants. Thus, there are solutions of Eqs. (4.88)
that satisfy Eqs. (4.90), which are of the form
X2k(x) = A1
2k sin μkx + A2
2k cos μkx + A3
2k sinh vkx + A4
2k cosh vkx
X1k(x) = skA1
2k sin μkx + skA2
2k cos μkx + tkA3
2k sinh vkx + tkA4
2k cosh vkx
(4.93)
where the second of Eqs. (4.91) has been used to determine the ratio of fast-tothermal
group components:
sk =
D2
k(μ2
k + B2
yz) + Σ2
ak
Σ1!2
sk
tk =
D2
k(	v2
k + B2
yz) + Σ2
ak
Σ1!2
sk
(4.94)
The symmetry conditions x = 0 require that A1
21 = A3
21 = 0, and the zero flux
conditions at x = x1 + x2 require that the solution in region 2 be of the form
X22(x) = C1
22 sin μ2(x1 + x2 	 x) + C2
22 sinh v2(x1 + x2 	 x)
X12(x) = s2C1
22 sin μ2(x1 + x2 	 x) + t2C2
22 sinh v2(x1 + x2 	 x)
(4.95)
Requiring the solution in region 1 given by Eqs. (4.93) and the solution in region 2
given by Eqs. (4.95) to satisfy the continuity of flux and current interface
conditions results in a set of four homogeneous equations for the constants
A2
21; A4
21; C1
22; and C2
22. The requirement for a nontrivial solution, the vanishing of
the determinant of the coefficients, then, is the criticality condition
det
s1 cos μ1x1
t1 cosh v1x1
	s2 sin μ2x2
	t2 sinh v2x2
s1D1
1μ1 sin μ1x1
	t1D1
1v1 sinh v1x1
	s1D1
2μ2 cos μ2x2
	t2D1
2 cosh v2x2
cos μ1x1
cosh v1x1
	sin μ2x2
	sin v2x2
D2
1μ1 sin μ1x1
	D2
1v1 sinh v1x1
	D2
2μ2 cos μ2x2
	D2
2v2 cosh v2x2
= 0
(4.96)
which may be solved for the effective multiplication constant, k. The four
equations can be solved for three of the constants in terms of the one remaining
constant, which must be determined from the total reactor power level.
Thisprocedure could be extended to multiregion reactors, but it becomes extremely
cumbersome, and direct numerical solution of Eqs. (4.85) becomes preferable.

<!-- page 133 (PDF 157) -->
### Two-Group Theory of Reflected Reactors

The results above can be specialized to the situation of a reflected reactor by
setting Σf = 0 in region 2, in which case Eq. (4.92) reduces to
μ2
2 = 	B2
yz 	 Σ1
r2
D1
;
	 v2
2 = 	B2
yz 	 Σ1
a2
D2
(4.97)
A solution of the type just described can be carried out in spherical and
cylindrical geometry (reflected axially or radially, but not both), as well as in the
block geometry. The results are summarized in Table 4.5, where Z(R = R, {R, z} or
[x, y, z}) and W are spatial flux shapes in the core and U and V are spatial flux
shapes in the reflector.
The thermal flux in the core of a spherical reflected reactor is given by
ϕ2
c(r) = ϕ0c
r (sin μcr + a sinh vcr)
(4.98)
and the thermal flux in the spherical shell reflector is given by
ϕ2
R(r) = ϕ0R
r
sinh μR(R´ 	 r) + b sinh vR(R´ 	 r)

(4.99)
The corresponding fast fluxes are related to the thermal fluxes by the factors sk
and tk given by Eqs. (4.94). These fluxes are plotted for a representative set of twogroup
constants in Fig. 4.7. The much larger ratio Σ1!2
s
=Σ2
a in the reflector than in
the core causes a peaking of the thermal flux in the reflector at the core–reflector
interface. Physically, fast neutrons are diffusing out of the core and being slowed
down into the thermal group in the reflector, where the thermal absorption is
greatly reduced relative to the core. This same type of peaking of the thermal flux
would occur in a water gap next to a fuel assembly within the core.
O
O
R
r sin Br
Core
Reflector
ϕ(r)
ϕ(r)
ϕth
ϕfast
R
r
r
~R’
~R’
~
r sin k(R’-r)
Fig. 4.7 Fast and thermal fluxes in a reflected spherical reactor with properties (core:
D1 = D2 = 1 cm, Σ1!2
s
= 0.009 cm	1, Σ1
a = 0.001, Σ2
a = 0.05 cm	1, vΣ2
f = 0.057; reflector: D1 = D2
= 1 cm, Σ1!2
s
= 0.009 cm	1, Σ1
a = 0.001, Σ2
a = 0.0049 cm	1, vΣ2
f = 0.0. (With permission from
Ref. [12]. Copyright 1960, McGraw-Hill.)

<!-- page 134 (PDF 158) -->
Geometry
Spherical
Rʹ
R
Z(R)
= sin μR
R
Z´(R)
= μ cos μR
R
	 sin μR
R2
W(R) = sinh λR
R
W ´(R) = λ cosh λR
R
	 sinh λR
R2
U(R)
= sinh κ3(R~´ 	 R)
R
U´(R) = 	 κ3 cosh κ3(R~´ 	 R)
R
	 sinh κ3(R~´ 	 R)
R2
V(R)
= sinh κ4(R~´ 	 R)
R2
V ´(R) = 	 κ4 cosh κ4(R~´ 	 R)
R
	 sinh κ4(R~´ 	 R)
R2
Cylinder:
Side
Reflectors
Cylinder: End
Reflectors
Z
R
ρ
Rʹ
O
h
h
Z
R
ρ
Rʹ
O
h
h
Z(R)
= J0(l1 R)cos l2z
Z´(R)
= 	l1J1(l1 R)cos l2z
W(R) = I0(l3 R)cos l2z
W ´(R) = l3I1(l3 R)cos l2z
l2
≡ μ2 	 l2
2 l2 ≡ π
2h~
l2
3 ≡ λ2 + l2
U(R)
= [I0(I4 R)K 0(l4 R~´) 	 I0(l4R~´)K 0(l4R)]cos l2z
U´(R) = l4[I1(l4 R)K0(l4 R~´) + I0(l4R~´)K 1(l4R)]cos l2z
V(R)
= [I0(l5 R)K 0(l5 R~´) 	 I0(l5 ~R
´)K0(l5 R)]cos l2z
V ´(R) = l5[I1(l5 R)K0(l5 R´~) + I0(l5R~´)K 1(l5 R)]cos l2z
l2
≡ κ2
3 + l2
l2
5 ≡ κ4
2 + l2
Z(R)
= J0(m1 ρ)cosm2h
Z´(R)
= 	m2J0(m1ρ) sinm2h
W(R) = J0(m1 ρ) coshm3h
W ´(R) = m3J0(m1 ρ) sinhm3h
m1
≡ 2:405
R~´
m2
2 ≡ μ2 	 m2
m2
3 ≡ λ2 + m2
U(R)
= J0(m1 ρ)sinh m4(d~	h)
U´(R) = 	m4J0(m1 ρ)cosh m4(d~	h)
m2
4 ≡ κ2
3 + m2
V(R)
= J0(m1 ρ)sinh m5(d~	h)
V ´(R) = 	m5J0(m1ρ)cosh m5(d~	h)
m2
5 ≡ κ2
4 + m2
Block
2c
O
x
y
z
2a 2d
2b
Z(R)
= cos n1a cos n2y cos n3z
Z´(R)
= 	n1 sin n1a cos n2y cos n3z
n2
≡ μ2 	 n2
2 	 n2
W(R) = cosh n4a cos n2y cos n3z
W ´(R) = n4 sinh n4a cos n2y cos n3z
n2
≡ λ2 + n2
2 + n2
n3 ≡ π
2c~
n2 ≡ π
2b~
U(R)
= sinh n5(d~	a)cos n2 cos n3z
U´(R) = 	n5 cosh n5(d~	a)cos n2y cos n3z
V(R)
= sinh n6(d~	a)cos n2y cos n3z
V ´(R) = 	n6 cosh n6(d~	a)cos n2y cos n3z
n2
≡ κ2
3 + n2
2 + n2
n2
6 ≡ κ2
4 + n2
2 + n2
Source: Adapted from Ref. [12]; used with permission of McGraw-Hill.
Prime on Z´, W´, U´, and V´ indicates spatial derivative.
Tilde on symbol indicates extrapolated boundary.

<!-- page 135 (PDF 159) -->
### Numerical Solutions for Multigroup Diffusion Theory

The numerical solution procedures discussed for the one-speed diffusion equation
in Section 3.10 are readily extended to the solution of the multigroup
diffusion equations. The G multigroup equations for the case of G 	 1 fast groups
and a thermal group G are
	∇? D1∇ϕ1 + Σ1
rϕ1 = 1
k χ1Sf
	∇? D2∇ϕ2 + Σ2
rϕ2 = 1
k χ2Sf + Σ1!2
s
ϕ1
	∇? D3∇ϕ3 + Σ3
rϕ3 = 1
k χ3Sf + Σ1!3
s
ϕ1 + Σ2!3
s
ϕ2
	∇? DG∇ϕG + ΣG
a ϕG = Σ1!G
s
ϕ1 + Σ2!G
s
ϕ2 + ∙∙∙+ ΣG	1!G
s
ϕG	1
(4.100)
where the fission source is
Sf (r) =
X
G
g=1
vΣg
f (r)ϕg(r)
(4.101)
The solution procedure is initiated by guessing a fission source distribution, S(0)
f ,
and an effective multiplication constant, k(0), and solving the group 1 equation for
the first iterate flux, ϕ(1)
1 :
	∇? D1∇ϕ(1)
1 + Σ1
rϕ(1)
1 = 1
k(0) χ1S(0)
f
(4.102)
Equation (4.102) is solved iteratively (e.g., by the successive relaxation method
described in Section 3.10). Next, the group 2 equation is solved for the first iterate
flux, ϕ(1)
	∇? D2∇ϕ(1)
2 + Σ2
rϕ(1)
2 = 1
k(0) χ2S(0)
f
+ Σ1!2
s
ϕ(1)
(4.103)
using the just calculated ϕ(1)
1 and an iteration procedure of the type described in
Section 3.10. This procedure is continued successively to all the lower groups,
using the just calculated values of the fluxes for higher energy groups to calculate
the scattering-in source, to determine the first iterate of all G group fluxes
[ϕ(1)
1 ; ϕ(1)
2 ; . . . ; ϕ(1)
G ], which are then used to compute a first iterate fission source:
S(1)
f (r) =
X
G
g=1
vΣg
f (e)ϕ(1)
g (r)
(4.104)

<!-- page 136 (PDF 160) -->
and a first iterate effective multiplication constant:
k(1) =
k(0)
∫dr S(1)
f (r)
∫drS(0)
f (r)
(4.105)
The iterations are continued until the effective multiplication constant converges,
as described in Section 3.10.
If a multigroup structure is chosen in which there is more than one group in the
thermal energy interval E < 1 eV, there is upscattering among the thermal groups
and the successive-group solution procedure must be modified by solving
simultaneously for the fluxes in the thermal groups or by an iterative solution
for the thermal group fluxes.

## References

1 A. F. HENRY, Nuclear-Reactor Analysis, MIT Press, Cambridge, MA (1975).
2 E. L. WACHSPRESS, Iterative Solutions of Elliptic Systems and Applications to the
Neutron Diffusion Equations of Reactor Physics, Prentice Hall, Englewood Cliffs,
NJ (1973).
3 R. S. VARGA, Matrix Iterative Analysis, Prentice Hall, Englewood Cliffs, NJ (1962).
4 G. J. HABETLER and M. A. MARTINO, Proc. Symp. Appl. Math. IX, 127 (1961).
5 R. KINSEY, Data Formats and Procedures for the Evaluated Nuclear Data File,
ENDF, BNL-NCS-50496, ENDG-1021, 2nd ed., ENDF/B-V, Brookhaven National
Laboratory, Upton, NY (1970); C. BREWSTER, ENDF/B Cross Sections, BNL-17100
(ENDF-200), 2nd ed., Brookhaven National Laboratory, Upton, NY (1975).
6 R. H. HOWERTON et al., Evaluation Techniques and Documentation of Specific
Evaluations of the LLL Evaluated Nuclear Data Library (ENDL), UCRL-50400,
Vol. 15, Lawrence Livermore Laboratory, Livermore, CA (1970).
7 R. E. MACFARLANE, D. W. MUIR, and R. M. BOICOURT, The NJOY Nuclear Data
Processing System, Vols. I and II, LA-9303-M, Los Alamos National Laboratory,
Los Alamos, NM (1982).
8 B. J. TOPPEL,“The New Multigroup Cross Section Code, MC2-II,” in Proc. Conf.
New Developments of Reactor Mathematics and Applications, CONF-710302,
Idaho Falls, ID (1971); H. HENRYSON et al., MC2-II: A Code to Calculate Fast
Neutron Spectra and Multigroup Cross Sections, ANL-8144, Argonne National
Laboratory, Argonne, IL (1976).
9 C. R. WEISBIN et al., MINX: A Multigroup Interpretation of Nuclear Cross
Sections from ENDF/B, LA-6486-MS-(ENDF-237), Los Alamos National
Laboratory, Los Alamos, NM (1976).
10 I. I. BONDARENKO et al., Group Constants for Nuclear Reactor Calculations,
Consultants Bureau, New York (1964).
11 J. J. DUDERSTADT and L. J. HAMILTON, Nuclear Reactor Analysis, Wiley, New York
(1976).
12 R. V. MEGHREBLIAN and D. K. HOLMES, Reactor Analysis, McGraw-Hill, New York
(1960).
