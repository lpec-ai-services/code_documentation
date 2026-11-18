# DEFINING SCORES DECOMPOSED OVER REAL SPHERICAL HARMONICS
<!-- source PDF pages 236-238 -->

<!-- page 236 -->
Chapter 16
DEFINING SCORES DECOMPOSED OVER
REAL SPHERICAL HARMONICS
For some applications, it may be of interest to compute reaction rates decomposed over real spherical
harmonics. When dealing with real spherical harmonics, there is many different conventions leading to
potential confusion [76]. In order to be consistent with the conventions used in the APOLLO deterministic
code, we chose the spherical harmonics convention named Schmidt semi-normalized in [76] with the z-axis
coordinate considered as cosine θ.
The neutron flux can be expanded over real spherical harmonics basis as :
ψg(Ω) =
Z
∆Eg
dEψ(Ω,E) ≈
ℓmax
∑
ℓ=1 ∑
|m|<ℓ
Aℓ,m(Ω)φg
ℓ,m
(16.1)
where φg
ℓ,m = 1
4π
Z
ΩdΩAℓ,m(Ω)
Z
∆Eg
dEψ(Ω,E)
(16.2)
where A is the real spherical harmonics basis defined as
Aℓ,m(Ω) =
(
¯Pℓ,m(cosθ)cos(mφ) if m ≥0
¯Pℓ,|m|(cosθ)sin(|m|φ) if m < 0
(16.3)
with ¯Pℓ,m(cosθ) = (−1)m
s
(2−δ0m)(ℓ−m)!
(ℓ+m)!Pℓ,m(cosθ)
(16.4)
With δ0m being the Kronecker delta and Pℓ,m the associated Legendre Polynomials derived from the following
relations :
Pℓ,m(x) = (−1)m(1−x2)m/2dmPℓ(x)
dxm
(16.5)

<!-- page 237 -->
where Pℓ(x) is the Legendre Polynomial.
In an exact similar way to the flux in equation 16.2, reaction rate for a reaction r and scattering matrix for
reaction s can decomposed over real spherical harmonics as :
τg
ℓ,m(r) = 1
4π
Z
ΩdΩAℓ,m(Ω)
Z
∆Eg
dEΣr(E)ψ(Ω,E)
(16.6)
τg′→g
ℓ,m (s) = 1
4π
Z
∆E′g
dE′
Z
∆Eg
dE
Z
ΩdΩAℓ,m(Ω)
Z
Ω′ dΩ′Σs(Ω′ ·Ω,E′ →E)ψ(Ω′,E′)
(16.7)
When scores decomposed over real spherical harmonics are required, TRIPOLI-4 computes the quantities defined
in 16.2, 16.6, 16.7 for the angular flux, the scattering matrix and the total, fission, scattering, absorption,
and nu fission cross sections.
These reaction rates decomposed over real spherical harmonics calculations are defined between the keywords
REACTION_RATES_SPHERICAL_HARMONICS and END_REACTION_RATES_SPHERICAL_HARMONICS. The syntax
is as follows:
REACTION_RATES_SPHERICAL_HARMONICS
Description of an extended mesh
ENERGY
GRID <energy_binning_name>
MOMENTS
<number_of_moments>
END_REACTION_RATES_SPHERICAL_HARMONICS
The extended mesh definition is the same as defined in the section 15.8. However, there is few limitations
for the moment: the NORMALIZE, ENTROPY and STORE_IN_FILE options cannot be used in the frame of the
REACTION_RATES_SPHERICAL_HARMONICS block.
The <energy_binning_name> is the name of an energy grid defined in the GRID_LIST command.
The
<number_of_moments> is an integer corresponding to the maximum ℓ-th order. This value must be positive.
Below is an example of requiring these reaction rates :
REACTION_RATES_SPHERICAL_HARMONICS
EXTENDED_MESH
WINDOW
-0.7470 -0.7470 -5
0.7470
0.7470
5
2 2 1
FRAME CARTESIAN
0. 0. 0.
1 0 0
0 1 0
0 0 1

<!-- page 238 -->
ENERGY GRID DEC_2G
MOMENTS 5
END_REACTION_RATES_SPHERICAL_HARMONICS
